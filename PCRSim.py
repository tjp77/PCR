#!/user/bin/python
import random;
import re;


#---------- Misc. Notes ----------

"""
two DNA primers that are complementary to the 3' (three prime) ends of each of the sense and anti-sense strands of the DNA target
specific primers that are complementary to the DNA target region are selected beforehand, and are often custom-made in a laboratory

"2. Your original DNA template is of n base-pairs (assume n = 2000 for your test case if you generate your template randomly).
3. The size of the DNA segment to be amplified is m (assume m = 200 if the template is generated randomly). "

https://teaching.ncl.ac.uk/bms/wiki/index.php/DNTP

list.append() adds its argument as a single element to the end of a list. The length of the list itself will increase by one.
list.extend() iterates over its argument adding each element to the list, extending the list. The length of the list will increase by however many elements were in the iterable argument.

https://www.khanacademy.org/science/biology/biotech-dna-technology/dna-sequencing-pcr-electrophoresis/a/polymerase-chain-reaction-pcr

------More straight forward step description:------

!) Denaturation (96°C): Heat the reaction strongly to separate, or denature, the DNA strands. This provides single-stranded template for the next step.
2) Annealing (5555 - 6565°C): Cool the reaction so the primers can bind to their complementary sequences on the single-stranded template DNA.
3) Extension (72°C): Raise the reaction temperatures so Taq polymerase extends the primers, synthesizing new strands of DNA.

"There are many copies of the primers and many molecules of Taq polymerase floating around in the reaction, so the number of DNA molecules can roughly double in each round of cycling."

Turn off primer decay,and use the below to test # copies made:
"Optimally, the formula used to calculate the number of DNA copies formed after a given number of cycles is 2n, where n is the number of cycles. Thus, a reaction set for 30 cycles results in 230, or 1073741824, copies of the original double-stranded DNA target region." 

Video with good animation of copying process and copy strand lengths. 
https://www.youtube.com/watch?v=JmveVAYKylk

https://cdn.kastatic.org/ka-perseus-images/41f0e0fd8b49ba824db0eb707015557bb72ae72b.png

"""

#---------------------------------

d = 200; e = 50; 


def buildComplimentaryStrand(strand):
    
    lowerStrand = strand.lower();
    tmp1 = lowerStrand.replace("a", "T");
    tmp2 = tmp1.replace("t", "A");
    tmp3 = tmp2.replace("g", "C");
    tmp4 = tmp3.replace("c", "G");
    
    return tmp4;


class DNA: 
    
    strand2 = " ";
    frwPrimerIndex = -1;
    bkwPrimerIndex = -1;
    
    def __init__(self, strand1, generateStrand2):
        
        self.strand1 = strand1;
        
        if (generateStrand2 == True):
            self.strand2 = buildComplimentaryStrand(strand1);
        
        def setStrand2(self, strand):
            self.strand2 = strand;


def generateDNA(): 
    
    bases = ["A", "T", "G", "C"];
    strand1 = bases[random.randint(0, 3)];
    basesAdded = 0;

    baseDNALen = int(input("Enter the length of the strand to generate:\n"));
    
    while basesAdded < baseDNALen - 1:
        
        strand1 = strand1 + bases[random.randint(0, 3)];
        basesAdded += 1; 
    
    dna = DNA(strand1.upper(), True);
    
    file = open("pcrData.txt", "w");
    data = dna.strand1 + "\n" + dna.strand2
    file.write(data);
    
    print("\nDNA Generated. Data saved to file 'pcrData.txt', in format required for PCR simulation, as follows: ");
    print("Lines 1 & 2: One strand of the DNA each. \n\nTo specify primers, add to that file as follows: \nLine 3: Forward primer. \nLine 4: Backward primer.\n\n[No whitepsace allowed]");

    return dna;
    
    
    
def readInDna(fileName, isDoubleStrand, generateStrand2):  
    
    try:
        
        file = open("pcrData.txt", "r");
        
        strand1 = file.readline();
        strand2 = file.readline();
        dna = DNA(strand1, False);
        dna.setStrand2(strand2);
        
        primerFrw = file.readline();
        primerBkw = file.readline();
        
    except:
        
        print("Trouble reading input file 'pcrData.txt'. Make sure file exists and is in correct format."); 
        print("Input format may be incorrect. File should be:\nLine 1 - strand 1, line 2 - strand 2, line 3 - forward primer, line 4 - backward primer.");
    
    else:
        
        print("pcrData.txt read successfully.");
    
    retVal = [dna, primerFrw, primerBkw];
    return retVal;


def RunDenaturation(dnaContainer): 

    # In the first step, the two strands of the DNA are physically separated.

    for section in dnaContainer:
        
        if section.strand2 != " ":
            
            dnaContainer.append(DNA(section.strand2[:], False));
            section.strand2 = " ";

    return 0; 
    
    
# Step 2 function. Primers bind to DNA.

