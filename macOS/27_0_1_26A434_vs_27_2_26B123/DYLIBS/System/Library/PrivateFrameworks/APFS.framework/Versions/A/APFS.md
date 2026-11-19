## APFS

> `/System/Library/PrivateFrameworks/APFS.framework/Versions/A/APFS`

```diff

-3288.1.3.0.0
-  __TEXT.__text: 0x5722c
+3288.41.1.0.0
+  __TEXT.__text: 0x575e0
   __TEXT.__const: 0x8540
-  __TEXT.__cstring: 0xeada
+  __TEXT.__cstring: 0xeb4f
   __TEXT.__oslogstring: 0x1467
   __TEXT.__gcc_except_tab: 0x1c
-  __TEXT.__unwind_info: 0xa30
+  __TEXT.__unwind_info: 0xa48
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x528
   __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x400
-  __AUTH_CONST.__cfstring: 0x14e0
+  __AUTH_CONST.__cfstring: 0x1520
   __AUTH_CONST.__weak_auth_got: 0x8
   __AUTH_CONST.__auth_got: 0x688
   __AUTH_CONST.__auth_ptr: 0x0
-  __AUTH.__data: 0x148
-  __DATA.__data: 0x9c
+  __DATA.__data: 0xc
   __DATA.__bss: 0x48
-  __DATA.__common: 0x418
+  __DATA.__common: 0x420
+  __DATA_DIRTY.__data: 0x1d8
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libutil.dylib
-  Functions: 930
-  Symbols:   1173
-  CStrings:  1448
+  Functions: 932
+  Symbols:   1176
+  CStrings:  1452
 
Symbols:
+ _btree_node_val_space_total
+ _g_temp_checkpoint_protected
+ _is_fake_mount_node
CStrings:
+ "%s:%d: Temp checkpoint protection: refusing regular checkpoint mount\n"
+ "3288.41.1"
+ "IOMatchCategory"
+ "btree_node_compact"
+ "mount_apfs"
- "3288.1.3"
```
