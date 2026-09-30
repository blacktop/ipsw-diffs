## SpotlightDaemon

> `/System/Library/PrivateFrameworks/SpotlightDaemon.framework/SpotlightDaemon`

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

-  __TEXT.__text: 0xbdb54
-  __TEXT.__auth_stubs: 0x2040
-  __TEXT.__objc_methlist: 0x4714
-  __TEXT.__const: 0x3c8
-  __TEXT.__cstring: 0x8ca3
-  __TEXT.__gcc_except_tab: 0x46bc
-  __TEXT.__oslogstring: 0xb5af
+  __TEXT.__text: 0xbf964
+  __TEXT.__auth_stubs: 0x2050
+  __TEXT.__objc_methlist: 0x475c
+  __TEXT.__const: 0x3e0
+  __TEXT.__cstring: 0x8e08
+  __TEXT.__gcc_except_tab: 0x4738
+  __TEXT.__oslogstring: 0xba6d
   __TEXT.__dlopen_cstrs: 0x4a
-  __TEXT.__unwind_info: 0x27a8
+  __TEXT.__unwind_info: 0x2828
   __TEXT.__objc_classname: 0x5b0
-  __TEXT.__objc_methname: 0xfea3
-  __TEXT.__objc_methtype: 0x27df
-  __TEXT.__objc_stubs: 0xc960
+  __TEXT.__objc_methname: 0xffdb
+  __TEXT.__objc_methtype: 0x27ee
+  __TEXT.__objc_stubs: 0xca60
   __DATA_CONST.__got: 0xbc0
-  __DATA_CONST.__const: 0x40e8
+  __DATA_CONST.__const: 0x4288
   __DATA_CONST.__objc_classlist: 0x1a0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x39a8
+  __DATA_CONST.__objc_selrefs: 0x39e8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x128
   __DATA_CONST.__objc_arraydata: 0x2e0
-  __AUTH_CONST.__auth_got: 0x1038
-  __AUTH_CONST.__const: 0x1188
-  __AUTH_CONST.__cfstring: 0x7820
+  __AUTH_CONST.__auth_got: 0x1040
+  __AUTH_CONST.__const: 0x11c8
+  __AUTH_CONST.__cfstring: 0x7a00
   __AUTH_CONST.__objc_const: 0x5b48
   __AUTH_CONST.__objc_arrayobj: 0x378
   __AUTH_CONST.__objc_intobj: 0x210

   __AUTH.__objc_data: 0x140
   __DATA.__objc_ivar: 0x4c8
   __DATA.__data: 0x810
-  __DATA.__bss: 0x128
+  __DATA.__bss: 0x140
   __DATA.__common: 0x4
   __DATA_DIRTY.__objc_data: 0xf00
   __DATA_DIRTY.__data: 0x158

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  Functions: 3120
-  Symbols:   6349
-  CStrings:  5165
+  Functions: 3151
+  Symbols:   6399
+  CStrings:  5208
 
