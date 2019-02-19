#!/user/bin/python
import random;
import re;
import sys;

from collections import defaultdict

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
    primer2Index = -1;
    
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
    data = dna.strand1 + "\n" + dna.strand2;
    file.write(data);
    
    print("\nDNA Generated. Data saved to file 'pcrData.txt', in format required for PCR simulation, as follows: ");
    print("Lines 1 & 2: One strand of the DNA each. \n\nTo specify primers, add to that file as follows: \nLine 3: Forward primer. \nLine 4: Backward primer.\n\n[No whitepsace allowed]");
    
    file.close();

    return dna;


def GeneratePrimers():
    
    
    try:
        
        file = open("pcrData.txt", "r");
        strand1 = file.readline(); 
        strand2 = file.readline();
        file.close();
        
        print("This Function will generate primers from the DNA regions around the one you wish to copy, based on the DNA strands found in pcrData.txt.");
        start = int(input("What is the start base position of the segment you wish to copy (not including primers)?"));
        segLen = int(input("What is the length of the segment you wish to copy?"));
        primerLen = int(input("What length do you want the primers to be?"));
        
        primer1 = strand2[start - primerLen : start]; 
        primer2 = strand1[start + segLen : start + segLen + primerLen]; 
        
        file = open("pcrData.txt", "a");
        output = "\n" + primer1 + "\n" + primer2; 
        file.write(output);
        file.close();
        
    except:
        
        print("Trouble reading input file 'pcrData.txt'. Make sure file exists and is in correct format, with the DNA strands you wish to work with."); 
        print("Input format may be incorrect. Refer to documentation for correct format.");
        sys.exit(0);
    
    else:
        
        print("\nPrimer data generated and saved to pcrData.txt successfully.\n");
    
    return 0;
    
    
def readInDna():
    
    primer1 = " ";
    primer2 = " "; 
    
    try:
        
        file = open("pcrData.txt", "r");
        
        strand1 = file.readline(); 
        strand2 = file.readline(); 
        dna = DNA(strand1.strip().upper(), False); 
        dna.setStrand2(strand2.strip().upper());
    
        primer1 = file.readline().strip().upper(); 
        primer2 = file.readline().strip().upper(); 
        
    except:
        
        print("Trouble reading input file 'pcrData.txt'. Make sure file exists and is in correct format."); 
        print("Input format may be incorrect. Refer to documentation for correct format.");
        sys.exit(0);
    
    else:
        
        print("\npcrData.txt read successfully.\n");
    
    file.close();
    retVal = [dna, primer1, primer2];
    return retVal;
    
    
    
# Step 1, the two strands of the DNA are physically separated.
def RunDenaturation(dnaContainer): 
    
    for section in dnaContainer:
        
        if section.strand2 != " ":
            
            dnaContainer.append(DNA(section.strand2[:], False));
            section.strand2 = " ";

    return 0; 
    
    
# Step, primers bind to DNA.
def RunAnnealing(dnaContainer, primers, bindingSites, availablePrimers, limitPrimers):
    
    # search strands for primer binding locations, if find a matching spot then can attach. 
    for section in dnaContainer:
        
        # Will be -1 if nothing found, as set as default above in the DNA class. 
        if limitPrimers == False or availablePrimers[0] > 0:
            
            section.primer1Index = section.strand1.find(bindingSites[1]); 
        else:
            section.primer1Index = -1;
            
        if limitPrimers == False or availablePrimers[1] > 0:
            
            section.primer2Index = section.strand1.find(bindingSites[2]);
        else:
            section.primer2Index = -1;
        
        # 'Attach' primers if the search for binding sites was succesful. 
        if section.primer1Index != -1:
            
            section.strand2 = primers[1];
            availablePrimers[0] -= 1; 

        elif section.primer2Index != -1:
            
            section.strand2 = primers[2]; 
            availablePrimers[1] -= 1;
        
    
    return 0;


# Step 3 function. Build copy off of primer, based on DNA.
def RunExtension(dnaContainer, ampSegLen, primerLen, lengthDistributions):
    
    count = 0;
    basesConsumed = 0;
     
    for section in dnaContainer:
        
        # print (section.strand1, "\n"); # Uncomment to display all current strands existing at the start of each cycle. 
        
        # If length of area to copy is longer than strand section to be copied, will get a partial strand of shorter length. 
        # This will determin if a full copy is to be made, and the length of the partial if not.
        taqDecay = random.randint(-e, e) + d; 
        copyLen = min(taqDecay, ampSegLen + primerLen); 
        
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

 
 

def PrintResults(dnaContainer, gcContents, fragmentCount, combinedLen, lengthDistributions): 
    
    # 1. Statistics Output of the PCR products:
    print("\nPCR Complete - Results:")
    print("\nPrimer 1 Clamp GC Content: ", gcContents[1]);
    print("Primer 2 Clamp GC Content: ", gcContents[2]);
    print("\nFragment Count: ", fragmentCount);
    print("Ave. Strand Length: ", combinedLen / fragmentCount);
    print("\nLength Distribution: ");
    
    try:
        del lengthDistributions[1];
        
    except KeyError:
        pass
    
    for len in sorted(lengthDistributions.keys()):
        print("Strands with", len, "bases:", lengthDistributions[len]);
    
    return 0;


