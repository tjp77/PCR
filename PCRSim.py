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

ampSegLen = 0; # Size of segment to copy. 
primerLen = 20; # "Assume that the length of the original forward and backward primers are fixed at p bases (assume p = 20)."
fragmentCount = 0; 
d = 200; e = 50; 
primerDecayOn = True; 


def buildComplimentaryStrand(strand):
    
    lowerStrand = strand.lower();
    tmp1 = lowerStrand.replace("a", "T");
    tmp2 = tmp1.replace("t", "A");
    tmp3 = tmp2.replace("g", "C");
    tmp4 = tmp3.replace("c", "G");
    
    return tmp4;
    
     
class DNA: 
    
    strand2 = "";
	frwPrimerIndex = -1;
	bkwPrimerIndex = -1;
    
    def __init__(self, strand1, generateStrand2):
        
        self.strand1 = strand1;
        
        if (generateStrand2 == True):
            self.strand2 = buildComplimentaryStrand(strand1);
        
        def setStrand2(self, strand):
            self.strand2 += strand;

            


def generateDNA():  # Finish. Change to actually generate a long enough first strand. Test with this first, or comment out new code till tested. 
    
    strand1 = "AGGCTTAAAGCCTGATGCACACCGATGACTAGGCTCTCATCGAGTAGCGATCGGCCTTAAATATCCGTGATCGATGACGTACGTACTGACTGACTGTACTTAATCGTACTTCGAGCTAGTCGATGCATCGAGTTAGGCCCCTAGTCGATCTGATCGGTACGT";
    
    dna = DNA(strand1, True);

    return dna;
    
    
    
def readInDna(fileName, isDoubleStrand, generateStrand2): # Finish. 
    
    dna = "x";
    
    return dna;


def Step1(dnaContainer): 

    # In the first step, the two strands of the DNA are physically separated.
	
	for section in dnaContainer:
		if section.strand2 is not "":
			dnaContainer.append(section.strand2);
			section.strand2 = "";
			
    
    return 0; 
    
    
# Step 2 function. Primers bind to DNA.

def Step2(dnaContainer, primerFrw, primerBkw):
    

    
    return 0;


# Step 3 function. Build copy off of primer, based on DNA.

# The two DNA strands then become templates for DNA polymerase to enzymatically assemble a new DNA strand from free nucleotides, the 
# building blocks of DNA.

def Step3():
    
    # If length of area to copy is longer than strand section to be copied, will get a partial strand of shorter length. 
	    for section in dnaContainer:
        
        if (primerDecayOn):
            
            # Generate decay/falloff rate for whatever primer will bind to the strand, if one does. 
            decay = random.randint(-e, e) + d;
        
            # If max bases primer can extend to/copy is less then the length
            # of area want copied, will only get partial copy.
            copyLen = min(decay, ampSegLen);
            
        else:
            
            copyLen = mpSegLen;

		
	# Build up part to be copied into the primer 'strand2'.
        
        # !!! Put new strands in new container at first. Not sure if python lets the iterated container be added to, 
        # and don't want them copied till next cycle even if so!
    
    

    return 0;


def computeAveStrandLen(dnaContainer):
    
    # Must count lengths of both strand1 and strand2, if exists, that is: strand2 is not " ", for each object in the dnaContainer.
    ave = 0;
    
    return ave;
    
    
def displayLenDistribution(dnaContainer):
    
    # 
    
    return 0;
 

def ResultPrint(dnaContainer):
    
    # Your output: (What you might see on the gel)
    
    # 1. Statistics of the PCR products:
    
    print ("Fragment Count: ", fragmentCount, "\n\n");
    print (computeAveStrandLen(dnaContainer), "\n\n"); 
    displayLenDistribution(dnaContainer) 
    
    # 2. Other things you find interesting.
    
    return 0;


def main():
    
    dnaContainer = []; # List to hold either strand pairs or individual strands depending how output needs and how we choose to represent. 
    
    # Get dna input sequence.
    dnaContainer.append(generateDNA());

    # Get input of what each primer should be so can choose region to copy. -------- Test with premade ones here first, then add in input options. 
    # Validate input that both entered primers are the same length, update common primer length var defined above. 
    
    primerFrw = "AGGCTTAAAGCCTGATGCAC"; 
    primerBkw = "TCAGCTAGACTAGCCATGCA";
    
    ampSegLen = int(input("What is the length of the segment you wish to copy?"));
    
    # Get cycle count input From user. 
    cycleCount = int(input("How many cycles should be ran?\n")); 
    completeCycles = 0;
    
    # Ask user if want to turn on primer decay. 
    
    while completeCycles < cycleCount:
        
        Step1(dnaContainer); 
        Step2(dnaContainer, primerFrw, primerBkw);
        Step3(dnaContainer);
        completeCycles += 1;
        
        # Print out results of each cycle, at least for checking program correctness and debugging purposes if nothing else? 
    
    ResultPrint(dnaContainer);
    
    # You will get bonus points if it you can add more parameters and some limitations (such as amount of primers, dNTPs, age of 
    # taqs, temperature, mutations, …)
    
    # Adding a chance for mutations which can be turned on and off seems like a good/simple one to do. 
    
    return 0; 


# copy = primerFrw + buildComplimentaryStrand(strand[frwSearch + primerLen : copyLen]);
        

main();

