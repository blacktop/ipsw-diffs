## SpringBoard

> `/System/Library/AccessibilityBundles/SpringBoard.axbundle/SpringBoard`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__DATA.__data`

```diff

-3042.0.0.0.0
-  __TEXT.__text: 0x3a1f0
-  __TEXT.__objc_methlist: 0x4e7c
+3045.0.0.0.0
+  __TEXT.__text: 0x399c4
+  __TEXT.__objc_methlist: 0x4d94
   __TEXT.__dlopen_cstrs: 0x98
   __TEXT.__const: 0xc8
-  __TEXT.__gcc_except_tab: 0xa34
-  __TEXT.__cstring: 0xaa04
+  __TEXT.__gcc_except_tab: 0xa6c
+  __TEXT.__cstring: 0xa83c
   __TEXT.__oslogstring: 0x72a
-  __TEXT.__unwind_info: 0x1348
+  __TEXT.__unwind_info: 0x1328
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xe18
-  __DATA_CONST.__objc_classlist: 0x9c0
+  __DATA_CONST.__const: 0xdf0
+  __DATA_CONST.__objc_classlist: 0x9a0
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x25d8
+  __DATA_CONST.__objc_selrefs: 0x25d0
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x3f8
+  __DATA_CONST.__objc_superrefs: 0x3e8
   __DATA_CONST.__objc_arraydata: 0x30
-  __DATA_CONST.__got: 0x5e0
-  __AUTH_CONST.__const: 0x7f0
-  __AUTH_CONST.__cfstring: 0xbf20
-  __AUTH_CONST.__objc_const: 0xb930
+  __DATA_CONST.__got: 0x5d8
+  __AUTH_CONST.__const: 0x7d0
+  __AUTH_CONST.__cfstring: 0xbde0
+  __AUTH_CONST.__objc_const: 0xb6f0
   __AUTH_CONST.__objc_intobj: 0xf0
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__auth_got: 0x0

   __DATA.__data: 0x248
   __DATA.__common: 0x11
   __DATA.__bss: 0xe0
-  __DATA_DIRTY.__objc_data: 0x5550
+  __DATA_DIRTY.__objc_data: 0x5410
   __DATA_DIRTY.__data: 0x4
   __DATA_DIRTY.__bss: 0xb8
   - /System/Library/Frameworks/Accessibility.framework/Accessibility

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1632
-  Symbols:   4797
-  CStrings:  1685
+  Functions: 1615
+  Symbols:   4763
+  CStrings:  1674
 
