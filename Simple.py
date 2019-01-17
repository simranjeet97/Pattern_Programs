"""

         *                   * 
        * *                 * * 
       * * *               * * * 
      * * * *             * * * * 
     * * * * *           * * * * * 
    * * * * * *         * * * * * * 
   * * * * * * *       * * * * * * * 
  * * * * * * * *     * * * * * * * * 
 * * * * * * * * *   * * * * * * * * * 
* * * * * * * * * * * * * * * * * * * * 
 * * * * * * * * * S * * * * * * * * * 
  * * * * * * * * S S * * * * * * * * 
   * * * * * * * S S S * * * * * * * 
    * * * * * * S S S S * * * * * * 
     * * * * * S S S S S * * * * * 
      * * * * S S S S S S * * * * 
       * * * S S S S S S S * * * 
        * * S S S S S S S S * * 
         * S S S S S S S S S * 
          S S S S S S S S S S 
         * S S S S S S S S S * 
        * * S S S S S S S S * * 
       * * * S S S S S S S * * * 
      * * * * S S S S S S * * * * 
     * * * * * S S S S S * * * * * 
    * * * * * * S S S S * * * * * * 
   * * * * * * * S S S * * * * * * * 
  * * * * * * * * S S * * * * * * * * 
 * * * * * * * * * S * * * * * * * * * 
* * * * * * * * * * * * * * * * * * * * 
 * * * * * * * * *   * * * * * * * * * 
  * * * * * * * *     * * * * * * * * 
   * * * * * * *       * * * * * * * 
    * * * * * *         * * * * * * 
     * * * * *           * * * * * 
      * * * *             * * * * 
       * * *               * * * 
        * *                 * * 
         *                   * 

"""

for i in range(10):
        for j in range(10,i,-1): #Spaces
            print(" ", end="")
        for k in range(1,i+1):
            print("*", end=" ")
        for j in range(10,i,-1): #Spaces
            print(" ", end=" ")
        for k in range(1,i+1):
            print("*", end=" ")
        print()
        
for i in range(10):
        for j in range(1,i+1): #Spaces
            print("", end=" ")
        for k in range(10,i,-1):
            print("*", end=" ")
        for a in range(1,i+1): #Spaces
            print("S", end=" ")
        for b in range(10,i,-1):
            print("*", end=" ")
        print()

for i in range(10):
        for j in range(10,i,-1): #Spaces
            print(" ", end="")
        for k in range(1,i+1):
            print("*", end=" ")
        for j in range(10,i,-1): #Spaces
            print("S", end=" ")
        for k in range(1,i+1):
            print("*", end=" ")
        print()
        
for i in range(10):
        for j in range(1,i+1): #Spaces
            print("", end=" ")
        for k in range(10,i,-1):
            print("*", end=" ")
        for a in range(1,i+1): #Spaces
            print(" ", end=" ")
        for b in range(10,i,-1):
            print("*", end=" ")
        print()
