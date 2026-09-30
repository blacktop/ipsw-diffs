## BiometricKitUI

> `/System/Library/PrivateFrameworks/BiometricKitUI.framework/BiometricKitUI`

```diff

-646.4.2.0.0
-  __TEXT.__text: 0x5bae4
-  __TEXT.__auth_stubs: 0xdf0
-  __TEXT.__objc_methlist: 0x6870
-  __TEXT.__const: 0x954
+653.0.0.0.0
+  __TEXT.__text: 0x5d4f0
+  __TEXT.__auth_stubs: 0xe00
+  __TEXT.__objc_methlist: 0x6988
+  __TEXT.__const: 0x994
   __TEXT.__gcc_except_tab: 0xdac
-  __TEXT.__cstring: 0x2d26
-  __TEXT.__oslogstring: 0x3d38
+  __TEXT.__cstring: 0x2d46
+  __TEXT.__oslogstring: 0x3ee4
   __TEXT.__dlopen_cstrs: 0x292
   __TEXT.__swift5_typeref: 0x96
   __TEXT.__swift5_capture: 0x34

   __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_proto: 0x8
   __TEXT.__swift5_types: 0xc
-  __TEXT.__unwind_info: 0x16d8
+  __TEXT.__unwind_info: 0x1710
   __TEXT.__objc_classname: 0xc5e
-  __TEXT.__objc_methname: 0x124b9
-  __TEXT.__objc_methtype: 0x311d
-  __TEXT.__objc_stubs: 0xcd40
-  __DATA_CONST.__got: 0x7e0
-  __DATA_CONST.__const: 0x1218
+  __TEXT.__objc_methname: 0x12711
+  __TEXT.__objc_methtype: 0x3115
+  __TEXT.__objc_stubs: 0xcf60
+  __DATA_CONST.__got: 0x7e8
+  __DATA_CONST.__const: 0x11f8
   __DATA_CONST.__objc_classlist: 0x210
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x148
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4308
+  __DATA_CONST.__objc_selrefs: 0x43a8
   __DATA_CONST.__objc_superrefs: 0x180
   __DATA_CONST.__objc_arraydata: 0x188
-  __AUTH_CONST.__auth_got: 0x710
+  __AUTH_CONST.__auth_got: 0x718
   __AUTH_CONST.__const: 0x2f0
   __AUTH_CONST.__cfstring: 0x3060
-  __AUTH_CONST.__objc_const: 0xe538
+  __AUTH_CONST.__objc_const: 0xe648
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__objc_floatobj: 0x80
   __AUTH_CONST.__objc_intobj: 0x228

   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0x1060
   __AUTH.__data: 0xe0
-  __DATA.__objc_ivar: 0x960
+  __DATA.__objc_ivar: 0x974
   __DATA.__data: 0x1018
   __DATA.__bss: 0x2f0
   __DATA.__common: 0x200

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_errno.dylib
-  - /usr/lib/swift/libswift_math.dylib
-  - /usr/lib/swift/libswift_signal.dylib
-  - /usr/lib/swift/libswift_stdio.dylib
-  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: E05F898F-E5BC-3921-9A09-0D49B272B838
-  Functions: 2407
-  Symbols:   8434
-  CStrings:  4813
+  UUID: 298DD268-FB49-37B1-BB55-B38B39FA7477
+  Functions: 2428
+  Symbols:   8489
+  CStrings:  4853
 
Symbols:
+ +[BKUIStyle buttonMarginsForPhones]
+ -[BKMesaSecureIntentProvider currentDevice]
+ -[BKMesaSecureIntentProvider initInBuddy:withBKUIDevice:]
+ -[BKMesaSecureIntentProvider setCurrentDevice:]
+ -[BKUIButtonTray allButtonsView]
+ -[BKUIButtonTray horizontalLayoutConstraints:]
+ -[BKUIButtonTray isSolarium]
+ -[BKUIButtonTray noButtonsView]
+ -[BKUIButtonTray oneButtonView:]
+ -[BKUIButtonTray resetAlphaForAllButtons]
+ -[BKUIButtonTray resetConstraintsForButtons]
+ -[BKUIButtonTray setIsSolarium:]
+ -[BKUIButtonTray setupDebugUITraits]
+ -[BKUIButtonTray twoButtonView:secondButton:]
+ -[BKUIButtonTray updateInitialButtonLayout]
+ -[BKUIFingerprintEnrollViewController didTapInValidRectForAlertInstructingWhereToTouch:]
+ -[BKUIPearlInstructionView isSolarium]
+ -[BKUIPearlInstructionView setIsSolarium:]
+ -[BKUISettingsSecureIntentClientView currentDevice]
+ -[BKUISettingsSecureIntentClientView setCurrentDevice:]
+ -[BuddySecureIntentClientView currentDevice]
+ -[BuddySecureIntentClientView setCurrentDevice:]
+ _BKUISolariumOBKButtonBottomPadding
+ _BKUISolariumOBKButtonHeight
+ _BKUISolariumOBKSpacingBetweenButtons
+ _OBJC_IVAR_$_BKMesaSecureIntentProvider._currentDevice
+ _OBJC_IVAR_$_BKUIButtonTray._isSolarium
+ _OBJC_IVAR_$_BKUIPearlInstructionView._isSolarium
+ _OBJC_IVAR_$_BKUISettingsSecureIntentClientView._currentDevice
+ _OBJC_IVAR_$_BuddySecureIntentClientView._currentDevice
+ _SolariumOBKButtonEdgePaddingForPhones
+ _SolariumOBKButtonSizeForPads
+ _UIFontWeightSemibold
+ __ZNSt12length_errorC1B8ne200100EPKc
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorI12InstanceInfoEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__120__throw_length_errorB8ne200100EPKc
+ __ZNSt3__16vectorI12InstanceInfoNS_9allocatorIS1_EEE20__throw_length_errorB8ne200100Ev
+ __ZSt28__throw_bad_array_new_lengthB8ne200100v
+ __ZnwmSt19__type_descriptor_t
+ ___118-[BKMesaSecureIntentProvider _getSecureIntentForAccessory:enrollmentOperation:showErrorToRetry:withCompletionHandler:]_block_invoke.26
+ ___118-[BKMesaSecureIntentProvider _getSecureIntentForAccessory:enrollmentOperation:showErrorToRetry:withCompletionHandler:]_block_invoke_2.28
+ ___67-[BKUIFingerprintEnrollViewController applicationWillResignActive:]_block_invoke.100
+ ___67-[BKUIFingerprintEnrollViewController applicationWillResignActive:]_block_invoke.100.cold.1
+ ___72-[BKUIPearlEnrollView setCameraBlurAmount:useShade:duration:completion:]_block_invoke.92
+ __os_feature_enabled_impl
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_BiometricKitUI
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_BiometricKitUI
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_BiometricKitUI
+ _objc_msgSend$_preferredFontForTextStyle:weight:
+ _objc_msgSend$addObjectsFromArray:
+ _objc_msgSend$allButtonsView
+ _objc_msgSend$arrayByAddingObjectsFromArray:
+ _objc_msgSend$buttonMarginsForPhones
+ _objc_msgSend$currentTitle
+ _objc_msgSend$didTapInValidRectForAlertInstructingWhereToTouch:
+ _objc_msgSend$grayColor
+ _objc_msgSend$horizontalLayoutConstraints:
+ _objc_msgSend$instanceForBKUIDevice:
+ _objc_msgSend$invalidateIntrinsicContentSize
+ _objc_msgSend$noButtonsView
+ _objc_msgSend$oneButtonView:
+ _objc_msgSend$resetAlphaForAllButtons
+ _objc_msgSend$resetConstraintsForButtons
+ _objc_msgSend$setCancelsTouchesInView:
+ _objc_msgSend$setupDebugUITraits
+ _objc_msgSend$twoButtonView:secondButton:
+ _objc_msgSend$updateInitialButtonLayout
- -[BKMesaSecureIntentProvider initWithAlertWindow:inBuddy:]
- __ZNKSt3__16vectorI12InstanceInfoNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
- __ZNSt12length_errorC1B8ne190102EPKc
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorI12InstanceInfoEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__120__throw_length_errorB8ne190102EPKc
- __ZSt28__throw_bad_array_new_lengthB8ne190102v
- __Znwm
- ___118-[BKMesaSecureIntentProvider _getSecureIntentForAccessory:enrollmentOperation:showErrorToRetry:withCompletionHandler:]_block_invoke.27
- ___118-[BKMesaSecureIntentProvider _getSecureIntentForAccessory:enrollmentOperation:showErrorToRetry:withCompletionHandler:]_block_invoke_2.29
- ___67-[BKUIFingerprintEnrollViewController applicationWillResignActive:]_block_invoke.99
- ___67-[BKUIFingerprintEnrollViewController applicationWillResignActive:]_block_invoke.99.cold.1
- ___72-[BKUIPearlEnrollView setCameraBlurAmount:useShade:duration:completion:]_block_invoke.93
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_errno_$_BiometricKitUI
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_math_$_BiometricKitUI
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_signal_$_BiometricKitUI
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_stdio_$_BiometricKitUI
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swift_time_$_BiometricKitUI
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftsys_time_$_BiometricKitUI
- __swift_FORCE_LOAD_$_swiftunistd
- __swift_FORCE_LOAD_$_swiftunistd_$_BiometricKitUI
- _objc_msgSend$instance
- _objc_msgSend$setNumberOfTapsRequired:
CStrings:
+ "@\"BKUIDevice\""
+ "@\"BKUIDevice\"16@0:8"
+ "@\"UIView<SecureIntentClientView>\"24@0:8@\"BKUIDevice\"16"
+ "@28@0:8B16@20"
+ "ButtonTray: Next State button [%@ - willShow:%@] | Bottom Link button [%@ - willShow:%@] | Top Link button [%@ - willShow:%@]"
+ "ButtonTray: Refreshing content"
+ "ButtonTray: will show allButtonsView"
+ "ButtonTray: will show noButtonsView"
+ "ButtonTray: will show oneButtonView"
+ "ButtonTray: will show twoButtonView"
+ "NaturalUI"
+ "OnBoardingKit"
+ "Solarium"
+ "SwiftUI"
+ "T@\"BKUIDevice\",&,V_currentDevice"
+ "T@\"BKUIDevice\",W,N"
+ "T@\"BKUIDevice\",W,N,V_currentDevice"
+ "TB,N,V_isSolarium"
+ "User tapped on screen: tutorialView [Hidden:%@] enrollmentView [Hidden:%@] tappedY [%f] validY [%f] -> tappedInValidRect [%@]"
+ "_currentDevice"
+ "_isSolarium"
+ "_preferredFontForTextStyle:weight:"
+ "addObjectsFromArray:"
+ "allButtonsView"
+ "arrayByAddingObjectsFromArray:"
+ "buttonMarginsForPhones"
+ "currentTitle"
+ "didTapInValidRectForAlertInstructingWhereToTouch:"
+ "grayColor"
+ "horizontalLayoutConstraints:"
+ "initInBuddy:withBKUIDevice:"
+ "instanceForBKUIDevice:"
+ "invalidateIntrinsicContentSize"
+ "isSolarium"
+ "noButtonsView"
+ "oneButtonView:"
+ "resetAlphaForAllButtons"
+ "resetConstraintsForButtons"
+ "setCancelsTouchesInView:"
+ "setCurrentDevice:"
+ "setIsSolarium:"
+ "setupDebugUITraits"
+ "twoButtonView:secondButton:"
+ "updateInitialButtonLayout"
+ "v24@0:8@\"BKUIDevice\"16"
+ "{vector<InstanceInfo, std::allocator<InstanceInfo>>=\"__begin_\"^{InstanceInfo}\"__end_\"^{InstanceInfo}\"__cap_\"^{InstanceInfo}}"
- "@\"UIView<SecureIntentClientView>\"16@0:8"
- "@28@0:8@16B24"
- "initWithAlertWindow:inBuddy:"
- "instance"
- "setNumberOfTapsRequired:"
- "{vector<InstanceInfo, std::allocator<InstanceInfo>>=\"__begin_\"^{InstanceInfo}\"__end_\"^{InstanceInfo}\"__end_cap_\"{__compressed_pair<InstanceInfo *, std::allocator<InstanceInfo>>=\"__value_\"^{InstanceInfo}}}"

```
