## MobileBackupUEA

> `/System/Library/UserEventPlugins/MobileBackupUEA.plugin/MobileBackupUEA`

```diff

-2969.120.2.0.0
-  __TEXT.__text: 0xa244
-  __TEXT.__auth_stubs: 0x680
-  __TEXT.__objc_stubs: 0x1440
-  __TEXT.__objc_methlist: 0x6f4
-  __TEXT.__const: 0x170
+3033.0.0.0.0
+  __TEXT.__text: 0x9ca4
+  __TEXT.__auth_stubs: 0x6d0
+  __TEXT.__objc_stubs: 0x14c0
+  __TEXT.__objc_methlist: 0x6fc
+  __TEXT.__const: 0x160
   __TEXT.__oslogstring: 0xfa5
-  __TEXT.__cstring: 0x1a35
-  __TEXT.__objc_classname: 0x97
-  __TEXT.__objc_methname: 0x1a3d
-  __TEXT.__objc_methtype: 0x591
-  __TEXT.__gcc_except_tab: 0x188
-  __TEXT.__unwind_info: 0x238
-  __DATA.__auth_got: 0x350
-  __DATA.__got: 0x128
-  __DATA.__auth_ptr: 0x8
-  __DATA.__const: 0x358
-  __DATA.__cfstring: 0x7c0
+  __TEXT.__cstring: 0x1b06
+  __TEXT.__objc_classname: 0x92
+  __TEXT.__objc_methname: 0x1a58
+  __TEXT.__objc_methtype: 0x4f9
+  __TEXT.__gcc_except_tab: 0x130
+  __TEXT.__unwind_info: 0x230
+  __DATA.__const: 0x398
+  __DATA.__cfstring: 0x7e0
   __DATA.__objc_classlist: 0x20
   __DATA.__objc_catlist: 0x8
   __DATA.__objc_protolist: 0x18
   __DATA.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0x960
-  __DATA.__objc_selrefs: 0x740
+  __DATA.__objc_const: 0x948
+  __DATA.__objc_selrefs: 0x760
   __DATA.__objc_superrefs: 0x10
   __DATA.__objc_ivar: 0x74
   __DATA.__objc_data: 0x140
   __DATA.__data: 0x120
   __DATA.__objc_arraydata: 0x30
   __DATA.__objc_arrayobj: 0x48
+  __DATA.__auth_got: 0x378
+  __DATA.__got: 0x128
+  __DATA.__auth_ptr: 0x8
   __DATA.__bss: 0x30
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 51C0AF2B-911C-3C4F-94A3-1FA3C263151A
-  Functions: 154
-  Symbols:   193
-  CStrings:  713
+  UUID: CFBE8888-75DC-35BA-B01A-8E0440DEC492
+  Functions: 160
+  Symbols:   198
+  CStrings:  721
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x23
+ _objc_retain_x3
+ _objc_retain_x4
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x26
CStrings:
+ "-[MBSuspendingClock clockByAddingPositiveTimeInterval:]"
+ "/private/var/mobile/Library/Caches/Backup/DT"
+ "/private/var/tmp/backupd-XXXXXXXXXXXXXXX"
+ "@24@0:8Q16"
+ "@24@0:8d16"
+ "@40@0:8@16@24^@32"
+ "B32@?0@\"MBFileSystemSnapshot\"8Q16^B24"
+ "MBSuspendingClock.m"
+ "Q24@0:8^@16"
+ "Snapshot %@ not found for volume %@"
+ "Unable to create /private/var/tmp/backupd-XXXXXXXXXX directory"
+ "Unable to create /private/var/tmp/backupd-XXXXXXXXXX directory (mkdtemp)"
+ "Unable to create /private/var/tmp/backupd-XXXXXXXXXX directory (strdup)"
+ "_initWithStartTime:"
+ "clockByAddingPositiveTimeInterval:"
+ "countOfSnapshotsForAllPersonae:"
+ "findSnapshotWithName:forVolume:error:"
+ "indexesOfObjectsPassingTest:"
+ "interval >= 0"
+ "set"
+ "unionSet:"
+ "v52@0:8@\"MBManager\"16f24Q28Q36@\"NSString\"44"
+ "v52@0:8@16f24Q28Q36@44"
- "/var/mobile/Library/Caches/Backup/DT"
- "/var/tmp/backupd-XXXXXXXXXXXXXXX"
- "Unable to create /var/tmp/backupd-XXXXXXXXXX directory"
- "Unable to create /var/tmp/backupd-XXXXXXXXXX directory (mkdtemp)"
- "Unable to create /var/tmp/backupd-XXXXXXXXXX directory (strdup)"
- "manager:didScanBundleWithID:bytesUsed:"
- "manager:didScanDomainWithName:forBundleID:bytesUsed:"
- "manager:didScanFiles:forDomainWithName:bundleID:"
- "v40@0:8@\"MBManager\"16@\"NSString\"24Q32"
- "v40@0:8@16@24Q32"
- "v48@0:8@\"MBManager\"16@\"NSSet\"24@\"NSString\"32@\"NSString\"40"
- "v48@0:8@\"MBManager\"16@\"NSString\"24@\"NSString\"32Q40"
- "v48@0:8@16@24@32@40"
- "v48@0:8@16@24@32Q40"
- "v52@0:8@\"MBManager\"16f24Q28q36@\"NSString\"44"
- "v52@0:8@16f24Q28q36@44"

```
