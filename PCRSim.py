#!/user/bin/python


#---------- Misc. Notes ----------

"""
two DNA primers that are complementary to the 3' (three prime) ends of each of the sense and anti-sense strands of the DNA target

specific primers that are complementary to the DNA target region are selected beforehand, and are often custom-made in a laboratory



"""

#---------------------------------



# The size of the DNA segment to be amplified. 

ampSeg = 200; # Set to something better later if needed. 
primerLen = 20; # "Assume that the length of the original forward and backward primers are fixed at p bases (assume p = 20)."
fragmentCount = 0;

# ADD/DO:

# 5. The processivity of the taq polymerase (“fall-off rate”) is d+r, where d is a fixed constant, and r is a random number between [-e, e], (assume d = 200, e=50).
   

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

# (is this below all step 3? wiki article not clear, doublecheck elsewhere.) 
# The two DNA strands then become templates for DNA polymerase to enzymatically assemble a new DNA strand from free nucleotides, the 
# building blocks of DNA. As PCR progresses, the DNA generated is itself used as a template for replication, setting in motion a 
# chain reaction in which the original DNA template is exponentially amplified.

def Step3():
    
    return 1;

 

def ResultPrint():
    
    # Your output: (What you might see on the gel)
    
    # 1. Statistics of the PCR products:
    
    #       (a)   Number of DNA fragments.
    #       (b)   !!! Average length of DNA fragments. !!! - Track, Add fragments to list. List of fragment strings/lists? || tup? 
    #       (c)   Distribution of the lengths of the DNA fragments (you may use column chart to show your result). (? Find out more.)
    
    # 2. Other things you find interesting.
    
    return 0;



def main():
    
    # Get dna input sequence.
    
    
    
    # Get cycle count input.
    
    cycleCount = 0;
    
    completeCycles = 0;
    
    # For any step where, for our purposes, changing the step time length would make a difference, allow time input.
    
    while completeCycles < cycleCount:
        
        Step1();
        Step2();
        Step3();
        
        # Print out results of each cycle, at least for checking program correctness and debugging purposes if nothing else? 
    
    ResultPrint();
    
    return 0; 
