## SiriHeadlessService

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.symptom_diagnostics"))
 		(require-not (global-name "com.apple.coreduetd.knowledge"))
 		(require-not (global-name "com.apple.assistantd.odeon-remote"))
+		(require-not (global-name "com.apple.intelligentroutingd.xpc.media"))
 		(require-not (global-name "com.apple.siri.attendingstates.xpc"))
 		(require-not (global-name "com.apple.siri.audiopowerupdate.xpc"))
+		(require-not (global-name "com.apple.agentboardd.telemetry"))
 		(require-not (global-name "com.apple.wifi.manager"))
 		(require-not (global-name "com.apple.siri.orchestration.capabilities"))
 		(require-not (global-name "com.apple.audio.AudioSession"))
 		(require-not (global-name "com.apple.assistant.device-context"))
+		(require-not (global-name "com.apple.campo"))
 		(require-not (global-name "com.apple.mobileasset.autoasset"))
+		(require-not (global-name "com.apple.itunescloudd.xpc"))
 		(require-not (global-name "com.apple.private.corewifi.mobilewifi-xpc"))
 		(require-not (global-name "com.apple.homed.xpc"))
 		(require-not (global-name "com.apple.siri.uaf.service"))

 		SYS_gettimeofday
 		SYS_getrusage
 		SYS_writev
+		SYS_rename
 		SYS_mkdir
 		SYS_rmdir
 		SYS_pread

 		SYS_openat_dprotected_np
 		SYS_getattrlist
 		SYS_setxattr
+		SYS_listxattr
 		SYS_fsctl
 		SYS_shm_open
 		SYS_shm_unlink

 		SYS_proc_rlimit_control
 		SYS_openat
 		SYS_openat_nocancel
+		SYS_renameat
 		SYS_fstatat
 		SYS_fstatat64
 		SYS_bsdthread_ctl
 		SYS_thread_selfusage
+		SYS_guarded_pwrite_np
 		SYS_mremap_encrypted
 		SYS_work_interval_ctl
 		SYS_getentropy

 		mach_port_get_context_from_user
 		task_info_from_user
 		semaphore_create
+		thread_info
 		vm_remap_external
 		vm_reallocate
 		mach_vm_range_create
```
