## AuthenticationServicesCore

> `/System/Library/PrivateFrameworks/AuthenticationServicesCore.framework/AuthenticationServicesCore`

```diff

-616.1.27.10.16
-  __TEXT.__text: 0x83fbc
-  __TEXT.__auth_stubs: 0x1ec0
-  __TEXT.__objc_methlist: 0x2008
-  __TEXT.__cstring: 0x46d9
+616.2.9.10.10
+  __TEXT.__text: 0x83e74
+  __TEXT.__auth_stubs: 0x1ef0
+  __TEXT.__objc_methlist: 0x1fd8
+  __TEXT.__cstring: 0x4789
   __TEXT.__ustring: 0x4bc
-  __TEXT.__oslogstring: 0x1898
+  __TEXT.__oslogstring: 0x1916
   __TEXT.__const: 0x4bc1
-  __TEXT.__gcc_except_tab: 0xd0
+  __TEXT.__gcc_except_tab: 0xb4
   __TEXT.__swift5_typeref: 0x13cd
   __TEXT.__constg_swiftt: 0x111c
   __TEXT.__swift5_reflstr: 0xcd4

   __TEXT.__swift5_capture: 0x1e8
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_protos: 0x18
-  __TEXT.__unwind_info: 0x24c4
+  __TEXT.__unwind_info: 0x2474
   __TEXT.__eh_frame: 0x2210
-  __TEXT.__objc_classname: 0x6c8
-  __TEXT.__objc_methname: 0x7d00
-  __TEXT.__objc_methtype: 0x1c02
-  __TEXT.__objc_stubs: 0x36c0
-  __DATA_CONST.__got: 0x3b8
+  __TEXT.__objc_classname: 0x6a0
+  __TEXT.__objc_methname: 0x7bfc
+  __TEXT.__objc_methtype: 0x1c24
+  __TEXT.__objc_stubs: 0x35e0
+  __DATA_CONST.__got: 0x398
   __DATA_CONST.__const: 0x738
   __DATA_CONST.__objc_classlist: 0x148
   __DATA_CONST.__objc_catlist: 0x18
-  __DATA_CONST.__objc_protolist: 0x148
+  __DATA_CONST.__objc_protolist: 0x140
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x5520
-  __DATA_CONST.__objc_selrefs: 0x1468
+  __DATA_CONST.__objc_const: 0x5418
+  __DATA_CONST.__objc_selrefs: 0x1408
   __DATA_CONST.__objc_arraydata: 0x10
   __AUTH_CONST.__cfstring: 0x19e0
   __AUTH_CONST.__objc_const: 0x0
-  __AUTH_CONST.__const: 0x1908
+  __AUTH_CONST.__const: 0x1948
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__auth_got: 0xf70
+  __AUTH_CONST.__auth_got: 0xf88
   __AUTH.__objc_data: 0x0
   __DATA.__objc_protorefs: 0x90
-  __DATA.__objc_classrefs: 0x398
+  __DATA.__objc_classrefs: 0x378
   __DATA.__objc_superrefs: 0xd0
-  __DATA.__objc_ivar: 0x35c
+  __DATA.__objc_ivar: 0x358
   __DATA.__objc_data: 0xa0
-  __DATA.__data: 0x2628
-  __DATA.__bss: 0x9760
+  __DATA.__data: 0x25c8
+  __DATA.__bss: 0x9750
   __DATA.__common: 0x1e8
-  __DATA_DIRTY.__const: 0x2208
+  __DATA_DIRTY.__const: 0x2248
   __DATA_DIRTY.__objc_const: 0xff8
   __DATA_DIRTY.__objc_data: 0x1518
   __DATA_DIRTY.__data: 0xba0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: BD49F6A7-414B-3FB9-AF3F-2BDB930CF4A9
-  Functions: 3421
-  Symbols:   3902
-  CStrings:  2132
+  UUID: 537FD00F-AD5E-3131-8117-EEC21F6DAF93
+  Functions: 3416
+  Symbols:   3875
+  CStrings:  2121
 
Symbols:
+ +[ASCPublicKeyCredentialDescriptor magicCredentialID]
+ -[ASAgentAutoFillListener getIsPasskeyAssertionRequestRunningForWebFrameIdentifier:orApplicationIdentifier:completionHandler:]
+ -[ASCAgent getCanCurrentProcessAccessPasskeysForRelyingParty:withCompletionHandler:].cold.1
+ -[ASCCredentialRequestContext applyMagicCredentialIDIfNecessary]
+ -[ASCPlatformPublicKeyCredentialAssertion isExternal]
+ -[ASCPlatformPublicKeyCredentialAssertion setIsExternal:]
+ -[ASCPublicKeyCredentialAssertionOptions setAllowedCredentials:]
+ GCC_except_table124
+ GCC_except_table127
+ _OBJC_CLASS_$_WBSKeychainSyncingMonitor
+ _OBJC_IVAR_$_ASCAgent._internalSemaphore
+ _OBJC_IVAR_$_ASCPlatformPublicKeyCredentialAssertion._isExternal
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
+ ___32-[ASCAgent cancelCurrentRequest]_block_invoke
+ ___32-[ASCAgent cancelCurrentRequest]_block_invoke.96
+ ___32-[ASCAgent cancelCurrentRequest]_block_invoke.99
+ ___32-[ASCAgent cancelCurrentRequest]_block_invoke.cold.1
+ ___52-[ASCAgent _credentialRequestedForCABLELoginChoice:]_block_invoke.279
+ ___52-[ASCAgent _credentialRequestedForCABLELoginChoice:]_block_invoke.282
+ ___52-[ASCAgent _credentialRequestedForCABLELoginChoice:]_block_invoke.285
+ ___56-[ASCAgent _authorizationCompletedWithCredential:error:]_block_invoke.307
+ ___69-[ASCAgent _configureAppleIDCredentialWithContext:completionHandler:]_block_invoke.153
+ ___69-[ASCAgent _configureAppleIDCredentialWithContext:completionHandler:]_block_invoke.153.cold.1
+ ___69-[ASCAgent _configureAppleIDCredentialWithContext:completionHandler:]_block_invoke.158
+ ___69-[ASCAgent openCABLEURL:fromSourceApplication:withCompletionHandler:]_block_invoke.160
+ ___69-[ASCAgent openCABLEURL:fromSourceApplication:withCompletionHandler:]_block_invoke.160.cold.1
+ ___69-[ASCAgent openCABLEURL:fromSourceApplication:withCompletionHandler:]_block_invoke.169
+ ___69-[ASCAgent openCABLEURL:fromSourceApplication:withCompletionHandler:]_block_invoke.173
+ ___72-[ASCAgent _implicitlySelectAssertionLoginChoiceFromChoices:forContext:]_block_invoke.85
+ ___72-[ASCAgent _implicitlySelectAssertionLoginChoiceFromChoices:forContext:]_block_invoke.85.cold.1
+ ___72-[ASCAgent _implicitlySelectAssertionLoginChoiceFromChoices:forContext:]_block_invoke.86
+ ___72-[ASCAgent _implicitlySelectAssertionLoginChoiceFromChoices:forContext:]_block_invoke.86.cold.1
+ ___72-[ASCAgent _implicitlySelectAssertionLoginChoiceFromChoices:forContext:]_block_invoke.89
+ ___72-[ASCAgent _implicitlySelectAssertionLoginChoiceFromChoices:forContext:]_block_invoke.89.cold.1
+ ___72-[ASCAgent _implicitlySelectAssertionLoginChoiceFromChoices:forContext:]_block_invoke.93
+ ___72-[ASCAgent _implicitlySelectAssertionLoginChoiceFromChoices:forContext:]_block_invoke.93.cold.1
+ ___73-[ASCAgent performAuthorizationRequestsForContext:withCompletionHandler:]_block_invoke.54.cold.1
+ ___73-[ASCAgent performAuthorizationRequestsForContext:withCompletionHandler:]_block_invoke.55
+ ___73-[ASCAgent performAuthorizationRequestsForContext:withCompletionHandler:]_block_invoke.59
+ ___73-[ASCAgent performAuthorizationRequestsForContext:withCompletionHandler:]_block_invoke.62
+ ___73-[ASCAgent performAuthorizationRequestsForContext:withCompletionHandler:]_block_invoke_2.63
+ ___73-[ASCAgent performAuthorizationRequestsForContext:withCompletionHandler:]_block_invoke_2.63.cold.1
+ ___74-[ASCAgent _isClientWithApplicationIdentifier:associatedWithRelyingParty:]_block_invoke.218
+ ___79-[ASCAgent performSilentAuthorizationRequestsForContext:withCompletionHandler:]_block_invoke.67
+ ___79-[ASCAgent performSilentAuthorizationRequestsForContext:withCompletionHandler:]_block_invoke.72
+ ___79-[ASCAgent performSilentAuthorizationRequestsForContext:withCompletionHandler:]_block_invoke.72.cold.1
+ ___79-[ASCAgent performSilentAuthorizationRequestsForContext:withCompletionHandler:]_block_invoke_2.71
+ ___79-[ASCAgent performSilentAuthorizationRequestsForContext:withCompletionHandler:]_block_invoke_2.71.cold.1
+ ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke.291
+ ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke.291.cold.1
+ ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke.292
+ ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke.295
+ ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke.295.cold.1
+ ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke.296
+ ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke.297
+ ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke.301
+ ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke.301.cold.1
+ ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke_2.298
+ ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke_2.298.cold.1
+ ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.233
+ ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.233.cold.1
+ ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.237
+ ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.237.cold.1
+ ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.243
+ ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.243.cold.1
+ ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.247
+ ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.250
+ ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.250.cold.1
+ ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.256
+ ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.259
+ ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.259.cold.1
+ ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.268
+ ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.268.cold.1
+ ___96-[ASCAgent _prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke.108
+ ___96-[ASCAgent _prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke.108.cold.1
+ ___96-[ASCAgent _prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke.115
+ ___96-[ASCAgent _prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke.118
+ ___96-[ASCAgent _prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke.118.cold.1
+ ___96-[ASCAgent _prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke.121
+ ___96-[ASCAgent _prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke.128
+ ___block_descriptor_56_e8_32s40s48bs_e45_v24?0"<ASCCredentialProtocol>"8"NSError"16ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e49_v24?0"ASCCredentialRequestContext"8"NSError"16ls32l8s40l8s56l8s48l8
+ ___block_literal_global.110
+ ___block_literal_global.117
+ ___block_literal_global.120
+ ___block_literal_global.127
+ ___block_literal_global.130
+ ___block_literal_global.152
+ ___block_literal_global.155
+ ___block_literal_global.162
+ ___block_literal_global.175
+ ___block_literal_global.179
+ ___block_literal_global.200
+ ___block_literal_global.221
+ ___block_literal_global.223
+ ___block_literal_global.239
+ ___block_literal_global.249
+ ___block_literal_global.252
+ ___block_literal_global.273
+ ___block_literal_global.276
+ ___block_literal_global.278
+ ___block_literal_global.281
+ ___block_literal_global.284
+ ___block_literal_global.287
+ ___block_literal_global.294
+ ___block_literal_global.300
+ ___block_literal_global.309
+ ___block_literal_global.313
+ ___block_literal_global.516
+ ___block_literal_global.57
+ ___block_literal_global.61
+ ___block_literal_global.74
+ ___block_literal_global.88
+ ___block_literal_global.95
+ _dispatch_semaphore_create
+ _dispatch_semaphore_signal
+ _dispatch_semaphore_wait
+ _dispatch_time
+ _objc_msgSend$applyMagicCredentialIDIfNecessary
+ _objc_msgSend$canKeychainSyncBeEnabled
+ _objc_msgSend$completeAssertionWithExternalPasskeyForUUID:usingCredential:
+ _objc_msgSend$getIsPasskeyAssertionRequestRunningForWebFrameIdentifier:orApplicationIdentifier:completionHandler:
+ _objc_msgSend$initWithBase64EncodedString:options:
+ _objc_msgSend$magicCredentialID
+ _objc_msgSend$setAllowedCredentials:
+ _objc_msgSend$setIsExternal:
+ _objc_msgSend$sharedMonitor
- -[ASFeatureManager _keychainSyncingStatusMayHaveChanged]
- -[ASFeatureManager _updateAccountOnInternalQueue:]
- -[ASFeatureManager _updateKeychainClique]
- -[ASFeatureManager accountCredentialChanged:]
- -[ASFeatureManager accountWasAdded:]
- -[ASFeatureManager accountWasModified:]
- -[ASFeatureManager accountWasRemoved:]
- -[ASFeatureManager canKeychainSyncBeEnabled]
- -[ASFeatureManager hasPrimaryAppleAccount]
- -[ASFeatureManager isKeychainSyncEnabled]
- -[ASFeatureManager isKeychainSyncEnabled].cold.1
- GCC_except_table117
- GCC_except_table120
- GCC_except_table4
- _AAAccountClassPrimary
- _ACAccountTypeIdentifierAppleAccount
- _ASKeychainSyncStatusMayHaveChangedNotification
- _MCFeatureCloudKeychainSyncAllowed
- _OBJC_CLASS_$_ACMonitoredAccountStore
- _OBJC_CLASS_$_MCProfileConnection
- _OBJC_CLASS_$_NSNotificationCenter
- _OBJC_CLASS_$_OTClique
- _OBJC_CLASS_$_OTConfigurationContext
- _OBJC_IVAR_$_ASFeatureManager._accountStore
- _OBJC_IVAR_$_ASFeatureManager._keychainClique
- _OBJC_IVAR_$_ASFeatureManager._primaryAppleAccountAltDSID
- _OTDefaultContext
- _WBS_LOG_CHANNEL_PREFIXKeychain
- _WBS_LOG_CHANNEL_PREFIXKeychain.log
- _WBS_LOG_CHANNEL_PREFIXKeychain.onceToken
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_ACMonitoredAccountStoreDelegateProtocol
- __OBJC_$_PROTOCOL_METHOD_TYPES_ACMonitoredAccountStoreDelegateProtocol
- __OBJC_$_PROTOCOL_REFS_ACMonitoredAccountStoreDelegateProtocol
- __OBJC_CLASS_PROTOCOLS_$_ASFeatureManager
- __OBJC_LABEL_PROTOCOL_$_ACMonitoredAccountStoreDelegateProtocol
- __OBJC_PROTOCOL_$_ACMonitoredAccountStoreDelegateProtocol
- ___24-[ASFeatureManager init]_block_invoke
- ___36-[ASFeatureManager accountWasAdded:]_block_invoke
- ___38-[ASFeatureManager accountWasRemoved:]_block_invoke
- ___39-[ASFeatureManager accountWasModified:]_block_invoke
- ___41-[ASFeatureManager isKeychainSyncEnabled]_block_invoke
- ___45-[ASFeatureManager accountCredentialChanged:]_block_invoke
- ___52-[ASCAgent _credentialRequestedForCABLELoginChoice:]_block_invoke.259
- ___52-[ASCAgent _credentialRequestedForCABLELoginChoice:]_block_invoke.262
- ___52-[ASCAgent _credentialRequestedForCABLELoginChoice:]_block_invoke.265
- ___56-[ASCAgent _authorizationCompletedWithCredential:error:]_block_invoke.287
- ___56-[ASFeatureManager _keychainSyncingStatusMayHaveChanged]_block_invoke
- ___69-[ASCAgent _configureAppleIDCredentialWithContext:completionHandler:]_block_invoke.135
- ___69-[ASCAgent _configureAppleIDCredentialWithContext:completionHandler:]_block_invoke.135.cold.1
- ___69-[ASCAgent _configureAppleIDCredentialWithContext:completionHandler:]_block_invoke.140
- ___69-[ASCAgent openCABLEURL:fromSourceApplication:withCompletionHandler:]_block_invoke.142
- ___69-[ASCAgent openCABLEURL:fromSourceApplication:withCompletionHandler:]_block_invoke.142.cold.1
- ___69-[ASCAgent openCABLEURL:fromSourceApplication:withCompletionHandler:]_block_invoke.151
- ___69-[ASCAgent openCABLEURL:fromSourceApplication:withCompletionHandler:]_block_invoke.155
- ___72-[ASCAgent _implicitlySelectAssertionLoginChoiceFromChoices:forContext:]_block_invoke.74
- ___72-[ASCAgent _implicitlySelectAssertionLoginChoiceFromChoices:forContext:]_block_invoke.74.cold.1
- ___72-[ASCAgent _implicitlySelectAssertionLoginChoiceFromChoices:forContext:]_block_invoke.75
- ___72-[ASCAgent _implicitlySelectAssertionLoginChoiceFromChoices:forContext:]_block_invoke.75.cold.1
- ___72-[ASCAgent _implicitlySelectAssertionLoginChoiceFromChoices:forContext:]_block_invoke.78
- ___72-[ASCAgent _implicitlySelectAssertionLoginChoiceFromChoices:forContext:]_block_invoke.78.cold.1
- ___72-[ASCAgent _implicitlySelectAssertionLoginChoiceFromChoices:forContext:]_block_invoke.82
- ___72-[ASCAgent _implicitlySelectAssertionLoginChoiceFromChoices:forContext:]_block_invoke.82.cold.1
- ___73-[ASCAgent performAuthorizationRequestsForContext:withCompletionHandler:]_block_invoke_2.cold.1
- ___74-[ASCAgent _isClientWithApplicationIdentifier:associatedWithRelyingParty:]_block_invoke.198
- ___79-[ASCAgent performSilentAuthorizationRequestsForContext:withCompletionHandler:]_block_invoke.58
- ___79-[ASCAgent performSilentAuthorizationRequestsForContext:withCompletionHandler:]_block_invoke.63
- ___79-[ASCAgent performSilentAuthorizationRequestsForContext:withCompletionHandler:]_block_invoke.63.cold.1
- ___79-[ASCAgent performSilentAuthorizationRequestsForContext:withCompletionHandler:]_block_invoke_2.62
- ___79-[ASCAgent performSilentAuthorizationRequestsForContext:withCompletionHandler:]_block_invoke_2.62.cold.1
- ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke.271
- ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke.271.cold.1
- ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke.272
- ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke.275
- ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke.275.cold.1
- ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke.276
- ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke.277
- ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke.281
- ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke.281.cold.1
- ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke_2.278
- ___81-[ASCAgent authorizationPresenter:startCABLEAuthenticationWithCompletionHandler:]_block_invoke_2.278.cold.1
- ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.207
- ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.210
- ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.213
- ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.213.cold.1
- ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.217
- ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.217.cold.1
- ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.223
- ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.223.cold.1
- ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.230.cold.1
- ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.236
- ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.239
- ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.239.cold.1
- ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.248
- ___87-[ASCAgent _isClientWithApplicationIdentifier:properlyEntitledForRequestContext:error:]_block_invoke.248.cold.1
- ___96-[ASCAgent _prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke.102
- ___96-[ASCAgent _prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke.109
- ___96-[ASCAgent _prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke.89
- ___96-[ASCAgent _prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke.89.cold.1
- ___96-[ASCAgent _prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke.96
- ___96-[ASCAgent _prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke.99
- ___96-[ASCAgent _prepareForAuthorizationRequestsForContext:clientConnection:withPresentationHandler:]_block_invoke.99.cold.1
- ___WBS_LOG_CHANNEL_PREFIXKeychain_block_invoke
- ___block_descriptor_56_e8_32s40r48r_e5_v8?0lr40l8s32l8r48l8
- ___block_descriptor_56_e8_32s40s48bs_e49_v24?0"ASCCredentialRequestContext"8"NSError"16ls32l8s48l8s40l8
- ___block_literal_global.108
- ___block_literal_global.111
- ___block_literal_global.134
- ___block_literal_global.137
- ___block_literal_global.144
- ___block_literal_global.157
- ___block_literal_global.160
- ___block_literal_global.181
- ___block_literal_global.184
- ___block_literal_global.201
- ___block_literal_global.209
- ___block_literal_global.212
- ___block_literal_global.219
- ___block_literal_global.238
- ___block_literal_global.241
- ___block_literal_global.253
- ___block_literal_global.256
- ___block_literal_global.264
- ___block_literal_global.267
- ___block_literal_global.269
- ___block_literal_global.274
- ___block_literal_global.280
- ___block_literal_global.285
- ___block_literal_global.293
- ___block_literal_global.35
- ___block_literal_global.494
- ___block_literal_global.7
- ___block_literal_global.77
- ___block_literal_global.80
- ___block_literal_global.85
- _dispatch_sync
- _objc_msgSend$_keychainSyncingStatusMayHaveChanged
- _objc_msgSend$_updateAccountOnInternalQueue:
- _objc_msgSend$_updateKeychainClique
- _objc_msgSend$aa_accountClass
- _objc_msgSend$aa_altDSID
- _objc_msgSend$aa_primaryAppleAccount
- _objc_msgSend$boolRestrictionForFeature:
- _objc_msgSend$defaultCenter
- _objc_msgSend$fetchUserControllableViewsSyncingEnabled:
- _objc_msgSend$initWithAccountTypes:delegate:
- _objc_msgSend$initWithContextData:
- _objc_msgSend$postNotificationName:object:
- _objc_msgSend$registerSynchronouslyWithError:
- _objc_msgSend$setAltDSID:
- _objc_msgSend$setContext:
- _objc_msgSend$sharedConnection
CStrings:
+ "\x01\x15\x1d\x12"
+ "\x18"
+ "-[ASCAgent cancelCurrentRequest]_block_invoke"
+ "-[ASCAgent performAuthorizationRequestsForContext:withCompletionHandler:]_block_invoke"
+ "-[ASCAgent performAuthorizationRequestsForContext:withCompletionHandler:]_block_invoke_2"
+ "@\"NSObject<OS_dispatch_semaphore>\""
+ "Acquired lock for %s"
+ "Failed to acquire lock for %s"
+ "Passkeys are unavailable because iCloud Keychain has been disabled by a configuration profile."
+ "Released lock for %s"
+ "T@\"NSArray\",C,N,V_allowedCredentials"
+ "T@\"NSData\",R,N"
+ "TB,N,V_isExternal"
+ "Updating request."
+ "_internalSemaphore"
+ "_isExternal"
+ "applyMagicCredentialIDIfNecessary"
+ "completeAssertionWithExternalPasskeyForUUID:usingCredential:"
+ "getIsPasskeyAssertionRequestRunningForWebFrameIdentifier:orApplicationIdentifier:completionHandler:"
+ "magicCredentialID"
+ "setAllowedCredentials:"
+ "setIsExternal:"
+ "sharedMonitor"
+ "v40@0:8@\"WBSGlobalFrameIdentifier\"16@\"NSString\"24@?<v@?B>32"
- "\x01\x15\x1c\x12"
- "\x05"
- "@\"ACMonitoredAccountStore\""
- "@\"OTClique\""
- "ACMonitoredAccountStoreDelegateProtocol"
- "Failed to read keychain sync status with error: %{public}@"
- "Keychain"
- "T@\"NSArray\",R,C,N,V_allowedCredentials"
- "TB,R,N,GcanKeychainSyncBeEnabled"
- "TB,R,N,GisKeychainSyncEnabled"
- "_accountStore"
- "_keychainClique"
- "_keychainSyncingStatusMayHaveChanged"
- "_primaryAppleAccountAltDSID"
- "_updateAccountOnInternalQueue:"
- "_updateKeychainClique"
- "aa_accountClass"
- "accountCredentialChanged:"
- "accountWasAdded:"
- "accountWasModified:"
- "accountWasRemoved:"
- "boolRestrictionForFeature:"
- "defaultCenter"
- "fetchUserControllableViewsSyncingEnabled:"
- "hasPrimaryAppleAccount"
- "initWithAccountTypes:delegate:"
- "initWithContextData:"
- "keychainSyncEnabled"
- "keychainSyncStatusMayHaveChanged"
- "postNotificationName:object:"
- "registerSynchronouslyWithError:"
- "setAltDSID:"
- "setContext:"
- "sharedConnection"
- "v24@0:8@\"ACAccount\"16"

```
