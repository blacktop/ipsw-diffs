## IMDMessageServicesAgent

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (global-name "com.apple.frontboard.systemappservices"))
 		(require-not (global-name "com.apple.coremedia.mediaplaybackd.asset.xpc"))
+		(require-not (global-name "com.apple.nsurlsessiond.NSURLSessionProxyService"))
 		(require-not (global-name "com.apple.idsremoteurlconnectionagent.embedded.auth"))
 		(require-not (global-name "com.apple.coremedia.asset.xpc"))
 		(require-not (global-name "com.apple.commcenter.coretelephony.xpc"))

 		(require-not (global-name "com.apple.commcenter.xpc"))
 		(require-not (global-name "com.apple.SystemConfiguration.configd"))
 		(require-not (global-name "com.apple.erm.logging"))
+		(require-not (global-name "com.apple.ctkd.token-client"))
 		(require-not (global-name "com.apple.managedconfiguration.profiled.public"))
 		(require-not (global-name "com.apple.nehelper"))
 		(require-not (global-name "com.apple.coremedia.customurlloader.xpc"))

 		SYS_kdebug_trace_string
 		SYS_kdebug_trace64
 		SYS_kdebug_trace
+		SYS_stat
+		SYS_fstat
+		SYS_lstat
 		SYS_pathconf
 		SYS_getrlimit
 		SYS_setrlimit

 		SYS_sem_open
 		SYS_sem_close
 		SYS_sysctlbyname
+		SYS_stat_extended
+		SYS_lstat_extended
+		SYS_fstat_extended
 		SYS_gettid
 		SYS_mkdir_extended
 		SYS_shared_region_check_np

 		SYS_stat64
 		SYS_fstat64
 		SYS_lstat64
+		SYS_stat64_extended
+		SYS_lstat64_extended
+		SYS_fstat64_extended
 		SYS_getdirentries64
 		SYS_statfs64
 		SYS_fstatfs64

 		SYS_guarded_close_np
 		SYS_change_fdguard_np
 		SYS_connectx
+		SYS_getattrlistbulk
 		SYS_openat
 		SYS_faccessat
 		SYS_fchownat
```
