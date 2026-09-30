## sysdiagnosed

> Group: ⬆️ Updated

```diff

 		(require-any
 			(require-all
 				(require-not (literal "/bin/bash"))
+				(require-not (literal "/bin/sleep"))
 				(require-not (literal "/sbin/mount"))
 				(require-not (literal "/System/Library/Frameworks/SystemConfiguration.framework/get-network-info"))
 				(require-not (literal "/bin/echo"))

 					(literal "/usr/bin/zprint")
 					(literal "/usr/sbin/ioreg")
 				))
-				(require-not (literal "/usr/bin/log"))
 				(require-not (literal "/usr/bin/find"))
+				(require-not (literal "/usr/bin/log"))
 				(require-not (require-any
 					(literal "/usr/sbin/lsof")
 					(literal "/usr/sbin/spindump")

 				))
 				(require-not (literal "/usr/local/bin/ddt"))
 				(require-not (literal "/bin/bash"))
+				(require-not (literal "/bin/sleep"))
 				(require-not (literal "/sbin/mount"))
 				(require-not (literal "/System/Library/Frameworks/SystemConfiguration.framework/get-network-info"))
 				(require-not (literal "/bin/echo"))

 					(literal "/usr/bin/zprint")
 					(literal "/usr/sbin/ioreg")
 				))
-				(require-not (literal "/usr/bin/log"))
 				(require-not (literal "/usr/bin/find"))
+				(require-not (literal "/usr/bin/log"))
 				(require-not (require-any
 					(literal "/usr/sbin/lsof")
 					(literal "/usr/sbin/spindump")

 		(require-any
 			(require-all
 				(require-not (literal "/bin/bash"))
+				(require-not (literal "/bin/sleep"))
 				(require-not (literal "/sbin/mount"))
 				(require-not (literal "/System/Library/Frameworks/SystemConfiguration.framework/get-network-info"))
 				(require-not (literal "/bin/echo"))

 					(literal "/usr/bin/zprint")
 					(literal "/usr/sbin/ioreg")
 				))
-				(require-not (literal "/usr/bin/log"))
 				(require-not (literal "/usr/bin/find"))
+				(require-not (literal "/usr/bin/log"))
 				(require-not (require-any
 					(literal "/usr/sbin/lsof")
 					(literal "/usr/sbin/spindump")

 				))
 				(require-not (literal "/usr/local/bin/ddt"))
 				(require-not (literal "/bin/bash"))
+				(require-not (literal "/bin/sleep"))
 				(require-not (literal "/sbin/mount"))
 				(require-not (literal "/System/Library/Frameworks/SystemConfiguration.framework/get-network-info"))
 				(require-not (literal "/bin/echo"))

 					(literal "/usr/bin/zprint")
 					(literal "/usr/sbin/ioreg")
 				))
-				(require-not (literal "/usr/bin/log"))
 				(require-not (literal "/usr/bin/find"))
+				(require-not (literal "/usr/bin/log"))
 				(require-not (require-any
 					(literal "/usr/sbin/lsof")
 					(literal "/usr/sbin/spindump")
```
