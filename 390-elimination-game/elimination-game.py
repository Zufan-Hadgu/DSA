class Solution:
    def lastRemaining(self, n: int) -> int:
        # evens = set()
        # for i in range(1,n + 1):
        #         evens.add(i)
        # def rec(evens):
        #     if len(evens) == 1:
        #         return evens[0]
        #     for num in evens:
        #         if i % 2 == 1:
        #             evens.remove(num)
        #     rec(evens)
        #     for num in evens:
        #         if i % 2 == 0:
        #             evens.remove(num)
        #     rec(evens)
        # output = rec(evens)
        # return output


        def rec(head,remaining,forward,step):
            if remaining == 1:
                return head
            if forward:
                head = head + step
            if not forward and remaining % 2 == 1:
                head = head + step
            step = step * 2
            remaining = remaining // 2
            return rec(head,remaining,not forward,step)
        output = rec(1,n,True,1)

        return output

 


            


        