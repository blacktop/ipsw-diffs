## inboxupdaterd

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
 		(iokit-registry-entry-class "AppleMobileApNonce")

 	)
 )
 
-(deny iokit-set-properties
+(deny iokit-open-service
 	(require-any
 		(require-not (iokit-property "IOPMUBootLPMCtrl"))
 		(require-not (iokit-registry-entry-class "AppleDialogSPMIPMU"))
 	)
 )
 
+(deny iokit-set-properties)
+
 (deny ipc*)
 
-(deny ipc-posix-shm-read-data)
-(allow ipc-posix-shm-read-data
+(deny ipc-posix-shm*)
+(allow ipc-posix-shm*
 	(require-any
 		(ipc-posix-name "apple.cfprefs.daemonv1")
 		(ipc-posix-name "apple.cfprefs.system.daemonv1")

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
 		(require-not (global-name "com.apple.mobilegestalt.xpc"))

 	)
 )
 
+(deny process-codesigning
+	(require-all
+		(require-not (literal "/usr/sbin/tcpdump"))
+		(require-any
+			(require-all
+				(require-not (literal "/usr/local/bin/smcif"))
+				(require-not (literal "/usr/local/bin/apple80211"))
+				(require-not (literal "/AppleInternal/Library/Frameworks/Python.framework/Versions/3.9/bin/python3.9"))
+			)
+			(require-not (system-attribute internal-build))
+		)
+	)
+)
+
 (deny process-exec*
 	(require-all
 		(require-not (literal "/usr/sbin/tcpdump"))

 		SYS_fsgetpath
 		SYS_fileport_makefd
 		SYS_memorystatus_control
+		SYS_guarded_open_np
 		SYS_guarded_close_np
 		SYS_guarded_kqueue_np
 		SYS_change_fdguard_np

 		F_SETPROTECTIONCLASS
 		F_SINGLE_WRITER
 		F_OFD_SETLK
+		F_OFD_GETLK
+		F_OFD_SETLKWTIMEOUT
 		F_SETCONFINED
 		F_GETCONFINED
 		F_ADDFILESIGS_RETURN
```
