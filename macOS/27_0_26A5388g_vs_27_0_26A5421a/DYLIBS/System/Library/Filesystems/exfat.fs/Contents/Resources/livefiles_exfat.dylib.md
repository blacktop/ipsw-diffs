## livefiles_exfat.dylib

> `/System/Library/Filesystems/exfat.fs/Contents/Resources/livefiles_exfat.dylib`

```diff

-561.0.1.0.0
-  __TEXT.__text: 0x1c10c
+561.0.3.0.0
+  __TEXT.__text: 0x1c284
   __TEXT.__const: 0x4b78
-  __TEXT.__oslogstring: 0x474f
+  __TEXT.__oslogstring: 0x47ff
   __TEXT.__cstring: 0x732
   __TEXT.__unwind_info: 0x260
   __TEXT.__objc_stubs: 0x0

   - /System/Library/PrivateFrameworks/LiveFS.framework/Versions/A/LiveFS
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 183
-  Symbols:   290
-  CStrings:  440
+  Functions: 184
+  Symbols:   291
+  CStrings:  442
 
Symbols:
+ _FAT_Access_M_FatBlockSize
Functions:
~ _FSOPS_ReadBootSector : 2076 -> 2236
~ _FAT_Access_M_GetFatEntry : 1188 -> 1196
+ _FAT_Access_M_FatBlockSize
CStrings:
+ "FAT_Access_M_FatBlockSize: block offset %llu is at/past FAT end %llu\n"
+ "FSOPS_ReadBootSector: FAT too small for ClusterCount: FatLength=%u sectors (%llu bytes), ClusterCount=%u\n"
```
