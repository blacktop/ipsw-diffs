## SafariCore

> `/System/Library/PrivateFrameworks/SafariCore.framework/Versions/A/SafariCore`

```diff

-625.1.29.11.27
-  __TEXT.__text: 0x1f1de4
-  __TEXT.__objc_methlist: 0xd514
-  __TEXT.__const: 0x7c14
-  __TEXT.__gcc_except_tab: 0x7dcc
-  __TEXT.__cstring: 0x17737
+625.2.4.1.0
+  __TEXT.__text: 0x1f7f40
+  __TEXT.__objc_methlist: 0xd634
+  __TEXT.__const: 0x7d14
+  __TEXT.__gcc_except_tab: 0x7ec8
+  __TEXT.__cstring: 0x177b7
   __TEXT.__ustring: 0x2784
-  __TEXT.__oslogstring: 0xe741
+  __TEXT.__oslogstring: 0xe9d1
   __TEXT.__dlopen_cstrs: 0x157
-  __TEXT.__constg_swiftt: 0x2214
-  __TEXT.__swift5_typeref: 0x2612
-  __TEXT.__swift5_reflstr: 0x14fb
-  __TEXT.__swift5_fieldmd: 0x19a0
+  __TEXT.__constg_swiftt: 0x2340
+  __TEXT.__swift5_typeref: 0x26ba
+  __TEXT.__swift5_reflstr: 0x156b
+  __TEXT.__swift5_fieldmd: 0x1a24
   __TEXT.__swift5_builtin: 0x154
   __TEXT.__swift5_assocty: 0x638
   __TEXT.__swift5_proto: 0x4e0
-  __TEXT.__swift5_types: 0x214
+  __TEXT.__swift5_types: 0x21c
   __TEXT.__swift5_types2: 0x4
-  __TEXT.__swift_as_entry: 0x328
-  __TEXT.__swift_as_ret: 0x370
+  __TEXT.__swift_as_entry: 0x324
+  __TEXT.__swift_as_ret: 0x36c
   __TEXT.__swift_as_cont: 0x6f0
-  __TEXT.__swift5_capture: 0x145c
-  __TEXT.__swift5_protos: 0x2c
+  __TEXT.__swift5_capture: 0x14d4
+  __TEXT.__swift5_protos: 0x30
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0xbf58
-  __TEXT.__eh_frame: 0xa2f8
+  __TEXT.__unwind_info: 0xc0b8
+  __TEXT.__eh_frame: 0xa328
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2888
-  __DATA_CONST.__objc_classlist: 0x710
+  __DATA_CONST.__const: 0x28b8
+  __DATA_CONST.__objc_classlist: 0x718
   __DATA_CONST.__objc_catlist: 0x160
   __DATA_CONST.__objc_protolist: 0x218
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x77f8
+  __DATA_CONST.__objc_selrefs: 0x7870
   __DATA_CONST.__objc_protorefs: 0xf8
   __DATA_CONST.__objc_superrefs: 0x4c8
   __DATA_CONST.__objc_arraydata: 0x2a98
-  __DATA_CONST.__got: 0x13d0
-  __AUTH_CONST.__const: 0xe8c0
+  __DATA_CONST.__got: 0x13e0
+  __AUTH_CONST.__const: 0xeba8
   __AUTH_CONST.__cfstring: 0x1b5c0
-  __AUTH_CONST.__objc_const: 0x166e0
+  __AUTH_CONST.__objc_const: 0x16890
   __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__objc_intobj: 0x930
   __AUTH_CONST.__objc_dictobj: 0x190
   __AUTH_CONST.__objc_arrayobj: 0x588
   __AUTH_CONST.__auth_got: 0x20c0
-  __AUTH.__objc_data: 0x2210
-  __AUTH.__data: 0x1038
-  __DATA.__objc_ivar: 0xd30
-  __DATA.__data: 0x34e0
-  __DATA.__common: 0x88
+  __AUTH.__objc_data: 0x2328
+  __AUTH.__data: 0x1078
+  __DATA.__objc_ivar: 0xd34
+  __DATA.__data: 0x35b0
+  __DATA.__common: 0xa8
   __DATA_DIRTY.__objc_data: 0x2ac0
   __DATA_DIRTY.__data: 0xed8
   __DATA_DIRTY.__bss: 0xe10

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 11456
-  Symbols:   15128
-  CStrings:  5347
+  Functions: 11557
+  Symbols:   15198
+  CStrings:  5357
 
Symbols:
+ +[NSURLSessionConfiguration(SafariCoreExtras) safari_persistentStateSessionConfiguration]
+ +[WBSFeatureAvailability automaticPasswordChangeShouldAlwaysRecommend]
+ +[WBSFeatureAvailability isAutomaticPasswordChangeTestFestModeEnabled]
+ +[WBSFeatureAvailability setAutomaticPasswordChangeTestFestModeEnabled:]
+ +[WBSSavedAccount isDebugAccountForAutomaticPasswordChangeForDomain:]
+ +[WBSSavedAccount isUUIDHighLevelDomain:]
+ -[NSURLProtectionSpace(SafariCoreExtras) safari_getAllowsCredentialSavingWithCompletionHandler:]
+ -[WBSPasswordWarningTopFraudTargets emailProviderFraudTargets]
+ -[WBSPasswordWarningTopFraudTargets initWithHighPriorityTargets:targets:financialTargets:emailProviderFraudTargets:]
+ -[WBSSavedAccount _adoptSidecarDataFromSavedAccount:]
+ -[WBSSavedAccountStore _logSavedAccountsWithTOTPGeneratorsOnlyInPasskeySidecars:]
+ -[WBSSavedAccountStore _savedAccountConflictingWithSavedAccountOnInternalQueue:afterUpdatingUsername:password:]
+ -[WBSSavedAccountStore canSaveUser:password:forProtectionSpace:highLevelDomain:notes:customTitle:groupID:completionHandler:]
+ -[WBSSavedAccountStore canSaveUser:password:forUserTypedSite:notes:customTitle:groupID:completionHandler:]
+ GCC_except_table139
+ GCC_except_table230
+ GCC_except_table242
+ GCC_except_table264
+ GCC_except_table274
+ GCC_except_table288
+ GCC_except_table404
+ GCC_except_table464
+ GCC_except_table477
+ GCC_except_table497
+ GCC_except_table502
+ OBJC_IVAR_$_WBSPasswordWarningTopFraudTargets._emailProviderFraudTargets
+ WBSOSLogSearchFeatureAvailability
+ WBSOSLogSearchFeatureAvailability.log
+ WBSOSLogSearchFeatureAvailability.onceToken
+ _OBJC_CLASS_$_WBSGuidedBrowsingNavigationEvent
+ _OBJC_METACLASS_$_WBSGuidedBrowsingNavigationEvent
+ _PROTOCOLS_WBSGuidedBrowsingNavigationEvent
+ _WBSAutomaticPasswordChangeDebugLogAutoFilledDataKey
+ _WBSOSLogSearchFeatureAvailability
+ __124-[WBSSavedAccountStore canSaveUser:password:forProtectionSpace:highLevelDomain:notes:customTitle:groupID:completionHandler:]_block_invoke
+ __CLASS_METHODS_WBSGuidedBrowsingNavigationEvent
+ __CLASS_PROPERTIES_WBSGuidedBrowsingNavigationEvent
+ __DATA_WBSGuidedBrowsingNavigationEvent
+ __INSTANCE_METHODS_WBSGuidedBrowsingNavigationEvent
+ __IVARS_WBSGuidedBrowsingNavigationEvent
+ __IVARS__TtCE10SafariCoreV15Synchronization5MutexP33_5EB6CF0E21105A7FACDF3B64E2151CBD10SendingBox
+ __METACLASS_DATA_WBSGuidedBrowsingNavigationEvent
+ __OBJC_$_INSTANCE_METHODS_WBSSavedAccountChangeRequest(SafariCore)
+ __PROPERTIES_WBSGuidedBrowsingNavigationEvent
+ __PROTOCOLS_WBSGuidedBrowsingNavigationEvent
+ __ZL30configureCommonSessionSettingsP25NSURLSessionConfiguration
+ ___111-[WBSSavedAccountStore _savedAccountConflictingWithSavedAccountOnInternalQueue:afterUpdatingUsername:password:]_block_invoke
+ ___124-[WBSSavedAccountStore canSaveUser:password:forProtectionSpace:highLevelDomain:notes:customTitle:groupID:completionHandler:]_block_invoke
+ ___49-[WBSSavedAccount lastUsedDateForSite:inContext:]_block_invoke
+ ___81-[WBSSavedAccountStore _logSavedAccountsWithTOTPGeneratorsOnlyInPasskeySidecars:]_block_invoke
+ ___81-[WBSSavedAccountStore _logSavedAccountsWithTOTPGeneratorsOnlyInPasskeySidecars:]_block_invoke_2
+ ___94-[WBSSavedAccountStore canSaveUser:password:forUserTypedSite:notes:customTitle:groupID:error:]_block_invoke
+ ___96-[NSURLProtectionSpace(SafariCoreExtras) safari_getAllowsCredentialSavingWithCompletionHandler:]_block_invoke
+ ___96-[NSURLProtectionSpace(SafariCoreExtras) safari_getAllowsCredentialSavingWithCompletionHandler:]_block_invoke_2
+ ___WBSOSLogSearchFeatureAvailability_block_invoke
+ ___block_descriptor_32_e30_B16?0"WBSSavedAccountMatch"8l
+ ___block_descriptor_40_e8_32bs_e36_v16?0"WBSSavedAccountMatchResult"8l
+ ___block_descriptor_40_e8_32r_e49_v32?0q8"<WBSSavedAccountSidecarInternal>"16^B24l
+ ___block_descriptor_41_e8_32s_e46_v32?0"NSString"8"NSMutableDictionary"16^B24l
+ ___block_descriptor_48_e8_32s40r_e8_v12?0B8l
+ ___block_descriptor_56_e8_32s40r48r_e20_v20?0B8"NSError"12l
+ ___block_descriptor_56_e8_32s40s48r_e46_v32?0"NSString"8"NSMutableDictionary"16^B24l
+ ___block_descriptor_73_e8_32s40s48s56s64r_e42_v32?0"NSString"8"WBSSavedAccount"16^B24l
+ ___block_descriptor_96_e8_32s40s48s56s64s72s80s88bs_e5_v8?0l
+ ___copy_helper_block_e8_32s40s48s56s64s72s80s88b
+ ___unnamed_2
+ __swift_closure_destructor.125Tm
+ __swift_closure_destructor.244Tm
+ __swift_closure_destructor.254Tm
+ __swift_closure_destructor.409Tm
+ __swift_closure_destructor.467Tm
+ __swift_closure_destructor.54Tm
+ __swift_closure_destructor.583Tm
+ __swift_closure_destructor.58Tm
+ _automaticPasswordChangeTestFestModeEnabled
+ _objc_msgSend$_adoptSidecarDataFromSavedAccount:
+ _objc_msgSend$_logSavedAccountsWithTOTPGeneratorsOnlyInPasskeySidecars:
+ _objc_msgSend$_savedAccountConflictingWithSavedAccountOnInternalQueue:afterUpdatingUsername:password:
+ _objc_msgSend$_savedAccountDidAdoptSidecarDataFromConflictingSavedAccount:
+ _objc_msgSend$automaticPasswordChangeShouldAlwaysRecommend
+ _objc_msgSend$canSaveUser:password:forProtectionSpace:highLevelDomain:notes:customTitle:groupID:completionHandler:
+ _objc_msgSend$canSaveUser:password:forUserTypedSite:notes:customTitle:groupID:completionHandler:
+ _objc_msgSend$currentURLChanged:inTabWithUUID:
+ _objc_msgSend$defaultSessionConfiguration
+ _objc_msgSend$emailProviderFraudTargets
+ _objc_msgSend$initWithHighPriorityTargets:targets:financialTargets:emailProviderFraudTargets:
+ _objc_msgSend$isAutomaticPasswordChangeTestFestModeEnabled
+ _objc_msgSend$isDebugAccountForAutomaticPasswordChangeForDomain:
+ _objc_msgSend$isUUIDHighLevelDomain:
+ _objc_msgSend$reportNavigationEvent:inTabWithUUID:
+ _objc_msgSend$safari_getAllowsCredentialSavingWithCompletionHandler:
+ _objc_msgSend$setConnectionCodeSigningRequirement:
+ _objc_msgSend$set_sourceApplicationBundleIdentifier:
+ _symbolic $s10SafariCore45WBSAutomaticPasswordChangeCompletionReportingP
+ _symbolic Shy_____G 10Foundation4UUIDV
+ _symbolic _____ 10SafariCore32WBSGuidedBrowsingNavigationEventC
+ _symbolic _____ 15Synchronization5MutexV10SafariCoreE10SendingBox33_5EB6CF0E21105A7FACDF3B64E2151CBDLLC
+ _symbolic _____SgXwz_Xx 10SafariCore27WBSGuidedBrowsingControllerC
+ _symbolic ______pIeghg_ 10SafariCore39WBSGuidedBrowsingUIRegistrationProtocolP
+ _symbolic _____m 10SafariCore32WBSGuidedBrowsingNavigationEventC
+ _symbolic _____ySbG 15Synchronization6AtomicV
+ _symbolic _____yShy_____GG 15Synchronization5MutexVAARi_zrlE 10Foundation4UUIDV
+ _symbolic _____ySo15NSXPCConnectionCSgG 15Synchronization5MutexVAARi_zrlE
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 10Foundation4UUIDV
+ _symbolic _____yxG 15Synchronization5MutexVAARi_zrlE
- +[WBSFeatureAvailability isAllowFavoritesInFrequentlyVisitedEnabled]
- +[WBSFeatureAvailability isAllowLogOnURLsInFrequentlyVisitedEnabled]
- +[WBSFeatureAvailability isDropOutliersInFrequentlyVisitedEnabled]
- -[WBSPasswordWarningTopFraudTargets initWithHighPriorityTargets:targets:financialTargets:]
- -[WBSWellKnownChangePasswordURLFallbackController didFinishLoad]
- GCC_except_table127
- GCC_except_table136
- GCC_except_table253
- GCC_except_table340
- GCC_except_table384
- GCC_except_table454
- GCC_except_table459
- GCC_except_table485
- GCC_except_table490
- _WBSEnableDropOutliersInFrequentlyVisitedKey
- _WBSFrequentlyVisitedSitesAllowLogonURLsPreferenceKey
- _WBSFrequentlyVisitedSitesAllowSitesFromFavoritesPreferenceKey
- __112-[WBSSavedAccountStore canSaveUser:password:forProtectionSpace:highLevelDomain:notes:customTitle:groupID:error:]_block_invoke
- __OBJC_$_CLASS_PROP_LIST_NSURLSessionConfiguration_$_SafariCoreExtras
- __OBJC_$_INSTANCE_METHODS_WBSSavedAccountChangeRequest
- ___block_descriptor_104_e8_32s40s48s56s64s72s80s88r96r_e5_v8?0l
- ___block_descriptor_48_e8_32s40s_e46_v32?0"NSString"8"NSMutableDictionary"16^B24l
- ___copy_helper_block_e8_32s40s48s56s64s72s80s88r96r
- ___destroy_helper_block_e8_32s40s48s56s64s72s80s88r96r
- __swift_closure_destructor.238Tm
- __swift_closure_destructor.248Tm
- __swift_closure_destructor.403Tm
- __swift_closure_destructor.461Tm
- __swift_closure_destructor.53Tm
- __swift_closure_destructor.577Tm
- __swift_closure_destructor.57Tm
- _objc_msgSend$initWithHighPriorityTargets:targets:financialTargets:
- _objc_msgSend$safari_isAppleSigned
- _symbolic So15NSXPCConnectionC
- _symbolic _____y_____G s23_ContiguousArrayStorageC 10SafariCore26WBSLocalizedPluralVariableV
CStrings:
+ "-[WBSSavedAccountStore canSaveUser:password:forUserTypedSite:notes:customTitle:groupID:error:]"
+ "Connected to broker"
+ "Error reporting navigation state to broker: %{public}s"
+ "Exceeded %.2f sec timeout while checking wheather credential saving is allowed for %{sensitive}@"
+ "Expired %.2f timeout waiting for canSaveUser:password: call to resolve"
+ "Expired %.2f timeout waiting for canSaveUser:password:forProtectionSpace: to complete"
+ "Expired timeout waiting for canSaveUser:password:forProtectionSpace: to complete"
+ "Found %lu saved account(s) with a TOTP generator in a passkey sidecar but not in a password sidecar"
+ "Found saved account for '%{sensitive}@' on %{sensitive}@ that will conflict with saved account for '%{sensitive}@' after updating username"
+ "Guided browser connection dropped during teardown; not reconnecting"
+ "PMAutomaticPasswordChangeDebugLogAutoFilledData"
+ "SafariCore.WBSGuidedBrowsingNavigationEvent"
+ "SearchFeatureAvailability"
+ "Unable to decode target URL for navigation event"
+ "WBSGuidedBrowsingNavigationEvent { targetURL (hash) = "
+ "currentURLChanged"
+ "emailProviderFraudTargets"
+ "reportNavigationEvent"
- "EnableDropOutliersInFrequentlyVisited"
- "FrequentlyVisitedSitesAllowLogonURLs"
- "FrequentlyVisitedSitesAllowSitesFromFavorites"
- "Incoming connection from %{private}s is not Apple-signed, rejecting"
- "New strong password has been saved for %ld"
- "New strong passwords have been saved for %ld"
- "New strong passwords have been saved for %ld out of %ld accounts."
- "strongPasswordsMessage"
```
