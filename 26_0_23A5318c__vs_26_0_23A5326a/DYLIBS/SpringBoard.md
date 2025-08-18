## SpringBoard

> `/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`

```diff

-4557.0.10.106.0
-  __TEXT.__text: 0xa85294
+4557.0.10.111.0
+  __TEXT.__text: 0xa85708
   __TEXT.__auth_stubs: 0x5530
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0xb7a20
-  __TEXT.__const: 0x12cd0
-  __TEXT.__oslogstring: 0x5e455
+  __TEXT.__objc_methlist: 0xb7a48
+  __TEXT.__const: 0x12cf0
+  __TEXT.__oslogstring: 0x5e502
   __TEXT.__cstring: 0x7cdcb
-  __TEXT.__gcc_except_tab: 0x17890
+  __TEXT.__gcc_except_tab: 0x17898
   __TEXT.__ustring: 0xcac
   __TEXT.__dlopen_cstrs: 0x313
   __TEXT.__unwind_info: 0x2c0e8
   __TEXT.__eh_frame: 0xb8
   __TEXT.__objc_classname: 0x220c0
-  __TEXT.__objc_methname: 0x1ced6a
+  __TEXT.__objc_methname: 0x1ceda5
   __TEXT.__objc_methtype: 0x4c859
-  __TEXT.__objc_stubs: 0xf38a0
+  __TEXT.__objc_stubs: 0xf38e0
   __DATA_CONST.__got: 0xa120
   __DATA_CONST.__const: 0x1cca8
   __DATA_CONST.__objc_classlist: 0x5238

   __DATA_CONST.__objc_nlcatlist: 0x8
   __DATA_CONST.__objc_protolist: 0x2928
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4a8f0
+  __DATA_CONST.__objc_selrefs: 0x4a900
   __DATA_CONST.__objc_protorefs: 0xb0
   __DATA_CONST.__objc_superrefs: 0x3f70
   __DATA_CONST.__objc_arraydata: 0x1850
   __AUTH_CONST.__auth_got: 0x2ab0
-  __AUTH_CONST.__const: 0x10958
+  __AUTH_CONST.__const: 0x10978
   __AUTH_CONST.__cfstring: 0x6ee00
-  __AUTH_CONST.__objc_const: 0x2691e0
+  __AUTH_CONST.__objc_const: 0x269308
   __AUTH_CONST.__objc_arrayobj: 0x1770
   __AUTH_CONST.__objc_doubleobj: 0x680
   __AUTH_CONST.__objc_intobj: 0x2bc8

   - /usr/lib/libsp.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libutil.dylib
-  UUID: 125455D2-E42B-3BE0-AD84-4ACF04907FFC
-  Functions: 70023
-  Symbols:   236758
-  CStrings:  104059
+  UUID: 29240BCF-63FC-34A5-A4A3-F4DE3DF56786
+  Functions: 70029
+  Symbols:   236776
+  CStrings:  104062
 
Symbols:
+ -[SBDeviceApplicationSceneHandle prefersClosingInSwitcherDisabled]
+ -[SBInCallPresentationManager isSceneHandleCloseableInSwitcher:]
+ -[SBInCallPresentationSession _updateActiveAppearance]
+ -[SBInCallPresentationSession assistantDidDisappear:windowScene:]
+ -[SBInCallPresentationSession isCloseableInSwitcher]
+ GCC_except_table196
+ GCC_except_table243
+ GCC_except_table323
+ GCC_except_table92
+ ___101-[SBInCallPresentationSession dismissAndFinalizeSceneDestructionAnimated:analyticsSource:completion:]_block_invoke.189
+ ___108-[SBMainSwitcherControllerCoordinator switcherContentController:reopenHiddenAppLayoutsWithBundleIdentifier:]_block_invoke.315
+ ___108-[SBMainSwitcherControllerCoordinator switcherContentController:reopenHiddenAppLayoutsWithBundleIdentifier:]_block_invoke_2.316
+ ___108-[SBMainSwitcherControllerCoordinator switcherContentController:reopenHiddenAppLayoutsWithBundleIdentifier:]_block_invoke_3.317
+ ___110-[SBInCallPresentationSession _updateVisibilityInSwitcherForPrefersHiddenWhenDismissedIfNeededForLayoutState:]_block_invoke.245
+ ___110-[SBMainSwitcherControllerCoordinator layoutStateTransitionCoordinator:transitionDidEndWithTransitionContext:]_block_invoke.197
+ ___111-[SBCoverSheetPresentationManager _setTransitionProgress:animated:gestureActive:coverSheetProgress:completion:]_block_invoke_4
+ ___111-[SBCoverSheetPresentationManager _setTransitionProgress:animated:gestureActive:coverSheetProgress:completion:]_block_invoke_5
+ ___111-[SBCoverSheetPresentationManager _setTransitionProgress:animated:gestureActive:coverSheetProgress:completion:]_block_invoke_6
+ ___121-[SBInCallPresentationSession _performSwitcherDismissalTransitionAnimated:shouldDestroyScene:analyticsSource:completion:]_block_invoke.174
+ ___121-[SBInCallPresentationSession _performSwitcherDismissalTransitionAnimated:shouldDestroyScene:analyticsSource:completion:]_block_invoke_2.175
+ ___133-[SBInCallPresentationSession _performPresentationWithRequestedPresentationMode:isUserInitiated:animated:analyticsSource:completion:]_block_invoke.183
+ ___47-[SBLockScreenManager handleTransitionRequest:]_block_invoke_2
+ ___54-[SBLockScreenManager unlockUIFromSource:withOptions:]_block_invoke.382
+ ___54-[SBLockScreenManager unlockUIFromSource:withOptions:]_block_invoke.385
+ ___54-[SBLockScreenManager unlockUIFromSource:withOptions:]_block_invoke_2.384
+ ___64-[SBInCallPresentationManager isSceneHandleCloseableInSwitcher:]_block_invoke
+ ___72-[SBLockScreenManager _finishUIUnlockFromSource:withOptions:completion:]_block_invoke.391
+ ___73-[SBInCallPresentationSession _performSceneUpdateTransactionWithContext:]_block_invoke.222
+ ___73-[SBInCallPresentationSession _performSceneUpdateTransactionWithContext:]_block_invoke_2.223
+ ___75-[SBLockScreenManager _unlockWithRequest:cancelPendingRequests:completion:]_block_invoke.413
+ ___81-[SBLockScreenManager _attemptUnlockWithPasscode:mesa:finishUIUnlock:completion:]_block_invoke.443
+ ___86-[SBMainSwitcherControllerCoordinator _performSceneDestructionForModelRemovalResults:]_block_invoke.373
+ ___86-[SBMainSwitcherControllerCoordinator _performSceneDestructionForModelRemovalResults:]_block_invoke_2.374
+ ___97-[SBLockScreenManager _setPasscodeVisible:animated:ignoringPreflightRequirementsForPresentation:]_block_invoke.394
+ ___block_literal_global.185
+ ___block_literal_global.237
+ ___block_literal_global.251
+ ___block_literal_global.299
+ ___block_literal_global.332
+ ___block_literal_global.338
+ ___block_literal_global.348
+ ___block_literal_global.350
+ ___block_literal_global.359
+ ___block_literal_global.366
+ ___block_literal_global.377
+ ___block_literal_global.489
+ _objc_msgSend$_updateActiveAppearance
+ _objc_msgSend$isCloseableInSwitcher
+ _objc_msgSend$isSceneHandleCloseableInSwitcher:
+ _objc_msgSend$prefersClosingInSwitcherDisabled
- -[SBInCallPresentationManager isSceneHandleKillableInSwitcher:]
- -[SBInCallPresentationSession isKillableInSwitcher]
- -[SBMainSwitcherControllerCoordinator layoutStateTransitionCoordinator:transitionDidEndWithTransitionContext:].cold.1
- GCC_except_table241
- GCC_except_table249
- GCC_except_table255
- GCC_except_table94
- GCC_except_table96
- ___101-[SBInCallPresentationSession dismissAndFinalizeSceneDestructionAnimated:analyticsSource:completion:]_block_invoke.188
- ___108-[SBMainSwitcherControllerCoordinator switcherContentController:reopenHiddenAppLayoutsWithBundleIdentifier:]_block_invoke.314
- ___108-[SBMainSwitcherControllerCoordinator switcherContentController:reopenHiddenAppLayoutsWithBundleIdentifier:]_block_invoke_2.315
- ___108-[SBMainSwitcherControllerCoordinator switcherContentController:reopenHiddenAppLayoutsWithBundleIdentifier:]_block_invoke_3.316
- ___110-[SBInCallPresentationSession _updateVisibilityInSwitcherForPrefersHiddenWhenDismissedIfNeededForLayoutState:]_block_invoke.244
- ___110-[SBMainSwitcherControllerCoordinator layoutStateTransitionCoordinator:transitionDidEndWithTransitionContext:]_block_invoke_4
- ___121-[SBInCallPresentationSession _performSwitcherDismissalTransitionAnimated:shouldDestroyScene:analyticsSource:completion:]_block_invoke.173
- ___121-[SBInCallPresentationSession _performSwitcherDismissalTransitionAnimated:shouldDestroyScene:analyticsSource:completion:]_block_invoke_2.174
- ___133-[SBInCallPresentationSession _performPresentationWithRequestedPresentationMode:isUserInitiated:animated:analyticsSource:completion:]_block_invoke.181
- ___54-[SBLockScreenManager unlockUIFromSource:withOptions:]_block_invoke.380
- ___54-[SBLockScreenManager unlockUIFromSource:withOptions:]_block_invoke.383
- ___54-[SBLockScreenManager unlockUIFromSource:withOptions:]_block_invoke_2.382
- ___63-[SBInCallPresentationManager isSceneHandleKillableInSwitcher:]_block_invoke
- ___72-[SBLockScreenManager _finishUIUnlockFromSource:withOptions:completion:]_block_invoke.389
- ___73-[SBInCallPresentationSession _performSceneUpdateTransactionWithContext:]_block_invoke.221
- ___73-[SBInCallPresentationSession _performSceneUpdateTransactionWithContext:]_block_invoke_2.222
- ___75-[SBLockScreenManager _unlockWithRequest:cancelPendingRequests:completion:]_block_invoke.411
- ___81-[SBLockScreenManager _attemptUnlockWithPasscode:mesa:finishUIUnlock:completion:]_block_invoke.441
- ___86-[SBMainSwitcherControllerCoordinator _performSceneDestructionForModelRemovalResults:]_block_invoke.372
- ___86-[SBMainSwitcherControllerCoordinator _performSceneDestructionForModelRemovalResults:]_block_invoke_2.373
- ___97-[SBLockScreenManager _setPasscodeVisible:animated:ignoringPreflightRequirementsForPresentation:]_block_invoke.392
- ___block_literal_global.129
- ___block_literal_global.165
- ___block_literal_global.219
- ___block_literal_global.255
- ___block_literal_global.287
- ___block_literal_global.291
- ___block_literal_global.297
- ___block_literal_global.347
- ___block_literal_global.360
- ___block_literal_global.363
- ___block_literal_global.365
- ___block_literal_global.368
- ___block_literal_global.375
- ___block_literal_global.487
- _objc_msgSend$isKillableInSwitcher
- _objc_msgSend$isSceneHandleKillableInSwitcher:
CStrings:
+ "The appLayouts array doesn't contain %{public}@, was transitioning from %{public}@ with source %lu, items crossing to other displays was %{public}@, number of switchers %lu"
+ "_updateActiveAppearance"
+ "isCloseableInSwitcher"
+ "isSceneHandleCloseableInSwitcher:"
+ "prefersClosingInSwitcherDisabled"
- "isKillableInSwitcher"
- "isSceneHandleKillableInSwitcher:"

```
