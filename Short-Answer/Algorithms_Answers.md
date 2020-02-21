#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) Run time is `O(n)`, because of the input size of n in a while loop condition.


b) Run time is `O(n^2)` because inner loop is dependant on the size of n, which is being used in the outer loop as well.


c) Run time is simply `O(n)` because there is one iteration here (done recursively) depending on the size of input n.

## Exercise II

1. Drop the egg from the first floor to see if it breaks
    1.1 Exit if it does, continue if not
2. Find the total ammount of floors and calculate the middle one, then drop the egg
    2.1 If egg survives the flight:
        2.1.1 remove the bottom floors and start the step 2 with again
    2.2. If egg breaks:
        2.2.1 remove upper floors and start again with the step 2
3. Terminate the process once there's one floor remaining
4. Return broken eggs count

Using this binary search algorithm has a run time complexity of `O(log n)` since it uses divide & conquer techique.