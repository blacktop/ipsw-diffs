## fskitd

> `/usr/libexec/fskitd`

```diff

-474.60.43.0.0
-  __TEXT.__text: 0x42590
-  __TEXT.__auth_stubs: 0x8d0
-  __TEXT.__objc_stubs: 0x4160
-  __TEXT.__objc_methlist: 0x1648
-  __TEXT.__const: 0x130
-  __TEXT.__gcc_except_tab: 0x1c18
-  __TEXT.__cstring: 0x24c4
-  __TEXT.__oslogstring: 0x2d04
-  __TEXT.__objc_classname: 0x1e4
-  __TEXT.__objc_methname: 0x4ea8
-  __TEXT.__objc_methtype: 0x1ecc
-  __TEXT.__unwind_info: 0xe80
-  __DATA_CONST.__auth_got: 0x478
-  __DATA_CONST.__got: 0x2d0
+531.101.1.0.0
+  __TEXT.__text: 0x43888
+  __TEXT.__auth_stubs: 0x910
+  __TEXT.__objc_stubs: 0x42a0
+  __TEXT.__objc_methlist: 0x1ce4
+  __TEXT.__const: 0x140
+  __TEXT.__gcc_except_tab: 0x1c30
+  __TEXT.__cstring: 0x249f
+  __TEXT.__oslogstring: 0x2f56
+  __TEXT.__objc_classname: 0x206
+  __TEXT.__objc_methname: 0x5077
+  __TEXT.__objc_methtype: 0x1fae
+  __TEXT.__unwind_info: 0xea8
+  __DATA_CONST.__auth_got: 0x498
+  __DATA_CONST.__got: 0x300
   __DATA_CONST.__const: 0x2208
-  __DATA_CONST.__cfstring: 0x900
-  __DATA_CONST.__objc_classlist: 0x78
+  __DATA_CONST.__cfstring: 0x7a0
+  __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x58
-  __DATA.__objc_const: 0x28a0
-  __DATA.__objc_selrefs: 0x1350
-  __DATA.__objc_ivar: 0x154
-  __DATA.__objc_data: 0x4b0
-  __DATA.__data: 0x370
+  __DATA_CONST.__objc_superrefs: 0x60
+  __DATA.__objc_const: 0x1f48
+  __DATA.__objc_selrefs: 0x1480
+  __DATA.__objc_ivar: 0x170
+  __DATA.__objc_data: 0x500
+  __DATA.__data: 0x6c0
   __DATA.__common: 0x64
-  __DATA.__bss: 0x28
+  __DATA.__bss: 0x29
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/DiskArbitration.framework/Versions/A/DiskArbitration
   - /System/Library/Frameworks/ExtensionFoundation.framework/Versions/A/ExtensionFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  UUID: 9EB91B53-F7ED-3451-920C-67FE2B04A635
-  Functions: 1208
-  Symbols:   244
-  CStrings:  1713
+  UUID: CA5607DF-A3C3-315A-AF7C-9F484DDA93AA
+  Functions: 1227
+  Symbols:   254
+  CStrings:  1760
 
Symbols:
+ _FSModuleIdentityAttributeSupportsGenericURLs
+ _FSModuleIdentityAttributeSupportsKOIO_OLD
+ _FSModuleIdentityAttributeSupportsPathURLs
+ ___stderrp
+ __set_user_dir_suffix
+ _confstr
+ _fprintf
+ _freemntopts
+ _getenv
+ _getgrnam
+ _getmntoptnum
+ _getmntoptstr
+ _getpwnam
+ _getpwuid
+ _mount
+ _opterr
+ _optind
+ _optopt
+ _optreset
+ _sandbox_init_with_parameters
- _OBJC_CLASS_$_NSMutableString
- _environ
- _posix_spawn
- _posix_spawn_file_actions_addinherit_np
- _posix_spawn_file_actions_destroy
- _posix_spawn_file_actions_init
- _posix_spawnattr_destroy
- _posix_spawnattr_init
- _posix_spawnattr_setflags
- _waitpid
CStrings:
+ "$HOME not set, falling back to using getpwuid"
+ "%s: Got error %u (flags 0x%x operationId %llu)"
+ "%s: Got error %u (ioStatus %u flags 0x%x operationId %llu"
+ "%s: illegal option -- %c\n"
+ "%s: option requires an argument -- %c\n"
+ "@\"NSArray\""
+ "@\"NSData\""
+ "DARWIN_CACHE_DIR"
+ "Failed to enter sandbox: %{public}s"
+ "Failed to resolve mounton path:%s"
+ "Failed to stat the mounton path:%s"
+ "HOME"
+ "Ignoring PFH option"
+ "Ignoring fh option '%s'"
+ "Ignoring fpnfs option"
+ "Ignoring local locks option"
+ "Ignoring port number option"
+ "Ignoring protocol option"
+ "T@\"NSArray\",&,V_options"
+ "T@\"NSData\",&,V_fh"
+ "TB,N,V_gidSet"
+ "TB,N,V_modeSet"
+ "TB,N,V_uidSet"
+ "TMPDIR"
+ "Ti,N,V_mntFlags"
+ "Too many command options"
+ "Too many command options in mount invocation"
+ "_gidSet"
+ "_installedExtensionWithBundleID:user:replyHandler:"
+ "_mntFlags"
+ "_modeSet"
+ "_options"
+ "_uidSet"
+ "actimeo"
+ "args"
+ "blockmapFile:range:flags:operationID:reply:"
+ "blockmapFile:range:flags:operationID:replyHandler:"
+ "com.apple.fskitd"
+ "dg:m:o:u:v"
+ "dsize"
+ "failed to get passwd entry for uid %u"
+ "failed to initialize cache directory: %{darwin.errno}d"
+ "failed to initialize temporary directory: %{darwin.errno}d"
+ "failed to parse mount options:%s"
+ "failed to resolve cache directory: %{darwin.errno}d"
+ "failed to resolve temporary directory: %{darwin.errno}d"
+ "failed to resolve user's home directory: %{darwin.errno}d"
+ "fpnfs"
+ "fskitdMounter"
+ "gidSet"
+ "ignoring strictatime options"
+ "initWithBytes:length:"
+ "initWithBytesNoCopy:length:freeWhenDone:"
+ "initWithCapacity:"
+ "initWithUTF8String:"
+ "initWithUUID:"
+ "insertObject:atIndex:"
+ "installedExtensionWithBundleID:replyHandler:"
+ "invalid file mode: %s"
+ "locallocks"
+ "mntFlags"
+ "modeSet"
+ "mount"
+ "mount(2) error: %d"
+ "options"
+ "parsed mntflags:0x%x, altflags:0x%x"
+ "pfh"
+ "port"
+ "proto"
+ "quota"
+ "readahead"
+ "rsize"
+ "setFh:"
+ "setGidSet:"
+ "setMntFlags:"
+ "setModeSet:"
+ "setOptions:"
+ "setUidSet:"
+ "stringByAppendingString:"
+ "transformOptions"
+ "uidSet"
+ "unknown user id: %s"
+ "usedBytes"
+ "v20@0:8i16"
+ "v60@0:8@\"NSString\"16{_NSRange=QQ}24I40Q44@?<v@?i@\"NSData\"@\"NSData\">52"
+ "v60@0:8@16{_NSRange=QQ}24I40Q44@?52"
+ "wsize"
+ "{lifs_mntargs=\"flags\"I\"rsize\"i\"wsize\"i\"dsize\"i\"actimeo\"i\"readahead\"i\"port\"[64c]\"mountfrom\"[1024c]\"mnton\"[1024c]\"fh\"[64c]\"fhlen\"i\"mount_uid\"I\"mount_gid\"I\"mode\"S}"
+ "\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\x82"
- "%s "
- "%s: Got error %u (ioStatus %u flags 0x%x opeId %llu"
- "%s: Got error %u (startIO %u flags 0x%x opeId %llu"
- "%s: options added to argv: %@"
- ",%s"
- ",fh=%s"
- ",noatime"
- ",nofollow"
- ",noowners"
- ",pfh"
- ",sync"
- "/sbin/mount_lifs"
- "0123456789abcdef"
- "FSSupportsServerURLs"
- "Mounting file system on port %@ with rootfh = %s"
- "appendFormat:"
- "appendString:"
- "blockmapFile:range:startIO:flags:operationID:reply:"
- "blockmapFile:range:startIO:flags:operationID:replyHandler:"
- "checkIn returned error %@"
- "cmd: %@"
- "mount:"
- "mount_lifs"
- "newContainerID"
- "rsize=%d,wsize=%d,readahead=%d,dsize=%d,actimeo=%d"
- "rsize=%d,wsize=%d,readahead=%d,dsize=%d,actimeo=%d,noowners,noatime"
- "spawner: %s: exited with status %d\n"
- "spawner: %s: terminated by signal %d\n"
- "spawner: posix_spawn %s: error=%d\n"
- "spawner: waitpid %s: errno=%d\n"
- "splitOptions"
- "v64@0:8@\"NSString\"16{_NSRange=QQ}24i40I44Q48@?<v@?i@\"NSData\"@\"NSData\">56"

```
