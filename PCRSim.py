#!/user/bin/python
import random;
import re;
import sys;

from collections import defaultdict


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

d = 200; 
e = 50;


def buildComplimentaryStrand(strand):
    
    lowerStrand = strand.lower();
    tmp1 = lowerStrand.replace("a", "T");
    tmp2 = tmp1.replace("t", "A");
    tmp3 = tmp2.replace("g", "C");
    tmp4 = tmp3.replace("c", "G");
    
    return tmp4;


class DNA: 
    
    strand2 = " ";
    primer1Index = -1;
    prime2rIndex = -1;
    
    def __init__(self, strand1, generateStrand2):
        
        self.strand1 = strand1.strip();
        
        if (generateStrand2 == True):
            self.strand2 = buildComplimentaryStrand(strand1);
        
    def setStrand2(self, strand):
        self.strand2 = strand.strip();


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
    
    
    
def readInDna():
    
    primer1 = " ";
    primer2 = " "; 
    
    try:
        
        file = open("pcrData.txt", "r");
        
        strand1 = file.readline(); 
        strand2 = file.readline(); 
        dna = DNA(strand1.strip(), False); 
        dna.setStrand2(strand2.strip());

        primer1 = file.readline().strip(); 
        primer2 = file.readline().strip(); 
        
    except:
        
        print("Trouble reading input file 'pcrData.txt'. Make sure file exists and is in correct format."); 
        print("Input format may be incorrect. Refer to documentation for correct format.");
        sys.exit(0);
    
    else:
        
        print("\npcrData.txt read successfully.\n");
    
    retVal = [dna, primer1, primer2];
    return retVal;
    

def RunDenaturation(dnaContainer): 

    # In the first step, the two strands of the DNA are physically separated.

    for section in dnaContainer:
        
        if section.strand2 != " ":
            
            dnaContainer.append(DNA(section.strand2[:], False));
            section.strand2 = " ";

    return 0; 
    
    
# Step 2 function. Primers bind to DNA.

def RunAnnealing(dnaContainer, primer1, primer2, bindingSite1, bindingSite2):
    
    # search strands for primer binding locations, if find a matching spot then can attach. 
    for section in dnaContainer:
        
        # Will be -1 if nothing found, as set as default above in the DNA class. 
        section.primer1Index = section.strand1.find(bindingSite1); 
        section.primer2Index = section.strand1.find(bindingSite2);
        
        # 'Attach' primers if the search for binding sites was succesful. 
        if section.primer1Index != -1:
            section.strand2 = primer1; 

        elif section.primer2Index != -1:
            section.strand2 = primer2; 
        
    
    return 0;


# Step 3 function. Build copy off of primer, based on DNA.

# The two DNA strands then become templates for DNA polymerase to enzymatically assemble a new DNA strand from free nucleotides, the 
# building blocks of DNA.

def RunExtension(dnaContainer, ampSegLen, primerLen, lengthDistributions):
    
    count = 0;
    basesConsumed = 0;
    
    # If length of area to copy is longer than strand section to be copied, will get a partial strand of shorter length. 
    # This will determin if a full copy is to be made, and the length of the partial if not. 
    for section in dnaContainer:
        
        #print (section.strand1, "\n");
        
        taqDecay = random.randint(-e, e) + d;
        copyLen = min(taqDecay, ampSegLen); 
        
        # Python str[:] copy tested in console, if endIndex is higher then the str length, will just copy as many as can. 
         
        if section.primer1Index != -1:
            
            # Calculate area being copied. 
            startIndex = section.primer1Index + primerLen;
            endIndex = section.primer1Index + primerLen + copyLen;
            
            # Build new strand on the primer. 
            section.strand2 = section.strand2 + buildComplimentaryStrand(section.strand1[startIndex : endIndex]);
            count += 1;
            basesConsumed += copyLen + primerLen;
            
        elif section.primer2Index != -1:
            
            # Calculate area being copied. 
            startIndex = section.primer2Index - copyLen;
            endIndex = section.primer2Index;
            
            if startIndex < 0:
                startIndex = 0;
            
            # Build new strand on the primer.
            section.strand2 = buildComplimentaryStrand(section.strand1[startIndex : endIndex]) + section.strand2;
            count += 1;
            basesConsumed += copyLen + primerLen;
        
        
        lengthDistributions[len(section.strand2)] += 1;
    
    retVal = [count, basesConsumed]
    return [count, basesConsumed];

 

