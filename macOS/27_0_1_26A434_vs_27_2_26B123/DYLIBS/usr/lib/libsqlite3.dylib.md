## libsqlite3.dylib

> `/usr/lib/libsqlite3.dylib`

```diff

-406.0.0.0.0
-  __TEXT.__text: 0x1e19c4
+408.0.0.0.0
+  __TEXT.__text: 0x1e1a08
   __TEXT.__const: 0x873c
-  __TEXT.__cstring: 0xce9c
+  __TEXT.__cstring: 0xcea8
   __TEXT.__oslogstring: 0x835
-  __TEXT.__unwind_info: 0x1e60
+  __TEXT.__unwind_info: 0x1e68
   __TEXT.__eh_frame: 0x88
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x1cd0

   __DATA_DIRTY.__data: 0x37c0
   __DATA_DIRTY.__bss: 0x20
   - /usr/lib/libSystem.B.dylib
-  Functions: 2536
-  Symbols:   2933
-  CStrings:  2394
+  Functions: 2537
+  Symbols:   2934
+  CStrings:  2395
 
Symbols:
+ _fts5LeafRead
Functions:
~ _readDbPage : 344 -> 400
~ _sqlite3VdbeExec : 52684 -> 52680
~ _sqlite3BtreeInsert : 3588 -> 3592
~ _defragmentPage : 976 -> 956
~ _ptrmapPut : 516 -> 520
~ _sqlite3WalCheckpoint : 5244 -> 6108
~ _unixFileControl : 9152 -> 9232
~ _sqlite3_db_config : 908 -> 904
~ _sessionChangesetApplyV23 : 7972 -> 7944
~ _sqlite3rebaser_configure : 384 -> 392
~ _sessionRebase : 6600 -> 6716
+ _unixInvalidateSupportFiles
- _unixInvalidateSupportFiles
~ ___appendOnePathElement_block_invoke : 192 -> 212
~ _getPageNormal : 880 -> 876
~ _readSuperJournal : 864 -> 872
~ _incrVacuumStep : 1140 -> 1136
~ _sqlite3VdbeRecordCompareWithSkip : 2368 -> 2364
~ _btreeComputeFreeSpace : 288 -> 308
~ _freeSpace : 724 -> 728
~ _allocateSpace : 488 -> 492
~ _jsonEachNext : 844 -> 868
~ _jsonEachColumn : 1192 -> 1228
~ _jsonTranslateBlobToText : 3588 -> 3600
~ _fts3SnippetFunc : 8216 -> 8228
~ _fts3OffsetsFunc : 2864 -> 2844
~ _fts5MultiIterNext : 2152 -> 1960
~ _fts5SegIterReverseNewPage : 728 -> 668
~ _fts5DataRead : 916 -> 900
+ _fts5LeafRead
~ _sqlite3Fts5IndexQuery : 15936 -> 15544
~ _fts5SegIterSeekInit : 6300 -> 5220
~ _fts5IndexMergeLevel : 5968 -> 6072
~ _fts5ChunkIterate : 700 -> 460
~ _fts5SegIterLoadTerm : 1364 -> 1184
~ _fts5SegIterNext_None : 1556 -> 1744
~ _fts5SegIterNext : 2040 -> 1900
~ _fts5SegIterInit : 928 -> 756
~ _fts5MergeRowidLists : 1056 -> 1060
~ _fts5ApiPhraseFirstColumn : 644 -> 684
~ _sqlite3Fts5StorageIntegrity : 11652 -> 12124
~ _sessionAppendPrintf : 640 -> 628
~ _sessionSelectStmt : 3288 -> 3456
~ _sessionReadRecord : 1152 -> 1148
~ _sessionApplyOneOp : 6788 -> 6628
~ _sessionAppendRecordMerge : 760 -> 912
CStrings:
+ "corespeechd"
```
