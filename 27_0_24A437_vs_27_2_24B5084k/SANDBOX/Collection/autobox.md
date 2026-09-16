## autobox

> Group: ⬆️ Updated

```diff

 			)
 			(require-all
 				(socket-option-name SO_REUSEADDR)
+				(%entitlement-is-bool-true "com.apple.security.network.server")
+			)
+			(require-all
+				(socket-option-name SO_REUSEPORT)
 				(require-any
 					(%entitlement-is-bool-true "com.apple.security.network.client")
 					(%entitlement-is-bool-true "com.apple.security.network.server")
```
