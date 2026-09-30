## libsqlite3.dylib

> `/usr/lib/libsqlite3.dylib`

```diff

-406.0.0.0.0
-  __TEXT.__text: 0x1df2d8
+408.0.0.0.0
+  __TEXT.__text: 0x1df328
   __TEXT.__const: 0x873c
-  __TEXT.__cstring: 0xce9c
+  __TEXT.__cstring: 0xcea8
   __TEXT.__oslogstring: 0x835
   __TEXT.__unwind_info: 0x2740
   __TEXT.__eh_frame: 0x88

   __DATA_DIRTY.__data: 0x37c0
   __DATA_DIRTY.__bss: 0x20
   - /usr/lib/libSystem.B.dylib
-  Functions: 2535
-  Symbols:   2933
-  CStrings:  2394
+  Functions: 2536
+  Symbols:   2934
+  CStrings:  2395
 
Symbols:
+ _fts5LeafRead
Functions:
~ _readDbPage : 340 -> 400
~ _sqlite3VdbeExec : 52628 -> 52624
~ _sqlite3BtreeInsert : 3552 -> 3556
~ _defragmentPage : 964 -> 944
~ _ptrmapPut : 516 -> 520
~ _sqlite3WalCheckpoint : 5240 -> 6096
~ _unixFileControl : 9092 -> 9172
~ _sqlite3_db_config : 896 -> 892
~ _sessionChangesetApplyV23 : 7972 -> 7944
~ _sqlite3rebaser_configure : 384 -> 392
~ _sessionRebase : 6600 -> 6716
+ _unixInvalidateSupportFiles
- _unixInvalidateSupportFiles
~ ___appendOnePathElement_block_invoke : 192 -> 212
~ _getPageNormal : 868 -> 864
~ _readSuperJournal : 864 -> 872
~ _incrVacuumStep : 1140 -> 1136
~ _sqlite3VdbeRecordCompareWithSkip : 2368 -> 2364
~ _btreeComputeFreeSpace : 288 -> 308
~ _freeSpace : 712 -> 716
~ _allocateSpace : 468 -> 472
~ _jsonEachNext : 844 -> 868
~ _jsonEachColumn : 1192 -> 1228
~ _jsonTranslateBlobToText : 3588 -> 3600
~ _fts3SnippetFunc : 8136 -> 8148
~ _fts3OffsetsFunc : 2864 -> 2844
~ _fts5MultiIterNext : 2148 -> 1956
~ _fts5SegIterReverseNewPage : 716 -> 656
~ _fts5DataRead : 916 -> 900
+ _fts5LeafRead
~ _sqlite3Fts5IndexQuery : 15928 -> 15540
~ _fts5SegIterSeekInit : 6292 -> 5212
~ _fts5IndexMergeLevel : 5968 -> 6072
~ _fts5ChunkIterate : 680 -> 452
~ _fts5SegIterLoadTerm : 1364 -> 1184
~ _fts5SegIterNext_None : 1544 -> 1732
~ _fts5SegIterNext : 2040 -> 1900
~ _fts5SegIterInit : 928 -> 756
~ _fts5MergeRowidLists : 1044 -> 1048
~ _fts5ApiPhraseFirstColumn : 644 -> 684
~ _sqlite3Fts5StorageIntegrity : 11652 -> 12124
~ _sessionAppendPrintf : 640 -> 628
~ _sessionSelectStmt : 3288 -> 3456
~ _sessionReadRecord : 1152 -> 1148
~ _sessionApplyOneOp : 6764 -> 6604
~ _sessionAppendRecordMerge : 760 -> 912
CStrings:
+ "corespeechd"
```
