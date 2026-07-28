class solution:

    def pattern1(self,n):
    # 1
    # 2 3
    # 4 5 6
    # 7 8 9 10
    # 11 12 13 14 15
        dig = 1
        for i in range (n):
            for j in range (i+1):
                print(dig,end=" ")
                dig +=1
            print()

    def pattern2(self,n):
        # A
        # A B
        # A B C
        # A B C D
        # A B C D E
        for i in range(n):
            for j in range (i+1):
                print(chr(65+j),end=" ")
            print()

    def pattern3(self,n):
        # A
        # B B
        # C C C
        # D D D D
        # E E E E E
        for i in range (n):
            for j in range (i+1):
                print(chr(65+i),end=" ")
            print()
    
    def pattern4(self,n):
        #       A
        #     A B A
        #   A B C B A
        # A B C D C B A
        for i in range (n-1):
            #starting gap
            for j in range (n-i-2):
                print(" ",end=" ")
            a = 0
            for j in range (i*2+1):
                if j<(i*2+1)/2:
                    print(chr(65+j),end=" ")
                    a =a+1
                else:
                    a=a-1
                    print(chr(65+a-1),end =" ")
            print()

    def pattern5(self,n):
        # E
        # D E
        # C D E
        # B C D E
        # A B C D E
        for i in range (n):
            a =n-i-1
            for j in range (i+1):
                print(chr(65+a),end=" ")
                a+=1
            print()

    def pattern6(self,n):
        # * * * * * * * * * *
        # * * * *     * * * *
        # * * *         * * *
        # * *             * *
        # *                 *
        # * *             * *
        # * * *         * * *
        # * * * *   * * * * *
        # * * * * * * * * * *
        a = n-2
        for i in range (n*2-1):
            if (i < n):
                print("* "*(n-i),end="")
                print("i "*(i*2),end = "")
                print("* "*(n-i),end=" ")
            else:
                print("* "*(i-n+2),end="")
                print("i "*a*2,end="")
                a=a-1
                print("* "*(i-n+2),end="")
            print()
            
    def pattern7(self,n):
        # *               *
        # * *           * * 
        # * * *       * * * 
        # * * * *   * * * * 
        # * * * * * * * * * 
        # * * * *   * * * * 
        # * * *       * * *
        # * *           * *
        # *               *
        for i in range (n*2-1):
            if i < n:
                print("* "*(i+1),end="")
                print("i "*(n*2-i*2-2),end="")
                print("* "*(i+1),end="")

            else:
                print("* "*(n*2-i-1),end="")
                print("i "*((i-n+1)*2),end="")
                print("* "*(n*2-i-1),end="")
            print()

    def pattern8(self,n):
        # * * * *
        # *     *
        # *     *
        # * * * *
        for i in range (n-1):
            if i==0 or i==n-2:
                print("* "*(n-1))
            else:
                print("* ",end="")
                print("  "*(n-3),end="")
                print("*")

    def pattern9(self,n):
        # 4 4 4 4 4 4 4
        # 4 3 3 3 3 3 4
        # 4 3 2 2 2 3 4
        # 4 3 2 1 2 3 4
        # 4 3 2 2 2 3 4
        # 4 3 3 3 3 3 4
        # 4 4 4 4 4 4 4
        for i in range (n*2-1):
            for j in range (n*2-1):
                top = i
                left = j
                bottom = (2*n-2)-i
                right = (2*n-2) - j
                minDist = min(top,bottom,left,right)
                print(n-minDist,end=" ")
            print()


sol = solution()
n=4
sol.pattern9(n)