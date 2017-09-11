import keras.backend as K
import numpy as np

E = 1e-10  # numerical stability


def cross_entropy(p, q):
    '''H(p, q) = -sum_i(p_i * log(q_i))'''
    with K.name_scope('crossentropy'):
        return -K.mean(p * K.log(E + q))


def entropy(p):
    '''H(p) = -sum_i(p_i * log(p_i))'''
    return cross_entropy(p, p)


def binary_crossentropy(p, q):
    with K.name_scope('binary_crossentropy'):
        pointwise = p * K.log(E + q) + (1 - p) * K.log(E + 1 - q)
        value = -K.mean(pointwise)
    return value


def squared_error(p, q):
    '''MSE(p, q) = ||p - q||^2'''
    with K.name_scope('squared_error'):
        return K.sum(K.square(p - q), axis=1)


def reconstruction_loss(original_images, reconstructed_images):
    if len(original_images.shape) > 2:
        flat_shape = [-1, int(np.prod(original_images.shape[1:]))]
        original_images = K.reshape(original_images, flat_shape)
        reconstructed_images = K.reshape(reconstructed_images, flat_shape)
    return squared_error(original_images, reconstructed_images)


def mutual_information(x, x_given_y):
    '''I(x;y) = H(x) - H(x|y)'''
    with K.name_scope('mutual_information'):
        h_x = entropy(x)
        # The cross entropy between x and x|y is H(x|y).
        h_x_given_y = cross_entropy(x, x_given_y)
        # The mutual information I(x;y) is now H(x) - H(x|y).
        # Usually we want to maximize mutual information, but to provide a
        # minimizable objective for TF's optimizer, we return E[-(H(x) -
        # H(x|y))] = E[H(x|y) - H(x).]
        return K.mean(h_x_given_y - h_x)
