## CheckerBoard

> Group: ⬆️ Updated

```diff

 
 (deny generic-issue-extension)
 
-(deny iokit-issue-extension)
+(deny iokit-get-properties)
 
-(deny iokit-open-user-client)
-(allow iokit-open-user-client
+(deny iokit-open*)
+(allow iokit-open*
 	(require-any
 		(iokit-registry-entry-class "${ENTITLEMENT:com.apple.security.exception.iokit-user-client-class}")
 		(iokit-registry-entry-class "${ENTITLEMENT:com.apple.security.iokit-user-client-class}")

 	)
 )
 
-(deny iokit-open-service)
-(allow iokit-open-service
+(deny iokit-open-user-client)
+(allow iokit-open-user-client
 	(require-any
 		(iokit-registry-entry-class "AGXAccelerator")
 		(iokit-registry-entry-class "AppleANS2CGNVMeController")

 		(iokit-registry-entry-class "AppleParavirtGPU")
 		(iokit-registry-entry-class "AppleS8000AESAccelerator")
 		(iokit-registry-entry-class "AppleSPUHIDDriver")
+		(iokit-registry-entry-class "AppleSPUHIDEventDriver")
 		(iokit-registry-entry-class "IOMobileFramebuffer")
 		(iokit-registry-entry-class "IOPMrootDomain")
 		(iokit-registry-entry-class "IOSurfaceRoot")

 	)
 )
 
+(deny iokit-open-service)
+
 (deny iokit-set-properties)
 
 (deny ipc*)
 
-(deny ipc-posix-sem-create)
-(allow ipc-posix-sem-create
+(deny ipc-posix-sem*)
+(allow ipc-posix-sem*
 	(ipc-posix-name "keyboard-flush.boot")
 )
 
-(deny ipc-posix-sem-open)
-(allow ipc-posix-sem-open
+(deny ipc-posix-sem-create)
+(allow ipc-posix-sem-create
 	(require-any
 		(ipc-posix-name "hangtelemetryd.onceatboot")
 		(ipc-posix-name "keyboard-flush.boot")
 	)
 )
 
-(deny ipc-posix-shm-read-data)
-(allow ipc-posix-shm-read-data
+(deny ipc-posix-shm*)
+(allow ipc-posix-shm*
 	(require-any
 		(ipc-posix-name "/FBW1:com.apple.frontboard.syst")
 		(ipc-posix-name "/FBW2:com.apple.frontboard.syst")

 	)
 )
 
-(deny ipc-posix-shm-write-create)
-(allow ipc-posix-shm-write-create
+(deny ipc-posix-shm-write*)
+(allow ipc-posix-shm-write*
 	(require-any
 		(ipc-posix-name "/FBW1:com.apple.frontboard.syst")
 		(ipc-posix-name "/FBW2:com.apple.frontboard.syst")
 	)
 )
 
-(deny ipc-posix-shm-write-unlink)
-(allow ipc-posix-shm-write-unlink
-	(require-any
-		(ipc-posix-name "/FBW1:com.apple.frontboard.syst")
-		(ipc-posix-name "/FBW2:com.apple.frontboard.syst")
-	)
-)
+(allow ipc-sysv-shm)
 
-(deny job-creation)
+(deny isp-command-send)
 
-(deny mach-issue-extension)
+(deny mach-host-special-port-set)
 
-(deny mach-lookup
+(deny mach-issue-extension
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
 		(require-not (global-name "com.apple.biome.access.user"))

 	)
 )
 
+(deny process-codesigning)
+
 (deny process-exec*)
 
+(allow process-exec-interpreter)
+
 (deny socket-ioctl)
 (allow socket-ioctl
 	(ioctl-command

 		MSC_mach_voucher_extract_attr_recipe_trap
 		MSC__kernelrpc_mach_port_type_trap
 		MSC__kernelrpc_mach_port_request_notification_trap
+		MSC__exclaves_ctl_trap
 		MSC_mach_timebase_info_trap
 		MSC_mk_timer_create
 		MSC_mk_timer_destroy
```
