## sysdiagnosed

> Group: ⬆️ Updated

```diff

 		))
 		(require-not (global-name "com.apple.logd.admin"))
 		(require-not (global-name "com.apple.usymptomsd"))
+		(require-not (global-name "com.apple.PowerManagement.control"))
 		(require-not (xpc-service-name "com.apple.ImageIOXPCService"))
 		(require-not (global-name "com.apple.diagd"))
 		(require-not (global-name "com.apple.springboard.statusbarservices"))

 		(require-not (global-name "com.apple.identityservicesd.embedded.auth"))
 		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (global-name "com.apple.lsd.open"))
-		(require-not (global-name "com.apple.PowerManagement.control"))
 		(require-not (global-name "com.apple.FileProvider"))
 		(require-not (global-name "com.apple.FileCoordination"))
 		(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))

 				(require-not (literal "/bin/ls"))
 				(require-not (require-any
 					(literal "/bin/sleep")
+					(literal "/usr/bin/uptime")
 					(literal "/usr/sbin/nvram")
 				))
 				(require-not (literal "/usr/bin/sw_vers"))

 			(require-all
 				(system-attribute internal-build)
 				(require-not (literal "/usr/local/bin/ddt"))
+				(require-not (require-any
+					(literal "/usr/local/bin/amstool")
+					(literal "/usr/local/bin/assistant_tool")
+					(literal "/usr/local/bin/csfctl")
+					(literal "/usr/local/bin/homeutil")
+					(literal "/usr/local/bin/iftool")
+					(literal "/usr/local/bin/imtool")
+					(literal "/usr/local/bin/switchcl")
+				))
+				(require-not (literal "/usr/local/bin/jetsam_priority"))
 				(require-not (require-any
 					(literal "/usr/appleinternal/bin/ACMTool")
 					(literal "/usr/appleinternal/bin/CiderCLI")

 					(literal "/usr/local/bin/hidreport")
 					(literal "/usr/local/bin/hidutil_internal")
 					(literal "/usr/local/bin/idstool")
-					(literal "/usr/local/bin/iftool")
-					(literal "/usr/local/bin/imtool")
 					(literal "/usr/local/bin/iopsutil")
 					(literal "/usr/local/bin/iordump")
 					(literal "/usr/local/bin/kcsharingdiagnose.py")

 					(literal "/usr/local/bin/sirianalytics_tool")
 					(literal "/usr/local/bin/skdump")
 					(literal "/usr/local/bin/spuctl")
-					(literal "/usr/local/bin/switchcl")
 					(literal "/usr/local/bin/sysconfig")
 					(literal "/usr/local/bin/testIOMFBGPO")
 					(literal "/usr/local/bin/usbctl")

 					(literal "/usr/local/bin/zeolitectl")
 					(literal "/usr/local/libexec/hidrecorderd.internal")
 				))
-				(require-not (literal "/usr/local/bin/jetsam_priority"))
 				(require-not (literal "/usr/local/bin/darwinup"))
 				(require-not (literal "/usr/local/bin/CADebug"))
-				(require-not (require-any
-					(literal "/usr/local/bin/amstool")
-					(literal "/usr/local/bin/assistant_tool")
-					(literal "/usr/local/bin/csfctl")
-					(literal "/usr/local/bin/homeutil")
-				))
 				(require-not (literal "/usr/local/bin/profilectl"))
 				(require-not (literal "/bin/ls"))
 				(require-not (require-any
 					(literal "/bin/sleep")
+					(literal "/usr/bin/uptime")
 					(literal "/usr/sbin/nvram")
 				))
 				(require-not (literal "/usr/bin/sw_vers"))

 				(require-not (literal "/bin/ls"))
 				(require-not (require-any
 					(literal "/bin/sleep")
+					(literal "/usr/bin/uptime")
 					(literal "/usr/sbin/nvram")
 				))
 				(require-not (literal "/usr/bin/sw_vers"))

 			(require-all
 				(system-attribute internal-build)
 				(require-not (literal "/usr/local/bin/ddt"))
+				(require-not (require-any
+					(literal "/usr/local/bin/amstool")
+					(literal "/usr/local/bin/assistant_tool")
+					(literal "/usr/local/bin/csfctl")
+					(literal "/usr/local/bin/homeutil")
+					(literal "/usr/local/bin/iftool")
+					(literal "/usr/local/bin/imtool")
+					(literal "/usr/local/bin/switchcl")
+				))
+				(require-not (literal "/usr/local/bin/jetsam_priority"))
 				(require-not (require-any
 					(literal "/usr/appleinternal/bin/ACMTool")
 					(literal "/usr/appleinternal/bin/CiderCLI")

 					(literal "/usr/local/bin/hidreport")
 					(literal "/usr/local/bin/hidutil_internal")
 					(literal "/usr/local/bin/idstool")
-					(literal "/usr/local/bin/iftool")
-					(literal "/usr/local/bin/imtool")
 					(literal "/usr/local/bin/iopsutil")
 					(literal "/usr/local/bin/iordump")
 					(literal "/usr/local/bin/kcsharingdiagnose.py")

 					(literal "/usr/local/bin/sirianalytics_tool")
 					(literal "/usr/local/bin/skdump")
 					(literal "/usr/local/bin/spuctl")
-					(literal "/usr/local/bin/switchcl")
 					(literal "/usr/local/bin/sysconfig")
 					(literal "/usr/local/bin/testIOMFBGPO")
 					(literal "/usr/local/bin/usbctl")

 					(literal "/usr/local/bin/zeolitectl")
 					(literal "/usr/local/libexec/hidrecorderd.internal")
 				))
-				(require-not (literal "/usr/local/bin/jetsam_priority"))
 				(require-not (literal "/usr/local/bin/darwinup"))
 				(require-not (literal "/usr/local/bin/CADebug"))
-				(require-not (require-any
-					(literal "/usr/local/bin/amstool")
-					(literal "/usr/local/bin/assistant_tool")
-					(literal "/usr/local/bin/csfctl")
-					(literal "/usr/local/bin/homeutil")
-				))
 				(require-not (literal "/usr/local/bin/profilectl"))
 				(require-not (literal "/bin/ls"))
 				(require-not (require-any
 					(literal "/bin/sleep")
+					(literal "/usr/bin/uptime")
 					(literal "/usr/sbin/nvram")
 				))
 				(require-not (literal "/usr/bin/sw_vers"))
```
