## ChunkingLibrary

> `/System/Library/PrivateFrameworks/ChunkingLibrary.framework/ChunkingLibrary`

```diff

-2300.104.0.0.0
-  __TEXT.__text: 0x4c784
-  __TEXT.__auth_stubs: 0xe70
+2700.0.0.0.0
+  __TEXT.__text: 0x4b264
   __TEXT.__const: 0x11e6
   __TEXT.__cstring: 0xa763
   __TEXT.__oslogstring: 0x807
-  __TEXT.__unwind_info: 0xc28
-  __DATA_CONST.__got: 0x88
+  __TEXT.__unwind_info: 0xc20
+  __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x7f20
-  __AUTH_CONST.__auth_got: 0x738
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x84e0
   __AUTH_CONST.__cfstring: 0x40e0
+  __AUTH_CONST.__auth_got: 0x738
   __DATA.__bss: 0x8a
   __DATA_DIRTY.__data: 0x60
   __DATA_DIRTY.__bss: 0x1128

   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 9F187054-B606-38B5-A0B0-4689AB42C052
+  UUID: 0CBC660D-60A7-38C6-8AB8-B93787D93C3F
   Functions: 2839
   Symbols:   7860
   CStrings:  1545
Functions:
~ _CSopenDB : 3812 -> 3768
~ _CS_corruption_checking_sqlite3_open_v2 : 392 -> 348
~ __CSHandleDatabaseIOError : 284 -> 224
~ __CSHandleDatabaseIOError : 284 -> 224
~ _CS_corruption_checking_sqlite3_exec : 412 -> 368
~ _CS_corruption_checking_sqlite3_exec : 392 -> 348
~ _CSsql_corruption_checking_do : 364 -> 320
~ _CSsql_corruption_checking_do : 344 -> 300
~ _CSsql_doV : 616 -> 572
~ __CSBeginTransactionSqlRc : 532 -> 488
~ __CSEndTransactionSqlRc : 524 -> 480
~ __CSChunkStoreClose : 180 -> 184
~ _CScloseDB : 232 -> 192
~ __CSChunkStoreCSChunkStoreFinalize : 448 -> 404
~ __CSCopier_PermuteChunkSignature : 300 -> 308
~ __CSCopier_PermuteFORD : 328 -> 336
~ __CSCopier_PermuteFileSignature : 316 -> 332
~ _CSsql_get64 : 864 -> 820
~ _CSsql_get64_safe : 1064 -> 1020
~ __CSMigrateChunkStore : 756 -> 720
~ __CSRetainChunk : 356 -> 312
~ _CSReadChunkData : 444 -> 400
~ _CSChunkFile : 432 -> 388
~ _CKCopyDataForChunkID : 652 -> 608
~ __StoreChunk : 2824 -> 2780
~ __CSFlushChunkBatch : 540 -> 496
~ _CKRegisterFile : 484 -> 440
~ _CKRegisterTemporaryChunks : 176 -> 180
~ _CKRelocateTemporaryChunk : 632 -> 564
~ _chunkFdForStorage : 1148 -> 1100
~ _CSRegisterChunksForFileCallback : 416 -> 376
~ _getChunkListCacheBlob : 604 -> 560
~ _chunkItem : 13800 -> 13936
~ _CSchunklist_for_file : 1024 -> 984
~ _CKCopyChunkCache : 2432 -> 2360
~ _CKFixupChunkCacheAfterExchangeData : 2620 -> 2548
~ _openFdUncached : 384 -> 340
~ _CSfixed_subchunk_stream : 856 -> 816
~ _CSchunklist_add_stream : 1268 -> 1272
~ _CSchunklist_add : 1684 -> 1688
~ __CSCheckChunkStoreDB : 1656 -> 1664
~ _CKChunkStoreGetLocation : 340 -> 296
~ _CKChunkStoreRelocateDB : 716 -> 672
~ __CSRollbackTransactionSqlRc : 320 -> 276
~ _CS_sqlite3_step : 348 -> 304
~ __CSPrepareStatement : 744 -> 700
~ __CSAddStorageFileToDb : 512 -> 468
~ __CSRemoveStorageFileFromDb : 380 -> 340
~ __CSUpdateStorageFileInfo : 988 -> 944
~ __CSCacheStorageFile : 128 -> 132
~ __CSCloseStorageFile : 440 -> 408
~ __CSCloseCachedStorageFile : 56 -> 60
~ __CSGetStorageFile : 2412 -> 2408
~ __CSStoreChunks : 3720 -> 3728
~ __CSStorageFileForChunkSignature : 496 -> 452
~ __CSRecordPendingChunks : 476 -> 432
~ __CSCommitChunkedFile : 460 -> 420
~ __CSRemovePendingBatchesForInode : 916 -> 872
~ __CSRegisterStorageChunkList : 576 -> 532
~ __CSRemoveStoredFile : 1520 -> 1476
~ __CSChunkRefsForToken : 824 -> 784
~ __CSChunkSignatureForToken : 412 -> 368
~ __CSReleaseChunkForSignature : 2212 -> 2168
~ __CSChunkSizeForToken : 476 -> 428
~ __CSChunkIsInvalid : 432 -> 388
~ __CSTokenForChunkSignature : 476 -> 432
~ __CSAddChunk : 728 -> 684
~ __CSChunkForToken : 784 -> 740
~ __CSStorageFileInode : 1144 -> 1140
~ __CSRetainChunkForRowID : 1628 -> 1584
~ __CSRefCountForChunkWithRowID : 644 -> 576
~ _addRegisteredChunk : 568 -> 572
~ _addStoredChunk : 404 -> 408
~ __CSRegisterChunkList : 416 -> 372
~ __CSRegisterChunk : 720 -> 676
~ __CSGetRegisteredChunk : 660 -> 616
~ __CSGetRegisteredChunks : 752 -> 708
~ _registerItem : 1420 -> 1416
~ _unregisterItem : 636 -> 592
~ __CSUnregisterChunksForItem : 820 -> 776
~ __CSCopyChunkListForItemID : 624 -> 580
~ __CSGetItemIdsForFileSignature : 616 -> 572
~ __CSGetSignatureForItemID : 1728 -> 1684
~ __CSUnregisterAllTemporaryChunks : 396 -> 352
~ __CSUnregisterTemporaryChunks : 692 -> 648
~ __CSRelocateRegisteredChunk : 1404 -> 1360
~ __CSUnregisterChunk : 500 -> 456
~ __CSConvertTemporaryChunks : 436 -> 392
~ __CSKeyForRegisteredChunk : 1180 -> 1136
~ __CSUnregisterAllChunksForItem : 624 -> 580
~ __CSRegisteredItemCount : 404 -> 360
~ __CSGetRegisteredItems : 500 -> 460
~ __CSReleaseOrphanedChunks : 444 -> 408
~ _CSChunkCopier_Initialize : 416 -> 424
~ _CKChunkCryptorV1Finalize : 352 -> 308
~ _CKChunkCryptorV1Update : 348 -> 304
~ _CKFileSignatureSize : 316 -> 272
~ __CSBruteForceDatabaseCorruptionRecovery : 1192 -> 1148
~ __CSUnlinkAndLog : 392 -> 348
~ _CKChunkSignatureSize : 304 -> 260
~ _CKChunkEncryptionKeySize : 324 -> 280
~ _CSAttemptFirstAidForStorageFile : 1492 -> 1500
~ _CSAttemptAutomaticFirstAidForStorageFile : 476 -> 432
~ _CSrabin_init : 260 -> 264
~ _CSrabin_reset : 56 -> 60
~ _CSrabin_slide8 : 100 -> 104
~ _compute_ringing : 140 -> 148
~ _CKChunkCoderFinish : 596 -> 552
~ _CSCopyData : 860 -> 816
~ _idIsNull : 104 -> 108
~ _CShex_to_string : 92 -> 96
~ _printNbytes : 368 -> 372
~ _printSignature : 748 -> 712
~ _printChunk : 496 -> 504
~ _printChunkReference : 628 -> 584
~ _printStoredChunk : 1824 -> 1780
~ _printSourceChunk : 680 -> 636
~ _printRegisteredChunk : 304 -> 260
~ _printRegisteredChunkList : 88 -> 92
~ _ck_copy_cfnumber_from_cftype_using_description : 780 -> 736
~ _getFileSignatureCacheBlob : 424 -> 380
~ _getCacheBlob : 692 -> 680
~ _get2FileSignatureCache : 1068 -> 1024
~ _setFileSignatureCache : 1248 -> 1204
~ _wgcChanged : 368 -> 324
~ _CK2CalculateItemSignatureWithFlags : 2568 -> 2524
~ _CKValidateSignature : 636 -> 592
~ _CKRegisteredChunkKey : 60 -> 64
~ _CKRegisteredSubchunkDigest : 68 -> 72
~ _CKRegisteredChunkAtIndex : 60 -> 64
~ _CKStoredChunkAtIndex : 76 -> 80
~ _CKRegisteredChunkSignatureCopyCString : 148 -> 152
~ _CKRegisteredChunkKeyCopyCString : 164 -> 168
~ _readOpCtx : 424 -> 380
~ _getOpCtxSectionLengthAtIndex : 544 -> 512
~ _changeFileFlags : 1088 -> 1044
~ _getMaxXattrSize : 340 -> 296
~ _getFileWriteGeneration : 412 -> 368
~ _CKGetCacheBlobFd : 848 -> 804
~ _CKSetCacheBlobFd : 952 -> 908
~ _CS_corruption_causing_sqlite3_open_v2 : 372 -> 304
~ _CS_corruption_causing_sqlite3_step : 348 -> 280
~ _CS_corruption_causing_sqlite3_prepare_v2 : 392 -> 324
~ _CS_corruption_causing_sqlite3_exec : 392 -> 324
~ _CSSQLiteCorruptionTestingShouldCorrupt : 464 -> 432
~ _create_sqlite3_db_s_profile : 692 -> 652
~ _print_sections : 452 -> 412
~ _copy_lowercase_suffix_for_type_hint : 984 -> 980
~ _create_default_fixed_profile : 1788 -> 1744
~ _create_safe_rabin_profile : 980 -> 936
~ _create_custom_fixed_profile : 492 -> 448
~ _create_zip_profile : 8008 -> 7624
~ _create_sqlite3_db_wal_profile : 1176 -> 1152
~ _detect_magics : 676 -> 636
~ _locate_zip64_extra_field : 656 -> 624

```
