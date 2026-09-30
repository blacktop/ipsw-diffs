## enhancedloggingd

> Group: ⬆️ Updated

```diff

 
 (deny socket-ioctl)
 (allow socket-ioctl
-	(ioctl-command CTLIOCGINFO SIOCGCONNINFO)
+	(ioctl-command
+		CTLIOCGINFO
+		SIOCGCONNINFO
+		SIOCGIFCONSTRAINED
+		SIOCGIFDELEGATE
+		SIOCGIFEXPENSIVE
+		SIOCGIFFLAGS
+		SIOCGIFFUNCTIONALTYPE
+		SIOCGIFLINKQUALITYMETRIC
+		SIOCGIFMTU
+		SIOCGIFULTRACONSTRAINED)
 )
 
 (deny syscall-unix)
```
