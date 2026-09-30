## LocalAuthenticationEmbeddedUI

> `/System/Library/Frameworks/LocalAuthenticationEmbeddedUI.framework/LocalAuthenticationEmbeddedUI`

```diff

-1656.80.6.0.0
-  __TEXT.__text: 0x21948
-  __TEXT.__auth_stubs: 0xb60
-  __TEXT.__objc_methlist: 0x2d14
-  __TEXT.__const: 0x482
-  __TEXT.__cstring: 0x240f
-  __TEXT.__gcc_except_tab: 0x4ec
-  __TEXT.__oslogstring: 0x5ff
+1656.100.222.0.0
+  __TEXT.__text: 0x2311c
+  __TEXT.__auth_stubs: 0xbf0
+  __TEXT.__objc_methlist: 0x3940
+  __TEXT.__const: 0x4a2
+  __TEXT.__cstring: 0x258f
+  __TEXT.__gcc_except_tab: 0x4c0
+  __TEXT.__oslogstring: 0x809
   __TEXT.__dlopen_cstrs: 0x4c
-  __TEXT.__swift5_typeref: 0x218
+  __TEXT.__swift5_typeref: 0x236
   __TEXT.__swift5_capture: 0x30
   __TEXT.__constg_swiftt: 0xb0
   __TEXT.__swift5_reflstr: 0x5e

   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_proto: 0x28
   __TEXT.__swift5_types: 0xc
-  __TEXT.__unwind_info: 0xc18
-  __TEXT.__objc_classname: 0xcd8
-  __TEXT.__objc_methname: 0x6f32
-  __TEXT.__objc_methtype: 0x1d92
-  __TEXT.__objc_stubs: 0x5660
-  __DATA_CONST.__got: 0x3d0
-  __DATA_CONST.__const: 0xf80
+  __TEXT.__unwind_info: 0xc98
+  __TEXT.__objc_classname: 0xcb9
+  __TEXT.__objc_methname: 0x742a
+  __TEXT.__objc_methtype: 0x1e7b
+  __TEXT.__objc_stubs: 0x5a20
+  __DATA_CONST.__got: 0x400
+  __DATA_CONST.__const: 0x1040
   __DATA_CONST.__objc_classlist: 0x268
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x100
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1880
+  __DATA_CONST.__objc_selrefs: 0x1c30
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x160
-  __AUTH_CONST.__auth_got: 0x5c0
-  __AUTH_CONST.__auth_ptr: 0x158
+  __AUTH_CONST.__auth_got: 0x608
+  __AUTH_CONST.__auth_ptr: 0x160
   __AUTH_CONST.__const: 0x388
-  __AUTH_CONST.__cfstring: 0x1060
-  __AUTH_CONST.__objc_const: 0xc340
+  __AUTH_CONST.__cfstring: 0x1140
+  __AUTH_CONST.__objc_const: 0xab60
   __AUTH_CONST.__objc_intobj: 0x150
   __AUTH.__objc_data: 0x1878
   __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0x37c
-  __DATA.__data: 0xb80
+  __DATA.__objc_ivar: 0x388
+  __DATA.__data: 0xb90
   __DATA.__bss: 0x580
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 1184
-  Symbols:   1384
-  CStrings:  1742
+  Functions: 1236
+  Symbols:   1448
+  CStrings:  1797
 
Symbols:
+ _LACEntitlementPasscodeServices
+ _LACEntitlementSPI
+ _LACErrorCodeDenied
+ _OBJC_CLASS_$_LACError
+ _OBJC_CLASS_$_LACFlags
+ _OBJC_CLASS_$_LACPSAuthorizerComposite
+ _OBJC_CLASS_$_LACPSAuthorizerDispatchDecorator
+ _OBJC_CLASS_$_LACPSAuthorizerEntitlementsAdapter
+ _malloc_size
+ _memcpy
+ _memmove
+ _objc_retain_x25
+ _swift_arrayDestroy
+ _swift_errorRetain
+ _swift_isUniquelyReferenced_nonNull_native
+ _swift_slowAlloc
+ _swift_slowDealloc
+ _swift_unknownObjectRetain
- _NSLocalizedStringFromLACBiometryType
- _OBJC_CLASS_$_LACMobileGestalt
- __swift_FORCE_LOAD_$_swiftFileProvider
- _objc_retain_x28
CStrings:
+ "\x06"
+ "\x12\x11"
+ "%{public}@ invalidated view model: %{public}s"
+ "%{public}@ opening URL: %{public}s"
+ "%{public}@ starting evaluation with presentation style: %ld"
+ "%{public}@ state changed from: %{public}s to: %{public}s"
+ "%{public}@ will inform delegate %{public}s about result: %{public}s error: %{public}s"
+ "-[LAPSPasscodeViewControllerBase _submitPasscode:]"
+ "-[LAPSPasscodeViewControllerBase passcodeField:didChangePasscodeLength:]"
+ "-[LAPSPasscodeViewControllerBase passcodeField:didSubmitPasscode:]"
+ "@\"<LACPSAuthorizer>\""
+ "@\"<LAPSPasscodeViewControllerDelegate>\"16@0:8"
+ "@\"LACPSAuthorizerComposite\"8@?0"
+ "@\"LAPSPasscodeViewControllerManagedViews\""
+ "@\"LAPSPasscodeViewControllerManagedViews\"8@?0"
+ "@\"UIViewController<LAPSPasscodeViewControlling>\""
+ "@\"UIViewController<LAPSPasscodeViewControlling>\"8@?0"
+ "@24@0:8@\"LAPSPasscodeViewControllerConfiguration\"16"
+ "Could not authenticate using credential %{public}@"
+ "Did finish passcode verification"
+ "Enter a strong passcode with 6 or more characters"
+ "LACPSAuthorizer"
+ "LAPSPasscodeViewControllerBase"
+ "LAPSPasscodeViewControllerBase.m"
+ "LAPSPasscodeViewControllerManagedViews"
+ "LAPSPasscodeViewControlling"
+ "PASSCODE_RECOVERY_ERROR_NEW_PASSCODE_MISMATCH_INLINE"
+ "PASSCODE_RECOVERY_ERROR_PASSCODE_DOES_NOT_MEET_REQUIREMENTS_INLINE_TEXT"
+ "PASSCODE_REMOVAL_NOT_ALLOWED_TEXT_FACE_ID"
+ "PASSCODE_REMOVAL_NOT_ALLOWED_TEXT_OPTIC_ID"
+ "PASSCODE_REMOVAL_NOT_ALLOWED_TEXT_TOUCH_ID"
+ "PASSCODE_REMOVAL_NOT_ALLOWED_TITLE_FACE_ID"
+ "PASSCODE_REMOVAL_NOT_ALLOWED_TITLE_OPTIC_ID"
+ "PASSCODE_REMOVAL_NOT_ALLOWED_TITLE_TOUCH_ID"
+ "Skipping entitlement checks while ff is disabled"
+ "T@\"<LAPSPasscodeViewControllerDelegate>\",W,N"
+ "T@\"LACUIPasscodeField\",W,N,V_passcodeFieldVC"
+ "T@\"NSString\",&,N,V_currentPasscodePrompt"
+ "T@\"UILabel\",W,N,V_errorCapsule"
+ "T@\"UILabel\",W,N,V_footerLabel"
+ "T@\"UILabel\",W,N,V_headerLabel"
+ "T@\"UIScrollView\",W,N,V_scrollView"
+ "T@\"UIView\",W,N,V_errorCapsuleContainer"
+ "Will start passcode verification"
+ "[self styleWithPasscodeType:[self passcodeType]] == [[self _passcodeFieldVC] style]"
+ "_currentPasscodePrompt"
+ "_dismissWithCompletion:"
+ "_footerLabel"
+ "_handleCancel:"
+ "_handleNext:"
+ "_headerLabel"
+ "_localizedDescriptionFromError:"
+ "_localizedErrorMessageForBiometryType:"
+ "_localizedErrorTitleForBiometryType:"
+ "_mainStackHorizontalPadding"
+ "_managedViews"
+ "_presentNewPasscodeVCWithTransitionStyle:errorMessage:"
+ "_showPasscodeOptionsSourceWithView:sourceItem:presentationStyle:shouldResignFirstResponder:"
+ "canRemovePasscode: YES (no biometry)"
+ "clearWithErrorMessage:"
+ "currentPasscodePrompt"
+ "errorCapsule"
+ "errorCapsuleContainer"
+ "featureFlagPasscodeServicesProtectionEnabled"
+ "footerLabel"
+ "headerLabel"
+ "initWithAuthorizers:"
+ "initWithRequiredEntitlements:"
+ "isAccessibilityTextEnabled"
+ "passcodeChangeErrorNewPasscodeMismatchInlineText"
+ "passcodeChangeErrorPasscodeDoesNotMeetRequirementsInlineText"
+ "passcodeField == [self _passcodeFieldVC]"
+ "passcodeFieldVC"
+ "passcodeRemovalNotAllowedTextFaceID"
+ "passcodeRemovalNotAllowedTextOpticID"
+ "passcodeRemovalNotAllowedTextTouchID"
+ "passcodeRemovalNotAllowedTitleFaceID"
+ "passcodeRemovalNotAllowedTitleOpticID"
+ "passcodeRemovalNotAllowedTitleTouchID"
+ "restartWithErrorMessage:"
+ "scrollView"
+ "setCredential:type:error:"
+ "setCurrentPasscodePrompt:"
+ "setErrorCapsule:"
+ "setErrorCapsuleContainer:"
+ "setFooterLabel:"
+ "setHeaderLabel:"
+ "setPasscodeFieldVC:"
+ "setScrollView:"
+ "setup"
+ "setupNavigationItem"
+ "sharedInstance"
+ "shouldShowPasscodeOptionsButton"
+ "showPasscodeOptionsSourceItem:presentationStyle:shouldResignFirstResponder:"
+ "showPasscodeOptionsSourceWithView:presentationStyle:shouldResignFirstResponder:"
+ "styleWithPasscodeType:"
+ "updateLayoutAfterPasscodeLengthChangeIfNeeded:"
+ "updateLayoutAfterPasscodeTypeChangeIfNeeded"
+ "v24@0:8@\"<LAPSPasscodeViewControllerDelegate>\"16"
+ "v24@0:8@\"NSString\"16"
+ "v28@0:8@\"UIViewController<LAPSPasscodeViewControlling>\"16B24"
+ "v32@0:8@\"UIViewController<LAPSPasscodeViewControlling>\"16@\"LAPSPasscode\"24"
+ "v32@0:8@\"UIViewController<LAPSPasscodeViewControlling>\"16@\"LAPSPasscodeType\"24"
+ "v32@0:8@\"UIViewController<LAPSPasscodeViewControlling>\"16@\"NSError\"24"
+ "v32@0:8q16@24"
+ "v36@0:8@16q24B32"
+ "v44@0:8@16@24q32B40"
- "\x02\x11"
- "\x16"
- " invalidated view model: "
- " starting evaluation with presentation style: "
- " state changed from: "
- " will inform delegate "
- "-[LAPSPasscodeViewController _submitPasscode:]"
- "-[LAPSPasscodeViewController passcodeField:didChangePasscodeLength:]"
- "-[LAPSPasscodeViewController passcodeField:didSubmitPasscode:]"
- "@\"<LAPSPasscodeChangeAuthorizer>\""
- "@\"LAPSPasscodeViewController\""
- "@\"LAPSPasscodeViewController\"8@?0"
- "@\"UILayoutGuide\""
- "@\"UIStackView\""
- "I\x11"
- "LACUIPasscodeFieldDelegate"
- "LAPSPasscodeChangeAuthorizer"
- "LAPSPasscodeChangeAuthorizerDispatchDecorator"
- "LAPSPasscodeChangeAuthorizerNullAdapter"
- "LAPSPasscodeViewController.m"
- "PASSCODE_REMOVAL_NOT_ALLOWED_TEXT"
- "T@\"<LAPSPasscodeViewControllerDelegate>\",W,N,V_delegate"
- "[self _styleWithPasscodeType:_passcodeType] == [_passcodeFieldVC style]"
- "_accessibilitySpacing"
- "_bottomAreaLayoutGuide"
- "_bottomPadding"
- "_cancel:"
- "_header"
- "_isAccessibilityTextEnabled"
- "_layoutIfNeeded"
- "_next:"
- "_optionsItem"
- "_passcodeOptionsPresentationStyle"
- "_passcodeTypeAllowsVariableLength"
- "_setNextButtonEnabled:"
- "_setupNavigationItem"
- "_shouldShowPasscodeOptionsButton"
- "_shouldShowPasscodeOptionsNavigationItem"
- "_stack"
- "_styleWithPasscodeType:"
- "ellipsis"
- "initWithImage:style:target:action:"
- "marketingDeviceFamilyName"
- "passcodeField == _passcodeFieldVC"
- "passcodeRemovalNotAllowedText:"
- "passcodeRemovalNotAllowedTitle:"
- "v28@0:8@\"LAPSPasscodeViewController\"16B24"
- "v32@0:8@\"LACUIPasscodeField\"16@\"NSString\"24"
- "v32@0:8@\"LACUIPasscodeField\"16Q24"
- "v32@0:8@\"LAPSPasscodeViewController\"16@\"LAPSPasscode\"24"
- "v32@0:8@\"LAPSPasscodeViewController\"16@\"LAPSPasscodeType\"24"
- "v32@0:8@\"LAPSPasscodeViewController\"16@\"NSError\"24"

```
