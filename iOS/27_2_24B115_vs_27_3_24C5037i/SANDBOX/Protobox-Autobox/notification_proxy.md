## notification_proxy

> Group: ⬆️ Updated

```diff

 	(require-any
 		(iokit-registry-entry-class "${ENTITLEMENT:com.apple.security.exception.iokit-user-client-class}")
 		(iokit-registry-entry-class "${ENTITLEMENT:com.apple.security.iokit-user-client-class}")
+		(iokit-registry-entry-class "AppleCredentialManagerUserClient")
 		(iokit-registry-entry-class "AppleKeyStoreUserClient")
 	)
 )
 
 (deny iokit-open-service)
 (allow iokit-open-service
-	(iokit-registry-entry-class "AppleKeyStore")
+	(require-any
+		(iokit-registry-entry-class "AppleCredentialManager")
+		(iokit-registry-entry-class "AppleKeyStore")
+	)
 )
 
 (deny iokit-set-properties)

 		io_service_open_extended
 		io_connect_method
 		io_server_version
+		io_service_get_matching_service_bin
 		mach_port_request_notification
 		mach_port_set_attributes
 		mach_port_get_context_from_user

 
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