def PrintResults(dnaContainer, fragmentCount, combinedLen, lengthDistributions): 
    
    ave = combinedLen // fragmentCount;
    
    # 1. Statistics of the PCR products:
    
    print ("\nFragment Count: ", fragmentCount);
    print ("Ave. Strand Length: ", combinedLen / fragmentCount");
    print ("\nLength Distribution: ");
    
    for len in lengthDistributions:
        print(len, "bases:", lengthDistributions[len]);

    return 0;


def getGCContent(primer):
    
    stability = 0;
    
    # 40-60% good. 
    # return overall GC content, if too high, loose primers to stciking.
    # can pass to extentsion function too, if too low, lower by rand range how long sticks and how much copied. 
    
    
    return stability;


def PCR():
    
    # List to hold DNA objects with strand pairs. 
    dnaContainer = []; 
    lengthDistributions = defaultdict(lambda: 0);
    
    fileInput = readInDna();
    
    dnaContainer.append(fileInput[0]);
    fragmentCount = 2;
    
    lengthDistributions[len(fileInput[0].strand1)] += 2;
    
    primer1 = fileInput[1]; 
    primer2 = fileInput[2]; 
    
    bindingSite1 = buildComplimentaryStrand(primer1);  
    bindingSite2 = buildComplimentaryStrand(primer2); 
    
    primerLen = len(primer1); 
    baseDNALen = len(dnaContainer[0].strand1);
    
    combinedLen = baseDNALen * 2;
    
    ampSegLen = int(input("What is the length of the segment you wish to copy?"));
     
    cycleCount = int(input("How many cycles should be ran?\n")); 
    completeCycles = 0;
    
    availablePrimers = cycleCount * 1.2;
    
    while completeCycles < cycleCount and availablePrimers > 0:
        
        RunDenaturation(dnaContainer); 
        RunAnnealing(dnaContainer, primer1, primer2, bindingSite1, bindingSite2); 
        retVal = RunExtension(dnaContainer, ampSegLen, primerLen, lengthDistributions); 
        
        fragmentCount += retVal[0];
        availablePrimers -= retVal[0];
        combinedLen += retVal[1];
        
        completeCycles += 1; # lengthDistributions[len(section.strand1)] += 1;
    
    PrintResults(dnaContainer, fragmentCount, combinedLen, lengthDistributions);


    return 0;


def main():
    
    menuChoice = 0;
    
    print ("1) Generate random DNA strands to file. \n[WARNING: This will overide existing data in pcrData.txt]\n\n2) Run PCR on pcrData.txt contents.\n");
    
    while menuChoice < 1 or menuChoice > 2:
        
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



[] Option turn primers limit on and off. 



------------



[] finish gc clamp func. and then add in some where. 

[] if limit primers, could have some of them bunch up (by even number) and becoem unuseable is too much GC in primers, instead of clamps. 
    > Set a bit more then what needed for max copies for given cycles, then the taq decay, primer fall-off, and sticking together would limit more. 



-----OPTIONAL-----

[] Allow G/C content at ends of primers to affect 'stickiness'. 

[] Add in convert file strands from RNA to DNA so user can add genback stuff.

[] optional-bonus: Add in possibility for mutations or any other potential parameters during the copy process
    "you will get bonus points if it you can add more parameters and some limitations (such as amount of primers, dNTPs, age of taqs, temperature, 
    mutations, …)"
    
    > Maybe number of primers limit? Rand? User set? Eh. 

"""
