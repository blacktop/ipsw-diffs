## FeedbackCore

> `/System/Library/PrivateFrameworks/FeedbackCore.framework/FeedbackCore`

```diff

-84.1.0.0.0
-  __TEXT.__text: 0x121c14
-  __TEXT.__auth_stubs: 0x23a0
-  __TEXT.__objc_methlist: 0x9104
-  __TEXT.__const: 0x1658
-  __TEXT.__cstring: 0xb0dc
-  __TEXT.__oslogstring: 0x8b8e
-  __TEXT.__gcc_except_tab: 0x13a8
+85.1.0.0.0
+  __TEXT.__text: 0x12a814
+  __TEXT.__auth_stubs: 0x2680
+  __TEXT.__objc_methlist: 0x947c
+  __TEXT.__const: 0x1948
+  __TEXT.__cstring: 0xb2cc
+  __TEXT.__oslogstring: 0x8e53
+  __TEXT.__gcc_except_tab: 0x13b4
   __TEXT.__ustring: 0xe6
-  __TEXT.__swift5_typeref: 0x248a
-  __TEXT.__constg_swiftt: 0x1174
-  __TEXT.__swift5_reflstr: 0x70e
-  __TEXT.__swift5_fieldmd: 0x874
-  __TEXT.__swift5_builtin: 0x3c
-  __TEXT.__swift5_assocty: 0xc0
-  __TEXT.__swift5_proto: 0xb0
-  __TEXT.__swift5_types: 0xb8
-  __TEXT.__swift5_capture: 0xc38
+  __TEXT.__swift5_typeref: 0x2f7a
+  __TEXT.__constg_swiftt: 0x13b8
+  __TEXT.__swift5_reflstr: 0x7ce
+  __TEXT.__swift5_fieldmd: 0x96c
+  __TEXT.__swift5_builtin: 0x50
+  __TEXT.__swift5_assocty: 0x108
+  __TEXT.__swift5_proto: 0xc0
+  __TEXT.__swift5_types: 0xcc
+  __TEXT.__swift5_capture: 0xc70
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__unwind_info: 0x47d4
-  __TEXT.__eh_frame: 0x1480
-  __TEXT.__objc_classname: 0x10ec
-  __TEXT.__objc_methname: 0x1aacb
-  __TEXT.__objc_methtype: 0x3ae1
-  __TEXT.__objc_stubs: 0x13560
-  __DATA_CONST.__got: 0x668
-  __DATA_CONST.__const: 0x3b18
-  __DATA_CONST.__objc_classlist: 0x488
+  __TEXT.__unwind_info: 0x4a4c
+  __TEXT.__eh_frame: 0x14d0
+  __TEXT.__objc_classname: 0x1114
+  __TEXT.__objc_methname: 0x1b2b3
+  __TEXT.__objc_methtype: 0x3b1e
+  __TEXT.__objc_stubs: 0x13940
+  __DATA_CONST.__got: 0x708
+  __DATA_CONST.__const: 0x3c00
+  __DATA_CONST.__objc_classlist: 0x4a0
   __DATA_CONST.__objc_catlist: 0xb8
   __DATA_CONST.__objc_protolist: 0x238
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x18100
-  __DATA_CONST.__objc_selrefs: 0x6710
-  __DATA_CONST.__objc_arraydata: 0x4b8
-  __AUTH_CONST.__cfstring: 0x89a0
-  __AUTH_CONST.__objc_const: 0x3c98
-  __AUTH_CONST.__const: 0x45e8
-  __AUTH_CONST.__objc_intobj: 0x2b8
+  __DATA_CONST.__objc_const: 0x19630
+  __DATA_CONST.__objc_selrefs: 0x68b0
+  __DATA_CONST.__objc_arraydata: 0x4d0
+  __AUTH_CONST.__cfstring: 0x8a80
+  __AUTH_CONST.__objc_const: 0x3d70
+  __AUTH_CONST.__const: 0x48f0
+  __AUTH_CONST.__objc_intobj: 0x2e8
   __AUTH_CONST.__objc_dictobj: 0xa0
-  __AUTH_CONST.__objc_arrayobj: 0x480
-  __AUTH_CONST.__auth_got: 0x11e0
-  __AUTH.__objc_data: 0x40b8
-  __AUTH.__data: 0x600
+  __AUTH_CONST.__objc_arrayobj: 0x498
+  __AUTH_CONST.__auth_got: 0x1350
+  __AUTH.__objc_data: 0x42e0
+  __AUTH.__data: 0x790
   __DATA.__objc_protorefs: 0xa0
-  __DATA.__objc_classrefs: 0x830
-  __DATA.__objc_superrefs: 0x270
-  __DATA.__objc_ivar: 0x640
+  __DATA.__objc_classrefs: 0x840
+  __DATA.__objc_superrefs: 0x278
+  __DATA.__objc_ivar: 0x67c
   __DATA.__objc_data: 0x128
-  __DATA.__data: 0x23c0
-  __DATA.__bss: 0x19c0
+  __DATA.__data: 0x25e0
+  __DATA.__bss: 0x1bf0
   __DATA.__common: 0x128
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox

   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftObservation.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: FB31B94C-21B2-3E9A-9613-39E72B8C8BBE
-  Functions: 6507
-  Symbols:   14154
-  CStrings:  8708
+  UUID: 4B5E4CDC-4ED7-3E28-8E21-F80D80757F15
+  Functions: 6785
+  Symbols:   14458
+  CStrings:  8841
 
Symbols:
+ +[FBKAttachmentViewingControllerSelector imageControllerForAttachment:]
+ +[FBKAttachmentViewingControllerSelector imageControllerForAttachment:].cold.1
+ +[FBKFilePromise displaySortDescriptors]
+ +[FBKFilePromiseStub fetchRequest]
+ +[FBKImageAttachmentViewController canDisplayURL:]
+ -[FBKAttachmentCell horizontalFrameInset]
+ -[FBKAttachmentCell setFrame:]
+ -[FBKAttachmentCell setHorizontalFrameInset:]
+ -[FBKBugFormTableViewController alternateImagePreviewEnabled]
+ -[FBKBugFormTableViewController cancelButton]
+ -[FBKBugFormTableViewController disableAccountSwitching]
+ -[FBKBugFormTableViewController identifierOfLastDeviceSection]
+ -[FBKBugFormTableViewController maxInlineChoices]
+ -[FBKBugFormTableViewController setAlternateImagePreviewEnabled:]
+ -[FBKBugFormTableViewController setCancelButton:]
+ -[FBKBugFormTableViewController setDisableAccountSwitching:]
+ -[FBKBugFormTableViewController setIdentifierOfLastDeviceSection:]
+ -[FBKBugFormTableViewController setMaxInlineChoices:]
+ -[FBKBugFormTableViewController setShouldShowAttachmentButton:]
+ -[FBKBugFormTableViewController setUseInlineChoices:]
+ -[FBKBugFormTableViewController shouldShowAttachmentButton]
+ -[FBKBugFormTableViewController useInlineChoices]
+ -[FBKContentItem canDeleteFiles]
+ -[FBKData deleteFilePromiseWithUUID:object:completion:]
+ -[FBKDeviceDisplayCell horizontalFrameInset]
+ -[FBKDeviceDisplayCell setFrame:]
+ -[FBKDeviceDisplayCell setHorizontalFrameInset:]
+ -[FBKFilePromise UUIDString]
+ -[FBKFilePromise canDelete]
+ -[FBKFilePromise createdAtDate]
+ -[FBKFilePromise filename]
+ -[FBKFilePromise status]
+ -[FBKFilePromiseStub UUIDString]
+ -[FBKFilePromiseStub canDelete]
+ -[FBKFilePromiseStub createdAtDate]
+ -[FBKFilePromiseStub filename]
+ -[FBKImageAttachmentViewController .cxx_destruct]
+ -[FBKImageAttachmentViewController didReceiveMemoryWarning]
+ -[FBKImageAttachmentViewController imageURL]
+ -[FBKImageAttachmentViewController imageView]
+ -[FBKImageAttachmentViewController loadImage]
+ -[FBKImageAttachmentViewController loadImage].cold.1
+ -[FBKImageAttachmentViewController scrollView]
+ -[FBKImageAttachmentViewController setImageURL:]
+ -[FBKImageAttachmentViewController setImageUrl:]
+ -[FBKImageAttachmentViewController setImageView:]
+ -[FBKImageAttachmentViewController setScrollView:]
+ -[FBKImageAttachmentViewController viewDidLoad]
+ -[FBKImageAttachmentViewController viewForZoomingInScrollView:]
+ -[FBKImageAttachmentViewController viewWillAppear:]
+ -[FBKLoginManager _completeAuthenticationWith:credentialToken:completion:]
+ -[FBKQuestion visibleChoiceSetExcludingPrompt]
+ -[FBKQuestionAnswerCell answerTextViewAccessoryImageView]
+ -[FBKQuestionAnswerCell answerTextViewTopConstraint]
+ -[FBKQuestionAnswerCell setAnswerTextViewAccessoryImageView:]
+ -[FBKQuestionAnswerCell setAnswerTextViewTopConstraint:]
+ -[FBKSeedPortalAPI deleteFilePromiseWithUUID:completion:]
+ -[FBKSeedPortalAPI filePromiseDeleteURLForUUID:]
+ -[FBKTeamPermissions canDelete]
+ -[FBKTeamPermissions initWithView:respond:close:download:delete:assign:demote:]
+ -[UITableViewController(FBKDocumentPresenter) presentAttachmentWithImagePush:fromIndexPath:]
+ -[UITableViewController(FBKDocumentPresenter) presentAttachmentWithImagePush:fromIndexPath:].cold.1
+ GCC_except_table102
+ GCC_except_table117
+ GCC_except_table141
+ GCC_except_table49
+ GCC_except_table54
+ GCC_except_table63
+ GCC_except_table71
+ GCC_except_table78
+ GCC_except_table99
+ _CGRectGetMinX
+ _CGRectGetMinY
+ _FBKDownloadableFilePromisesSelectVisible
+ _FBKImageAttachmentStoryboardID
+ _FBKInlineChoicesLimitDisabled
+ _FBKMaxInlineChoices
+ _OBJC_CLASS_$_FBKImageAttachmentViewController
+ _OBJC_CLASS_$__TtC12FeedbackCore21FBKExpandedChoiceCell
+ _OBJC_IVAR_$_FBKAttachmentCell._horizontalFrameInset
+ _OBJC_IVAR_$_FBKBugFormTableViewController._alternateImagePreviewEnabled
+ _OBJC_IVAR_$_FBKBugFormTableViewController._cancelButton
+ _OBJC_IVAR_$_FBKBugFormTableViewController._disableAccountSwitching
+ _OBJC_IVAR_$_FBKBugFormTableViewController._identifierOfLastDeviceSection
+ _OBJC_IVAR_$_FBKBugFormTableViewController._maxInlineChoices
+ _OBJC_IVAR_$_FBKBugFormTableViewController._shouldShowAttachmentButton
+ _OBJC_IVAR_$_FBKBugFormTableViewController._useInlineChoices
+ _OBJC_IVAR_$_FBKDeviceDisplayCell._horizontalFrameInset
+ _OBJC_IVAR_$_FBKImageAttachmentViewController._imageURL
+ _OBJC_IVAR_$_FBKImageAttachmentViewController._imageView
+ _OBJC_IVAR_$_FBKImageAttachmentViewController._scrollView
+ _OBJC_IVAR_$_FBKQuestionAnswerCell._answerTextViewAccessoryImageView
+ _OBJC_IVAR_$_FBKQuestionAnswerCell._answerTextViewTopConstraint
+ _OBJC_IVAR_$_FBKTeamPermissions._canDelete
+ _OBJC_METACLASS_$_FBKImageAttachmentViewController
+ _OBJC_METACLASS_$__TtC12FeedbackCore21FBKExpandedChoiceCell
+ __DATA__TtC12FeedbackCore19ChoiceCellViewModel
+ __DATA__TtC12FeedbackCore21FBKExpandedChoiceCell
+ __IVARS__TtC12FeedbackCore19ChoiceCellViewModel
+ __IVARS__TtC12FeedbackCore21FBKExpandedChoiceCell
+ __METACLASS_DATA__TtC12FeedbackCore19ChoiceCellViewModel
+ __METACLASS_DATA__TtC12FeedbackCore21FBKExpandedChoiceCell
+ __OBJC_$_CLASS_METHODS_FBKFilePromiseStub
+ __OBJC_$_CLASS_METHODS_FBKImageAttachmentViewController
+ __OBJC_$_CLASS_METHODS__TtC12FeedbackCore21FBKExpandedChoiceCell
+ __OBJC_$_INSTANCE_METHODS_FBKFilePromiseStub
+ __OBJC_$_INSTANCE_METHODS_FBKImageAttachmentViewController
+ __OBJC_$_INSTANCE_METHODS__TtC12FeedbackCore21FBKExpandedChoiceCell
+ __OBJC_$_INSTANCE_VARIABLES_FBKImageAttachmentViewController
+ __OBJC_$_PROP_LIST_FBKFilePromiseStub
+ __OBJC_$_PROP_LIST_FBKImageAttachmentViewController
+ __OBJC_$_PROTOCOL_REFS_FBKDownloadableFilePromise
+ __OBJC_CLASS_PROTOCOLS_$_FBKImageAttachmentViewController
+ __OBJC_CLASS_RO_$_FBKImageAttachmentViewController
+ __OBJC_METACLASS_RO_$_FBKImageAttachmentViewController
+ __PROPERTIES__TtC12FeedbackCore21FBKExpandedChoiceCell
+ __PROTOCOLS__TtC12FeedbackCore21FBKExpandedChoiceCell
+ __PROTOCOLS__TtC12FeedbackCore21FBKExpandedChoiceCell.24
+ ___39-[FBKBugFormTableViewController submit]_block_invoke.223
+ ___39-[FBKBugFormTableViewController submit]_block_invoke.223.cold.1
+ ___39-[FBKBugFormTableViewController submit]_block_invoke.230
+ ___39-[FBKBugFormTableViewController submit]_block_invoke.232
+ ___46-[FBKQuestion visibleChoiceSetExcludingPrompt]_block_invoke
+ ___55-[FBKData deleteFilePromiseWithUUID:object:completion:]_block_invoke
+ ___55-[FBKData deleteFilePromiseWithUUID:object:completion:]_block_invoke_2
+ ___55-[FBKData deleteFilePromiseWithUUID:object:completion:]_block_invoke_2.cold.1
+ ___55-[FBKData deleteFilePromiseWithUUID:object:completion:]_block_invoke_2.cold.2
+ ___56-[FBKLoginManager loginWithSystemAccountWithCompletion:]_block_invoke.73
+ ___56-[FBKLoginManager loginWithSystemAccountWithCompletion:]_block_invoke.73.cold.1
+ ___56-[FBKLoginManager loginWithSystemAccountWithCompletion:]_block_invoke.73.cold.2
+ ___56-[FBKLoginManager loginWithSystemAccountWithCompletion:]_block_invoke.74.cold.1
+ ___56-[FBKLoginManager loginWithSystemAccountWithCompletion:]_block_invoke.74.cold.2
+ ___56-[FBKLoginManager loginWithSystemAccountWithCompletion:]_block_invoke.74.cold.3
+ ___56-[FBKLoginManager loginWithSystemAccountWithCompletion:]_block_invoke.75
+ ___56-[FBKLoginManager loginWithSystemAccountWithCompletion:]_block_invoke.cold.1
+ ___56-[FBKLoginManager loginWithSystemAccountWithCompletion:]_block_invoke.cold.2
+ ___57-[FBKBugFormTableViewController beginPresubmissionCheck:]_block_invoke.181
+ ___57-[FBKBugFormTableViewController beginPresubmissionCheck:]_block_invoke.185
+ ___57-[FBKBugFormTableViewController beginPresubmissionCheck:]_block_invoke.189
+ ___57-[FBKBugFormTableViewController beginPresubmissionCheck:]_block_invoke.196
+ ___57-[FBKBugFormTableViewController beginPresubmissionCheck:]_block_invoke.200
+ ___57-[FBKBugFormTableViewController beginPresubmissionCheck:]_block_invoke_2.201
+ ___57-[FBKSeedPortalAPI deleteFilePromiseWithUUID:completion:]_block_invoke
+ ___57-[FBKSeedPortalAPI deleteFilePromiseWithUUID:completion:]_block_invoke_2
+ ___61-[FBKSeedPortalAPI getFormResponseStubWithID:withCompletion:]_block_invoke.225
+ ___61-[FBKSeedPortalAPI updateContentItemsForTeam:withCompletion:]_block_invoke.187
+ ___61-[FBKSeedPortalAPI updateContentItemsForTeam:withCompletion:]_block_invoke.187.cold.1
+ ___67-[FBKSeedPortalAPI fetchAnnouncementForContentItem:withCompletion:]_block_invoke.237
+ ___68-[FBKSeedPortalAPI getFileDownloadURLForFilePromiseUUID:completion:]_block_invoke.255
+ ___71-[FBKLoginManager _loginWithUsername:authenticationResults:completion:]_block_invoke.84
+ ___73-[FBKSeedPortalAPI updateFormItemsForUser:inTeam:formTat:withCompletion:]_block_invoke.160
+ ___73-[FBKSeedPortalAPI updateFormItemsForUser:inTeam:formTat:withCompletion:]_block_invoke.160.cold.1
+ ___73-[FBKSeedPortalAPI updateFormItemsForUser:inTeam:formTat:withCompletion:]_block_invoke.160.cold.2
+ ___73-[FBKSeedPortalAPI updateFormItemsForUser:inTeam:formTat:withCompletion:]_block_invoke.160.cold.3
+ ___73-[FBKSeedPortalAPI updateFormItemsForUser:inTeam:formTat:withCompletion:]_block_invoke.162
+ ___74-[FBKLoginManager _completeAuthenticationWith:credentialToken:completion:]_block_invoke
+ ___74-[FBKLoginManager _completeAuthenticationWith:credentialToken:completion:]_block_invoke.80
+ ___74-[FBKLoginManager _completeAuthenticationWith:credentialToken:completion:]_block_invoke_2
+ ___74-[FBKLoginManager _completeAuthenticationWith:credentialToken:completion:]_block_invoke_2.81
+ ___74-[FBKLoginManager _completeAuthenticationWith:credentialToken:completion:]_block_invoke_3
+ ___75-[FBKBugFormTableViewController _reallyChangeToBugFormStub:withTeam:force:]_block_invoke.152
+ ___75-[FBKBugFormTableViewController _reallyChangeToBugFormStub:withTeam:force:]_block_invoke.152.cold.1
+ ___75-[FBKBugFormTableViewController _reallyChangeToBugFormStub:withTeam:force:]_block_invoke.160
+ ___75-[FBKBugFormTableViewController _reallyChangeToBugFormStub:withTeam:force:]_block_invoke.164
+ ___75-[FBKBugFormTableViewController alertControllerForDismissWithLaunchAction:]_block_invoke.270
+ ___75-[FBKBugFormTableViewController alertControllerForDismissWithLaunchAction:]_block_invoke.272
+ ___79-[FBKSeedPortalAPI createFormResponseForBugForm:inTeam:appToken:success:error:]_block_invoke.208
+ ___87-[FBKSeedPortalAPI fetchBugFormWithID:forTeamID:requestPlugIns:appToken:success:error:]_block_invoke.200
+ ___89-[FBKLoginManager autoLoginWithUserID:userName:deviceToken:usesSystemAccount:completion:]_block_invoke.82
+ ___89-[FBKLoginManager autoLoginWithUserID:userName:deviceToken:usesSystemAccount:completion:]_block_invoke_2.83
+ ___FBKDownloadableFilePromisesSelectVisible_block_invoke
+ ___block_descriptor_32_e38_B16?0"<FBKDownloadableFilePromise>"8l
+ ___block_descriptor_56_e8_32s40s48bs_e20_v24?0q8"NSError"16ls32l8s48l8s40l8
+ ___block_descriptor_56_e8_32s40s48bs_e30_v24?0"NSString"8"NSError"16ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48bs_e30_v24?0"NSString"8"NSError"16ls48l8s32l8s40l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e17_v16?0"NSError"8ls32l8s40l8s48l8s56l8
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
+ ___block_literal_global.118
+ ___block_literal_global.205
+ ___block_literal_global.259
+ ___block_literal_global.439
+ ___block_literal_global.441
+ ___block_literal_global.641
+ ___block_literal_global.87
+ __unnamed_array_storage.218
+ __unnamed_array_storage.219
+ _associated conformance 12FeedbackCore10ChoiceCellV7SwiftUI4ViewAA4BodyAdEP_AdE
+ _associated conformance 12FeedbackCore19EvenWidthGridLayoutV7SwiftUI0F0AaD10Animatable
+ _associated conformance 12FeedbackCore19EvenWidthGridLayoutV7SwiftUI10AnimatableAA0I4DataAdEP_AD16VectorArithmetic
+ _get_witness_table 7SwiftUI15ModifiedContentVyAA6HStackVyAA9TupleViewVyACyAA0G0PAAE10fontWeightyQrAA4FontV0I0VSgFQOyACyACyACyAA5ImageVAA20_ColorMultiplyEffectVGAA18_AspectRatioLayoutVGAA06_FrameQ0VG_Qo_AA21_TraitWritingModifierVyAA010TransitionS3KeyVGGSg_ACyACyACyAA6VStackVyAGyAA4TextV_AA09_VariadicG0O4TreeVy_AA01_Q4RootVy12FeedbackCore013EvenWidthGridQ0VGAA7ForEachVySaySo17FBKQuestionChoiceCGA24_ACyACyAiAE11toggleStyleyQrqd__AA11ToggleStyleRd__lFQOyAA6ToggleVyACyA10_AA05_FlexrQ0VGG_AA17ButtonToggleStyleVQo_A1_yAA08TagValuesW0VyA24_GGGAA08_PaddingQ0VGGGtGGA31_GAYGA43_GtGGA31_GAaHHPA53_AaHHPyHC_A31_AA0gU0HPyHCHC.65
+ _keypath_get.18Tm
+ _objc_msgSend$_completeAuthenticationWith:credentialToken:completion:
+ _objc_msgSend$accountStore
+ _objc_msgSend$aida_renewCredentialsForAccount:services:completion:
+ _objc_msgSend$aida_tokenForService:completionHandler:
+ _objc_msgSend$canDelete
+ _objc_msgSend$clearColor
+ _objc_msgSend$defaultStore
+ _objc_msgSend$deleteFilePromiseWithUUID:completion:
+ _objc_msgSend$disableRemoteHoverEffect
+ _objc_msgSend$disableRemoteHoverEffectAndClearBackground
+ _objc_msgSend$filePromiseDeleteURLForUUID:
+ _objc_msgSend$filename
+ _objc_msgSend$identifierOfLastDeviceSection
+ _objc_msgSend$imageControllerForAttachment:
+ _objc_msgSend$imageURL
+ _objc_msgSend$isPrompt
+ _objc_msgSend$loadImage
+ _objc_msgSend$maxInlineChoices
+ _objc_msgSend$presentAttachmentWithImagePush:fromIndexPath:
+ _objc_msgSend$scrollView
+ _objc_msgSend$setAlwaysBounceHorizontal:
+ _objc_msgSend$setAlwaysBounceVertical:
+ _objc_msgSend$setClipsToBounds:
+ _objc_msgSend$setHorizontalFrameInset:
+ _objc_msgSend$setIdentifierOfLastDeviceSection:
+ _objc_msgSend$setImageURL:
+ _objc_msgSend$setImageUrl:
+ _objc_msgSend$setMaximumZoomScale:
+ _objc_msgSend$setMinimumZoomScale:
+ _objc_msgSend$setMultipleTouchEnabled:
+ _objc_msgSend$setShowsHorizontalScrollIndicator:
+ _objc_msgSend$setShowsVerticalScrollIndicator:
+ _objc_msgSend$shouldShowAttachmentButton
+ _objc_msgSend$updateCellContent
+ _objc_msgSend$visibleChoiceSetExcludingPrompt
+ _objectdestroy.54Tm
+ _symbolic $s7SwiftUI10AnimatableP
+ _symbolic $s7SwiftUI6LayoutP
+ _symbolic Si6offset______7elementt 7SwiftUI13LayoutSubviewV
+ _symbolic Si6offset______7elementtSg 7SwiftUI13LayoutSubviewV
+ _symbolic So17FBKQuestionChoiceC
+ _symbolic _____ 11Observation0A9RegistrarV
+ _symbolic _____ 12CoreGraphics7CGFloatV
+ _symbolic _____ 12FeedbackCore10ChoiceCellV
+ _symbolic _____ 12FeedbackCore19ChoiceCellViewModelC
+ _symbolic _____ 12FeedbackCore19EvenWidthGridLayoutV
+ _symbolic _____ 12FeedbackCore21FBKExpandedChoiceCellC
+ _symbolic _____ 7SwiftUI19EmptyAnimatableDataV
+ _symbolic _____ So6CGSizeV
+ _symbolic _____Sg 12FeedbackCore19ChoiceCellViewModelC
+ _symbolic _____Sg 7SwiftUI13LayoutSubviewV
+ _symbolic _____Sg 7SwiftUI5ImageV21TemplateRenderingModeO
+ _symbolic _____SgXw 12FeedbackCore21FBKExpandedChoiceCellC
+ _symbolic ___________y______y_____G_____ySaySo17FBKQuestionChoiceCGAH_____yAJy_____y_____yAJyAA_____GG______Qo______y_____yAHGGG_____GGGt 7SwiftUI4TextV AA13_VariadicViewO4TreeV AA11_LayoutRootV 12FeedbackCore013EvenWidthGridG0V AA7ForEachV AA15ModifiedContentV AA0E0PAAE11toggleStyleyQrqd__AA06ToggleS0Rd__lFQO AA0T0V AA010_FlexFrameG0V AA06ButtontS0V AA21_TraitWritingModifierV AA08TagValueX3KeyV AA08_PaddingG0V
+ _symbolic _____yAAyAAy__________G_____G_____G 7SwiftUI15ModifiedContentV AA5ImageV AA20_ColorMultiplyEffectV AA18_AspectRatioLayoutV AA06_FrameK0V
+ _symbolic _____yAAyAAy_____y_____y___________y______y_____G_____ySaySo17FBKQuestionChoiceCGAkAyAAy_____y_____yAAyAD_____GG______Qo______y_____yAKGGG_____GGGtGGANG_____GAXG 7SwiftUI15ModifiedContentV AA6VStackV AA9TupleViewV AA4TextV AA09_VariadicG0O4TreeV AA11_LayoutRootV 12FeedbackCore013EvenWidthGridK0V AA7ForEachV AA0G0PAAE11toggleStyleyQrqd__AA06ToggleU0Rd__lFQO AA0V0V AA010_FlexFrameK0V AA06ButtonvU0V AA21_TraitWritingModifierV AA08TagValueZ3KeyV AA08_PaddingK0V AA01_xK0V
+ _symbolic _____yAAy__________G_____G 7SwiftUI15ModifiedContentV AA5ImageV AA20_ColorMultiplyEffectV AA18_AspectRatioLayoutV
+ _symbolic _____yAAy_____y_____yAAy__________GG______Qo______y_____ySo17FBKQuestionChoiceCGGG_____G 7SwiftUI15ModifiedContentV AA4ViewPAAE11toggleStyleyQrqd__AA06ToggleG0Rd__lFQO AA0H0V AA4TextV AA16_FlexFrameLayoutV AA06ButtonhG0V AA21_TraitWritingModifierV AA08TagValueN3KeyV AA08_PaddingL0V
+ _symbolic _____yAAy_____y_____y___________y______y_____G_____ySaySo17FBKQuestionChoiceCGAkAyAAy_____y_____yAAyAD_____GG______Qo______y_____yAKGGG_____GGGtGGANG_____G 7SwiftUI15ModifiedContentV AA6VStackV AA9TupleViewV AA4TextV AA09_VariadicG0O4TreeV AA11_LayoutRootV 12FeedbackCore013EvenWidthGridK0V AA7ForEachV AA0G0PAAE11toggleStyleyQrqd__AA06ToggleU0Rd__lFQO AA0V0V AA010_FlexFrameK0V AA06ButtonvU0V AA21_TraitWritingModifierV AA08TagValueZ3KeyV AA08_PaddingK0V AA01_xK0V
+ _symbolic _____y_____G s16IndexingIteratorV 7SwiftUI14LayoutSubviewsV
+ _symbolic _____y_____G s18EnumeratedSequenceV 7SwiftUI14LayoutSubviewsV
+ _symbolic _____y_____G s23_ContiguousArrayStorageC So6CGSizeV
+ _symbolic _____y______G s18EnumeratedSequenceV8IteratorV 7SwiftUI14LayoutSubviewsV
+ _symbolic _____y__________G 7SwiftUI15ModifiedContentV AA5ImageV AA20_ColorMultiplyEffectV
+ _symbolic _____y__________G 7SwiftUI22UIHostingConfigurationV 12FeedbackCore10ChoiceCellV AA9EmptyViewV
+ _symbolic _____y___________y______AAy______y_____G_____ySaySo17FBKQuestionChoiceCGAJ_____yALy_____y_____yALyAD_____GG______Qo______y_____yAJGGG_____GGGtGG 7SwiftUI13_VariadicViewO4TreeV AA13_VStackLayoutV AA05TupleD0V AA4TextV AA01_G4RootV 12FeedbackCore013EvenWidthGridG0V AA7ForEachV AA15ModifiedContentV AA0D0PAAE11toggleStyleyQrqd__AA06ToggleU0Rd__lFQO AA0V0V AA010_FlexFrameG0V AA06ButtonvU0V AA21_TraitWritingModifierV AA08TagValueZ3KeyV AA08_PaddingG0V
+ _symbolic _____y___________y_____y_____yADyADyADy__________G_____G_____G_Qo______y_____GGSg_ADyADyADy_____yACy______AAy______y_____G_____ySaySo17FBKQuestionChoiceCGAyDyADy_____y_____yADyAS_____GG______Qo_AMy_____yAYGGG_____GGGtGGA0_GAJGA9_GtGG 7SwiftUI13_VariadicViewO4TreeV AA13_HStackLayoutV AA05TupleD0V AA15ModifiedContentV AA0D0PAAE10fontWeightyQrAA4FontV0L0VSgFQO AA5ImageV AA20_ColorMultiplyEffectV AA012_AspectRatioG0V AA06_FrameG0V AA21_TraitWritingModifierV AA010TransitionU3KeyV AA6VStackV AA4TextV AA01_G4RootV 12FeedbackCore013EvenWidthGridG0V AA7ForEachV AmAE11toggleStyleyQrqd__AA11ToggleStyleRd__lFQO AA6ToggleV AA05_FlextG0V AA17ButtonToggleStyleV AA08TagValueuY0V AA08_PaddingG0V
+ _symbolic _____y______y_____G_____ySaySo17FBKQuestionChoiceCGAG_____yAIy_____y_____yAIy__________GG______Qo______y_____yAGGGG_____GGG 7SwiftUI13_VariadicViewO4TreeV AA11_LayoutRootV 12FeedbackCore013EvenWidthGridF0V AA7ForEachV AA15ModifiedContentV AA0D0PAAE11toggleStyleyQrqd__AA06ToggleR0Rd__lFQO AA0S0V AA4TextV AA010_FlexFrameF0V AA06ButtonsR0V AA21_TraitWritingModifierV AA08TagValueX3KeyV AA08_PaddingF0V
+ _symbolic _____y_____yAAyAAyAAy__________G_____G_____G_Qo______y_____GG 7SwiftUI15ModifiedContentV AA4ViewPAAE10fontWeightyQrAA4FontV0G0VSgFQO AA5ImageV AA20_ColorMultiplyEffectV AA18_AspectRatioLayoutV AA06_FrameO0V AA21_TraitWritingModifierV AA010TransitionQ3KeyV
+ _symbolic _____y_____yAAyAAyAAy__________G_____G_____G_Qo______y_____GGSg 7SwiftUI15ModifiedContentV AA4ViewPAAE10fontWeightyQrAA4FontV0G0VSgFQO AA5ImageV AA20_ColorMultiplyEffectV AA18_AspectRatioLayoutV AA06_FrameO0V AA21_TraitWritingModifierV AA010TransitionQ3KeyV
+ _symbolic _____y_____yAAyAAyAAy__________G_____G_____G_Qo______y_____GGSg_AAyAAyAAy_____y_____y___________y______y_____G_____ySaySo17FBKQuestionChoiceCGAxAyAAy_____y_____yAAyAQ_____GG______Qo_AJy_____yAXGGG_____GGGtGGA_GAGGA8_Gt 7SwiftUI15ModifiedContentV AA4ViewPAAE10fontWeightyQrAA4FontV0G0VSgFQO AA5ImageV AA20_ColorMultiplyEffectV AA18_AspectRatioLayoutV AA06_FrameO0V AA21_TraitWritingModifierV AA010TransitionQ3KeyV AA6VStackV AA05TupleE0V AA4TextV AA09_VariadicE0O4TreeV AA01_O4RootV 12FeedbackCore013EvenWidthGridO0V AA7ForEachV AeAE11toggleStyleyQrqd__AA11ToggleStyleRd__lFQO AA6ToggleV AA05_FlexpO0V AA17ButtonToggleStyleV AA08TagValueqU0V AA08_PaddingO0V
+ _symbolic _____y_____yAAyAAy__________G_____G_____G_Qo_ 7SwiftUI4ViewPAAE10fontWeightyQrAA4FontV0E0VSgFQO AA15ModifiedContentV AA5ImageV AA20_ColorMultiplyEffectV AA18_AspectRatioLayoutV AA06_FrameO0V
+ _symbolic _____y_____ySo17FBKQuestionChoiceCGG 7SwiftUI21_TraitWritingModifierV AA08TagValueC3KeyV
+ _symbolic _____y_____y__________GG 7SwiftUI6ToggleV AA15ModifiedContentV AA4TextV AA16_FlexFrameLayoutV
+ _symbolic _____y_____y___________y______y_____G_____ySaySo17FBKQuestionChoiceCGAJ_____yALy_____y_____yALyAC_____GG______Qo______y_____yAJGGG_____GGGtGG 7SwiftUI6VStackV AA9TupleViewV AA4TextV AA09_VariadicE0O4TreeV AA11_LayoutRootV 12FeedbackCore013EvenWidthGridI0V AA7ForEachV AA15ModifiedContentV AA0E0PAAE11toggleStyleyQrqd__AA06ToggleU0Rd__lFQO AA0V0V AA010_FlexFrameI0V AA06ButtonvU0V AA21_TraitWritingModifierV AA08TagValueZ3KeyV AA08_PaddingI0V
+ _symbolic _____y_____y_____yAAy__________GG______Qo______y_____ySo17FBKQuestionChoiceCGGG 7SwiftUI15ModifiedContentV AA4ViewPAAE11toggleStyleyQrqd__AA06ToggleG0Rd__lFQO AA0H0V AA4TextV AA16_FlexFrameLayoutV AA06ButtonhG0V AA21_TraitWritingModifierV AA08TagValueN3KeyV
+ _symbolic _____y_____y_____yAAy_____yAAyAAyAAy__________G_____G_____G_Qo______y_____GGSg_AAyAAyAAy_____yACy___________y______y_____G_____ySaySo17FBKQuestionChoiceCGAyAyAAy_____y_____yAAyAR_____GG______Qo_ALy_____yAYGGG_____GGGtGGA0_GAIGA9_GtGGA0_G 7SwiftUI15ModifiedContentV AA6HStackV AA9TupleViewV AA0G0PAAE10fontWeightyQrAA4FontV0I0VSgFQO AA5ImageV AA20_ColorMultiplyEffectV AA18_AspectRatioLayoutV AA06_FrameQ0V AA21_TraitWritingModifierV AA010TransitionS3KeyV AA6VStackV AA4TextV AA09_VariadicG0O4TreeV AA01_Q4RootV 12FeedbackCore013EvenWidthGridQ0V AA7ForEachV AiAE11toggleStyleyQrqd__AA11ToggleStyleRd__lFQO AA6ToggleV AA05_FlexrQ0V AA17ButtonToggleStyleV AA08TagValuesW0V AA08_PaddingQ0V
+ _symbolic _____y_____y_____y__________GG______Qo_ 7SwiftUI4ViewPAAE11toggleStyleyQrqd__AA06ToggleE0Rd__lFQO AA0F0V AA15ModifiedContentV AA4TextV AA16_FlexFrameLayoutV AA06ButtonfE0V
+ _symbolic _____y_____y_____y___________y______y_____G_____ySaySo17FBKQuestionChoiceCGAkAyAAy_____y_____yAAyAD_____GG______Qo______y_____yAKGGG_____GGGtGGANG 7SwiftUI15ModifiedContentV AA6VStackV AA9TupleViewV AA4TextV AA09_VariadicG0O4TreeV AA11_LayoutRootV 12FeedbackCore013EvenWidthGridK0V AA7ForEachV AA0G0PAAE11toggleStyleyQrqd__AA06ToggleU0Rd__lFQO AA0V0V AA010_FlexFrameK0V AA06ButtonvU0V AA21_TraitWritingModifierV AA08TagValueZ3KeyV AA08_PaddingK0V
+ _symbolic _____y_____y_____y_____yACyACyACy__________G_____G_____G_Qo______y_____GGSg_ACyACyACy_____yABy___________y______y_____G_____ySaySo17FBKQuestionChoiceCGAyCyACy_____y_____yACyAR_____GG______Qo_ALy_____yAYGGG_____GGGtGGA0_GAIGA9_GtGG 7SwiftUI6HStackV AA9TupleViewV AA15ModifiedContentV AA0E0PAAE10fontWeightyQrAA4FontV0I0VSgFQO AA5ImageV AA20_ColorMultiplyEffectV AA18_AspectRatioLayoutV AA06_FrameQ0V AA21_TraitWritingModifierV AA010TransitionS3KeyV AA6VStackV AA4TextV AA09_VariadicE0O4TreeV AA01_Q4RootV 12FeedbackCore013EvenWidthGridQ0V AA7ForEachV AiAE11toggleStyleyQrqd__AA11ToggleStyleRd__lFQO AA6ToggleV AA05_FlexrQ0V AA17ButtonToggleStyleV AA08TagValuesW0V AA08_PaddingQ0V
+ _symbolic ySo17FBKQuestionChoiceCcSg
+ _symbolic yt
- +[FBKFilePromiseStub(CoreDataProperties) fetchRequest]
- -[FBKFeedbackFollowup visibleFileNamesIncludingResponsesOfTypeFileAndPromisesSorted]
- -[FBKFeedbackFollowup visibleFilePromisesForResponsesAndPromisesByName]
- -[FBKFeedbackFollowup visibleFileResponses]
- -[FBKFilePromise UUID]
- -[FBKTeamPermissions initWithView:respond:close:download:assign:demote:]
- GCC_except_table101
- GCC_except_table108
- GCC_except_table116
- GCC_except_table137
- GCC_except_table47
- GCC_except_table52
- GCC_except_table60
- GCC_except_table70
- GCC_except_table72
- GCC_except_table76
- GCC_except_table79
- GCC_except_table86
- GCC_except_table97
- __OBJC_$_CLASS_METHODS_FBKFilePromiseStub(CoreDataProperties)
- __OBJC_$_INSTANCE_METHODS_FBKFilePromiseStub(CoreDataProperties)
- ___39-[FBKBugFormTableViewController submit]_block_invoke.222
- ___39-[FBKBugFormTableViewController submit]_block_invoke.222.cold.1
- ___39-[FBKBugFormTableViewController submit]_block_invoke.229
- ___39-[FBKBugFormTableViewController submit]_block_invoke.231
- ___42-[FBKFeedbackFollowup visibleFilePromises]_block_invoke
- ___43-[FBKFeedbackFollowup visibleFileResponses]_block_invoke
- ___43-[FBKFeedbackFollowup visibleFileResponses]_block_invoke_2
- ___56-[FBKLoginManager loginWithSystemAccountWithCompletion:]_block_invoke_2
- ___56-[FBKLoginManager loginWithSystemAccountWithCompletion:]_block_invoke_2.75
- ___56-[FBKLoginManager loginWithSystemAccountWithCompletion:]_block_invoke_3
- ___57-[FBKBugFormTableViewController beginPresubmissionCheck:]_block_invoke.180
- ___57-[FBKBugFormTableViewController beginPresubmissionCheck:]_block_invoke.184
- ___57-[FBKBugFormTableViewController beginPresubmissionCheck:]_block_invoke.188
- ___57-[FBKBugFormTableViewController beginPresubmissionCheck:]_block_invoke.195
- ___57-[FBKBugFormTableViewController beginPresubmissionCheck:]_block_invoke.199
- ___57-[FBKBugFormTableViewController beginPresubmissionCheck:]_block_invoke_2.200
- ___61-[FBKSeedPortalAPI getFormResponseStubWithID:withCompletion:]_block_invoke.222
- ___61-[FBKSeedPortalAPI updateContentItemsForTeam:withCompletion:]_block_invoke.184
- ___61-[FBKSeedPortalAPI updateContentItemsForTeam:withCompletion:]_block_invoke.184.cold.1
- ___67-[FBKSeedPortalAPI fetchAnnouncementForContentItem:withCompletion:]_block_invoke.234
- ___68-[FBKSeedPortalAPI getFileDownloadURLForFilePromiseUUID:completion:]_block_invoke.252
- ___71-[FBKLoginManager _loginWithUsername:authenticationResults:completion:]_block_invoke.78
- ___73-[FBKSeedPortalAPI updateFormItemsForUser:inTeam:formTat:withCompletion:]_block_invoke.157
- ___73-[FBKSeedPortalAPI updateFormItemsForUser:inTeam:formTat:withCompletion:]_block_invoke.157.cold.1
- ___73-[FBKSeedPortalAPI updateFormItemsForUser:inTeam:formTat:withCompletion:]_block_invoke.157.cold.2
- ___73-[FBKSeedPortalAPI updateFormItemsForUser:inTeam:formTat:withCompletion:]_block_invoke.157.cold.3
- ___73-[FBKSeedPortalAPI updateFormItemsForUser:inTeam:formTat:withCompletion:]_block_invoke.159
- ___75-[FBKBugFormTableViewController _reallyChangeToBugFormStub:withTeam:force:]_block_invoke.150
- ___75-[FBKBugFormTableViewController _reallyChangeToBugFormStub:withTeam:force:]_block_invoke.150.cold.1
- ___75-[FBKBugFormTableViewController _reallyChangeToBugFormStub:withTeam:force:]_block_invoke.159
- ___75-[FBKBugFormTableViewController _reallyChangeToBugFormStub:withTeam:force:]_block_invoke.163
- ___75-[FBKBugFormTableViewController alertControllerForDismissWithLaunchAction:]_block_invoke.269
- ___75-[FBKBugFormTableViewController alertControllerForDismissWithLaunchAction:]_block_invoke.271
- ___79-[FBKSeedPortalAPI createFormResponseForBugForm:inTeam:appToken:success:error:]_block_invoke.205
- ___84-[FBKFeedbackFollowup visibleFileNamesIncludingResponsesOfTypeFileAndPromisesSorted]_block_invoke
- ___87-[FBKSeedPortalAPI fetchBugFormWithID:forTeamID:requestPlugIns:appToken:success:error:]_block_invoke.197
- ___89-[FBKLoginManager autoLoginWithUserID:userName:deviceToken:usesSystemAccount:completion:]_block_invoke.76
- ___89-[FBKLoginManager autoLoginWithUserID:userName:deviceToken:usesSystemAccount:completion:]_block_invoke_2.77
- ___block_descriptor_32_e24_B16?0"FBKFilePromise"8l
- ___block_descriptor_32_e27_24?0"FBKFilePromise"8Q16l
- ___block_descriptor_32_e40_24?0"FBKFeedbackFollowupResponse"8Q16l
- ___block_literal_global.121
- ___block_literal_global.126
- ___block_literal_global.198
- ___block_literal_global.247
- ___block_literal_global.254
- ___block_literal_global.438
- ___block_literal_global.440
- ___block_literal_global.635
- ___block_literal_global.81
- __unnamed_array_storage.213
- __unnamed_array_storage.215
- _objc_msgSend$credentialForAccount:serviceID:
- _objc_msgSend$sortedArrayUsingSelector:
- _objc_msgSend$token
- _objc_msgSend$visibleFileResponses
CStrings:
+ "\x01\x12"
+ "\x111\""
+ "\x11T"
+ "!"
+ "81$\x14\x14\x12"
+ "@\"UIScrollView\""
+ "@44@0:8B16B20B24B28B32B36B40"
+ "B16@?0@\"<FBKDownloadableFilePromise>\"8"
+ "Credential renewal failed with [%{public}@]"
+ "Credential token for FBK IDMS is nil after renewing credential"
+ "Error details: %@"
+ "ExpandedChoiceCell"
+ "FBKImageAttachmentViewController"
+ "FILE_DOWNLOAD_UNAVAILABLE_TEAM_DELETED"
+ "Failed to get token after renewal: %{public}@"
+ "Failed to get token for FBK IDMS Service: %{public}@"
+ "Failed to save file promise [%{public}@] with error [%{public}@]"
+ "MaxInlineChoices"
+ "Nil credential token for FBK IDMS Service. Will renew"
+ "Performing authentication with account [%{private}@] alternate DSID [%{private}@] has credential token? [%i]"
+ "Personal team has stale permissions. Reseting"
+ "T@\"<FBKBugFormEditorDelegate>\",N,W,Vdelegate"
+ "T@\"FBKFeedbackFollowup\",&,D,N"
+ "T@\"NSArray\",R"
+ "T@\"NSLayoutConstraint\",W,N,V_answerTextViewTopConstraint"
+ "T@\"NSString\",&,N,V_identifierOfLastDeviceSection"
+ "T@\"NSURL\",&,V_imageURL"
+ "T@\"UIBarButtonItem\",W,N,V_cancelButton"
+ "T@\"UIImageView\",W,N,V_answerTextViewAccessoryImageView"
+ "T@\"UIImageView\",W,N,V_imageView"
+ "T@\"UIScrollView\",W,N,V_scrollView"
+ "TB,N,V_alternateImagePreviewEnabled"
+ "TB,N,V_disableAccountSwitching"
+ "TB,N,V_shouldShowAttachmentButton"
+ "TB,N,V_useInlineChoices"
+ "TB,N,VshowError"
+ "TB,R,N,V_canDelete"
+ "TQ,N,V_maxInlineChoices"
+ "Td,N,V_horizontalFrameInset"
+ "This file has been deleted."
+ "Unknown type sent. Cannot update file promise [%{public}@]"
+ "_$observationRegistrar"
+ "_TtC12FeedbackCore19ChoiceCellViewModel"
+ "_TtC12FeedbackCore21FBKExpandedChoiceCell"
+ "_alternateImagePreviewEnabled"
+ "_answerTextViewAccessoryImageView"
+ "_answerTextViewTopConstraint"
+ "_bridgedUpdateConfigurationUsingState:"
+ "_canDelete"
+ "_cancelButton"
+ "_completeAuthenticationWith:credentialToken:completion:"
+ "_disableAccountSwitching"
+ "_horizontalFrameInset"
+ "_identifierOfLastDeviceSection"
+ "_imageURL"
+ "_imageView"
+ "_maxInlineChoices"
+ "_scrollView"
+ "_shouldShowAttachmentButton"
+ "_useInlineChoices"
+ "accountStore"
+ "aida_renewCredentialsForAccount:services:completion:"
+ "aida_tokenForService:completionHandler:"
+ "alternateImagePreviewEnabled"
+ "answerTextViewAccessoryImageView"
+ "answerTextViewTopConstraint"
+ "b\""
+ "canDelete"
+ "canDeleteFiles"
+ "cancelButton"
+ "clearColor"
+ "createdAtDate"
+ "defaultStore"
+ "delete"
+ "deleteFilePromiseWithUUID:completion:"
+ "deleteFilePromiseWithUUID:object:completion:"
+ "deleted"
+ "disableAccountSwitching"
+ "disableRemoteHoverEffect"
+ "disableRemoteHoverEffectAndClearBackground"
+ "displaySortDescriptors"
+ "filePromiseDeleteURLForUUID:"
+ "file_promise/%@"
+ "filename"
+ "horizontalFrameInset"
+ "identifierOfLastDeviceSection"
+ "imageControllerForAttachment:"
+ "imageURL"
+ "imageView and/or imageURL nil"
+ "initWithView:respond:close:download:delete:assign:demote:"
+ "jpeg"
+ "loadImage"
+ "maxInlineChoices"
+ "onSelected"
+ "prepareForReuse"
+ "presentAttachmentWithImagePush:fromIndexPath:"
+ "renewal result: failed"
+ "renewal result: rejected"
+ "renewal result: renewed"
+ "renewal result: unhandled case"
+ "scrollView"
+ "setAlternateImagePreviewEnabled:"
+ "setAlwaysBounceHorizontal:"
+ "setAlwaysBounceVertical:"
+ "setAnswerTextViewAccessoryImageView:"
+ "setAnswerTextViewTopConstraint:"
+ "setCancelButton:"
+ "setClipsToBounds:"
+ "setDisableAccountSwitching:"
+ "setHorizontalFrameInset:"
+ "setIdentifierOfLastDeviceSection:"
+ "setImageURL:"
+ "setImageUrl:"
+ "setImageView:"
+ "setMaxInlineChoices:"
+ "setMaximumZoomScale:"
+ "setMinimumZoomScale:"
+ "setMultipleTouchEnabled:"
+ "setNeedsUpdateConfiguration"
+ "setScrollView:"
+ "setShouldShowAttachmentButton:"
+ "setShowsHorizontalScrollIndicator:"
+ "setUseInlineChoices:"
+ "shouldShowAttachmentButton"
+ "updateCellContent"
+ "useInlineChoices"
+ "user_delete_requested"
+ "user_deleted"
+ "v24@?0@\"NSString\"8@\"NSError\"16"
+ "v24@?0q8@\"NSError\"16"
+ "v48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
+ "viewModel"
+ "visibleChoiceSetExcludingPrompt"
+ "will display image"
+ "\xb12\xe1"
- "\x11!\""
- "\x114"
- "8!\x13\x14\x14\x12"
- "@24@?0@\"FBKFeedbackFollowupResponse\"8Q16"
- "@24@?0@\"FBKFilePromise\"8Q16"
- "@40@0:8B16B20B24B28B32B36"
- "R\""
- "credentialForAccount:serviceID:"
- "initWithView:respond:close:download:assign:demote:"
- "localizedCaseInsensitiveCompare:"
- "sortedArrayUsingSelector:"
- "visibleFileNamesIncludingResponsesOfTypeFileAndPromisesSorted"
- "visibleFilePromisesForResponsesAndPromisesByName"
- "visibleFileResponses"
- "\xb1!\xd1"

```
