pen_qnty = int(input())
marker_qnty = int(input())
cleaning_detergent = int(input())
discount_prst = int(input()) / 100
subtotal = (pen_qnty * 5.80) + (marker_qnty * 7.20) + (cleaning_detergent * 1.20)
total = subtotal - (subtotal * discount_prst)
print(total)
