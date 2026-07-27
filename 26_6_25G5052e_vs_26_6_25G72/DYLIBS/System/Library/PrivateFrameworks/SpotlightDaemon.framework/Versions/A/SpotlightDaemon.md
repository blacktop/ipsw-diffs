## SpotlightDaemon

> `/System/Library/PrivateFrameworks/SpotlightDaemon.framework/Versions/A/SpotlightDaemon`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__got`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-2418.6.3.6.0
-  __TEXT.__text: 0xbeef8
-  __TEXT.__auth_stubs: 0x1df0
-  __TEXT.__objc_methlist: 0x465c
-  __TEXT.__const: 0x3a0
-  __TEXT.__cstring: 0x89d8
-  __TEXT.__gcc_except_tab: 0x4294
-  __TEXT.__oslogstring: 0xa152
-  __TEXT.__unwind_info: 0x2678
+2418.6.3.9.400
+  __TEXT.__text: 0xc0f90
+  __TEXT.__auth_stubs: 0x1e10
+  __TEXT.__objc_methlist: 0x469c
+  __TEXT.__const: 0x3b8
+  __TEXT.__cstring: 0x8b39
+  __TEXT.__gcc_except_tab: 0x4354
+  __TEXT.__oslogstring: 0xa63b
+  __TEXT.__unwind_info: 0x26e8
   __TEXT.__objc_classname: 0x5ae
-  __TEXT.__objc_methname: 0xf7d4
-  __TEXT.__objc_methtype: 0x2799
-  __TEXT.__objc_stubs: 0xc260
+  __TEXT.__objc_methname: 0xf90c
+  __TEXT.__objc_methtype: 0x27a8
+  __TEXT.__objc_stubs: 0xc360
   __DATA_CONST.__got: 0xb40
-  __DATA_CONST.__const: 0x560
+  __DATA_CONST.__const: 0x5c0
   __DATA_CONST.__objc_classlist: 0x1a0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3840
+  __DATA_CONST.__objc_selrefs: 0x3880
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x128
   __DATA_CONST.__objc_arraydata: 0x2c0
-  __AUTH_CONST.__auth_got: 0xf10
-  __AUTH_CONST.__const: 0x4f28
-  __AUTH_CONST.__cfstring: 0x7520
+  __AUTH_CONST.__auth_got: 0xf20
+  __AUTH_CONST.__const: 0x50b8
+  __AUTH_CONST.__cfstring: 0x76e0
   __AUTH_CONST.__objc_const: 0x59f8
   __AUTH_CONST.__objc_arrayobj: 0x318
   __AUTH_CONST.__objc_intobj: 0x1f8

   __AUTH.__objc_data: 0x140
   __DATA.__objc_ivar: 0x4a0
   __DATA.__data: 0x7f0
-  __DATA.__bss: 0x120
+  __DATA.__bss: 0x138
   __DATA.__common: 0x4
   __DATA_DIRTY.__objc_data: 0xf00
   __DATA_DIRTY.__data: 0x158

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  Functions: 3112
-  Symbols:   6380
-  CStrings:  4958
+  Functions: 3143
+  Symbols:   6429
+  CStrings:  5001
 
Symbols:
+ -[SPConcreteCoreSpotlightIndexer _finishUserActivityPurgeWithDeleted:completionHandler:]
+ -[SPConcreteCoreSpotlightIndexer deleteUserActivitiesForBundleID:activityType:fromClient:completionHandler:]
+ -[SPConcreteCoreSpotlightIndexer issueUserActivityPurgeFixup:]
+ -[SPConcreteCoreSpotlightIndexer resetUserActivityPurgeFixupVersion]
+ -[SPConcreteCoreSpotlightIndexer runUserActivityPurgeFixupWithGroup:]
+ -[SPCoreSpotlightIndexer issueUserActivityPurgeCommand:completionHandler:]
+ GCC_except_table1002
+ GCC_except_table1003
+ GCC_except_table1047
+ GCC_except_table1052
+ GCC_except_table1116
+ GCC_except_table1159
+ GCC_except_table1165
+ GCC_except_table1166
+ GCC_except_table1172
+ GCC_except_table1173
+ GCC_except_table1174
+ GCC_except_table1184
+ GCC_except_table1199
+ GCC_except_table1203
+ GCC_except_table1225
+ GCC_except_table1232
+ GCC_except_table1239
+ GCC_except_table1246
+ GCC_except_table1253
+ GCC_except_table1270
+ GCC_except_table1338
+ GCC_except_table1339
+ GCC_except_table1341
+ GCC_except_table1347
+ GCC_except_table1394
+ GCC_except_table1401
+ GCC_except_table1520
+ GCC_except_table1588
+ GCC_except_table1591
+ GCC_except_table1592
+ GCC_except_table1595
+ GCC_except_table1596
+ GCC_except_table1756
+ GCC_except_table234
+ GCC_except_table245
+ GCC_except_table249
+ GCC_except_table252
+ GCC_except_table253
+ GCC_except_table256
+ GCC_except_table261
+ GCC_except_table262
+ GCC_except_table274
+ GCC_except_table275
+ GCC_except_table297
+ GCC_except_table304
+ GCC_except_table318
+ GCC_except_table326
+ GCC_except_table365
+ GCC_except_table375
+ GCC_except_table387
+ GCC_except_table422
+ GCC_except_table423
+ GCC_except_table427
+ GCC_except_table452
+ GCC_except_table481
+ GCC_except_table502
+ GCC_except_table503
+ GCC_except_table531
+ GCC_except_table558
+ GCC_except_table574
+ GCC_except_table626
+ GCC_except_table640
+ GCC_except_table651
+ GCC_except_table677
+ GCC_except_table683
+ GCC_except_table696
+ GCC_except_table697
+ GCC_except_table708
+ GCC_except_table730
+ GCC_except_table756
+ GCC_except_table757
+ GCC_except_table758
+ GCC_except_table782
+ GCC_except_table846
+ GCC_except_table867
+ GCC_except_table888
+ GCC_except_table892
+ GCC_except_table896
+ GCC_except_table925
+ GCC_except_table947
+ GCC_except_table976
+ GCC_except_table977
+ GCC_except_table986
+ _OUTLINED_FUNCTION_44
+ _OUTLINED_FUNCTION_45
+ _SIGetAccumulatedUACountResolved
+ __62-[SPConcreteCoreSpotlightIndexer issueUserActivityPurgeFixup:]_block_invoke
+ __62-[SPConcreteCoreSpotlightIndexer issueUserActivityPurgeFixup:]_block_invoke_2
+ __74-[SPCoreSpotlightIndexer issueUserActivityPurgeCommand:completionHandler:]_block_invoke
+ __88-[SPConcreteCoreSpotlightIndexer _finishUserActivityPurgeWithDeleted:completionHandler:]_block_invoke_3
+ ___108-[SPConcreteCoreSpotlightIndexer deleteUserActivitiesForBundleID:activityType:fromClient:completionHandler:]_block_invoke
+ ___62-[SPConcreteCoreSpotlightIndexer issueUserActivityPurgeFixup:]_block_invoke
+ ___62-[SPConcreteCoreSpotlightIndexer issueUserActivityPurgeFixup:]_block_invoke_2
+ ___69-[SPConcreteCoreSpotlightIndexer runUserActivityPurgeFixupWithGroup:]_block_invoke
+ ___74-[SPCoreSpotlightIndexer issueUserActivityPurgeCommand:completionHandler:]_block_invoke
+ ___74-[SPCoreSpotlightIndexer issueUserActivityPurgeCommand:completionHandler:]_block_invoke_2
+ ___74-[SPCoreSpotlightIndexer issueUserActivityPurgeCommand:completionHandler:]_block_invoke_3
+ ___74-[SPCoreSpotlightIndexer issueUserActivityPurgeCommand:completionHandler:]_block_invoke_4
+ ___74-[SPCoreSpotlightIndexer issueUserActivityPurgeCommand:completionHandler:]_block_invoke_5
+ ___74-[SPCoreSpotlightIndexer issueUserActivityPurgeCommand:completionHandler:]_block_invoke_6
+ ___74-[SPCoreSpotlightIndexer issueUserActivityPurgeCommand:completionHandler:]_block_invoke_7
+ ___88-[SPConcreteCoreSpotlightIndexer _finishUserActivityPurgeWithDeleted:completionHandler:]_block_invoke
+ ___88-[SPConcreteCoreSpotlightIndexer _finishUserActivityPurgeWithDeleted:completionHandler:]_block_invoke_2
+ ___88-[SPConcreteCoreSpotlightIndexer _finishUserActivityPurgeWithDeleted:completionHandler:]_block_invoke_3
+ ___block_descriptor_40_e8_32bs_e20_v24?0"NSError"8q16l
+ ___block_descriptor_48_e8_32s40w_e17_v16?0"NSError"8l
+ ___block_descriptor_56_e8_32s40w_e17_v16?0"NSError"8l
+ ___block_descriptor_57_e8_32s40bs_e17_v16?0"NSError"8l
+ ___block_descriptor_65_e8_32s40s48bs_e5_v8?0l
+ ___block_descriptor_72_e8_32s40s48r56r_e5_v8?0l
+ ___block_descriptor_72_e8_32s40s48s56r64r_e20_v24?0"NSError"8q16l
+ ___block_descriptor_73_e8_32s40s48s56s64s_e40_v16?0"SPConcreteCoreSpotlightIndexer"8l
+ __os_log_fault_impl
+ _kSPUserActivityPurgeTargets
+ _objc_msgSend$_finishUserActivityPurgeWithDeleted:completionHandler:
+ _objc_msgSend$contentTypeTree
+ _objc_msgSend$deleteUserActivitiesForBundleID:activityType:fromClient:completionHandler:
+ _objc_msgSend$initWithObjects:
+ _objc_msgSend$issueUserActivityPurgeCommand:completionHandler:
+ _objc_msgSend$issueUserActivityPurgeFixup:
+ _objc_msgSend$resetUserActivityPurgeFixupVersion
+ _objc_msgSend$runUserActivityPurgeFixupWithGroup:
+ sLoginNotificatonQueue_block_invoke_7.sLoggedUACapKeys
+ sLoginNotificatonQueue_block_invoke_7.sLoggedUACapKeysLock
+ sLoginNotificatonQueue_block_invoke_7.sLoggedUACapOnce
- GCC_except_table1028
- GCC_except_table1092
- GCC_except_table1135
- GCC_except_table1141
- GCC_except_table1142
- GCC_except_table1148
- GCC_except_table1149
- GCC_except_table1150
- GCC_except_table1160
- GCC_except_table1175
- GCC_except_table1179
- GCC_except_table1190
- GCC_except_table1200
- GCC_except_table1207
- GCC_except_table1221
- GCC_except_table1228
- GCC_except_table1245
- GCC_except_table1313
- GCC_except_table1314
- GCC_except_table1316
- GCC_except_table1322
- GCC_except_table1369
- GCC_except_table1376
- GCC_except_table1495
- GCC_except_table1563
- GCC_except_table1566
- GCC_except_table1567
- GCC_except_table1570
- GCC_except_table1571
- GCC_except_table1725
- GCC_except_table242
- GCC_except_table243
- GCC_except_table247
- GCC_except_table250
- GCC_except_table251
- GCC_except_table254
- GCC_except_table259
- GCC_except_table260
- GCC_except_table270
- GCC_except_table273
- GCC_except_table295
- GCC_except_table298
- GCC_except_table316
- GCC_except_table324
- GCC_except_table362
- GCC_except_table372
- GCC_except_table384
- GCC_except_table419
- GCC_except_table420
- GCC_except_table424
- GCC_except_table449
- GCC_except_table478
- GCC_except_table499
- GCC_except_table500
- GCC_except_table528
- GCC_except_table555
- GCC_except_table568
- GCC_except_table624
- GCC_except_table635
- GCC_except_table661
- GCC_except_table667
- GCC_except_table680
- GCC_except_table681
- GCC_except_table692
- GCC_except_table714
- GCC_except_table740
- GCC_except_table741
- GCC_except_table742
- GCC_except_table766
- GCC_except_table830
- GCC_except_table851
- GCC_except_table872
- GCC_except_table876
- GCC_except_table880
- GCC_except_table909
- GCC_except_table932
- GCC_except_table961
- GCC_except_table962
- GCC_except_table971
- GCC_except_table987
- GCC_except_table988
- ___block_descriptor_65_e8_32s40s48s56s_e40_v16?0"SPConcreteCoreSpotlightIndexer"8l
CStrings:
+ "\"\\"
+ "%@\n%@"
+ "UA-CAP: dropping user activity for %{public}@ (dataclass %{public}@): count %u >= cap %u (shared:%d)"
+ "UA-PURGE uapurge: fixup error for %{public}@: %{public}@"
+ "UA-PURGE: delete error for %{public}@/%{public}@: %{public}@"
+ "UA-PURGE: deleted %ld for %{public}@/%{public}@"
+ "UA-PURGE: fixup aborted before vacuum (delete error), will retry next launch"
+ "UA-PURGE: fixup complete for %{public}@, version %ld -> %ld"
+ "UA-PURGE: fixup deferred for %{public}@, will retry next launch (version still %ld): %{public}@"
+ "UA-PURGE: no vacuum owed (delete state %ld), skipping vacuum"
+ "UA-PURGE: refusing delete with empty bundleID(%{public}@) or activityType(%{public}@)"
+ "UA-PURGE: refusing delete with unsafe characters in bundleID(%{public}@) or activityType(%{public}@)"
+ "UA-PURGE: skipped vacuum, insufficient free space (deleted %ld), will retry next launch"
+ "UA-PURGE: skipping fixup for %{public}@, stored version %ld %{public}s target %d"
+ "UA-PURGE: starting fixup for %{public}@ (version before: %ld, target: %d)"
+ "UA-PURGE: vacuum complete (size query unavailable)"
+ "UA-PURGE: vacuum complete, reclaimed %lld bytes (best-effort)"
+ "UA-PURGE: vacuum error: %{public}@ (version not stamped, will retry)"
+ "UA-PURGE: vacuum requested (deleted %ld)"
+ "_finishUserActivityPurgeWithDeleted:completionHandler:"
+ "_kMDItemBundleID=\"%@\" && _kMDItemUserActivityType=\"%@\""
+ "ahead of"
+ "already at"
+ "com.apple.Keynote"
+ "com.apple.Numbers"
+ "com.apple.Pages"
+ "com.apple.iWork.Keynote"
+ "com.apple.iWork.Numbers"
+ "com.apple.iWork.Pages"
+ "com.apple.keynote.documentEditing"
+ "com.apple.numbers.documentEditing"
+ "com.apple.pages.documentEditing"
+ "contentTypeTree"
+ "deleteUserActivitiesForBundleID:activityType:fromClient:completionHandler:"
+ "initWithObjects:"
+ "issueUserActivityPurgeCommand:completionHandler:"
+ "issueUserActivityPurgeFixup:"
+ "kSPUserActivityDelete"
+ "kSPUserActivityPurge"
+ "openIndex index delegate directory is NULL"
+ "resetUserActivityPurgeFixupVersion"
+ "runUserActivityPurgeFixupWithGroup:"
+ "uapurge"
+ "v28@0:8B16@?20"
- "25F"
```
