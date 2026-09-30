## diskarbitrationd

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
 		(iokit-registry-entry-class "AppleAPFSContainer")
 		(iokit-registry-entry-class "AppleKeyStore")
 	)
 )
 
+(deny iokit-open-service)
+
 (deny iokit-set-properties)
 
 (deny ipc*)
 
-(deny ipc-posix-shm-read-data)
-(allow ipc-posix-shm-read-data
+(deny ipc-posix-shm*)
+(allow ipc-posix-shm*
 	(require-any
 		(ipc-posix-name "apple.cfprefs.system.daemonv1")
 		(ipc-posix-name "apple.cfprefs.user.daemonv1")

 	)
 )
 
-(deny ipc-posix-shm-write-data)
-(allow ipc-posix-shm-write-data
+(deny ipc-posix-shm-write-create)
+(allow ipc-posix-shm-write-create
 	(require-any
 		(ipc-posix-name "apple.cfprefs.*")
 		(ipc-posix-name "apple.cfprefs.user.daemonv1")
 	)
 )
 
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
 		(require-not (global-name "com.apple.filesystems.fskitd.livefs"))

 	)
 )
 
+(deny process-codesigning)
+(allow process-codesigning
+	(require-any
+		(literal "/System/Library/Filesystems/apfs.fs/apfs.util")
+		(literal "/System/Library/Filesystems/apfs.fs/fsck_apfs")
+		(literal "/System/Library/Filesystems/apfs_userfs.fs/apfs_userfs.util")
+		(literal "/System/Library/Filesystems/exfat.fs/exfat.util")
+		(literal "/System/Library/Filesystems/exfat.fs/fsck_exfat")
+		(literal "/System/Library/Filesystems/hfs.fs/Contents/Resources/hfs.util")
+		(literal "/System/Library/Filesystems/hfs.fs/fsck_hfs")
+		(literal "/System/Library/Filesystems/msdos.fs/Contents/Resources/msdos.util")
+		(literal "/System/Library/Filesystems/msdos.fs/fsck_msdos")
+		(literal "/System/Library/Filesystems/msdos.fs/fsck_msdos2")
+		(literal "/System/Library/Filesystems/ntfs.fs/ntfs.util")
+		(literal "/System/Library/Filesystems/virtiofs.fs/virtiofs.util")
+		(literal "/sbin/mount")
+		(literal "/sbin/umount")
+	)
+)
+
 (deny process-exec*)
 (allow process-exec*
 	(require-any
```
