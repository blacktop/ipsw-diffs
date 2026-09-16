## StandaloneHIDAudService

> Group: ⬆️ Updated

```diff

 (deny process-exec*)
 
 (deny socket-ioctl)
+(allow socket-ioctl
+	(ioctl-command
+		SIOCGIFCONSTRAINED
+		SIOCGIFDELEGATE
+		SIOCGIFEXPENSIVE
+		SIOCGIFFLAGS
+		SIOCGIFFUNCTIONALTYPE
+		SIOCGIFLINKQUALITYMETRIC
+		SIOCGIFMTU
+		SIOCGIFULTRACONSTRAINED)
+)
 
 (deny syscall-unix)
 (allow syscall-unix
```