Symbols:
+ -[SBFloatingDockControllerAccessibility presentFloatingDockIfDismissedAnimated:presentationSource:completionHandler:]
+ -[SBFloatingDockWindowAccessibility _accessibilityWindowVisible]
+ -[SBFloatingDockWindowAccessibility accessibilityElementsHidden]
+ -[SBFluidSwitcherViewControllerAccessibility _axDeferredElementCreationTimer]
+ -[SBFluidSwitcherViewControllerAccessibility _axElementCreationTimer]
+ -[SBFluidSwitcherViewControllerAccessibility _setAXElementCreationTimer:]
+ -[SBHomeScreenWindowAccessibility _accessibilityIsHomeScreenVisible]
+ GCC_except_table1139
+ GCC_except_table1159
+ GCC_except_table1166
+ GCC_except_table1170
+ GCC_except_table1173
+ GCC_except_table1330
+ GCC_except_table1357
+ GCC_except_table1362
+ GCC_except_table1367
+ GCC_except_table1386
+ GCC_except_table1392
+ GCC_except_table1394
+ GCC_except_table1402
+ GCC_except_table1408
+ GCC_except_table1420
+ GCC_except_table1422
+ GCC_except_table1545
+ GCC_except_table1599
+ GCC_except_table211
+ GCC_except_table232
+ GCC_except_table259
+ GCC_except_table263
+ GCC_except_table289
+ GCC_except_table314
+ GCC_except_table319
+ GCC_except_table322
+ GCC_except_table383
+ GCC_except_table395
+ GCC_except_table438
+ GCC_except_table544
+ GCC_except_table579
+ GCC_except_table606
+ GCC_except_table612
+ GCC_except_table613
+ GCC_except_table617
+ GCC_except_table716
+ GCC_except_table722
+ GCC_except_table723
+ GCC_except_table725
+ GCC_except_table727
+ GCC_except_table747
+ GCC_except_table748
+ GCC_except_table752
+ GCC_except_table754
+ GCC_except_table775
+ GCC_except_table777
+ GCC_except_table793
+ GCC_except_table813
+ GCC_except_table820
+ GCC_except_table962
+ GCC_except_table964
+ ___117-[SBFloatingDockControllerAccessibility presentFloatingDockIfDismissedAnimated:presentationSource:completionHandler:]_block_invoke
+ ___95-[SBFluidSwitcherViewControllerAccessibility performTransitionWithContext:animated:completion:]_block_invoke_3
+ ___SBFluidSwitcherViewControllerAccessibility___axElementCreationTimer
+ _objc_msgSend$_accessibilityIsHomeScreenVisible
+ _objc_msgSend$_axDeferredElementCreationTimer
+ _objc_msgSend$_axElementCreationTimer
+ _objc_msgSend$_setAXElementCreationTimer:
+ _objc_msgSend$cancel
+ _objc_msgSend$isPending
+ _objc_msgSend$liveRecognitionOverlayOpen
- +[SBMedusaDecoratedDeviceApplicationSceneViewControllerAccessibility _accessibilityPerformValidations:]
- +[SBMedusaDecoratedDeviceApplicationSceneViewControllerAccessibility(SafeCategory) safeCategoryBaseClass]
- +[SBMedusaDecoratedDeviceApplicationSceneViewControllerAccessibility(SafeCategory) safeCategoryTargetClassName]
- +[SBTopAffordanceDotsViewAccessibility _accessibilityPerformValidations:]
- +[SBTopAffordanceDotsViewAccessibility(SafeCategory) safeCategoryBaseClass]
- +[SBTopAffordanceDotsViewAccessibility(SafeCategory) safeCategoryTargetClassName]
- -[SBFloatingDockControllerAccessibility presentFloatingDockIfDismissedAnimated:completionHandler:]
- -[SBMedusaDecoratedDeviceApplicationSceneViewControllerAccessibility _accessibilityLoadAccessibilityInformation]
- -[SBMedusaDecoratedDeviceApplicationSceneViewControllerAccessibility _axSetUpAffordanceViewController]
- -[SBMedusaDecoratedDeviceApplicationSceneViewControllerAccessibility initWithDeviceApplicationSceneHandle:layoutRole:]
- -[SBMedusaDecoratedDeviceApplicationSceneViewControllerAccessibility viewDidAppear:]
- -[SBTopAffordanceDotsViewAccessibility _accessibilityIsNonDismissableStatusBarElement]
- -[SBTopAffordanceDotsViewAccessibility _accessibilityRoleDescription]
- -[SBTopAffordanceDotsViewAccessibility _axApplicationDisplayName]
- -[SBTopAffordanceDotsViewAccessibility _axMainSwitcher]
- -[SBTopAffordanceDotsViewAccessibility _axSetApplicationDisplayName:]
- -[SBTopAffordanceDotsViewAccessibility accessibilityCustomActions]
- -[SBTopAffordanceDotsViewAccessibility accessibilityHint]
- -[SBTopAffordanceDotsViewAccessibility accessibilityLabel]
- -[SBTopAffordanceDotsViewAccessibility accessibilityTraits]
- -[SBTopAffordanceDotsViewAccessibility axBounds]
- -[SBTopAffordanceDotsViewAccessibility isAccessibilityElement]
- GCC_except_table1156
- GCC_except_table1176
- GCC_except_table1183
- GCC_except_table1187
- GCC_except_table1190
- GCC_except_table1347
- GCC_except_table1374
- GCC_except_table1379
- GCC_except_table1384
- GCC_except_table1403
- GCC_except_table1409
- GCC_except_table1411
- GCC_except_table1419
- GCC_except_table1425
- GCC_except_table1437
- GCC_except_table1439
- GCC_except_table1562
- GCC_except_table1616
- GCC_except_table228
- GCC_except_table249
- GCC_except_table276
- GCC_except_table280
- GCC_except_table306
- GCC_except_table331
- GCC_except_table336
- GCC_except_table339
- GCC_except_table400
- GCC_except_table412
- GCC_except_table455
- GCC_except_table561
- GCC_except_table596
- GCC_except_table623
- GCC_except_table629
- GCC_except_table630
- GCC_except_table634
- GCC_except_table731
- GCC_except_table737
- GCC_except_table738
- GCC_except_table742
- GCC_except_table755
- GCC_except_table762
- GCC_except_table763
- GCC_except_table767
- GCC_except_table769
- GCC_except_table790
- GCC_except_table792
- GCC_except_table808
- GCC_except_table833
- GCC_except_table972
- GCC_except_table974
- _OBJC_CLASS_$_SBMedusaDecoratedDeviceApplicationSceneViewControllerAccessibility
- _OBJC_CLASS_$_SBTopAffordanceDotsViewAccessibility
- _OBJC_CLASS_$___SBMedusaDecoratedDeviceApplicationSceneViewControllerAccessibility_super
- _OBJC_CLASS_$___SBTopAffordanceDotsViewAccessibility_super
- _OBJC_METACLASS_$_SBMedusaDecoratedDeviceApplicationSceneViewControllerAccessibility
- _OBJC_METACLASS_$_SBTopAffordanceDotsViewAccessibility
- _OBJC_METACLASS_$___SBMedusaDecoratedDeviceApplicationSceneViewControllerAccessibility_super
- _OBJC_METACLASS_$___SBTopAffordanceDotsViewAccessibility_super
- __OBJC_$_CLASS_METHODS_SBMedusaDecoratedDeviceApplicationSceneViewControllerAccessibility(SafeCategory)
- __OBJC_$_CLASS_METHODS_SBTopAffordanceDotsViewAccessibility(SafeCategory)
- __OBJC_$_INSTANCE_METHODS_SBMedusaDecoratedDeviceApplicationSceneViewControllerAccessibility
- __OBJC_$_INSTANCE_METHODS_SBTopAffordanceDotsViewAccessibility
- __OBJC_CLASS_RO_$_SBMedusaDecoratedDeviceApplicationSceneViewControllerAccessibility
- __OBJC_CLASS_RO_$_SBTopAffordanceDotsViewAccessibility
- __OBJC_CLASS_RO_$___SBMedusaDecoratedDeviceApplicationSceneViewControllerAccessibility_super
- __OBJC_CLASS_RO_$___SBTopAffordanceDotsViewAccessibility_super
- __OBJC_METACLASS_RO_$_SBMedusaDecoratedDeviceApplicationSceneViewControllerAccessibility
- __OBJC_METACLASS_RO_$_SBTopAffordanceDotsViewAccessibility
- __OBJC_METACLASS_RO_$___SBMedusaDecoratedDeviceApplicationSceneViewControllerAccessibility_super
- __OBJC_METACLASS_RO_$___SBTopAffordanceDotsViewAccessibility_super
- ___66-[SBTopAffordanceDotsViewAccessibility accessibilityCustomActions]_block_invoke
- ___66-[SBTopAffordanceDotsViewAccessibility accessibilityCustomActions]_block_invoke_2
- ___69-[SBTopAffordanceDotsViewAccessibility _accessibilityRoleDescription]_block_invoke
- ___98-[SBFloatingDockControllerAccessibility presentFloatingDockIfDismissedAnimated:completionHandler:]_block_invoke
- ___SBTopAffordanceDotsViewAccessibility___axApplicationDisplayName
- ___block_descriptor_40_e8_32s_e37_B16?0"UIAccessibilityCustomAction"8ls32l8
- _objc_msgSend$_axApplicationDisplayName
- _objc_msgSend$_axSetApplicationDisplayName:
- _objc_msgSend$_axSetUpAffordanceViewController
- _objc_msgSend$continuousExposeStripTongueViewTapped:
CStrings:
+ "SBScreenSleepCoordinator"
+ "conferenceManager"
+ "presentFloatingDockIfDismissedAnimated:presentationSource:completionHandler:"
+ "screenSleepCoordinator"
+ "wallpaperController"
- "SBDefaultImplementationsSwitcherModifier"
- "SBMedusaDecoratedDeviceApplicationSceneViewControllerAccessibility"
- "SBSceneHostingDisplayControllerProvider"
- "SBTopAffordanceDotsViewAccessibility"
- "_deviceApplicationSceneHandle"
- "_deviceApplicationSceneHandle.application"
- "_extendedDisplayControllerProvider"
- "_topAffordanceViewController"
- "continuousExposeStripTongueViewTapped:"
- "initWithDeviceApplicationSceneHandle:layoutRole:"
- "isContinuousExposeStripVisible"
- "presentFloatingDockIfDismissedAnimated:completionHandler:"
- "stage.manager.app.strip.custom.action.label"
- "top.affordance.button"
- "top.affordance.button.hint"
- "topAffordanceViewController"
```
