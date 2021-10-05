# Patent claim dependecy

Patent claims that refer back to and further limit another claim are called dependent claims. Each claim usually contains a set of features. 

## Example

Let us take the following example of patent claims:

- claim 1
- claim 2
-- depending on claim 1
- claim 3
-- depending on claim 1 and 2
- claim 4
-- depending on claim 1
- claim 5
-- depending on claim 2
- claim 6
-- depending on claim 1 to 5
- claim 7
-- depending on claim 2 and 5
- claim 8
-- depending on claim 3 and 4

where claim 2 to 8 are dependet claims of claim 1.

And let us say, claim 2 defines feature A. 

Question: **Which claim may refer to feature A of claim 2?**

Solution:
- claim 1: Feature A is first defined in claim 2 - No
- claim 2: Definition of feature A - Yes
- claim 3: Refers to claim 1 and claim 2. Claim 1 does not disclose feature A. A combination of claim 1 and claim 3 would not contain feature A. Therefore claim 3 may not refer to feaure A of claim 2 as a definitely existing feature - No
- claim 4: Refers to claim 1 only - No
- claim 5: Refers to claim 2 only - Yes
- claim 6: Refers to claims 1 to 5; some claims do not disclose the feature A - No
- claim 7: Refers to claim 2 and 5; claim 5 refers to claim 2 only - Yes
- claim 8: Refers to claim 3 and 4; both claims do not contain feature A - No 


## Aim

In this small project, I would like to tackle questions like the one above. Also, some Python code is provided, which might help to solve these issues.

## Coding

Let us take a look again at the example above and use some code to get an answer to the stated question of dependency.

### Defining the dependency

Following lines define the dependency of the claims:

<code>claim = [[1], [1], [1,2], [1], [2], [1,2,3,4,5], [2,5], [3,4]]</code>


Claim 1 ("[1]") only depends on itself. Claim 2 ("[1]") depends on claim 1. Claim 3 ("[1,2]") depends on claim 1 and 2. And so on.

Now, the claim containing the definition of feature A has to be defined:

<code>claim_containing_definition = 2</code> 

Claim 2 defines the feature A.

### Function dependency_check()

Put this in the function "dependency_check()":

<code>dependency_check(claim, claim_containing_definition)</code> 

Output:

<code>[False, True, False, False, True, False, True, False]</code> 

The output list gives the same results as explained above, saying which claim may refer to feature A:

- claim 1: False - No
- claim 2: True  - Yes
- claim 3: False - No
- claim 4: False - No
- claim 5: True  - Yes
- claim 6: False - No
- claim 7: True  - Yes
- claim 8: False - No 



