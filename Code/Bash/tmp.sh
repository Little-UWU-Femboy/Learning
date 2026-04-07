var="One Two Three" # String that has speace separeted values inside it
arr=($var) # this creates an array with 3 indexes with a separate one for each part

echo ${arr[@]} # will print One Two Three
echo ${#arr[@]}
