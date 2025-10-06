## UIAccessibility

> `/System/Library/PrivateFrameworks/UIAccessibility.framework/UIAccessibility`

```diff

-3093.2.4.4.11
-  __TEXT.__text: 0x62248
-  __TEXT.__auth_stubs: 0x1540
-  __TEXT.__objc_methlist: 0x5e78
-  __TEXT.__const: 0x1f8
-  __TEXT.__cstring: 0x669a
-  __TEXT.__oslogstring: 0x2aad
+3093.23.0.0.0
+  __TEXT.__text: 0x6273c
+  __TEXT.__auth_stubs: 0x1550
+  __TEXT.__objc_methlist: 0x5eb0
+  __TEXT.__const: 0x218
+  __TEXT.__cstring: 0x66ee
+  __TEXT.__oslogstring: 0x2aeb
   __TEXT.__gcc_except_tab: 0xb80
   __TEXT.__dlopen_cstrs: 0x208
   __TEXT.__ustring: 0xe
-  __TEXT.__unwind_info: 0x19c4
+  __TEXT.__unwind_info: 0x19e0
   __TEXT.__objc_classname: 0xb74
-  __TEXT.__objc_methname: 0x15e9e
-  __TEXT.__objc_methtype: 0x1d0f
-  __TEXT.__objc_stubs: 0xfce0
-  __DATA_CONST.__got: 0x7f0
-  __DATA_CONST.__const: 0x1500
+  __TEXT.__objc_methname: 0x16020
+  __TEXT.__objc_methtype: 0x1d67
+  __TEXT.__objc_stubs: 0xfde0
+  __DATA_CONST.__got: 0x800
+  __DATA_CONST.__const: 0x1520
   __DATA_CONST.__objc_classlist: 0x1e8
   __DATA_CONST.__objc_catlist: 0xa0
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x3e80
-  __DATA_CONST.__objc_selrefs: 0x4e08
+  __DATA_CONST.__objc_const: 0x3ea0
+  __DATA_CONST.__objc_selrefs: 0x4e48
+  __DATA_CONST.__objc_protorefs: 0x28
+  __DATA_CONST.__objc_classrefs: 0x498
+  __DATA_CONST.__objc_superrefs: 0x110
   __DATA_CONST.__objc_arraydata: 0x128
   __AUTH_CONST.__const: 0x1188
-  __AUTH_CONST.__cfstring: 0x5ae0
+  __AUTH_CONST.__cfstring: 0x5b00
   __AUTH_CONST.__objc_const: 0x1868
   __AUTH_CONST.__objc_intobj: 0x480
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x48
-  __AUTH_CONST.__auth_got: 0xab0
+  __AUTH_CONST.__auth_got: 0xab8
   __AUTH.__objc_data: 0xe60
-  __DATA.__objc_protorefs: 0x28
-  __DATA.__objc_classrefs: 0x490
-  __DATA.__objc_superrefs: 0x110
   __DATA.__objc_ivar: 0x174
   __DATA.__data: 0x7a0
   __DATA.__bss: 0x400
   __DATA.__common: 0x11
   __DATA_DIRTY.__objc_data: 0x4b0
-  __DATA_DIRTY.__bss: 0x210
+  __DATA_DIRTY.__bss: 0x208
   __DATA_DIRTY.__common: 0x230
   - /System/Library/Frameworks/Accessibility.framework/Accessibility
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D65FBD58-41F7-327B-81E3-A31FE5CFD3DB
-  Functions: 2683
-  Symbols:   9243
-  CStrings:  5050
+  UUID: B67CA843-1B2C-311D-A9D2-B532E42020DD
+  Functions: 2690
+  Symbols:   9270
+  CStrings:  5070
 
Symbols:
+ +[UIAccessibilityLoader _accessibilityUpdateSafeCategoryThread]
+ +[UIAccessibilityLoader _accessibilityUpdateSafeCategoryThread].cold.1
+ -[NSObject(AXPrivCategory) _accessibilityContentSize]
+ -[NSObject(AXPrivCategory) _accessibilityIsSwitch]
+ -[NSObject(AXPrivCategory) _setAccessibilityShouldUseViewHierarchyForFindingScrollParent:]
+ -[NSObject(AXPrivCategory) accessibilityIsInNonNativeTextControl]
+ GCC_except_table1015
+ GCC_except_table1118
+ GCC_except_table1164
+ GCC_except_table118
+ GCC_except_table122
+ GCC_except_table126
+ GCC_except_table128
+ GCC_except_table1301
+ GCC_except_table140
+ GCC_except_table168
+ GCC_except_table216
+ GCC_except_table219
+ GCC_except_table231
+ GCC_except_table265
+ GCC_except_table284
+ GCC_except_table340
+ GCC_except_table343
+ GCC_except_table415
+ GCC_except_table450
+ GCC_except_table461
+ GCC_except_table476
+ GCC_except_table484
+ GCC_except_table576
+ GCC_except_table685
+ GCC_except_table696
+ GCC_except_table721
+ GCC_except_table725
+ GCC_except_table76
+ GCC_except_table777
+ GCC_except_table787
+ GCC_except_table80
+ GCC_except_table818
+ GCC_except_table83
+ GCC_except_table850
+ GCC_except_table90
+ GCC_except_table92
+ GCC_except_table96
+ _AXLogValidations
+ _OBJC_CLASS_$_NSOperationQueue
+ _UIApplicationDidBecomeActiveNotification
+ _UIApplicationWillResignActiveNotification
+ ___104+[UIAccessibilityLoader _performInitialAccessibilityBundleLoad:monitorForFutureLoadEvents:trackingMode:]_block_invoke.236
+ ___104+[UIAccessibilityLoader _performInitialAccessibilityBundleLoad:monitorForFutureLoadEvents:trackingMode:]_block_invoke.244
+ ___104+[UIAccessibilityLoader _performInitialAccessibilityBundleLoad:monitorForFutureLoadEvents:trackingMode:]_block_invoke.249
+ ___104+[UIAccessibilityLoader _performInitialAccessibilityBundleLoad:monitorForFutureLoadEvents:trackingMode:]_block_invoke.256
+ ___104+[UIAccessibilityLoader _performInitialAccessibilityBundleLoad:monitorForFutureLoadEvents:trackingMode:]_block_invoke_2.250
+ ___146-[NSObject(AXPrivCategory) _accessibilityMoveFocusToNextOpaqueElementForTechnology:direction:searchType:range:shouldScrollToVisible:honorsGroups:]_block_invoke.1168
+ ___148-[NSObject(UIAccessibilityAutomation) _accessibilityUserTestingSnapshotAncestorsWithAttributes:maxDepth:maxChildren:maxArrayCount:honorsModalViews:]_block_invoke.348
+ ___148-[NSObject(UIAccessibilityAutomation) _accessibilityUserTestingSnapshotAncestorsWithAttributes:maxDepth:maxChildren:maxArrayCount:honorsModalViews:]_block_invoke.348.cold.1
+ ___150-[NSObject(UIAccessibilityAutomation) _accessibilityUserTestingSnapshotDescendantsWithAttributes:maxDepth:maxChildren:maxArrayCount:honorsModalViews:]_block_invoke.345
+ ___150-[NSObject(UIAccessibilityAutomation) _accessibilityUserTestingSnapshotDescendantsWithAttributes:maxDepth:maxChildren:maxArrayCount:honorsModalViews:]_block_invoke.345.cold.1
+ ___150-[NSObject(UIAccessibilityAutomation) _accessibilityUserTestingSnapshotDescendantsWithAttributes:maxDepth:maxChildren:maxArrayCount:honorsModalViews:]_block_invoke.345.cold.2
+ ___150-[NSObject(UIAccessibilityAutomation) _accessibilityUserTestingSnapshotDescendantsWithAttributes:maxDepth:maxChildren:maxArrayCount:honorsModalViews:]_block_invoke.345.cold.3
+ ___174-[NSObject(AXPrivCategory) _accessibilitySearchSubtreesAfterChildElement:direction:searchType:allowOutOfBoundsChild:range:shouldScrollToVisible:honorGroups:updatedContainer:]_block_invoke.1184
+ ___174-[NSObject(AXPrivCategory) _accessibilitySearchSubtreesAfterChildElement:direction:searchType:allowOutOfBoundsChild:range:shouldScrollToVisible:honorGroups:updatedContainer:]_block_invoke.1189
+ ___54+[UIAccessibilityLoader _accessibilityStartMiniServer]_block_invoke
+ ___60+[UIAccessibilityLegacyLoader _accessibilityLoadSubbundles:]_block_invoke.325
+ ___60+[UIAccessibilityLegacyLoader _accessibilityLoadSubbundles:]_block_invoke_2.326
+ ___60-[NSObject(AXPrivCategory) _iosAccessibilityAttributeValue:]_block_invoke.928
+ ___60-[NSObject(AXPrivCategory) _iosAccessibilityAttributeValue:]_block_invoke.928.cold.1
+ ___63+[UIAccessibilityLegacyLoader loadExtendedAccessibilityBundles]_block_invoke.264
+ ___63+[UIAccessibilityLegacyLoader loadExtendedAccessibilityBundles]_block_invoke.266
+ ___79-[NSObject(AXPrivCategory) _accessibilityReplaceCharactersAtCursor:withString:]_block_invoke.1552
+ ____copyElementAtPositionCallback_block_invoke.242
+ ____copyElementAtPositionCallback_block_invoke.256
+ ___block_descriptor_40_e24_v16?0"NSNotification"8l
+ ___block_literal_global.1111
+ ___block_literal_global.1113
+ ___block_literal_global.1149
+ ___block_literal_global.1153
+ ___block_literal_global.1155
+ ___block_literal_global.1159
+ ___block_literal_global.1161
+ ___block_literal_global.1165
+ ___block_literal_global.1167
+ ___block_literal_global.1170
+ ___block_literal_global.1176
+ ___block_literal_global.1180
+ ___block_literal_global.1187
+ ___block_literal_global.1208
+ ___block_literal_global.1213
+ ___block_literal_global.1215
+ ___block_literal_global.1217
+ ___block_literal_global.1219
+ ___block_literal_global.1221
+ ___block_literal_global.1227
+ ___block_literal_global.1312
+ ___block_literal_global.1315
+ ___block_literal_global.1544
+ ___block_literal_global.1546
+ ___block_literal_global.1548
+ ___block_literal_global.1554
+ ___block_literal_global.1634
+ ___block_literal_global.1644
+ ___block_literal_global.1646
+ ___block_literal_global.1649
+ ___block_literal_global.1651
+ ___block_literal_global.1655
+ ___block_literal_global.239
+ ___block_literal_global.242
+ ___block_literal_global.243
+ ___block_literal_global.244
+ ___block_literal_global.247
+ ___block_literal_global.249
+ ___block_literal_global.251
+ ___block_literal_global.252
+ ___block_literal_global.258
+ ___block_literal_global.259
+ ___block_literal_global.270
+ ___block_literal_global.2703
+ ___block_literal_global.279
+ ___block_literal_global.2891
+ ___block_literal_global.2893
+ ___block_literal_global.2895
+ ___block_literal_global.2903
+ ___block_literal_global.291
+ ___block_literal_global.2911
+ ___block_literal_global.2914
+ ___block_literal_global.2916
+ ___block_literal_global.302
+ ___block_literal_global.308
+ ___block_literal_global.311
+ ___block_literal_global.315
+ ___block_literal_global.331
+ ___block_literal_global.333
+ ___block_literal_global.337
+ ___block_literal_global.340
+ ___block_literal_global.341
+ ___block_literal_global.342
+ ___block_literal_global.347
+ ___block_literal_global.359
+ ___block_literal_global.378
+ ___block_literal_global.383
+ ___block_literal_global.399
+ ___block_literal_global.402
+ ___block_literal_global.404
+ ___block_literal_global.441
+ ___block_literal_global.459
+ ___block_literal_global.465
+ ___block_literal_global.468
+ ___block_literal_global.470
+ ___block_literal_global.476
+ ___block_literal_global.496
+ ___block_literal_global.498
+ ___block_literal_global.534
+ ___block_literal_global.543
+ ___block_literal_global.544
+ ___block_literal_global.557
+ ___block_literal_global.574
+ ___block_literal_global.579
+ ___block_literal_global.581
+ ___block_literal_global.588
+ ___block_literal_global.598
+ ___block_literal_global.688
+ ___block_literal_global.757
+ ___block_literal_global.788
+ ___block_literal_global.796
+ ___block_literal_global.805
+ ___block_literal_global.836
+ ___block_literal_global.910
+ ___block_literal_global.930
+ __unnamed_array_storage.1323
+ __unnamed_array_storage.1325
+ __unnamed_array_storage.1326
+ __unnamed_array_storage.349
+ __unnamed_array_storage.406
+ _objc_msgSend$_accessibilityContentSize
+ _objc_msgSend$_accessibilityIsOrnamentWindow
+ _objc_msgSend$_accessibilityIsSwitch
+ _objc_msgSend$_accessibilityUpdateSafeCategoryThread
+ _objc_msgSend$accessibilityIsInNonNativeTextControl
+ _objc_msgSend$addObserverForName:object:queue:usingBlock:
+ _objc_msgSend$mainQueue
+ _objc_msgSend$setInstallSafeCategoriesOffMainThread:
- GCC_except_table1011
- GCC_except_table1114
- GCC_except_table1160
- GCC_except_table117
- GCC_except_table121
- GCC_except_table125
- GCC_except_table127
- GCC_except_table1297
- GCC_except_table139
- GCC_except_table167
- GCC_except_table215
- GCC_except_table218
- GCC_except_table230
- GCC_except_table264
- GCC_except_table283
- GCC_except_table339
- GCC_except_table342
- GCC_except_table412
- GCC_except_table449
- GCC_except_table459
- GCC_except_table470
- GCC_except_table482
- GCC_except_table574
- GCC_except_table682
- GCC_except_table693
- GCC_except_table718
- GCC_except_table722
- GCC_except_table75
- GCC_except_table774
- GCC_except_table784
- GCC_except_table79
- GCC_except_table814
- GCC_except_table82
- GCC_except_table846
- GCC_except_table89
- GCC_except_table91
- GCC_except_table95
- ___104+[UIAccessibilityLoader _performInitialAccessibilityBundleLoad:monitorForFutureLoadEvents:trackingMode:]_block_invoke.212
- ___104+[UIAccessibilityLoader _performInitialAccessibilityBundleLoad:monitorForFutureLoadEvents:trackingMode:]_block_invoke.220
- ___104+[UIAccessibilityLoader _performInitialAccessibilityBundleLoad:monitorForFutureLoadEvents:trackingMode:]_block_invoke.225
- ___104+[UIAccessibilityLoader _performInitialAccessibilityBundleLoad:monitorForFutureLoadEvents:trackingMode:]_block_invoke.232
- ___104+[UIAccessibilityLoader _performInitialAccessibilityBundleLoad:monitorForFutureLoadEvents:trackingMode:]_block_invoke_2.226
- ___146-[NSObject(AXPrivCategory) _accessibilityMoveFocusToNextOpaqueElementForTechnology:direction:searchType:range:shouldScrollToVisible:honorsGroups:]_block_invoke.1139
- ___148-[NSObject(UIAccessibilityAutomation) _accessibilityUserTestingSnapshotAncestorsWithAttributes:maxDepth:maxChildren:maxArrayCount:honorsModalViews:]_block_invoke.324
- ___148-[NSObject(UIAccessibilityAutomation) _accessibilityUserTestingSnapshotAncestorsWithAttributes:maxDepth:maxChildren:maxArrayCount:honorsModalViews:]_block_invoke.324.cold.1
- ___150-[NSObject(UIAccessibilityAutomation) _accessibilityUserTestingSnapshotDescendantsWithAttributes:maxDepth:maxChildren:maxArrayCount:honorsModalViews:]_block_invoke.321
- ___150-[NSObject(UIAccessibilityAutomation) _accessibilityUserTestingSnapshotDescendantsWithAttributes:maxDepth:maxChildren:maxArrayCount:honorsModalViews:]_block_invoke.321.cold.1
- ___150-[NSObject(UIAccessibilityAutomation) _accessibilityUserTestingSnapshotDescendantsWithAttributes:maxDepth:maxChildren:maxArrayCount:honorsModalViews:]_block_invoke.321.cold.2
- ___150-[NSObject(UIAccessibilityAutomation) _accessibilityUserTestingSnapshotDescendantsWithAttributes:maxDepth:maxChildren:maxArrayCount:honorsModalViews:]_block_invoke.321.cold.3
- ___174-[NSObject(AXPrivCategory) _accessibilitySearchSubtreesAfterChildElement:direction:searchType:allowOutOfBoundsChild:range:shouldScrollToVisible:honorGroups:updatedContainer:]_block_invoke.1155
- ___174-[NSObject(AXPrivCategory) _accessibilitySearchSubtreesAfterChildElement:direction:searchType:allowOutOfBoundsChild:range:shouldScrollToVisible:honorGroups:updatedContainer:]_block_invoke.1160
- ___60+[UIAccessibilityLegacyLoader _accessibilityLoadSubbundles:]_block_invoke.301
- ___60+[UIAccessibilityLegacyLoader _accessibilityLoadSubbundles:]_block_invoke_2.302
- ___60-[NSObject(AXPrivCategory) _iosAccessibilityAttributeValue:]_block_invoke.899
- ___60-[NSObject(AXPrivCategory) _iosAccessibilityAttributeValue:]_block_invoke.899.cold.1
- ___63+[UIAccessibilityLegacyLoader loadExtendedAccessibilityBundles]_block_invoke.240
- ___63+[UIAccessibilityLegacyLoader loadExtendedAccessibilityBundles]_block_invoke.242
- ___79-[NSObject(AXPrivCategory) _accessibilityReplaceCharactersAtCursor:withString:]_block_invoke.1520
- ____copyElementAtPositionCallback_block_invoke.218
- ____copyElementAtPositionCallback_block_invoke.232
- ___block_literal_global.1082
- ___block_literal_global.1084
- ___block_literal_global.1120
- ___block_literal_global.1124
- ___block_literal_global.1126
- ___block_literal_global.1130
- ___block_literal_global.1132
- ___block_literal_global.1136
- ___block_literal_global.1138
- ___block_literal_global.1141
- ___block_literal_global.1147
- ___block_literal_global.1151
- ___block_literal_global.1158
- ___block_literal_global.1163
- ___block_literal_global.1179
- ___block_literal_global.1184
- ___block_literal_global.1186
- ___block_literal_global.1188
- ___block_literal_global.1190
- ___block_literal_global.1198
- ___block_literal_global.1283
- ___block_literal_global.1286
- ___block_literal_global.1512
- ___block_literal_global.1514
- ___block_literal_global.1516
- ___block_literal_global.1522
- ___block_literal_global.1580
- ___block_literal_global.1591
- ___block_literal_global.1602
- ___block_literal_global.1614
- ___block_literal_global.1617
- ___block_literal_global.1619
- ___block_literal_global.213
- ___block_literal_global.215
- ___block_literal_global.217
- ___block_literal_global.218
- ___block_literal_global.219
- ___block_literal_global.220
- ___block_literal_global.223
- ___block_literal_global.225
- ___block_literal_global.227
- ___block_literal_global.228
- ___block_literal_global.234
- ___block_literal_global.235
- ___block_literal_global.255
- ___block_literal_global.2666
- ___block_literal_global.274
- ___block_literal_global.278
- ___block_literal_global.283
- ___block_literal_global.284
- ___block_literal_global.2854
- ___block_literal_global.2856
- ___block_literal_global.2858
- ___block_literal_global.286
- ___block_literal_global.2866
- ___block_literal_global.287
- ___block_literal_global.2874
- ___block_literal_global.2877
- ___block_literal_global.2879
- ___block_literal_global.305
- ___block_literal_global.306
- ___block_literal_global.307
- ___block_literal_global.310
- ___block_literal_global.314
- ___block_literal_global.317
- ___block_literal_global.323
- ___block_literal_global.346
- ___block_literal_global.349
- ___block_literal_global.351
- ___block_literal_global.356
- ___block_literal_global.370
- ___block_literal_global.375
- ___block_literal_global.411
- ___block_literal_global.417
- ___block_literal_global.424
- ___block_literal_global.437
- ___block_literal_global.440
- ___block_literal_global.442
- ___block_literal_global.444
- ___block_literal_global.446
- ___block_literal_global.486
- ___block_literal_global.514
- ___block_literal_global.516
- ___block_literal_global.520
- ___block_literal_global.528
- ___block_literal_global.550
- ___block_literal_global.552
- ___block_literal_global.559
- ___block_literal_global.570
- ___block_literal_global.659
- ___block_literal_global.728
- ___block_literal_global.759
- ___block_literal_global.767
- ___block_literal_global.776
- ___block_literal_global.778
- ___block_literal_global.881
- ___block_literal_global.901
- __unnamed_array_storage.1294
- __unnamed_array_storage.1296
- __unnamed_array_storage.1297
- __unnamed_array_storage.325
- __unnamed_array_storage.382
CStrings:
+ "Did not post. Blocking all notifications: %d (%{sensitive}@)"
+ "Safe categories installing on background thread %@"
+ "T@\"NSString\",?,C,N"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",?,R,C,N"
+ "T@\"UIFocusEffect\",?,R,C,N"
+ "T@\"UITextInputPasswordRules\",?,C,N"
+ "T@\"UIView\",?,R,N"
+ "T@\"UIView\",?,R,W,N"
+ "T@,?,R,N"
+ "TB,?,N"
+ "TB,?,N,GisSecureTextEntry"
+ "TB,?,R,N"
+ "Tq,?,N"
+ "Tq,?,R,N"
+ "_accessibilityIsSwitch"
+ "_accessibilityUpdateSafeCategoryThread"
+ "_setAccessibilityShouldUseViewHierarchyForFindingScrollParent:"
+ "accessibilityIsInNonNativeTextControl"
+ "addObserverForName:object:queue:usingBlock:"
+ "caretTransformForPosition:"
+ "mainQueue"
+ "setInstallSafeCategoriesOffMainThread:"
+ "v16@?0@\"NSNotification\"8"
+ "{CGAffineTransform=dddddd}24@0:8@\"UITextPosition\"16"
+ "{CGAffineTransform=dddddd}24@0:8@16"
- "Did not post. Blocking all notifications: %d (%@)"
- "T@\"NSString\",C,N"
- "T@\"UIFocusEffect\",R,C,N"
- "T@\"UITextInputPasswordRules\",C,N"
- "T@\"UIView\",R,N"
- "T@\"UIView\",R,W,N"
- "T@,R,N"
- "TB,N,GisSecureTextEntry"
- "Tq,R,N"

```
