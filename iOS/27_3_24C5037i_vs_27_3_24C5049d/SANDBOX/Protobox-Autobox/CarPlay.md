## CarPlay

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.caraccessoryframework.cardata"))
 		(require-not (global-name "com.apple.containermanagerd"))
 		(require-not (global-name "com.apple.runningboard"))
+		(require-not (global-name "com.apple.coremedia.endpointstream.xpc"))
 		(require-not (global-name "com.apple.coremedia.endpointremotecontrolsession.xpc"))
 		(require-not (global-name "com.apple.CarPlayApp.service"))
 		(require-not (global-name "com.apple.coreduetd.people"))

 (allow socket-ioctl
 	(ioctl-command
 		CTLIOCGINFO
+		SIOCGCONNINFO
 		SIOCGIFCONSTRAINED
 		SIOCGIFDELEGATE
 		SIOCGIFEXPENSIVE

 		SYS_getpid
 		SYS_getuid
 		SYS_geteuid
+		SYS_recvmsg
+		SYS_sendmsg
 		SYS_recvfrom
 		SYS_getsockname
 		SYS_access

 		SYS_write_nocancel
 		SYS_open_nocancel
 		SYS_close_nocancel
+		SYS_recvmsg_nocancel
 		SYS_sendmsg_nocancel
 		SYS_recvfrom_nocancel
 		SYS_fcntl_nocancel
```
