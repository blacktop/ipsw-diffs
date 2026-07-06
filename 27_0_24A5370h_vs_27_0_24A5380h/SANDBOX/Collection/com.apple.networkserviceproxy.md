## com.apple.networkserviceproxy

> Group: ⬆️ Updated

```diff

 (allow system-privilege)
 
 (allow system-socket
-	(socket-domain 39 AF_ROUTE AF_SYSTEM)
+	(socket-domain AF_ROUTE AF_SYSTEM 39)
 )
 
 (allow user-preference-read
```
