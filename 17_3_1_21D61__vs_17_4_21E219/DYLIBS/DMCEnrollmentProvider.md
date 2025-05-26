## DMCEnrollmentProvider

> `/System/Library/PrivateFrameworks/DMCEnrollmentProvider.framework/DMCEnrollmentProvider`

```diff

-3.26.4.1.0
-  __TEXT.__text: 0x3b818
-  __TEXT.__auth_stubs: 0x730
-  __TEXT.__objc_methlist: 0x4c44
+3.26.5.12.0
+  __TEXT.__text: 0x3f300
+  __TEXT.__auth_stubs: 0x7b0
+  __TEXT.__objc_methlist: 0x5014
   __TEXT.__const: 0x188
-  __TEXT.__oslogstring: 0x11be
-  __TEXT.__cstring: 0x2483
-  __TEXT.__gcc_except_tab: 0x4d0
+  __TEXT.__oslogstring: 0x15a8
+  __TEXT.__cstring: 0x2602
+  __TEXT.__gcc_except_tab: 0x51c
   __TEXT.__dlopen_cstrs: 0x47
-  __TEXT.__ustring: 0xc
-  __TEXT.__unwind_info: 0x1080
-  __TEXT.__objc_classname: 0xfdd
-  __TEXT.__objc_methname: 0x104b9
-  __TEXT.__objc_methtype: 0x389a
-  __TEXT.__objc_stubs: 0xb140
-  __DATA_CONST.__got: 0x4a0
-  __DATA_CONST.__const: 0xb58
-  __DATA_CONST.__objc_classlist: 0x2d0
+  __TEXT.__ustring: 0x50
+  __TEXT.__unwind_info: 0x1158
+  __TEXT.__objc_classname: 0x10b2
+  __TEXT.__objc_methname: 0x11dfd
+  __TEXT.__objc_methtype: 0x446d
+  __TEXT.__objc_stubs: 0xbd80
+  __DATA_CONST.__got: 0x518
+  __DATA_CONST.__const: 0xc70
+  __DATA_CONST.__objc_classlist: 0x2f0
   __DATA_CONST.__objc_catlist: 0x40
-  __DATA_CONST.__objc_protolist: 0x150
+  __DATA_CONST.__objc_protolist: 0x178
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xe9f0
-  __DATA_CONST.__objc_selrefs: 0x35a8
+  __DATA_CONST.__objc_const: 0x10680
+  __DATA_CONST.__objc_selrefs: 0x39c0
+  __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_classrefs: 0x7c8
+  __DATA_CONST.__objc_superrefs: 0x250
   __DATA_CONST.__objc_arraydata: 0x60
-  __AUTH_CONST.__objc_const: 0x22e8
-  __AUTH_CONST.__cfstring: 0x2840
+  __AUTH_CONST.__objc_const: 0x23c0
+  __AUTH_CONST.__cfstring: 0x2a60
   __AUTH_CONST.__const: 0x120
   __AUTH_CONST.__objc_arrayobj: 0x120
   __AUTH_CONST.__objc_floatobj: 0x30
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH_CONST.__auth_got: 0x3a8
-  __AUTH.__objc_data: 0x1ae0
-  __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x748
-  __DATA.__objc_superrefs: 0x240
-  __DATA.__objc_ivar: 0x51c
-  __DATA.__data: 0xfc8
+  __AUTH_CONST.__auth_got: 0x3e8
+  __AUTH.__objc_data: 0x1c20
+  __DATA.__objc_ivar: 0x558
+  __DATA.__data: 0x11a8
   __DATA.__bss: 0x60
   __DATA_DIRTY.__objc_data: 0x140
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/NetworkExtension.framework/NetworkExtension
   - /System/Library/Frameworks/Security.framework/Security
+  - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
   - /System/Library/Frameworks/UIKit.framework/UIKit
+  - /System/Library/Frameworks/WebKit.framework/WebKit
   - /System/Library/PrivateFrameworks/AccountsUI.framework/AccountsUI
   - /System/Library/PrivateFrameworks/AppStoreComponents.framework/AppStoreComponents
+  - /System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount
   - /System/Library/PrivateFrameworks/AppleIDSSOAuthentication.framework/AppleIDSSOAuthentication
   - /System/Library/PrivateFrameworks/AuthKit.framework/AuthKit
   - /System/Library/PrivateFrameworks/AuthKitUI.framework/AuthKitUI

   - /System/Library/PrivateFrameworks/Preferences.framework/Preferences
   - /System/Library/PrivateFrameworks/RemoteManagementUI.framework/RemoteManagementUI
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
+  - /System/Library/PrivateFrameworks/WebKitLegacy.framework/WebKitLegacy
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1722
-  Symbols:   6845
-  CStrings:  3522
+  Functions: 1817
+  Symbols:   7268
+  CStrings:  3840
 
Symbols:
+ -[DMCBYODEnrollmentFlowUIPresenter _fakeAppleAccountWithAuthenticationResults:personaID:store:]
+ -[DMCBYODEnrollmentFlowUIPresenter _fakeiTunesAccountWithAuthenticationResults:personaID:store:]
+ -[DMCBYODEnrollmentFlowUIPresenter ensureNetworkConnectionWithCompletionHandler:]
+ -[DMCBYODEnrollmentFlowUIPresenter fetchEnrollmentProfileWithWebAuthURL:machineInfo:anchorCertificateRefs:completionHandler:]
+ -[DMCBYODEnrollmentFlowUIPresenter recievedProfile:]
+ -[DMCBYODEnrollmentFlowUIPresenter requestMDMUsernameAndPasswordWithCompletionHandler:]
+ -[DMCBYODEnrollmentFlowUIPresenter requestUserConsentWithCloudConfig:completionHandler:]
+ -[DMCBYODEnrollmentFlowUIPresenter setUsernameAndPasswordCompletionHandler:]
+ -[DMCBYODEnrollmentFlowUIPresenter setWebURLCompletionHandler:]
+ -[DMCBYODEnrollmentFlowUIPresenter showFetchingCloudConfigurationScene]
+ -[DMCBYODEnrollmentFlowUIPresenter usernameAndPasswordCompletionHandler]
+ -[DMCBYODEnrollmentFlowUIPresenter webAuthCanceled:]
+ -[DMCBYODEnrollmentFlowUIPresenter webURLCompletionHandler]
+ -[DMCEnrollmentFlowManagedConfigurationHelper _cloudConfigDidChange:]
+ -[DMCEnrollmentFlowManagedConfigurationHelper awaitDeviceConfigurationCompletionHandler]
+ -[DMCEnrollmentFlowManagedConfigurationHelper awaitDeviceConfiguredWithCompletionHandler:]
+ -[DMCEnrollmentFlowManagedConfigurationHelper fetchCloudConfigWithCompletionHandler:]
+ -[DMCEnrollmentFlowManagedConfigurationHelper isDeviceConfigured]
+ -[DMCEnrollmentFlowManagedConfigurationHelper markCloudConfigurationAsUICompleted]
+ -[DMCEnrollmentFlowManagedConfigurationHelper restoreSetAsideCloudConfigAndProfilesWithCompletionHandler:]
+ -[DMCEnrollmentFlowManagedConfigurationHelper setAwaitDeviceConfigurationCompletionHandler:]
+ -[DMCEnrollmentFlowManagedConfigurationHelper storeCloudConfig:completionHandler:]
+ -[DMCEnrollmentInterface startInBuddyEnrollment]
+ -[DMCPayloadDetailsCell .cxx_destruct]
+ -[DMCPayloadDetailsCell _addCopyEditMenuAction]
+ -[DMCPayloadDetailsCell _didLongPress:]
+ -[DMCPayloadDetailsCell canPerformAction:withSender:]
+ -[DMCPayloadDetailsCell copy:]
+ -[DMCPayloadDetailsCell copyableText]
+ -[DMCPayloadDetailsCell editMenuInteraction]
+ -[DMCPayloadDetailsCell longPress]
+ -[DMCPayloadDetailsCell setCopyableText:]
+ -[DMCPayloadDetailsCell setEditMenuInteraction:]
+ -[DMCPayloadDetailsCell setLongPress:]
+ -[DMCRFFakeSnapshot dateCreated]
+ -[DMCRFFakeSnapshot dateModified]
+ -[DMCRFFakeSnapshot date]
+ -[DMCRFFakeSnapshot deviceName]
+ -[DMCRFFakeSnapshot identifier]
+ -[DMCTestNetworkMonitor .cxx_destruct]
+ -[DMCTestNetworkMonitor availableHanlder]
+ -[DMCTestNetworkMonitor initWithNetworkAvailableHandler:]
+ -[DMCTestNetworkMonitor isNetworkAvailableWithFlags:]
+ -[DMCTestNetworkMonitor reachability]
+ -[DMCTestNetworkMonitor setAvailableHanlder:]
+ -[DMCTestNetworkMonitor setReachability:]
+ -[DMCTestNetworkMonitor startMonitoring]
+ -[DMCTestNetworkMonitor verifyNetworkFlags:]
+ -[DMCTestWebViewController .cxx_destruct]
+ -[DMCTestWebViewController _download:decideDestinationWithSuggestedFilename:completionHandler:]
+ -[DMCTestWebViewController _download:didCreateDestination:]
+ -[DMCTestWebViewController _download:didFailWithError:]
+ -[DMCTestWebViewController _download:didReceiveAuthenticationChallenge:completionHandler:]
+ -[DMCTestWebViewController _downloadDidCancel:]
+ -[DMCTestWebViewController _downloadDidFinish:]
+ -[DMCTestWebViewController _downloadDidStart:]
+ -[DMCTestWebViewController _downloadProcessDidCrash:]
+ -[DMCTestWebViewController _getEncodedMachineInfo]
+ -[DMCTestWebViewController _showFailureAlertWithTitle:andMessage:]
+ -[DMCTestWebViewController anchorCerts]
+ -[DMCTestWebViewController cancelButtonTapped]
+ -[DMCTestWebViewController delegate]
+ -[DMCTestWebViewController downloadDestination]
+ -[DMCTestWebViewController downloadedProfileData]
+ -[DMCTestWebViewController evaluateAuthenticationChallenge:withCompletionHandler:]
+ -[DMCTestWebViewController machineInfo]
+ -[DMCTestWebViewController setAnchorCerts:]
+ -[DMCTestWebViewController setDelegate:]
+ -[DMCTestWebViewController setDownloadDestination:]
+ -[DMCTestWebViewController setDownloadedProfileData:]
+ -[DMCTestWebViewController setMachineInfo:]
+ -[DMCTestWebViewController setWebURL:]
+ -[DMCTestWebViewController setWebView:]
+ -[DMCTestWebViewController viewDidLoad]
+ -[DMCTestWebViewController webURL]
+ -[DMCTestWebViewController webView:decidePolicyForNavigationResponse:decisionHandler:]
+ -[DMCTestWebViewController webView:didFailProvisionalNavigation:withError:]
+ -[DMCTestWebViewController webView:didReceiveAuthenticationChallenge:completionHandler:]
+ -[DMCTestWebViewController webView]
+ GCC_except_table17
+ GCC_except_table26
+ GCC_except_table27
+ GCC_except_table66
+ GCC_except_table8
+ _AAAccountClassFull
+ _AKAuthenticationAppleIDMDMInfoRequired
+ _AKAuthenticationDSIDKey
+ _AKAuthenticationFirstNameKey
+ _AKAuthenticationLastNameKey
+ _CFRunLoopGetMain
+ _MCCloudConfigurationDidChangeNotification
+ _NSURLAuthenticationMethodServerTrust
+ _NSURLErrorDomain
+ _NSURLErrorFailingURLErrorKey
+ _OBJC_CLASS_$_DMCDefaults
+ _OBJC_CLASS_$_DMCRFFakeSnapshot
+ _OBJC_CLASS_$_DMCRFFakeSnapshotIdentifier
+ _OBJC_CLASS_$_DMCTestNetworkMonitor
+ _OBJC_CLASS_$_DMCTestWebViewController
+ _OBJC_CLASS_$_NSFileManager
+ _OBJC_CLASS_$_NSMutableURLRequest
+ _OBJC_CLASS_$_NSURLCredential
+ _OBJC_CLASS_$_UIEditMenuConfiguration
+ _OBJC_CLASS_$_UIEditMenuInteraction
+ _OBJC_CLASS_$_UILongPressGestureRecognizer
+ _OBJC_CLASS_$_UIPasteboard
+ _OBJC_CLASS_$_WKWebView
+ _OBJC_CLASS_$_WKWebViewConfiguration
+ _OBJC_CLASS_$_WKWebsiteDataStore
+ _OBJC_IVAR_$_DMCBYODEnrollmentFlowUIPresenter._usernameAndPasswordCompletionHandler
+ _OBJC_IVAR_$_DMCBYODEnrollmentFlowUIPresenter._webURLCompletionHandler
+ _OBJC_IVAR_$_DMCEnrollmentFlowManagedConfigurationHelper._awaitDeviceConfigurationCompletionHandler
+ _OBJC_IVAR_$_DMCPayloadDetailsCell._copyableText
+ _OBJC_IVAR_$_DMCPayloadDetailsCell._editMenuInteraction
+ _OBJC_IVAR_$_DMCPayloadDetailsCell._longPress
+ _OBJC_IVAR_$_DMCTestNetworkMonitor._availableHanlder
+ _OBJC_IVAR_$_DMCTestNetworkMonitor._reachability
+ _OBJC_IVAR_$_DMCTestWebViewController._anchorCerts
+ _OBJC_IVAR_$_DMCTestWebViewController._delegate
+ _OBJC_IVAR_$_DMCTestWebViewController._downloadDestination
+ _OBJC_IVAR_$_DMCTestWebViewController._downloadedProfileData
+ _OBJC_IVAR_$_DMCTestWebViewController._machineInfo
+ _OBJC_IVAR_$_DMCTestWebViewController._webURL
+ _OBJC_IVAR_$_DMCTestWebViewController._webView
+ _OBJC_METACLASS_$_DMCRFFakeSnapshot
+ _OBJC_METACLASS_$_DMCRFFakeSnapshotIdentifier
+ _OBJC_METACLASS_$_DMCTestNetworkMonitor
+ _OBJC_METACLASS_$_DMCTestWebViewController
+ _SCNetworkReachabilityCreateWithOptions
+ _SCNetworkReachabilityGetFlags
+ _SCNetworkReachabilityScheduleWithRunLoop
+ _SCNetworkReachabilitySetCallback
+ _SCNetworkReachabilityUnscheduleFromRunLoop
+ _SecTrustEvaluate
+ _SecTrustSetAnchorCertificates
+ _WebKitErrorDomain
+ __OBJC_$_INSTANCE_METHODS_DMCRFFakeSnapshot
+ __OBJC_$_INSTANCE_METHODS_DMCTestNetworkMonitor
+ __OBJC_$_INSTANCE_METHODS_DMCTestWebViewController
+ __OBJC_$_INSTANCE_VARIABLES_DMCPayloadDetailsCell
+ __OBJC_$_INSTANCE_VARIABLES_DMCTestNetworkMonitor
+ __OBJC_$_INSTANCE_VARIABLES_DMCTestWebViewController
+ __OBJC_$_PROP_LIST_DMCPayloadDetailsCell
+ __OBJC_$_PROP_LIST_DMCRFFakeSnapshot
+ __OBJC_$_PROP_LIST_DMCRFFakeSnapshotIdentifier
+ __OBJC_$_PROP_LIST_DMCTestNetworkMonitor
+ __OBJC_$_PROP_LIST_DMCTestWebViewController
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_DMCCloudConfigWebAuthDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_UIEditMenuInteractionDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_WKNavigationDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_WKUIDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT__WKDownloadDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_DMCCloudConfigWebAuthDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_UIEditMenuInteractionDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_WKNavigationDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_WKUIDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES__WKDownloadDelegate
+ __OBJC_$_PROTOCOL_REFS_DMCCloudConfigWebAuthDelegate
+ __OBJC_$_PROTOCOL_REFS_UIEditMenuInteractionDelegate
+ __OBJC_$_PROTOCOL_REFS_WKNavigationDelegate
+ __OBJC_$_PROTOCOL_REFS_WKUIDelegate
+ __OBJC_$_PROTOCOL_REFS__WKDownloadDelegate
+ __OBJC_CLASS_PROTOCOLS_$_DMCPayloadDetailsCell
+ __OBJC_CLASS_PROTOCOLS_$_DMCRFFakeSnapshot
+ __OBJC_CLASS_PROTOCOLS_$_DMCRFFakeSnapshotIdentifier
+ __OBJC_CLASS_PROTOCOLS_$_DMCTestWebViewController
+ __OBJC_CLASS_RO_$_DMCRFFakeSnapshot
+ __OBJC_CLASS_RO_$_DMCRFFakeSnapshotIdentifier
+ __OBJC_CLASS_RO_$_DMCTestNetworkMonitor
+ __OBJC_CLASS_RO_$_DMCTestWebViewController
+ __OBJC_LABEL_PROTOCOL_$_DMCCloudConfigWebAuthDelegate
+ __OBJC_LABEL_PROTOCOL_$_UIEditMenuInteractionDelegate
+ __OBJC_LABEL_PROTOCOL_$_WKNavigationDelegate
+ __OBJC_LABEL_PROTOCOL_$_WKUIDelegate
+ __OBJC_LABEL_PROTOCOL_$__WKDownloadDelegate
+ __OBJC_METACLASS_RO_$_DMCRFFakeSnapshot
+ __OBJC_METACLASS_RO_$_DMCRFFakeSnapshotIdentifier
+ __OBJC_METACLASS_RO_$_DMCTestNetworkMonitor
+ __OBJC_METACLASS_RO_$_DMCTestWebViewController
+ __OBJC_PROTOCOL_$_DMCCloudConfigWebAuthDelegate
+ __OBJC_PROTOCOL_$_UIEditMenuInteractionDelegate
+ __OBJC_PROTOCOL_$_WKNavigationDelegate
+ __OBJC_PROTOCOL_$_WKUIDelegate
+ __OBJC_PROTOCOL_$__WKDownloadDelegate
+ ___101-[DMCBYODEnrollmentFlowUIPresenter suggestRestoreForAccountWithUsername:personaID:completionHandler:]_block_invoke_4
+ ___111-[DMCEnrollmentAuthenticationController fetchAuthenticationModeForUsername:requireAppleMAID:completionHandler:]_block_invoke
+ ___124-[DMCBYODEnrollmentFlowUIPresenter _makeAuthenticationActionHandlerWithEphemeral:requireAppleMAID:presentingViewController:]_block_invoke_4
+ ___125-[DMCBYODEnrollmentFlowUIPresenter fetchEnrollmentProfileWithWebAuthURL:machineInfo:anchorCertificateRefs:completionHandler:]_block_invoke
+ ___135-[DMCBYODEnrollmentFlowUIPresenter requestMAIDAuthenticationWithManagedAppleID:personaID:ephemeral:requireAppleMAID:completionHandler:]_block_invoke_3.79
+ ___135-[DMCBYODEnrollmentFlowUIPresenter requestMAIDAuthenticationWithManagedAppleID:personaID:ephemeral:requireAppleMAID:completionHandler:]_block_invoke_6
+ ___48-[DMCEnrollmentInterface startInBuddyEnrollment]_block_invoke
+ ___57-[DMCTestNetworkMonitor initWithNetworkAvailableHandler:]_block_invoke
+ ___58-[DMCEnrollmentConsentViewController _requiredAppCellData]_block_invoke.60
+ ___66-[DMCTestWebViewController _showFailureAlertWithTitle:andMessage:]_block_invoke
+ ___81-[DMCBYODEnrollmentFlowUIPresenter ensureNetworkConnectionWithCompletionHandler:]_block_invoke
+ ___81-[DMCBYODEnrollmentFlowUIPresenter ensureNetworkConnectionWithCompletionHandler:]_block_invoke_2
+ ___85-[DMCEnrollmentFlowManagedConfigurationHelper fetchCloudConfigWithCompletionHandler:]_block_invoke
+ ___87-[DMCBYODEnrollmentFlowUIPresenter requestMDMUsernameAndPasswordWithCompletionHandler:]_block_invoke
+ ___88-[DMCBYODEnrollmentFlowUIPresenter requestUserConsentWithCloudConfig:completionHandler:]_block_invoke
+ ___96-[DMCBYODEnrollmentFlowUIPresenter authenticationViewController:didReceivePassword:forUsername:]_block_invoke_2
+ ___block_descriptor_40_e8_32bs_e34_v24?0"NSError"8"NSDictionary"16ls32l8
+ ___block_descriptor_40_e8_32s_e23_v16?0"UIAlertAction"8ls32l8
+ ___block_descriptor_42_e8_32w_e18_v16?0"NSString"8lw32l8
+ ___block_descriptor_48_e8_32bs40bs_e21_v20?0"NSString"8B16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e5_v8?0ls40l8s32l8
+ ___block_descriptor_65_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s56l8s48l8
+ ___block_descriptor_65_e8_32s40s48s56bs_e5_v8?0ls56l8s32l8s40l8s48l8
+ __networkReachabilityCallback
+ _kCCConfigurationSourceKey
+ _kCCIsSupervisedKey
+ _kCFRunLoopCommonModes
+ _kMCInstallProfileOptionIsCloudLocked
+ _kMCInstallProfileOptionIsCloudProfile
+ _objc_msgSend$ADETestModeEnabled
+ _objc_msgSend$MIMEType
+ _objc_msgSend$URL
+ _objc_msgSend$_addCopyEditMenuAction
+ _objc_msgSend$_fakeAppleAccountWithAuthenticationResults:personaID:store:
+ _objc_msgSend$_fakeiTunesAccountWithAuthenticationResults:personaID:store:
+ _objc_msgSend$_getEncodedMachineInfo
+ _objc_msgSend$_setDiagnosticLoggingEnabled:
+ _objc_msgSend$_setDownloadDelegate:
+ _objc_msgSend$_showFailureAlertWithTitle:andMessage:
+ _objc_msgSend$aa_setAccountClass:
+ _objc_msgSend$aa_setFirstName:
+ _objc_msgSend$aa_setLastName:
+ _objc_msgSend$accountTypeWithAccountTypeIdentifier:
+ _objc_msgSend$addGestureRecognizer:
+ _objc_msgSend$addInteraction:
+ _objc_msgSend$authenticationMethod
+ _objc_msgSend$availableHanlder
+ _objc_msgSend$awaitDeviceConfigurationCompletionHandler
+ _objc_msgSend$base64EncodedStringWithOptions:
+ _objc_msgSend$caseInsensitiveCompare:
+ _objc_msgSend$center
+ _objc_msgSend$configuration
+ _objc_msgSend$configurationWithIdentifier:sourcePoint:
+ _objc_msgSend$configurationWithPaletteColors:
+ _objc_msgSend$copyableText
+ _objc_msgSend$credentialForTrust:
+ _objc_msgSend$dataWithContentsOfFile:
+ _objc_msgSend$defaultManager
+ _objc_msgSend$dmc_setAltDSID:
+ _objc_msgSend$dmc_setDSID:
+ _objc_msgSend$dmc_setPersonaIdentifier:
+ _objc_msgSend$downloadDestination
+ _objc_msgSend$downloadedProfileData
+ _objc_msgSend$errorWithDomain:code:userInfo:
+ _objc_msgSend$evaluateAuthenticationChallenge:withCompletionHandler:
+ _objc_msgSend$generalPasteboard
+ _objc_msgSend$gestureRecognizers
+ _objc_msgSend$indexPathForCell:
+ _objc_msgSend$initWithAccountType:
+ _objc_msgSend$initWithDelegate:
+ _objc_msgSend$initWithFrame:configuration:
+ _objc_msgSend$initWithNetworkAvailableHandler:
+ _objc_msgSend$initWithTarget:action:
+ _objc_msgSend$initWithURL:
+ _objc_msgSend$isAwaitingDeviceConfigured
+ _objc_msgSend$isDeviceConfigured
+ _objc_msgSend$isNetworkAvailableWithFlags:
+ _objc_msgSend$isVisionDevice
+ _objc_msgSend$loadRequest:
+ _objc_msgSend$localizedStringWithFormat:
+ _objc_msgSend$machineInfo
+ _objc_msgSend$mainBundle
+ _objc_msgSend$nonPersistentDataStore
+ _objc_msgSend$preferences
+ _objc_msgSend$presentEditMenuWithConfiguration:
+ _objc_msgSend$processPool
+ _objc_msgSend$protectionSpace
+ _objc_msgSend$recievedProfile:
+ _objc_msgSend$removeItemAtPath:error:
+ _objc_msgSend$response
+ _objc_msgSend$restoreCloudConfigAndMDMProfileFromSetAsideDataWithCompletion:
+ _objc_msgSend$retrieveCloudConfigurationDetailsCompletionBlock:
+ _objc_msgSend$saveVerifiedAccount:error:
+ _objc_msgSend$serverTrust
+ _objc_msgSend$setAccountDescription:
+ _objc_msgSend$setActive:
+ _objc_msgSend$setAnchorCerts:
+ _objc_msgSend$setAuthenticated:
+ _objc_msgSend$setAvailableHanlder:
+ _objc_msgSend$setAwaitDeviceConfigurationCompletionHandler:
+ _objc_msgSend$setCopyableText:
+ _objc_msgSend$setDownloadDestination:
+ _objc_msgSend$setDownloadedProfileData:
+ _objc_msgSend$setMachineInfo:
+ _objc_msgSend$setNavigationDelegate:
+ _objc_msgSend$setString:
+ _objc_msgSend$setUIDelegate:
+ _objc_msgSend$setUsernameAndPasswordCompletionHandler:
+ _objc_msgSend$setValue:forHTTPHeaderField:
+ _objc_msgSend$setView:
+ _objc_msgSend$setWebURL:
+ _objc_msgSend$setWebURLCompletionHandler:
+ _objc_msgSend$setWebView:
+ _objc_msgSend$setWebsiteDataStore:
+ _objc_msgSend$shouldSimulateMDMAccountDrivenEnrollment
+ _objc_msgSend$showInstallingEnrollmentProfileScene
+ _objc_msgSend$simluatedMDMAccountDrivenEnrollmentAuthenticationResults
+ _objc_msgSend$startInBuddyEnrollmentFlowRestartIfFail:completionHandler:
+ _objc_msgSend$startMonitoring
+ _objc_msgSend$statusCode
+ _objc_msgSend$stopLoading
+ _objc_msgSend$systemWhiteColor
+ _objc_msgSend$usernameAndPasswordCompletionHandler
+ _objc_msgSend$verifyNetworkFlags:
+ _objc_msgSend$webAuthCanceled:
+ _objc_msgSend$webURL
+ _objc_msgSend$webURLCompletionHandler
+ _objc_msgSend$webView
- GCC_except_table24
- GCC_except_table25
- GCC_except_table61
- ___58-[DMCEnrollmentConsentViewController _requiredAppCellData]_block_invoke.61
- _objc_msgSend$modelSpecificLocalizedStringKeyForKey:
CStrings:
+ "\x04\x12"
+ "\x1f\x01"
+ "%lu"
+ "/tmp/%@"
+ "@\"<DMCCloudConfigWebAuthDelegate>\""
+ "@\"NSString\"40@0:8@\"_WKDownload\"16@\"NSString\"24^B32"
+ "@\"NSURL\""
+ "@\"UIEditMenuInteraction\""
+ "@\"UILongPressGestureRecognizer\""
+ "@\"UIMenu\"40@0:8@\"UIEditMenuInteraction\"16@\"UIEditMenuConfiguration\"24@\"NSArray\"32"
+ "@\"UIViewController\"40@0:8@\"WKWebView\"16@\"WKPreviewElementInfo\"24@\"NSArray\"32"
+ "@\"WKWebView\""
+ "@\"WKWebView\"48@0:8@\"WKWebView\"16@\"WKWebViewConfiguration\"24@\"WKNavigationAction\"32@\"WKWindowFeatures\"40"
+ "@24@0:8@?16"
+ "@40@0:8@16@24^B32"
+ "ADETestModeEnabled"
+ "Accepting server trust!"
+ "B20@0:8I16"
+ "B32@0:8:16@24"
+ "B32@0:8@\"WKWebView\"16@\"WKPreviewElementInfo\"24"
+ "B32@0:8@\"_WKDownload\"16@\"NSString\"24"
+ "BYCloudConfigRetreiveProfileFromWebErrorDomain"
+ "Cloud Config Test"
+ "Cloud Configuration fetched"
+ "Cloud config changed but device is not configured."
+ "Could not evaluate trust! Error Code:  %d"
+ "DMCCloudConfigWebAuthDelegate"
+ "DMCRFFakeSnapshot"
+ "DMCRFFakeSnapshotIdentifier"
+ "DMCTestNetworkMonitor"
+ "DMCTestWebViewController"
+ "Device is configured!"
+ "Device was unsupervised and now we are changing supervision state. Abort"
+ "Failed to set Anchor Certs on trust! With secError code: %d"
+ "Fake Device"
+ "Localizable"
+ "MIMEType"
+ "Network is available."
+ "OK"
+ "REMOTE_MANAGEMENT_FAILED_TO_LOAD_PAGE"
+ "REMOTE_MANAGEMENT_TITLE"
+ "REMOTE_MANAGEMENT_UNABLE_TO_RESOLVE_HOST"
+ "Received an Authentication method other than Server Trust!!"
+ "ResolverBypass"
+ "Showing failure alert title: %@, message: %@"
+ "Suppressing web navigation error caused by policy change"
+ "T@\"<DMCCloudConfigWebAuthDelegate>\",W,N,V_delegate"
+ "T@\"NSArray\",&,N,V_anchorCerts"
+ "T@\"NSData\",&,N,V_machineInfo"
+ "T@\"NSData\",&,V_downloadedProfileData"
+ "T@\"NSString\",&,N,V_copyableText"
+ "T@\"NSString\",&,V_downloadDestination"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSURL\",&,N,V_webURL"
+ "T@\"UIEditMenuInteraction\",&,N,V_editMenuInteraction"
+ "T@\"UILongPressGestureRecognizer\",&,N,V_longPress"
+ "T@\"WKWebView\",&,N,V_webView"
+ "T@?,C,N,V_availableHanlder"
+ "T@?,C,N,V_awaitDeviceConfigurationCompletionHandler"
+ "T@?,C,N,V_usernameAndPasswordCompletionHandler"
+ "T@?,C,N,V_webURLCompletionHandler"
+ "T^{__SCNetworkReachability=},N,V_reachability"
+ "UIEditMenuInteractionDelegate"
+ "URL"
+ "WKNavigationDelegate"
+ "WKUIDelegate"
+ "^{__SCNetworkReachability=}"
+ "^{__SCNetworkReachability=}16@0:8"
+ "_WKDownloadDelegate"
+ "_addCopyEditMenuAction"
+ "_anchorCerts"
+ "_availableHanlder"
+ "_awaitDeviceConfigurationCompletionHandler"
+ "_cloudConfigDidChange:"
+ "_copyableText"
+ "_didLongPress:"
+ "_download:decideDestinationWithSuggestedFilename:allowOverwrite:"
+ "_download:decideDestinationWithSuggestedFilename:completionHandler:"
+ "_download:didCreateDestination:"
+ "_download:didFailWithError:"
+ "_download:didReceiveAuthenticationChallenge:completionHandler:"
+ "_download:didReceiveData:"
+ "_download:didReceiveResponse:"
+ "_download:didReceiveServerRedirectToURL:"
+ "_download:didWriteData:totalBytesWritten:totalBytesExpectedToWrite:"
+ "_download:shouldDecodeSourceDataOfMIMEType:"
+ "_downloadDestination"
+ "_downloadDidCancel:"
+ "_downloadDidFinish:"
+ "_downloadDidStart:"
+ "_downloadProcessDidCrash:"
+ "_downloadedProfileData"
+ "_editMenuInteraction"
+ "_fakeAppleAccountWithAuthenticationResults:personaID:store:"
+ "_fakeiTunesAccountWithAuthenticationResults:personaID:store:"
+ "_getEncodedMachineInfo"
+ "_longPress"
+ "_machineInfo"
+ "_reachability"
+ "_setDiagnosticLoggingEnabled:"
+ "_setDownloadDelegate:"
+ "_showFailureAlertWithTitle:andMessage:"
+ "_usernameAndPasswordCompletionHandler"
+ "_webURL"
+ "_webURLCompletionHandler"
+ "_webView"
+ "aa_setAccountClass:"
+ "aa_setFirstName:"
+ "aa_setLastName:"
+ "accountTypeWithAccountTypeIdentifier:"
+ "addGestureRecognizer:"
+ "addInteraction:"
+ "anchorCerts"
+ "application/x-apple-aspen-config"
+ "authenticationMethod"
+ "availableHanlder"
+ "awaitDeviceConfigurationCompletionHandler"
+ "awaitDeviceConfiguredWithCompletionHandler:"
+ "base64EncodedStringWithOptions:"
+ "canPerformAction:withSender:"
+ "cancelButtonTapped"
+ "caseInsensitiveCompare:"
+ "center"
+ "configuration"
+ "configurationWithIdentifier:sourcePoint:"
+ "configurationWithPaletteColors:"
+ "copy:"
+ "copyableText"
+ "credentialForTrust:"
+ "dataWithContentsOfFile:"
+ "defaultManager"
+ "did not recieve download response!"
+ "dmc_setAltDSID:"
+ "dmc_setDSID:"
+ "dmc_setPersonaIdentifier:"
+ "domain of download does not match domain of initial URL from cloud config!"
+ "download canceled! "
+ "download did Start!"
+ "download did create destination"
+ "download failed with error from WKDownload!: %@"
+ "downloadDestination"
+ "downloadedProfileData"
+ "editMenuInteraction"
+ "editMenuInteraction:menuForConfiguration:suggestedActions:"
+ "editMenuInteraction:targetRectForConfiguration:"
+ "editMenuInteraction:willDismissMenuForConfiguration:animator:"
+ "editMenuInteraction:willPresentMenuForConfiguration:animator:"
+ "enrollmentFlowController:didReceiveCloudConfiguration:"
+ "ensureNetworkConnectionWithCompletionHandler:"
+ "errorWithDomain:code:userInfo:"
+ "evaluateAuthenticationChallenge:withCompletionHandler:"
+ "evaluating trust for %@ using %lu anchor certs"
+ "fetchCloudConfigWithCompletionHandler:"
+ "fetchEnrollmentProfileWithWebAuthURL:machineInfo:anchorCertificateRefs:completionHandler:"
+ "generalPasteboard"
+ "gestureRecognizers"
+ "indexPathForCell:"
+ "initWithAccountType:"
+ "initWithDelegate:"
+ "initWithFrame:configuration:"
+ "initWithNetworkAvailableHandler:"
+ "initWithTarget:action:"
+ "initWithURL:"
+ "isAwaitingDeviceConfigured"
+ "isDeviceConfigured"
+ "isManagedAppleID"
+ "isNetworkAvailableWithFlags:"
+ "isVisionDevice"
+ "loadRequest:"
+ "localizedStringWithFormat:"
+ "longPress"
+ "machineInfo"
+ "mainBundle"
+ "markCloudConfigurationAsUICompleted"
+ "no delegate defined for buddy web auth!"
+ "nodename"
+ "nonPersistentDataStore"
+ "preferences"
+ "presentEditMenuWithConfiguration:"
+ "processPool"
+ "protectionSpace"
+ "reachability"
+ "recieved 404 response from website!"
+ "recievedProfile:"
+ "removeItemAtPath:error:"
+ "requestMDMUsernameAndPasswordWithCompletionHandler:"
+ "requestSoftwareUpdateWithOSVersion:buildVersion:completionHandler:"
+ "requestUserConsentWithCloudConfig:completionHandler:"
+ "response"
+ "restoreCloudConfigAndMDMProfileFromSetAsideDataWithCompletion:"
+ "restoreSetAsideCloudConfigAndProfilesWithCompletionHandler:"
+ "retrieveCloudConfigurationDetailsCompletionBlock:"
+ "saveVerifiedAccount:error:"
+ "serverTrust"
+ "setAccountDescription:"
+ "setActive:"
+ "setAnchorCerts:"
+ "setAuthenticated:"
+ "setAvailableHanlder:"
+ "setAwaitDeviceConfigurationCompletionHandler:"
+ "setCopyableText:"
+ "setDownloadDestination:"
+ "setDownloadedProfileData:"
+ "setEditMenuInteraction:"
+ "setLongPress:"
+ "setMachineInfo:"
+ "setNavigationDelegate:"
+ "setReachability:"
+ "setString:"
+ "setUIDelegate:"
+ "setUsernameAndPasswordCompletionHandler:"
+ "setValue:forHTTPHeaderField:"
+ "setView:"
+ "setWebURL:"
+ "setWebURLCompletionHandler:"
+ "setWebView:"
+ "setWebsiteDataStore:"
+ "shouldSimulateMDMAccountDrivenEnrollment"
+ "showAwaitingDeviceConfigurationScene"
+ "showFetchingCloudConfigurationScene"
+ "simluatedMDMAccountDrivenEnrollmentAuthenticationResults"
+ "startInBuddyEnrollment"
+ "startInBuddyEnrollmentFlowRestartIfFail:completionHandler:"
+ "startMonitoring"
+ "statusCode"
+ "stopLoading"
+ "storeCloudConfig:completionHandler:"
+ "systemWhiteColor"
+ "the download process crashed!"
+ "user"
+ "usernameAndPasswordCompletionHandler"
+ "v16@?0@\"NSString\"8"
+ "v20@?0@\"NSString\"8B16"
+ "v24@0:8@\"NSData\"16"
+ "v24@0:8@\"WKWebView\"16"
+ "v24@0:8@\"_WKDownload\"16"
+ "v24@0:8@?<v@?>16"
+ "v24@0:8@?<v@?@\"NSDictionary\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"NSString\"@\"NSString\"B>16"
+ "v24@0:8^{__SCNetworkReachability=}16"
+ "v24@?0@\"NSError\"8@\"NSDictionary\"16"
+ "v32@0:8@\"DMCEnrollmentFlowController\"16@\"NSDictionary\"24"
+ "v32@0:8@\"NSDictionary\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"NSDictionary\"16@?<v@?B>24"
+ "v32@0:8@\"WKWebView\"16@\"<UIEditMenuInteractionAnimating>\"24"
+ "v32@0:8@\"WKWebView\"16@\"UIViewController\"24"
+ "v32@0:8@\"WKWebView\"16@\"WKContextMenuElementInfo\"24"
+ "v32@0:8@\"WKWebView\"16@\"WKNavigation\"24"
+ "v32@0:8@\"_WKDownload\"16@\"NSError\"24"
+ "v32@0:8@\"_WKDownload\"16@\"NSString\"24"
+ "v32@0:8@\"_WKDownload\"16@\"NSURL\"24"
+ "v32@0:8@\"_WKDownload\"16@\"NSURLResponse\"24"
+ "v32@0:8@\"_WKDownload\"16Q24"
+ "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"NSError\">32"
+ "v40@0:8@\"UIEditMenuInteraction\"16@\"UIEditMenuConfiguration\"24@\"<UIEditMenuInteractionAnimating>\"32"
+ "v40@0:8@\"WKWebView\"16@\"NSString\"24@?<v@?q>32"
+ "v40@0:8@\"WKWebView\"16@\"NSURLAuthenticationChallenge\"24@?<v@?B>32"
+ "v40@0:8@\"WKWebView\"16@\"NSURLAuthenticationChallenge\"24@?<v@?q@\"NSURLCredential\">32"
+ "v40@0:8@\"WKWebView\"16@\"WKContextMenuElementInfo\"24@\"<UIContextMenuInteractionCommitAnimating>\"32"
+ "v40@0:8@\"WKWebView\"16@\"WKContextMenuElementInfo\"24@?<v@?@\"UIContextMenuConfiguration\">32"
+ "v40@0:8@\"WKWebView\"16@\"WKNavigation\"24@\"NSError\"32"
+ "v40@0:8@\"WKWebView\"16@\"WKNavigationAction\"24@\"WKDownload\"32"
+ "v40@0:8@\"WKWebView\"16@\"WKNavigationAction\"24@?<v@?q>32"
+ "v40@0:8@\"WKWebView\"16@\"WKNavigationResponse\"24@\"WKDownload\"32"
+ "v40@0:8@\"WKWebView\"16@\"WKNavigationResponse\"24@?<v@?q>32"
+ "v40@0:8@\"_WKDownload\"16@\"NSString\"24@?<v@?B@\"NSString\">32"
+ "v40@0:8@\"_WKDownload\"16@\"NSURLAuthenticationChallenge\"24@?<v@?q@\"NSURLCredential\">32"
+ "v48@0:8@\"NSURL\"16@\"NSData\"24@\"NSArray\"32@?<v@?@\"NSData\"B@\"NSError\">40"
+ "v48@0:8@\"WKWebView\"16@\"NSString\"24@\"WKFrameInfo\"32@?<v@?>40"
+ "v48@0:8@\"WKWebView\"16@\"NSString\"24@\"WKFrameInfo\"32@?<v@?B>40"
+ "v48@0:8@\"WKWebView\"16@\"WKNavigationAction\"24@\"WKWebpagePreferences\"32@?<v@?q@\"WKWebpagePreferences\">40"
+ "v48@0:8@\"WKWebView\"16@\"WKSecurityOrigin\"24@\"WKFrameInfo\"32@?<v@?q>40"
+ "v48@0:8@\"_WKDownload\"16Q24Q32Q40"
+ "v48@0:8@16Q24Q32Q40"
+ "v56@0:8@\"WKWebView\"16@\"NSString\"24@\"NSString\"32@\"WKFrameInfo\"40@?<v@?@\"NSString\">48"
+ "v56@0:8@\"WKWebView\"16@\"WKSecurityOrigin\"24@\"WKFrameInfo\"32q40@?<v@?q>48"
+ "v56@0:8@16@24@32q40@?48"
+ "verifyNetworkFlags:"
+ "we downloaded a profile with data length of %@!"
+ "webAuthCanceled:"
+ "webURL"
+ "webURLCompletionHandler"
+ "webView"
+ "webView:authenticationChallenge:shouldAllowDeprecatedTLS:"
+ "webView:commitPreviewingViewController:"
+ "webView:contextMenuConfigurationForElement:completionHandler:"
+ "webView:contextMenuDidEndForElement:"
+ "webView:contextMenuForElement:willCommitWithAnimator:"
+ "webView:contextMenuWillPresentForElement:"
+ "webView:createWebViewWithConfiguration:forNavigationAction:windowFeatures:"
+ "webView:decidePolicyForNavigationAction:decisionHandler:"
+ "webView:decidePolicyForNavigationAction:preferences:decisionHandler:"
+ "webView:decidePolicyForNavigationResponse:decisionHandler:"
+ "webView:didCommitNavigation:"
+ "webView:didFailNavigation:withError:"
+ "webView:didFailProvisionalNavigation:withError:"
+ "webView:didFinishNavigation:"
+ "webView:didReceiveAuthenticationChallenge:completionHandler:"
+ "webView:didReceiveServerRedirectForProvisionalNavigation:"
+ "webView:didStartProvisionalNavigation:"
+ "webView:navigationAction:didBecomeDownload:"
+ "webView:navigationResponse:didBecomeDownload:"
+ "webView:previewingViewControllerForElement:defaultActions:"
+ "webView:requestDeviceOrientationAndMotionPermissionForOrigin:initiatedByFrame:decisionHandler:"
+ "webView:requestMediaCapturePermissionForOrigin:initiatedByFrame:type:decisionHandler:"
+ "webView:runJavaScriptAlertPanelWithMessage:initiatedByFrame:completionHandler:"
+ "webView:runJavaScriptConfirmPanelWithMessage:initiatedByFrame:completionHandler:"
+ "webView:runJavaScriptTextInputPanelWithPrompt:defaultText:initiatedByFrame:completionHandler:"
+ "webView:shouldPreviewElement:"
+ "webView:showLockdownModeFirstUseMessage:completionHandler:"
+ "webView:willDismissEditMenuWithAnimator:"
+ "webView:willPresentEditMenuWithAnimator:"
+ "webViewDidClose:"
+ "webViewWebContentProcessDidTerminate:"
+ "webview didReceiveAuthenticationChallenge"
+ "wkdownload didReceiveAuthenticationChallenge"
+ "www.apple.com"
+ "x-apple-aspen-deviceinfo"
+ "{CGRect={CGPoint=dd}{CGSize=dd}}32@0:8@\"UIEditMenuInteraction\"16@\"UIEditMenuConfiguration\"24"
+ "{CGRect={CGPoint=dd}{CGSize=dd}}32@0:8@16@24"
- "AKMDMInfoRequired"
- "modelSpecificLocalizedStringKeyForKey:"

```
