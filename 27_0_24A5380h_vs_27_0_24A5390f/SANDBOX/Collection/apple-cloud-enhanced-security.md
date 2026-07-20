## apple-cloud-enhanced-security

> Group: ⬆️ Updated

```diff

 
 (allow fs-info)
 
-(allow iokit-get-properties
+(allow iokit*
 	(require-all
 		(iokit-property "iommu-present")
 		(iokit-registry-entry-class "IOPlatformDevice")
 	)
 )
-(allow iokit-get-properties
+(allow iokit*
 	(require-all
 		(iokit-property "platform-name")
 		(iokit-registry-entry-class "IOPlatformExpertDevice")
 	)
 )
-(allow iokit-get-properties
+(allow iokit*
 	(require-all
 		(iokit-property "product-id")
 		(iokit-registry-entry-class "IOPlatformDevice")
 	)
 )
-(allow iokit-get-properties
+(allow iokit*
 	(require-all
 		(iokit-property "soc-generation")
 		(iokit-registry-entry-class "IOPlatformDevice")
 	)
 )
-(allow iokit-get-properties
+(allow iokit*
 	(require-all
 		(require-any
 			(iokit-property "artwork-device-idiom")

 	)
 )
 
-(allow iokit-open-user-client
+(allow iokit-open*
 	(extension "com.apple.security.exception.iokit-user-client-class")
 )
-(deny iokit-open-user-client
+(deny iokit-open*
 	(with no-report)
 )
 
-(allow iokit-open-service
+(allow iokit-open-user-client
 	(%entitlement-is-present "com.apple.security.exception.iokit-user-client-class")
 )
 
-(allow ipc-posix-shm-read-data
+(allow ipc-posix-shm*
 	(ipc-posix-name "apple.shm.notification_center")
 )
 
-(allow isp-command-send)
+(allow ipc-sysv-shm)
 
-(deny job-creation)
+(deny isp-command-send)
 
-(deny lsopen
+(deny job-creation
 	(profile-flag "deny-lsopen")
 )
 
-(allow mach-derive-port)
+(allow mach-cross-domain-lookup)
 
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-any
 		(extension "com.apple.security.exception.mach-lookup.global-name")
 		(extension "com.apple.security.exception.mach-lookup.local-name")

 		(global-name "com.apple.system.notification_center")
 	)
 )
-(deny mach-lookup
+(deny mach-issue-extension
 	(with no-report)
 	(require-any
 		(global-name "com.apple.CARenderServer")

 		(global-name "com.apple.system.logger")
 	)
 )
-(deny mach-lookup
+(deny mach-issue-extension
 	(xpc-service-name "*")
 )
 
-(allow mach-register
+(allow mach-priv-task-port
 	(extension "com.apple.security.exception.mach-register.global-name")
 )
 
-(allow mach-task-exception-port-set)
+(allow mach-task*)
+
+(allow mach-task-exception-port-set
+	(target self)
+)
 
 (allow mach-task-inspect
 	(target self)

 	(target self)
 )
 
-(allow mach-task-read
+(deny mach-task-read)
+
+(allow mach-task-special-port*
 	(target self)
 )
-
 (deny mach-task-special-port*)
 
-(allow mach-task-special-port-get
-	(target self)
-)
 (deny mach-task-special-port-get)
 
-(deny necp-client-open)
+(deny mach-task-special-port-set)
 
-(deny network-outbound
+(deny network-bind
 	(with no-report)
 	(literal "/private/var/run/syslog")
 )
 
-(allow process-codesigning)
+(allow process*)
 
-(allow process-info-codesignature)
-
-(allow process-info-dirtycontrol
+(allow process-info-codesignature
 	(target self)
 )
 
-(allow process-info-pidinfo
+(allow process-info-listpids
 	(target self)
 )
 
-(allow process-info-setcontrol
+(allow process-info-sandbox-container
 	(target self)
 )
 
-(allow process-iopolicy*)
-
-(allow process-legacy-codesigning-blob-get)
-
-(allow process-legacy-codesigning-cdhash-get)
-
-(allow process-legacy-codesigning-entitlements-blob-get)
-
-(allow process-legacy-codesigning-entitlements-der-blob-get)
-
-(allow process-legacy-codesigning-identity-get)
-
-(allow process-legacy-codesigning-status-get)
-
-(allow process-legacy-codesigning-status-set)
-
-(allow process-legacy-codesigning-teamid-get)
-
-(allow process-legacy-codesigning-text-offset-get)
-
 (allow sandbox-check)
 
 (allow signal

 		SYS_readlink
 		SYS_removexattr
 		SYS_rename
+		SYS_renameat
+		SYS_renameatx_np
 		SYS_setrlimit
 		SYS_setxattr
 		SYS_shared_region_check_np

 )
 
 (allow exception-entitlement)
-
-(allow process-exec-update-label)
```
