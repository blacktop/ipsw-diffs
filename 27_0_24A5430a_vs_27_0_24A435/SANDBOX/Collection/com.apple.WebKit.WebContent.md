## com.apple.WebKit.WebContent

> Group: ⬆️ Updated

```diff

 					(require-all
 						(extension "com.apple.assets.read")
 						(require-any
-							(require-any
-								(subpath "${HOME}/Library/Assets/com_apple_MobileAsset_VoiceServicesVocalizerVoice")
-								(subpath "${HOME}/Library/VoiceServices/Assets")
-							)
+							(literal "${HOME}/Library/Preferences/com.apple.security.plist")
 							(subpath "${HOME}/Library/Assets")
 							(subpath "/private/var/MobileAsset")
 						)

 						(literal "${HOME}/Library/Preferences/com.apple.corevideo.plist")
 						(literal "${HOME}/Library/Preferences/com.apple.itunesstored.plist")
 						(literal "${HOME}/Library/Preferences/com.apple.mediaremote.plist")
+						(subpath "/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_Font7")
+						(subpath "/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_Font8")
 					)
 					(require-any
 						(literal "/dev/null")

 						(subpath "${HOME}/Library/VoiceServices/Assets")
 					)
 					(require-any
-						(subpath "/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_Font7")
-						(subpath "/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_Font8")
+						(subpath "/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs")
+						(subpath "/private/var/db/datadetectors/sys")
 					)
 					(subpath "${HOME}/Library/Caches/com.apple.keyboards")
 					(subpath "/")
-					(subpath "/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs")
 					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.icloud.findmydevice.managed/Library")
-					(subpath "/private/var/db/datadetectors/sys")
 				)
 			)
 			(require-any

 					(require-all
 						(extension "com.apple.assets.read")
 						(require-any
-							(require-any
-								(subpath "${HOME}/Library/Assets/com_apple_MobileAsset_VoiceServicesVocalizerVoice")
-								(subpath "${HOME}/Library/VoiceServices/Assets")
-							)
+							(literal "${HOME}/Library/Preferences/com.apple.security.plist")
 							(subpath "${HOME}/Library/Assets")
 							(subpath "/private/var/MobileAsset")
 						)

 						(literal "${HOME}/Library/Preferences/com.apple.corevideo.plist")
 						(literal "${HOME}/Library/Preferences/com.apple.itunesstored.plist")
 						(literal "${HOME}/Library/Preferences/com.apple.mediaremote.plist")
+						(subpath "/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_Font7")
+						(subpath "/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_Font8")
 					)
 					(require-any
 						(literal "/dev/null")

 						(subpath "${HOME}/Library/VoiceServices/Assets")
 					)
 					(require-any
-						(subpath "/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_Font7")
-						(subpath "/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_Font8")
+						(subpath "/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs")
+						(subpath "/private/var/db/datadetectors/sys")
 					)
 					(subpath "${HOME}/Library/Caches/com.apple.keyboards")
 					(subpath "/")
-					(subpath "/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs")
 					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.icloud.findmydevice.managed/Library")
-					(subpath "/private/var/db/datadetectors/sys")
 				)
 			)
 			(require-any

 							(require-all
 								(extension "com.apple.assets.read")
 								(require-any
-									(require-any
-										(subpath "${HOME}/Library/Assets/com_apple_MobileAsset_VoiceServicesVocalizerVoice")
-										(subpath "${HOME}/Library/VoiceServices/Assets")
-									)
+									(literal "${HOME}/Library/Preferences/com.apple.security.plist")
 									(subpath "${HOME}/Library/Assets")
 									(subpath "/private/var/MobileAsset")
 								)

 								(literal "${HOME}/Library/Preferences/com.apple.corevideo.plist")
 								(literal "${HOME}/Library/Preferences/com.apple.itunesstored.plist")
 								(literal "${HOME}/Library/Preferences/com.apple.mediaremote.plist")
+								(subpath "/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_Font7")
+								(subpath "/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_Font8")
 							)
 							(require-any
 								(literal "/dev/null")

 								(subpath "${HOME}/Library/VoiceServices/Assets")
 							)
 							(require-any
-								(subpath "/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_Font7")
-								(subpath "/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_Font8")
+								(subpath "/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs")
+								(subpath "/private/var/db/datadetectors/sys")
 							)
 							(subpath "${HOME}/Library/Caches/com.apple.keyboards")
 							(subpath "/")
-							(subpath "/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs")
 							(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.icloud.findmydevice.managed/Library")
-							(subpath "/private/var/db/datadetectors/sys")
 						)
 					)
 					(require-any

 (deny syscall-unix)
 (allow syscall-unix
 	(syscall-number
-		SYS_exit
-		SYS_read
-		SYS_open
-		SYS_close
-		SYS_getuid
-		SYS_geteuid
+		SYS___disable_threadsignal
+		SYS___mac_syscall
 		SYS_access
-		SYS_dup
-		SYS_getegid
-		SYS_sigprocmask
-		SYS_ioctl
-		SYS_readlink
-		SYS_umask
-		SYS_munmap
-		SYS_mprotect
-		SYS_madvise
-		SYS_fcntl
-		SYS_gettimeofday
-		SYS_getrusage
-		SYS_writev
-		SYS_pread
+		SYS_bsdthread_create
+		SYS_bsdthread_ctl
+		SYS_bsdthread_terminate
+		SYS_close
+		SYS_close_nocancel
 		SYS_csops
 		SYS_csops_audittoken
-		SYS_pathconf
-		SYS_getrlimit
-		SYS_mmap
-		SYS_lseek
-		SYS_sysctl
-		SYS_getattrlist
-		SYS_getxattr
+		SYS_dup
+		SYS_exit
+		SYS_faccessat
+		SYS_fcntl
+		SYS_fcntl_nocancel
 		SYS_fgetxattr
-		SYS_shm_open
+		SYS_fstat64
+		SYS_fstatat64
+		SYS_fstatfs64
+		SYS_getattrlist
+		SYS_getdirentries64
+		SYS_getegid
+		SYS_getentropy
+		SYS_geteuid
+		SYS_getfsstat64
+		SYS_getrlimit
+		SYS_getrusage
 		SYS_gettid
-		SYS_psynch_mutexwait
-		SYS_psynch_mutexdrop
+		SYS_gettimeofday
+		SYS_getuid
+		SYS_getxattr
+		SYS_ioctl
+		SYS_issetugid
+		SYS_kevent_id
+		SYS_kevent_qos
+		SYS_lseek
+		SYS_lstat64
+		SYS_madvise
+		SYS_map_with_linking_np
+		SYS_memorystatus_control
+		SYS_mmap
+		SYS_mprotect
+		SYS_munmap
+		SYS_open
+		SYS_open_nocancel
+		SYS_openat
+		SYS_os_fault_with_payload
+		SYS_pathconf
+		SYS_pread
+		SYS_proc_info
 		SYS_psynch_cvbroad
+		SYS_psynch_cvclrprepost
 		SYS_psynch_cvsignal
 		SYS_psynch_cvwait
+		SYS_psynch_mutexdrop
+		SYS_psynch_mutexwait
 		SYS_psynch_rw_rdlock
-		SYS_psynch_rw_wrlock
 		SYS_psynch_rw_unlock
-		SYS_psynch_cvclrprepost
-		SYS_issetugid
-		SYS___disable_threadsignal
-		SYS_proc_info
-		SYS_stat64
-		SYS_fstat64
-		SYS_lstat64
-		SYS_getdirentries64
-		SYS_statfs64
-		SYS_fstatfs64
-		SYS_getfsstat64
-		SYS_bsdthread_create
-		SYS_bsdthread_terminate
-		SYS_workq_kernreturn
-		SYS_thread_selfid
-		SYS_kevent_qos
-		SYS_kevent_id
-		SYS___mac_syscall
+		SYS_psynch_rw_wrlock
+		SYS_read
 		SYS_read_nocancel
-		SYS_write_nocancel
-		SYS_open_nocancel
-		SYS_close_nocancel
-		SYS_fcntl_nocancel
-		SYS_memorystatus_control
-		SYS_openat
-		SYS_faccessat
-		SYS_fstatat64
-		SYS_bsdthread_ctl
-		SYS_getentropy
+		SYS_readlink
+		SYS_shm_open
+		SYS_sigprocmask
+		SYS_stat64
+		SYS_statfs64
+		SYS_sysctl
+		SYS_thread_selfid
 		SYS_ulock_wait
-		SYS_ulock_wake
-		SYS_os_fault_with_payload
 		SYS_ulock_wait2
-		SYS_map_with_linking_np)
+		SYS_ulock_wake
+		SYS_umask
+		SYS_workq_kernreturn
+		SYS_write_nocancel
+		SYS_writev)
 )
 (allow syscall-unix
 	(require-all
```
