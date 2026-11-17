## sysdiagnosed

> Group: ⬆️ Updated

```diff

 				(require-not (literal "/System/Library/Frameworks/SystemConfiguration.framework/get-network-info"))
 				(require-not (literal "/bin/bash"))
 				(require-not (literal "/usr/sbin/kextstat"))
+				(require-not (require-any
+					(literal "/bin/df")
+					(literal "/bin/ps")
+					(literal "/usr/libexec/remotectl")
+				))
 				(require-not (require-any
 					(literal "/usr/sbin/lsof")
 					(literal "/usr/sbin/spindump")

 					(literal "/usr/local/bin/aopvtctl")
 					(literal "/usr/local/bin/apsclient")
 					(literal "/usr/local/bin/arkitctl")
-					(literal "/usr/local/bin/asclient")
 					(literal "/usr/local/bin/assistant_tool")
 					(literal "/usr/local/bin/audioDeviceDump")
 					(literal "/usr/local/bin/benchrun")

 					(literal "/usr/local/bin/findmydevicetool")
 					(literal "/usr/local/bin/fmltool")
 					(literal "/usr/local/bin/freezerctl")
-					(literal "/usr/local/bin/gmstool")
 					(literal "/usr/local/bin/hidreport")
 					(literal "/usr/local/bin/hidutil_internal")
 					(literal "/usr/local/bin/homepodsettingstool")
 					(literal "/usr/local/bin/homeutil")
 					(literal "/usr/local/bin/idstool")
-					(literal "/usr/local/bin/iftool")
 					(literal "/usr/local/bin/imtool")
 					(literal "/usr/local/bin/iopsutil")
 					(literal "/usr/local/bin/iordump")

 				))
 				(require-not (literal "/usr/local/bin/darwinup"))
 				(require-not (literal "/usr/local/bin/CADebug"))
+				(require-not (require-any
+					(literal "/usr/local/bin/asclient")
+					(literal "/usr/local/bin/gmstool")
+					(literal "/usr/local/bin/iftool")
+				))
 				(require-not (literal "/bin/ls"))
 				(require-not (literal "/bin/echo"))
 				(require-not (literal "/usr/sbin/sysctl"))

 				(require-not (literal "/System/Library/Frameworks/SystemConfiguration.framework/get-network-info"))
 				(require-not (literal "/bin/bash"))
 				(require-not (literal "/usr/sbin/kextstat"))
+				(require-not (require-any
+					(literal "/bin/df")
+					(literal "/bin/ps")
+					(literal "/usr/libexec/remotectl")
+				))
 				(require-not (require-any
 					(literal "/usr/sbin/lsof")
 					(literal "/usr/sbin/spindump")

 				(require-not (literal "/System/Library/Frameworks/SystemConfiguration.framework/get-network-info"))
 				(require-not (literal "/bin/bash"))
 				(require-not (literal "/usr/sbin/kextstat"))
+				(require-not (require-any
+					(literal "/bin/df")
+					(literal "/bin/ps")
+					(literal "/usr/libexec/remotectl")
+				))
 				(require-not (require-any
 					(literal "/usr/sbin/lsof")
 					(literal "/usr/sbin/spindump")

 					(literal "/usr/local/bin/aopvtctl")
 					(literal "/usr/local/bin/apsclient")
 					(literal "/usr/local/bin/arkitctl")
-					(literal "/usr/local/bin/asclient")
 					(literal "/usr/local/bin/assistant_tool")
 					(literal "/usr/local/bin/audioDeviceDump")
 					(literal "/usr/local/bin/benchrun")

 					(literal "/usr/local/bin/findmydevicetool")
 					(literal "/usr/local/bin/fmltool")
 					(literal "/usr/local/bin/freezerctl")
-					(literal "/usr/local/bin/gmstool")
 					(literal "/usr/local/bin/hidreport")
 					(literal "/usr/local/bin/hidutil_internal")
 					(literal "/usr/local/bin/homepodsettingstool")
 					(literal "/usr/local/bin/homeutil")
 					(literal "/usr/local/bin/idstool")
-					(literal "/usr/local/bin/iftool")
 					(literal "/usr/local/bin/imtool")
 					(literal "/usr/local/bin/iopsutil")
 					(literal "/usr/local/bin/iordump")

 				))
 				(require-not (literal "/usr/local/bin/darwinup"))
 				(require-not (literal "/usr/local/bin/CADebug"))
+				(require-not (require-any
+					(literal "/usr/local/bin/asclient")
+					(literal "/usr/local/bin/gmstool")
+					(literal "/usr/local/bin/iftool")
+				))
 				(require-not (literal "/bin/ls"))
 				(require-not (literal "/bin/echo"))
 				(require-not (literal "/usr/sbin/sysctl"))

 				(require-not (literal "/System/Library/Frameworks/SystemConfiguration.framework/get-network-info"))
 				(require-not (literal "/bin/bash"))
 				(require-not (literal "/usr/sbin/kextstat"))
+				(require-not (require-any
+					(literal "/bin/df")
+					(literal "/bin/ps")
+					(literal "/usr/libexec/remotectl")
+				))
 				(require-not (require-any
 					(literal "/usr/sbin/lsof")
 					(literal "/usr/sbin/spindump")
```
