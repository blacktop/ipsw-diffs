## AppleMediaServices

> `/System/Library/PrivateFrameworks/AppleMediaServices.framework/Versions/A/AppleMediaServices`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift5_protos`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__lazy_load_got`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_dictobj`
- `__DATA_DIRTY.__objc_ivar`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-10.0.50.0.0
-  __TEXT.__text: 0x8e988c
+10.0.52.0.0
+  __TEXT.__text: 0x8eddcc
   __TEXT.__lazy_helpers: 0x2e98
-  __TEXT.__objc_methlist: 0x23b2c
-  __TEXT.__const: 0xba308
+  __TEXT.__objc_methlist: 0x23d04
+  __TEXT.__const: 0xba328
   __TEXT.__dlopen_cstrs: 0x834
-  __TEXT.__cstring: 0x2ba17
+  __TEXT.__cstring: 0x2baea
   __TEXT.__swift5_typeref: 0x75a9
-  __TEXT.__swift5_reflstr: 0x3ec3
+  __TEXT.__swift5_reflstr: 0x3ef3
   __TEXT.__swift5_assocty: 0xf60
-  __TEXT.__constg_swiftt: 0x59e8
+  __TEXT.__constg_swiftt: 0x5a18
   __TEXT.__swift5_builtin: 0x3d4
-  __TEXT.__swift5_fieldmd: 0x55a8
+  __TEXT.__swift5_fieldmd: 0x55c0
   __TEXT.__swift5_proto: 0x11f8
   __TEXT.__swift5_types: 0x6dc
   __TEXT.__swift_as_entry: 0x89c

   __TEXT.__swift5_capture: 0x3f7c
   __TEXT.__swift5_mpenum: 0x8c
   __TEXT.__swift5_protos: 0x118
-  __TEXT.__oslogstring: 0x30b67
-  __TEXT.__gcc_except_tab: 0x5258
+  __TEXT.__oslogstring: 0x30d08
+  __TEXT.__gcc_except_tab: 0x5260
   __TEXT.__ustring: 0x210
-  __TEXT.__unwind_info: 0x12e10
-  __TEXT.__eh_frame: 0x17864
+  __TEXT.__unwind_info: 0x12ab8
+  __TEXT.__eh_frame: 0x17b2c
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x5c58
-  __DATA_CONST.__objc_classlist: 0x1588
+  __DATA_CONST.__const: 0x5c88
+  __DATA_CONST.__objc_classlist: 0x1598
   __DATA_CONST.__objc_catlist: 0xe0
   __DATA_CONST.__objc_protolist: 0x488
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xf918
+  __DATA_CONST.__objc_selrefs: 0xf9c8
   __DATA_CONST.__objc_protorefs: 0x258
-  __DATA_CONST.__objc_superrefs: 0xcf0
+  __DATA_CONST.__objc_superrefs: 0xcf8
   __DATA_CONST.__objc_arraydata: 0x498
   __DATA_CONST.__got: 0x19c8
-  __AUTH_CONST.__const: 0x443a8
-  __AUTH_CONST.__cfstring: 0x22e80
-  __AUTH_CONST.__objc_const: 0x3ece8
+  __AUTH_CONST.__const: 0x44430
+  __AUTH_CONST.__cfstring: 0x23020
+  __AUTH_CONST.__objc_const: 0x3eff8
   __AUTH_CONST.__lazy_load_got: 0x460
   __AUTH_CONST.__objc_intobj: 0xc30
   __AUTH_CONST.__objc_arrayobj: 0x180
   __AUTH_CONST.__objc_dictobj: 0x78
-  __AUTH_CONST.__auth_got: 0x2370
-  __AUTH.__objc_data: 0x9a18
-  __AUTH.__data: 0x2b88
-  __DATA.__objc_ivar: 0x1a00
-  __DATA.__data: 0x7b54
+  __AUTH_CONST.__auth_got: 0x2388
+  __AUTH.__objc_data: 0x9b18
+  __AUTH.__data: 0x2bb8
+  __DATA.__objc_ivar: 0x1a24
+  __DATA.__data: 0x7b64
   __DATA.__bss: 0x1bb58
-  __DATA.__common: 0x1514
+  __DATA.__common: 0x1520
   __DATA_DIRTY.__objc_ivar: 0x6c8
   __DATA_DIRTY.__objc_data: 0x5b00
   __DATA_DIRTY.__data: 0x2e60

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 28980
-  Symbols:   31960
-  CStrings:  8771
+  Functions: 29068
+  Symbols:   32032
+  CStrings:  8789
 
Symbols:
+ +[ACAccount(AppleMediaServices) _ams_storageForDomain:]
+ +[AMSBiometrics _nonKeyHeadersWithAccount:headerNames:state:signatureResult:]
+ +[AMSBiometrics _stateValueForHeaderNames:account:]
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
+ -[ACAccountStore(AppleMediaServices) ams_isActiveAccountCombinedForMediaType:]
+ -[AMSDialogRequest account]
+ -[AMSDialogRequest setAccount:]
+ -[AMSMediaTokenService invalidateMediaTokenPromise:]
+ -[AMSMediaTokenService invalidateMediaTokenPromise]
+ -[AMSMediaTokenService invalidatePATMediaTokenPromise]
+ -[AMSMediaTokenService setCachedMediaTokenPromise:patBasedToken:]
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
+ GCC_except_table110
+ GCC_except_table126
+ GCC_except_table138
+ GCC_except_table147
+ GCC_except_table177
+ GCC_except_table92
+ OBJC_IVAR_$_AMSDialogRequest._account
+ OBJC_IVAR_$_AMSProcessInfo._mappedPropertiesResolved
+ OBJC_IVAR_$_AMSProcessInfo._recordPropertiesResolved
+ OBJC_IVAR_$_AMSProcessInfoBundleFacts._bundleURL
+ OBJC_IVAR_$_AMSProcessInfoBundleFacts._bundleVersion
+ OBJC_IVAR_$_AMSProcessInfoBundleFacts._clientVersion
+ OBJC_IVAR_$_AMSProcessInfoBundleFacts._executableName
+ OBJC_IVAR_$_AMSProcessInfoBundleFacts._localizedName
+ OBJC_IVAR_$_AMSURLTaskInfo._buyParamsSnapshot
+ _AMSErrorUserInfoKeyFPDIStage
+ _AMSMetricsLoggingSubsystemMediaTokenService
+ _CFBundleCopyExecutableURL
+ _CFBundleGetIdentifier
+ _J43arc1316S2
+ _OBJC_CLASS_$_AMSByteCountRounding
+ _OBJC_CLASS_$_AMSProcessInfoBundleFacts
+ _OBJC_METACLASS_$_AMSByteCountRounding
+ _OBJC_METACLASS_$_AMSProcessInfoBundleFacts
+ __58+[AMSProcessInfo _launchServicesBundleFactsForIdentifier:]_block_invoke
+ __65-[AMSMediaProtocolHandler handleResponse:task:completionHandler:]_block_invoke
+ __CLASS_METHODS_AMSByteCountRounding
+ __DATA_AMSByteCountRounding
+ __INSTANCE_METHODS_AMSByteCountRounding
+ __METACLASS_DATA_AMSByteCountRounding
+ __OBJC_$_INSTANCE_METHODS_AMSProcessInfoBundleFacts
+ __OBJC_$_INSTANCE_VARIABLES_AMSProcessInfoBundleFacts
+ __OBJC_$_PROP_LIST_AMSProcessInfoBundleFacts
+ __OBJC_CLASS_RO_$_AMSProcessInfoBundleFacts
+ __OBJC_METACLASS_RO_$_AMSProcessInfoBundleFacts
+ ___109-[ACAccount(AppleMediaServices) ams_didAcknowledgeBundleHolderPrivacyAcknowledgementOnDeviceInStorageDomain:]_block_invoke
+ ___44+[AMSProcessInfo _currentProcessBundleFacts]_block_invoke
+ ___50+[AMSProcessInfo _cacheBundleFacts:forIdentifier:]_block_invoke
+ ___50+[AMSProcessInfo _cachedBundleFactsForIdentifier:]_block_invoke
+ ___51-[AMSEngagementClientData _enumerateAppsWithBlock:]_block_invoke_2
+ ___52-[AMSMediaTokenService invalidateMediaTokenPromise:]_block_invoke
+ ___58+[AMSProcessInfo _launchServicesBundleFactsForIdentifier:]_block_invoke
+ ___62+[AMSMediaTokenService _signingErrorFromResult:encodingError:]_block_invoke
+ ___block_descriptor_40_e8_32bs_e47_v32?0"NSString"8"AMSEngagementAppData"16^B24l
+ ___block_descriptor_48_e8_32s40s_e21_v16?0"AMSLRUCache"8l
+ ___block_descriptor_48_e8_32s40s_e51_"AMSBinaryPromise"24?0"AMSOptional"8"NSError"16l
+ ___block_descriptor_48_e8_32s40s_e60_"AMSPromise"24?0"AMSURLRequestEncoderResult"8"NSError"16l
+ ___block_descriptor_80_e8_32s40s48s56s64r_e15_v32?08Q16^B24l
+ ___block_descriptor_89_e8_32s40s48s56s64s72s_e41_"AMSPromise"24?0"NSArray"8"NSError"16l
+ _objc_msgSend$_ams_storageForDomain:
+ _objc_msgSend$_bundleFactsForIdentifier:
+ _objc_msgSend$_cacheBundleFacts:forIdentifier:
+ _objc_msgSend$_cachedBundleFactsForIdentifier:
+ _objc_msgSend$_computeCurrentProcessBundleFacts
+ _objc_msgSend$_currentProcessBundleFacts
+ _objc_msgSend$_ensureAllPropertiesResolved
+ _objc_msgSend$_equalityFieldsSnapshot
+ _objc_msgSend$_launchServicesBundleFactsForIdentifier:
+ _objc_msgSend$_mergedStyleDictionaryFromOuter:inner:
+ _objc_msgSend$_nonKeyHeadersWithAccount:headerNames:state:signatureResult:
+ _objc_msgSend$_resolveMappedPropertiesIfNeededLocked
+ _objc_msgSend$_resolveRecordPropertiesIfNeededLocked
+ _objc_msgSend$_shouldCancelInFlightTaskForError:
+ _objc_msgSend$_signingErrorFromResult:encodingError:
+ _objc_msgSend$_stateValueForHeaderNames:account:
+ _objc_msgSend$ams_didAcknowledgeBundleHolderPrivacyAcknowledgementOnDeviceInStorageDomain:
+ _objc_msgSend$ams_isExpiredForCookieExpiry:asOf:
+ _objc_msgSend$ams_setDidAcknowledgeBundleHolderPrivacyAcknowledgementOnDevice:inStorageDomain:
+ _objc_msgSend$buyParamsSnapshot
+ _objc_msgSend$expandableInfo
+ _objc_msgSend$initWithBundleURL:executableName:localizedName:bundleVersion:clientVersion:
+ _objc_msgSend$initWithTitle:info:clientInfo:
+ _objc_msgSend$invalidateMediaTokenPromise:
+ _objc_msgSend$invalidatePATMediaTokenPromise
+ _objc_msgSend$roundBytesToNearestTens:
+ _objc_msgSend$setAccountIdentifier:
+ _objc_msgSend$setBuyParamsSnapshot:
+ _objc_msgSend$setCachedMediaTokenPromise:patBasedToken:
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
- GCC_except_table109
- GCC_except_table125
- GCC_except_table137
- GCC_except_table146
- GCC_except_table176
- GCC_except_table40
- GCC_except_table44
- GCC_except_table76
- __60-[AMSProcessInfo _setComputedPropertiesForBundleIdentifier:]_block_invoke
- ___36+[AMSProcessInfo _cacheProcessInfo:]_block_invoke
- ___42+[AMSProcessInfo _accessProcessInfoCache:]_block_invoke_2
- ___42+[AMSProcessInfo _accessProcessInfoCache:]_block_invoke_3
- ___50+[AMSProcessInfo _cachedProcessInfoForIdentifier:]_block_invoke
- ___60-[AMSProcessInfo _setComputedPropertiesForBundleIdentifier:]_block_invoke
- ___67-[AMSMediaTokenService _tokenRequestPromiseWithPrivateAccessToken:]_block_invoke_3
- ___93-[ACAccount(AppleMediaServices) ams_didAcknowledgeBundleHolderPrivacyAcknowledgementOnDevice]_block_invoke
- ___block_descriptor_40_e8_32s_e21_v16?0"AMSLRUCache"8l
- ___block_descriptor_40_e8_32s_e60_"AMSPromise"24?0"AMSURLRequestEncoderResult"8"NSError"16l
- ___block_descriptor_72_e8_32s40s48s56r_e15_v32?08Q16^B24l
- ___block_descriptor_88_e8_32s40s48s56s64s72s_e41_"AMSPromise"24?0"NSArray"8"NSError"16l
- _kCFBundleIdentifierKey
- _objc_msgSend$_ams_storage
- _objc_msgSend$_cacheProcessInfo:
- _objc_msgSend$_cachedProcessInfoForIdentifier:
- _objc_msgSend$_nonKeyHeadersWithAccount:headerNames:signatureResult:
- _objc_msgSend$_roundTransferBytesToNearestTens:
- _objc_msgSend$_setComputedPropertiesForBundleIdentifier:
- _objc_msgSend$ams_isExpiredCookieExpiresValue:asOfDate:
- _objc_msgSend$copyPropertiesFrom:to:
- _objc_msgSend$invalidatePATMediaToken
- _objc_msgSend$partnerHeader
- _objc_msgSend$setExecutableName:
CStrings:
+ "%{public}@: Failed to invalidate PAT media token. Error: %{public}@"
+ "%{public}@: [%{public}@] Failed to invalidate media token. Error: %{public}@"
+ "%{public}@: [%{public}@] Failed to read cached media token for invalidation. Error: %{public}@"
+ "%{public}@Account flags decryption failed in daemon. Treating as stale key and triggering repair. error = %{public}@"
+ "%{public}@Account flags decryption failed locally. Falling back to XPC. error = %{public}@"
+ "%{public}@Failed to add FPDI signing headers. stage = %{public}@, error = %{public}@"
+ "%{public}@Successfully retrieved account flags via XPC fallback after crypto error."
+ "@\"AMSBinaryPromise\"24@?0@\"AMSOptional\"8@\"NSError\"16"
+ "AMSError-%@"
+ "AMSFPDIStage"
+ "MediaTokenService"
+ "MissingSignature"
+ "PAT"
+ "amsErrorCode"
+ "fpdiRetryCount"
+ "fpdiStage"
+ "fpdiStatus"
+ "httpMethod"
+ "kAccountIdentifier"
+ "kCodingKeyAccountIdentifier"
+ "requestHost"
+ "requestPathHash"
- "%{public}@: [%{public}@] Account flags decryption failed with crypto error (possible stale key). Deleting property. error = %{public}@"
- "%{public}@Failed to add FPDI signing headers. error = %{public}@"
- "SigningHeaders"
- "com.apple.AMSProcessInfo"
```
