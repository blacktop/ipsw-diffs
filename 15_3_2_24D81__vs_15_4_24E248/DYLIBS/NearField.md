## NearField

> `/System/Library/PrivateFrameworks/NearField.framework/Versions/A/NearField`

```diff

-353.3.0.0.0
-  __TEXT.__text: 0x8bf38
+354.27.0.0.0
+  __TEXT.__text: 0x9422c
   __TEXT.__auth_stubs: 0x4e0
-  __TEXT.__objc_methlist: 0x4e18
+  __TEXT.__objc_methlist: 0x6100
   __TEXT.__const: 0x237
-  __TEXT.__cstring: 0x5936
-  __TEXT.__oslogstring: 0x4789
+  __TEXT.__cstring: 0x5c48
+  __TEXT.__oslogstring: 0x49b5
   __TEXT.__dlopen_cstrs: 0xa8
-  __TEXT.__unwind_info: 0x16f0
-  __TEXT.__objc_classname: 0xc2d
-  __TEXT.__objc_methname: 0xc369
-  __TEXT.__objc_methtype: 0x2f2d
-  __TEXT.__objc_stubs: 0x6ae0
-  __DATA_CONST.__got: 0x3b8
-  __DATA_CONST.__const: 0x990
-  __DATA_CONST.__objc_classlist: 0x2e0
+  __TEXT.__unwind_info: 0x1780
+  __TEXT.__objc_classname: 0xc9c
+  __TEXT.__objc_methname: 0xc5d9
+  __TEXT.__objc_methtype: 0x3143
+  __TEXT.__objc_stubs: 0x6ca0
+  __DATA_CONST.__got: 0x3d8
+  __DATA_CONST.__const: 0xe20
+  __DATA_CONST.__objc_classlist: 0x2e8
   __DATA_CONST.__objc_catlist: 0x30
-  __DATA_CONST.__objc_protolist: 0x1a0
+  __DATA_CONST.__objc_protolist: 0x1c0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2c90
-  __DATA_CONST.__objc_protorefs: 0x108
-  __DATA_CONST.__objc_superrefs: 0x1e8
+  __DATA_CONST.__objc_selrefs: 0x2dd0
+  __DATA_CONST.__objc_protorefs: 0x128
+  __DATA_CONST.__objc_superrefs: 0x1e0
   __DATA_CONST.__objc_arraydata: 0x70
   __AUTH_CONST.__auth_got: 0x278
-  __AUTH_CONST.__const: 0x19e0
-  __AUTH_CONST.__cfstring: 0x3ba0
-  __AUTH_CONST.__objc_const: 0xc4b8
-  __AUTH_CONST.__objc_intobj: 0x4b0
+  __AUTH_CONST.__const: 0x1b90
+  __AUTH_CONST.__cfstring: 0x3ce0
+  __AUTH_CONST.__objc_const: 0xa488
+  __AUTH_CONST.__objc_intobj: 0x648
   __AUTH_CONST.__objc_dictobj: 0xc8
-  __AUTH.__objc_data: 0x1040
+  __AUTH.__objc_data: 0x1090
   __DATA.__objc_ivar: 0x658
-  __DATA.__data: 0x1380
+  __DATA.__data: 0x1500
   __DATA.__bss: 0xa0
   __DATA_DIRTY.__objc_data: 0xc80
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libnfshared.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 65FA8A53-8017-3592-986D-4B665A08CF8E
-  Functions: 2249
-  Symbols:   4784
-  CStrings:  4266
+  UUID: 28605B7E-BFE3-3CB5-918F-6E259A5019F3
+  Functions: 2291
+  Symbols:   4881
+  CStrings:  4340
 
Symbols:
+ +[NFSingleUserSessionInterface interface]
+ -[NFApplet moduleIdentifierAsData]
+ -[NFAssertion dealloc]
+ -[NFAssertion deassert]
+ -[NFAssertion isReleased]
+ -[NFAssertion setIsReleased:]
+ -[NFFieldNotificationECP2_0 _initCategoryWithType:subType:]
+ -[NFHardwareManager queueAssertion:completion:]
+ -[NFHardwareManager queueAssertionWithParams:completion:]
+ -[NFHardwareManager releaseAssertion:completion:]
+ -[NFHardwareManager requestAssertionWithParams:error:]
+ -[NFHardwareManager startSingleUserSession:]
+ -[NFSecureElementManagerSession initWithCallbackQueue:]
+ -[NFSecureElementManagerSession transceive:forSEID:toOS:secureZeroOut:error:]
+ -[NFSecureElementManagerSession transceiveMultiple:forSEID:toOS:secureZeroOut:error:]
+ -[NFSession initWithCallbackQueue:]
+ -[NFSession internalInit]
+ -[NFSession requestBugCapture:subtype:context:]
+ -[NFSingleUserSession checkUserBlessing:hasCards:]
+ -[NFSingleUserSession hasCard:]
+ -[NFSingleUserSession setBlessedUser:keybagUUID:withAuthorization:]
+ -[NFSingleUserSession setBlessedUser:withAuthorization:]
+ OBJC_IVAR_$_NFAssertion._isReleased
+ _OBJC_CLASS_$_NFSingleUserSession
+ _OBJC_CLASS_$_NFSingleUserSessionInterface
+ _OBJC_CLASS_$_NSUUID
+ _OBJC_METACLASS_$_NFSingleUserSession
+ _OBJC_METACLASS_$_NFSingleUserSessionInterface
+ __112-[NFReaderSession felicaStateForSystemCode:withRequestService:withBlockReadList:performSearchServiceCode:error:]_block_invoke.144
+ __28-[NFHardwareManager hasCard]_block_invoke.142
+ __29-[NFHardwareManager preWarm:]_block_invoke.268
+ __29-[NFSession _endProxySession]_block_invoke.36
+ __30-[NFSession prioritizeSession]_block_invoke.42
+ __31-[NFHardwareManager rfSettings]_block_invoke.86
+ __31-[NFHardwareManager stateInfo:]_block_invoke.80
+ __31-[NFSession activateWithToken:]_block_invoke.47
+ __31-[NFSingleUserSession hasCard:]_block_invoke.41
+ __32-[NFHardwareManager blessedUser]_block_invoke.135
+ __32-[NFHardwareManager toggleGPIO:]_block_invoke.172
+ __32-[NFXPCServiceClient connection]_block_invoke.7
+ __32-[NFXPCServiceClient connection]_block_invoke_2.8
+ __33-[NFSession setSessionTimeLimit:]_block_invoke.16
+ __34-[NFHardwareManager pushSignedRF:]_block_invoke.98
+ __34-[NFHardwareManager setChipscope:]_block_invoke.305
+ __34-[NFHardwareManager triggerCrash:]_block_invoke.170
+ __35-[NFReaderSession ndefWrite:error:]_block_invoke.128
+ __36-[NFHardwareManager disableHeadless]_block_invoke.119
+ __36-[NFHardwareManager dumpLPMDebugLog]_block_invoke.127
+ __36-[NFHardwareManager getTemperature:]_block_invoke.74
+ __36-[NFReaderSession connectTag:error:]_block_invoke.115
+ __36-[NFReaderSession performVAS:error:]_block_invoke.153
+ __36-[NFReaderSession transceive:error:]_block_invoke.134
+ __37-[NFHardwareManager getUniqueFDRKey:]_block_invoke.94
+ __37-[NFHardwareManager hostEmulationLog]_block_invoke.198
+ __37-[NFHardwareManager setAntiRelayRID:]_block_invoke.89
+ __37-[NFReaderSession ndefReadWithError:]_block_invoke.129
+ __38-[NFHardwareManager getPowerCounters:]_block_invoke.120
+ __38-[NFHardwareManager releaseAssertion:]_block_invoke.167
+ __38-[NFHardwareManager setAuthorization:]_block_invoke.139
+ __39-[NFHardwareManager enableLPEMFeature:]_block_invoke.113
+ __39-[NFHardwareManager getDieIDWithError:]_block_invoke.90
+ __39-[NFHardwareManager getLPEMFTALogging:]_block_invoke.306
+ __39-[NFReaderSession setECPPayload:error:]_block_invoke.106
+ __39-[NFSession createSessionHandoffToken:]_block_invoke.45
+ __40-[NFContactlessSession didStartSession:]_block_invoke.19
+ __40-[NFContactlessSession didStartSession:]_block_invoke.22
+ __40-[NFHardwareManager disableLPEMFeature:]_block_invoke.114
+ __40-[NFHardwareManager expressModesEnabled]_block_invoke.101
+ __40-[NFHardwareManager triggerDelayedWake:]_block_invoke.169
+ __40-[NFReaderSession felicaStateWithError:]_block_invoke.138
+ __40-[NFReaderSession stopPollingWithError:]_block_invoke.111
+ __40-[NFReaderSession updateUIAlertMessage:]_block_invoke.151
+ __40-[NFRemoteAdminManager _connectIfNeeded]_block_invoke.74
+ __40-[NFRemoteAdminManager registrationInfo]_block_invoke.91
+ __41-[NFReaderSession startPollingWithError:]_block_invoke.107
+ __41-[NFRemoteAdminManager getAPNPublicToken]_block_invoke.119
+ __42-[NFContactlessSession stopCardEmulation:]_block_invoke.63
+ __42-[NFHardwareManager getRadioEnabledState:]_block_invoke.71
+ __42-[NFReaderSession checkPresenceWithError:]_block_invoke.122
+ __42-[NFRemoteAdminManager primaryRegionTopic]_block_invoke.95
+ __43-[NFContactlessSession startCardEmulation:]_block_invoke.60
+ __43-[NFHardwareManager getFlashWriteCounters:]_block_invoke.124
+ __43-[NFHardwareManager setFieldDetectEnabled:]_block_invoke.146
+ __43-[NFReaderSession formatNdefWithKey:error:]_block_invoke.126
+ __43-[NFReaderSession restartPollingWithError:]_block_invoke.112
+ __43-[NFReaderSession setPollingProfile:error:]_block_invoke.158
+ __43-[NFReaderSession skipMifareClassification]_block_invoke.152
+ __43-[NFRemoteAdminManager cancelCardIngestion]_block_invoke.118
+ __44-[NFHardwareManager enableHeadlessTestMode:]_block_invoke.171
+ __44-[NFHardwareManager expressModeControlState]_block_invoke.105
+ __44-[NFHardwareManager requestAssertion:error:]_block_invoke.151
+ __44-[NFHardwareManager setRadioEnabledSetting:]_block_invoke.73
+ __45-[NFECommercePaymentSession didStartSession:]_block_invoke.19
+ __45-[NFECommercePaymentSession didStartSession:]_block_invoke.22
+ __45-[NFHardwareManager controllerInfoWithError:]_block_invoke.82
+ __45-[NFHardwareManager secureElementsWithError:]_block_invoke.190
+ __45-[NFReaderSession startLPCDPollingWithError:]_block_invoke.108
+ __45-[NFRemoteAdminManager getSELDInfoForBroker:]_block_invoke.123
+ __45-[NFRemoteAdminManager nextRequestForServer:]_block_invoke.99
+ __45-[NFSecureElementManagerSession _appletsById]_block_invoke.30
+ __46-[NFContactlessSession setActiveApplet:error:]_block_invoke.58
+ __46-[NFLoyaltyAndPaymentSession didStartSession:]_block_invoke.19
+ __46-[NFLoyaltyAndPaymentSession didStartSession:]_block_invoke.22
+ __46-[NFReaderSession felicaRequestService:error:]_block_invoke.145
+ __46-[NFRemoteAdminManager queueServerConnection:]_block_invoke.101
+ __47-[NFContactlessPaymentSession didStartSession:]_block_invoke.19
+ __47-[NFContactlessPaymentSession didStartSession:]_block_invoke.22
+ __47-[NFHardwareManager queueAssertion:completion:]_block_invoke.164
+ __47-[NFLPEMConfigSession enableLPEMFeature:error:]_block_invoke.44
+ __47-[NFLoyaltyAndPaymentSession startExpressMode:]_block_invoke.95
+ __47-[NFSecureElementManagerSession getOSUpdateLog]_block_invoke.185
+ __48-[NFHardwareManager checkUserBlessing:hasCards:]_block_invoke.128
+ __48-[NFLPEMConfigSession disableLPEMFeature:error:]_block_invoke.39
+ __48-[NFLPEMConfigSession getLPEMFeaturesWithError:]_block_invoke.50
+ __48-[NFLoyaltyAndPaymentSession stopCardEmulation:]_block_invoke.86
+ __48-[NFReaderSession startPollingWithConfig:error:]_block_invoke.110
+ __49-[NFContactlessPaymentSession stopCardEmulation:]_block_invoke.88
+ __49-[NFHardwareManager expressPassConfigsWithError:]_block_invoke.106
+ __49-[NFHardwareManager releaseAssertion:completion:]_block_invoke.168
+ __50-[NFHardwareManager configureHeadlessFactoryMode:]_block_invoke.112
+ __50-[NFSingleUserSession checkUserBlessing:hasCards:]_block_invoke.28
+ __51-[NFReaderSession didDetectTags:connectedTagIndex:]_block_invoke.90
+ __51-[NFReaderSession startPollingForTechnology:error:]_block_invoke.109
+ __52-[NFHardwareManager refreshSecureElementsWithError:]_block_invoke.197
+ __52-[NFLPEMConfigSession getLPEMBluetoothLogWithError:]_block_invoke.56
+ __53-[NFConnectionHandoverReceiver _processRetryRequest:]_block_invoke.520
+ __54-[NFConnectionHandoverInitiator send:responseHandler:]_block_invoke.242
+ __54-[NFConnectionHandoverInitiator send:responseHandler:]_block_invoke.244
+ __54-[NFConnectionHandoverInitiator send:responseHandler:]_block_invoke.246
+ __54-[NFConnectionHandoverReceiver _emuAssertTimerExpired]_block_invoke.478
+ __54-[NFConnectionHandoverReceiver _emuAssertTimerExpired]_block_invoke.482
+ __54-[NFHardwareManager requestAssertionWithParams:error:]_block_invoke.163
+ __54-[NFLoyaltyAndPaymentSession _startHostCardEmulation:]_block_invoke.84
+ __54-[NFLoyaltyAndPaymentSession felicaAppletState:error:]_block_invoke.87
+ __54-[NFSecureElementManagerSession powerCycleSEID:error:]_block_invoke.184
+ __55-[NFContactlessPaymentSession felicaAppletState:error:]_block_invoke.89
+ __55-[NFLoyaltyAndPaymentSession transitAppletState:error:]_block_invoke.91
+ __56-[NFContactlessPaymentSession transitAppletState:error:]_block_invoke.93
+ __56-[NFHardwareManager updateHWSupportWithXPC:waitForInit:]_block_invoke.63
+ __56-[NFHardwareManager updateHWSupportWithXPC:waitForInit:]_block_invoke.64
+ __56-[NFHardwareManager updateHWSupportWithXPC:waitForInit:]_block_invoke.69
+ __56-[NFReaderSession checkNdefSupportsRead:andWrite:error:]_block_invoke.118
+ __56-[NFRemoteAdminManager queueServerConnectionForApplets:]_block_invoke.102
+ __56-[NFSecureElementManagerSession deleteAllApplets:error:]_block_invoke.70
+ __56-[NFSecureElementManagerSession getAndResetLPEMCounter:]_block_invoke.144
+ __57-[NFHardwareManager _startFieldDetectSession:completion:]_block_invoke.221
+ __57-[NFHardwareManager _startFieldDetectSession:completion:]_block_invoke.222
+ __57-[NFHardwareManager checkExpressPassCompatibility:error:]_block_invoke.107
+ __57-[NFHardwareManager queueAssertionWithParams:completion:]_block_invoke.165
+ __57-[NFHardwareManager startSinglePollExpressModeAssertion:]_block_invoke.125
+ __57-[NFLPEMConfigSession configureHardwareForLPEMWithError:]_block_invoke.34
+ __57-[NFReaderSession(Private) runScript:parameters:results:]_block_invoke.289
+ __57-[NFRemoteAdminManager deleteAllAppletsAndCleanupWithTSM]_block_invoke.126
+ __57-[NFRemoteAdminManager ingestCard:withCompletionHandler:]_block_invoke.112
+ __57-[NFSecureElementManagerSession expressModeControlState:]_block_invoke.152
+ __57-[NFSecureElementManagerSession felicaAppletState:error:]_block_invoke.134
+ __58-[NFConnectionHandoverReceiver hceSession:didReceiveAPDU:]_block_invoke.534
+ __58-[NFHardwareManager releaseSinglePollExpressModeAssertion]_block_invoke.126
+ __58-[NFLoyaltyAndPaymentSession enablePlasticCardMode:error:]_block_invoke.94
+ __58-[NFReaderSession _disconnectTagWithCardRemoval:outError:]_block_invoke.117
+ __58-[NFSecureElementManagerSession dumpDomain:forSEID:error:]_block_invoke.183
+ __58-[NFSecureElementManagerSession transitAppletState:error:]_block_invoke.138
+ __59-[NFRemoteAdminManager deleteAllSPAppletsAndCleanupWithTSM]_block_invoke.128
+ __59-[NFSecureElementManagerSession signChallenge:certs:error:]_block_invoke.51
+ __60-[NFLPEMConfigSession getAndClearLPEMBluetoothLogWithError:]_block_invoke.64
+ __60-[NFReaderSession felicaRequestService:forSystemCode:error:]_block_invoke.149
+ __60-[NFSecureElementManagerSession getAttackLogPresence:error:]_block_invoke.179
+ __60-[NFSecureElementManagerSession refreshSecureElement:error:]_block_invoke.177
+ __61-[NFConnectionHandoverInitiator readerSession:didDetectTags:]_block_invoke.286
+ __61-[NFECommercePaymentSession validateEcommercePaymentRequest:]_block_invoke.30
+ __61-[NFHardwareManager cachedEmbeddedSecureElementSerialNumber:]_block_invoke.194
+ __61-[NFSecureElementManagerSession didExitRestrictedMode:error:]_block_invoke.159
+ __61-[NFSecureElementManagerSession setExpressModesControlState:]_block_invoke.90
+ __62-[NFSecureElementManagerSession expressModesEnabledWithError:]_block_invoke.148
+ __63-[NFConnectionHandoverInitiator _startWithCustomBroadcastData:]_block_invoke.206
+ __63-[NFConnectionHandoverInitiator _startWithCustomBroadcastData:]_block_invoke_2.207
+ __63-[NFRemoteAdminManager deleteAllWalletAppletsAndCleanupWithTSM]_block_invoke.127
+ __63-[NFRemoteAdminManager setRegistrationInfo:primaryRegionTopic:]_block_invoke.90
+ __63-[NFSecureElementManagerSession getExpressPassConfigWithError:]_block_invoke.113
+ __64-[NFLoyaltyAndPaymentSession setActivePaymentApplet:keys:error:]_block_invoke.81
+ __65-[NFHardwareManager actOnUserInitiatedSystemShutDown:completion:]_block_invoke.301
+ __65-[NFHardwareManager setBlessedUser:keybagUUID:withAuthorization:]_block_invoke.132
+ __66-[NFHardwareManager _synchronousQueueSessionWithRetry:queueBlock:]_block_invoke.203
+ __67-[NFECommercePaymentSession performECommercePayment:request:error:]_block_invoke.28
+ __67-[NFSecureElementManagerSession expressAppletIdentifiersWithError:]_block_invoke.153
+ __67-[NFSingleUserSession setBlessedUser:keybagUUID:withAuthorization:]_block_invoke.34
+ __68-[NFSecureElementManagerSession getSignedPlatformDataForSeid:error:]_block_invoke.61
+ __68-[NFSecureElementManagerSession performPeerPaymentEnrollment:error:]_block_invoke.154
+ __68-[NFSecureElementManagerSession runScript:parameters:outputResults:]_block_invoke.166
+ __68-[NFSecureElementManagerSession signChallenge:forAID:sigInfo:error:]_block_invoke.60
+ __69-[NFConnectionHandoverInitiator sendHandoverRequest:responseHandler:]_block_invoke.233
+ __69-[NFConnectionHandoverInitiator sendHandoverRequest:responseHandler:]_block_invoke.237
+ __71-[NFSecureElementManagerSession getCryptogram:challengeResponse:error:]_block_invoke.75
+ __71-[NFSecureElementManagerSession getServiceProviderDataForApplet:error:]_block_invoke.139
+ __72-[NFSecureElementManagerSession stateInformationWithRedirectInfo:error:]_block_invoke.49
+ __72-[NFSecureElementManagerSession validateSEPairings:outSEPairingVersion:]_block_invoke.71
+ __73-[NFConnectionHandoverReceiver _startWithAutoResume:customBroadcastData:]_block_invoke.454
+ __73-[NFConnectionHandoverReceiver _startWithAutoResume:customBroadcastData:]_block_invoke_2.455
+ __73-[NFContactlessPaymentSession startCardEmulationWithAuthorization:error:]_block_invoke.84
+ __73-[NFHardwareManager validateExpressPassCompatibilityWithConfig:outError:]_block_invoke.111
+ __73-[NFLoyaltyAndPaymentSession _startCardEmulationWithAuthorization:error:]_block_invoke.83
+ __74-[NFContactlessPaymentSession setActivePaymentApplet:authorization:error:]_block_invoke.82
+ __74-[NFRemoteAdminManager connectToServer:initialClientRequestInfo:callback:]_block_invoke.100
+ __75-[NFConnectionHandoverReceiver sendHandoverSelect:delay:completionHandler:]_block_invoke.492
+ __75-[NFConnectionHandoverReceiver sendHandoverSelect:delay:completionHandler:]_block_invoke.495
+ __75-[NFConnectionHandoverReceiver sendHandoverSelect:delay:completionHandler:]_block_invoke.497
+ __75-[NFConnectionHandoverReceiver sendHandoverSelect:delay:completionHandler:]_block_invoke_2.498
+ __75-[NFSecureElementManagerSession deleteApplets:queueServerConnection:error:]_block_invoke.63
+ __75-[NFSecureElementManagerSession setExpressPassConfig:restoreAuthorization:]_block_invoke.109
+ __75-[NFSecureElementManagerSession stateInformationWithoutFilteringWithError:]_block_invoke.50
+ __76-[NFSecureElementManagerSession restoreAuthorizarionForKeys:onApplet:error:]_block_invoke.127
+ __77-[NFSecureElementManagerSession disableAuthorizationForPasses:authorization:]_block_invoke.133
+ __77-[NFSecureElementManagerSession transceive:forSEID:toOS:secureZeroOut:error:]_block_invoke.162
+ __78-[NFHardwareManager startNdefTagSessionWithBluetoothLESecureOOBData:callback:]_block_invoke.278
+ __79-[NFConnectionHandoverInitiator readerSession:externalReaderFieldNotification:]_block_invoke.296
+ __79-[NFConnectionHandoverReceiver _processDisconnectWithPossibleDiscoveryRestart:]_block_invoke.524
+ __79-[NFSecureElementManagerSession restoreAuthorizationForAllAppletsExcept:error:]_block_invoke.120
+ __80-[NFSecureElementManagerSession signChallenge:useOSVersion:signatureInfo:error:]_block_invoke.53
+ __81-[NFContactlessPaymentSession startDeferredCardEmulationWithAuthorization:error:]_block_invoke.87
+ __81-[NFLoyaltyAndPaymentSession _startDeferredCardEmulationWithAuthorization:error:]_block_invoke.85
+ __82-[NFSecureElementManagerSession getAttackCounterLogForSEID:acknowledgeLogs:error:]_block_invoke.178
+ __85-[NFConnectionHandoverInitiator _processSelectRetry:originalRequest:responseHandler:]_block_invoke.230
+ __85-[NFSecureElementManagerSession transceiveMultiple:forSEID:toOS:secureZeroOut:error:]_block_invoke.164
+ __87-[NFHardwareManager getReaderProhibitTimerInfoSERmRunning:hostRmRunning:remainingInMs:]_block_invoke.78
+ __88-[NFSecureElementManagerSession getServiceProviderDataForApplet:publicKey:scheme:error:]_block_invoke.143
+ __91-[NFSecureElementManagerSession disableAuthorizationForApplets:andKey:authorization:error:]_block_invoke.132
+ __Block_byref_object_copy_.476
+ __Block_byref_object_dispose_.477
+ __OBJC_$_INSTANCE_METHODS_NFSingleUserSession
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NFLPEMConfigSessionInterface
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NFSingleUserSessionInterface
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NFLPEMConfigSessionInterface
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NFSingleUserSessionInterface
+ __OBJC_$_PROTOCOL_REFS_NFLPEMConfigSessionCallbacks
+ __OBJC_$_PROTOCOL_REFS_NFLPEMConfigSessionInterface
+ __OBJC_$_PROTOCOL_REFS_NFSingleUserSessionCallbacks
+ __OBJC_$_PROTOCOL_REFS_NFSingleUserSessionInterface
+ __OBJC_CLASS_RO_$_NFSingleUserSession
+ __OBJC_CLASS_RO_$_NFSingleUserSessionInterface
+ __OBJC_LABEL_PROTOCOL_$_NFLPEMConfigSessionCallbacks
+ __OBJC_LABEL_PROTOCOL_$_NFLPEMConfigSessionInterface
+ __OBJC_LABEL_PROTOCOL_$_NFSingleUserSessionCallbacks
+ __OBJC_LABEL_PROTOCOL_$_NFSingleUserSessionInterface
+ __OBJC_METACLASS_RO_$_NFSingleUserSession
+ __OBJC_METACLASS_RO_$_NFSingleUserSessionInterface
+ __OBJC_PROTOCOL_$_NFLPEMConfigSessionCallbacks
+ __OBJC_PROTOCOL_$_NFLPEMConfigSessionInterface
+ __OBJC_PROTOCOL_$_NFSingleUserSessionCallbacks
+ __OBJC_PROTOCOL_$_NFSingleUserSessionInterface
+ __OBJC_PROTOCOL_REFERENCE_$_NFLPEMConfigSessionCallbacks
+ __OBJC_PROTOCOL_REFERENCE_$_NFLPEMConfigSessionInterface
+ __OBJC_PROTOCOL_REFERENCE_$_NFSingleUserSessionCallbacks
+ __OBJC_PROTOCOL_REFERENCE_$_NFSingleUserSessionInterface
+ ___31-[NFSingleUserSession hasCard:]_block_invoke
+ ___44-[NFHardwareManager startLPEMConfigSession:]_block_invoke
+ ___44-[NFHardwareManager startLPEMConfigSession:]_block_invoke_2
+ ___44-[NFHardwareManager startSingleUserSession:]_block_invoke
+ ___44-[NFHardwareManager startSingleUserSession:]_block_invoke_2
+ ___47-[NFHardwareManager queueAssertion:completion:]_block_invoke
+ ___47-[NFLPEMConfigSession enableLPEMFeature:error:]_block_invoke
+ ___47-[NFSession remoteObjectProxyWithErrorHandler:]_block_invoke
+ ___48-[NFLPEMConfigSession disableLPEMFeature:error:]_block_invoke
+ ___48-[NFLPEMConfigSession getLPEMFeaturesWithError:]_block_invoke
+ ___49-[NFHardwareManager releaseAssertion:completion:]_block_invoke
+ ___50-[NFSingleUserSession checkUserBlessing:hasCards:]_block_invoke
+ ___52-[NFLPEMConfigSession getLPEMBluetoothLogWithError:]_block_invoke
+ ___54-[NFHardwareManager requestAssertionWithParams:error:]_block_invoke
+ ___55-[NFHardwareManager remoteObjectProxyWithErrorHandler:]_block_invoke
+ ___57-[NFHardwareManager queueAssertionWithParams:completion:]_block_invoke
+ ___57-[NFLPEMConfigSession configureHardwareForLPEMWithError:]_block_invoke
+ ___58-[NFRemoteAdminManager remoteObjectProxyWithErrorHandler:]_block_invoke
+ ___58-[NFSession synchronousRemoteObjectProxyWithErrorHandler:]_block_invoke
+ ___60-[NFLPEMConfigSession getAndClearLPEMBluetoothLogWithError:]_block_invoke
+ ___66-[NFHardwareManager synchronousRemoteObjectProxyWithErrorHandler:]_block_invoke
+ ___67-[NFSingleUserSession setBlessedUser:keybagUUID:withAuthorization:]_block_invoke
+ ___69-[NFRemoteAdminManager synchronousRemoteObjectProxyWithErrorHandler:]_block_invoke
+ ___77-[NFSecureElementManagerSession transceive:forSEID:toOS:secureZeroOut:error:]_block_invoke
+ ___85-[NFSecureElementManagerSession transceiveMultiple:forSEID:toOS:secureZeroOut:error:]_block_invoke
+ ___block_descriptor_40_8_32bs_e17_v16?0"NSError"8l
+ ___block_descriptor_48_8_32r40r_e20_v24?0q8"NSError"16l
+ ___block_descriptor_48_8_32r_e17_v16?0"NSError"8l
+ ___block_descriptor_48_8_32s_e29_v24?0"NSArray"8"NSError"16l
+ ___block_descriptor_48_8_32s_e42_v32?0"NSArray"8"NFApplet"16"NSError"24l
+ ___block_descriptor_56_8_32r40r_e20_v20?0B8"NSError"12l
+ ___block_descriptor_56_8_32r_e20_v20?0B8"NSError"12l
+ ___block_descriptor_56_8_32s40r_e42_v32?0"NSArray"8"NFApplet"16"NSError"24l
+ ___block_descriptor_57_8_32s40r_e17_v16?0"NSError"8l
+ ___block_descriptor_64_8_32s40r48r_e20_v24?0"NSError"8Q16l
+ ___block_descriptor_64_8_32s40s48r_e17_v16?0"NSError"8l
+ ___block_descriptor_72_8_32s40s48s56r_e17_v16?0"NSError"8l
+ ___block_descriptor_80_8_32s40s48s56r64r_e17_v16?0"NSError"8l
+ ___copy_helper_block_8_32s40s48s56r
+ ___copy_helper_block_8_32s40s48s56r64r
+ ___destroy_helper_block_8_32s40s48s56r
+ ___destroy_helper_block_8_32s40s48s56r64r
+ __block_literal_global.141
+ __block_literal_global.22
+ __block_literal_global.288
+ __block_literal_global.292
+ __block_literal_global.297
+ __block_literal_global.309
+ __block_literal_global.33
+ __block_literal_global.35
+ __block_literal_global.40
+ __block_literal_global.44
+ __block_literal_global.49
+ __block_literal_global.51
+ __block_literal_global.53
+ __block_literal_global.56
+ __block_literal_global.58
+ _objc_msgSend$_initCategoryWithType:subType:
+ _objc_msgSend$_newZeroingDataWithBytes:length:
+ _objc_msgSend$configureHardwareForLPEMWithCompletion:
+ _objc_msgSend$deassert
+ _objc_msgSend$getLPEMBluetoothLog:withCompletion:
+ _objc_msgSend$getLPEMFeaturesWithCompletion:
+ _objc_msgSend$initWithCallbackQueue:
+ _objc_msgSend$internalInit
+ _objc_msgSend$queueLPEMConfigSession:sessionAttribute:completion:
+ _objc_msgSend$queueSingleUserSession:sessionAttribute:completion:
+ _objc_msgSend$releaseAssertion:waitOnComplete:completion:
+ _objc_msgSend$requestAssertion:waitOnComplete:completion:
+ _objc_msgSend$requestBugCapture:subtype:context:
+ _objc_msgSend$setIsReleased:
+ _objc_msgSend$transceive:forSEID:toOS:redact:completion:
+ _objc_msgSend$transceive:forSEID:toOS:secureZeroOut:error:
+ _objc_msgSend$transceiveMultiple:forSEID:toOS:redact:completion:
+ _objc_msgSend$transceiveMultiple:forSEID:toOS:secureZeroOut:error:
- +[NFUnifiedAccessSession requestAssertionForKeyID:options:error:]
- -[NFDigitalCarKeySession init]
- -[NFFieldNotificationECP2_0 _initCategoryWithType:]
- -[NFSecureElementManagerSession init]
- -[NFSession init]
- -[NFUnifiedAccessAssertion .cxx_destruct]
- -[NFUnifiedAccessAssertion dealloc]
- -[NFUnifiedAccessAssertion initWithSESAssertion:]
- -[NFUnifiedAccessAssertion invalidate]
- -[NFUnifiedAccessAssertion keyIdentifier]
- -[NFUnifiedAccessAssertion sesAssertion]
- OBJC_IVAR_$_NFContactlessSession._fieldNotificationSent
- OBJC_IVAR_$_NFLoyaltyAndPaymentSession._fieldNotificationSent
- OBJC_IVAR_$_NFUnifiedAccessAssertion._sesAssertion
- _OBJC_CLASS_$_NFUnifiedAccessAssertion
- _OBJC_METACLASS_$_NFUnifiedAccessAssertion
- __112-[NFReaderSession felicaStateForSystemCode:withRequestService:withBlockReadList:performSearchServiceCode:error:]_block_invoke.142
- __28-[NFHardwareManager hasCard]_block_invoke.137
- __29-[NFHardwareManager preWarm:]_block_invoke.255
- __29-[NFSession _endProxySession]_block_invoke.32
- __30-[NFSession prioritizeSession]_block_invoke.36
- __31-[NFHardwareManager rfSettings]_block_invoke.81
- __31-[NFHardwareManager stateInfo:]_block_invoke.75
- __31-[NFSession activateWithToken:]_block_invoke.41
- __32-[NFHardwareManager blessedUser]_block_invoke.130
- __32-[NFHardwareManager toggleGPIO:]_block_invoke.162
- __32-[NFXPCServiceClient connection]_block_invoke.3
- __32-[NFXPCServiceClient connection]_block_invoke_2.4
- __33-[NFSession setSessionTimeLimit:]_block_invoke.15
- __34-[NFHardwareManager pushSignedRF:]_block_invoke.93
- __34-[NFHardwareManager setChipscope:]_block_invoke.290
- __34-[NFHardwareManager triggerCrash:]_block_invoke.160
- __35-[NFReaderSession ndefWrite:error:]_block_invoke.126
- __36-[NFHardwareManager disableHeadless]_block_invoke.114
- __36-[NFHardwareManager dumpLPMDebugLog]_block_invoke.122
- __36-[NFHardwareManager getTemperature:]_block_invoke.69
- __36-[NFReaderSession connectTag:error:]_block_invoke.113
- __36-[NFReaderSession performVAS:error:]_block_invoke.151
- __36-[NFReaderSession transceive:error:]_block_invoke.132
- __37-[NFHardwareManager getUniqueFDRKey:]_block_invoke.89
- __37-[NFHardwareManager hostEmulationLog]_block_invoke.186
- __37-[NFHardwareManager setAntiRelayRID:]_block_invoke.84
- __37-[NFReaderSession ndefReadWithError:]_block_invoke.127
- __38-[NFHardwareManager getPowerCounters:]_block_invoke.115
- __38-[NFHardwareManager releaseAssertion:]_block_invoke.158
- __38-[NFHardwareManager setAuthorization:]_block_invoke.134
- __39-[NFHardwareManager enableLPEMFeature:]_block_invoke.108
- __39-[NFHardwareManager getDieIDWithError:]_block_invoke.85
- __39-[NFHardwareManager getLPEMFTALogging:]_block_invoke.291
- __39-[NFReaderSession setECPPayload:error:]_block_invoke.104
- __39-[NFSession createSessionHandoffToken:]_block_invoke.39
- __40-[NFContactlessSession didStartSession:]_block_invoke.13
- __40-[NFContactlessSession didStartSession:]_block_invoke.18
- __40-[NFHardwareManager disableLPEMFeature:]_block_invoke.109
- __40-[NFHardwareManager expressModesEnabled]_block_invoke.96
- __40-[NFHardwareManager triggerDelayedWake:]_block_invoke.159
- __40-[NFReaderSession felicaStateWithError:]_block_invoke.136
- __40-[NFReaderSession stopPollingWithError:]_block_invoke.109
- __40-[NFReaderSession updateUIAlertMessage:]_block_invoke.149
- __40-[NFRemoteAdminManager _connectIfNeeded]_block_invoke.68
- __40-[NFRemoteAdminManager registrationInfo]_block_invoke.84
- __41-[NFReaderSession startPollingWithError:]_block_invoke.105
- __41-[NFRemoteAdminManager getAPNPublicToken]_block_invoke.112
- __42-[NFContactlessSession stopCardEmulation:]_block_invoke.61
- __42-[NFHardwareManager getRadioEnabledState:]_block_invoke.64
- __42-[NFReaderSession checkPresenceWithError:]_block_invoke.120
- __42-[NFRemoteAdminManager primaryRegionTopic]_block_invoke.88
- __43-[NFContactlessSession startCardEmulation:]_block_invoke.58
- __43-[NFHardwareManager getFlashWriteCounters:]_block_invoke.119
- __43-[NFHardwareManager setFieldDetectEnabled:]_block_invoke.141
- __43-[NFReaderSession formatNdefWithKey:error:]_block_invoke.124
- __43-[NFReaderSession restartPollingWithError:]_block_invoke.110
- __43-[NFReaderSession setPollingProfile:error:]_block_invoke.156
- __43-[NFReaderSession skipMifareClassification]_block_invoke.150
- __43-[NFRemoteAdminManager cancelCardIngestion]_block_invoke.111
- __44-[NFHardwareManager enableHeadlessTestMode:]_block_invoke.161
- __44-[NFHardwareManager expressModeControlState]_block_invoke.100
- __44-[NFHardwareManager requestAssertion:error:]_block_invoke.142
- __44-[NFHardwareManager setRadioEnabledSetting:]_block_invoke.66
- __45-[NFECommercePaymentSession didStartSession:]_block_invoke.13
- __45-[NFECommercePaymentSession didStartSession:]_block_invoke.18
- __45-[NFHardwareManager controllerInfoWithError:]_block_invoke.77
- __45-[NFHardwareManager secureElementsWithError:]_block_invoke.180
- __45-[NFReaderSession startLPCDPollingWithError:]_block_invoke.106
- __45-[NFRemoteAdminManager getSELDInfoForBroker:]_block_invoke.116
- __45-[NFRemoteAdminManager nextRequestForServer:]_block_invoke.92
- __45-[NFSecureElementManagerSession _appletsById]_block_invoke.24
- __46-[NFContactlessSession setActiveApplet:error:]_block_invoke.56
- __46-[NFLoyaltyAndPaymentSession didStartSession:]_block_invoke.13
- __46-[NFLoyaltyAndPaymentSession didStartSession:]_block_invoke.16
- __46-[NFReaderSession felicaRequestService:error:]_block_invoke.143
- __46-[NFRemoteAdminManager queueServerConnection:]_block_invoke.94
- __47-[NFContactlessPaymentSession didStartSession:]_block_invoke.13
- __47-[NFContactlessPaymentSession didStartSession:]_block_invoke.18
- __47-[NFLoyaltyAndPaymentSession startExpressMode:]_block_invoke.94
- __47-[NFSecureElementManagerSession getOSUpdateLog]_block_invoke.144
- __48-[NFHardwareManager checkUserBlessing:hasCards:]_block_invoke.123
- __48-[NFLoyaltyAndPaymentSession stopCardEmulation:]_block_invoke.85
- __48-[NFReaderSession startPollingWithConfig:error:]_block_invoke.108
- __49-[NFContactlessPaymentSession stopCardEmulation:]_block_invoke.84
- __49-[NFHardwareManager expressPassConfigsWithError:]_block_invoke.101
- __50-[NFHardwareManager configureHeadlessFactoryMode:]_block_invoke.107
- __51-[NFReaderSession didDetectTags:connectedTagIndex:]_block_invoke.88
- __51-[NFReaderSession startPollingForTechnology:error:]_block_invoke.107
- __52-[NFHardwareManager refreshSecureElementsWithError:]_block_invoke.185
- __53-[NFConnectionHandoverReceiver _processRetryRequest:]_block_invoke.514
- __54-[NFConnectionHandoverInitiator send:responseHandler:]_block_invoke.236
- __54-[NFConnectionHandoverInitiator send:responseHandler:]_block_invoke.238
- __54-[NFConnectionHandoverInitiator send:responseHandler:]_block_invoke.240
- __54-[NFConnectionHandoverReceiver _emuAssertTimerExpired]_block_invoke.472
- __54-[NFConnectionHandoverReceiver _emuAssertTimerExpired]_block_invoke.476
- __54-[NFLoyaltyAndPaymentSession _startHostCardEmulation:]_block_invoke.83
- __54-[NFLoyaltyAndPaymentSession felicaAppletState:error:]_block_invoke.86
- __54-[NFSecureElementManagerSession powerCycleSEID:error:]_block_invoke.143
- __55-[NFContactlessPaymentSession felicaAppletState:error:]_block_invoke.85
- __55-[NFLoyaltyAndPaymentSession transitAppletState:error:]_block_invoke.90
- __56-[NFContactlessPaymentSession transitAppletState:error:]_block_invoke.89
- __56-[NFHardwareManager updateHWSupportWithXPC:waitForInit:]_block_invoke.56
- __56-[NFHardwareManager updateHWSupportWithXPC:waitForInit:]_block_invoke.57
- __56-[NFHardwareManager updateHWSupportWithXPC:waitForInit:]_block_invoke.62
- __56-[NFReaderSession checkNdefSupportsRead:andWrite:error:]_block_invoke.116
- __56-[NFRemoteAdminManager queueServerConnectionForApplets:]_block_invoke.95
- __56-[NFSecureElementManagerSession deleteAllApplets:error:]_block_invoke.64
- __56-[NFSecureElementManagerSession getAndResetLPEMCounter:]_block_invoke.106
- __57-[NFHardwareManager _startFieldDetectSession:completion:]_block_invoke.208
- __57-[NFHardwareManager _startFieldDetectSession:completion:]_block_invoke.209
- __57-[NFHardwareManager checkExpressPassCompatibility:error:]_block_invoke.102
- __57-[NFHardwareManager startSinglePollExpressModeAssertion:]_block_invoke.120
- __57-[NFReaderSession(Private) runScript:parameters:results:]_block_invoke.287
- __57-[NFRemoteAdminManager deleteAllAppletsAndCleanupWithTSM]_block_invoke.119
- __57-[NFRemoteAdminManager ingestCard:withCompletionHandler:]_block_invoke.105
- __57-[NFSecureElementManagerSession expressModeControlState:]_block_invoke.114
- __57-[NFSecureElementManagerSession felicaAppletState:error:]_block_invoke.96
- __58-[NFConnectionHandoverReceiver hceSession:didReceiveAPDU:]_block_invoke.528
- __58-[NFHardwareManager releaseSinglePollExpressModeAssertion]_block_invoke.121
- __58-[NFLoyaltyAndPaymentSession enablePlasticCardMode:error:]_block_invoke.93
- __58-[NFReaderSession _disconnectTagWithCardRemoval:outError:]_block_invoke.115
- __58-[NFSecureElementManagerSession dumpDomain:forSEID:error:]_block_invoke.142
- __58-[NFSecureElementManagerSession transitAppletState:error:]_block_invoke.100
- __59-[NFRemoteAdminManager deleteAllSPAppletsAndCleanupWithTSM]_block_invoke.121
- __59-[NFSecureElementManagerSession signChallenge:certs:error:]_block_invoke.45
- __60-[NFReaderSession felicaRequestService:forSystemCode:error:]_block_invoke.147
- __60-[NFSecureElementManagerSession getAttackLogPresence:error:]_block_invoke.138
- __60-[NFSecureElementManagerSession refreshSecureElement:error:]_block_invoke.136
- __61-[NFConnectionHandoverInitiator readerSession:didDetectTags:]_block_invoke.274
- __61-[NFECommercePaymentSession validateEcommercePaymentRequest:]_block_invoke.29
- __61-[NFHardwareManager cachedEmbeddedSecureElementSerialNumber:]_block_invoke.184
- __61-[NFSecureElementManagerSession didExitRestrictedMode:error:]_block_invoke.121
- __61-[NFSecureElementManagerSession setExpressModesControlState:]_block_invoke.84
- __62-[NFSecureElementManagerSession expressModesEnabledWithError:]_block_invoke.110
- __63-[NFConnectionHandoverInitiator _startWithCustomBroadcastData:]_block_invoke.200
- __63-[NFConnectionHandoverInitiator _startWithCustomBroadcastData:]_block_invoke_2.201
- __63-[NFRemoteAdminManager deleteAllWalletAppletsAndCleanupWithTSM]_block_invoke.120
- __63-[NFRemoteAdminManager setRegistrationInfo:primaryRegionTopic:]_block_invoke.83
- __63-[NFSecureElementManagerSession getExpressPassConfigWithError:]_block_invoke.90
- __63-[NFSecureElementManagerSession transceive:forSEID:toOS:error:]_block_invoke.123
- __64-[NFLoyaltyAndPaymentSession setActivePaymentApplet:keys:error:]_block_invoke.80
- __65-[NFHardwareManager actOnUserInitiatedSystemShutDown:completion:]_block_invoke.286
- __65-[NFHardwareManager setBlessedUser:keybagUUID:withAuthorization:]_block_invoke.127
- __66-[NFHardwareManager _synchronousQueueSessionWithRetry:queueBlock:]_block_invoke.191
- __67-[NFECommercePaymentSession performECommercePayment:request:error:]_block_invoke.27
- __67-[NFSecureElementManagerSession expressAppletIdentifiersWithError:]_block_invoke.115
- __68-[NFSecureElementManagerSession getSignedPlatformDataForSeid:error:]_block_invoke.55
- __68-[NFSecureElementManagerSession performPeerPaymentEnrollment:error:]_block_invoke.116
- __68-[NFSecureElementManagerSession runScript:parameters:outputResults:]_block_invoke.127
- __68-[NFSecureElementManagerSession signChallenge:forAID:sigInfo:error:]_block_invoke.54
- __69-[NFConnectionHandoverInitiator sendHandoverRequest:responseHandler:]_block_invoke.227
- __69-[NFConnectionHandoverInitiator sendHandoverRequest:responseHandler:]_block_invoke.231
- __71-[NFSecureElementManagerSession getCryptogram:challengeResponse:error:]_block_invoke.69
- __71-[NFSecureElementManagerSession getServiceProviderDataForApplet:error:]_block_invoke.101
- __71-[NFSecureElementManagerSession transceiveMultiple:forSEID:toOS:error:]_block_invoke.125
- __72-[NFSecureElementManagerSession stateInformationWithRedirectInfo:error:]_block_invoke.43
- __72-[NFSecureElementManagerSession validateSEPairings:outSEPairingVersion:]_block_invoke.65
- __73-[NFConnectionHandoverReceiver _startWithAutoResume:customBroadcastData:]_block_invoke.448
- __73-[NFConnectionHandoverReceiver _startWithAutoResume:customBroadcastData:]_block_invoke_2.449
- __73-[NFContactlessPaymentSession startCardEmulationWithAuthorization:error:]_block_invoke.80
- __73-[NFHardwareManager validateExpressPassCompatibilityWithConfig:outError:]_block_invoke.106
- __73-[NFLoyaltyAndPaymentSession _startCardEmulationWithAuthorization:error:]_block_invoke.82
- __74-[NFContactlessPaymentSession setActivePaymentApplet:authorization:error:]_block_invoke.78
- __74-[NFRemoteAdminManager connectToServer:initialClientRequestInfo:callback:]_block_invoke.93
- __75-[NFConnectionHandoverReceiver sendHandoverSelect:delay:completionHandler:]_block_invoke.483
- __75-[NFConnectionHandoverReceiver sendHandoverSelect:delay:completionHandler:]_block_invoke.486
- __75-[NFConnectionHandoverReceiver sendHandoverSelect:delay:completionHandler:]_block_invoke.491
- __75-[NFConnectionHandoverReceiver sendHandoverSelect:delay:completionHandler:]_block_invoke_2.492
- __75-[NFSecureElementManagerSession deleteApplets:queueServerConnection:error:]_block_invoke.57
- __75-[NFSecureElementManagerSession setExpressPassConfig:restoreAuthorization:]_block_invoke.89
- __75-[NFSecureElementManagerSession stateInformationWithoutFilteringWithError:]_block_invoke.44
- __76-[NFSecureElementManagerSession restoreAuthorizarionForKeys:onApplet:error:]_block_invoke.92
- __77-[NFSecureElementManagerSession disableAuthorizationForPasses:authorization:]_block_invoke.95
- __78-[NFHardwareManager startNdefTagSessionWithBluetoothLESecureOOBData:callback:]_block_invoke.265
- __79-[NFConnectionHandoverInitiator readerSession:externalReaderFieldNotification:]_block_invoke.290
- __79-[NFConnectionHandoverReceiver _processDisconnectWithPossibleDiscoveryRestart:]_block_invoke.518
- __79-[NFSecureElementManagerSession restoreAuthorizationForAllAppletsExcept:error:]_block_invoke.91
- __80-[NFSecureElementManagerSession signChallenge:useOSVersion:signatureInfo:error:]_block_invoke.47
- __81-[NFContactlessPaymentSession startDeferredCardEmulationWithAuthorization:error:]_block_invoke.83
- __81-[NFLoyaltyAndPaymentSession _startDeferredCardEmulationWithAuthorization:error:]_block_invoke.84
- __82-[NFSecureElementManagerSession getAttackCounterLogForSEID:acknowledgeLogs:error:]_block_invoke.137
- __85-[NFConnectionHandoverInitiator _processSelectRetry:originalRequest:responseHandler:]_block_invoke.224
- __87-[NFHardwareManager getReaderProhibitTimerInfoSERmRunning:hostRmRunning:remainingInMs:]_block_invoke.73
- __88-[NFSecureElementManagerSession getServiceProviderDataForApplet:publicKey:scheme:error:]_block_invoke.105
- __91-[NFSecureElementManagerSession disableAuthorizationForApplets:andKey:authorization:error:]_block_invoke.94
- __Block_byref_object_copy_.470
- __Block_byref_object_dispose_.471
- __OBJC_$_CLASS_METHODS_NFUnifiedAccessSession
- __OBJC_$_INSTANCE_METHODS_NFUnifiedAccessAssertion
- __OBJC_$_INSTANCE_VARIABLES_NFUnifiedAccessAssertion
- __OBJC_$_PROP_LIST_NFUnifiedAccessAssertion
- __OBJC_CLASS_RO_$_NFUnifiedAccessAssertion
- __OBJC_METACLASS_RO_$_NFUnifiedAccessAssertion
- ___40-[NFContactlessSession didStartSession:]_block_invoke_2
- ___45-[NFECommercePaymentSession didStartSession:]_block_invoke_2
- ___46-[NFLoyaltyAndPaymentSession didStartSession:]_block_invoke_2
- ___63-[NFSecureElementManagerSession transceive:forSEID:toOS:error:]_block_invoke
- ___71-[NFSecureElementManagerSession transceiveMultiple:forSEID:toOS:error:]_block_invoke
- ___block_descriptor_40_8_32s_e25_v32?0"NFApplet"8Q16^B24l
- ___block_descriptor_40_8_32s_e29_v24?0"NSArray"8"NSError"16l
- ___block_descriptor_48_8_32r_e20_v24?0q8"NSError"16l
- ___block_descriptor_48_8_32s40r_e42_v32?0"NSArray"8"NFApplet"16"NSError"24l
- __block_literal_global.136
- __block_literal_global.16
- __block_literal_global.21
- __block_literal_global.23
- __block_literal_global.25
- __block_literal_global.273
- __block_literal_global.277
- __block_literal_global.282
- __block_literal_global.287
- __block_literal_global.34
- __block_literal_global.38
- __block_literal_global.39
- __block_literal_global.41
- __block_literal_global.50
- __block_literal_global.52
- _objc_msgSend$requestAssertion:completion:
- _objc_msgSend$transceive:forSEID:toOS:completion:
- _objc_msgSend$transceiveMultiple:forSEID:toOS:completion:
- _objc_msgSend$transceiveMultiple:forSEID:toOS:error:
CStrings:
+ "%c[%{public}s %{public}s]:%i %@"
+ "%c[%{public}s %{public}s]:%i %{public}@ auto released"
+ "%c[%{public}s %{public}s]:%i Duplicated applet found: %{public}@"
+ "%c[%{public}s %{public}s]:%i Missing / invalid NFAssertionTypeKey value"
+ "%c[%{public}s %{public}s]:%i Proxy cleared"
+ "%c[%{public}s %{public}s]:%i Session already ended"
+ "%c[%{public}s %{public}s]:%i Session not active yet"
+ "%c[%{public}s %{public}s]:%i Session proxy is nil"
+ "%c[%{public}s %{public}s]:%i started=%@ isFirstInQueue=%d"
+ "@32@0:8@16^B24"
+ "@32@0:8Q16@?24"
+ "@52@0:8@16@24q32B40^@44"
+ "AID:%@  : Keys=%@ :  Error: %@"
+ "AIDS: %@   :  Error: %@"
+ "Express config failure - restoreAuthorizationForAllAppletsExcept"
+ "Express config failure - restoreAuthorizationForKeys"
+ "Express config failure: setExpressPassconfig:restoreAuthorization:%@"
+ "Legacy wallet force as default presentment"
+ "NFLPEMConfigSessionCallbacks"
+ "NFLPEMConfigSessionInterface"
+ "NFSingleUserSession"
+ "NFSingleUserSessionCallbacks"
+ "NFSingleUserSessionInterface"
+ "No connection to seld"
+ "Processing error"
+ "T@\"NSData\",R,N"
+ "TB,V_isReleased"
+ "Vv24@0:8@?<v@?@\"NSError\"Q>16"
+ "Vv28@0:8B16@?<v@?@\"NSError\"@\"NSDictionary\">20"
+ "Vv32@0:8@\"NSUUID\"16@?<v@?B@\"NSError\">24"
+ "Vv36@0:8@\"NFAssertionInternal\"16B24@?<v@?@\"NSError\">28"
+ "Vv36@0:8@\"NSDictionary\"16B24@?<v@?@\"NFAssertionInternal\"@\"NSError\">28"
+ "Vv40@0:8@\"NSObject<NFLPEMConfigSessionCallbacks>\"16@\"NSDictionary\"24@?<v@?@\"NSObject<NFLPEMConfigSessionInterface>\"B@\"NSError\">32"
+ "Vv40@0:8@\"NSObject<NFSingleUserSessionCallbacks>\"16@\"NSDictionary\"24@?<v@?@\"NSObject<NFSingleUserSessionInterface>\"B@\"NSError\">32"
+ "Vv48@0:8@\"NSUUID\"16@\"NSUUID\"24@\"NSData\"32@?<v@?@\"NSError\">40"
+ "Vv52@0:8@\"NSArray\"16@\"NSString\"24q32B40@?<v@?@\"NSArray\"@\"NSError\">44"
+ "Vv52@0:8@\"NSData\"16@\"NSString\"24q32B40@?<v@?@\"NSData\"@\"NSError\">44"
+ "Vv52@0:8@16@24q32B40@?44"
+ "XPC error"
+ "_initCategoryWithType:subType:"
+ "_isReleased"
+ "_newZeroingDataWithBytes:length:"
+ "configureHardwareForLPEMWithCompletion:"
+ "deassert"
+ "getLPEMBluetoothLog:withCompletion:"
+ "getLPEMFeaturesWithCompletion:"
+ "hasCard:"
+ "initWithCallbackQueue:"
+ "internalInit"
+ "isReleased"
+ "moduleIdentifierAsData"
+ "processing error"
+ "queueAssertion:completion:"
+ "queueAssertionWithParams:completion:"
+ "queueLPEMConfigSession:sessionAttribute:completion:"
+ "queueSingleUserSession:sessionAttribute:completion:"
+ "releaseAssertion:completion"
+ "releaseAssertion:waitOnComplete:completion:"
+ "requestAssertion:waitOnComplete:completion:"
+ "requestAssertionWithParams:error:"
+ "requestBugCapture:subtype:context:"
+ "setIsReleased:"
+ "startSingleUserSession:"
+ "transceive:forSEID:toOS:redact:completion:"
+ "transceive:forSEID:toOS:secureZeroOut:error:"
+ "transceiveMultiple:forSEID:toOS:redact:completion:"
+ "transceiveMultiple:forSEID:toOS:secureZeroOut:error:"
+ "v28@0:8Q16C24"
+ "v40@0:8@16@24@32"
- "%c[%{public}s %{public}s]:%i Unsupported."
- "@\"SESAssertion\""
- "NFUnifiedAccessAssertion"
- "T@\"SESAssertion\",R,N,V_sesAssertion"
- "Vv32@0:8@\"NFAssertionInternal\"16@?<v@?@\"NSError\">24"
- "Vv32@0:8Q16@?<v@?@\"NFAssertionInternal\"@\"NSError\">24"
- "Vv48@0:8@\"NSArray\"16@\"NSString\"24q32@?<v@?@\"NSArray\"@\"NSError\">40"
- "Vv48@0:8@\"NSData\"16@\"NSString\"24q32@?<v@?@\"NSData\"@\"NSError\">40"
- "Vv48@0:8@16@24q32@?40"
- "_sesAssertion"
- "initWithSESAssertion:"
- "requestAssertion:completion:"
- "requestAssertionForKeyID:options:error:"
- "sesAssertion"
- "setActivePaymentApplets:keys:error:"
- "transceive:forSEID:toOS:completion:"
- "transceiveMultiple:forSEID:toOS:completion:"

```
