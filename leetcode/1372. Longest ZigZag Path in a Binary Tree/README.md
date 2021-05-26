### idea

when we are at a node, 
there are 2 options: left or right
if the current dir is left, we go left and change dir
if the current dir is right, we go right and change dir
we can also have the option to override the dir and start again
the `step` variable is there to do the memo. when "overriding", we need to set step to 0 to disconnect the current path with its parrent
else the previous path will be added (remember the false solution)
