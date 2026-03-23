import numpy as np
def f1_micro(y_true, y_pred) -> float:
    """
    Compute micro-averaged F1 for multi-class integer labels.
    """
    # Write code here
    y_true, y_pred = np.array(y_true), np.array(y_pred)
    TP = (y_true == y_pred).sum()
    total = len(y_true)

    accuracy = TP / total
    return accuracy