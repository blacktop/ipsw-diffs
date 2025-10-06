## SpringBoardFoundation

> `/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`

```diff

-4557.1.8.105.0
-  __TEXT.__text: 0xb543c
+4557.1.15.102.0
+  __TEXT.__text: 0xb6ca4
   __TEXT.__auth_stubs: 0x1a00
-  __TEXT.__objc_methlist: 0x8064
+  __TEXT.__objc_methlist: 0x8144
   __TEXT.__const: 0x2350
-  __TEXT.__cstring: 0xde6c
-  __TEXT.__gcc_except_tab: 0x7c8
+  __TEXT.__cstring: 0xe152
+  __TEXT.__gcc_except_tab: 0x7b0
   __TEXT.__dlopen_cstrs: 0x4d2
-  __TEXT.__oslogstring: 0x2fc6
-  __TEXT.__ustring: 0x2e4
-  __TEXT.__unwind_info: 0x2290
-  __TEXT.__objc_classname: 0x1a1a
-  __TEXT.__objc_methname: 0x198f5
-  __TEXT.__objc_methtype: 0x33bd
-  __TEXT.__objc_stubs: 0xe400
-  __DATA_CONST.__got: 0xc18
-  __DATA_CONST.__const: 0x1978
+  __TEXT.__oslogstring: 0x302b
+  __TEXT.__ustring: 0x2ea
+  __TEXT.__unwind_info: 0x22a0
+  __TEXT.__objc_classname: 0x1a1d
+  __TEXT.__objc_methname: 0x19c72
+  __TEXT.__objc_methtype: 0x33f5
+  __TEXT.__objc_stubs: 0xe540
+  __DATA_CONST.__got: 0xc28
+  __DATA_CONST.__const: 0x19a8
   __DATA_CONST.__objc_classlist: 0x600
   __DATA_CONST.__objc_catlist: 0x70
   __DATA_CONST.__objc_protolist: 0x1b8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4ff0
+  __DATA_CONST.__objc_selrefs: 0x5050
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x348
   __DATA_CONST.__objc_arraydata: 0x508
   __AUTH_CONST.__auth_got: 0xd10
   __AUTH_CONST.__const: 0xd20
-  __AUTH_CONST.__cfstring: 0xb4a0
-  __AUTH_CONST.__objc_const: 0x19f60
+  __AUTH_CONST.__cfstring: 0xb8c0
+  __AUTH_CONST.__objc_const: 0x1a0e8
   __AUTH_CONST.__objc_intobj: 0x570
   __AUTH_CONST.__objc_arrayobj: 0x240
   __AUTH_CONST.__objc_doubleobj: 0x500
   __AUTH.__objc_data: 0x37a0
-  __DATA.__objc_ivar: 0x9f0
+  __DATA.__objc_ivar: 0xa08
   __DATA.__data: 0x14ca
   __DATA.__bss: 0x870
   __DATA_DIRTY.__objc_data: 0x460

   - /System/Library/PrivateFrameworks/MaterialKit.framework/MaterialKit
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/MobileObliteration.framework/MobileObliteration
+  - /System/Library/PrivateFrameworks/MobileStoreDemoKit.framework/MobileStoreDemoKit
   - /System/Library/PrivateFrameworks/PaperBoardUI.framework/PaperBoardUI
   - /System/Library/PrivateFrameworks/PersistentConnection.framework/PersistentConnection
   - /System/Library/PrivateFrameworks/PrototypeTools.framework/PrototypeTools

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3CB0B072-3F98-3F12-A654-D1D03806EC91
-  Functions: 3698
-  Symbols:   12762
-  CStrings:  8575
+  UUID: 7C6D9339-2219-3B6C-A6B5-0EE8A536FD3F
+  Functions: 3735
+  Symbols:   12854
+  CStrings:  8669
 
Symbols:
+ -[SBFLockScreenDateView _updateAdaptiveTime]
+ -[SBFLockScreenDateViewController luminanceChangeAnimationResponse]
+ -[SBFLockScreenDateViewController setLuminanceChangeAnimationResponse:]
+ -[SBFMobileKeyBag isInStoreDemoMode]
+ -[SBFZStackParticipant allowCameraButtonDeferringWhileFocusLocked]
+ -[SBFZStackParticipant allowsKeyboardArbiterToDetermineFocusTarget]
+ -[SBFZStackParticipant overrideKeyboardFocusTarget]
+ -[SBFZStackParticipant setAllowCameraButtonDeferringWhileFocusLocked:]
+ -[SBFZStackParticipant setAllowsKeyboardArbiterToDetermineFocusTarget:]
+ -[SBFZStackParticipant setOverrideKeyboardFocusTarget:]
+ -[SBFZStackParticipantPreferences allowCameraButtonDeferringWhileFocusLocked]
+ -[SBFZStackParticipantPreferences allowsKeyboardArbiterToDetermineFocusTarget]
+ -[SBFZStackParticipantPreferences overrideKeyboardFocusTarget]
+ -[SBFZStackParticipantPreferences setAllowCameraButtonDeferringWhileFocusLocked:]
+ -[SBFZStackParticipantPreferences setAllowsKeyboardArbiterToDetermineFocusTarget:]
+ -[SBFZStackParticipantPreferences setOverrideKeyboardFocusTarget:]
+ -[SBFZStackResolver _resolveActivationStateOfSortedParticipants:changedHandler:prevailingHandler:]
+ -[SBFZStackResolver _resolveAudioCategoriesDisablingVolumeHUDOfSortedParticipants:changedHandler:prevailingHandler:]
+ -[SBFZStackResolver _resolveCameraButtonDeferringToAppsOfSortedParticipants:changedHandler:prevailingHandler:]
+ -[SBFZStackResolver _resolveCaptureButtonFullFidelityEventRequestingScenesOfSortedParticipants:changedHandler:prevailingHandler:]
+ -[SBFZStackResolver _resolveForegroundCaptureApplicationsOfSortedParticipants:changedHandler:prevailingHandler:]
+ -[SBFZStackResolver _resolveHomeAffordanceDrawingSuppressionOfSortedParticipants:changedHandler:prevailingHandler:]
+ -[SBFZStackResolver _resolveHomeGestureOwnershipOfSortedParticipants:changedHandler:prevailingHandler:]
+ -[SBFZStackResolver _resolveKeyboardArbiterFocusTargetOfSortedParticipants:changedHandler:prevailingHandler:]
+ -[SBFZStackResolver _resolveOverrideKeyboardFocusTargetOfSortedParticipants:changedHandler:prevailingHandler:]
+ -[SBFZStackResolver _resolveParticipantBelowAllowsDimmingOfSortedParticipants:changedHandler:prevailingHandler:]
+ -[SBFZStackResolver _resolvePhysicalButtonSceneTargetsOfSortedParticipants:changedHandler:prevailingHandler:]
+ -[SBFZStackResolver _resolveSystemApertureSuppressionOfSortedParticipants:changedHandler:prevailingHandler:]
+ -[SBFZStackResolver _updateResolutionsForAddedParticipant:removedParticipant:reason:]
+ -[SBFZStackResolver setSortedParticipants:]
+ -[SBFZStackResolver sortedParticipants]
+ GCC_except_table101
+ GCC_except_table103
+ GCC_except_table105
+ GCC_except_table107
+ GCC_except_table109
+ GCC_except_table111
+ GCC_except_table113
+ GCC_except_table66
+ GCC_except_table68
+ GCC_except_table85
+ GCC_except_table89
+ GCC_except_table91
+ GCC_except_table93
+ GCC_except_table95
+ GCC_except_table97
+ GCC_except_table99
+ _OBJC_CLASS_$_BSMutableOrderedDictionary
+ _OBJC_CLASS_$_MSDKDemoState
+ _OBJC_IVAR_$_SBFLockScreenDateViewController._luminanceChangeAnimationResponse
+ _OBJC_IVAR_$_SBFZStackParticipant._allowCameraButtonDeferringWhileFocusLocked
+ _OBJC_IVAR_$_SBFZStackParticipant._allowsKeyboardArbiterToDetermineFocusTarget
+ _OBJC_IVAR_$_SBFZStackParticipant._overrideKeyboardFocusTarget
+ _OBJC_IVAR_$_SBFZStackParticipantPreferences._allowCameraButtonDeferringWhileFocusLocked
+ _OBJC_IVAR_$_SBFZStackParticipantPreferences._allowsKeyboardArbiterToDetermineFocusTarget
+ _OBJC_IVAR_$_SBFZStackParticipantPreferences._overrideKeyboardFocusTarget
+ _OBJC_IVAR_$_SBFZStackResolver._sortedParticipants
+ _SBFIsSlideOverAvailable
+ _SBFTestWithSlideOver
+ _SlideOverDefaultValueFunction
+ ___39-[SBFZStackResolver _updateResolutions]_block_invoke_3
+ ___44-[SBFZStackResolver _unregisterParticipant:]_block_invoke.41
+ ___52-[SBFLockScreenDateViewController _startUpdateTimer]_block_invoke_2
+ ___85-[SBFZStackResolver _updateResolutionsForAddedParticipant:removedParticipant:reason:]_block_invoke
+ ___SlideOverStorage
+ ___block_descriptor_40_e8_32s_e43_v24?0"NSString"8"SBFZStackParticipant"16ls32l8
+ ___block_literal_global.346
+ ___block_literal_global.348
+ ___block_literal_global.99
+ _objc_msgSend$_updateAdaptiveTime
+ _objc_msgSend$allowCameraButtonDeferringWhileFocusLocked
+ _objc_msgSend$allowsKeyboardArbiterToDetermineFocusTarget
+ _objc_msgSend$bs_reverse
+ _objc_msgSend$isInStoreDemoMode
+ _objc_msgSend$isStoreDemoModeEnabled:
+ _objc_msgSend$overrideKeyboardFocusTarget
+ _objc_msgSend$setAllowCameraButtonDeferringWhileFocusLocked:
+ _objc_msgSend$setAllowsKeyboardArbiterToDetermineFocusTarget:
+ _objc_msgSend$setOverrideKeyboardFocusTarget:
+ _objc_msgSend$setUsesLightTimeFontVariant:response:
+ _objc_msgSend$stringByReplacingOccurrencesOfString:withString:
- -[SBFZStackResolver _resolveActivationStateOfSortedParticipants:changedParticipantHandler:]
- -[SBFZStackResolver _resolveAudioCategoriesDisablingVolumeHUDOfSortedParticipants:changedParticipantHandler:]
- -[SBFZStackResolver _resolveCaptureButtonFullFidelityEventRequestingScenesOfSortedParticipants:changedParticipantHandler:]
- -[SBFZStackResolver _resolveForegroundCaptureApplicationsOfSortedParticipants:changedParticipantHandler:]
- -[SBFZStackResolver _resolveHomeAffordanceDrawingSuppressionOfSortedParticipants:changedParticipantHandler:]
- -[SBFZStackResolver _resolveHomeGestureOwnershipOfSortedParticipants:changedParticipantHandler:]
- -[SBFZStackResolver _resolveParticipantBelowAllowsDimmingOfSortedParticipants:changedParticipantHandler:]
- -[SBFZStackResolver _resolvePhysicalButtonSceneTargetsOfSortedParticipants:changedParticipantHandler:]
- -[SBFZStackResolver _resolveSystemApertureSuppressionOfSortedParticipants:changedParticipantHandler:]
- -[SBFZStackResolver _updateResolutionsForAddedParticipant:removedParticipant:]
- GCC_except_table100
- GCC_except_table102
- GCC_except_table104
- GCC_except_table106
- GCC_except_table108
- GCC_except_table110
- GCC_except_table112
- GCC_except_table67
- GCC_except_table84
- GCC_except_table88
- GCC_except_table90
- GCC_except_table92
- GCC_except_table94
- GCC_except_table96
- GCC_except_table98
- _OBJC_IVAR_$_SBFLockScreenDateViewController._miscellaneousDefaults
- _OBJC_IVAR_$_SBFLockScreenDateViewController._miscellaneousDefaultsObserver
- ___44-[SBFZStackResolver _unregisterParticipant:]_block_invoke.35
- ___58-[SBFLockScreenDateViewController initWithNibName:bundle:]_block_invoke_2
- ___78-[SBFZStackResolver _updateResolutionsForAddedParticipant:removedParticipant:]_block_invoke
- ___block_literal_global.302
- ___block_literal_global.304
- ___block_literal_global.50
- _objc_msgSend$sensitiveUIEnabled
- _objc_msgSend$setUsesLightTimeFontVariant:
CStrings:
+ "\a+ "
+ "!&!"
+ "!\x81"
+ "%@ %@"
+ "%@%@:"
+ "%@->%@"
+ "; "
+ "@\"SBKeyboardFocusTarget\""
+ "@\"SBKeyboardFocusTarget\"16@0:8"
+ "N"
+ "No Change (%{public}@)"
+ "No Visible Change (%{public}@)"
+ "NotificationWake"
+ "Resolved Stack (%{public}@) %{public}@"
+ "SBSlideOver"
+ "T@\"SBKeyboardFocusTarget\",&,N,V_overrideKeyboardFocusTarget"
+ "T@\"SBKeyboardFocusTarget\",R,N"
+ "TB,N,V_allowCameraButtonDeferringWhileFocusLocked"
+ "TB,N,V_allowsKeyboardArbiterToDetermineFocusTarget"
+ "Td,N,V_luminanceChangeAnimationResponse"
+ "Topmost Value Sources: %{public}@"
+ "Tq,N,V_allowCameraButtonDeferringWhileFocusLocked"
+ "Tq,N,V_allowsKeyboardArbiterToDetermineFocusTarget"
+ "Y"
+ "_allowCameraButtonDeferringWhileFocusLocked"
+ "_allowsKeyboardArbiterToDetermineFocusTarget"
+ "_luminanceChangeAnimationResponse"
+ "_overrideKeyboardFocusTarget"
+ "_sortedParticipants"
+ "_updateAdaptiveTime"
+ "add(%@)"
+ "allowCameraButtonDeferringWhileFocusLocked"
+ "allowCameraButtonDeferringWhileFocusLocked: %@->%@"
+ "allowCameraButtonWhileFocusLocked"
+ "allowsKeyboardArbiterToDetermineFocusTarget"
+ "audioCategories: %@"
+ "audioCategories: %@->%@"
+ "belowAllowsDimming"
+ "belowAllowsDimming: %@->%@"
+ "bs_reverse"
+ "captureButtonScenes: %lu"
+ "captureButtonScenes: %lu->%lu"
+ "com.apple."
+ "fgCaptureButtonTargets: %lu"
+ "fgCaptureButtonTargets: %lu->%lu"
+ "homeAffordanceDrawingSuppressed: %@->%@"
+ "isInStoreDemoMode"
+ "isStoreDemoModeEnabled:"
+ "keyboardArbiter"
+ "keyboardArbiter: %@->%@"
+ "luminanceChangeAnimationResponse"
+ "no changes"
+ "overrideKeyboardFocusTarget"
+ "overrideKeyboardTarget"
+ "overrideKeyboardTarget: %@->%@"
+ "ownsHomeGesture: %@->%@"
+ "physicalButtonTargets: %lu"
+ "physicalButtonTargets: %lu->%lu"
+ "remove(%@)"
+ "setAllowCameraButtonDeferringWhileFocusLocked:"
+ "setAllowsKeyboardArbiterToDetermineFocusTarget:"
+ "setLuminanceChangeAnimationResponse:"
+ "setOverrideKeyboardFocusTarget:"
+ "setUsesLightTimeFontVariant:response:"
+ "stringByReplacingOccurrencesOfString:withString:"
+ "suppressedBundles: %@"
+ "suppressedBundles: %@->%@"
+ "suppressedScenes: %d"
+ "suppressedScenes: %d->%d"
+ "systemApertureSuppressed"
+ "systemApertureSuppressed: %@->%@"
+ "update(%@)"
+ "v24@?0@\"NSString\"8@\"SBFZStackParticipant\"16"
- "!&"
- "!q"
- "%@ to %@; "
- "%@; "
- "%@<%@> %@%@%@%@"
- "Resolved Stack %{public}@"
- "_miscellaneousDefaults"
- "_miscellaneousDefaultsObserver"
- "ownsHomeGesture: %@; "
- "ownsHomeGesture: from %@ to %@; "
- "participantBelowAllowsDimming: %@"
- "participantBelowAllowsDimming: from %@ to %@;"
- "setUsesLightTimeFontVariant:"
- "suppression: %@; "
- "suppression: from %@ to %@; "

```
