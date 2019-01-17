"""
         *                   *                   *                   * 
        * *                 * *                 * *                 * * 
       * * *               * * *               * * *               * * * 
      * * * *             * * * *             * * * *             * * * * 
     * * * * *           * * * * *           * * * * *           * * * * * 
    * * * * * *         * * * * * *         * * * * * *         * * * * * * 
   * * * * * * *       * * * * * * *       * * * * * * *       * * * * * * * 
  * * * * * * * *     * * * * * * * *     * * * * * * * *     * * * * * * * * 
 * * * * * * * * *   * * * * * * * * *   * * * * * * * * *   * * * * * * * * * 
"""

for i in range(10):
    for j in range(10,i,-1):
        print(" ",end="")
    for k in range(1,i+1):
        print("*",end=" ")
    for l in range(10,i,-1):
        print(" ", end=" ")
    for m in range(1,i+1):
        print("*", end=" ")
    for n in range(10,i,-1):
        print(" ", end=" ")
    for o in range(1,i+1):
        print("*", end=" ")
    for p in range(10,i,-1):
        print(" ", end=" ")
    for q in range(1,i+1):
        print("*", end=" ")
    print()
    