def getGCContent(primer):
    
    # https://www.biocompare.com/Bench-Tips/133581-Primers-by-Design-Tips-for-Optimal-DNA-Primer-Design/
    # "The presence of G and C bases at the 3′ end of the primer—the GC clamp—helps promote correct binding at the 3′ end because of 
    # the stronger hydrogen bonding of G and C bases. GC bonds contribute more to the stability—i.e., increased melting temperatures—of 
    # primer and template, binding more than AT bonds. Primers with 40% to 60% GC content ensure stable binding of primer and template. 
    # However, sequences containing more than three repeats of sequences of G or C in sequence should be avoided in the first five bases 
    # (!) from the 3′ end of the primer because of the higher probability of primer-dimer formation."  
    
    # From other site: Clamp Region is first 5 bases of the 3' end of the primer. 
    
    gcContent = ( ( primer.count('G') + primer.count('C') ) / len(primer[0:6]) ) * 100; 
    
    return gcContent;


def setPrimerQuantity(gcContents):
    
    primerCount1 = int(input("How many copies of primer 1 should there be?\n"));
    primerCount2 = int(input("How many copies of primer 2 should there be?\n"));
    impact = 0;
    
    if gcContents[1] > 60:
        
         primerCount1 -= primerCount1 // (gcContents[1] - 60);
        
    if gcContents[2] > 60:
        
        primerCount2 -= primerCount2 // (gcContents[2] - 60);
    
    primerCounts = [primerCount1, primerCount2];
    
    return primerCounts;


def CheckPrimers(dnaSegment, primer1, primer2):
    
    multOccurring = False;
    
    p1s2 = dnaSegment.strand2.find(primer1);
    
    p1s1Base = dnaSegment.strand1.find(primer1);
    p1s1 = dnaSegment.strand1[p1s1Base + 1:].find(primer1);
    
    if p1s2 != -1 or p1s1 != -1:
        
        print("Primer 1, strand 1 binding primer, is not unique within the strands. ");
        multOccurring = True;
    
    p2s1 = dnaSegment.strand1.find(primer2);
    
    p2s2Base = dnaSegment.strand2.find(primer2);
    p2s2 = dnaSegment.strand2[p2s2Base + 1:].find(primer2);
    
    if p2s1 != -1 or p2s2 != -1:
        
        print("Primer 2, strand 2 binding primer, is not unique within the strands. ");
        multOccurring = True;
    
    if multOccurring == True:
        
        print("This will lead to primers binding to incorrect regions, compromising the PCR process. Please create new primers.\n");
        sys.exit(0);
    
    return 0;


def PCR():
    
    # __________ PCR Environment SetUp __________
    
    # List to hold DNA objects with strand pairs. 
    dnaContainer = []; 
    lengthDistributions = defaultdict(lambda: 0);
    
    fileInput = readInDna();
    
    dnaContainer.append(fileInput[0]);
    fragmentCount = 2;
    lengthDistributions[len(fileInput[0].strand1)] += 2;
    
    # Offset item used to keep designaitions of primer "1" and primer "2" for easier tracking/modling. 
    primers = ( 0, fileInput[1], fileInput[2] ); 
    bindingSites = ( 0, buildComplimentaryStrand(primers[1]), buildComplimentaryStrand(primers[2]) ); 
    gcContents = ( 0, getGCContent(primers[1][::-1]), getGCContent(primers[2]) );
    
    CheckPrimers(fileInput[0], primers[1], primers[2]);
    
    primerLen = len(primers[1]); 
    baseDNALen = len(dnaContainer[0].strand1);
    combinedLen = baseDNALen * 2;
    
    ampSegLen = int(input("What is the length of the segment you wish to copy?\n"));
    
    cycleCount = int(input("How many cycles should be ran?\n")); 
    completeCycles = 0;
    
    limitPrimers = False; 
    availablePrimers = [0, 0];
    userInput = " "; 
    
    while userInput not in ["y", "Y", "n", "N"]:
        
        userInput = input("Turn on primer limitations? Primer quantity will be limited to a starting amount you enter, and GC content will have an affect. (y/n)");
    
    if userInput == "y" or userInput == "Y":
        
        limitPrimers = True; 
        availablePrimers = setPrimerQuantity(gcContents);  
    
    
    # __________ Run of PCR Experiment __________
    
    while completeCycles < cycleCount:
        
        RunDenaturation(dnaContainer); 
        RunAnnealing(dnaContainer, primers, bindingSites, availablePrimers, limitPrimers); 
        retVal = RunExtension(dnaContainer, ampSegLen, primerLen, lengthDistributions); 
        
        fragmentCount += retVal[0];
        
        combinedLen += retVal[1];
        
        completeCycles += 1;  
    
    print("\nPCR Complete.\n");
    
    
    # __________ Experiment Completion & Results __________
    
    PrintResults(dnaContainer, gcContents, fragmentCount, combinedLen, lengthDistributions);

    return 0;


def main():
    
    menuChoice = 0;
    
    print("Welcome to the PCR simulator. You can use the options below to generate random DNA strands and primers for a simulattion, or enter your own into the pcrData.txt data file. ");
    
    print("\nThe file format is:\nDNA strand 1, 3' -> 5'\nDNA strand 2, 5' -> 3'\nStrand 1 binding primer, 5' -> 3'\nStrand 2 binding primer, 3' -> 5'");
    
    print("\nMENU:\n\n1) Generate random DNA strands to file. \n[WARNING: This will overide existing data in pcrData.txt]\n\n2) Generate primers based on copy region.[This will save them to the data file as required]\n\n3) Run PCR on pcrData.txt contents.\n");
    
    while menuChoice < 1 or menuChoice > 3:
        
        menuChoice = int(input("What would you like to do?\n"));
    
    if menuChoice == 1:
        
        generateDNA()
    
    elif menuChoice == 2:
        
        GeneratePrimers();
        
    elif menuChoice == 3:
        
        PCR();
        
    else:
        
        print("Menu input error.");
    
    return 0; 
        


main();

