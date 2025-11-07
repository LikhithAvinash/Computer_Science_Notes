Here is the full explanation converted into **clean and neat Markdown (MD)** format for GitHub:

---

# 📊 MAE vs MSE vs RMSE — Explained Clearly

This document explains the differences between **MAE**, **MSE**, and **RMSE** using **5 data points**.
It includes calculations, tables, and penalties comparison.

---

## ✅ Sample Dataset (5 Points)

| Actual | Predicted |
| ------ | --------- |
| 100    | 90        |
| 150    | 160       |
| 200    | 190       |
| 250    | 260       |
| 300    | 280       |

---

## ✅ Step 1 — Error Calculations

We compute:

```
error = actual - predicted
abs_error = |error|
sq_error = error²
```

| Actual | Pred | Error | Abs Error | Squared Error |
| ------ | ---- | ----- | --------- | ------------- |
| 100    | 90   | 10    | 10        | 100           |
| 150    | 160  | -10   | 10        | 100           |
| 200    | 190  | 10    | 10        | 100           |
| 250    | 260  | -10   | 10        | 100           |
| 300    | 280  | 20    | 20        | 400           |

* **Sum of absolute errors = 60**
* **Sum of squared errors = 800**

---

## ✅ Step 2 — MAE (Mean Absolute Error)

Formula:

```
MAE = (sum of absolute errors) / n
```

Calculation:

```
MAE = 60 / 5 = 12
```

✅ **MAE = 12**

---

## ✅ Step 3 — MSE (Mean Squared Error)

Formula:

```
MSE = (sum of squared errors) / n
```

Calculation:

```
MSE = 800 / 5 = 160
```

✅ **MSE = 160**

---

## ✅ Step 4 — RMSE (Root Mean Squared Error)

Formula:

```
RMSE = √MSE
```

Calculation:

```
RMSE = √160 ≈ 12.65
```

✅ **RMSE ≈ 12.65**

---

## ✅ Final Results Summary

| Metric   | Value |
| -------- | ----- |
| **MAE**  | 12    |
| **MSE**  | 160   |
| **RMSE** | 12.65 |

---

## ✅ Which Metric Gives More Penalty?

### ✅ **Most Penalty → MSE**

### ✅ **Medium Penalty → RMSE**

### ✅ **Least Penalty → MAE**

### Why?

Because large errors get amplified:

* In **MAE**:
  Error = 20 → penalty = 20
* In **MSE/RMSE**:
  Error = 20 → penalty = 400 (because 20²)

So **MSE** and **RMSE** punish big mistakes much more heavily.

---

## ✅ Quick Summary

| Metric   | Penalizes Large Errors? | Sensitive to Outliers? | Units          |
| -------- | ----------------------- | ---------------------- | -------------- |
| **MAE**  | ❌ No                    | ❌ No                   | Same as target |
| **MSE**  | ✅ Yes (squares errors)  | ✅ Yes                  | Squared units  |
| **RMSE** | ✅ Yes                   | ✅ Yes                  | Same as target |

---

If you want, I can also generate:
✅ A graph comparing penalties
✅ Python code version
✅ A README-ready explanation

Just tell me!

