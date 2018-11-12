
import numpy as np


class BinaryLogisticRegression:

	def __init__(self, X_train, Y_train, alpha):
		"""
		This is the constructor for this class. It assigns the hyper parameters based on the training data and other arguments.

		:param X_train: Input training vector of size (x_n, m)
		:param Y_train: Output training vector of size (1, m)
		:param alpha: Learning rate of this classifier
		"""
		# Getting training sets
		self.X_train = X_train
		self.Y_train = Y_train

		# Getting relevant dimension sizes
		self.x_n = X_train.shape[0]
		self.m = X_train.shape[1]

		# Initialising parameters
		self.W = np.zeros(self.x_n, 1)
		self.b = 0

		# Setting hyper-parameters
		self.alpha = alpha

	def _forward_prop(self, X):
		"""
		This function performs forward propagation using the current parameters of the model using the giver input vector(s)
		and returns the corresponding output value(s)

		:param X: Single or multiple input vector(s) of shape (x_n, m) where m can be 1
		:return: A: Output vector of shape (1, m) corresponding to the current models output for each input vector passed where m can be 1
		"""
		pass

	@staticmethod
	def loss(A, Y):
		"""
		This function calculates the loss after forward propagation.
		If A, Y are vectors shaped (1, m) then this function returns the cost instead of the loss.

		:param A: Output vector of shape (1, m) corresponding to the current models output for each input vector passed where m can be 1
		:param Y: Expected output vector of shape (1, m) corresponding to the current models output for each input vector passed where m can be 1
		:return: Loss if A.shape == (1, 1) else Cost
		"""
		pass

	def _backward_prop(self, A):
		"""
		This function performs backward propagation given the current output vector A.

		:param A: Output vector of shape (1, m) corresponding to the current models output for each input vector passed where m can be 1
		:return: Dictionary with gradient descent results stored in it with keys - { dW, db }
		"""
		pass

	def train(self, iterations=1000):
		"""
		This function trains this model by running `iteration` number of forward and backward propagation.
		The model must be trained before trying to use it to make predictions.

		:param iterations: The number of iterations we want it to run for
		:return: None
		"""
		pass

	def predict(self, X, Y=None):
		"""
		This function performs predictions using its current parameters on X and return the appropriate results.
		If Y is provided, it will instead return the accuracy of the predictions w.r.t Y.

		:param X: Input vector of size (x_n, m) where m can be 1
		:param Y: Output vector of size (x_n, m) where m can be 1 (optional)
		:return: Prediction vector on X if y is not provided, else accuracy vector
		"""
		pass