## blastdoor-ids

> Group: ⬆️ Updated

```diff

 )
 (allow file-read*
 	(require-all
-		(require-not (literal "/private/var"))
+		(require-not (literal "/dev"))
 		(require-not (require-any
 			(subpath "/AppleInternal/Library/VideoCodecs")
 			(subpath "/private/xarts")
 			(subpath "/usr/standalone/firmware")
 		))
+		(require-not (subpath "/private/var/MobileSoftwareUpdate"))
 		(require-not (subpath "/private/var/wireless/baseband_data"))
 		(require-not (subpath "/private/var/hardware"))
-		(require-not (literal "/dev"))
-		(require-not (subpath "/private/var/MobileSoftwareUpdate"))
+		(require-not (literal "/private/var"))
 		(require-any
 			(extension "com.apple.sandbox.executable")
-			(literal "/dev/null")
 			(literal "/dev/random")
 			(literal "/dev/urandom")
-			(literal "/dev/zero")
 			(literal "/private/etc/fstab")
 			(literal "/private/etc/hosts")
 			(literal "/private/etc/passwd")

 			(require-all
 				(file-mode #o0004)
 				(require-any
-					(literal "/private/etc/hosts")
+					(require-any
+						(literal "/private/etc/group")
+						(literal "/private/etc/protocols")
+					)
 					(subpath "/System")
 					(subpath "/private/var/db/timezone")
 					(subpath "/usr/lib")

 				(literal "/private/preboot")
 				(process-attribute is-apple-signed-executable)
 			)
+			(require-any
+				(literal "/dev/null")
+				(literal "/dev/zero")
+			)
 			(require-any
 				(literal "/private/etc/group")
 				(literal "/private/etc/protocols")

 			(literal "/private/var/preferences/Logging/com.apple.diagnosticd.filter.plist")
 			(literal "/tmp")
 			(require-all
-				(require-not (literal "/private/var"))
+				(require-not (literal "/dev"))
 				(require-not (require-any
 					(subpath "/AppleInternal/Library/VideoCodecs")
 					(subpath "/private/xarts")
 					(subpath "/usr/standalone/firmware")
 				))
+				(require-not (subpath "/private/var/MobileSoftwareUpdate"))
 				(require-not (subpath "/private/var/wireless/baseband_data"))
 				(require-not (subpath "/private/var/hardware"))
-				(require-not (literal "/dev"))
-				(require-not (subpath "/private/var/MobileSoftwareUpdate"))
+				(require-not (literal "/private/var"))
 				(require-any
 					(extension "com.apple.sandbox.executable")
-					(literal "/dev/null")
 					(literal "/dev/random")
 					(literal "/dev/urandom")
-					(literal "/dev/zero")
 					(literal "/private/etc/fstab")
 					(literal "/private/etc/hosts")
 					(literal "/private/etc/passwd")

 					(require-all
 						(file-mode #o0004)
 						(require-any
-							(literal "/private/etc/hosts")
+							(require-any
+								(literal "/private/etc/group")
+								(literal "/private/etc/protocols")
+							)
 							(subpath "/System")
 							(subpath "/private/var/db/timezone")
 							(subpath "/usr/lib")

 						(literal "/private/preboot")
 						(process-attribute is-apple-signed-executable)
 					)
+					(require-any
+						(literal "/dev/null")
+						(literal "/dev/zero")
+					)
 					(require-any
 						(literal "/private/etc/group")
 						(literal "/private/etc/protocols")

 )
 
 (allow file-write-data
+	(require-any
+		(literal "/dev/null")
+		(literal "/dev/zero")
+	)
+)
+(deny file-write-data
 	(require-all
-		(require-not (literal "/dev/dtracehelper"))
 		(require-any
 			(literal "/dev/null")
 			(literal "/dev/zero")
 		)
+		(literal "/dev/dtracehelper")
 	)
 )
 

 	(with no-report)
 	(require-all
 		(require-not (xpc-service-name "*"))
-		(require-not (global-name "com.apple.powerlog.plxpclogger.xpc"))
+		(require-not (global-name "com.apple.mobilegestalt.xpc"))
 		(require-not (global-name "com.apple.CARenderServer"))
-		(require-not (global-name "com.apple.audio.AudioComponentRegistrar"))
 		(require-not (global-name "com.apple.mobileassetd.v2"))
 		(require-not (global-name "com.apple.coremedia.mediaparserd.utilities"))
+		(require-not (global-name "com.apple.powerlog.plxpclogger.xpc"))
+		(require-not (global-name "com.apple.audio.AudioComponentRegistrar"))
 		(require-not (global-name "com.apple.system.logger"))
-		(require-not (global-name "com.apple.analyticsd"))
-		(global-name "com.apple.mobilegestalt.xpc")
+		(global-name "com.apple.analyticsd")
 	)
 )
 (deny mach-lookup
 	(require-all
 		(require-not (xpc-service-name "*"))
-		(require-not (global-name "com.apple.powerlog.plxpclogger.xpc"))
+		(require-not (global-name "com.apple.mobilegestalt.xpc"))
 		(require-not (global-name "com.apple.CARenderServer"))
-		(require-not (global-name "com.apple.audio.AudioComponentRegistrar"))
 		(require-not (global-name "com.apple.mobileassetd.v2"))
 		(require-not (global-name "com.apple.coremedia.mediaparserd.utilities"))
+		(require-not (global-name "com.apple.powerlog.plxpclogger.xpc"))
+		(require-not (global-name "com.apple.audio.AudioComponentRegistrar"))
 		(require-not (global-name "com.apple.system.logger"))
-		(require-not (global-name "com.apple.analyticsd"))
-		(global-name "com.apple.mobilegestalt.xpc")
+		(global-name "com.apple.analyticsd")
 	)
 )
 

 		(require-any
 			(require-any
 				(sysctl-name "hw.activecpu")
+				(sysctl-name "hw.machine")
+				(sysctl-name "hw.memsize")
 				(sysctl-name "hw.ncpu")
+				(sysctl-name "kern.osproductversion")
 				(sysctl-name "kern.osvariant_status")
 				(sysctl-name "kern.secure_kernel")
 			)

 				(sysctl-name "hw.physicalcpu_max")
 				(sysctl-name "hw.product")
 			)
-			(require-any
-				(sysctl-name "hw.machine")
-				(sysctl-name "kern.osproductversion")
-			)
 			(require-any
 				(sysctl-name "hw.optional.arm.caps")
 				(sysctl-name "hw.optional.neon_fp16")

 				(sysctl-name "kern.maxfilesperproc")
 				(sysctl-name "kern.osversion")
 			)
-			(sysctl-name "hw.memsize")
 			(sysctl-name "hw.osenvironment")
 			(sysctl-name "hw.pagesize_compat")
 			(sysctl-name "hw.physicalcpu")
```
