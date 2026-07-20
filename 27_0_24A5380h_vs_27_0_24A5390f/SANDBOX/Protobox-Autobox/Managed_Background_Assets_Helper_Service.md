## Managed Background Assets Helper Service

> Group: ⬆️ Updated

```diff

 
 (deny generic-issue-extension)
 
-(deny iokit-issue-extension)
+(deny iokit-get-properties)
 
-(deny iokit-open-user-client)
-(allow iokit-open-user-client
+(deny iokit-open*)
+(allow iokit-open*
 	(require-any
 		(iokit-registry-entry-class "${ENTITLEMENT:com.apple.security.exception.iokit-user-client-class}")
 		(iokit-registry-entry-class "${ENTITLEMENT:com.apple.security.iokit-user-client-class}")
 	)
 )
 
-(deny iokit-open-service)
-(allow iokit-open-service
+(deny iokit-open-user-client)
+(allow iokit-open-user-client
 	(iokit-registry-entry-class "AppleKeyStore")
 )
 
+(deny iokit-open-service)
+
 (deny iokit-set-properties)
 
 (deny ipc*)
 
-(deny job-creation)
+(allow ipc-sysv-shm)
 
-(deny mach-issue-extension)
+(deny isp-command-send)
 
-(deny mach-lookup
+(deny mach-host-special-port-set)
+
+(deny mach-issue-extension
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
 		(require-not (global-name "com.apple.symptom_diagnostics"))
 		(require-not (global-name "com.apple.mobile.keybagd.UserManager.xpc"))
+		(require-not (global-name "com.apple.userprofiles"))
 		(require-not (global-name "com.apple.appstored.xpc"))
 		(require-not (global-name "com.apple.fairplayd.versioned"))
 		(require-not (global-name "com.apple.symptom_analytics"))

 	)
 )
 
+(deny process-codesigning)
+
 (deny process-exec*)
 
+(allow process-exec-interpreter)
+
 (deny socket-ioctl)
 (allow socket-ioctl
 	(ioctl-command

 			SYS_flock
 			SYS_sendto
 			SYS_shutdown
+			SYS_socketpair
 			SYS_mkdir
 			SYS_rmdir
 			SYS_pread
```
