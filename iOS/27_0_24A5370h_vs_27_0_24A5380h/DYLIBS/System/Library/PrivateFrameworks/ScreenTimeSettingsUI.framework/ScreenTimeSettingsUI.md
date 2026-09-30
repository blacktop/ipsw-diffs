## ScreenTimeSettingsUI

> `/System/Library/PrivateFrameworks/ScreenTimeSettingsUI.framework/ScreenTimeSettingsUI`

```diff

-  __TEXT.__text: 0x124f50
-  __TEXT.__objc_methlist: 0xc4dc
+  __TEXT.__text: 0x12730c
+  __TEXT.__objc_methlist: 0xc61c
   __TEXT.__const: 0x3d44
-  __TEXT.__cstring: 0xd355
-  __TEXT.__oslogstring: 0x5f53
+  __TEXT.__cstring: 0xd6e5
+  __TEXT.__oslogstring: 0x60e3
   __TEXT.__gcc_except_tab: 0x1228
   __TEXT.__dlopen_cstrs: 0x10a
   __TEXT.__swift5_typeref: 0x43dc

   __TEXT.__swift_as_entry: 0x94
   __TEXT.__swift_as_ret: 0x88
   __TEXT.__swift_as_cont: 0x234
-  __TEXT.__unwind_info: 0x3ce8
+  __TEXT.__unwind_info: 0x3d20
   __TEXT.__eh_frame: 0x2030
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x26f8
+  __DATA_CONST.__const: 0x2748
   __DATA_CONST.__objc_classlist: 0x7a0
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x210
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6de8
+  __DATA_CONST.__objc_selrefs: 0x6f68
   __DATA_CONST.__objc_protorefs: 0x80
   __DATA_CONST.__objc_superrefs: 0x608
-  __DATA_CONST.__objc_arraydata: 0x2e0
-  __DATA_CONST.__got: 0x1438
+  __DATA_CONST.__objc_arraydata: 0x318
+  __DATA_CONST.__got: 0x1498
   __AUTH_CONST.__const: 0x2f88
-  __AUTH_CONST.__cfstring: 0xb1c0
-  __AUTH_CONST.__objc_const: 0x25e48
-  __AUTH_CONST.__objc_intobj: 0x8d0
-  __AUTH_CONST.__objc_arrayobj: 0xf0
+  __AUTH_CONST.__cfstring: 0xb5c0
+  __AUTH_CONST.__objc_const: 0x25f50
+  __AUTH_CONST.__objc_intobj: 0x918
+  __AUTH_CONST.__objc_arrayobj: 0x138
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0x258
   __AUTH_CONST.__auth_got: 0x1848
   __AUTH.__objc_data: 0x5170
   __AUTH.__data: 0xa38
-  __DATA.__objc_ivar: 0xd00
+  __DATA.__objc_ivar: 0xd14
   __DATA.__data: 0x2838
   __DATA.__bss: 0x1e40
   __DATA.__common: 0xc0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 6231
-  Symbols:   16961
-  CStrings:  3559
+  Functions: 6272
+  Symbols:   17077
+  CStrings:  3630
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift_as_ret : content changed
~ __TEXT.__swift_as_cont : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__objc_doubleobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH.__objc_data : content changed
~ __AUTH.__data : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
Symbols:
+ -[STContentPrivacyMediaRestrictionsDetailController setWebContentSpecifier:]
+ -[STContentPrivacyMediaRestrictionsDetailController webContentSpecifier]
+ -[STContentPrivacySiriAndIntelligenceRestrictionsDetailController _capabilityIconWithSymbolName:backgroundColor:]
+ -[STContentPrivacySiriAndIntelligenceRestrictionsDetailController _getRealisticImageGenerationLinkListSpecifierValue:]
+ -[STContentPrivacySiriAndIntelligenceRestrictionsDetailController _getSensitiveTopicsLinkListSpecifierValue:]
+ -[STContentPrivacySiriAndIntelligenceRestrictionsDetailController _getSiriPickerSpecifierValue:]
+ -[STContentPrivacySiriAndIntelligenceRestrictionsDetailController _realisticImageGenerationSpecifier]
+ -[STContentPrivacySiriAndIntelligenceRestrictionsDetailController _sensitiveTopicsSpecifier]
+ -[STContentPrivacySiriAndIntelligenceRestrictionsDetailController _setRealisticImageGenerationLinkListSpecifierValue:specifier:]
+ -[STContentPrivacySiriAndIntelligenceRestrictionsDetailController _setSensitiveTopicsLinkListSpecifierValue:specifier:]
+ -[STContentPrivacySiriAndIntelligenceRestrictionsDetailController _setSiriPickerSpecifierValue:specifier:]
+ -[STContentPrivacySiriAndIntelligenceRestrictionsDetailController _siriPickerSpecifier]
+ -[STContentPrivacyViewModel isRealisticImageGenerationAllowed]
+ -[STContentPrivacyViewModel isSensitiveTopicsAllowed]
+ -[STContentPrivacyViewModel isSiriAIAllowed]
+ -[STContentPrivacyViewModel regulatoryIntelligenceSiriPolicy]
+ -[STContentPrivacyViewModel setIsRealisticImageGenerationAllowed:]
+ -[STContentPrivacyViewModel setIsSensitiveTopicsAllowed:]
+ -[STContentPrivacyViewModel setIsSiriAIAllowed:]
+ -[STContentPrivacyViewModel setRegulatoryIntelligenceSiriPolicy:]
+ -[STContentPrivacyViewModelCoordinator saveRealisticImageGenerationIsAllowed:error:]
+ -[STContentPrivacyViewModelCoordinator saveSensitiveTopicsIsAllowed:error:]
+ -[STContentPrivacyViewModelCoordinator saveSiriAIIsAllowed:error:]
+ GCC_except_table119
+ GCC_except_table18
+ GCC_except_table204
+ GCC_except_table213
+ _OBJC_CLASS_$_UIGraphicsImageRendererFormat
+ _OBJC_IVAR_$_STContentPrivacyMediaRestrictionsDetailController._webContentSpecifier
+ _OBJC_IVAR_$_STContentPrivacyViewModel._isRealisticImageGenerationAllowed
+ _OBJC_IVAR_$_STContentPrivacyViewModel._isSensitiveTopicsAllowed
+ _OBJC_IVAR_$_STContentPrivacyViewModel._isSiriAIAllowed
+ _OBJC_IVAR_$_STContentPrivacyViewModel._regulatoryIntelligenceSiriPolicy
+ ___106-[STContentPrivacySiriAndIntelligenceRestrictionsDetailController _setSiriPickerSpecifierValue:specifier:]_block_invoke
+ ___113-[STContentPrivacySiriAndIntelligenceRestrictionsDetailController _capabilityIconWithSymbolName:backgroundColor:]_block_invoke
+ ___159-[STContentPrivacyViewModelCoordinator initWithPersistenceController:userDSID:userName:currentAccountIsProto:regulatoryUIPolicyProvider:loadCompletionHandler:]_block_invoke
+ ___67-[STContentPrivacyMediaRestrictionsDetailController viewDidAppear:]_block_invoke_2
+ ___69-[STRootViewModelCoordinator loadRegionRatingsWithCompletionHandler:]_block_invoke_2
+ ___block_descriptor_133_e8_32s40s48s56s64s72s80s88s96s104s112bs_e20_v20?0B8"NSError"12ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8s104l8s112l8
+ ___block_descriptor_145_e8_32s40s48s56s64s72s80s88s96s104s112s120bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8s104l8s120l8s112l8
+ ___block_descriptor_40_e8_32s_e41_"STRegulatoryIntelligenceSiriPolicy"8?0ls32l8
+ ___block_descriptor_48_e8_32s40s_e40_v16?0"UIGraphicsImageRendererContext"8ls32l8s40l8
+ _objc_msgSend$_capabilityIconWithSymbolName:backgroundColor:
+ _objc_msgSend$_realisticImageGenerationSpecifier
+ _objc_msgSend$_sensitiveTopicsSpecifier
+ _objc_msgSend$_siriPickerSpecifier
+ _objc_msgSend$_systemImageNamed:
+ _objc_msgSend$bezierPathWithRoundedRect:cornerRadius:
+ _objc_msgSend$configurationWithPointSize:weight:
+ _objc_msgSend$drawInRect:
+ _objc_msgSend$extensionsEditable
+ _objc_msgSend$extensionsFooter
+ _objc_msgSend$fetchRestrictionsForUserDSID:persistenceController:organizationSettingsRestrictionUtility:completionHandler:
+ _objc_msgSend$fill
+ _objc_msgSend$imageWithTintColor:renderingMode:
+ _objc_msgSend$initWithBool:
+ _objc_msgSend$initWithPersistenceController:restrictionPayloadUtility:regulatoryIntelligenceSiriPolicyProvider:
+ _objc_msgSend$initWithSize:format:
+ _objc_msgSend$intelligenceSiri
+ _objc_msgSend$isInFamily
+ _objc_msgSend$isRealisticImageGenerationAllowed
+ _objc_msgSend$isRealisticImageGenerationAllowedForUserDSID:error:
+ _objc_msgSend$isSensitiveTopicsAllowed
+ _objc_msgSend$isSensitiveTopicsAllowedForUserDSID:error:
+ _objc_msgSend$isSiriAIAllowed
+ _objc_msgSend$isSiriAIAllowedForUserDSID:error:
+ _objc_msgSend$preferredFormat
+ _objc_msgSend$realisticImagesEditable
+ _objc_msgSend$realisticImagesFooter
+ _objc_msgSend$regulatoryIntelligenceSiriPolicy
+ _objc_msgSend$saveRealisticImageGenerationIsAllowed:error:
+ _objc_msgSend$saveSensitiveTopicsIsAllowed:error:
+ _objc_msgSend$saveSiriAIIsAllowed:error:
+ _objc_msgSend$setFill
+ _objc_msgSend$setIsRealisticImageGenerationAllowed:
+ _objc_msgSend$setIsSensitiveTopicsAllowed:
+ _objc_msgSend$setIsSiriAIAllowed:
+ _objc_msgSend$setOpaque:
+ _objc_msgSend$setRealisticImageGenerationAllowed:forUserDSID:error:
+ _objc_msgSend$setRegulatoryIntelligenceSiriPolicy:
+ _objc_msgSend$setSensitiveTopicsAllowed:forUserDSID:error:
+ _objc_msgSend$setSiriAIAllowed:forUserDSID:error:
+ _objc_msgSend$setWebContentSpecifier:
+ _objc_msgSend$showWebFilterRestrictions:
+ _objc_msgSend$siriAIEditable
+ _objc_msgSend$siriAIFooter
+ _objc_msgSend$webContentSpecifier
- GCC_except_table110
- GCC_except_table203
- GCC_except_table212
- ___block_descriptor_125_e8_32s40s48s56s64s72s80s88s96s104bs_e20_v20?0B8"NSError"12ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8s104l8
- ___block_descriptor_134_e8_32s40s48s56s64s72s80s88s96s104s112bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8s112l8s104l8
- _objc_msgSend$_defaultSwitchSpecifierWithConfiguration:key:fallbackLabel:
- _objc_msgSend$fetchRestrictionsForUserDSID:persistenceController:completionHandler:
- _objc_msgSend$initWithPersistenceController:restrictionPayloadUtility:
- _objc_msgSend$setSupportedInterfaceOrientations:
- _objc_retain_x7
CStrings:
+ "@\"STRegulatoryIntelligenceSiriPolicy\"8@?0"
+ "AllowedSiriVersionFooterText"
+ "AllowedSiriVersionFooterText_ChildRestricted"
+ "AllowedSiriVersionLabel"
+ "CONTENT_RESTRICTIONS/WEB_CONTENT"
+ "CapabilitiesLabel"
+ "DictationSpecifierName"
+ "ExplicitLanguageFooterText"
+ "Failed to fetch Realistic Image Generation restriction: %{public}@. Assuming Don't Allow."
+ "Failed to fetch Sensitive Topics restriction: %{public}@. Assuming Reduce."
+ "Failed to fetch Siri AI restriction: %{public}@. Assuming Don't Allow."
+ "Failed to save Realistic Image Generation restriction: %{public}@"
+ "Failed to save Sensitive Topics restriction: %{public}@"
+ "Failed to save Siri AI restriction: %{public}@"
+ "ImageCreationFooterText"
+ "ImageCreationFooterTextWithRealisticImages"
+ "ImageCreationFooterTextWithRealisticImages_ChildRestricted"
+ "IntelligenceExtensionsFooterText_ChildRestricted"
+ "MathAssistanceFooterText"
+ "MathAssistanceSpecifierName"
+ "RealisticImageGenerationSpecifierName"
+ "ReduceLabel"
+ "SensitiveTopicsFooterText"
+ "SensitiveTopicsSpecifierName"
+ "SiriAIOptionLabel"
+ "SiriClassicOptionLabel"
+ "SiriSpecifierName"
+ "WEB_CONTENT"
+ "WebContentAndKnowledgeFooterText"
+ "WebContentAndKnowledgeSpecifierName"
+ "WritingAssistanceFooterText"
+ "WritingAssistanceSpecifierName"
+ "com.apple.graphic-icon.microphone"
+ "exclamationmark.bubble.fill"
+ "exclamationmark.shield.fill"
+ "globe"
+ "math.operators"
+ "person.crop.artframe"
+ "photo.artframe"
+ "puzzlepiece.extension"
+ "summary.writing.tools.page"
- "AppleIntelligenceLabel"
- "IntelligenceExtensionsDetailFooterText"

```
