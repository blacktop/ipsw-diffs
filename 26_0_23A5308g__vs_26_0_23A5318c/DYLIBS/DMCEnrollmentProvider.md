## DMCEnrollmentProvider

> `/System/Library/PrivateFrameworks/DMCEnrollmentProvider.framework/DMCEnrollmentProvider`

```diff

-50.0.0.0.0
-  __TEXT.__text: 0x4df88
-  __TEXT.__auth_stubs: 0xfc0
-  __TEXT.__objc_methlist: 0x70d0
-  __TEXT.__const: 0x4b4
-  __TEXT.__oslogstring: 0x1f0f
-  __TEXT.__cstring: 0x2cb5
+52.0.0.0.0
+  __TEXT.__text: 0x4e560
+  __TEXT.__auth_stubs: 0xfd0
+  __TEXT.__objc_methlist: 0x70e4
+  __TEXT.__const: 0x4c4
+  __TEXT.__oslogstring: 0x211f
+  __TEXT.__cstring: 0x2d45
   __TEXT.__gcc_except_tab: 0x7a0
   __TEXT.__dlopen_cstrs: 0x47
   __TEXT.__ustring: 0xa8
   __TEXT.__swift5_typeref: 0x1b6
+  __TEXT.__swift5_capture: 0x9c
+  __TEXT.__swift_as_entry: 0x1c
+  __TEXT.__swift_as_ret: 0x28
   __TEXT.__swift5_reflstr: 0x47
   __TEXT.__swift5_assocty: 0x38
   __TEXT.__constg_swiftt: 0x88
   __TEXT.__swift5_fieldmd: 0x54
   __TEXT.__swift5_proto: 0x10
   __TEXT.__swift5_types: 0xc
-  __TEXT.__swift5_capture: 0x9c
-  __TEXT.__swift_as_entry: 0x1c
-  __TEXT.__swift_as_ret: 0x28
-  __TEXT.__unwind_info: 0x1588
+  __TEXT.__unwind_info: 0x1568
   __TEXT.__eh_frame: 0x480
-  __TEXT.__objc_classname: 0x117c
-  __TEXT.__objc_methname: 0x14368
-  __TEXT.__objc_methtype: 0x498c
-  __TEXT.__objc_stubs: 0xd1a0
-  __DATA_CONST.__got: 0xeb0
+  __TEXT.__objc_classname: 0x117b
+  __TEXT.__objc_methname: 0x14452
+  __TEXT.__objc_methtype: 0x4932
+  __TEXT.__objc_stubs: 0xd280
+  __DATA_CONST.__got: 0xec0
   __DATA_CONST.__const: 0x1038
   __DATA_CONST.__objc_classlist: 0x310
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x198
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x48b8
+  __DATA_CONST.__objc_selrefs: 0x48d0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x258
   __DATA_CONST.__objc_arraydata: 0xc8
-  __AUTH_CONST.__auth_got: 0x7f0
+  __AUTH_CONST.__auth_got: 0x7f8
   __AUTH_CONST.__const: 0x4a0
-  __AUTH_CONST.__cfstring: 0x2f00
-  __AUTH_CONST.__objc_const: 0x113f8
+  __AUTH_CONST.__cfstring: 0x2f60
+  __AUTH_CONST.__objc_const: 0x11430
   __AUTH_CONST.__objc_arrayobj: 0x168
   __AUTH_CONST.__objc_intobj: 0x120
   __AUTH_CONST.__objc_floatobj: 0x30
   __AUTH.__objc_data: 0x1bf0
   __AUTH.__data: 0xc0
-  __DATA.__objc_ivar: 0x5e4
+  __DATA.__objc_ivar: 0x5ec
   __DATA.__data: 0x13f8
   __DATA.__bss: 0x260
   __DATA.__common: 0x18

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 261A0E21-4A8E-3043-BA19-EEEAF78D44AC
-  Functions: 2177
-  Symbols:   8184
-  CStrings:  4618
+  UUID: 25137EEE-E366-3F93-885A-48DE6901B95F
+  Functions: 2183
+  Symbols:   8209
+  CStrings:  4634
 
Symbols:
+ -[DMCEnrollmentFlowManagedConfigurationHelper isLockdownModeEnabled]
+ -[DMCEnrollmentInterface _presentSignInUnavailableAccountModificationRestricted]
+ -[DMCEnrollmentInterface _presentSignInUnavailableAlertWithMessage:]
+ -[DMCEnrollmentInterface _presentSignInUnavailableLockdownMode]
+ -[DMCEnrollmentInterface _specifierForButtonNamed:]
+ -[DMCEnrollmentInterface _specifiersForSignInButtonWithSelector:]
+ -[DMCEnrollmentInterface debugSpecifiers]
+ -[DMCEnrollmentInterface migrationSpecifiers]
+ -[DMCEnrollmentInterface setDebugSpecifiers:]
+ -[DMCEnrollmentInterface setMigrationSpecifiers:]
+ -[DMCTestWebViewController _evaluateAuthenticationChallenge:withCompletionHandler:]
+ -[DMCTestWebViewController download:decideDestinationUsingResponse:suggestedFilename:completionHandler:]
+ -[DMCTestWebViewController download:didFailWithError:resumeData:]
+ -[DMCTestWebViewController download:didReceiveAuthenticationChallenge:completionHandler:]
+ -[DMCTestWebViewController downloadDidFinish:]
+ -[DMCTestWebViewController downloadedResponseData]
+ -[DMCTestWebViewController setDownloadedResponseData:]
+ -[DMCTestWebViewController setWillDownloadError:]
+ -[DMCTestWebViewController webView:navigationResponse:didBecomeDownload:]
+ -[DMCTestWebViewController willDownloadError]
+ GCC_except_table50
+ _DMCHTTPContentTypeApplicationJSON
+ _OBJC_CLASS_$_DMCHTTPRequestor
+ _OBJC_IVAR_$_DMCEnrollmentInterface._debugSpecifiers
+ _OBJC_IVAR_$_DMCEnrollmentInterface._migrationSpecifiers
+ _OBJC_IVAR_$_DMCTestWebViewController._downloadedResponseData
+ _OBJC_IVAR_$_DMCTestWebViewController._willDownloadError
+ _SecTrustEvaluateWithError
+ _SecTrustGetTrustResult
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_WKDownloadDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_WKDownloadDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_WKDownloadDelegate
+ __OBJC_$_PROTOCOL_REFS_WKDownloadDelegate
+ __OBJC_LABEL_PROTOCOL_$_WKDownloadDelegate
+ __OBJC_PROTOCOL_$_WKDownloadDelegate
+ ___118-[DMCBYODEnrollmentFlowUIPresenter requestWebAuthenticationWithWebAuthURL:authenticator:authParams:completionHandler:]_block_invoke.60
+ ___135-[DMCBYODEnrollmentFlowUIPresenter requestMAIDAuthenticationWithManagedAppleID:personaID:ephemeral:requireAppleMAID:completionHandler:]_block_invoke.65
+ ___135-[DMCBYODEnrollmentFlowUIPresenter requestMAIDAuthenticationWithManagedAppleID:personaID:ephemeral:requireAppleMAID:completionHandler:]_block_invoke_2.66
+ ___135-[DMCBYODEnrollmentFlowUIPresenter requestMAIDAuthenticationWithManagedAppleID:personaID:ephemeral:requireAppleMAID:completionHandler:]_block_invoke_3.69
+ ___block_literal_global.123
+ _objc_msgSend$_evaluateAuthenticationChallenge:withCompletionHandler:
+ _objc_msgSend$_presentSignInUnavailableAlertWithMessage:
+ _objc_msgSend$_specifierForButtonNamed:
+ _objc_msgSend$_specifiersForSignInButtonWithSelector:
+ _objc_msgSend$debugSpecifiers
+ _objc_msgSend$downloadedResponseData
+ _objc_msgSend$fileURLWithPath:
+ _objc_msgSend$isLockdownModeEnabled
+ _objc_msgSend$jsonDictFromResponse:
+ _objc_msgSend$migrationSpecifiers
+ _objc_msgSend$parsePredefined403ErrorWithResponseDictionary:outError:
+ _objc_msgSend$setDebugSpecifiers:
+ _objc_msgSend$setDownloadedResponseData:
+ _objc_msgSend$setMigrationSpecifiers:
+ _objc_msgSend$setWillDownloadError:
+ _objc_msgSend$willDownloadError
- -[DMCEnrollmentInterface _specifiersForManagedAccountSignIn]
- -[DMCEnrollmentInterface beginMigrationButton]
- -[DMCEnrollmentInterface setBeginMigrationButton:]
- -[DMCTestWebViewController _download:decideDestinationWithSuggestedFilename:completionHandler:]
- -[DMCTestWebViewController _download:didCreateDestination:]
- -[DMCTestWebViewController _download:didFailWithError:]
- -[DMCTestWebViewController _download:didReceiveAuthenticationChallenge:completionHandler:]
- -[DMCTestWebViewController _downloadDidCancel:]
- -[DMCTestWebViewController _downloadDidFinish:]
- -[DMCTestWebViewController _downloadDidStart:]
- -[DMCTestWebViewController _downloadProcessDidCrash:]
- -[DMCTestWebViewController downloadedProfileData]
- -[DMCTestWebViewController evaluateAuthenticationChallenge:withCompletionHandler:]
- -[DMCTestWebViewController setDownloadedProfileData:]
- GCC_except_table49
- _OBJC_IVAR_$_DMCEnrollmentInterface._beginMigrationButton
- _OBJC_IVAR_$_DMCTestWebViewController._downloadedProfileData
- _SecTrustEvaluate
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT__WKDownloadDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES__WKDownloadDelegate
- __OBJC_$_PROTOCOL_REFS__WKDownloadDelegate
- __OBJC_LABEL_PROTOCOL_$__WKDownloadDelegate
- __OBJC_PROTOCOL_$__WKDownloadDelegate
- ___118-[DMCBYODEnrollmentFlowUIPresenter requestWebAuthenticationWithWebAuthURL:authenticator:authParams:completionHandler:]_block_invoke_2
- ___135-[DMCBYODEnrollmentFlowUIPresenter requestMAIDAuthenticationWithManagedAppleID:personaID:ephemeral:requireAppleMAID:completionHandler:]_block_invoke.64
- ___135-[DMCBYODEnrollmentFlowUIPresenter requestMAIDAuthenticationWithManagedAppleID:personaID:ephemeral:requireAppleMAID:completionHandler:]_block_invoke_2.65
- ___135-[DMCBYODEnrollmentFlowUIPresenter requestMAIDAuthenticationWithManagedAppleID:personaID:ephemeral:requireAppleMAID:completionHandler:]_block_invoke_3.68
- ___block_literal_global.118
- _objc_msgSend$_setDownloadDelegate:
- _objc_msgSend$_specifiersForManagedAccountSignIn
- _objc_msgSend$beginMigrationButton
- _objc_msgSend$configuration
- _objc_msgSend$downloadedProfileData
- _objc_msgSend$evaluateAuthenticationChallenge:withCompletionHandler:
- _objc_msgSend$processPool
- _objc_msgSend$setBeginMigrationButton:
- _objc_msgSend$setDownloadedProfileData:
CStrings:
+ "!\x81"
+ "ACCOUNTS_SIGN_IN_UNAVAILABLE"
+ "ACCOUNTS_SIGN_IN_UNAVAILABLE_ACCOUNT_MODIFICATION_RESTRICTED"
+ "ACCOUNTS_SIGN_IN_UNAVAILABLE_LOCKDOWN_MODE"
+ "ASWebAuthenticationSession finished with callback URL: %{public}@, error: %{public}@"
+ "Authentication started. ephemeral: %d, requireAppleMAID: %d"
+ "Beginning web authentication with URL: %{public}@"
+ "Could not evaluate trust! Error: %{public}@"
+ "Could not get trust result! Error Code:  %d"
+ "DMCEnrollmentInstallAppButtonView: App state did change: %{public}@"
+ "DebugEnrollmentGroup"
+ "Evaluating trust for %@ using %lu anchor certs"
+ "No-op Managed Sign In button because Lockdown Mode is enabled"
+ "No-op Managed Sign In button because account modification is restricted"
+ "T@\"NSArray\",&,N,V_debugSpecifiers"
+ "T@\"NSArray\",&,N,V_migrationSpecifiers"
+ "T@\"NSData\",&,N,V_downloadedResponseData"
+ "T@\"NSString\",&,N,V_downloadDestination"
+ "TB,N,V_willDownloadError"
+ "WKDownloadDelegate"
+ "WebAuthView received 403 error %{public}@!"
+ "_debugSpecifiers"
+ "_downloadedResponseData"
+ "_evaluateAuthenticationChallenge:withCompletionHandler:"
+ "_migrationSpecifiers"
+ "_presentSignInUnavailableAccountModificationRestricted"
+ "_presentSignInUnavailableAlertWithMessage:"
+ "_presentSignInUnavailableLockdownMode"
+ "_specifierForButtonNamed:"
+ "_specifiersForSignInButtonWithSelector:"
+ "_willDownloadError"
+ "debugSpecifiers"
+ "download failed with error from WKDownload!: %{public}@"
+ "download:decideDestinationUsingResponse:suggestedFilename:completionHandler:"
+ "download:decidePlaceholderPolicy:"
+ "download:didFailWithError:resumeData:"
+ "download:didReceiveAuthenticationChallenge:completionHandler:"
+ "download:didReceiveFinalURL:"
+ "download:didReceivePlaceholderURL:completionHandler:"
+ "download:willPerformHTTPRedirection:newRequest:decisionHandler:"
+ "downloadDidFinish:"
+ "downloadedResponseData"
+ "fileURLWithPath:"
+ "isLockdownModeEnabled"
+ "jsonDictFromResponse:"
+ "migrationSpecifiers"
+ "parsePredefined403ErrorWithResponseDictionary:outError:"
+ "recieved 403 response from website!"
+ "setDebugSpecifiers:"
+ "setDownloadedResponseData:"
+ "setMigrationSpecifiers:"
+ "setWillDownloadError:"
+ "v24@0:8@\"WKDownload\"16"
+ "v32@0:8@\"WKDownload\"16@\"NSURL\"24"
+ "v32@0:8@\"WKDownload\"16@?<v@?q@\"NSURL\">24"
+ "v40@0:8@\"WKDownload\"16@\"NSError\"24@\"NSData\"32"
+ "v40@0:8@\"WKDownload\"16@\"NSURL\"24@?<v@?>32"
+ "v40@0:8@\"WKDownload\"16@\"NSURLAuthenticationChallenge\"24@?<v@?q@\"NSURLCredential\">32"
+ "v48@0:8@\"WKDownload\"16@\"NSHTTPURLResponse\"24@\"NSURLRequest\"32@?<v@?q>40"
+ "v48@0:8@\"WKDownload\"16@\"NSURLResponse\"24@\"NSString\"32@?<v@?@\"NSURL\">40"
+ "we downloaded a profile with data length of %{public}@!"
+ "we downloaded an error with data length of %{public}@!"
+ "webview navigationResponse didBecomeDownload"
+ "willDownloadError"
+ "wkdownload decideDestinationUsingResponse"
+ "wkdownload downloadDidFinish"
- "!q"
- "@\"NSString\"40@0:8@\"_WKDownload\"16@\"NSString\"24^B32"
- "@40@0:8@16@24^B32"
- "B32@0:8@\"_WKDownload\"16@\"NSString\"24"
- "Could not evaluate trust! Error Code:  %d"
- "Debugging"
- "No Managed Sign In button because account modification is disallowed"
- "T@\"NSData\",&,V_downloadedProfileData"
- "T@\"NSString\",&,V_downloadDestination"
- "T@\"PSSpecifier\",&,N,V_beginMigrationButton"
- "_WKDownloadDelegate"
- "_beginMigrationButton"
- "_download:decideDestinationWithSuggestedFilename:allowOverwrite:"
- "_download:decideDestinationWithSuggestedFilename:completionHandler:"
- "_download:didCreateDestination:"
- "_download:didFailWithError:"
- "_download:didReceiveAuthenticationChallenge:completionHandler:"
- "_download:didReceiveData:"
- "_download:didReceiveResponse:"
- "_download:didReceiveServerRedirectToURL:"
- "_download:didWriteData:totalBytesWritten:totalBytesExpectedToWrite:"
- "_download:shouldDecodeSourceDataOfMIMEType:"
- "_downloadDidCancel:"
- "_downloadDidFinish:"
- "_downloadDidStart:"
- "_downloadProcessDidCrash:"
- "_downloadedProfileData"
- "_setDownloadDelegate:"
- "_specifiersForManagedAccountSignIn"
- "beginMigrationButton"
- "configuration"
- "download canceled! "
- "download did Start!"
- "download did create destination"
- "download failed with error from WKDownload!: %@"
- "downloadedProfileData"
- "evaluateAuthenticationChallenge:withCompletionHandler:"
- "evaluating trust for %@ using %lu anchor certs"
- "processPool"
- "setBeginMigrationButton:"
- "setDownloadedProfileData:"
- "the download process crashed!"
- "v24@0:8@\"_WKDownload\"16"
- "v32@0:8@\"_WKDownload\"16@\"NSError\"24"
- "v32@0:8@\"_WKDownload\"16@\"NSString\"24"
- "v32@0:8@\"_WKDownload\"16@\"NSURL\"24"
- "v32@0:8@\"_WKDownload\"16@\"NSURLResponse\"24"
- "v32@0:8@\"_WKDownload\"16Q24"
- "v40@0:8@\"_WKDownload\"16@\"NSString\"24@?<v@?B@\"NSString\">32"
- "v40@0:8@\"_WKDownload\"16@\"NSURLAuthenticationChallenge\"24@?<v@?q@\"NSURLCredential\">32"
- "v48@0:8@\"_WKDownload\"16Q24Q32Q40"
- "v48@0:8@16Q24Q32Q40"
- "we downloaded a profile with data length of %@!"

```
