## CacheDeleteAppContainerCaches

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

 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (global-name "com.apple.containermanagerd"))
 		(require-not (global-name "com.apple.runningboard"))
-		(require-not (global-name "com.apple.cache_delete"))
 		(require-not (global-name "com.apple.diagd"))
 		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.logd"))
+		(require-not (global-name "com.apple.cache_delete"))
 		(require-not (system-attribute developer-mode))
 	)
 )
 
+(deny process-codesigning)
+
 (deny process-exec*)
 
+(allow process-exec-interpreter)
+
 (deny socket-ioctl)
 
 (deny syscall-unix)

 		MSC_task_self_trap
 		MSC_host_self_trap
 		MSC_semaphore_signal_trap
+		MSC_semaphore_wait_trap
 		MSC_semaphore_timedwait_trap
 		MSC__kernelrpc_mach_port_guard_trap
 		MSC_mach_generate_activity_id
```
