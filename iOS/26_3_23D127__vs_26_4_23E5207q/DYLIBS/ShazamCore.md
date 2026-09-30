## ShazamCore

> `/System/Library/PrivateFrameworks/ShazamCore.framework/ShazamCore`

```diff

-426.1.3.0.0
-  __TEXT.__text: 0xc580
-  __TEXT.__auth_stubs: 0x7d0
-  __TEXT.__objc_methlist: 0x1090
-  __TEXT.__const: 0xf0
-  __TEXT.__cstring: 0xdbc
-  __TEXT.__oslogstring: 0x577
-  __TEXT.__gcc_except_tab: 0x108
-  __TEXT.__swift5_typeref: 0x60
+426.4.31.0.0
+  __TEXT.__text: 0x16ffc
+  __TEXT.__auth_stubs: 0xcd0
+  __TEXT.__objc_methlist: 0x146c
+  __TEXT.__const: 0x1454
+  __TEXT.__gcc_except_tab: 0x1e8
+  __TEXT.__oslogstring: 0x813
+  __TEXT.__cstring: 0x10d2
+  __TEXT.__swift5_typeref: 0x3b2
   __TEXT.__swift5_capture: 0x5c
   __TEXT.__swift_as_entry: 0x14
   __TEXT.__swift_as_ret: 0x14
-  __TEXT.__unwind_info: 0x490
-  __TEXT.__eh_frame: 0x280
-  __TEXT.__objc_classname: 0x235
-  __TEXT.__objc_methname: 0x2e83
-  __TEXT.__objc_methtype: 0x59e
-  __TEXT.__objc_stubs: 0x1e40
-  __DATA_CONST.__got: 0x1e0
-  __DATA_CONST.__const: 0x4d0
-  __DATA_CONST.__objc_classlist: 0xe8
+  __TEXT.__swift5_fieldmd: 0x334
+  __TEXT.__constg_swiftt: 0x310
+  __TEXT.__swift5_reflstr: 0xa8
+  __TEXT.__swift5_builtin: 0x14
+  __TEXT.__swift5_mpenum: 0x8
+  __TEXT.__swift5_protos: 0x4
+  __TEXT.__swift5_proto: 0x128
+  __TEXT.__swift5_types: 0x54
+  __TEXT.__unwind_info: 0x958
+  __TEXT.__eh_frame: 0x688
+  __TEXT.__objc_classname: 0x351
+  __TEXT.__objc_methname: 0x39e8
+  __TEXT.__objc_methtype: 0x76c
+  __TEXT.__objc_stubs: 0x2580
+  __DATA_CONST.__got: 0x2e8
+  __DATA_CONST.__const: 0x700
+  __DATA_CONST.__objc_classlist: 0x128
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x18
+  __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb40
-  __DATA_CONST.__objc_superrefs: 0xa8
-  __AUTH_CONST.__auth_got: 0x3f8
-  __AUTH_CONST.__const: 0x2a8
-  __AUTH_CONST.__cfstring: 0x10e0
-  __AUTH_CONST.__objc_const: 0x21b8
-  __AUTH.__objc_data: 0x750
+  __DATA_CONST.__objc_selrefs: 0xda0
+  __DATA_CONST.__objc_superrefs: 0xe0
+  __AUTH_CONST.__auth_got: 0x678
+  __AUTH_CONST.__const: 0xd88
+  __AUTH_CONST.__cfstring: 0x1260
+  __AUTH_CONST.__objc_const: 0x2bd0
+  __AUTH.__objc_data: 0x9d0
   __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0xf4
-  __DATA.__data: 0x140
+  __DATA.__objc_ivar: 0x144
+  __DATA.__data: 0x550
+  __DATA.__bss: 0x2500
+  __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0x1e0
   __DATA_DIRTY.__bss: 0x30
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
   - /System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
+  - /System/Library/PrivateFrameworks/FeatureFlags.framework/FeatureFlags
   - /System/Library/PrivateFrameworks/TCC.framework/TCC
   - /usr/lib/libAppleArchive.dylib
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: B4CC635C-8852-3F45-A5E6-866476C415C7
-  Functions: 384
-  Symbols:   1486
-  CStrings:  924
+  UUID: 5F0EE09C-C202-3057-8B84-CD303D2B8196
+  Functions: 783
+  Symbols:   2000
+  CStrings:  1111
 
Symbols:
+ +[SHEntitlements disableShazamLibraryCloudKitAccess]
+ +[SHNetworkDownloadUtilities cachedFileURLWithFilename:type:]
+ +[SHNetworkDownloadUtilities downloadDirectory]
+ +[SHNetworkDownloadUtilities renameDownloadedFile:withFilename:usingType:error:]
+ -[SHAMSEndpointRequester .cxx_destruct]
+ -[SHAMSEndpointRequester buildEncoderForSession:clientType:clientIdentifier:]
+ -[SHAMSEndpointRequester clientIdentifier]
+ -[SHAMSEndpointRequester clientType]
+ -[SHAMSEndpointRequester encoder]
+ -[SHAMSEndpointRequester handleResultData:forResponse:callback:error:]
+ -[SHAMSEndpointRequester initWithClientIdentifier:clientType:]
+ -[SHAMSEndpointRequester invalidate]
+ -[SHAMSEndpointRequester isTokenFailureError:]
+ -[SHAMSEndpointRequester performDownloadRequest:filename:fileType:reply:]
+ -[SHAMSEndpointRequester performRequest:withReply:]
+ -[SHAMSEndpointRequester sessionConfiguration]
+ -[SHAMSEndpointRequester session]
+ -[SHAMSEndpointRequester setClientIdentifier:]
+ -[SHAMSEndpointRequester setClientType:]
+ -[SHAMSEndpointRequester setSession:]
+ -[SHAMSPaginatedEndpointRequester .cxx_destruct]
+ -[SHAMSPaginatedEndpointRequester endpointRequester]
+ -[SHAMSPaginatedEndpointRequester initWithClientIdentifier:clientType:]
+ -[SHAMSPaginatedEndpointRequester invalidate]
+ -[SHAMSPaginatedEndpointRequester performRequests:completionHandler:]
+ -[SHAMSPaginatedEndpointRequester setEndpointRequester:]
+ -[SHAnnouncementsBagConfiguration .cxx_destruct]
+ -[SHAnnouncementsBagConfiguration configuration]
+ -[SHAnnouncementsBagConfiguration initWithConfiguration:languageCode:]
+ -[SHAnnouncementsBagConfiguration languageCode]
+ -[SHAnnouncementsBagConfiguration trackPageEndpoint]
+ -[SHAnnouncementsRequester .cxx_destruct]
+ -[SHAnnouncementsRequester endpointURLWithHost:path:languageCode:storefront:]
+ -[SHAnnouncementsRequester initWithRemoteConfiguration:]
+ -[SHAnnouncementsRequester initWithRemoteConfiguration:storefrontProvider:]
+ -[SHAnnouncementsRequester remoteConfiguration]
+ -[SHAnnouncementsRequester setStorefrontProvider:]
+ -[SHAnnouncementsRequester storefrontProvider]
+ -[SHAnnouncementsRequester trackPageEndpointWithCompletion:]
+ -[SHCampaignTokens campaignGroup]
+ -[SHCampaignTokens initWithConfiguration:defaultConfigurationValues:]
+ -[SHCampaignTokens providerToken]
+ -[SHNetworkDownloadResponse .cxx_destruct]
+ -[SHNetworkDownloadResponse downloadedFileLocation]
+ -[SHNetworkDownloadResponse error]
+ -[SHNetworkDownloadResponse initWithDownloadedFileLocation:urlResponse:error:]
+ -[SHNetworkDownloadResponse urlResponse]
+ -[SHNetworkResponse .cxx_destruct]
+ -[SHNetworkResponse data]
+ -[SHNetworkResponse error]
+ -[SHNetworkResponse initWithData:urlResponse:error:]
+ -[SHNetworkResponse urlResponse]
+ -[SHOffers campaignPreviewUpsellActionText]
+ -[SHOffers campaignPreviewUpsellSubtitle]
+ -[SHOffers campaignPreviewUpsellTitle]
+ -[SHOffers defaultPreviewUpsellActionText]
+ -[SHOffers defaultPreviewUpsellSubtitle]
+ -[SHOffers defaultPreviewUpsellTitle]
+ -[SHOffers previewUpsellActionForOfferNamed:bundleID:]
+ -[SHOffers previewUpsellSubtitleForOfferNamed:bundleID:]
+ -[SHOffers previewUpsellTitleForOfferNamed:bundleID:]
+ -[SHRematchBagConfiguration .cxx_destruct]
+ -[SHRematchBagConfiguration configuration]
+ -[SHRematchBagConfiguration initWithConfiguration:]
+ -[SHRematchBagConfiguration isEnabledForClientIdentifier:]
+ -[SHRemoteConfiguration announcementsBagConfigurationWithCompletion:]
+ -[SHRemoteConfiguration announcementsBagValue]
+ -[SHRemoteConfiguration rematchBagConfigurationValue]
+ -[SHRemoteConfiguration rematchBagConfigurationWithCompletion:]
+ -[SHRemoteConfiguration setAnnouncementsBagValue:]
+ -[SHRemoteConfiguration setRematchBagConfigurationValue:]
+ GCC_except_table19
+ GCC_except_table24
+ GCC_except_table29
+ GCC_except_table50
+ GCC_except_table7
+ _AMSErrorDomain
+ _NSSearchPathForDirectoriesInDomains
+ _NSTemporaryDirectory
+ _OBJC_CLASS_$_AMSMediaProtocolHandler
+ _OBJC_CLASS_$_AMSMediaRequestEncoder
+ _OBJC_CLASS_$_AMSMediaTokenService
+ _OBJC_CLASS_$_AMSURLSession
+ _OBJC_CLASS_$_NSMutableArray
+ _OBJC_CLASS_$_NSNull
+ _OBJC_CLASS_$_NSProcessInfo
+ _OBJC_CLASS_$_NSURLSessionConfiguration
+ _OBJC_CLASS_$_SHAMSEndpointRequester
+ _OBJC_CLASS_$_SHAMSPaginatedEndpointRequester
+ _OBJC_CLASS_$_SHAnnouncementsBagConfiguration
+ _OBJC_CLASS_$_SHAnnouncementsRequester
+ _OBJC_CLASS_$_SHNetworkDownloadResponse
+ _OBJC_CLASS_$_SHNetworkDownloadUtilities
+ _OBJC_CLASS_$_SHNetworkResponse
+ _OBJC_CLASS_$_SHRematchBagConfiguration
+ _OBJC_IVAR_$_SHAMSEndpointRequester._clientIdentifier
+ _OBJC_IVAR_$_SHAMSEndpointRequester._clientType
+ _OBJC_IVAR_$_SHAMSEndpointRequester._encoder
+ _OBJC_IVAR_$_SHAMSEndpointRequester._session
+ _OBJC_IVAR_$_SHAMSPaginatedEndpointRequester._endpointRequester
+ _OBJC_IVAR_$_SHAnnouncementsBagConfiguration._configuration
+ _OBJC_IVAR_$_SHAnnouncementsBagConfiguration._languageCode
+ _OBJC_IVAR_$_SHAnnouncementsRequester._remoteConfiguration
+ _OBJC_IVAR_$_SHAnnouncementsRequester._storefrontProvider
+ _OBJC_IVAR_$_SHCampaignTokens._campaignGroup
+ _OBJC_IVAR_$_SHCampaignTokens._providerToken
+ _OBJC_IVAR_$_SHNetworkDownloadResponse._downloadedFileLocation
+ _OBJC_IVAR_$_SHNetworkDownloadResponse._error
+ _OBJC_IVAR_$_SHNetworkDownloadResponse._urlResponse
+ _OBJC_IVAR_$_SHNetworkResponse._data
+ _OBJC_IVAR_$_SHNetworkResponse._error
+ _OBJC_IVAR_$_SHNetworkResponse._urlResponse
+ _OBJC_IVAR_$_SHRematchBagConfiguration._configuration
+ _OBJC_IVAR_$_SHRemoteConfiguration._announcementsBagValue
+ _OBJC_IVAR_$_SHRemoteConfiguration._rematchBagConfigurationValue
+ _OBJC_METACLASS_$_SHAMSEndpointRequester
+ _OBJC_METACLASS_$_SHAMSPaginatedEndpointRequester
+ _OBJC_METACLASS_$_SHAnnouncementsBagConfiguration
+ _OBJC_METACLASS_$_SHAnnouncementsRequester
+ _OBJC_METACLASS_$_SHNetworkDownloadResponse
+ _OBJC_METACLASS_$_SHNetworkDownloadUtilities
+ _OBJC_METACLASS_$_SHNetworkResponse
+ _OBJC_METACLASS_$_SHRematchBagConfiguration
+ _SHAnalyticsPayloadTypeKey
+ _TCCAccessSetForBundleId
+ __OBJC_$_CLASS_METHODS_SHEntitlements
+ __OBJC_$_CLASS_METHODS_SHNetworkDownloadUtilities
+ __OBJC_$_INSTANCE_METHODS_SHAMSEndpointRequester
+ __OBJC_$_INSTANCE_METHODS_SHAMSPaginatedEndpointRequester
+ __OBJC_$_INSTANCE_METHODS_SHAnnouncementsBagConfiguration
+ __OBJC_$_INSTANCE_METHODS_SHAnnouncementsRequester
+ __OBJC_$_INSTANCE_METHODS_SHNetworkDownloadResponse
+ __OBJC_$_INSTANCE_METHODS_SHNetworkResponse
+ __OBJC_$_INSTANCE_METHODS_SHRematchBagConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_SHAMSEndpointRequester
+ __OBJC_$_INSTANCE_VARIABLES_SHAMSPaginatedEndpointRequester
+ __OBJC_$_INSTANCE_VARIABLES_SHAnnouncementsBagConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_SHAnnouncementsRequester
+ __OBJC_$_INSTANCE_VARIABLES_SHNetworkDownloadResponse
+ __OBJC_$_INSTANCE_VARIABLES_SHNetworkResponse
+ __OBJC_$_INSTANCE_VARIABLES_SHRematchBagConfiguration
+ __OBJC_$_PROP_LIST_SHAMSEndpointRequester
+ __OBJC_$_PROP_LIST_SHAMSPaginatedEndpointRequester
+ __OBJC_$_PROP_LIST_SHAnnouncementsBagConfiguration
+ __OBJC_$_PROP_LIST_SHAnnouncementsRequester
+ __OBJC_$_PROP_LIST_SHNetworkDownloadResponse
+ __OBJC_$_PROP_LIST_SHNetworkResponse
+ __OBJC_$_PROP_LIST_SHRematchBagConfiguration
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SHNetworkPaginatedRequester
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SHNetworkRecognitionRequester
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SHNetworkPaginatedRequester
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SHNetworkRecognitionRequester
+ __OBJC_$_PROTOCOL_REFS_SHNetworkPaginatedRequester
+ __OBJC_$_PROTOCOL_REFS_SHNetworkRecognitionRequester
+ __OBJC_CLASS_PROTOCOLS_$_SHAMSEndpointRequester
+ __OBJC_CLASS_PROTOCOLS_$_SHAMSPaginatedEndpointRequester
+ __OBJC_CLASS_RO_$_SHAMSEndpointRequester
+ __OBJC_CLASS_RO_$_SHAMSPaginatedEndpointRequester
+ __OBJC_CLASS_RO_$_SHAnnouncementsBagConfiguration
+ __OBJC_CLASS_RO_$_SHAnnouncementsRequester
+ __OBJC_CLASS_RO_$_SHNetworkDownloadResponse
+ __OBJC_CLASS_RO_$_SHNetworkDownloadUtilities
+ __OBJC_CLASS_RO_$_SHNetworkResponse
+ __OBJC_CLASS_RO_$_SHRematchBagConfiguration
+ __OBJC_LABEL_PROTOCOL_$_SHNetworkPaginatedRequester
+ __OBJC_LABEL_PROTOCOL_$_SHNetworkRecognitionRequester
+ __OBJC_METACLASS_RO_$_SHAMSEndpointRequester
+ __OBJC_METACLASS_RO_$_SHAMSPaginatedEndpointRequester
+ __OBJC_METACLASS_RO_$_SHAnnouncementsBagConfiguration
+ __OBJC_METACLASS_RO_$_SHAnnouncementsRequester
+ __OBJC_METACLASS_RO_$_SHNetworkDownloadResponse
+ __OBJC_METACLASS_RO_$_SHNetworkDownloadUtilities
+ __OBJC_METACLASS_RO_$_SHNetworkResponse
+ __OBJC_METACLASS_RO_$_SHRematchBagConfiguration
+ __OBJC_PROTOCOL_$_SHNetworkPaginatedRequester
+ __OBJC_PROTOCOL_$_SHNetworkRecognitionRequester
+ ___51-[SHAMSEndpointRequester performRequest:withReply:]_block_invoke
+ ___51-[SHAMSEndpointRequester performRequest:withReply:]_block_invoke.5
+ ___52-[SHRemoteConfiguration populateRemoteConfiguration]_block_invoke_12
+ ___52-[SHRemoteConfiguration populateRemoteConfiguration]_block_invoke_13
+ ___53-[SHRemoteConfiguration campaignTokenWithCompletion:]_block_invoke.91
+ ___56-[SHAnnouncementsRequester initWithRemoteConfiguration:]_block_invoke
+ ___60-[SHAnnouncementsRequester trackPageEndpointWithCompletion:]_block_invoke
+ ___60-[SHAnnouncementsRequester trackPageEndpointWithCompletion:]_block_invoke_2
+ ___60-[SHAnnouncementsRequester trackPageEndpointWithCompletion:]_block_invoke_3
+ ___63-[SHRemoteConfiguration rematchBagConfigurationWithCompletion:]_block_invoke
+ ___69-[SHAMSPaginatedEndpointRequester performRequests:completionHandler:]_block_invoke
+ ___69-[SHAMSPaginatedEndpointRequester performRequests:completionHandler:]_block_invoke_2
+ ___69-[SHAMSPaginatedEndpointRequester performRequests:completionHandler:]_block_invoke_3
+ ___69-[SHRemoteConfiguration announcementsBagConfigurationWithCompletion:]_block_invoke
+ ___69-[SHRemoteConfiguration announcementsBagConfigurationWithCompletion:]_block_invoke.102
+ ___73-[SHAMSEndpointRequester performDownloadRequest:filename:fileType:reply:]_block_invoke
+ ___73-[SHAMSEndpointRequester performDownloadRequest:filename:fileType:reply:]_block_invoke.9
+ ___block_descriptor_32_e25_v16?0?<v?"NSString">8l
+ ___block_descriptor_40_e8_32w_e22_v16?0"NSDictionary"8lw32l8
+ ___block_descriptor_48_e8_32bs40w_e23_v28?08B16"NSError"20ls32l8w40l8
+ ___block_descriptor_48_e8_32bs40w_e28_v24?0"SHHost"8"NSError"16ls32l8w40l8
+ ___block_descriptor_48_e8_32bs40w_e34_v24?0"AMSURLResult"8"NSError"16lw40l8s32l8
+ ___block_descriptor_48_e8_32bs40w_e35_v24?0"AMSURLRequest"8"NSError"16ls32l8w40l8
+ ___block_descriptor_48_e8_32bs40w_e50_v24?0"SHDefaultConfigurationValues"8"NSError"16ls32l8w40l8
+ ___block_descriptor_48_e8_32s40bs_e5_v8?0ls40l8s32l8
+ ___block_descriptor_48_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_56_e8_32s40bs48w_e53_v24?0"SHAnnouncementsBagConfiguration"8"NSError"16ls40l8w48l8s32l8
+ ___block_descriptor_56_e8_32s40s48bs_e45_v32?0"NSURL"8"NSURLResponse"16"NSError"24ls48l8s32l8s40l8
+ ___block_descriptor_64_e8_32s40s48bs56w_e18_v16?0"NSString"8ls32l8w56l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48bs56w_e35_v24?0"AMSURLRequest"8"NSError"16ls48l8w56l8s32l8s40l8
+ ___block_descriptor_64_e8_32s40s48s56s_e27_v16?0"SHNetworkResponse"8ls32l8s40l8s48l8s56l8
+ ___block_literal_global.74
+ ___block_literal_global.76
+ ___block_literal_global.78
+ ___block_literal_global.80
+ ___block_literal_global.82
+ ___swift_allocate_value_buffer
+ ___swift_destroy_boxed_opaque_existential_1
+ ___swift_destroy_boxed_opaque_existential_1Tm
+ ___swift_instantiateConcreteTypeFromMangledNameAbstractV2
+ ___swift_memcpy0_1
+ ___swift_memcpy16_8
+ ___swift_memcpy17_8
+ ___swift_memcpy1_1
+ ___swift_memcpy48_8
+ ___swift_noop_void_return
+ ___swift_project_boxed_opaque_existential_1Tm
+ ___swift_project_value_buffer
+ __swiftEmptyArrayStorage
+ __swiftImmortalRefCount
+ __swift_stdlib_bridgeErrorToNSError
+ __swift_stdlib_malloc_size
+ _associated conformance 10ShazamCore12FeatureFlagsOSHAASQ
+ _associated conformance 10ShazamCore21AnnouncementsResponseV0cD5ErrorO10Foundation09LocalizedE0AAs0E0
+ _associated conformance 10ShazamCore21AnnouncementsResponseV10CodingKeys33_24416F8B5A8CBE27877FFEFDBAE95ECFLLOSHAASQ
+ _associated conformance 10ShazamCore21AnnouncementsResponseV10CodingKeys33_24416F8B5A8CBE27877FFEFDBAE95ECFLLOs0E3KeyAAs23CustomStringConvertible
+ _associated conformance 10ShazamCore21AnnouncementsResponseV10CodingKeys33_24416F8B5A8CBE27877FFEFDBAE95ECFLLOs0E3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 10ShazamCore21AnnouncementsResponseV16ResultsContainerV10CodingKeys33_24416F8B5A8CBE27877FFEFDBAE95ECFLLOSHAASQ
+ _associated conformance 10ShazamCore21AnnouncementsResponseV16ResultsContainerV10CodingKeys33_24416F8B5A8CBE27877FFEFDBAE95ECFLLOs0G3KeyAAs23CustomStringConvertible
+ _associated conformance 10ShazamCore21AnnouncementsResponseV16ResultsContainerV10CodingKeys33_24416F8B5A8CBE27877FFEFDBAE95ECFLLOs0G3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 10ShazamCore21AnnouncementsResponseV17ResourceReferenceV10CodingKeys33_24416F8B5A8CBE27877FFEFDBAE95ECFLLOSHAASQ
+ _associated conformance 10ShazamCore21AnnouncementsResponseV17ResourceReferenceV10CodingKeys33_24416F8B5A8CBE27877FFEFDBAE95ECFLLOs0G3KeyAAs23CustomStringConvertible
+ _associated conformance 10ShazamCore21AnnouncementsResponseV17ResourceReferenceV10CodingKeys33_24416F8B5A8CBE27877FFEFDBAE95ECFLLOs0G3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 10ShazamCore21AnnouncementsResponseV18ResourcesContainerV10CodingKeys33_24416F8B5A8CBE27877FFEFDBAE95ECFLLOSHAASQ
+ _associated conformance 10ShazamCore21AnnouncementsResponseV18ResourcesContainerV10CodingKeys33_24416F8B5A8CBE27877FFEFDBAE95ECFLLOs0G3KeyAAs23CustomStringConvertible
+ _associated conformance 10ShazamCore21AnnouncementsResponseV18ResourcesContainerV10CodingKeys33_24416F8B5A8CBE27877FFEFDBAE95ECFLLOs0G3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 10ShazamCore21AnnouncementsResponseV7AnyJSONO10CodingKeys33_24416F8B5A8CBE27877FFEFDBAE95ECFLLOSHAASQ
+ _associated conformance 10ShazamCore21AnnouncementsResponseV7AnyJSONO10CodingKeys33_24416F8B5A8CBE27877FFEFDBAE95ECFLLOs0G3KeyAAs23CustomStringConvertible
+ _associated conformance 10ShazamCore21AnnouncementsResponseV7AnyJSONO10CodingKeys33_24416F8B5A8CBE27877FFEFDBAE95ECFLLOs0G3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 10ShazamCore21AnnouncementsResponseV7AnyJSONO14BoolCodingKeys33_24416F8B5A8CBE27877FFEFDBAE95ECFLLOSHAASQ
+ _associated conformance 10ShazamCore21AnnouncementsResponseV7AnyJSONO14BoolCodingKeys33_24416F8B5A8CBE27877FFEFDBAE95ECFLLOs0H3KeyAAs23CustomStringConvertible
+ _associated conformance 10ShazamCore21AnnouncementsResponseV7AnyJSONO14BoolCodingKeys33_24416F8B5A8CBE27877FFEFDBAE95ECFLLOs0H3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 10ShazamCore21AnnouncementsResponseV7AnyJSONO14NullCodingKeys33_24416F8B5A8CBE27877FFEFDBAE95ECFLLOs0H3KeyAAs23CustomStringConvertible
+ _associated conformance 10ShazamCore21AnnouncementsResponseV7AnyJSONO14NullCodingKeys33_24416F8B5A8CBE27877FFEFDBAE95ECFLLOs0H3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 10ShazamCore21AnnouncementsResponseV7AnyJSONO15ArrayCodingKeys33_24416F8B5A8CBE27877FFEFDBAE95ECFLLOSHAASQ
+ _associated conformance 10ShazamCore21AnnouncementsResponseV7AnyJSONO15ArrayCodingKeys33_24416F8B5A8CBE27877FFEFDBAE95ECFLLOs0H3KeyAAs23CustomStringConvertible
+ _associated conformance 10ShazamCore21AnnouncementsResponseV7AnyJSONO15ArrayCodingKeys33_24416F8B5A8CBE27877FFEFDBAE95ECFLLOs0H3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 10ShazamCore21AnnouncementsResponseV7AnyJSONO16NumberCodingKeys33_24416F8B5A8CBE27877FFEFDBAE95ECFLLOSHAASQ
+ _associated conformance 10ShazamCore21AnnouncementsResponseV7AnyJSONO16NumberCodingKeys33_24416F8B5A8CBE27877FFEFDBAE95ECFLLOs0H3KeyAAs23CustomStringConvertible
+ _associated conformance 10ShazamCore21AnnouncementsResponseV7AnyJSONO16NumberCodingKeys33_24416F8B5A8CBE27877FFEFDBAE95ECFLLOs0H3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 10ShazamCore21AnnouncementsResponseV7AnyJSONO16ObjectCodingKeys33_24416F8B5A8CBE27877FFEFDBAE95ECFLLOSHAASQ
+ _associated conformance 10ShazamCore21AnnouncementsResponseV7AnyJSONO16ObjectCodingKeys33_24416F8B5A8CBE27877FFEFDBAE95ECFLLOs0H3KeyAAs23CustomStringConvertible
+ _associated conformance 10ShazamCore21AnnouncementsResponseV7AnyJSONO16ObjectCodingKeys33_24416F8B5A8CBE27877FFEFDBAE95ECFLLOs0H3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 10ShazamCore21AnnouncementsResponseV7AnyJSONO16StringCodingKeys33_24416F8B5A8CBE27877FFEFDBAE95ECFLLOSHAASQ
+ _associated conformance 10ShazamCore21AnnouncementsResponseV7AnyJSONO16StringCodingKeys33_24416F8B5A8CBE27877FFEFDBAE95ECFLLOs0H3KeyAAs011CustomDebugG11Convertible
+ _associated conformance 10ShazamCore21AnnouncementsResponseV7AnyJSONO16StringCodingKeys33_24416F8B5A8CBE27877FFEFDBAE95ECFLLOs0H3KeyAAs06CustomG11Convertible
+ _associated conformance 10ShazamCore21AnnouncementsResponseV7RawJSONV10CodingKeys33_24416F8B5A8CBE27877FFEFDBAE95ECFLLOSHAASQ
+ _associated conformance 10ShazamCore21AnnouncementsResponseV7RawJSONV10CodingKeys33_24416F8B5A8CBE27877FFEFDBAE95ECFLLOs0G3KeyAAs23CustomStringConvertible
+ _associated conformance 10ShazamCore21AnnouncementsResponseV7RawJSONV10CodingKeys33_24416F8B5A8CBE27877FFEFDBAE95ECFLLOs0G3KeyAAs28CustomDebugStringConvertible
+ _dispatch_group_create
+ _dispatch_group_enter
+ _dispatch_group_leave
+ _dispatch_group_notify
+ _dispatch_queue_create
+ _dispatch_semaphore_create
+ _dispatch_semaphore_signal
+ _dispatch_semaphore_wait
+ _dispatch_sync
+ _dispatch_time
+ _get_enum_tag_for_layout_string 10Foundation4DataV15_RepresentationO
+ _get_enum_tag_for_layout_string 10ShazamCore21AnnouncementsResponseV0cD5ErrorO
+ _get_enum_tag_for_layout_string 10ShazamCore21AnnouncementsResponseV7AnyJSONO
+ _kTCCServiceLiverpool
+ _malloc_size
+ _memcpy
+ _memmove
+ _objc_msgSend$URLByAppendingPathComponent:
+ _objc_msgSend$URLByAppendingPathComponent:conformingToType:
+ _objc_msgSend$addFinishBlock:
+ _objc_msgSend$announcementsBagConfigurationWithCompletion:
+ _objc_msgSend$announcementsBagValue
+ _objc_msgSend$arrayWithCapacity:
+ _objc_msgSend$buildEncoderForSession:clientType:clientIdentifier:
+ _objc_msgSend$campaignGroup
+ _objc_msgSend$clientIdentifier
+ _objc_msgSend$dataTaskPromiseWithRequest:
+ _objc_msgSend$defaultSessionConfiguration
+ _objc_msgSend$defaultValuesWithCompletion:
+ _objc_msgSend$downloadDirectory
+ _objc_msgSend$downloadTaskWithRequest:completionHandler:
+ _objc_msgSend$encoder
+ _objc_msgSend$endpointRequester
+ _objc_msgSend$endpointURLWithHost:path:languageCode:storefront:
+ _objc_msgSend$fileExistsAtPath:
+ _objc_msgSend$fileURLWithPath:
+ _objc_msgSend$firstObject
+ _objc_msgSend$globallyUniqueString
+ _objc_msgSend$handleResultData:forResponse:callback:error:
+ _objc_msgSend$init
+ _objc_msgSend$initWithClientIdentifier:bag:
+ _objc_msgSend$initWithClientIdentifier:clientType:
+ _objc_msgSend$initWithConfiguration:defaultConfigurationValues:
+ _objc_msgSend$initWithConfiguration:languageCode:
+ _objc_msgSend$initWithData:urlResponse:error:
+ _objc_msgSend$initWithDownloadedFileLocation:urlResponse:error:
+ _objc_msgSend$initWithRemoteConfiguration:storefrontProvider:
+ _objc_msgSend$initWithTokenService:
+ _objc_msgSend$initWithTokenService:bag:
+ _objc_msgSend$invalidate
+ _objc_msgSend$invalidateAndCancel
+ _objc_msgSend$isTokenFailureError:
+ _objc_msgSend$languageCode
+ _objc_msgSend$moveItemAtURL:toURL:error:
+ _objc_msgSend$performRequest:withReply:
+ _objc_msgSend$previewUpsellActionForOfferNamed:bundleID:
+ _objc_msgSend$previewUpsellSubtitleForOfferNamed:bundleID:
+ _objc_msgSend$previewUpsellTitleForOfferNamed:bundleID:
+ _objc_msgSend$processInfo
+ _objc_msgSend$providerToken
+ _objc_msgSend$rematchBagConfigurationValue
+ _objc_msgSend$remoteConfiguration
+ _objc_msgSend$removeItemAtURL:error:
+ _objc_msgSend$renameDownloadedFile:withFilename:usingType:error:
+ _objc_msgSend$requestByEncodingRequest:parameters:
+ _objc_msgSend$response
+ _objc_msgSend$session
+ _objc_msgSend$sessionConfiguration
+ _objc_msgSend$setClientType:
+ _objc_msgSend$setDiscretionary:
+ _objc_msgSend$setProtocolHandler:
+ _objc_msgSend$setSession:
+ _objc_msgSend$setTimeoutIntervalForRequest:
+ _objc_msgSend$setWaitsForConnectivity:
+ _objc_msgSend$storefrontProvider
+ _objc_msgSend$trackPageEndpoint
+ _objc_retainBlock
+ _objc_retain_x26
+ _objc_setProperty_nonatomic_copy
+ _swift_allocError
+ _swift_arrayDestroy
+ _swift_arrayInitWithCopy
+ _swift_bridgeObjectRetain
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_enumFn_getEnumTag
+ _swift_cvw_initWithCopy
+ _swift_cvw_initializeBufferWithCopyOfBuffer
+ _swift_errorRetain
+ _swift_getTypeByMangledNameInContextInMetadataState2
+ _swift_isUniquelyReferenced_nonNull_native
+ _swift_once
+ _swift_slowAlloc
+ _swift_slowDealloc
+ _swift_willThrow
+ _symbolic $s10ShazamCore29AnnouncementsResponseResourceP
+ _symbolic SDySSSDySS_____GG 10ShazamCore21AnnouncementsResponseV7RawJSONV
+ _symbolic SDySSSay_____GG 10ShazamCore21AnnouncementsResponseV17ResourceReferenceV
+ _symbolic SDySS_____G 10ShazamCore21AnnouncementsResponseV7AnyJSONO
+ _symbolic SDySS_____G 10ShazamCore21AnnouncementsResponseV7RawJSONV
+ _symbolic SDySSypG
+ _symbolic SS
+ _symbolic SSSg
+ _symbolic Say_____G 10ShazamCore21AnnouncementsResponseV17ResourceReferenceV
+ _symbolic Say_____G 10ShazamCore21AnnouncementsResponseV7AnyJSONO
+ _symbolic SayypG
+ _symbolic Sb
+ _symbolic Sd
+ _symbolic So8NSObjectCSg
+ _symbolic _____ 10Foundation4DataV
+ _symbolic _____ 10ShazamCore12FeatureFlagsO
+ _symbolic _____ 10ShazamCore16_FeatureFlagsKeyV
+ _symbolic _____ 10ShazamCore21AnnouncementsResponseV
+ _symbolic _____ 10ShazamCore21AnnouncementsResponseV0cD5ErrorO
+ _symbolic _____ 10ShazamCore21AnnouncementsResponseV10CodingKeys33_24416F8B5A8CBE27877FFEFDBAE95ECFLLO
+ _symbolic _____ 10ShazamCore21AnnouncementsResponseV16ResultsContainerV
+ _symbolic _____ 10ShazamCore21AnnouncementsResponseV16ResultsContainerV10CodingKeys33_24416F8B5A8CBE27877FFEFDBAE95ECFLLO
+ _symbolic _____ 10ShazamCore21AnnouncementsResponseV17ResourceReferenceV
+ _symbolic _____ 10ShazamCore21AnnouncementsResponseV17ResourceReferenceV10CodingKeys33_24416F8B5A8CBE27877FFEFDBAE95ECFLLO
+ _symbolic _____ 10ShazamCore21AnnouncementsResponseV18ResourcesContainerV
+ _symbolic _____ 10ShazamCore21AnnouncementsResponseV18ResourcesContainerV10CodingKeys33_24416F8B5A8CBE27877FFEFDBAE95ECFLLO
+ _symbolic _____ 10ShazamCore21AnnouncementsResponseV7AnyJSONO
+ _symbolic _____ 10ShazamCore21AnnouncementsResponseV7AnyJSONO10CodingKeys33_24416F8B5A8CBE27877FFEFDBAE95ECFLLO
+ _symbolic _____ 10ShazamCore21AnnouncementsResponseV7AnyJSONO14BoolCodingKeys33_24416F8B5A8CBE27877FFEFDBAE95ECFLLO
+ _symbolic _____ 10ShazamCore21AnnouncementsResponseV7AnyJSONO14NullCodingKeys33_24416F8B5A8CBE27877FFEFDBAE95ECFLLO
+ _symbolic _____ 10ShazamCore21AnnouncementsResponseV7AnyJSONO15ArrayCodingKeys33_24416F8B5A8CBE27877FFEFDBAE95ECFLLO
+ _symbolic _____ 10ShazamCore21AnnouncementsResponseV7AnyJSONO16NumberCodingKeys33_24416F8B5A8CBE27877FFEFDBAE95ECFLLO
+ _symbolic _____ 10ShazamCore21AnnouncementsResponseV7AnyJSONO16ObjectCodingKeys33_24416F8B5A8CBE27877FFEFDBAE95ECFLLO
+ _symbolic _____ 10ShazamCore21AnnouncementsResponseV7AnyJSONO16StringCodingKeys33_24416F8B5A8CBE27877FFEFDBAE95ECFLLO
+ _symbolic _____ 10ShazamCore21AnnouncementsResponseV7RawJSONV
+ _symbolic _____ 10ShazamCore21AnnouncementsResponseV7RawJSONV10CodingKeys33_24416F8B5A8CBE27877FFEFDBAE95ECFLLO
+ _symbolic _____ySSG s23_ContiguousArrayStorageC
+ _symbolic _____ySSypG s18_DictionaryStorageC
+ _symbolic _____y_____G s22KeyedDecodingContainerV 10ShazamCore21AnnouncementsResponseV10CodingKeys33_24416F8B5A8CBE27877FFEFDBAE95ECFLLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 10ShazamCore21AnnouncementsResponseV17ResourceReferenceV10CodingKeys33_24416F8B5A8CBE27877FFEFDBAE95ECFLLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 10ShazamCore21AnnouncementsResponseV07ResultsC0V10CodingKeys33_24416F8B5A8CBE27877FFEFDBAE95ECFLLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 10ShazamCore21AnnouncementsResponseV09ResourcesC0V10CodingKeys33_24416F8B5A8CBE27877FFEFDBAE95ECFLLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 10ShazamCore21AnnouncementsResponseV17ResourceReferenceV10CodingKeys33_24416F8B5A8CBE27877FFEFDBAE95ECFLLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 10ShazamCore21AnnouncementsResponseV7AnyJSONO10CodingKeys33_24416F8B5A8CBE27877FFEFDBAE95ECFLLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 10ShazamCore21AnnouncementsResponseV7AnyJSONO14BoolCodingKeys33_24416F8B5A8CBE27877FFEFDBAE95ECFLLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 10ShazamCore21AnnouncementsResponseV7AnyJSONO14NullCodingKeys33_24416F8B5A8CBE27877FFEFDBAE95ECFLLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 10ShazamCore21AnnouncementsResponseV7AnyJSONO15ArrayCodingKeys33_24416F8B5A8CBE27877FFEFDBAE95ECFLLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 10ShazamCore21AnnouncementsResponseV7AnyJSONO16NumberCodingKeys33_24416F8B5A8CBE27877FFEFDBAE95ECFLLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 10ShazamCore21AnnouncementsResponseV7AnyJSONO16ObjectCodingKeys33_24416F8B5A8CBE27877FFEFDBAE95ECFLLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 10ShazamCore21AnnouncementsResponseV7AnyJSONO16StringCodingKeys33_24416F8B5A8CBE27877FFEFDBAE95ECFLLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 10ShazamCore21AnnouncementsResponseV7RawJSONV10CodingKeys33_24416F8B5A8CBE27877FFEFDBAE95ECFLLO
+ _symbolic _____y_____G s23_ContiguousArrayStorageC s5UInt8V
+ _symbolic _____yypG s23_ContiguousArrayStorageC
+ _symbolic x
+ _symbolic ypXmT______t s13DecodingErrorO7ContextV
+ _type_layout_string 10ShazamCore16_FeatureFlagsKeyV
+ _type_layout_string 10ShazamCore21AnnouncementsResponseV
+ _type_layout_string 10ShazamCore21AnnouncementsResponseV0cD5ErrorO
+ _type_layout_string 10ShazamCore21AnnouncementsResponseV16ResultsContainerV
+ _type_layout_string 10ShazamCore21AnnouncementsResponseV17ResourceReferenceV
+ _type_layout_string 10ShazamCore21AnnouncementsResponseV7AnyJSONO
+ _type_layout_string 10ShazamCore21AnnouncementsResponseV7RawJSONV
- -[SHCampaignTokens initWithConfiguration:]
- -[SHDefaultConfigurationValues liveAudioMinimumRecordingDuration]
- GCC_except_table17
- GCC_except_table22
- ___block_literal_global.52
- ___block_literal_global.54
- ___block_literal_global.56
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$objectForKey:
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x2
- _objc_retain_x4
- _objc_retain_x9
CStrings:
+ "@\"AMSMediaRequestEncoder\""
+ "@\"AMSURLSession\""
+ "@\"NSData\""
+ "@\"NSError\""
+ "@\"NSURLResponse\""
+ "@\"SHAMSEndpointRequester\""
+ "@\"SHRemoteConfiguration\""
+ "@32@0:8@16@?24"
+ "@48@0:8@16@24@32^@40"
+ "@?"
+ "@?16@0:8"
+ "Announcements configuration values fetch complete with value %@ error %@"
+ "Decoding failed: "
+ "Downloaded archive file from server %@"
+ "Existing downloaded file at %@ could not be removed for a new download. Error: %@."
+ "Failed to create directory for network downloads. Error: %@"
+ "Failed to create dispatch group"
+ "Failed to create dispatch group for paginated network request"
+ "Failed to decode %s with ID %s: %@"
+ "Failed to encode network request %@"
+ "Failed to fetch data task %@"
+ "Failed to rename item at %@ to %@ Error: %@"
+ "Failed to start paginated network request"
+ "Fetching announcements configuration values..."
+ "Fetching rematch configuration values..."
+ "Invalid JSON format"
+ "Invalid string data"
+ "Please check that you have enabled the ShazamKit App Service for this app identifier (%@)"
+ "Rematch configuration values fetch complete with value %@ error %@"
+ "SHAMSEndpointRequester"
+ "SHAMSPaginatedEndpointRequester"
+ "SHAnnouncementsBagConfiguration"
+ "SHAnnouncementsRequester"
+ "SHNetworkDownloadResponse"
+ "SHNetworkDownloadUtilities"
+ "SHNetworkPaginatedRequester"
+ "SHNetworkRecognitionRequester"
+ "SHNetworkResponse"
+ "SHRematchBagConfiguration"
+ "Saving downloaded file to %@ instead"
+ "ShazamKit"
+ "T@\"AMSBagValue\",&,N,V_announcementsBagValue"
+ "T@\"AMSBagValue\",&,N,V_rematchBagConfigurationValue"
+ "T@\"AMSMediaRequestEncoder\",R,N,V_encoder"
+ "T@\"AMSURLSession\",&,N,V_session"
+ "T@\"NSData\",R,N,V_data"
+ "T@\"NSError\",R,N,V_error"
+ "T@\"NSString\",C,N,V_clientIdentifier"
+ "T@\"NSString\",R,C,N,V_campaignGroup"
+ "T@\"NSString\",R,C,N,V_languageCode"
+ "T@\"NSString\",R,C,N,V_providerToken"
+ "T@\"NSURL\",R,N,V_downloadedFileLocation"
+ "T@\"NSURLResponse\",R,N,V_urlResponse"
+ "T@\"SHAMSEndpointRequester\",&,N,V_endpointRequester"
+ "T@\"SHRemoteConfiguration\",R,N,V_remoteConfiguration"
+ "T@?,C,N,V_storefrontProvider"
+ "Tq,N,V_clientType"
+ "TrackPreviewUpsell"
+ "Type"
+ "URLByAppendingPathComponent:"
+ "URLByAppendingPathComponent:conformingToType:"
+ "Unsupported JSON"
+ "Zeus"
+ "_announcementsBagValue"
+ "_campaignGroup"
+ "_clientIdentifier"
+ "_clientType"
+ "_data"
+ "_downloadedFileLocation"
+ "_encoder"
+ "_endpointRequester"
+ "_error"
+ "_languageCode"
+ "_providerToken"
+ "_rematchBagConfigurationValue"
+ "_remoteConfiguration"
+ "_session"
+ "_storefrontProvider"
+ "_urlResponse"
+ "addFinishBlock:"
+ "announcementsBagConfigurationWithCompletion:"
+ "announcementsBagValue"
+ "arrayWithCapacity:"
+ "buildEncoderForSession:clientType:clientIdentifier:"
+ "cachedFileURLWithFilename:type:"
+ "campaignPreviewUpsellActionText"
+ "campaignPreviewUpsellSubtitle"
+ "campaignPreviewUpsellTitle"
+ "clientIdentifier"
+ "clientType"
+ "com.apple.ShazamKit.PaginatedEndpointRequester"
+ "com.apple.musicrecognition"
+ "com.apple.shazam.shazamcore"
+ "com.apple.shazamd/Downloads"
+ "dataTaskPromiseWithRequest:"
+ "defaultPreviewUpsellActionText"
+ "defaultPreviewUpsellSubtitle"
+ "defaultPreviewUpsellTitle"
+ "defaultSessionConfiguration"
+ "disableShazamLibraryCloudKitAccess"
+ "downloadDirectory"
+ "downloadTaskWithRequest:completionHandler:"
+ "downloadedFileLocation"
+ "encoder"
+ "endpointRequester"
+ "endpointURLWithHost:path:languageCode:storefront:"
+ "error"
+ "feature-enabled"
+ "fileExistsAtPath:"
+ "fileURLWithPath:"
+ "firstObject"
+ "globallyUniqueString"
+ "handleResultData:forResponse:callback:error:"
+ "initWithClientIdentifier:bag:"
+ "initWithClientIdentifier:clientType:"
+ "initWithConfiguration:defaultConfigurationValues:"
+ "initWithConfiguration:languageCode:"
+ "initWithData:urlResponse:error:"
+ "initWithDownloadedFileLocation:urlResponse:error:"
+ "initWithRemoteConfiguration:"
+ "initWithRemoteConfiguration:storefrontProvider:"
+ "initWithTokenService:"
+ "initWithTokenService:bag:"
+ "invalidate"
+ "invalidateAndCancel"
+ "isEnabledForClientIdentifier:"
+ "isTokenFailureError:"
+ "languageCode"
+ "moveItemAtURL:toURL:error:"
+ "performDownloadRequest:filename:fileType:reply:"
+ "performRequest:withReply:"
+ "performRequests:completionHandler:"
+ "previewUpsellAction"
+ "previewUpsellActionForOfferNamed:bundleID:"
+ "previewUpsellSubtitle"
+ "previewUpsellSubtitleForOfferNamed:bundleID:"
+ "previewUpsellTitle"
+ "previewUpsellTitleForOfferNamed:bundleID:"
+ "processInfo"
+ "q"
+ "rematchBagConfigurationValue"
+ "rematchBagConfigurationWithCompletion:"
+ "remoteConfiguration"
+ "removeItemAtURL:error:"
+ "renameDownloadedFile:withFilename:usingType:error:"
+ "requestByEncodingRequest:parameters:"
+ "response"
+ "session"
+ "sessionConfiguration"
+ "setAnnouncementsBagValue:"
+ "setClientIdentifier:"
+ "setClientType:"
+ "setDiscretionary:"
+ "setEndpointRequester:"
+ "setProtocolHandler:"
+ "setRematchBagConfigurationValue:"
+ "setSession:"
+ "setStorefrontProvider:"
+ "setTimeoutIntervalForRequest:"
+ "setWaitsForConnectivity:"
+ "shazam-announcements"
+ "shazam-rematch-configuration"
+ "storefrontProvider"
+ "track-page-endpoint"
+ "trackPageEndpoint"
+ "trackPageEndpointWithCompletion:"
+ "urlResponse"
+ "v16@?0@\"SHNetworkResponse\"8"
+ "v16@?0@?<v@?@\"NSString\">8"
+ "v24@0:8q16"
+ "v24@?0@\"AMSURLRequest\"8@\"NSError\"16"
+ "v24@?0@\"AMSURLResult\"8@\"NSError\"16"
+ "v24@?0@\"SHAnnouncementsBagConfiguration\"8@\"NSError\"16"
+ "v24@?0@\"SHDefaultConfigurationValues\"8@\"NSError\"16"
+ "v32@0:8@\"NSArray\"16@?<v@?@\"NSArray\"@\"NSError\">24"
+ "v32@0:8@\"NSURLRequest\"16@?<v@?@\"SHNetworkResponse\">24"
+ "v32@?0@\"NSURL\"8@\"NSURLResponse\"16@\"NSError\"24"
+ "v48@0:8@\"NSURLRequest\"16@\"NSString\"24@\"UTType\"32@?<v@?@\"SHNetworkDownloadResponse\">40"
+ "v48@0:8@16@24@32@?40"
+ "v48@0:8@16@24@?32@40"
- "liveAudioMinimumRecordingDuration"
- "objectForKey:"

```
