## AppleMediaServices

> `/System/Library/PrivateFrameworks/AppleMediaServices.framework/Versions/A/AppleMediaServices`

```diff

-10.0.52.0.0
-  __TEXT.__text: 0x8eddcc
+10.0.60.1.3
+  __TEXT.__text: 0x8ee3e4
   __TEXT.__lazy_helpers: 0x2e98
-  __TEXT.__objc_methlist: 0x23d04
-  __TEXT.__const: 0xba328
+  __TEXT.__objc_methlist: 0x23ea4
+  __TEXT.__const: 0xba548
   __TEXT.__dlopen_cstrs: 0x834
-  __TEXT.__cstring: 0x2baea
-  __TEXT.__swift5_typeref: 0x75a9
-  __TEXT.__swift5_reflstr: 0x3ef3
-  __TEXT.__swift5_assocty: 0xf60
-  __TEXT.__constg_swiftt: 0x5a18
+  __TEXT.__cstring: 0x2bbe9
+  __TEXT.__swift5_typeref: 0x75f7
+  __TEXT.__constg_swiftt: 0x5a54
   __TEXT.__swift5_builtin: 0x3d4
-  __TEXT.__swift5_fieldmd: 0x55c0
-  __TEXT.__swift5_proto: 0x11f8
-  __TEXT.__swift5_types: 0x6dc
-  __TEXT.__swift_as_entry: 0x89c
-  __TEXT.__swift_as_ret: 0xa04
-  __TEXT.__swift_as_cont: 0x1318
-  __TEXT.__swift5_capture: 0x3f7c
+  __TEXT.__swift5_reflstr: 0x3f13
+  __TEXT.__swift5_fieldmd: 0x55f8
+  __TEXT.__swift5_assocty: 0xfc0
+  __TEXT.__swift5_proto: 0x120c
+  __TEXT.__swift5_types: 0x6e4
+  __TEXT.__swift_as_entry: 0x88c
+  __TEXT.__swift_as_ret: 0x9f4
+  __TEXT.__swift_as_cont: 0x12f4
+  __TEXT.__swift5_capture: 0x3f24
   __TEXT.__swift5_mpenum: 0x8c
   __TEXT.__swift5_protos: 0x118
-  __TEXT.__oslogstring: 0x30d08
-  __TEXT.__gcc_except_tab: 0x5260
+  __TEXT.__oslogstring: 0x30df1
+  __TEXT.__gcc_except_tab: 0x52a0
   __TEXT.__ustring: 0x210
-  __TEXT.__unwind_info: 0x12ab8
-  __TEXT.__eh_frame: 0x17b2c
+  __TEXT.__unwind_info: 0x12ed8
+  __TEXT.__eh_frame: 0x17640
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x5c88
-  __DATA_CONST.__objc_classlist: 0x1598
+  __DATA_CONST.__const: 0x5c98
+  __DATA_CONST.__objc_classlist: 0x15a0
   __DATA_CONST.__objc_catlist: 0xe0
-  __DATA_CONST.__objc_protolist: 0x488
+  __DATA_CONST.__objc_protolist: 0x490
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xf9c8
+  __DATA_CONST.__objc_selrefs: 0xfb08
   __DATA_CONST.__objc_protorefs: 0x258
   __DATA_CONST.__objc_superrefs: 0xcf8
   __DATA_CONST.__objc_arraydata: 0x498
-  __DATA_CONST.__got: 0x19c8
-  __AUTH_CONST.__const: 0x44430
-  __AUTH_CONST.__cfstring: 0x23020
-  __AUTH_CONST.__objc_const: 0x3eff8
+  __DATA_CONST.__got: 0x19d8
+  __AUTH_CONST.__const: 0x44510
+  __AUTH_CONST.__cfstring: 0x230a0
+  __AUTH_CONST.__objc_const: 0x3f220
   __AUTH_CONST.__lazy_load_got: 0x460
   __AUTH_CONST.__objc_intobj: 0xc30
   __AUTH_CONST.__objc_arrayobj: 0x180
   __AUTH_CONST.__objc_dictobj: 0x78
-  __AUTH_CONST.__auth_got: 0x2388
-  __AUTH.__objc_data: 0x9b18
-  __AUTH.__data: 0x2bb8
-  __DATA.__objc_ivar: 0x1a24
-  __DATA.__data: 0x7b64
-  __DATA.__bss: 0x1bb58
+  __AUTH_CONST.__auth_got: 0x2398
+  __AUTH.__objc_data: 0x9b68
+  __AUTH.__data: 0x2bd8
+  __DATA.__objc_ivar: 0x1a30
+  __DATA.__data: 0x7c74
+  __DATA.__bss: 0x1bdd8
   __DATA.__common: 0x1520
   __DATA_DIRTY.__objc_ivar: 0x6c8
-  __DATA_DIRTY.__objc_data: 0x5b00
-  __DATA_DIRTY.__data: 0x2e60
-  __DATA_DIRTY.__bss: 0x6390
+  __DATA_DIRTY.__objc_data: 0x5b08
+  __DATA_DIRTY.__data: 0x2e50
+  __DATA_DIRTY.__bss: 0x63b0
   __DATA_DIRTY.__common: 0x88
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/Versions/A/CFNetwork

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 29068
-  Symbols:   32032
-  CStrings:  8789
+  Functions: 29132
+  Symbols:   32122
+  CStrings:  8798
 
Symbols:
+ +[AMSBagNetworkTask _expirationDateForInterval:now:]
+ +[AMSBagNetworkTask _selectedStorefrontForResponseStorefront:queryItems:]
+ +[AMSBagNetworkTask _shouldRetryForStorefrontChangeWithRequestStorefront:responseStorefront:]
+ +[AMSBiometrics _nonKeyHeadersWithAccount:descriptor:state:signatureResult:]
+ +[AMSBiometrics _publicKeyHeadersWithAccount:descriptor:options:signatureResult:]
+ +[AMSBiometrics identitySource]
+ +[AMSBiometrics setIdentitySource:]
+ +[AMSCardEnrollment shouldSkipCardEnrollmentForWalletBiometricsCheck:walletBiometricsEnabled:]
+ +[AMSDefaults metricsInternalLegacyRoutingPercentage]
+ +[AMSDefaults saveSelfieDiagnostics]
+ +[AMSDefaults setMetricsInternalLegacyRoutingPercentage:]
+ +[AMSDefaults setSaveSelfieDiagnostics:]
+ +[AMSFinancePaymentSheetResponse _credentialAccountForPaymentAccount:]
+ +[AMSProcessInfo attributionBundleIdentifierForProxyAppBundleID:hasImpersonateEntitlement:]
+ +[AMSProcessInfo hasNetworkImpersonationEntitlement]
+ +[AMSURLSession _defaultConfiguration]
+ +[AMSURLSession sessionForAttributedBundleIdentifier:]
+ -[AMSAuthenticateOptions setSuppressOtherMediaTypeStorefrontSync:]
+ -[AMSAuthenticateOptions suppressOtherMediaTypeStorefrontSync]
+ -[AMSAuthenticateTask _signIntoMediaTypes:withVerifiedAccount:authenticationResults:]
+ -[AMSAuthenticateTask _signIntoOtherMediaTypesWithVerifiedAccount:authenticationResults:]
+ -[AMSBagNetworkTask _bagURLSession]
+ -[AMSBagNetworkTask _promiseResultForURLResult:error:queryItems:responseStorefront:account:]
+ -[AMSEngagementRequest setShouldRunCampaignAttribution:]
+ -[AMSEngagementRequest shouldRunCampaignAttribution]
+ -[AMSLiveBiometricIdentitySource identities]
+ -[AMSPaymentSheetPerformanceMetrics pageUserInteractiveTime]
+ -[AMSPaymentSheetPerformanceMetrics setPageUserInteractiveTime:]
+ -[AMSProcessInfo networkAttributionBundleIdentifier]
+ -[NSMutableURLRequest(AppleMediaServices) _ams_removeIdentifierCookies:forAccounts:]
+ -[NSMutableURLRequest(AppleMediaServices) ams_addCookiesAsynchronouslyForAccount:clientInfo:bag:cleanupGlobalCookies:excludeAccountIdentifierCookies:]
+ -[NSMutableURLRequest(AppleMediaServices) ams_addCookiesForAccount:clientInfo:bag:cleanupGlobalCookies:excludeAccountIdentifierCookies:]
+ -[NSURLSessionConfiguration(AppleMediaServices_Project) ams_attributeNetworkingToBundleIdentifier:]
+ GCC_except_table112
+ GCC_except_table139
+ GCC_except_table148
+ GCC_except_table178
+ GCC_except_table61
+ GCC_except_table67
+ GCC_except_table82
+ GCC_except_table89
+ GCC_except_table95
+ GCC_except_table98
+ OBJC_IVAR_$_AMSAuthenticateOptions._suppressOtherMediaTypeStorefrontSync
+ OBJC_IVAR_$_AMSEngagementRequest._shouldRunCampaignAttribution
+ OBJC_IVAR_$_AMSPaymentSheetPerformanceMetrics._pageUserInteractiveTime
+ _OBJC_CLASS_$_AMSLiveBiometricIdentitySource
+ _OBJC_CLASS_$_AMSLocalAuthHeaderDescriptor
+ _OBJC_CLASS_$_RBSAcquisitionCompletionAttribute
+ _OBJC_METACLASS_$_AMSLiveBiometricIdentitySource
+ _OBJC_METACLASS_$_AMSLocalAuthHeaderDescriptor
+ __150-[NSMutableURLRequest(AppleMediaServices) ams_addCookiesAsynchronouslyForAccount:clientInfo:bag:cleanupGlobalCookies:excludeAccountIdentifierCookies:]_block_invoke
+ __150-[NSMutableURLRequest(AppleMediaServices) ams_addCookiesAsynchronouslyForAccount:clientInfo:bag:cleanupGlobalCookies:excludeAccountIdentifierCookies:]_block_invoke_2
+ __67+[AMSBiometrics headersPromiseWithAccount:options:signatureResult:]_block_invoke
+ __DATA_AMSLocalAuthHeaderDescriptor
+ __INSTANCE_METHODS_AMSLocalAuthHeaderDescriptor
+ __IVARS_AMSLocalAuthHeaderDescriptor
+ __METACLASS_DATA_AMSLocalAuthHeaderDescriptor
+ __OBJC_$_INSTANCE_METHODS_AMSLiveBiometricIdentitySource
+ __OBJC_$_PROP_LIST_AMSLiveBiometricIdentitySource
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AMSBiometricIdentitySource
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AMSBiometricIdentitySource
+ __OBJC_$_PROTOCOL_REFS_AMSBiometricIdentitySource
+ __OBJC_CLASS_PROTOCOLS_$_AMSLiveBiometricIdentitySource
+ __OBJC_CLASS_RO_$_AMSLiveBiometricIdentitySource
+ __OBJC_LABEL_PROTOCOL_$_AMSBiometricIdentitySource
+ __OBJC_METACLASS_RO_$_AMSLiveBiometricIdentitySource
+ __OBJC_PROTOCOL_$_AMSBiometricIdentitySource
+ __PROPERTIES_AMSLocalAuthHeaderDescriptor
+ ___150-[NSMutableURLRequest(AppleMediaServices) ams_addCookiesAsynchronouslyForAccount:clientInfo:bag:cleanupGlobalCookies:excludeAccountIdentifierCookies:]_block_invoke
+ ___150-[NSMutableURLRequest(AppleMediaServices) ams_addCookiesAsynchronouslyForAccount:clientInfo:bag:cleanupGlobalCookies:excludeAccountIdentifierCookies:]_block_invoke_2
+ ___67+[AMSBiometrics headersPromiseWithAccount:options:signatureResult:]_block_invoke_2
+ ___85-[AMSAuthenticateTask _signIntoMediaTypes:withVerifiedAccount:authenticationResults:]_block_invoke
+ ___block_descriptor_41_e8_32w_e43_v24?0"AMSAuthenticateResult"8"NSError"16l
+ ___block_descriptor_48_e8_32s40s_e40_"AMSPromise"16?0"AMSKeychainOptions"8l
+ ___block_descriptor_49_e8_32s40s_e31_v24?0"ACAccount"8"NSError"16l
+ ___block_descriptor_49_e8_32s40s_e41_"AMSPromise"24?0"NSArray"8"NSError"16l
+ ___block_descriptor_49_e8_32s40s_e44_v24?0"AMSAuthKitUpdateResult"8"NSError"16l
+ ___block_descriptor_57_e8_32s40s48s_e30_v16?0"AMSAuthKitUpdateTask"8l
+ ___block_descriptor_58_e8_32s40s_e29_"AMSPromise"16?0"NSArray"8l
+ ___block_descriptor_72_e8_32s40s48s56s64s_e55_"AMSPromise"24?0"AMSAuthenticateResult"8"NSError"16l
+ ___block_descriptor_72_e8_32s40s48s56s_e32_"AMSPromise"24?08"NSError"16l
+ ___block_descriptor_80_e8_32s40s48s56s64s_e35_"AMSPromise"16?0"AMSURLRequest"8l
+ ___block_descriptor_80_e8_32s40s48s56s64s_e46_"AMSPromise"24?0"AMSURLResult"8"NSError"16l
+ _associated conformance 18AppleMediaServices21LocalAuthHeaderFieldsVs10SetAlgebraAASQ
+ _associated conformance 18AppleMediaServices21LocalAuthHeaderFieldsVs10SetAlgebraAAs25ExpressibleByArrayLiteral
+ _associated conformance 18AppleMediaServices21LocalAuthHeaderFieldsVs9OptionSetAASY
+ _associated conformance 18AppleMediaServices21LocalAuthHeaderFieldsVs9OptionSetAAs0I7Algebra
+ _flat unique So23AMSLocalAuthHeaderNames_p
+ _objc_msgSend$_ams_removeIdentifierCookies:forAccounts:
+ _objc_msgSend$_bagURLSession
+ _objc_msgSend$_credentialAccountForPaymentAccount:
+ _objc_msgSend$_defaultConfiguration
+ _objc_msgSend$_expirationDateForInterval:now:
+ _objc_msgSend$_nonKeyHeadersWithAccount:descriptor:state:signatureResult:
+ _objc_msgSend$_promiseResultForURLResult:error:queryItems:responseStorefront:account:
+ _objc_msgSend$_publicKeyHeadersWithAccount:descriptor:options:signatureResult:
+ _objc_msgSend$_selectedStorefrontForResponseStorefront:queryItems:
+ _objc_msgSend$_shouldRetryForStorefrontChangeWithRequestStorefront:responseStorefront:
+ _objc_msgSend$_signIntoMediaTypes:withVerifiedAccount:authenticationResults:
+ _objc_msgSend$_signIntoOtherMediaTypesWithVerifiedAccount:authenticationResults:
+ _objc_msgSend$ams_addCookiesAsynchronouslyForAccount:clientInfo:bag:cleanupGlobalCookies:excludeAccountIdentifierCookies:
+ _objc_msgSend$ams_addCookiesForAccount:clientInfo:bag:cleanupGlobalCookies:excludeAccountIdentifierCookies:
+ _objc_msgSend$ams_attributeNetworkingToBundleIdentifier:
+ _objc_msgSend$attributeWithCompletionPolicy:
+ _objc_msgSend$attributionBundleIdentifierForProxyAppBundleID:hasImpersonateEntitlement:
+ _objc_msgSend$bundleAdamID
+ _objc_msgSend$hasNetworkImpersonationEntitlement
+ _objc_msgSend$headerDescriptorsFor:
+ _objc_msgSend$identities
+ _objc_msgSend$identitySource
+ _objc_msgSend$includesChallenge
+ _objc_msgSend$includesPublicKey
+ _objc_msgSend$includesSignature
+ _objc_msgSend$includesState
+ _objc_msgSend$isPasscodePurchaseFallbackAvailableWith:completionHandler:
+ _objc_msgSend$metricsInternalLegacyRoutingPercentage
+ _objc_msgSend$names
+ _objc_msgSend$networkAttributionBundleIdentifier
+ _objc_msgSend$pageUserInteractiveTime
+ _objc_msgSend$sessionForAttributedBundleIdentifier:
+ _objc_msgSend$setShouldRunCampaignAttribution:
+ _objc_msgSend$setSuppressOtherMediaTypeStorefrontSync:
+ _objc_msgSend$set_sourceApplicationBundleIdentifier:
+ _objc_msgSend$shouldRunCampaignAttribution
+ _objc_msgSend$shouldSkipCardEnrollmentForWalletBiometricsCheck:walletBiometricsEnabled:
+ _objc_msgSend$signatureHeaderNamesFor:
+ _objc_msgSend$subarrayWithRange:
+ _objc_msgSend$supportsPasscodePurchaseWithAttestationStyle:
+ _objc_msgSend$suppressOtherMediaTypeStorefrontSync
+ _symbolic _____ 18AppleMediaServices20AssetsJetpackFetcherO
+ _symbolic _____ 18AppleMediaServices21LocalAuthHeaderFieldsV
+ _symbolic _____ 18AppleMediaServices25LocalAuthHeaderDescriptorC
+ _symbolic _____XMT 18AppleMediaServices28BagUnderlyingDataPersistenceC
+ _symbolic ______p 18AppleMediaServices20LocalAuthHeaderNamesP
+ _symbolic y_____Kc 10Foundation3URLV
+ _type_layout_string 18AppleMediaServices21LocalAuthHeaderFieldsV
- +[AMSBiometrics _nonKeyHeadersWithAccount:headerNames:state:signatureResult:]
- -[AMSAuthenticateTask _signIntoOtherMediaTypeWithVerifiedAccount:authenticationResults:]
- -[NSDictionary(AMSAccount) ams_firstName]
- -[NSDictionary(AMSAccount) ams_lastName]
- -[NSMutableURLRequest(AppleMediaServices) ams_addCookiesAsynchronouslyForAccount:clientInfo:bag:cleanupGlobalCookies:]
- -[NSMutableURLRequest(AppleMediaServices) ams_addCookiesForAccount:clientInfo:bag:cleanupGlobalCookies:]
- GCC_except_table110
- GCC_except_table138
- GCC_except_table147
- GCC_except_table177
- GCC_except_table59
- GCC_except_table88
- GCC_except_table91
- GCC_except_table97
- _OBJC_CLASS_$__TtC18AppleMediaServices20AssetsJetpackFetcher
- _OBJC_METACLASS_$__TtC18AppleMediaServices20AssetsJetpackFetcher
- __118-[NSMutableURLRequest(AppleMediaServices) ams_addCookiesAsynchronouslyForAccount:clientInfo:bag:cleanupGlobalCookies:]_block_invoke
- __118-[NSMutableURLRequest(AppleMediaServices) ams_addCookiesAsynchronouslyForAccount:clientInfo:bag:cleanupGlobalCookies:]_block_invoke_2
- __72-[AMSBagNetworkTask _performFetchWithAttemptedCount:account:storefront:]_block_invoke
- __CLASS_METHODS__TtC18AppleMediaServices20AssetsJetpackFetcher
- __CLASS_PROPERTIES__TtC18AppleMediaServices20AssetsJetpackFetcher
- __DATA__TtC18AppleMediaServices20AssetsJetpackFetcher
- __IVARS__TtC18AppleMediaServices20AssetsJetpackFetcher
- __METACLASS_DATA__TtC18AppleMediaServices20AssetsJetpackFetcher
- __OBJC_$_INSTANCE_METHODS__TtC18AppleMediaServices20AssetsJetpackFetcher(AppleMediaServices)
- __OBJC_CLASS_PROTOCOLS_$__TtC18AppleMediaServices20AssetsJetpackFetcher(AppleMediaServices)
- ___118-[NSMutableURLRequest(AppleMediaServices) ams_addCookiesAsynchronouslyForAccount:clientInfo:bag:cleanupGlobalCookies:]_block_invoke
- ___118-[NSMutableURLRequest(AppleMediaServices) ams_addCookiesAsynchronouslyForAccount:clientInfo:bag:cleanupGlobalCookies:]_block_invoke_2
- ___67+[AMSBiometrics headersPromiseWithAccount:options:signatureResult:]_block_invoke
- ___88-[AMSAuthenticateTask _signIntoOtherMediaTypeWithVerifiedAccount:authenticationResults:]_block_invoke
- ___block_descriptor_40_e8_32w_e43_v24?0"AMSAuthenticateResult"8"NSError"16l
- ___block_descriptor_48_e8_32s40s_e44_v24?0"AMSAuthKitUpdateResult"8"NSError"16l
- ___block_descriptor_56_e8_32s40s48s_e30_v16?0"AMSAuthKitUpdateTask"8l
- ___block_descriptor_56_e8_32s40s48s_e55_"AMSPromise"24?0"AMSAuthenticateResult"8"NSError"16l
- ___block_descriptor_57_e8_32s40s_e29_"AMSPromise"16?0"NSArray"8l
- ___block_descriptor_64_e8_32s40s48s_e32_"AMSPromise"24?08"NSError"16l
- ___block_descriptor_72_e8_32s40s48s56s_e34_"AMSPromise"16?0"AMSURLResult"8l
- _objc_msgSend$_nonKeyHeadersWithAccount:headerNames:state:signatureResult:
- _objc_msgSend$_signIntoOtherMediaTypeWithVerifiedAccount:authenticationResults:
- _objc_msgSend$ams_addCookiesAsynchronouslyForAccount:clientInfo:bag:cleanupGlobalCookies:
- _objc_msgSend$ams_addCookiesForAccount:clientInfo:bag:
- _objc_msgSend$ams_addCookiesForAccount:clientInfo:bag:cleanupGlobalCookies:
- _objc_msgSend$downloadTaskWithRequest:completionHandler:
- _objc_msgSend$headerNamesFor:
- _symbolic So6AMSBagC
- _symbolic _____ 18AppleMediaServices20AssetsJetpackFetcherC
- _symbolic _____IeyBy_ 10ObjectiveC8ObjCBoolV
CStrings:
+ "!\xa1"
+ "%{public}@: Could not find network override for %{public}@"
+ "%{public}@Excluding account-identifier cookie from request. cookie-name = %{public}@"
+ "%{public}@Passcode availability check failed (%{public}@); loading configuration anyway."
+ "-[AMSAuthenticateTask _signIntoMediaTypes:withVerifiedAccount:authenticationResults:]"
+ "@\"AMSPromise\"16@?0@\"AMSKeychainOptions\"8"
+ "AMSAuthenticateOptionsSuppressOtherMediaTypeStorefrontSyncKey"
+ "AMSMetricsInternalLegacyRoutingPercentage"
+ "AMSMockNetworkProxy: no override for %@"
+ "AMSSaveSelfieDiagnostics"
+ "AppleMediaServices.LocalAuthHeaderDescriptor"
+ "AssetsJetpackFetcher:"
+ "AssetsJetpackFetcher: ["
+ "Failed to exclude persisted bags directory from backup. error = "
+ "Unexpected status code: "
+ "com.apple.private.nsurlsession.impersonate"
+ "pageUserInteractiveTime"
+ "shouldRunCampaignAttribution"
- "!\x91"
- "-[AMSAuthenticateTask _signIntoOtherMediaTypeWithVerifiedAccount:authenticationResults:]"
- "Failed download with error: "
- "Failed to fetch and cache assets Jetpack with error = "
- "Fetching Jetpack..."
- "Jetpack successfully fetched and written to "
- "Maximum number of attempts exceeded."
- "accountInfo.address.firstName"
- "accountInfo.address.lastName"
```
