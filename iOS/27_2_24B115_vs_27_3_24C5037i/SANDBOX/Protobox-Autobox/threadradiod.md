## threadradiod

> Group: ⬆️ Updated

```diff

 
 (deny iokit-open-service)
 (allow iokit-open-service
-	(iokit-registry-entry-class "IOUserService")
+	(require-any
+		(iokit-registry-entry-class "AppleFillmoreDevice")
+		(iokit-registry-entry-class "IOUserService")
+	)
 )
 
 (deny iokit-set-properties)

 
 (deny system-kas-info)
 
+(deny system-mac-syscall
+	(require-all
+		(mac-syscall-number 96)
+		(require-not (mac-policy-name "AMFI"))
+	)
+)
 (with-filter (mac-policy-name "Sandbox")
 	(deny system-mac-syscall
 		(require-all
```