def RunAnnealing(dnaContainer, primerFrw, primerBkw):
    
    # search strands for primer binding locations, if find a matching spot then can attach. 
    for section in dnaContainer:
        
       # print("-", section.strand2, "\n");
        
        # Will be -1 if nothing found, as set as default above in the DNA class. 
        section.frwPrimerIndex = section.strand1.find(primerFrw);
        section.bkwPrimerIndex = section.strand1.find(primerBkw);

        # 'Attach' primers if the search for binding sites was succesful. 
        if section.frwPrimerIndex != -1:
            section.strand2 = primerFrw;

        elif section.bkwPrimerIndex != -1:
            section.strand2 = primerBkw;
        
    
    return 0;


# Step 3 function. Build copy off of primer, based on DNA.

# The two DNA strands then become templates for DNA polymerase to enzymatically assemble a new DNA strand from free nucleotides, the 
# building blocks of DNA.

def RunExtension(dnaContainer, ampSegLen, usePrimerDecay, primerLen):
    
    count = 0;
    basesConsumed = 0;
    
    # If length of area to copy is longer than strand section to be copied, will get a partial strand of shorter length. 
    # This will determin if a full copy is to be made, and the length of the partial if not. 
    for section in dnaContainer:
        
        print (section.strand1, "\n");
        
        if (usePrimerDecay):

            decay = random.randint(-e, e) + d;
            copyLen = min(decay, ampSegLen); 

        else:
            
            copyLen = ampSegLen;
         
        
        if section.frwPrimerIndex != -1 and section.frwPrimerIndex + primerLen + copyLen <= len(section.strand1):
            
            # Calculate area being copied. 
            startIndex = section.frwPrimerIndex + primerLen;
            endIndex = section.frwPrimerIndex + primerLen + copyLen;
            
            # Build new strand on the primer. 
            section.strand2 = section.strand2 + buildComplimentaryStrand(section.strand1[startIndex : endIndex]);
            count += 1;
            basesConsumed += copyLen + primerLen;
            
        elif section.bkwPrimerIndex != -1 and section.bkwPrimerIndex >= copyLen:
            
            # Calculate area being copied. 
            startIndex = section.bkwPrimerIndex - copyLen;
            endIndex = section.bkwPrimerIndex;
            
            # Build new strand on the primer.
            section.strand2 = buildComplimentaryStrand(section.strand1[startIndex : endIndex]) + section.strand2;
            count += 1;
            basesConsumed += copyLen + primerLen;
            
    #print("---");
    retVal = [count, basesConsumed]
    return [count, basesConsumed];

 

def PrintResults(dnaContainer, fragmentCount, combinedLen, lenDistributionContainer):
    
    ave = combinedLen // fragmentCount;
    
    # 1. Statistics of the PCR products:
    
    print ("Fragment Count: ", fragmentCount, "\n\n");
    print ("Ave. Strand Length: ", fragmentCount, "\n\n");
    
    for len in lenDistributionContainer:
        print("# strands of length ", "key", "value");

    return 0;


def PCR():
    
    # List to hold DNA objects with strand pairs. 
    dnaContainer = [];  
    
    fileInput = readInDna();
    
    dnaContainer.append(fileInput[0]);
    fragmentCount = 2;
    
    primerFrw = fileInput[1]; 
    primerBkw = fileInput[2];
    
    primerLen = len(primerFrw); 
    baseDNALen = len(dnaContainer[0].strand1);
    
    combinedLen = baseDNALen * 2;
    
    ampSegLen = int(input("What is the length of the segment you wish to copy?"));
     
    cycleCount = int(input("How many cycles should be ran?\n")); 
    completeCycles = 0;
    
    usePrimerDecay = False; 
    
    if input("Would you like to turn on primer fall-off? (y/n)") == "y":
        usePrimerDecay = True; 
        print ("primer decay on");
    
    while completeCycles < cycleCount:
        
        RunDenaturation(dnaContainer); 
        RunAnnealing(dnaContainer, primerFrw, primerBkw); 
        retVal = RunExtension(dnaContainer, ampSegLen, usePrimerDecay, primerLen); # print(retVal);
        fragmentCount += retVal[0];
        combinedLen += retVal[1];
        
        completeCycles += 1; 
        # print(fragmentCount);

    
    PrintResults(dnaContainer, fragmentCount, combinedLen);


    return 0;


def main():
    
    menuChoice = 0;
    
    print ("1) Generate random DNA strands to file. \n[WARNING: This will overide existing data in pcrData.txt]\n\n2) Run PCR on pcrData.txt contents.\n");
    
    while menuChoice != 1 and input != 2:
        menuChoice = int(input("What would you like to do?"));
    
    if menuChoice == 1:
        
        generateDNA()
        
    elif menuChoice == 2:
        
        PCR();
        
    else:
        
        print("Menu input error.");

    return 0; 
        

main();



"""
TODO:

[] Menu choice 2 error. 

[] check if primer decay is turning on. 

[] Allow for forward and backwards primers of different lengths? 

[] Finish length distrubtion section.



-----OPTIONAL-----

[] Allow G/C content at ends of primers to affect 'stickiness'.

[] Add in convert file strands from RNA to DNA so user can add genback stuff.

[] optional-bonus: Add in possibility for mutations or any other potential parameters during the copy process
    "you will get bonus points if it you can add more parameters and some limitations (such as amount of primers, dNTPs, age of taqs, temperature, 
    mutations, …)"
    
    > Maybe number of primers limit? Rand? User set? Eh. 

"""
