## managedappdistributiond

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
 	(require-any
 		(iokit-registry-entry-class "AppleKeyStore")
 		(iokit-registry-entry-class "AvpFairPlayDriver")

 	)
 )
 
+(deny iokit-open-service)
+
 (deny iokit-set-properties)
 
 (deny ipc*)
 
-(deny ipc-posix-sem-create)
-(allow ipc-posix-sem-create
+(deny ipc-posix-sem*)
+(allow ipc-posix-sem*
 	(ipc-posix-name "installcood.f.7aedbc07119961d2")
 )
 
-(deny ipc-posix-sem-open)
-(allow ipc-posix-sem-open
-	(ipc-posix-name "installcood.f.7aedbc07119961d2")
-)
-
-(deny ipc-posix-shm-read-data)
-(allow ipc-posix-shm-read-data
+(deny ipc-posix-shm*)
+(allow ipc-posix-shm*
 	(require-any
 		(ipc-posix-name "apple.cfprefs.system.daemonv1")
 		(ipc-posix-name "apple.cfprefs.user.daemonv1")

 	)
 )
 
-(deny job-creation)
+(allow ipc-sysv-shm)
 
-(deny mach-issue-extension)
+(deny isp-command-send)
 
-(deny mach-lookup
+(deny mach-host-special-port-set)
+
+(deny mach-issue-extension
 	(require-all
 		(require-not (global-name "com.apple.storekitd"))
 		(require-not (global-name "com.apple.mobilegestalt.xpc"))

 		(require-not (global-name "com.apple.duetactivityscheduler"))
 		(require-not (global-name "com.apple.cdp.daemon"))
 		(require-not (global-name "com.apple.mobile.installd"))
+		(require-not (global-name "com.apple.mobileassetd.v2"))
 		(require-not (global-name "com.apple.lsd.mapdb"))
 		(require-not (global-name "com.apple.trustd"))
 		(require-not (global-name "com.apple.system.notification_center"))

 		(require-not (global-name "com.apple.nehelper"))
 		(require-not (global-name "com.apple.installcoordinationd"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
-		(require-not (global-name "com.apple.AppSSO.service-xpc"))
 		(require-not (global-name "com.apple.containermanagerd"))
 		(require-not (global-name "com.apple.runningboard"))
 		(require-not (global-name "com.apple.fairplayd.xpc"))

 		(require-any
 			(require-all
 				(global-name "com.apple.dt.testmanagerd.uiprocess")
+				(require-not (global-name "com.apple.AppSSO.service-xpc"))
 				(require-not (global-name "com.apple.AppDistributionLaunchAngel"))
 				(require-not (system-attribute developer-mode))
 			)

 				(xpc-service-name "*")
 				(global-name "com.apple.dt.testmanagerd.uiprocess")
 				(require-not (extension "com.apple.pluginkit.plugin-service"))
+				(require-not (global-name "com.apple.AppSSO.service-xpc"))
 				(require-not (global-name "com.apple.AppDistributionLaunchAngel"))
 				(require-not (system-attribute developer-mode))
 			)

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

 		SYS_clonefileat
 		SYS_openat
 		SYS_openat_nocancel
+		SYS_renameat
 		SYS_faccessat
 		SYS_fstatat
 		SYS_fstatat64
```
