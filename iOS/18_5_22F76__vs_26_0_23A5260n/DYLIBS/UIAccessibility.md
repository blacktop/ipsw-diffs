## UIAccessibility

> `/System/Library/PrivateFrameworks/UIAccessibility.framework/UIAccessibility`

```diff

-3148.15.26.0.0
-  __TEXT.__text: 0x654e8
+3180.6.1.0.0
+  __TEXT.__text: 0x65914
   __TEXT.__auth_stubs: 0x1560
-  __TEXT.__objc_methlist: 0x690c
+  __TEXT.__objc_methlist: 0x6964
   __TEXT.__const: 0x2d0
-  __TEXT.__cstring: 0x6caf
-  __TEXT.__oslogstring: 0x2bc0
+  __TEXT.__cstring: 0x6cd5
+  __TEXT.__oslogstring: 0x2c06
   __TEXT.__gcc_except_tab: 0xda8
   __TEXT.__dlopen_cstrs: 0x266
   __TEXT.__ustring: 0x14
-  __TEXT.__unwind_info: 0x1b80
+  __TEXT.__unwind_info: 0x1b70
   __TEXT.__objc_classname: 0xb74
-  __TEXT.__objc_methname: 0x16b8e
+  __TEXT.__objc_methname: 0x16c6f
   __TEXT.__objc_methtype: 0x1f07
-  __TEXT.__objc_stubs: 0x10660
+  __TEXT.__objc_stubs: 0x10740
   __DATA_CONST.__got: 0xd00
   __DATA_CONST.__const: 0x1588
   __DATA_CONST.__objc_classlist: 0x1e8
   __DATA_CONST.__objc_catlist: 0xa0
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x54c8
+  __DATA_CONST.__objc_selrefs: 0x54f8
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x110
   __DATA_CONST.__objc_arraydata: 0x128
   __AUTH_CONST.__auth_got: 0xac0
-  __AUTH_CONST.__const: 0x11a8
-  __AUTH_CONST.__cfstring: 0x6280
-  __AUTH_CONST.__objc_const: 0x48d0
-  __AUTH_CONST.__objc_intobj: 0x498
+  __AUTH_CONST.__const: 0x11e8
+  __AUTH_CONST.__cfstring: 0x62a0
+  __AUTH_CONST.__objc_const: 0x48f8
+  __AUTH_CONST.__objc_intobj: 0x4b0
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH.__objc_data: 0xe60
   __DATA.__objc_ivar: 0x178
   __DATA.__data: 0x748
-  __DATA.__bss: 0x4d8
+  __DATA.__bss: 0x4c0
   __DATA.__common: 0x11
   __DATA_DIRTY.__objc_data: 0x4b0
-  __DATA_DIRTY.__bss: 0x208
-  __DATA_DIRTY.__common: 0x234
+  __DATA_DIRTY.__bss: 0x220
+  __DATA_DIRTY.__common: 0x238
   - /System/Library/Frameworks/Accessibility.framework/Accessibility
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/BrowserEngineKit.framework/BrowserEngineKit

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3ECF4B1D-3D4B-34C0-A53B-75BC4C27A2A0
-  Functions: 2728
-  Symbols:   9533
-  CStrings:  5308
+  UUID: 687D2078-2687-3355-BAE5-71E3EF3D14CE
+  Functions: 2738
+  Symbols:   9563
+  CStrings:  5317
 
Symbols:
+ -[NSObject(AXPrivCategory) _accessibilityElementTextualContent]
+ -[NSObject(AXPrivCategory) _accessibilityKeyboardKeyCanStartContinuousPath]
+ -[NSObject(AXPrivCategory) _accessibilityMapSmartDescriptionDictionary]
+ -[NSObject(AXPrivCategory) _accessibilityScreenTextualContent]
+ -[NSObject(AXPrivCategory) _accessibilityTraversalWindows]
+ -[NSObject(UIStorage) _focusRingManagerShouldDrawFocusRingWhenChildrenFocused]
+ -[NSObject(UIStorage) _iosAccessibilityPerformAction:withValue:fencePort:].cold.6
+ -[NSObjectAccessibility _accessibilitySetTextInsertionGlowModeEnabled:]
+ GCC_except_table1041
+ GCC_except_table1147
+ GCC_except_table1194
+ GCC_except_table120
+ GCC_except_table124
+ GCC_except_table128
+ GCC_except_table130
+ GCC_except_table1336
+ GCC_except_table142
+ GCC_except_table170
+ GCC_except_table219
+ GCC_except_table222
+ GCC_except_table234
+ GCC_except_table273
+ GCC_except_table293
+ GCC_except_table349
+ GCC_except_table352
+ GCC_except_table424
+ GCC_except_table431
+ GCC_except_table596
+ GCC_except_table706
+ GCC_except_table717
+ GCC_except_table746
+ GCC_except_table78
+ GCC_except_table798
+ GCC_except_table808
+ GCC_except_table82
+ GCC_except_table839
+ GCC_except_table85
+ GCC_except_table871
+ GCC_except_table92
+ GCC_except_table94
+ GCC_except_table98
+ _OUTLINED_FUNCTION_25
+ _OUTLINED_FUNCTION_26
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_GCControllerProductInfo
+ ___104+[UIAccessibilityLoader _performInitialAccessibilityBundleLoad:monitorForFutureLoadEvents:trackingMode:]_block_invoke.278
+ ___104+[UIAccessibilityLoader _performInitialAccessibilityBundleLoad:monitorForFutureLoadEvents:trackingMode:]_block_invoke.286
+ ___104+[UIAccessibilityLoader _performInitialAccessibilityBundleLoad:monitorForFutureLoadEvents:trackingMode:]_block_invoke.291
+ ___104+[UIAccessibilityLoader _performInitialAccessibilityBundleLoad:monitorForFutureLoadEvents:trackingMode:]_block_invoke.298
+ ___104+[UIAccessibilityLoader _performInitialAccessibilityBundleLoad:monitorForFutureLoadEvents:trackingMode:]_block_invoke_2.292
+ ___148-[NSObject(UIAccessibilityAutomation) _accessibilityUserTestingSnapshotAncestorsWithAttributes:maxDepth:maxChildren:maxArrayCount:honorsModalViews:]_block_invoke.390
+ ___148-[NSObject(UIAccessibilityAutomation) _accessibilityUserTestingSnapshotAncestorsWithAttributes:maxDepth:maxChildren:maxArrayCount:honorsModalViews:]_block_invoke.390.cold.1
+ ___149-[NSObject(AXPrivCategory) _accessibilityNextOpaqueElementsForTechnology:startElement:direction:searchType:range:shouldScrollToVisible:honorsGroups:]_block_invoke.1382
+ ___150-[NSObject(UIAccessibilityAutomation) _accessibilityUserTestingSnapshotDescendantsWithAttributes:maxDepth:maxChildren:maxArrayCount:honorsModalViews:]_block_invoke.387
+ ___150-[NSObject(UIAccessibilityAutomation) _accessibilityUserTestingSnapshotDescendantsWithAttributes:maxDepth:maxChildren:maxArrayCount:honorsModalViews:]_block_invoke.387.cold.1
+ ___150-[NSObject(UIAccessibilityAutomation) _accessibilityUserTestingSnapshotDescendantsWithAttributes:maxDepth:maxChildren:maxArrayCount:honorsModalViews:]_block_invoke.387.cold.2
+ ___150-[NSObject(UIAccessibilityAutomation) _accessibilityUserTestingSnapshotDescendantsWithAttributes:maxDepth:maxChildren:maxArrayCount:honorsModalViews:]_block_invoke.387.cold.3
+ ___174-[NSObject(AXPrivCategory) _accessibilitySearchSubtreesAfterChildElement:direction:searchType:allowOutOfBoundsChild:range:shouldScrollToVisible:honorGroups:updatedContainer:]_block_invoke.1398
+ ___174-[NSObject(AXPrivCategory) _accessibilitySearchSubtreesAfterChildElement:direction:searchType:allowOutOfBoundsChild:range:shouldScrollToVisible:honorGroups:updatedContainer:]_block_invoke.1403
+ ___60+[UIAccessibilityLegacyLoader _accessibilityLoadSubbundles:]_block_invoke.367
+ ___60+[UIAccessibilityLegacyLoader _accessibilityLoadSubbundles:]_block_invoke_2.368
+ ___60-[NSObject(AXPrivCategory) _iosAccessibilityAttributeValue:]_block_invoke.1150
+ ___63+[UIAccessibilityLegacyLoader loadExtendedAccessibilityBundles]_block_invoke.306
+ ___63+[UIAccessibilityLegacyLoader loadExtendedAccessibilityBundles]_block_invoke.308
+ ___63-[NSObject(AXPrivCategory) _accessibilityElementTextualContent]_block_invoke
+ ___78-[NSObject(UIStorage) _focusRingManagerShouldDrawFocusRingWhenChildrenFocused]_block_invoke
+ ___79-[NSObject(AXPrivCategory) _accessibilityReplaceCharactersAtCursor:withString:]_block_invoke.1858
+ ____copyElementAtPositionCallback_block_invoke.284
+ ____copyElementAtPositionCallback_block_invoke.298
+ ___block_literal_global.1153
+ ___block_literal_global.1268
+ ___block_literal_global.1322
+ ___block_literal_global.1324
+ ___block_literal_global.1363
+ ___block_literal_global.1369
+ ___block_literal_global.1373
+ ___block_literal_global.1375
+ ___block_literal_global.1379
+ ___block_literal_global.1381
+ ___block_literal_global.1384
+ ___block_literal_global.1390
+ ___block_literal_global.1394
+ ___block_literal_global.1401
+ ___block_literal_global.1406
+ ___block_literal_global.1422
+ ___block_literal_global.1429
+ ___block_literal_global.1431
+ ___block_literal_global.1433
+ ___block_literal_global.1435
+ ___block_literal_global.1441
+ ___block_literal_global.1528
+ ___block_literal_global.1531
+ ___block_literal_global.1848
+ ___block_literal_global.1854
+ ___block_literal_global.1860
+ ___block_literal_global.1923
+ ___block_literal_global.1953
+ ___block_literal_global.1965
+ ___block_literal_global.1968
+ ___block_literal_global.1970
+ ___block_literal_global.1974
+ ___block_literal_global.279
+ ___block_literal_global.284
+ ___block_literal_global.289
+ ___block_literal_global.293
+ ___block_literal_global.294
+ ___block_literal_global.300
+ ___block_literal_global.301
+ ___block_literal_global.3044
+ ___block_literal_global.312
+ ___block_literal_global.321
+ ___block_literal_global.3249
+ ___block_literal_global.3251
+ ___block_literal_global.3261
+ ___block_literal_global.3269
+ ___block_literal_global.3272
+ ___block_literal_global.3274
+ ___block_literal_global.336
+ ___block_literal_global.347
+ ___block_literal_global.351
+ ___block_literal_global.356
+ ___block_literal_global.363
+ ___block_literal_global.375
+ ___block_literal_global.379
+ ___block_literal_global.381
+ ___block_literal_global.383
+ ___block_literal_global.388
+ ___block_literal_global.389
+ ___block_literal_global.390
+ ___block_literal_global.396
+ ___block_literal_global.400
+ ___block_literal_global.401
+ ___block_literal_global.415
+ ___block_literal_global.436
+ ___block_literal_global.441
+ ___block_literal_global.446
+ ___block_literal_global.450
+ ___block_literal_global.452
+ ___block_literal_global.477
+ ___block_literal_global.483
+ ___block_literal_global.491
+ ___block_literal_global.502
+ ___block_literal_global.539
+ ___block_literal_global.541
+ ___block_literal_global.546
+ ___block_literal_global.548
+ ___block_literal_global.552
+ ___block_literal_global.553
+ ___block_literal_global.554
+ ___block_literal_global.597
+ ___block_literal_global.607
+ ___block_literal_global.677
+ _objc_msgSend$_accessibilityElementTextualContent
+ _objc_msgSend$_accessibilityKeyboardKeyCanStartContinuousPath
+ _objc_msgSend$_accessibilityMapSmartDescriptionDictionary
+ _objc_msgSend$_accessibilityScreenTextualContent
+ _objc_msgSend$_accessibilitySetTextInsertionGlowModeEnabled:
+ _objc_msgSend$_accessibilityTraversalWindows
+ _objc_msgSend$browserAccessibilityContainerType
- -[NSObject(AXPrivCategory) _accessibilityShouldIncludeKeyboardInRemoteSubstituteChildren]
- -[NSObject(UIStorage) _drawsFocusRingWhenChildrenFocused]
- GCC_except_table1037
- GCC_except_table1142
- GCC_except_table1188
- GCC_except_table121
- GCC_except_table125
- GCC_except_table129
- GCC_except_table131
- GCC_except_table1329
- GCC_except_table143
- GCC_except_table171
- GCC_except_table220
- GCC_except_table223
- GCC_except_table235
- GCC_except_table274
- GCC_except_table294
- GCC_except_table350
- GCC_except_table353
- GCC_except_table427
- GCC_except_table432
- GCC_except_table592
- GCC_except_table702
- GCC_except_table713
- GCC_except_table738
- GCC_except_table79
- GCC_except_table794
- GCC_except_table804
- GCC_except_table83
- GCC_except_table835
- GCC_except_table86
- GCC_except_table867
- GCC_except_table93
- GCC_except_table95
- GCC_except_table99
- ___104+[UIAccessibilityLoader _performInitialAccessibilityBundleLoad:monitorForFutureLoadEvents:trackingMode:]_block_invoke.275
- ___104+[UIAccessibilityLoader _performInitialAccessibilityBundleLoad:monitorForFutureLoadEvents:trackingMode:]_block_invoke.283
- ___104+[UIAccessibilityLoader _performInitialAccessibilityBundleLoad:monitorForFutureLoadEvents:trackingMode:]_block_invoke.288
- ___104+[UIAccessibilityLoader _performInitialAccessibilityBundleLoad:monitorForFutureLoadEvents:trackingMode:]_block_invoke.295
- ___104+[UIAccessibilityLoader _performInitialAccessibilityBundleLoad:monitorForFutureLoadEvents:trackingMode:]_block_invoke_2.289
- ___148-[NSObject(UIAccessibilityAutomation) _accessibilityUserTestingSnapshotAncestorsWithAttributes:maxDepth:maxChildren:maxArrayCount:honorsModalViews:]_block_invoke.387
- ___148-[NSObject(UIAccessibilityAutomation) _accessibilityUserTestingSnapshotAncestorsWithAttributes:maxDepth:maxChildren:maxArrayCount:honorsModalViews:]_block_invoke.387.cold.1
- ___149-[NSObject(AXPrivCategory) _accessibilityNextOpaqueElementsForTechnology:startElement:direction:searchType:range:shouldScrollToVisible:honorsGroups:]_block_invoke.1368
- ___150-[NSObject(UIAccessibilityAutomation) _accessibilityUserTestingSnapshotDescendantsWithAttributes:maxDepth:maxChildren:maxArrayCount:honorsModalViews:]_block_invoke.384
- ___150-[NSObject(UIAccessibilityAutomation) _accessibilityUserTestingSnapshotDescendantsWithAttributes:maxDepth:maxChildren:maxArrayCount:honorsModalViews:]_block_invoke.384.cold.1
- ___150-[NSObject(UIAccessibilityAutomation) _accessibilityUserTestingSnapshotDescendantsWithAttributes:maxDepth:maxChildren:maxArrayCount:honorsModalViews:]_block_invoke.384.cold.2
- ___150-[NSObject(UIAccessibilityAutomation) _accessibilityUserTestingSnapshotDescendantsWithAttributes:maxDepth:maxChildren:maxArrayCount:honorsModalViews:]_block_invoke.384.cold.3
- ___174-[NSObject(AXPrivCategory) _accessibilitySearchSubtreesAfterChildElement:direction:searchType:allowOutOfBoundsChild:range:shouldScrollToVisible:honorGroups:updatedContainer:]_block_invoke.1384
- ___174-[NSObject(AXPrivCategory) _accessibilitySearchSubtreesAfterChildElement:direction:searchType:allowOutOfBoundsChild:range:shouldScrollToVisible:honorGroups:updatedContainer:]_block_invoke.1389
- ___57-[NSObject(UIStorage) _drawsFocusRingWhenChildrenFocused]_block_invoke
- ___60+[UIAccessibilityLegacyLoader _accessibilityLoadSubbundles:]_block_invoke.364
- ___60+[UIAccessibilityLegacyLoader _accessibilityLoadSubbundles:]_block_invoke_2.365
- ___63+[UIAccessibilityLegacyLoader loadExtendedAccessibilityBundles]_block_invoke.303
- ___63+[UIAccessibilityLegacyLoader loadExtendedAccessibilityBundles]_block_invoke.305
- ___79-[NSObject(AXPrivCategory) _accessibilityReplaceCharactersAtCursor:withString:]_block_invoke.1844
- ____copyElementAtPositionCallback_block_invoke.281
- ____copyElementAtPositionCallback_block_invoke.295
- ___block_literal_global.1308
- ___block_literal_global.1310
- ___block_literal_global.1349
- ___block_literal_global.1353
- ___block_literal_global.1355
- ___block_literal_global.1359
- ___block_literal_global.1361
- ___block_literal_global.1365
- ___block_literal_global.1370
- ___block_literal_global.1376
- ___block_literal_global.1380
- ___block_literal_global.1387
- ___block_literal_global.1392
- ___block_literal_global.1408
- ___block_literal_global.1413
- ___block_literal_global.1415
- ___block_literal_global.1417
- ___block_literal_global.1419
- ___block_literal_global.1421
- ___block_literal_global.1514
- ___block_literal_global.1517
- ___block_literal_global.1832
- ___block_literal_global.1834
- ___block_literal_global.1840
- ___block_literal_global.1912
- ___block_literal_global.1931
- ___block_literal_global.1952
- ___block_literal_global.1954
- ___block_literal_global.1957
- ___block_literal_global.1959
- ___block_literal_global.276
- ___block_literal_global.278
- ___block_literal_global.280
- ___block_literal_global.288
- ___block_literal_global.290
- ___block_literal_global.297
- ___block_literal_global.298
- ___block_literal_global.3029
- ___block_literal_global.306
- ___block_literal_global.318
- ___block_literal_global.3230
- ___block_literal_global.3232
- ___block_literal_global.3234
- ___block_literal_global.3242
- ___block_literal_global.3250
- ___block_literal_global.3255
- ___block_literal_global.333
- ___block_literal_global.344
- ___block_literal_global.348
- ___block_literal_global.350
- ___block_literal_global.357
- ___block_literal_global.372
- ___block_literal_global.376
- ___block_literal_global.378
- ___block_literal_global.380
- ___block_literal_global.385
- ___block_literal_global.386
- ___block_literal_global.387
- ___block_literal_global.393
- ___block_literal_global.397
- ___block_literal_global.398
- ___block_literal_global.412
- ___block_literal_global.433
- ___block_literal_global.438
- ___block_literal_global.443
- ___block_literal_global.444
- ___block_literal_global.449
- ___block_literal_global.474
- ___block_literal_global.480
- ___block_literal_global.488
- ___block_literal_global.499
- ___block_literal_global.536
- ___block_literal_global.538
- ___block_literal_global.540
- ___block_literal_global.545
- ___block_literal_global.547
- ___block_literal_global.549
- ___block_literal_global.551
- ___block_literal_global.594
- ___block_literal_global.604
- ___block_literal_global.674
CStrings:
+ "UIDictationWillInsertHypothesisNotification"
+ "Unexpected parameter for kAXSetTextInsertionGlowModeEnabledAction: %@"
+ "_accessibilityElementTextualContent"
+ "_accessibilityKeyboardKeyCanStartContinuousPath"
+ "_accessibilityMapSmartDescriptionDictionary"
+ "_accessibilityScreenTextualContent"
+ "_accessibilitySetTextInsertionGlowModeEnabled:"
+ "_accessibilityTableAncestor"
+ "_focusRingManagerShouldDrawFocusRingWhenChildrenFocused"
+ "uniformTypeIdentifier"
- "_accessibilityShouldIncludeKeyboardInRemoteSubstituteChildren"
- "_drawsFocusRingWhenChildrenFocused"

```
