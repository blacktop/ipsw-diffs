## livefiles_exfat.dylib

> `/System/Library/PrivateFrameworks/UserFS.framework/PlugIns/livefiles_exfat.dylib`

```diff

-522.100.20.0.0
-  __TEXT.__text: 0x1c8fc
-  __TEXT.__auth_stubs: 0x430
+560.0.0.0.0
+  __TEXT.__text: 0x1be14
   __TEXT.__const: 0x4b78
-  __TEXT.__oslogstring: 0x46d8
+  __TEXT.__oslogstring: 0x4745
   __TEXT.__cstring: 0x70d
   __TEXT.__unwind_info: 0x258
-  __TEXT.__objc_methname: 0xe2
-  __TEXT.__objc_stubs: 0xe0
-  __DATA_CONST.__got: 0x20
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_methname: 0x0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x38
-  __AUTH_CONST.__auth_got: 0x220
-  __AUTH.__data: 0x140
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__auth_got: 0x0
+  __AUTH.__data: 0x148
   __DATA.__data: 0x27
   __DATA.__common: 0x18
   __DATA.__bss: 0x10

   - /System/Library/PrivateFrameworks/LiveFS.framework/LiveFS
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 96D7CBF9-C259-3F99-82A6-AFB8C8F7B007
-  Functions: 182
-  Symbols:   349
-  CStrings:  446
+  UUID: 91DDF4FA-2910-3DAE-A9B1-7B1091912D64
+  Functions: 181
+  Symbols:   346
+  CStrings:  441
 
Symbols:
+ _CONV_NormalizeUnistr255ToPrecomposed
+ _objc_claimAutoreleasedReturnValue
- _OUTLINED_FUNCTION_1
- _OUTLINED_FUNCTION_2
- _objc_retainAutoreleasedReturnValue
Functions:
~ _FSOPS_SetDeviceAsDirty : 296 -> 252
~ _EXFAT_Init : 276 -> 232
~ _EXFAT_Taste : 584 -> 540
~ _EXFAT_Mount : 960 -> 916
~ _EXFAT_Sync : 488 -> 444
~ _EXFAT_Sync_async : 488 -> 444
~ _EXFAT_Unmount : 484 -> 440
~ _EXFAT_GetFSAttr : 1964 -> 1920
~ _EXFAT_SetFSAttr : 1220 -> 1176
~ _EXFAT_ScanVols : 1256 -> 1212
~ _FSOPS_ReadBootSector : 2108 -> 2068
~ _FSOPS_CreateRootRecord : 1572 -> 1524
~ _FSOPS_lookupVolumeLabel : 772 -> 724
~ _FSOPS_ReadUpcase : 1272 -> 1240
~ _exfat_sync_internal : 464 -> 420
~ _RAWFILE_read : 1276 -> 1236
~ _RAWFILE_write : 1520 -> 1476
~ _metaWrite : 520 -> 472
~ _metaWriteSync : 520 -> 472
~ _metaRead : 560 -> 512
~ _metaFlush : 320 -> 276
~ _metaClear : 376 -> 328
~ _metaPurge : 328 -> 284
~ _ZeroFill_DeInit : 236 -> 192
~ _ZeroFill_Fill : 332 -> 288
~ _ZeroFill_FillClusterSuffixWithZeros : 272 -> 228
- _OUTLINED_FUNCTION_1
- _FILEOPS_GetFileAllocatedSize
~ _FileOPS_SetAttrToDirEntry : 2044 -> 1992
~ _FileOPS_FillFileSuffixWithZeros : 664 -> 620
~ _FILEOPS_GetAtrrFromDirEntry : 548 -> 552
~ _EXFAT_Read : 824 -> 780
~ _EXFAT_Write : 2556 -> 2552
~ _EXFAT_BeginBlockmap : 2628 -> 2564
~ _FILEOPS_FetchFileExtents : 816 -> 772
~ _FILEOPS_CreateBlockmapRequestEntry : 336 -> 292
~ _EXFAT_EndBlockmap : 1868 -> 1748
~ _EXFAT_Create : 1420 -> 1376
~ _EXFAT_Inactive : 936 -> 892
~ _EXFAT_Reclaim : 796 -> 752
~ _EXFAT_ReadLink : 1128 -> 1092
~ _EXFAT_SymLink : 1392 -> 1348
~ _DIROPS_CreateLinkAccordingToContent : 944 -> 904
~ _EXFAT_Rename : 4612 -> 4600
~ _FILEOPS_PreAllocateClusters : 1168 -> 1124
~ _FILEOPS_FlushDirEntryIfNeeded : 316 -> 272
~ _CONV_UTF8ToUnistr255 : 1324 -> 1360
~ _CONV_Unistr255ToUTF8 : 872 -> 876
~ _CONV_Unistr255ToUpperCase : 56 -> 60
~ _CONV_UnistrUTF8ToUpperCase : 204 -> 208
+ _CONV_NormalizeUnistr255ToPrecomposed
~ _DIROPS_ChecksumFileSet : 76 -> 80
~ _DIROPS_GetFileDirEntryDataByOffset : 624 -> 580
~ _DIROPS_GetDirEntryByOffset : 3284 -> 3244
~ _DIROPS_isDirEmpty : 964 -> 920
~ _DIROPS_AllocateDirBlockBuffer : 316 -> 272
~ _DIROPS_FreeDirBlockBuffer : 280 -> 212
~ _DIROPS_GetMD5Digest : 216 -> 220
~ _DIROPS_VerifyIfLinkAndGetLinkLength : 220 -> 224
~ _DIROPS_GetRecordId : 876 -> 832
~ _DIROPS_LookForDirEntryByName : 1552 -> 1716
~ _DIROPS_LookForDirEntry : 2668 -> 2932
~ _DIROPS_CreateNewEntry : 2240 -> 2196
~ _DIROPS_LookForFreeEntriesInDirectory : 2140 -> 2080
~ _DIROPS_CreateFileEntrySet : 800 -> 808
~ _DIROPS_SaveNewEntriesIntoDevice : 1000 -> 956
~ _DIROPS_UpdateDirLastModifiedTime : 364 -> 316
~ _DIROPS_MarkNodeDirEntriesAsDeleted : 1364 -> 1320
~ _DIROPS_PopulateHT : 1008 -> 1224
~ _DIROPS_UpdateDirectoryEntries : 2804 -> 2768
~ _DIROPS_ReadDirInternal : 2872 -> 2784
~ _EXFAT_MkDir : 1428 -> 1384
~ _DIROPS_ClearNewDirectoryClusters : 724 -> 892
~ _DIROPS_LookupInternal : 732 -> 692
~ _EXFAT_RmDir : 1360 -> 1312
~ _EXFAT_Remove : 1128 -> 1084
~ _EXFAT_ScanDir : 944 -> 900
~ _DIROPS_VerifyCookie : 880 -> 836
~ _DIROPS_GetDirEntryOffsetByIndex : 916 -> 872
~ _DIROPS_WriteVolumeLableEntry : 1312 -> 1300
~ _ht_insert : 568 -> 524
~ _ht_remove : 604 -> 560
~ _ht_free_all : 124 -> 128
~ _FILERECORD_AllocateRecord : 1308 -> 1312
~ _FILERECORD_FreeRecord : 400 -> 356
~ _FILERECORD_GetChainFromCache : 1840 -> 1796
~ _FILERECORD_FindClusterToCreateChainCacheEntry : 976 -> 932
~ _FILERECORD_GetClusterFromChainArray : 504 -> 460
~ _FILERECORD_AddChainCacheEntryToMainList : 348 -> 356
~ _FAT_Access_M_GetFatEntry : 1136 -> 1092
~ _FAT_Access_M_ContiguousClustersInChain : 360 -> 316
~ _FAT_Access_M_ChainLength : 496 -> 452
~ _FAT_Access_M_BitmapMap : 1468 -> 1424
~ _FATMOD_FlushAllCacheEntries : 736 -> 692
~ _FAT_Access_M_FlushCacheEntry : 520 -> 476
~ _FAT_Access_M_FATChainFree : 780 -> 736
~ _FAT_Access_M_BitmapMarkBits : 896 -> 852
~ _FAT_Access_M_AllocateClusters : 4288 -> 4252
~ _FAT_Access_M_FATChainAlloc : 352 -> 304
~ _FAT_Access_M_TruncateLastClusters : 524 -> 480
~ _FAT_Access_M_FlushPartialBitmapCache : 488 -> 444
~ _FAT_Access_M_MarkAllBitGivenRange : 556 -> 512
~ _FAT_Access_M_SetBitampCacheDirtyBitmap : 348 -> 304
~ _MultiReadSingleWrite_LockRead.cold.1 : 92 -> 76
~ _MultiReadSingleWrite_LockWrite.cold.1 : 92 -> 76
CStrings:
+ "%s: (%{private}s) got ENOENT with normalization enabled"
+ "%s: Failed normalizing UTF-16 file name. Error = %d."
- "clearMetaBlocks:ranges:rangesCount:wait:"
- "defaultClient"
- "flushMeta:wait:"
- "purgeMetaBlocks:ranges:rangesCount:"
- "readMeta:buffer:offset:length:"
- "readMetaWithRA:buffer:offset:length:raList:raListCount:"
- "writeMeta:buffer:offset:length:"

```
