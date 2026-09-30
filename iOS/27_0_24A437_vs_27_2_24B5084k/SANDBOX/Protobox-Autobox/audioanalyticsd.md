## audioanalyticsd

> Group: ⬆️ Updated

```diff

 
 (deny socket-ioctl)
 (allow socket-ioctl
-	(ioctl-command CTLIOCGINFO SIOCGCONNINFO)
+	(ioctl-command
+		CTLIOCGINFO
+		SIOCGCONNINFO
+		SIOCGIFAGENTDATA
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

 		SYS_recvmsg
 		SYS_sendmsg
 		SYS_recvfrom
+		SYS_getsockname
 		SYS_access
 		SYS_kill
 		SYS_crossarch_trap

 		SYS_fsync
 		SYS_socket
 		SYS_connect
+		SYS_bind
 		SYS_setsockopt
 		SYS_sigsuspend
 		SYS_gettimeofday
```
