## container

> Group: ⬆️ Updated

```diff

 		(iokit-registry-entry-class "IOHIDLibUserClient")
 	)
 )
+(allow iokit-open-user-client
+	(require-all
+		(process-attribute is-platform-binary)
+		(iokit-registry-entry-class "IOHIDEventServiceFastPathUserClient")
+	)
+)
 (allow iokit-open-user-client
 	(require-all
 		(system-attribute virtual-device)
```
