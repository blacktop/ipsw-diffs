## fskitd

> `/usr/libexec/fskitd`

```diff

-474.60.43.0.0
-  __TEXT.__text: 0x3edc4
-  __TEXT.__auth_stubs: 0xaa0
-  __TEXT.__objc_stubs: 0x45a0
-  __TEXT.__objc_methlist: 0x1678
-  __TEXT.__const: 0x128
-  __TEXT.__gcc_except_tab: 0x1fd0
-  __TEXT.__cstring: 0x2578
-  __TEXT.__oslogstring: 0x31b8
-  __TEXT.__objc_classname: 0x1f8
-  __TEXT.__objc_methname: 0x51d7
-  __TEXT.__objc_methtype: 0x1ecc
-  __TEXT.__unwind_info: 0xec8
-  __DATA_CONST.__auth_got: 0x560
-  __DATA_CONST.__got: 0x300
-  __DATA_CONST.__const: 0x1d50
-  __DATA_CONST.__cfstring: 0x940
-  __DATA_CONST.__objc_classlist: 0x80
+531.100.55.0.1
+  __TEXT.__text: 0x4042c
+  __TEXT.__auth_stubs: 0xb00
+  __TEXT.__objc_stubs: 0x4660
+  __TEXT.__objc_methlist: 0x1d24
+  __TEXT.__const: 0x130
+  __TEXT.__gcc_except_tab: 0x1fe8
+  __TEXT.__cstring: 0x25f5
+  __TEXT.__oslogstring: 0x33d0
+  __TEXT.__objc_classname: 0x21a
+  __TEXT.__objc_methname: 0x5378
+  __TEXT.__objc_methtype: 0x1fae
+  __TEXT.__unwind_info: 0xee8
+  __DATA_CONST.__auth_got: 0x590
+  __DATA_CONST.__got: 0x338
+  __DATA_CONST.__const: 0x1fc0
+  __DATA_CONST.__cfstring: 0x820
+  __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x58
+  __DATA_CONST.__objc_superrefs: 0x60
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x2930
-  __DATA.__objc_selrefs: 0x1420
-  __DATA.__objc_ivar: 0x154
-  __DATA.__objc_data: 0x500
-  __DATA.__data: 0x370
+  __DATA.__objc_const: 0x1fd8
+  __DATA.__objc_selrefs: 0x1540
+  __DATA.__objc_ivar: 0x170
+  __DATA.__objc_data: 0x550
+  __DATA.__data: 0x6c0
   __DATA.__common: 0x74
-  __DATA.__bss: 0x30
+  __DATA.__bss: 0x31
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreSpotlight.framework/CoreSpotlight
   - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  Functions: 1182
-  Symbols:   280
-  CStrings:  1681
+  Functions: 1207
+  Symbols:   293
+  CStrings:  1765
 
Symbols:
+ _FSModuleIdentityAttributeSupportsGenericURLs
+ _FSModuleIdentityAttributeSupportsKOIO_OLD
+ _FSModuleIdentityAttributeSupportsPathURLs
+ ___stderrp
+ ___strlcpy_chk
+ _bzero
+ _fprintf
+ _freemntopts
+ _getgrnam
+ _getmnt_silent
+ _getmntoptnum
+ _getmntopts
+ _getmntoptstr
+ _getpwnam
+ _mount
+ _opterr
+ _optind
+ _optopt
+ _optreset
+ _realpath$DARWIN_EXTSN
+ _snprintf
+ _strchr
+ _strdup
+ _strsep
- _OBJC_CLASS_$_NSMutableString
- _environ
- _objc_retain_x9
- _posix_spawn
- _posix_spawn_file_actions_addinherit_np
- _posix_spawn_file_actions_destroy
- _posix_spawn_file_actions_init
- _posix_spawnattr_destroy
- _posix_spawnattr_init
- _posix_spawnattr_setflags
- _waitpid
CStrings:
+ "%s,%s"
+ "%s: Got error %u (flags 0x%x operationId %llu)"
+ "%s: Got error %u (ioStatus %u flags 0x%x operationId %llu"
+ "%s: argc after parseMountOption: %d"
+ "%s: argc before parseMountOption: %d"
+ "%s: illegal option -- %c\n"
+ "%s: option requires an argument -- %c\n"
+ "%s: options after parseMountOption: %s"
+ "%s: options before parseMountOption: %s"
+ "%s:MNT_FORCE||MNT_UPDATE||MNT_RELOAD:options:%s:EINVAL"
+ "%s:cmdParamCount:%d:options:%s"
+ "%s:unsupported:options:%s:EINVAL"
+ ","
+ "@\"NSArray\""
+ "@\"NSData\""
+ "Failed to parse options %{darwin.errno}d"
+ "Failed to resolve mounton path:%s"
+ "Failed to stat the mounton path:%s"
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
+ "async"
+ "auto"
+ "automounted"
+ "blockmapFile:range:flags:operationID:reply:"
+ "blockmapFile:range:flags:operationID:replyHandler:"
+ "browse"
+ "defwrite"
+ "dev"
+ "dg:m:o:u:v"
+ "dsize"
+ "exec"
+ "failed to parse mount options:%s"
+ "follow"
+ "force"
+ "fpnfs"
+ "fskitdMounter"
+ "gidSet"
+ "groupquota"
+ "ignoring strictatime options"
+ "initWithBytes:length:"
+ "initWithBytesNoCopy:length:freeWhenDone:"
+ "initWithCapacity:"
+ "initWithUTF8String:"
+ "installedExtensionWithBundleID:replyHandler:"
+ "invalid file mode: %s"
+ "locallocks"
+ "mntFlags"
+ "modeSet"
+ "mount"
+ "mount(2) error: %d"
+ "options"
+ "owners"
+ "parseMountOption"
+ "parsed mntflags:0x%x, altflags:0x%x"
+ "perm"
+ "pfh"
+ "port"
+ "protect"
+ "proto"
+ "quarantine"
+ "quota"
+ "rdonly"
+ "readahead"
+ "reload"
+ "ro"
+ "rsize"
+ "rw"
+ "setFh:"
+ "setGidSet:"
+ "setMntFlags:"
+ "setModeSet:"
+ "setOptions:"
+ "setUidSet:"
+ "strictatime"
+ "suid"
+ "sync"
+ "transformOptions"
+ "uidSet"
+ "union"
+ "unknown user id: %s"
+ "update"
+ "usedBytes"
+ "userquota"
+ "v20@0:8i16"
+ "v60@0:8@\"NSString\"16{_NSRange=QQ}24I40Q44@?<v@?i@\"NSData\"@\"NSData\">52"
+ "v60@0:8@16{_NSRange=QQ}24I40Q44@?52"
+ "wsize"
+ "{lifs_mntargs=\"flags\"I\"rsize\"i\"wsize\"i\"dsize\"i\"actimeo\"i\"readahead\"i\"port\"[64c]\"mountfrom\"[1024c]\"mnton\"[1024c]\"fh\"[64c]\"fhlen\"i\"mount_uid\"I\"mount_gid\"I\"mode\"S}"
+ "\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\x82"
- "%s "
- "%s: Got error %u (ioStatus %u flags 0x%x opeId %llu"
- "%s: Got error %u (startIO %u flags 0x%x opeId %llu"
- ",fh=%s"
- ",nofollow"
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
- "fpnfs,noatime,%@,port=%@,rsize=%d,wsize=%d,readahead=%d,dsize=%d,actimeo=%d,locallocks,noquota,noexec,noowners,nobrowse"
- "mount:"
- "mount_lifs"
- "proto=tcp"
- "proto=ticotsord"
- "spawner: %s: exited with status %d\n"
- "spawner: %s: terminated by signal %d\n"
- "spawner: posix_spawn %s: error=%d\n"
- "spawner: waitpid %s: errno=%d\n"
- "v64@0:8@\"NSString\"16{_NSRange=QQ}24i40I44Q48@?<v@?i@\"NSData\"@\"NSData\">56"

```
