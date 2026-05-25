from sympy import (
    symbols,
    sympify,
    SympifyError,
    sin,
    cos,
    tan,
    exp,
    log,
    sqrt
)

# =========================================
# SYMBOLS
# =========================================

x, y = symbols('x y')


# =========================================
# SAFE FUNCTIONS
# =========================================

SAFE_FUNCTIONS = {

    "x": x,
    "y": y,

    "sin": sin,
    "cos": cos,
    "tan": tan,

    "exp": exp,
    "log": log,
    "sqrt": sqrt

}


# =========================================
# HEUN METHOD
# =========================================

def heun_method(
    func_str,
    x0,
    y0,
    h,
    steps
):

    # =====================================
    # VALIDATION
    # =====================================

    if steps <= 0:

        raise ValueError(
            "Number of steps must be positive."
        )

    if h <= 0:

        raise ValueError(
            "Step size must be positive."
        )

    # =====================================
    # SAFE PARSING
    # =====================================

    try:

        func = sympify(
            func_str,
            locals=SAFE_FUNCTIONS
        )

    except SympifyError:

        raise ValueError(
            "Invalid mathematical expression."
        )

    # =====================================
    # RESULTS STORAGE
    # =====================================

    results = []

    x_values = [x0]
    y_values = [y0]

    # =====================================
    # ITERATIONS
    # =====================================

    for i in range(steps):

        # ---------------------------------
        # FIRST SLOPE
        # ---------------------------------

        f1 = float(

            func.subs({

                
                x: x0,
                y: y0

            })

        )

        # ---------------------------------
        # PREDICTOR
        # ---------------------------------

        predictor = y0 + h * f1

        # ---------------------------------
        # NEXT X
        # ---------------------------------

        x1 = x0 + h

        # ---------------------------------
        # SECOND SLOPE
        # ---------------------------------

        f2 = float(

            func.subs({

                x: x1,
                y: predictor

            })

        )

        # ---------------------------------
        # CORRECTOR
        # ---------------------------------

        corrected = y0 + (h / 2) * (f1 + f2)

        # =================================
        # SAVE RESULTS
        # =================================

        results.append({

            "step":
                i + 1,

            "x0":
                round(x0, 6),

            "y0":
                round(y0, 6),

            "f1":
                round(f1, 6),

            "predictor":
                round(predictor, 6),

            "f2":
                round(f2, 6),

            "x":
                round(x1, 6),

            "corrected":
                round(corrected, 6)

        })

        # =================================
        # UPDATE VALUES
        # =================================
         
        x_values.append(x1)
        y_values.append(corrected)

        x0 = x1
        y0 = corrected

    return results, x_values, y_values