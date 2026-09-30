## sysdiagnosed

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
 
-(deny process-exec*
+(deny process-codesigning
 	(require-all
 		(require-not (literal "/System/Library/PrivateFrameworks/IOSurfaceAccelerator.framework/Resources/IOSADiagnose"))
 		(require-any

 				))
 				(require-not (literal "/usr/bin/sw_vers"))
 				(require-not (literal "/bin/echo"))
+				(require-not (literal "/usr/sbin/sysctl"))
 				(require-not (literal "/usr/bin/fileproviderctl"))
 				(require-not (literal "/System/Library/Frameworks/SystemConfiguration.framework/get-network-info"))
 				(require-not (literal "/bin/bash"))

 			(require-all
 				(system-attribute internal-build)
 				(require-not (literal "/usr/local/bin/ddt"))
-				(require-not (literal "/usr/local/bin/jetsam_priority"))
-				(require-not (literal "/usr/local/bin/darwinup"))
-				(require-not (require-any
-					(literal "/usr/local/bin/amstool")
-					(literal "/usr/local/bin/homeutil")
-				))
-				(require-not (literal "/usr/local/bin/CADebug"))
 				(require-not (require-any
 					(literal "/usr/appleinternal/bin/ACMTool")
 					(literal "/usr/appleinternal/bin/CiderCLI")

 					(literal "/usr/local/bin/apsclient")
 					(literal "/usr/local/bin/arkitctl")
 					(literal "/usr/local/bin/asclient")
-					(literal "/usr/local/bin/assistant_tool")
 					(literal "/usr/local/bin/audioDeviceDump")
 					(literal "/usr/local/bin/benchrun")
 					(literal "/usr/local/bin/c26tool")

 					(literal "/usr/local/bin/clpcctrl")
 					(literal "/usr/local/bin/clpctop")
 					(literal "/usr/local/bin/controlbits")
-					(literal "/usr/local/bin/csfctl")
 					(literal "/usr/local/bin/ctsctl")
 					(literal "/usr/local/bin/dastool")
 					(literal "/usr/local/bin/diagpipectl")

 					(literal "/usr/local/bin/zeolitectl")
 					(literal "/usr/local/libexec/hidrecorderd.internal")
 				))
+				(require-not (literal "/usr/local/bin/jetsam_priority"))
+				(require-not (literal "/usr/local/bin/darwinup"))
+				(require-not (literal "/usr/local/bin/CADebug"))
+				(require-not (require-any
+					(literal "/usr/local/bin/amstool")
+					(literal "/usr/local/bin/assistant_tool")
+					(literal "/usr/local/bin/csfctl")
+					(literal "/usr/local/bin/homeutil")
+				))
 				(require-not (literal "/usr/local/bin/profilectl"))
 				(require-not (literal "/bin/ls"))
 				(require-not (require-any

 				))
 				(require-not (literal "/usr/bin/sw_vers"))
 				(require-not (literal "/bin/echo"))
+				(require-not (literal "/usr/sbin/sysctl"))
 				(require-not (literal "/usr/bin/fileproviderctl"))
 				(require-not (literal "/System/Library/Frameworks/SystemConfiguration.framework/get-network-info"))
 				(require-not (literal "/bin/bash"))

 	)
 )
 
-(deny process-exec-interpreter
+(deny process-exec*
 	(require-all
 		(require-not (literal "/bin/zsh"))
 		(require-not (literal "/bin/sh"))

 				))
 				(require-not (literal "/usr/bin/sw_vers"))
 				(require-not (literal "/bin/echo"))
+				(require-not (literal "/usr/sbin/sysctl"))
 				(require-not (literal "/usr/bin/fileproviderctl"))
 				(require-not (literal "/System/Library/Frameworks/SystemConfiguration.framework/get-network-info"))
 				(require-not (literal "/bin/bash"))

 			(require-all
 				(system-attribute internal-build)
 				(require-not (literal "/usr/local/bin/ddt"))
-				(require-not (literal "/usr/local/bin/jetsam_priority"))
-				(require-not (literal "/usr/local/bin/darwinup"))
-				(require-not (require-any
-					(literal "/usr/local/bin/amstool")
-					(literal "/usr/local/bin/homeutil")
-				))
-				(require-not (literal "/usr/local/bin/CADebug"))
 				(require-not (require-any
 					(literal "/usr/appleinternal/bin/ACMTool")
 					(literal "/usr/appleinternal/bin/CiderCLI")

 					(literal "/usr/local/bin/apsclient")
 					(literal "/usr/local/bin/arkitctl")
 					(literal "/usr/local/bin/asclient")
-					(literal "/usr/local/bin/assistant_tool")
 					(literal "/usr/local/bin/audioDeviceDump")
 					(literal "/usr/local/bin/benchrun")
 					(literal "/usr/local/bin/c26tool")

 					(literal "/usr/local/bin/clpcctrl")
 					(literal "/usr/local/bin/clpctop")
 					(literal "/usr/local/bin/controlbits")
-					(literal "/usr/local/bin/csfctl")
 					(literal "/usr/local/bin/ctsctl")
 					(literal "/usr/local/bin/dastool")
 					(literal "/usr/local/bin/diagpipectl")

 					(literal "/usr/local/bin/zeolitectl")
 					(literal "/usr/local/libexec/hidrecorderd.internal")
 				))
+				(require-not (literal "/usr/local/bin/jetsam_priority"))
+				(require-not (literal "/usr/local/bin/darwinup"))
+				(require-not (literal "/usr/local/bin/CADebug"))
+				(require-not (require-any
+					(literal "/usr/local/bin/amstool")
+					(literal "/usr/local/bin/assistant_tool")
+					(literal "/usr/local/bin/csfctl")
+					(literal "/usr/local/bin/homeutil")
+				))
 				(require-not (literal "/usr/local/bin/profilectl"))
 				(require-not (literal "/bin/ls"))
 				(require-not (require-any

 				))
 				(require-not (literal "/usr/bin/sw_vers"))
 				(require-not (literal "/bin/echo"))
+				(require-not (literal "/usr/sbin/sysctl"))
 				(require-not (literal "/usr/bin/fileproviderctl"))
 				(require-not (literal "/System/Library/Frameworks/SystemConfiguration.framework/get-network-info"))
 				(require-not (literal "/bin/bash"))

 		SYS_clonefileat
 		SYS_openat
 		SYS_openat_nocancel
+		SYS_renameat
 		SYS_faccessat
 		SYS_fstatat
 		SYS_fstatat64
```
