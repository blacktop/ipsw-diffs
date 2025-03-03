## fsck_apfs

> `/System/Library/Filesystems/apfs.fs/fsck_apfs`

```diff

-2332.100.53.0.6
-  __TEXT.__text: 0x4ca04
+2332.100.75.502.1
+  __TEXT.__text: 0x4cb74
   __TEXT.__auth_stubs: 0x930
-  __TEXT.__cstring: 0x186b3
+  __TEXT.__cstring: 0x187bc
   __TEXT.__const: 0x8104
   __TEXT.__unwind_info: 0xa30
   __DATA_CONST.__auth_got: 0x498

   - /usr/lib/libutil.dylib
   Functions: 824
   Symbols:   164
-  CStrings:  1847
+  CStrings:  1850
 
CStrings:
+ "%s (id %llu): invalid dir-stats flags (0x%x) on volume without attribution tags\n"
+ "%s (id %llu): invalid internal_flags (0x%llx) given apfs_fs_flags (0x%llx) PFK bit\n"
+ "%s (id %llu): invalid internal_flags (0x%llx) given volume readonly compatible features (0x%llx)\n"
+ "2332.100.75.502.1"
- "2332.100.53.0.6"

```
