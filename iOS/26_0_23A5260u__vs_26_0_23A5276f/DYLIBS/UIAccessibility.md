## UIAccessibility

> `/System/Library/PrivateFrameworks/UIAccessibility.framework/UIAccessibility`

```diff

-3180.6.1.0.0
-  __TEXT.__text: 0x65914
-  __TEXT.__auth_stubs: 0x1560
-  __TEXT.__objc_methlist: 0x6964
+3183.1.0.0.0
+  __TEXT.__text: 0x659e8
+  __TEXT.__auth_stubs: 0x1580
+  __TEXT.__objc_methlist: 0x6984
   __TEXT.__const: 0x2d0
-  __TEXT.__cstring: 0x6cd5
+  __TEXT.__cstring: 0x6ce2
   __TEXT.__oslogstring: 0x2c06
   __TEXT.__gcc_except_tab: 0xda8
   __TEXT.__dlopen_cstrs: 0x266
   __TEXT.__ustring: 0x14
   __TEXT.__unwind_info: 0x1b70
   __TEXT.__objc_classname: 0xb74
-  __TEXT.__objc_methname: 0x16c6f
-  __TEXT.__objc_methtype: 0x1f07
-  __TEXT.__objc_stubs: 0x10740
+  __TEXT.__objc_methname: 0x16c9a
+  __TEXT.__objc_methtype: 0x1f0a
+  __TEXT.__objc_stubs: 0x10760
   __DATA_CONST.__got: 0xd00
   __DATA_CONST.__const: 0x1588
   __DATA_CONST.__objc_classlist: 0x1e8
-  __DATA_CONST.__objc_catlist: 0xa0
+  __DATA_CONST.__objc_catlist: 0xa8
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x54f8
+  __DATA_CONST.__objc_selrefs: 0x5508
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x110
   __DATA_CONST.__objc_arraydata: 0x128
-  __AUTH_CONST.__auth_got: 0xac0
+  __AUTH_CONST.__auth_got: 0xad0
   __AUTH_CONST.__const: 0x11e8
   __AUTH_CONST.__cfstring: 0x62a0
-  __AUTH_CONST.__objc_const: 0x48f8
+  __AUTH_CONST.__objc_const: 0x4950
   __AUTH_CONST.__objc_intobj: 0x4b0
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH.__objc_data: 0xe60
   __DATA.__objc_ivar: 0x178
   __DATA.__data: 0x748
-  __DATA.__bss: 0x4c0
-  __DATA.__common: 0x11
+  __DATA.__bss: 0x4c8
+  __DATA.__common: 0x1c
   __DATA_DIRTY.__objc_data: 0x4b0
   __DATA_DIRTY.__bss: 0x220
   __DATA_DIRTY.__common: 0x238

   - /System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices
   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /System/Library/PrivateFrameworks/GraphicsServices.framework/GraphicsServices
+  - /System/Library/PrivateFrameworks/HangTracer.framework/HangTracer
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/TextToSpeech.framework/TextToSpeech
   - /usr/lib/libAXSafeCategoryBundle.dylib

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 687D2078-2687-3355-BAE5-71E3EF3D14CE
-  Functions: 2738
-  Symbols:   9563
-  CStrings:  5317
+  UUID: F76610F4-7764-3B8C-BC94-7F160BAE4364
+  Functions: 2740
+  Symbols:   9576
+  CStrings:  5320
 
Symbols:
+ -[NSObject(AXPrivCategory) _accessibilityPerformPublicCustomRotorSearch:searchDirection:currentItem:honorsGroups:]
+ -[UIAccessibilityCustomRotorSearchPredicate(AXPrivate) honorsGroups]
+ -[UIAccessibilityCustomRotorSearchPredicate(AXPrivate) setHonorsGroups:]
+ _HTBeginNonResponsiveTaskWithNameAndExpiration
+ _HTEndNonResponsiveTask
+ _UIAccessibilityEyeTrackingCalibrationEndNotification
+ _UIAccessibilityEyeTrackingCalibrationStartNotification
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_UIAccessibilityCustomRotorSearchPredicate_$_AXPrivate
+ __OBJC_$_CATEGORY_UIAccessibilityCustomRotorSearchPredicate_$_AXPrivate
+ __OBJC_$_PROP_LIST_UIAccessibilityCustomRotorSearchPredicate_$_AXPrivate
+ ___104+[UIAccessibilityLoader _performInitialAccessibilityBundleLoad:monitorForFutureLoadEvents:trackingMode:]_block_invoke.281
+ ___104+[UIAccessibilityLoader _performInitialAccessibilityBundleLoad:monitorForFutureLoadEvents:trackingMode:]_block_invoke.289
+ ___104+[UIAccessibilityLoader _performInitialAccessibilityBundleLoad:monitorForFutureLoadEvents:trackingMode:]_block_invoke.294
+ ___104+[UIAccessibilityLoader _performInitialAccessibilityBundleLoad:monitorForFutureLoadEvents:trackingMode:]_block_invoke.301
+ ___104+[UIAccessibilityLoader _performInitialAccessibilityBundleLoad:monitorForFutureLoadEvents:trackingMode:]_block_invoke_2.295
+ ___148-[NSObject(UIAccessibilityAutomation) _accessibilityUserTestingSnapshotAncestorsWithAttributes:maxDepth:maxChildren:maxArrayCount:honorsModalViews:]_block_invoke.393
+ ___148-[NSObject(UIAccessibilityAutomation) _accessibilityUserTestingSnapshotAncestorsWithAttributes:maxDepth:maxChildren:maxArrayCount:honorsModalViews:]_block_invoke.393.cold.1
+ ___149-[NSObject(AXPrivCategory) _accessibilityNextOpaqueElementsForTechnology:startElement:direction:searchType:range:shouldScrollToVisible:honorsGroups:]_block_invoke.1385
+ ___150-[NSObject(UIAccessibilityAutomation) _accessibilityUserTestingSnapshotDescendantsWithAttributes:maxDepth:maxChildren:maxArrayCount:honorsModalViews:]_block_invoke.390
+ ___150-[NSObject(UIAccessibilityAutomation) _accessibilityUserTestingSnapshotDescendantsWithAttributes:maxDepth:maxChildren:maxArrayCount:honorsModalViews:]_block_invoke.390.cold.1
+ ___150-[NSObject(UIAccessibilityAutomation) _accessibilityUserTestingSnapshotDescendantsWithAttributes:maxDepth:maxChildren:maxArrayCount:honorsModalViews:]_block_invoke.390.cold.2
+ ___150-[NSObject(UIAccessibilityAutomation) _accessibilityUserTestingSnapshotDescendantsWithAttributes:maxDepth:maxChildren:maxArrayCount:honorsModalViews:]_block_invoke.390.cold.3
+ ___174-[NSObject(AXPrivCategory) _accessibilitySearchSubtreesAfterChildElement:direction:searchType:allowOutOfBoundsChild:range:shouldScrollToVisible:honorGroups:updatedContainer:]_block_invoke.1401
+ ___174-[NSObject(AXPrivCategory) _accessibilitySearchSubtreesAfterChildElement:direction:searchType:allowOutOfBoundsChild:range:shouldScrollToVisible:honorGroups:updatedContainer:]_block_invoke.1406
+ ___60+[UIAccessibilityLegacyLoader _accessibilityLoadSubbundles:]_block_invoke.370
+ ___60+[UIAccessibilityLegacyLoader _accessibilityLoadSubbundles:]_block_invoke_2.371
+ ___60-[NSObject(AXPrivCategory) _iosAccessibilityAttributeValue:]_block_invoke.1126
+ ___60-[NSObject(AXPrivCategory) _iosAccessibilityAttributeValue:]_block_invoke.1126.cold.1
+ ___60-[NSObject(AXPrivCategory) _iosAccessibilityAttributeValue:]_block_invoke.1126.cold.2
+ ___60-[NSObject(AXPrivCategory) _iosAccessibilityAttributeValue:]_block_invoke.1153
+ ___63+[UIAccessibilityLegacyLoader loadExtendedAccessibilityBundles]_block_invoke.309
+ ___63+[UIAccessibilityLegacyLoader loadExtendedAccessibilityBundles]_block_invoke.311
+ ___79-[NSObject(AXPrivCategory) _accessibilityReplaceCharactersAtCursor:withString:]_block_invoke.1861
+ ___UIAccessibilityCustomRotorSearchPredicate__honorsGroups
+ ____copyElementAtPositionCallback_block_invoke.287
+ ____copyElementAtPositionCallback_block_invoke.301
+ ___block_literal_global.1027
+ ___block_literal_global.1108
+ ___block_literal_global.1128
+ ___block_literal_global.1156
+ ___block_literal_global.1271
+ ___block_literal_global.1325
+ ___block_literal_global.1327
+ ___block_literal_global.1366
+ ___block_literal_global.1370
+ ___block_literal_global.1372
+ ___block_literal_global.1376
+ ___block_literal_global.1378
+ ___block_literal_global.1382
+ ___block_literal_global.1387
+ ___block_literal_global.1393
+ ___block_literal_global.1397
+ ___block_literal_global.1404
+ ___block_literal_global.1409
+ ___block_literal_global.1425
+ ___block_literal_global.1430
+ ___block_literal_global.1432
+ ___block_literal_global.1434
+ ___block_literal_global.1436
+ ___block_literal_global.1438
+ ___block_literal_global.1444
+ ___block_literal_global.1534
+ ___block_literal_global.1849
+ ___block_literal_global.1851
+ ___block_literal_global.1857
+ ___block_literal_global.1863
+ ___block_literal_global.1926
+ ___block_literal_global.1945
+ ___block_literal_global.1956
+ ___block_literal_global.1966
+ ___block_literal_global.1971
+ ___block_literal_global.1973
+ ___block_literal_global.1977
+ ___block_literal_global.282
+ ___block_literal_global.287
+ ___block_literal_global.292
+ ___block_literal_global.296
+ ___block_literal_global.297
+ ___block_literal_global.303
+ ___block_literal_global.304
+ ___block_literal_global.3047
+ ___block_literal_global.315
+ ___block_literal_global.324
+ ___block_literal_global.3252
+ ___block_literal_global.3254
+ ___block_literal_global.3256
+ ___block_literal_global.3264
+ ___block_literal_global.3275
+ ___block_literal_global.3277
+ ___block_literal_global.339
+ ___block_literal_global.350
+ ___block_literal_global.354
+ ___block_literal_global.359
+ ___block_literal_global.366
+ ___block_literal_global.378
+ ___block_literal_global.382
+ ___block_literal_global.384
+ ___block_literal_global.386
+ ___block_literal_global.391
+ ___block_literal_global.392
+ ___block_literal_global.393
+ ___block_literal_global.399
+ ___block_literal_global.403
+ ___block_literal_global.404
+ ___block_literal_global.419
+ ___block_literal_global.439
+ ___block_literal_global.444
+ ___block_literal_global.449
+ ___block_literal_global.453
+ ___block_literal_global.455
+ ___block_literal_global.481
+ ___block_literal_global.487
+ ___block_literal_global.494
+ ___block_literal_global.505
+ ___block_literal_global.542
+ ___block_literal_global.544
+ ___block_literal_global.549
+ ___block_literal_global.551
+ ___block_literal_global.555
+ ___block_literal_global.556
+ ___block_literal_global.557
+ ___block_literal_global.600
+ ___block_literal_global.610
+ ___block_literal_global.680
+ ___block_literal_global.729
+ ___block_literal_global.731
+ ___block_literal_global.738
+ ___block_literal_global.745
+ ___block_literal_global.762
+ ___block_literal_global.766
+ ___block_literal_global.768
+ ___block_literal_global.775
+ ___block_literal_global.875
+ ___block_literal_global.948
+ ___block_literal_global.979
+ ___block_literal_global.987
+ ___block_literal_global.996
+ ___block_literal_global.998
+ _objc_msgSend$_accessibilityPerformPublicCustomRotorSearch:searchDirection:currentItem:honorsGroups:
+ _objc_msgSend$setHonorsGroups:
- -[NSObject(AXPrivCategory) _accessibilityPerformPublicCustomRotorSearch:searchDirection:currentItem:]
- ___104+[UIAccessibilityLoader _performInitialAccessibilityBundleLoad:monitorForFutureLoadEvents:trackingMode:]_block_invoke.278
- ___104+[UIAccessibilityLoader _performInitialAccessibilityBundleLoad:monitorForFutureLoadEvents:trackingMode:]_block_invoke.286
- ___104+[UIAccessibilityLoader _performInitialAccessibilityBundleLoad:monitorForFutureLoadEvents:trackingMode:]_block_invoke.291
- ___104+[UIAccessibilityLoader _performInitialAccessibilityBundleLoad:monitorForFutureLoadEvents:trackingMode:]_block_invoke.298
- ___104+[UIAccessibilityLoader _performInitialAccessibilityBundleLoad:monitorForFutureLoadEvents:trackingMode:]_block_invoke_2.292
- ___148-[NSObject(UIAccessibilityAutomation) _accessibilityUserTestingSnapshotAncestorsWithAttributes:maxDepth:maxChildren:maxArrayCount:honorsModalViews:]_block_invoke.390
- ___148-[NSObject(UIAccessibilityAutomation) _accessibilityUserTestingSnapshotAncestorsWithAttributes:maxDepth:maxChildren:maxArrayCount:honorsModalViews:]_block_invoke.390.cold.1
- ___149-[NSObject(AXPrivCategory) _accessibilityNextOpaqueElementsForTechnology:startElement:direction:searchType:range:shouldScrollToVisible:honorsGroups:]_block_invoke.1382
- ___150-[NSObject(UIAccessibilityAutomation) _accessibilityUserTestingSnapshotDescendantsWithAttributes:maxDepth:maxChildren:maxArrayCount:honorsModalViews:]_block_invoke.387
- ___150-[NSObject(UIAccessibilityAutomation) _accessibilityUserTestingSnapshotDescendantsWithAttributes:maxDepth:maxChildren:maxArrayCount:honorsModalViews:]_block_invoke.387.cold.1
- ___150-[NSObject(UIAccessibilityAutomation) _accessibilityUserTestingSnapshotDescendantsWithAttributes:maxDepth:maxChildren:maxArrayCount:honorsModalViews:]_block_invoke.387.cold.2
- ___150-[NSObject(UIAccessibilityAutomation) _accessibilityUserTestingSnapshotDescendantsWithAttributes:maxDepth:maxChildren:maxArrayCount:honorsModalViews:]_block_invoke.387.cold.3
- ___174-[NSObject(AXPrivCategory) _accessibilitySearchSubtreesAfterChildElement:direction:searchType:allowOutOfBoundsChild:range:shouldScrollToVisible:honorGroups:updatedContainer:]_block_invoke.1398
- ___174-[NSObject(AXPrivCategory) _accessibilitySearchSubtreesAfterChildElement:direction:searchType:allowOutOfBoundsChild:range:shouldScrollToVisible:honorGroups:updatedContainer:]_block_invoke.1403
- ___60+[UIAccessibilityLegacyLoader _accessibilityLoadSubbundles:]_block_invoke.367
- ___60+[UIAccessibilityLegacyLoader _accessibilityLoadSubbundles:]_block_invoke_2.368
- ___60-[NSObject(AXPrivCategory) _iosAccessibilityAttributeValue:]_block_invoke.1123
- ___60-[NSObject(AXPrivCategory) _iosAccessibilityAttributeValue:]_block_invoke.1123.cold.1
- ___60-[NSObject(AXPrivCategory) _iosAccessibilityAttributeValue:]_block_invoke.1123.cold.2
- ___60-[NSObject(AXPrivCategory) _iosAccessibilityAttributeValue:]_block_invoke.1150
- ___63+[UIAccessibilityLegacyLoader loadExtendedAccessibilityBundles]_block_invoke.306
- ___63+[UIAccessibilityLegacyLoader loadExtendedAccessibilityBundles]_block_invoke.308
- ___79-[NSObject(AXPrivCategory) _accessibilityReplaceCharactersAtCursor:withString:]_block_invoke.1858
- ____copyElementAtPositionCallback_block_invoke.284
- ____copyElementAtPositionCallback_block_invoke.298
- ___block_literal_global.1024
- ___block_literal_global.1105
- ___block_literal_global.1125
- ___block_literal_global.1153
- ___block_literal_global.1268
- ___block_literal_global.1322
- ___block_literal_global.1324
- ___block_literal_global.1363
- ___block_literal_global.1367
- ___block_literal_global.1369
- ___block_literal_global.1373
- ___block_literal_global.1375
- ___block_literal_global.1379
- ___block_literal_global.1381
- ___block_literal_global.1390
- ___block_literal_global.1394
- ___block_literal_global.1401
- ___block_literal_global.1406
- ___block_literal_global.1422
- ___block_literal_global.1427
- ___block_literal_global.1429
- ___block_literal_global.1431
- ___block_literal_global.1433
- ___block_literal_global.1435
- ___block_literal_global.1441
- ___block_literal_global.1528
- ___block_literal_global.1846
- ___block_literal_global.1848
- ___block_literal_global.1854
- ___block_literal_global.1860
- ___block_literal_global.1923
- ___block_literal_global.1942
- ___block_literal_global.1953
- ___block_literal_global.1963
- ___block_literal_global.1965
- ___block_literal_global.1970
- ___block_literal_global.1974
- ___block_literal_global.279
- ___block_literal_global.281
- ___block_literal_global.283
- ___block_literal_global.291
- ___block_literal_global.293
- ___block_literal_global.300
- ___block_literal_global.301
- ___block_literal_global.3044
- ___block_literal_global.309
- ___block_literal_global.321
- ___block_literal_global.3249
- ___block_literal_global.3251
- ___block_literal_global.3253
- ___block_literal_global.3261
- ___block_literal_global.3269
- ___block_literal_global.3274
- ___block_literal_global.336
- ___block_literal_global.347
- ___block_literal_global.351
- ___block_literal_global.353
- ___block_literal_global.360
- ___block_literal_global.375
- ___block_literal_global.379
- ___block_literal_global.381
- ___block_literal_global.383
- ___block_literal_global.388
- ___block_literal_global.389
- ___block_literal_global.390
- ___block_literal_global.396
- ___block_literal_global.400
- ___block_literal_global.401
- ___block_literal_global.415
- ___block_literal_global.436
- ___block_literal_global.441
- ___block_literal_global.446
- ___block_literal_global.447
- ___block_literal_global.452
- ___block_literal_global.477
- ___block_literal_global.483
- ___block_literal_global.491
- ___block_literal_global.502
- ___block_literal_global.539
- ___block_literal_global.541
- ___block_literal_global.543
- ___block_literal_global.548
- ___block_literal_global.550
- ___block_literal_global.552
- ___block_literal_global.554
- ___block_literal_global.597
- ___block_literal_global.607
- ___block_literal_global.677
- ___block_literal_global.726
- ___block_literal_global.728
- ___block_literal_global.735
- ___block_literal_global.742
- ___block_literal_global.759
- ___block_literal_global.763
- ___block_literal_global.765
- ___block_literal_global.772
- ___block_literal_global.872
- ___block_literal_global.945
- ___block_literal_global.976
- ___block_literal_global.984
- ___block_literal_global.993
- ___block_literal_global.995
- _objc_msgSend$_accessibilityPerformPublicCustomRotorSearch:searchDirection:currentItem:
CStrings:
+ "@44@0:8@16q24@32B40"
+ "UIAutomation"
+ "_accessibilityPerformPublicCustomRotorSearch:searchDirection:currentItem:honorsGroups:"
+ "honorsGroups"
+ "setHonorsGroups:"
- "@40@0:8@16q24@32"
- "_accessibilityPerformPublicCustomRotorSearch:searchDirection:currentItem:"

```
