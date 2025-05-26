## PlatformSSO

> `/System/Library/PrivateFrameworks/PlatformSSO.framework/PlatformSSO`

```diff

-384.100.11.0.0
-  __TEXT.__text: 0xafde4
+384.120.7.0.0
+  __TEXT.__text: 0xb02c0
   __TEXT.__auth_stubs: 0x1540
-  __TEXT.__objc_methlist: 0x65dc
+  __TEXT.__objc_methlist: 0x6604
   __TEXT.__const: 0xfc4
-  __TEXT.__cstring: 0xd978
-  __TEXT.__oslogstring: 0x2a5c
-  __TEXT.__gcc_except_tab: 0xeb8
+  __TEXT.__cstring: 0xda26
+  __TEXT.__oslogstring: 0x2a8c
+  __TEXT.__gcc_except_tab: 0xecc
   __TEXT.__dlopen_cstrs: 0x162
-  __TEXT.__unwind_info: 0x24f4
+  __TEXT.__unwind_info: 0x2514
   __TEXT.__objc_classname: 0xdfc
-  __TEXT.__objc_methname: 0xe7b0
+  __TEXT.__objc_methname: 0xe868
   __TEXT.__objc_methtype: 0x294b
-  __TEXT.__objc_stubs: 0x9bc0
+  __TEXT.__objc_stubs: 0x9c60
   __DATA_CONST.__got: 0x2d0
   __DATA_CONST.__const: 0x2a48
   __DATA_CONST.__objc_classlist: 0x4a0
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x120e0
-  __DATA_CONST.__objc_selrefs: 0x30a0
+  __DATA_CONST.__objc_const: 0x12120
+  __DATA_CONST.__objc_selrefs: 0x30d0
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_classrefs: 0x608
   __DATA_CONST.__objc_superrefs: 0x218
   __DATA_CONST.__objc_arraydata: 0x88
   __AUTH_CONST.__objc_const: 0x37e8
-  __AUTH_CONST.__cfstring: 0x9060
+  __AUTH_CONST.__cfstring: 0x9040
   __AUTH_CONST.__const: 0xb60
   __AUTH_CONST.__objc_intobj: 0x168
   __AUTH_CONST.__auth_ptr: 0x20

   __AUTH.__objc_data: 0x2e40
   __DATA.__objc_ivar: 0x6fc
   __DATA.__data: 0xed0
-  __DATA.__bss: 0x449
+  __DATA.__bss: 0x451
   __DATA.__common: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
-  Functions: 4707
-  Symbols:   14032
-  CStrings:  4820
+  Functions: 4716
+  Symbols:   14058
+  CStrings:  4829
 
Symbols:
+ -[POAgentAuthenticationProcess handleKeyUpdatesWithPasswordContext:]
+ -[POAgentAuthenticationProcess handleKeyUpdatesWithPasswordContext:].cold.1
+ -[POConfigurationManager createAppSSOCachePath]
+ -[POConfigurationManager createAppSSOCachePath].cold.1
+ -[PODaemonConnection createAppSSOCachePathWithCompletion:]
+ -[PODaemonProcess createAppSSOCachePathWithCompletion:]
+ -[PODaemonProcess createAppSSOCachePathWithCompletion:].cold.1
+ GCC_except_table203
+ GCC_except_table59
+ GCC_except_table75
+ _AppSSOLibrary
+ ___100-[POAgentAuthenticationProcess handleKerberosMappingForTokens:loginConfiguration:userConfiguration:]_block_invoke.557
+ ___100-[POAgentAuthenticationProcess handleKerberosMappingForTokens:loginConfiguration:userConfiguration:]_block_invoke.557.cold.1
+ ___100-[POAgentAuthenticationProcess handleKerberosMappingForTokens:loginConfiguration:userConfiguration:]_block_invoke.563
+ ___100-[POAgentAuthenticationProcess handleKerberosMappingForTokens:loginConfiguration:userConfiguration:]_block_invoke.563.cold.1
+ ___100-[POAgentAuthenticationProcess handleKerberosMappingForTokens:loginConfiguration:userConfiguration:]_block_invoke.567
+ ___100-[POAgentAuthenticationProcess handleKerberosMappingForTokens:loginConfiguration:userConfiguration:]_block_invoke.567.cold.1
+ ___108-[POAgentAuthenticationProcess userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:]_block_invoke.675
+ ___119-[POAgentAuthenticationProcess handleUserRegistrationForUser:repair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke.464
+ ___119-[POAgentAuthenticationProcess handleUserRegistrationForUser:repair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke.464.cold.1
+ ___119-[POAgentAuthenticationProcess handleUserRegistrationForUser:repair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke.473
+ ___119-[POAgentAuthenticationProcess handleUserRegistrationForUser:repair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke.473.cold.1
+ ___123-[POAgentAuthenticationProcess handleDeviceAndUserRegistrationForRepair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke.448
+ ___123-[POAgentAuthenticationProcess handleDeviceAndUserRegistrationForRepair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke.448.cold.1
+ ___123-[POAgentAuthenticationProcess handleDeviceAndUserRegistrationForRepair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke.451
+ ___123-[POAgentAuthenticationProcess handleDeviceAndUserRegistrationForRepair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke.451.cold.1
+ ___123-[POAgentAuthenticationProcess handleDeviceAndUserRegistrationForRepair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke.458
+ ___39-[PODaemonConnection _connectToService]_block_invoke.80
+ ___39-[PODaemonConnection _connectToService]_block_invoke.80.cold.1
+ ___47-[POConfigurationManager createAppSSOCachePath]_block_invoke
+ ___54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.355
+ ___54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.355.cold.1
+ ___54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.364
+ ___54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.364.cold.1
+ ___54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.374
+ ___54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.374.cold.1
+ ___54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.390
+ ___54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.390.cold.1
+ ___54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.407
+ ___54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.414
+ ___54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.414.cold.1
+ ___54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.422
+ ___54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.422.cold.1
+ ___54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke_2.403
+ ___54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke_2.403.cold.1
+ ___54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke_2.408
+ ___54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke_2.408.cold.1
+ ___54-[POAgentAuthenticationProcess isCurrentSSOExtension:]_block_invoke.607
+ ___54-[POAgentAuthenticationProcess isCurrentSSOExtension:]_block_invoke.607.cold.1
+ ___56-[POAgentAuthenticationProcess _startDeviceRegistration]_block_invoke.318
+ ___56-[POAgentAuthenticationProcess _startDeviceRegistration]_block_invoke.323
+ ___56-[POAgentAuthenticationProcess _startDeviceRegistration]_block_invoke.323.cold.1
+ ___56-[POAgentAuthenticationProcess _startDeviceRegistration]_block_invoke.333
+ ___56-[POAgentAuthenticationProcess _startDeviceRegistration]_block_invoke.333.cold.1
+ ___56-[POAgentAuthenticationProcess _startDeviceRegistration]_block_invoke.346
+ ___56-[POAgentAuthenticationProcess _startDeviceRegistration]_block_invoke.347
+ ___58-[PODaemonConnection createAppSSOCachePathWithCompletion:]_block_invoke
+ ___58-[PODaemonConnection createAppSSOCachePathWithCompletion:]_block_invoke.cold.1
+ ___59-[POAgentAuthenticationProcess finishRegistrationWithRetry]_block_invoke.438
+ ___59-[POAgentAuthenticationProcess handleConfigurationChanged:]_block_invoke.493
+ ___59-[POAgentAuthenticationProcess handleConfigurationChanged:]_block_invoke.493.cold.1
+ ___60-[POAgentAuthenticationProcess handleUnfinishedTGTExchanges]_block_invoke.587
+ ___60-[POAgentAuthenticationProcess handleUnfinishedTGTExchanges]_block_invoke.587.cold.1
+ ___60-[POAgentAuthenticationProcess requestDidCompleteWithError:]_block_invoke.616
+ ___60-[POAgentAuthenticationProcess requestDidCompleteWithError:]_block_invoke.616.cold.1
+ ___60-[POAgentAuthenticationProcess requestDidCompleteWithError:]_block_invoke.622
+ ___63-[POAgentAuthenticationProcess handleKeyRequestWithCompletion:]_block_invoke.255
+ ___63-[POAgentAuthenticationProcess handleKeyRequestWithCompletion:]_block_invoke.255.cold.1
+ ___63-[POAgentAuthenticationProcess handleKeyRequestWithCompletion:]_block_invoke.265
+ ___63-[POAgentAuthenticationProcess handleKeyRequestWithCompletion:]_block_invoke.265.cold.1
+ ___63-[POAgentAuthenticationProcess handleKeyRequestWithCompletion:]_block_invoke.269
+ ___63-[POAgentAuthenticationProcess handleKeyRequestWithCompletion:]_block_invoke.270
+ ___63-[POAgentAuthenticationProcess handleKeyRequestWithCompletion:]_block_invoke.270.cold.1
+ ___63-[POAgentAuthenticationProcess handleKeyRequestWithCompletion:]_block_invoke.274
+ ___63-[POAgentAuthenticationProcess handleKeyRequestWithCompletion:]_block_invoke.274.cold.1
+ ___63-[POAgentAuthenticationProcess handleKeyRequestWithCompletion:]_block_invoke.278
+ ___63-[POAgentAuthenticationProcess handleKeyRequestWithCompletion:]_block_invoke.278.cold.1
+ ___69-[POAgentAuthenticationProcess handlePendingSSOTokensWithSharedData:]_block_invoke.576
+ ___69-[POAgentAuthenticationProcess handlePendingSSOTokensWithSharedData:]_block_invoke.576.cold.1
+ ___74-[POAgentAuthenticationProcess handleUserNeedsReauthenticationAfterDelay:]_block_invoke.286
+ ___74-[POAgentAuthenticationProcess handleUserNeedsReauthenticationAfterDelay:]_block_invoke.286.cold.1
+ ___74-[POAgentAuthenticationProcess handleUserNeedsReauthenticationAfterDelay:]_block_invoke.296
+ ___74-[POAgentAuthenticationProcess handleUserNeedsReauthenticationAfterDelay:]_block_invoke.296.cold.1
+ ___79-[POAgentAuthenticationProcess requestUserAuthenticationWithWindow:completion:]_block_invoke.244
+ ___79-[POAgentAuthenticationProcess requestUserAuthenticationWithWindow:completion:]_block_invoke.244.cold.1
+ ___98-[POAgentAuthenticationProcess handleRegistrationViewControllerForExtensionIdentifier:completion:]_block_invoke.530
+ ___98-[POAgentAuthenticationProcess handleRegistrationViewControllerForExtensionIdentifier:completion:]_block_invoke.530.cold.1
+ ___98-[POAgentAuthenticationProcess handleRegistrationViewControllerForExtensionIdentifier:completion:]_block_invoke.536
+ ___block_literal_global.119
+ ___block_literal_global.264
+ ___block_literal_global.266
+ ___block_literal_global.321
+ ___block_literal_global.402
+ ___block_literal_global.481
+ ___block_literal_global.543
+ ___block_literal_global.985
+ ___block_literal_global.989
+ ___getSOConfigurationHostClass_block_invoke
+ ___getSOConfigurationHostClass_block_invoke.cold.1
+ _getSOConfigurationHostClass.softClass
+ _objc_msgSend$_defaultCacheFile
+ _objc_msgSend$_initCachePath:ifNeededWithError:
+ _objc_msgSend$createAppSSOCachePathWithCompletion:
+ _objc_msgSend$handleKeyUpdatesWithPasswordContext:
+ _objc_msgSend$stringByDeletingLastPathComponent
- -[POAgentAuthenticationProcess handleConfigurationChanged:].cold.4
- GCC_except_table204
- GCC_except_table73
- ___100-[POAgentAuthenticationProcess handleKerberosMappingForTokens:loginConfiguration:userConfiguration:]_block_invoke.569
- ___100-[POAgentAuthenticationProcess handleKerberosMappingForTokens:loginConfiguration:userConfiguration:]_block_invoke.569.cold.1
- ___100-[POAgentAuthenticationProcess handleKerberosMappingForTokens:loginConfiguration:userConfiguration:]_block_invoke.575
- ___100-[POAgentAuthenticationProcess handleKerberosMappingForTokens:loginConfiguration:userConfiguration:]_block_invoke.575.cold.1
- ___100-[POAgentAuthenticationProcess handleKerberosMappingForTokens:loginConfiguration:userConfiguration:]_block_invoke.579
- ___100-[POAgentAuthenticationProcess handleKerberosMappingForTokens:loginConfiguration:userConfiguration:]_block_invoke.579.cold.1
- ___108-[POAgentAuthenticationProcess userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:]_block_invoke.687
- ___114-[POAgentAuthenticationProcess _handleLoginResult:authenticationContext:tokens:passwordContext:tokenId:tokenHash:]_block_invoke.241
- ___114-[POAgentAuthenticationProcess _handleLoginResult:authenticationContext:tokens:passwordContext:tokenId:tokenHash:]_block_invoke.241.cold.1
- ___119-[POAgentAuthenticationProcess handleUserRegistrationForUser:repair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke.476
- ___119-[POAgentAuthenticationProcess handleUserRegistrationForUser:repair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke.476.cold.1
- ___119-[POAgentAuthenticationProcess handleUserRegistrationForUser:repair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke.479.cold.1
- ___119-[POAgentAuthenticationProcess handleUserRegistrationForUser:repair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke.485
- ___123-[POAgentAuthenticationProcess handleDeviceAndUserRegistrationForRepair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke.454
- ___123-[POAgentAuthenticationProcess handleDeviceAndUserRegistrationForRepair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke.454.cold.1
- ___123-[POAgentAuthenticationProcess handleDeviceAndUserRegistrationForRepair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke.457
- ___123-[POAgentAuthenticationProcess handleDeviceAndUserRegistrationForRepair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke.457.cold.1
- ___123-[POAgentAuthenticationProcess handleDeviceAndUserRegistrationForRepair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke.464
- ___39-[PODaemonConnection _connectToService]_block_invoke.79
- ___39-[PODaemonConnection _connectToService]_block_invoke.79.cold.1
- ___54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.361
- ___54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.361.cold.1
- ___54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.370.cold.1
- ___54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.376
- ___54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.392
- ___54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.392.cold.1
- ___54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.396.cold.1
- ___54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.408
- ___54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.413
- ___54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.420.cold.1
- ___54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.426
- ___54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.428
- ___54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.428.cold.1
- ___54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke_2.409
- ___54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke_2.409.cold.1
- ___54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke_2.414
- ___54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke_2.414.cold.1
- ___54-[POAgentAuthenticationProcess isCurrentSSOExtension:]_block_invoke.619
- ___54-[POAgentAuthenticationProcess isCurrentSSOExtension:]_block_invoke.619.cold.1
- ___56-[POAgentAuthenticationProcess _startDeviceRegistration]_block_invoke.324
- ___56-[POAgentAuthenticationProcess _startDeviceRegistration]_block_invoke.329.cold.1
- ___56-[POAgentAuthenticationProcess _startDeviceRegistration]_block_invoke.335
- ___56-[POAgentAuthenticationProcess _startDeviceRegistration]_block_invoke.345.cold.1
- ___56-[POAgentAuthenticationProcess _startDeviceRegistration]_block_invoke.351
- ___56-[POAgentAuthenticationProcess _startDeviceRegistration]_block_invoke.352
- ___56-[POAgentAuthenticationProcess _startDeviceRegistration]_block_invoke.353
- ___59-[POAgentAuthenticationProcess finishRegistrationWithRetry]_block_invoke.444
- ___59-[POAgentAuthenticationProcess handleConfigurationChanged:]_block_invoke.523.cold.1
- ___59-[POAgentAuthenticationProcess handleConfigurationChanged:]_block_invoke.529
- ___59-[POAgentAuthenticationProcess handleConfigurationChanged:]_block_invoke.529.cold.1
- ___59-[POAgentAuthenticationProcess handleConfigurationChanged:]_block_invoke.535
- ___60-[POAgentAuthenticationProcess handleUnfinishedTGTExchanges]_block_invoke.599
- ___60-[POAgentAuthenticationProcess handleUnfinishedTGTExchanges]_block_invoke.599.cold.1
- ___60-[POAgentAuthenticationProcess requestDidCompleteWithError:]_block_invoke.628
- ___60-[POAgentAuthenticationProcess requestDidCompleteWithError:]_block_invoke.628.cold.1
- ___60-[POAgentAuthenticationProcess requestDidCompleteWithError:]_block_invoke.634
- ___63-[POAgentAuthenticationProcess handleKeyRequestWithCompletion:]_block_invoke.267
- ___63-[POAgentAuthenticationProcess handleKeyRequestWithCompletion:]_block_invoke.267.cold.1
- ___63-[POAgentAuthenticationProcess handleKeyRequestWithCompletion:]_block_invoke.271
- ___63-[POAgentAuthenticationProcess handleKeyRequestWithCompletion:]_block_invoke.271.cold.1
- ___63-[POAgentAuthenticationProcess handleKeyRequestWithCompletion:]_block_invoke.275
- ___63-[POAgentAuthenticationProcess handleKeyRequestWithCompletion:]_block_invoke.276
- ___63-[POAgentAuthenticationProcess handleKeyRequestWithCompletion:]_block_invoke.276.cold.1
- ___63-[POAgentAuthenticationProcess handleKeyRequestWithCompletion:]_block_invoke.280
- ___63-[POAgentAuthenticationProcess handleKeyRequestWithCompletion:]_block_invoke.280.cold.1
- ___63-[POAgentAuthenticationProcess handleKeyRequestWithCompletion:]_block_invoke.284
- ___63-[POAgentAuthenticationProcess handleKeyRequestWithCompletion:]_block_invoke.284.cold.1
- ___69-[POAgentAuthenticationProcess handlePendingSSOTokensWithSharedData:]_block_invoke.588
- ___69-[POAgentAuthenticationProcess handlePendingSSOTokensWithSharedData:]_block_invoke.588.cold.1
- ___74-[POAgentAuthenticationProcess handleUserNeedsReauthenticationAfterDelay:]_block_invoke.298
- ___74-[POAgentAuthenticationProcess handleUserNeedsReauthenticationAfterDelay:]_block_invoke.298.cold.1
- ___74-[POAgentAuthenticationProcess handleUserNeedsReauthenticationAfterDelay:]_block_invoke.308.cold.1
- ___74-[POAgentAuthenticationProcess handleUserNeedsReauthenticationAfterDelay:]_block_invoke.314
- ___79-[POAgentAuthenticationProcess requestUserAuthenticationWithWindow:completion:]_block_invoke.250
- ___79-[POAgentAuthenticationProcess requestUserAuthenticationWithWindow:completion:]_block_invoke.250.cold.1
- ___98-[POAgentAuthenticationProcess handleRegistrationViewControllerForExtensionIdentifier:completion:]_block_invoke.542
- ___98-[POAgentAuthenticationProcess handleRegistrationViewControllerForExtensionIdentifier:completion:]_block_invoke.542.cold.1
- ___98-[POAgentAuthenticationProcess handleRegistrationViewControllerForExtensionIdentifier:completion:]_block_invoke.548
- ___block_literal_global.1000
- ___block_literal_global.118
- ___block_literal_global.263
- ___block_literal_global.265
- ___block_literal_global.327
- ___block_literal_global.399
- ___block_literal_global.487
- ___block_literal_global.555
- ___block_literal_global.996
CStrings:
+ "-[POConfigurationManager createAppSSOCachePath]"
+ "-[PODaemonProcess createAppSSOCachePathWithCompletion:]"
+ "//s:Envelope/s:Body/trust:RequestSecurityTokenResponseCollection/trust:RequestSecurityTokenResponse/trust:RequestedSecurityToken/saml2:Assertion"
+ "Checking for key updates"
+ "SOConfigurationHost"
+ "_defaultCacheFile"
+ "_initCachePath:ifNeededWithError:"
+ "createAppSSOCachePath"
+ "createAppSSOCachePathWithCompletion:"
+ "failed to create cache directory at %{public}@: %{public}@"
+ "handleKeyUpdatesWithPasswordContext:"
+ "s=http://www.w3.org/2003/05/soap-envelope a=http://www.w3.org/2005/08/addressing u=http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd o=http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd  wsu=http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd saml=urn:oasis:names:tc:SAML:1.0:assertion saml2=urn:oasis:names:tc:SAML:2.0:assertion"
+ "stringByDeletingLastPathComponent"
- "Extension protocol version changed."
- "Failed to save device configuration with new capabilities in configuration changed."
- "Failed to save user configuration after token binding."
- "s=http://www.w3.org/2003/05/soap-envelope a=http://www.w3.org/2005/08/addressing u=http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd o=http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd  wsu=http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd saml=urn:oasis:names:tc:SAML:1.0:assertion"

```
