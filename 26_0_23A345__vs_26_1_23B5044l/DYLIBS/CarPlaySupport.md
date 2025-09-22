## CarPlaySupport

> `/System/Library/PrivateFrameworks/CarPlaySupport.framework/CarPlaySupport`

```diff

-487.3.1.0.0
-  __TEXT.__text: 0x10322c
-  __TEXT.__auth_stubs: 0x1070
-  __TEXT.__objc_methlist: 0x9b14
+488.11.0.0.0
+  __TEXT.__text: 0x102934
+  __TEXT.__auth_stubs: 0x10e0
+  __TEXT.__objc_methlist: 0x9ad4
   __TEXT.__const: 0x724
-  __TEXT.__cstring: 0x1c4e
-  __TEXT.__gcc_except_tab: 0x104c
-  __TEXT.__oslogstring: 0x2484
+  __TEXT.__cstring: 0x1cae
+  __TEXT.__gcc_except_tab: 0x1060
+  __TEXT.__oslogstring: 0x251e
   __TEXT.__ustring: 0x4
   __TEXT.__constg_swiftt: 0x2f4
-  __TEXT.__swift5_typeref: 0x77c
+  __TEXT.__swift5_typeref: 0x8f0
   __TEXT.__swift5_reflstr: 0x9b
   __TEXT.__swift5_fieldmd: 0x140
   __TEXT.__swift5_types: 0x20
   __TEXT.__swift5_assocty: 0x60
   __TEXT.__swift5_builtin: 0x14
-  __TEXT.__swift5_capture: 0x20
+  __TEXT.__swift5_capture: 0x30
   __TEXT.__swift5_proto: 0x18
-  __TEXT.__unwind_info: 0x19c8
-  __TEXT.__objc_classname: 0x1617
-  __TEXT.__objc_methname: 0x1af7d
-  __TEXT.__objc_methtype: 0x4d89
-  __TEXT.__objc_stubs: 0x12500
-  __DATA_CONST.__got: 0xc78
-  __DATA_CONST.__const: 0x2e68
+  __TEXT.__unwind_info: 0x19f8
+  __TEXT.__objc_classname: 0x1614
+  __TEXT.__objc_methname: 0x1b05e
+  __TEXT.__objc_methtype: 0x4d87
+  __TEXT.__objc_stubs: 0x12600
+  __DATA_CONST.__got: 0xca8
+  __DATA_CONST.__const: 0x3980
   __DATA_CONST.__objc_classlist: 0x3e8
   __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_protolist: 0x300
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5e30
+  __DATA_CONST.__objc_selrefs: 0x5e80
   __DATA_CONST.__objc_protorefs: 0x80
-  __DATA_CONST.__objc_superrefs: 0x300
+  __DATA_CONST.__objc_superrefs: 0x308
   __DATA_CONST.__objc_arraydata: 0x100
-  __AUTH_CONST.__auth_got: 0x848
-  __AUTH_CONST.__const: 0x730
-  __AUTH_CONST.__cfstring: 0x1860
-  __AUTH_CONST.__objc_const: 0x1dd68
+  __AUTH_CONST.__auth_got: 0x880
+  __AUTH_CONST.__const: 0x758
+  __AUTH_CONST.__cfstring: 0x1920
+  __AUTH_CONST.__objc_const: 0x1dc88
   __AUTH_CONST.__objc_intobj: 0x168
   __AUTH_CONST.__objc_arrayobj: 0x198
   __AUTH.__objc_data: 0x2930
   __AUTH.__data: 0x198
-  __DATA.__objc_ivar: 0x9f4
-  __DATA.__data: 0x2638
+  __DATA.__objc_ivar: 0x9d8
+  __DATA.__data: 0x2678
   __DATA.__bss: 0x450
   __DATA.__common: 0x20
   - /System/Library/Frameworks/CarPlay.framework/CarPlay

   - /System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard
   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
   - /System/Library/PrivateFrameworks/GraphicsServices.framework/GraphicsServices
+  - /System/Library/PrivateFrameworks/IconServices.framework/IconServices
   - /System/Library/PrivateFrameworks/MobileIcons.framework/MobileIcons
   - /System/Library/PrivateFrameworks/NetAppsUtilities.framework/NetAppsUtilities
   - /System/Library/PrivateFrameworks/PlatterKit.framework/PlatterKit
   - /System/Library/PrivateFrameworks/SiriActivation.framework/SiriActivation
+  - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
+  - /System/Library/PrivateFrameworks/SpringBoardUIServices.framework/SpringBoardUIServices
   - /System/Library/PrivateFrameworks/UIFoundation.framework/UIFoundation
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 6B8DAD9E-0872-3161-9539-AAFF29827003
-  Functions: 3277
-  Symbols:   13521
-  CStrings:  5665
+  UUID: 7A2D90D5-5B95-386C-9B58-0B94B241F845
+  Functions: 3288
+  Symbols:   13911
+  CStrings:  5689
 
Symbols:
+ -[CPSAudioPlaybackManager nowPlayingManager:didReceiveArtworkResponse:]
+ -[CPSAudioPlaybackManager nowPlayingManager:willStartLoadingArtworkForCatalog:bundleIdentifier:]
+ -[CPSAudioPlaybackManager placeholderTimer]
+ -[CPSAudioPlaybackManager setPlaceholderTimer:]
+ -[CPSAudioPlaybackManager setPlaceholderTimerActive:]
+ -[CPSBannerView applicationIconImageWithCompletion:]
+ -[CPSBannerView iconImageQueue]
+ -[CPSBannerView setIconImageQueue:]
+ -[CPSGuidanceBannerView _updateApplicationIconImage]
+ -[CPSMapButton hasFocusedImage]
+ -[CPSMapButton setHasFocusedImage:]
+ -[CPSSectionedDataSource _updateLimitingLists]
+ -[CPSSectionedDataSource setIsLimitingLists:]
+ GCC_except_table53
+ _$s14CarPlaySupport23ContactActionButtonView33_E85FB5A4CE27235491446378D391A496LLV4bodyQrvg7SwiftUI05TupleG0VyAF19_ConditionalContentVyAF0G0PAFE11buttonStyleyQrqd__AF0fU0Rd__lFQOyAF0F0VyAlFE7paddingyQr12CoreGraphics7CGFloatVFQOyAF5ImageV_Qo_G_AA0defU0ACLLVQo_AlFEAMyQrqd__AfNRd__lFQOyAPyAlFE5frame5width6height9alignmentQrATSg_A4_AF9AlignmentVtFQOyAV_Qo_G_AZQo_G_AlFEA0_A1_A2_A3_QrA4__A4_A6_tFQOyAF4TextV_Qo_tGyXEfU_
+ _$s14CarPlaySupport23ContactActionButtonView33_E85FB5A4CE27235491446378D391A496LLV4bodyQrvg7SwiftUI05TupleG0VyAF19_ConditionalContentVyAF0G0PAFE11buttonStyleyQrqd__AF0fU0Rd__lFQOyAF0F0VyAlFE7paddingyQr12CoreGraphics7CGFloatVFQOyAF5ImageV_Qo_G_AA0defU0ACLLVQo_AlFEAMyQrqd__AfNRd__lFQOyAPyAlFE5frame5width6height9alignmentQrATSg_A4_AF9AlignmentVtFQOyAV_Qo_G_AZQo_G_AlFEA0_A1_A2_A3_QrA4__A4_A6_tFQOyAF4TextV_Qo_tGyXEfU_A7_yXEfU2_
+ _$s14CarPlaySupport23ContactActionButtonView33_E85FB5A4CE27235491446378D391A496LLV4bodyQrvg7SwiftUI05TupleG0VyAF19_ConditionalContentVyAF0G0PAFE11buttonStyleyQrqd__AF0fU0Rd__lFQOyAF0F0VyAlFE7paddingyQr12CoreGraphics7CGFloatVFQOyAF5ImageV_Qo_G_AA0defU0ACLLVQo_AlFEAMyQrqd__AfNRd__lFQOyAPyAlFE5frame5width6height9alignmentQrATSg_A4_AF9AlignmentVtFQOyAV_Qo_G_AZQo_G_AlFEA0_A1_A2_A3_QrA4__A4_A6_tFQOyAF4TextV_Qo_tGyXEfU_A7_yXEfU2_TA
+ _$s14CarPlaySupport23ContactActionButtonView33_E85FB5A4CE27235491446378D391A496LLV4bodyQrvg7SwiftUI05TupleG0VyAF19_ConditionalContentVyAF0G0PAFE11buttonStyleyQrqd__AF0fU0Rd__lFQOyAF0F0VyAlFE7paddingyQr12CoreGraphics7CGFloatVFQOyAF5ImageV_Qo_G_AA0defU0ACLLVQo_AlFEAMyQrqd__AfNRd__lFQOyAPyAlFE5frame5width6height9alignmentQrATSg_A4_AF9AlignmentVtFQOyAV_Qo_G_AZQo_G_AlFEA0_A1_A2_A3_QrA4__A4_A6_tFQOyAF4TextV_Qo_tGyXEfU_AWyXEfU0_
+ _$s14CarPlaySupport23ContactActionButtonView33_E85FB5A4CE27235491446378D391A496LLV4bodyQrvg7SwiftUI05TupleG0VyAF19_ConditionalContentVyAF0G0PAFE11buttonStyleyQrqd__AF0fU0Rd__lFQOyAF0F0VyAlFE7paddingyQr12CoreGraphics7CGFloatVFQOyAF5ImageV_Qo_G_AA0defU0ACLLVQo_AlFEAMyQrqd__AfNRd__lFQOyAPyAlFE5frame5width6height9alignmentQrATSg_A4_AF9AlignmentVtFQOyAV_Qo_G_AZQo_G_AlFEA0_A1_A2_A3_QrA4__A4_A6_tFQOyAF4TextV_Qo_tGyXEfU_AWyXEfU0_TA
+ _$s14CarPlaySupport23ContactActionButtonView33_E85FB5A4CE27235491446378D391A496LLV4bodyQrvg7SwiftUI05TupleG0VyAF19_ConditionalContentVyAF0G0PAFE11buttonStyleyQrqd__AF0fU0Rd__lFQOyAF0F0VyAlFE7paddingyQr12CoreGraphics7CGFloatVFQOyAF5ImageV_Qo_G_AA0defU0ACLLVQo_AlFEAMyQrqd__AfNRd__lFQOyAPyAlFE5frame5width6height9alignmentQrATSg_A4_AF9AlignmentVtFQOyAV_Qo_G_AZQo_G_AlFEA0_A1_A2_A3_QrA4__A4_A6_tFQOyAF4TextV_Qo_tGyXEfU_yyScMYccfU1_TA
+ _$s14CarPlaySupport23ContactActionButtonView33_E85FB5A4CE27235491446378D391A496LLV4bodyQrvg7SwiftUI05TupleG0VyAF19_ConditionalContentVyAF0G0PAFE11buttonStyleyQrqd__AF0fU0Rd__lFQOyAF0F0VyAlFE7paddingyQr12CoreGraphics7CGFloatVFQOyAF5ImageV_Qo_G_AA0defU0ACLLVQo_AlFEAMyQrqd__AfNRd__lFQOyAPyAlFE5frame5width6height9alignmentQrATSg_A4_AF9AlignmentVtFQOyAV_Qo_G_AZQo_G_AlFEA0_A1_A2_A3_QrA4__A4_A6_tFQOyAF4TextV_Qo_tGyXEfU_yyScMYccfU_TA
+ _$s14CarPlaySupport23ContactActionButtonView33_E85FB5A4CE27235491446378D391A496LLV4bodyQrvg7SwiftUI05TupleG0VyAF19_ConditionalContentVyAF0G0PAFE11buttonStyleyQrqd__AF0fU0Rd__lFQOyAF0F0VyAlFE7paddingyQr12CoreGraphics7CGFloatVFQOyAF5ImageV_Qo_G_AA0defU0ACLLVQo_AlFEAMyQrqd__AfNRd__lFQOyAPyAlFE5frame5width6height9alignmentQrATSg_A4_AF9AlignmentVtFQOyAV_Qo_G_AZQo_G_AlFEA0_A1_A2_A3_QrA4__A4_A6_tFQOyAF4TextV_Qo_tGyXEfU_yyScMYccfU_TATm
+ _$s14CarPlaySupport23ContactActionButtonView33_E85FB5A4CE27235491446378D391A496LLV4bodyQrvg7SwiftUI05TupleG0VyAF19_ConditionalContentVyAF0G0PAFE11buttonStyleyQrqd__AF0fU0Rd__lFQOyAF0F0VyAlFE7paddingyQr12CoreGraphics7CGFloatVFQOyAF5ImageV_Qo_G_AA0defU0ACLLVQo_AlFEAMyQrqd__AfNRd__lFQOyAPyAlFE5frame5width6height9alignmentQrATSg_A4_AF9AlignmentVtFQOyAV_Qo_G_AZQo_G_AlFEA0_A1_A2_A3_QrA4__A4_A6_tFQOyAF4TextV_Qo_tGyXEfU_yyScMYccfU_Tm
+ _$s7SwiftUI11EnvironmentV7ContentOyAA11ColorSchemeO_GWOcTm
+ _$s7SwiftUI11EnvironmentVyAA11ColorSchemeOGWOhTm
+ _$s7SwiftUI12_FrameLayoutV5width6height9alignmentAC12CoreGraphics7CGFloatVSg_AjA9AlignmentVtcfC
+ _$s7SwiftUI12_FrameLayoutVAA12ViewModifierAAWP
+ _$s7SwiftUI12_FrameLayoutVMn
+ _$s7SwiftUI13_VariadicViewO4TreeVy_AA13_VStackLayoutVAA05TupleD0VyAA19_ConditionalContentVyAA0D0PAAE11buttonStyleyQrqd__AA06ButtonL0Rd__lFQOyAA0M0VyAA08ModifiedJ0VyAA5ImageVAA08_PaddingG0VGG_14CarPlaySupport013ContactActionmL033_E85FB5A4CE27235491446378D391A496LLVQo_AmAEANyQrqd__AaORd__lFQOyAQyASyAuA06_FrameG0VGG_A1_Qo_G_ASyAA4TextVA4_GtGGMD
+ _$s7SwiftUI15ModifiedContentVyAA4TextVAA12_FrameLayoutVGMD
+ _$s7SwiftUI15ModifiedContentVyAA5ImageVAA12_FrameLayoutVGACyxq_GAA4ViewA2aJRzAA0H8ModifierR_rlWL
+ _$s7SwiftUI15ModifiedContentVyAA5ImageVAA12_FrameLayoutVGMD
+ _$s7SwiftUI15ModifiedContentVyAA5ImageVAA14_PaddingLayoutVGACyxq_GAA4ViewA2aJRzAA0H8ModifierR_rlWlTm
+ _$s7SwiftUI19_ConditionalContentV7StorageOMn
+ _$s7SwiftUI19_ConditionalContentV7StorageOyAA4ViewPAAE11buttonStyleyQrqd__AA06ButtonH0Rd__lFQOyAA0I0VyAA08ModifiedD0VyAA5ImageVAA14_PaddingLayoutVGG_14CarPlaySupport013ContactActioniH033_E85FB5A4CE27235491446378D391A496LLVQo_AgAEAHyQrqd__AaIRd__lFQOyAKyAMyAoA06_FrameM0VGG_AWQo__GMD
+ _$s7SwiftUI19_ConditionalContentVA2A4ViewRzAaDR_rlE7storageACyxq_GAC7StorageOyxq__G_tcfC
+ _$s7SwiftUI19_ConditionalContentVMn
+ _$s7SwiftUI19_ConditionalContentVyAA4ViewPAAE11buttonStyleyQrqd__AA06ButtonG0Rd__lFQOyAA0H0VyAA08ModifiedD0VyAA5ImageVAA14_PaddingLayoutVGG_14CarPlaySupport013ContactActionhG033_E85FB5A4CE27235491446378D391A496LLVQo_AeAEAFyQrqd__AaGRd__lFQOyAIyAKyAmA06_FrameL0VGG_AUQo_GMD
+ _$s7SwiftUI19_ConditionalContentVyAA4ViewPAAE11buttonStyleyQrqd__AA06ButtonG0Rd__lFQOyAA0H0VyAA08ModifiedD0VyAA5ImageVAA14_PaddingLayoutVGG_14CarPlaySupport013ContactActionhG033_E85FB5A4CE27235491446378D391A496LLVQo_AeAEAFyQrqd__AaGRd__lFQOyAIyAKyAmA06_FrameL0VGG_AUQo_G_AKyAA4TextVAXGtMD
+ _$s7SwiftUI4ViewPAAE11buttonStyleyQrqd__AA06ButtonE0Rd__lFQOyAA0F0VyAA15ModifiedContentVyAA5ImageVAA12_FrameLayoutVGG_14CarPlaySupport013ContactActionfE033_E85FB5A4CE27235491446378D391A496LLVQo_MD
+ _$s7SwiftUI5ImageV12ResizingModeO7stretchyA2EmFWC
+ _$s7SwiftUI5ImageV12ResizingModeOMa
+ _$s7SwiftUI5ImageV9resizable9capInsets12resizingModeAcA04EdgeF0V_AC08ResizingH0OtF
+ _$s7SwiftUI6ButtonVyAA15ModifiedContentVyAA5ImageVAA12_FrameLayoutVGGACyxGAA4ViewAAWL
+ _$s7SwiftUI6ButtonVyAA15ModifiedContentVyAA5ImageVAA12_FrameLayoutVGGMD
+ _$s7SwiftUI6VStackVyAA9TupleViewVyAA19_ConditionalContentVyAA0E0PAAE11buttonStyleyQrqd__AA06ButtonI0Rd__lFQOyAA0J0VyAA08ModifiedG0VyAA5ImageVAA14_PaddingLayoutVGG_14CarPlaySupport013ContactActionjI033_E85FB5A4CE27235491446378D391A496LLVQo_AiAEAJyQrqd__AaKRd__lFQOyAMyAOyAqA06_FrameN0VGG_AYQo_G_AOyAA4TextVA0_GtGGACyxGAahAWL
+ _$s7SwiftUI6VStackVyAA9TupleViewVyAA19_ConditionalContentVyAA0E0PAAE11buttonStyleyQrqd__AA06ButtonI0Rd__lFQOyAA0J0VyAA08ModifiedG0VyAA5ImageVAA14_PaddingLayoutVGG_14CarPlaySupport013ContactActionjI033_E85FB5A4CE27235491446378D391A496LLVQo_AiAEAJyQrqd__AaKRd__lFQOyAMyAOyAqA06_FrameN0VGG_AYQo_G_AOyAA4TextVA0_GtGGMD
+ _$s7SwiftUI9AlignmentV6centerACvgZ
+ _CPUIImageRowCellFirstCellContentInsets
+ _OBJC_CLASS_$_ISIcon
+ _OBJC_CLASS_$_ISImageDescriptor
+ _OBJC_CLASS_$_SBSUITraitHomeScreenIconStyle
+ _OBJC_IVAR_$_CPSAudioPlaybackManager._placeholderTimer
+ _OBJC_IVAR_$_CPSBannerView._iconImageQueue
+ _OBJC_IVAR_$_CPSMapButton._hasFocusedImage
+ _OBJC_IVAR_$_CPSSectionedDataSource._isLimitingLists
+ __OBJC_$_PROP_LIST_CPSBaseTemplateViewController.317
+ ___35-[CPSPanButton updateConfiguration]_block_invoke
+ ___38-[CPSActionButton updateConfiguration]_block_invoke
+ ___38-[CPSSectionedDataSource reloadItems:]_block_invoke.43
+ ___41-[CPSEntityMapButton updateConfiguration]_block_invoke
+ ___45-[CPSListTemplateViewController _viewDidLoad]_block_invoke.187
+ ___45-[CPSListTemplateViewController _viewDidLoad]_block_invoke.189
+ ___45-[CPSListTemplateViewController _viewDidLoad]_block_invoke.191
+ ___45-[CPSListTemplateViewController _viewDidLoad]_block_invoke_2.192
+ ___45-[CPSListTemplateViewController _viewDidLoad]_block_invoke_3.195
+ ___52-[CPSBannerView applicationIconImageWithCompletion:]_block_invoke
+ ___52-[CPSGuidanceBannerView _updateApplicationIconImage]_block_invoke
+ ___52-[CPSGuidanceBannerView _updateApplicationIconImage]_block_invoke_2
+ ___53-[CPSAudioPlaybackManager setPlaceholderTimerActive:]_block_invoke
+ ___57-[CPSDashboardGuidanceViewController setShortCutButtons:]_block_invoke.44
+ ___57-[CPSDashboardGuidanceViewController setShortCutButtons:]_block_invoke_2.46
+ ___61-[CPSMapTemplateViewController showNavigationAlert:animated:]_block_invoke.199
+ ___62-[CPSTemplateInstance viewController:didUpdateSafeAreaInsets:]_block_invoke.202
+ ___62-[CPSTemplateInstance viewController:didUpdateSafeAreaInsets:]_block_invoke.203
+ ___77-[CPSTemplateInstance presentVoiceTemplate:withProxyDelegate:animated:reply:]_block_invoke.123
+ ___90-[CPSTemplateInstance pushMapTemplate:withProxyDelegate:animated:presentationStyle:reply:]_block_invoke.113
+ ___91-[CPSTemplateInstance pushGridTemplate:withProxyDelegate:animated:presentationStyle:reply:]_block_invoke.109
+ ___91-[CPSTemplateInstance pushListTemplate:withProxyDelegate:animated:presentationStyle:reply:]_block_invoke.115
+ ___91-[CPSTemplateInstance pushListTemplate:withProxyDelegate:animated:presentationStyle:reply:]_block_invoke.117
+ ___93-[CPSTemplateInstance pushEntityTemplate:withProxyDelegate:animated:presentationStyle:reply:]_block_invoke.130
+ ___93-[CPSTemplateInstance pushSearchTemplate:withProxyDelegate:animated:presentationStyle:reply:]_block_invoke.121
+ ___97-[CPSTemplateInstance pushNowPlayingTemplate:withProxyDelegate:animated:presentationStyle:reply:]_block_invoke.118
+ ___98-[CPSTemplateInstance pushInformationTemplate:withProxyDelegate:animated:presentationStyle:reply:]_block_invoke.111
+ ___block_descriptor_40_e8_32s_e17_v16?0"UIImage"8ls32l8
+ ___block_descriptor_40_e8_32w_e17_v16?0"NSTimer"8lw32l8
+ ___block_descriptor_41_e8_32s_e26_"UIColor"16?0"UIColor"8ls32l8
+ ___block_literal_global.103
+ ___block_literal_global.136
+ ___block_literal_global.139
+ ___block_literal_global.172
+ ___block_literal_global.178
+ ___block_literal_global.183
+ ___block_literal_global.267
+ ___block_literal_global.289
+ ___block_literal_global.292
+ ___block_literal_global.294
+ ___block_literal_global.297
+ ___block_literal_global.299
+ ___block_literal_global.301
+ ___block_literal_global.303
+ ___block_literal_global.305
+ ___block_literal_global.311
+ ___block_literal_global.36
+ ___block_literal_global.48
+ ___block_literal_global.97
+ _dispatch_queue_attr_make_with_autorelease_frequency
+ _dispatch_queue_attr_make_with_qos_class
+ _get_witness_table 7SwiftUI15ModifiedContentVyACyACyAA4ViewPAAE11glassEffect_2inQrAA5GlassV_qd__tAA5ShapeRd__lFQOyAA24ButtonStyleConfigurationV5LabelV_AA6CircleVQo_AA011_BackgroundL8ModifierVyAA5ColorVGGAA011_ForegroundlQ0VyAUGGAA05_ClipG0VyAPGGAaDHPA_AaDHPAwaDHPqd0__AaDHD3_AQHO_AvA0eQ0HPyHCHC_AzAA4_HPyHCHC_A2_AAA4_HPyHCHC.40
+ _get_witness_table 7SwiftUI6VStackVyAA9TupleViewVyAA19_ConditionalContentVyAA0E0PAAE11buttonStyleyQrqd__AA06ButtonI0Rd__lFQOyAA0J0VyAA08ModifiedG0VyAA5ImageVAA14_PaddingLayoutVGG_14CarPlaySupport013ContactActionjI033_E85FB5A4CE27235491446378D391A496LLVQo_AiAEAJyQrqd__AaKRd__lFQOyAMyAOyAqA06_FrameN0VGG_AYQo_G_AOyAA4TextVA0_GtGGAaHHPyHC.38
+ _kISImageDescriptorCarNotification
+ _kInternalCapabilitiesDomainInsets
+ _kInternalCapabilitiesDomainInsetsBottom
+ _kInternalCapabilitiesDomainInsetsLeft
+ _kInternalCapabilitiesDomainInsetsRight
+ _kInternalCapabilitiesDomainInsetsTop
+ _objc_msgSend$CGImage
+ _objc_msgSend$UTF8String
+ _objc_msgSend$_updateApplicationIconImage
+ _objc_msgSend$_updateLimitingLists
+ _objc_msgSend$applicationIconImageWithCompletion:
+ _objc_msgSend$artwork
+ _objc_msgSend$hasFocusedImage
+ _objc_msgSend$iconImageQueue
+ _objc_msgSend$iconServicesAppearanceUsingDarkInterfaceStyle:
+ _objc_msgSend$imageDescriptorNamed:
+ _objc_msgSend$imageWithCGImage:scale:orientation:
+ _objc_msgSend$initWithBundleIdentifier:
+ _objc_msgSend$objectForTrait:
+ _objc_msgSend$prepareImageForDescriptor:
+ _objc_msgSend$secondarySystemFillColor
+ _objc_msgSend$setAppearance:
+ _objc_msgSend$setBaseBackgroundColor:
+ _objc_msgSend$setImageColorTransformer:
+ _objc_msgSend$setPlaceholderTimerActive:
+ _objectdestroy.24Tm
+ _symbolic _____y__________G 7SwiftUI15ModifiedContentV AA4TextV AA12_FrameLayoutV
+ _symbolic _____y__________G 7SwiftUI15ModifiedContentV AA5ImageV AA12_FrameLayoutV
+ _symbolic _____y___________y_____y_____y_____y_____y__________GG______Qo______yAEyAFyAG_____GG_AKQo_G_AFy_____AMGtGG 7SwiftUI13_VariadicViewO4TreeV AA13_VStackLayoutV AA05TupleD0V AA19_ConditionalContentV AA0D0PAAE11buttonStyleyQrqd__AA06ButtonL0Rd__lFQO AA0M0V AA08ModifiedJ0V AA5ImageV AA08_PaddingG0V 14CarPlaySupport013ContactActionmL033_E85FB5A4CE27235491446378D391A496LLV AmAEANyQrqd__AaORd__lFQO AA06_FrameG0V AA4TextV
+ _symbolic _____y_____y__________GG 7SwiftUI6ButtonV AA15ModifiedContentV AA5ImageV AA12_FrameLayoutV
+ _symbolic _____y_____y_____y__________GG______Qo_ 7SwiftUI4ViewPAAE11buttonStyleyQrqd__AA06ButtonE0Rd__lFQO AA0F0V AA15ModifiedContentV AA5ImageV AA12_FrameLayoutV 14CarPlaySupport013ContactActionfE033_E85FB5A4CE27235491446378D391A496LLV
+ _symbolic _____y_____y_____y_____y__________GG______Qo______yAByACyAD_____GG_AHQo_G 7SwiftUI19_ConditionalContentV AA4ViewPAAE11buttonStyleyQrqd__AA06ButtonG0Rd__lFQO AA0H0V AA08ModifiedD0V AA5ImageV AA14_PaddingLayoutV 14CarPlaySupport013ContactActionhG033_E85FB5A4CE27235491446378D391A496LLV AeAEAFyQrqd__AaGRd__lFQO AA06_FrameL0V
+ _symbolic _____y_____y_____y_____y__________GG______Qo______yAByACyAD_____GG_AHQo_G_ACy_____AJGt 7SwiftUI19_ConditionalContentV AA4ViewPAAE11buttonStyleyQrqd__AA06ButtonG0Rd__lFQO AA0H0V AA08ModifiedD0V AA5ImageV AA14_PaddingLayoutV 14CarPlaySupport013ContactActionhG033_E85FB5A4CE27235491446378D391A496LLV AeAEAFyQrqd__AaGRd__lFQO AA06_FrameL0V AA4TextV
+ _symbolic _____y_____y_____y_____y__________GG______Qo______yAByACyAD_____GG_AHQo__G 7SwiftUI19_ConditionalContentV7StorageO AA4ViewPAAE11buttonStyleyQrqd__AA06ButtonH0Rd__lFQO AA0I0V AA08ModifiedD0V AA5ImageV AA14_PaddingLayoutV 14CarPlaySupport013ContactActioniH033_E85FB5A4CE27235491446378D391A496LLV AgAEAHyQrqd__AaIRd__lFQO AA06_FrameM0V
+ _symbolic _____y_____y_____y_____y_____y_____y__________GG______Qo______yADyAEyAF_____GG_AJQo_G_AEy_____ALGtGG 7SwiftUI6VStackV AA9TupleViewV AA19_ConditionalContentV AA0E0PAAE11buttonStyleyQrqd__AA06ButtonI0Rd__lFQO AA0J0V AA08ModifiedG0V AA5ImageV AA14_PaddingLayoutV 14CarPlaySupport013ContactActionjI033_E85FB5A4CE27235491446378D391A496LLV AiAEAJyQrqd__AaKRd__lFQO AA06_FrameN0V AA4TextV
- -[CPSActionButton _updateFocusedView]
- -[CPSActionButton buttonAttributes]
- -[CPSActionButton disabledButtonFocused]
- -[CPSActionButton setButtonAttributes:]
- -[CPSActionButton setDisabledButtonFocused:]
- -[CPSActionButton setTintColor:forState:]
- -[CPSAudioPlaybackManager nowPlayingManager:didReceiveArtwork:forArtworkCatalog:]
- -[CPSBannerView applicationIconImage]
- -[CPSEntityMapButton .cxx_destruct]
- -[CPSEntityMapButton _updateFocusedView]
- -[CPSEntityMapButton buttonAttributes]
- -[CPSMapButton _updateFocusedView]
- -[CPSMapButton buttonImageView]
- -[CPSMapButton focusedView]
- -[CPSMapButton setButtonImageView:]
- -[CPSMapButton setFocusedView:]
- -[CPSPanButton .cxx_destruct]
- -[CPSPanButton _updateFocusedView]
- _$s14CarPlaySupport23ContactActionButtonView33_E85FB5A4CE27235491446378D391A496LLV4bodyQrvg7SwiftUI05TupleG0VyAF0G0PAFE11buttonStyleyQrqd__AF0fS0Rd__lFQOyAF0F0VyAjFE7paddingyQr12CoreGraphics7CGFloatVFQOyAF5ImageV_Qo_G_AA0defS0ACLLVQo__AF4TextVtGyXEfU_
- _$s14CarPlaySupport23ContactActionButtonView33_E85FB5A4CE27235491446378D391A496LLV4bodyQrvg7SwiftUI05TupleG0VyAF0G0PAFE11buttonStyleyQrqd__AF0fS0Rd__lFQOyAF0F0VyAjFE7paddingyQr12CoreGraphics7CGFloatVFQOyAF5ImageV_Qo_G_AA0defS0ACLLVQo__AF4TextVtGyXEfU_AUyXEfU0_
- _$s14CarPlaySupport23ContactActionButtonView33_E85FB5A4CE27235491446378D391A496LLV4bodyQrvg7SwiftUI05TupleG0VyAF0G0PAFE11buttonStyleyQrqd__AF0fS0Rd__lFQOyAF0F0VyAjFE7paddingyQr12CoreGraphics7CGFloatVFQOyAF5ImageV_Qo_G_AA0defS0ACLLVQo__AF4TextVtGyXEfU_AUyXEfU0_TA
- _$s14CarPlaySupport23ContactActionButtonView33_E85FB5A4CE27235491446378D391A496LLV4bodyQrvg7SwiftUI05TupleG0VyAF0G0PAFE11buttonStyleyQrqd__AF0fS0Rd__lFQOyAF0F0VyAjFE7paddingyQr12CoreGraphics7CGFloatVFQOyAF5ImageV_Qo_G_AA0defS0ACLLVQo__AF4TextVtGyXEfU_yyScMYccfU_
- _$s14CarPlaySupport23ContactActionButtonView33_E85FB5A4CE27235491446378D391A496LLV4bodyQrvg7SwiftUI05TupleG0VyAF0G0PAFE11buttonStyleyQrqd__AF0fS0Rd__lFQOyAF0F0VyAjFE7paddingyQr12CoreGraphics7CGFloatVFQOyAF5ImageV_Qo_G_AA0defS0ACLLVQo__AF4TextVtGyXEfU_yyScMYccfU_TA
- _$s7SwiftUI11EnvironmentV7ContentOyAA11ColorSchemeO_GWOc
- _$s7SwiftUI11EnvironmentVyAA11ColorSchemeOGWOh
- _$s7SwiftUI13_VariadicViewO4TreeVy_AA13_VStackLayoutVAA05TupleD0VyAA0D0PAAE11buttonStyleyQrqd__AA06ButtonJ0Rd__lFQOyAA0K0VyAA15ModifiedContentVyAA5ImageVAA08_PaddingG0VGG_14CarPlaySupport013ContactActionkJ033_E85FB5A4CE27235491446378D391A496LLVQo__AA4TextVtGGMD
- _$s7SwiftUI15ModifiedContentVyAA5ImageVAA14_PaddingLayoutVGACyxq_GAA4ViewA2aJRzAA0H8ModifierR_rlWl
- _$s7SwiftUI4TextV7StorageOWOy
- _$s7SwiftUI4ViewPAAE11buttonStyleyQrqd__AA06ButtonE0Rd__lFQOyAA0F0VyAA15ModifiedContentVyAA5ImageVAA14_PaddingLayoutVGG_14CarPlaySupport013ContactActionfE033_E85FB5A4CE27235491446378D391A496LLVQo__AA4TextVtMD
- _$s7SwiftUI6VStackVyAA9TupleViewVyAA0E0PAAE11buttonStyleyQrqd__AA06ButtonG0Rd__lFQOyAA0H0VyAA15ModifiedContentVyAA5ImageVAA14_PaddingLayoutVGG_14CarPlaySupport013ContactActionhG033_E85FB5A4CE27235491446378D391A496LLVQo__AA4TextVtGGACyxGAafAWL
- _$s7SwiftUI6VStackVyAA9TupleViewVyAA0E0PAAE11buttonStyleyQrqd__AA06ButtonG0Rd__lFQOyAA0H0VyAA15ModifiedContentVyAA5ImageVAA14_PaddingLayoutVGG_14CarPlaySupport013ContactActionhG033_E85FB5A4CE27235491446378D391A496LLVQo__AA4TextVtGGMD
- _CPUIImageRowCellFirstCellContentInsets_Solarium
- _OBJC_IVAR_$_CPSActionButton._buttonAttributes
- _OBJC_IVAR_$_CPSActionButton._buttonImageView
- _OBJC_IVAR_$_CPSActionButton._buttonTextLabel
- _OBJC_IVAR_$_CPSActionButton._disabledButtonFocused
- _OBJC_IVAR_$_CPSActionButton._focusedView
- _OBJC_IVAR_$_CPSEntityMapButton._focusedView
- _OBJC_IVAR_$_CPSEntityMapButton._imageView
- _OBJC_IVAR_$_CPSMapButton._buttonImageView
- _OBJC_IVAR_$_CPSMapButton._focusedView
- _OBJC_IVAR_$_CPSPanButton._focusedView
- _OBJC_IVAR_$_CPSPanButton._imageView
- __OBJC_$_PROP_LIST_CPSBaseTemplateViewController.302
- ___38-[CPSSectionedDataSource reloadItems:]_block_invoke.28
- ___45-[CPSListTemplateViewController _viewDidLoad]_block_invoke.172
- ___45-[CPSListTemplateViewController _viewDidLoad]_block_invoke.174
- ___45-[CPSListTemplateViewController _viewDidLoad]_block_invoke.176
- ___45-[CPSListTemplateViewController _viewDidLoad]_block_invoke_2.177
- ___45-[CPSListTemplateViewController _viewDidLoad]_block_invoke_3.180
- ___57-[CPSDashboardGuidanceViewController setShortCutButtons:]_block_invoke.29
- ___57-[CPSDashboardGuidanceViewController setShortCutButtons:]_block_invoke_2.31
- ___61-[CPSMapTemplateViewController showNavigationAlert:animated:]_block_invoke.184
- ___62-[CPSTemplateInstance viewController:didUpdateSafeAreaInsets:]_block_invoke.187
- ___62-[CPSTemplateInstance viewController:didUpdateSafeAreaInsets:]_block_invoke.188
- ___77-[CPSTemplateInstance presentVoiceTemplate:withProxyDelegate:animated:reply:]_block_invoke.108
- ___90-[CPSTemplateInstance pushMapTemplate:withProxyDelegate:animated:presentationStyle:reply:]_block_invoke.98
- ___91-[CPSTemplateInstance pushGridTemplate:withProxyDelegate:animated:presentationStyle:reply:]_block_invoke.94
- ___91-[CPSTemplateInstance pushListTemplate:withProxyDelegate:animated:presentationStyle:reply:]_block_invoke.100
- ___91-[CPSTemplateInstance pushListTemplate:withProxyDelegate:animated:presentationStyle:reply:]_block_invoke.102
- ___93-[CPSTemplateInstance pushEntityTemplate:withProxyDelegate:animated:presentationStyle:reply:]_block_invoke.115
- ___93-[CPSTemplateInstance pushSearchTemplate:withProxyDelegate:animated:presentationStyle:reply:]_block_invoke.106
- ___97-[CPSTemplateInstance pushNowPlayingTemplate:withProxyDelegate:animated:presentationStyle:reply:]_block_invoke.103
- ___98-[CPSTemplateInstance pushInformationTemplate:withProxyDelegate:animated:presentationStyle:reply:]_block_invoke.96
- ___NSDictionary0__struct
- ___block_literal_global.121
- ___block_literal_global.124
- ___block_literal_global.153
- ___block_literal_global.157
- ___block_literal_global.163
- ___block_literal_global.21
- ___block_literal_global.252
- ___block_literal_global.274
- ___block_literal_global.277
- ___block_literal_global.279
- ___block_literal_global.282
- ___block_literal_global.284
- ___block_literal_global.286
- ___block_literal_global.288
- ___block_literal_global.290
- ___block_literal_global.296
- ___block_literal_global.33
- ___block_literal_global.82
- ___block_literal_global.88
- _get_witness_table 7SwiftUI15ModifiedContentVyACyACyAA4ViewPAAE11glassEffect_2inQrAA5GlassV_qd__tAA5ShapeRd__lFQOyAA24ButtonStyleConfigurationV5LabelV_AA6CircleVQo_AA011_BackgroundL8ModifierVyAA5ColorVGGAA011_ForegroundlQ0VyAUGGAA05_ClipG0VyAPGGAaDHPA_AaDHPAwaDHPqd0__AaDHD3_AQHO_AvA0eQ0HPyHCHC_AzAA4_HPyHCHC_A2_AAA4_HPyHCHC.36
- _get_witness_table 7SwiftUI6VStackVyAA9TupleViewVyAA0E0PAAE11buttonStyleyQrqd__AA06ButtonG0Rd__lFQOyAA0H0VyAA15ModifiedContentVyAA5ImageVAA14_PaddingLayoutVGG_14CarPlaySupport013ContactActionhG033_E85FB5A4CE27235491446378D391A496LLVQo__AA4TextVtGGAaFHPyHC.34
- _objc_msgSend$_updateFocusedView
- _objc_msgSend$applicationIconImage
- _objc_msgSend$buttonImageView
- _objc_msgSend$focusedView
- _objc_msgSend$layoutWithLayoutType:
- _objc_msgSend$preferredArtworkScale
- _objc_msgSend$setButtonImageView:
- _objc_msgSend$setFocusedView:
- _objc_msgSend$setShowETA:
- _objc_msgSend$setTintColors:
- _objc_msgSend$tintColors
- _symbolic _____y___________y_____y_____y_____y__________GG______Qo_______tGG 7SwiftUI13_VariadicViewO4TreeV AA13_VStackLayoutV AA05TupleD0V AA0D0PAAE11buttonStyleyQrqd__AA06ButtonJ0Rd__lFQO AA0K0V AA15ModifiedContentV AA5ImageV AA08_PaddingG0V 14CarPlaySupport013ContactActionkJ033_E85FB5A4CE27235491446378D391A496LLV AA4TextV
- _symbolic _____y_____y_____y__________GG______Qo_______t 7SwiftUI4ViewPAAE11buttonStyleyQrqd__AA06ButtonE0Rd__lFQO AA0F0V AA15ModifiedContentV AA5ImageV AA14_PaddingLayoutV 14CarPlaySupport013ContactActionfE033_E85FB5A4CE27235491446378D391A496LLV AA4TextV
- _symbolic _____y_____y_____y_____y_____y__________GG______Qo_______tGG 7SwiftUI6VStackV AA9TupleViewV AA0E0PAAE11buttonStyleyQrqd__AA06ButtonG0Rd__lFQO AA0H0V AA15ModifiedContentV AA5ImageV AA14_PaddingLayoutV 14CarPlaySupport013ContactActionhG033_E85FB5A4CE27235491446378D391A496LLV AA4TextV
CStrings:
+ "$$"
+ "Artwork placeholder timer fired."
+ "Artwork response is not visually identical to current snapshot; ignoring."
+ "B#"
+ "Bottom"
+ "CARCapabilitesInsets"
+ "CGImage"
+ "Cancelling artwork placeholder timer."
+ "Left"
+ "Limited user interface changed to %{public}@"
+ "Received a now playing update for a different app: %{public}@ vs ours: %{public}@"
+ "Received an artwork update for a different app: %{public}@ vs ours: %{public}@"
+ "Received an artwork update for the current catalog."
+ "Right"
+ "Scheduling artwork placeholder timer."
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_iconImageQueue"
+ "T@\"NSTimer\",&,N,V_placeholderTimer"
+ "TB,N,V_hasFocusedImage"
+ "TB,N,V_isLimitingLists"
+ "Top"
+ "UTF8String"
+ "_hasFocusedImage"
+ "_iconImageQueue"
+ "_isLimitingLists"
+ "_placeholderTimer"
+ "_updateApplicationIconImage"
+ "_updateLimitingLists"
+ "applicationIconImageWithCompletion:"
+ "artwork"
+ "com.apple.carplaysupport.CPSBannerView-%p"
+ "hasFocusedImage"
+ "iconImageQueue"
+ "iconServicesAppearanceUsingDarkInterfaceStyle:"
+ "imageDescriptorNamed:"
+ "imageWithCGImage:scale:orientation:"
+ "nowPlayingManager:didReceiveArtworkResponse:"
+ "nowPlayingManager:willStartLoadingArtworkForCatalog:bundleIdentifier:"
+ "objectForTrait:"
+ "placeholderTimer"
+ "prepareImageForDescriptor:"
+ "secondarySystemFillColor"
+ "setAppearance:"
+ "setBaseBackgroundColor:"
+ "setHasFocusedImage:"
+ "setIconImageQueue:"
+ "setImageColorTransformer:"
+ "setIsLimitingLists:"
+ "setPlaceholderTimer:"
+ "setPlaceholderTimerActive:"
+ "v16@?0@\"UIImage\"8"
+ "v32@0:8@\"CPUINowPlayingManager\"16@\"CPUINowPlayingSnapshotArtwork\"24"
+ "v40@0:8@\"CPUINowPlayingManager\"16@\"MPArtworkCatalog\"24@\"NSString\"32"
- "$#"
- "%@: Cluster safe area width %@ greater than 300. Showing ETA."
- "%@: Cluster safe area width %@ less/equal to 300. Using center layout."
- "2#"
- "@\"NSDictionary\""
- "Limited user interface changed to %@"
- "Received a now playing update for a different app: %@ vs ours: %@"
- "T@\"NSDictionary\",&,N,V_buttonAttributes"
- "T@\"UIImageView\",&,N,V_buttonImageView"
- "T@\"UIView\",&,N,V_focusedView"
- "TB,N,V_disabledButtonFocused"
- "Template artwork size %{public}@, scale %{public}@"
- "_buttonAttributes"
- "_buttonImageView"
- "_buttonTextLabel"
- "_disabledButtonFocused"
- "_focusedView"
- "_updateFocusedView"
- "applicationIconImage"
- "buttonAttributes"
- "buttonImageView"
- "disabledButtonFocused"
- "focusedView"
- "nowPlayingManager:didReceiveArtwork:forArtworkCatalog:"
- "nowPlayingManager:willStartLoadingArtworkForCatalog:"
- "preferredArtworkScale"
- "setButtonAttributes:"
- "setButtonImageView:"
- "setDisabledButtonFocused:"
- "setFocusedView:"
- "setTintColor:forState:"
- "tertiarySystemBackgroundColor"
- "v32@0:8@\"CPUINowPlayingManager\"16@\"MPArtworkCatalog\"24"
- "v40@0:8@\"CPUINowPlayingManager\"16@\"UIImage\"24@\"MPArtworkCatalog\"32"

```
