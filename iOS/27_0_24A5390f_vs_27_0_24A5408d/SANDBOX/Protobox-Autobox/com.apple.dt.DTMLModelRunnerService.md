## com.apple.dt.DTMLModelRunnerService

> Group: ⬆️ Updated

```diff

 		SYS___pthread_fchdir
 		SYS_bsdthread_create
 		SYS_bsdthread_terminate
+		SYS_kqueue
 		SYS_kevent
 		SYS_bsdthread_register
 		SYS_workq_open

 		SYS_fsgetpath
 		SYS_memorystatus_control
 		SYS_guarded_close_np
+		SYS_guarded_kqueue_np
 		SYS_change_fdguard_np
 		SYS_proc_rlimit_control
 		SYS_getattrlistbulk

 		SYS_terminate_with_payload
 		SYS_abort_with_payload
 		SYS_os_fault_with_payload
+		SYS_kqueue_workloop_ctl
 		SYS_memorystatus_available_memory
 		SYS_objc_bp_assist_cfg_np
 		SYS_preadv

 (deny system-fcntl)
 (allow system-fcntl
 	(fcntl-command
+		F_GETFD
 		F_SETFD
 		F_GETFL
 		F_SETLK
```
