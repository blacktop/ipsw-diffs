## appstorecomponentsd

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
-	(iokit-registry-entry-class "IOMobileFramebufferShim")
+(deny iokit-open-user-client)
+(allow iokit-open-user-client
+	(require-any
+		(iokit-registry-entry-class "AppleKeyStore")
+		(iokit-registry-entry-class "IOMobileFramebufferShim")
+	)
 )
 
+(deny iokit-open-service)
+
 (deny iokit-set-properties)
 
 (deny ipc*)
 
-(deny job-creation)
+(deny ipc-posix-shm*)
+(allow ipc-posix-shm*
+	(require-any
+		(ipc-posix-name "apple.cfprefs.system.daemonv1")
+		(ipc-posix-name "apple.cfprefs.user.daemonv1")
+	)
+)
 
-(deny mach-issue-extension)
+(allow ipc-sysv-shm)
 
-(deny mach-lookup
+(deny isp-command-send)
+
+(deny mach-host-special-port-set)
+
+(deny mach-issue-extension
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
 		(require-not (global-name "com.apple.storekitd"))

 		(require-not (global-name "com.apple.ap.promotedcontent.metrics"))
 		(require-not (global-name "com.apple.lsd.mapdb"))
 		(require-not (global-name "com.apple.ak.auth.xpc"))
+		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (global-name "com.apple.lsd.xpc"))
 		(require-not (global-name "com.apple.TapToRadarKit.service"))
+		(require-not (global-name "com.apple.accountsd.accountmanager"))
 		(require-not (global-name "com.apple.SBUserNotification"))
 		(require-not (global-name "com.apple.geod"))
 		(require-not (global-name "com.apple.commcenter.coretelephony.xpc"))

 		(require-not (global-name "com.apple.distributed_notifications@1v3"))
 		(require-not (global-name "com.apple.symptom_analytics"))
 		(require-not (global-name "com.apple.carousel.connectionstatusservice"))
+		(require-not (global-name "com.apple.nehelper"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (global-name "com.apple.runningboard"))
 		(require-not (global-name "com.apple.locationd.registration"))
+		(require-not (global-name "com.apple.dnssd.service"))
+		(require-not (global-name "com.apple.FileCoordination"))
 		(require-not (global-name "com.apple.adid"))
 		(require-not (global-name "com.apple.servicesanalytics.xpc"))
 		(require-not (global-name "com.apple.fairplaydeviceidentityd"))

 		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (global-name "com.apple.lsd.open"))
 		(require-not (xpc-service-name "com.apple.JetTracingSupport.JetTracingService"))
-		(require-not (global-name "com.apple.FileCoordination"))
+		(require-not (global-name "com.apple.AppSSO.service-xpc"))
 		(require-not (global-name "com.apple.AppDistributionLaunchAngel"))
 		(require-not (system-attribute developer-mode))
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

 		SYS_getattrlistbulk
 		SYS_openat
 		SYS_openat_nocancel
+		SYS_renameat
 		SYS_faccessat
 		SYS_fstatat
 		SYS_fstatat64
```
