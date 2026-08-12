## livefiles_apfs.dylib

> `/System/Library/PrivateFrameworks/UserFS.framework/PlugIns/livefiles_apfs.dylib`

```diff

-3283.0.13.0.0
-  __TEXT.__text: 0xb19ec
+3288.2.1.0.0
+  __TEXT.__text: 0xb1a28
   __TEXT.__const: 0x86b0
   __TEXT.__oslogstring: 0x16438
-  __TEXT.__cstring: 0x5c33
-  __TEXT.__unwind_info: 0x1090
+  __TEXT.__cstring: 0x5c35
+  __TEXT.__unwind_info: 0x10a0
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x3c8
   __DATA_CONST.__got: 0x0

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libutil.dylib
-  Functions: 2581
-  Symbols:   1505
+  Functions: 2582
+  Symbols:   1506
   CStrings:  2243
 
Symbols:
+ _decrement_dstream_id_for_deletion_ex
Functions:
~ _fs_delete_inode_internal : 836 -> 840
~ _decrement_dstream_id_for_deletion : 832 -> 12
+ _decrement_dstream_id_for_deletion_ex
CStrings:
+ "3288.2.1"
+ "decrement_dstream_id_for_deletion_ex"
- "3283.0.13"
- "decrement_dstream_id_for_deletion"
```
