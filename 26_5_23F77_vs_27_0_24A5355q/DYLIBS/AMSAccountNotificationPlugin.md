## AMSAccountNotificationPlugin

> `/System/Library/Accounts/Notification/AMSAccountNotificationPlugin.bundle/AMSAccountNotificationPlugin`

```diff

-9.5.8.2.2
-  __TEXT.__text: 0x1100c
-  __TEXT.__auth_stubs: 0x7a0
-  __TEXT.__objc_methlist: 0x5dc
-  __TEXT.__const: 0x228
-  __TEXT.__cstring: 0x9d5
-  __TEXT.__gcc_except_tab: 0xc4
-  __TEXT.__oslogstring: 0x2a51
-  __TEXT.__dlopen_cstrs: 0x15e
+10.0.40.4.1
+  __TEXT.__text: 0x10030
+  __TEXT.__objc_methlist: 0x5f4
+  __TEXT.__const: 0x222
+  __TEXT.__cstring: 0xa15
+  __TEXT.__gcc_except_tab: 0x84
+  __TEXT.__oslogstring: 0x2a7e
+  __TEXT.__dlopen_cstrs: 0x106
   __TEXT.__constg_swiftt: 0x8c
   __TEXT.__swift5_typeref: 0xbe
   __TEXT.__swift5_fieldmd: 0x30

   __TEXT.__swift5_types: 0x8
   __TEXT.__swift_as_entry: 0x20
   __TEXT.__swift_as_ret: 0x24
+  __TEXT.__swift_as_cont: 0x38
   __TEXT.__unwind_info: 0x388
-  __TEXT.__eh_frame: 0x420
-  __TEXT.__objc_classname: 0xca
-  __TEXT.__objc_methname: 0x1f3c
-  __TEXT.__objc_methtype: 0x315
-  __TEXT.__objc_stubs: 0x2040
-  __DATA_CONST.__got: 0x190
-  __DATA_CONST.__const: 0x470
+  __TEXT.__eh_frame: 0x438
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x448
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x930
+  __DATA_CONST.__objc_selrefs: 0x970
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__objc_arraydata: 0x28
-  __AUTH_CONST.__auth_got: 0x3e0
-  __AUTH_CONST.__const: 0x228
-  __AUTH_CONST.__cfstring: 0x7e0
+  __DATA_CONST.__got: 0x1a0
+  __AUTH_CONST.__const: 0x1a8
+  __AUTH_CONST.__cfstring: 0x800
   __AUTH_CONST.__objc_const: 0x568
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x28
+  __AUTH_CONST.__auth_got: 0x408
   __AUTH.__objc_data: 0x1b0
   __AUTH.__data: 0x50
   __DATA.__objc_ivar: 0x10
   __DATA.__data: 0x130
-  __DATA.__bss: 0x40
+  __DATA.__bss: 0x30
   __DATA_DIRTY.__objc_data: 0x50
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: A2D1B3A8-5925-3D8C-9AB5-BDC1C7DEE07E
-  Functions: 224
-  Symbols:   186
-  CStrings:  647
+  UUID: 7330B9E5-EA02-3551-9D65-ECCA8CD5C357
+  Functions: 213
+  Symbols:   194
+  CStrings:  294
 
Symbols:
+ _OBJC_CLASS_$_AKAccountManager
+ _OBJC_CLASS_$_AMSAccountPostSignInService
+ _objc_autoreleasePoolPop
+ _objc_autoreleasePoolPush
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x8
+ _swift_release_x19
+ _swift_release_x20
+ _swift_release_x23
+ _swift_release_x24
+ _swift_release_x8
- _dlerror
- _dlsym
- _objc_retain_x26
- _objc_retain_x28
- _swift_retain
- _swift_unknownObjectRetain
CStrings:
+ "%{public}@: [%{public}@] Posting a com.apple.AppleMediaServices.selectedprofilechanged notification."
+ "%{public}@: [%{public}@] The iTunes account already has the updated username. iTunesAccount = %{public}@"
+ "%{public}@: [%{public}@] Triggering post-auth data sync after account save. account = %{public}@"
+ "%{public}@Apple Account consent version copied."
+ "%{public}@Copying Apple Account consent version: %{public}@"
+ "%{public}@Failed to authenticate the iCloud account with iTunes. error = %{public}@"
+ "%{public}@Failed to copy Apple Account consent version. error = %{public}@"
+ "%{public}@IdMS account does not have a consent version."
+ "%{public}@Successfully authenticated the iCloud account with iTunes."
+ "%{public}@The user signed into iCloud. We’ll attempt to authenticate the account with iTunes."
+ "-[AMSAccountNotificationPlugin _processiCloudAccountAddition:inStore:]"
+ "com.apple.AppleMediaServices.selectedprofilechanged"
+ "com.apple.onboarding.appleid"
- "#16@0:8"
- "%{public}@: [%{public}@] The iTunes account already as the updated username. iTunesAccount = %{public}@"
- "%{public}@: [%{public}@] The user signed into iCloud. We'll attempt to authenticate the account with iTunes."
- ".cxx_destruct"
- "@\"<AMSBagProtocol>\""
- "@\"ACAccount\""
- "@\"ICCloudServiceStatusMonitor\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSString\"16@0:8"
- "@16@0:8"
- "@20@0:8i16"
- "@24@0:8:16"
- "@24@0:8@16"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@40@0:8:16@24@32"
- "ACDAccountNotificationPlugin"
- "AMSAccount"
- "AMSAccountNotificationPlugin"
- "AMSAccountNotificationPlugin _processiCloudAccountAddition:inStore:"
- "AMSAccountNotificationPlugin: [%{public}@] An iCloud account was added, recording GDPR acknowledgement for Apple ID."
- "AMSAccountNotificationPlugin: [%{public}@] Apple ID GDPR acknowledgement recorded."
- "AMSAccountNotificationPlugin: [%{public}@] Failed to authenticate the iCloud account with iTunes. error = %{public}@"
- "AMSAccountNotificationPlugin: [%{public}@] Failed to recording Apple ID GDPR acknowledgement.. error = %{public}@"
- "AMSAccountNotificationPlugin: [%{public}@] Successfully authenticated the iCloud account with iTunes."
- "AMSEmptyUsernameBugReport"
- "AMSLogoutTask"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B24@0:8^@16"
- "B28@0:8@16i24"
- "B32@0:8@\"ACAccount\"16@\"ACDAccountStore\"24"
- "B32@0:8@16@24"
- "B32@0:8@16^@24"
- "B36@0:8@16@24i32"
- "B40@0:8@\"ACAccount\"16@\"ACDAccountStore\"24^@32"
- "B40@0:8@16@24@32"
- "B40@0:8@16@24^@32"
- "B44@0:8@\"ACAccount\"16i24@\"ACDAccountStore\"28@\"ACAccount\"36"
- "B44@0:8@16i24@28@36"
- "NSObject"
- "OBPrivacyAppleIDIdentifier"
- "OSLogObject"
- "Q16@0:8"
- "T#,R"
- "T@\"<AMSBagProtocol>\",&,N,V_bag"
- "T@\"ACAccount\",R,N,V_account"
- "T@\"ICCloudServiceStatusMonitor\",&,N,V_iCloudServiceMonitor"
- "T@\"NSDate\",&,N,Sams_setLastAuthenticated:"
- "T@\"NSDictionary\",R,N"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_processingQueue"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "TQ,D,N,Sams_setLastAuthenticationCredentialSource:"
- "TQ,R"
- "URLForKey:"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_TtC28AMSAccountNotificationPlugin32AccountStorefrontChangeResponder"
- "_account"
- "_activeStorefrontIdentifier"
- "_ams_localiTunesAccount"
- "_bag"
- "_canSaveAccount:withOtherAccounts:"
- "_deactivateAllAccountsExcept:inStore:"
- "_deselectAllAccountsExcept:inStore:"
- "_disableAutomaticDownloadKindsWithError:"
- "_disableBookkeeperWithBag:error:"
- "_fetchPersonaIDIfCurrentPersonaIsEnterprise"
- "_handleAccountMediaTypeLogicForAccountWillChange:"
- "_handleCookieLogicForAccountWillChange:oldAccount:inStore:"
- "_handleLocalAccountLogicForAccountWillChange:"
- "_handleMultiUserLogicForAccountWillChange:"
- "_handlePrivacyAcknowledgementLogicForAccountWillChange:oldAccount:inStore:"
- "_handleRemoteDeviceChangeLogicForAccountWillChange:oldAccount:"
- "_handleSandboxAccountLogicForAccountWillChange:inStore:"
- "_handleStorefrontLogicForAccountWillChange:"
- "_handleUserManagementLogicForAccountWillChange:changeType:"
- "_iCloudServiceMonitor"
- "_logDeltasForCookies:oldCookies:"
- "_logDirtyPropertiesForAccount:oldAccount:"
- "_logoutOfAccount:store:"
- "_mergeCookiesForAccount:oldAccount:"
- "_mergeLocalPrivacyAcknowledgementIntoAccount:withStore:"
- "_performDaemonSignOutTasksForAccountWithID:"
- "_postAccountsChangedInternalNotification"
- "_postAccountsChangedNotification"
- "_postAccountsChangedNotificationsIfNeededForAccount:oldAccount:changeType:"
- "_postActiveAccountChangedNotification"
- "_postActiveiCloudAccountChangedNotification"
- "_postEligibilityOverrideNotificationIfNeededForAccount:oldAccount:"
- "_postStorefontChangedNotificationIfNeededForAccount:oldAccount:store:"
- "_postStorefrontChangedNotification"
- "_processAccountAddition:inStore:"
- "_processAccountDeletion:inStore:"
- "_processAccountModification:oldAccount:inStore:"
- "_processChangedAccount:"
- "_processIDMSAccountModification:oldAccount:inStore:"
- "_processPrivacyAcknowledgementForAccount:oldAccount:"
- "_processiCloudAccountAddition:inStore:"
- "_processiTunesAccountAddition:inStore:"
- "_processiTunesAccountModification:oldAccount:inStore:"
- "_processingQueue"
- "_removeAccount:"
- "_removeAuthenticationStateForAccount:store:"
- "_resetBiometricsForAccount:"
- "_resetBundleOwnerState"
- "_resetDeviceOffersIfNeeded"
- "_resetFollowUpsForAccount:"
- "_resetServerDataCacheForAccountWithDSID:"
- "_resetSpringBoardDefaultPNGSnapshots"
- "_resetSubscriptionStatusForAccount:"
- "_revokeMusicKitUserTokensWithError:"
- "_saveAccount:"
- "_sendLogoutRequestWithBag:error:"
- "_setActiveStorefrontIdentifier:"
- "_shouldProcessChangeForAccount:oldAccount:changeType:"
- "_shouldRemoveModifiedAccount:"
- "_shouldSignOutOfModifiedAccount:"
- "_stringForAccountChangeType:"
- "_updateActiveStateForSelected:inStore:"
- "_updateBetaLocalAccountStorefrontIfNeededFromProductionLocalAccount:store:"
- "_updateLocalAccountStorefrontIfNeededForAccount:store:"
- "account"
- "account:didChangeWithType:inStore:oldAccount:"
- "account:didPerformActionsForDataclasses:"
- "account:willChangeWithType:inStore:oldAccount:"
- "account:willPerformActionsForDataclasses:"
- "accountPropertyForKey:"
- "accountStorefrontDidChangeWithAccount:"
- "accountType"
- "accountTypeWithIdentifier:"
- "accountsWithAccountTypeIdentifier:"
- "acknowledgePrivacy"
- "acknowledgementNeededForPrivacyIdentifier:"
- "addErrorBlock:"
- "addObject:"
- "addObjectsFromArray:"
- "addSuccessBlock:"
- "allKeys"
- "allowDuplicateAccounts"
- "ams_DSID"
- "ams_accountFlags"
- "ams_accountID"
- "ams_activeiCloudAccount"
- "ams_activeiTunesAccount"
- "ams_addNullableObject:"
- "ams_altDSID"
- "ams_bagForProcessInfo:"
- "ams_copyStorefrontFromAccount:"
- "ams_delta:"
- "ams_disablePrivacyAcknowledgementSync"
- "ams_enumerateObjectsForArrays:usingBlock:"
- "ams_filterUsingTest:"
- "ams_firstObjectPassingTest:"
- "ams_iTunesAccountForAccount:"
- "ams_iTunesAccounts"
- "ams_isDeleted"
- "ams_isDuplicate:"
- "ams_isEquivalent:"
- "ams_isExpired"
- "ams_isIDMSAccount"
- "ams_isLocalAccount"
- "ams_isLocalBetaAccount"
- "ams_isManagedAppleID"
- "ams_isRegulatoryAccount"
- "ams_isSandboxAccount"
- "ams_isSelectedProfile"
- "ams_isSimpleProfile"
- "ams_isiCloudAccount"
- "ams_isiTunesAccount"
- "ams_lastAuthenticated"
- "ams_lastAuthenticationCredentialSource"
- "ams_lastAuthenticationServerResponse"
- "ams_localiTunesAccountForAccountType:"
- "ams_mapWithTransform:"
- "ams_mediaType"
- "ams_mergePrivacyAcknowledgement:"
- "ams_mergedPrivacyAcknowledgement"
- "ams_migrateCookiePropertiesWithError:"
- "ams_password"
- "ams_privacyAcknowledgement"
- "ams_pushRegistrationThrottleMap"
- "ams_removeAllCookies"
- "ams_removeObjectsPassingTest:"
- "ams_saveAccount:"
- "ams_saveAccount:verifyCredentials:"
- "ams_setAltDSID:"
- "ams_setDSID:"
- "ams_setDisablePrivacyAcknowledgementSync:"
- "ams_setInUse:"
- "ams_setLastAuthenticated:"
- "ams_setLastAuthenticationCredentialSource:"
- "ams_setMergedPrivacyAcknowledgement:"
- "ams_setNullableObject:forKey:"
- "ams_setPassword:"
- "ams_setPushRegistrationThrottleMap:"
- "ams_setRawPassword:"
- "ams_setRegisterSuccessCriteria:"
- "ams_setSecureToken:forAccount:error:"
- "ams_setServerResponse:"
- "ams_setStorefront:"
- "ams_sharedAccountStore"
- "ams_simpleProfileAccounts"
- "ams_storefront"
- "ams_storefrontForMediaType:"
- "ams_syncPrivacyAcknowledgementForAccount:"
- "arrayByAddingObjectsFromArray:"
- "arrayWithObjects:count:"
- "autorelease"
- "bag"
- "bagForProfile:profileVersion:processInfo:"
- "binaryPromiseAdapter"
- "boolValue"
- "bundleID"
- "canRemoveAccount:inStore:"
- "canRemoveAccount:inStore:error:"
- "canSaveAccount:inStore:"
- "canSaveAccount:inStore:error:"
- "class"
- "clearFollowUpWithIdentifier:account:"
- "clearRegistrationDenyList"
- "client"
- "code"
- "conformsToProtocol:"
- "containsObject:"
- "copy"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "createBagForSubProfile"
- "currentPersona"
- "dataTaskPromiseWithRequest:"
- "dataTaskPromiseWithRequestPromise:"
- "dealloc"
- "debugDescription"
- "defaultSession"
- "deleteAccountNoSave:error:"
- "description"
- "deviceGUID"
- "deviceIsAudioAccessory"
- "deviceOffers"
- "dictionaryWithObjects:forKeys:count:"
- "domain"
- "enumerateKeysAndObjectsUsingBlock:"
- "enumerateObjectsUsingBlock:"
- "enumerateObjectsWithOptions:usingBlock:"
- "errorOnlyCompletionHandlerAdapter"
- "fileExistsAtPath:"
- "first"
- "hash"
- "iCloudServiceMonitor"
- "identifier"
- "init"
- "initWithAccount:"
- "initWithAccount:options:"
- "initWithBag:"
- "initWithEnabledMediaKinds:account:bag:"
- "initWithPrivacyIdentifier:"
- "initWithProperties:"
- "isActive"
- "isEnterprisePersona"
- "isEqual:"
- "isEqualToNumber:"
- "isEqualToString:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "isRunningUnitTests"
- "isiCloudAccountBackingOf:"
- "length"
- "logout"
- "mutableCopy"
- "object"
- "objectAtIndexedSubscript:"
- "objectForKeyedSubscript:"
- "parentAccount"
- "pathWithComponents:"
- "pendingFollowUpsForAccount:"
- "perform"
- "performAuthentication"
- "performBinaryTaskWithBlock:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "performSignOutTasksInDaemonForAccount:"
- "processingQueue"
- "promiseWithError:"
- "promiseWithResult:"
- "registerTokensIfNeeded"
- "release"
- "reload"
- "removeAccount:withCompletionHandler:"
- "removeItemAtPath:error:"
- "removeObjectAtIndex:"
- "removeObjectsForKeys:"
- "removeUserDefaultsForAccountIdentifier:"
- "reportEmptyUsernameBug"
- "requestWithMethod:bagURL:parameters:"
- "respondsToSelector:"
- "resultWithCompletion:"
- "resultWithError:"
- "retain"
- "retainCount"
- "revokeMusicKitUserTokensForAccountDSID:withCompletion:"
- "second"
- "self"
- "setAccount:"
- "setAccountProperty:forKey:"
- "setAccountType:"
- "setActive:"
- "setAllowServerDialogs:"
- "setAuthenticated:"
- "setAuthenticationType:"
- "setBag:"
- "setCanMakeAccountActive:"
- "setDebugReason:"
- "setDialogOptions:"
- "setDidFetchBundleOwnerStatus:"
- "setDidRetrieveDeviceOffers:"
- "setDidRetrieveTVOffers:"
- "setDidSetUpServerDataCache:"
- "setFlushTimerEnabled:"
- "setICloudServiceMonitor:"
- "setIgnoreAccountConversion:"
- "setLastCarrierOfferRegistrationDate:"
- "setLogKey:"
- "setLogUUID:"
- "setObject:forKeyedSubscript:"
- "setOrigin:"
- "setProcessingQueue:"
- "setRequestEncoding:"
- "setShowSandboxAccountUI:"
- "setState:forAccount:"
- "setUpCacheForAccountDSID:"
- "setUsername:"
- "sharedAccountsNotificationPluginConfig"
- "sharedAccountsOversizeConfig"
- "sharedAccountsStorefrontConfig"
- "sharedConfig"
- "sharedInstance"
- "sharedManager"
- "sharedPrivacyConfig"
- "showSandboxAccountUI"
- "softlink:r:path:/System/Library/PrivateFrameworks/OnBoardingKit.framework/OnBoardingKit"
- "stringWithFormat:"
- "subscriptionBagSyncDataForAccount:"
- "superclass"
- "syncWithRequest:"
- "tearDownCacheForAccountDSID:"
- "thenWithBlock:"
- "unsignedIntegerValue"
- "updateAccountNoSave:error:"
- "userPersonaUniqueString"
- "username"
- "v16@0:8"
- "v24@0:8@16"
- "v32@0:8@\"ACAccount\"16@\"NSArray\"24"
- "v32@0:8@16@24"
- "v36@0:8@16@24i32"
- "v40@0:8@16@24@32"
- "v44@0:8@\"ACAccount\"16i24@\"ACDAccountStore\"28@\"ACAccount\"36"
- "v44@0:8@16i24@28@36"
- "zone"

```
