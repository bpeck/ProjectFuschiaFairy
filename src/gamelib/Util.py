def clamp(x, min=0.0, max=1.0):
    if clamp < min:
        return min
    if clamp > max:
        return max
    return x

def clampAmp(x, amp=1.0):
    if abs(x) <= amp:
        return x
    if x < -amp:
        return -amp
    return amp
