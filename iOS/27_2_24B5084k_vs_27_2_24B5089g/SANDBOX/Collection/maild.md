## maild

> Group: ⬆️ Updated

```diff

 		(iokit-registry-entry-class "IOHIDEventServiceFastPathUserClient")
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
 		(process-attribute is-apple-signed-executable)
```
