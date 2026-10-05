## CarPlay

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.symptom_diagnostics"))
 		(require-not (global-name "com.apple.accessibility.AXBackBoardServer"))
 		(require-not (global-name "com.apple.hangtracerd"))
+		(require-not (global-name "com.apple.manageddeviced.managed-apps"))
 		(require-not (require-any
 			(global-name "com.apple.CarPlayApp.punch-through-service")
 			(global-name "com.apple.CarPlayApp.volume-notification-service")
```
