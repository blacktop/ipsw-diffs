## SafariCore

> `/System/Library/PrivateFrameworks/SafariCore.framework/SafariCore`

```diff

-626.1.12.10.3
-  __TEXT.__text: 0x21892c
-  __TEXT.__objc_methlist: 0xdbcc
+626.1.17.0.0
+  __TEXT.__text: 0x21a064
+  __TEXT.__objc_methlist: 0xdc54
   __TEXT.__const: 0x8d74
-  __TEXT.__gcc_except_tab: 0x7be8
-  __TEXT.__cstring: 0x1a09b
+  __TEXT.__gcc_except_tab: 0x7cd4
+  __TEXT.__cstring: 0x1a37b
   __TEXT.__ustring: 0x1dd8
-  __TEXT.__oslogstring: 0xed61
+  __TEXT.__oslogstring: 0xef81
   __TEXT.__dlopen_cstrs: 0x157
   __TEXT.__constg_swiftt: 0x26e0
   __TEXT.__swift5_typeref: 0x2b4e

   __TEXT.__swift5_capture: 0x1690
   __TEXT.__swift5_protos: 0x40
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__unwind_info: 0xce10
-  __TEXT.__eh_frame: 0xb938
+  __TEXT.__unwind_info: 0xce68
+  __TEXT.__eh_frame: 0xba00
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x5ee0
+  __DATA_CONST.__const: 0x5f20
   __DATA_CONST.__objc_classlist: 0x760
   __DATA_CONST.__objc_catlist: 0x160
   __DATA_CONST.__objc_protolist: 0x208
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7b70
+  __DATA_CONST.__objc_selrefs: 0x7bc0
   __DATA_CONST.__objc_protorefs: 0xf8
   __DATA_CONST.__objc_superrefs: 0x4b8
   __DATA_CONST.__objc_arraydata: 0x2aa0
   __DATA_CONST.__got: 0x14d8
-  __AUTH_CONST.__const: 0xc7c0
-  __AUTH_CONST.__cfstring: 0x1b600
-  __AUTH_CONST.__objc_const: 0x172e0
+  __AUTH_CONST.__const: 0xc7e0
+  __AUTH_CONST.__cfstring: 0x1b6a0
+  __AUTH_CONST.__objc_const: 0x17310
   __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__objc_intobj: 0x930
   __AUTH_CONST.__objc_dictobj: 0x190
   __AUTH_CONST.__objc_arrayobj: 0x5a0
-  __AUTH_CONST.__auth_got: 0x2388
+  __AUTH_CONST.__auth_got: 0x2390
   __AUTH.__objc_data: 0xc68
   __AUTH.__data: 0x6f8
-  __DATA.__objc_ivar: 0xd44
+  __DATA.__objc_ivar: 0xd48
   __DATA.__data: 0x3d10
   __DATA.__common: 0x88
   __DATA_DIRTY.__objc_data: 0x4548

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 12485
-  Symbols:   12486
-  CStrings:  5541
+  Functions: 12498
+  Symbols:   12497
+  CStrings:  5563
 
Symbols:
+ +[NSURLSessionConfiguration(SafariCoreExtras) safari_ephemeralSessionConfigurationWithSecondaryIdentifier:]
+ +[WBSFeatureAvailability isNotifyMeWhenInternalAnalyticsEnabled]
+ +[WBSSavedAccountStore _sharedStoreWithAutoFillQuirksManager:]
+ +[WBSSavedAccountStore sharedStoreWithAutoFillQuirksManager:]
+ -[WBSAnalyticsLogger reportNotifyMeWhenPollResultWithDetails:errorType:automationID:url:userPrompt:]
+ -[WBSSavedAccountKeychainCoordinator allPersonalSidecarKeychainItemsInPersonalKeychain]
+ -[WBSSavedAccountKeychainCoordinator personalSidecarsFromKeychainItems:]
+ -[WBSSavedAccountStore _loadSavedAccountsFromSharedAccountsGroupsIntoAllSavedAccounts:]
+ -[WBSSavedAccountStore _mergeSavedAccountsFromSharedAccountsGroupsIntoLoadedSavedAccounts]
+ -[WBSSavedAccountStore _resetForReason:]
+ -[WBSSavedAccountStore _resetOnInternalQueueForReason:]
+ -[WBSSavedAccountStore initAndPrewarmSavedAccounts:autoFillQuirksManager:forTesting:]
+ -[WBSSavedAccountStore initWithAuthenticationServicesAgentProxy:shouldPrewarmSavedAccounts:limitedToDomains:autoFillQuirksManager:forTesting:]
+ -[WBSWellKnownURLResponseCodeReliabilityChecker initWithURL:sessionConfiguration:]
+ GCC_except_table144
+ GCC_except_table184
+ GCC_except_table236
+ GCC_except_table239
+ GCC_except_table309
+ GCC_except_table326
+ GCC_except_table373
+ GCC_except_table474
+ GCC_except_table511
+ GCC_except_table514
+ _OBJC_IVAR_$_WBSSavedAccountStore._cachedPersonalSidecarItems
+ _SecTaskCreateFromSelf
+ _WBSDebugNotifyMeWhenInternalAnalyticsEnabledKey
+ _WBSPasswordWarningManagerDidUpdateWarningsNotification
+ __ZL30configureCommonSessionSettingsP25NSURLSessionConfigurationP8NSString
+ __ZZL30configureCommonSessionSettingsP25NSURLSessionConfigurationP8NSStringE9onceToken
+ __ZZL40processCanAttributeNetworkingToOtherAppsvE33canAttributeNetworkingToOtherApps
+ __ZZL40processCanAttributeNetworkingToOtherAppsvE9onceToken
+ ___100-[WBSAnalyticsLogger reportNotifyMeWhenPollResultWithDetails:errorType:automationID:url:userPrompt:]_block_invoke
+ ___142-[WBSSavedAccountStore initWithAuthenticationServicesAgentProxy:shouldPrewarmSavedAccounts:limitedToDomains:autoFillQuirksManager:forTesting:]_block_invoke
+ ___142-[WBSSavedAccountStore initWithAuthenticationServicesAgentProxy:shouldPrewarmSavedAccounts:limitedToDomains:autoFillQuirksManager:forTesting:]_block_invoke_2
+ ___142-[WBSSavedAccountStore initWithAuthenticationServicesAgentProxy:shouldPrewarmSavedAccounts:limitedToDomains:autoFillQuirksManager:forTesting:]_block_invoke_3
+ ___142-[WBSSavedAccountStore initWithAuthenticationServicesAgentProxy:shouldPrewarmSavedAccounts:limitedToDomains:autoFillQuirksManager:forTesting:]_block_invoke_4
+ ___40-[WBSSavedAccountStore _resetForReason:]_block_invoke
+ ___40-[WBSSavedAccountStore _resetForReason:]_block_invoke_2
+ ___55-[WBSSavedAccountStore _resetOnInternalQueueForReason:]_block_invoke
+ ___62+[WBSSavedAccountStore _sharedStoreWithAutoFillQuirksManager:]_block_invoke
+ ___72-[WBSSavedAccountKeychainCoordinator personalSidecarsFromKeychainItems:]_block_invoke
+ ___90-[WBSSavedAccountStore _mergeSavedAccountsFromSharedAccountsGroupsIntoLoadedSavedAccounts]_block_invoke
+ ____ZL30configureCommonSessionSettingsP25NSURLSessionConfigurationP8NSString_block_invoke
+ ____ZL40processCanAttributeNetworkingToOtherAppsv_block_invoke
+ ___block_descriptor_56_e8_32s40s48r_e43_v16?0"WBSPasswordWarningTopFraudTargets"8ls32l8r48l8s40l8
+ ___block_descriptor_57_e8_32s40s48r_e5_v8?0ls32l8s40l8r48l8
+ ___block_descriptor_72_ea8_32s40s48s_e19_"NSDictionary"8?0ls32l8s40l8s48l8
+ ___savedAccountsWithPasswordCredentials_block_invoke
+ __sharedStoreWithAutoFillQuirksManager:.onceToken
+ _os_unfair_recursive_lock_lock
- +[WBSFeatureAvailability isMacSearchFieldRewriteEnabled]
- -[WBSSavedAccountKeychainCoordinator _allPersonalSidecarEntriesInPersonalKeychain]
- -[WBSSavedAccountStore _resetOnInternalQueue]
- -[WBSSavedAccountStore initWithAuthenticationServicesAgentProxy:shouldPrewarmSavedAccounts:limitedToDomains:forTesting:]
- GCC_except_table119
- GCC_except_table137
- GCC_except_table140
- GCC_except_table182
- GCC_except_table216
- GCC_except_table234
- GCC_except_table241
- GCC_except_table323
- GCC_except_table330
- GCC_except_table361
- GCC_except_table370
- GCC_except_table430
- GCC_except_table432
- GCC_except_table437
- GCC_except_table468
- GCC_except_table76
- GCC_except_table89
- GCC_except_table91
- __ZL30configureCommonSessionSettingsP25NSURLSessionConfiguration
- ___120-[WBSSavedAccountStore initWithAuthenticationServicesAgentProxy:shouldPrewarmSavedAccounts:limitedToDomains:forTesting:]_block_invoke
- ___120-[WBSSavedAccountStore initWithAuthenticationServicesAgentProxy:shouldPrewarmSavedAccounts:limitedToDomains:forTesting:]_block_invoke_2
- ___120-[WBSSavedAccountStore initWithAuthenticationServicesAgentProxy:shouldPrewarmSavedAccounts:limitedToDomains:forTesting:]_block_invoke_3
- ___120-[WBSSavedAccountStore initWithAuthenticationServicesAgentProxy:shouldPrewarmSavedAccounts:limitedToDomains:forTesting:]_block_invoke_4
- ___29-[WBSSavedAccountStore reset]_block_invoke
- ___29-[WBSSavedAccountStore reset]_block_invoke_2
- ___35+[WBSSavedAccountStore sharedStore]_block_invoke
- ___45-[WBSSavedAccountStore _resetOnInternalQueue]_block_invoke
- ___56+[WBSFeatureAvailability isMacSearchFieldRewriteEnabled]_block_invoke
- ___75-[WBSSavedAccountKeychainCoordinator allPersonalSidecarsInPersonalKeychain]_block_invoke
- ___76-[WBSSavedAccountStore setShouldShowServiceNamesForPasswordAndPasskeyItems:]_block_invoke_4
- ___90-[WBSSavedAccountKeychainCoordinator allRecentlyDeletedPersonalSidecarsInPersonalKeychain]_block_invoke
- ___block_descriptor_40_e8_32s_e43_v16?0"WBSPasswordWarningTopFraudTargets"8ls32l8
- ___block_descriptor_49_e8_32s40s_e5_v8?0ls32l8s40l8
- _isMacSearchFieldRewriteEnabled.isMacSearchFieldRewriteEnabled
- _isMacSearchFieldRewriteEnabled.onceToken
- _os_unfair_recursive_lock_lock_with_options
CStrings:
+ "Attributing network session to Safari, but %{public}@ lacks the socket delegate entitlement and has no secondary identifier; DNS resolution may be rejected with NoAuth"
+ "Not attributing network sessions with secondary identifier %{public}@ to Safari: %{public}@ lacks the socket delegate entitlement"
+ "Recently Deleted maintenance changed the keychain"
+ "Resetting saved account store because %{public}s"
+ "Shared account groups changed (%lu groups); resetting saved account store"
+ "Shared account groups loaded (%lu groups); merging their saved accounts into the loaded saved accounts"
+ "Skipping account store reset because the key bag is locked (reset reason: %{public}s)"
+ "WBSDebugNotifyMeWhenInternalAnalyticsEnabled"
+ "WBSPasswordWarningManagerDidUpdateWarningsNotification"
+ "a client requested a reset"
+ "automationID"
+ "com.apple.Safari.NotifyMeWhen.PollResultWithDetails"
+ "com.apple.private.network.socket-delegate"
+ "contributed saved accounts were moved back to the personal keychain"
+ "items from exited groups were cleaned up"
+ "loading saved accounts after loading groups was requested"
+ "passwords with invalid authentication types were migrated"
+ "saved accounts were moved out of a group"
+ "saved accounts with unknown original contributors were cleaned up"
+ "shared account groups changed"
+ "the AuthenticationServicesAgent maintenance activity ended"
+ "the AutoFill quirks manager changed"
+ "the keychain changed"
+ "the service names setting changed"
+ "userPrompt"
- "EnableMacSearchFieldRewrite"
- "No topic: the topic must be a non-empty string."
- "Skipping account store reset because the key bag is locked"
```
