## icprefd-xpc

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
 
+(deny iokit-open-user-client)
+
 (deny iokit-open-service)
 
 (deny iokit-set-properties)
 
 (deny ipc*)
 
-(deny job-creation)
+(allow ipc-sysv-shm)
 
-(deny mach-issue-extension)
+(deny isp-command-send)
 
-(deny mach-lookup
+(deny mach-host-special-port-set)
+
+(deny mach-issue-extension
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
 		(require-not (global-name "com.apple.lsd.mapdb"))

 	)
 )
 
+(deny process-codesigning)
+
 (deny process-exec*)
 
+(allow process-exec-interpreter)
+
 (deny socket-ioctl)
 
 (deny syscall-unix)

 		SYS_gettid
 		SYS_mkdir_extended
 		SYS_shared_region_check_np
+		SYS_psynch_rw_longrdlock
+		SYS_psynch_rw_yieldwrlock
+		SYS_psynch_rw_downgrade
+		SYS_psynch_rw_upgrade
+		SYS_psynch_mutexwait
+		SYS_psynch_mutexdrop
+		SYS_psynch_rw_rdlock
+		SYS_psynch_rw_wrlock
+		SYS_psynch_rw_unlock
+		SYS_psynch_rw_unlock2
 		SYS_issetugid
 		SYS___pthread_kill
 		SYS___pthread_sigmask
```
