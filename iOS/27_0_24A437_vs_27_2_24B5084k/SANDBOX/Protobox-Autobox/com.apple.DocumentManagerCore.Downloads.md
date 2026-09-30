## com.apple.DocumentManagerCore.Downloads

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (global-name "com.apple.dmd.policy"))
+		(require-not (global-name "com.apple.revisiond"))
 		(require-not (global-name "com.apple.spotlight.SearchAgent"))
 		(require-not (global-name "com.apple.FileProvider"))
 		(require-not (global-name "com.apple.DesktopServicesHelper"))

 		SYS_pwrite_nocancel
 		SYS___semwait_signal_nocancel
 		SYS_fsgetpath
+		SYS_fileport_makeport
 		SYS_fileport_makefd
 		SYS_memorystatus_control
 		SYS_guarded_close_np

 		MSC__kernelrpc_mach_vm_allocate_trap
 		MSC__kernelrpc_mach_vm_purgable_control_trap
 		MSC__kernelrpc_mach_vm_deallocate_trap
+		MSC_task_dyld_process_info_notify_get
 		MSC__kernelrpc_mach_vm_protect_trap
 		MSC__kernelrpc_mach_vm_map_trap
 		MSC__kernelrpc_mach_port_allocate_trap
```
