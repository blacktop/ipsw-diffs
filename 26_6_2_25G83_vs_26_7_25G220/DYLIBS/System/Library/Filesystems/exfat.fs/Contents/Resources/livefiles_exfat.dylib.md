## livefiles_exfat.dylib

> `/System/Library/Filesystems/exfat.fs/Contents/Resources/livefiles_exfat.dylib`

```diff

-522.100.20.0.0
-  __TEXT.__text: 0x1cb18
+522.100.20.700.1
+  __TEXT.__text: 0x1ccc0
   __TEXT.__auth_stubs: 0x430
   __TEXT.__const: 0x4b78
-  __TEXT.__oslogstring: 0x46e2
+  __TEXT.__oslogstring: 0x4792
   __TEXT.__cstring: 0x732
   __TEXT.__unwind_info: 0x258
   __TEXT.__objc_methname: 0x157

   - /System/Library/PrivateFrameworks/LiveFS.framework/Versions/A/LiveFS
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 184
-  Symbols:   291
-  CStrings:  447
+  Functions: 185
+  Symbols:   292
+  CStrings:  449
 
Symbols:
+ _FAT_Access_M_FatBlockSize
Functions:
~ _FSOPS_ReadBootSector : 2120 -> 2280
~ _FAT_Access_M_GetFatEntry : 1136 -> 1148
+ _FAT_Access_M_FatBlockSize
CStrings:
+ "FAT_Access_M_FatBlockSize: block offset %llu is at/past FAT end %llu\n"
+ "FSOPS_ReadBootSector: FAT too small for ClusterCount: FatLength=%u sectors (%llu bytes), ClusterCount=%u\n"
```
