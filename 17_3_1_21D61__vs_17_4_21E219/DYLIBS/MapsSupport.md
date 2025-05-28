## MapsSupport

> `/System/Library/PrivateFrameworks/MapsSupport.framework/MapsSupport`

```diff

-2811.33.11.14.6
-  __TEXT.__text: 0x6ca4c
-  __TEXT.__auth_stubs: 0xa50
-  __TEXT.__objc_methlist: 0x6694
+2811.34.10.5.30
+  __TEXT.__text: 0x70c58
+  __TEXT.__auth_stubs: 0xad0
+  __TEXT.__objc_methlist: 0x6954
   __TEXT.__const: 0x134
-  __TEXT.__cstring: 0x53ab
-  __TEXT.__oslogstring: 0x6afc
-  __TEXT.__gcc_except_tab: 0xac0
+  __TEXT.__cstring: 0x5900
+  __TEXT.__oslogstring: 0x6e2d
+  __TEXT.__gcc_except_tab: 0xbfc
   __TEXT.__dlopen_cstrs: 0x104
   __TEXT.__ustring: 0x2b2
-  __TEXT.__unwind_info: 0x1ad4
-  __TEXT.__objc_classname: 0xfde
-  __TEXT.__objc_methname: 0x100ab
-  __TEXT.__objc_methtype: 0x30d9
-  __TEXT.__objc_stubs: 0xb900
-  __DATA_CONST.__got: 0x1c0
-  __DATA_CONST.__const: 0x22b8
-  __DATA_CONST.__objc_classlist: 0x2d0
-  __DATA_CONST.__objc_catlist: 0x78
-  __DATA_CONST.__objc_protolist: 0x210
+  __TEXT.__unwind_info: 0x1bbc
+  __TEXT.__objc_classname: 0x1091
+  __TEXT.__objc_methname: 0x10e55
+  __TEXT.__objc_methtype: 0x3276
+  __TEXT.__objc_stubs: 0xc360
+  __DATA_CONST.__got: 0x1d8
+  __DATA_CONST.__const: 0x25b8
+  __DATA_CONST.__objc_classlist: 0x2f8
+  __DATA_CONST.__objc_catlist: 0x80
+  __DATA_CONST.__objc_protolist: 0x218
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xbd50
-  __DATA_CONST.__objc_selrefs: 0x3bd0
-  __AUTH_CONST.__cfstring: 0x3d00
-  __AUTH_CONST.__objc_const: 0x2610
-  __AUTH_CONST.__const: 0x9c0
+  __DATA_CONST.__objc_const: 0xc420
+  __DATA_CONST.__objc_selrefs: 0x3ea0
+  __DATA_CONST.__objc_protorefs: 0x68
+  __DATA_CONST.__objc_classrefs: 0x5f8
+  __DATA_CONST.__objc_superrefs: 0x318
+  __AUTH_CONST.__cfstring: 0x3ee0
+  __AUTH_CONST.__objc_const: 0x2770
+  __AUTH_CONST.__const: 0xac0
   __AUTH_CONST.__objc_intobj: 0x1b0
-  __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH_CONST.__auth_got: 0x538
-  __AUTH.__objc_data: 0x1270
+  __AUTH_CONST.__objc_doubleobj: 0x20
+  __AUTH_CONST.__auth_got: 0x578
+  __AUTH.__objc_data: 0x13b0
   __AUTH.__data: 0x10
-  __DATA.__objc_protorefs: 0x68
-  __DATA.__objc_classrefs: 0x598
-  __DATA.__objc_superrefs: 0x2f8
-  __DATA.__objc_ivar: 0x414
-  __DATA.__data: 0x1b40
+  __DATA.__objc_ivar: 0x45c
+  __DATA.__data: 0x1bf0
+  __DATA.__bss: 0x20
   __DATA.__common: 0x10
-  __DATA.__bss: 0x30
   __DATA_DIRTY.__objc_ivar: 0x32c
-  __DATA_DIRTY.__objc_data: 0x9b0
+  __DATA_DIRTY.__objc_data: 0xa00
   __DATA_DIRTY.__data: 0x10
-  __DATA_DIRTY.__bss: 0x1c0
+  __DATA_DIRTY.__bss: 0x260
   __DATA_DIRTY.__common: 0x30
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /System/Library/PrivateFrameworks/TCC.framework/TCC
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2551
-  Symbols:   8672
-  CStrings:  4422
+  Functions: 2649
+  Symbols:   9058
+  CStrings:  4623
 
Symbols:
+ -[GEOPDBankTransactionInformation(MSPWallet) initWithMSPWalletBankTransactionInformation:rawMerchantCode:industryCategory:]
+ -[MSPAuthFeedbackReportTicket _dataToSign]
+ -[MSPAuthFeedbackReportTicket submitWithCallbackQueue:handler:networkActivity:]
+ -[MSPBaseFeedbackReportTicket .cxx_destruct]
+ -[MSPBaseFeedbackReportTicket _submitWithCallbackQueue:handler:networkActivity:]
+ -[MSPBaseFeedbackReportTicket cancel]
+ -[MSPBaseFeedbackReportTicket initWithFeedbackRequestParameters:traits:userInfoType:]
+ -[MSPBaseFeedbackReportTicket requestParameters]
+ -[MSPBaseFeedbackReportTicket setTicket:]
+ -[MSPBaseFeedbackReportTicket setWillSubmitRequestBlock:]
+ -[MSPBaseFeedbackReportTicket submitWithCallbackQueue:handler:networkActivity:]
+ -[MSPBaseFeedbackReportTicket submitWithHandler:networkActivity:]
+ -[MSPBaseFeedbackReportTicket ticket]
+ -[MSPBaseFeedbackReportTicket traits]
+ -[MSPBaseFeedbackReportTicket userInfoType]
+ -[MSPBaseFeedbackReportTicket userInfo]
+ -[MSPBaseFeedbackReportTicket willSubmitRequestBlock]
+ -[MSPSharedTripCapabilityLevelFetcher _retryAfterBackoff]
+ -[MSPWalletBankTransactionInformation .cxx_destruct]
+ -[MSPWalletBankTransactionInformation bankIdentifier]
+ -[MSPWalletBankTransactionInformation bankTransactionDescriptionClean]
+ -[MSPWalletBankTransactionInformation bankTransactionDescription]
+ -[MSPWalletBankTransactionInformation enableBrandMuidFallback]
+ -[MSPWalletBankTransactionInformation industryCode]
+ -[MSPWalletBankTransactionInformation merchantInformation]
+ -[MSPWalletBankTransactionInformation otherTransactionLocations]
+ -[MSPWalletBankTransactionInformation setBankIdentifier:]
+ -[MSPWalletBankTransactionInformation setBankTransactionDescription:]
+ -[MSPWalletBankTransactionInformation setBankTransactionDescriptionClean:]
+ -[MSPWalletBankTransactionInformation setEnableBrandMuidFallback:]
+ -[MSPWalletBankTransactionInformation setIndustryCode:]
+ -[MSPWalletBankTransactionInformation setMerchantInformation:]
+ -[MSPWalletBankTransactionInformation setOtherTransactionLocations:]
+ -[MSPWalletBankTransactionInformation setTransactionCurrencyCode:]
+ -[MSPWalletBankTransactionInformation setTransactionStatus:]
+ -[MSPWalletBankTransactionInformation setTransactionTimestamp:]
+ -[MSPWalletBankTransactionInformation setTransactionType:]
+ -[MSPWalletBankTransactionInformation transactionCurrencyCode]
+ -[MSPWalletBankTransactionInformation transactionStatus]
+ -[MSPWalletBankTransactionInformation transactionTimestamp]
+ -[MSPWalletBankTransactionInformation transactionType]
+ -[MSPWalletRAPReport .cxx_destruct]
+ -[MSPWalletRAPReport correlationId]
+ -[MSPWalletRAPReport initForMerchantIssue:merchantIndustryCode:mapsIdentifier:merchantName:merchantRawName:merchantIndustryCategory:merchantURL:merchantFormattedAddress:transactionTime:transactionType:transactionLocation:bankTransactionInformation:]
+ -[MSPWalletRAPReport isAppleCard]
+ -[MSPWalletRAPReport lookupTransactionType]
+ -[MSPWalletRAPReport merchantAdamId]
+ -[MSPWalletRAPReport reportersComment]
+ -[MSPWalletRAPReport requestParameters]
+ -[MSPWalletRAPReport setCorrelationId:]
+ -[MSPWalletRAPReport setIsAppleCard:]
+ -[MSPWalletRAPReport setLookupTransactionType:]
+ -[MSPWalletRAPReport setMerchantAdamId:]
+ -[MSPWalletRAPReport setReportersComment:]
+ GCC_except_table1
+ _DeviceIdentityLibrary
+ _DeviceIdentityLibraryCore.frameworkLibrary
+ _GEOConfigMSPDefaultArrivingSoonInterval_Metadata_block_invoke_28
+ _GEOConfigMSPDefaultMaxNumberOfNotifications_Metadata_block_invoke_29
+ _GEOConfigMSPDefaultMinimumNotificationInterval_Metadata_block_invoke_30
+ _GEOConfigMSPDefaultTripAbandonExpiryInterval_Metadata_block_invoke_31
+ _GEOConfigMSPDefaultTripClosedExpiryInterval_Metadata_block_invoke_32
+ _GEOConfigMSPDefaultTripExpirationCheckupInterval_Metadata_block_invoke_33
+ _GEOConfigMSPForceLiveStrategy_Metadata_block_invoke_34
+ _GEOConfigMSPInitialMinimumETADifference_Metadata_block_invoke_35
+ _GEOConfigMSPMaximumNumberNotificationsMessageStrategy_Metadata_block_invoke_36
+ _GEOConfigMSPMinimumETADifferenceIncrement_Metadata_block_invoke_37
+ _GEOConfigMSPSenderLiveStrategyETAUpdateIntervalThrottle_Metadata_block_invoke_38
+ _GEOConfigMSPSenderMinimalStrategyETANearArrivalInterval_Metadata_block_invoke_39
+ _GEOConfigMSPSenderMinimalStrategyETAUpdateIntervalThrottle_Metadata_block_invoke_40
+ _GEOConfigMSPSenderMinimalStrategyETAUpdateNearArrivalIntervalThrottle_Metadata_block_invoke_41
+ _GEOConfigMSPSharedETASenderIdentifier_Metadata_block_invoke_42
+ _GEOConfigMSPSharedTripServerEnabled_Metadata_block_invoke_43
+ _GEOConfigMSPUGCLogDiscardCertificateDurationInMinutes
+ _GEOConfigMSPUGCLogDiscardCertificateDurationInMinutes_Metadata
+ _GEOConfigMSPUGCLogDiscardCertificateDurationInMinutes_Metadata_block_invoke_23
+ _GEOConfigMSPUGCLogDiscardShouldReuseExistingKey
+ _GEOConfigMSPUGCLogDiscardShouldReuseExistingKey_Metadata
+ _GEOConfigMSPUGCLogDiscardShouldReuseExistingKey_Metadata_block_invoke_24
+ _GEOConfigMSPUGCShouldCacheBAACertificatesForRAPRequests
+ _GEOConfigMSPUGCShouldCacheBAACertificatesForRAPRequests_Metadata
+ _GEOConfigMSPUGCShouldCacheBAACertificatesForRAPRequests_Metadata_block_invoke_26
+ _GEOConfigMSPUGCShouldSendNonceInBAACertificate
+ _GEOConfigMSPUGCShouldSendNonceInBAACertificate_Metadata
+ _GEOConfigMSPUGCShouldSendNonceInBAACertificate_Metadata_block_invoke_25
+ _GEOConfigMSPUGCTimeIntervalToCacheBAACertificatesForRAPRequests
+ _GEOConfigMSPUGCTimeIntervalToCacheBAACertificatesForRAPRequests_Metadata
+ _GEOConfigMSPUGCTimeIntervalToCacheBAACertificatesForRAPRequests_Metadata_block_invoke_27
+ _MSPGetMSPAuthFeedbackReportTicketLog
+ _MSPGetUGCBAAUtilitiesLog
+ _MSPUGCFetchClientCertificate
+ _MSPUGCFetchClientCertificateWithCompletion
+ _MSPUGCPerformLogDiscardForCurrentSessionWithCompletion
+ _MSPUGCPerformLogDiscardForSessionEntityWithCompletion
+ _MSPUGCPerformLogDiscardForSessionWithCompletion
+ _MSPWalletRAPAuthenticatedFeedbackTicket
+ _MSPWalletRAPUnauthenticatedFeedbackTicket
+ _NSUnderlyingErrorKey
+ _OBJC_CLASS_$_GEOMapService
+ _OBJC_CLASS_$_GEOPDBankTransactionInformation
+ _OBJC_CLASS_$_GEORPFeedbackCommonCorrections
+ _OBJC_CLASS_$_GEORPFeedbackRequest
+ _OBJC_CLASS_$_GEORPFeedbackRequestParameters
+ _OBJC_CLASS_$_GEORPFeedbackUserInfo
+ _OBJC_CLASS_$_GEORPMerchantLookupCorrections
+ _OBJC_CLASS_$_GEORPTdmInfo
+ _OBJC_CLASS_$_GEORPUserCredentials
+ _OBJC_CLASS_$_GEOUserSessionEntity
+ _OBJC_CLASS_$_MSPAuthFeedbackReportTicket
+ _OBJC_CLASS_$_MSPBaseFeedbackReportTicket
+ _OBJC_CLASS_$_MSPUnauthFeedbackReportTicket
+ _OBJC_CLASS_$_MSPWalletBankTransactionInformation
+ _OBJC_CLASS_$_MSPWalletRAPReport
+ _OBJC_IVAR_$_MSPBaseFeedbackReportTicket._requestParameters
+ _OBJC_IVAR_$_MSPBaseFeedbackReportTicket._ticket
+ _OBJC_IVAR_$_MSPBaseFeedbackReportTicket._traits
+ _OBJC_IVAR_$_MSPBaseFeedbackReportTicket._userInfo
+ _OBJC_IVAR_$_MSPBaseFeedbackReportTicket._userInfoType
+ _OBJC_IVAR_$_MSPBaseFeedbackReportTicket._willSubmitRequestBlock
+ _OBJC_IVAR_$_MSPSharedTripCapabilityLevelFetcher._workQueue
+ _OBJC_IVAR_$_MSPWalletBankTransactionInformation._bankIdentifier
+ _OBJC_IVAR_$_MSPWalletBankTransactionInformation._bankTransactionDescription
+ _OBJC_IVAR_$_MSPWalletBankTransactionInformation._bankTransactionDescriptionClean
+ _OBJC_IVAR_$_MSPWalletBankTransactionInformation._enableBrandMuidFallback
+ _OBJC_IVAR_$_MSPWalletBankTransactionInformation._industryCode
+ _OBJC_IVAR_$_MSPWalletBankTransactionInformation._merchantInformation
+ _OBJC_IVAR_$_MSPWalletBankTransactionInformation._otherTransactionLocations
+ _OBJC_IVAR_$_MSPWalletBankTransactionInformation._transactionCurrencyCode
+ _OBJC_IVAR_$_MSPWalletBankTransactionInformation._transactionStatus
+ _OBJC_IVAR_$_MSPWalletBankTransactionInformation._transactionTimestamp
+ _OBJC_IVAR_$_MSPWalletBankTransactionInformation._transactionType
+ _OBJC_IVAR_$_MSPWalletRAPReport._requestParameters
+ _OBJC_METACLASS_$_MSPAuthFeedbackReportTicket
+ _OBJC_METACLASS_$_MSPBaseFeedbackReportTicket
+ _OBJC_METACLASS_$_MSPUnauthFeedbackReportTicket
+ _OBJC_METACLASS_$_MSPWalletBankTransactionInformation
+ _OBJC_METACLASS_$_MSPWalletRAPReport
+ _SecCertificateCopyData
+ _SecKeyCreateSignature
+ __OBJC_$_CATEGORY_GEOPDBankTransactionInformation_$_MSPWallet
+ __OBJC_$_INSTANCE_METHODS_GEOPDBankTransactionInformation(MSPWallet)
+ __OBJC_$_INSTANCE_METHODS_MSPAuthFeedbackReportTicket
+ __OBJC_$_INSTANCE_METHODS_MSPBaseFeedbackReportTicket
+ __OBJC_$_INSTANCE_METHODS_MSPWalletBankTransactionInformation
+ __OBJC_$_INSTANCE_METHODS_MSPWalletRAPReport
+ __OBJC_$_INSTANCE_VARIABLES_MSPBaseFeedbackReportTicket
+ __OBJC_$_INSTANCE_VARIABLES_MSPWalletBankTransactionInformation
+ __OBJC_$_INSTANCE_VARIABLES_MSPWalletRAPReport
+ __OBJC_$_PROP_LIST_MSPBaseFeedbackReportTicket
+ __OBJC_$_PROP_LIST_MSPFeedbackReportTicket
+ __OBJC_$_PROP_LIST_MSPWalletBankTransactionInformation
+ __OBJC_$_PROP_LIST_MSPWalletRAPReport
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MSPFeedbackReportTicket
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MSPFeedbackReportTicket
+ __OBJC_$_PROTOCOL_REFS_MSPFeedbackReportTicket
+ __OBJC_CLASS_PROTOCOLS_$_MSPBaseFeedbackReportTicket
+ __OBJC_CLASS_RO_$_MSPAuthFeedbackReportTicket
+ __OBJC_CLASS_RO_$_MSPBaseFeedbackReportTicket
+ __OBJC_CLASS_RO_$_MSPUnauthFeedbackReportTicket
+ __OBJC_CLASS_RO_$_MSPWalletBankTransactionInformation
+ __OBJC_CLASS_RO_$_MSPWalletRAPReport
+ __OBJC_LABEL_PROTOCOL_$_MSPFeedbackReportTicket
+ __OBJC_METACLASS_RO_$_MSPAuthFeedbackReportTicket
+ __OBJC_METACLASS_RO_$_MSPBaseFeedbackReportTicket
+ __OBJC_METACLASS_RO_$_MSPUnauthFeedbackReportTicket
+ __OBJC_METACLASS_RO_$_MSPWalletBankTransactionInformation
+ __OBJC_METACLASS_RO_$_MSPWalletRAPReport
+ __OBJC_PROTOCOL_$_MSPFeedbackReportTicket
+ ___28-[MSPSharedTripService init]_block_invoke.68
+ ___47-[MSPSharedTripService _openConnectionIfNeeded]_block_invoke.187
+ ___54-[MSPSharedTripService _performBlockAfterInitialSync:]_block_invoke.80
+ ___58-[MSPSharedTripServer listener:shouldAcceptNewConnection:]_block_invoke.131
+ ___60-[MSPSharedTripService _performBlockAfterInitialConnection:]_block_invoke.77
+ ___60-[MSPSharedTripService _startSharingWithContact:completion:]_block_invoke.85
+ ___60-[MSPSharedTripService _startSharingWithContact:completion:]_block_invoke_2.86
+ ___60-[MSPSharedTripService stopAllSharingWithReason:completion:]_block_invoke.97
+ ___61-[MSPSharedTripService _stopAllSharingWithReason:completion:]_block_invoke.98
+ ___61-[MSPSharedTripService _stopAllSharingWithReason:completion:]_block_invoke_2.99
+ ___65-[MSPSharedTripCapabilityLevelFetcher capabilityLevelForContact:]_block_invoke
+ ___66-[MSPSharedTripService _stopSharingWithContact:reason:completion:]_block_invoke.95
+ ___66-[MSPSharedTripService _stopSharingWithContact:reason:completion:]_block_invoke_2.96
+ ___79-[MSPAuthFeedbackReportTicket submitWithCallbackQueue:handler:networkActivity:]_block_invoke
+ ___79-[MSPSharedTripService _subscribeToSharedTripUpdatesWithIdentifier:completion:]_block_invoke.128
+ ___80-[MSPBaseFeedbackReportTicket _submitWithCallbackQueue:handler:networkActivity:]_block_invoke
+ ___80-[MSPBaseFeedbackReportTicket _submitWithCallbackQueue:handler:networkActivity:]_block_invoke_2
+ ___80-[MSPBaseFeedbackReportTicket _submitWithCallbackQueue:handler:networkActivity:]_block_invoke_3
+ ___80-[MSPBaseFeedbackReportTicket _submitWithCallbackQueue:handler:networkActivity:]_block_invoke_4
+ ___DeviceIdentityLibraryCore_block_invoke
+ ___MSPGetMSPAuthFeedbackReportTicketLog_block_invoke
+ ___MSPGetMSPWalletRAPLog_block_invoke
+ ___MSPGetUGCBAAUtilitiesLog_block_invoke
+ ___MSPUGCFetchClientCertificate_block_invoke
+ ___MSPUGCFetchClientCertificate_block_invoke.19
+ ___MSPUGCPerformLogDiscardForSessionEntityWithCompletion_block_invoke
+ ___MSPWalletRAPAuthenticatedFeedbackTicket_block_invoke
+ ___MSPWalletRAPUnauthenticatedFeedbackTicket_block_invoke
+ ___UGCFetchLogDiscardCertificatesForSessionWithCompletion_block_invoke
+ ___UGCFetchLogDiscardCertificatesForSessionWithCompletion_block_invoke.64
+ ___block_descriptor_40_e30_v16?0"GEORPFeedbackRequest"8l
+ ___block_descriptor_41_e8_32bs_e5_v8?0ls32l8
+ ___block_descriptor_48_e8_32r_e5_v8?0lr32l8
+ ___block_descriptor_48_e8_32s40bs_e40_v32?0"NSArray"8"NSData"16"NSError"24ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e43_v32?0^{__SecKey=}8"NSArray"16"NSError"24ls40l8s32l8
+ ___block_descriptor_48_e8_32s40bs_e54_v32?0"GEORPFeedbackResponse"8"NSData"16"NSError"24ls40l8s32l8
+ ___block_descriptor_48_e8_32s40bs_e8_v12?0B8ls40l8s32l8
+ ___block_descriptor_64_e8_32s40s48bs56bs_e40_v32?0"NSArray"8"NSData"16"NSError"24ls48l8s32l8s40l8s56l8
+ ___block_descriptor_64_e8_32s40s48r56r_e5_v8?0lr48l8s32l8s40l8r56l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e5_v8?0ls56l8s32l8s40l8s48l8
+ ___block_descriptor_76_e8_32s40s48s56bs_e40_v32?0"NSArray"8"NSData"16"NSError"24ls32l8s40l8s48l8s56l8
+ ___block_descriptor_81_e8_32s40s48s56s64bs_e5_v8?0ls32l8s40l8s48l8s64l8s56l8
+ ___block_literal_global.101
+ ___block_literal_global.129
+ ___block_literal_global.134
+ ___block_literal_global.139
+ ___block_literal_global.144
+ ___block_literal_global.151
+ ___block_literal_global.158
+ ___block_literal_global.165
+ ___block_literal_global.172
+ ___block_literal_global.179
+ ___block_literal_global.186
+ ___block_literal_global.193
+ ___block_literal_global.198
+ ___block_literal_global.203
+ ___block_literal_global.210
+ ___block_literal_global.215
+ ___block_literal_global.222
+ ___block_literal_global.229
+ ___block_literal_global.236
+ ___block_literal_global.243
+ ___block_literal_global.248
+ ___block_literal_global.90
+ ___block_literal_global.98
+ ___getDeviceIdentityIssueClientCertificateWithCompletionSymbolLoc_block_invoke
+ ___getDeviceIdentityUCRTAttestationSupportedSymbolLoc_block_invoke
+ ___getkMAOptionsBAAKeychainLabelSymbolLoc_block_invoke
+ ___getkMAOptionsBAANonceSymbolLoc_block_invoke
+ ___getkMAOptionsBAAOIDHardwarePropertiesSymbolLoc_block_invoke
+ ___getkMAOptionsBAAOIDKeyUsagePropertiesSymbolLoc_block_invoke
+ ___getkMAOptionsBAAOIDNonceSymbolLoc_block_invoke
+ ___getkMAOptionsBAAOIDSToIncludeSymbolLoc_block_invoke
+ ___getkMAOptionsBAASCRTAttestationSymbolLoc_block_invoke
+ ___getkMAOptionsBAAValiditySymbolLoc_block_invoke
+ ___getkMAOptionsResuseExistingKeySymbolLoc_block_invoke
+ __os_log_default
+ __os_log_error_impl
+ __os_log_fault_impl
+ _dlerror
+ _dlsym
+ _kSecKeyAlgorithmECDSASignatureMessageX962SHA256
+ _objc_msgSend$_credentialsForPrimaryICloudAccount
+ _objc_msgSend$_dataToSign
+ _objc_msgSend$_retryAfterBackoff
+ _objc_msgSend$_submitWithCallbackQueue:handler:networkActivity:
+ _objc_msgSend$addOtherTransactionLocations:
+ _objc_msgSend$anonymousUserId
+ _objc_msgSend$baaCertificates
+ _objc_msgSend$baaSignature
+ _objc_msgSend$bankIdentifier
+ _objc_msgSend$bankTransactionDescription
+ _objc_msgSend$bankTransactionDescriptionClean
+ _objc_msgSend$cancel
+ _objc_msgSend$captureUgcDeleteWithSignature:certificates:trigger:queue:completion:
+ _objc_msgSend$comments
+ _objc_msgSend$commonCorrections
+ _objc_msgSend$context
+ _objc_msgSend$correlationId
+ _objc_msgSend$dataUsingEncoding:
+ _objc_msgSend$details
+ _objc_msgSend$enableBrandMuidFallback
+ _objc_msgSend$feedbackRequestParameters
+ _objc_msgSend$icloudUserPersonId
+ _objc_msgSend$industryCode
+ _objc_msgSend$initWithFeedbackRequestParameters:traits:userInfoType:
+ _objc_msgSend$initWithFeedbackRequestParameters:userInfo:traits:
+ _objc_msgSend$initWithMSPWalletBankTransactionInformation:rawMerchantCode:industryCategory:
+ _objc_msgSend$initWithMerchantIndustryCode:mapsIdentifier:merchantName:merchantRawName:merchantIndustryCategory:merchantURL:merchantFormattedAddress:transactionTime:transactionType:transactionLocation:merchantBankTransactionInfo:
+ _objc_msgSend$initWithSessionID:sessionCreationTime:sequenceNumber:
+ _objc_msgSend$isAppleCard
+ _objc_msgSend$mapsUserSessionEntity
+ _objc_msgSend$merchantAdamId
+ _objc_msgSend$merchantBankTransactionInfo
+ _objc_msgSend$merchantInformation
+ _objc_msgSend$merchantLookupFeedback
+ _objc_msgSend$otherTransactionLocations
+ _objc_msgSend$requestParameters
+ _objc_msgSend$requestTransactionType
+ _objc_msgSend$sessionID
+ _objc_msgSend$sessionUUIDString
+ _objc_msgSend$setAnonymisedUserId:
+ _objc_msgSend$setAnonymousUserId:
+ _objc_msgSend$setBaaCertificates:
+ _objc_msgSend$setBaaSignature:
+ _objc_msgSend$setBankIdentifier:
+ _objc_msgSend$setBankTransactionDescription:
+ _objc_msgSend$setBankTransactionDescriptionClean:
+ _objc_msgSend$setBankTransactionType:
+ _objc_msgSend$setComments:
+ _objc_msgSend$setCommonCorrections:
+ _objc_msgSend$setCorrections:
+ _objc_msgSend$setCorrelationId:
+ _objc_msgSend$setEnableBrandMuidFallback:
+ _objc_msgSend$setIndustryCategory:
+ _objc_msgSend$setIndustryCode:
+ _objc_msgSend$setIsAppleCard:
+ _objc_msgSend$setIsCategoryIncorrect:
+ _objc_msgSend$setIsMerchantIncorrect:
+ _objc_msgSend$setIsOtherIssue:
+ _objc_msgSend$setMerchantAdamId:
+ _objc_msgSend$setMerchantInformation:
+ _objc_msgSend$setRawMerchantCode:
+ _objc_msgSend$setRequestTransactionType:
+ _objc_msgSend$setShareSessionWithMaps:
+ _objc_msgSend$setTdmUserInfo:
+ _objc_msgSend$setTicket:
+ _objc_msgSend$setTransactionCurrencyCode:
+ _objc_msgSend$setTransactionStatus:
+ _objc_msgSend$setTransactionTimestamp:
+ _objc_msgSend$setUserCredentials:
+ _objc_msgSend$setWillSubmitRequestBlock:
+ _objc_msgSend$sharedService
+ _objc_msgSend$submissionParameters
+ _objc_msgSend$submitWithCallbackQueue:handler:networkActivity:
+ _objc_msgSend$submitWithHandler:networkActivity:
+ _objc_msgSend$tdmUserInfo
+ _objc_msgSend$ticket
+ _objc_msgSend$ticketForFeedbackRequest:traits:
+ _objc_msgSend$traits
+ _objc_msgSend$transactionCurrencyCode
+ _objc_msgSend$transactionStatus
+ _objc_msgSend$transactionTimestamp
+ _objc_msgSend$transactionType
+ _objc_msgSend$userCredentials
+ _objc_msgSend$userInfoType
+ _objc_msgSend$willSubmitRequestBlock
+ _objc_retain_x6
+ _strcmp
- _GEOConfigMSPDefaultArrivingSoonInterval_Metadata_block_invoke_23
- _GEOConfigMSPDefaultMaxNumberOfNotifications_Metadata_block_invoke_24
- _GEOConfigMSPDefaultMinimumNotificationInterval_Metadata_block_invoke_25
- _GEOConfigMSPDefaultTripAbandonExpiryInterval_Metadata_block_invoke_26
- _GEOConfigMSPDefaultTripClosedExpiryInterval_Metadata_block_invoke_27
- _GEOConfigMSPDefaultTripExpirationCheckupInterval_Metadata_block_invoke_28
- _GEOConfigMSPForceLiveStrategy_Metadata_block_invoke_29
- _GEOConfigMSPInitialMinimumETADifference_Metadata_block_invoke_30
- _GEOConfigMSPMaximumNumberNotificationsMessageStrategy_Metadata_block_invoke_31
- _GEOConfigMSPMinimumETADifferenceIncrement_Metadata_block_invoke_32
- _GEOConfigMSPSenderLiveStrategyETAUpdateIntervalThrottle_Metadata_block_invoke_33
- _GEOConfigMSPSenderMinimalStrategyETANearArrivalInterval_Metadata_block_invoke_34
- _GEOConfigMSPSenderMinimalStrategyETAUpdateIntervalThrottle_Metadata_block_invoke_35
- _GEOConfigMSPSenderMinimalStrategyETAUpdateNearArrivalIntervalThrottle_Metadata_block_invoke_36
- _GEOConfigMSPSharedETASenderIdentifier_Metadata_block_invoke_37
- _GEOConfigMSPSharedTripServerEnabled_Metadata_block_invoke_38
- _OBJC_IVAR_$_MSPSharedTripCapabilityLevelFetcher._mapsInfoQueryController
- ___28-[MSPSharedTripService init]_block_invoke.67
- ___47-[MSPSharedTripService _openConnectionIfNeeded]_block_invoke.186
- ___54-[MSPSharedTripService _performBlockAfterInitialSync:]_block_invoke.79
- ___58-[MSPSharedTripServer listener:shouldAcceptNewConnection:]_block_invoke.130
- ___60-[MSPSharedTripCapabilityLevelFetcher _fetchQueuesDidUpdate]_block_invoke.86
- ___60-[MSPSharedTripService _performBlockAfterInitialConnection:]_block_invoke.76
- ___60-[MSPSharedTripService _startSharingWithContact:completion:]_block_invoke.82
- ___60-[MSPSharedTripService _startSharingWithContact:completion:]_block_invoke_2.85
- ___60-[MSPSharedTripService stopAllSharingWithReason:completion:]_block_invoke.96
- ___61-[MSPSharedTripService _stopAllSharingWithReason:completion:]_block_invoke.97
- ___61-[MSPSharedTripService _stopAllSharingWithReason:completion:]_block_invoke_2.98
- ___66-[MSPSharedTripService _stopSharingWithContact:reason:completion:]_block_invoke.94
- ___66-[MSPSharedTripService _stopSharingWithContact:reason:completion:]_block_invoke_2.95
- ___79-[MSPSharedTripService _subscribeToSharedTripUpdatesWithIdentifier:completion:]_block_invoke.127
- ___block_descriptor_40_e8_32s_e17_v16?0"NSTimer"8ls32l8
- ___block_literal_global.100
- ___block_literal_global.109
- ___block_literal_global.123
- ___block_literal_global.131
- ___block_literal_global.138
- ___block_literal_global.145
- ___block_literal_global.152
- ___block_literal_global.159
- ___block_literal_global.166
- ___block_literal_global.171
- ___block_literal_global.176
- ___block_literal_global.183
- ___block_literal_global.188
- ___block_literal_global.195
- ___block_literal_global.202
- ___block_literal_global.209
- ___block_literal_global.216
- ___block_literal_global.221
- ___block_literal_global.78
- ___block_literal_global.89
- ___block_literal_global.95
- ___block_literal_global.97
- _objc_msgSend$fire
- _objc_msgSend$timerWithTimeInterval:repeats:block:
CStrings:
+ "\"!\x13"
+ "%@ - LogDiscard error during BAA authentication: %@"
+ "%@ - LogDiscard for trigger %@"
+ "%@ - LogDiscard succeeded"
+ "/AppleInternal/Library/Frameworks/DeviceIdentity.framework/DeviceIdentity"
+ "/System/Library/Frameworks/DeviceIdentity.framework/DeviceIdentity"
+ "/System/Library/PrivateFrameworks/DeviceIdentity.framework/DeviceIdentity"
+ "@\"<GEOMapServiceFeedbackReportTicket>\""
+ "@\"GEOMapServiceTraits\""
+ "@\"GEOMapServiceTraits\"16@0:8"
+ "@\"GEOPDMerchantInformation\""
+ "@\"GEORPFeedbackRequestParameters\""
+ "@\"GEORPFeedbackUserInfo\""
+ "@120@0:8Q16q24Q32@40@48@56@64@72d80@88{?=dd}96@112"
+ "@40@0:8@16@24q32"
+ "Assertion failed: completion != ((void *)0)"
+ "Assertion failed: dataToSign != ((void *)0)"
+ "BAA service did not return enough certificates"
+ "BAA service did not return enough certificates.  Only returned %lu certificate(s)"
+ "BAACertificateRequest"
+ "Certificate is nil"
+ "Device doesn't support UCRT attestation, use SCRT attestation instead"
+ "DeviceIdentityIssueClientCertificateWithCompletion"
+ "DeviceIdentityUCRTAttestationSupported"
+ "Failed BAA authentication with error %@"
+ "Failed certificate fetch with error %@"
+ "Failed certificate request"
+ "Failed certificate request with error %@"
+ "Failed to create data from certificate at index %lu with error %@"
+ "Failed to receive BAA certificate and signature with error %@"
+ "LOG_DISCARD_TRIGGER_POI_ENRICHMENT"
+ "LOG_DISCARD_TRIGGER_RAP"
+ "LOG_DISCARD_TRIGGER_UNSPECIFIED"
+ "MSPAuthFeedbackReportTicket"
+ "MSPBaseFeedbackReportTicket"
+ "MSPFeedbackReportTicket"
+ "MSPUGCLogDiscardCertificateDurationInMinutesKey"
+ "MSPUGCLogDiscardShouldReuseExistingKeyKey"
+ "MSPUGCShouldCacheBAACertificatesForRAPRequestsKey"
+ "MSPUGCShouldSendNonceInBAACertificateKey"
+ "MSPUGCTimeIntervalToCacheBAACertificatesForRAPRequestsKey"
+ "MSPUnauthFeedbackReportTicket"
+ "MSPWallet"
+ "MSPWalletBankTransactionInformation"
+ "MSPWalletRAP"
+ "MSPWalletRAPReport"
+ "No data to sign"
+ "Nonce data exceeds 32 byte limit.  Nonce data is %lu bytes long"
+ "Received high %{private}llu and low %{private}llu"
+ "T@\"<GEOMapServiceFeedbackReportTicket>\",&,N,V_ticket"
+ "T@\"GEOMapServiceTraits\",R,N"
+ "T@\"GEOMapServiceTraits\",R,N,V_traits"
+ "T@\"GEOPDMerchantInformation\",C,N,V_merchantInformation"
+ "T@\"GEORPFeedbackRequestParameters\",R,N,V_requestParameters"
+ "T@\"GEORPFeedbackUserInfo\",R,N"
+ "T@\"GEOStyleAttributes\",?,R,N"
+ "T@\"NSArray\",C,N,V_otherTransactionLocations"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",C,N,V_bankIdentifier"
+ "T@\"NSString\",C,N,V_bankTransactionDescription"
+ "T@\"NSString\",C,N,V_bankTransactionDescriptionClean"
+ "T@\"NSString\",C,N,V_transactionCurrencyCode"
+ "T@?,C,N,V_willSubmitRequestBlock"
+ "TB,N,V_enableBrandMuidFallback"
+ "TI,?,R,N"
+ "TQ,N"
+ "TQ,N,V_transactionStatus"
+ "TQ,N,V_transactionType"
+ "Td,N,V_transactionTimestamp"
+ "Tq,N,V_industryCode"
+ "Tq,R,N,V_userInfoType"
+ "UGCBAAErrorDomain"
+ "UGCBAAUtilities"
+ "Unable to create signature with error %@"
+ "_bankIdentifier"
+ "_bankTransactionDescription"
+ "_bankTransactionDescriptionClean"
+ "_credentialsForPrimaryICloudAccount"
+ "_dataToSign"
+ "_enableBrandMuidFallback"
+ "_industryCode"
+ "_merchantInformation"
+ "_otherTransactionLocations"
+ "_requestParameters"
+ "_retryAfterBackoff"
+ "_submitWithCallbackQueue:handler:networkActivity:"
+ "_ticket"
+ "_traits"
+ "_transactionCurrencyCode"
+ "_transactionStatus"
+ "_transactionTimestamp"
+ "_transactionType"
+ "_userInfo"
+ "_userInfoType"
+ "_willSubmitRequestBlock"
+ "_workQueue"
+ "addOtherTransactionLocations:"
+ "anonymousUserId"
+ "baaCertificates"
+ "baaSignature"
+ "bankIdentifier"
+ "bankTransactionDescription"
+ "bankTransactionDescriptionClean"
+ "cancel"
+ "captureUgcDeleteWithSignature:certificates:trigger:queue:completion:"
+ "com.apple.Maps.CommunityID"
+ "com.apple.Maps.LogDiscard"
+ "com.apple.Maps.MSPSharedTripCapabilityFetcher"
+ "com.apple.maps.UGCBAACertificateFetching"
+ "comments"
+ "commonCorrections"
+ "context"
+ "correlationId"
+ "dataUsingEncoding:"
+ "details"
+ "enableBrandMuidFallback"
+ "feedbackRequestParameters"
+ "icloudUserPersonId"
+ "industryCode"
+ "initForMerchantIssue:merchantIndustryCode:mapsIdentifier:merchantName:merchantRawName:merchantIndustryCategory:merchantURL:merchantFormattedAddress:transactionTime:transactionType:transactionLocation:bankTransactionInformation:"
+ "initWithFeedbackRequestParameters:traits:userInfoType:"
+ "initWithFeedbackRequestParameters:userInfo:traits:"
+ "initWithMSPWalletBankTransactionInformation:rawMerchantCode:industryCategory:"
+ "initWithMerchantIndustryCode:mapsIdentifier:merchantName:merchantRawName:merchantIndustryCategory:merchantURL:merchantFormattedAddress:transactionTime:transactionType:transactionLocation:merchantBankTransactionInfo:"
+ "initWithSessionID:sessionCreationTime:sequenceNumber:"
+ "isAppleCard"
+ "kMAOptionsBAAKeychainLabel"
+ "kMAOptionsBAANonce"
+ "kMAOptionsBAAOIDHardwareProperties"
+ "kMAOptionsBAAOIDKeyUsageProperties"
+ "kMAOptionsBAAOIDNonce"
+ "kMAOptionsBAAOIDSToInclude"
+ "kMAOptionsBAASCRTAttestation"
+ "kMAOptionsBAAValidity"
+ "kMAOptionsResuseExistingKey"
+ "lookupTransactionType"
+ "mapsUserSessionEntity"
+ "merchantAdamId"
+ "merchantBankTransactionInfo"
+ "merchantInformation"
+ "merchantLookupFeedback"
+ "otherTransactionLocations"
+ "reportersComment"
+ "requestParameters"
+ "requestTransactionType"
+ "sessionID"
+ "sessionUUIDString"
+ "setAnonymisedUserId:"
+ "setAnonymousUserId:"
+ "setBaaCertificates:"
+ "setBaaSignature:"
+ "setBankIdentifier:"
+ "setBankTransactionDescription:"
+ "setBankTransactionDescriptionClean:"
+ "setBankTransactionType:"
+ "setComments:"
+ "setCommonCorrections:"
+ "setCorrections:"
+ "setCorrelationId:"
+ "setEnableBrandMuidFallback:"
+ "setIndustryCategory:"
+ "setIndustryCode:"
+ "setIsAppleCard:"
+ "setIsCategoryIncorrect:"
+ "setIsMerchantIncorrect:"
+ "setIsOtherIssue:"
+ "setLookupTransactionType:"
+ "setMerchantAdamId:"
+ "setMerchantInformation:"
+ "setOtherTransactionLocations:"
+ "setRawMerchantCode:"
+ "setReportersComment:"
+ "setRequestTransactionType:"
+ "setShareSessionWithMaps:"
+ "setTdmUserInfo:"
+ "setTicket:"
+ "setTransactionCurrencyCode:"
+ "setTransactionStatus:"
+ "setTransactionTimestamp:"
+ "setTransactionType:"
+ "setUserCredentials:"
+ "setWillSubmitRequestBlock:"
+ "sharedService"
+ "submissionParameters"
+ "submitWithCallbackQueue:handler:networkActivity:"
+ "submitWithHandler:networkActivity:"
+ "tdmUserInfo"
+ "ticket"
+ "ticketForFeedbackRequest:traits:"
+ "traits"
+ "transactionCurrencyCode"
+ "transactionStatus"
+ "transactionTimestamp"
+ "transactionType"
+ "userCredentials"
+ "userInfoType"
+ "userInfoType can't be None"
+ "v12@?0B8"
+ "v16@?0@\"GEORPFeedbackRequest\"8"
+ "v32@0:8@?<v@?@\"GEORPFeedbackResponse\"@\"NSData\"@\"NSError\">16@?<v@?B>24"
+ "v32@?0@\"GEORPFeedbackResponse\"8@\"NSData\"16@\"NSError\"24"
+ "v32@?0@\"NSArray\"8@\"NSData\"16@\"NSError\"24"
+ "v32@?0^{__SecKey=}8@\"NSArray\"16@\"NSError\"24"
+ "v40@0:8@\"NSObject<OS_dispatch_queue>\"16@?<v@?@\"GEORPFeedbackResponse\"@\"NSData\"@\"NSError\">24@?<v@?B>32"
+ "v40@0:8@16@?24@?32"
+ "willSubmitRequestBlock"
- "@\"IDSIDQueryController\""
- "T@\"GEOStyleAttributes\",R,N"
- "TI,R,N"
- "_mapsInfoQueryController"
- "fire"
- "timerWithTimeInterval:repeats:block:"
- "v16@?0@\"NSTimer\"8"

```
