## SpringBoard

> `/System/Library/AccessibilityBundles/SpringBoard.axbundle/SpringBoard`

```diff

-3050.3.5.0.0
-  __TEXT.__text: 0x39144
-  __TEXT.__objc_methlist: 0x4d1c
+3050.3.8.0.0
+  __TEXT.__text: 0x39534
+  __TEXT.__objc_methlist: 0x4d4c
   __TEXT.__dlopen_cstrs: 0x98
-  __TEXT.__const: 0xe0
-  __TEXT.__gcc_except_tab: 0xb40
-  __TEXT.__cstring: 0xa686
-  __TEXT.__oslogstring: 0xa3b
-  __TEXT.__unwind_info: 0x1718
+  __TEXT.__const: 0xe8
+  __TEXT.__gcc_except_tab: 0xb2c
+  __TEXT.__cstring: 0xa3f2
+  __TEXT.__oslogstring: 0xd4d
+  __TEXT.__unwind_info: 0x1728
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xdf0
+  __DATA_CONST.__const: 0xe18
   __DATA_CONST.__objc_classlist: 0x970
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2638
+  __DATA_CONST.__objc_selrefs: 0x2650
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x3d8
   __DATA_CONST.__objc_arraydata: 0x30
   __DATA_CONST.__got: 0x5d0
   __AUTH_CONST.__const: 0x770
-  __AUTH_CONST.__cfstring: 0xbc80
+  __AUTH_CONST.__cfstring: 0xbb40
   __AUTH_CONST.__objc_const: 0xb390
   __AUTH_CONST.__objc_intobj: 0xf0
   __AUTH_CONST.__objc_arrayobj: 0x48

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1619
-  Symbols:   3855
-  CStrings:  1670
+  Functions: 1624
+  Symbols:   3860
+  CStrings:  1674
 
Symbols:
+ -[SBFluidSwitcherItemContainerAccessibility _axSwitcherViewController]
+ -[SBFluidSwitcherViewControllerAccessibility _axAppExposeBundleIdentifier]
+ -[SBFluidSwitcherViewControllerAccessibility _axAppLayoutIsPlaceableInDeck:]
+ -[SBFluidSwitcherViewControllerAccessibility _axReachableAppLayouts]
+ GCC_except_table1123
+ GCC_except_table1143
+ GCC_except_table1150
+ GCC_except_table1154
+ GCC_except_table1158
+ GCC_except_table1161
+ GCC_except_table1165
+ GCC_except_table1321
+ GCC_except_table1328
+ GCC_except_table1332
+ GCC_except_table1359
+ GCC_except_table1368
+ GCC_except_table1371
+ GCC_except_table1390
+ GCC_except_table1396
+ GCC_except_table1398
+ GCC_except_table1407
+ GCC_except_table1413
+ GCC_except_table1424
+ GCC_except_table1426
+ GCC_except_table1550
+ GCC_except_table1604
+ GCC_except_table756
+ GCC_except_table758
+ GCC_except_table779
+ GCC_except_table781
+ GCC_except_table799
+ GCC_except_table821
+ GCC_except_table828
+ GCC_except_table971
+ GCC_except_table973
+ ___68-[SBFluidSwitcherViewControllerAccessibility _axReachableAppLayouts]_block_invoke
+ ___block_descriptor_40_e8_32s_e15_B32?08Q16^B24ls32l8
- GCC_except_table1118
- GCC_except_table1138
- GCC_except_table1145
- GCC_except_table1149
- GCC_except_table1153
- GCC_except_table1156
- GCC_except_table1160
- GCC_except_table1316
- GCC_except_table1323
- GCC_except_table1327
- GCC_except_table1354
- GCC_except_table1358
- GCC_except_table1366
- GCC_except_table1385
- GCC_except_table1391
- GCC_except_table1393
- GCC_except_table1397
- GCC_except_table1408
- GCC_except_table1419
- GCC_except_table1421
- GCC_except_table1545
- GCC_except_table1599
- GCC_except_table755
- GCC_except_table757
- GCC_except_table778
- GCC_except_table780
- GCC_except_table796
- GCC_except_table816
- GCC_except_table823
- GCC_except_table966
- GCC_except_table968
- __AXLogWithFacility
CStrings:
+ "Applying screen curtain change to %d"
+ "Could not check in as: %{public}s"
+ "Lock button: returning SBBacklightActionNone, awake behind screen curtain"
+ "SBVOT: failed to read entitlements for caller (pid=%d): %{public}@"
+ "Screen curtain changed to %d while asleep, applying on next wake"
+ "VoiceOverTouch is back... (%d)"
+ "app.has.multiple.windows"
+ "show.all.shelf.apps"
- "Could not check in as: %s\n"
- "SBVOT: failed to read entitlements for caller (pid=%d): %@"
- "SBVOT: skipping screen curtain apply for enabled=%d because system is sleeping; will not be resynced on wake"
- "VoiceOverTouch is back... (%d)\n"
```
