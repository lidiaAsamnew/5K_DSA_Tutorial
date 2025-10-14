class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        next_greater = defaultdict(lambda: -1)

        for num in nums2:
            while stack and num > stack[-1]:
                value = stack.pop()
                next_greater[value] = num
            stack.append(num)

        return [next_greater[num] for num in nums1]
