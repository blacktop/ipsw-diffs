## assessmentagent

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
 
+(deny iokit-open-user-client)
+
 (deny iokit-open-service)
 
 (deny iokit-set-properties)
 
 (deny ipc*)
 
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
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
+		(require-not (global-name "com.apple.accessibility.AXBackBoardServer"))
 		(require-not (global-name "com.apple.lsd.mapdb"))
 		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (global-name "com.apple.frontboard.systemappservices"))
 		(require-not (global-name "com.apple.mobile.keybagd.UserManager.xpc"))
-		(require-not (global-name "com.apple.siri.assessment-mode-restriction"))
+		(require-not (global-name "com.apple.SBUserNotification"))
+		(require-not (require-any
+			(global-name "com.apple.DeviceConfigurationAgent.provider.async")
+			(global-name "com.apple.siri.assessment-mode-restriction")
+		))
 		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3"))
 		(require-not (global-name "com.apple.coremedia.routingcontext.xpc"))

 		(require-not (global-name "com.apple.nehelper"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (global-name "com.apple.mediaremoted.xpc"))
+		(require-not (global-name "com.apple.nesessionmanager.flow-divert-token"))
 		(require-not (global-name "com.apple.runningboard"))
 		(require-not (global-name "com.apple.managedconfiguration.profiled"))
 		(require-not (global-name "com.apple.cfprefsd.daemon"))

 		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (global-name "com.apple.coremedia.volumecontroller.xpc"))
-		(require-not (global-name "com.apple.nesessionmanager.flow-divert-token"))
-		(require-not (global-name "com.apple.accessibility.AXBackBoardServer"))
-		(require-not (global-name "com.apple.SBUserNotification"))
 		(require-not (system-attribute developer-mode))
 	)
 )
 
+(deny process-codesigning)
+
 (deny process-exec*)
 
+(allow process-exec-interpreter)
+
 (deny socket-ioctl)
 
 (deny syscall-unix)

 		SYS_lseek
 		SYS_sysctl
 		SYS_getumask
+		SYS_open_dprotected_np
 		SYS_getattrlist
 		SYS_listxattr
 		SYS_fsctl

 
 (deny system-fcntl)
 (allow system-fcntl
-	(fcntl-command F_SETFD F_GETFL F_GETPATH F_ADDFILESIGS_RETURN F_CHECK_LV)
+	(fcntl-command
+		F_SETFD
+		F_GETFL
+		F_GETPATH
+		F_SETPROTECTIONCLASS
+		F_ADDFILESIGS_RETURN
+		F_CHECK_LV)
 )
 
 (deny system-fsctl)
```
