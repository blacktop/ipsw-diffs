## VideoSubscriberAccountUI

> `/System/Library/PrivateFrameworks/VideoSubscriberAccountUI.framework/VideoSubscriberAccountUI`

```diff

-593.40.9.0.0
-  __TEXT.__text: 0x5ffc8
-  __TEXT.__auth_stubs: 0xae0
-  __TEXT.__objc_methlist: 0x87a0
-  __TEXT.__const: 0x2e2
-  __TEXT.__cstring: 0x53ea
-  __TEXT.__gcc_except_tab: 0xfa8
-  __TEXT.__oslogstring: 0x341b
+593.50.1.0.0
+  __TEXT.__text: 0x69bbc
+  __TEXT.__auth_stubs: 0xb00
+  __TEXT.__objc_methlist: 0x8e58
+  __TEXT.__const: 0x2f2
+  __TEXT.__gcc_except_tab: 0x10a4
+  __TEXT.__cstring: 0x590d
+  __TEXT.__oslogstring: 0x43cb
   __TEXT.__ustring: 0x10
   __TEXT.__swift5_typeref: 0x53
   __TEXT.__swift5_reflstr: 0x21

   __TEXT.__swift5_fieldmd: 0x28
   __TEXT.__swift5_proto: 0x10
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x1c58
+  __TEXT.__unwind_info: 0x1ef0
   __TEXT.__eh_frame: 0x40
-  __TEXT.__objc_classname: 0x13d9
-  __TEXT.__objc_methname: 0x14db2
-  __TEXT.__objc_methtype: 0x356a
-  __TEXT.__objc_stubs: 0xe1a0
-  __DATA_CONST.__got: 0xa10
-  __DATA_CONST.__const: 0x1990
-  __DATA_CONST.__objc_classlist: 0x3f8
+  __TEXT.__objc_classname: 0x1469
+  __TEXT.__objc_methname: 0x160ca
+  __TEXT.__objc_methtype: 0x363e
+  __TEXT.__objc_stubs: 0xef60
+  __DATA_CONST.__got: 0xa78
+  __DATA_CONST.__const: 0x1d80
+  __DATA_CONST.__objc_classlist: 0x418
   __DATA_CONST.__objc_catlist: 0x50
-  __DATA_CONST.__objc_protolist: 0x1f8
+  __DATA_CONST.__objc_protolist: 0x200
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4b00
+  __DATA_CONST.__objc_selrefs: 0x4e50
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0x310
+  __DATA_CONST.__objc_superrefs: 0x328
   __DATA_CONST.__objc_arraydata: 0x60
-  __AUTH_CONST.__auth_got: 0x580
-  __AUTH_CONST.__const: 0x7b2
-  __AUTH_CONST.__cfstring: 0x4600
-  __AUTH_CONST.__objc_const: 0x15550
+  __AUTH_CONST.__auth_got: 0x590
+  __AUTH_CONST.__const: 0x892
+  __AUTH_CONST.__cfstring: 0x4860
+  __AUTH_CONST.__objc_const: 0x163b0
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_floatobj: 0x30
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH.__objc_data: 0x2530
-  __DATA.__objc_ivar: 0x978
-  __DATA.__data: 0x1848
-  __DATA.__bss: 0x1c0
+  __AUTH.__objc_data: 0x2670
+  __DATA.__objc_ivar: 0x9fc
+  __DATA.__data: 0x18a8
+  __DATA.__bss: 0x1e0
   __DATA_DIRTY.__objc_data: 0x280
   __DATA_DIRTY.__data: 0x8
   __DATA_DIRTY.__bss: 0x110

   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/OnBoardingKit.framework/OnBoardingKit
   - /System/Library/PrivateFrameworks/Preferences.framework/Preferences
+  - /System/Library/PrivateFrameworks/UIFoundation.framework/UIFoundation
   - /System/Library/PrivateFrameworks/VideosUI.framework/VideosUI
   - /System/Library/PrivateFrameworks/WatchListKit.framework/WatchListKit
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: C4266CA5-9F58-3355-AD13-7D64D02351F9
-  Functions: 2745
-  Symbols:   10206
-  CStrings:  5542
+  UUID: 62478F92-5B57-3C0C-BE66-B5815A80C8ED
+  Functions: 2977
+  Symbols:   10933
+  CStrings:  5842
 
Symbols:
+ +[VSSetupFlowConfiguration supportsSecureCoding]
+ +[VSSetupFlowController sharedInstance]
+ +[VSSetupFlowController sharedInstance].cold.1
+ -[VSSetupFlowConfiguration .cxx_destruct]
+ -[VSSetupFlowConfiguration bundlesIDsToConsent]
+ -[VSSetupFlowConfiguration canShowSupportedAppsButton]
+ -[VSSetupFlowConfiguration copyWithZone:]
+ -[VSSetupFlowConfiguration description]
+ -[VSSetupFlowConfiguration encodeWithCoder:]
+ -[VSSetupFlowConfiguration hash]
+ -[VSSetupFlowConfiguration identityProvider]
+ -[VSSetupFlowConfiguration initWithCoder:]
+ -[VSSetupFlowConfiguration init]
+ -[VSSetupFlowConfiguration isEqual:]
+ -[VSSetupFlowConfiguration msoAppDescription]
+ -[VSSetupFlowConfiguration preferredAppID]
+ -[VSSetupFlowConfiguration providerAccountUsername]
+ -[VSSetupFlowConfiguration setBundlesIDsToConsent:]
+ -[VSSetupFlowConfiguration setCanShowSupportedAppsButton:]
+ -[VSSetupFlowConfiguration setIdentityProvider:]
+ -[VSSetupFlowConfiguration setMsoAppDescription:]
+ -[VSSetupFlowConfiguration setPreferredAppID:]
+ -[VSSetupFlowConfiguration setProviderAccountUsername:]
+ -[VSSetupFlowConfiguration setShouldOfferAuthenticationFlow:]
+ -[VSSetupFlowConfiguration setShouldOfferSTBAuthenticationFlow:]
+ -[VSSetupFlowConfiguration setShouldOfferSoleAuthenticationFlow:]
+ -[VSSetupFlowConfiguration setShouldSkipSetupEntirely:]
+ -[VSSetupFlowConfiguration setSupportedApps:]
+ -[VSSetupFlowConfiguration setVouchersByBundleID:]
+ -[VSSetupFlowConfiguration shouldOfferAuthenticationFlow]
+ -[VSSetupFlowConfiguration shouldOfferSTBAuthenticationFlow]
+ -[VSSetupFlowConfiguration shouldOfferSoleAuthenticationFlow]
+ -[VSSetupFlowConfiguration shouldSkipSetupEntirely]
+ -[VSSetupFlowConfiguration supportedApps]
+ -[VSSetupFlowConfiguration vouchersByBundleID]
+ -[VSSetupFlowController .cxx_destruct]
+ -[VSSetupFlowController _appleAccountDidChange:]
+ -[VSSetupFlowController _didStartLoading]
+ -[VSSetupFlowController _dismissViewController:completion:]
+ -[VSSetupFlowController _finishAfterOfferingOptions:endingUndoGrouping:]
+ -[VSSetupFlowController _getProviderWithUserTokenFromAllProviders:]
+ -[VSSetupFlowController _obtainConsentForBundleIDs:vouchers:withAppleAccountName:identityProvider:endingUndoGrouping:arrivedViaNotNowButton:arrivedAfterSigningIn:goingBack:]
+ -[VSSetupFlowController _offerAuthenticationForProvider:withSupportedAppsButton:msoAppDescription:]
+ -[VSSetupFlowController _offerAuthenticationForSTBProvider:msoAppDescription:providerAccountUsername:]
+ -[VSSetupFlowController _offerAuthenticationWithSupportedAppsButton:]
+ -[VSSetupFlowController _offerFreeOnBoardingIfNeededAfterOfferingOptions:endingUndoGrouping:arrivedViaNotNowButton:arrivedAfterSigningIn:goingBack:]
+ -[VSSetupFlowController _pickProviderWithViewController:]
+ -[VSSetupFlowController _presentError:]
+ -[VSSetupFlowController _presentError:].cold.1
+ -[VSSetupFlowController _presentViewController:completion:]
+ -[VSSetupFlowController _requestAccessWithViewController:]
+ -[VSSetupFlowController _startLoadingAfterOfferingOptions:endingUndoGrouping:arrivedViaNotNowButton:arrivedAfterSigningIn:goingBack:]
+ -[VSSetupFlowController appDescription]
+ -[VSSetupFlowController currentDevice]
+ -[VSSetupFlowController dealloc]
+ -[VSSetupFlowController delegate]
+ -[VSSetupFlowController didSelectNoAppsforInstall]
+ -[VSSetupFlowController dismissIdentityProviderViewController:]
+ -[VSSetupFlowController finishOrIsGoingBack:didOfferOptions:endingUndoGrouping:]
+ -[VSSetupFlowController finishSTBSuccessFlowForProvider:shouldShowBulkConsent:]
+ -[VSSetupFlowController finishSTBSuccessFlowForProvider:shouldShowBulkConsent:].cold.1
+ -[VSSetupFlowController finishSTBSuccessFlowForProvider:shouldShowBulkConsent:].cold.2
+ -[VSSetupFlowController finishSTBSuccessFlowForProvider:shouldShowBulkConsent:].cold.3
+ -[VSSetupFlowController finishSTBSuccessFlowForProvider:shouldShowBulkConsent:].cold.4
+ -[VSSetupFlowController forceSignOutWithAccount:]
+ -[VSSetupFlowController freeOnBoardingBundleIDs]
+ -[VSSetupFlowController goingBackActivationCompletionBlock]
+ -[VSSetupFlowController identityProviderPickerViewController:didPickIdentityProvider:]
+ -[VSSetupFlowController identityProviderRequestManager:finishedRequest:withResult:]
+ -[VSSetupFlowController identityProviderViewController:didAuthenticateAccount:forRequest:]
+ -[VSSetupFlowController identityProviderViewController:didFinishRequest:withResult:]
+ -[VSSetupFlowController identityProviderViewControllerDidCancel:]
+ -[VSSetupFlowController init]
+ -[VSSetupFlowController isInSTBMode]
+ -[VSSetupFlowController isSigningIn]
+ -[VSSetupFlowController markShouldSkipSetup]
+ -[VSSetupFlowController notNowWithIdentityProvider:]
+ -[VSSetupFlowController notNow]
+ -[VSSetupFlowController notifyDelegateFromActivation]
+ -[VSSetupFlowController performDismissalOfIdentityProviderViewController:]
+ -[VSSetupFlowController preferences]
+ -[VSSetupFlowController privateQueue]
+ -[VSSetupFlowController providerAccountUsername]
+ -[VSSetupFlowController remoteNotifier:didReceiveRemoteNotificationWithUserInfo:]
+ -[VSSetupFlowController remoteNotifier]
+ -[VSSetupFlowController requestManager]
+ -[VSSetupFlowController serializationCenter]
+ -[VSSetupFlowController setAppDescription:]
+ -[VSSetupFlowController setCurrentDevice:]
+ -[VSSetupFlowController setDelegate:]
+ -[VSSetupFlowController setDidSelectNoAppsforInstall:]
+ -[VSSetupFlowController setFreeOnBoardingBundleIDs:]
+ -[VSSetupFlowController setGoingBackActivationCompletionBlock:]
+ -[VSSetupFlowController setNotifyDelegateFromActivation:]
+ -[VSSetupFlowController setPreferences:]
+ -[VSSetupFlowController setPrivateQueue:]
+ -[VSSetupFlowController setProviderAccountUsername:]
+ -[VSSetupFlowController setRemoteNotifier:]
+ -[VSSetupFlowController setRequestManager:]
+ -[VSSetupFlowController setSerializationCenter:]
+ -[VSSetupFlowController setSigningIn:]
+ -[VSSetupFlowController setStorage:]
+ -[VSSetupFlowController setSupportedApps:]
+ -[VSSetupFlowController showMultiAppInstallVC:]
+ -[VSSetupFlowController showSupportedApps]
+ -[VSSetupFlowController signOutForNotNowFlowWithIdentityProvider:]
+ -[VSSetupFlowController signOutForNotNowFlowWithIdentityProvider:].cold.1
+ -[VSSetupFlowController signOutForNotNowFlowWithIdentityProvider:].cold.2
+ -[VSSetupFlowController startLoadingWhenGoingBack:serializedAccountDataToImport:]
+ -[VSSetupFlowController startSigningInForIdentityProvider:]
+ -[VSSetupFlowController startSigningInForIdentityProvider:].cold.1
+ -[VSSetupFlowController startSigningIn]
+ -[VSSetupFlowController startSilentSigningInForSTBFromActivation:withCompletion:]
+ -[VSSetupFlowController storage]
+ -[VSSetupFlowController supportedAppsViewControllerDidFinish:]
+ -[VSSetupFlowController supportedApps]
+ -[VSSetupFlowPreparationOperation .cxx_destruct]
+ -[VSSetupFlowPreparationOperation _checkAvailability]
+ -[VSSetupFlowPreparationOperation _checkForExistingAccounts]
+ -[VSSetupFlowPreparationOperation _checkForSupportedAppsButtonWithFlow:]
+ -[VSSetupFlowPreparationOperation _checkForSupportedAppsButton]
+ -[VSSetupFlowPreparationOperation _checkForSupportedAppsFromProvider:withCompletion:]
+ -[VSSetupFlowPreparationOperation _checkPreferences]
+ -[VSSetupFlowPreparationOperation _fetchAllProvidersIfNeeded]
+ -[VSSetupFlowPreparationOperation _fetchAllProviders]
+ -[VSSetupFlowPreparationOperation _fetchProviderForAccount:]
+ -[VSSetupFlowPreparationOperation _finishWithError:]
+ -[VSSetupFlowPreparationOperation _finishWithError:].cold.1
+ -[VSSetupFlowPreparationOperation _finishWithFlow:]
+ -[VSSetupFlowPreparationOperation _getPersonalAppDescriptions:identityProvider:completion:]
+ -[VSSetupFlowPreparationOperation _getSTBProviderFromAllProviders:completionHandler:]
+ -[VSSetupFlowPreparationOperation _isInSTBMode]
+ -[VSSetupFlowPreparationOperation _loadProviderAppDescriptionWithFlow:]
+ -[VSSetupFlowPreparationOperation _loadProviderAppDescriptionWithFlow:].cold.1
+ -[VSSetupFlowPreparationOperation _loadProviderAppDescriptionWithFlow:].cold.2
+ -[VSSetupFlowPreparationOperation _resolveBundleIDs:forFlow:]
+ -[VSSetupFlowPreparationOperation currentDevice]
+ -[VSSetupFlowPreparationOperation executionDidBegin]
+ -[VSSetupFlowPreparationOperation init]
+ -[VSSetupFlowPreparationOperation preferences]
+ -[VSSetupFlowPreparationOperation prepareSTBSetupForAccount:forProvider:]
+ -[VSSetupFlowPreparationOperation privateQueue]
+ -[VSSetupFlowPreparationOperation result]
+ -[VSSetupFlowPreparationOperation setCurrentDevice:]
+ -[VSSetupFlowPreparationOperation setPreferences:]
+ -[VSSetupFlowPreparationOperation setPrivateQueue:]
+ -[VSSetupFlowPreparationOperation setResult:]
+ -[VSSetupFlowPreparationOperation setStorage:]
+ -[VSSetupFlowPreparationOperation storage]
+ GCC_except_table20
+ GCC_except_table33
+ GCC_except_table44
+ _OBJC_CLASS_$_VSAccountMonitor
+ _OBJC_CLASS_$_VSAccountSerializationCenter
+ _OBJC_CLASS_$_VSAppChannelsFilter
+ _OBJC_CLASS_$_VSPrivacyConsentVoucher
+ _OBJC_CLASS_$_VSRequestAppInstallUtility
+ _OBJC_CLASS_$_VSSetupFlowConfiguration
+ _OBJC_CLASS_$_VSSetupFlowController
+ _OBJC_CLASS_$_VSSetupFlowPreparationOperation
+ _OBJC_IVAR_$_VSSetupFlowConfiguration._bundlesIDsToConsent
+ _OBJC_IVAR_$_VSSetupFlowConfiguration._canShowSupportedAppsButton
+ _OBJC_IVAR_$_VSSetupFlowConfiguration._identityProvider
+ _OBJC_IVAR_$_VSSetupFlowConfiguration._msoAppDescription
+ _OBJC_IVAR_$_VSSetupFlowConfiguration._preferredAppID
+ _OBJC_IVAR_$_VSSetupFlowConfiguration._providerAccountUsername
+ _OBJC_IVAR_$_VSSetupFlowConfiguration._shouldOfferAuthenticationFlow
+ _OBJC_IVAR_$_VSSetupFlowConfiguration._shouldOfferSTBAuthenticationFlow
+ _OBJC_IVAR_$_VSSetupFlowConfiguration._shouldOfferSoleAuthenticationFlow
+ _OBJC_IVAR_$_VSSetupFlowConfiguration._shouldSkipSetupEntirely
+ _OBJC_IVAR_$_VSSetupFlowConfiguration._supportedApps
+ _OBJC_IVAR_$_VSSetupFlowConfiguration._vouchersByBundleID
+ _OBJC_IVAR_$_VSSetupFlowController._appDescription
+ _OBJC_IVAR_$_VSSetupFlowController._currentDevice
+ _OBJC_IVAR_$_VSSetupFlowController._delegate
+ _OBJC_IVAR_$_VSSetupFlowController._didSelectNoAppsforInstall
+ _OBJC_IVAR_$_VSSetupFlowController._freeOnBoardingBundleIDs
+ _OBJC_IVAR_$_VSSetupFlowController._goingBackActivationCompletionBlock
+ _OBJC_IVAR_$_VSSetupFlowController._notifyDelegateFromActivation
+ _OBJC_IVAR_$_VSSetupFlowController._preferences
+ _OBJC_IVAR_$_VSSetupFlowController._privateQueue
+ _OBJC_IVAR_$_VSSetupFlowController._providerAccountUsername
+ _OBJC_IVAR_$_VSSetupFlowController._remoteNotifier
+ _OBJC_IVAR_$_VSSetupFlowController._requestManager
+ _OBJC_IVAR_$_VSSetupFlowController._serializationCenter
+ _OBJC_IVAR_$_VSSetupFlowController._signingIn
+ _OBJC_IVAR_$_VSSetupFlowController._storage
+ _OBJC_IVAR_$_VSSetupFlowController._supportedApps
+ _OBJC_IVAR_$_VSSetupFlowPreparationOperation._currentDevice
+ _OBJC_IVAR_$_VSSetupFlowPreparationOperation._preferences
+ _OBJC_IVAR_$_VSSetupFlowPreparationOperation._privateQueue
+ _OBJC_IVAR_$_VSSetupFlowPreparationOperation._result
+ _OBJC_IVAR_$_VSSetupFlowPreparationOperation._storage
+ _OBJC_METACLASS_$_VSRequestAppInstallUtility
+ _OBJC_METACLASS_$_VSSetupFlowConfiguration
+ _OBJC_METACLASS_$_VSSetupFlowController
+ _OBJC_METACLASS_$_VSSetupFlowPreparationOperation
+ _VSAMSBagKeyCountryCode
+ _VSAMSBagKeySoleProviderFeatureEnabled
+ _VSAccountMonitorAccountStoreDidChange
+ _VSAssertNotMainThread
+ _VSErrorDomain
+ _VSPrivateErrorWithRecoverySuggestion
+ _VSSetupFlowConfigurationValueType
+ _VSSetupFlowConfigurationValueType.__vs_lazy_init_predicate
+ _VSSetupFlowConfigurationValueType.__vs_lazy_init_variable
+ _VSSetupFlowConfigurationValueType.cold.1
+ __OBJC_$_CLASS_METHODS_VSSetupFlowConfiguration
+ __OBJC_$_CLASS_METHODS_VSSetupFlowController
+ __OBJC_$_INSTANCE_METHODS_VSSetupFlowConfiguration
+ __OBJC_$_INSTANCE_METHODS_VSSetupFlowController
+ __OBJC_$_INSTANCE_METHODS_VSSetupFlowPreparationOperation
+ __OBJC_$_INSTANCE_VARIABLES_VSSetupFlowConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_VSSetupFlowController
+ __OBJC_$_INSTANCE_VARIABLES_VSSetupFlowPreparationOperation
+ __OBJC_$_PROP_LIST_VSSetupFlowConfiguration
+ __OBJC_$_PROP_LIST_VSSetupFlowController
+ __OBJC_$_PROP_LIST_VSSetupFlowPreparationOperation
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_VSSupportedAppsViewControllerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_VSSupportedAppsViewControllerDelegate
+ __OBJC_$_PROTOCOL_REFS_VSSupportedAppsViewControllerDelegate
+ __OBJC_CLASS_PROTOCOLS_$_VSSetupFlowController
+ __OBJC_CLASS_RO_$_VSRequestAppInstallUtility
+ __OBJC_CLASS_RO_$_VSSetupFlowConfiguration
+ __OBJC_CLASS_RO_$_VSSetupFlowController
+ __OBJC_CLASS_RO_$_VSSetupFlowPreparationOperation
+ __OBJC_LABEL_PROTOCOL_$_VSSupportedAppsViewControllerDelegate
+ __OBJC_METACLASS_RO_$_VSRequestAppInstallUtility
+ __OBJC_METACLASS_RO_$_VSSetupFlowConfiguration
+ __OBJC_METACLASS_RO_$_VSSetupFlowController
+ __OBJC_METACLASS_RO_$_VSSetupFlowPreparationOperation
+ __OBJC_PROTOCOL_$_VSSupportedAppsViewControllerDelegate
+ ___133-[VSSetupFlowController _startLoadingAfterOfferingOptions:endingUndoGrouping:arrivedViaNotNowButton:arrivedAfterSigningIn:goingBack:]_block_invoke
+ ___133-[VSSetupFlowController _startLoadingAfterOfferingOptions:endingUndoGrouping:arrivedViaNotNowButton:arrivedAfterSigningIn:goingBack:]_block_invoke.26
+ ___133-[VSSetupFlowController _startLoadingAfterOfferingOptions:endingUndoGrouping:arrivedViaNotNowButton:arrivedAfterSigningIn:goingBack:]_block_invoke.33
+ ___133-[VSSetupFlowController _startLoadingAfterOfferingOptions:endingUndoGrouping:arrivedViaNotNowButton:arrivedAfterSigningIn:goingBack:]_block_invoke.33.cold.1
+ ___133-[VSSetupFlowController _startLoadingAfterOfferingOptions:endingUndoGrouping:arrivedViaNotNowButton:arrivedAfterSigningIn:goingBack:]_block_invoke_2
+ ___173-[VSSetupFlowController _obtainConsentForBundleIDs:vouchers:withAppleAccountName:identityProvider:endingUndoGrouping:arrivedViaNotNowButton:arrivedAfterSigningIn:goingBack:]_block_invoke
+ ___39+[VSSetupFlowController sharedInstance]_block_invoke
+ ___39-[VSSetupFlowController startSigningIn]_block_invoke
+ ___39-[VSSetupFlowController startSigningIn]_block_invoke.39
+ ___39-[VSSetupFlowController startSigningIn]_block_invoke_2
+ ___39-[VSSetupFlowController startSigningIn]_block_invoke_2.41
+ ___39-[VSSetupFlowController startSigningIn]_block_invoke_3
+ ___39-[VSSetupFlowController startSigningIn]_block_invoke_4
+ ___39-[VSSetupFlowController startSigningIn]_block_invoke_5
+ ___49-[VSSetupFlowController forceSignOutWithAccount:]_block_invoke
+ ___53-[VSSetupFlowPreparationOperation _checkAvailability]_block_invoke
+ ___53-[VSSetupFlowPreparationOperation _fetchAllProviders]_block_invoke
+ ___53-[VSSetupFlowPreparationOperation _fetchAllProviders]_block_invoke.33
+ ___53-[VSSetupFlowPreparationOperation _fetchAllProviders]_block_invoke.47
+ ___53-[VSSetupFlowPreparationOperation _fetchAllProviders]_block_invoke.47.cold.1
+ ___53-[VSSetupFlowPreparationOperation _fetchAllProviders]_block_invoke_2
+ ___53-[VSSetupFlowPreparationOperation _fetchAllProviders]_block_invoke_2.34
+ ___53-[VSSetupFlowPreparationOperation _fetchAllProviders]_block_invoke_2.34.cold.1
+ ___60-[VSSetupFlowPreparationOperation _checkForExistingAccounts]_block_invoke
+ ___60-[VSSetupFlowPreparationOperation _checkForExistingAccounts]_block_invoke.13
+ ___60-[VSSetupFlowPreparationOperation _checkForExistingAccounts]_block_invoke.13.cold.1
+ ___60-[VSSetupFlowPreparationOperation _checkForExistingAccounts]_block_invoke_2
+ ___60-[VSSetupFlowPreparationOperation _fetchProviderForAccount:]_block_invoke
+ ___60-[VSSetupFlowPreparationOperation _fetchProviderForAccount:]_block_invoke.50
+ ___60-[VSSetupFlowPreparationOperation _fetchProviderForAccount:]_block_invoke.51
+ ___60-[VSSetupFlowPreparationOperation _fetchProviderForAccount:]_block_invoke_2
+ ___60-[VSSetupFlowPreparationOperation _fetchProviderForAccount:]_block_invoke_2.cold.1
+ ___61-[VSSetupFlowPreparationOperation _fetchAllProvidersIfNeeded]_block_invoke
+ ___61-[VSSetupFlowPreparationOperation _fetchAllProvidersIfNeeded]_block_invoke_2
+ ___61-[VSSetupFlowPreparationOperation _resolveBundleIDs:forFlow:]_block_invoke
+ ___71-[VSSetupFlowPreparationOperation _loadProviderAppDescriptionWithFlow:]_block_invoke
+ ___72-[VSSetupFlowPreparationOperation _checkForSupportedAppsButtonWithFlow:]_block_invoke
+ ___72-[VSSetupFlowPreparationOperation _checkForSupportedAppsButtonWithFlow:]_block_invoke.93
+ ___72-[VSSetupFlowPreparationOperation _checkForSupportedAppsButtonWithFlow:]_block_invoke.93.cold.1
+ ___72-[VSSetupFlowPreparationOperation _checkForSupportedAppsButtonWithFlow:]_block_invoke_2
+ ___81-[VSSetupFlowController startLoadingWhenGoingBack:serializedAccountDataToImport:]_block_invoke
+ ___81-[VSSetupFlowController startLoadingWhenGoingBack:serializedAccountDataToImport:]_block_invoke.20
+ ___81-[VSSetupFlowController startLoadingWhenGoingBack:serializedAccountDataToImport:]_block_invoke_2
+ ___81-[VSSetupFlowController startLoadingWhenGoingBack:serializedAccountDataToImport:]_block_invoke_2.21
+ ___81-[VSSetupFlowController startSilentSigningInForSTBFromActivation:withCompletion:]_block_invoke
+ ___81-[VSSetupFlowController startSilentSigningInForSTBFromActivation:withCompletion:]_block_invoke.60
+ ___81-[VSSetupFlowController startSilentSigningInForSTBFromActivation:withCompletion:]_block_invoke.60.cold.1
+ ___81-[VSSetupFlowController startSilentSigningInForSTBFromActivation:withCompletion:]_block_invoke_2
+ ___81-[VSSetupFlowController startSilentSigningInForSTBFromActivation:withCompletion:]_block_invoke_3
+ ___81-[VSSetupFlowController startSilentSigningInForSTBFromActivation:withCompletion:]_block_invoke_4
+ ___83-[VSSetupFlowController identityProviderRequestManager:finishedRequest:withResult:]_block_invoke
+ ___83-[VSSetupFlowController identityProviderRequestManager:finishedRequest:withResult:]_block_invoke.65
+ ___83-[VSSetupFlowController identityProviderRequestManager:finishedRequest:withResult:]_block_invoke.65.cold.1
+ ___84-[VSSetupFlowController identityProviderViewController:didFinishRequest:withResult:]_block_invoke
+ ___84-[VSSetupFlowController identityProviderViewController:didFinishRequest:withResult:]_block_invoke.73
+ ___84-[VSSetupFlowController identityProviderViewController:didFinishRequest:withResult:]_block_invoke.73.cold.1
+ ___84-[VSSetupFlowController identityProviderViewController:didFinishRequest:withResult:]_block_invoke.73.cold.2
+ ___84-[VSSetupFlowController identityProviderViewController:didFinishRequest:withResult:]_block_invoke.74
+ ___85-[VSSetupFlowPreparationOperation _checkForSupportedAppsFromProvider:withCompletion:]_block_invoke
+ ___85-[VSSetupFlowPreparationOperation _checkForSupportedAppsFromProvider:withCompletion:]_block_invoke.56
+ ___85-[VSSetupFlowPreparationOperation _checkForSupportedAppsFromProvider:withCompletion:]_block_invoke.56.cold.1
+ ___85-[VSSetupFlowPreparationOperation _checkForSupportedAppsFromProvider:withCompletion:]_block_invoke.61
+ ___85-[VSSetupFlowPreparationOperation _checkForSupportedAppsFromProvider:withCompletion:]_block_invoke_2
+ ___85-[VSSetupFlowPreparationOperation _checkForSupportedAppsFromProvider:withCompletion:]_block_invoke_2.62
+ ___85-[VSSetupFlowPreparationOperation _checkForSupportedAppsFromProvider:withCompletion:]_block_invoke_3
+ ___85-[VSSetupFlowPreparationOperation _checkForSupportedAppsFromProvider:withCompletion:]_block_invoke_3.66
+ ___85-[VSSetupFlowPreparationOperation _getSTBProviderFromAllProviders:completionHandler:]_block_invoke
+ ___86-[VSSetupFlowController identityProviderPickerViewController:didPickIdentityProvider:]_block_invoke
+ ___86-[VSSetupFlowController identityProviderPickerViewController:didPickIdentityProvider:]_block_invoke.68
+ ___86-[VSSetupFlowController identityProviderPickerViewController:didPickIdentityProvider:]_block_invoke.69
+ ___86-[VSSetupFlowController identityProviderPickerViewController:didPickIdentityProvider:]_block_invoke_2
+ ___86-[VSSetupFlowController identityProviderPickerViewController:didPickIdentityProvider:]_block_invoke_2.71
+ ___86-[VSSetupFlowController identityProviderPickerViewController:didPickIdentityProvider:]_block_invoke_3
+ ___91-[VSSetupFlowPreparationOperation _getPersonalAppDescriptions:identityProvider:completion:]_block_invoke
+ ___91-[VSSetupFlowPreparationOperation _getPersonalAppDescriptions:identityProvider:completion:]_block_invoke.79
+ ___91-[VSSetupFlowPreparationOperation _getPersonalAppDescriptions:identityProvider:completion:]_block_invoke.cold.1
+ ___VSSetupFlowConfigurationValueType_block_invoke
+ ___VSSetupFlowConfigurationValueType_block_invoke_2
+ ___block_descriptor_32_e20_v20?0B8"NSError"12l
+ ___block_descriptor_32_e36_v16?0"VSIdentityProviderResponse"8l
+ ___block_descriptor_40_e8_32bs_e20_v20?0B8"NSError"12ls32l8
+ ___block_descriptor_40_e8_32r_e17_v16?0"NSError"8lr32l8
+ ___block_descriptor_40_e8_32s_e20_v16?0"VSFailable"8ls32l8
+ ___block_descriptor_40_e8_32s_e40_v24?0"VSSetTopBoxProfile"8"NSError"16ls32l8
+ ___block_descriptor_41_e8_32w_e5_v8?0lw32l8
+ ___block_descriptor_43_e8_32s_e17_v16?0"NSError"8ls32l8
+ ___block_descriptor_45_e8_32s_e34_v16?0"VSSetupFlowConfiguration"8ls32l8
+ ___block_descriptor_48_e8_32s40bs_e17_v16?0"NSArray"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e40_v24?0"VSSetTopBoxProfile"8"NSError"16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e20_v16?0"VSOptional"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e20_v20?0"NSArray"8B16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e28_v16?0"VSIdentityProvider"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e47_v16?0"VSIdentityProviderChannelAppsResponse"8ls32l8s40l8
+ ___block_descriptor_49_e8_32s40bs_e5_v8?0ls32l8s40l8
+ ___block_descriptor_49_e8_32s40bs_e5_v8?0ls40l8s32l8
+ ___block_descriptor_50_e8_32s40s_e11_v16?0B8B12ls32l8s40l8
+ ___block_descriptor_53_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48bs_e27_v16?0"VSAccountChannels"8ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48bs_e8_v12?0B8ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48s_e29_v24?0"NSArray"8"NSError"16ls32l8s40l8s48l8
+ ___block_descriptor_57_e8_32s40bs48bs_e40_v24?0"VSSetTopBoxProfile"8"NSError"16ls40l8s48l8s32l8
+ ___block_descriptor_62_e8_32s40s48s_e8_v12?0B8ls32l8s40l8s48l8
+ ___block_literal_global.59
+ ___block_literal_global.64
+ ___block_literal_global.67
+ ___block_literal_global.68
+ __swift_FORCE_LOAD_$_swiftCoreImage
+ __swift_FORCE_LOAD_$_swiftCoreImage_$_VideoSubscriberAccountUI
+ __swift_FORCE_LOAD_$_swiftSpatial
+ __swift_FORCE_LOAD_$_swiftSpatial_$_VideoSubscriberAccountUI
+ __swift_FORCE_LOAD_$_swiftUIKit
+ __swift_FORCE_LOAD_$_swiftUIKit_$_VideoSubscriberAccountUI
+ _objc_msgSend$_checkForExistingAccounts
+ _objc_msgSend$_checkForSupportedAppsButton
+ _objc_msgSend$_checkForSupportedAppsButtonWithFlow:
+ _objc_msgSend$_checkForSupportedAppsFromProvider:withCompletion:
+ _objc_msgSend$_checkPreferences
+ _objc_msgSend$_didStartLoading
+ _objc_msgSend$_dismissViewController:completion:
+ _objc_msgSend$_fetchAllProviders
+ _objc_msgSend$_fetchAllProvidersIfNeeded
+ _objc_msgSend$_fetchProviderForAccount:
+ _objc_msgSend$_finishAfterOfferingOptions:endingUndoGrouping:
+ _objc_msgSend$_finishWithFlow:
+ _objc_msgSend$_getPersonalAppDescriptions:identityProvider:completion:
+ _objc_msgSend$_getProviderWithUserTokenFromAllProviders:
+ _objc_msgSend$_getSTBProviderFromAllProviders:completionHandler:
+ _objc_msgSend$_isInSTBMode
+ _objc_msgSend$_loadProviderAppDescriptionWithFlow:
+ _objc_msgSend$_obtainConsentForBundleIDs:vouchers:withAppleAccountName:identityProvider:endingUndoGrouping:arrivedViaNotNowButton:arrivedAfterSigningIn:goingBack:
+ _objc_msgSend$_offerAuthenticationForProvider:withSupportedAppsButton:msoAppDescription:
+ _objc_msgSend$_offerAuthenticationForSTBProvider:msoAppDescription:providerAccountUsername:
+ _objc_msgSend$_offerAuthenticationWithSupportedAppsButton:
+ _objc_msgSend$_offerFreeOnBoardingIfNeededAfterOfferingOptions:endingUndoGrouping:arrivedViaNotNowButton:arrivedAfterSigningIn:goingBack:
+ _objc_msgSend$_pickProviderWithViewController:
+ _objc_msgSend$_presentError:
+ _objc_msgSend$_presentViewController:completion:
+ _objc_msgSend$_requestAccessWithViewController:
+ _objc_msgSend$_resolveBundleIDs:forFlow:
+ _objc_msgSend$_startLoadingAfterOfferingOptions:endingUndoGrouping:arrivedViaNotNowButton:arrivedAfterSigningIn:goingBack:
+ _objc_msgSend$appPlacementPosition
+ _objc_msgSend$bundlesIDsToConsent
+ _objc_msgSend$canShowSupportedAppsButton
+ _objc_msgSend$deleteAccountRequestWithAccount:storage:
+ _objc_msgSend$determineMultiAppEnabledForProvider:completion:
+ _objc_msgSend$domain
+ _objc_msgSend$finishOrIsGoingBack:didOfferOptions:endingUndoGrouping:
+ _objc_msgSend$finishSTBSuccessFlowForProvider:shouldShowBulkConsent:
+ _objc_msgSend$firstAccountIfLoaded
+ _objc_msgSend$forceSignOutWithAccount:
+ _objc_msgSend$freeOnBoardingBundleIDs
+ _objc_msgSend$goingBackActivationCompletionBlock
+ _objc_msgSend$importData:withCompletionHandler:
+ _objc_msgSend$initWithAppAdamID:providerID:
+ _objc_msgSend$isFirstAccountLoaded
+ _objc_msgSend$isInSTBMode
+ _objc_msgSend$isSigningIn
+ _objc_msgSend$issueVouchers:
+ _objc_msgSend$makeAccountRequestWithStorage:
+ _objc_msgSend$markSTBProviderAppsForInstallation:rootAppPlacementPosition:
+ _objc_msgSend$markShouldSkipSetup
+ _objc_msgSend$msoAppDescription
+ _objc_msgSend$notNowWithIdentityProvider:
+ _objc_msgSend$noteDesiredApp:
+ _objc_msgSend$notifyDelegateFromActivation
+ _objc_msgSend$performDismissalOfIdentityProviderViewController:
+ _objc_msgSend$personalAppDescriptions
+ _objc_msgSend$personalChannelIDs
+ _objc_msgSend$popViewControllerAnimated:
+ _objc_msgSend$prepareSTBSetupForAccount:forProvider:
+ _objc_msgSend$presentingViewController
+ _objc_msgSend$providerAccountUsername
+ _objc_msgSend$providersForStorefront:
+ _objc_msgSend$removeObjectsForKeys:
+ _objc_msgSend$removeSkipSetupPreset
+ _objc_msgSend$serializationCenter
+ _objc_msgSend$setAllPersonalizedAppDescriptions:
+ _objc_msgSend$setAppDescription:
+ _objc_msgSend$setBundlesIDsToConsent:
+ _objc_msgSend$setCanIssuePrivacyVouchers:
+ _objc_msgSend$setCanShowSupportedAppsButton:
+ _objc_msgSend$setFreeOnBoardingBundleIDs:
+ _objc_msgSend$setGoingBackActivationCompletionBlock:
+ _objc_msgSend$setIsInSTBMode:
+ _objc_msgSend$setMsoAppDescription:
+ _objc_msgSend$setNotifyDelegateFromActivation:
+ _objc_msgSend$setPersonalChannelIDs:
+ _objc_msgSend$setProviderAccountUsername:
+ _objc_msgSend$setRequestManager:
+ _objc_msgSend$setResultCompletionBlock:
+ _objc_msgSend$setSetTopBoxActivationTime
+ _objc_msgSend$setShouldFetchImages:
+ _objc_msgSend$setShouldOfferAuthenticationFlow:
+ _objc_msgSend$setShouldOfferSTBAuthenticationFlow:
+ _objc_msgSend$setShouldOfferSoleAuthenticationFlow:
+ _objc_msgSend$setShouldSkipSetup
+ _objc_msgSend$setShouldSkipSetupEntirely:
+ _objc_msgSend$setSigningIn:
+ _objc_msgSend$setVouchersByBundleID:
+ _objc_msgSend$setupFlowController:authenticateProviderWithViewController:
+ _objc_msgSend$setupFlowController:dismissViewController:completion:
+ _objc_msgSend$setupFlowController:offerAuthenticationForProvider:withSupportedAppsButton:msoAppDescription:isSTB:providerAccountUsername:
+ _objc_msgSend$setupFlowController:offerAuthenticationWithSupportedAppsButton:
+ _objc_msgSend$setupFlowController:pickProviderWithViewController:
+ _objc_msgSend$setupFlowController:presentViewController:completion:
+ _objc_msgSend$setupFlowController:requestAccessWithViewController:
+ _objc_msgSend$setupFlowControllerDidFinish:
+ _objc_msgSend$setupFlowControllerDidFinishSilentSigningIn:
+ _objc_msgSend$setupFlowControllerDidStartLoading:
+ _objc_msgSend$setupFlowControllerNeedsDismissalOfSetupView
+ _objc_msgSend$shouldOfferAuthenticationFlow
+ _objc_msgSend$shouldOfferSTBAuthenticationFlow
+ _objc_msgSend$shouldOfferSoleAuthenticationFlow
+ _objc_msgSend$shouldSkipSetup
+ _objc_msgSend$shouldSkipSetupEntirely
+ _objc_msgSend$showMultiAppInstallVC:
+ _objc_msgSend$signOutForNotNowFlowWithIdentityProvider:
+ _objc_msgSend$silentMakeAccountRequestWithStorage:
+ _objc_msgSend$startSilentSigningInForSTBFromActivation:withCompletion:
+ _objc_msgSend$viewControllerForAppsSupportedByIdentityProvider:supportedApps:delegate:
+ _objc_msgSend$viewControllerForPlaybackActivityReportingFromAppsWithBundleIDs:grantingVouchers:appleAccountName:identityProvider:completionHandler:
+ _objc_msgSend$vouchersByBundleID
+ _sharedInstance.__vs_lazy_init_predicate
+ _sharedInstance.__vs_lazy_init_variable
CStrings:
+ "%s: %@"
+ "%s: nil provider"
+ "%s: no bundle id"
+ "%s: not stb/sole"
+ "%s: not stb/solo, proceed to display all providers"
+ "%s: result: %@"
+ ","
+ "-[VSSetupFlowController _startLoadingAfterOfferingOptions:endingUndoGrouping:arrivedViaNotNowButton:arrivedAfterSigningIn:goingBack:]_block_invoke_2"
+ "-[VSSetupFlowController finishSTBSuccessFlowForProvider:shouldShowBulkConsent:]"
+ "-[VSSetupFlowController identityProviderRequestManager:finishedRequest:withResult:]"
+ "-[VSSetupFlowController startSilentSigningInForSTBFromActivation:withCompletion:]"
+ "-[VSSetupFlowPreparationOperation _fetchAllProvidersIfNeeded]_block_invoke"
+ "-[VSSetupFlowPreparationOperation _fetchAllProviders]_block_invoke_2"
+ "-[VSSetupFlowPreparationOperation _loadProviderAppDescriptionWithFlow:]"
+ "@\"<VSSetupFlowControllerDelegate>\""
+ "@\"VSAccountSerializationCenter\""
+ "Account import complete. Will complete start loading. didImport=%{bool}d, error=%@"
+ "All providers: %@"
+ "Checking for Supported Apps to show Bulk Consent before the GetTheApp screen"
+ "Checking for existing account."
+ "Checking for feature availability."
+ "Checking preferences."
+ "Error Fetching Provider Apps: %@"
+ "Error Unwrapping VSSetupFlowPreparationOperation result: %@"
+ "Existing account %@"
+ "Failed to create account"
+ "Failed to save account: %@"
+ "Failed to set all app icon images: %@"
+ "Fetching all providers"
+ "Fetching provider for account"
+ "Finished setting supported apps for provider"
+ "Force sign out request completed.  Success: %d, Error:%@"
+ "Found channels: %@"
+ "Found matching provider %@"
+ "Found stb provider %@"
+ "Has bundle IDs to consent."
+ "Identity Provider Picker failed with error: %@"
+ "No Account Channels found for provider %@"
+ "No Channel IDs found for provider %@\n with Channels \n%@"
+ "No Personal App Descriptions found for provider %@\n with personalChannelIDs \n%@"
+ "No appDescription"
+ "No apple account; finishing;"
+ "No channel apps"
+ "No existing accounts."
+ "No storefront returned from bag load operation, falling back on non-STB or sole provider flow."
+ "Non-nil account found for sign out in not now flow, but could not log out with identity provider: %@.  Manually removing account from account store"
+ "Not in STB mode"
+ "Not now sign out request completed with error: %@"
+ "Not now sign out request completed with response: %@"
+ "Nothing to do; finishing."
+ "Offering STB authentication flow"
+ "Offering authentication flow."
+ "Offering sole authentication flow."
+ "Provider is not supported."
+ "Provider is supported."
+ "Setting All Supported App Descriptions: %lu"
+ "Setup flow did authenticate account: %@"
+ "Setup flow did pick provider: %@"
+ "Setup flow did start loading."
+ "Setup flow identity auth request %@ did finish: %@ for provider %@, isInSTBMode %d"
+ "Setup flow received remote notification: %@"
+ "Setup flow supported apps did finish: %@"
+ "Setup flow will dismiss view controller: %@"
+ "Setup flow will finish."
+ "Setup flow will not now."
+ "Setup flow will offer authentication for SOLE provider."
+ "Setup flow will offer authentication for STB."
+ "Setup flow will offer authentication."
+ "Setup flow will offer provider picker: %@"
+ "Setup flow will present error: %@"
+ "Setup flow will present view controller: %@."
+ "Setup flow will request access."
+ "Setup flow will show supported apps."
+ "Setup flow will start loading."
+ "Setup flow will start signing in."
+ "Showing MultiAppInstall Directly"
+ "Sign out attempted for not now flow, but no account exists in store"
+ "Skipping setup entirely."
+ "Successfully saved unsupported account"
+ "Successfully set all app icon images."
+ "T@\"<VSSetupFlowControllerDelegate>\",W,N,V_delegate"
+ "T@\"NSArray\",C,N,V_bundlesIDsToConsent"
+ "T@\"NSArray\",C,N,V_freeOnBoardingBundleIDs"
+ "T@\"NSDictionary\",C,N,V_vouchersByBundleID"
+ "T@\"NSString\",&,N,V_providerAccountUsername"
+ "T@\"NSString\",C,N,V_preferredAppID"
+ "T@\"NSString\",C,N,V_providerAccountUsername"
+ "T@\"VSAccountSerializationCenter\",&,N,V_serializationCenter"
+ "T@\"VSAppDescription\",&,N,V_msoAppDescription"
+ "T@?,C,N,V_goingBackActivationCompletionBlock"
+ "TB,N,GisSigningIn,V_signingIn"
+ "TB,N,V_canShowSupportedAppsButton"
+ "TB,N,V_didSelectNoAppsforInstall"
+ "TB,N,V_notifyDelegateFromActivation"
+ "TB,N,V_shouldOfferAuthenticationFlow"
+ "TB,N,V_shouldOfferSTBAuthenticationFlow"
+ "TB,N,V_shouldOfferSoleAuthenticationFlow"
+ "TB,N,V_shouldSkipSetupEntirely"
+ "The [profile providerID] parameter must not be nil."
+ "The [providersForStorefront firstObject] parameter must not be nil."
+ "The channelIDsOrNil parameter must not be nil."
+ "The identityProviderOrNil parameter must not be nil."
+ "The soleProviderOrNil parameter must not be nil."
+ "Unable to fetch accounts: %@"
+ "Unable to fetch all providers: %@"
+ "Unable to load bag value for all provider apps: %@"
+ "Unexpectedly, value was %@, instead of NSString."
+ "Unsupported Provider selected"
+ "Unsupported provider.  Will skip entire flow."
+ "VSRequestAppInstallUtility"
+ "VSSetupFlowConfiguration"
+ "VSSetupFlowController"
+ "VSSetupFlowPreparationOperation"
+ "VSSupportedAppsViewControllerDelegate"
+ "We are *not* in STB mode and are *not* going back but we have serialized account data. Will try importing that."
+ "Will check for endpoint to show supported apps."
+ "Will check for personalized channels for provider %@ with response %@"
+ "Will check for supported apps from provider: %@"
+ "Will exit %s"
+ "Will finish setup flow prep with error: %@"
+ "Will finish setup flow with config: %@"
+ "Will resolve bundle IDs: %@"
+ "_appleAccountDidChange:"
+ "_bundlesIDsToConsent"
+ "_canShowSupportedAppsButton"
+ "_checkForExistingAccounts"
+ "_checkForSupportedAppsButton"
+ "_checkForSupportedAppsButtonWithFlow:"
+ "_checkForSupportedAppsFromProvider:withCompletion:"
+ "_checkPreferences"
+ "_didSelectNoAppsforInstall"
+ "_didStartLoading"
+ "_dismissViewController:completion:"
+ "_fetchAllProviders"
+ "_fetchAllProvidersIfNeeded"
+ "_fetchProviderForAccount:"
+ "_fetchProviderForAccount: isInSTBMode %d"
+ "_fetchProviderForAccount: provider not fully supported"
+ "_finishAfterOfferingOptions:endingUndoGrouping:"
+ "_finishWithFlow:"
+ "_freeOnBoardingBundleIDs"
+ "_getPersonalAppDescriptions:identityProvider:completion:"
+ "_getProviderWithUserTokenFromAllProviders:"
+ "_getSTBProviderFromAllProviders:completionHandler:"
+ "_goingBackActivationCompletionBlock"
+ "_isInSTBMode"
+ "_loadProviderAppDescriptionWithFlow:"
+ "_msoAppDescription"
+ "_notifyDelegateFromActivation"
+ "_obtainConsentForBundleIDs:vouchers:withAppleAccountName:identityProvider:endingUndoGrouping:arrivedViaNotNowButton:arrivedAfterSigningIn:goingBack:"
+ "_offerAuthenticationForProvider:withSupportedAppsButton:msoAppDescription:"
+ "_offerAuthenticationForSTBProvider:msoAppDescription:providerAccountUsername:"
+ "_offerAuthenticationWithSupportedAppsButton:"
+ "_offerFreeOnBoardingIfNeededAfterOfferingOptions:endingUndoGrouping:arrivedViaNotNowButton:arrivedAfterSigningIn:goingBack:"
+ "_pickProviderWithViewController:"
+ "_preferredAppID"
+ "_presentViewController:completion:"
+ "_providerAccountUsername"
+ "_requestAccessWithViewController:"
+ "_resolveBundleIDs:forFlow:"
+ "_serializationCenter"
+ "_shouldOfferAuthenticationFlow"
+ "_shouldOfferSTBAuthenticationFlow"
+ "_shouldOfferSoleAuthenticationFlow"
+ "_shouldSkipSetupEntirely"
+ "_signingIn"
+ "_startLoadingAfterOfferingOptions:endingUndoGrouping:arrivedViaNotNowButton:arrivedAfterSigningIn:goingBack:"
+ "_vouchersByBundleID"
+ "appPlacementPosition"
+ "bundlesIDsToConsent"
+ "canShowSupportedAppsButton"
+ "didSelectNoAppsforInstall"
+ "domain"
+ "finishOrIsGoingBack:didOfferOptions:endingUndoGrouping:"
+ "finishSTBSuccessFlowForProvider: issue voucher for adam# %@"
+ "finishSTBSuccessFlowForProvider: no adam id"
+ "finishSTBSuccessFlowForProvider: no appDescription"
+ "finishSTBSuccessFlowForProvider: no bundle id"
+ "finishSTBSuccessFlowForProvider: no identityProvider"
+ "finishSTBSuccessFlowForProvider: no voucher"
+ "finishSTBSuccessFlowForProvider:shouldShowBulkConsent:"
+ "firstAccountIfLoaded"
+ "forceSignOutWithAccount:"
+ "freeOnBoardingBundleIDs"
+ "goingBackActivationCompletionBlock"
+ "importData:withCompletionHandler:"
+ "initWithAppAdamID:providerID:"
+ "isFirstAccountLoaded"
+ "isInSTBMode"
+ "isSigningIn"
+ "isSoleProviderFeatureEnabled %d"
+ "issueVouchers:"
+ "markSTBProviderAppsForInstallation:rootAppPlacementPosition:"
+ "markShouldSkipSetup"
+ "msoAppDescription"
+ "notNow"
+ "notNowWithIdentityProvider:"
+ "noteDesiredApp:"
+ "notifyDelegateFromActivation"
+ "performDismissalOfIdentityProviderViewController:"
+ "personalAppDescriptions"
+ "personalChannelIDs"
+ "popViewControllerAnimated:"
+ "prepareSTBSetupForAccount:forProvider:"
+ "presentingViewController"
+ "providerAccountUsername"
+ "removeObjectsForKeys:"
+ "removeSkipSetupPreset"
+ "serializationCenter"
+ "setAllPersonalizedAppDescriptions:"
+ "setBundlesIDsToConsent:"
+ "setCanShowSupportedAppsButton:"
+ "setDidSelectNoAppsforInstall:"
+ "setFreeOnBoardingBundleIDs:"
+ "setGoingBackActivationCompletionBlock:"
+ "setIsInSTBMode:"
+ "setMsoAppDescription:"
+ "setNotifyDelegateFromActivation:"
+ "setPersonalChannelIDs:"
+ "setProviderAccountUsername:"
+ "setSerializationCenter:"
+ "setSetTopBoxActivationTime"
+ "setShouldOfferAuthenticationFlow:"
+ "setShouldOfferSTBAuthenticationFlow:"
+ "setShouldOfferSoleAuthenticationFlow:"
+ "setShouldSkipSetup"
+ "setShouldSkipSetupEntirely:"
+ "setSigningIn:"
+ "setVouchersByBundleID:"
+ "setupFlowController:authenticateProviderWithViewController:"
+ "setupFlowController:dismissViewController:completion:"
+ "setupFlowController:offerAuthenticationForProvider:withSupportedAppsButton:msoAppDescription:isSTB:providerAccountUsername:"
+ "setupFlowController:offerAuthenticationWithSupportedAppsButton:"
+ "setupFlowController:pickProviderWithViewController:"
+ "setupFlowController:presentViewController:completion:"
+ "setupFlowController:requestAccessWithViewController:"
+ "setupFlowControllerDidFinish:"
+ "setupFlowControllerDidFinishSilentSigningIn:"
+ "setupFlowControllerDidStartLoading:"
+ "setupFlowControllerNeedsDismissalOfSetupView"
+ "shouldOfferAuthenticationFlow"
+ "shouldOfferSTBAuthenticationFlow"
+ "shouldOfferSoleAuthenticationFlow"
+ "shouldSkipSetup"
+ "shouldSkipSetupEntirely"
+ "showMultiAppInstallVC:"
+ "showSupportedApps"
+ "signOutForNotNowFlowWithIdentityProvider:"
+ "signingIn"
+ "startLoadingWhenGoingBack:serializedAccountDataToImport:"
+ "startSigningIn"
+ "startSigningInForIdentityProvider:"
+ "startSigningInForIdentityProvider: %@, STB %d, providerAccountUsername %@, app desc %@"
+ "startSilentSigningInForSTB: %ld providers"
+ "startSilentSigningInForSTB: Error fetching identity provider %@"
+ "startSilentSigningInForSTB: Provider is not fully supported."
+ "startSilentSigningInForSTBFromActivation:withCompletion:"
+ "user gave up on waiting for authentication to finish"
+ "v16@?0@\"VSSetupFlowConfiguration\"8"
+ "v16@?0B8B12"
+ "v20@?0@\"NSArray\"8B16"
+ "v24@0:8@\"VSSupportedAppsViewController\"16"
+ "v24@0:8B16B20"
+ "v28@0:8B16B20B24"
+ "v36@0:8@16B24@28"
+ "v36@0:8B16B20B24B28B32"
+ "v64@0:8@16@24@32@40B48B52B56B60"
+ "vouchersByBundleID"

```
