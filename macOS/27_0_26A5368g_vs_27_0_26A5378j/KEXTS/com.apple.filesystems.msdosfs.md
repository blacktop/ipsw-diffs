## com.apple.filesystems.msdosfs

> `com.apple.filesystems.msdosfs`

```diff

   __TEXT.__const: 0x2f8
-  __TEXT.__cstring: 0xe40
-  __TEXT_EXEC.__text: 0xc64c
+  __TEXT.__cstring: 0x1080
+  __TEXT_EXEC.__text: 0xc69c
   __TEXT_EXEC.__auth_stubs: 0x890
   __DATA.__data: 0x600
   __DATA.__common: 0x28

   __DATA_CONST.__got: 0x20
   Functions: 138
   Symbols:   357
-  CStrings:  79
+  CStrings:  88
 
Sections:
~ __DATA.__data : content changed
~ __DATA_CONST.__kalloc_type : content changed
~ __DATA_CONST.__auth_got : content changed
~ __DATA_CONST.__got : content changed
Symbols:
+ msdosfs_mount.kalloc_type_view_1078
+ msdosfs_vfs_unmount.kalloc_type_view_1159
- msdosfs_mount.kalloc_type_view_1017
- msdosfs_vfs_unmount.kalloc_type_view_1098
Functions:
~ _msdosfs_dos2unicodefn : 280 -> 276
~ _msdosfs_unicode_to_dos_name : 984 -> 940
~ _msdosfs_unicode2winfn : 260 -> 212
~ _msdosfs_winChkName : 512 -> 504
~ _msdosfs_getunicodefn : 344 -> 300
~ _msdosfs_createde : 1184 -> 1188
~ _msdosfs_mount : 2496 -> 2720
CStrings:
+ "msdosfs_mount: FAT cluster computation overflows\n"
+ "msdosfs_mount: FAT size overflows (fat_sectors=%u, BytesPerSec=%u)\n"
+ "msdosfs_mount: FSInfo sector conversion overflows\n"
+ "msdosfs_mount: device block size (%u) larger than logical sector size (%u)\n"
+ "msdosfs_mount: first cluster block conversion overflows\n"
+ "msdosfs_mount: first cluster offset overflows\n"
+ "msdosfs_mount: root directory block conversion overflows (BlocksPerSec=%u)\n"
+ "msdosfs_mount: root directory block overflows (FATs=%u, fat_sectors=%u, ResSectors=%u)\n"
+ "msdosfs_mount: root directory size overflows (RootDirEnts=%u)\n"

```
