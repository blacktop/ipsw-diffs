## FeedbackCore

> `/System/Library/PrivateFrameworks/FeedbackCore.framework/FeedbackCore`

### Sections with Same Size but Changed Content

- `__TEXT.__ustring`

```diff

-238.0.0.0.0
-  __TEXT.__text: 0x141ba8
+240.0.0.0.0
+  __TEXT.__text: 0x1434dc
   __TEXT.__lazy_helpers: 0x2a0
-  __TEXT.__objc_methlist: 0xb934
-  __TEXT.__const: 0x3a44
-  __TEXT.__cstring: 0xa4c8
-  __TEXT.__oslogstring: 0xb006
+  __TEXT.__objc_methlist: 0xb9bc
+  __TEXT.__const: 0x3bc4
+  __TEXT.__cstring: 0xa60b
+  __TEXT.__oslogstring: 0xb20e
+  __TEXT.__gcc_except_tab: 0x1610
   __TEXT.__ustring: 0xe6
-  __TEXT.__gcc_except_tab: 0x15f0
   __TEXT.__dlopen_cstrs: 0x62
-  __TEXT.__constg_swiftt: 0x1fc0
-  __TEXT.__swift5_typeref: 0x3ec2
+  __TEXT.__constg_swiftt: 0x206c
+  __TEXT.__swift5_typeref: 0x3dbe
   __TEXT.__swift5_builtin: 0xdc
-  __TEXT.__swift5_reflstr: 0xd1b
-  __TEXT.__swift5_fieldmd: 0xea4
+  __TEXT.__swift5_reflstr: 0xd62
+  __TEXT.__swift5_fieldmd: 0xf14
   __TEXT.__swift5_assocty: 0x2b8
-  __TEXT.__swift5_proto: 0x174
-  __TEXT.__swift5_types: 0x154
+  __TEXT.__swift5_proto: 0x180
+  __TEXT.__swift5_types: 0x15c
   __TEXT.__swift5_capture: 0xd5c
   __TEXT.__swift_as_entry: 0xc
   __TEXT.__swift_as_ret: 0xc
   __TEXT.__swift_as_cont: 0x24
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__unwind_info: 0x6480
-  __TEXT.__eh_frame: 0x1360
+  __TEXT.__unwind_info: 0x6548
+  __TEXT.__eh_frame: 0x12d0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x42d8
-  __DATA_CONST.__objc_classlist: 0x550
+  __DATA_CONST.__const: 0x4300
+  __DATA_CONST.__objc_classlist: 0x558
   __DATA_CONST.__objc_catlist: 0xc0
   __DATA_CONST.__objc_protolist: 0x238
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7800
+  __DATA_CONST.__objc_selrefs: 0x7850
   __DATA_CONST.__objc_protorefs: 0x98
-  __DATA_CONST.__objc_superrefs: 0x278
+  __DATA_CONST.__objc_superrefs: 0x280
   __DATA_CONST.__objc_arraydata: 0x580
-  __DATA_CONST.__got: 0x11f8
-  __AUTH_CONST.__const: 0x49a0
-  __AUTH_CONST.__cfstring: 0x9200
-  __AUTH_CONST.__objc_const: 0x1db50
+  __DATA_CONST.__got: 0x1268
+  __AUTH_CONST.__const: 0x4a18
+  __AUTH_CONST.__cfstring: 0x92c0
+  __AUTH_CONST.__objc_const: 0x1dca8
   __AUTH_CONST.__lazy_load_got: 0x40
   __AUTH_CONST.__objc_intobj: 0x318
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_arrayobj: 0x4c8
-  __AUTH_CONST.__auth_got: 0x1810
-  __AUTH.__objc_data: 0xbb0
-  __AUTH.__data: 0x1f8
-  __DATA.__objc_ivar: 0x730
-  __DATA.__data: 0x2d84
+  __AUTH_CONST.__auth_got: 0x1888
+  __AUTH.__objc_data: 0x5228
+  __AUTH.__data: 0xf78
+  __DATA.__objc_ivar: 0x73c
+  __DATA.__data: 0x2fb4
   __DATA.__objc_stublist: 0x8
-  __DATA.__common: 0x120
-  __DATA_DIRTY.__objc_data: 0x4678
-  __DATA_DIRTY.__data: 0xe68
-  __DATA_DIRTY.__bss: 0x1e0
-  __DATA_DIRTY.__common: 0x40
+  __DATA.__common: 0x160
+  __DATA_DIRTY.__objc_data: 0x50
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/Combine.framework/Combine

   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/ImageIO.framework/ImageIO
   - /System/Library/Frameworks/Intents.framework/Intents
-  - /System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication
   - /System/Library/Frameworks/PhotosUI.framework/PhotosUI
   - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
   - /System/Library/Frameworks/QuickLook.framework/QuickLook

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftObservation.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftRegexBuilder.dylib
   - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 7728
-  Symbols:   10404
-  CStrings:  2632
+  Functions: 7786
+  Symbols:   10459
+  CStrings:  2647
 
Symbols:
+ +[FBKEnvironmentConfig configForEnvironmentName:]
+ +[FBKEnvironmentConfig internalEnvironmentsByName]
+ +[FBKEnvironmentConfig isInternalInstall]
+ +[FBKEnvironmentConfig productionConfig]
+ +[FBKEnvironmentConfig resolvedConfigForEnvironmentName:]
+ +[FBKEnvironmentConfig resolvedConfigForEnvironmentName:defaults:]
+ +[FBKSharedConstants currentConfigLogDescription]
+ +[FBKSharedConstants currentConfig]
+ +[FBKSharedConstants displayTitleForEnvironmentName:]
+ +[FBKSharedConstants seedingCookieName]
+ +[FBKSharedConstants seedingFilerURL]
+ +[FBKSharedConstants usesCertificatePinning]
+ +[FBKSharedConstants usesProductionAuthentication]
+ -[FBKEnvironmentConfig .cxx_destruct]
+ -[FBKEnvironmentConfig cookieName]
+ -[FBKEnvironmentConfig description]
+ -[FBKEnvironmentConfig disableCertificatePinning]
+ -[FBKEnvironmentConfig filerURL]
+ -[FBKEnvironmentConfig host]
+ -[FBKEnvironmentConfig initWithName:host:disableCertificatePinning:usesUATAuth:cookieName:filerURL:]
+ -[FBKEnvironmentConfig logDescription]
+ -[FBKEnvironmentConfig name]
+ -[FBKEnvironmentConfig usesUATAuth]
+ _CGImageSourceCreateThumbnailAtIndex
+ _CGImageSourceCreateWithURL
+ _FBKBoolFromPlistEntry
+ _FBKSCustomCookieNameKey
+ _FBKSCustomDisableCertificatePinningKey
+ _FBKSCustomFilerURLKey
+ _FBKSCustomHostKey
+ _FBKSCustomUsesUATAuthKey
+ _FBKSLog
+ _FBKStringFromPlistEntry
+ _FBKValidateBoolField
+ _FBKValidateStringField
+ _OBJC_CLASS_$_FBKEnvironmentConfig
+ _OBJC_IVAR_$_FBKEnvironmentConfig._cookieName
+ _OBJC_IVAR_$_FBKEnvironmentConfig._disableCertificatePinning
+ _OBJC_IVAR_$_FBKEnvironmentConfig._filerURL
+ _OBJC_IVAR_$_FBKEnvironmentConfig._host
+ _OBJC_IVAR_$_FBKEnvironmentConfig._name
+ _OBJC_IVAR_$_FBKEnvironmentConfig._usesUATAuth
+ _OBJC_METACLASS_$_FBKEnvironmentConfig
+ __OBJC_$_CATEGORY_NSDate_$_FBKString
+ __OBJC_$_CLASS_METHODS_FBKEnvironmentConfig
+ __OBJC_$_CLASS_METHODS_NSDate(FBKString|Utils)
+ __OBJC_$_INSTANCE_METHODS_FBKDeviceDisplayCell(FeedbackCore)
+ __OBJC_$_INSTANCE_METHODS_FBKEnvironmentConfig
+ __OBJC_$_INSTANCE_METHODS_NSDate(FBKString|Utils)
+ __OBJC_$_INSTANCE_VARIABLES_FBKEnvironmentConfig
+ __OBJC_$_PROP_LIST_FBKEnvironmentConfig
+ __OBJC_CLASS_RO_$_FBKEnvironmentConfig
+ __OBJC_METACLASS_RO_$_FBKEnvironmentConfig
+ ___40+[FBKEnvironmentConfig productionConfig]_block_invoke
+ ___50+[FBKEnvironmentConfig internalEnvironmentsByName]_block_invoke
+ ___block_descriptor_40_e8_32s_e15_v32?0816^B24ls32l8
+ ___block_descriptor_64_e8_32s40s48s56w_e16_v16?0"NSData"8lw56l8s32l8s40l8s48l8
+ ___block_descriptor_65_e8_32s40bs_e18_v16?0"NSString"8ls32l8s40l8
+ _associated conformance 12FeedbackCore19FBKIconTitleRowViewVyxG7SwiftUI0F0AA4BodyAeFP_AeF
+ _associated conformance So11CFStringRefa14CoreFoundation9_CFObjectSCSH
+ _associated conformance So11CFStringRefaSHSCSQ
+ _get_enum_tag_for_layout_string 12FeedbackCore19FBKIconTitleRowViewV9AccessoryOyx_G
+ _get_witness_table 7SwiftUI15ModifiedContentVyAA4ViewPAAE20accessibilityElement8childrenQrAA26AccessibilityChildBehaviorV_tFQOyACy12FeedbackCore015FBKIconTitleRowE0VyAJ014AttachmentIconE0VGAA14_PaddingLayoutVG_Qo_AA0iQ8ModifierVGAaDHPqd__AaDHD2_ASHO_AuA0eU0HPyHCHC
+ _get_witness_table 7SwiftUI15ModifiedContentVyACyAA6VStackVyAA012_ConditionalD0VyACyACyACyAA5ImageVAA12_FrameLayoutVGAA24_ForegroundStyleModifierVyAA09TintShapeK0VGGAKG12FeedbackCore21AttachmentPreviewViewVGGAKGAA13_OffsetEffectVGAA0S0HPAyAA1_HPAxAA1_HPyHC_AkA0sL0HPyHCHC_A_AAA2_HPyHCHC
+ _get_witness_table 7SwiftUI4ViewRzlAA6HStackVyAA12TupleContentVyAA08ModifiedF0VyAHyxAA12_FrameLayoutVGAA08_PaddingI0VG_AHyAHyAA6VStackVyAFyAA012_ConditionalF0VyAA4TextVATG_AHyAHyAtA30_EnvironmentKeyWritingModifierVySiSgGGAWyAT14TruncationModeOGGSgA3_QPGGAMGAMGAA6SpacerVARyARyAA05EmptyC0VAHyAHyAtA010_FixedSizeI0VGAA023AccessibilityAttachmentQ0VGGAHyAHyAA5ImageVAWyAA4FontVSgGGAA016_ForegroundStyleQ0VyAA22HierarchicalShapeStyleVGGGQPGGAaBHPyHC
+ _internalEnvironmentsByName.environments
+ _internalEnvironmentsByName.onceToken
+ _kCGImageSourceCreateThumbnailFromImageIfAbsent
+ _kCGImageSourceCreateThumbnailWithTransform
+ _kCGImageSourceShouldCache
+ _kCGImageSourceShouldCacheImmediately
+ _kCGImageSourceThumbnailMaxPixelSize
+ _keypath_get.26Tm
+ _keypath_get.32Tm
+ _objc_msgSend$configForEnvironmentName:
+ _objc_msgSend$cookieName
+ _objc_msgSend$currentConfig
+ _objc_msgSend$currentConfigLogDescription
+ _objc_msgSend$dictionaryWithContentsOfFile:
+ _objc_msgSend$disableCertificatePinning
+ _objc_msgSend$enumerateKeysAndObjectsUsingBlock:
+ _objc_msgSend$fbk_updateHostedContentWithName:type:icon:
+ _objc_msgSend$filerURL
+ _objc_msgSend$initWithName:host:disableCertificatePinning:usesUATAuth:cookieName:filerURL:
+ _objc_msgSend$internalEnvironmentsByName
+ _objc_msgSend$isInternalInstall
+ _objc_msgSend$itemIdentifier
+ _objc_msgSend$logDescription
+ _objc_msgSend$productionConfig
+ _objc_msgSend$resolvedConfigForEnvironmentName:
+ _objc_msgSend$resolvedConfigForEnvironmentName:defaults:
+ _objc_msgSend$seedingCookieName
+ _objc_msgSend$seedingFilerURL
+ _objc_msgSend$setSeedingCookieName:
+ _objc_msgSend$setSeedingFilerURL:
+ _objc_msgSend$setSeedingUsesPinning:
+ _objc_msgSend$usesCertificatePinning
+ _objc_msgSend$usesProductionAuthentication
+ _objc_msgSend$usesUATAuth
+ _productionConfig.config
+ _productionConfig.onceToken
+ _swift_checkMetadataState
+ _swift_cvw_allocateGenericValueMetadataWithLayoutString
+ _swift_cvw_instantiateLayoutString
+ _swift_getTupleTypeMetadata
+ _symbolic _____ 12FeedbackCore19FBKIconTitleRowViewV
+ _symbolic _____ 12FeedbackCore19FBKIconTitleRowViewV9AccessoryO
+ _symbolic ______ypt So11CFStringRefa
+ _symbolic _____yAAy__________yACy__________G_____GGACyACy__________y_____SgGG_____y_____GGG 7SwiftUI19_ConditionalContentV AA9EmptyViewV AA08ModifiedD0V AA4TextV AA16_FixedSizeLayoutV AA31AccessibilityAttachmentModifierV AA5ImageV AA022_EnvironmentKeyWritingN0V AA4FontV AA016_ForegroundStyleN0V AA017HierarchicalShapeU0V
+ _symbolic _____yAAy_____y_____yAAyAAyAAy__________G_____y_____GGAEG_____GGAEG_____G 7SwiftUI15ModifiedContentV AA6VStackV AA012_ConditionalD0V AA5ImageV AA12_FrameLayoutV AA24_ForegroundStyleModifierV AA09TintShapeK0V 12FeedbackCore21AttachmentPreviewViewV AA13_OffsetEffectV
+ _symbolic _____y_____G 12FeedbackCore19FBKIconTitleRowViewV AA014AttachmentIconF0V
+ _symbolic _____y__________yACy__________G_____GG 7SwiftUI19_ConditionalContentV AA9EmptyViewV AA08ModifiedD0V AA4TextV AA16_FixedSizeLayoutV AA31AccessibilityAttachmentModifierV
+ _symbolic _____y__________yACy__________G_____G_G 7SwiftUI19_ConditionalContentV7StorageO AA9EmptyViewV AA08ModifiedD0V AA4TextV AA16_FixedSizeLayoutV AA31AccessibilityAttachmentModifierV
+ _symbolic _____y______yptG s23_ContiguousArrayStorageC So11CFStringRefa
+ _symbolic _____y_____yAAy_____y_____G_____G_Qo______G 7SwiftUI15ModifiedContentV AA4ViewPAAE20accessibilityElement8childrenQrAA26AccessibilityChildBehaviorV_tFQO 12FeedbackCore015FBKIconTitleRowE0V AJ014AttachmentIconE0V AA14_PaddingLayoutV AA0iQ8ModifierV
+ _symbolic _____y_____yABy__________G_____GG 12FeedbackCore19FBKIconTitleRowViewV 7SwiftUI15ModifiedContentV AD5ImageV AD18_AspectRatioLayoutV AD06_FrameN0V
+ _symbolic _____y_____y_____G_____G 7SwiftUI15ModifiedContentV 12FeedbackCore19FBKIconTitleRowViewV AD014AttachmentIconJ0V AA14_PaddingLayoutV
+ _symbolic _____y_____y__________yADy__________G_____GGADyADy__________y_____SgGG_____y_____GG_G 7SwiftUI19_ConditionalContentV7StorageO AC AA9EmptyViewV AA08ModifiedD0V AA4TextV AA16_FixedSizeLayoutV AA31AccessibilityAttachmentModifierV AA5ImageV AA022_EnvironmentKeyWritingO0V AA4FontV AA016_ForegroundStyleO0V AA017HierarchicalShapeV0V
+ _symbolic _____y_____y_____yACy__________G_____GG_____G 7SwiftUI22UIHostingConfigurationV 12FeedbackCore19FBKIconTitleRowViewV AA15ModifiedContentV AA5ImageV AA18_AspectRatioLayoutV AA06_FrameP0V AA05EmptyJ0V
+ _symbolic _____y_____y_____yACyx_____G_____G_ACyACy_____yABy_____y_____AJG_ACyACyAJ_____ySiSgGGALy_____GGSgASQPGGAFGAFG_____AIyAIy_____ACyACyAJ_____G_____GGACyACy_____ALy_____SgGG_____y_____GGGQPGG 7SwiftUI6HStackV AA12TupleContentV AA08ModifiedE0V AA12_FrameLayoutV AA08_PaddingH0V AA6VStackV AA012_ConditionalE0V AA4TextV AA30_EnvironmentKeyWritingModifierV AQ14TruncationModeO AA6SpacerV AA9EmptyViewV AA010_FixedSizeH0V AA023AccessibilityAttachmentP0V AA5ImageV AA4FontV AA016_ForegroundStyleP0V AA22HierarchicalShapeStyleV
+ _symbolic _____y_____y_____y_____ADG______yAFyAD_____ySiSgGGAGy_____GGSgANQPGG 7SwiftUI6VStackV AA12TupleContentV AA012_ConditionalE0V AA4TextV AA08ModifiedE0V AA30_EnvironmentKeyWritingModifierV AI14TruncationModeO
+ _symbolic _____y_____y_____y_____G_____G_Qo_ 7SwiftUI4ViewPAAE20accessibilityElement8childrenQrAA26AccessibilityChildBehaviorV_tFQO AA15ModifiedContentV 12FeedbackCore015FBKIconTitleRowC0V AJ014AttachmentIconC0V AA14_PaddingLayoutV
+ _symbolic _____y_____ypG s18_DictionaryStorageC So11CFStringRefa
+ _symbolic _____yx_G 12FeedbackCore19FBKIconTitleRowViewV9AccessoryO
+ _type_layout_string 7SwiftUI4ViewRzl12FeedbackCore015FBKIconTitleRowC0V9AccessoryOyx_G
- +[FBKDEDHelper _seedingHost]
- +[FBKSharedConstants isProductionEnvironment]
- +[iFBKUtils deviceSupportsFaceID]
- -[FBKDeviceDisplayCell deviceIcon]
- -[FBKDeviceDisplayCell layoutSubviews]
- -[FBKDeviceDisplayCell nameLabel]
- -[FBKDeviceDisplayCell setDeviceIcon:]
- -[FBKDeviceDisplayCell setNameLabel:]
- -[FBKDeviceDisplayCell setTypeLabel:]
- -[FBKDeviceDisplayCell setupConstraints]
- -[FBKDeviceDisplayCell setupViews]
- -[FBKDeviceDisplayCell traitCollectionDidChange:]
- -[FBKDeviceDisplayCell typeLabel]
- -[FBKDeviceDisplayCell updateNumberOfLines]
- _FBKDraftingExtensionResourceMemoryLimit
- _FBKSEnvironmentDemoString
- _FBKSEnvironmentDevelopmentString
- _FBKSEnvironmentProductionString
- _FBKSEnvironmentStagingDevString
- _FBKSEnvironmentStagingString
- _NSURLFileSizeKey
- _OBJC_CLASS_$_LAContext
- _OBJC_IVAR_$_FBKDeviceDisplayCell._deviceIcon
- _OBJC_IVAR_$_FBKDeviceDisplayCell._nameLabel
- _OBJC_IVAR_$_FBKDeviceDisplayCell._typeLabel
- __OBJC_$_CATEGORY_CLASS_METHODS_NSDate_$_Utils
- __OBJC_$_CATEGORY_NSDate_$_Utils
- __OBJC_$_INSTANCE_METHODS_FBKDeviceDisplayCell
- __OBJC_$_INSTANCE_METHODS_NSDate(Utils|FBKString)
- ___28+[FBKDEDHelper _seedingHost]_block_invoke
- ___33+[iFBKUtils deviceSupportsFaceID]_block_invoke
- ___block_descriptor_73_e8_32s40bs_e18_v16?0"NSString"8ls32l8s40l8
- __seedingHost._host
- __seedingHost.onceToken
- _associated conformance 12FeedbackCore23AttachmentAccessoryViewV7SwiftUI0E0AA4BodyAdEP_AdE
- _deviceSupportsFaceID._usesFaceID
- _deviceSupportsFaceID.onceToken
- _get_witness_table 7SwiftUI15ModifiedContentVyAA4ViewPAAE20accessibilityElement8childrenQrAA26AccessibilityChildBehaviorV_tFQOyACyAA6HStackVyAA05TupleD0VyACyACyACy12FeedbackCore014AttachmentIconE0VAA14_PaddingLayoutVGARGARG_ACyACyAA6VStackVyAMyAA012_ConditionalD0VyAA4TextVA_G_ACyACyA_AA30_EnvironmentKeyWritingModifierVySiSgGGA2_yA_14TruncationModeOGGSgA10_QPGGARGARGAA6SpacerVACyAN0p9AccessoryE0VARGQPGGARG_Qo_AA0ipZ0VGAaDHPqd__AaDHD2_A23_HO_A25_AA0eZ0HPyHCHC
- _get_witness_table 7SwiftUI15ModifiedContentVyAA6VStackVyAA012_ConditionalD0VyACyACyACyAA5ImageVAA12_FrameLayoutVGAA24_ForegroundStyleModifierVyAA09TintShapeK0VGGAKG12FeedbackCore21AttachmentPreviewViewVGGAKGAA0S0HPAxaZHPyHC_AkA0sL0HPyHCHC
- _get_witness_table 7SwiftUI19_ConditionalContentVyAA08ModifiedD0VyAEyAA4TextVAA16_FixedSizeLayoutVGAA31AccessibilityAttachmentModifierVGAEyAEyAA5ImageVAA022_EnvironmentKeyWritingL0VyAA4FontVSgGGAA016_ForegroundStyleL0VyAA017HierarchicalShapeS0VGGGAA4ViewHPAmAA2_HPAjAA2_HPAgAA2_HPyHC_AiA0vL0HPyHCHC_AlAA3_HPyHCHC_A0_AAA2_HPAvAA2_HPAoAA2_HPyHC_AuAA3_HPyHCHC_A_AAA3_HPyHCHCHC
- _keypath_get.24Tm
- _keypath_get.30Tm
- _objc_msgSend$_seedingHost
- _objc_msgSend$biometryType
- _objc_msgSend$canEvaluatePolicy:error:
- _objc_msgSend$deviceIcon
- _objc_msgSend$hostUrl
- _objc_msgSend$isProductionEnvironment
- _objc_msgSend$nameLabel
- _objc_msgSend$setDeviceIcon:
- _objc_msgSend$setNameLabel:
- _objc_msgSend$setTypeLabel:
- _objc_msgSend$setupConstraints
- _objc_msgSend$setupViews
- _objc_msgSend$typeLabel
- _objc_msgSend$updateNumberOfLines
- _symbolic _____ 12FeedbackCore23AttachmentAccessoryViewV
- _symbolic _____yAAyAAy__________GACGACG 7SwiftUI15ModifiedContentV 12FeedbackCore18AttachmentIconViewV AA14_PaddingLayoutV
- _symbolic _____yAAyAAy__________GACGACG_AAyAAy_____y_____y_____y_____AJG_AAyAAyAJ_____ySiSgGGALy_____GGSgASQPGGACGACG_____AAy_____ACGt 7SwiftUI15ModifiedContentV 12FeedbackCore18AttachmentIconViewV AA14_PaddingLayoutV AA6VStackV AA05TupleD0V AA012_ConditionalD0V AA4TextV AA30_EnvironmentKeyWritingModifierV AP14TruncationModeO AA6SpacerV AD0g9AccessoryI0V
- _symbolic _____yAAy__________GACG 7SwiftUI15ModifiedContentV 12FeedbackCore18AttachmentIconViewV AA14_PaddingLayoutV
- _symbolic _____ySsG s23_ContiguousArrayStorageC
- _symbolic _____y__________G 7SwiftUI15ModifiedContentV 12FeedbackCore18AttachmentIconViewV AA14_PaddingLayoutV
- _symbolic _____y__________G 7SwiftUI15ModifiedContentV 12FeedbackCore23AttachmentAccessoryViewV AA14_PaddingLayoutV
- _symbolic _____y___________y_____yADyADy__________GAFGAFG_ADyADy_____yACy_____y_____ALG_ADyADyAL_____ySiSgGGANy_____GGSgAUQPGGAFGAFG_____ADy_____AFGQPGG 7SwiftUI13_VariadicViewO4TreeV AA13_HStackLayoutV AA12TupleContentV AA08ModifiedI0V 12FeedbackCore014AttachmentIconD0V AA08_PaddingG0V AA6VStackV AA012_ConditionalI0V AA4TextV AA30_EnvironmentKeyWritingModifierV AV14TruncationModeO AA6SpacerV AL0m9AccessoryD0V
- _symbolic _____y_____yAAy_____y_____yAAyAAyAAy__________GAEGAEG_AAyAAy_____yACy_____y_____AKG_AAyAAyAK_____ySiSgGGAMy_____GGSgATQPGGAEGAEG_____AAy_____AEGQPGGAEG_Qo______G 7SwiftUI15ModifiedContentV AA4ViewPAAE20accessibilityElement8childrenQrAA26AccessibilityChildBehaviorV_tFQO AA6HStackV AA05TupleD0V 12FeedbackCore014AttachmentIconE0V AA14_PaddingLayoutV AA6VStackV AA012_ConditionalD0V AA4TextV AA30_EnvironmentKeyWritingModifierV AX14TruncationModeO AA6SpacerV AN0p9AccessoryE0V AA0ipZ0V
- _symbolic _____y_____yABy__________G_____GAByABy__________y_____SgGG_____y_____GGG 7SwiftUI19_ConditionalContentV AA08ModifiedD0V AA4TextV AA16_FixedSizeLayoutV AA31AccessibilityAttachmentModifierV AA5ImageV AA022_EnvironmentKeyWritingL0V AA4FontV AA016_ForegroundStyleL0V AA017HierarchicalShapeS0V
- _symbolic _____y_____yABy__________G_____GAByABy__________y_____SgGG_____y_____GG_G 7SwiftUI19_ConditionalContentV7StorageO AA08ModifiedD0V AA4TextV AA16_FixedSizeLayoutV AA31AccessibilityAttachmentModifierV AA5ImageV AA022_EnvironmentKeyWritingM0V AA4FontV AA016_ForegroundStyleM0V AA017HierarchicalShapeT0V
- _symbolic _____y_____y_____yAAyAAyAAy__________GAEGAEG_AAyAAy_____yACy_____y_____AKG_AAyAAyAK_____ySiSgGGAMy_____GGSgATQPGGAEGAEG_____AAy_____AEGQPGGAEG 7SwiftUI15ModifiedContentV AA6HStackV AA05TupleD0V 12FeedbackCore18AttachmentIconViewV AA14_PaddingLayoutV AA6VStackV AA012_ConditionalD0V AA4TextV AA30_EnvironmentKeyWritingModifierV AR14TruncationModeO AA6SpacerV AH0i9AccessoryK0V
- _symbolic _____y_____y_____yACyACy__________GAEGAEG_ACyACy_____yABy_____y_____AKG_ACyACyAK_____ySiSgGGAMy_____GGSgATQPGGAEGAEG_____ACy_____AEGQPGG 7SwiftUI6HStackV AA12TupleContentV AA08ModifiedE0V 12FeedbackCore18AttachmentIconViewV AA14_PaddingLayoutV AA6VStackV AA012_ConditionalE0V AA4TextV AA30_EnvironmentKeyWritingModifierV AR14TruncationModeO AA6SpacerV AH0i9AccessoryK0V
- _symbolic _____y_____y_____y_____yAAyAAyAAy__________GAEGAEG_AAyAAy_____yACy_____y_____AKG_AAyAAyAK_____ySiSgGGAMy_____GGSgATQPGGAEGAEG_____AAy_____AEGQPGGAEG_Qo_ 7SwiftUI4ViewPAAE20accessibilityElement8childrenQrAA26AccessibilityChildBehaviorV_tFQO AA15ModifiedContentV AA6HStackV AA05TupleK0V 12FeedbackCore014AttachmentIconC0V AA14_PaddingLayoutV AA6VStackV AA012_ConditionalK0V AA4TextV AA30_EnvironmentKeyWritingModifierV AX14TruncationModeO AA6SpacerV AN0p9AccessoryC0V
CStrings:
+ "/AppleInternal/Library/Application Support/com.apple.feedback/environments.plist"
+ "<%@: %@ host=%@ disablePinning=%@ usesUATAuth=%@>"
+ "Running in custom environment; skipping pinning check (internal only)."
+ "To share diagnostic logs with Apple, select all of the devices experiencing this issue. If your device is not listed, make sure it is nearby, online, and signed in to your Apple Account."
+ "To share diagnostic logs with Apple, select the device experiencing this issue. If your device is not listed, make sure it is nearby, online, and signed in to your Apple Account."
+ "Unable to get explicit display preview from fileURL %{public}s"
+ "_seedportal_session"
+ "cookieName"
+ "disableCertificatePinning"
+ "environments.plist at %{public}@ is missing or not a dictionary"
+ "environments.plist contains a malformed top-level entry (key or value has wrong type); skipping"
+ "environments.plist entry '%{public}@' failed validation; skipping"
+ "environments.plist entry '%{public}@' missing or invalid required bool field '%{public}@'"
+ "environments.plist entry '%{public}@' missing or invalid required string field '%{public}@'"
+ "filerURL"
+ "host"
+ "https://cssubmissions.apple.com/CusSeedSub/submit?version=2"
+ "https://fba.apple.com/"
+ "name=[%@] host=[%@] cookie=[%@] filer=[%@] disablePinning=[%@] usesUATAuth=[%@]"
+ "non-production followup submission for FFU [%d]: %{public}@"
+ "non-production login: %{public}@"
+ "non-production submission for form [%d]: %{public}@"
+ "usesUATAuth"
+ "v32@?0@8@16^B24"
- "Running in development/stagingDev mode; skipping pinning check (internal only)."
- "To share diagnostic logs with Apple, select all of the devices experiencing this issue. If your device is not listed, make sure it is nearby, online, and signed in to your iCloud account."
- "To share diagnostic logs with Apple, select the device experiencing this issue. If your device is not listed, make sure it is nearby, online, and signed in to your iCloud account."
- "Unable to get explicit display preview from fileURL %{public}s with error: %{public}s"
- "demo"
- "development"
- "sp"
- "staging"
- "stagingDev"
```
