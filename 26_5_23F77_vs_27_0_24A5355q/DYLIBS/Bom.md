## Bom

> `/System/Library/PrivateFrameworks/Bom.framework/Bom`

```diff

 277.0.0.0.0
-  __TEXT.__text: 0x5a478
-  __TEXT.__auth_stubs: 0x18d0
+  __TEXT.__text: 0x5a6a0
   __TEXT.__cstring: 0x129f6
   __TEXT.__const: 0x1728
   __TEXT.__oslogstring: 0x103e
-  __TEXT.__unwind_info: 0xac8
-  __DATA_CONST.__got: 0x70
+  __TEXT.__unwind_info: 0xad0
+  __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x9a0
-  __AUTH_CONST.__auth_got: 0xc68
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x180
   __AUTH_CONST.__cfstring: 0x11c0
+  __AUTH_CONST.__auth_got: 0xc68
   __DATA.__data: 0x168
   __DATA.__bss: 0x8dc
   __DATA_DIRTY.__data: 0x160

   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libbz2.1.0.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 5B346802-D27B-3C9B-8B27-5997642B61DD
+  UUID: 2F069176-9EE4-38F6-9F12-3A2ABB77F916
   Functions: 1095
   Symbols:   2156
   CStrings:  2532
Functions:
~ _BOM_strrncmp : 112 -> 116
~ _darc_format_entry_free : 276 -> 284
~ _BOMPatternListExtractFromFile : 340 -> 348
~ _BOMPatternListExtractFromStrings : 272 -> 280
~ _BOMFileClose : 1156 -> 1160
~ __BOMFileDirectRead : 948 -> 952
~ __BOMFileAsyncRead : 288 -> 292
~ _BOMFileWrite : 452 -> 460
~ __BOMFileDirectWrite : 500 -> 508
~ _BOMFileSeek : 644 -> 648
~ __BOMFileFinishGzipCompression : 344 -> 348
~ __BOMFileReadRaw : 180 -> 184
~ __BOMFileWriteRaw : 176 -> 180
~ _bom_crc32_finalize : 376 -> 380
~ _BOMCRC32ForBufferSegmentFinal : 380 -> 384
~ __readArchInfo : 208 -> 212
~ __writeArchInfo : 168 -> 172
~ _BOMBomNewFromBomWithOptions : 1456 -> 1468
~ _BOMBomNewFromDirectoryWithSys : 2200 -> 2204
~ __visitDir : 1316 -> 1336
~ _BOMBomPathIDAndArchsForKey : 272 -> 276
~ __addArchInfoForFSObject : 336 -> 340
~ __maskWithBom : 996 -> 968
~ _BOMBomApproximateBytesRepresentedByVariantWithBlockSize : 1132 -> 1164
~ _release_fts_agent_state : 292 -> 296
~ _populate_read_buffer : 240 -> 236
~ _parse_entry_posix_ustar : 3108 -> 3116
~ _data_archive_decoder_rewind_data : 312 -> 316
~ _parse_entry_pkzip_extra_field : 2716 -> 2788
~ _init_pkzip_cipher : 432 -> 436
~ _path_tree_node_release : 116 -> 120
~ _next_source_entry : 8164 -> 8112
~ _next_data_archive_entry : 508 -> 464
~ _populate_sequester_stack : 328 -> 332
~ _synthesize_filesystem_stuff : 2124 -> 2144
~ _adjust_filesystem_entry_path : 280 -> 284
~ _synthesize_replay_apple_double : 664 -> 620
~ ___add_sequester_entry_block_invoke : 796 -> 800
~ _path_tree_node_push : 540 -> 548
~ _BOMCopierDestinationFree : 596 -> 600
~ _make_path : 668 -> 624
~ _finalize_entry_filesystem : 6964 -> 6960
~ _BOMCopierDestinationEntryGetMatchRecord : 236 -> 240
~ _BOMCopierDestinationEntryWriteFatHeader : 712 -> 720
~ _BOMCopierDestinationEntryWrite : 728 -> 732
~ _BOMCopierCopySourceEntryToDestinationSet : 4140 -> 4104
~ _release_copy_state : 148 -> 156
~ _set_timestamps : 524 -> 476
~ _read_from_source : 276 -> 284
~ _BOMBomHLIndexCommit : 236 -> 240
~ _BOMCopierNewWithSys : 212 -> 216
~ __resetCopier : 784 -> 788
~ __prepareCopierState : 608 -> 612
~ __prepareCopierDestination : 652 -> 656
~ __BOMCopierCopyFromFilesystem : 2756 -> 2760
~ __BOMCopierCopyFromPKZip : 2124 -> 2128
~ __finalizeCopierDestination : 292 -> 296
~ _BOMCopierRedirectPath : 116 -> 120
~ _BOMCopierRedirectSourcePath : 116 -> 120
~ __initializeAFSCData : 184 -> 196
~ __copyFromFileToDir : 632 -> 644
~ __copyExtendedAttributes : 912 -> 916
~ __checkForDestinationConflict : 696 -> 700
~ __copyDir : 1868 -> 1896
~ __copyDataFork : 6480 -> 6552
~ __copyFromCPIO : 1888 -> 1892
~ __copyFromPKZip : 2020 -> 2092
~ __mergeAppleDouble : 592 -> 596
~ _BOMCopierPrepareMatchContext : 1332 -> 1336
~ _BOMCopierMatchBinary : 1092 -> 1096
~ _BOMFSOArchInfoGetArchSubtype : 40 -> 44
~ _BOMFSOArchInfoGetArchSize : 40 -> 44
~ _BOMFSOArchInfoThinKeepingArchs : 348 -> 356
~ _BOMFSOArchInfoThinKeepingArchsAndSubArchs : 384 -> 392
~ _BOMCopierSourceEntryNewFromPath : 1008 -> 1012
~ _BOMCopierSourceEntryFree : 584 -> 588
~ _parse_regular_file : 1408 -> 1416
~ _BOMCopierSourceEntryNewFromFTSENT : 1072 -> 1076
~ _BOMCopierSourceEntryNewFromFSObject : 1920 -> 1924
~ _BOMCopierSourceEntryNewFromLibarchive : 1016 -> 1012
~ _BOMCopierSourceEntryNewFromDataArchive : 1000 -> 996
~ _BOMCopierSourceEntryGetExtendedAttributeSize : 148 -> 152
~ _BOMCopierSourceEntryCopyExtendedAttribute : 480 -> 484
~ _BOMCopierSourceEntryRead : 456 -> 472
~ _skip_remaining_file_data : 248 -> 252
~ _parse_apple_archive_xat_blob : 704 -> 708
~ _BOMFSOTypeInfoInitialize : 396 -> 400
~ _BOMFSOTypeInfoInitializeDeferred : 528 -> 532
~ _BOMFSOTypeInfoParseSummaryWithSys : 876 -> 884
~ _BOMFSOArchInfoArchive : 268 -> 272
~ _BOMFSOArchInfoUnarchive : 356 -> 360
~ __ReadBlockTable : 324 -> 328
~ _BOMStorageCommit : 492 -> 496
~ _BOMStorageNewBlock : 152 -> 156
~ _BOMStorageSizeOfBlock : 80 -> 84
~ _BOMStorageFreeBlock : 136 -> 140
~ _BOMStorageCopyToBlock : 60 -> 64
~ _BOMStorageCopyToBlockRange : 780 -> 788
~ _BOMStorageCopyFromBlock : 236 -> 240
~ _BOMStorageCopyFromBlockRange : 660 -> 664
~ _BOMStorageCompact : 944 -> 952
~ _BOMStorageFindActualFreeSpace : 264 -> 268
~ _BOMStorageDump : 1228 -> 1232
~ _BOMTreeFree : 216 -> 224
~ __SyncCache : 80 -> 84
~ __WritePage : 224 -> 236
~ __PageSetValue : 908 -> 924
~ __findRemove : 1740 -> 1748
~ __findPage : 428 -> 432
~ __BOMTreeDiagnosticTraverse : 456 -> 476
~ _BOMStorageDumpTree : 680 -> 684
~ __ReadPage : 232 -> 244
~ __removePageFromCache : 188 -> 196
~ __shiftKeysAndValues : 388 -> 420
~ _BOMBomEnumeratorNewWithOptions : 548 -> 556
~ _BOMBomEnumeratorNext : 1516 -> 1548
~ _BOMCPIOReadHeader : 564 -> 568
~ _BOMPKZipFree : 208 -> 216
~ _BOMPKZipReadLocalHeader : 1096 -> 1100
~ _BOMPKZipWriteLocalHeader : 936 -> 940
~ _BOMPKZipReadCentralHeader : 708 -> 712
~ _BOMPKZipWriteCentralDirectory : 764 -> 768
~ _BOMPKZipGetFileCompressedSize : 48 -> 52
~ _BOMPKZipGetFileUncompressedSize : 48 -> 52
~ _BOMPKZipLoadCentralDirectory : 616 -> 620
~ _BOMPKZipSeekToCentralDirectory : 580 -> 584
~ _BOMPKZipCopyQuarantinePath : 128 -> 132
~ _is_valid_utf8_string : 80 -> 88
~ __normalizeBomCopySpecification : 648 -> 660
~ __printBomCopySpecification : 576 -> 580
~ __executeBomCopySpecification : 1748 -> 1752
~ __sanitizePath : 716 -> 720
~ __parse_arch_list : 1100 -> 1104
~ __dense_allocateRange : 316 -> 356
~ _BOMFilesystemInfoQuery : 924 -> 944
~ _notify_fatal_error : 220 -> 180
~ _release_copy_state : 136 -> 140
~ _notify_file_error : 284 -> 240
~ _notify_fatal_file_error : 292 -> 252
~ _parse_copier_options : 12204 -> 12160
~ _source_error_handler : 256 -> 216
~ _passphrase_callback : 188 -> 184
~ _BOMCopierSandbox_opendir : 460 -> 464
CStrings:
+ "May 21 2026"
- "Apr 18 2026"

```
