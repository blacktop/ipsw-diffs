## demod_helper

> Group: ⬆️ Updated

```diff

 		(iokit-registry-entry-class "${ENTITLEMENT:com.apple.security.exception.iokit-user-client-class}")
 		(iokit-registry-entry-class "${ENTITLEMENT:com.apple.security.iokit-user-client-class}")
 		(iokit-registry-entry-class "AppleAPFSUserClient")
+		(iokit-registry-entry-class "AppleSMCClient")
 	)
 )
 
 (deny iokit-open-service)
 (allow iokit-open-service
-	(iokit-registry-entry-class "AppleAPFSContainer")
+	(require-any
+		(iokit-registry-entry-class "AppleAPFSContainer")
+		(iokit-registry-entry-class "AppleSMCKeysEndpoint")
+	)
 )
 
 (deny iokit-set-properties)
```
