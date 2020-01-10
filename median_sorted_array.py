class Solution:
    @staticmethod
    def findMedianSortedArrays(nums1: object, nums2: object) -> object:
        if nums1 and nums2:
            new_list = sorted(nums1 + nums2)
            len_list = len(new_list)
            middle = len_list // 2
            if len_list % 2 == 0:
                return (new_list[middle - 1] + new_list[middle]) / 2
            else:
                return new_list[int((len_list - 1) / 2)]


def main():
    obj = Solution()
    print(obj.findMedianSortedArrays([1, 3], []))


if __name__ == '__main__':
    main()
