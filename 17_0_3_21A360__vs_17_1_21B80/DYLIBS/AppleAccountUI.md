## AppleAccountUI

> `/System/Library/PrivateFrameworks/AppleAccountUI.framework/AppleAccountUI`

```diff

-486.1.1.4.0
-  __TEXT.__text: 0xb4020
-  __TEXT.__auth_stubs: 0x1bc0
-  __TEXT.__objc_methlist: 0x6df4
-  __TEXT.__const: 0x1114
-  __TEXT.__gcc_except_tab: 0xe74
-  __TEXT.__cstring: 0x4797
-  __TEXT.__oslogstring: 0x8df6
+493.2.1.1.0
+  __TEXT.__text: 0xb58b8
+  __TEXT.__auth_stubs: 0x1bf0
+  __TEXT.__objc_methlist: 0x6f4c
+  __TEXT.__const: 0x1144
+  __TEXT.__gcc_except_tab: 0xe78
+  __TEXT.__cstring: 0x47a7
+  __TEXT.__oslogstring: 0x910a
   __TEXT.__dlopen_cstrs: 0x387
   __TEXT.__ustring: 0x4
-  __TEXT.__swift5_typeref: 0x1646
+  __TEXT.__swift5_typeref: 0x16be
   __TEXT.__swift5_capture: 0x1a4
   __TEXT.__swift5_reflstr: 0x4a5
   __TEXT.__swift5_assocty: 0x178

   __TEXT.__swift5_proto: 0x70
   __TEXT.__swift5_types: 0x8c
   __TEXT.__swift5_builtin: 0x50
-  __TEXT.__unwind_info: 0x2d04
+  __TEXT.__unwind_info: 0x2d7c
   __TEXT.__eh_frame: 0x53c
-  __TEXT.__objc_classname: 0x1a7d
-  __TEXT.__objc_methname: 0x15c99
-  __TEXT.__objc_methtype: 0x40c1
-  __TEXT.__objc_stubs: 0x10600
-  __DATA_CONST.__got: 0x8b8
+  __TEXT.__objc_classname: 0x1aa2
+  __TEXT.__objc_methname: 0x1621d
+  __TEXT.__objc_methtype: 0x42ef
+  __TEXT.__objc_stubs: 0x10800
+  __DATA_CONST.__got: 0x8c8
   __DATA_CONST.__const: 0x23f8
   __DATA_CONST.__objc_classlist: 0x548
   __DATA_CONST.__objc_catlist: 0x68
-  __DATA_CONST.__objc_protolist: 0x200
+  __DATA_CONST.__objc_protolist: 0x208
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x28498
-  __DATA_CONST.__objc_selrefs: 0x4fd0
-  __DATA_CONST.__objc_arraydata: 0xb0
-  __AUTH_CONST.__objc_const: 0x3a18
-  __AUTH_CONST.__cfstring: 0x3d00
-  __AUTH_CONST.__const: 0x1a28
+  __DATA_CONST.__objc_const: 0x286d8
+  __DATA_CONST.__objc_selrefs: 0x50b8
+  __DATA_CONST.__objc_arraydata: 0xb8
+  __AUTH_CONST.__objc_const: 0x3a60
+  __AUTH_CONST.__cfstring: 0x3d60
+  __AUTH_CONST.__const: 0x1a68
   __AUTH_CONST.__objc_intobj: 0x90
-  __AUTH_CONST.__objc_arrayobj: 0x48
-  __AUTH_CONST.__auth_got: 0xdf0
+  __AUTH_CONST.__objc_arrayobj: 0x60
+  __AUTH_CONST.__auth_got: 0xe08
   __AUTH.__objc_data: 0x3678
   __AUTH.__data: 0x220
   __DATA.__objc_protorefs: 0x28
-  __DATA.__objc_classrefs: 0xb50
+  __DATA.__objc_classrefs: 0xb60
   __DATA.__objc_superrefs: 0x398
-  __DATA.__objc_ivar: 0x970
-  __DATA.__data: 0x1ef8
-  __DATA.__bss: 0x11e8
-  __DATA.__common: 0x298
+  __DATA.__objc_ivar: 0x994
+  __DATA.__data: 0x1f68
+  __DATA.__bss: 0x11f0
+  __DATA.__common: 0x280
   __DATA_DIRTY.__const: 0x18
   __DATA_DIRTY.__objc_data: 0x230
   __DATA_DIRTY.__bss: 0x28

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: AC530AF4-4DDD-3155-8710-FB4F585E075F
-  Functions: 4262
-  Symbols:   12403
-  CStrings:  5962
+  UUID: B00F8E57-5A00-331D-A807-4659895182D8
+  Functions: 4311
+  Symbols:   12538
+  CStrings:  6030
 
Symbols:
+ +[AAUISignInViewController _isRunningInMuseBuddy]
+ +[UIAlertController(AppleAccountUI) alertWithTitle:message:]
+ +[_AAUIDataclassOptionCache _hasPrescriptionEnrollment]
+ -[AAUIProfilePictureStore initWithAppleAccount:grandSlamAccount:accountStore:].cold.1
+ -[AAUIProfilePictureStore initWithGrandSlamSigner:].cold.1
+ -[AAUIProfilePictureStore initWithGrandSlamSigner:].cold.2
+ -[AAUIProfilePictureStore initWithGrandSlamSigner:].cold.3
+ -[AAUIProfilePictureStore updateCacheWithPhoto:cropRect:].cold.5
+ -[AAUIServerSuppliedProfilePictureCache _entryForPersonID:].cold.1
+ -[AAUIServerSuppliedProfilePictureCache _entryForPersonID:].cold.2
+ -[AAUISignInController akURLBag]
+ -[AAUISignInController preferredContentSize]
+ -[AAUISignInController setAKURLBag:]
+ -[AAUISignInViewController _accountHelpStackView]
+ -[AAUISignInViewController _delegate_signInViewControllerDidCompleteWithAuthenticationResults:completionHandler:]
+ -[AAUISignInViewController _initialHeight]
+ -[AAUISignInViewController _updateExpandingViewInFooterForCellChange:]
+ -[AAUISignInViewController accountHelpStackView]
+ -[AAUISignInViewController akURLBag]
+ -[AAUISignInViewController authenticationController:shouldContinueWithAuthenticationResults:error:forContext:completion:]
+ -[AAUISignInViewController authenticationController:shouldContinueWithAuthenticationResults:error:forContext:completion:].cold.1
+ -[AAUISignInViewController authenticationController:shouldContinueWithAuthenticationResults:error:forContext:completion:].cold.2
+ -[AAUISignInViewController createButton]
+ -[AAUISignInViewController forgotButton]
+ -[AAUISignInViewController forgotOrCreateButton]
+ -[AAUISignInViewController initialHeight]
+ -[AAUISignInViewController setAKURLBag:]
+ -[AAUISignInViewController setAccountHelpStackView:]
+ -[AAUISignInViewController setCreateButton:]
+ -[AAUISignInViewController setForgotButton:]
+ -[AAUISignInViewController setForgotOrCreateButton:]
+ -[AAUISignInViewController setInitialHeight:]
+ -[AAUISignInViewController setTintColor:]
+ -[AAUISignInViewController tableView:heightForFooterInSection:]
+ -[AAUISignInViewController tintColor]
+ -[AAUISignInViewControllerTableFooterView naturalHeight]
+ -[AAUISignInViewControllerTableFooterView privacyLinkController]
+ -[AAUISignInViewControllerTableFooterView setPrivacyLinkController:]
+ -[AAUISignInViewControllerTableFooterView totalHeight]
+ -[UIImage(AppleAccountUI) _cropRectForRawImageOrientation:]
+ -[_AAUIDataclassOptionCache dataclassDetails]
+ -[_AAUIDataclassOptionCache setDataclassDetails:]
+ GCC_except_table41
+ GCC_except_table55
+ GCC_except_table72
+ _ACAccountDataclassHealth
+ _CGAffineTransformIdentity
+ _CGAffineTransformRotate
+ _CGAffineTransformTranslate
+ _CGRectApplyAffineTransform
+ _OBJC_CLASS_$_CNAvatarImageRendererSettings
+ _OBJC_CLASS_$_UINavigationBar
+ _OBJC_IVAR_$_AAUISignInController._akURLBag
+ _OBJC_IVAR_$_AAUISignInViewController._accountHelpStackView
+ _OBJC_IVAR_$_AAUISignInViewController._akURLBag
+ _OBJC_IVAR_$_AAUISignInViewController._createButton
+ _OBJC_IVAR_$_AAUISignInViewController._forgotButton
+ _OBJC_IVAR_$_AAUISignInViewController._forgotOrCreateButton
+ _OBJC_IVAR_$_AAUISignInViewController._initialHeight
+ _OBJC_IVAR_$_AAUISignInViewController._tintColor
+ _OBJC_IVAR_$__AAUIDataclassOptionCache._dataclassDetails
+ __OBJC_$_CLASS_METHODS__AAUIDataclassOptionCache
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_AKAppleIDAuthenticationDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AKAppleIDAuthenticationDelegate
+ __OBJC_$_PROTOCOL_REFS_AKAppleIDAuthenticationDelegate
+ __OBJC_LABEL_PROTOCOL_$_AKAppleIDAuthenticationDelegate
+ __OBJC_PROTOCOL_$_AKAppleIDAuthenticationDelegate
+ ___107-[AAUISignInController _attemptSignInForService:withAuthenticationResults:parentViewController:completion:]_block_invoke.166
+ ___107-[AAUISignInController _attemptSignInForService:withAuthenticationResults:parentViewController:completion:]_block_invoke.166.cold.1
+ ___49+[AAUISignInViewController _isRunningInMuseBuddy]_block_invoke
+ ___50-[AAUISignInViewController viewWillLayoutSubviews]_block_invoke_2
+ ___52-[AAUIProfilePictureStore meCardWithVisualIdentity:]_block_invoke.58
+ ___52-[AAUIProfilePictureStore meCardWithVisualIdentity:]_block_invoke.58.cold.1
+ ___52-[AAUIProfilePictureStore meCardWithVisualIdentity:]_block_invoke.58.cold.2
+ ___52-[AAUISignInViewController _setPasswordFieldHidden:]_block_invoke_5
+ ___52-[AAUISignInViewController _setPasswordFieldHidden:]_block_invoke_6
+ ___55+[_AAUIDataclassOptionCache _hasPrescriptionEnrollment]_block_invoke
+ ___62-[AAUIProfilePictureStore fetchProfilePictureForAccountOwner:]_block_invoke.37
+ ___62-[AAUIProfilePictureStore fetchProfilePictureForAccountOwner:]_block_invoke.37.cold.1
+ ___62-[AAUIProfilePictureStore fetchProfilePictureForAccountOwner:]_block_invoke.37.cold.2
+ ___62-[AAUIProfilePictureStore fetchProfilePictureForAccountOwner:]_block_invoke.38
+ ___62-[AAUIProfilePictureStore fetchProfilePictureForAccountOwner:]_block_invoke.38.cold.1
+ ___62-[AAUISignInViewController _attemptAuthenticationWithContext:]_block_invoke.221
+ ___67-[AAUIProfilePictureStore fetchRawImageAndCropRectForAccountOwner:]_block_invoke.43
+ ___70-[AAUISignInController _delegate_signInControllerFinishedWithResults:]_block_invoke.174
+ ___70-[AAUISignInController _delegate_signInControllerFinishedWithResults:]_block_invoke.174.cold.1
+ ___71-[AAUIProfilePictureStore profilePictureForAccountOwnerWithCompletion:]_block_invoke.33
+ ___71-[AAUIProfilePictureStore profilePictureForAccountOwnerWithCompletion:]_block_invoke.33.cold.1
+ ___71-[AAUIProfilePictureStore profilePictureForAccountOwnerWithCompletion:]_block_invoke.34
+ ___71-[AAUIProfilePictureStore profilePictureForAccountOwnerWithCompletion:]_block_invoke.34.cold.1
+ ___78-[AAUIProfilePictureStore fetchRawImageAndCropRectForFamilyMember:completion:]_block_invoke.46
+ ___79-[AAUISignInController _delegate_signInControllerDidCompleteWithSuccess:error:]_block_invoke.172
+ ___79-[AAUISignInController _delegate_signInControllerDidCompleteWithSuccess:error:]_block_invoke.172.cold.1
+ ___96-[AAUISignInController _mainQueue_continueSignInWithAuthenticationResults:parentViewController:]_block_invoke.136
+ ___96-[AAUISignInController _mainQueue_continueSignInWithAuthenticationResults:parentViewController:]_block_invoke.139
+ ___97-[AAUISignInController _attemptSignInForServices:withAuthenticationResults:parentViewController:]_block_invoke.162
+ ___99-[AAUISignInController _continueUsingControllerForAccount:serviceType:inViewController:completion:]_block_invoke.68
+ ___99-[AAUISignInController _continueUsingControllerForAccount:serviceType:inViewController:completion:]_block_invoke.72
+ ___block_literal_global.131
+ ___block_literal_global.165
+ ___block_literal_global.182
+ ___block_literal_global.187
+ ___block_literal_global.49
+ __hasPrescriptionEnrollment.onceToken
+ __isRunningInMuseBuddy.isRunningInMuseBuddy
+ __isRunningInMuseBuddy.onceToken
+ _get_witness_table 7SwiftUI19_ConditionalContentVyAA08ModifiedD0VyAEyAA6ButtonVyAEyAEyAA5ImageVAA18_AspectRatioLayoutVGAA11_ClipEffectVyAA6CircleVGGGAA06_FrameJ0VGAQGAEyAEyAlUGAQGGAA4ViewHPAwAA_HPAvAA_HPAsAA_HPyHC_AuA0O8ModifierHPyHCHC_AqAA0_HPyHCHC_AyAA_HPAxAA_HPAlAA_HPAiAA_HPyHC_AkAA0_HPyHCHC_AuAA0_HPyHCHC_AqAA0_HPyHCHCHC.2
+ _get_witness_table 7SwiftUI6VStackVyAA9TupleViewVyAA19_ConditionalContentVyAGyAA08ModifiedG0VyAIyAA6ButtonVyAIyAIyAA5ImageVAA18_AspectRatioLayoutVGAA11_ClipEffectVyAA6CircleVGGGAA06_FrameM0VGAUGAIyAIyApYGAUGGA2_G_ACyAEyAA4TextV_A5_SgtGGtGGAA0E0HPyHC.1
+ _objc_msgSend$_accountHelpStackView
+ _objc_msgSend$_cropRectForRawImageOrientation:
+ _objc_msgSend$_delegate_signInViewControllerDidCompleteWithAuthenticationResults:completionHandler:
+ _objc_msgSend$_hasPrescriptionEnrollment
+ _objc_msgSend$_initialHeight
+ _objc_msgSend$_updateExpandingViewInFooterForCellChange:
+ _objc_msgSend$akURLBag
+ _objc_msgSend$alertWithTitle:message:
+ _objc_msgSend$defaultSettingsWithCacheSize:skipContactLookup:
+ _objc_msgSend$forgotOrCreateButton
+ _objc_msgSend$imageOrientation
+ _objc_msgSend$imageWithCIImage:scale:orientation:
+ _objc_msgSend$initWithSettings:
+ _objc_msgSend$isWalrusRecoveryKeyAvailableWithCompletion:
+ _objc_msgSend$naturalHeight
+ _objc_msgSend$privacyLinkController
+ _objc_msgSend$setAKURLBag:
+ _objc_msgSend$setCustomTintColor:
+ _objc_msgSend$setForgotOrCreateButton:
+ _objc_msgSend$setLinkEnabled:
+ _objc_msgSend$setPreferredStyle:
+ _objc_msgSend$signInViewController:didCompleteWithAuthenticationResults:completionHandler:
+ _objc_msgSend$signInViewController:shouldContinueWithAuthenticationResults:error:forContext:completion:
+ _objc_msgSend$statusBarFrame
+ _objc_msgSend$totalHeight
+ _symbolic _____yAAy__________G_____y_____GG 7SwiftUI15ModifiedContentV AA5ImageV AA18_AspectRatioLayoutV AA11_ClipEffectV AA6CircleV
+ _symbolic _____yAAy_____yAAyAAy__________G_____y_____GGG_____GAHG 7SwiftUI15ModifiedContentV AA6ButtonV AA5ImageV AA18_AspectRatioLayoutV AA11_ClipEffectV AA6CircleV AA06_FrameI0V
+ _symbolic _____yAAy_____yABy_____yAByABy__________G_____y_____GGG_____GAIGAByAByAfLGAIGGAQG 7SwiftUI19_ConditionalContentV AA08ModifiedD0V AA6ButtonV AA5ImageV AA18_AspectRatioLayoutV AA11_ClipEffectV AA6CircleV AA06_FrameJ0V
+ _symbolic _____yAAy_____yABy_____yAByABy__________G_____y_____GGG_____GAIGAByAByAfLGAIGGAQG______y_____y______AUSgtGGt 7SwiftUI19_ConditionalContentV AA08ModifiedD0V AA6ButtonV AA5ImageV AA18_AspectRatioLayoutV AA11_ClipEffectV AA6CircleV AA06_FrameJ0V AA6VStackV AA9TupleViewV AA4TextV
+ _symbolic _____y___________y_____yADy_____yAEy_____yAEyAEy__________G_____y_____GGG_____GALGAEyAEyAiOGALGGATG______yACy______AWSgtGGtGG 7SwiftUI13_VariadicViewO4TreeV AA13_VStackLayoutV AA05TupleD0V AA19_ConditionalContentV AA08ModifiedJ0V AA6ButtonV AA5ImageV AA012_AspectRatioG0V AA11_ClipEffectV AA6CircleV AA06_FrameG0V AA0F0V AA4TextV
+ _symbolic _____y_____yAAyAAy__________G_____y_____GGG_____G 7SwiftUI15ModifiedContentV AA6ButtonV AA5ImageV AA18_AspectRatioLayoutV AA11_ClipEffectV AA6CircleV AA06_FrameI0V
+ _symbolic _____y_____yABy__________G_____y_____GGG 7SwiftUI6ButtonV AA15ModifiedContentV AA5ImageV AA18_AspectRatioLayoutV AA11_ClipEffectV AA6CircleV
+ _symbolic _____y_____yABy_____yAByABy__________G_____y_____GGG_____GAIGAByAByAfLGAIGG 7SwiftUI19_ConditionalContentV AA08ModifiedD0V AA6ButtonV AA5ImageV AA18_AspectRatioLayoutV AA11_ClipEffectV AA6CircleV AA06_FrameJ0V
+ _symbolic _____y_____yABy_____yAByABy__________G_____y_____GGG_____GAIGAByAByAfLGAIG_G 7SwiftUI19_ConditionalContentV7StorageO AA08ModifiedD0V AA6ButtonV AA5ImageV AA18_AspectRatioLayoutV AA11_ClipEffectV AA6CircleV AA06_FrameK0V
+ _symbolic _____y_____yABy_____yACy_____yACyACy__________G_____y_____GGG_____GAJGACyACyAgMGAJGGARG______yAAy______AUSgtGGtG 7SwiftUI9TupleViewV AA19_ConditionalContentV AA08ModifiedF0V AA6ButtonV AA5ImageV AA18_AspectRatioLayoutV AA11_ClipEffectV AA6CircleV AA06_FrameL0V AA6VStackV AA4TextV
+ _symbolic _____y_____y_____yACy_____yACyACy__________G_____y_____GGG_____GAJGACyACyAgMGAJGGAR_G 7SwiftUI19_ConditionalContentV7StorageO AC AA08ModifiedD0V AA6ButtonV AA5ImageV AA18_AspectRatioLayoutV AA11_ClipEffectV AA6CircleV AA06_FrameK0V
+ _symbolic _____y_____y_____yACy_____yADy_____yADyADy__________G_____y_____GGG_____GAKGADyADyAhNGAKGGASG_AAyABy______AUSgtGGtGG 7SwiftUI6VStackV AA9TupleViewV AA19_ConditionalContentV AA08ModifiedG0V AA6ButtonV AA5ImageV AA18_AspectRatioLayoutV AA11_ClipEffectV AA6CircleV AA06_FrameM0V AA4TextV
- -[AAUIDataclassPickerViewController constrainView:toFillHeaderFooterView:]
- -[AAUISignInViewController _actionButtonsStackView]
- -[AAUISignInViewController _delegate_signInViewControllerDidCompleteWithAuthenticationResults:]
- -[AAUISignInViewController _tableFooterView].cold.1
- -[AAUISignInViewController _updateExpandingViewInFooter]
- -[AAUISignInViewControllerTableFooterView naturalSize]
- GCC_except_table40
- GCC_except_table50
- GCC_except_table54
- GCC_except_table61
- ___107-[AAUISignInController _attemptSignInForService:withAuthenticationResults:parentViewController:completion:]_block_invoke.165
- ___107-[AAUISignInController _attemptSignInForService:withAuthenticationResults:parentViewController:completion:]_block_invoke.165.cold.1
- ___52-[AAUIProfilePictureStore meCardWithVisualIdentity:]_block_invoke.55
- ___52-[AAUIProfilePictureStore meCardWithVisualIdentity:]_block_invoke.55.cold.1
- ___52-[AAUIProfilePictureStore meCardWithVisualIdentity:]_block_invoke.55.cold.2
- ___62-[AAUIProfilePictureStore fetchProfilePictureForAccountOwner:]_block_invoke.34
- ___62-[AAUIProfilePictureStore fetchProfilePictureForAccountOwner:]_block_invoke.34.cold.1
- ___62-[AAUIProfilePictureStore fetchProfilePictureForAccountOwner:]_block_invoke.34.cold.2
- ___62-[AAUIProfilePictureStore fetchProfilePictureForAccountOwner:]_block_invoke.35
- ___62-[AAUIProfilePictureStore fetchProfilePictureForAccountOwner:]_block_invoke.35.cold.1
- ___67-[AAUIProfilePictureStore fetchRawImageAndCropRectForAccountOwner:]_block_invoke.40
- ___70-[AAUISignInController _delegate_signInControllerFinishedWithResults:]_block_invoke.173
- ___70-[AAUISignInController _delegate_signInControllerFinishedWithResults:]_block_invoke.173.cold.1
- ___71-[AAUIProfilePictureStore profilePictureForAccountOwnerWithCompletion:]_block_invoke.30
- ___71-[AAUIProfilePictureStore profilePictureForAccountOwnerWithCompletion:]_block_invoke.30.cold.1
- ___71-[AAUIProfilePictureStore profilePictureForAccountOwnerWithCompletion:]_block_invoke.31
- ___71-[AAUIProfilePictureStore profilePictureForAccountOwnerWithCompletion:]_block_invoke.31.cold.1
- ___78-[AAUIProfilePictureStore fetchRawImageAndCropRectForFamilyMember:completion:]_block_invoke.43
- ___79-[AAUISignInController _delegate_signInControllerDidCompleteWithSuccess:error:]_block_invoke.171
- ___79-[AAUISignInController _delegate_signInControllerDidCompleteWithSuccess:error:]_block_invoke.171.cold.1
- ___96-[AAUISignInController _mainQueue_continueSignInWithAuthenticationResults:parentViewController:]_block_invoke.135
- ___96-[AAUISignInController _mainQueue_continueSignInWithAuthenticationResults:parentViewController:]_block_invoke.138
- ___97-[AAUISignInController _attemptSignInForServices:withAuthenticationResults:parentViewController:]_block_invoke.161
- ___99-[AAUISignInController _continueUsingControllerForAccount:serviceType:inViewController:completion:]_block_invoke.67
- ___99-[AAUISignInController _continueUsingControllerForAccount:serviceType:inViewController:completion:]_block_invoke.71
- ___block_literal_global.119
- ___block_literal_global.162
- ___block_literal_global.177
- _get_witness_table 7SwiftUI19_ConditionalContentVyAA08ModifiedD0VyAEyAA6ButtonVyAEyAA5ImageVAA18_AspectRatioLayoutVGGAA06_FrameJ0VGAA11_ClipEffectVyAA6CircleVGGAEyAEyAlOGAUGGAA4ViewHPAvaZHPApaZHPAmaZHPyHC_AoA0O8ModifierHPyHCHC_AuAA_HPyHCHC_AxaZHPAwaZHPAlaZHPAiaZHPyHC_AkAA_HPyHCHC_AoAA_HPyHCHC_AuAA_HPyHCHCHC.2
- _get_witness_table 7SwiftUI6VStackVyAA9TupleViewVyAA19_ConditionalContentVyAGyAA08ModifiedG0VyAIyAA6ButtonVyAIyAA5ImageVAA18_AspectRatioLayoutVGGAA06_FrameM0VGAA11_ClipEffectVyAA6CircleVGGAIyAIyApSGAYGGA1_G_ACyAEyAA4TextV_A4_SgtGGtGGAA0E0HPyHC.1
- _objc_msgSend$_actionButtonsStackView
- _objc_msgSend$_delegate_signInViewControllerDidCompleteWithAuthenticationResults:
- _objc_msgSend$_updateExpandingViewInFooter
- _objc_msgSend$beginUpdates
- _objc_msgSend$endUpdates
- _objc_msgSend$imageWithCGImage:
- _objc_msgSend$imageWithCIImage:
- _objc_msgSend$isRecoveryKeyAvailableWithCompletion:
- _objc_msgSend$naturalSize
- _symbolic _____yAAy_____yAAy__________GG_____G_____y_____GG 7SwiftUI15ModifiedContentV AA6ButtonV AA5ImageV AA18_AspectRatioLayoutV AA06_FrameI0V AA11_ClipEffectV AA6CircleV
- _symbolic _____yAAy_____yABy_____yABy__________GG_____G_____y_____GGAByAByAfHGALGGAPG 7SwiftUI19_ConditionalContentV AA08ModifiedD0V AA6ButtonV AA5ImageV AA18_AspectRatioLayoutV AA06_FrameJ0V AA11_ClipEffectV AA6CircleV
- _symbolic _____yAAy_____yABy_____yABy__________GG_____G_____y_____GGAByAByAfHGALGGAPG______y_____y______ATSgtGGt 7SwiftUI19_ConditionalContentV AA08ModifiedD0V AA6ButtonV AA5ImageV AA18_AspectRatioLayoutV AA06_FrameJ0V AA11_ClipEffectV AA6CircleV AA6VStackV AA9TupleViewV AA4TextV
- _symbolic _____y___________y_____yADy_____yAEy_____yAEy__________GG_____G_____y_____GGAEyAEyAiKGAOGGASG______yACy______AVSgtGGtGG 7SwiftUI13_VariadicViewO4TreeV AA13_VStackLayoutV AA05TupleD0V AA19_ConditionalContentV AA08ModifiedJ0V AA6ButtonV AA5ImageV AA012_AspectRatioG0V AA06_FrameG0V AA11_ClipEffectV AA6CircleV AA0F0V AA4TextV
- _symbolic _____y_____yAAy__________GG_____G 7SwiftUI15ModifiedContentV AA6ButtonV AA5ImageV AA18_AspectRatioLayoutV AA06_FrameI0V
- _symbolic _____y_____yABy_____yABy__________GG_____G_____y_____GGAByAByAfHGALGG 7SwiftUI19_ConditionalContentV AA08ModifiedD0V AA6ButtonV AA5ImageV AA18_AspectRatioLayoutV AA06_FrameJ0V AA11_ClipEffectV AA6CircleV
- _symbolic _____y_____yABy_____yABy__________GG_____G_____y_____GGAByAByAfHGALG_G 7SwiftUI19_ConditionalContentV7StorageO AA08ModifiedD0V AA6ButtonV AA5ImageV AA18_AspectRatioLayoutV AA06_FrameK0V AA11_ClipEffectV AA6CircleV
- _symbolic _____y_____yABy_____yACy_____yACy__________GG_____G_____y_____GGACyACyAgIGAMGGAQG______yAAy______ATSgtGGtG 7SwiftUI9TupleViewV AA19_ConditionalContentV AA08ModifiedF0V AA6ButtonV AA5ImageV AA18_AspectRatioLayoutV AA06_FrameL0V AA11_ClipEffectV AA6CircleV AA6VStackV AA4TextV
- _symbolic _____y_____y__________GG 7SwiftUI6ButtonV AA15ModifiedContentV AA5ImageV AA18_AspectRatioLayoutV
- _symbolic _____y_____y_____yACy_____yACy__________GG_____G_____y_____GGACyACyAgIGAMGGAQ_G 7SwiftUI19_ConditionalContentV7StorageO AC AA08ModifiedD0V AA6ButtonV AA5ImageV AA18_AspectRatioLayoutV AA06_FrameK0V AA11_ClipEffectV AA6CircleV
- _symbolic _____y_____y_____yACy_____yADy_____yADy__________GG_____G_____y_____GGADyADyAhJGANGGARG_AAyABy______ATSgtGGtGG 7SwiftUI6VStackV AA9TupleViewV AA19_ConditionalContentV AA08ModifiedG0V AA6ButtonV AA5ImageV AA18_AspectRatioLayoutV AA06_FrameM0V AA11_ClipEffectV AA6CircleV AA4TextV
CStrings:
+ "\x02$!\x15"
+ "\x06\x11"
+ "\t\x15R\x172"
+ "@\"AAUIButton\""
+ "@\"AKURLBag\""
+ "@32@0:8@\"NSString\"16@\"NSString\"24"
+ "AKAppleIDAuthenticationDelegate"
+ "Authentication controller called back with auth results."
+ "B48@0:8@\"AKAppleIDAuthenticationController\"16@\"NSMutableDictionary\"24@\"NSError\"32@\"AKAppleIDAuthenticationContext\"40"
+ "Bailing due to error: %@"
+ "Calling delegate for should continue"
+ "SIGN_OUT_HEALTH_ROW_DETAIL_TEXT"
+ "T@\"AAUIButton\",W,N,V_createButton"
+ "T@\"AAUIButton\",W,N,V_forgotButton"
+ "T@\"AKURLBag\",&,N,SsetAKURLBag:,V_akURLBag"
+ "T@\"NSDictionary\",C,N,V_dataclassDetails"
+ "T@\"NSNumber\",&,N,V_initialHeight"
+ "T@\"OBPrivacyLinkController\",&,N,V_privacyLinkController"
+ "T@\"UIButton\",W,N,V_forgotOrCreateButton"
+ "T@\"UIColor\",&,N,V_tintColor"
+ "T@\"UIStackView\",&,N,V_accountHelpStackView"
+ "[AAUIProfilePictureStore initWithAppleAccount]: AppleAccount exists."
+ "[AAUIProfilePictureStore initWithGrandSlamSigner]: AppleAccount is nil. Getting the personID from grandSlam Account."
+ "[AAUIProfilePictureStore initWithGrandSlamSigner]: Getting AppleAccount with personID: %@, from Account Store"
+ "[AAUIProfilePictureStore updateCacheWithPhoto]: After updating Profile picture on the server successfully, tried updating the cache, but, cache did not update‼️"
+ "[AAUIProfilePictureStore updateCacheWithPhoto]: AppleAccount not found. Abort updateCacheWithPhoto"
+ "[AAUIProfilePictureStore updateCacheWithPhoto]: Cache has changed. Posting a notification."
+ "[AAUIProfilePictureStore updateCacheWithPhoto]: profilePictureForPersonID completed."
+ "[AAUIProfilePictureStore]: initWithGrandSlamSigner called."
+ "[AAUIProfilePictureStore]: updateCacheWithPhoto was called."
+ "[AAUIServerSuppliedProfilePictureCache entryForPersonID]: %@ Created entry %@"
+ "[AAUIServerSuppliedProfilePictureCache entryForPersonID]: %@ Found entry %@"
+ "_accountHelpStackView"
+ "_akURLBag"
+ "_createButton"
+ "_cropRectForRawImageOrientation:"
+ "_dataclassDetails"
+ "_delegate_signInViewControllerDidCompleteWithAuthenticationResults:completionHandler:"
+ "_forgotButton"
+ "_forgotOrCreateButton"
+ "_hasPrescriptionEnrollment"
+ "_initialHeight"
+ "_isRunningInMuseBuddy"
+ "_tintColor"
+ "_updateExpandingViewInFooterForCellChange:"
+ "accountHelpStackView"
+ "akURLBag"
+ "alertWithTitle:message:"
+ "authenticationController:shouldContinueWithAuthenticationResults:error:forContext:"
+ "authenticationController:shouldContinueWithAuthenticationResults:error:forContext:completion:"
+ "com.apple.MuseBuddy"
+ "continue-button"
+ "createButton"
+ "dataclassDetails"
+ "defaultSettingsWithCacheSize:skipContactLookup:"
+ "forgotButton"
+ "forgotOrCreateButton"
+ "imageOrientation"
+ "imageWithCIImage:scale:orientation:"
+ "initWithCGImage:scale:orientation:"
+ "initWithSettings:"
+ "initialHeight"
+ "isWalrusRecoveryKeyAvailableWithCompletion:"
+ "naturalHeight"
+ "privacyLinkController"
+ "setAKURLBag:"
+ "setAccountHelpStackView:"
+ "setCreateButton:"
+ "setCustomTintColor:"
+ "setDataclassDetails:"
+ "setForgotButton:"
+ "setForgotOrCreateButton:"
+ "setInitialHeight:"
+ "setLinkEnabled:"
+ "setPreferredStyle:"
+ "setPrivacyLinkController:"
+ "signInViewController:didCompleteWithAuthenticationResults:completionHandler:"
+ "signInViewController:shouldContinueWithAuthenticationResults:error:forContext:completion:"
+ "statusBarFrame"
+ "totalHeight"
+ "v40@0:8@\"AAUISignInViewController\"16@\"NSDictionary\"24@?<v@?>32"
+ "v56@0:8@\"AAUISignInViewController\"16@\"NSMutableDictionary\"24@\"NSError\"32@\"AKAppleIDAuthenticationContext\"40@?<v@?B>48"
+ "v56@0:8@\"AKAppleIDAuthenticationController\"16@\"NSMutableDictionary\"24@\"NSError\"32@\"AKAppleIDAuthenticationContext\"40@?<v@?B>48"
+ "{CGRect={CGPoint=dd}{CGSize=dd}}48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
+ "\xf01\xb3"
- "\x02$!\x14"
- "\t\x15Q\x16"
- "AAUIPPS entryForPersonID: %@ Created entry %@"
- "AAUIPPS entryForPersonID: %@ Found entry %@"
- "After updating Profile picture on the server successfully, tried updating the cache, but, cache did not update‼️"
- "Building table view"
- "Cache has changed. Posting a notification."
- "_delegate_signInViewControllerDidCompleteWithAuthenticationResults:"
- "_updateExpandingViewInFooter"
- "appleAccountServiceIcon"
- "beginUpdates"
- "endUpdates"
- "imageWithCGImage:"
- "imageWithCIImage:"
- "initWithCGImage:"
- "isRecoveryKeyAvailableWithCompletion:"
- "naturalSize"
- "profilePictureForPersonID completed."
- "updateCacheWithPhoto was called."
- "\xf01"

```
