## apfs_boot_util

> `/System/Library/Filesystems/apfs.fs/apfs_boot_util`

```diff

-2235.80.4.0.1
-  __TEXT.__text: 0x1114
-  __TEXT.__auth_stubs: 0x2a0
-  __TEXT.__cstring: 0x6f8
-  __TEXT.__const: 0x18
-  __TEXT.__unwind_info: 0x84
-  __DATA_CONST.__auth_got: 0x150
+2236.102.1.0.0
+  __TEXT.__text: 0x16f8
+  __TEXT.__auth_stubs: 0x320
+  __TEXT.__const: 0x20
+  __TEXT.__cstring: 0xa1e
+  __TEXT.__unwind_info: 0x98
+  __DATA_CONST.__auth_got: 0x190
   __DATA_CONST.__got: 0x20
   __DATA_CONST.__auth_ptr: 0x8
   __DATA.__data: 0x4

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/APFS.framework/APFS
   - /usr/lib/libSystem.B.dylib
-  Functions: 16
-  Symbols:   49
-  CStrings:  47
+  Functions: 18
+  Symbols:   57
+  CStrings:  71
 
Symbols:
+ ___strlcpy_chk
+ _fcntl
+ _ffsctl
+ _getxattr
+ _graftdmg
+ _openat
+ _strspn
+ _sysctlbyname
CStrings:
+ "%s:%d: Successfully grafted and registered ExclaveOS Cryptex [%s] on [%s]\n"
+ "%s:%d: failed to get boot object path: %d\n"
+ "%s:%d: failed to get exclaves status: %d\n"
+ "%s:%d: failed to get graft dir path: %d\n"
+ "%s:%d: failed to graftdmg: %d\n"
+ "%s:%d: failed to open ExclaveOS directory [%s]: %d\n"
+ "%s:%d: failed to open boot object path [%s]: %d\n"
+ "%s:%d: failed to open dmg: %d\n"
+ "%s:%d: failed to open graft dir: %d\n"
+ "%s:%d: failed to open preboot volume mount dir: %d\n"
+ "%s:%d: failed to open volume root hash: %d\n"
+ "%s:%d: failed to register graft dir: %d\n"
+ "%s:%d: invalid exclaves status: %d\n"
+ "/System/Cryptexes/ExclaveOS"
+ "/private/preboot"
+ "Ap,ExclaveOS.dmg"
+ "Ap,ExclaveOSVolume.img4"
+ "Cryptexes/ExclaveOS"
+ "ExclaveOS graft"
+ "com.apple.root.cryptex"
+ "graft_exclaveos"
+ "kern.bootobjectspath"
+ "kern.exclaves_status"
+ "usr/standalone/firmware/FUD/"

```
