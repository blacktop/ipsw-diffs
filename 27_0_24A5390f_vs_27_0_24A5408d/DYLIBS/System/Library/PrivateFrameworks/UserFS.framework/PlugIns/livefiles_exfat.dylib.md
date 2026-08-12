## livefiles_exfat.dylib

> `/System/Library/PrivateFrameworks/UserFS.framework/PlugIns/livefiles_exfat.dylib`

```diff

-561.0.1.0.0
-  __TEXT.__text: 0x1bf50
+561.0.3.0.0
+  __TEXT.__text: 0x1c0c8
   __TEXT.__const: 0x4b78
-  __TEXT.__oslogstring: 0x4745
+  __TEXT.__oslogstring: 0x47f5
   __TEXT.__cstring: 0x70d
   __TEXT.__unwind_info: 0x258
   __TEXT.__objc_stubs: 0x0

   - /System/Library/PrivateFrameworks/LiveFS.framework/LiveFS
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 181
-  Symbols:   285
-  CStrings:  439
+  Functions: 182
+  Symbols:   286
+  CStrings:  441
 
Symbols:
+ _FAT_Access_M_FatBlockSize
Functions:
~ _FSOPS_ReadBootSector : 2064 -> 2224
~ _FAT_Access_M_GetFatEntry : 1188 -> 1196
+ _FAT_Access_M_FatBlockSize
CStrings:
+ "FAT_Access_M_FatBlockSize: block offset %llu is at/past FAT end %llu\n"
+ "FSOPS_ReadBootSector: FAT too small for ClusterCount: FatLength=%u sectors (%llu bytes), ClusterCount=%u\n"
```
