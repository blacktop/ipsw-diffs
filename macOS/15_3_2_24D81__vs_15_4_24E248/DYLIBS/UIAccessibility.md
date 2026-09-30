## UIAccessibility

> `/System/iOSSupport/System/Library/PrivateFrameworks/UIAccessibility.framework/Versions/A/UIAccessibility`

```diff

-3148.7.15.0.0
-  __TEXT.__text: 0x60fa4
-  __TEXT.__auth_stubs: 0x1520
-  __TEXT.__objc_methlist: 0x5d1c
+3148.15.11.1.0
+  __TEXT.__text: 0x614cc
+  __TEXT.__auth_stubs: 0x1510
+  __TEXT.__objc_methlist: 0x64ec
   __TEXT.__const: 0x2c0
-  __TEXT.__cstring: 0x671d
+  __TEXT.__cstring: 0x6762
   __TEXT.__oslogstring: 0x2adc
-  __TEXT.__gcc_except_tab: 0xbf4
+  __TEXT.__gcc_except_tab: 0xc04
   __TEXT.__dlopen_cstrs: 0x162
   __TEXT.__ustring: 0x14
-  __TEXT.__unwind_info: 0x19c0
+  __TEXT.__unwind_info: 0x1a38
   __TEXT.__objc_classname: 0xa19
-  __TEXT.__objc_methname: 0x15bcd
-  __TEXT.__objc_methtype: 0x1a80
-  __TEXT.__objc_stubs: 0xfaa0
-  __DATA_CONST.__got: 0xca0
+  __TEXT.__objc_methname: 0x15c77
+  __TEXT.__objc_methtype: 0x1adf
+  __TEXT.__objc_stubs: 0xfb00
+  __DATA_CONST.__got: 0xca8
   __DATA_CONST.__const: 0x1450
   __DATA_CONST.__objc_classlist: 0x1b8
   __DATA_CONST.__objc_catlist: 0xa0
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4d70
+  __DATA_CONST.__objc_selrefs: 0x5100
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0xe8
   __DATA_CONST.__objc_arraydata: 0x128
-  __AUTH_CONST.__auth_got: 0xaa0
+  __AUTH_CONST.__auth_got: 0xa98
   __AUTH_CONST.__const: 0x1168
-  __AUTH_CONST.__cfstring: 0x5ec0
-  __AUTH_CONST.__objc_const: 0x4e50
-  __AUTH_CONST.__objc_intobj: 0x480
+  __AUTH_CONST.__cfstring: 0x5f20
+  __AUTH_CONST.__objc_const: 0x3fe8
+  __AUTH_CONST.__objc_intobj: 0x498
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH.__objc_data: 0x10e0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 18A655BB-4DB3-3DCF-826C-3992F372230E
-  Functions: 2589
-  Symbols:   6565
-  CStrings:  5030
+  UUID: DE3B74A9-B9AE-3CB9-B432-20B26473D6AF
+  Functions: 2643
+  Symbols:   6635
+  CStrings:  5045
 
Symbols:
+ +[UIAccessibilityAutoscrollManager sharedInstance].cold.1
+ +[UIAccessibilityInformationLoader sharedInstance].cold.1
+ +[UIAccessibilityLegacyLoader initialize].cold.1
+ +[UIAccessibilityLoader _accessibilityBundlesForBundle:].cold.1
+ +[UIAccessibilityLoader _accessibilityInitializeRuntimeOverrides].cold.1
+ +[UIAccessibilityLoader _accessibilityStartMiniServer].cold.1
+ +[UIAccessibilityLoader _stringLocalizationStarted:].cold.1
+ +[UIAccessibilityLoader loadAccessibilityBundle:didLoadCallback:loadSubbundles:].cold.1
+ +[UIAccessibilityLoader loadAccessibilityBundleForBundle:didLoadCallback:forceLoad:loadSubbundles:loadAllAccessibilityInfo:].cold.1
+ -[NSBundleAccessibility loadAndReturnError:].cold.1
+ -[NSObject(AXPrivCategory) _accessibilityFirstElementsForSpeakThis].cold.1
+ -[NSObject(AXPrivCategory) _accessibilityNextElementsForSpeakThis].cold.1
+ -[NSObject(AXPrivCategory) _accessibilityOverridesPotentiallyAttributedAPISelector:].cold.1
+ -[NSObject(AXPrivCategory) _accessibilityPotentiallyAttributedValueForNonAttributedSelector:attributedSelector:].cold.1
+ -[NSObject(AXPrivCategory) _accessibilityPrefersNonAttributedAttributeWithOverrideSelector:nonAttributedSelector:attributedSelector:].cold.1
+ -[NSObject(AXPrivCategory) _accessibilityPublicCustomRotors].cold.1
+ -[NSObject(AXPrivCategory) _accessibilitySupportedLanguages].cold.1
+ -[NSObject(AXPrivCategory) _accessibilityUserTestingActionIdentifiers].cold.1
+ -[NSObject(AXPrivCategory) _accessibilityUserTestingActionIdentifiers].cold.2
+ -[NSObject(AXPrivCategory) accessibilityShouldEnumerateContainerElementsArrayDirectly].cold.1
+ -[NSObject(UIAccessibilityAutomation) _accessibilityUserTestingSnapshotWithOptions:].cold.1
+ -[NSObject(UIAccessibilityAutomation) _accessibilityUserTestingSnapshot].cold.1
+ -[NSObject(UIStorage) _accessibilityIsContainedByVideoElement].cold.1
+ -[UIAccessibilityCustomAction(Private) _accessibilityAXAttributedName].cold.1
+ -[UIAccessibilityCustomRotor(AXPrivate) _accessibilityAXAttributedName].cold.1
+ -[UIAccessibilityInMemoryStringBasedTreeLogger initWithPrefix:elementDescriptionKey:].cold.1
+ -[UIApplication(UIAccessibility) _accessibilityMaximumAllowedOutOfBoundsPercent].cold.1
+ GCC_except_table1031
+ GCC_except_table1177
+ GCC_except_table1318
+ GCC_except_table430
+ GCC_except_table462
+ GCC_except_table473
+ GCC_except_table484
+ GCC_except_table486
+ GCC_except_table488
+ GCC_except_table496
+ GCC_except_table590
+ GCC_except_table700
+ GCC_except_table711
+ GCC_except_table736
+ GCC_except_table740
+ GCC_except_table792
+ GCC_except_table802
+ GCC_except_table833
+ GCC_except_table864
+ UIAccessibilityBundle.cold.1
+ UIAccessibilityIsAppExtension.cold.1
+ UIAccessibilityIsWidgetExtension.cold.1
+ UIAccessibilityStartCapturingStringDrawingText.cold.1
+ _OBJC_CLASS_$_NSTextContentStorage
+ _OUTLINED_FUNCTION_16
+ _OUTLINED_FUNCTION_17
+ _OUTLINED_FUNCTION_18
+ _OUTLINED_FUNCTION_19
+ _OUTLINED_FUNCTION_20
+ _OUTLINED_FUNCTION_21
+ _OUTLINED_FUNCTION_22
+ _OUTLINED_FUNCTION_23
+ _OUTLINED_FUNCTION_24
+ _OUTLINED_FUNCTION_25
+ _OUTLINED_FUNCTION_26
+ _OUTLINED_FUNCTION_27
+ _OUTLINED_FUNCTION_28
+ _UIAXAutomationIgnoreLogging.cold.1
+ _UIAXInitializeConstantValues.cold.1
+ _UIAccessibilityBlockPostingOfNotification.cold.1
+ _UIAccessibilityQueueNotification.cold.1
+ _UIAccessibilitySetFocusedElement.cold.1
+ _UIAccessibilityStart.cold.2
+ __149-[NSObject(AXPrivCategory) _accessibilityNextOpaqueElementsForTechnology:startElement:direction:searchType:range:shouldScrollToVisible:honorsGroups:]_block_invoke.1362
+ __174-[NSObject(AXPrivCategory) _accessibilitySearchSubtreesAfterChildElement:direction:searchType:allowOutOfBoundsChild:range:shouldScrollToVisible:honorGroups:updatedContainer:]_block_invoke.1378
+ __174-[NSObject(AXPrivCategory) _accessibilitySearchSubtreesAfterChildElement:direction:searchType:allowOutOfBoundsChild:range:shouldScrollToVisible:honorGroups:updatedContainer:]_block_invoke.1383
+ __50+[UIAccessibilityLoader _accessibilityStartServer]_block_invoke.cold.1
+ __59-[NSObject(AXPrivCategory) _accessibilityLastOpaqueElement]_block_invoke.cold.2
+ __60-[NSObject(AXPrivCategory) _accessibilityFirstOpaqueElement]_block_invoke.cold.2
+ __60-[NSObject(AXPrivCategory) _accessibilityHitTest:withEvent:]_block_invoke.cold.2
+ __60-[NSObject(AXPrivCategory) _iosAccessibilityAttributeValue:]_block_invoke.1117
+ __60-[NSObject(AXPrivCategory) _iosAccessibilityAttributeValue:]_block_invoke.1117.cold.1
+ __60-[NSObject(AXPrivCategory) _iosAccessibilityAttributeValue:]_block_invoke.1117.cold.2
+ __62-[NSObject(AXPrivCategory) _accessibilityFirstElementForFocus]_block_invoke.cold.2
+ __62-[NSObject(AXPrivCategory) _accessibilitySortedElementsWithin]_block_invoke.cold.2
+ __68-[NSObject(AXPrivCategory) _accessibilityFirstOpaqueElementForFocus]_block_invoke.cold.2
+ __71-[NSObject(AXPrivCategory) _accessibilityLastOpaqueElementWithOptions:]_block_invoke.cold.2
+ __72-[NSObject(AXPrivCategory) _accessibilityFirstOpaqueElementWithOptions:]_block_invoke.cold.2
+ __74-[NSObject(AXPrivCategory) _accessibilityFirstElementForFocusWithOptions:]_block_invoke.cold.2
+ __74-[NSObject(AXPrivCategory) _accessibilitySortedElementsWithinWithOptions:]_block_invoke.cold.2
+ __79-[NSObject(AXPrivCategory) _accessibilityReplaceCharactersAtCursor:withString:]_block_invoke.1808
+ __80-[NSObject(AXPrivCategory) _accessibilityFirstOpaqueElementForFocusWithOptions:]_block_invoke.cold.2
+ ___63-[NSObject(AXPrivCategory) _accessibilityFocusableFrameForZoom]_block_invoke
+ __block_literal_global.1099
+ __block_literal_global.1119
+ __block_literal_global.1302
+ __block_literal_global.1304
+ __block_literal_global.1359
+ __block_literal_global.1361
+ __block_literal_global.1370
+ __block_literal_global.1374
+ __block_literal_global.1381
+ __block_literal_global.1386
+ __block_literal_global.1402
+ __block_literal_global.1411
+ __block_literal_global.1413
+ __block_literal_global.1421
+ __block_literal_global.1505
+ __block_literal_global.1508
+ __block_literal_global.1798
+ __block_literal_global.1804
+ __block_literal_global.1810
+ __block_literal_global.1874
+ __block_literal_global.1893
+ __block_literal_global.1908
+ __block_literal_global.1910
+ __block_literal_global.1913
+ __block_literal_global.1915
+ __block_literal_global.1919
+ __block_literal_global.2977
+ __block_literal_global.3176
+ __block_literal_global.3178
+ __block_literal_global.3180
+ __block_literal_global.3188
+ __block_literal_global.3196
+ __block_literal_global.3199
+ __block_literal_global.3201
+ __block_literal_global.348
+ __block_literal_global.357
+ __block_literal_global.360
+ __block_literal_global.376
+ __block_literal_global.378
+ __block_literal_global.387
+ __block_literal_global.447
+ __block_literal_global.449
+ __block_literal_global.540
+ __block_literal_global.545
+ __block_literal_global.547
+ __block_literal_global.549
+ __block_literal_global.551
+ __block_literal_global.674
+ _copyElementAtPositionCallback.cold.1
+ _objc_msgSend$safeCGPointForKey:
+ _objc_msgSend$textContentManager
+ _objc_msgSend$textLayoutManager
+ _objc_msgSend$validateClass:isKindOfClass:
+ _switchControlNegatesPerformEscapeAnswer.cold.1
- GCC_except_table1030
- GCC_except_table1176
- GCC_except_table1317
- GCC_except_table461
- GCC_except_table472
- GCC_except_table483
- GCC_except_table485
- GCC_except_table487
- GCC_except_table495
- GCC_except_table589
- GCC_except_table699
- GCC_except_table710
- GCC_except_table735
- GCC_except_table739
- GCC_except_table791
- GCC_except_table801
- GCC_except_table832
- GCC_except_table863
- __149-[NSObject(AXPrivCategory) _accessibilityNextOpaqueElementsForTechnology:startElement:direction:searchType:range:shouldScrollToVisible:honorsGroups:]_block_invoke.1356
- __174-[NSObject(AXPrivCategory) _accessibilitySearchSubtreesAfterChildElement:direction:searchType:allowOutOfBoundsChild:range:shouldScrollToVisible:honorGroups:updatedContainer:]_block_invoke.1372
- __174-[NSObject(AXPrivCategory) _accessibilitySearchSubtreesAfterChildElement:direction:searchType:allowOutOfBoundsChild:range:shouldScrollToVisible:honorGroups:updatedContainer:]_block_invoke.1377
- __60-[NSObject(AXPrivCategory) _iosAccessibilityAttributeValue:]_block_invoke.1113
- __60-[NSObject(AXPrivCategory) _iosAccessibilityAttributeValue:]_block_invoke.1113.cold.1
- __79-[NSObject(AXPrivCategory) _accessibilityReplaceCharactersAtCursor:withString:]_block_invoke.1794
- __block_literal_global.1095
- __block_literal_global.1115
- __block_literal_global.1296
- __block_literal_global.1298
- __block_literal_global.1337
- __block_literal_global.1341
- __block_literal_global.1358
- __block_literal_global.1368
- __block_literal_global.1375
- __block_literal_global.1380
- __block_literal_global.1396
- __block_literal_global.1401
- __block_literal_global.1403
- __block_literal_global.1405
- __block_literal_global.1499
- __block_literal_global.1502
- __block_literal_global.1782
- __block_literal_global.1784
- __block_literal_global.1790
- __block_literal_global.1860
- __block_literal_global.1879
- __block_literal_global.1894
- __block_literal_global.1896
- __block_literal_global.1899
- __block_literal_global.1901
- __block_literal_global.1905
- __block_literal_global.2963
- __block_literal_global.3162
- __block_literal_global.3164
- __block_literal_global.3166
- __block_literal_global.3174
- __block_literal_global.3182
- __block_literal_global.3185
- __block_literal_global.3187
- __block_literal_global.342
- __block_literal_global.351
- __block_literal_global.354
- __block_literal_global.370
- __block_literal_global.372
- __block_literal_global.374
- __block_literal_global.379
- __block_literal_global.381
- __block_literal_global.438
- __block_literal_global.441
- __block_literal_global.443
- __block_literal_global.532
- __block_literal_global.535
- __block_literal_global.537
- __block_literal_global.539
- __block_literal_global.541
- __block_literal_global.665
- _objc_msgSend$layoutManager
- _strcmp
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AccessibilityFrameworks/Source/UIAccessibility/AXRemoteElement+UIAccessibility.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AccessibilityFrameworks/Source/UIAccessibility/NSBundle+UIAccessibilityLoader.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AccessibilityFrameworks/Source/UIAccessibility/NSObjectAccessibility.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AccessibilityFrameworks/Source/UIAccessibility/UIAccessibilityElementTraversal.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AccessibilityFrameworks/Source/UIAccessibility/UIAccessibilityNotification.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AccessibilityFrameworks/Source/UIAccessibility/UIAccessibilityOpaqueElementProvider.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AccessibilityFrameworks/Source/UIAccessibility/UIKitAccessibility.m"
+ "@\"UIConversationContext\"16@0:8"
+ "DashBoard.DBDockSceneHostWindow"
+ "NSTextContentManager"
+ "NSTextContentStorage"
+ "T@\"UIConversationContext\",?,&,N"
+ "_focusTargetOffset"
+ "conversationContext"
+ "insertInputSuggestion:"
+ "safeCGPointForKey:"
+ "setConversationContext:"
+ "textContentManager"
+ "textLayoutManager"
+ "v24@0:8@\"UIConversationContext\"16"
+ "v24@0:8@\"UIInputSuggestion\"16"
+ "validateClass:isKindOfClass:"
- "/AppleInternal/Library/BuildRoots/91509d18-d3bf-11ef-a177-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AccessibilityFrameworks/Source/UIAccessibility/AXRemoteElement+UIAccessibility.m"
- "/AppleInternal/Library/BuildRoots/91509d18-d3bf-11ef-a177-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AccessibilityFrameworks/Source/UIAccessibility/NSBundle+UIAccessibilityLoader.m"
- "/AppleInternal/Library/BuildRoots/91509d18-d3bf-11ef-a177-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AccessibilityFrameworks/Source/UIAccessibility/NSObjectAccessibility.m"
- "/AppleInternal/Library/BuildRoots/91509d18-d3bf-11ef-a177-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AccessibilityFrameworks/Source/UIAccessibility/UIAccessibilityElementTraversal.m"
- "/AppleInternal/Library/BuildRoots/91509d18-d3bf-11ef-a177-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AccessibilityFrameworks/Source/UIAccessibility/UIAccessibilityNotification.m"
- "/AppleInternal/Library/BuildRoots/91509d18-d3bf-11ef-a177-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AccessibilityFrameworks/Source/UIAccessibility/UIAccessibilityOpaqueElementProvider.m"
- "/AppleInternal/Library/BuildRoots/91509d18-d3bf-11ef-a177-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AccessibilityFrameworks/Source/UIAccessibility/UIKitAccessibility.m"
- "DBStatusBarHostWindow"
- "layoutManager"

```
