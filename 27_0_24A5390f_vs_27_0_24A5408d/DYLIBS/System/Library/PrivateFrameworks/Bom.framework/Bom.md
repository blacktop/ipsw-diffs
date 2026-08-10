## Bom

> `/System/Library/PrivateFrameworks/Bom.framework/Bom`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH.__data`

```diff

-277.0.0.0.0
-  __TEXT.__text: 0x5a6b8
-  __TEXT.__cstring: 0x129f6
+279.1.0.0.0
+  __TEXT.__text: 0x5b4ac
+  __TEXT.__cstring: 0x129d0
   __TEXT.__const: 0x1728
   __TEXT.__oslogstring: 0x103e
   __TEXT.__unwind_info: 0xad8

   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libbz2.1.0.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 1095
-  Symbols:   1556
-  CStrings:  2391
+  Functions: 1100
+  Symbols:   1561
+  CStrings:  2390
 
Symbols:
+ _BOM_calloc_typed
+ _BOM_malloc_typed
+ _BOM_malloczero_typed
+ _BOM_realloc_typed
+ _BOM_realloczero_typed
+ _platform_calloc_typed
+ _platform_malloc_typed
+ _platform_realloc_typed
+ _platform_valloc_typed
- _platform_calloc
- _platform_malloc
- _platform_realloc
- _platform_valloc
Functions:
~ _BOMCFStringGetUTF8String : 296 -> 312
~ _BOMCFPropertyListReadFromPathWithSys : 332 -> 340
+ _BOM_malloc_typed
+ _BOM_malloczero_typed
+ _BOM_calloc_typed
+ _BOM_realloc_typed
+ _BOM_realloczero_typed
~ _BOMStackNew : 88 -> 120
~ _BOMStackPush : 136 -> 144
~ _darc_format_entry_new : 92 -> 108
~ _darc_format_entry_set_attribute : 576 -> 592
~ _BOMPatternCompileString : 144 -> 160
~ _BOMFileNewFromFDWithSys : 348 -> 380
~ __BOMFileInit : 1196 -> 1212
~ _BOMFileNewFromCFWriteStream : 152 -> 168
~ _BOMFileNewFromCFReadStream : 152 -> 168
~ _BOMFileNewMirrorWithSys : 104 -> 120
~ __BOMFileSetupGzip : 420 -> 444
~ __BOMFileSetupBzip2 : 376 -> 400
~ _fts_agent_new : 308 -> 316
~ _create_node : 148 -> 164
~ _fts_agent_read : 4596 -> 4644
~ _child_allocate : 140 -> 156
~ _BOMBomOpenWithSys : 488 -> 504
~ __readArchInfo : 208 -> 224
~ _BOMBomOpenWithStorage : 412 -> 428
~ _BOMBomNewWithStorage : 328 -> 360
~ _BOMBomNewFromBom : 992 -> 1008
~ _BOMBomNewFromBomWithOptions : 1452 -> 1484
~ __copyFilesFromBomToBom : 2124 -> 2132
~ _BOMBomNewFromDirectoryWithSys : 2208 -> 2140
~ _BOMBomGetRootFSObject : 392 -> 268
~ _BOMBomGetFSObjectAtPath : 380 -> 388
~ __addArchInfoForFSObject : 356 -> 392
~ __BOMBlockIDForFSObject : 276 -> 284
~ _BOMBomApproximateBytesRepresentedByVariantWithBlockSize : 1160 -> 1192
~ _release_fts_agent_state : 324 -> 312
~ _drain_fts_state : 1064 -> 1080
~ _BOMHardLinkTableNew : 8 -> 24
~ _BOMHardLinkTableSetPathAndData : 376 -> 384
~ _BOMFSEnumeratorNewWithSys : 328 -> 344
~ _BOMBomVIndexNew : 256 -> 272
~ _BOMBomVIndexOpen : 216 -> 232
~ _BOMBomVIndexGetList : 516 -> 532
~ _BOMBomVIndexDiskSpaceKey : 200 -> 208
~ _byte_stream_new : 100 -> 116
~ _byte_stream_read_string : 324 -> 340
~ _data_archive_decoder_new : 132 -> 148
~ _data_archive_decoder_set_stream : 728 -> 736
~ _parse_entry_posix_ustar : 3116 -> 3124
~ _parse_entry_cpio : 1572 -> 1596
~ _parse_entry_pkzip : 5380 -> 5468
~ _parse_entry_pkzip_data_descriptor : 664 -> 672
~ _data_source_new : 100 -> 116
~ _data_archive_new : 124 -> 140
~ _data_archive_read_entry : 1008 -> 1016
~ _data_archive_read_data : 2288 -> 2336
~ _BOMNewPathKey : 188 -> 204
~ _BOMNewPathValue : 156 -> 172
~ _data_read_stream_new : 92 -> 108
~ _data_read_stream_set_source : 896 -> 944
~ _BOMBomHLIndexNew : 132 -> 148
~ _BOMBomHLIndexFree : 224 -> 248
~ _BOMBomHLIndexOpen : 152 -> 168
~ _BOMBomHLIndexCommit : 232 -> 256
~ _BOMCopierNewWithSys : 216 -> 232
~ __BOMCopierCopyFromPKZip : 2128 -> 2252
~ __copyFromDirToDir : 2836 -> 2956
~ __copyExtendedAttributes : 920 -> 936
~ __copyDir : 1896 -> 1916
~ __copyLink : 1752 -> 1792
~ __copyDataFork : 6596 -> 6676
~ __copyFromCPIO : 1868 -> 1908
~ __copyFromPKZip : 2108 -> 2148
~ _BOMFSOArchInfoInitialize : 1068 -> 1084
~ _BOMFSOArchInfoCopy : 152 -> 168
~ _BOMFSOArchInfoThinKeepingArchs : 360 -> 376
~ _BOMFSOArchInfoThinKeepingArchsAndSubArchs : 392 -> 408
~ _BOMFSOArchInfoSet : 240 -> 256
~ __handleMachO_common : 124 -> 140
~ _BOMFSObjectUnarchive : 436 -> 444
~ _BOMFSObjectNew : 64 -> 8
~ _BOMFSObjectNewWithSys : 84 -> 100
~ _BOMFSObjectNewFromPathWithSys : 764 -> 788
~ _BOMFSObjectENewFromPathWithSys : 724 -> 756
~ _BOMFSObjectCopy : 396 -> 428
~ _BOMFSObjectNewFromPathDeferredWithSys : 388 -> 428
~ _BOMFSObjectNewFromPathStringWithSys : 160 -> 176
~ _BOMFSObjectSetPathName : 140 -> 156
~ _BOMFSObjectSetShortName : 140 -> 156
~ _BOMFSObjectSetOpaqueData : 192 -> 200
~ _capture_error : 340 -> 356
~ _BOMFSOTypeInfoUnarchive : 480 -> 504
~ _BOMFSOTypeInfoInitialize : 396 -> 412
~ _BOMFSOTypeInfoSetSymlinkTarget : 180 -> 188
~ _BOMFSOTypeInfoInitializeDeferred : 528 -> 544
~ _BOMFSOTypeInfoCopy : 120 -> 128
~ _BOMFSOTypeInfoSummary : 672 -> 688
~ _BOMFSOTypeInfoSummaryWithFormat : 2672 -> 2688
~ _BOMFSOArchInfoUnarchive : 380 -> 396
~ _BOMStorageOpenWithSys : 1260 -> 1276
~ _BOMStorageNewInRAM : 184 -> 200
~ __ReadFreeList : 176 -> 184
~ _BOMStorageOpenInRAM : 896 -> 912
~ _BOMStorageCompact : 952 -> 976
~ __newFreeListEntry : 128 -> 144
~ _BOMTreeIteratorNew : 260 -> 292
~ _BOMTreeIteratorKey : 292 -> 300
~ __findIndexForKey : 496 -> 504
~ _BOMTreeGetValue : 272 -> 296
~ _BOMTreeIteratorValue : 260 -> 268
~ __newBOMTree : 140 -> 156
~ __NewPage : 184 -> 224
~ __invalidateIterator : 300 -> 308
~ _data_archive_entry_new : 92 -> 108
~ _data_archive_entry_set_format_entry : 3392 -> 3456
~ _BOMStreamWithBlockID : 384 -> 408
~ _BOMStreamWithFileAndSys : 460 -> 484
~ _BOMStreamWithAddress : 212 -> 228
~ _BOMBomEnumeratorNewWithOptions : 556 -> 572
~ _BOMBomEnumeratorNext : 1540 -> 1548
~ _BOMAppleDoublePathToADPath : 236 -> 244
~ _BOMAppleDoubleCopyHeader : 224 -> 232
~ _BOMCPIONew : 128 -> 144
~ _BOMCPIOWriteTerminator : 212 -> 228
~ _BOMPKZipNew : 124 -> 156
~ _BOMPKZipReadNextSignature : 492 -> 524
~ _BOMPKZipReadLocalHeader : 1096 -> 1104
~ _BOMPKZipWriteLocalHeader : 936 -> 944
~ __squirrelAwayInfo : 320 -> 344
~ _BOMPKZipReadCentralHeader : 712 -> 728
~ _BOMPKZipWriteCentralDirectory : 760 -> 768
~ _BOMPKZipSkipDigitalSignature : 148 -> 156
~ _BOMPKZipSkipZIP64CentralDirectoryRecord : 148 -> 156
~ _BOMPKZipSkipEndOfCentralDirectoryRecord : 248 -> 256
~ _BOMPKZipLoadCentralDirectory : 620 -> 644
~ _BOMPKZipStoreQuarantinePath : 364 -> 412
~ __filterFatArchs : 492 -> 540
~ __normalizeBomCopySpecification : 692 -> 708
~ __executeBomCopySpecification : 1752 -> 1768
~ __parse_arch_list : 1104 -> 1152
~ __BOMFreeListAllocate : 540 -> 572
~ __BOMFreeListAllocateDense : 256 -> 304
~ __dense_serialize : 224 -> 232
~ __dense_addFreeRange : 212 -> 252
~ _BOMFilesystemInfoCreate : 416 -> 424
~ _BOMBufferAllocate : 88 -> 104
~ _BOMBufferPoolAllocate : 208 -> 224
~ _BOMBufferFIFOCreate : 116 -> 132
~ _BomSys_init : 112 -> 128
~ _BomSys_clone : 112 -> 128
~ _BomSys_log_attach : 340 -> 356
~ _data_stack_new : 184 -> 200
~ _data_stack_push : 288 -> 304
~ _BOMCopierSandbox_boxup : 444 -> 468
~ _BOMCopierSandbox_opendir : 460 -> 476
CStrings:
+ "Aug  3 2026"
- "Could not create empty hardlink path\n"
- "Jul  8 2026"
```
