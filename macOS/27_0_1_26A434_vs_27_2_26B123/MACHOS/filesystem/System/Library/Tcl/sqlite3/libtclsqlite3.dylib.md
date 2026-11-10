## libtclsqlite3.dylib

> `/System/Library/Tcl/sqlite3/libtclsqlite3.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA.__data`

```diff

-406.0.0.0.0
-  __TEXT.__text: 0x102dc8
+408.0.0.0.0
+  __TEXT.__text: 0x102ff0
   __TEXT.__auth_stubs: 0xf10
   __TEXT.__const: 0x9368
-  __TEXT.__cstring: 0xd2f7
+  __TEXT.__cstring: 0xd303
   __TEXT.__oslogstring: 0x835
   __TEXT.__unwind_info: 0x2a48
   __DATA_CONST.__const: 0x3588

   - /usr/lib/libSystem.B.dylib
   Functions: 2787
   Symbols:   3334
-  CStrings:  2430
+  CStrings:  2431
 
Functions:
~ _sqlite3_db_config : 612 -> 608
~ _unixFileControl : 7524 -> 7592
~ _sqlite_guarded_fcopyfile -> _unixInvalidateSupportFiles : 528 -> 796
~ _unixInvalidateSupportFiles -> _sqlite_guarded_fcopyfile : 724 -> 528
~ ___appendOnePathElement_block_invoke : 180 -> 200
~ _getPageNormal : 644 -> 640
~ _readDbPage : 284 -> 320
~ _readSuperJournal : 464 -> 472
~ _incrVacuumStep : 780 -> 776
~ _ptrmapPut : 400 -> 404
~ _sqlite3WalCheckpoint : 2880 -> 3176
~ _sqlite3VdbeExec : 33244 -> 33240
~ _sqlite3VdbeRecordCompareWithSkip : 1508 -> 1504
~ _btreeComputeFreeSpace : 284 -> 308
~ _freeSpace : 692 -> 696
~ _allocateSpace : 440 -> 444
~ _defragmentPage : 960 -> 948
~ _jsonSkipLabel : 92 -> 104
~ _jsonTranslateBlobToText : 2488 -> 2504
~ _fts3EvalTestExpr : 1556 -> 1528
~ _fts3StringAppend : 196 -> 180
~ _fts5DataRead : 476 -> 460
~ _fts5LeafRead : 136 -> 160
~ _sqlite3Fts5IndexQuery : 3336 -> 3356
~ _fts5MergeRowidLists : 580 -> 584
~ _fts5ApiPhraseFirstColumn : 344 -> 368
~ _sqlite3Fts5StorageIntegrity : 3424 -> 3432
CStrings:
+ "corespeechd"
```
