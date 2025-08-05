## UIAccessibility

> `/System/Library/PrivateFrameworks/UIAccessibility.framework/UIAccessibility`

```diff

-3187.1.0.0.0
-  __TEXT.__text: 0x65e00
+3189.2.0.0.0
+  __TEXT.__text: 0x65fc4
   __TEXT.__auth_stubs: 0x15a0
-  __TEXT.__objc_methlist: 0x69ec
+  __TEXT.__objc_methlist: 0x6a14
   __TEXT.__const: 0x2d0
   __TEXT.__cstring: 0x6d01
-  __TEXT.__oslogstring: 0x2c1c
+  __TEXT.__oslogstring: 0x2c1e
   __TEXT.__gcc_except_tab: 0xdd4
   __TEXT.__dlopen_cstrs: 0x266
   __TEXT.__ustring: 0x14
-  __TEXT.__unwind_info: 0x1bc8
+  __TEXT.__unwind_info: 0x1bd0
   __TEXT.__objc_classname: 0xb74
-  __TEXT.__objc_methname: 0x16db4
+  __TEXT.__objc_methname: 0x16e4a
   __TEXT.__objc_methtype: 0x1f0a
-  __TEXT.__objc_stubs: 0x10800
+  __TEXT.__objc_stubs: 0x10860
   __DATA_CONST.__got: 0xd08
   __DATA_CONST.__const: 0x15d0
   __DATA_CONST.__objc_classlist: 0x1e8
   __DATA_CONST.__objc_catlist: 0xa8
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5548
+  __DATA_CONST.__objc_selrefs: 0x5560
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x110
   __DATA_CONST.__objc_arraydata: 0x128

   __DATA.__objc_ivar: 0x178
   __DATA.__data: 0x748
   __DATA.__bss: 0x4c8
-  __DATA.__common: 0x1c
+  __DATA.__common: 0x11
   __DATA_DIRTY.__objc_data: 0x4b0
   __DATA_DIRTY.__bss: 0x220
-  __DATA_DIRTY.__common: 0x238
+  __DATA_DIRTY.__common: 0x23c
   - /System/Library/Frameworks/Accessibility.framework/Accessibility
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/BrowserEngineKit.framework/BrowserEngineKit

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 189482B7-CB1A-380F-90C6-291FCD1BFB32
-  Functions: 2750
-  Symbols:   9607
-  CStrings:  5329
+  UUID: 567ABADF-01DF-342E-A65F-A0ED6D258B33
+  Functions: 2754
+  Symbols:   9617
+  CStrings:  5332
 
Symbols:
+ -[NSObject(AXPrivCategory) _accessibilityElementsForReadingInDirection:]
+ -[NSObject(AXPrivCategory) _accessibilityElementsForReadingInDirection:].cold.1
+ -[NSObject(AXPrivCategory) _accessibilityFindDescendant:shouldStopAtLeafNodes:]
+ -[NSObject(AXPrivCategory) _accessibilityPreviousElementsForAccessibilityReader]
+ GCC_except_table1049
+ GCC_except_table1155
+ GCC_except_table1202
+ GCC_except_table1344
+ GCC_except_table351
+ GCC_except_table354
+ GCC_except_table42
+ GCC_except_table427
+ GCC_except_table428
+ GCC_except_table433
+ GCC_except_table466
+ GCC_except_table47
+ GCC_except_table477
+ GCC_except_table492
+ GCC_except_table50
+ GCC_except_table500
+ GCC_except_table599
+ GCC_except_table709
+ GCC_except_table720
+ GCC_except_table745
+ GCC_except_table749
+ GCC_except_table767
+ GCC_except_table806
+ GCC_except_table816
+ GCC_except_table847
+ GCC_except_table879
+ GCC_except_table90
+ _UIAXStringForAllLeafNodeChildren
+ ___104+[UIAccessibilityLoader _performInitialAccessibilityBundleLoad:monitorForFutureLoadEvents:trackingMode:]_block_invoke.281
+ ___104+[UIAccessibilityLoader _performInitialAccessibilityBundleLoad:monitorForFutureLoadEvents:trackingMode:]_block_invoke.289
+ ___104+[UIAccessibilityLoader _performInitialAccessibilityBundleLoad:monitorForFutureLoadEvents:trackingMode:]_block_invoke.294
+ ___104+[UIAccessibilityLoader _performInitialAccessibilityBundleLoad:monitorForFutureLoadEvents:trackingMode:]_block_invoke.301
+ ___104+[UIAccessibilityLoader _performInitialAccessibilityBundleLoad:monitorForFutureLoadEvents:trackingMode:]_block_invoke_2.295
+ ___148-[NSObject(UIAccessibilityAutomation) _accessibilityUserTestingSnapshotAncestorsWithAttributes:maxDepth:maxChildren:maxArrayCount:honorsModalViews:]_block_invoke.393
+ ___148-[NSObject(UIAccessibilityAutomation) _accessibilityUserTestingSnapshotAncestorsWithAttributes:maxDepth:maxChildren:maxArrayCount:honorsModalViews:]_block_invoke.393.cold.1
+ ___149-[NSObject(AXPrivCategory) _accessibilityNextOpaqueElementsForTechnology:startElement:direction:searchType:range:shouldScrollToVisible:honorsGroups:]_block_invoke.1384
+ ___150-[NSObject(UIAccessibilityAutomation) _accessibilityUserTestingSnapshotDescendantsWithAttributes:maxDepth:maxChildren:maxArrayCount:honorsModalViews:]_block_invoke.390
+ ___150-[NSObject(UIAccessibilityAutomation) _accessibilityUserTestingSnapshotDescendantsWithAttributes:maxDepth:maxChildren:maxArrayCount:honorsModalViews:]_block_invoke.390.cold.1
+ ___150-[NSObject(UIAccessibilityAutomation) _accessibilityUserTestingSnapshotDescendantsWithAttributes:maxDepth:maxChildren:maxArrayCount:honorsModalViews:]_block_invoke.390.cold.2
+ ___150-[NSObject(UIAccessibilityAutomation) _accessibilityUserTestingSnapshotDescendantsWithAttributes:maxDepth:maxChildren:maxArrayCount:honorsModalViews:]_block_invoke.390.cold.3
+ ___174-[NSObject(AXPrivCategory) _accessibilitySearchSubtreesAfterChildElement:direction:searchType:allowOutOfBoundsChild:range:shouldScrollToVisible:honorGroups:updatedContainer:]_block_invoke.1400
+ ___174-[NSObject(AXPrivCategory) _accessibilitySearchSubtreesAfterChildElement:direction:searchType:allowOutOfBoundsChild:range:shouldScrollToVisible:honorGroups:updatedContainer:]_block_invoke.1405
+ ___60+[UIAccessibilityLegacyLoader _accessibilityLoadSubbundles:]_block_invoke.370
+ ___60+[UIAccessibilityLegacyLoader _accessibilityLoadSubbundles:]_block_invoke_2.371
+ ___60-[NSObject(AXPrivCategory) _iosAccessibilityAttributeValue:]_block_invoke.1125
+ ___60-[NSObject(AXPrivCategory) _iosAccessibilityAttributeValue:]_block_invoke.1125.cold.1
+ ___60-[NSObject(AXPrivCategory) _iosAccessibilityAttributeValue:]_block_invoke.1125.cold.2
+ ___60-[NSObject(AXPrivCategory) _iosAccessibilityAttributeValue:]_block_invoke.1152
+ ___63+[UIAccessibilityLegacyLoader loadExtendedAccessibilityBundles]_block_invoke.309
+ ___63+[UIAccessibilityLegacyLoader loadExtendedAccessibilityBundles]_block_invoke.311
+ ___72-[NSObject(AXPrivCategory) _accessibilityElementsForReadingInDirection:]_block_invoke
+ ___79-[NSObject(AXPrivCategory) _accessibilityFindDescendant:shouldStopAtLeafNodes:]_block_invoke
+ ___79-[NSObject(AXPrivCategory) _accessibilityFindDescendant:shouldStopAtLeafNodes:]_block_invoke_2
+ ___79-[NSObject(AXPrivCategory) _accessibilityReplaceCharactersAtCursor:withString:]_block_invoke.1865
+ ____copyElementAtPositionCallback_block_invoke.287
+ ____copyElementAtPositionCallback_block_invoke.301
+ ___block_descriptor_41_e8_32s_e18_v24?0?<B?>816ls32l8
+ ___block_literal_global.1026
+ ___block_literal_global.1107
+ ___block_literal_global.1127
+ ___block_literal_global.1155
+ ___block_literal_global.1270
+ ___block_literal_global.1324
+ ___block_literal_global.1326
+ ___block_literal_global.1365
+ ___block_literal_global.1369
+ ___block_literal_global.1371
+ ___block_literal_global.1375
+ ___block_literal_global.1377
+ ___block_literal_global.1381
+ ___block_literal_global.1386
+ ___block_literal_global.1392
+ ___block_literal_global.1396
+ ___block_literal_global.1403
+ ___block_literal_global.1408
+ ___block_literal_global.1424
+ ___block_literal_global.1429
+ ___block_literal_global.1431
+ ___block_literal_global.1433
+ ___block_literal_global.1437
+ ___block_literal_global.1439
+ ___block_literal_global.1445
+ ___block_literal_global.1535
+ ___block_literal_global.1853
+ ___block_literal_global.1855
+ ___block_literal_global.1861
+ ___block_literal_global.1867
+ ___block_literal_global.1930
+ ___block_literal_global.1949
+ ___block_literal_global.1960
+ ___block_literal_global.1970
+ ___block_literal_global.1975
+ ___block_literal_global.1977
+ ___block_literal_global.1981
+ ___block_literal_global.282
+ ___block_literal_global.287
+ ___block_literal_global.292
+ ___block_literal_global.297
+ ___block_literal_global.303
+ ___block_literal_global.304
+ ___block_literal_global.3057
+ ___block_literal_global.315
+ ___block_literal_global.324
+ ___block_literal_global.3263
+ ___block_literal_global.3265
+ ___block_literal_global.3267
+ ___block_literal_global.3275
+ ___block_literal_global.3283
+ ___block_literal_global.3286
+ ___block_literal_global.3288
+ ___block_literal_global.339
+ ___block_literal_global.350
+ ___block_literal_global.354
+ ___block_literal_global.359
+ ___block_literal_global.366
+ ___block_literal_global.377
+ ___block_literal_global.382
+ ___block_literal_global.384
+ ___block_literal_global.386
+ ___block_literal_global.391
+ ___block_literal_global.392
+ ___block_literal_global.393
+ ___block_literal_global.398
+ ___block_literal_global.402
+ ___block_literal_global.404
+ ___block_literal_global.419
+ ___block_literal_global.438
+ ___block_literal_global.443
+ ___block_literal_global.448
+ ___block_literal_global.453
+ ___block_literal_global.455
+ ___block_literal_global.481
+ ___block_literal_global.487
+ ___block_literal_global.495
+ ___block_literal_global.506
+ ___block_literal_global.543
+ ___block_literal_global.545
+ ___block_literal_global.552
+ ___block_literal_global.556
+ ___block_literal_global.558
+ ___block_literal_global.560
+ ___block_literal_global.600
+ ___block_literal_global.610
+ ___block_literal_global.683
+ ___block_literal_global.728
+ ___block_literal_global.730
+ ___block_literal_global.737
+ ___block_literal_global.744
+ ___block_literal_global.761
+ ___block_literal_global.765
+ ___block_literal_global.767
+ ___block_literal_global.774
+ ___block_literal_global.874
+ ___block_literal_global.947
+ ___block_literal_global.978
+ ___block_literal_global.986
+ ___block_literal_global.995
+ ___block_literal_global.997
+ __accessibilityElementsForReadingInDirection:.onceToken
+ __accessibilityElementsForReadingInDirection:.speakThisElementsBaseMethod
+ __accessibilityElementsForReadingInDirection:.speakThisElementsVCBaseMethod
+ _objc_msgSend$_accessibilityElementsForReadingInDirection:
+ _objc_msgSend$_accessibilityFindDescendant:shouldStopAtLeafNodes:
+ _objc_msgSend$_accessibilityPreviousElementsForAccessibilityReader
- -[NSObject(AXPrivCategory) _accessibilityNextElementsForSpeakThis].cold.1
- GCC_except_table1046
- GCC_except_table1152
- GCC_except_table1199
- GCC_except_table1341
- GCC_except_table349
- GCC_except_table352
- GCC_except_table41
- GCC_except_table424
- GCC_except_table425
- GCC_except_table431
- GCC_except_table46
- GCC_except_table464
- GCC_except_table475
- GCC_except_table486
- GCC_except_table498
- GCC_except_table597
- GCC_except_table707
- GCC_except_table718
- GCC_except_table743
- GCC_except_table747
- GCC_except_table764
- GCC_except_table803
- GCC_except_table813
- GCC_except_table844
- GCC_except_table876
- GCC_except_table89
- ___104+[UIAccessibilityLoader _performInitialAccessibilityBundleLoad:monitorForFutureLoadEvents:trackingMode:]_block_invoke.278
- ___104+[UIAccessibilityLoader _performInitialAccessibilityBundleLoad:monitorForFutureLoadEvents:trackingMode:]_block_invoke.286
- ___104+[UIAccessibilityLoader _performInitialAccessibilityBundleLoad:monitorForFutureLoadEvents:trackingMode:]_block_invoke.291
- ___104+[UIAccessibilityLoader _performInitialAccessibilityBundleLoad:monitorForFutureLoadEvents:trackingMode:]_block_invoke.298
- ___104+[UIAccessibilityLoader _performInitialAccessibilityBundleLoad:monitorForFutureLoadEvents:trackingMode:]_block_invoke_2.292
- ___148-[NSObject(UIAccessibilityAutomation) _accessibilityUserTestingSnapshotAncestorsWithAttributes:maxDepth:maxChildren:maxArrayCount:honorsModalViews:]_block_invoke.390
- ___148-[NSObject(UIAccessibilityAutomation) _accessibilityUserTestingSnapshotAncestorsWithAttributes:maxDepth:maxChildren:maxArrayCount:honorsModalViews:]_block_invoke.390.cold.1
- ___149-[NSObject(AXPrivCategory) _accessibilityNextOpaqueElementsForTechnology:startElement:direction:searchType:range:shouldScrollToVisible:honorsGroups:]_block_invoke.1381
- ___150-[NSObject(UIAccessibilityAutomation) _accessibilityUserTestingSnapshotDescendantsWithAttributes:maxDepth:maxChildren:maxArrayCount:honorsModalViews:]_block_invoke.387
- ___150-[NSObject(UIAccessibilityAutomation) _accessibilityUserTestingSnapshotDescendantsWithAttributes:maxDepth:maxChildren:maxArrayCount:honorsModalViews:]_block_invoke.387.cold.1
- ___150-[NSObject(UIAccessibilityAutomation) _accessibilityUserTestingSnapshotDescendantsWithAttributes:maxDepth:maxChildren:maxArrayCount:honorsModalViews:]_block_invoke.387.cold.2
- ___150-[NSObject(UIAccessibilityAutomation) _accessibilityUserTestingSnapshotDescendantsWithAttributes:maxDepth:maxChildren:maxArrayCount:honorsModalViews:]_block_invoke.387.cold.3
- ___174-[NSObject(AXPrivCategory) _accessibilitySearchSubtreesAfterChildElement:direction:searchType:allowOutOfBoundsChild:range:shouldScrollToVisible:honorGroups:updatedContainer:]_block_invoke.1397
- ___174-[NSObject(AXPrivCategory) _accessibilitySearchSubtreesAfterChildElement:direction:searchType:allowOutOfBoundsChild:range:shouldScrollToVisible:honorGroups:updatedContainer:]_block_invoke.1402
- ___57-[NSObject(AXPrivCategory) _accessibilityFindDescendant:]_block_invoke
- ___57-[NSObject(AXPrivCategory) _accessibilityFindDescendant:]_block_invoke_2
- ___60+[UIAccessibilityLegacyLoader _accessibilityLoadSubbundles:]_block_invoke.367
- ___60+[UIAccessibilityLegacyLoader _accessibilityLoadSubbundles:]_block_invoke_2.368
- ___60-[NSObject(AXPrivCategory) _iosAccessibilityAttributeValue:]_block_invoke.1122
- ___60-[NSObject(AXPrivCategory) _iosAccessibilityAttributeValue:]_block_invoke.1122.cold.1
- ___60-[NSObject(AXPrivCategory) _iosAccessibilityAttributeValue:]_block_invoke.1122.cold.2
- ___60-[NSObject(AXPrivCategory) _iosAccessibilityAttributeValue:]_block_invoke.1149
- ___63+[UIAccessibilityLegacyLoader loadExtendedAccessibilityBundles]_block_invoke.306
- ___63+[UIAccessibilityLegacyLoader loadExtendedAccessibilityBundles]_block_invoke.308
- ___66-[NSObject(AXPrivCategory) _accessibilityNextElementsForSpeakThis]_block_invoke
- ___79-[NSObject(AXPrivCategory) _accessibilityReplaceCharactersAtCursor:withString:]_block_invoke.1862
- ____copyElementAtPositionCallback_block_invoke.284
- ____copyElementAtPositionCallback_block_invoke.298
- ___block_descriptor_40_e8_32s_e18_v24?0?<B?>816ls32l8
- ___block_literal_global.1023
- ___block_literal_global.1104
- ___block_literal_global.1124
- ___block_literal_global.1152
- ___block_literal_global.1267
- ___block_literal_global.1321
- ___block_literal_global.1323
- ___block_literal_global.1362
- ___block_literal_global.1366
- ___block_literal_global.1368
- ___block_literal_global.1372
- ___block_literal_global.1374
- ___block_literal_global.1378
- ___block_literal_global.1380
- ___block_literal_global.1389
- ___block_literal_global.1393
- ___block_literal_global.1400
- ___block_literal_global.1405
- ___block_literal_global.1421
- ___block_literal_global.1426
- ___block_literal_global.1428
- ___block_literal_global.1430
- ___block_literal_global.1434
- ___block_literal_global.1436
- ___block_literal_global.1442
- ___block_literal_global.1529
- ___block_literal_global.1850
- ___block_literal_global.1852
- ___block_literal_global.1858
- ___block_literal_global.1864
- ___block_literal_global.1927
- ___block_literal_global.1946
- ___block_literal_global.1957
- ___block_literal_global.1967
- ___block_literal_global.1969
- ___block_literal_global.1974
- ___block_literal_global.1978
- ___block_literal_global.279
- ___block_literal_global.280
- ___block_literal_global.281
- ___block_literal_global.291
- ___block_literal_global.298
- ___block_literal_global.300
- ___block_literal_global.3051
- ___block_literal_global.309
- ___block_literal_global.321
- ___block_literal_global.3257
- ___block_literal_global.3259
- ___block_literal_global.3261
- ___block_literal_global.3269
- ___block_literal_global.3277
- ___block_literal_global.3280
- ___block_literal_global.3282
- ___block_literal_global.336
- ___block_literal_global.347
- ___block_literal_global.351
- ___block_literal_global.353
- ___block_literal_global.360
- ___block_literal_global.374
- ___block_literal_global.379
- ___block_literal_global.381
- ___block_literal_global.383
- ___block_literal_global.388
- ___block_literal_global.389
- ___block_literal_global.390
- ___block_literal_global.395
- ___block_literal_global.399
- ___block_literal_global.401
- ___block_literal_global.416
- ___block_literal_global.435
- ___block_literal_global.440
- ___block_literal_global.445
- ___block_literal_global.447
- ___block_literal_global.452
- ___block_literal_global.478
- ___block_literal_global.484
- ___block_literal_global.492
- ___block_literal_global.503
- ___block_literal_global.540
- ___block_literal_global.542
- ___block_literal_global.546
- ___block_literal_global.551
- ___block_literal_global.553
- ___block_literal_global.555
- ___block_literal_global.597
- ___block_literal_global.607
- ___block_literal_global.680
- ___block_literal_global.725
- ___block_literal_global.727
- ___block_literal_global.734
- ___block_literal_global.741
- ___block_literal_global.758
- ___block_literal_global.762
- ___block_literal_global.764
- ___block_literal_global.771
- ___block_literal_global.871
- ___block_literal_global.944
- ___block_literal_global.975
- ___block_literal_global.983
- ___block_literal_global.992
- ___block_literal_global.994
- __accessibilityNextElementsForSpeakThis.onceToken
- __accessibilityNextElementsForSpeakThis.speakThisElementsBaseMethod
- __accessibilityNextElementsForSpeakThis.speakThisElementsVCBaseMethod
CStrings:
+ "Did not post. Not allowed. notification: %@ (%d) data:%{sensitive}@"
+ "_accessibilityElementsForReadingInDirection:"
+ "_accessibilityFindDescendant:shouldStopAtLeafNodes:"
+ "_accessibilityPreviousElementsForAccessibilityReader"
- "Did not post. Not allowed. notification: %@ (%d) data:%{private}@"

```
