## BTMap

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

 		mach_exception_raise
 		mach_exception_raise_state
 		mach_exception_raise_state_identity
+		io_iterator_next
 		io_registry_create_iterator
 		io_registry_entry_from_path
 		io_service_open_extended
```
