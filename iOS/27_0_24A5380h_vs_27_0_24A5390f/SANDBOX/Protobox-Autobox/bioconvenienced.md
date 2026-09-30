## bioconvenienced

> Group: ⬆️ Updated

```diff

 	(process-attribute is-autoboxed)
 )
 
-(deny iokit-issue-extension
+(deny iokit-get-properties
 	(with no-report)
 	(process-attribute is-autoboxed)
 )
 
-(deny iokit-open-user-client
+(deny iokit-open*
 	(process-attribute is-autoboxed)
 )
-(allow iokit-open-user-client
+(allow iokit-open*
 	(require-all
 		(process-attribute is-autoboxed)
 		(require-any

 	)
 )
 
+(deny iokit-open-service
+	(with no-report)
+	(process-attribute is-autoboxed)
+)
+
 (deny iokit-set-properties
 	(with no-report)
 	(process-attribute is-autoboxed)

 	(process-attribute is-autoboxed)
 )
 
-(deny ipc-posix-shm-read-data
+(deny ipc-posix-shm*
 	(process-attribute is-autoboxed)
 )
-(allow ipc-posix-shm-read-data
+(allow ipc-posix-shm*
 	(require-all
 		(process-attribute is-autoboxed)
-		(ipc-posix-name "com.apple.featureflags.shm")
+		(require-any
+			(ipc-posix-name "apple.cfprefs.system.daemonv1")
+			(ipc-posix-name "apple.cfprefs.user.daemonv1")
+			(ipc-posix-name "apple.shm.notification_center")
+			(ipc-posix-name "com.apple.featureflags.shm")
+		)
 	)
 )
 
-(deny job-creation
+(deny isp-command-send
+	(with no-report)
+	(process-attribute is-autoboxed)
+)
+
+(deny mach-host-special-port-set
 	(with no-report)
 	(process-attribute is-autoboxed)
 )
 
 (deny mach-issue-extension
-	(with no-report)
-	(process-attribute is-autoboxed)
+	(require-all
+		(require-not (global-name "com.apple.symptom_diagnostics"))
+		(require-not (global-name "com.apple.system.notification_center"))
+		(require-not (global-name "com.apple.mobile.keybagd.UserManager.xpc"))
+		(require-not (global-name "com.apple.mobile.usermanagerd.xpc"))
+		(require-not (global-name "com.apple.perceptiond.api"))
+		(require-not (global-name "com.apple.diagnosticd"))
+		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
+		(require-not (global-name "com.apple.cfprefsd.daemon"))
+		(require-not (global-name "com.apple.logd"))
+		(require-any
+			(process-attribute is-autoboxed)
+			(require-all
+				(system-attribute developer-mode)
+				(process-attribute is-autoboxed)
+				(require-not (global-name "com.apple.dt.testmanagerd.uiprocess"))
+			)
+		)
+	)
 )
 
-(deny mach-lookup
+(deny process-codesigning
+	(with no-report)
 	(process-attribute is-autoboxed)
 )
 
```
