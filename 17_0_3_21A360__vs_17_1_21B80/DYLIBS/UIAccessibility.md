## UIAccessibility

> `/System/Library/PrivateFrameworks/UIAccessibility.framework/UIAccessibility`

```diff

-3089.1.0.0.0
-  __TEXT.__text: 0x61d1c
-  __TEXT.__auth_stubs: 0x1510
-  __TEXT.__objc_methlist: 0x5e58
+3093.2.4.0.2
+  __TEXT.__text: 0x61fd4
+  __TEXT.__auth_stubs: 0x1530
+  __TEXT.__objc_methlist: 0x5e70
   __TEXT.__const: 0x1f8
-  __TEXT.__cstring: 0x66d8
-  __TEXT.__oslogstring: 0x2a3c
+  __TEXT.__cstring: 0x669a
+  __TEXT.__oslogstring: 0x2a66
   __TEXT.__gcc_except_tab: 0xb80
   __TEXT.__dlopen_cstrs: 0x208
-  __TEXT.__unwind_info: 0x19b8
+  __TEXT.__ustring: 0xe
+  __TEXT.__unwind_info: 0x19c8
   __TEXT.__objc_classname: 0xb74
-  __TEXT.__objc_methname: 0x15e28
+  __TEXT.__objc_methname: 0x15e66
   __TEXT.__objc_methtype: 0x1d0f
-  __TEXT.__objc_stubs: 0xfc80
-  __DATA_CONST.__got: 0x7f0
+  __TEXT.__objc_stubs: 0xfcc0
+  __DATA_CONST.__got: 0x7e0
   __DATA_CONST.__const: 0x1500
   __DATA_CONST.__objc_classlist: 0x1e8
   __DATA_CONST.__objc_catlist: 0xa0
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x3e80
-  __DATA_CONST.__objc_selrefs: 0x4df0
-  __DATA_CONST.__objc_arraydata: 0x118
+  __DATA_CONST.__objc_selrefs: 0x4e00
+  __DATA_CONST.__objc_arraydata: 0x128
   __AUTH_CONST.__const: 0x1188
-  __AUTH_CONST.__cfstring: 0x5b00
+  __AUTH_CONST.__cfstring: 0x5ae0
   __AUTH_CONST.__objc_const: 0x1868
   __AUTH_CONST.__objc_intobj: 0x480
-  __AUTH_CONST.__objc_dictobj: 0x50
+  __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x48
-  __AUTH_CONST.__auth_got: 0xa98
+  __AUTH_CONST.__auth_got: 0xaa8
   __AUTH.__objc_data: 0xe60
   __DATA.__objc_protorefs: 0x28
   __DATA.__objc_classrefs: 0x490

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7A58D0B7-812D-322C-9AEA-32E4481965C1
-  Functions: 2677
-  Symbols:   9224
-  CStrings:  5048
+  UUID: C0C13570-58A1-3098-B055-E2D96887078B
+  Functions: 2682
+  Symbols:   9237
+  CStrings:  5047
 
Symbols:
+ -[NSObject(AXAutoscrolling) _accessibilityGetAllScrollViews]
+ -[NSObject(AXPrivCategory) accessibilityCustomAttribute:]
+ -[NSObject(UIAccessibilityElementTraversal) _accessibilityShouldBeAddedToViewChildrenWithOptions:]
+ -[NSObject(UIAccessibilityElementTraversal) _addAccessibilityElementsAndOrderedContainersWithOptions:toCollection:]
+ GCC_except_table1011
+ GCC_except_table1114
+ GCC_except_table1160
+ GCC_except_table1297
+ GCC_except_table167
+ GCC_except_table47
+ GCC_except_table60
+ GCC_except_table63
+ GCC_except_table718
+ GCC_except_table722
+ GCC_except_table774
+ GCC_except_table784
+ GCC_except_table814
+ GCC_except_table846
+ GCC_except_table86
+ _AXUIAccessibilitySpeechAttributePhonemeSubstitution
+ _CGColorGetTypeID
+ _UIImageGetNavigationBarBackArrow
+ __UIAXColorForObject
+ __UIAccessibilityPostPlaybackControlsVisibilityChangedNotification
+ ___104+[UIAccessibilityLoader _performInitialAccessibilityBundleLoad:monitorForFutureLoadEvents:trackingMode:]_block_invoke.212
+ ___104+[UIAccessibilityLoader _performInitialAccessibilityBundleLoad:monitorForFutureLoadEvents:trackingMode:]_block_invoke.220
+ ___104+[UIAccessibilityLoader _performInitialAccessibilityBundleLoad:monitorForFutureLoadEvents:trackingMode:]_block_invoke.225
+ ___104+[UIAccessibilityLoader _performInitialAccessibilityBundleLoad:monitorForFutureLoadEvents:trackingMode:]_block_invoke.232
+ ___104+[UIAccessibilityLoader _performInitialAccessibilityBundleLoad:monitorForFutureLoadEvents:trackingMode:]_block_invoke_2.226
+ ___115-[NSObject(UIAccessibilityElementTraversal) _addAccessibilityElementsAndOrderedContainersWithOptions:toCollection:]_block_invoke
+ ___115-[NSObject(UIAccessibilityElementTraversal) _addAccessibilityElementsAndOrderedContainersWithOptions:toCollection:]_block_invoke_2
+ ___146-[NSObject(AXPrivCategory) _accessibilityMoveFocusToNextOpaqueElementForTechnology:direction:searchType:range:shouldScrollToVisible:honorsGroups:]_block_invoke.1139
+ ___148-[NSObject(UIAccessibilityAutomation) _accessibilityUserTestingSnapshotAncestorsWithAttributes:maxDepth:maxChildren:maxArrayCount:honorsModalViews:]_block_invoke.324
+ ___148-[NSObject(UIAccessibilityAutomation) _accessibilityUserTestingSnapshotAncestorsWithAttributes:maxDepth:maxChildren:maxArrayCount:honorsModalViews:]_block_invoke.324.cold.1
+ ___150-[NSObject(UIAccessibilityAutomation) _accessibilityUserTestingSnapshotDescendantsWithAttributes:maxDepth:maxChildren:maxArrayCount:honorsModalViews:]_block_invoke.321
+ ___150-[NSObject(UIAccessibilityAutomation) _accessibilityUserTestingSnapshotDescendantsWithAttributes:maxDepth:maxChildren:maxArrayCount:honorsModalViews:]_block_invoke.321.cold.1
+ ___150-[NSObject(UIAccessibilityAutomation) _accessibilityUserTestingSnapshotDescendantsWithAttributes:maxDepth:maxChildren:maxArrayCount:honorsModalViews:]_block_invoke.321.cold.2
+ ___150-[NSObject(UIAccessibilityAutomation) _accessibilityUserTestingSnapshotDescendantsWithAttributes:maxDepth:maxChildren:maxArrayCount:honorsModalViews:]_block_invoke.321.cold.3
+ ___174-[NSObject(AXPrivCategory) _accessibilitySearchSubtreesAfterChildElement:direction:searchType:allowOutOfBoundsChild:range:shouldScrollToVisible:honorGroups:updatedContainer:]_block_invoke.1155
+ ___174-[NSObject(AXPrivCategory) _accessibilitySearchSubtreesAfterChildElement:direction:searchType:allowOutOfBoundsChild:range:shouldScrollToVisible:honorGroups:updatedContainer:]_block_invoke.1160
+ ___60+[UIAccessibilityLegacyLoader _accessibilityLoadSubbundles:]_block_invoke.301
+ ___60+[UIAccessibilityLegacyLoader _accessibilityLoadSubbundles:]_block_invoke_2.302
+ ___60-[NSObject(AXAutoscrolling) _accessibilityGetAllScrollViews]_block_invoke
+ ___60-[NSObject(AXPrivCategory) _iosAccessibilityAttributeValue:]_block_invoke.899
+ ___60-[NSObject(AXPrivCategory) _iosAccessibilityAttributeValue:]_block_invoke.899.cold.1
+ ___63+[UIAccessibilityLegacyLoader loadExtendedAccessibilityBundles]_block_invoke.240
+ ___63+[UIAccessibilityLegacyLoader loadExtendedAccessibilityBundles]_block_invoke.242
+ ___79-[NSObject(AXPrivCategory) _accessibilityReplaceCharactersAtCursor:withString:]_block_invoke.1520
+ ____copyElementAtPositionCallback_block_invoke.218
+ ____copyElementAtPositionCallback_block_invoke.232
+ ___block_literal_global.1082
+ ___block_literal_global.1084
+ ___block_literal_global.1120
+ ___block_literal_global.1124
+ ___block_literal_global.1141
+ ___block_literal_global.1151
+ ___block_literal_global.1158
+ ___block_literal_global.1163
+ ___block_literal_global.1179
+ ___block_literal_global.1184
+ ___block_literal_global.1186
+ ___block_literal_global.1188
+ ___block_literal_global.1283
+ ___block_literal_global.1286
+ ___block_literal_global.1512
+ ___block_literal_global.1514
+ ___block_literal_global.1516
+ ___block_literal_global.1580
+ ___block_literal_global.1591
+ ___block_literal_global.1602
+ ___block_literal_global.1612
+ ___block_literal_global.1614
+ ___block_literal_global.1617
+ ___block_literal_global.1619
+ ___block_literal_global.213
+ ___block_literal_global.215
+ ___block_literal_global.217
+ ___block_literal_global.218
+ ___block_literal_global.220
+ ___block_literal_global.227
+ ___block_literal_global.228
+ ___block_literal_global.235
+ ___block_literal_global.237
+ ___block_literal_global.255
+ ___block_literal_global.2666
+ ___block_literal_global.267
+ ___block_literal_global.278
+ ___block_literal_global.282
+ ___block_literal_global.285
+ ___block_literal_global.2854
+ ___block_literal_global.2856
+ ___block_literal_global.2866
+ ___block_literal_global.287
+ ___block_literal_global.2874
+ ___block_literal_global.2877
+ ___block_literal_global.2879
+ ___block_literal_global.302
+ ___block_literal_global.304
+ ___block_literal_global.306
+ ___block_literal_global.311
+ ___block_literal_global.313
+ ___block_literal_global.335
+ ___block_literal_global.346
+ ___block_literal_global.349
+ ___block_literal_global.351
+ ___block_literal_global.356
+ ___block_literal_global.369
+ ___block_literal_global.372
+ ___block_literal_global.374
+ ___block_literal_global.411
+ ___block_literal_global.424
+ ___block_literal_global.435
+ ___block_literal_global.437
+ ___block_literal_global.440
+ ___block_literal_global.442
+ ___block_literal_global.444
+ ___block_literal_global.472
+ ___block_literal_global.486
+ ___block_literal_global.509
+ ___block_literal_global.514
+ ___block_literal_global.516
+ ___block_literal_global.545
+ ___block_literal_global.550
+ ___block_literal_global.552
+ ___block_literal_global.559
+ ___block_literal_global.570
+ ___block_literal_global.659
+ ___block_literal_global.728
+ ___block_literal_global.759
+ ___block_literal_global.767
+ ___block_literal_global.776
+ ___block_literal_global.778
+ ___block_literal_global.807
+ ___block_literal_global.881
+ ___block_literal_global.901
+ __unnamed_array_storage.1294
+ __unnamed_array_storage.1296
+ __unnamed_array_storage.1297
+ __unnamed_array_storage.325
+ __unnamed_array_storage.382
+ _objc_msgSend$_accessibilityGetAllScrollViews
+ _objc_msgSend$accessibilityCustomAttribute:
- -[UIView(UIAccessibilityElementTraversal) _accessibilityShouldBeAddedToViewChildrenWithOptions:]
- -[UIView(UIAccessibilityElementTraversal) _addAccessibilityElementsAndOrderedContainersWithOptions:toCollection:]
- GCC_except_table1010
- GCC_except_table1113
- GCC_except_table1159
- GCC_except_table1294
- GCC_except_table166
- GCC_except_table45
- GCC_except_table59
- GCC_except_table62
- GCC_except_table717
- GCC_except_table721
- GCC_except_table773
- GCC_except_table783
- GCC_except_table813
- GCC_except_table845
- GCC_except_table85
- _AXUIAccessibilitySpeechAttributePoorMansPronunciationHelp
- _AXUIAccessibilitySpeechAttributePoorMansPronunciationHelpForMacintalk
- _AXUIAccessibilitySpeechAttributePoorMansPronunciationHelpForNashville
- ___104+[UIAccessibilityLoader _performInitialAccessibilityBundleLoad:monitorForFutureLoadEvents:trackingMode:]_block_invoke.218
- ___104+[UIAccessibilityLoader _performInitialAccessibilityBundleLoad:monitorForFutureLoadEvents:trackingMode:]_block_invoke.226
- ___104+[UIAccessibilityLoader _performInitialAccessibilityBundleLoad:monitorForFutureLoadEvents:trackingMode:]_block_invoke.231
- ___104+[UIAccessibilityLoader _performInitialAccessibilityBundleLoad:monitorForFutureLoadEvents:trackingMode:]_block_invoke.238
- ___104+[UIAccessibilityLoader _performInitialAccessibilityBundleLoad:monitorForFutureLoadEvents:trackingMode:]_block_invoke_2.232
- ___113-[UIView(UIAccessibilityElementTraversal) _addAccessibilityElementsAndOrderedContainersWithOptions:toCollection:]_block_invoke
- ___113-[UIView(UIAccessibilityElementTraversal) _addAccessibilityElementsAndOrderedContainersWithOptions:toCollection:]_block_invoke_2
- ___146-[NSObject(AXPrivCategory) _accessibilityMoveFocusToNextOpaqueElementForTechnology:direction:searchType:range:shouldScrollToVisible:honorsGroups:]_block_invoke.1145
- ___148-[NSObject(UIAccessibilityAutomation) _accessibilityUserTestingSnapshotAncestorsWithAttributes:maxDepth:maxChildren:maxArrayCount:honorsModalViews:]_block_invoke.330
- ___148-[NSObject(UIAccessibilityAutomation) _accessibilityUserTestingSnapshotAncestorsWithAttributes:maxDepth:maxChildren:maxArrayCount:honorsModalViews:]_block_invoke.330.cold.1
- ___150-[NSObject(UIAccessibilityAutomation) _accessibilityUserTestingSnapshotDescendantsWithAttributes:maxDepth:maxChildren:maxArrayCount:honorsModalViews:]_block_invoke.327
- ___150-[NSObject(UIAccessibilityAutomation) _accessibilityUserTestingSnapshotDescendantsWithAttributes:maxDepth:maxChildren:maxArrayCount:honorsModalViews:]_block_invoke.327.cold.1
- ___150-[NSObject(UIAccessibilityAutomation) _accessibilityUserTestingSnapshotDescendantsWithAttributes:maxDepth:maxChildren:maxArrayCount:honorsModalViews:]_block_invoke.327.cold.2
- ___150-[NSObject(UIAccessibilityAutomation) _accessibilityUserTestingSnapshotDescendantsWithAttributes:maxDepth:maxChildren:maxArrayCount:honorsModalViews:]_block_invoke.327.cold.3
- ___174-[NSObject(AXPrivCategory) _accessibilitySearchSubtreesAfterChildElement:direction:searchType:allowOutOfBoundsChild:range:shouldScrollToVisible:honorGroups:updatedContainer:]_block_invoke.1161
- ___174-[NSObject(AXPrivCategory) _accessibilitySearchSubtreesAfterChildElement:direction:searchType:allowOutOfBoundsChild:range:shouldScrollToVisible:honorGroups:updatedContainer:]_block_invoke.1166
- ___60+[UIAccessibilityLegacyLoader _accessibilityLoadSubbundles:]_block_invoke.307
- ___60+[UIAccessibilityLegacyLoader _accessibilityLoadSubbundles:]_block_invoke_2.308
- ___60-[NSObject(AXPrivCategory) _iosAccessibilityAttributeValue:]_block_invoke.905
- ___60-[NSObject(AXPrivCategory) _iosAccessibilityAttributeValue:]_block_invoke.905.cold.1
- ___63+[UIAccessibilityLegacyLoader loadExtendedAccessibilityBundles]_block_invoke.246
- ___63+[UIAccessibilityLegacyLoader loadExtendedAccessibilityBundles]_block_invoke.248
- ___79-[NSObject(AXPrivCategory) _accessibilityReplaceCharactersAtCursor:withString:]_block_invoke.1526
- ____copyElementAtPositionCallback_block_invoke.224
- ____copyElementAtPositionCallback_block_invoke.238
- ___block_literal_global.1088
- ___block_literal_global.1090
- ___block_literal_global.1142
- ___block_literal_global.1144
- ___block_literal_global.1153
- ___block_literal_global.1157
- ___block_literal_global.1164
- ___block_literal_global.1169
- ___block_literal_global.1185
- ___block_literal_global.1194
- ___block_literal_global.1196
- ___block_literal_global.1204
- ___block_literal_global.1289
- ___block_literal_global.1292
- ___block_literal_global.1518
- ___block_literal_global.1520
- ___block_literal_global.1528
- ___block_literal_global.1586
- ___block_literal_global.1597
- ___block_literal_global.1608
- ___block_literal_global.1618
- ___block_literal_global.1620
- ___block_literal_global.1625
- ___block_literal_global.1629
- ___block_literal_global.221
- ___block_literal_global.224
- ___block_literal_global.226
- ___block_literal_global.229
- ___block_literal_global.231
- ___block_literal_global.233
- ___block_literal_global.240
- ___block_literal_global.243
- ___block_literal_global.247
- ___block_literal_global.261
- ___block_literal_global.2671
- ___block_literal_global.279
- ___block_literal_global.2860
- ___block_literal_global.2862
- ___block_literal_global.2870
- ___block_literal_global.2878
- ___block_literal_global.288
- ___block_literal_global.2881
- ___block_literal_global.2883
- ___block_literal_global.290
- ___block_literal_global.291
- ___block_literal_global.293
- ___block_literal_global.308
- ___block_literal_global.312
- ___block_literal_global.316
- ___block_literal_global.319
- ___block_literal_global.329
- ___block_literal_global.341
- ___block_literal_global.352
- ___block_literal_global.355
- ___block_literal_global.357
- ___block_literal_global.362
- ___block_literal_global.375
- ___block_literal_global.378
- ___block_literal_global.380
- ___block_literal_global.423
- ___block_literal_global.443
- ___block_literal_global.450
- ___block_literal_global.452
- ___block_literal_global.454
- ___block_literal_global.465
- ___block_literal_global.476
- ___block_literal_global.478
- ___block_literal_global.492
- ___block_literal_global.520
- ___block_literal_global.522
- ___block_literal_global.534
- ___block_literal_global.551
- ___block_literal_global.556
- ___block_literal_global.558
- ___block_literal_global.565
- ___block_literal_global.576
- ___block_literal_global.665
- ___block_literal_global.734
- ___block_literal_global.765
- ___block_literal_global.773
- ___block_literal_global.782
- ___block_literal_global.784
- ___block_literal_global.813
- ___block_literal_global.887
- ___block_literal_global.907
- __unnamed_array_storage.1300
- __unnamed_array_storage.1302
- __unnamed_array_storage.1303
- __unnamed_array_storage.331
CStrings:
+ "-[NSObject(UIAccessibilityElementTraversal) _accessibilityShouldBeAddedToViewChildrenWithOptions:]"
+ "-[NSObject(UIAccessibilityElementTraversal) _addAccessibilityElementsAndOrderedContainersWithOptions:toCollection:]"
+ "Attempting to send notification: %@ (%d) %{sensitive}@"
+ "Checking visibility for %{private}@"
+ "Did post notification. notification: %@ (%d) error:%d data:%{sensitive}@"
+ "Performing visible point test: %{private}@, parent: %@, window: %@"
+ "Post notification failed. notification: %@ (%d) error:%d data:%{sensitive}@"
+ "Received visible point %@ for %@{private}"
+ "_accessibilityGetAllScrollViews"
+ "accessibilityCustomAttribute:"
+ "\xc8\x02l"
- "\x1b\\toi=lhp\\la&Iv\x1b\\toi=orth\\"
- "-[UIView(UIAccessibilityElementTraversal) _accessibilityShouldBeAddedToViewChildrenWithOptions:]"
- "-[UIView(UIAccessibilityElementTraversal) _addAccessibilityElementsAndOrderedContainersWithOptions:toCollection:]"
- "Attempting to send notification: %@ (%d) %@"
- "Checking visibility for %@"
- "Did post notification. notification: %@ (%d) error:%d data:%{private}@"
- "Performing visible point test: %@, parent: %@, window: %@"
- "Post notification failed. notification: %@ (%d) error:%d data:%{private}@"
- "Received visible point %@ for %@"
- "[[ctxt adjective]] live [[ctxt norm]] "

```
