class solution:
    def pattern1(self,n):
        #         *
        #       * * *
        #     * * * * *
        #   * * * * * * * 
        # * * * * * * * * *
        # time- O(n^2) space-O(1)
        for i in range (n):
            #frount space
            for j in range (n-i-1):
                print(" ",end=" ")
            #stars
            for j in range (2*i +1):
                print("*",end = " ")
            #last space
            for j in range (n-i-1):
                print(" ",end=" ")
            print()
        
    def pattern2(self,n):
        # *
        # * *
        # * * *
        # * * * *
        # * * * * * 
        # time- O(n^2) space-0(1)
        for i in range (n):
            for j in range (i+1):
                print("*", end = " ")
            print()

    def pattern3(self,n):
        # * * * * *
        # * * * * *
        # * * * * *
        # * * * * *
        # * * * * *
        for i in range (n):
            for j in range (n):
                print("*", end =" ")
            print()

    def pattern4(self,n):
        # 1
        # 1 2
        # 1 2 3 
        # 1 2 3 4
        # 1 2 3 4 5
        # time-O(n^2) space-O(1)
        for i in range (n):
            for j in range (i+1):
                print(j+1,end=" ")
            print()

    def pattern5(self,n):
        # 1
        # 2 2
        # 3 3 3 
        # 4 4 4 4
        # 5 5 5 5 5
        # Time - O(N^2) Space-O(1)
        for i in range (n):
            for j in range (i+1):
                print(i+1, end=" ")
            print()

    def pattern6(self,n):
            # * * * * * 
            # * * * *
            # * * *
            # * *
            # *
            #Time - O(n^2) space- O(1)
        for i in range (n):
            for j in range (n-i):
                print("*", end= " ")
            print()

    def pattern7(self,n):
        # 1 2 3 4 5
        # 1 2 3 4
        # 1 2 3
        # 1 2
        # 1
        #Time-O(N^2) Space-O(1)
        for i in range (n):
            for j in range (n-i):
                print(j+1,end=" ")
            print()

    def pattern8(self,n):
        #  * * * * * * * * *
        #    * * * * * * *
        #      * * * * *    
        #        * * *
        #          *
        # Time-O(N^2) Space-O(1)
        for i in range (n):
            #starting gap
            for j in range (i):
                print(" ",end=" ")
            # stars
            for j in range ((n-1-i)*2+1):
                print("*",end =" ")
            #ending gap
            for j in range (i):
                print(" ",end=" ")
            print()

    def pattern9(self,n):
        #          *
        #        * * *
        #      * * * * *
        #    * * * * * * *
        #  * * * * * * * * *
        #    * * * * * * *
        #      * * * * *
        #        * * *
        #          *
        # Time-O(N^2) [n^2 + n^2 = 2n^2 ~ n^2 ] Space- O(1)
        for i in range (n):
            #frount space
            for j in range (n-i-1):
                print(" ",end=" ")
            #stars
            for j in range (2*i +1):
                print("*",end = " ")
            #last space
            for j in range (n-i-1):
                print(" ",end=" ")
            print()
        for i in range (n):
            #starting gap
            for j in range (i):
                print(" ",end=" ")
            # stars
            for j in range ((n-1-i)*2+1):
                print("*",end =" ")
            #ending gap
            for j in range (i):
                print(" ",end=" ")
            print()

    def pattern10(self,n):
        # *
        # * *
        # * * *
        # * * * *
        # * * * * *
        # * * * *
        # * * *
        # * * 
        # *
        # Time-O(N^2) Space-O(1)
        for i in range (n*2-1):
            if i <5:
                print("* "*(i+1))
            else:
                print("* "*(n*2-1-i))

    def pattern11(self,n):
        # 1
        # 0 1
        # 1 0 1
        # 1 0 1 0
        # 0 1 0 1 0
        for i in range (n):
            value = 1
            if i%2 != 0:
                for j in range (i+1):
                    print(value,end=" ")
                    value = 1 - value
            else:
                for j in range (i+1):
                    print(value,end=" ")
                    value = 1 - value
            print()

    def pattern12(self,n):
        # 1             1
        # 1 2         2 1
        # 1 2 3     3 2 1
        # 1 2 3 4 4 3 2 1
        for i in range (n-1):
            # starting digits
            for j in range (i+1):
                print(j+1,end=" ")
            # for middle space
            for j in range (n*2-4-i*2):
                print(" ",end=" ")
            # ending digits
            for j in range (i+1):
                print(i-j+1,end=" ")
    
            print()




sol = solution()
n=5
sol.pattern12(n)