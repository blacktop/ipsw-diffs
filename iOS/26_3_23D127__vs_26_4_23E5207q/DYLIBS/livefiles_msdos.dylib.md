## livefiles_msdos.dylib

> `/System/Library/PrivateFrameworks/UserFS.framework/PlugIns/livefiles_msdos.dylib`

```diff

-788.40.4.0.0
-  __TEXT.__text: 0x19b54
+788.100.30.0.0
+  __TEXT.__text: 0x19ad4
   __TEXT.__auth_stubs: 0x430
   __TEXT.__const: 0x4da0
-  __TEXT.__oslogstring: 0x458b
-  __TEXT.__cstring: 0x707
-  __TEXT.__unwind_info: 0x278
+  __TEXT.__oslogstring: 0x45d9
+  __TEXT.__cstring: 0x71f
+  __TEXT.__unwind_info: 0x260
   __TEXT.__objc_methname: 0xe2
   __TEXT.__objc_stubs: 0xe0
   __DATA_CONST.__got: 0x20

   - /System/Library/PrivateFrameworks/LiveFS.framework/LiveFS
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 63818290-7105-3381-85A6-1AB839BEEB69
+  UUID: D05B974B-827A-395A-8791-EAFADB100ED0
   Functions: 186
   Symbols:   350
-  CStrings:  427
+  CStrings:  429
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
- _objc_claimAutoreleasedReturnValue
Functions:
~ _msdosfs_unicode_to_dos_name : 948 -> 944
~ _msdosfs_winSlotCnt : 60 -> 56
~ _MSDOS_Taste : 580 -> 564
~ _MSDOS_Unmount : 524 -> 520
~ _MSDOS_ScanVols : 1104 -> 1100
~ _FSOPS_InitReadBootSectorAndSetFATType : 3952 -> 3956
~ _FSOPS_validateBootSectorSignature : 420 -> 444
~ _msdos_sync_interal : 572 -> 568
~ _metaWrite : 516 -> 528
~ _metaRead : 556 -> 568
~ _metaFlush : 316 -> 340
~ _metaClear : 372 -> 396
~ _metaPurge : 324 -> 348
~ _FILERECORD_RemoveChainCacheEntry : 88 -> 80
~ _FILERECORD_GetChainFromCache : 1884 -> 1868
~ _FILERECORD_UpdateNewAllocatedClustersInChain : 572 -> 564
~ _FILERECORD_AddChainCacheEntryToMainList : 352 -> 348
~ _MSDOS_SetAttrToDirEntry : 2396 -> 2392
~ _MSDOS_GetAttrFromDirEntry : 1212 -> 1208
~ _MSDOS_Inactive : 540 -> 528
~ _MSDOS_Reclaim : 536 -> 524
~ _MSDOS_Write : 2760 -> 2732
~ _MSDOS_BeginBlockmap : 2580 -> 2576
~ _FILEOPS_FetchFileExtents : 652 -> 648
~ _MSDOS_EndBlockmap : 1916 -> 1904
~ _MSDOS_Rename : 4072 -> 4068
~ _FAT_Access_M_FindFirstFreeClusterFromGivenCluster : 308 -> 304
~ _FAT_Access_M_FATChainFree : 608 -> 604
~ _FAT_Access_M_AllocateClusters : 1796 -> 1736
~ _FATMOD_SetDriveDirtyBit : 440 -> 576
~ _FAT_Access_M_FreeChainLength : 160 -> 156
~ _FAT_Access_M_FATChainAlloc : 372 -> 364
~ _ht_remove_from_list : 240 -> 248
~ _CONV_UTF8ToUnistr255 : 1344 -> 1324
~ _priortysort : 144 -> 140
~ _CONV_LabelUTF8ToUTF16LocalEncoding : 348 -> 332
~ _RAWFILE_read : 1248 -> 1236
~ _DIROPS_UpdateDirLastModifiedTime : 520 -> 512
~ _DIROPS_CreateNewEntry : 1668 -> 1664
~ _DIROPS_LookForFreeEntriesInDirectory : 1656 -> 1672
~ _DIROPS_SaveNewEntriesIntoDevice : 1244 -> 1192
~ _MSDOS_MkDir : 1512 -> 1508
~ _DIROPS_ReadDirInternal : 2864 -> 2784
~ _DIROPS_GetDirEntryByOffset : 1528 -> 1468
~ _DIROPS_MarkNodeDirEntriesAsDeleted : 1228 -> 1224
~ _DIROPS_PopulateHT : 892 -> 904
~ _DIROPS_isDirEmpty : 800 -> 824
~ _DIROPS_LookForDirEntry : 2620 -> 2700
~ _MSDOS_RmDir : 1272 -> 1276
~ _DIROPS_UpdateDirectoryEntry : 1208 -> 1188
~ _MSDOS_ScanDir : 776 -> 760
~ _DIROPS_GetDirEntryOffsetByIndex : 948 -> 952
CStrings:
+ "%s: The device is gone. Setting the in-memory copy of the dirty bit to [%d].\n"
+ "FATMOD_SetDriveDirtyBit"

```
