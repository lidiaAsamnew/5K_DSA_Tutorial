class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        num_sorted = sorted(nums)
        target_idx = []
        for i in range(len(num_sorted)):
            if num_sorted[i] == target:
                target_idx.append(i)
        return target_idx
