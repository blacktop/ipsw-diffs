## livefiles_hfs.dylib

> `/System/Library/PrivateFrameworks/UserFS.framework/PlugIns/livefiles_hfs.dylib`

```diff

-715.120.1.0.0
-  __TEXT.__text: 0x3d944
+715.120.4.0.0
+  __TEXT.__text: 0x3db14
   __TEXT.__auth_stubs: 0x470
   __TEXT.__const: 0x4e60
-  __TEXT.__oslogstring: 0x5bb4
+  __TEXT.__oslogstring: 0x5c74
   __TEXT.__cstring: 0x26fb
   __TEXT.__unwind_info: 0x6d8
   __DATA_CONST.__got: 0x30

   __DATA.__common: 0x100
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /usr/lib/libSystem.B.dylib
-  UUID: 7171AD62-8980-392E-AB6F-35EBD9B96163
+  UUID: B39D209B-8E67-3148-B2EB-74B5E498E57D
   Functions: 677
   Symbols:   1163
-  CStrings:  734
+  CStrings:  738
 
Functions:
~ _getkey : 296 -> 356
~ _hfs_vnop_getxattr : 2016 -> 2228
~ _hfs_vnop_setxattr : 2692 -> 2900
~ _remove_attribute_records : 988 -> 964
~ _replay_journal : 5972 -> 5980
CStrings:
+ "hfs_getxattr: %s has a malformed attr extent\n"
+ "hfs_getxattr: %s has a malformed overflow extent\n"
+ "hfs_setxattr: %s has a malformed attr extent\n"
+ "hfs_setxattr: %s has a malformed overflow extent\n"

```
