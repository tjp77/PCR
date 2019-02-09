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

ampSegLen = 200; # Size of segment to copy. Will need later when put in real data, or generate dna other then test strands. Let user input this?
primerLen = 20; # "Assume that the length of the original forward and backward primers are fixed at p bases (assume p = 20)."
fragmentCount = 0; 
d = 200; e = 50; 
primerDecayOn = True;


def getDNA():
    # Get/Generate DNA to use here. Replace test/placeholder var value. 
    
    dna1 = "AGGCTTAAAGCCTGATGCACACCGATGACTAGGCTCTCATCGAGTAGCGATCGGCCTTAAATATCCGTGATCGATGACGTACGTACTGACTGACTGTACTTAATCGTACTTCGAGCTAGTCGATGCATCGAGTTAGGCCCCTAGTCGATCTGATCGGTACGT";
    
    dna2 = "TCCGAATTTCGGACTACGTGTGGCTACTGATCCGAGAGTAGCTCATCGCTAGCCGGAATTTATAGGCACTAGCTACTGCATGCATGACTGACTGACATGAATTAGCATGAAGCTCGATCAGCTACGTAGCTCAATCCGGGGATCAGCTAGACTAGCCATGCA";
    
    return dna1;


def Step1(): 
    # In the first step, the two strands of the DNA are physically separated.
    
    return 1; # 


# Step 2 function. Primers bind to DNA.

# In the second step, the temperature is lowered and the primers bind to the complementary sequences of DNA.
# The primers are single-stranded sequences themselves, but are much shorter than the length of the target region, 
# complementing only very short sequences at the 3' end of each strand.


def Step2(primerFrw, primerBkw):
    
    # search strands for primer binding locations (regex), if find a matching spot then can attach. 
    
    return 1;


# Step 3 function. Build copy off of primer, based on DNA.

# The two DNA strands then become templates for DNA polymerase to enzymatically assemble a new DNA strand from free nucleotides, the 
# building blocks of DNA.

def Step3():
    
    # If length of area to copy is longer than strand section to be copied, will get a partial strand of shorter length. 
    
    # Generate random fall off rate with: random.randint(-e, e) + d for primer of current strand being copied. 
    # Fall-off rate means that primer falls off after copying that many bases (A, T, G, C). [Confirmed]
    
    # Use list copy thing [:] => [extention start point:extention start point + (max(target segement len, bases before fall off)] 
    # to copy the segment of the dna to be copied into one string. Prime begining/end of the this string of course depending on if fwd or bkw primer.
    # Remember [:] thing going backwards for backwards primer. 
    # Convert to oppsite bases as done in class, to make the primer extention. 
    
    
    # +1 strand made for each copy.
    # Record length of each new strand made so can display average base length of strands in output. 
    
    return 1;

 

def ResultPrint():
    
    # Your output: (What you might see on the gel)
    
    # 1. Statistics of the PCR products:
    
    print ("Fragment Count: ", fragmentCount, "\n");
    #       (b)   !!! Average length (# bases) of DNA fragments. !!! - Track, Add fragments to list. List of fragment strings/lists? || tup? 
    #       (c)   Distribution of the lengths of the DNA fragments (you may use column chart to show your result). 
    
    # 2. Other things you find interesting.
    
    return 0;


# ----- Turn off the primer decay/fall off at first to check if getting the right amount of copied by the end for testing purposes. 
# ----- Adding bool to use to turn of and on. Default set to True.

def main():
    
    dnaContainer; # List to hold either strand pairs or individual strands depending how output needs and how we choose to represent. 
    
    # Get dna input sequence.
    getDNA();

    # Get input of what each primer should be so can choose region to copy. 
    # Validate input that both entered primers are the same length, update common primer length var defined above. 
    
    primerFrw = "AGGCTTAAAGCCTGATGCAC";
    primerBkw = "TCAGCTAGACTAGCCATGCA";
    
    # Get cycle count input From user. Default/base testing = 1;
    cycleCount = 1; 
    
    completeCycles = 0;
    
    # Ask user if want to turn on primer decay. 
    
    # If for any step where, for our purposes, changing the step time length would make a difference, allow time input.
    
    while completeCycles < cycleCount:
        
        Step1();
        Step2(primerFrw, primerBkw); # Maybe easier to combine steps 2^3 ^ just attach primer ^ build in one step from code perspective, one string.
        Step3();
        completeCycles += 1;
        
        # Print out results of each cycle, at least for checking program correctness and debugging purposes if nothing else? 
    
    ResultPrint();
    
    
    # You will get bonus points if it you can add more parameters and some limitations (such as amount of primers, dNTPs, age of 
    # taqs, temperature, mutations, …)
    
    # Adding a chance for mutations which can be turned on and off seems like a good/simple one to do. 
    
    return 0; 




main();

