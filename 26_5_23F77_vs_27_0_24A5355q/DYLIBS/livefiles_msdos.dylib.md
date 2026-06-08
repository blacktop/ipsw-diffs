## livefiles_msdos.dylib

> `/System/Library/PrivateFrameworks/UserFS.framework/PlugIns/livefiles_msdos.dylib`

```diff

-788.100.31.0.0
-  __TEXT.__text: 0x19ad4
-  __TEXT.__auth_stubs: 0x430
+844.0.0.0.0
+  __TEXT.__text: 0x19150
   __TEXT.__const: 0x4da0
   __TEXT.__oslogstring: 0x45d9
   __TEXT.__cstring: 0x71f
   __TEXT.__unwind_info: 0x260
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
   __DATA.__data: 0x165
   __DATA.__common: 0x18
   __DATA.__bss: 0x10

   - /System/Library/PrivateFrameworks/LiveFS.framework/LiveFS
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 291CBAA2-E1F8-3121-9BD5-0F7524DC76BA
+  UUID: 08D3E5D3-8756-3444-A8AD-D1712D0BE850
   Functions: 186
   Symbols:   350
-  CStrings:  429
+  CStrings:  422
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleasedReturnValue
Functions:
~ _msdosfs_unicode2dos : 320 -> 324
~ _msdosfs_dos2unicodefn : 296 -> 316
~ _msdosfs_unicode_to_dos_name : 944 -> 960
~ _msdosfs_apply_generation_to_short_name : 176 -> 192
~ _msdosfs_unicode2winfn : 220 -> 232
~ _msdosfs_winChkName : 456 -> 492
~ _msdosfs_getunicodefn : 272 -> 284
~ _MSDOS_Init : 224 -> 180
~ _MSDOS_Mount : 1372 -> 1328
~ _MSDOS_Sync : 328 -> 284
~ _MSDOS_Sync_async : 328 -> 284
~ _MSDOS_Unmount : 520 -> 476
~ _FSOPS_InitReadBootSectorAndSetFATType : 3956 -> 3952
~ _FSOPS_validateBootSectorSignature : 444 -> 400
~ _FSOPS_CopyVolumeLabel : 500 -> 468
~ _msdos_sync_interal : 568 -> 524
~ _metaWrite : 528 -> 480
~ _metaRead : 568 -> 520
~ _metaFlush : 340 -> 292
~ _metaClear : 396 -> 348
~ _metaPurge : 348 -> 300
~ _ZeroFill_DeInit : 236 -> 192
~ _ZeroFill_Fill : 332 -> 288
~ _ZeroFill_FillClusterSuffixWithZeros : 272 -> 228
~ _FILERECORD_AllocateRecord : 1360 -> 1364
~ _FILERECORD_FreeRecord : 380 -> 336
~ _FILERECORD_GetChainFromCache : 1868 -> 1824
~ _FILERECORD_FindClusterToCreateChainCacheEntry : 884 -> 840
~ _FILERECORD_GetClusterFromChainArray : 504 -> 460
~ _FILERECORD_AddChainCacheEntryToMainList : 348 -> 356
~ _MSDOS_GetAttrFromDirEntry : 1208 -> 1172
~ _MSDOS_Inactive : 528 -> 484
~ _FILEOPS_FreeUnusedPreAllocatedClusters : 680 -> 636
~ _MSDOS_Reclaim : 524 -> 480
~ _MSDOS_ReadLink : 1332 -> 1292
~ _MSDOS_Read : 720 -> 676
~ _MSDOS_Write : 2732 -> 2688
~ _MSDOS_BeginBlockmap : 2576 -> 2412
~ _FILEOPS_FetchFileExtents : 648 -> 604
~ _FILEOPS_CreateBlockmapRequestEntry : 320 -> 276
~ _MSDOS_EndBlockmap : 1904 -> 1828
~ _MSDOS_Create : 1384 -> 1392
~ _MSDOS_SymLink : 1376 -> 1380
~ _DIROPS_CreateLinkAccordingToContent : 940 -> 888
~ _MSDOS_Rename : 4068 -> 4076
~ _FILEOPS_PreAllocateClusters : 996 -> 952
~ _FileOPS_FillFileSuffixWithZeros : 664 -> 620
~ _FAT_Access_M_FlushCacheEntry : 404 -> 360
~ _FAT_Access_M_ContiguousClustersInChain : 376 -> 332
~ _FAT_Access_M_GetFatEntry : 944 -> 900
~ _FAT_Access_M_ChainLength : 624 -> 580
~ _FAT_Access_M_FATChainFree : 604 -> 560
~ _FAT_Access_M_AllocateClusters : 1736 -> 1692
~ _FAT_Access_M_TruncateLastClusters : 512 -> 480
~ _FATMOD_SetDriveDirtyBit : 576 -> 536
~ _FAT_Access_M_GetTotalFreeClusters : 328 -> 284
~ _FAT_Access_M_FATChainAlloc : 364 -> 308
~ _ht_insert : 564 -> 520
~ _ht_remove : 620 -> 576
~ _ht_free_all : 124 -> 128
~ _CONV_UTF8ToUnistr255 : 1324 -> 1364
~ _CONV_Unistr255ToUTF8 : 836 -> 840
~ _CONV_Unistr255ToLowerCase : 56 -> 60
~ _CONV_UTF8ToLowerCase : 200 -> 204
~ _CONV_ConvertToFSM : 120 -> 124
~ _CONV_LabelUTF8ToUTF16LocalEncoding : 332 -> 344
~ _RAWFILE_read : 1236 -> 1192
~ _RAWFILE_write : 1440 -> 1396
~ _DIROPS_UpdateDirLastModifiedTime : 512 -> 468
~ _DIROPS_AllocateDirBlockBuffer : 332 -> 288
~ _DIROPS_GetDirBlockRelative : 1112 -> 1116
~ _DIROPS_FreeDirBlockBuffer : 280 -> 212
~ _DIROPS_GetMD5Digest : 216 -> 220
~ _DIROPS_VerifyIfLinkAndGetLinkLength : 220 -> 224
~ _DIROPS_CreateShortNameEntry : 1192 -> 1196
~ _DIROPS_LookForDirEntryByName : 1360 -> 1316
~ _DIROPS_LookupInternal : 872 -> 876
~ _DIROPS_GetRecordId : 856 -> 808
~ _DIROPS_ReadDirInternal : 2784 -> 2816
~ _DIROPS_GetFileDirEntryDataByOffset : 640 -> 596
~ _DIROPS_GetDirEntryByOffset : 1468 -> 1436
~ _DIROPS_HandleLongNameCharacter : 88 -> 92
~ _DIROPS_MarkNodeDirEntriesAsDeleted : 1224 -> 1180
~ _DIROPS_LookForDirEntry : 2700 -> 2712
~ _DIROPS_UpdateDirectoryEntry : 1188 -> 1144
~ _DIROPS_VerifyCookie : 1168 -> 1124
CStrings:
- "clearMetaBlocks:ranges:rangesCount:wait:"
- "defaultClient"
- "flushMeta:wait:"
- "purgeMetaBlocks:ranges:rangesCount:"
- "readMeta:buffer:offset:length:"
- "readMetaWithRA:buffer:offset:length:raList:raListCount:"
- "writeMeta:buffer:offset:length:"

```