Symbols:
+ -[SPConcreteCoreSpotlightIndexer _finishUserActivityPurgeWithDeleted:completionHandler:]
+ -[SPConcreteCoreSpotlightIndexer deleteUserActivitiesForBundleID:activityType:fromClient:completionHandler:]
+ -[SPConcreteCoreSpotlightIndexer issueUserActivityPurgeFixup:]
+ -[SPConcreteCoreSpotlightIndexer resetUserActivityPurgeFixupVersion]
+ -[SPConcreteCoreSpotlightIndexer runUserActivityPurgeFixupWithGroup:]
+ -[SPCoreSpotlightIndexer issueUserActivityPurgeCommand:completionHandler:]
+ GCC_except_table1019
+ GCC_except_table1024
+ GCC_except_table1075
+ GCC_except_table1111
+ GCC_except_table1117
+ GCC_except_table1118
+ GCC_except_table1124
+ GCC_except_table1125
+ GCC_except_table1126
+ GCC_except_table1136
+ GCC_except_table1155
+ GCC_except_table1176
+ GCC_except_table1183
+ GCC_except_table1190
+ GCC_except_table1197
+ GCC_except_table1204
+ GCC_except_table1220
+ GCC_except_table1289
+ GCC_except_table1290
+ GCC_except_table1292
+ GCC_except_table1298
+ GCC_except_table1345
+ GCC_except_table1352
+ GCC_except_table1474
+ GCC_except_table1479
+ GCC_except_table1480
+ GCC_except_table1541
+ GCC_except_table1544
+ GCC_except_table1546
+ GCC_except_table1549
+ GCC_except_table1550
+ GCC_except_table1744
+ GCC_except_table205
+ GCC_except_table215
+ GCC_except_table218
+ GCC_except_table221
+ GCC_except_table222
+ GCC_except_table225
+ GCC_except_table230
+ GCC_except_table231
+ GCC_except_table239
+ GCC_except_table240
+ GCC_except_table253
+ GCC_except_table260
+ GCC_except_table274
+ GCC_except_table282
+ GCC_except_table321
+ GCC_except_table331
+ GCC_except_table343
+ GCC_except_table375
+ GCC_except_table376
+ GCC_except_table380
+ GCC_except_table402
+ GCC_except_table431
+ GCC_except_table432
+ GCC_except_table447
+ GCC_except_table448
+ GCC_except_table478
+ GCC_except_table502
+ GCC_except_table516
+ GCC_except_table519
+ GCC_except_table532
+ GCC_except_table533
+ GCC_except_table569
+ GCC_except_table583
+ GCC_except_table594
+ GCC_except_table613
+ GCC_except_table619
+ GCC_except_table636
+ GCC_except_table637
+ GCC_except_table646
+ GCC_except_table668
+ GCC_except_table693
+ GCC_except_table694
+ GCC_except_table695
+ GCC_except_table719
+ GCC_except_table783
+ GCC_except_table807
+ GCC_except_table828
+ GCC_except_table832
+ GCC_except_table836
+ GCC_except_table864
+ GCC_except_table893
+ GCC_except_table923
+ GCC_except_table952
+ GCC_except_table953
+ GCC_except_table962
+ GCC_except_table978
+ GCC_except_table979
+ _OUTLINED_FUNCTION_51
+ _OUTLINED_FUNCTION_52
+ _OUTLINED_FUNCTION_53
+ _SIGetAccumulatedUACountResolved
+ ___108-[SPConcreteCoreSpotlightIndexer deleteUserActivitiesForBundleID:activityType:fromClient:completionHandler:]_block_invoke
+ ___62-[SPConcreteCoreSpotlightIndexer issueUserActivityPurgeFixup:]_block_invoke
+ ___62-[SPConcreteCoreSpotlightIndexer issueUserActivityPurgeFixup:]_block_invoke_2
+ ___62-[SPConcreteCoreSpotlightIndexer issueUserActivityPurgeFixup:]_block_invoke_3
+ ___62-[SPConcreteCoreSpotlightIndexer issueUserActivityPurgeFixup:]_block_invoke_4
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
+ ___block_descriptor_40_e8_32bs_e20_v24?0"NSError"8q16ls32l8
+ ___block_descriptor_48_e8_32s40w_e17_v16?0"NSError"8lw40l8s32l8
+ ___block_descriptor_56_e8_32s40w_e17_v16?0"NSError"8lw40l8s32l8
+ ___block_descriptor_57_e8_32s40bs_e17_v16?0"NSError"8ls40l8s32l8
+ ___block_descriptor_64_e8_32s40bs48r56r_e5_v8?0lr48l8s40l8s32l8r56l8
+ ___block_descriptor_65_e8_32s40s48bs_e5_v8?0ls32l8s48l8s40l8
+ ___block_descriptor_72_e8_32s40s48r56r_e5_v8?0ls32l8r48l8r56l8s40l8
+ ___block_descriptor_72_e8_32s40s48s56r64r_e20_v24?0"NSError"8q16ls32l8s40l8r56l8r64l8s48l8
+ ___block_descriptor_73_e8_32s40s48s56s64s_e40_v16?0"SPConcreteCoreSpotlightIndexer"8ls32l8s40l8s48l8s56l8s64l8
+ _gMediaStatusDomain_block_invoke_8.sLoggedUACapKeys
+ _gMediaStatusDomain_block_invoke_8.sLoggedUACapKeysLock
+ _gMediaStatusDomain_block_invoke_8.sLoggedUACapOnce
+ _kSPUserActivityPurgeTargets
+ _objc_msgSend$_finishUserActivityPurgeWithDeleted:completionHandler:
+ _objc_msgSend$contentTypeTree
+ _objc_msgSend$deleteUserActivitiesForBundleID:activityType:fromClient:completionHandler:
+ _objc_msgSend$initWithObjects:
+ _objc_msgSend$issueUserActivityPurgeCommand:completionHandler:
+ _objc_msgSend$issueUserActivityPurgeFixup:
+ _objc_msgSend$resetUserActivityPurgeFixupVersion
+ _objc_msgSend$runUserActivityPurgeFixupWithGroup:
- GCC_except_table1000
- GCC_except_table1051
- GCC_except_table1087
- GCC_except_table1093
- GCC_except_table1094
- GCC_except_table1100
- GCC_except_table1101
- GCC_except_table1102
- GCC_except_table1103
- GCC_except_table1112
- GCC_except_table1131
- GCC_except_table1141
- GCC_except_table1158
- GCC_except_table1172
- GCC_except_table1179
- GCC_except_table1195
- GCC_except_table1264
- GCC_except_table1265
- GCC_except_table1267
- GCC_except_table1273
- GCC_except_table1320
- GCC_except_table1327
- GCC_except_table1449
- GCC_except_table1454
- GCC_except_table1455
- GCC_except_table1516
- GCC_except_table1519
- GCC_except_table1521
- GCC_except_table1524
- GCC_except_table1525
- GCC_except_table1714
- GCC_except_table213
- GCC_except_table214
- GCC_except_table219
- GCC_except_table220
- GCC_except_table228
- GCC_except_table229
- GCC_except_table235
- GCC_except_table238
- GCC_except_table251
- GCC_except_table254
- GCC_except_table272
- GCC_except_table280
- GCC_except_table319
- GCC_except_table329
- GCC_except_table341
- GCC_except_table373
- GCC_except_table374
- GCC_except_table378
- GCC_except_table400
- GCC_except_table429
- GCC_except_table430
- GCC_except_table445
- GCC_except_table446
- GCC_except_table476
- GCC_except_table500
- GCC_except_table514
- GCC_except_table517
- GCC_except_table528
- GCC_except_table531
- GCC_except_table568
- GCC_except_table579
- GCC_except_table598
- GCC_except_table604
- GCC_except_table621
- GCC_except_table622
- GCC_except_table631
- GCC_except_table653
- GCC_except_table678
- GCC_except_table679
- GCC_except_table680
- GCC_except_table704
- GCC_except_table768
- GCC_except_table792
- GCC_except_table813
- GCC_except_table817
- GCC_except_table821
- GCC_except_table849
- GCC_except_table878
- GCC_except_table908
- GCC_except_table937
- GCC_except_table938
- GCC_except_table947
- GCC_except_table963
- GCC_except_table964
- ___block_descriptor_65_e8_32s40s48s56s_e40_v16?0"SPConcreteCoreSpotlightIndexer"8ls32l8s40l8s48l8s56l8
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
+ "resetUserActivityPurgeFixupVersion"
+ "runUserActivityPurgeFixupWithGroup:"
+ "uapurge"
+ "v28@0:8B16@?20"
```
