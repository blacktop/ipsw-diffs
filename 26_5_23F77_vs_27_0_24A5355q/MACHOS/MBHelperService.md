## MBHelperService

> `/System/Library/PrivateFrameworks/MobileBackup.framework/XPCServices/MBHelperService.xpc/MBHelperService`

```diff

-2969.120.2.0.0
-  __TEXT.__text: 0x14d24
-  __TEXT.__auth_stubs: 0xb80
-  __TEXT.__objc_stubs: 0x2080
-  __TEXT.__objc_methlist: 0xc84
+3033.0.0.0.0
+  __TEXT.__text: 0x1410c
+  __TEXT.__auth_stubs: 0xbc0
+  __TEXT.__objc_stubs: 0x20a0
+  __TEXT.__objc_methlist: 0xca4
   __TEXT.__const: 0x228
-  __TEXT.__objc_methname: 0x2652
-  __TEXT.__cstring: 0x3aca
-  __TEXT.__objc_classname: 0x142
-  __TEXT.__objc_methtype: 0x775
+  __TEXT.__objc_methname: 0x26af
+  __TEXT.__cstring: 0x3b92
+  __TEXT.__objc_classname: 0x137
+  __TEXT.__objc_methtype: 0x78b
   __TEXT.__oslogstring: 0x1f26
-  __TEXT.__gcc_except_tab: 0x58
-  __TEXT.__unwind_info: 0x418
-  __DATA_CONST.__auth_got: 0x5d0
-  __DATA_CONST.__got: 0x158
-  __DATA_CONST.__auth_ptr: 0x8
+  __TEXT.__gcc_except_tab: 0x3c
+  __TEXT.__unwind_info: 0x3b8
   __DATA_CONST.__const: 0x588
-  __DATA_CONST.__cfstring: 0x1540
+  __DATA_CONST.__cfstring: 0x1560
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x28

   __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_arraydata: 0x50
   __DATA_CONST.__objc_arrayobj: 0x78
+  __DATA_CONST.__auth_got: 0x5f0
+  __DATA_CONST.__got: 0x158
+  __DATA_CONST.__auth_ptr: 0x8
   __DATA.__objc_const: 0xfa8
-  __DATA.__objc_selrefs: 0xba0
+  __DATA.__objc_selrefs: 0xbb8
   __DATA.__objc_ivar: 0x80
   __DATA.__objc_data: 0x410
   __DATA.__data: 0x228

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: C6A2C189-F728-31A2-BA6F-0795E6991B93
-  Functions: 399
-  Symbols:   287
-  CStrings:  1345
+  UUID: AD6C73BB-F97A-3932-8AAB-5E9C3237C7E9
+  Functions: 401
+  Symbols:   291
+  CStrings:  1355
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x3
+ _objc_retain_x4
- _objc_retainAutoreleasedReturnValue
CStrings:
+ "-[MBSuspendingClock clockByAddingPositiveTimeInterval:]"
+ "/private/var/mobile/Library/Caches/Backup/DT"
+ "/private/var/mobile/tmp/com.apple.backup.testing"
+ "/private/var/tmp/backupd-XXXXXXXXXXXXXXX"
+ "/private/var/tmp/com.apple.backup"
+ "/private/var/tmp/com.apple.backup.testing"
+ "@24@0:8Q16"
+ "@24@0:8d16"
+ "MBSuspendingClock.m"
+ "Snapshot %@ not found for volume %@"
+ "Unable to create /private/var/tmp/backupd-XXXXXXXXXX directory"
+ "Unable to create /private/var/tmp/backupd-XXXXXXXXXX directory (mkdtemp)"
+ "Unable to create /private/var/tmp/backupd-XXXXXXXXXX directory (strdup)"
+ "_initWithStartTime:"
+ "clockByAddingPositiveTimeInterval:"
+ "findSnapshotWithName:forVolume:error:"
+ "interval >= 0"
- "/var/mobile/Library/Caches/Backup/DT"
- "/var/mobile/tmp/com.apple.backup.testing"
- "/var/tmp/backupd-XXXXXXXXXXXXXXX"
- "/var/tmp/com.apple.backup"
- "/var/tmp/com.apple.backup.testing"
- "Unable to create /var/tmp/backupd-XXXXXXXXXX directory"
- "Unable to create /var/tmp/backupd-XXXXXXXXXX directory (mkdtemp)"
- "Unable to create /var/tmp/backupd-XXXXXXXXXX directory (strdup)"

```
