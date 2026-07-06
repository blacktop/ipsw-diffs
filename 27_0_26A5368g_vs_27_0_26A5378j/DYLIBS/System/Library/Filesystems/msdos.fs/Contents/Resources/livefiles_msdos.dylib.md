## livefiles_msdos.dylib

> `/System/Library/Filesystems/msdos.fs/Contents/Resources/livefiles_msdos.dylib`

```diff

-  __TEXT.__text: 0x19520
+  __TEXT.__text: 0x19690
   __TEXT.__const: 0x4da0
-  __TEXT.__oslogstring: 0x4605
+  __TEXT.__oslogstring: 0x4762
   __TEXT.__cstring: 0x744
   __TEXT.__unwind_info: 0x260
   __TEXT.__objc_stubs: 0x0

   - /usr/lib/libobjc.A.dylib
   Functions: 187
   Symbols:   298
-  CStrings:  424
+  CStrings:  428
 
Sections:
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __AUTH.__data : content changed
Functions:
~ _msdosfs_dos2unicodefn : 276 -> 272
~ _msdosfs_unicode_to_dos_name : 984 -> 940
~ _msdosfs_unicode2winfn : 248 -> 200
~ _msdosfs_winChkName : 492 -> 468
~ _msdosfs_getunicodefn : 324 -> 280
~ _FSOPS_InitReadBootSectorAndSetFATType : 3964 -> 4472
~ _FAT_Access_M_GetFatEntry : 940 -> 948
~ _FATMOD_FlushSpecificCacheEntry : 276 -> 284
~ _priortysort : 140 -> 148
CStrings:
+ "FSOPS_InitReadBootSectorAndSetFATType: FAT size overflows (fat_sectors=%u, bytes/sector=%u)\n"
+ "FSOPS_InitReadBootSectorAndSetFATType: cluster offset overflows\n"
+ "FSOPS_InitReadBootSectorAndSetFATType: device reported zero bytes-per-sector\n"
+ "FSOPS_InitReadBootSectorAndSetFATType: root directory block overflows (FATs=%u, fat_sectors=%u, res_sectors=%u)\n"

```
