# Euler-Assembly
Assignment from 576 bioinformatics, assembles full length sequences from smaller parts
 

Assignment instructions
Begin your Eulerian cycle algorithm by starting at the vertex that is first in lexicographical order
(e.g., if the set of vertices are CT,AC, and TA, you should start at vertex AC ).
•
When  you  reach  a  vertex  with  multiple  unused  outgoing  edges,  choose  the  edge  that  is  first  in
lexicographical order.
•
After each cycle-finding and merging iteration, start your next cycle at the first vertex within your
current cycle that has an unused outgoing edge. For example,if your current cycle is
AT->TC->CA->AT, and both TC and CA have unused outgoing edges, then begin your next cycle at TC, because it
comes first in the listing of your cycle, which starts with the vertex you selected at the beginning
of the algorithm (see point above)
•
At the end of your algorithm, when removing the fake edge from your cycle (if such an edge was
added to balance the graph), if there are two copies of that edge (see note below), then remove the
copy that comes first in the listing of your cycle.
 
Note:  there exist valid k-mer spectra for which the corresponding k-mer graph has two unbalanced
vertices, and the fake edge one would add to balance those vertices already exists in the graph.  To make
the Eulerian cycle algorithm work, one still needs to add an extra fake edge in this case, which results
in two identical edges, making the graph a multigraph.  You will need to use data structures that can
accommodate this case.
