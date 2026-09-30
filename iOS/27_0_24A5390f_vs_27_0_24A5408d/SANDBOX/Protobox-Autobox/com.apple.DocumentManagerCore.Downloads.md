## com.apple.DocumentManagerCore.Downloads

> Group: ⬆️ Updated

```diff

 
 (deny socket-ioctl)
 (allow socket-ioctl
-	(ioctl-command CTLIOCGINFO)
+	(ioctl-command
+		CTLIOCGINFO
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
