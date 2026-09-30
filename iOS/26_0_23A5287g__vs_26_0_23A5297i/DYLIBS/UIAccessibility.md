## UIAccessibility

> `/System/Library/PrivateFrameworks/UIAccessibility.framework/UIAccessibility`

```diff

-3185.4.0.0.0
-  __TEXT.__text: 0x659f0
-  __TEXT.__auth_stubs: 0x1590
-  __TEXT.__objc_methlist: 0x6984
+3187.1.0.0.0
+  __TEXT.__text: 0x65e00
+  __TEXT.__auth_stubs: 0x15a0
+  __TEXT.__objc_methlist: 0x69ec
   __TEXT.__const: 0x2d0
-  __TEXT.__cstring: 0x6ce2
-  __TEXT.__oslogstring: 0x2c06
-  __TEXT.__gcc_except_tab: 0xda8
+  __TEXT.__cstring: 0x6d01
+  __TEXT.__oslogstring: 0x2c1c
+  __TEXT.__gcc_except_tab: 0xdd4
   __TEXT.__dlopen_cstrs: 0x266
   __TEXT.__ustring: 0x14
-  __TEXT.__unwind_info: 0x1bb0
+  __TEXT.__unwind_info: 0x1bc8
   __TEXT.__objc_classname: 0xb74
-  __TEXT.__objc_methname: 0x16c9a
+  __TEXT.__objc_methname: 0x16db4
   __TEXT.__objc_methtype: 0x1f0a
-  __TEXT.__objc_stubs: 0x10760
-  __DATA_CONST.__got: 0xd00
-  __DATA_CONST.__const: 0x1588
+  __TEXT.__objc_stubs: 0x10800
+  __DATA_CONST.__got: 0xd08
+  __DATA_CONST.__const: 0x15d0
   __DATA_CONST.__objc_classlist: 0x1e8
   __DATA_CONST.__objc_catlist: 0xa8
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5508
+  __DATA_CONST.__objc_selrefs: 0x5548
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x110
   __DATA_CONST.__objc_arraydata: 0x128
-  __AUTH_CONST.__auth_got: 0xad8
-  __AUTH_CONST.__const: 0x11e8
+  __AUTH_CONST.__auth_got: 0xae0
+  __AUTH_CONST.__const: 0x1208
   __AUTH_CONST.__cfstring: 0x62a0
-  __AUTH_CONST.__objc_const: 0x4950
+  __AUTH_CONST.__objc_const: 0x4970
   __AUTH_CONST.__objc_intobj: 0x4b0
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x48

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 55B3A00A-3715-3AAD-9AD8-B786AC0F0F99
-  Functions: 2740
-  Symbols:   9577
-  CStrings:  5320
+  UUID: 189482B7-CB1A-380F-90C6-291FCD1BFB32
+  Functions: 2750
+  Symbols:   9607
+  CStrings:  5329
 
Symbols:
+ +[UIAccessibilityElementTraversalOptions voiceOverOptions]
+ -[AXRemoteElement(UIAccessibility) _accessibilityWindowScene]
+ -[NSObject(AXPrivCategory) _accessibilityAdditionalHitTestElements]
+ -[NSObject(AXPrivCategory) _accessibilityFindViewControllerAncestor:]
+ -[NSObject(AXPrivCategory) _accessibilityFindViewControllerAncestorOfType:]
+ -[UIWindowScene(UIAccessibilityElementTraversal) _accessibilityLeadingMultitaskingElements]
+ -[UIWindowScene(UIAccessibilityElementTraversal) _accessibilityTrailingMultitaskingElements]
+ GCC_except_table104
+ GCC_except_table1046
+ GCC_except_table1152
+ GCC_except_table1199
+ GCC_except_table1341
+ GCC_except_table597
+ GCC_except_table62
+ GCC_except_table65
+ GCC_except_table707
+ GCC_except_table718
+ GCC_except_table743
+ GCC_except_table747
+ GCC_except_table764
+ GCC_except_table803
+ GCC_except_table813
+ GCC_except_table844
+ GCC_except_table876
+ _AXRemoteElementFromObject
+ ___104+[UIAccessibilityLoader _performInitialAccessibilityBundleLoad:monitorForFutureLoadEvents:trackingMode:]_block_invoke.278
+ ___104+[UIAccessibilityLoader _performInitialAccessibilityBundleLoad:monitorForFutureLoadEvents:trackingMode:]_block_invoke.286
+ ___104+[UIAccessibilityLoader _performInitialAccessibilityBundleLoad:monitorForFutureLoadEvents:trackingMode:]_block_invoke.291
+ ___104+[UIAccessibilityLoader _performInitialAccessibilityBundleLoad:monitorForFutureLoadEvents:trackingMode:]_block_invoke.298
+ ___104+[UIAccessibilityLoader _performInitialAccessibilityBundleLoad:monitorForFutureLoadEvents:trackingMode:]_block_invoke_2.292
+ ___148-[NSObject(UIAccessibilityAutomation) _accessibilityUserTestingSnapshotAncestorsWithAttributes:maxDepth:maxChildren:maxArrayCount:honorsModalViews:]_block_invoke.390
+ ___148-[NSObject(UIAccessibilityAutomation) _accessibilityUserTestingSnapshotAncestorsWithAttributes:maxDepth:maxChildren:maxArrayCount:honorsModalViews:]_block_invoke.390.cold.1
+ ___149-[NSObject(AXPrivCategory) _accessibilityNextOpaqueElementsForTechnology:startElement:direction:searchType:range:shouldScrollToVisible:honorsGroups:]_block_invoke.1381
+ ___150-[NSObject(UIAccessibilityAutomation) _accessibilityUserTestingSnapshotDescendantsWithAttributes:maxDepth:maxChildren:maxArrayCount:honorsModalViews:]_block_invoke.387
+ ___150-[NSObject(UIAccessibilityAutomation) _accessibilityUserTestingSnapshotDescendantsWithAttributes:maxDepth:maxChildren:maxArrayCount:honorsModalViews:]_block_invoke.387.cold.1
+ ___150-[NSObject(UIAccessibilityAutomation) _accessibilityUserTestingSnapshotDescendantsWithAttributes:maxDepth:maxChildren:maxArrayCount:honorsModalViews:]_block_invoke.387.cold.2
+ ___150-[NSObject(UIAccessibilityAutomation) _accessibilityUserTestingSnapshotDescendantsWithAttributes:maxDepth:maxChildren:maxArrayCount:honorsModalViews:]_block_invoke.387.cold.3
+ ___174-[NSObject(AXPrivCategory) _accessibilitySearchSubtreesAfterChildElement:direction:searchType:allowOutOfBoundsChild:range:shouldScrollToVisible:honorGroups:updatedContainer:]_block_invoke.1397
+ ___174-[NSObject(AXPrivCategory) _accessibilitySearchSubtreesAfterChildElement:direction:searchType:allowOutOfBoundsChild:range:shouldScrollToVisible:honorGroups:updatedContainer:]_block_invoke.1402
+ ___60+[UIAccessibilityLegacyLoader _accessibilityLoadSubbundles:]_block_invoke.367
+ ___60+[UIAccessibilityLegacyLoader _accessibilityLoadSubbundles:]_block_invoke_2.368
+ ___60-[NSObject(AXPrivCategory) _iosAccessibilityAttributeValue:]_block_invoke.1122
+ ___60-[NSObject(AXPrivCategory) _iosAccessibilityAttributeValue:]_block_invoke.1122.cold.1
+ ___60-[NSObject(AXPrivCategory) _iosAccessibilityAttributeValue:]_block_invoke.1122.cold.2
+ ___60-[NSObject(AXPrivCategory) _iosAccessibilityAttributeValue:]_block_invoke.1149
+ ___61-[AXRemoteElement(UIAccessibility) _accessibilityWindowScene]_block_invoke
+ ___63+[UIAccessibilityLegacyLoader loadExtendedAccessibilityBundles]_block_invoke.306
+ ___63+[UIAccessibilityLegacyLoader loadExtendedAccessibilityBundles]_block_invoke.308
+ ___69-[NSObject(AXPrivCategory) _accessibilityFindViewControllerAncestor:]_block_invoke
+ ___75-[NSObject(AXPrivCategory) _accessibilityFindViewControllerAncestorOfType:]_block_invoke
+ ___79-[NSObject(AXPrivCategory) _accessibilityReplaceCharactersAtCursor:withString:]_block_invoke.1862
+ ____copyElementAtPositionCallback_block_invoke.284
+ ____copyElementAtPositionCallback_block_invoke.298
+ ___block_descriptor_40_e30_B24?0"UIViewController"8^B16lu32l8
+ ___block_descriptor_56_e8_32bs40r48r_e8_B16?08ls32l8r40l8r48l8
+ ___block_literal_global.1023
+ ___block_literal_global.1104
+ ___block_literal_global.1124
+ ___block_literal_global.1152
+ ___block_literal_global.1267
+ ___block_literal_global.1321
+ ___block_literal_global.1323
+ ___block_literal_global.1362
+ ___block_literal_global.1368
+ ___block_literal_global.1374
+ ___block_literal_global.1380
+ ___block_literal_global.1383
+ ___block_literal_global.1389
+ ___block_literal_global.1400
+ ___block_literal_global.1405
+ ___block_literal_global.1421
+ ___block_literal_global.1426
+ ___block_literal_global.1428
+ ___block_literal_global.1442
+ ___block_literal_global.1529
+ ___block_literal_global.1532
+ ___block_literal_global.1850
+ ___block_literal_global.1852
+ ___block_literal_global.1858
+ ___block_literal_global.1864
+ ___block_literal_global.1927
+ ___block_literal_global.1946
+ ___block_literal_global.1957
+ ___block_literal_global.1967
+ ___block_literal_global.1969
+ ___block_literal_global.1972
+ ___block_literal_global.1974
+ ___block_literal_global.1978
+ ___block_literal_global.279
+ ___block_literal_global.280
+ ___block_literal_global.281
+ ___block_literal_global.283
+ ___block_literal_global.291
+ ___block_literal_global.298
+ ___block_literal_global.300
+ ___block_literal_global.301
+ ___block_literal_global.3051
+ ___block_literal_global.309
+ ___block_literal_global.321
+ ___block_literal_global.3257
+ ___block_literal_global.3259
+ ___block_literal_global.3261
+ ___block_literal_global.3269
+ ___block_literal_global.3280
+ ___block_literal_global.3282
+ ___block_literal_global.336
+ ___block_literal_global.347
+ ___block_literal_global.351
+ ___block_literal_global.353
+ ___block_literal_global.360
+ ___block_literal_global.374
+ ___block_literal_global.379
+ ___block_literal_global.381
+ ___block_literal_global.383
+ ___block_literal_global.388
+ ___block_literal_global.389
+ ___block_literal_global.390
+ ___block_literal_global.395
+ ___block_literal_global.401
+ ___block_literal_global.416
+ ___block_literal_global.435
+ ___block_literal_global.440
+ ___block_literal_global.445
+ ___block_literal_global.447
+ ___block_literal_global.452
+ ___block_literal_global.478
+ ___block_literal_global.484
+ ___block_literal_global.492
+ ___block_literal_global.503
+ ___block_literal_global.540
+ ___block_literal_global.554
+ ___block_literal_global.597
+ ___block_literal_global.607
+ ___block_literal_global.725
+ ___block_literal_global.727
+ ___block_literal_global.734
+ ___block_literal_global.741
+ ___block_literal_global.758
+ ___block_literal_global.764
+ ___block_literal_global.771
+ ___block_literal_global.871
+ ___block_literal_global.944
+ ___block_literal_global.975
+ ___block_literal_global.983
+ ___block_literal_global.992
+ ___block_literal_global.994
+ _objc_msgSend$_accessibilityAdditionalHitTestElements
+ _objc_msgSend$_accessibilityFindViewControllerAncestor:
+ _objc_msgSend$_accessibilityLeadingMultitaskingElements
+ _objc_msgSend$_accessibilityTrailingMultitaskingElements
+ _objc_msgSend$voiceOverOptions
- GCC_except_table101
- GCC_except_table1041
- GCC_except_table1147
- GCC_except_table1194
- GCC_except_table1336
- GCC_except_table47
- GCC_except_table596
- GCC_except_table61
- GCC_except_table64
- GCC_except_table706
- GCC_except_table717
- GCC_except_table742
- GCC_except_table746
- GCC_except_table798
- GCC_except_table808
- GCC_except_table839
- GCC_except_table871
- ___104+[UIAccessibilityLoader _performInitialAccessibilityBundleLoad:monitorForFutureLoadEvents:trackingMode:]_block_invoke.281
- ___104+[UIAccessibilityLoader _performInitialAccessibilityBundleLoad:monitorForFutureLoadEvents:trackingMode:]_block_invoke.289
- ___104+[UIAccessibilityLoader _performInitialAccessibilityBundleLoad:monitorForFutureLoadEvents:trackingMode:]_block_invoke.294
- ___104+[UIAccessibilityLoader _performInitialAccessibilityBundleLoad:monitorForFutureLoadEvents:trackingMode:]_block_invoke.301
- ___104+[UIAccessibilityLoader _performInitialAccessibilityBundleLoad:monitorForFutureLoadEvents:trackingMode:]_block_invoke_2.295
- ___148-[NSObject(UIAccessibilityAutomation) _accessibilityUserTestingSnapshotAncestorsWithAttributes:maxDepth:maxChildren:maxArrayCount:honorsModalViews:]_block_invoke.393
- ___148-[NSObject(UIAccessibilityAutomation) _accessibilityUserTestingSnapshotAncestorsWithAttributes:maxDepth:maxChildren:maxArrayCount:honorsModalViews:]_block_invoke.393.cold.1
- ___149-[NSObject(AXPrivCategory) _accessibilityNextOpaqueElementsForTechnology:startElement:direction:searchType:range:shouldScrollToVisible:honorsGroups:]_block_invoke.1385
- ___150-[NSObject(UIAccessibilityAutomation) _accessibilityUserTestingSnapshotDescendantsWithAttributes:maxDepth:maxChildren:maxArrayCount:honorsModalViews:]_block_invoke.390
- ___150-[NSObject(UIAccessibilityAutomation) _accessibilityUserTestingSnapshotDescendantsWithAttributes:maxDepth:maxChildren:maxArrayCount:honorsModalViews:]_block_invoke.390.cold.1
- ___150-[NSObject(UIAccessibilityAutomation) _accessibilityUserTestingSnapshotDescendantsWithAttributes:maxDepth:maxChildren:maxArrayCount:honorsModalViews:]_block_invoke.390.cold.2
- ___150-[NSObject(UIAccessibilityAutomation) _accessibilityUserTestingSnapshotDescendantsWithAttributes:maxDepth:maxChildren:maxArrayCount:honorsModalViews:]_block_invoke.390.cold.3
- ___174-[NSObject(AXPrivCategory) _accessibilitySearchSubtreesAfterChildElement:direction:searchType:allowOutOfBoundsChild:range:shouldScrollToVisible:honorGroups:updatedContainer:]_block_invoke.1401
- ___174-[NSObject(AXPrivCategory) _accessibilitySearchSubtreesAfterChildElement:direction:searchType:allowOutOfBoundsChild:range:shouldScrollToVisible:honorGroups:updatedContainer:]_block_invoke.1406
- ___60+[UIAccessibilityLegacyLoader _accessibilityLoadSubbundles:]_block_invoke.370
- ___60+[UIAccessibilityLegacyLoader _accessibilityLoadSubbundles:]_block_invoke_2.371
- ___60-[NSObject(AXPrivCategory) _iosAccessibilityAttributeValue:]_block_invoke.1126
- ___60-[NSObject(AXPrivCategory) _iosAccessibilityAttributeValue:]_block_invoke.1126.cold.1
- ___60-[NSObject(AXPrivCategory) _iosAccessibilityAttributeValue:]_block_invoke.1126.cold.2
- ___60-[NSObject(AXPrivCategory) _iosAccessibilityAttributeValue:]_block_invoke.1153
- ___63+[UIAccessibilityLegacyLoader loadExtendedAccessibilityBundles]_block_invoke.309
- ___63+[UIAccessibilityLegacyLoader loadExtendedAccessibilityBundles]_block_invoke.311
- ___79-[NSObject(AXPrivCategory) _accessibilityReplaceCharactersAtCursor:withString:]_block_invoke.1861
- ____copyElementAtPositionCallback_block_invoke.287
- ____copyElementAtPositionCallback_block_invoke.301
- ___block_literal_global.1027
- ___block_literal_global.1108
- ___block_literal_global.1128
- ___block_literal_global.1156
- ___block_literal_global.1271
- ___block_literal_global.1325
- ___block_literal_global.1327
- ___block_literal_global.1370
- ___block_literal_global.1376
- ___block_literal_global.1382
- ___block_literal_global.1384
- ___block_literal_global.1387
- ___block_literal_global.1397
- ___block_literal_global.1404
- ___block_literal_global.1409
- ___block_literal_global.1425
- ___block_literal_global.1432
- ___block_literal_global.1438
- ___block_literal_global.1444
- ___block_literal_global.1531
- ___block_literal_global.1534
- ___block_literal_global.1849
- ___block_literal_global.1851
- ___block_literal_global.1857
- ___block_literal_global.1863
- ___block_literal_global.1926
- ___block_literal_global.1945
- ___block_literal_global.1956
- ___block_literal_global.1966
- ___block_literal_global.1968
- ___block_literal_global.1971
- ___block_literal_global.1973
- ___block_literal_global.1977
- ___block_literal_global.282
- ___block_literal_global.287
- ___block_literal_global.292
- ___block_literal_global.296
- ___block_literal_global.297
- ___block_literal_global.303
- ___block_literal_global.304
- ___block_literal_global.3047
- ___block_literal_global.315
- ___block_literal_global.324
- ___block_literal_global.3252
- ___block_literal_global.3254
- ___block_literal_global.3256
- ___block_literal_global.3264
- ___block_literal_global.3272
- ___block_literal_global.3275
- ___block_literal_global.339
- ___block_literal_global.350
- ___block_literal_global.354
- ___block_literal_global.359
- ___block_literal_global.366
- ___block_literal_global.378
- ___block_literal_global.382
- ___block_literal_global.384
- ___block_literal_global.386
- ___block_literal_global.391
- ___block_literal_global.392
- ___block_literal_global.393
- ___block_literal_global.403
- ___block_literal_global.404
- ___block_literal_global.419
- ___block_literal_global.439
- ___block_literal_global.444
- ___block_literal_global.449
- ___block_literal_global.453
- ___block_literal_global.455
- ___block_literal_global.481
- ___block_literal_global.487
- ___block_literal_global.494
- ___block_literal_global.505
- ___block_literal_global.544
- ___block_literal_global.556
- ___block_literal_global.600
- ___block_literal_global.610
- ___block_literal_global.729
- ___block_literal_global.731
- ___block_literal_global.738
- ___block_literal_global.745
- ___block_literal_global.766
- ___block_literal_global.768
- ___block_literal_global.775
- ___block_literal_global.875
- ___block_literal_global.948
- ___block_literal_global.979
- ___block_literal_global.987
- ___block_literal_global.996
- ___block_literal_global.998
CStrings:
+ "B24@?0@\"UIViewController\"8^B16"
+ "Is descendant of desired element: %{sensitive}@"
+ "Trying pt[%{sensitive}@]: %@ (original: %@)"
+ "_accessibilityAdditionalHitTestElements"
+ "_accessibilityFindViewControllerAncestor:"
+ "_accessibilityFindViewControllerAncestorOfType:"
+ "_accessibilityLeadingMultitaskingElements"
+ "_accessibilityTrailingMultitaskingElements"
+ "allowsNumberPadPopover"
+ "setAllowsNumberPadPopover:"
+ "voiceOverOptions"
- "Is descendant of desired element: %@"
- "Trying pt[%@]: %@ (original: %@)"

```
