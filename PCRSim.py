#!/user/bin/python


#---------- Misc. Notes ----------

"""
two DNA primers that are complementary to the 3' (three prime) ends of each of the sense and anti-sense strands of the DNA target

specific primers that are complementary to the DNA target region are selected beforehand, and are often custom-made in a laboratory


"2. Your original DNA template is of n base-pairs (assume n = 2000 for your test case if you generate your template randomly).

3. The size of the DNA segment to be amplified is m (assume m = 200 if the template is generated randomly). "


https://teaching.ncl.ac.uk/bms/wiki/index.php/DNTP


list.append() adds its argument as a single element to the end of a list. The length of the list itself will increase by one.
list.extend() iterates over its argument adding each element to the list, extending the list. The length of the list will increase by however many elements were in the iterable argument.


Can't have single fall off rate, dif primers would have dif rates, primer for each strand being copied, one to copy each of those copies, etc...

backwards primer, use of from back indexing functionality?

(!!!) Each primer extend for 200 base pairs on each end (stated length to copy) area between them is copied segment. 
      So have to have primers end before part want copied, they act as a scafold to build on. 

https://www.khanacademy.org/science/biology/biotech-dna-technology/dna-sequencing-pcr-electrophoresis/a/polymerase-chain-reaction-pcr




------More straight forward step description:------

!) Denaturation (96°C): Heat the reaction strongly to separate, or denature, the DNA strands. This provides single-stranded template for the next step.

2) Annealing (5555 - 6565°C): Cool the reaction so the primers can bind to their complementary sequences on the single-stranded template DNA.

3) Extension (72°C): Raise the reaction temperatures so Taq polymerase extends the primers, synthesizing new strands of DNA.


Each primer have an end point var to track how far extended? 

"There are many copies of the primers and many molecules of Taq polymerase floating around in the reaction, so the number of DNA molecules can roughly double in each round of cycling."


"""

#---------------------------------



# The size of the DNA segment to be amplified. 

ampSegLen = 200; 
primerLen = 20; # "Assume that the length of the original forward and backward primers are fixed at p bases (assume p = 20)."
fragmentCount = 0;
fallOffRate = 0 # Set: The taq polymerase “fall-off rate” is d+r, where d is a fixed constant, and r is a random number between [-e, e], (assume d = 200, e=50). 

# Forward and backward primer could have 'fall off' at different times... Set separately. 
# For every copy made, make new 'active' primer, - 1 primer for a fall off. 
https://cdn.kastatic.org/ka-perseus-images/41f0e0fd8b49ba824db0eb707015557bb72ae72b.png

# !!!!![not just one primer, replace single fo variable with something more.] !!!!!

d = 200;
e = 50;

# Assuming fall-off rate is falls off after copying that many bases, since max fo rate is 250, min 150, and supossed to only run 1-50 cycles. 



def getDNA():
    # Get/ Generate DNA to use here. 
    return dna;
   

# Step 1 function.

# In the first step of PCR, the two strands of the DNA double helix are physically separated at a high temperature in a process called DNA melting. 


def Step1():
    
    return 1; # Placeholder. 


# Step 2 function. 

# In the second step, the temperature is lowered and the primers bind to the complementary sequences of DNA.
# In the next step, the reaction temperature is lowered allowing annealing of the primers to each of the single-stranded DNA templates.
# The primers are single-stranded sequences themselves, but are much shorter than the length of the target region, 
# complementing only very short sequences at the 3' end of each strand.


def Step2():
    
    return 1;


# Step 3 function.

# The two DNA strands then become templates for DNA polymerase to enzymatically assemble a new DNA strand from free nucleotides, the 
# building blocks of DNA. As PCR progresses, the DNA generated is itself used as a template for replication, setting in motion a 
# chain reaction in which the original DNA template is exponentially amplified.

def Step3():
    
    return 1;

 

def ResultPrint():
    
    # Your output: (What you might see on the gel)
    
    # 1. Statistics of the PCR products:
    
    print ("Fragment Count: ", fragmentCount, "\n");
    #       (b)   !!! Average length (# bases) of DNA fragments. !!! - Track, Add fragments to list. List of fragment strings/lists? || tup? 
    #       (c)   Distribution of the lengths of the DNA fragments (you may use column chart to show your result). (? Find out more.)
    
    # 2. Other things you find interesting.
    
    return 0;



def main():
    
    # Get dna input sequence.
    dnaSeg = getDNA();
    
    # Get cycle count input From user.
    
    cycleCount = 0;
    
    completeCycles = 0;
    
    # For any step where, for our purposes, changing the step time length would make a difference, allow time input.
    
    while completeCycles < cycleCount:
        
        Step1();
        Step2();
        Step3();
        completeCycles += 1;
        
        # Print out results of each cycle, at least for checking program correctness and debugging purposes if nothing else? 
    
    ResultPrint();
    
    return 0; 





