## MobileBackupCacheDeleteService

> `/System/Library/PrivateFrameworks/MobileBackup.framework/MobileBackupCacheDeleteService`

```diff

-2969.120.2.0.0
-  __TEXT.__text: 0x12b98
-  __TEXT.__auth_stubs: 0x7a0
-  __TEXT.__objc_stubs: 0x1f40
-  __TEXT.__objc_methlist: 0x7f0
-  __TEXT.__const: 0x1b0
-  __TEXT.__gcc_except_tab: 0x1fc
-  __TEXT.__cstring: 0x3b5f
+3033.0.0.0.0
+  __TEXT.__text: 0x1282c
+  __TEXT.__auth_stubs: 0x860
+  __TEXT.__objc_stubs: 0x20c0
+  __TEXT.__objc_methlist: 0x868
+  __TEXT.__const: 0x1a0
+  __TEXT.__gcc_except_tab: 0x2c4
+  __TEXT.__cstring: 0x3dbd
   __TEXT.__oslogstring: 0x1f0d
-  __TEXT.__objc_methname: 0x2466
-  __TEXT.__objc_classname: 0xea
-  __TEXT.__objc_methtype: 0x3d5
-  __TEXT.__unwind_info: 0x358
-  __DATA_CONST.__auth_got: 0x3e0
-  __DATA_CONST.__got: 0x160
-  __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x4f8
-  __DATA_CONST.__cfstring: 0xf40
+  __TEXT.__objc_methname: 0x263e
+  __TEXT.__objc_classname: 0xe1
+  __TEXT.__objc_methtype: 0x444
+  __TEXT.__unwind_info: 0x378
+  __DATA_CONST.__const: 0x538
+  __DATA_CONST.__cfstring: 0x1000
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0x30
   __DATA_CONST.__objc_arrayobj: 0x48
   __DATA_CONST.__objc_intobj: 0x18
+  __DATA_CONST.__auth_got: 0x440
+  __DATA_CONST.__got: 0x168
+  __DATA_CONST.__auth_ptr: 0x8
   __DATA.__objc_const: 0x9c0
-  __DATA.__objc_selrefs: 0x9b0
+  __DATA.__objc_selrefs: 0xa30
   __DATA.__objc_ivar: 0x44
   __DATA.__objc_data: 0x280
   __DATA.__bss: 0x98

   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: CF2B0643-2CCE-359C-B72B-F083B1C3004C
-  Functions: 319
-  Symbols:   178
-  CStrings:  1102
+  UUID: 1F94ACC9-1763-3A42-B273-CBECC5AFC9BC
+  Functions: 340
+  Symbols:   191
+  CStrings:  1143
 
Symbols:
+ _OBJC_CLASS_$_NSMutableSet
+ _fchownat
+ _fcopyfile
+ _mkdirat
+ _objc_begin_catch
+ _objc_claimAutoreleasedReturnValue
+ _objc_end_catch
+ _objc_exception_rethrow
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_terminate
CStrings:
+ "(flags & O_CREAT) == 0"
+ "+[MBFileOperation createDirectories:permissions:owner:group:error:]"
+ "+[MBFileOperation createOrOpenFD:baseFD:rpath:flags:mode:error:]"
+ "+[MBFileOperation createOrOpenFD:path:flags:mode:error:]"
+ "-[MBSuspendingClock clockByAddingPositiveTimeInterval:]"
+ "/private/var/mobile/Library/Caches/Backup/DT"
+ "/private/var/mobile/tmp/com.apple.backup.testing"
+ "/private/var/tmp/com.apple.backup"
+ "/private/var/tmp/com.apple.backup.testing"
+ "@24@0:8Q16"
+ "@24@0:8d16"
+ "B32@?0@\"MBFileSystemSnapshot\"8Q16^B24"
+ "B44@0:8@16S24I28I32^@36"
+ "B48@0:8^i16@24i32S36^@40"
+ "B52@0:8^i16i24@28i36S40^@44"
+ "Cannot call copyfile() on root dir"
+ "Failed to open %@ when trying restore parent of %@"
+ "MBSuspendingClock.m"
+ "Q24@0:8^@16"
+ "Snapshot %@ not found for volume %@"
+ "_initWithStartTime:"
+ "_openFD:baseFD:rpath:flags:mode:error:"
+ "_openFD:path:flags:mode:error:"
+ "characterAtIndex:"
+ "clockByAddingPositiveTimeInterval:"
+ "copyRegularFileFrom:to:replaceDestination:error:"
+ "countOfSnapshotsForAllPersonae:"
+ "createDirectories:permissions:owner:group:error:"
+ "createOrOpenFD:baseFD:rpath:flags:mode:error:"
+ "createOrOpenFD:path:flags:mode:error:"
+ "fchownat failed at %@ for %@/%@"
+ "fcopyfile failed"
+ "findSnapshotWithName:forVolume:error:"
+ "indexesOfObjectsPassingTest:"
+ "interval >= 0"
+ "isError:withCodes:"
+ "mkdirat failed at %@ for %@/%@"
+ "path.length > 0 && [path characterAtIndex:0] == '/'"
+ "pathComponents"
+ "set"
+ "unionSet:"
- "/var/mobile/Library/Caches/Backup/DT"
- "/var/mobile/tmp/com.apple.backup.testing"
- "/var/tmp/com.apple.backup"
- "/var/tmp/com.apple.backup.testing"
- "destinationBaseFD != 1"
- "flags"

```
