# 🧭 PyQt5 Window Close Flow with closeEvent()

## 1. User or Code Initiates Close

```
[User clicks ❌ button]  
        OR  
[Your code calls self.close()]
        ↓
        ↓
Qt triggers:
→ closeEvent(self, event)
```

## 2. Your `closeEvent()` Method Runs

```python
def closeEvent(self, event):
    self.main_window.second_window = None  # Reset reference
    super().closeEvent(event)               # Proceed with actual closing
```

✅ This clears the reference in MainWindow  
✅ Prevents stale pointer next time MainWindow tries to open SecondWindow

## 3. Optional: You Call self.close() in enter()

```python
def enter(self):
    # Optional: update MainWindow widgets
    self.close()  # Triggers closeEvent()
```

## 📊 Summary Flow

```text
+-------------------+
| MainWindow Button |
+--------+----------+
         |
         v
+-------------------------+
| self.second_window =    |
| SecondWindow(self)      |
+--------+----------------+
         |
         v
+-------------------+
|  User clicks btn  |
|  in SecondWindow  |
+--------+----------+
         |
         v
+-------------------+
|  self.close()     | ← called in enter()
+--------+----------+
         |
         v
+-------------------+
| closeEvent runs   |
| → clears pointer  |
+-------------------+
```
