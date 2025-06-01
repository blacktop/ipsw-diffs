## UIKitCore

> `/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`

```diff

-7209.1.104.0.0
-  __TEXT.__text: 0x130875c
+7303.0.102.0.0
+  __TEXT.__text: 0x13093ec
   __TEXT.__auth_stubs: 0x7760
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x13e6c4
+  __TEXT.__objc_methlist: 0x13e6fc
   __TEXT.__const: 0x13960
   __TEXT.__swift5_typeref: 0x32e0
   __TEXT.__swift5_capture: 0x154c
-  __TEXT.__cstring: 0xc91a7
+  __TEXT.__cstring: 0xc8fa7
   __TEXT.__swift5_reflstr: 0x12b4
   __TEXT.__swift5_assocty: 0xdf8
   __TEXT.__swift5_fieldmd: 0x227c

   __TEXT.__swift5_proto: 0x750
   __TEXT.__swift5_types: 0x3f0
   __TEXT.__swift5_mpenum: 0x44
-  __TEXT.__gcc_except_tab: 0x1a2b4
+  __TEXT.__gcc_except_tab: 0x1a2cc
   __TEXT.__dlopen_cstrs: 0x3bf2
-  __TEXT.__oslogstring: 0x3a2f8
+  __TEXT.__oslogstring: 0x3a4d6
   __TEXT.__ustring: 0x15a0
   __TEXT.__objc_const_ax: 0xa68
-  __TEXT.__unwind_info: 0x510f4
+  __TEXT.__unwind_info: 0x5111c
   __TEXT.__eh_frame: 0xe38
   __TEXT.__objc_classname: 0x2e702
-  __TEXT.__objc_methname: 0x2ae327
+  __TEXT.__objc_methname: 0x2ae371
   __TEXT.__objc_methtype: 0x66fb7
-  __TEXT.__objc_stubs: 0x1aa580
+  __TEXT.__objc_stubs: 0x1aa5c0
   __DATA_CONST.__got: 0x1d80
   __DATA_CONST.__const: 0x364a8
   __DATA_CONST.__objc_classlist: 0x8e30
   __DATA_CONST.__objc_catlist: 0x2f8
   __DATA_CONST.__objc_protolist: 0x25b0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1c15d8
-  __DATA_CONST.__objc_selrefs: 0x80950
+  __DATA_CONST.__objc_const: 0x1c15c8
+  __DATA_CONST.__objc_selrefs: 0x80968
   __DATA_CONST.__objc_arraydata: 0x3570
   __AUTH_CONST.__const: 0x1e3c0
   __AUTH_CONST.__objc_const: 0x69ea8
-  __AUTH_CONST.__cfstring: 0x9c440
+  __AUTH_CONST.__cfstring: 0x9c300
   __AUTH_CONST.__objc_arrayobj: 0x2580
   __AUTH_CONST.__objc_doubleobj: 0xd10
   __AUTH_CONST.__objc_intobj: 0x4770

   __DATA.__objc_protorefs: 0x6d0
   __DATA.__objc_classrefs: 0x8aa0
   __DATA.__objc_superrefs: 0x67c8
-  __DATA.__objc_ivar: 0xeb10
+  __DATA.__objc_ivar: 0xeb18
   __DATA.__objc_const_ax: 0x0
-  __DATA.__data: 0x20180
+  __DATA.__data: 0x20170
   __DATA.__uikit_ip: 0xff0
   __DATA.__crash_info: 0x40
   __DATA.__uikit_ipl: 0x10
   __DATA.__common: 0x2580
-  __DATA.__bss: 0xfd30
-  __DATA_DIRTY.__objc_ivar: 0x8758
+  __DATA.__bss: 0xfd40
+  __DATA_DIRTY.__objc_ivar: 0x874c
   __DATA_DIRTY.__objc_data: 0x249f0
   __DATA_DIRTY.__uikit_ip: 0x518
   __DATA_DIRTY.__data: 0xe50
   __DATA_DIRTY.__common: 0x2b0
-  __DATA_DIRTY.__bss: 0xb620
+  __DATA_DIRTY.__bss: 0xb630
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/Accessibility.framework/Accessibility
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 99AD2A31-9360-369F-9C0B-A7A0AF33E2E7
-  Functions: 130962
-  Symbols:   373195
-  CStrings:  157301
+  UUID: 6398DDD4-EA36-31CD-B849-2F6217205BED
+  Functions: 130969
+  Symbols:   373213
+  CStrings:  157285
 
Symbols:
+ -[UIControl _safeHoverStyle]
+ -[UIKeyboard _isDictationCurrentView]
+ -[UIKeyboard _toggleMenuGestureRecognizer:]
+ -[UIKeyboardImpl(UIKitInternal) setInitialDirectionIgnoreRangeCheck:]
+ -[UIKeyboardLayoutCursor _menuTapShouldStopDictation]
+ -[UISearchBar(ForTVOSOnly) _setHelperPlaceholderOverride:]
+ -[_UIFocusUpdateRequest destinationEnvironment]
+ -[_UIFocusUpdateRequest initWithFocusSystem:environment:destinationEnvironment:]
+ -[_UIKeyboardArbiterClient queue_endInputSessionWithCompletion:]
+ GCC_except_table1616
+ GCC_except_table224
+ _OBJC_IVAR_$_UIKeyboardLayoutStar._keyplaneName
+ _OBJC_IVAR_$_UIKeyboardLayoutStar._pendingDictationReload
+ _OBJC_IVAR_$__UIFocusUpdateRequest._destinationEnvironment
+ ___43-[_UIRemoteKeyboards peekApplicationEvent:]_block_invoke.674
+ ___52+[UIDictationController activeSLSDictationLanguages]_block_invoke.1200
+ ___53-[UIKBRTIPartner inputSession:performInputOperation:]_block_invoke.382
+ ___53-[UIKBRTIPartner inputSession:performInputOperation:]_block_invoke.428
+ ___53-[UIKBRTIPartner inputSession:performInputOperation:]_block_invoke_2.429
+ ___53-[UIKBRTIPartner inputSession:performInputOperation:]_block_invoke_3.440
+ ___54-[UIKBRTIPartner performTextOperations:resultHandler:]_block_invoke.492
+ ___55-[_UIPhysicalButtonInteractionArbiter _handleBSAction:]_block_invoke.218
+ ___58-[UIDictationController _getRangeOfString:inDocumentText:]_block_invoke.889
+ ___64-[_UIKeyboardArbiterClient queue_endInputSessionWithCompletion:]_block_invoke
+ ___65-[UIDictationController _updateLastHypothesis:WithNewHypothesis:]_block_invoke.1015
+ ___block_literal_global.1013
+ ___block_literal_global.1029
+ ___block_literal_global.1036
+ ___block_literal_global.1040
+ ___block_literal_global.1061
+ ___block_literal_global.1124
+ ___block_literal_global.1126
+ ___block_literal_global.1140
+ ___block_literal_global.1194
+ ___block_literal_global.1197
+ ___block_literal_global.1206
+ ___block_literal_global.1209
+ ___block_literal_global.1225
+ ___block_literal_global.1230
+ ___block_literal_global.1461
+ ___block_literal_global.1465
+ ___block_literal_global.1474
+ ___block_literal_global.1517
+ ___block_literal_global.1524
+ ___block_literal_global.1806
+ ___block_literal_global.1867
+ ___block_literal_global.1871
+ ___block_literal_global.3864
+ ___block_literal_global.3881
+ ___block_literal_global.3899
+ ___block_literal_global.488
+ ___block_literal_global.490
+ ___block_literal_global.590
+ ___block_literal_global.603
+ ___block_literal_global.612
+ ___block_literal_global.658
+ ___block_literal_global.661
+ ___block_literal_global.669
+ ___block_literal_global.678
+ ___block_literal_global.682
+ ___block_literal_global.684
+ ___block_literal_global.686
+ ___block_literal_global.707
+ ___block_literal_global.870
+ ___block_literal_global.910
+ ___block_literal_global.917
+ __unnamed_array_storage.1033
+ __unnamed_array_storage.1059
+ __unnamed_array_storage.1069
+ __unnamed_array_storage.1156
+ __unnamed_array_storage.1166
+ __unnamed_array_storage.1173
+ __unnamed_array_storage.1176
+ __unnamed_array_storage.1183
+ __unnamed_array_storage.1186
+ __unnamed_array_storage.1247
+ __unnamed_array_storage.1423
+ __unnamed_array_storage.1424
+ __unnamed_array_storage.1453
+ __unnamed_array_storage.1454
+ __unnamed_array_storage.1470
+ __unnamed_array_storage.1822
+ __unnamed_array_storage.1827
+ __unnamed_array_storage.661
+ __unnamed_array_storage.831
+ _initWithFocusSystem:environment:destinationEnvironment:.__s_category
+ _objc_msgSend$_isDictationCurrentView
+ _objc_msgSend$_menuTapShouldStopDictation
+ _objc_msgSend$_toggleMenuGestureRecognizer:
+ _objc_msgSend$destinationEnvironment
+ _objc_msgSend$setInitialDirectionIgnoreRangeCheck:
- -[UIKeyboard _toggleVariantsMenuGesture:]
- -[UIScrollView _overridingPreferredFocusEnvironment]
- -[UISearchController _updateSearchTextOnDidSelectSuggestion:]
- GCC_except_table1615
- _OBJC_IVAR_$_UISearchController.__updateSearchTextOnDidSelectSuggestion
- __MergedGlobals.43
- ___43-[_UIRemoteKeyboards peekApplicationEvent:]_block_invoke.679
- ___52+[UIDictationController activeSLSDictationLanguages]_block_invoke.1242
- ___53-[UIKBRTIPartner inputSession:performInputOperation:]_block_invoke.381
- ___53-[UIKBRTIPartner inputSession:performInputOperation:]_block_invoke.427
- ___53-[UIKBRTIPartner inputSession:performInputOperation:]_block_invoke_2.428
- ___53-[UIKBRTIPartner inputSession:performInputOperation:]_block_invoke_3.439
- ___54-[UIKBRTIPartner performTextOperations:resultHandler:]_block_invoke.490
- ___55-[_UIPhysicalButtonInteractionArbiter _handleBSAction:]_block_invoke.211
- ___58-[UIDictationController _getRangeOfString:inDocumentText:]_block_invoke.931
- ___65-[UIDictationController _updateLastHypothesis:WithNewHypothesis:]_block_invoke.1057
- ___block_literal_global.1018
- ___block_literal_global.1050
- ___block_literal_global.1066
- ___block_literal_global.1078
- ___block_literal_global.1120
- ___block_literal_global.1136
- ___block_literal_global.1205
- ___block_literal_global.1216
- ___block_literal_global.1221
- ___block_literal_global.1234
- ___block_literal_global.1244
- ___block_literal_global.1298
- ___block_literal_global.1318
- ___block_literal_global.1335
- ___block_literal_global.1503
- ___block_literal_global.1507
- ___block_literal_global.1516
- ___block_literal_global.1559
- ___block_literal_global.1566
- ___block_literal_global.1809
- ___block_literal_global.1870
- ___block_literal_global.1874
- ___block_literal_global.193
- ___block_literal_global.3863
- ___block_literal_global.3880
- ___block_literal_global.3898
- ___block_literal_global.489
- ___block_literal_global.493
- ___block_literal_global.608
- ___block_literal_global.617
- ___block_literal_global.657
- ___block_literal_global.671
- ___block_literal_global.677
- ___block_literal_global.683
- ___block_literal_global.685
- ___block_literal_global.687
- ___block_literal_global.689
- ___block_literal_global.713
- ___block_literal_global.816
- ___block_literal_global.916
- ___block_literal_global.918
- ___block_literal_global.952
- ___block_literal_global.959
- ___viewServiceDidUpdateResolvedPhysicalButtonConfigurations:.__s_category
- __unnamed_array_storage.1064
- __unnamed_array_storage.1074
- __unnamed_array_storage.1075
- __unnamed_array_storage.1198
- __unnamed_array_storage.1208
- __unnamed_array_storage.1215
- __unnamed_array_storage.1218
- __unnamed_array_storage.1225
- __unnamed_array_storage.1228
- __unnamed_array_storage.1289
- __unnamed_array_storage.1465
- __unnamed_array_storage.1466
- __unnamed_array_storage.1495
- __unnamed_array_storage.1496
- __unnamed_array_storage.1512
- __unnamed_array_storage.1825
- __unnamed_array_storage.1830
- __unnamed_array_storage.660
- __unnamed_array_storage.828
- _objc_msgSend$_supportsPushToTalk
- _objc_msgSend$_toggleVariantsMenuGesture:
- _objc_msgSend$assistantIsEnabled
CStrings:
+ "\x01\xf0\xf0\xf0\xf0a\xd1\xf0\xf1\xf0\xf0\xf0a"
+ "%@%@ (%llu)"
+ "%@%llu"
+ "%s: Interaction reuses an existing configuration from another interaction which is unsupported: interaction: %@; uniqueGenerations: %@; arbiter: %@"
+ "Actions for resolved configurations update from service: %{public}@; shouldCreate: %{public}d; shouldDisable: %{public}d; shouldEnable: %{public}d; shouldUpdate: %{public}d"
+ "Cannot request a focus update to destinationEnvironment %@ from non-ancestor environment %@"
+ "Cannot request a focus update to destinationEnvironment %@ from non-ancestor environment %@  This will become an assert in a future version."
+ "Received resolved configurations update from service: self: %{public}@; configurations: %{public}@"
+ "T@\"<UIFocusEnvironment>\",R,W,N,V_destinationEnvironment"
+ "TB,N,S_setUpdateSearchTextOnDidSelectSuggestion:"
+ "_destinationEnvironment"
+ "_isDictationCurrentView"
+ "_isHandlingGeometryChange"
+ "_menuTapShouldStopDictation"
+ "_toggleMenuGestureRecognizer:"
+ "destinationEnvironment"
+ "initWithFocusSystem:environment:destinationEnvironment:"
+ "setInitialDirectionIgnoreRangeCheck:"
+ "\xc1\xf0\xc1D\xf0\x11-\xf0\xf1\x13\x84t\xa5s!!\x11\x11\x11\x16\x12\x11"
- "\x01\xf0\xf0\xf0\xf0a\xd1\xf0\xf1\xf0\xf0\xf0q"
- "%s: Interaction reuses an existing configuration from another interaction which is unsupported: interaction: %@; arbiter: %@"
- "ATV_DICTATION_HOLD_FOR_SIRI"
- "ATV_DICTATION_PRESS_TO_DICTATE"
- "ATV_DICTATION_SEARCH_HELP"
- "ATV_DICTATION_SEARCH_HELP_LANGUAGE"
- "Help text for AppleTV search dictation"
- "Help text for AppleTV search dictation with language"
- "Help text for AppleTV to hold for Siri instead of dictating"
- "Help text for AppleTV to hold to dictate when Siri is disabled"
- "Hold %@ for Siri"
- "Hold %@ to dictate search"
- "Hold %@ to dictate search in %@"
- "Press %@ to dictate"
- "PressToDictateSystemOverlay"
- "Received resolved configurations update from service: self: %@; configurations: %@"
- "TB,N,S_setUpdateSearchTextOnDidSelectSuggestion:,V__updateSearchTextOnDidSelectSuggestion"
- "__updateSearchTextOnDidSelectSuggestion"
- "_shouldStopDictationOnPressUp"
- "_toggleVariantsMenuGesture:"
- "_updateSearchTextOnDidSelectSuggestion:"
- "_variantsMenuGesture"
- "afui_handles_multiple_rti_sessions"
- "assistantIsEnabled"
- "com.apple.TVSystemUIService"
- "\xc1\xf0\xc1D\xf0\x11-\xf0\xf1\x13\x85t\xa5s!!\x11\x11\x11\x16\x12\x11"

```
