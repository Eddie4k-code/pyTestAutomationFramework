h = [0,1,0,2,1,0,1,3,2,1,2,1]


def trap(h):
    left = 0
    right = len(h) - 1

    maxL = h[left]
    maxR = h[right]

    res = 0

    while left < right:
        if maxL < maxR:
            left += 1
            maxL = max(maxL, h[left])
            res += maxL - h[left]

        else:
            right -= 1
            maxR = max(maxRight)



