## UIKitCore

> `/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`

```diff

-8604.0.0.0.0
-  __TEXT.__text: 0x166cca4
-  __TEXT.__auth_stubs: 0x9d00
+8605.0.0.0.0
+  __TEXT.__text: 0x166b13c
+  __TEXT.__auth_stubs: 0x9cf0
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0x175970
   __TEXT.__const: 0x23710
   __TEXT.__dlopen_cstrs: 0x4509
-  __TEXT.__cstring: 0xe173f
+  __TEXT.__cstring: 0xe16e5
   __TEXT.__swift5_typeref: 0x9f7a
   __TEXT.__swift5_capture: 0x66a4
   __TEXT.__swift5_reflstr: 0x61c7

   __TEXT.__swift5_protos: 0x134
   __TEXT.__swift5_proto: 0xfd4
   __TEXT.__swift5_types: 0xa64
-  __TEXT.__oslogstring: 0x46900
+  __TEXT.__oslogstring: 0x4685f
   __TEXT.__swift_as_entry: 0x168
   __TEXT.__swift_as_ret: 0x124
   __TEXT.__swift5_mpenum: 0xd0
-  __TEXT.__gcc_except_tab: 0x24be0
+  __TEXT.__gcc_except_tab: 0x24bb4
   __TEXT.__ustring: 0x23f0
-  __TEXT.__unwind_info: 0x5b9a8
+  __TEXT.__unwind_info: 0x5b988
   __TEXT.__eh_frame: 0x54ec
   __TEXT.__objc_classname: 0x329fe
   __TEXT.__objc_methname: 0x2e5361

   __DATA_CONST.__objc_selrefs: 0x8aa40
   __DATA_CONST.__objc_protorefs: 0x8e0
   __DATA_CONST.__objc_superrefs: 0x6ed8
-  __DATA_CONST.__objc_arraydata: 0x3fc0
-  __AUTH_CONST.__auth_got: 0x4e98
+  __DATA_CONST.__objc_arraydata: 0x3f98
+  __AUTH_CONST.__auth_got: 0x4e90
   __AUTH_CONST.__const: 0x35570
-  __AUTH_CONST.__cfstring: 0xa7260
+  __AUTH_CONST.__cfstring: 0xa7200
   __AUTH_CONST.__objc_const: 0x22efe0
-  __AUTH_CONST.__objc_arrayobj: 0x2b50
+  __AUTH_CONST.__objc_arrayobj: 0x2b38
   __AUTH_CONST.__objc_doubleobj: 0xfb0
   __AUTH_CONST.__objc_intobj: 0x4d70
   __AUTH_CONST.__objc_dictobj: 0x6e0

   __DATA.__data: 0x265a8
   __DATA.__uikit_ip: 0x7c0
   __DATA.__uikit_ipl: 0x10
-  __DATA.__bss: 0x214b8
+  __DATA.__bss: 0x21360
   __DATA.__common: 0x28b8
   __DATA_DIRTY.__objc_ivar: 0x8b5c
   __DATA_DIRTY.__objc_data: 0x25c78
   __DATA_DIRTY.__uikit_ip: 0xe30
   __DATA_DIRTY.__data: 0x1d10
-  __DATA_DIRTY.__bss: 0xc208
+  __DATA_DIRTY.__bss: 0xc308
   __DATA_DIRTY.__common: 0x2b0
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/Accessibility.framework/Accessibility

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: E8596987-79F2-3F52-9FF6-1AE942174E88
-  Functions: 149510
-  Symbols:   406866
-  CStrings:  169794
+  UUID: 5E794CAA-4162-3FF6-861E-45F29F6B8AC0
+  Functions: 149509
+  Symbols:   406843
+  CStrings:  169786
 
Symbols:
+ ___102-[UIKeyboardSceneDelegate _reloadInputViewsForKeyWindowSceneResponder:force:fromBecomeFirstResponder:]_block_invoke.564
+ ___102-[UIKeyboardSceneDelegate _reloadInputViewsForKeyWindowSceneResponder:force:fromBecomeFirstResponder:]_block_invoke.575
+ ___103-[_UIKeyboardStateManager acceptAutocorrectionWithCompletionHandler:requestedByRemoteInputDestination:]_block_invoke.1398
+ ___37-[_UIRemoteKeyboards startConnection]_block_invoke.428
+ ___37-[_UIRemoteKeyboards startConnection]_block_invoke.430
+ ___38-[UIKeyboardImpl keyboardMenuElements]_block_invoke.283
+ ___38-[UIKeyboardImpl keyboardMenuElements]_block_invoke.294
+ ___43-[_UIRemoteKeyboards peekApplicationEvent:]_block_invoke.715
+ ___44-[_UIRemoteKeyboards applicationDidSuspend:]_block_invoke.632
+ ___45-[_UIRemoteKeyboards queue_failedConnection:]_block_invoke.415
+ ___47-[_UIKeyboardStateManager acceptAutocorrection]_block_invoke.1411
+ ___47-[_UIKeyboardStateManager acceptAutocorrection]_block_invoke.1422
+ ___47-[_UIKeyboardStateManager acceptAutocorrection]_block_invoke_2.1423
+ ___47-[_UIKeyboardStateManager acceptAutocorrection]_block_invoke_3.1426
+ ___47-[_UIKeyboardStateManager acceptAutocorrection]_block_invoke_4.1429
+ ___51-[_UIKeyboardArbiterClient queue_failedConnection:]_block_invoke.143
+ ___58-[_UIKeyboardArbiterClient startConnectionWithCompletion:]_block_invoke.133
+ ___58-[_UIKeyboardStateManager performKeyboardOutput:userInfo:]_block_invoke.1080
+ ___64-[_UIKeyboardStateManager handleKeyboardInput:executionContext:]_block_invoke.1013
+ ___64-[_UIKeyboardStateManager handleKeyboardInput:executionContext:]_block_invoke.966
+ ___70-[UIKeyboardImpl presentKeyboardPopoverWithType:keyString:completion:]_block_invoke.338
+ ___70-[UIKeyboardSceneDelegate setKeyWindowSceneInputViews:animationStyle:]_block_invoke.612
+ ___70-[UIKeyboardSceneDelegate setKeyWindowSceneInputViews:animationStyle:]_block_invoke.617
+ ___77-[UIInputWindowController moveFromPlacement:toPlacement:starting:completion:]_block_invoke.529
+ ___77-[UIInputWindowController moveFromPlacement:toPlacement:starting:completion:]_block_invoke.530
+ ___77-[UIInputWindowController moveFromPlacement:toPlacement:starting:completion:]_block_invoke.535
+ ___77-[UIInputWindowController moveFromPlacement:toPlacement:starting:completion:]_block_invoke.536
+ ___77-[UIInputWindowController moveFromPlacement:toPlacement:starting:completion:]_block_invoke.537
+ ___77-[UIInputWindowController moveFromPlacement:toPlacement:starting:completion:]_block_invoke.557
+ ___77-[UIInputWindowController moveFromPlacement:toPlacement:starting:completion:]_block_invoke_2.534
+ ___77-[UIInputWindowController moveFromPlacement:toPlacement:starting:completion:]_block_invoke_2.553
+ ___77-[UIInputWindowController moveFromPlacement:toPlacement:starting:completion:]_block_invoke_3.554
+ ___94-[_UIRemoteKeyboards didHandleKeyboardChange:shouldConsiderSnapshottingKeyboard:isLocalEvent:]_block_invoke.449
+ ___94-[_UIRemoteKeyboards didHandleKeyboardChange:shouldConsiderSnapshottingKeyboard:isLocalEvent:]_block_invoke.453
+ ___94-[_UIRemoteKeyboards didHandleKeyboardChange:shouldConsiderSnapshottingKeyboard:isLocalEvent:]_block_invoke.459
+ ___94-[_UIRemoteKeyboards didHandleKeyboardChange:shouldConsiderSnapshottingKeyboard:isLocalEvent:]_block_invoke_2.457
+ ___94-[_UIRemoteKeyboards didHandleKeyboardChange:shouldConsiderSnapshottingKeyboard:isLocalEvent:]_block_invoke_2.462
+ ___94-[_UIRemoteKeyboards didHandleKeyboardChange:shouldConsiderSnapshottingKeyboard:isLocalEvent:]_block_invoke_3.458
+ ___94-[_UIRemoteKeyboards didHandleKeyboardChange:shouldConsiderSnapshottingKeyboard:isLocalEvent:]_block_invoke_3.463
+ ___block_literal_global.1006
+ ___block_literal_global.1016
+ ___block_literal_global.1021
+ ___block_literal_global.1035
+ ___block_literal_global.1042
+ ___block_literal_global.1057
+ ___block_literal_global.1064
+ ___block_literal_global.1074
+ ___block_literal_global.1080
+ ___block_literal_global.1097
+ ___block_literal_global.1105
+ ___block_literal_global.1121
+ ___block_literal_global.1125
+ ___block_literal_global.1130
+ ___block_literal_global.1137
+ ___block_literal_global.1141
+ ___block_literal_global.1148
+ ___block_literal_global.1153
+ ___block_literal_global.1201
+ ___block_literal_global.1238
+ ___block_literal_global.1244
+ ___block_literal_global.1265
+ ___block_literal_global.1272
+ ___block_literal_global.1316
+ ___block_literal_global.1322
+ ___block_literal_global.1346
+ ___block_literal_global.1358
+ ___block_literal_global.1369
+ ___block_literal_global.1448
+ ___block_literal_global.1457
+ ___block_literal_global.1460
+ ___block_literal_global.1474
+ ___block_literal_global.1484
+ ___block_literal_global.1489
+ ___block_literal_global.1493
+ ___block_literal_global.1511
+ ___block_literal_global.1527
+ ___block_literal_global.1540
+ ___block_literal_global.1612
+ ___block_literal_global.1644
+ ___block_literal_global.1720
+ ___block_literal_global.1738
+ ___block_literal_global.1749
+ ___block_literal_global.1751
+ ___block_literal_global.1756
+ ___block_literal_global.1758
+ ___block_literal_global.1776
+ ___block_literal_global.1778
+ ___block_literal_global.1788
+ ___block_literal_global.1790
+ ___block_literal_global.1792
+ ___block_literal_global.1794
+ ___block_literal_global.1796
+ ___block_literal_global.1798
+ ___block_literal_global.1800
+ ___block_literal_global.1802
+ ___block_literal_global.1805
+ ___block_literal_global.1807
+ ___block_literal_global.1809
+ ___block_literal_global.1811
+ ___block_literal_global.1813
+ ___block_literal_global.1854
+ ___block_literal_global.1856
+ ___block_literal_global.1858
+ ___block_literal_global.1876
+ ___block_literal_global.1878
+ ___block_literal_global.1880
+ ___block_literal_global.1889
+ ___block_literal_global.1893
+ ___block_literal_global.222
+ ___block_literal_global.2503
+ ___block_literal_global.3696
+ ___block_literal_global.3720
+ ___block_literal_global.376
+ ___block_literal_global.406
+ ___block_literal_global.445
+ ___block_literal_global.524
+ ___block_literal_global.528
+ ___block_literal_global.546
+ ___block_literal_global.564
+ ___block_literal_global.585
+ ___block_literal_global.614
+ ___block_literal_global.615
+ ___block_literal_global.619
+ ___block_literal_global.621
+ ___block_literal_global.623
+ ___block_literal_global.625
+ ___block_literal_global.637
+ ___block_literal_global.707
+ ___block_literal_global.717
+ ___block_literal_global.726
+ ___block_literal_global.728
+ ___block_literal_global.786
+ ___block_literal_global.799
+ ___block_literal_global.862
+ ___block_literal_global.879
+ ___block_literal_global.891
+ ___block_literal_global.896
+ ___block_literal_global.930
+ ___block_literal_global.936
+ ___block_literal_global.943
+ _activeKeyboard
- __MergedGlobals.18
- __MergedGlobals.51
- __UIKBHTVerifyFrameworkDepth
- ___102-[UIKeyboardSceneDelegate _reloadInputViewsForKeyWindowSceneResponder:force:fromBecomeFirstResponder:]_block_invoke.567
- ___102-[UIKeyboardSceneDelegate _reloadInputViewsForKeyWindowSceneResponder:force:fromBecomeFirstResponder:]_block_invoke.578
- ___103-[_UIKeyboardStateManager acceptAutocorrectionWithCompletionHandler:requestedByRemoteInputDestination:]_block_invoke.1400
- ___37-[_UIRemoteKeyboards startConnection]_block_invoke.431
- ___37-[_UIRemoteKeyboards startConnection]_block_invoke.433
- ___38-[UIKeyboardImpl keyboardMenuElements]_block_invoke.286
- ___38-[UIKeyboardImpl keyboardMenuElements]_block_invoke.297
- ___43-[_UIRemoteKeyboards peekApplicationEvent:]_block_invoke.718
- ___44-[_UIRemoteKeyboards applicationDidSuspend:]_block_invoke.635
- ___45-[_UIRemoteKeyboards queue_failedConnection:]_block_invoke.418
- ___47-[_UIKeyboardStateManager acceptAutocorrection]_block_invoke.1413
- ___47-[_UIKeyboardStateManager acceptAutocorrection]_block_invoke.1424
- ___47-[_UIKeyboardStateManager acceptAutocorrection]_block_invoke_2.1425
- ___47-[_UIKeyboardStateManager acceptAutocorrection]_block_invoke_3.1428
- ___47-[_UIKeyboardStateManager acceptAutocorrection]_block_invoke_4.1431
- ___51-[_UIKeyboardArbiterClient queue_failedConnection:]_block_invoke.146
- ___58-[_UIKeyboardArbiterClient startConnectionWithCompletion:]_block_invoke.139
- ___58-[_UIKeyboardStateManager performKeyboardOutput:userInfo:]_block_invoke.1082
- ___64-[_UIKeyboardStateManager handleKeyboardInput:executionContext:]_block_invoke.1015
- ___64-[_UIKeyboardStateManager handleKeyboardInput:executionContext:]_block_invoke.968
- ___70-[UIKeyboardImpl presentKeyboardPopoverWithType:keyString:completion:]_block_invoke.344
- ___70-[UIKeyboardSceneDelegate setKeyWindowSceneInputViews:animationStyle:]_block_invoke.615
- ___70-[UIKeyboardSceneDelegate setKeyWindowSceneInputViews:animationStyle:]_block_invoke.620
- ___77-[UIInputWindowController moveFromPlacement:toPlacement:starting:completion:]_block_invoke.532
- ___77-[UIInputWindowController moveFromPlacement:toPlacement:starting:completion:]_block_invoke.533
- ___77-[UIInputWindowController moveFromPlacement:toPlacement:starting:completion:]_block_invoke.538
- ___77-[UIInputWindowController moveFromPlacement:toPlacement:starting:completion:]_block_invoke.539
- ___77-[UIInputWindowController moveFromPlacement:toPlacement:starting:completion:]_block_invoke.540
- ___77-[UIInputWindowController moveFromPlacement:toPlacement:starting:completion:]_block_invoke.560
- ___77-[UIInputWindowController moveFromPlacement:toPlacement:starting:completion:]_block_invoke_2.537
- ___77-[UIInputWindowController moveFromPlacement:toPlacement:starting:completion:]_block_invoke_2.556
- ___77-[UIInputWindowController moveFromPlacement:toPlacement:starting:completion:]_block_invoke_3.557
- ___94-[_UIRemoteKeyboards didHandleKeyboardChange:shouldConsiderSnapshottingKeyboard:isLocalEvent:]_block_invoke.452
- ___94-[_UIRemoteKeyboards didHandleKeyboardChange:shouldConsiderSnapshottingKeyboard:isLocalEvent:]_block_invoke.456
- ___94-[_UIRemoteKeyboards didHandleKeyboardChange:shouldConsiderSnapshottingKeyboard:isLocalEvent:]_block_invoke.462
- ___94-[_UIRemoteKeyboards didHandleKeyboardChange:shouldConsiderSnapshottingKeyboard:isLocalEvent:]_block_invoke_2.460
- ___94-[_UIRemoteKeyboards didHandleKeyboardChange:shouldConsiderSnapshottingKeyboard:isLocalEvent:]_block_invoke_2.465
- ___94-[_UIRemoteKeyboards didHandleKeyboardChange:shouldConsiderSnapshottingKeyboard:isLocalEvent:]_block_invoke_3.461
- ___94-[_UIRemoteKeyboards didHandleKeyboardChange:shouldConsiderSnapshottingKeyboard:isLocalEvent:]_block_invoke_3.466
- ___block_literal_global.1009
- ___block_literal_global.1020
- ___block_literal_global.1027
- ___block_literal_global.1037
- ___block_literal_global.1055
- ___block_literal_global.1066
- ___block_literal_global.1076
- ___block_literal_global.1083
- ___block_literal_global.1100
- ___block_literal_global.1101
- ___block_literal_global.1109
- ___block_literal_global.1116
- ___block_literal_global.1124
- ___block_literal_global.1129
- ___block_literal_global.1135
- ___block_literal_global.1146
- ___block_literal_global.1160
- ___block_literal_global.1269
- ___block_literal_global.1302
- ___block_literal_global.1345
- ___block_literal_global.1350
- ___block_literal_global.1366
- ___block_literal_global.1373
- ___block_literal_global.1391
- ___block_literal_global.1412
- ___block_literal_global.1423
- ___block_literal_global.1427
- ___block_literal_global.1430
- ___block_literal_global.1433
- ___block_literal_global.1456
- ___block_literal_global.1462
- ___block_literal_global.1469
- ___block_literal_global.1481
- ___block_literal_global.1486
- ___block_literal_global.1492
- ___block_literal_global.1509
- ___block_literal_global.1523
- ___block_literal_global.1531
- ___block_literal_global.1544
- ___block_literal_global.1616
- ___block_literal_global.1648
- ___block_literal_global.1742
- ___block_literal_global.1752
- ___block_literal_global.1757
- ___block_literal_global.1759
- ___block_literal_global.1777
- ___block_literal_global.1779
- ___block_literal_global.1789
- ___block_literal_global.1791
- ___block_literal_global.1793
- ___block_literal_global.1795
- ___block_literal_global.1797
- ___block_literal_global.1799
- ___block_literal_global.1801
- ___block_literal_global.1803
- ___block_literal_global.1806
- ___block_literal_global.1808
- ___block_literal_global.1810
- ___block_literal_global.1812
- ___block_literal_global.1814
- ___block_literal_global.1853
- ___block_literal_global.1855
- ___block_literal_global.1857
- ___block_literal_global.1859
- ___block_literal_global.1877
- ___block_literal_global.1881
- ___block_literal_global.1883
- ___block_literal_global.1890
- ___block_literal_global.1892
- ___block_literal_global.1896
- ___block_literal_global.2505
- ___block_literal_global.3697
- ___block_literal_global.3721
- ___block_literal_global.443
- ___block_literal_global.459
- ___block_literal_global.464
- ___block_literal_global.549
- ___block_literal_global.561
- ___block_literal_global.567
- ___block_literal_global.583
- ___block_literal_global.610
- ___block_literal_global.617
- ___block_literal_global.618
- ___block_literal_global.622
- ___block_literal_global.624
- ___block_literal_global.626
- ___block_literal_global.628
- ___block_literal_global.639
- ___block_literal_global.640
- ___block_literal_global.652
- ___block_literal_global.716
- ___block_literal_global.720
- ___block_literal_global.722
- ___block_literal_global.727
- ___block_literal_global.729
- ___block_literal_global.731
- ___block_literal_global.788
- ___block_literal_global.801
- ___block_literal_global.866
- ___block_literal_global.895
- ___block_literal_global.900
- ___block_literal_global.928
- ___block_literal_global.934
- ___block_literal_global.940
- ___block_literal_global.945
- __verifyClient.didReport
- _acceptAutocorrection._UIKBHT_hit
- _activeKeyboardSceneDelegate._UIKBHT_hit
- _addSubview:._UIKBHT_hit
- _autocorrectionController._UIKBHT_hit
- _candidateController._UIKBHT_hit
- _candidateViewController._UIKBHT_hit
- _compatibilityViewController._UIKBHT_hit
- _inlineTextCompletionController._UIKBHT_hit
- _inputManager._UIKBHT_hit
- _predictionViewController._UIKBHT_hit
- _predictiveViewController._UIKBHT_hit
- _remoteKeyboardWindowForScreen:create:._UIKBHT_hit
- _remoteTextInputPartner._UIKBHT_hit
- _rootViewController._UIKBHT_hit
- _sharedInstance._UIKBHT_hit
- _thread_stack_pcs
- _window._UIKBHT_hit
CStrings:
+ "FeedbackFCSBehavior"
- "%{public}@ Called into an unapproved SPI."
- "Unknown UIKeyboardViewController client (bundleID=%@)"
- "Verify UIKeyboardViewController client (bundleID=%@, isKnown=%s)"
- "com.apple.ContactsUI.MonogramPosterExtension"
- "com.apple.QuickboardViewService"
- "keyboard_spi_caller_verification"

```
