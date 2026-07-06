## libsqlite3.dylib

> `/usr/lib/libsqlite3.dylib`

```diff

-  __TEXT.__text: 0x1e1020
+  __TEXT.__text: 0x1e14d4
   __TEXT.__const: 0x873c
-  __TEXT.__cstring: 0xcdf8
+  __TEXT.__cstring: 0xce51
   __TEXT.__oslogstring: 0x7c0
   __TEXT.__unwind_info: 0x1e60
   __TEXT.__eh_frame: 0x88

   - /usr/lib/libSystem.B.dylib
   Functions: 2536
   Symbols:   2977
-  CStrings:  2391
+  CStrings:  2396
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__unwind_info : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__const : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH.__data : content changed
~ __DATA_DIRTY.__data : content changed
Functions:
~ _openDatabase : 3568 -> 3580
~ _sqlite3BtreeOpen : 5872 -> 5832
~ _fillInUnixFile : 1452 -> 1432
~ _sqlite3FindFunction : 1200 -> 1192
~ _sqlite3Prepare : 2672 -> 2684
~ _yy_reduce : 10356 -> 10340
~ _sqlite3Pragma : 24332 -> 24224
~ _sqlite3StartTable : 2128 -> 2132
~ _sqlite3EndTable : 4348 -> 4312
~ _purgeableCacheFetch : 2048 -> 2052
~ _sqlite3Select : 16540 -> 16412
~ _selectExpander : 11056 -> 11052
~ _resolveExprStep : 13160 -> 13072
~ _resolveOrderGroupBy : 928 -> 920
~ _sqlite3WhereEnd : 6128 -> 6080
~ _sqlite3SrcListDelete : 1320 -> 1304
~ _sqlite3VdbeExec : 52772 -> 52552
~ _sqlite3ExprListDup : 572 -> 568
~ _exprAnalyze : 9928 -> 9908
~ _sqlite3Insert : 8868 -> 8776
~ _sqlite3GenerateConstraintChecks : 14832 -> 15096
~ _balance : 10296 -> 10292
~ _sqlite3VdbeAddOpList : 760 -> 748
~ _sqlite3CreateForeignKey : 1716 -> 1712
~ _sqlite3CodeSubselect : 1832 -> 1848
~ _generateSortTail : 5456 -> 5476
~ _sqlite3Update : 10052 -> 9980
~ _resetAccumulator : 1308 -> 1304
~ _updateAccumulator : 3716 -> 3712
~ _codeRowTrigger : 2604 -> 2584
~ _likeFunc : 972 -> 984
~ _defragmentPage : 976 -> 980
~ _ptrmapPut : 516 -> 520
~ _sqlite3Prepare16 : 900 -> 912
~ _isDate : 8836 -> 8984
~ _sqlite3NestedParse : 808 -> 796
~ _pager_playback : 1896 -> 2348
~ _output_sql_from_query : 664 -> 648
~ _sqlite3VdbeDelete : 2196 -> 2180
~ _sqlite3_str_vappendf : 12728 -> 12776
~ _sqlite3_deserialize : 1096 -> 1092
~ _sqlite3_database_file_object : 52 -> 68
~ _sqlite3_backup_init : 752 -> 800
~ _findBtree : 576 -> 556
~ _sqlite3_backup_step : 2084 -> 2260
~ _sqlite3_backup_finish : 516 -> 528
~ _sqlite3_blob_open : 2624 -> 2628
~ _sqlite3ErrorMsg : 1412 -> 1396
~ _sqlite3_declare_vtab : 1176 -> 1180
~ _sqlite3_vtab_config : 440 -> 436
~ _sqlite3_incomplete : 3024 -> 2988
~ _sqlite3PCacheBufferSetup : 192 -> 188
~ _setupLookaside : 896 -> 888
~ _sqlite3_free_filename : 272 -> 284
~ _sqlite3_uri_parameter : 212 -> 188
~ _sqlite3_uri_key : 216 -> 200
~ _sqlite3_filename_database : 64 -> 60
~ _sqlite3_filename_journal : 172 -> 148
~ _sqlite3_filename_wal : 192 -> 168
~ _sqlite3session_diff : 3124 -> 3116
~ _sessionTableInfo : 1896 -> 1892
~ _sessionChangesetApplyV23 : 7984 -> 7972
~ _sessionRebase : 6276 -> 6600
~ _unixOpenChildFile : 820 -> 828
~ _findCreateFileMode : 520 -> 528
~ _memdbClose : 824 -> 828
~ _btreeBeginTrans : 2372 -> 2380
~ _setDefaultSyncFlag : 228 -> 236
~ _readSuperJournal : 796 -> 864
~ _walDecodeFrame : 276 -> 280
~ _sqlite3Atoi64 : 740 -> 716
~ _sqlite3BtreeIndexMoveto : 1916 -> 2056
~ _sqlite3VdbeRecordCompareWithSkip : 2372 -> 2368
~ _freeSpace : 732 -> 728
~ _decodeIntArray : 732 -> 708
~ _sqlite3GetInt32 : 1024 -> 1028
~ _sqlite3AffinityType : 500 -> 496
~ ___sqlite3ErrorTelemetryEnabled_block_invoke : 356 -> 404
~ _pragmaVtabBestIndex : 388 -> 380
~ _jsonEachBestIndex : 960 -> 952
~ _jsonEachFilter : 1548 -> 1552
~ _jsonConvertTextToBlob : 444 -> 448
~ _carrayBestIndex : 1220 -> 1212
~ _carrayFilter : 1004 -> 984
~ _sqlite3Utf8Read : 136 -> 132
~ _exprListDeleteNN : 628 -> 624
~ _sqlite3CreateView : 948 -> 952
~ _sqlite3Reindex : 2004 -> 2000
~ _sqlite3AlterRenameTable : 1664 -> 1676
~ _sqlite3WithAdd : 560 -> 556
~ _sqlite3WindowChain : 364 -> 360
~ _sqlite3DequoteNumber : 544 -> 524
~ _lockTable : 772 -> 780
~ _sqlite3ExprCodeExprList : 644 -> 628
~ _sqlite3VdbeScanStatusRange : 192 -> 176
~ _sqlite3ResultSetOfSelect : 296 -> 440
~ _sqlite3ColumnsFromExprList : 2024 -> 1996
~ _sqlite3ResolveOrderGroupBy : 264 -> 268
~ _renameWalkWith : 596 -> 564
~ _sqlite3ExprAnalyzeAggList : 108 -> 100
~ _analyzeAggFuncArgs : 488 -> 480
~ _sqlite3WhereMinMaxOptEarlyOut : 172 -> 184
~ _propagateConstantExprRewrite : 956 -> 928
~ _sqlite3ExprIsSingleTableConstraint : 272 -> 300
~ _wherePathSolver : 3740 -> 3688
~ _sqlite3ConstructBloomFilter : 2216 -> 2292
~ _sqlite3WhereCodeOneLoopStart : 12536 -> 12584
~ _sqlite3WhereAddScanStatus : 1396 -> 1420
~ _whereLoopAddVirtual : 3620 -> 3604
~ _whereLoopAddBtree : 2572 -> 2544
~ _whereLoopAddOr : 1552 -> 1536
~ _whereLoopInsert : 2564 -> 2544
~ _whereUsablePartialIndex : 400 -> 388
~ _wherePathMatchSubqueryOB : 432 -> 420
~ _whereApplyPartialIndexConstraints : 200 -> 192
~ _sqlite3WhereClauseClear : 180 -> 164
~ _sqlite3ProcessReturningSubqueries : 268 -> 264
~ _getAutoVacuum : 284 -> 292
~ _attachFunc : 3820 -> 3828
~ _sqlite3ParseUri : 2628 -> 2592
~ _trimFunc : 1288 -> 1304
~ _lengthFunc : 488 -> 492
~ _printfFunc : 416 -> 828
~ _roundFunc : 1120 -> 1116
~ _substrFunc : 1252 -> 1260
~ _sumStep : 1312 -> 1308
~ _sumInverse : 1424 -> 1420
~ _ceilingFunc : 744 -> 740
~ _percentSort : 336 -> 372
~ _renameColumnFunc : 3724 -> 3740
~ _renameTableTest : 1364 -> 1368
~ _dropColumnFunc : 1392 -> 1396
~ _renameQuotefixFunc : 1180 -> 1184
~ _renameParseSql : 1152 -> 1148
~ _nth_valueStepFunc : 976 -> 972
~ _parseHhMmSs : 584 -> 580
~ _jsonErrorFunc : 1244 -> 1248
~ _pcache1FetchStage2 : 1284 -> 1292
~ _fts3auxNextMethod : 988 -> 992
~ _fts3SelectLeaf : 2516 -> 2360
~ _sqlite3Fts3SegReaderStep : 3452 -> 3436
~ _porterNext : 7476 -> 7496
~ _m_gt_0 : 188 -> 180
~ _m_eq_1 : 304 -> 288
~ _m_gt_1 : 284 -> 264
~ _fts3UpdateMethod : 7580 -> 7584
~ _fts3InitVtab : 10560 -> 10532
~ _sqlite3Fts3InitTokenizer : 1896 -> 1920
~ _fts3ExprParse : 4264 -> 4320
~ _fts3EvalSelectDeferred : 3768 -> 3752
~ _fts3EvalPhraseMergeToken : 2724 -> 2720
~ _fts3PoslistMerge : 1660 -> 1548
~ _fts3PoslistPhraseMerge : 2036 -> 2032
~ _sqlite3Fts3EvalTestDeferred : 1824 -> 1816
~ _fts3PendingListAppendVarint : 504 -> 500
~ _fts3InsertDocsize : 824 -> 828
~ _fts3UpdateDocTotals : 1508 -> 1512
~ _fts3SegmentMerge : 5772 -> 5816
~ _fts3PromoteSegments : 2000 -> 2012
~ _fts3NodeAddTerm : 796 -> 804
~ _sqlite3Fts3Incrmerge : 14200 -> 14224
~ _fts3IncrmergeHintPush : 328 -> 336
~ _fts3AppendToNode : 620 -> 616
~ _fts3TruncateNode : 1140 -> 1148
~ _sqlite3Fts3EvalPhrasePoslist : 1940 -> 1956
~ _fts5FilterMethod : 4112 -> 4096
~ _fts5UpdateMethod : 7484 -> 7492
~ _fts5InitVtab : 9616 -> 9576
~ _fts5ConfigSkipLiteral : 476 -> 480
~ _sqlite3Fts5ConfigParseRank : 676 -> 660
~ _fts5SegIterReverseNewPage : 668 -> 728
~ _fts5ExprNodeTest_STRING : 4452 -> 4336
~ _fts5FlushSecureDelete : 4884 -> 4948
~ _fts5StructurePromote : 1564 -> 1556
~ _fts5IterSetOutputs_Full : 672 -> 784
~ _fts5PoslistFilterCallback : 832 -> 856
~ _sqlite3Fts5StorageIntegrity : 11876 -> 11664
~ _fts5IndexOptimizeStruct : 776 -> 784
~ _fts5IndexTombstoneRebuild : 2380 -> 2444
~ _fts5SnippetFunction : 3416 -> 3780
~ _fts5TriTokenize : 1660 -> 1664
~ _fts5PorterCreate : 432 -> 544
~ _fts5PorterCb : 10788 -> 10764
~ _fts5VocabInitVtab : 1428 -> 1416
~ _rtreenode : 1440 -> 1436
~ _rtreeBestIndex : 2912 -> 2908
~ _rtreeFilter : 2372 -> 2364
~ _nodeAcquire : 1484 -> 1472
~ _csvtabConnect : 4968 -> 4952
~ _testSqllog : 1256 -> 1264
~ _sqllogCopydb : 932 -> 900
CStrings:
+ "-mj"
+ "Pythonsqlite3"
+ "VIEWs and/or subqueries nested too deep"
+ "recon"
+ "triggers nested too deep"

```
