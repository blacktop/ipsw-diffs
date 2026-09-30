## SecureMessagingAgent

> Group: ⬆️ Updated

```diff

 				(socket-option-name SO_REUSEADDR)
 				(%entitlement-is-bool-true "com.apple.security.network.server")
 			)
+			(require-all
+				(socket-option-name SO_REUSEPORT)
+				(%entitlement-is-bool-true "com.apple.security.network.server")
+			)
 			(socket-option-name SO_NOSIGPIPE)
 		)
 	)
```
