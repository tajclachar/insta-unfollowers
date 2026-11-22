# **CS5002 Final Project Proposal**

#### **Taj Clachar ∙ November 15th 2026**

---

## **Instagram Follower / Unfollower Set Comparison**

Hi Professor,

I plan on building a Python program that will analyze Instagram followers. Today, most people analyze their follower data using apps that are against Instagram guidelines and often lead to accounts getting either hacked or banned. A week ago I created a program for fun that only returns a set of people that are in a user’s following list but not in their followers list.  I would love to use this project as an opportunity to take the script I created, expand it, and make it into a polished program.

The program would take the followers and following lists from a user's downloaded data, turn them into sets, and answer the following questions...

1. Who doesn't follow me back? (Module 3\)  
2. Who do I not follow back? (Module 3\)  
3. Who are my mutuals? (Module 3\)  
4. How likely is it that a random account I follow, follows me back? (Module 6\)

**Module Coverage**  
U: All the followers and following, the universal set  
F: Followers  
G: Following 

**3 (Set Operations & Set Builder Notation):** Compare the sets to see who doesn’t follow you back, who you don’t follow back and your mutuals. Write this in set builder notation while also using Python to display the results and calculation. Also show that the set, mutuals, is a subset of the following set as well as the followers set.   
**2** (**Logic and De Morgan’s):** Use logic to validate elements in different sets like  x ∈ F ∩ G means (x ∈ F) AND (x ∈ G). Also, check that complement(F ∩ G) \= complement(F) ∪ complement(G).   
**4 (Inclusion-exclusion):** Inclusion-exclusion formula will deliver the number of people in both followers and following while getting rid of the overlap. This can be used to confirm the “length” of the universal set.  
**3/4 (Cartesian Products and Counting):** Cartesian product can be used to find the mutuals but, it will be a much lengthier process compared to set notation. This can be used as an example to show the usefulness of sets. I’’ll count the comparisons and compare that to using the sets to also show the higher efficiency of sets.  
**6 (Probability)**: Calculate the probability that an account I follow follows me back. Can also do the chance that a random follower is someone I follow back.

**Deliverable**

1. Python code files  
2. Read me  
3. Samples dataset(s)  
4. Program output. Summary tables with counts and results and probabilities  
5. Recorded presentation

**Stretch Goals**

1. Simple webpage where someone can upload their export and see their results.  
2. Tracking changes over time (ex. “Since your last comparison, you have followed x people, unfollowed y people and now have z mutuals”)

