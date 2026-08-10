## idcredd

> Group: ⬆️ Updated

```diff

 		(iokit-registry-entry-class "${ENTITLEMENT:com.apple.security.exception.iokit-user-client-class}")
 		(iokit-registry-entry-class "${ENTITLEMENT:com.apple.security.iokit-user-client-class}")
 		(iokit-registry-entry-class "AppleIDVUserClient")
+		(iokit-registry-entry-class "AppleKeyStoreUserClient")
 	)
 )
 

 		(require-not (global-name "com.apple.trustd"))
 		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (global-name "com.apple.tccd"))
+		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.mobileactivationd"))
 		(require-not (global-name "com.apple.system.libinfo.muser"))
 		(require-not (global-name "com.apple.timed.xpc"))
+		(require-not (global-name "com.apple.ctkd.token-client"))
+		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (global-name "com.apple.nfcd.hwmanager"))
+		(require-not (global-name "com.apple.dnssd.service"))
+		(require-not (global-name "com.apple.usymptomsd"))
+		(require-not (global-name "com.apple.diagd"))
 		(require-not (global-name "com.apple.seld.tsmmanager"))
 		(require-not (global-name "com.apple.securityd"))
 		(require-not (global-name "com.apple.logd.events"))
+		(require-not (global-name "com.apple.cfprefsd.daemon"))
+		(require-not (global-name "com.apple.NPKCompanionAgent.library"))
 		(require-not (global-name "com.apple.system.logger"))
 		(require-not (global-name "com.apple.logd"))
-		(require-not (global-name "com.apple.diagnosticd"))
-		(require-not (global-name "com.apple.diagd"))
-		(require-not (global-name "com.apple.ctkd.token-client"))
-		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
-		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (global-name "com.apple.CoreAuthentication.daemon"))
+		(require-not (global-name "com.apple.AppSSO.service-xpc"))
 		(require-not (system-attribute developer-mode))
 	)
 )

 		io_service_open_extended
 		io_connect_method
 		io_server_version
+		io_service_get_matching_service_bin
 		io_service_get_matching_services_bin
 		io_registry_entry_get_property_bin_buf
 		mach_port_request_notification

 (deny system-fcntl)
 (allow system-fcntl
 	(fcntl-command
+		F_GETFD
 		F_SETFD
 		F_GETFL
 		F_NOCACHE

 		NECP_CLIENT_ACTION_COPY_AGENT
 		NECP_CLIENT_ACTION_COPY_INTERFACE
 		NECP_CLIENT_ACTION_COPY_RESULT
-		NECP_CLIENT_ACTION_COPY_UPDATED_RESULT)
+		NECP_CLIENT_ACTION_COPY_UPDATED_RESULT
+		NECP_CLIENT_ACTION_REMOVE)
 )
 
 (allow process-exec-update-label)
```
