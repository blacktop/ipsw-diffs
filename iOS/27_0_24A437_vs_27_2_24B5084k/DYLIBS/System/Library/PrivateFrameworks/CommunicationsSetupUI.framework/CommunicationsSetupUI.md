## CommunicationsSetupUI

> `/System/Library/PrivateFrameworks/CommunicationsSetupUI.framework/CommunicationsSetupUI`

```diff

-1570.100.1.0.0
-  __TEXT.__text: 0x8c3fc
-  __TEXT.__objc_methlist: 0x8aac
-  __TEXT.__cstring: 0xc747
-  __TEXT.__const: 0x714
-  __TEXT.__gcc_except_tab: 0x4314
-  __TEXT.__oslogstring: 0x653a
+1576.200.41.0.0
+  __TEXT.__text: 0x94bdc
+  __TEXT.__objc_methlist: 0x8cec
+  __TEXT.__cstring: 0xc9dc
+  __TEXT.__const: 0xec4
+  __TEXT.__gcc_except_tab: 0x4364
+  __TEXT.__oslogstring: 0x65ea
   __TEXT.__ustring: 0x1b4
   __TEXT.__dlopen_cstrs: 0x62
-  __TEXT.__swift5_typeref: 0x2aa
-  __TEXT.__constg_swiftt: 0x18c
-  __TEXT.__swift5_fieldmd: 0x2b4
-  __TEXT.__swift5_proto: 0x30
-  __TEXT.__swift5_types: 0x20
-  __TEXT.__swift5_reflstr: 0x473
-  __TEXT.__swift5_assocty: 0x60
-  __TEXT.__unwind_info: 0x30e0
+  __TEXT.__swift5_typeref: 0x66c
+  __TEXT.__constg_swiftt: 0x484
+  __TEXT.__swift5_fieldmd: 0x4c0
+  __TEXT.__swift5_proto: 0x44
+  __TEXT.__swift5_types: 0x50
+  __TEXT.__swift5_reflstr: 0x633
+  __TEXT.__swift5_assocty: 0xc8
+  __TEXT.__swift5_builtin: 0x14
+  __TEXT.__swift5_mpenum: 0x8
+  __TEXT.__swift5_capture: 0x68
+  __TEXT.__swift_as_entry: 0x20
+  __TEXT.__swift_as_ret: 0x20
+  __TEXT.__swift_as_cont: 0x44
+  __TEXT.__unwind_info: 0x3488
+  __TEXT.__eh_frame: 0x430
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x14e0
-  __DATA_CONST.__objc_classlist: 0x338
+  __DATA_CONST.__const: 0x1568
+  __DATA_CONST.__objc_classlist: 0x370
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x130
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5bd0
+  __DATA_CONST.__objc_selrefs: 0x5d58
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x290
+  __DATA_CONST.__objc_superrefs: 0x298
   __DATA_CONST.__objc_arraydata: 0x98
-  __DATA_CONST.__got: 0xb70
-  __AUTH_CONST.__const: 0xdc9
-  __AUTH_CONST.__cfstring: 0xbb40
-  __AUTH_CONST.__objc_const: 0xd8c0
+  __DATA_CONST.__got: 0xc58
+  __AUTH_CONST.__const: 0x1151
+  __AUTH_CONST.__cfstring: 0xbba0
+  __AUTH_CONST.__objc_const: 0xe208
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__auth_got: 0x988
-  __AUTH.__objc_data: 0x1fb8
-  __AUTH.__data: 0xc0
-  __DATA.__objc_ivar: 0x578
-  __DATA.__data: 0xf18
-  __DATA.__common: 0x30
+  __AUTH_CONST.__auth_got: 0xcb8
+  __AUTH.__objc_data: 0x2430
+  __AUTH.__data: 0x258
+  __DATA.__objc_ivar: 0x590
+  __DATA.__data: 0x1050
+  __DATA.__common: 0x78
   __DATA_DIRTY.__objc_data: 0xa0
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accounts.framework/Accounts
+  - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/ContactsUI.framework/ContactsUI
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/swift/libswiftNaturalLanguage.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftObservation.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3067
-  Symbols:   7378
-  CStrings:  1794
+  Functions: 3308
+  Symbols:   7635
+  CStrings:  1819
 
Symbols:
+ -[CKSettingsMessagesController nameAndPhotoSharingCoordinator]
+ -[CKSettingsMessagesController setNameAndPhotoSharingCoordinator:]
+ -[CNFRegSettingsController _nicknameSettingsDidChange:]
+ -[CNFRegSettingsController getNameAndPhotoSharingSpecifierSummary:]
+ -[CNFRegSettingsController nameAndPhotoSharingCoordinator]
+ -[CNFRegSettingsController nameAndPhotoSharingForSpecifier:]
+ -[CNFRegSettingsController setNameAndPhotoSharingCoordinator:]
+ -[CNFRegSettingsNameAndPhotoSharingCoordinator .cxx_destruct]
+ -[CNFRegSettingsNameAndPhotoSharingCoordinator _dismissExistingOnboardingFlowThen:]
+ -[CNFRegSettingsNameAndPhotoSharingCoordinator _fetchMeContactForOnboarding]
+ -[CNFRegSettingsNameAndPhotoSharingCoordinator _imageForkedFromMeCard]
+ -[CNFRegSettingsNameAndPhotoSharingCoordinator _localizedStringForKey:]
+ -[CNFRegSettingsNameAndPhotoSharingCoordinator _makeIntroAssetViewControllerForFaceTime]
+ -[CNFRegSettingsNameAndPhotoSharingCoordinator _meCardSharingAudience]
+ -[CNFRegSettingsNameAndPhotoSharingCoordinator _meCardSharingEnabled]
+ -[CNFRegSettingsNameAndPhotoSharingCoordinator _nearestPresentingAncestor]
+ -[CNFRegSettingsNameAndPhotoSharingCoordinator _presentNicknameOnboardingControllerWithClass:]
+ -[CNFRegSettingsNameAndPhotoSharingCoordinator _primaryFaceTimeHandleForOnboarding]
+ -[CNFRegSettingsNameAndPhotoSharingCoordinator context]
+ -[CNFRegSettingsNameAndPhotoSharingCoordinator initWithPresentingViewController:reloadBlock:context:]
+ -[CNFRegSettingsNameAndPhotoSharingCoordinator nameAndPhotoSharingFooterText]
+ -[CNFRegSettingsNameAndPhotoSharingCoordinator nameAndPhotoSharingTapped]
+ -[CNFRegSettingsNameAndPhotoSharingCoordinator onboardingControllerDidFinish:]
+ -[CNFRegSettingsNameAndPhotoSharingCoordinator onboardingController]
+ -[CNFRegSettingsNameAndPhotoSharingCoordinator presentingViewControllerForOnboardingController:]
+ -[CNFRegSettingsNameAndPhotoSharingCoordinator presentingViewController]
+ -[CNFRegSettingsNameAndPhotoSharingCoordinator reloadBlock]
+ -[CNFRegSettingsNameAndPhotoSharingCoordinator setContext:]
+ -[CNFRegSettingsNameAndPhotoSharingCoordinator setOnboardingController:]
+ -[CNFRegSettingsNameAndPhotoSharingCoordinator setPresentingViewController:]
+ -[CNFRegSettingsNameAndPhotoSharingCoordinator setReloadBlock:]
+ -[CNFRegSettingsNameAndPhotoSharingCoordinator sharingSettingsViewController:didSelectSharingAudience:]
+ -[CNFRegSettingsNameAndPhotoSharingCoordinator sharingSettingsViewController:didUpdateSharingState:]
+ -[CNFRegSettingsNameAndPhotoSharingCoordinator sharingSettingsViewController:didUpdateWithSharingResult:]
+ -[CNFRegSettingsNameAndPhotoSharingCoordinator sharingSettingsViewControllerDidUpdateContact:]
+ -[CNFRegSettingsNameAndPhotoSharingCoordinator showMeCardViewControllerWithNickname:]
+ -[CNFRegSettingsNameAndPhotoSharingCoordinator showMultiplePhoneNumbersAlertForNicknames]
+ -[CNFRegSettingsNameAndPhotoSharingCoordinator showNicknameOnboardingController]
+ -[CNFRegSettingsNameAndPhotoSharingCoordinator showNicknameOnboardingOrEditFlowController]
+ -[CNFRegSettingsNameAndPhotoSharingCoordinator showiCloudNotSignedInAlertForNicknames]
+ -[CNFRegSettingsNameAndPhotoSharingCoordinator specifierSummary]
+ GCC_except_table167
+ GCC_except_table170
+ GCC_except_table175
+ GCC_except_table203
+ GCC_except_table213
+ GCC_except_table220
+ GCC_except_table221
+ GCC_except_table225
+ GCC_except_table235
+ GCC_except_table243
+ GCC_except_table249
+ GCC_except_table250
+ GCC_except_table251
+ GCC_except_table263
+ GCC_except_table264
+ GCC_except_table265
+ GCC_except_table40
+ GCC_except_table61
+ GCC_except_table85
+ _CGRectIsEmpty
+ _CGRectIsInfinite
+ _OBJC_CLASS_$_CAGradientLayer
+ _OBJC_CLASS_$_CNContactFormatter
+ _OBJC_CLASS_$_CNFRegSettingsNameAndPhotoSharingCoordinator
+ _OBJC_CLASS_$_CNFRegSettingsNameAndPhotoSharingIntroAsset
+ _OBJC_CLASS_$_NSPersonNameComponentsFormatter
+ _OBJC_CLASS_$_UIBlurEffect
+ _OBJC_CLASS_$_UIVisualEffectView
+ _OBJC_IVAR_$_CKSettingsMessagesController._nameAndPhotoSharingCoordinator
+ _OBJC_IVAR_$_CNFRegSettingsController._nameAndPhotoSharingCoordinator
+ _OBJC_IVAR_$_CNFRegSettingsController._sharedNameAndPhotoVisionOSSpecifiers
+ _OBJC_IVAR_$_CNFRegSettingsNameAndPhotoSharingCoordinator._context
+ _OBJC_IVAR_$_CNFRegSettingsNameAndPhotoSharingCoordinator._onboardingController
+ _OBJC_IVAR_$_CNFRegSettingsNameAndPhotoSharingCoordinator._presentingViewController
+ _OBJC_IVAR_$_CNFRegSettingsNameAndPhotoSharingCoordinator._reloadBlock
+ _OBJC_METACLASS_$_CNFRegSettingsNameAndPhotoSharingCoordinator
+ _OBJC_METACLASS_$_CNFRegSettingsNameAndPhotoSharingIntroAsset
+ _OBJC_METACLASS_$__TtC21CommunicationsSetupUIP33_AE9FED825916BC5005A8C98C287D71C916TileMonogramView
+ _OBJC_METACLASS_$__TtC21CommunicationsSetupUIP33_AE9FED825916BC5005A8C98C287D71C919ParticipantTileView
+ _OBJC_METACLASS_$__TtC21CommunicationsSetupUIP33_AE9FED825916BC5005A8C98C287D71C921TileContactCircleView
+ _OBJC_METACLASS_$__TtC21CommunicationsSetupUIP33_AE9FED825916BC5005A8C98C287D71C922TileLabelContainerView
+ _UIFontDescriptorSystemDesignRounded
+ _UIFontTextStyleFootnote
+ _UIFontWeightMedium
+ __Block_copy
+ __Block_release
+ __CLASS_METHODS_CNFRegSettingsNameAndPhotoSharingIntroAsset
+ __DATA_CNFRegSettingsNameAndPhotoSharingIntroAsset
+ __DATA__TtC21CommunicationsSetupUIP33_16C51FFE58DD94CA2F6A49E8049FE50123SNaPIntroAssetViewModel
+ __DATA__TtC21CommunicationsSetupUIP33_AE9FED825916BC5005A8C98C287D71C916TileMonogramView
+ __DATA__TtC21CommunicationsSetupUIP33_AE9FED825916BC5005A8C98C287D71C919ParticipantTileView
+ __DATA__TtC21CommunicationsSetupUIP33_AE9FED825916BC5005A8C98C287D71C921TileContactCircleView
+ __DATA__TtC21CommunicationsSetupUIP33_AE9FED825916BC5005A8C98C287D71C922TileLabelContainerView
+ __INSTANCE_METHODS_CNFRegSettingsNameAndPhotoSharingIntroAsset
+ __INSTANCE_METHODS__TtC21CommunicationsSetupUIP33_AE9FED825916BC5005A8C98C287D71C916TileMonogramView
+ __INSTANCE_METHODS__TtC21CommunicationsSetupUIP33_AE9FED825916BC5005A8C98C287D71C919ParticipantTileView
+ __INSTANCE_METHODS__TtC21CommunicationsSetupUIP33_AE9FED825916BC5005A8C98C287D71C921TileContactCircleView
+ __INSTANCE_METHODS__TtC21CommunicationsSetupUIP33_AE9FED825916BC5005A8C98C287D71C922TileLabelContainerView
+ __IVARS__TtC21CommunicationsSetupUIP33_16C51FFE58DD94CA2F6A49E8049FE50123SNaPIntroAssetViewModel
+ __IVARS__TtC21CommunicationsSetupUIP33_AE9FED825916BC5005A8C98C287D71C916TileMonogramView
+ __IVARS__TtC21CommunicationsSetupUIP33_AE9FED825916BC5005A8C98C287D71C919ParticipantTileView
+ __IVARS__TtC21CommunicationsSetupUIP33_AE9FED825916BC5005A8C98C287D71C921TileContactCircleView
+ __IVARS__TtC21CommunicationsSetupUIP33_AE9FED825916BC5005A8C98C287D71C922TileLabelContainerView
+ __METACLASS_DATA_CNFRegSettingsNameAndPhotoSharingIntroAsset
+ __METACLASS_DATA__TtC21CommunicationsSetupUIP33_16C51FFE58DD94CA2F6A49E8049FE50123SNaPIntroAssetViewModel
+ __METACLASS_DATA__TtC21CommunicationsSetupUIP33_AE9FED825916BC5005A8C98C287D71C916TileMonogramView
+ __METACLASS_DATA__TtC21CommunicationsSetupUIP33_AE9FED825916BC5005A8C98C287D71C919ParticipantTileView
+ __METACLASS_DATA__TtC21CommunicationsSetupUIP33_AE9FED825916BC5005A8C98C287D71C921TileContactCircleView
+ __METACLASS_DATA__TtC21CommunicationsSetupUIP33_AE9FED825916BC5005A8C98C287D71C922TileLabelContainerView
+ __MergedGlobals
+ __OBJC_$_INSTANCE_METHODS_CNFRegSettingsNameAndPhotoSharingCoordinator
+ __OBJC_$_INSTANCE_VARIABLES_CNFRegSettingsNameAndPhotoSharingCoordinator
+ __OBJC_$_PROP_LIST_CNFRegSettingsNameAndPhotoSharingCoordinator
+ __OBJC_CLASS_PROTOCOLS_$_CNFRegSettingsNameAndPhotoSharingCoordinator
+ __OBJC_CLASS_RO_$_CNFRegSettingsNameAndPhotoSharingCoordinator
+ __OBJC_METACLASS_RO_$_CNFRegSettingsNameAndPhotoSharingCoordinator
+ __PROPERTIES__TtC21CommunicationsSetupUIP33_AE9FED825916BC5005A8C98C287D71C922TileLabelContainerView
+ ___36-[CKSettingsMessagesController init]_block_invoke
+ ___73-[CNFRegSettingsNameAndPhotoSharingCoordinator nameAndPhotoSharingTapped]_block_invoke
+ ___73-[CNFRegSettingsNameAndPhotoSharingCoordinator nameAndPhotoSharingTapped]_block_invoke_2
+ ___73-[CNFRegSettingsNameAndPhotoSharingCoordinator nameAndPhotoSharingTapped]_block_invoke_3
+ ___73-[CNFRegSettingsNameAndPhotoSharingCoordinator nameAndPhotoSharingTapped]_block_invoke_4
+ ___80-[CNFRegSettingsNameAndPhotoSharingCoordinator showNicknameOnboardingController]_block_invoke
+ ___88-[CNFRegSettingsNameAndPhotoSharingCoordinator _makeIntroAssetViewControllerForFaceTime]_block_invoke
+ ___block_descriptor_40_e8_32w_e16_"CNContact"8?0lw32l8
+ ___block_descriptor_40_e8_32w_e20_v16?0"IMNickname"8lw32l8
+ ___block_descriptor_48_e8_32s40w_e5_v8?0ls32l8w40l8
+ ___block_descriptor_48_e8_32w_e5_v8?0lw32l8u40l8
+ ___isOSVersionAtLeast
+ ___isPlatformVersionAtLeast
+ ___swift_async_cont_functlets
+ ___swift_async_entry_functlets
+ ___swift_async_ret_functlets
+ ___swift_closure_destructor
+ ___swift_memcpy17_8
+ ___swift_memcpy64_8
+ __availability_version_check
+ __initializeAvailabilityCheck
+ __swiftEmptyArrayStorage
+ __swift_stdlib_malloc_size
+ _associated conformance 21CommunicationsSetupUI15ParticipantTileV05SwiftC04ViewAA4BodyAdEP_AdE
+ _associated conformance 21CommunicationsSetupUI18SNaPIntroAssetView33_16C51FFE58DD94CA2F6A49E8049FE501LLV05SwiftC00G0AA4BodyAeFP_AeF
+ _associated conformance 21CommunicationsSetupUI28ParticipantTileRepresentable33_AE9FED825916BC5005A8C98C287D71C9LLV05SwiftC006UIViewF0AaE4View
+ _associated conformance 21CommunicationsSetupUI28ParticipantTileRepresentable33_AE9FED825916BC5005A8C98C287D71C9LLV05SwiftC04ViewAA4BodyAeFP_AeF
+ _block_copy_helper
+ _block_descriptor
+ _block_destroy_helper
+ _compatibilityInitializeAvailabilityCheck
+ _dispatch_once_f
+ _fclose
+ _fopen
+ _fread
+ _fseek
+ _ftell
+ _get_enum_tag_for_layout_string 21CommunicationsSetupUI14MonogramConfigV7ContentO
+ _get_underlying_type_ref 7SwiftUI4ViewPAAEAcAE4task4name8priority4file4line_QrSSSg_ScPSSSiyyYaYAcntFQOQr
+ _get_underlying_witness 7SwiftUI4ViewPAAEAcAE4task4name8priority4file4line_QrSSSg_ScPSSSiyyYaYAcntFQOqd__AaBHC
+ _get_witness_table 21CommunicationsSetupUI28ParticipantTileRepresentable33_AE9FED825916BC5005A8C98C287D71C9LLV05SwiftC04ViewHPyHC
+ _get_witness_table qd__7SwiftUI4ViewHD2_AaBPAAE4task4name8priority4file4line_QrSSSg_ScPSSSiyyYaYAcntFQOyAA15ModifiedContentVyAKyAA6ZStackVyAA05TupleJ0VyAKyAKyAKy019CommunicationsSetupB015ParticipantTileVAA18_AspectRatioLayoutVGAA12_ScaleEffectVGAA08_OpacityU0VG_A_QPGGAA08_PaddingS0VGAA18_AnimationModifierVySbGG_Qo_HO
+ _initializeAvailabilityCheck
+ _kCACornerCurveContinuous
+ _kCAGradientLayerRadial
+ _malloc
+ _malloc_size
+ _memmove
+ _objc_msgSend$_dismissExistingOnboardingFlowThen:
+ _objc_msgSend$_fetchMeContactForOnboarding
+ _objc_msgSend$_localizedStringForKey:
+ _objc_msgSend$_makeIntroAssetViewControllerForFaceTime
+ _objc_msgSend$_nearestPresentingAncestor
+ _objc_msgSend$_presentNicknameOnboardingControllerWithClass:
+ _objc_msgSend$_primaryFaceTimeHandleForOnboarding
+ _objc_msgSend$addSublayer:
+ _objc_msgSend$configurationWithPaletteColors:
+ _objc_msgSend$effectWithStyle:
+ _objc_msgSend$familyName
+ _objc_msgSend$fontDescriptor
+ _objc_msgSend$fontDescriptorWithDesign:
+ _objc_msgSend$fontDescriptorWithSymbolicTraits:
+ _objc_msgSend$fontWithDescriptor:size:
+ _objc_msgSend$givenName
+ _objc_msgSend$imageForkedFromMeCard
+ _objc_msgSend$initWithEffect:
+ _objc_msgSend$initWithPresentingViewController:reloadBlock:context:
+ _objc_msgSend$insertSubview:atIndex:
+ _objc_msgSend$intrinsicContentSize
+ _objc_msgSend$isHidden
+ _objc_msgSend$layer
+ _objc_msgSend$makeViewControllerWithUnknownDisplayName:primaryHandle:meContactProvider:
+ _objc_msgSend$nameAndPhotoSharingCoordinator
+ _objc_msgSend$nameAndPhotoSharingFooterText
+ _objc_msgSend$nameAndPhotoSharingTapped
+ _objc_msgSend$setColors:
+ _objc_msgSend$setCornerCurve:
+ _objc_msgSend$setCornerRadius:
+ _objc_msgSend$setCustomIntroAssetViewController:
+ _objc_msgSend$setCustomIntroDetailText:
+ _objc_msgSend$setCustomIntroTitle:
+ _objc_msgSend$setEndPoint:
+ _objc_msgSend$setLocations:
+ _objc_msgSend$setNameAndPhotoSharingCoordinator:
+ _objc_msgSend$setOpacity:
+ _objc_msgSend$setPriority:
+ _objc_msgSend$setSharingAudience:
+ _objc_msgSend$setStartPoint:
+ _objc_msgSend$setType:
+ _objc_msgSend$sharingAudience
+ _objc_msgSend$sharingEnabled
+ _objc_msgSend$specifierSummary
+ _objc_msgSend$stringFromContact:style:
+ _objc_msgSend$stringFromPersonNameComponents:
+ _objc_msgSend$systemFontOfSize:weight:
+ _rewind
+ _sscanf
+ _swift_allocObject
+ _swift_arrayInitWithCopy
+ _swift_asyncLet_begin
+ _swift_asyncLet_finish
+ _swift_asyncLet_get
+ _swift_bridgeObjectRetain
+ _swift_continuation_await
+ _swift_continuation_init
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_enumFn_getEnumTag
+ _swift_cvw_initWithCopy
+ _swift_cvw_initializeBufferWithCopyOfBuffer
+ _swift_deallocObject
+ _swift_errorRelease
+ _swift_getForeignTypeMetadata
+ _swift_getObjectType
+ _swift_getSingletonMetadata
+ _swift_release_x22
+ _swift_release_x24
+ _swift_release_x25
+ _swift_release_x8
+ _swift_retain_x2
+ _swift_task_alloc
+ _swift_task_create
+ _swift_task_dealloc
+ _swift_task_switch
+ _swift_unknownObjectRelease
+ _swift_unknownObjectRetain
+ _swift_updateClassMetadata2
+ _symbolic $s7SwiftUI19UIViewRepresentableP
+ _symbolic SSSg
+ _symbolic SaySo7UIColorCG
+ _symbolic Sb
+ _symbolic ScA_pSg
+ _symbolic ScCySo10IMNicknameCSg_____G s5NeverO
+ _symbolic ScGySo10IMNicknameCSgG
+ _symbolic ScPSg
+ _symbolic Sd
+ _symbolic So10IMNicknameCSg
+ _symbolic So10IMNicknameCSgIeAgHr_
+ _symbolic So11UIImageViewC
+ _symbolic So15CAGradientLayerC
+ _symbolic So18UIVisualEffectViewC
+ _symbolic So6UIViewC
+ _symbolic So7UILabelC
+ _symbolic So9CNContactCSgIeyBa_
+ _symbolic So9CNContactCSgyc
+ _symbolic _____ 11Observation0A9RegistrarV
+ _symbolic _____ 21CommunicationsSetupUI14MonogramConfigV
+ _symbolic _____ 21CommunicationsSetupUI14MonogramConfigV7ContentO
+ _symbolic _____ 21CommunicationsSetupUI15ParticipantTileV
+ _symbolic _____ 21CommunicationsSetupUI16TileMonogramView33_AE9FED825916BC5005A8C98C287D71C9LLC
+ _symbolic _____ 21CommunicationsSetupUI18SNaPIntroAssetView33_16C51FFE58DD94CA2F6A49E8049FE501LLV
+ _symbolic _____ 21CommunicationsSetupUI19ParticipantTileView33_AE9FED825916BC5005A8C98C287D71C9LLC
+ _symbolic _____ 21CommunicationsSetupUI21TileContactCircleView33_AE9FED825916BC5005A8C98C287D71C9LLC
+ _symbolic _____ 21CommunicationsSetupUI22TileLabelContainerView33_AE9FED825916BC5005A8C98C287D71C9LLC
+ _symbolic _____ 21CommunicationsSetupUI23SNaPIntroAssetViewModel33_16C51FFE58DD94CA2F6A49E8049FE501LLC
+ _symbolic _____ 21CommunicationsSetupUI28ParticipantTileRepresentable33_AE9FED825916BC5005A8C98C287D71C9LLV
+ _symbolic _____ 21CommunicationsSetupUI43CNFRegSettingsNameAndPhotoSharingIntroAssetC
+ _symbolic _____ s5NeverO
+ _symbolic _____Sg 21CommunicationsSetupUI14MonogramConfigV
+ _symbolic _____yAAyAAy__________G_____G_____G 7SwiftUI15ModifiedContentV 019CommunicationsSetupB015ParticipantTileV AA18_AspectRatioLayoutV AA12_ScaleEffectV AA08_OpacityM0V
+ _symbolic _____yAAyAAy_____y_____yAAyAAyAAy__________G_____G_____G_AJQPGG_____G_____ySbGG_____G 7SwiftUI15ModifiedContentV AA6ZStackV AA05TupleD0V 019CommunicationsSetupB015ParticipantTileV AA18_AspectRatioLayoutV AA12_ScaleEffectV AA08_OpacityO0V AA08_PaddingM0V AA18_AnimationModifierV AA14_TaskModifier2V
+ _symbolic _____yAAy__________G_____G 7SwiftUI15ModifiedContentV 019CommunicationsSetupB015ParticipantTileV AA18_AspectRatioLayoutV AA12_ScaleEffectV
+ _symbolic _____yAAy_____y_____yAAyAAyAAy__________G_____G_____G_AJQPGG_____G_____ySbGG 7SwiftUI15ModifiedContentV AA6ZStackV AA05TupleD0V 019CommunicationsSetupB015ParticipantTileV AA18_AspectRatioLayoutV AA12_ScaleEffectV AA08_OpacityO0V AA08_PaddingM0V AA18_AnimationModifierV
+ _symbolic _____ySbG 7SwiftUI18_AnimationModifierV
+ _symbolic _____y_____G 7SwiftUI19UIHostingControllerC 019CommunicationsSetupB018SNaPIntroAssetView33_16C51FFE58DD94CA2F6A49E8049FE501LLV
+ _symbolic _____y__________G 7SwiftUI15ModifiedContentV 019CommunicationsSetupB015ParticipantTileV AA18_AspectRatioLayoutV
+ _symbolic _____y_____yAAy_____y_____yAAyAAyAAy__________G_____G_____G_AJQPGG_____G_____ySbGG_Qo_ 7SwiftUI4ViewPAAE4task4name8priority4file4line_QrSSSg_ScPSSSiyyYaYAcntFQO AA15ModifiedContentV AA6ZStackV AA05TupleJ0V 019CommunicationsSetupB015ParticipantTileV AA18_AspectRatioLayoutV AA12_ScaleEffectV AA08_OpacityU0V AA08_PaddingS0V AA18_AnimationModifierV
+ _symbolic _____y_____y_____yAAyAAyAAy__________G_____G_____G_AJQPGG_____G 7SwiftUI15ModifiedContentV AA6ZStackV AA05TupleD0V 019CommunicationsSetupB015ParticipantTileV AA18_AspectRatioLayoutV AA12_ScaleEffectV AA08_OpacityO0V AA08_PaddingM0V
+ _symbolic _____y_____y_____yACyACy__________G_____G_____G_AJQPGG 7SwiftUI6ZStackV AA12TupleContentV AA08ModifiedE0V 019CommunicationsSetupB015ParticipantTileV AA18_AspectRatioLayoutV AA12_ScaleEffectV AA08_OpacityO0V
+ _symbolic _____yyXlG s23_ContiguousArrayStorageC
+ _symbolic _____yypG s23_ContiguousArrayStorageC
+ _symbolic qd__
+ _symbolic yt
+ _type_layout_string 21CommunicationsSetupUI14MonogramConfigV
+ _type_layout_string 21CommunicationsSetupUI14MonogramConfigV7ContentO
+ _type_layout_string 21CommunicationsSetupUI15ParticipantTileV
+ _type_layout_string 21CommunicationsSetupUI18SNaPIntroAssetView33_16C51FFE58DD94CA2F6A49E8049FE501LLV
- -[CKSettingsMessagesController _imageForkedFromMeCard]
- -[CKSettingsMessagesController _meCardSharingAudience]
- -[CKSettingsMessagesController _meCardSharingEnabled]
- -[CKSettingsMessagesController onboardingControllerDidFinish:]
- -[CKSettingsMessagesController onboardingController]
- -[CKSettingsMessagesController presentingViewControllerForOnboardingController:]
- -[CKSettingsMessagesController setOnboardingController:]
- -[CKSettingsMessagesController sharingSettingsViewController:didSelectSharingAudience:]
- -[CKSettingsMessagesController sharingSettingsViewController:didUpdateSharingState:]
- -[CKSettingsMessagesController sharingSettingsViewController:didUpdateWithSharingResult:]
- -[CKSettingsMessagesController sharingSettingsViewControllerDidUpdateContact:]
- -[CKSettingsMessagesController showMeCardViewControllerWithNickname:]
- -[CKSettingsMessagesController showMultiplePhoneNumbersAlertForNicknames]
- -[CKSettingsMessagesController showNicknameOnboardingController]
- -[CKSettingsMessagesController showNicknameOnboardingOrEditFlowController]
- -[CKSettingsMessagesController showiCloudNotSignedInAlertForNicknames]
- GCC_except_table180
- GCC_except_table192
- GCC_except_table200
- GCC_except_table210
- GCC_except_table223
- GCC_except_table237
- GCC_except_table238
- GCC_except_table239
- GCC_except_table242
- GCC_except_table246
- GCC_except_table247
- GCC_except_table260
- GCC_except_table261
- GCC_except_table262
- GCC_except_table78
- GCC_except_table80
- GCC_except_table84
- _OBJC_IVAR_$_CKSettingsMessagesController._onboardingController
- ___64-[CKSettingsMessagesController nameAndPhotoSharingForSpecifier:]_block_invoke
- ___64-[CKSettingsMessagesController nameAndPhotoSharingForSpecifier:]_block_invoke_2
- ___64-[CKSettingsMessagesController nameAndPhotoSharingForSpecifier:]_block_invoke_3
- ___64-[CKSettingsMessagesController nameAndPhotoSharingForSpecifier:]_block_invoke_4
- ___block_descriptor_40_e8_32s_e20_v16?0"IMNickname"8ls32l8
CStrings:
+ "%d.%d.%d"
+ "/System/Library/CoreServices/SystemVersion.plist"
+ "@\"CNContact\"8@?0"
+ "CFDataCreateWithBytesNoCopy"
+ "CFDictionaryGetValue"
+ "CFGetTypeID"
+ "CFPropertyListCreateFromXMLData"
+ "CFPropertyListCreateWithData"
+ "CFRelease"
+ "CFStringCreateWithCStringNoCopy"
+ "CFStringGetCString"
+ "CFStringGetTypeID"
+ "CKMeCardSharingNameProvider"
+ "CommunicationsSetupUI/CNFRegSettingsNameAndPhotoSharingTile.swift"
+ "Fatal error"
+ "ME"
+ "NAME_AND_PHOTO_SHARING_INTRO_DESCRIPTION"
+ "NAME_AND_PHOTO_SHARING_INTRO_TITLE"
+ "NAME_AND_PHOTO_SHARING_INTRO_UNKNOWN_TILE_NAME"
+ "NameAndPhotoSharing: dismissing live onboarding flow %{public}@ before re-presenting"
+ "P`"
+ "ProductVersion"
+ "SHARED_NAME_AND_PHOTO_SETTINGS_GROUP_VISIONOS"
+ "SHARED_NAME_AND_PHOTO_SETTINGS_VISIONOS"
+ "View.task @ CommunicationsSetupUI/CNFRegSettingsNameAndPhotoSharingIntroAsset.swift:"
+ "[WARN] NameAndPhotoSharing: superseded onboarding controller %{public}@ denied a presenter"
+ "fetchPersonalNickname(timeout:)"
+ "kCFAllocatorNull"
+ "person.crop.circle.fill"
+ "r"
- "MeCardSharingAudience"
- "MeCardSharingEnabled"
- "MeCardSharingImageForkedFromMeCard"
- "RCSOnPartiallyActiveSim"
- "com.apple.messages.nicknames"
```
