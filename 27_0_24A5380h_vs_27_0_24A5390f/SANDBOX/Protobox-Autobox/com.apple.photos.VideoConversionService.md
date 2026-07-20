## com.apple.photos.VideoConversionService

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
 		(iokit-registry-entry-class "AGXAccelerator")
 		(iokit-registry-entry-class "AppleJPEGDriver")

 	)
 )
 
+(deny iokit-open-service)
+
 (deny iokit-set-properties)
 
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
 		(require-not (global-name "com.apple.appleneuralengine"))
 		(require-not (global-name "com.apple.coremedia.mediaplaybackd.customurlloader.xpc"))
+		(require-not (global-name "com.apple.symptom_diagnostics"))
 		(require-not (global-name "com.apple.coremedia.mediaparserd.formatreader.xpc"))
 		(require-not (global-name "com.apple.coremedia.mediaplaybackd.assetimagegenerator.xpc"))
 		(require-not (global-name "com.apple.coremedia.videocodecd.compressionsession"))

 	)
 )
 
+(deny process-codesigning)
+
 (deny process-exec*)
 
+(allow process-exec-interpreter)
+
 (deny socket-ioctl)
 
 (deny syscall-unix)

 		SYS_fileport_makefd
 		SYS_memorystatus_control
 		SYS_guarded_open_np
+		SYS_guarded_close_np
 		SYS_guarded_kqueue_np
 		SYS_change_fdguard_np
 		SYS_getattrlistbulk

 		F_GETPATH
 		F_GETPROTECTIONCLASS
 		F_SINGLE_WRITER
+		F_OFD_SETLK
+		F_SETCONFINED
 		F_ADDFILESIGS_RETURN
 		F_CHECK_LV)
 )
```
