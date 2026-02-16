## UIAccessibility

> `/System/Library/PrivateFrameworks/UIAccessibility.framework/UIAccessibility`

```diff

-3191.7.24.0.0
-  __TEXT.__text: 0x669a4
-  __TEXT.__auth_stubs: 0x15c0
-  __TEXT.__objc_methlist: 0x6a74
+3191.19.0.0.0
+  __TEXT.__text: 0x6ac88
+  __TEXT.__auth_stubs: 0x1550
+  __TEXT.__objc_methlist: 0x6a9c
   __TEXT.__const: 0x2d0
-  __TEXT.__cstring: 0x6d4c
+  __TEXT.__cstring: 0x6f61
   __TEXT.__oslogstring: 0x2c88
-  __TEXT.__gcc_except_tab: 0xddc
+  __TEXT.__gcc_except_tab: 0xdb8
   __TEXT.__dlopen_cstrs: 0x266
   __TEXT.__ustring: 0x14
-  __TEXT.__unwind_info: 0x1bf0
+  __TEXT.__unwind_info: 0x1cc0
   __TEXT.__objc_classname: 0xb74
-  __TEXT.__objc_methname: 0x17025
-  __TEXT.__objc_methtype: 0x1f3a
-  __TEXT.__objc_stubs: 0x10920
+  __TEXT.__objc_methname: 0x170d8
+  __TEXT.__objc_methtype: 0x1f53
+  __TEXT.__objc_stubs: 0x10960
   __DATA_CONST.__got: 0xd20
   __DATA_CONST.__const: 0x1620
   __DATA_CONST.__objc_classlist: 0x1e8
   __DATA_CONST.__objc_catlist: 0xa8
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x55c0
+  __DATA_CONST.__objc_selrefs: 0x55d8
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x110
   __DATA_CONST.__objc_arraydata: 0x128
-  __AUTH_CONST.__auth_got: 0xaf0
-  __AUTH_CONST.__const: 0x1208
-  __AUTH_CONST.__cfstring: 0x62e0
-  __AUTH_CONST.__objc_const: 0x4970
+  __AUTH_CONST.__auth_got: 0xab8
+  __AUTH_CONST.__const: 0x1228
+  __AUTH_CONST.__cfstring: 0x6300
+  __AUTH_CONST.__objc_const: 0x4988
   __AUTH_CONST.__objc_intobj: 0x4b0
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH.__objc_data: 0xe60
   __DATA.__objc_ivar: 0x178
   __DATA.__data: 0x748
-  __DATA.__bss: 0x4e0
+  __DATA.__bss: 0x4c8
   __DATA.__common: 0x11
   __DATA_DIRTY.__objc_data: 0x4b0
-  __DATA_DIRTY.__bss: 0x210
+  __DATA_DIRTY.__bss: 0x220
   __DATA_DIRTY.__common: 0x254
   - /System/Library/Frameworks/Accessibility.framework/Accessibility
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 34896A83-4DD8-3A3D-94E3-5F585128DD18
-  Functions: 2765
-  Symbols:   9651
-  CStrings:  5350
+  UUID: D039242D-77CA-3803-94AC-3E5E60514CB9
+  Functions: 2790
+  Symbols:   9713
+  CStrings:  5357
 
Symbols:
+ -[NSObject(AXPrivCategory) _accessibilityVisiblePointHitTestingAllWindows]
+ -[NSObject(AXPrivCategory) _accessibilityVisiblePointHitTestingAnyElement:shouldCheckAllWindows:]
+ GCC_except_table1054
+ GCC_except_table1162
+ GCC_except_table1209
+ GCC_except_table1351
+ GCC_except_table355
+ GCC_except_table358
+ GCC_except_table431
+ GCC_except_table432
+ GCC_except_table437
+ GCC_except_table470
+ GCC_except_table481
+ GCC_except_table496
+ GCC_except_table504
+ GCC_except_table603
+ GCC_except_table713
+ GCC_except_table724
+ GCC_except_table749
+ GCC_except_table753
+ GCC_except_table771
+ GCC_except_table810
+ GCC_except_table820
+ GCC_except_table851
+ GCC_except_table883
+ _OUTLINED_FUNCTION_27
+ _OUTLINED_FUNCTION_28
+ _OUTLINED_FUNCTION_29
+ _OUTLINED_FUNCTION_30
+ _OUTLINED_FUNCTION_31
+ _OUTLINED_FUNCTION_32
+ _OUTLINED_FUNCTION_33
+ _OUTLINED_FUNCTION_34
+ _OUTLINED_FUNCTION_35
+ _OUTLINED_FUNCTION_36
+ _OUTLINED_FUNCTION_37
+ _OUTLINED_FUNCTION_38
+ _OUTLINED_FUNCTION_39
+ __AXIsWebTouchContainerType
+ ___104+[UIAccessibilityLoader _performInitialAccessibilityBundleLoad:monitorForFutureLoadEvents:trackingMode:]_block_invoke.329
+ ___104+[UIAccessibilityLoader _performInitialAccessibilityBundleLoad:monitorForFutureLoadEvents:trackingMode:]_block_invoke.337
+ ___104+[UIAccessibilityLoader _performInitialAccessibilityBundleLoad:monitorForFutureLoadEvents:trackingMode:]_block_invoke.342
+ ___104+[UIAccessibilityLoader _performInitialAccessibilityBundleLoad:monitorForFutureLoadEvents:trackingMode:]_block_invoke.349
+ ___104+[UIAccessibilityLoader _performInitialAccessibilityBundleLoad:monitorForFutureLoadEvents:trackingMode:]_block_invoke_2.343
+ ___106-[NSObject(UIAccessibilityElementTraversal) _accessibilityEnumerateSiblingsWithParent:options:usingBlock:]_block_invoke.536
+ ___148-[NSObject(UIAccessibilityAutomation) _accessibilityUserTestingSnapshotAncestorsWithAttributes:maxDepth:maxChildren:maxArrayCount:honorsModalViews:]_block_invoke.441
+ ___148-[NSObject(UIAccessibilityAutomation) _accessibilityUserTestingSnapshotAncestorsWithAttributes:maxDepth:maxChildren:maxArrayCount:honorsModalViews:]_block_invoke.441.cold.1
+ ___149-[NSObject(AXPrivCategory) _accessibilityNextOpaqueElementsForTechnology:startElement:direction:searchType:range:shouldScrollToVisible:honorsGroups:]_block_invoke.1435
+ ___150-[NSObject(UIAccessibilityAutomation) _accessibilityUserTestingSnapshotDescendantsWithAttributes:maxDepth:maxChildren:maxArrayCount:honorsModalViews:]_block_invoke.438
+ ___150-[NSObject(UIAccessibilityAutomation) _accessibilityUserTestingSnapshotDescendantsWithAttributes:maxDepth:maxChildren:maxArrayCount:honorsModalViews:]_block_invoke.438.cold.1
+ ___150-[NSObject(UIAccessibilityAutomation) _accessibilityUserTestingSnapshotDescendantsWithAttributes:maxDepth:maxChildren:maxArrayCount:honorsModalViews:]_block_invoke.438.cold.2
+ ___150-[NSObject(UIAccessibilityAutomation) _accessibilityUserTestingSnapshotDescendantsWithAttributes:maxDepth:maxChildren:maxArrayCount:honorsModalViews:]_block_invoke.438.cold.3
+ ___174-[NSObject(AXPrivCategory) _accessibilitySearchSubtreesAfterChildElement:direction:searchType:allowOutOfBoundsChild:range:shouldScrollToVisible:honorGroups:updatedContainer:]_block_invoke.1451
+ ___174-[NSObject(AXPrivCategory) _accessibilitySearchSubtreesAfterChildElement:direction:searchType:allowOutOfBoundsChild:range:shouldScrollToVisible:honorGroups:updatedContainer:]_block_invoke.1456
+ ___60+[UIAccessibilityLegacyLoader _accessibilityLoadSubbundles:]_block_invoke.418
+ ___60+[UIAccessibilityLegacyLoader _accessibilityLoadSubbundles:]_block_invoke_2.419
+ ___60-[NSObject(AXPrivCategory) _iosAccessibilityAttributeValue:]_block_invoke.1176
+ ___60-[NSObject(AXPrivCategory) _iosAccessibilityAttributeValue:]_block_invoke.1176.cold.1
+ ___60-[NSObject(AXPrivCategory) _iosAccessibilityAttributeValue:]_block_invoke.1176.cold.2
+ ___60-[NSObject(AXPrivCategory) _iosAccessibilityAttributeValue:]_block_invoke.1203
+ ___63+[UIAccessibilityLegacyLoader loadExtendedAccessibilityBundles]_block_invoke.357
+ ___63+[UIAccessibilityLegacyLoader loadExtendedAccessibilityBundles]_block_invoke.359
+ ___79-[NSObject(AXPrivCategory) _accessibilityReplaceCharactersAtCursor:withString:]_block_invoke.1919
+ ____axuiElementForNotificationData_block_invoke_2
+ ____copyElementAtPositionCallback_block_invoke.335
+ ____copyElementAtPositionCallback_block_invoke.349
+ ___block_literal_global.1029
+ ___block_literal_global.1037
+ ___block_literal_global.1046
+ ___block_literal_global.1048
+ ___block_literal_global.1077
+ ___block_literal_global.1158
+ ___block_literal_global.1178
+ ___block_literal_global.1206
+ ___block_literal_global.1323
+ ___block_literal_global.1375
+ ___block_literal_global.1416
+ ___block_literal_global.1422
+ ___block_literal_global.1426
+ ___block_literal_global.1428
+ ___block_literal_global.1432
+ ___block_literal_global.1434
+ ___block_literal_global.1437
+ ___block_literal_global.1447
+ ___block_literal_global.1454
+ ___block_literal_global.1459
+ ___block_literal_global.1475
+ ___block_literal_global.1480
+ ___block_literal_global.1482
+ ___block_literal_global.1484
+ ___block_literal_global.1488
+ ___block_literal_global.1490
+ ___block_literal_global.1496
+ ___block_literal_global.1583
+ ___block_literal_global.1586
+ ___block_literal_global.1907
+ ___block_literal_global.1909
+ ___block_literal_global.1915
+ ___block_literal_global.1921
+ ___block_literal_global.2006
+ ___block_literal_global.2017
+ ___block_literal_global.2027
+ ___block_literal_global.2029
+ ___block_literal_global.2032
+ ___block_literal_global.2034
+ ___block_literal_global.2038
+ ___block_literal_global.3123
+ ___block_literal_global.330
+ ___block_literal_global.331
+ ___block_literal_global.332
+ ___block_literal_global.3332
+ ___block_literal_global.3334
+ ___block_literal_global.3336
+ ___block_literal_global.334
+ ___block_literal_global.3344
+ ___block_literal_global.335
+ ___block_literal_global.3352
+ ___block_literal_global.3355
+ ___block_literal_global.3357
+ ___block_literal_global.337
+ ___block_literal_global.340
+ ___block_literal_global.342
+ ___block_literal_global.345
+ ___block_literal_global.349
+ ___block_literal_global.351
+ ___block_literal_global.352
+ ___block_literal_global.360
+ ___block_literal_global.374
+ ___block_literal_global.387
+ ___block_literal_global.398
+ ___block_literal_global.404
+ ___block_literal_global.407
+ ___block_literal_global.411
+ ___block_literal_global.430
+ ___block_literal_global.432
+ ___block_literal_global.434
+ ___block_literal_global.439
+ ___block_literal_global.440
+ ___block_literal_global.441
+ ___block_literal_global.449
+ ___block_literal_global.452
+ ___block_literal_global.453
+ ___block_literal_global.467
+ ___block_literal_global.489
+ ___block_literal_global.494
+ ___block_literal_global.498
+ ___block_literal_global.499
+ ___block_literal_global.501
+ ___block_literal_global.503
+ ___block_literal_global.529
+ ___block_literal_global.535
+ ___block_literal_global.545
+ ___block_literal_global.556
+ ___block_literal_global.594
+ ___block_literal_global.596
+ ___block_literal_global.601
+ ___block_literal_global.604
+ ___block_literal_global.606
+ ___block_literal_global.608
+ ___block_literal_global.610
+ ___block_literal_global.612
+ ___block_literal_global.648
+ ___block_literal_global.658
+ ___block_literal_global.735
+ ___block_literal_global.781
+ ___block_literal_global.788
+ ___block_literal_global.795
+ ___block_literal_global.812
+ ___block_literal_global.816
+ ___block_literal_global.818
+ ___block_literal_global.825
+ ___block_literal_global.925
+ _objc_msgSend$_accessibilityVisiblePointHitTestingAllWindows
+ _objc_msgSend$_accessibilityVisiblePointHitTestingAnyElement:shouldCheckAllWindows:
- GCC_except_table1052
- GCC_except_table1160
- GCC_except_table1207
- GCC_except_table1349
- GCC_except_table353
- GCC_except_table356
- GCC_except_table428
- GCC_except_table429
- GCC_except_table435
- GCC_except_table468
- GCC_except_table479
- GCC_except_table490
- GCC_except_table502
- GCC_except_table601
- GCC_except_table711
- GCC_except_table722
- GCC_except_table747
- GCC_except_table751
- GCC_except_table769
- GCC_except_table808
- GCC_except_table818
- GCC_except_table849
- GCC_except_table881
- ___104+[UIAccessibilityLoader _performInitialAccessibilityBundleLoad:monitorForFutureLoadEvents:trackingMode:]_block_invoke.290
- ___104+[UIAccessibilityLoader _performInitialAccessibilityBundleLoad:monitorForFutureLoadEvents:trackingMode:]_block_invoke.298
- ___104+[UIAccessibilityLoader _performInitialAccessibilityBundleLoad:monitorForFutureLoadEvents:trackingMode:]_block_invoke.303
- ___104+[UIAccessibilityLoader _performInitialAccessibilityBundleLoad:monitorForFutureLoadEvents:trackingMode:]_block_invoke.310
- ___104+[UIAccessibilityLoader _performInitialAccessibilityBundleLoad:monitorForFutureLoadEvents:trackingMode:]_block_invoke_2.304
- ___106-[NSObject(UIAccessibilityElementTraversal) _accessibilityEnumerateSiblingsWithParent:options:usingBlock:]_block_invoke.497
- ___148-[NSObject(UIAccessibilityAutomation) _accessibilityUserTestingSnapshotAncestorsWithAttributes:maxDepth:maxChildren:maxArrayCount:honorsModalViews:]_block_invoke.402
- ___148-[NSObject(UIAccessibilityAutomation) _accessibilityUserTestingSnapshotAncestorsWithAttributes:maxDepth:maxChildren:maxArrayCount:honorsModalViews:]_block_invoke.402.cold.1
- ___149-[NSObject(AXPrivCategory) _accessibilityNextOpaqueElementsForTechnology:startElement:direction:searchType:range:shouldScrollToVisible:honorsGroups:]_block_invoke.1396
- ___150-[NSObject(UIAccessibilityAutomation) _accessibilityUserTestingSnapshotDescendantsWithAttributes:maxDepth:maxChildren:maxArrayCount:honorsModalViews:]_block_invoke.399
- ___150-[NSObject(UIAccessibilityAutomation) _accessibilityUserTestingSnapshotDescendantsWithAttributes:maxDepth:maxChildren:maxArrayCount:honorsModalViews:]_block_invoke.399.cold.1
- ___150-[NSObject(UIAccessibilityAutomation) _accessibilityUserTestingSnapshotDescendantsWithAttributes:maxDepth:maxChildren:maxArrayCount:honorsModalViews:]_block_invoke.399.cold.2
- ___150-[NSObject(UIAccessibilityAutomation) _accessibilityUserTestingSnapshotDescendantsWithAttributes:maxDepth:maxChildren:maxArrayCount:honorsModalViews:]_block_invoke.399.cold.3
- ___174-[NSObject(AXPrivCategory) _accessibilitySearchSubtreesAfterChildElement:direction:searchType:allowOutOfBoundsChild:range:shouldScrollToVisible:honorGroups:updatedContainer:]_block_invoke.1412
- ___174-[NSObject(AXPrivCategory) _accessibilitySearchSubtreesAfterChildElement:direction:searchType:allowOutOfBoundsChild:range:shouldScrollToVisible:honorGroups:updatedContainer:]_block_invoke.1417
- ___60+[UIAccessibilityLegacyLoader _accessibilityLoadSubbundles:]_block_invoke.379
- ___60+[UIAccessibilityLegacyLoader _accessibilityLoadSubbundles:]_block_invoke_2.380
- ___60-[NSObject(AXPrivCategory) _iosAccessibilityAttributeValue:]_block_invoke.1137
- ___60-[NSObject(AXPrivCategory) _iosAccessibilityAttributeValue:]_block_invoke.1137.cold.1
- ___60-[NSObject(AXPrivCategory) _iosAccessibilityAttributeValue:]_block_invoke.1137.cold.2
- ___60-[NSObject(AXPrivCategory) _iosAccessibilityAttributeValue:]_block_invoke.1164
- ___63+[UIAccessibilityLegacyLoader loadExtendedAccessibilityBundles]_block_invoke.318
- ___63+[UIAccessibilityLegacyLoader loadExtendedAccessibilityBundles]_block_invoke.320
- ___79-[NSObject(AXPrivCategory) _accessibilityReplaceCharactersAtCursor:withString:]_block_invoke.1877
- ____copyElementAtPositionCallback_block_invoke.296
- ____copyElementAtPositionCallback_block_invoke.310
- ___block_literal_global.1007
- ___block_literal_global.1009
- ___block_literal_global.1038
- ___block_literal_global.1119
- ___block_literal_global.1139
- ___block_literal_global.1167
- ___block_literal_global.1284
- ___block_literal_global.1336
- ___block_literal_global.1338
- ___block_literal_global.1381
- ___block_literal_global.1383
- ___block_literal_global.1387
- ___block_literal_global.1389
- ___block_literal_global.1393
- ___block_literal_global.1395
- ___block_literal_global.1398
- ___block_literal_global.1404
- ___block_literal_global.1408
- ___block_literal_global.1415
- ___block_literal_global.1436
- ___block_literal_global.1441
- ___block_literal_global.1445
- ___block_literal_global.1449
- ___block_literal_global.1451
- ___block_literal_global.1457
- ___block_literal_global.1544
- ___block_literal_global.1547
- ___block_literal_global.1865
- ___block_literal_global.1867
- ___block_literal_global.1873
- ___block_literal_global.1879
- ___block_literal_global.1945
- ___block_literal_global.1964
- ___block_literal_global.1975
- ___block_literal_global.1985
- ___block_literal_global.1990
- ___block_literal_global.1992
- ___block_literal_global.1996
- ___block_literal_global.291
- ___block_literal_global.292
- ___block_literal_global.293
- ___block_literal_global.295
- ___block_literal_global.296
- ___block_literal_global.298
- ___block_literal_global.301
- ___block_literal_global.303
- ___block_literal_global.306
- ___block_literal_global.3078
- ___block_literal_global.310
- ___block_literal_global.312
- ___block_literal_global.313
- ___block_literal_global.321
- ___block_literal_global.324
- ___block_literal_global.3284
- ___block_literal_global.3286
- ___block_literal_global.3288
- ___block_literal_global.3296
- ___block_literal_global.3304
- ___block_literal_global.3307
- ___block_literal_global.3309
- ___block_literal_global.333
- ___block_literal_global.348
- ___block_literal_global.359
- ___block_literal_global.365
- ___block_literal_global.368
- ___block_literal_global.372
- ___block_literal_global.375
- ___block_literal_global.389
- ___block_literal_global.391
- ___block_literal_global.393
- ___block_literal_global.395
- ___block_literal_global.400
- ___block_literal_global.401
- ___block_literal_global.410
- ___block_literal_global.413
- ___block_literal_global.450
- ___block_literal_global.455
- ___block_literal_global.459
- ___block_literal_global.460
- ___block_literal_global.462
- ___block_literal_global.464
- ___block_literal_global.490
- ___block_literal_global.496
- ___block_literal_global.506
- ___block_literal_global.517
- ___block_literal_global.555
- ___block_literal_global.557
- ___block_literal_global.558
- ___block_literal_global.561
- ___block_literal_global.563
- ___block_literal_global.565
- ___block_literal_global.567
- ___block_literal_global.569
- ___block_literal_global.609
- ___block_literal_global.619
- ___block_literal_global.692
- ___block_literal_global.740
- ___block_literal_global.742
- ___block_literal_global.749
- ___block_literal_global.756
- ___block_literal_global.773
- ___block_literal_global.777
- ___block_literal_global.786
- ___block_literal_global.886
- ___block_literal_global.959
- ___block_literal_global.990
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x6
- _objc_retain_x8
- _objc_retain_x9
CStrings:
+ "/Library/Caches/com.apple.xbs/7C126D7A-075C-4FD4-8FBE-1C3F919E1EFC/TemporaryDirectory.OP8WH1/Sources/AccessibilityFrameworks/Source/UIAccessibility/AXRemoteElement+UIAccessibility.m"
+ "/Library/Caches/com.apple.xbs/7C126D7A-075C-4FD4-8FBE-1C3F919E1EFC/TemporaryDirectory.OP8WH1/Sources/AccessibilityFrameworks/Source/UIAccessibility/NSBundle+UIAccessibilityLoader.m"
+ "/Library/Caches/com.apple.xbs/7C126D7A-075C-4FD4-8FBE-1C3F919E1EFC/TemporaryDirectory.OP8WH1/Sources/AccessibilityFrameworks/Source/UIAccessibility/NSObjectAccessibility.m"
+ "/Library/Caches/com.apple.xbs/7C126D7A-075C-4FD4-8FBE-1C3F919E1EFC/TemporaryDirectory.OP8WH1/Sources/AccessibilityFrameworks/Source/UIAccessibility/UIAccessibilityElementTraversal.m"
+ "/Library/Caches/com.apple.xbs/7C126D7A-075C-4FD4-8FBE-1C3F919E1EFC/TemporaryDirectory.OP8WH1/Sources/AccessibilityFrameworks/Source/UIAccessibility/UIAccessibilityMathExpression.m"
+ "/Library/Caches/com.apple.xbs/7C126D7A-075C-4FD4-8FBE-1C3F919E1EFC/TemporaryDirectory.OP8WH1/Sources/AccessibilityFrameworks/Source/UIAccessibility/UIAccessibilityNotification.m"
+ "/Library/Caches/com.apple.xbs/7C126D7A-075C-4FD4-8FBE-1C3F919E1EFC/TemporaryDirectory.OP8WH1/Sources/AccessibilityFrameworks/Source/UIAccessibility/UIAccessibilityOpaqueElementProvider.m"
+ "/Library/Caches/com.apple.xbs/7C126D7A-075C-4FD4-8FBE-1C3F919E1EFC/TemporaryDirectory.OP8WH1/Sources/AccessibilityFrameworks/Source/UIAccessibility/UIKitAccessibility.m"
+ "AXFallbackFocusRingTintColor"
+ "T{CGRect={CGPoint=dd}{CGSize=dd}},?,R,N"
+ "_accessibilityVisiblePointHitTestingAllWindows"
+ "_accessibilityVisiblePointHitTestingAnyElement:shouldCheckAllWindows:"
+ "unobscuredContentRect"
+ "{CGPoint=dd}24@0:8B16B20"
- "/Library/Caches/com.apple.xbs/Sources/AccessibilityFrameworks/Source/UIAccessibility/AXRemoteElement+UIAccessibility.m"
- "/Library/Caches/com.apple.xbs/Sources/AccessibilityFrameworks/Source/UIAccessibility/NSBundle+UIAccessibilityLoader.m"
- "/Library/Caches/com.apple.xbs/Sources/AccessibilityFrameworks/Source/UIAccessibility/NSObjectAccessibility.m"
- "/Library/Caches/com.apple.xbs/Sources/AccessibilityFrameworks/Source/UIAccessibility/UIAccessibilityElementTraversal.m"
- "/Library/Caches/com.apple.xbs/Sources/AccessibilityFrameworks/Source/UIAccessibility/UIAccessibilityMathExpression.m"
- "/Library/Caches/com.apple.xbs/Sources/AccessibilityFrameworks/Source/UIAccessibility/UIAccessibilityNotification.m"
- "/Library/Caches/com.apple.xbs/Sources/AccessibilityFrameworks/Source/UIAccessibility/UIAccessibilityOpaqueElementProvider.m"
- "/Library/Caches/com.apple.xbs/Sources/AccessibilityFrameworks/Source/UIAccessibility/UIKitAccessibility.m"

```
