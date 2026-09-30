## slurpAPFSMeta

> `/System/Library/Filesystems/apfs.fs/Contents/Resources/slurpAPFSMeta`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-3283.0.9.501.1
-  __TEXT.__text: 0x374ec
+3283.0.13.501.1
+  __TEXT.__text: 0x376f0
   __TEXT.__auth_stubs: 0x830
-  __TEXT.__cstring: 0x8b8d
+  __TEXT.__cstring: 0x8c68
   __TEXT.__const: 0x1b0
   __TEXT.__unwind_info: 0x6b0
   __DATA_CONST.__const: 0x470

   - /usr/lib/libSystem.B.dylib
   Functions: 533
   Symbols:   144
-  CStrings:  753
+  CStrings:  757
 
Functions:
~ sub_100009778 : 596 -> 640
~ sub_10001ba38 -> sub_10001ba64 : 632 -> 636
~ sub_1000218c8 -> sub_1000218f8 : 4160 -> 4172
~ sub_100022c7c -> sub_100022cb8 : 3476 -> 3504
~ sub_10002656c -> sub_1000265c4 : 180 -> 172
~ sub_100032494 -> sub_1000324e4 : 1204 -> 1640
CStrings:
+ "%s:%d: %s Invalid reap list free entry %d\n"
+ "%s:%d: %s reap list object expected %u entries, max %u, but we walked %u\n"
+ "%s:%d: %s reap list object expected %u entries, max %u, but we walked %u + %u = %u\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XQJT3Z/Sources/apfs_executables/nx/obj.c"
+ "apfs_sanity_check"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qgu8Kl/Sources/apfs_executables/nx/obj.c"
```
