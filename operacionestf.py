import tensorflow as tf 
a = tf.constant ([10,20,30])
b = tf.constant([1,2,3])

suma=tf.add(a,b)
resta=tf.subtract(a,b)
producto=tf.multiply(a,b)
division=tf.divide(a,b)

print("Tensor A: ",a.numpy())
print("Tensor B: ",b.numpy())
print("Suma: ",suma.numpy())
print("Resta : ",resta.numpy())
print("Multiplicacion : ",producto.numpy())
print("Division : ",division.numpy())