## AppleMediaServices

> `/System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift5_protos`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__lazy_load_got`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_dictobj`
- `__DATA_DIRTY.__objc_ivar`
- `__DATA_DIRTY.__objc_data`

```diff

-10.0.50.0.0
-  __TEXT.__text: 0x81c848
+10.0.54.0.0
+  __TEXT.__text: 0x81f38c
   __TEXT.__delay_stubs: 0x40
   __TEXT.__delay_helper: 0x134
   __TEXT.__lazy_helpers: 0x4028
-  __TEXT.__objc_methlist: 0x248dc
-  __TEXT.__const: 0x5b048
+  __TEXT.__objc_methlist: 0x24b34
+  __TEXT.__const: 0x5b058
   __TEXT.__dlopen_cstrs: 0x990
-  __TEXT.__cstring: 0x2e878
-  __TEXT.__swift5_typeref: 0x7dcb
-  __TEXT.__swift5_reflstr: 0x4993
+  __TEXT.__cstring: 0x2e9af
+  __TEXT.__swift5_typeref: 0x7df1
+  __TEXT.__swift5_reflstr: 0x4953
   __TEXT.__swift5_assocty: 0x10f8
-  __TEXT.__constg_swiftt: 0x63f8
+  __TEXT.__constg_swiftt: 0x640c
   __TEXT.__swift5_builtin: 0x474
   __TEXT.__swift5_fieldmd: 0x621c
   __TEXT.__swift5_proto: 0x1414
   __TEXT.__swift5_types: 0x784
-  __TEXT.__swift_as_entry: 0x918
-  __TEXT.__swift_as_ret: 0xb04
-  __TEXT.__swift_as_cont: 0x1514
-  __TEXT.__swift5_capture: 0x46b8
+  __TEXT.__swift_as_entry: 0x90c
+  __TEXT.__swift_as_ret: 0xaf4
+  __TEXT.__swift_as_cont: 0x14f4
+  __TEXT.__swift5_capture: 0x4644
   __TEXT.__swift5_mpenum: 0x8c
   __TEXT.__swift5_protos: 0x120
-  __TEXT.__oslogstring: 0x34463
-  __TEXT.__gcc_except_tab: 0x536c
+  __TEXT.__oslogstring: 0x34709
+  __TEXT.__gcc_except_tab: 0x53b0
   __TEXT.__ustring: 0x1b2
-  __TEXT.__unwind_info: 0x142c0
-  __TEXT.__eh_frame: 0x1a250
+  __TEXT.__unwind_info: 0x14730
+  __TEXT.__eh_frame: 0x1a0d4
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xd3c0
-  __DATA_CONST.__objc_classlist: 0x1610
+  __DATA_CONST.__const: 0xd4b8
+  __DATA_CONST.__objc_classlist: 0x1620
   __DATA_CONST.__objc_catlist: 0xe8
-  __DATA_CONST.__objc_protolist: 0x498
+  __DATA_CONST.__objc_protolist: 0x4a0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x10070
+  __DATA_CONST.__objc_selrefs: 0x10178
   __DATA_CONST.__objc_protorefs: 0x248
-  __DATA_CONST.__objc_superrefs: 0xd20
+  __DATA_CONST.__objc_superrefs: 0xd28
   __DATA_CONST.__objc_arraydata: 0x5f8
-  __DATA_CONST.__got: 0x1ac8
-  __AUTH_CONST.__const: 0x31640
-  __AUTH_CONST.__cfstring: 0x23c20
-  __AUTH_CONST.__objc_const: 0x40300
+  __DATA_CONST.__got: 0x1ad0
+  __AUTH_CONST.__const: 0x317f0
+  __AUTH_CONST.__cfstring: 0x23e20
+  __AUTH_CONST.__objc_const: 0x406a0
   __AUTH_CONST.__lazy_load_got: 0x5f8
   __AUTH_CONST.__objc_intobj: 0xcf0
   __AUTH_CONST.__objc_arrayobj: 0x180
   __AUTH_CONST.__objc_dictobj: 0x118
-  __AUTH_CONST.__auth_got: 0x2710
-  __AUTH.__objc_data: 0xaa98
-  __AUTH.__data: 0x30a8
-  __DATA.__objc_ivar: 0x1a14
-  __DATA.__data: 0x8354
+  __AUTH_CONST.__auth_got: 0x2738
+  __AUTH.__objc_data: 0xab20
+  __AUTH.__data: 0x30b0
+  __DATA.__objc_ivar: 0x1a3c
+  __DATA.__data: 0x83dc
   __DATA.__bss: 0x20050
-  __DATA.__common: 0xb68
+  __DATA.__common: 0xb64
   __DATA_DIRTY.__objc_ivar: 0x710
   __DATA_DIRTY.__objc_data: 0x5658
-  __DATA_DIRTY.__data: 0x2c08
-  __DATA_DIRTY.__bss: 0x62d0
+  __DATA_DIRTY.__data: 0x2be8
+  __DATA_DIRTY.__bss: 0x62e0
   __DATA_DIRTY.__common: 0x98
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 31053
-  Symbols:   32816
-  CStrings:  9301
+  Functions: 31099
+  Symbols:   32926
+  CStrings:  9325
 
Symbols:
+ +[ACAccount(AppleMediaServices) _ams_storageForDomain:]
+ +[AMSBagNetworkTask _expirationDateForInterval:now:]
+ +[AMSBagNetworkTask _selectedStorefrontForResponseStorefront:queryItems:]
+ +[AMSBagNetworkTask _shouldRetryForStorefrontChangeWithRequestStorefront:responseStorefront:]
+ +[AMSBiometrics _nonKeyHeadersWithAccount:headerNames:state:signatureResult:]
+ +[AMSBiometrics _stateValueForHeaderNames:account:]
+ +[AMSBiometrics identitySource]
+ +[AMSBiometrics setIdentitySource:]
+ +[AMSCardEnrollment shouldSkipCardEnrollmentForWalletBiometricsCheck:walletBiometricsEnabled:]
+ +[AMSFinancePaymentSheetResponse _credentialAccountForPaymentAccount:]
+ +[AMSFinancePaymentSheetResponse _mergedStyleDictionaryFromOuter:inner:]
+ +[AMSKeychainOptions _attestationStyleForBiometricsEnabled:passcodeEnabled:]
+ +[AMSMediaTokenService _signingErrorFromResult:encodingError:]
+ +[AMSProcessInfo _bundleFactsForIdentifier:]
+ +[AMSProcessInfo _cacheBundleFacts:forIdentifier:]
+ +[AMSProcessInfo _cachedBundleFactsForIdentifier:]
+ +[AMSProcessInfo _computeCurrentProcessBundleFacts]
+ +[AMSProcessInfo _currentProcessBundleFacts]
+ +[AMSProcessInfo _launchServicesBundleFactsForIdentifier:]
+ +[AMSURLSession _shouldCancelInFlightTaskForError:]
+ +[NSHTTPCookie(AMSCookieExpiry) ams_isExpiredForCookieExpiry:asOf:]
+ -[ACAccount(AppleMediaServices) ams_didAcknowledgeBundleHolderPrivacyAcknowledgementOnDeviceInStorageDomain:]
+ -[ACAccount(AppleMediaServices) ams_setDidAcknowledgeBundleHolderPrivacyAcknowledgementOnDevice:inStorageDomain:]
+ -[ACAccount(AppleMediaServices) ams_setSimpleProfileIdentifiers:]
+ -[ACAccount(AppleMediaServices) ams_simpleProfileIdentifiers]
+ -[AMSBagNetworkTask _promiseResultForURLResult:error:queryItems:responseStorefront:account:]
+ -[AMSDialogRequest account]
+ -[AMSDialogRequest setAccount:]
+ -[AMSLiveBiometricIdentitySource identities]
+ -[AMSMediaTokenService invalidateMediaTokenPromise:]
+ -[AMSMediaTokenService invalidateMediaTokenPromise]
+ -[AMSMediaTokenService invalidatePATMediaTokenPromise]
+ -[AMSMediaTokenService setCachedMediaTokenPromise:patBasedToken:]
+ -[AMSPaymentSheetPerformanceMetrics pageUserInteractiveTime]
+ -[AMSPaymentSheetPerformanceMetrics setPageUserInteractiveTime:]
+ -[AMSProcessInfo _ensureAllPropertiesResolved]
+ -[AMSProcessInfo _equalityFieldsSnapshot]
+ -[AMSProcessInfo _resolveMappedPropertiesIfNeededLocked]
+ -[AMSProcessInfo _resolveRecordPropertiesIfNeededLocked]
+ -[AMSProcessInfoBundleFacts .cxx_destruct]
+ -[AMSProcessInfoBundleFacts bundleURL]
+ -[AMSProcessInfoBundleFacts bundleVersion]
+ -[AMSProcessInfoBundleFacts clientVersion]
+ -[AMSProcessInfoBundleFacts executableName]
+ -[AMSProcessInfoBundleFacts initWithBundleURL:executableName:localizedName:bundleVersion:clientVersion:]
+ -[AMSProcessInfoBundleFacts localizedName]
+ -[AMSURLTaskInfo buyParamsSnapshot]
+ -[AMSURLTaskInfo setBuyParamsSnapshot:]
+ GCC_except_table100
+ GCC_except_table108
+ GCC_except_table141
+ GCC_except_table148
+ GCC_except_table176
+ GCC_except_table62
+ GCC_except_table77
+ GCC_except_table83
+ GCC_except_table88
+ GCC_except_table90
+ GCC_except_table91
+ GCC_except_table94
+ GCC_except_table97
+ _AMSErrorUserInfoKeyFPDIStage
+ _AMSMetricsLoggingSubsystemMediaTokenService
+ _CFBundleCopyExecutableURL
+ _CFBundleGetIdentifier
+ _OBJC_CLASS_$_AMSByteCountRounding
+ _OBJC_CLASS_$_AMSLiveBiometricIdentitySource
+ _OBJC_CLASS_$_AMSProcessInfoBundleFacts
+ _OBJC_IVAR_$_AMSDialogRequest._account
+ _OBJC_IVAR_$_AMSPaymentSheetPerformanceMetrics._pageUserInteractiveTime
+ _OBJC_IVAR_$_AMSProcessInfo._mappedPropertiesResolved
+ _OBJC_IVAR_$_AMSProcessInfo._recordPropertiesResolved
+ _OBJC_IVAR_$_AMSProcessInfoBundleFacts._bundleURL
+ _OBJC_IVAR_$_AMSProcessInfoBundleFacts._bundleVersion
+ _OBJC_IVAR_$_AMSProcessInfoBundleFacts._clientVersion
+ _OBJC_IVAR_$_AMSProcessInfoBundleFacts._executableName
+ _OBJC_IVAR_$_AMSProcessInfoBundleFacts._localizedName
+ _OBJC_IVAR_$_AMSURLTaskInfo._buyParamsSnapshot
+ _OBJC_METACLASS_$_AMSByteCountRounding
+ _OBJC_METACLASS_$_AMSLiveBiometricIdentitySource
+ _OBJC_METACLASS_$_AMSProcessInfoBundleFacts
+ __CLASS_METHODS_AMSByteCountRounding
+ __DATA_AMSByteCountRounding
+ __INSTANCE_METHODS_AMSByteCountRounding
+ __METACLASS_DATA_AMSByteCountRounding
+ __OBJC_$_INSTANCE_METHODS_AMSLiveBiometricIdentitySource
+ __OBJC_$_INSTANCE_METHODS_AMSProcessInfoBundleFacts
+ __OBJC_$_INSTANCE_VARIABLES_AMSProcessInfoBundleFacts
+ __OBJC_$_PROP_LIST_AMSLiveBiometricIdentitySource
+ __OBJC_$_PROP_LIST_AMSProcessInfoBundleFacts
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AMSBiometricIdentitySource
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AMSBiometricIdentitySource
+ __OBJC_$_PROTOCOL_REFS_AMSBiometricIdentitySource
+ __OBJC_CLASS_PROTOCOLS_$_AMSLiveBiometricIdentitySource
+ __OBJC_CLASS_RO_$_AMSLiveBiometricIdentitySource
+ __OBJC_CLASS_RO_$_AMSProcessInfoBundleFacts
+ __OBJC_LABEL_PROTOCOL_$_AMSBiometricIdentitySource
+ __OBJC_METACLASS_RO_$_AMSLiveBiometricIdentitySource
+ __OBJC_METACLASS_RO_$_AMSProcessInfoBundleFacts
+ __OBJC_PROTOCOL_$_AMSBiometricIdentitySource
+ ___109-[ACAccount(AppleMediaServices) ams_didAcknowledgeBundleHolderPrivacyAcknowledgementOnDeviceInStorageDomain:]_block_invoke
+ ___44+[AMSProcessInfo _currentProcessBundleFacts]_block_invoke
+ ___50+[AMSProcessInfo _cacheBundleFacts:forIdentifier:]_block_invoke
+ ___50+[AMSProcessInfo _cachedBundleFactsForIdentifier:]_block_invoke
+ ___51-[AMSEngagementClientData _enumerateAppsWithBlock:]_block_invoke_2
+ ___52-[AMSMediaTokenService invalidateMediaTokenPromise:]_block_invoke
+ ___58+[AMSProcessInfo _launchServicesBundleFactsForIdentifier:]_block_invoke
+ ___58+[AMSProcessInfo _launchServicesBundleFactsForIdentifier:]_block_invoke_2
+ ___62+[AMSMediaTokenService _signingErrorFromResult:encodingError:]_block_invoke
+ ___67+[AMSBiometrics headersPromiseWithAccount:options:signatureResult:]_block_invoke_2
+ ___67+[AMSBiometrics headersPromiseWithAccount:options:signatureResult:]_block_invoke_3
+ ___67+[AMSBiometrics headersPromiseWithAccount:options:signatureResult:]_block_invoke_4
+ ___block_descriptor_40_e8_32bs_e47_v32?0"NSString"8"AMSEngagementAppData"16^B24ls32l8
+ ___block_descriptor_41_e8_32w_e43_v24?0"AMSAuthenticateResult"8"NSError"16lw32l8
+ ___block_descriptor_48_e8_32s40s_e21_v16?0"AMSLRUCache"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e40_"AMSPromise"16?0"AMSKeychainOptions"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e51_"AMSBinaryPromise"24?0"AMSOptional"8"NSError"16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e60_"AMSPromise"24?0"AMSURLRequestEncoderResult"8"NSError"16ls32l8s40l8
+ ___block_descriptor_49_e8_32s40s_e31_v24?0"ACAccount"8"NSError"16ls32l8s40l8
+ ___block_descriptor_49_e8_32s40s_e44_v24?0"AMSAuthKitUpdateResult"8"NSError"16ls32l8s40l8
+ ___block_descriptor_57_e8_32s40s48s_e30_v16?0"AMSAuthKitUpdateTask"8ls32l8s40l8s48l8
+ ___block_descriptor_80_e8_32s40s48s56s64r_e15_v32?08Q16^B24lr64l8s32l8s40l8s48l8s56l8
+ ___block_descriptor_80_e8_32s40s48s56s64s_e35_"AMSPromise"16?0"AMSURLRequest"8ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_80_e8_32s40s48s56s64s_e46_"AMSPromise"24?0"AMSURLResult"8"NSError"16ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_89_e8_32s40s48s56s64s72s_e41_"AMSPromise"24?0"NSArray"8"NSError"16ls32l8s40l8s48l8s56l8s64l8s72l8
+ _flat unique So23AMSLocalAuthHeaderNames_p
+ _objc_msgSend$_ams_storageForDomain:
+ _objc_msgSend$_attestationStyleForBiometricsEnabled:passcodeEnabled:
+ _objc_msgSend$_bundleFactsForIdentifier:
+ _objc_msgSend$_cacheBundleFacts:forIdentifier:
+ _objc_msgSend$_cachedBundleFactsForIdentifier:
+ _objc_msgSend$_computeCurrentProcessBundleFacts
+ _objc_msgSend$_credentialAccountForPaymentAccount:
+ _objc_msgSend$_currentProcessBundleFacts
+ _objc_msgSend$_ensureAllPropertiesResolved
+ _objc_msgSend$_equalityFieldsSnapshot
+ _objc_msgSend$_expirationDateForInterval:now:
+ _objc_msgSend$_launchServicesBundleFactsForIdentifier:
+ _objc_msgSend$_mergedStyleDictionaryFromOuter:inner:
+ _objc_msgSend$_nonKeyHeadersWithAccount:headerNames:state:signatureResult:
+ _objc_msgSend$_promiseResultForURLResult:error:queryItems:responseStorefront:account:
+ _objc_msgSend$_resolveMappedPropertiesIfNeededLocked
+ _objc_msgSend$_resolveRecordPropertiesIfNeededLocked
+ _objc_msgSend$_selectedStorefrontForResponseStorefront:queryItems:
+ _objc_msgSend$_shouldCancelInFlightTaskForError:
+ _objc_msgSend$_shouldRetryForStorefrontChangeWithRequestStorefront:responseStorefront:
+ _objc_msgSend$_signingErrorFromResult:encodingError:
+ _objc_msgSend$_stateValueForHeaderNames:account:
+ _objc_msgSend$ams_didAcknowledgeBundleHolderPrivacyAcknowledgementOnDeviceInStorageDomain:
+ _objc_msgSend$ams_isExpiredForCookieExpiry:asOf:
+ _objc_msgSend$ams_setDidAcknowledgeBundleHolderPrivacyAcknowledgementOnDevice:inStorageDomain:
+ _objc_msgSend$ams_simpleProfileIdentifiers
+ _objc_msgSend$buyParamsSnapshot
+ _objc_msgSend$expandableInfo
+ _objc_msgSend$identities
+ _objc_msgSend$identitySource
+ _objc_msgSend$initWithBundleURL:executableName:localizedName:bundleVersion:clientVersion:
+ _objc_msgSend$initWithTitle:info:clientInfo:
+ _objc_msgSend$invalidateMediaTokenPromise:
+ _objc_msgSend$invalidatePATMediaTokenPromise
+ _objc_msgSend$pageUserInteractiveTime
+ _objc_msgSend$roundBytesToNearestTens:
+ _objc_msgSend$setBuyParamsSnapshot:
+ _objc_msgSend$setCachedMediaTokenPromise:patBasedToken:
+ _objc_msgSend$setPageUserInteractiveTime:
+ _objc_msgSend$shouldSkipCardEnrollmentForWalletBiometricsCheck:walletBiometricsEnabled:
+ _objc_msgSend$signatureHeaderNamesFor:
+ _objc_msgSend$supportsPasscodePurchaseWithAttestationStyle:
+ _symbolic _____ 18AppleMediaServices20AssetsJetpackFetcherO
+ _symbolic ______p 18AppleMediaServices20LocalAuthHeaderNamesP
- +[ACAccount(AppleMediaServices) _ams_storage]
- +[AMSBiometrics _nonKeyHeadersWithAccount:headerNames:signatureResult:]
- +[AMSMetricsLoadURLEvent _roundTransferBytesToNearestTens:]
- +[AMSProcessInfo _cacheProcessInfo:]
- +[AMSProcessInfo _cachedProcessInfoForIdentifier:]
- +[AMSProcessInfo copyPropertiesFrom:to:]
- +[NSHTTPCookie(AMSCookieExpiry) ams_isExpiredCookieExpiresValue:asOfDate:]
- -[AMSMediaTokenService invalidatePATMediaToken]
- -[AMSMediaTokenService setCachedMediaToken:patBasedToken:]
- -[AMSProcessInfo _setComputedPropertiesForBundleIdentifier:]
- GCC_except_table107
- GCC_except_table138
- GCC_except_table173
- GCC_except_table40
- GCC_except_table89
- GCC_except_table92
- GCC_except_table98
- _OBJC_CLASS_$__TtC18AppleMediaServices20AssetsJetpackFetcher
- _OBJC_METACLASS_$__TtC18AppleMediaServices20AssetsJetpackFetcher
- __CLASS_METHODS__TtC18AppleMediaServices20AssetsJetpackFetcher
- __CLASS_PROPERTIES__TtC18AppleMediaServices20AssetsJetpackFetcher
- __DATA__TtC18AppleMediaServices20AssetsJetpackFetcher
- __IVARS__TtC18AppleMediaServices20AssetsJetpackFetcher
- __METACLASS_DATA__TtC18AppleMediaServices20AssetsJetpackFetcher
- __OBJC_$_INSTANCE_METHODS__TtC18AppleMediaServices20AssetsJetpackFetcher(AppleMediaServices)
- __OBJC_CLASS_PROTOCOLS_$__TtC18AppleMediaServices20AssetsJetpackFetcher(AppleMediaServices)
- ___35-[AMSMockNetworkProxy startLoading]_block_invoke_3
- ___36+[AMSProcessInfo _cacheProcessInfo:]_block_invoke
- ___42+[AMSProcessInfo _accessProcessInfoCache:]_block_invoke_2
- ___42+[AMSProcessInfo _accessProcessInfoCache:]_block_invoke_3
- ___50+[AMSProcessInfo _cachedProcessInfoForIdentifier:]_block_invoke
- ___54-[ACAccount(AppleMediaServices) ams_hasSimpleProfiles]_block_invoke
- ___60-[AMSProcessInfo _setComputedPropertiesForBundleIdentifier:]_block_invoke
- ___60-[AMSProcessInfo _setComputedPropertiesForBundleIdentifier:]_block_invoke_2
- ___67+[AMSBiometrics headersPromiseWithAccount:options:signatureResult:]_block_invoke
- ___67-[AMSMediaTokenService _tokenRequestPromiseWithPrivateAccessToken:]_block_invoke_3
- ___72-[AMSBagNetworkTask _performFetchWithAttemptedCount:account:storefront:]_block_invoke_4
- ___93-[ACAccount(AppleMediaServices) ams_didAcknowledgeBundleHolderPrivacyAcknowledgementOnDevice]_block_invoke
- ___block_descriptor_40_e8_32s_e21_v16?0"AMSLRUCache"8ls32l8
- ___block_descriptor_40_e8_32s_e60_"AMSPromise"24?0"AMSURLRequestEncoderResult"8"NSError"16ls32l8
- ___block_descriptor_40_e8_32w_e43_v24?0"AMSAuthenticateResult"8"NSError"16lw32l8
- ___block_descriptor_48_e8_32s40s_e44_v24?0"AMSAuthKitUpdateResult"8"NSError"16ls32l8s40l8
- ___block_descriptor_56_e8_32s40s48s_e30_v16?0"AMSAuthKitUpdateTask"8ls32l8s40l8s48l8
- ___block_descriptor_72_e8_32s40s48s56r_e15_v32?08Q16^B24lr56l8s32l8s40l8s48l8
- ___block_descriptor_72_e8_32s40s48s56s_e34_"AMSPromise"16?0"AMSURLResult"8ls32l8s40l8s48l8s56l8
- ___block_descriptor_88_e8_32s40s48s56s64s72s_e41_"AMSPromise"24?0"NSArray"8"NSError"16ls32l8s40l8s48l8s56l8s64l8s72l8
- _kCFBundleIdentifierKey
- _objc_msgSend$_ams_storage
- _objc_msgSend$_cacheProcessInfo:
- _objc_msgSend$_cachedProcessInfoForIdentifier:
- _objc_msgSend$_nonKeyHeadersWithAccount:headerNames:signatureResult:
- _objc_msgSend$_roundTransferBytesToNearestTens:
- _objc_msgSend$_setComputedPropertiesForBundleIdentifier:
- _objc_msgSend$ams_isExpiredCookieExpiresValue:asOfDate:
- _objc_msgSend$copyPropertiesFrom:to:
- _objc_msgSend$downloadTaskWithRequest:completionHandler:
- _objc_msgSend$invalidatePATMediaToken
- _objc_msgSend$partnerHeader
- _objc_msgSend$setExecutableName:
- _symbolic _____ 18AppleMediaServices20AssetsJetpackFetcherC
CStrings:
+ " | selectedProfile = %@"
+ "!\xa1"
+ "%{public}@: Could not find network override for %{public}@"
+ "%{public}@: Failed to invalidate PAT media token. Error: %{public}@"
+ "%{public}@: [%{public}@] Failed to invalidate media token. Error: %{public}@"
+ "%{public}@: [%{public}@] Failed to read cached media token for invalidation. Error: %{public}@"
+ "%{public}@: [%{public}@] Silent-enrollment payment session failed. error: %{public}@"
+ "%{public}@Account flags decryption failed in daemon. Treating as stale key and triggering repair. error = %{public}@"
+ "%{public}@Account flags decryption failed locally. Falling back to XPC. error = %{public}@"
+ "%{public}@Failed to add FPDI signing headers. stage = %{public}@, error = %{public}@"
+ "%{public}@Storing password onto a Simple Profile. This is likely a bug. account = %{public}@ | password = %{public}@"
+ "%{public}@Successfully retrieved account flags via XPC fallback after crypto error."
+ "@\"AMSBinaryPromise\"24@?0@\"AMSOptional\"8@\"NSError\"16"
+ "@\"AMSPromise\"16@?0@\"AMSKeychainOptions\"8"
+ "AMSError-%@"
+ "AMSFPDIStage"
+ "AMSMockNetworkProxy: no override for %@"
+ "AssetsJetpackFetcher:"
+ "AssetsJetpackFetcher: ["
+ "MediaTokenService"
+ "MissingSignature"
+ "PAT"
+ "Payment services merchant URL was nil"
+ "Unexpected status code: "
+ "amsErrorCode"
+ "fpdiRetryCount"
+ "fpdiStage"
+ "fpdiStatus"
+ "httpMethod"
+ "kAccountIdentifier"
+ "kCodingKeyAccountIdentifier"
+ "pageUserInteractiveTime"
+ "profileIdentifiers"
+ "requestHost"
+ "requestPathHash"
- " | selected = %@"
- "!\x91"
- "%{public}@: [%{public}@] Account flags decryption failed with crypto error (possible stale key). Deleting property. error = %{public}@"
- "%{public}@Failed to add FPDI signing headers. error = %{public}@"
- "Failed download with error: "
- "Failed to fetch and cache assets Jetpack with error = "
- "Fetching Jetpack..."
- "Jetpack successfully fetched and written to "
- "Maximum number of attempts exceeded."
- "SigningHeaders"
- "com.apple.AMSProcessInfo"
```
