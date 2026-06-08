## newfs_exfat

> `/System/Library/Filesystems/exfat.fs/newfs_exfat`

```diff

-522.100.20.0.0
-  __TEXT.__text: 0x345c
+560.0.0.0.0
+  __TEXT.__text: 0x353c
   __TEXT.__auth_stubs: 0x380
   __TEXT.__const: 0x4a58
-  __TEXT.__cstring: 0xed0
-  __TEXT.__unwind_info: 0xd8
+  __TEXT.__cstring: 0xecf
+  __TEXT.__unwind_info: 0xe0
+  __DATA_CONST.__cfstring: 0x60
   __DATA_CONST.__auth_got: 0x1c0
   __DATA_CONST.__got: 0x30
-  __DATA_CONST.__cfstring: 0x60
   __DATA.__data: 0x1ee3
   __DATA.__common: 0x68
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libutil.dylib
-  UUID: E59B5B36-B811-3DA7-AB48-198B30A8210B
-  Functions: 56
+  UUID: E612EF75-85E4-306A-B253-B09F05812098
+  Functions: 57
   Symbols:   65
   CStrings:  107
 
CStrings:
+ "Partition offset was not initialized, setting to default value (%d)\n"
- "Partition offset was not initialized , setting to default value (%d)\n"

```
