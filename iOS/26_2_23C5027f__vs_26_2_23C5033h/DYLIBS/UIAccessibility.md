## UIAccessibility

> `/System/Library/PrivateFrameworks/UIAccessibility.framework/UIAccessibility`

```diff

-3191.7.13.0.0
-  __TEXT.__text: 0x6698c
+3191.7.15.0.0
+  __TEXT.__text: 0x669a4
   __TEXT.__auth_stubs: 0x15c0
-  __TEXT.__objc_methlist: 0x6a5c
+  __TEXT.__objc_methlist: 0x6a74
   __TEXT.__const: 0x2d0
-  __TEXT.__cstring: 0x6d0d
+  __TEXT.__cstring: 0x6d4c
   __TEXT.__oslogstring: 0x2c88
   __TEXT.__gcc_except_tab: 0xddc
   __TEXT.__dlopen_cstrs: 0x266
   __TEXT.__ustring: 0x14
   __TEXT.__unwind_info: 0x1bf0
   __TEXT.__objc_classname: 0xb74
-  __TEXT.__objc_methname: 0x16fc5
+  __TEXT.__objc_methname: 0x17025
   __TEXT.__objc_methtype: 0x1f3a
   __TEXT.__objc_stubs: 0x10920
   __DATA_CONST.__got: 0xd20

   __DATA_CONST.__objc_catlist: 0xa8
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x55b0
+  __DATA_CONST.__objc_selrefs: 0x55c0
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x110
   __DATA_CONST.__objc_arraydata: 0x128
   __AUTH_CONST.__auth_got: 0xaf0
   __AUTH_CONST.__const: 0x1208
-  __AUTH_CONST.__cfstring: 0x62c0
+  __AUTH_CONST.__cfstring: 0x62e0
   __AUTH_CONST.__objc_const: 0x4970
   __AUTH_CONST.__objc_intobj: 0x4b0
   __AUTH_CONST.__objc_dictobj: 0x78

   __AUTH.__objc_data: 0xe60
   __DATA.__objc_ivar: 0x178
   __DATA.__data: 0x748
-  __DATA.__bss: 0x4c8
+  __DATA.__bss: 0x4e0
   __DATA.__common: 0x11
   __DATA_DIRTY.__objc_data: 0x4b0
-  __DATA_DIRTY.__bss: 0x228
+  __DATA_DIRTY.__bss: 0x210
   __DATA_DIRTY.__common: 0x254
   - /System/Library/Frameworks/Accessibility.framework/Accessibility
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 06191CEA-048C-311C-8F76-D29C6C3228B3
-  Functions: 2763
-  Symbols:   9647
-  CStrings:  5346
+  UUID: 0BF37AE5-AA16-3E2C-BC4A-47118F1AB33A
+  Functions: 2765
+  Symbols:   9651
+  CStrings:  5350
 
Symbols:
+ -[NSObject(AXPrivCategory) _accessibilitySetUseAccessibilityFrameForHittest:]
+ -[NSObject(AXPrivCategory) _accessibilityUseAccessibilityFrameForHittest]
+ GCC_except_table100
+ GCC_except_table1052
+ GCC_except_table1160
+ GCC_except_table1207
+ GCC_except_table122
+ GCC_except_table126
+ GCC_except_table132
+ GCC_except_table1349
+ GCC_except_table144
+ GCC_except_table172
+ GCC_except_table221
+ GCC_except_table224
+ GCC_except_table236
+ GCC_except_table275
+ GCC_except_table295
+ GCC_except_table353
+ GCC_except_table356
+ GCC_except_table429
+ GCC_except_table430
+ GCC_except_table435
+ GCC_except_table468
+ GCC_except_table479
+ GCC_except_table494
+ GCC_except_table502
+ GCC_except_table601
+ GCC_except_table711
+ GCC_except_table722
+ GCC_except_table747
+ GCC_except_table751
+ GCC_except_table769
+ GCC_except_table80
+ GCC_except_table808
+ GCC_except_table818
+ GCC_except_table84
+ GCC_except_table849
+ GCC_except_table87
+ GCC_except_table881
+ GCC_except_table96
+ _UIAccessibilityStorageKeyShouldUseAccessibilityFrameForHittest_block_invoke.BaseImplementation
+ _UIAccessibilityStorageKeyShouldUseAccessibilityFrameForHittest_block_invoke.onceToken
+ _UIAccessibilityStorageKeyShouldUseAccessibilityFrameForHittest_block_invoke_2.BaseNSObjectMethod
+ ___104+[UIAccessibilityLoader _performInitialAccessibilityBundleLoad:monitorForFutureLoadEvents:trackingMode:]_block_invoke.290
+ ___104+[UIAccessibilityLoader _performInitialAccessibilityBundleLoad:monitorForFutureLoadEvents:trackingMode:]_block_invoke.298
+ ___104+[UIAccessibilityLoader _performInitialAccessibilityBundleLoad:monitorForFutureLoadEvents:trackingMode:]_block_invoke.303
+ ___104+[UIAccessibilityLoader _performInitialAccessibilityBundleLoad:monitorForFutureLoadEvents:trackingMode:]_block_invoke.310
+ ___104+[UIAccessibilityLoader _performInitialAccessibilityBundleLoad:monitorForFutureLoadEvents:trackingMode:]_block_invoke_2.304
+ ___106-[NSObject(UIAccessibilityElementTraversal) _accessibilityEnumerateSiblingsWithParent:options:usingBlock:]_block_invoke.497
+ ___148-[NSObject(UIAccessibilityAutomation) _accessibilityUserTestingSnapshotAncestorsWithAttributes:maxDepth:maxChildren:maxArrayCount:honorsModalViews:]_block_invoke.402
+ ___148-[NSObject(UIAccessibilityAutomation) _accessibilityUserTestingSnapshotAncestorsWithAttributes:maxDepth:maxChildren:maxArrayCount:honorsModalViews:]_block_invoke.402.cold.1
+ ___149-[NSObject(AXPrivCategory) _accessibilityNextOpaqueElementsForTechnology:startElement:direction:searchType:range:shouldScrollToVisible:honorsGroups:]_block_invoke.1396
+ ___150-[NSObject(UIAccessibilityAutomation) _accessibilityUserTestingSnapshotDescendantsWithAttributes:maxDepth:maxChildren:maxArrayCount:honorsModalViews:]_block_invoke.399
+ ___150-[NSObject(UIAccessibilityAutomation) _accessibilityUserTestingSnapshotDescendantsWithAttributes:maxDepth:maxChildren:maxArrayCount:honorsModalViews:]_block_invoke.399.cold.1
+ ___150-[NSObject(UIAccessibilityAutomation) _accessibilityUserTestingSnapshotDescendantsWithAttributes:maxDepth:maxChildren:maxArrayCount:honorsModalViews:]_block_invoke.399.cold.2
+ ___150-[NSObject(UIAccessibilityAutomation) _accessibilityUserTestingSnapshotDescendantsWithAttributes:maxDepth:maxChildren:maxArrayCount:honorsModalViews:]_block_invoke.399.cold.3
+ ___174-[NSObject(AXPrivCategory) _accessibilitySearchSubtreesAfterChildElement:direction:searchType:allowOutOfBoundsChild:range:shouldScrollToVisible:honorGroups:updatedContainer:]_block_invoke.1412
+ ___174-[NSObject(AXPrivCategory) _accessibilitySearchSubtreesAfterChildElement:direction:searchType:allowOutOfBoundsChild:range:shouldScrollToVisible:honorGroups:updatedContainer:]_block_invoke.1417
+ ___60+[UIAccessibilityLegacyLoader _accessibilityLoadSubbundles:]_block_invoke.379
+ ___60+[UIAccessibilityLegacyLoader _accessibilityLoadSubbundles:]_block_invoke_2.380
+ ___60-[NSObject(AXPrivCategory) _iosAccessibilityAttributeValue:]_block_invoke.1137
+ ___60-[NSObject(AXPrivCategory) _iosAccessibilityAttributeValue:]_block_invoke.1137.cold.1
+ ___60-[NSObject(AXPrivCategory) _iosAccessibilityAttributeValue:]_block_invoke.1137.cold.2
+ ___60-[NSObject(AXPrivCategory) _iosAccessibilityAttributeValue:]_block_invoke.1164
+ ___63+[UIAccessibilityLegacyLoader loadExtendedAccessibilityBundles]_block_invoke.318
+ ___63+[UIAccessibilityLegacyLoader loadExtendedAccessibilityBundles]_block_invoke.320
+ ___79-[NSObject(AXPrivCategory) _accessibilityReplaceCharactersAtCursor:withString:]_block_invoke.1877
+ ____copyElementAtPositionCallback_block_invoke.296
+ ____copyElementAtPositionCallback_block_invoke.310
+ ___block_literal_global.1007
+ ___block_literal_global.1009
+ ___block_literal_global.1038
+ ___block_literal_global.1119
+ ___block_literal_global.1139
+ ___block_literal_global.1167
+ ___block_literal_global.1284
+ ___block_literal_global.1336
+ ___block_literal_global.1338
+ ___block_literal_global.1387
+ ___block_literal_global.1389
+ ___block_literal_global.1393
+ ___block_literal_global.1395
+ ___block_literal_global.1398
+ ___block_literal_global.1404
+ ___block_literal_global.1415
+ ___block_literal_global.1420
+ ___block_literal_global.1436
+ ___block_literal_global.1441
+ ___block_literal_global.1443
+ ___block_literal_global.1449
+ ___block_literal_global.1451
+ ___block_literal_global.1457
+ ___block_literal_global.1544
+ ___block_literal_global.1547
+ ___block_literal_global.1865
+ ___block_literal_global.1873
+ ___block_literal_global.1879
+ ___block_literal_global.1945
+ ___block_literal_global.1964
+ ___block_literal_global.1985
+ ___block_literal_global.1987
+ ___block_literal_global.1990
+ ___block_literal_global.1992
+ ___block_literal_global.1996
+ ___block_literal_global.291
+ ___block_literal_global.293
+ ___block_literal_global.295
+ ___block_literal_global.296
+ ___block_literal_global.298
+ ___block_literal_global.306
+ ___block_literal_global.3078
+ ___block_literal_global.310
+ ___block_literal_global.313
+ ___block_literal_global.321
+ ___block_literal_global.3284
+ ___block_literal_global.3286
+ ___block_literal_global.3288
+ ___block_literal_global.3296
+ ___block_literal_global.3304
+ ___block_literal_global.3307
+ ___block_literal_global.3309
+ ___block_literal_global.333
+ ___block_literal_global.348
+ ___block_literal_global.365
+ ___block_literal_global.368
+ ___block_literal_global.372
+ ___block_literal_global.375
+ ___block_literal_global.389
+ ___block_literal_global.395
+ ___block_literal_global.400
+ ___block_literal_global.401
+ ___block_literal_global.410
+ ___block_literal_global.413
+ ___block_literal_global.414
+ ___block_literal_global.428
+ ___block_literal_global.459
+ ___block_literal_global.460
+ ___block_literal_global.462
+ ___block_literal_global.464
+ ___block_literal_global.490
+ ___block_literal_global.496
+ ___block_literal_global.506
+ ___block_literal_global.517
+ ___block_literal_global.555
+ ___block_literal_global.557
+ ___block_literal_global.561
+ ___block_literal_global.563
+ ___block_literal_global.565
+ ___block_literal_global.567
+ ___block_literal_global.569
+ ___block_literal_global.609
+ ___block_literal_global.619
+ ___block_literal_global.692
+ ___block_literal_global.740
+ ___block_literal_global.742
+ ___block_literal_global.749
+ ___block_literal_global.756
+ ___block_literal_global.773
+ ___block_literal_global.777
+ ___block_literal_global.779
+ ___block_literal_global.786
+ ___block_literal_global.886
+ ___block_literal_global.959
+ ___block_literal_global.990
+ ___block_literal_global.998
- GCC_except_table1050
- GCC_except_table1158
- GCC_except_table120
- GCC_except_table1205
- GCC_except_table124
- GCC_except_table128
- GCC_except_table1347
- GCC_except_table142
- GCC_except_table170
- GCC_except_table219
- GCC_except_table222
- GCC_except_table234
- GCC_except_table273
- GCC_except_table293
- GCC_except_table351
- GCC_except_table354
- GCC_except_table426
- GCC_except_table427
- GCC_except_table433
- GCC_except_table466
- GCC_except_table477
- GCC_except_table488
- GCC_except_table500
- GCC_except_table599
- GCC_except_table709
- GCC_except_table720
- GCC_except_table745
- GCC_except_table749
- GCC_except_table767
- GCC_except_table78
- GCC_except_table806
- GCC_except_table816
- GCC_except_table82
- GCC_except_table847
- GCC_except_table85
- GCC_except_table879
- GCC_except_table92
- GCC_except_table98
- _UIAccessibilityStorageKeyShouldHittestFallBackToNearestChild_block_invoke.BaseImplementation
- _UIAccessibilityStorageKeyShouldHittestFallBackToNearestChild_block_invoke.onceToken
- _UIAccessibilityStorageKeyShouldHittestFallBackToNearestChild_block_invoke_2.BaseNSObjectMethod
- ___104+[UIAccessibilityLoader _performInitialAccessibilityBundleLoad:monitorForFutureLoadEvents:trackingMode:]_block_invoke.281
- ___104+[UIAccessibilityLoader _performInitialAccessibilityBundleLoad:monitorForFutureLoadEvents:trackingMode:]_block_invoke.289
- ___104+[UIAccessibilityLoader _performInitialAccessibilityBundleLoad:monitorForFutureLoadEvents:trackingMode:]_block_invoke.294
- ___104+[UIAccessibilityLoader _performInitialAccessibilityBundleLoad:monitorForFutureLoadEvents:trackingMode:]_block_invoke.301
- ___104+[UIAccessibilityLoader _performInitialAccessibilityBundleLoad:monitorForFutureLoadEvents:trackingMode:]_block_invoke_2.295
- ___106-[NSObject(UIAccessibilityElementTraversal) _accessibilityEnumerateSiblingsWithParent:options:usingBlock:]_block_invoke.488
- ___148-[NSObject(UIAccessibilityAutomation) _accessibilityUserTestingSnapshotAncestorsWithAttributes:maxDepth:maxChildren:maxArrayCount:honorsModalViews:]_block_invoke.393
- ___148-[NSObject(UIAccessibilityAutomation) _accessibilityUserTestingSnapshotAncestorsWithAttributes:maxDepth:maxChildren:maxArrayCount:honorsModalViews:]_block_invoke.393.cold.1
- ___149-[NSObject(AXPrivCategory) _accessibilityNextOpaqueElementsForTechnology:startElement:direction:searchType:range:shouldScrollToVisible:honorsGroups:]_block_invoke.1384
- ___150-[NSObject(UIAccessibilityAutomation) _accessibilityUserTestingSnapshotDescendantsWithAttributes:maxDepth:maxChildren:maxArrayCount:honorsModalViews:]_block_invoke.390
- ___150-[NSObject(UIAccessibilityAutomation) _accessibilityUserTestingSnapshotDescendantsWithAttributes:maxDepth:maxChildren:maxArrayCount:honorsModalViews:]_block_invoke.390.cold.1
- ___150-[NSObject(UIAccessibilityAutomation) _accessibilityUserTestingSnapshotDescendantsWithAttributes:maxDepth:maxChildren:maxArrayCount:honorsModalViews:]_block_invoke.390.cold.2
- ___150-[NSObject(UIAccessibilityAutomation) _accessibilityUserTestingSnapshotDescendantsWithAttributes:maxDepth:maxChildren:maxArrayCount:honorsModalViews:]_block_invoke.390.cold.3
- ___174-[NSObject(AXPrivCategory) _accessibilitySearchSubtreesAfterChildElement:direction:searchType:allowOutOfBoundsChild:range:shouldScrollToVisible:honorGroups:updatedContainer:]_block_invoke.1400
- ___174-[NSObject(AXPrivCategory) _accessibilitySearchSubtreesAfterChildElement:direction:searchType:allowOutOfBoundsChild:range:shouldScrollToVisible:honorGroups:updatedContainer:]_block_invoke.1405
- ___60+[UIAccessibilityLegacyLoader _accessibilityLoadSubbundles:]_block_invoke.370
- ___60+[UIAccessibilityLegacyLoader _accessibilityLoadSubbundles:]_block_invoke_2.371
- ___60-[NSObject(AXPrivCategory) _iosAccessibilityAttributeValue:]_block_invoke.1125
- ___60-[NSObject(AXPrivCategory) _iosAccessibilityAttributeValue:]_block_invoke.1125.cold.1
- ___60-[NSObject(AXPrivCategory) _iosAccessibilityAttributeValue:]_block_invoke.1125.cold.2
- ___60-[NSObject(AXPrivCategory) _iosAccessibilityAttributeValue:]_block_invoke.1152
- ___63+[UIAccessibilityLegacyLoader loadExtendedAccessibilityBundles]_block_invoke.309
- ___63+[UIAccessibilityLegacyLoader loadExtendedAccessibilityBundles]_block_invoke.311
- ___79-[NSObject(AXPrivCategory) _accessibilityReplaceCharactersAtCursor:withString:]_block_invoke.1865
- ____copyElementAtPositionCallback_block_invoke.287
- ____copyElementAtPositionCallback_block_invoke.301
- ___block_literal_global.1026
- ___block_literal_global.1107
- ___block_literal_global.1127
- ___block_literal_global.1155
- ___block_literal_global.1272
- ___block_literal_global.1324
- ___block_literal_global.1326
- ___block_literal_global.1365
- ___block_literal_global.1369
- ___block_literal_global.1371
- ___block_literal_global.1375
- ___block_literal_global.1386
- ___block_literal_global.1392
- ___block_literal_global.1396
- ___block_literal_global.1403
- ___block_literal_global.1424
- ___block_literal_global.1429
- ___block_literal_global.1431
- ___block_literal_global.1433
- ___block_literal_global.1437
- ___block_literal_global.1439
- ___block_literal_global.1532
- ___block_literal_global.1535
- ___block_literal_global.1853
- ___block_literal_global.1855
- ___block_literal_global.1861
- ___block_literal_global.1933
- ___block_literal_global.1952
- ___block_literal_global.1963
- ___block_literal_global.1973
- ___block_literal_global.1978
- ___block_literal_global.1980
- ___block_literal_global.1984
- ___block_literal_global.282
- ___block_literal_global.283
- ___block_literal_global.284
- ___block_literal_global.286
- ___block_literal_global.287
- ___block_literal_global.289
- ___block_literal_global.294
- ___block_literal_global.297
- ___block_literal_global.304
- ___block_literal_global.3064
- ___block_literal_global.315
- ___block_literal_global.3270
- ___block_literal_global.3272
- ___block_literal_global.3274
- ___block_literal_global.3282
- ___block_literal_global.3290
- ___block_literal_global.3293
- ___block_literal_global.3295
- ___block_literal_global.339
- ___block_literal_global.350
- ___block_literal_global.354
- ___block_literal_global.356
- ___block_literal_global.366
- ___block_literal_global.377
- ___block_literal_global.382
- ___block_literal_global.384
- ___block_literal_global.386
- ___block_literal_global.392
- ___block_literal_global.398
- ___block_literal_global.404
- ___block_literal_global.419
- ___block_literal_global.438
- ___block_literal_global.443
- ___block_literal_global.448
- ___block_literal_global.453
- ___block_literal_global.481
- ___block_literal_global.487
- ___block_literal_global.497
- ___block_literal_global.508
- ___block_literal_global.546
- ___block_literal_global.548
- ___block_literal_global.549
- ___block_literal_global.552
- ___block_literal_global.554
- ___block_literal_global.556
- ___block_literal_global.560
- ___block_literal_global.600
- ___block_literal_global.610
- ___block_literal_global.683
- ___block_literal_global.728
- ___block_literal_global.730
- ___block_literal_global.737
- ___block_literal_global.744
- ___block_literal_global.761
- ___block_literal_global.765
- ___block_literal_global.767
- ___block_literal_global.774
- ___block_literal_global.874
- ___block_literal_global.947
- ___block_literal_global.978
- ___block_literal_global.986
- ___block_literal_global.995
- ___block_literal_global.997
CStrings:
+ "UIAccessibilityStorageKeyShouldUseAccessibilityFrameForHittest"
+ "_accessibilitySetUseAccessibilityFrameForHittest:"
+ "_accessibilityUseAccessibilityFrameForHittest"

```
