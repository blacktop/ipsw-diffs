## fsck_hfs

> `/System/Library/Filesystems/hfs.fs/fsck_hfs`

```diff

-683.120.3.0.0
-  __TEXT.__text: 0x2ff70
-  __TEXT.__auth_stubs: 0x770
-  __TEXT.__const: 0x112c
-  __TEXT.__cstring: 0x6cab
+704.0.0.0.0
+  __TEXT.__text: 0x301b0
+  __TEXT.__auth_stubs: 0x7b0
+  __TEXT.__const: 0x111c
+  __TEXT.__cstring: 0x6cbc
   __TEXT.__unwind_info: 0x508
-  __DATA_CONST.__auth_got: 0x3b8
+  __DATA_CONST.__auth_got: 0x3d8
   __DATA_CONST.__got: 0x50
   __DATA_CONST.__auth_ptr: 0x20
   __DATA_CONST.__const: 0x370
   __DATA_CONST.__cfstring: 0x40
   __DATA.__data: 0x33e8
-  __DATA.__common: 0x50c8
-  __DATA.__bss: 0x185
+  __DATA.__common: 0x50e0
+  __DATA.__bss: 0x186
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
+  - /System/Library/PrivateFrameworks/FSKit.framework/FSKit
   - /usr/lib/libSystem.B.dylib
-  UUID: 1F6DEBBE-7BCF-332F-B864-62FF9A376A53
-  Functions: 468
-  Symbols:   134
-  CStrings:  780
+  UUID: D782815F-2D5A-346C-AFCE-F046E0C769AE
+  Functions: 471
+  Symbols:   138
+  CStrings:  781
 
Symbols:
+ _FSKitCheckDone
+ _FSKitCheckStart
+ _FSKitCheckUpdate
+ _os_variant_has_internal_content
CStrings:
+ "b:B:c:dD:e:EfgJlm:npqrR:SuxXy"
+ "com.apple.FSKit"
- "b:B:c:D:e:Edfglm:npqrR:SuyxJ"

```
