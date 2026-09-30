## SocialLayer

> `/System/iOSSupport/System/Library/PrivateFrameworks/SocialLayer.framework/Versions/A/SocialLayer`

```diff

-175.300.101.0.0
-  __TEXT.__text: 0xa58d0
-  __TEXT.__auth_stubs: 0x2130
-  __TEXT.__objc_methlist: 0x53fc
+175.500.141.0.0
+  __TEXT.__text: 0xa4ad8
+  __TEXT.__auth_stubs: 0x20e0
+  __TEXT.__objc_methlist: 0x5d2c
   __TEXT.__const: 0x1e94
   __TEXT.__gcc_except_tab: 0x1434
-  __TEXT.__cstring: 0x608d
+  __TEXT.__cstring: 0x5d5d
   __TEXT.__oslogstring: 0xc734
   __TEXT.__dlopen_cstrs: 0x2b3
-  __TEXT.__swift5_typeref: 0xc84
+  __TEXT.__swift5_typeref: 0xc96
   __TEXT.__constg_swiftt: 0xec4
   __TEXT.__swift5_reflstr: 0x5a3
   __TEXT.__swift5_fieldmd: 0x9b8

   __TEXT.__swift5_types: 0xec
   __TEXT.__swift5_protos: 0x1c
   __TEXT.__swift5_capture: 0x468
-  __TEXT.__unwind_info: 0x2b00
-  __TEXT.__eh_frame: 0x11a8
+  __TEXT.__swift_as_entry: 0x48
+  __TEXT.__swift_as_ret: 0x4c
+  __TEXT.__unwind_info: 0x2b20
+  __TEXT.__eh_frame: 0x1240
   __TEXT.__objc_classname: 0xe4a
   __TEXT.__objc_methname: 0xeeb2
   __TEXT.__objc_methtype: 0x25f6
   __TEXT.__objc_stubs: 0xa7a0
   __DATA_CONST.__got: 0xcc8
-  __DATA_CONST.__const: 0x1b90
+  __DATA_CONST.__const: 0x1c00
   __DATA_CONST.__objc_classlist: 0x360
   __DATA_CONST.__objc_nlclslist: 0x8
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x140
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x32b8
+  __DATA_CONST.__objc_selrefs: 0x3468
   __DATA_CONST.__objc_protorefs: 0x98
   __DATA_CONST.__objc_superrefs: 0x250
   __DATA_CONST.__objc_arraydata: 0x38
-  __AUTH_CONST.__auth_got: 0x10a8
-  __AUTH_CONST.__const: 0x2ac0
+  __AUTH_CONST.__auth_got: 0x1080
+  __AUTH_CONST.__const: 0x2ae8
   __AUTH_CONST.__cfstring: 0x2e20
-  __AUTH_CONST.__objc_const: 0xb680
+  __AUTH_CONST.__objc_const: 0xa680
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH.__objc_data: 0x2850
+  __AUTH.__objc_data: 0x2830
   __AUTH.__data: 0x4f0
   __DATA.__objc_ivar: 0x5a4
-  __DATA.__data: 0x14c8
+  __DATA.__data: 0x14b8
   __DATA.__bss: 0x1d50
-  __DATA.__common: 0x100
+  __DATA.__common: 0xf0
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/CloudKit.framework/Versions/A/CloudKit
   - /System/Library/Frameworks/Contacts.framework/Versions/A/Contacts

   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftIOKit.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 6E93382A-EEAE-3F84-AF70-C6E6B44CC9EB
-  Functions: 4193
-  Symbols:   10066
-  CStrings:  4458
+  UUID: BB5A8A7F-D638-3EFA-91A3-D5FA103BFECA
+  Functions: 4226
+  Symbols:   10109
+  CStrings:  4441
 
Symbols:
+ +[SLConversationExtensionHostContext _extensionAuxiliaryHostProtocol].cold.1
+ +[SLConversationExtensionHostContext _extensionAuxiliaryVendorProtocol].cold.1
+ +[SLDActiveCallService sharedService].cold.1
+ +[SLDCloudDocsService sharedService].cold.1
+ +[SLDCloudKitSyncReader sharedInstance].cold.1
+ +[SLDCloudKitSyncWriter sharedInstance].cold.1
+ +[SLDCollaborationAttributionViewService sharedService].cold.1
+ +[SLDCollaborationFooterService sharedService].cold.1
+ +[SLDCollaborationHandshakeService sharedService].cold.1
+ +[SLDCollaborationNoticeService sharedService].cold.1
+ +[SLDCollaborationSigningService sharedService].cold.1
+ +[SLDFaceTimeService sharedService].cold.1
+ +[SLDPillService sharedService].cold.1
+ +[SLDServiceCenter sharedCenter].cold.1
+ +[SLDShareableContentService sharedService].cold.1
+ +[SLDSyndicationService sharedService].cold.1
+ +[SLHighlightCenter highlightCenterQueue].cold.1
+ +[SLHighlightCenter rapportClient].cold.1
+ +[SLHighlightsCache highlightFetchQueue].cold.1
+ +[SLHighlightsCache highlightQueryHandlerQueue].cold.1
+ +[SLHighlightsCache userInitiatedHighlightFetchQueue].cold.1
+ +[SLPerson fetchMeContact].cold.1
+ +[SLPerson keysForCNContact].cold.1
+ +[SLSyndicationController sharedController].cold.1
+ +[SLSyndicationController syndicationProcessingQueue].cold.1
+ -[SLDCloudKitSyncReader _syncDirectory].cold.1
+ -[SLShareableContentLoadResult archivedObjectClass].cold.1
+ CoreGlyphsCatalog.cold.1
+ GCC_except_table123
+ GCC_except_table150
+ GCC_except_table153
+ SLDAllowedServiceClasses.cold.1
+ SLDAssetCatalog.cold.1
+ SLDCUINamedImageDeviceClass.cold.1
+ SLDClientGlobalWorkloop.cold.1
+ SLDCreateColorNamed.cold.1
+ SLDGlobalWorkloop.cold.1
+ SLDSystemVectorGlyph.cold.1
+ SLDSystemVectorGlyph.cold.2
+ SLDaemonLogHandle.cold.1
+ SLFrameworkBundle.cold.1
+ SLFrameworkLogHandle.cold.1
+ SLGeneralTelemetryLogHandle.cold.1
+ SLIsRunningInDaemon.cold.1
+ SLIsRunningInGelatoTester.cold.1
+ SLIsRunningInSLTester.cold.1
+ SLMakeAppKitBridge.cold.1
+ SLShareableContentLogHandle.cold.1
+ _$s10Foundation4DataV15_RepresentationO15withUnsafeBytesyxxSWKXEKlFSb_Tgq5015$s10Foundation4B26V2eeoiySbAC_ACtFZSbSWXEfU_ACTf1cn_n
+ _$s10Foundation4DataV15_RepresentationO15withUnsafeBytesyxxSWKXEKlFyt_Tg5063$s9CryptoKit12HashFunctionPAAE6update4datayqd___t10Foundation12B70ProtocolRd__lFy7Regions_7ElementQYd__XEfU_ySWXEfU_AA6SHA256V_AF0H0VTg50H3Kit0X0VTf1ncn_n
+ _$s10Foundation4DataVyACxcSTRzs5UInt8V7ElementRtzlufCAC_Tt0g5Tf4g_n
+ _$s10Foundation4DataVyACxcSTRzs5UInt8V7ElementRtzlufCSS8UTF8ViewV_Tt0g5
+ _$s10Foundation4DataVyACxcSTRzs5UInt8V7ElementRtzlufCSayAEG_Tt0g5Tf4g_n
+ _$s10Foundation4DataVyACxcSTRzs5UInt8V7ElementRtzlufcAC15_RepresentationOSRyAEGXEfU0_
+ _$s11SocialLayer23PersonIdentityGeneratorC22SLIDSServiceNameGelatoSSvpZMV
+ _$s11SocialLayer32HighlightPillSenderNameAttributeO4nameSSvpZMV
+ _$s11SocialLayer33HighlightPillListOfNamesAttributeO4nameSSvpZMV
+ _$s11SocialLayer33HighlightPillNumContactsAttributeO4nameSSvpZMV
+ _$s11SocialLayer3LogV13keyController2os6LoggerVvpZMV
+ _$s11SocialLayer3LogV13keyController_WZTm
+ _$s11SocialLayer3LogV15ProcessVerifier2os6LoggerVvpZMV
+ _$s11SocialLayer3LogV21collaborationRenderer2os6LoggerVvpZMV
+ _$s11SocialLayer3LogV23personIdentityGenerator2os6LoggerVvpZMV
+ _$s11SocialLayer3LogV7default2os6LoggerVvpZMV
+ _$s11SocialLayer43CollaborationAttributionViewMetricsProviderC15singleLineTitle3for7metricsSo9CTLineRefaSgSS_xtAA0cdeF9ProvidingRzlFZAA0cde12ConversationF033_7A1E2A6E1127C7C0B9C39195EE6C007BLLV_Tt1g5
+ _$s9CryptoKit12SHA256DigestVAcA0D0AAWlTm
+ _$s9CryptoKit3AESO3GCMO9SealedBoxV8combinedAGx_tKc10Foundation12DataProtocolRzlufCAI0I0V_Tt1g5
+ _$s9CryptoKit4P256O7SigningO9PublicKeyV3key_10Foundation4DataV3tpstWOc
+ _$s9CryptoKit4P256O7SigningO9PublicKeyV3key_10Foundation4DataV3tpstWOcTm
+ _$s9CryptoKit4P256O7SigningO9PublicKeyVSgWOhTm
+ _$sSD17dictionaryLiteralSDyxq_Gx_q_td_tcfCSS_So16SWPersonIdentityCTt0g5
+ _$sSD17dictionaryLiteralSDyxq_Gx_q_td_tcfCSS_ypTt0g5
+ _$sSD17dictionaryLiteralSDyxq_Gx_q_td_tcfCSo11CFStringRefaSg_ADTt0g5
+ _$sSD17dictionaryLiteralSDyxq_Gx_q_td_tcfCSo11CFStringRefaSg_ypTt0g5
+ _$sSD17dictionaryLiteralSDyxq_Gx_q_td_tcfCSo11CFStringRefa_12CoreGraphics7CGFloatVTt0g5
+ _$sSD17dictionaryLiteralSDyxq_Gx_q_td_tcfCSo11CFStringRefa_SDyAD12CoreGraphics7CGFloatVGTt0g5
+ _$sSD17dictionaryLiteralSDyxq_Gx_q_td_tcfCSo11CFStringRefa_SDyADSgADGTt0g5
+ _$sSD17dictionaryLiteralSDyxq_Gx_q_td_tcfCSo11CFStringRefa_SDyADSgypGTt0g5
+ _$sSD17dictionaryLiteralSDyxq_Gx_q_td_tcfCSo11CFStringRefa_SDyADSgypGTt0g5Tm
+ _$sSD17dictionaryLiteralSDyxq_Gx_q_td_tcfCSo11CFStringRefa_SDyADSiGTt0g5
+ _$sSD17dictionaryLiteralSDyxq_Gx_q_td_tcfCSo11CFStringRefa_SDyADypGTt0g5
+ _$sSD17dictionaryLiteralSDyxq_Gx_q_td_tcfCSo11CFStringRefa_SiTt0g5
+ _$sSD17dictionaryLiteralSDyxq_Gx_q_td_tcfCSo11CFStringRefa_ypTt0g5
+ _$sSD17dictionaryLiteralSDyxq_Gx_q_td_tcfCSo21NSAttributedStringKeya_ypTt0g5
+ _$sScTss5NeverORs_rlE8priority9operationScTyxABGScPSg_xyYaYAcntcfCyt_Tt1gq5
+ _$sSccy10Foundation4DataVs5Error_pGMD
+ _$sSo8NSObjectCSgWOh
+ _$sSo8NSObjectCSgWOhTm
+ _$sSw17withMemoryRebound2to_q0_xm_q0_SryxGq_YKXEtq_YKs5ErrorR_Ri_zRi_0_r1_lFs5UInt8V_s5NeverOs16IndexingIteratorVySS8UTF8ViewVG_SitTt1g5
+ _$ss22_ContiguousArrayBufferV19_uninitializedCount15minimumCapacityAByxGSi_SitcfCs5UInt8V_Tt1gq5
+ __113+[SLCoreSpotlightUtilities fetchCSSearchableItemForUniqueIdentifier:forContentType:withRequiredAttributes:error:]_block_invoke.25
+ __113+[SLCoreSpotlightUtilities fetchCSSearchableItemForUniqueIdentifier:forContentType:withRequiredAttributes:error:]_block_invoke.25.cold.1
+ __43-[SLHighlightCenter _registerNotifications]_block_invoke.141
+ __43-[SLHighlightsCache _registerNotifications]_block_invoke.37
+ __43-[SLHighlightsCache _registerNotifications]_block_invoke.39
+ __50-[SLHighlightsCache runAfterInitialFetch:onQueue:]_block_invoke.28
+ __50-[SLHighlightsCache runAfterInitialFetch:onQueue:]_block_invoke.30
+ __55-[SLDCloudKitSyncWriter fetchAndProcessFreshHighlights]_block_invoke.433
+ __55-[SLDCloudKitSyncWriter fetchAndProcessFreshHighlights]_block_invoke.496
+ __55-[SLDCloudKitSyncWriter fetchAndProcessFreshHighlights]_block_invoke.528
+ __55-[SLDCloudKitSyncWriter fetchAndProcessFreshHighlights]_block_invoke_2.435
+ __55-[SLDCloudKitSyncWriter fetchAndProcessFreshHighlights]_block_invoke_3.483
+ __55-[SLDCloudKitSyncWriter fetchAndProcessFreshHighlights]_block_invoke_3.483.cold.1
+ __61-[SLDCloudKitSyncWriter syncEngine:failedToSaveRecord:error:]_block_invoke.563
+ __63-[SLDCloudKitSyncBase checkForAccountChangesNowWithCompletion:]_block_invoke.220
+ __63-[SLDCloudKitSyncBase fetchContainerInformationWithCompletion:]_block_invoke.217
+ __63-[SLDCloudKitSyncBase fetchContainerInformationWithCompletion:]_block_invoke.217.cold.1
+ __65-[SLDCloudKitSyncWriter syncEngine:failedToSaveRecordZone:error:]_block_invoke.562
+ __69-[SLDCloudKitSyncWriter syncEngine:failedToDeleteRecordWithID:error:]_block_invoke.564
+ __Block_byref_object_copy_.46
+ __Block_byref_object_dispose_.47
+ __CoreGlyphsCatalog_block_invoke.cold.1
+ __SLDCoreGlyphsBundle_block_invoke.cold.1
+ ___swift_async_entry_functlets
+ ___swift_async_ret_functlets
+ ___swift_destroy_boxed_opaque_existential_1Tm
+ ___swift_project_boxed_opaque_existential_1Tm
+ __block_literal_global.126
+ __block_literal_global.17
+ __block_literal_global.20
+ __block_literal_global.51
+ __block_literal_global.56
+ __block_literal_global.605
+ __block_literal_global.61
+ __block_literal_global.65
+ __block_literal_global.687
+ _symbolic Sccy___________pG 10Foundation4DataV s5ErrorP
+ block_copy_helper.23
+ block_copy_helper.29
+ block_descriptor.25
+ block_descriptor.31
+ block_destroy_helper.24
+ block_destroy_helper.30
+ sharedInstance.onceToken.602
+ sharedInstance.sharedInstance.603
- GCC_except_table122
- GCC_except_table149
- GCC_except_table152
- _$s10Foundation4DataV06InlineB0V15withUnsafeBytesyxxSWKXEKlFSb_Tgq5015$s10Foundation4B26V2eeoiySbAC_ACtFZSbSWXEfU_ACTf1cn_nTf4ng_n
- _$s10Foundation4DataV15_RepresentationOyAESWcfCTf4nd_n
- _$s10Foundation4DataVyACxcSTRzs5UInt8V7ElementRtzlufCAC_Tgm5
- _$s10Foundation4DataVyACxcSTRzs5UInt8V7ElementRtzlufCSS8UTF8ViewV_Tgm5
- _$s10Foundation4DataVyACxcSTRzs5UInt8V7ElementRtzlufCSayAEG_Tgm5Tf4g_n
- _$s11SocialLayer19KeychainAccessGroup_WZ
- _$s11SocialLayer19KeychainAccessGroup_Wz
- _$s11SocialLayer23SLDHighlightPillMetrics33_00C2B47D0280335DFFDBB3BC8927527ALLVSgMD
- _$s11SocialLayer23SLDHighlightPillMetrics33_00C2B47D0280335DFFDBB3BC8927527ALLVSgWOb
- _$s11SocialLayer36SLHighlightDisambiguationPillMetrics33_C5DA7C7764DCEDFB9B9BF94750149602LLVSgMD
- _$s11SocialLayer36SLHighlightDisambiguationPillMetrics33_C5DA7C7764DCEDFB9B9BF94750149602LLVSgWOb
- _$s11SocialLayer43CollaborationAttributionViewMetricsProviderC15singleLineTitle3for7metricsSo9CTLineRefaSgSS_xtAA0cdeF9ProvidingRzlFZAA0cde12ConversationF033_7A1E2A6E1127C7C0B9C39195EE6C007BLLV_Tgm5
- _$s11SocialLayer43CollaborationAttributionViewStandardMetrics33_7A1E2A6E1127C7C0B9C39195EE6C007BLLVAA06RemoteeG9ProvidingA2aEP11drawingSizeSo6CGSizeVyFTWTm
- _$s21DeveloperToolsSupport13ImageResourceV11SocialLayerE7preview_WZTm
- _$s9CryptoKit12SHA256DigestVSgWOhTm
- _$s9CryptoKit12SymmetricKeyVSgSgWOhTm
- _$s9CryptoKit3AESO3GCMO9SealedBoxV8combinedAGx_tKc10Foundation12DataProtocolRzlufCAI0I0V_Tgm5
- _$s9CryptoKit4P256O7SigningO9PublicKeyVSgWOc
- _$s9CryptoKit6SHA256VAcA12HashFunctionAAWlTm
- _$sSD17dictionaryLiteralSDyxq_Gx_q_td_tcfCSS_So16SWPersonIdentityCTgm5
- _$sSD17dictionaryLiteralSDyxq_Gx_q_td_tcfCSS_ypTgm5
- _$sSD17dictionaryLiteralSDyxq_Gx_q_td_tcfCSo11CFStringRefaSg_ADTgm5
- _$sSD17dictionaryLiteralSDyxq_Gx_q_td_tcfCSo11CFStringRefaSg_ypTgm5
- _$sSD17dictionaryLiteralSDyxq_Gx_q_td_tcfCSo11CFStringRefa_12CoreGraphics7CGFloatVTgm5
- _$sSD17dictionaryLiteralSDyxq_Gx_q_td_tcfCSo11CFStringRefa_SDyAD12CoreGraphics7CGFloatVGTgm5
- _$sSD17dictionaryLiteralSDyxq_Gx_q_td_tcfCSo11CFStringRefa_SDyADSgADGTgm5
- _$sSD17dictionaryLiteralSDyxq_Gx_q_td_tcfCSo11CFStringRefa_SDyADSgypGTgm5
- _$sSD17dictionaryLiteralSDyxq_Gx_q_td_tcfCSo11CFStringRefa_SDyADSgypGTgm5Tm
- _$sSD17dictionaryLiteralSDyxq_Gx_q_td_tcfCSo11CFStringRefa_SDyADSiGTgm5
- _$sSD17dictionaryLiteralSDyxq_Gx_q_td_tcfCSo11CFStringRefa_SDyADypGTgm5
- _$sSD17dictionaryLiteralSDyxq_Gx_q_td_tcfCSo11CFStringRefa_SiTgm5
- _$sSD17dictionaryLiteralSDyxq_Gx_q_td_tcfCSo11CFStringRefa_ypTgm5
- _$sSD17dictionaryLiteralSDyxq_Gx_q_td_tcfCSo21NSAttributedStringKeya_ypTgm5
- _$sSa12_endMutationyyFyXl_Ts5
- _$sScTss5NeverORs_rlE8priority9operationScTyxABGScPSg_xyYaYAcntcfCyt_Tgmq5
- _$sSw10copyMemory4fromySW_tF
- _$sSw17withMemoryRebound2to_q0_xm_q0_SryxGq_YKXEtq_YKs5ErrorR_Ri_zRi_0_r1_lFs5UInt8V_s5NeverOs16IndexingIteratorVySS8UTF8ViewVG_SitTgm5
- _$sSwys5UInt8VSicis
- _$ss12_ArrayBufferV13_copyContents8subRange12initializingSpyxGSnySiG_AFtF10Foundation4DataV_Tg5Tf4nng_n
- _$ss12_ArrayBufferV13_copyContents8subRange12initializingSpyxGSnySiG_AFtF11SocialLayer8Endpoint_p_Tg5Tf4nng_n
- _$ss12_ArrayBufferV13_copyContents8subRange12initializingSpyxGSnySiG_AFtF9CryptoKit4P256O7SigningO9PublicKeyV_Tg5Tf4nng_nTm
- _$ss12_ArrayBufferV13_copyContents8subRange12initializingSpyxGSnySiG_AFtFSS_Tg5Tf4nng_n
- _$ss12_ArrayBufferV13_copyContents8subRange12initializingSpyxGSnySiG_AFtFSo8_NSRangeV_Tg5Tf4nng_n
- _$ss17_assertionFailure__4file4line5flagss5NeverOs12StaticStringV_A2HSus6UInt32VtF
- _$ss18_fatalErrorMessage__4file4line5flagss5NeverOs12StaticStringV_A2HSus6UInt32VtF
- _$ss22_ContiguousArrayBufferV19_uninitializedCount15minimumCapacityAByxGSi_SitcfCs5UInt8V_Tgmq5
- _OUTLINED_FUNCTION_18
- _OUTLINED_FUNCTION_19
- _OUTLINED_FUNCTION_20
- __113+[SLCoreSpotlightUtilities fetchCSSearchableItemForUniqueIdentifier:forContentType:withRequiredAttributes:error:]_block_invoke.19
- __113+[SLCoreSpotlightUtilities fetchCSSearchableItemForUniqueIdentifier:forContentType:withRequiredAttributes:error:]_block_invoke.19.cold.1
- __43-[SLHighlightCenter _registerNotifications]_block_invoke.135
- __43-[SLHighlightsCache _registerNotifications]_block_invoke.31
- __43-[SLHighlightsCache _registerNotifications]_block_invoke.33
- __50-[SLHighlightsCache runAfterInitialFetch:onQueue:]_block_invoke.22
- __50-[SLHighlightsCache runAfterInitialFetch:onQueue:]_block_invoke.24
- __55-[SLDCloudKitSyncWriter fetchAndProcessFreshHighlights]_block_invoke.427
- __55-[SLDCloudKitSyncWriter fetchAndProcessFreshHighlights]_block_invoke.490
- __55-[SLDCloudKitSyncWriter fetchAndProcessFreshHighlights]_block_invoke.522
- __55-[SLDCloudKitSyncWriter fetchAndProcessFreshHighlights]_block_invoke_2.429
- __55-[SLDCloudKitSyncWriter fetchAndProcessFreshHighlights]_block_invoke_3.477
- __55-[SLDCloudKitSyncWriter fetchAndProcessFreshHighlights]_block_invoke_3.477.cold.1
- __61-[SLDCloudKitSyncWriter syncEngine:failedToSaveRecord:error:]_block_invoke.557
- __63-[SLDCloudKitSyncBase checkForAccountChangesNowWithCompletion:]_block_invoke.214
- __63-[SLDCloudKitSyncBase fetchContainerInformationWithCompletion:]_block_invoke.211
- __63-[SLDCloudKitSyncBase fetchContainerInformationWithCompletion:]_block_invoke.211.cold.1
- __65-[SLDCloudKitSyncWriter syncEngine:failedToSaveRecordZone:error:]_block_invoke.556
- __69-[SLDCloudKitSyncWriter syncEngine:failedToDeleteRecordWithID:error:]_block_invoke.558
- __Block_byref_object_copy_.40
- __Block_byref_object_dispose_.41
- __block_literal_global.11
- __block_literal_global.120
- __block_literal_global.14
- __block_literal_global.45
- __block_literal_global.55
- __block_literal_global.59
- __block_literal_global.599
- __block_literal_global.681
- __swift_FORCE_LOAD_$_swiftFileProvider
- __swift_FORCE_LOAD_$_swiftFileProvider_$_SocialLayer
- block_copy_helper.27
- block_descriptor.29
- block_destroy_helper.28
- sharedInstance.onceToken.596
- sharedInstance.sharedInstance.597
CStrings:
- "Division by zero"
- "Division results in an overflow"
- "Insufficient space allocated to copy string contents"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/IntegerTypes.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.initialize with negative count"
- "UnsafeMutablePointer.moveInitialize with negative count"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "invalid Collection: less than 'count' elements in collection"

```
