
size = [500, 700, 900, 1100, 1300]
price = [100, 150, 200, 250, 300]


n = len(size)

mean_x = sum(size)/n
mean_y = sum(price)/n

num = sum((size[i]-mean_x)*(price[i]-mean_y) for i in range(n))
den = sum((size[i]-mean_x)**2 for i in range(n))

b1 = num/den
b0 = mean_y - b1*mean_x

print("Intercept:", b0)
print("Slope:", b1)


new_size = 1000
predicted_price = b0 + b1*new_size

print("Predicted price for 1000 sqft:", predicted_price)