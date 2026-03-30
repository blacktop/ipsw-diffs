## AppleMediaServices

> `/System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices`

```diff

-9.4.28.2.1
-  __TEXT.__text: 0x7df8d0
+9.5.4.0.0
+  __TEXT.__text: 0x7e4cf8
   __TEXT.__auth_stubs: 0x4cd0
-  __TEXT.__objc_methlist: 0x2369c
-  __TEXT.__const: 0x5f1b0
+  __TEXT.__objc_methlist: 0x23994
+  __TEXT.__const: 0x5f220
   __TEXT.__dlopen_cstrs: 0x933
-  __TEXT.__cstring: 0x2aff8
-  __TEXT.__swift5_typeref: 0x73fb
-  __TEXT.__swift5_reflstr: 0x3ca4
-  __TEXT.__swift5_assocty: 0xfd8
-  __TEXT.__constg_swiftt: 0x5998
+  __TEXT.__cstring: 0x2b468
+  __TEXT.__swift5_typeref: 0x744b
+  __TEXT.__constg_swiftt: 0x59f0
+  __TEXT.__swift5_reflstr: 0x3d24
+  __TEXT.__swift5_fieldmd: 0x533c
   __TEXT.__swift5_builtin: 0x384
-  __TEXT.__swift5_fieldmd: 0x5258
+  __TEXT.__swift5_assocty: 0xfd8
   __TEXT.__swift5_proto: 0x12a8
-  __TEXT.__swift5_types: 0x6ac
-  __TEXT.__swift_as_entry: 0x820
-  __TEXT.__swift_as_ret: 0x9c8
-  __TEXT.__swift5_capture: 0x3b90
+  __TEXT.__swift5_types: 0x6b4
+  __TEXT.__swift5_capture: 0x3ba0
+  __TEXT.__swift_as_entry: 0x824
+  __TEXT.__swift_as_ret: 0x9cc
   __TEXT.__swift5_mpenum: 0x84
   __TEXT.__swift5_protos: 0x108
-  __TEXT.__oslogstring: 0x31f68
-  __TEXT.__gcc_except_tab: 0x5ab4
+  __TEXT.__oslogstring: 0x3247f
+  __TEXT.__gcc_except_tab: 0x5aac
   __TEXT.__ustring: 0x1b2
-  __TEXT.__unwind_info: 0x13c10
-  __TEXT.__eh_frame: 0x185c4
-  __TEXT.__objc_classname: 0x5b69
-  __TEXT.__objc_methname: 0x48705
-  __TEXT.__objc_methtype: 0x928b
-  __TEXT.__objc_stubs: 0x30ec0
+  __TEXT.__unwind_info: 0x13de8
+  __TEXT.__eh_frame: 0x18644
+  __TEXT.__objc_classname: 0x5bc9
+  __TEXT.__objc_methname: 0x48f55
+  __TEXT.__objc_methtype: 0x9306
+  __TEXT.__objc_stubs: 0x312e0
   __DATA_CONST.__got: 0x1b80
-  __DATA_CONST.__const: 0xc948
-  __DATA_CONST.__objc_classlist: 0x1548
+  __DATA_CONST.__const: 0xcaf0
+  __DATA_CONST.__objc_classlist: 0x1558
   __DATA_CONST.__objc_catlist: 0xf8
-  __DATA_CONST.__objc_protolist: 0x460
+  __DATA_CONST.__objc_protolist: 0x468
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xf7a0
-  __DATA_CONST.__objc_protorefs: 0x228
+  __DATA_CONST.__objc_selrefs: 0xf8d0
+  __DATA_CONST.__objc_protorefs: 0x230
   __DATA_CONST.__objc_superrefs: 0xce8
   __DATA_CONST.__objc_arraydata: 0x5f0
   __AUTH_CONST.__auth_got: 0x2680
-  __AUTH_CONST.__const: 0x2e878
-  __AUTH_CONST.__cfstring: 0x22cc0
-  __AUTH_CONST.__objc_const: 0x3de28
+  __AUTH_CONST.__const: 0x2ea78
+  __AUTH_CONST.__cfstring: 0x22f20
+  __AUTH_CONST.__objc_const: 0x3e340
   __AUTH_CONST.__objc_intobj: 0xc90
   __AUTH_CONST.__objc_arrayobj: 0x168
   __AUTH_CONST.__objc_dictobj: 0x118
-  __AUTH.__objc_data: 0x9e68
-  __AUTH.__data: 0x2b38
-  __DATA.__objc_ivar: 0x194c
-  __DATA.__data: 0x7eb8
+  __AUTH.__objc_data: 0xa028
+  __AUTH.__data: 0x2b78
+  __DATA.__objc_ivar: 0x1958
+  __DATA.__data: 0x7e98
   __DATA.__bss: 0x1f690
   __DATA.__common: 0xb68
   __DATA_DIRTY.__objc_ivar: 0x6d8
   __DATA_DIRTY.__objc_data: 0x5b08
-  __DATA_DIRTY.__data: 0x1ef8
+  __DATA_DIRTY.__data: 0x1ef0
   __DATA_DIRTY.__bss: 0x4030
   __DATA_DIRTY.__common: 0x88
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 954A40FE-99C9-33FD-9B19-9D09E9631E1F
-  Functions: 28741
-  Symbols:   56806
-  CStrings:  26162
+  UUID: 8A823C88-4A1B-3D03-9266-3C5A34481F25
+  Functions: 28859
+  Symbols:   57007
+  CStrings:  26282
 
Symbols:
+ +[AMSDefaults allowSensitiveScreenCapture]
+ +[AMSDefaults setAllowSensitiveScreenCapture:]
+ +[AMSKeychainOptions _attestationStyleForLocalAuthSettings]
+ +[AMSKeychainOptions supportsPasscodePurchaseWithAttestationStyle:]
+ +[AMSURLRequestDecoration _treatmentNamespaceOverrideFromConfig:forHost:]
+ +[AMSURLRequestDecoration addTreatmentHeadersToRequest:forTreatmentNamespace:bag:canonicalAccountIdentifierProvider:]
+ +[AMSURLRequestDecoration addTreatmentHeadersToRequest:forTreatmentNamespace:canonicalAccountIdentifierProvider:]
+ -[ACAccount(AppleMediaServices) ams_isLocalBetaAccount]
+ -[ACAccountStore(AppleMediaServices) _createLocaliTunesAccountForAccountType:mediaType:]
+ -[ACAccountStore(AppleMediaServices) _createLocaliTunesAccountForAccountType:mediaType:error:]
+ -[ACAccountStore(AppleMediaServices) _fetchLocalAccountForAccountType:mediaType:error:]
+ -[ACAccountStore(AppleMediaServices) _fetchLocaliTunesAccountForAccountType:mediaType:shouldUpdateStorefront:]
+ -[ACAccountStore(AppleMediaServices_Project) _ams_localiTunesAccountForAccountType:mediaType:error:]
+ -[ACAccountStore(AppleMediaServices_Project) _ams_localiTunesAccountForAccountType:mediaType:shouldUpdateStorefront:]
+ -[AMSAccountManagementService performCreateLocalAccountWithIdentifier:mediaType:]
+ -[AMSAccountManagementService performCreateLocalAccountWithIdentifier:mediaType:error:]
+ -[AMSAccountManagementService performCreateLocalAccountWithType:mediaType:]
+ -[AMSAccountManagementService performCreateLocalAccountWithType:mediaType:error:]
+ -[AMSBuyParams isRedownload]
+ -[AMSEngagementConnection serviceInterfaceForSelector:]
+ -[AMSKeychainOptions attestationModel]
+ -[AMSPaymentSheetRequest authorizingTitle]
+ -[AMSPaymentSheetRequest disablePasswordFallback]
+ -[AMSPaymentSheetRequest setAuthorizingTitle:]
+ -[AMSPaymentSheetRequest setDisablePasswordFallback:]
+ -[AMSProcessInfo setTreatmentCanonicalAccountIdentifierProvider:]
+ -[AMSProcessInfo treatmentCanonicalAccountIdentifierProvider]
+ -[AMSTreatmentStore activeTreatmentsForAreas:canonicalAccountIdentifierProvider:]
+ -[AMSTreatmentStore activeTreatmentsForAreas:userId:canonicalAccountIdentifier:]
+ -[AMSTreatmentStore activeTreatmentsForAreas:userId:canonicalAccountIdentifierProvider:]
+ -[AMSTreatmentStore encodeExperimentDataForTopic:userId:canonicalAccountIdentifier:]
+ -[AMSTreatmentStore experimentDataForAreas:userId:canonicalAccountIdentifier:]
+ -[AMSTreatmentStore treatmentsForAreas:startDate:endDate:userId:canonicalAccountIdentifier:]
+ GCC_except_table137
+ GCC_except_table151
+ GCC_except_table165
+ GCC_except_table84
+ GCC_except_table90
+ GCC_except_table93
+ _AMSBagKeyPaymentHardwareStatusTimeout
+ _AMSBagKeyTreatmentNamespaceOverride
+ _OBJC_CLASS_$_AMSBiometricHeaderNames
+ _OBJC_CLASS_$_AMSPasscodeHeaderNames
+ _OBJC_IVAR_$_AMSPaymentSheetRequest._authorizingTitle
+ _OBJC_IVAR_$_AMSPaymentSheetRequest._disablePasswordFallback
+ _OBJC_IVAR_$_AMSProcessInfo._lock
+ _OBJC_IVAR_$_AMSProcessInfo._treatmentCanonicalAccountIdentifierProvider
+ _OBJC_METACLASS_$_AMSBiometricHeaderNames
+ _OBJC_METACLASS_$_AMSPasscodeHeaderNames
+ _OUTLINED_FUNCTION_208
+ __DATA_AMSBiometricHeaderNames
+ __DATA_AMSPasscodeHeaderNames
+ __INSTANCE_METHODS_AMSBiometricHeaderNames
+ __INSTANCE_METHODS_AMSPasscodeHeaderNames
+ __IVARS_AMSBiometricHeaderNames
+ __IVARS_AMSPasscodeHeaderNames
+ __METACLASS_DATA_AMSBiometricHeaderNames
+ __METACLASS_DATA_AMSPasscodeHeaderNames
+ __OBJC_$_CLASS_METHODS_AMSKeychainOptions(AppleMediaServices)
+ __OBJC_$_INSTANCE_METHODS_AMSKeychainOptions(AppleMediaServices)
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_AMSAccountManagementServiceInterface
+ __PROPERTIES_AMSBiometricHeaderNames
+ __PROPERTIES_AMSPasscodeHeaderNames
+ __PROTOCOLS_AMSBiometricHeaderNames
+ __PROTOCOLS_AMSBiometricHeaderNames.2
+ __PROTOCOLS_AMSPasscodeHeaderNames
+ __PROTOCOLS_AMSPasscodeHeaderNames.7
+ __PROTOCOL_AMSLocalAuthHeaderNames
+ __PROTOCOL_INSTANCE_METHODS_AMSLocalAuthHeaderNames
+ __PROTOCOL_METHOD_TYPES_AMSLocalAuthHeaderNames
+ __PROTOCOL_PROPERTIES_AMSLocalAuthHeaderNames
+ ___110-[ACAccountStore(AppleMediaServices) _fetchLocaliTunesAccountForAccountType:mediaType:shouldUpdateStorefront:]_block_invoke
+ ___110-[ACAccountStore(AppleMediaServices) _fetchLocaliTunesAccountForAccountType:mediaType:shouldUpdateStorefront:]_block_invoke_2
+ ___110-[ACAccountStore(AppleMediaServices) _fetchLocaliTunesAccountForAccountType:mediaType:shouldUpdateStorefront:]_block_invoke_3
+ ___112+[AMSFinancePaymentSheetResponse _flexListDictionaryForValues:styles:account:shouldUppercaseText:designVersion:]_block_invoke.318
+ ___112+[AMSFinancePaymentSheetResponse _flexListDictionaryForValues:styles:account:shouldUppercaseText:designVersion:]_block_invoke.320
+ ___113+[AMSURLRequestDecoration addTreatmentHeadersToRequest:forTreatmentNamespace:canonicalAccountIdentifierProvider:]_block_invoke
+ ___113+[AMSURLRequestDecoration addTreatmentHeadersToRequest:forTreatmentNamespace:canonicalAccountIdentifierProvider:]_block_invoke.42
+ ___113+[AMSURLRequestDecoration addTreatmentHeadersToRequest:forTreatmentNamespace:canonicalAccountIdentifierProvider:]_block_invoke.43
+ ___113+[AMSURLRequestDecoration addTreatmentHeadersToRequest:forTreatmentNamespace:canonicalAccountIdentifierProvider:]_block_invoke.45
+ ___113+[AMSURLRequestDecoration addTreatmentHeadersToRequest:forTreatmentNamespace:canonicalAccountIdentifierProvider:]_block_invoke_2
+ ___113+[AMSURLRequestDecoration addTreatmentHeadersToRequest:forTreatmentNamespace:canonicalAccountIdentifierProvider:]_block_invoke_3
+ ___113+[AMSURLRequestDecoration addTreatmentHeadersToRequest:forTreatmentNamespace:canonicalAccountIdentifierProvider:]_block_invoke_4
+ ___113+[AMSURLRequestDecoration addTreatmentHeadersToRequest:forTreatmentNamespace:canonicalAccountIdentifierProvider:]_block_invoke_5
+ ___117+[AMSURLRequestDecoration addTreatmentHeadersToRequest:forTreatmentNamespace:bag:canonicalAccountIdentifierProvider:]_block_invoke
+ ___117-[ACAccountStore(AppleMediaServices_Project) _ams_localiTunesAccountForAccountType:mediaType:shouldUpdateStorefront:]_block_invoke
+ ___117-[ACAccountStore(AppleMediaServices_Project) _ams_localiTunesAccountForAccountType:mediaType:shouldUpdateStorefront:]_block_invoke_2
+ ___34-[AMSTreatmentStore areasWithIDs:]_block_invoke.65
+ ___36-[AMSTreatmentStore areasForTopics:]_block_invoke.64
+ ___40-[AMSEngagement _handleServiceResponse:]_block_invoke.143
+ ___40-[AMSEngagement _handleServiceResponse:]_block_invoke.149
+ ___40-[AMSEngagement _handleServiceResponse:]_block_invoke.156
+ ___40-[AMSEngagement _handleServiceResponse:]_block_invoke.159
+ ___40-[AMSEngagement _handleServiceResponse:]_block_invoke.162
+ ___40-[AMSEngagement _handleServiceResponse:]_block_invoke.163
+ ___40-[AMSEngagement _handleServiceResponse:]_block_invoke_2.153
+ ___40-[AMSTreatmentStore areasForNamespaces:]_block_invoke.62
+ ___42-[AMSTreatmentStore synchronizeTreatments]_block_invoke.71
+ ___44-[ACAccount(AppleMediaServices) ams_cookies]_block_invoke.192
+ ___50-[AMSEngagement _failAllRunningPromisesWithError:]_block_invoke.138
+ ___56-[AMSBiometricsSignatureTask _performSignatureInProcess]_block_invoke.19
+ ___56-[AMSBiometricsSignatureTask _performSignatureInProcess]_block_invoke.26
+ ___65-[ACAccount(AppleMediaServices) ams_mergePrivacyAcknowledgement:]_block_invoke.274
+ ___70-[ACAccountStore(AppleMediaServices) _updateStorefrontInLocalAccount:]_block_invoke.194
+ ___72-[AMSFinancePaymentSheetResponse performWithTaskInfo:completionHandler:]_block_invoke.300
+ ___76-[ACAccount(AppleMediaServices) ams_cookiesForURL:bag:cleanupGlobalCookies:]_block_invoke.290
+ ___77+[AMSFinancePaymentSheetResponse _attributedListDictionaryForValues:account:]_block_invoke.310
+ ___77+[AMSFinancePaymentSheetResponse _attributedListDictionaryForValues:account:]_block_invoke_2.313
+ ___78-[AMSTreatmentStore experimentDataForAreas:userId:canonicalAccountIdentifier:]_block_invoke
+ ___80-[AMSTreatmentStore activeTreatmentsForAreas:userId:canonicalAccountIdentifier:]_block_invoke
+ ___80-[AMSTreatmentStore activeTreatmentsForAreas:userId:canonicalAccountIdentifier:]_block_invoke_2
+ ___81+[AMSURLRequestDecoration addStoreFrontHeaderToRequest:forAccount:mediaType:bag:]_block_invoke.73
+ ___81-[AMSAccountManagementService performCreateLocalAccountWithIdentifier:mediaType:]_block_invoke
+ ___81-[AMSAccountManagementService performCreateLocalAccountWithIdentifier:mediaType:]_block_invoke.28
+ ___81-[AMSAccountManagementService performCreateLocalAccountWithIdentifier:mediaType:]_block_invoke.29
+ ___81-[AMSAccountManagementService performCreateLocalAccountWithIdentifier:mediaType:]_block_invoke.30
+ ___84-[AMSTreatmentStore encodeExperimentDataForTopic:userId:canonicalAccountIdentifier:]_block_invoke
+ ___84-[AMSTreatmentStore encodeExperimentDataForTopic:userId:canonicalAccountIdentifier:]_block_invoke_2
+ ___85-[AMSFinancePaymentSheetResponse _performPaymentSheetWithTaskInfo:completionHandler:]_block_invoke.337
+ ___87-[ACAccountStore(AppleMediaServices) _fetchLocalAccountForAccountType:mediaType:error:]_block_invoke
+ ___87-[AMSAccountManagementService performCreateLocalAccountWithIdentifier:mediaType:error:]_block_invoke
+ ___87-[AMSAccountManagementService performCreateLocalAccountWithIdentifier:mediaType:error:]_block_invoke.31
+ ___88-[ACAccountStore(AppleMediaServices) _createLocaliTunesAccountForAccountType:mediaType:]_block_invoke
+ ___88-[AMSTreatmentStore activeTreatmentsForAreas:userId:canonicalAccountIdentifierProvider:]_block_invoke
+ ___88-[AMSTreatmentStore activeTreatmentsForAreas:userId:canonicalAccountIdentifierProvider:]_block_invoke_2
+ ___90+[AMSDefaults shouldSampleWithPercentageValue:sessionDurationValue:identifier:completion:]_block_invoke.364
+ ___92-[AMSTreatmentStore treatmentsForAreas:startDate:endDate:userId:canonicalAccountIdentifier:]_block_invoke
+ ___92-[AMSTreatmentStore treatmentsForAreas:startDate:endDate:userId:canonicalAccountIdentifier:]_block_invoke.84
+ ___92-[AMSTreatmentStore treatmentsForAreas:startDate:endDate:userId:canonicalAccountIdentifier:]_block_invoke.87
+ ___92-[AMSTreatmentStore treatmentsForAreas:startDate:endDate:userId:canonicalAccountIdentifier:]_block_invoke.88
+ ___92-[AMSTreatmentStore treatmentsForAreas:startDate:endDate:userId:canonicalAccountIdentifier:]_block_invoke_2
+ ___92-[AMSTreatmentStore treatmentsForAreas:startDate:endDate:userId:canonicalAccountIdentifier:]_block_invoke_3
+ ___block_descriptor_104_e8_32s40s48s56s64s72s80s88s96s_e44_v16?0"<AMSTreatmentStoreServiceProtocol>"8ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8
+ ___block_descriptor_33_e19_B16?0"ACAccount"8l
+ ___block_descriptor_42_e8_32s_e29_"AMSPromise"16?0"NSArray"8ls32l8
+ ___block_descriptor_49_e8_32s40s_e35_"AMSPromise"16?0"ACAccountType"8ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48s_e33_"AMSPromise"16?0"AMSOptional"8ls32l8s40l8s48l8
+ ___block_descriptor_57_e8_32s40s48s_e29_"AMSPromise"16?0"NSError"8ls32l8s40l8s48l8
+ ___block_descriptor_57_e8_32s40s48s_e30_"AMSPromise"16?0"NSNumber"8ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48bs_e46_"AMSPromise"24?0"NSDictionary"8"NSError"16ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56s_e34_"AMSPromise"16?0"NSDictionary"8ls32l8s40l8s48l8s56l8
+ ___block_descriptor_72_e8_32s40s48s56bs_e46_"AMSPromise"24?0"NSDictionary"8"NSError"16ls32l8s40l8s48l8s56l8
+ ___block_descriptor_72_e8_32s40s48s56s_e42_"AMSPromise"24?0"NSNumber"8"NSError"16ls32l8s40l8s48l8s56l8
+ ___block_descriptor_80_e8_32s40s48s56s64s72r_e78_"AMSBinaryPromise"24?0"<AMSAccountManagementServiceInterface>"8"NSError"16ls32l8r72l8s40l8s48l8s56l8s64l8
+ ___block_literal_global.146
+ ___block_literal_global.168
+ ___block_literal_global.179
+ ___block_literal_global.184
+ ___block_literal_global.210
+ ___block_literal_global.248
+ ___block_literal_global.317
+ ___block_literal_global.321
+ ___block_literal_global.323
+ ___block_literal_global.324
+ ___block_literal_global.342
+ ___block_literal_global.343
+ ___block_literal_global.350
+ ___block_literal_global.354
+ ___block_literal_global.356
+ ___block_literal_global.358
+ ___block_literal_global.366
+ ___block_literal_global.367
+ ___block_literal_global.368
+ ___block_literal_global.87
+ _getSSSilentEnrollmentContextClass
+ _objc_msgSend$_ams_localiTunesAccountForAccountType:mediaType:error:
+ _objc_msgSend$_ams_localiTunesAccountForAccountType:mediaType:shouldUpdateStorefront:
+ _objc_msgSend$_attestationStyleForLocalAuthSettings
+ _objc_msgSend$_createLocaliTunesAccountForAccountType:mediaType:
+ _objc_msgSend$_createLocaliTunesAccountForAccountType:mediaType:error:
+ _objc_msgSend$_fetchLocalAccountForAccountType:mediaType:error:
+ _objc_msgSend$_fetchLocaliTunesAccountForAccountType:mediaType:shouldUpdateStorefront:
+ _objc_msgSend$_treatmentNamespaceOverrideFromConfig:forHost:
+ _objc_msgSend$activeTreatmentsForAreas:canonicalAccountIdentifierProvider:
+ _objc_msgSend$activeTreatmentsForAreas:userId:canonicalAccountIdentifier:
+ _objc_msgSend$activeTreatmentsForAreas:userId:canonicalAccountIdentifierProvider:
+ _objc_msgSend$addTreatmentHeadersToRequest:forTreatmentNamespace:bag:canonicalAccountIdentifierProvider:
+ _objc_msgSend$addTreatmentHeadersToRequest:forTreatmentNamespace:canonicalAccountIdentifierProvider:
+ _objc_msgSend$ams_fetchMethodOfVerificationWithTimeout:returningStaleData:
+ _objc_msgSend$ams_isLocalBetaAccount
+ _objc_msgSend$attestationModel
+ _objc_msgSend$attestationStyleSupportsBOP:
+ _objc_msgSend$authorizingTitle
+ _objc_msgSend$disablePasswordFallback
+ _objc_msgSend$encodeExperimentDataForTopic:userId:canonicalAccountIdentifier:
+ _objc_msgSend$experimentDataForAreas:userId:canonicalAccountIdentifier:
+ _objc_msgSend$headerNamesFor:
+ _objc_msgSend$isPasscodePurchaseEnabled
+ _objc_msgSend$performCreateLocalAccountWithIdentifier:mediaType:
+ _objc_msgSend$performCreateLocalAccountWithIdentifier:mediaType:completion:
+ _objc_msgSend$performCreateLocalAccountWithIdentifier:mediaType:error:
+ _objc_msgSend$performCreateLocalAccountWithType:mediaType:
+ _objc_msgSend$performCreateLocalAccountWithType:mediaType:error:
+ _objc_msgSend$serviceInterfaceForSelector:
+ _objc_msgSend$setAuthorizingTitle:
+ _objc_msgSend$setDisablePasswordFallback:
+ _objc_msgSend$setLocalizedAuthorizingTitle:
+ _objc_msgSend$setTreatmentCanonicalAccountIdentifierProvider:
+ _objc_msgSend$signatureVersion
+ _objc_msgSend$treatmentCanonicalAccountIdentifierProvider
+ _objc_msgSend$treatmentsForAreas:cachePolicy:startDate:endDate:canonicalAccountIdentifier:completion:
+ _objc_msgSend$treatmentsForAreas:startDate:endDate:userId:canonicalAccountIdentifier:
+ _symbolic $s18AppleMediaServices20LocalAuthHeaderNamesP
+ _symbolic So8NSStringCSgIeyBy_
+ _symbolic _____ 18AppleMediaServices19PasscodeHeaderNamesC
+ _symbolic _____ 18AppleMediaServices20BiometricHeaderNamesC
+ _symbolic _____ So20AMSServerTokenActionV
- +[AMSURLRequestDecoration addTreatmentHeadersToRequest:forTreatmentNamespace:]
- -[AMSTreatmentStore treatmentsForAreas:startDate:endDate:userId:]
- GCC_except_table136
- GCC_except_table142
- GCC_except_table164
- GCC_except_table80
- GCC_except_table86
- GCC_except_table89
- GCC_except_table92
- _OBJC_IVAR_$_AMSProcessInfo._internalQueue
- _OUTLINED_FUNCTION_207
- __OBJC_$_CLASS_METHODS_AMSKeychainOptions
- __OBJC_$_INSTANCE_METHODS_AMSKeychainOptions
- __OBJC_$_PROP_LIST_AMSKeychainOptions
- ___112+[AMSFinancePaymentSheetResponse _flexListDictionaryForValues:styles:account:shouldUppercaseText:designVersion:]_block_invoke.315
- ___112+[AMSFinancePaymentSheetResponse _flexListDictionaryForValues:styles:account:shouldUppercaseText:designVersion:]_block_invoke.317
- ___31-[AMSProcessInfo partnerHeader]_block_invoke
- ___34-[AMSTreatmentStore areasWithIDs:]_block_invoke.62
- ___35-[AMSProcessInfo setPartnerHeader:]_block_invoke
- ___36-[AMSTreatmentStore areasForTopics:]_block_invoke.61
- ___40-[AMSEngagement _handleServiceResponse:]_block_invoke.164
- ___40-[AMSEngagement _handleServiceResponse:]_block_invoke.170
- ___40-[AMSEngagement _handleServiceResponse:]_block_invoke.177
- ___40-[AMSEngagement _handleServiceResponse:]_block_invoke.180
- ___40-[AMSEngagement _handleServiceResponse:]_block_invoke.183
- ___40-[AMSEngagement _handleServiceResponse:]_block_invoke.184
- ___40-[AMSEngagement _handleServiceResponse:]_block_invoke_2.174
- ___40-[AMSTreatmentStore areasForNamespaces:]_block_invoke.59
- ___42-[AMSTreatmentStore synchronizeTreatments]_block_invoke.68
- ___44-[ACAccount(AppleMediaServices) ams_cookies]_block_invoke.186
- ___50-[AMSEngagement _failAllRunningPromisesWithError:]_block_invoke.159
- ___51-[AMSTreatmentStore experimentDataForAreas:userId:]_block_invoke
- ___53-[AMSTreatmentStore activeTreatmentsForAreas:userId:]_block_invoke
- ___53-[AMSTreatmentStore activeTreatmentsForAreas:userId:]_block_invoke_2
- ___56-[AMSBiometricsSignatureTask _performSignatureInProcess]_block_invoke.16
- ___56-[AMSBiometricsSignatureTask _performSignatureInProcess]_block_invoke.23
- ___57-[AMSTreatmentStore encodeExperimentDataForTopic:userId:]_block_invoke
- ___57-[AMSTreatmentStore encodeExperimentDataForTopic:userId:]_block_invoke_2
- ___65-[ACAccount(AppleMediaServices) ams_mergePrivacyAcknowledgement:]_block_invoke.271
- ___65-[AMSTreatmentStore treatmentsForAreas:startDate:endDate:userId:]_block_invoke
- ___65-[AMSTreatmentStore treatmentsForAreas:startDate:endDate:userId:]_block_invoke.73
- ___65-[AMSTreatmentStore treatmentsForAreas:startDate:endDate:userId:]_block_invoke.78
- ___65-[AMSTreatmentStore treatmentsForAreas:startDate:endDate:userId:]_block_invoke.80
- ___65-[AMSTreatmentStore treatmentsForAreas:startDate:endDate:userId:]_block_invoke_2
- ___65-[AMSTreatmentStore treatmentsForAreas:startDate:endDate:userId:]_block_invoke_2.79
- ___65-[AMSTreatmentStore treatmentsForAreas:startDate:endDate:userId:]_block_invoke_3
- ___70-[ACAccountStore(AppleMediaServices) _updateStorefrontInLocalAccount:]_block_invoke.180
- ___72-[AMSFinancePaymentSheetResponse performWithTaskInfo:completionHandler:]_block_invoke.297
- ___76-[ACAccount(AppleMediaServices) ams_cookiesForURL:bag:cleanupGlobalCookies:]_block_invoke.287
- ___77+[AMSFinancePaymentSheetResponse _attributedListDictionaryForValues:account:]_block_invoke.307
- ___77+[AMSFinancePaymentSheetResponse _attributedListDictionaryForValues:account:]_block_invoke_2.310
- ___78+[AMSURLRequestDecoration addTreatmentHeadersToRequest:forTreatmentNamespace:]_block_invoke
- ___78+[AMSURLRequestDecoration addTreatmentHeadersToRequest:forTreatmentNamespace:]_block_invoke.33
- ___78+[AMSURLRequestDecoration addTreatmentHeadersToRequest:forTreatmentNamespace:]_block_invoke.34
- ___78+[AMSURLRequestDecoration addTreatmentHeadersToRequest:forTreatmentNamespace:]_block_invoke.36
- ___78+[AMSURLRequestDecoration addTreatmentHeadersToRequest:forTreatmentNamespace:]_block_invoke_2
- ___78+[AMSURLRequestDecoration addTreatmentHeadersToRequest:forTreatmentNamespace:]_block_invoke_3
- ___78+[AMSURLRequestDecoration addTreatmentHeadersToRequest:forTreatmentNamespace:]_block_invoke_4
- ___78+[AMSURLRequestDecoration addTreatmentHeadersToRequest:forTreatmentNamespace:]_block_invoke_5
- ___81+[AMSURLRequestDecoration addStoreFrontHeaderToRequest:forAccount:mediaType:bag:]_block_invoke.64
- ___85-[AMSFinancePaymentSheetResponse _performPaymentSheetWithTaskInfo:completionHandler:]_block_invoke.334
- ___90+[AMSDefaults shouldSampleWithPercentageValue:sessionDurationValue:identifier:completion:]_block_invoke.361
- ___block_descriptor_41_e8_32s_e35_"AMSPromise"16?0"ACAccountType"8ls32l8
- ___block_descriptor_56_e8_32s40s48r_e5_v8?0ls32l8s40l8r48l8
- ___block_descriptor_64_e8_32s40s48s_e42_"AMSPromise"24?0"NSNumber"8"NSError"16ls32l8s40l8s48l8
- ___block_descriptor_96_e8_32s40s48s56s64s72s80s88s_e44_v16?0"<AMSTreatmentStoreServiceProtocol>"8ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8
- ___block_literal_global.167
- ___block_literal_global.170
- ___block_literal_global.189
- ___block_literal_global.197
- ___block_literal_global.200
- ___block_literal_global.203
- ___block_literal_global.204
- ___block_literal_global.208
- ___block_literal_global.242
- ___block_literal_global.299
- ___block_literal_global.301
- ___block_literal_global.303
- ___block_literal_global.306
- ___block_literal_global.337
- ___block_literal_global.338
- ___block_literal_global.339
- ___block_literal_global.347
- ___block_literal_global.351
- ___block_literal_global.353
- ___block_literal_global.355
- ___block_literal_global.363
- ___block_literal_global.364
- ___block_literal_global.365
- ___block_literal_global.51
- _objc_msgSend$activeTreatmentsForAreas:userId:
- _objc_msgSend$addTreatmentHeadersToRequest:forTreatmentNamespace:
- _objc_msgSend$ams_localiTunesAccountForAccountType:error:
- _objc_msgSend$treatmentsForAreas:startDate:endDate:userId:
- _symbolic _____ So24AMSServerBiometricActionV
CStrings:
+ "%@ Account Not Found"
+ "%{public}@: [%{public}@] Fetching treatments (areas: %{public}@, userId: %{public}@, canonicalAccountIdentifier: %{public}@)"
+ "%{public}@: [%{public}@] Silent-enrollment payment session failed due to missing payment session URL bag key."
+ "%{public}@: [%{public}@] userId and canonicalAccountIdentifier are mutually exclusive but both were provided."
+ "%{public}@Bag misconfiguration: '%{public}@' expected a non-empty string, found %{public}@ in %{public}@ rule"
+ "%{public}@Bag misconfiguration: '%{public}@' expected an array, found %{public}@ in %{public}@"
+ "%{public}@Bag misconfiguration: '%{public}@' expected an array, found %{public}@ in %{public}@ rule"
+ "%{public}@Bag misconfiguration: hostSuffix entry is empty in %{public}@ rule"
+ "%{public}@Bag misconfiguration: hostSuffix entry is not a string in %{public}@ rule"
+ "%{public}@Bag misconfiguration: rule entry is not a dictionary in %{public}@"
+ "%{public}@Failed to load %{public}@ from bag. Treatment headers won't be added. error = %{public}@"
+ "%{public}@Local account creation finished with success: %{public}@ (legacy path)"
+ "%{public}@Local account requested with identifier: %{public}@ | mediaType: %{public}@"
+ "%{public}@Using bag-driven treatment namespace override: %{public}@ (default was: %{public}@)"
+ "%{public}@_treatmentNamespaceOverrideFromConfig called with nil config"
+ "%{public}@_treatmentNamespaceOverrideFromConfig called with nil host"
+ "AMSAllowSensitiveScreenCapture"
+ "AMSBiometricHeaderNames"
+ "AMSLocalAuthHeaderNames"
+ "AMSPasscodeHeaderNames"
+ "AutoAccountCreationAgeBasedVerification"
+ "AutoExistingValidCardOnFile"
+ "Beta local"
+ "BetaLocalAccount"
+ "Biometrics signature unavailable"
+ "ExplicitAddCardInASEStack"
+ "ExplicitApplePayCardOnDevice"
+ "ExplicitCardInWallet"
+ "ExplicitEmailVerification"
+ "ExplicitIdInWallet"
+ "ExplicitIdVerification"
+ "ExplicitVerifyCardInASEStack"
+ "ExplicitVerifyCardWithoutAddInStack"
+ "ExplicitVerifyCardZipOnlyWithoutAddInStack"
+ "ImplicitAddCreditCardInWallet"
+ "ImplicitAddCreditCardOnFileInAse"
+ "ImplicitVerifyCardInAseStack"
+ "Local"
+ "T@\"<AMSLocalAuthHeaderNames>\",N,R"
+ "T@\"NSString\",C,N,V_authorizingTitle"
+ "T@?,C,N"
+ "TB,N,V_disablePasswordFallback"
+ "TB,R,N,Gams_isLocalBetaAccount"
+ "The %@ account doesn't exist."
+ "_ams_localiTunesAccountForAccountType:mediaType:error:"
+ "_ams_localiTunesAccountForAccountType:mediaType:shouldUpdateStorefront:"
+ "_attestationStyleForLocalAuthSettings"
+ "_authorizingTitle"
+ "_createLocaliTunesAccountForAccountType:mediaType:"
+ "_createLocaliTunesAccountForAccountType:mediaType:error:"
+ "_disablePasswordFallback"
+ "_fetchLocalAccountForAccountType:mediaType:error:"
+ "_fetchLocaliTunesAccountForAccountType:mediaType:shouldUpdateStorefront:"
+ "_treatmentCanonicalAccountIdentifierProvider"
+ "_treatmentNamespaceOverrideFromConfig:forHost:"
+ "activeTreatmentsForAreas:canonicalAccountIdentifierProvider:"
+ "activeTreatmentsForAreas:userId:canonicalAccountIdentifier:"
+ "activeTreatmentsForAreas:userId:canonicalAccountIdentifierProvider:"
+ "addTreatmentHeadersToRequest:forTreatmentNamespace:bag:canonicalAccountIdentifierProvider:"
+ "addTreatmentHeadersToRequest:forTreatmentNamespace:canonicalAccountIdentifierProvider:"
+ "allowSensitiveScreenCapture"
+ "ams_isLocalBetaAccount"
+ "ams_localBetaAccount"
+ "attestationModel"
+ "attestationStyleSupportsBOP:"
+ "authorizingTitle"
+ "biometricWithPasscode"
+ "com.apple.AppleMediaServices.cert.X509.BOP.client.primary"
+ "com.apple.AppleMediaServices.cert.X509.BOP.primary"
+ "disablePasswordFallback"
+ "encodeExperimentDataForTopic:userId:canonicalAccountIdentifier:"
+ "enterPasscodePressed"
+ "experimentDataForAreas:userId:canonicalAccountIdentifier:"
+ "governmentIDVerified"
+ "headerNames"
+ "headerNamesFor:"
+ "hostMatchingRules"
+ "hostSuffixes"
+ "kAuthorizingTitle"
+ "kDisablePasswordFallback"
+ "local-beta"
+ "paymentHardwareStatusTimeout"
+ "performCreateLocalAccountWithIdentifier:mediaType:"
+ "performCreateLocalAccountWithIdentifier:mediaType:completion:"
+ "performCreateLocalAccountWithIdentifier:mediaType:error:"
+ "performCreateLocalAccountWithType:mediaType:"
+ "performCreateLocalAccountWithType:mediaType:error:"
+ "seed"
+ "serviceInterfaceForSelector:"
+ "setAllowSensitiveScreenCapture:"
+ "setAuthorizingTitle:"
+ "setDisablePasswordFallback:"
+ "setLocalizedAuthorizingTitle:"
+ "setTreatmentCanonicalAccountIdentifierProvider:"
+ "signatureVersion"
+ "supportsBOP"
+ "supportsPasscodePurchaseWithAttestationStyle:"
+ "treatmentCanonicalAccountIdentifierProvider"
+ "treatmentNamespaceOverride"
+ "treatmentsForAreas:cachePolicy:startDate:endDate:canonicalAccountIdentifier:completion:"
+ "treatmentsForAreas:startDate:endDate:userId:canonicalAccountIdentifier:"
+ "userId and canonicalAccountIdentifier are mutually exclusive but both were provided"
+ "v16@?0@?<v@?@\"NSString\">8"
+ "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?B@\"NSError\">32"
- "%{public}@: [%{public}@] Fetching treatments (areas: %{public}@, userId: %{public}@)"
- "<private>"
- "addTreatmentHeadersToRequest:forTreatmentNamespace:"
- "com.apple.AppleMediaServices.AMSClientInfo"
- "treatmentsForAreas:startDate:endDate:userId:"

```
