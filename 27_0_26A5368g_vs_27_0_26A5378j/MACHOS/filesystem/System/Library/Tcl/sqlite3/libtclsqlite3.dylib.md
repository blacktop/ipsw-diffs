## libtclsqlite3.dylib

> `/System/Library/Tcl/sqlite3/libtclsqlite3.dylib`

```diff

-  __TEXT.__text: 0x104f98
+  __TEXT.__text: 0x105100
   __TEXT.__auth_stubs: 0xf10
   __TEXT.__const: 0x9358
-  __TEXT.__cstring: 0xd253
+  __TEXT.__cstring: 0xd2ac
   __TEXT.__oslogstring: 0x7c0
   __TEXT.__unwind_info: 0x2188
-  __DATA_CONST.__const: 0x3578
+  __DATA_CONST.__const: 0x3588
   __DATA_CONST.__auth_got: 0x788
   __DATA_CONST.__got: 0x98
   __DATA_CONST.__auth_ptr: 0x10

   - /usr/lib/libSystem.B.dylib
   Functions: 2788
   Symbols:   3384
-  CStrings:  2427
+  CStrings:  2432
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA.__data : content changed
Functions:
~ _output_sql_from_query : 504 -> 496
~ _sqlite3_str_vappendf : 7764 -> 7752
~ _unixSetSystemCall : 208 -> 212
~ _unixGetSystemCall : 112 -> 116
~ _sqlite3_database_file_object : 52 -> 68
~ _sqlite3_backup_init : 408 -> 432
~ _findBtree : 372 -> 352
~ _sqlite3_backup_step : 1612 -> 1708
~ _sqlite3_backup_finish : 352 -> 364
~ _sqlite3_blob_open : 1644 -> 1656
~ _sqlite3ErrorMsg : 688 -> 672
~ _sqlite3VdbeAddOpList : 224 -> 216
~ _sqlite3Prepare16 : 664 -> 676
~ _sqlite3_declare_vtab : 968 -> 972
~ _sqlite3_vtab_config : 328 -> 324
~ _sqlite3_incomplete : 1240 -> 1248
~ _sqlite3PCacheBufferSetup : 192 -> 188
~ _sqlite3_db_config : 612 -> 620
~ _setupLookaside : 568 -> 560
~ _sqlite3FindFunction : 528 -> 520
~ _openDatabase : 2448 -> 2444
~ _sqlite3FindTable : 976 -> 980
~ _sqlite3_free_filename : 52 -> 68
~ _sqlite3_uri_parameter : 76 -> 60
~ _sqlite3_uri_key : 216 -> 200
~ _sqlite3_filename_database : 64 -> 56
~ _sqlite3_filename_journal : 168 -> 148
~ _sqlite3_compileoption_used : 296 -> 300
~ _findCreateFileMode : 444 -> 452
~ _memdbClose : 408 -> 412
~ _setDefaultSyncFlag : 112 -> 120
~ _pager_playback : 1352 -> 1520
~ _readSuperJournal : 392 -> 464
~ _btreeParseCellPtrIndex : 136 -> 132
~ _walTryBeginRead : 2112 -> 2108
~ _walDecodeFrame : 240 -> 248
~ _ptrmapPut : 400 -> 404
~ _vdbeFreeOpArray : 148 -> 140
~ _sqlite3Atoi64 : 656 -> 648
~ _sqlite3VdbeExec : 33376 -> 33280
~ _sqlite3BtreeIndexMoveto : 1388 -> 1440
~ _sqlite3VdbeRecordCompareWithSkip : 1512 -> 1508
~ _sqlite3SrcListDelete : 332 -> 324
~ _indexCellCompare : 100 -> 140
~ _balance : 6128 -> 6132
~ _freeSpace : 712 -> 708
~ _defragmentPage : 972 -> 976
~ _vdbeSorterSort : 452 -> 440
~ _sqlite3Prepare : 1220 -> 1224
~ _sqlite3GetInt32 : 368 -> 364
~ _resolveP2Values : 300 -> 292
~ _pragmaVtabBestIndex : 312 -> 304
~ _jsonEachBestIndex : 344 -> 336
~ _jsonConvertTextToBlob : 244 -> 248
~ _jsonTranslateTextToBlob : 3392 -> 3400
~ _carrayBestIndex : 296 -> 288
~ _sqlite3Utf8Read : 136 -> 132
~ _exprListDeleteNN : 140 -> 128
~ _sqlite3AffinityType : 456 -> 452
~ _yy_reduce : 9368 -> 9352
~ _sqlite3StartTable : 1492 -> 1496
~ _sqlite3EndTable : 2344 -> 2348
~ _sqlite3AddColumn : 1136 -> 1152
~ _sqlite3CreateForeignKey : 1232 -> 1228
~ _sqlite3DropTable : 1004 -> 1012
~ _sqlite3CreateView : 688 -> 696
~ _sqlite3Select : 10020 -> 9988
~ _sqlite3JoinType : 364 -> 372
~ _sqlite3Pragma : 16880 -> 16868
~ _sqlite3Reindex : 824 -> 816
~ _sqlite3AlterRenameTable : 1008 -> 1020
~ _sqlite3WithAdd : 428 -> 424
~ _sqlite3DequoteNumber : 388 -> 380
~ _lockTable : 276 -> 284
~ _codeInteger : 424 -> 428
~ _sqlite3ExprCodeExprList : 496 -> 476
~ _sqlite3ExprListDup : 468 -> 448
~ _sqlite3CheckObjectName : 424 -> 428
~ _sqlite3ResultSetOfSelect : 296 -> 356
~ _sqlite3NestedParse : 356 -> 344
~ _resolveExprStep : 7204 -> 7232
~ _sqlite3WindowUpdate : 572 -> 576
~ _sqlite3MatchEName : 368 -> 376
~ _isValidSchemaTableName : 428 -> 432
~ _selectExpander : 6144 -> 6140
~ _sqlite3SubqueryColumnTypes : 772 -> 780
~ _columnTypeImpl : 548 -> 544
~ _tableAndColumnIndex : 244 -> 260
~ _sqlite3ResolveOrderGroupBy : 280 -> 264
~ _multiSelect : 2144 -> 2160
~ _sqlite3WhereEnd : 2484 -> 2464
~ _sqlite3ExprAnalyzeAggList : 108 -> 100
~ _resetAccumulator : 556 -> 548
~ _sqlite3WhereMinMaxOptEarlyOut : 108 -> 124
~ _propagateConstantExprRewriteOne : 292 -> 288
~ _sqlite3ExprIsSingleTableConstraint : 276 -> 292
~ _wherePathSolver : 2604 -> 2568
~ _sqlite3WhereCodeOneLoopStart : 9156 -> 9148
~ _exprAnalyze : 6756 -> 6704
~ _whereLoopAddVirtual : 2220 -> 2204
~ _whereLoopAddBtree : 2044 -> 2028
~ _whereOrInsert : 216 -> 200
~ _whereUsablePartialIndex : 292 -> 276
~ _translateColumnToCopy : 172 -> 164
~ _whereApplyPartialIndexConstraints : 188 -> 180
~ _sqlite3WhereClauseClear : 172 -> 156
~ _getRowTrigger : 1724 -> 1772
~ _sqlite3GenerateConstraintChecks : 5860 -> 5760
~ _getAutoVacuum : 296 -> 280
~ _getSafetyLevel : 256 -> 264
~ _likeFunc : 500 -> 512
~ _sqlite3ParseUri : 1504 -> 1484
~ _detachFunc : 492 -> 500
~ _statInit : 612 -> 600
~ _isAlterableTable : 216 -> 220
~ _trimFunc : 644 -> 664
~ _lengthFunc : 276 -> 280
~ _printfFunc : 200 -> 296
~ _substrFunc : 764 -> 776
~ _percentSort : 308 -> 356
~ _renameColumnFunc : 1972 -> 1996
~ _renameTableTest : 604 -> 608
~ _dropColumnFunc : 636 -> 640
~ _renameQuotefixFunc : 744 -> 748
~ _isDate : 4324 -> 4344
~ _parseHhMmSs : 532 -> 528
~ _purgeableCacheFetch : 1284 -> 1288
~ _pcache1FetchStage2 : 884 -> 892
~ _fts3auxNextMethod : 604 -> 612
~ _fts3SelectLeaf : 952 -> 960
~ _sqlite3Fts3GetVarintU : 180 -> 168
~ _sqlite3Fts3SegReaderStep : 1544 -> 1532
~ _porterNext : 3208 -> 3192
~ _m_gt_0 : 172 -> 164
~ _m_eq_1 : 276 -> 260
~ _m_gt_1 : 268 -> 252
~ _fts3UpdateMethod : 2960 -> 2988
~ _fts3FindFunctionMethod : 120 -> 128
~ _fts3InitVtab : 4660 -> 4576
~ _sqlite3Fts3NextToken : 232 -> 224
~ _fts3EvalSelectDeferred : 1148 -> 1100
~ _fts3EvalPhraseMergeToken : 944 -> 940
~ _fts3DoclistOrMerge : 1008 -> 984
~ _fts3PoslistMerge : 888 -> 856
~ _fts3PoslistPhraseMerge : 1152 -> 1140
~ _fts3PendingListAppendVarint : 296 -> 292
~ _fts3InsertDocsize : 332 -> 336
~ _fts3UpdateDocTotals : 820 -> 824
~ _fts3SegmentMerge : 2780 -> 2744
~ _fts3NodeAddTerm : 764 -> 772
~ _fts3ReadEndBlockField : 232 -> 244
~ _sqlite3Fts3Incrmerge : 5492 -> 5504
~ _fts3IncrmergeHintPush : 196 -> 204
~ _fts3AppendToNode : 540 -> 536
~ _fts3TruncateNode : 476 -> 484
~ _fts3MatchinfoFunc : 2624 -> 2608
~ _fts3MatchinfoSelectDoctotal : 284 -> 268
~ _fts5BestIndexMethod : 1452 -> 1472
~ _fts5FilterMethod : 2416 -> 2424
~ _fts5UpdateMethod : 3280 -> 3288
~ _fts5InitVtab : 4416 -> 4428
~ _fts5ConfigSkipLiteral : 408 -> 412
~ _sqlite3Fts5ConfigParseRank : 440 -> 424
~ _sqlite3Fts5HashScanInit : 356 -> 368
~ _fts5FlushSecureDelete : 2988 -> 3036
~ _fts5StructurePromote : 532 -> 536
~ _fts5PoslistFilterCallback : 568 -> 592
~ _sqlite3Fts5StorageDelete : 2436 -> 2440
~ _fts5IndexOptimizeStruct : 460 -> 468
~ _fts5SnippetFunction : 1692 -> 1752
~ _fts5TriTokenize : 948 -> 952
~ _fts5PorterCreate : 300 -> 420
~ _fts5Porter_Ostar : 152 -> 148
~ _fts5VocabInitVtab : 820 -> 808
~ _nodeAcquire : 716 -> 728
~ _csvtabConnect : 2300 -> 2304
~ _csv_parameter : 252 -> 264
~ _DbObjCmd : 8576 -> 8580
~ _testSqllog : 1216 -> 1224
~ _sqllogCopydb : 920 -> 904
CStrings:
+ "-mj"
+ "Pythonsqlite3"
+ "VIEWs and/or subqueries nested too deep"
+ "recon"
+ "triggers nested too deep"

```
