## NearField

> `/System/Library/PrivateFrameworks/NearField.framework/NearField`

```diff

-342.4.1.0.0
-  __TEXT.__text: 0x94a20
-  __TEXT.__auth_stubs: 0x7e0
-  __TEXT.__objc_methlist: 0x4ef0
+344.25.0.0.0
+  __TEXT.__text: 0x987e8
+  __TEXT.__auth_stubs: 0x800
+  __TEXT.__objc_methlist: 0x4ff0
   __TEXT.__const: 0x1e0
-  __TEXT.__cstring: 0x5f42
-  __TEXT.__oslogstring: 0x4903
+  __TEXT.__cstring: 0x6213
+  __TEXT.__oslogstring: 0x4b68
   __TEXT.__dlopen_cstrs: 0x10c
-  __TEXT.__unwind_info: 0x18b4
-  __TEXT.__objc_classname: 0xe1f
-  __TEXT.__objc_methname: 0xc741
-  __TEXT.__objc_methtype: 0x33e4
-  __TEXT.__objc_stubs: 0x77a0
-  __DATA_CONST.__got: 0xa0
-  __DATA_CONST.__const: 0x2410
-  __DATA_CONST.__objc_classlist: 0x308
+  __TEXT.__unwind_info: 0x1918
+  __TEXT.__objc_classname: 0xe4c
+  __TEXT.__objc_methname: 0xcbe1
+  __TEXT.__objc_methtype: 0x3420
+  __TEXT.__objc_stubs: 0x7940
+  __DATA_CONST.__got: 0xa8
+  __DATA_CONST.__const: 0x2470
+  __DATA_CONST.__objc_classlist: 0x310
   __DATA_CONST.__objc_catlist: 0x30
-  __DATA_CONST.__objc_protolist: 0x220
+  __DATA_CONST.__objc_protolist: 0x228
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x9ff0
-  __DATA_CONST.__objc_selrefs: 0x2e00
+  __DATA_CONST.__objc_const: 0xa2f8
+  __DATA_CONST.__objc_selrefs: 0x2ec0
+  __DATA_CONST.__objc_protorefs: 0x168
+  __DATA_CONST.__objc_classrefs: 0x408
+  __DATA_CONST.__objc_superrefs: 0x220
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__cfstring: 0x3ee0
-  __AUTH_CONST.__objc_intobj: 0x738
+  __AUTH_CONST.__cfstring: 0x3fe0
+  __AUTH_CONST.__objc_intobj: 0x7f8
   __AUTH_CONST.__objc_const: 0x2cd0
-  __AUTH_CONST.__const: 0x2e0
+  __AUTH_CONST.__const: 0x2c0
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH_CONST.__auth_got: 0x3f8
-  __AUTH.__objc_data: 0xd70
-  __DATA.__objc_protorefs: 0x160
-  __DATA.__objc_classrefs: 0x400
-  __DATA.__objc_superrefs: 0x218
-  __DATA.__objc_ivar: 0x4e4
-  __DATA.__data: 0x1980
+  __AUTH_CONST.__auth_got: 0x408
+  __AUTH.__objc_data: 0xdc0
+  __DATA.__objc_ivar: 0x4fc
+  __DATA.__data: 0x19e0
   __DATA.__bss: 0x40
-  __DATA_DIRTY.__objc_ivar: 0x148
+  __DATA_DIRTY.__objc_ivar: 0x168
   __DATA_DIRTY.__objc_data: 0x10e0
-  __DATA_DIRTY.__bss: 0xf0
+  __DATA_DIRTY.__bss: 0xe0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/SEService.framework/SEService

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libnfshared.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: CB1643D1-E01D-35C3-8903-5B6BEB36F067
-  Functions: 2327
-  Symbols:   7463
-  CStrings:  4440
+  UUID: 59AECD9A-2BCA-31C8-B2AA-7265657B3DCC
+  Functions: 2368
+  Symbols:   7576
+  CStrings:  4519
 
Symbols:
+ +[NFFieldNotification fieldNotificationFromXPCObject:]
+ -[NFConnectionHandoverController startWithCustomBroadcastData:]
+ -[NFConnectionHandoverInitiator _startWithCustomBroadcastData:]
+ -[NFConnectionHandoverInitiator setEcpFrame:]
+ -[NFConnectionHandoverInitiator startWithCustomBroadcastData:]
+ -[NFConnectionHandoverReceiver _startWithAutoResume:customBroadcastData:]
+ -[NFConnectionHandoverReceiver startAutoResumeOnFieldDisableWithCustomBroadcastData:]
+ -[NFConnectionHandoverReceiver startWithCustomBroadcastData:]
+ -[NFFieldNotification asXPCObject]
+ -[NFFieldNotification category]
+ -[NFFieldNotification setCategory:]
+ -[NFFieldNotification(ConnectionHandover) chRandomData]
+ -[NFFieldNotificationECP1_0 _initCategoryWithType:]
+ -[NFFieldNotificationECP2_0 _initCategoryWithType:]
+ -[NFHardwareManager validateExpressPassCompatibilityWithConfig:outError:]
+ -[NFLPEMConfigSession getAndClearLPEMBluetoothLogWithError:]
+ -[NFRemoteAdminManager deleteAllSPAppletsAndCleanupWithTSM]
+ -[NFRemoteAdminManager deleteAllWalletAppletsAndCleanupWithTSM]
+ -[NFSecureElementManagerSession deleteAllAppletsOfType:queueConnection:error:]
+ -[NFWalletPresentation .cxx_destruct]
+ -[NFWalletPresentation dealloc]
+ -[NFWalletPresentation didInterrupt:]
+ -[NFWalletPresentation didInvalidate]
+ -[NFWalletPresentation init]
+ -[NFWalletPresentation invalidateXPCClient]
+ -[NFWalletPresentation present]
+ -[NFXPCServiceClient .cxx_destruct]
+ -[NFXPCServiceClient addDelegate:]
+ -[NFXPCServiceClient connection]
+ -[NFXPCServiceClient initWithService:remoteObjectInterface:exportedInterface:exportedObject:]
+ -[NFXPCServiceClient initWithService:remoteObjectInterface:exportedInterface:exportedObject:xpcDispatchQueue:]
+ -[NFXPCServiceClient removeDelegate:]
+ _OBJC_CLASS_$_NFWalletPresentation
+ _OBJC_CLASS_$_NFXPCServiceClient
+ _OBJC_CLASS_$_NSKeyedArchiver
+ _OBJC_IVAR_$_NFFieldNotification._category
+ _OBJC_IVAR_$_NFHardwareManager._xpcQueue
+ _OBJC_IVAR_$_NFWalletPresentation._xpcClient
+ _OBJC_IVAR_$_NFWalletPresentation._xpcClientLock
+ _OBJC_IVAR_$_NFXPCServiceClient._clientCount
+ _OBJC_IVAR_$_NFXPCServiceClient._delegates
+ _OBJC_IVAR_$_NFXPCServiceClient._exportedInterface
+ _OBJC_IVAR_$_NFXPCServiceClient._exportedObject
+ _OBJC_IVAR_$_NFXPCServiceClient._remoteObjectInterface
+ _OBJC_IVAR_$_NFXPCServiceClient._serviceName
+ _OBJC_IVAR_$_NFXPCServiceClient._xpcConnection
+ _OBJC_IVAR_$_NFXPCServiceClient._xpcQueue
+ _OBJC_METACLASS_$_NFWalletPresentation
+ _OBJC_METACLASS_$_NFXPCServiceClient
+ __CFXPCCreateCFObjectFromXPCObject
+ __GenerateAutoNegotiationECPFrame
+ __OBJC_$_INSTANCE_METHODS_NFWalletPresentation
+ __OBJC_$_INSTANCE_METHODS_NFXPCServiceClient
+ __OBJC_$_INSTANCE_VARIABLES_NFWalletPresentation
+ __OBJC_$_INSTANCE_VARIABLES_NFXPCServiceClient
+ __OBJC_$_PROP_LIST_NFNdefMessage.82
+ __OBJC_$_PROP_LIST_NFNdefRecord.156
+ __OBJC_$_PROP_LIST_NFTag.195
+ __OBJC_$_PROP_LIST_NFXPCServiceClient
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NFWalletPresentationInterface
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NFXPCServiceClientDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NFWalletPresentationInterface
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NFXPCServiceClientDelegate
+ __OBJC_CLASS_PROTOCOLS_$_NFWalletPresentation
+ __OBJC_CLASS_RO_$_NFWalletPresentation
+ __OBJC_CLASS_RO_$_NFXPCServiceClient
+ __OBJC_LABEL_PROTOCOL_$_NFWalletPresentationInterface
+ __OBJC_LABEL_PROTOCOL_$_NFXPCServiceClientDelegate
+ __OBJC_METACLASS_RO_$_NFWalletPresentation
+ __OBJC_METACLASS_RO_$_NFXPCServiceClient
+ __OBJC_PROTOCOL_$_NFWalletPresentationInterface
+ __OBJC_PROTOCOL_$_NFXPCServiceClientDelegate
+ __OBJC_PROTOCOL_REFERENCE_$_NFWalletPresentationInterface
+ ___29-[NFHardwareManager preWarm:]_block_invoke.177
+ ___31-[NFHardwareManager rfSettings]_block_invoke.65
+ ___31-[NFHardwareManager stateInfo:]_block_invoke.61
+ ___31-[NFWalletPresentation present]_block_invoke
+ ___31-[NFWalletPresentation present]_block_invoke.10
+ ___32-[NFHardwareManager toggleGPIO:]_block_invoke.97
+ ___32-[NFXPCServiceClient connection]_block_invoke
+ ___32-[NFXPCServiceClient connection]_block_invoke_2
+ ___32-[NFXPCServiceClient connection]_block_invoke_3
+ ___32-[NFXPCServiceClient connection]_block_invoke_4
+ ___33-[NFWalletPresentation xpcClient]_block_invoke
+ ___34-[NFHardwareManager pushSignedRF:]_block_invoke.70
+ ___34-[NFHardwareManager setChipscope:]_block_invoke.250
+ ___36-[NFHardwareManager disableHeadless]_block_invoke.84
+ ___36-[NFHardwareManager dumpLPMDebugLog]_block_invoke.90
+ ___36-[NFHardwareManager getTemperature:]_block_invoke.59
+ ___37-[NFHardwareManager getUniqueFDRKey:]_block_invoke.68
+ ___37-[NFHardwareManager hostEmulationLog]_block_invoke.112
+ ___37-[NFWalletPresentation didInvalidate]_block_invoke
+ ___38-[NFHardwareManager getPowerCounters:]_block_invoke.85
+ ___38-[NFHardwareManager releaseAssertion:]_block_invoke.94
+ ___39-[NFHardwareManager enableLPEMFeature:]_block_invoke.80
+ ___39-[NFHardwareManager getDieIDWithError:]_block_invoke.66
+ ___39-[NFHardwareManager getLPEMFTALogging:]_block_invoke.251
+ ___40-[NFHardwareManager disableLPEMFeature:]_block_invoke.81
+ ___40-[NFHardwareManager expressModesEnabled]_block_invoke.73
+ ___40-[NFHardwareManager startSesHatSession:]_block_invoke.168
+ ___40-[NFHardwareManager triggerDelayedWake:]_block_invoke.95
+ ___40-[NFRemoteAdminManager registrationInfo]_block_invoke.83
+ ___41-[NFRemoteAdminManager getAPNPublicToken]_block_invoke.105
+ ___42-[NFHardwareManager getRadioEnabledState:]_block_invoke.56
+ ___42-[NFRemoteAdminManager primaryRegionTopic]_block_invoke.85
+ ___43-[NFHardwareManager getFlashWriteCounters:]_block_invoke.87
+ ___43-[NFHardwareManager setFieldDetectEnabled:]_block_invoke.91
+ ___43-[NFRemoteAdminManager cancelCardIngestion]_block_invoke.104
+ ___43-[NFWalletPresentation invalidateXPCClient]_block_invoke
+ ___44-[NFHardwareManager enableHeadlessTestMode:]_block_invoke.96
+ ___44-[NFHardwareManager expressModeControlState]_block_invoke.75
+ ___44-[NFHardwareManager requestAssertion:error:]_block_invoke.92
+ ___44-[NFHardwareManager setRadioEnabledSetting:]_block_invoke.58
+ ___45-[NFHardwareManager controllerInfoWithError:]_block_invoke.63
+ ___45-[NFHardwareManager secureElementsWithError:]_block_invoke.107
+ ___45-[NFRemoteAdminManager getSELDInfoForBroker:]_block_invoke.107
+ ___45-[NFRemoteAdminManager nextRequestForServer:]_block_invoke.87
+ ___46-[NFRemoteAdminManager queueServerConnection:]_block_invoke.89
+ ___47-[NFSecureElementManagerSession getOSUpdateLog]_block_invoke.116
+ ___50-[NFHardwareManager configureHeadlessFactoryMode:]_block_invoke.79
+ ___52-[NFHardwareManager refreshSecureElementsWithError:]_block_invoke.111
+ ___53-[NFConnectionHandoverReceiver _processRetryRequest:]_block_invoke.468
+ ___54-[NFConnectionHandoverInitiator send:responseHandler:]_block_invoke.222
+ ___54-[NFConnectionHandoverInitiator send:responseHandler:]_block_invoke.224
+ ___54-[NFConnectionHandoverInitiator send:responseHandler:]_block_invoke_2.225
+ ___54-[NFConnectionHandoverReceiver _emuAssertTimerExpired]_block_invoke.438
+ ___54-[NFSecureElementManagerSession powerCycleSEID:error:]_block_invoke.115
+ ___56-[NFHardwareManager updateHWSupportWithXPC:waitForInit:]_block_invoke.50
+ ___56-[NFHardwareManager updateHWSupportWithXPC:waitForInit:]_block_invoke.51
+ ___56-[NFHardwareManager updateHWSupportWithXPC:waitForInit:]_block_invoke.54
+ ___56-[NFRemoteAdminManager queueServerConnectionForApplets:]_block_invoke.90
+ ___56-[NFSecureElementManagerSession deleteAllApplets:error:]_block_invoke.58
+ ___56-[NFSecureElementManagerSession getAndResetLPEMCounter:]_block_invoke.92
+ ___57-[NFHardwareManager _startFieldDetectSession:completion:]_block_invoke.129
+ ___57-[NFHardwareManager checkExpressPassCompatibility:error:]_block_invoke.76
+ ___57-[NFHardwareManager startSinglePollExpressModeAssertion:]_block_invoke.88
+ ___57-[NFReaderSession(Private) runScript:parameters:results:]_block_invoke.270
+ ___57-[NFRemoteAdminManager deleteAllAppletsAndCleanupWithTSM]_block_invoke.108
+ ___57-[NFRemoteAdminManager ingestCard:withCompletionHandler:]_block_invoke.100
+ ___57-[NFSecureElementManagerSession expressModeControlState:]_block_invoke.96
+ ___57-[NFSecureElementManagerSession felicaAppletState:error:]_block_invoke.86
+ ___58-[NFConnectionHandoverReceiver hceSession:didReceiveAPDU:]_block_invoke.482
+ ___58-[NFHardwareManager releaseSinglePollExpressModeAssertion]_block_invoke.89
+ ___58-[NFSecureElementManagerSession dumpDomain:forSEID:error:]_block_invoke.114
+ ___58-[NFSecureElementManagerSession transitAppletState:error:]_block_invoke.88
+ ___59-[NFRemoteAdminManager deleteAllSPAppletsAndCleanupWithTSM]_block_invoke
+ ___59-[NFRemoteAdminManager deleteAllSPAppletsAndCleanupWithTSM]_block_invoke.110
+ ___60-[NFLPEMConfigSession getAndClearLPEMBluetoothLogWithError:]_block_invoke
+ ___60-[NFLPEMConfigSession getAndClearLPEMBluetoothLogWithError:]_block_invoke.56
+ ___60-[NFSecureElementManagerSession getAttackLogPresence:error:]_block_invoke.112
+ ___60-[NFSecureElementManagerSession refreshSecureElement:error:]_block_invoke.110
+ ___61-[NFConnectionHandoverInitiator readerSession:didDetectTags:]_block_invoke.253
+ ___61-[NFConnectionHandoverInitiator readerSession:didDetectTags:]_block_invoke.256
+ ___61-[NFConnectionHandoverReceiver startWithCustomBroadcastData:]_block_invoke
+ ___61-[NFHardwareManager cachedEmbeddedSecureElementSerialNumber:]_block_invoke.110
+ ___61-[NFSecureElementManagerSession didExitRestrictedMode:error:]_block_invoke.101
+ ___61-[NFSecureElementManagerSession setExpressModesControlState:]_block_invoke.76
+ ___62-[NFConnectionHandoverInitiator startWithCustomBroadcastData:]_block_invoke
+ ___62-[NFSecureElementManagerSession expressModesEnabledWithError:]_block_invoke.94
+ ___63-[NFConnectionHandoverInitiator _startWithCustomBroadcastData:]_block_invoke
+ ___63-[NFConnectionHandoverInitiator _startWithCustomBroadcastData:]_block_invoke_2
+ ___63-[NFRemoteAdminManager deleteAllWalletAppletsAndCleanupWithTSM]_block_invoke
+ ___63-[NFRemoteAdminManager deleteAllWalletAppletsAndCleanupWithTSM]_block_invoke.109
+ ___63-[NFRemoteAdminManager setRegistrationInfo:primaryRegionTopic:]_block_invoke.82
+ ___63-[NFSecureElementManagerSession getExpressPassConfigWithError:]_block_invoke.80
+ ___63-[NFSecureElementManagerSession transceive:forSEID:toOS:error:]_block_invoke.103
+ ___65-[NFHardwareManager actOnUserInitiatedSystemShutDown:completion:]_block_invoke.248
+ ___66-[NFHardwareManager _synchronousQueueSessionWithRetry:queueBlock:]_block_invoke.115
+ ___67-[NFSecureElementManagerSession expressAppletIdentifiersWithError:]_block_invoke.97
+ ___68-[NFSecureElementManagerSession performPeerPaymentEnrollment:error:]_block_invoke.98
+ ___68-[NFSecureElementManagerSession runScript:parameters:outputResults:]_block_invoke.107
+ ___69-[NFConnectionHandoverInitiator sendHandoverRequest:responseHandler:]_block_invoke.214
+ ___69-[NFConnectionHandoverInitiator sendHandoverRequest:responseHandler:]_block_invoke.218
+ ___71-[NFSecureElementManagerSession getCryptogram:challengeResponse:error:]_block_invoke.61
+ ___71-[NFSecureElementManagerSession getServiceProviderDataForApplet:error:]_block_invoke.89
+ ___71-[NFSecureElementManagerSession transceiveMultiple:forSEID:toOS:error:]_block_invoke.105
+ ___72-[NFSecureElementManagerSession validateSEPairings:outSEPairingVersion:]_block_invoke.59
+ ___73-[NFConnectionHandoverReceiver _startWithAutoResume:customBroadcastData:]_block_invoke
+ ___73-[NFConnectionHandoverReceiver _startWithAutoResume:customBroadcastData:]_block_invoke_2
+ ___73-[NFHardwareManager validateExpressPassCompatibilityWithConfig:outError:]_block_invoke
+ ___73-[NFHardwareManager validateExpressPassCompatibilityWithConfig:outError:]_block_invoke.78
+ ___74-[NFRemoteAdminManager connectToServer:initialClientRequestInfo:callback:]_block_invoke.88
+ ___75-[NFConnectionHandoverReceiver sendHandoverSelect:delay:completionHandler:]_block_invoke.445
+ ___75-[NFConnectionHandoverReceiver sendHandoverSelect:delay:completionHandler:]_block_invoke.448
+ ___75-[NFConnectionHandoverReceiver sendHandoverSelect:delay:completionHandler:]_block_invoke.450
+ ___75-[NFConnectionHandoverReceiver sendHandoverSelect:delay:completionHandler:]_block_invoke_2.451
+ ___75-[NFConnectionHandoverReceiver sendHandoverSelect:delay:completionHandler:]_block_invoke_3.452
+ ___75-[NFSecureElementManagerSession setExpressPassConfig:restoreAuthorization:]_block_invoke.79
+ ___76-[NFSecureElementManagerSession restoreAuthorizarionForKeys:onApplet:error:]_block_invoke.82
+ ___77-[NFSecureElementManagerSession disableAuthorizationForPasses:authorization:]_block_invoke.85
+ ___78-[NFHardwareManager startNdefTagSessionWithBluetoothLESecureOOBData:callback:]_block_invoke.185
+ ___79-[NFConnectionHandoverInitiator readerSession:externalReaderFieldNotification:]_block_invoke.264
+ ___79-[NFConnectionHandoverReceiver _processDisconnectWithPossibleDiscoveryRestart:]_block_invoke.472
+ ___79-[NFSecureElementManagerSession restoreAuthorizationForAllAppletsExcept:error:]_block_invoke.81
+ ___82-[NFSecureElementManagerSession getAttackCounterLogForSEID:acknowledgeLogs:error:]_block_invoke.111
+ ___85-[NFConnectionHandoverInitiator _processSelectRetry:originalRequest:responseHandler:]_block_invoke.211
+ ___85-[NFConnectionHandoverReceiver startAutoResumeOnFieldDisableWithCustomBroadcastData:]_block_invoke
+ ___88-[NFSecureElementManagerSession getServiceProviderDataForApplet:publicKey:scheme:error:]_block_invoke.91
+ ___91-[NFSecureElementManagerSession disableAuthorizationForApplets:andKey:authorization:error:]_block_invoke.84
+ ___Block_byref_object_copy_.433
+ ___Block_byref_object_dispose_.434
+ ___block_literal_global.238
+ ___block_literal_global.243
+ ___block_literal_global.246
+ ___block_literal_global.302
+ ___block_literal_global.37
+ ___block_literal_global.40
+ ___block_literal_global.85
+ __unnamed_array_storage.147
+ __unnamed_array_storage.149
+ __unnamed_array_storage.150
+ __xpc_type_data
+ _objc_msgSend$_initCategoryWithType:
+ _objc_msgSend$_queue
+ _objc_msgSend$_startWithAutoResume:customBroadcastData:
+ _objc_msgSend$_startWithCustomBroadcastData:
+ _objc_msgSend$archivedDataWithRootObject:requiringSecureCoding:error:
+ _objc_msgSend$checkExpressPassCompatibilityDeprecated:callback:
+ _objc_msgSend$controllerDidDetectPotentialInitiator:field:
+ _objc_msgSend$deleteAllSPAppletsAndCleanupWithTSMithCompletion:
+ _objc_msgSend$deleteAllWalletAppletsAndCleanupWithTSMWithCompletion:
+ _objc_msgSend$felicaStateForSystemCode:withRequestService:performSearchServiceCode:completion:
+ _objc_msgSend$getLPEMBluetoothLog:withCompletion:
+ _objc_msgSend$initWithService:remoteObjectInterface:exportedInterface:exportedObject:
+ _objc_msgSend$initWithService:remoteObjectInterface:exportedInterface:exportedObject:xpcDispatchQueue:
+ _objc_msgSend$managedBySP
+ _objc_msgSend$presentWithCompletion:
+ _objc_msgSend$setCategory:
+ _objc_msgSend$setWithObjects:
+ _objc_msgSend$unarchivedArrayOfObjectsOfClasses:fromData:error:
+ _xpc_get_type
- +[NFHardwareManagerXPC sharedXPC]
- -[NFConnectionHandoverInitiator _start]
- -[NFConnectionHandoverReceiver _startWithAutoResume:]
- -[NFHardwareManagerXPC .cxx_destruct]
- -[NFHardwareManagerXPC addDelegate:]
- -[NFHardwareManagerXPC connection]
- -[NFHardwareManagerXPC init]
- -[NFHardwareManagerXPC removeDelegate:]
- _OBJC_CLASS_$_NFHardwareManagerXPC
- _OBJC_IVAR_$_NFFieldDetectSession._delegate
- _OBJC_IVAR_$_NFFieldDetectSession._fieldNotificationSent
- _OBJC_IVAR_$_NFHardwareManagerXPC._clientCount
- _OBJC_IVAR_$_NFHardwareManagerXPC._delegates
- _OBJC_IVAR_$_NFHardwareManagerXPC._xpcConnection
- _OBJC_IVAR_$_NFHardwareManagerXPC._xpcQueue
- _OBJC_METACLASS_$_NFHardwareManagerXPC
- __OBJC_$_CLASS_METHODS_NFHardwareManagerXPC
- __OBJC_$_INSTANCE_METHODS_NFHardwareManagerXPC
- __OBJC_$_INSTANCE_VARIABLES_NFHardwareManagerXPC
- __OBJC_$_PROP_LIST_NFHardwareManagerXPC
- __OBJC_$_PROP_LIST_NFNdefMessage.81
- __OBJC_$_PROP_LIST_NFNdefRecord.155
- __OBJC_$_PROP_LIST_NFTag.194
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NFHardwareManagerXPCDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_NFHardwareManagerXPCDelegate
- __OBJC_CLASS_RO_$_NFHardwareManagerXPC
- __OBJC_LABEL_PROTOCOL_$_NFHardwareManagerXPCDelegate
- __OBJC_METACLASS_RO_$_NFHardwareManagerXPC
- __OBJC_PROTOCOL_$_NFHardwareManagerXPCDelegate
- ___29-[NFHardwareManager preWarm:]_block_invoke.171
- ___31-[NFHardwareManager rfSettings]_block_invoke.60
- ___31-[NFHardwareManager stateInfo:]_block_invoke.56
- ___32-[NFHardwareManager toggleGPIO:]_block_invoke.91
- ___33+[NFHardwareManagerXPC sharedXPC]_block_invoke
- ___34-[NFHardwareManager pushSignedRF:]_block_invoke.65
- ___34-[NFHardwareManager setChipscope:]_block_invoke.241
- ___34-[NFHardwareManagerXPC connection]_block_invoke
- ___34-[NFHardwareManagerXPC connection]_block_invoke_2
- ___34-[NFHardwareManagerXPC connection]_block_invoke_3
- ___34-[NFHardwareManagerXPC connection]_block_invoke_4
- ___36-[NFHardwareManager disableHeadless]_block_invoke.78
- ___36-[NFHardwareManager dumpLPMDebugLog]_block_invoke.84
- ___36-[NFHardwareManager getTemperature:]_block_invoke.54
- ___37-[NFHardwareManager getUniqueFDRKey:]_block_invoke.63
- ___37-[NFHardwareManager hostEmulationLog]_block_invoke.106
- ___38-[NFHardwareManager getPowerCounters:]_block_invoke.79
- ___38-[NFHardwareManager releaseAssertion:]_block_invoke.88
- ___39-[NFConnectionHandoverInitiator _start]_block_invoke
- ___39-[NFConnectionHandoverInitiator _start]_block_invoke_2
- ___39-[NFHardwareManager enableLPEMFeature:]_block_invoke.74
- ___39-[NFHardwareManager getDieIDWithError:]_block_invoke.61
- ___39-[NFHardwareManager getLPEMFTALogging:]_block_invoke.242
- ___40-[NFHardwareManager disableLPEMFeature:]_block_invoke.75
- ___40-[NFHardwareManager expressModesEnabled]_block_invoke.68
- ___40-[NFHardwareManager startSesHatSession:]_block_invoke.162
- ___40-[NFHardwareManager triggerDelayedWake:]_block_invoke.89
- ___40-[NFRemoteAdminManager registrationInfo]_block_invoke.82
- ___41-[NFRemoteAdminManager getAPNPublicToken]_block_invoke.104
- ___42-[NFHardwareManager getRadioEnabledState:]_block_invoke.51
- ___42-[NFRemoteAdminManager primaryRegionTopic]_block_invoke.84
- ___43-[NFHardwareManager getFlashWriteCounters:]_block_invoke.81
- ___43-[NFHardwareManager setFieldDetectEnabled:]_block_invoke.85
- ___43-[NFRemoteAdminManager cancelCardIngestion]_block_invoke.103
- ___44-[NFHardwareManager enableHeadlessTestMode:]_block_invoke.90
- ___44-[NFHardwareManager expressModeControlState]_block_invoke.70
- ___44-[NFHardwareManager requestAssertion:error:]_block_invoke.86
- ___44-[NFHardwareManager setRadioEnabledSetting:]_block_invoke.53
- ___45-[NFHardwareManager controllerInfoWithError:]_block_invoke.58
- ___45-[NFHardwareManager secureElementsWithError:]_block_invoke.101
- ___45-[NFRemoteAdminManager getSELDInfoForBroker:]_block_invoke.106
- ___45-[NFRemoteAdminManager nextRequestForServer:]_block_invoke.86
- ___46-[NFRemoteAdminManager queueServerConnection:]_block_invoke.88
- ___47-[NFSecureElementManagerSession getOSUpdateLog]_block_invoke.114
- ___50-[NFHardwareManager configureHeadlessFactoryMode:]_block_invoke.73
- ___52-[NFHardwareManager refreshSecureElementsWithError:]_block_invoke.105
- ___53-[NFConnectionHandoverReceiver _processRetryRequest:]_block_invoke.438
- ___53-[NFConnectionHandoverReceiver _startWithAutoResume:]_block_invoke
- ___53-[NFConnectionHandoverReceiver _startWithAutoResume:]_block_invoke_2
- ___54-[NFConnectionHandoverInitiator send:responseHandler:]_block_invoke.205
- ___54-[NFConnectionHandoverInitiator send:responseHandler:]_block_invoke.207
- ___54-[NFConnectionHandoverInitiator send:responseHandler:]_block_invoke_2.208
- ___54-[NFConnectionHandoverReceiver _emuAssertTimerExpired]_block_invoke.408
- ___54-[NFSecureElementManagerSession powerCycleSEID:error:]_block_invoke.113
- ___56-[NFHardwareManager updateHWSupportWithXPC:waitForInit:]_block_invoke.45
- ___56-[NFHardwareManager updateHWSupportWithXPC:waitForInit:]_block_invoke.46
- ___56-[NFHardwareManager updateHWSupportWithXPC:waitForInit:]_block_invoke.49
- ___56-[NFRemoteAdminManager queueServerConnectionForApplets:]_block_invoke.89
- ___56-[NFSecureElementManagerSession deleteAllApplets:error:]_block_invoke.54
- ___56-[NFSecureElementManagerSession getAndResetLPEMCounter:]_block_invoke.90
- ___57-[NFHardwareManager _startFieldDetectSession:completion:]_block_invoke.123
- ___57-[NFHardwareManager checkExpressPassCompatibility:error:]_block_invoke.71
- ___57-[NFHardwareManager startSinglePollExpressModeAssertion:]_block_invoke.82
- ___57-[NFReaderSession(Private) runScript:parameters:results:]_block_invoke.269
- ___57-[NFRemoteAdminManager deleteAllAppletsAndCleanupWithTSM]_block_invoke.107
- ___57-[NFRemoteAdminManager ingestCard:withCompletionHandler:]_block_invoke.99
- ___57-[NFSecureElementManagerSession expressModeControlState:]_block_invoke.94
- ___57-[NFSecureElementManagerSession felicaAppletState:error:]_block_invoke.84
- ___58-[NFConnectionHandoverReceiver hceSession:didReceiveAPDU:]_block_invoke.452
- ___58-[NFHardwareManager releaseSinglePollExpressModeAssertion]_block_invoke.83
- ___58-[NFSecureElementManagerSession dumpDomain:forSEID:error:]_block_invoke.112
- ___58-[NFSecureElementManagerSession transitAppletState:error:]_block_invoke.86
- ___60-[NFSecureElementManagerSession getAttackLogPresence:error:]_block_invoke.110
- ___60-[NFSecureElementManagerSession refreshSecureElement:error:]_block_invoke.108
- ___61-[NFConnectionHandoverInitiator readerSession:didDetectTags:]_block_invoke.236
- ___61-[NFConnectionHandoverInitiator readerSession:didDetectTags:]_block_invoke.239
- ___61-[NFHardwareManager cachedEmbeddedSecureElementSerialNumber:]_block_invoke.104
- ___61-[NFSecureElementManagerSession didExitRestrictedMode:error:]_block_invoke.99
- ___61-[NFSecureElementManagerSession setExpressModesControlState:]_block_invoke.74
- ___62-[NFSecureElementManagerSession expressModesEnabledWithError:]_block_invoke.92
- ___63-[NFRemoteAdminManager setRegistrationInfo:primaryRegionTopic:]_block_invoke.81
- ___63-[NFSecureElementManagerSession getExpressPassConfigWithError:]_block_invoke.78
- ___63-[NFSecureElementManagerSession transceive:forSEID:toOS:error:]_block_invoke.101
- ___65-[NFHardwareManager actOnUserInitiatedSystemShutDown:completion:]_block_invoke.239
- ___66-[NFHardwareManager _synchronousQueueSessionWithRetry:queueBlock:]_block_invoke.109
- ___67-[NFSecureElementManagerSession expressAppletIdentifiersWithError:]_block_invoke.95
- ___68-[NFSecureElementManagerSession performPeerPaymentEnrollment:error:]_block_invoke.96
- ___68-[NFSecureElementManagerSession runScript:parameters:outputResults:]_block_invoke.105
- ___69-[NFConnectionHandoverInitiator sendHandoverRequest:responseHandler:]_block_invoke.197
- ___69-[NFConnectionHandoverInitiator sendHandoverRequest:responseHandler:]_block_invoke.201
- ___71-[NFSecureElementManagerSession getCryptogram:challengeResponse:error:]_block_invoke.57
- ___71-[NFSecureElementManagerSession getServiceProviderDataForApplet:error:]_block_invoke.87
- ___71-[NFSecureElementManagerSession transceiveMultiple:forSEID:toOS:error:]_block_invoke.103
- ___72-[NFSecureElementManagerSession validateSEPairings:outSEPairingVersion:]_block_invoke.55
- ___74-[NFRemoteAdminManager connectToServer:initialClientRequestInfo:callback:]_block_invoke.87
- ___75-[NFConnectionHandoverReceiver sendHandoverSelect:delay:completionHandler:]_block_invoke.415
- ___75-[NFConnectionHandoverReceiver sendHandoverSelect:delay:completionHandler:]_block_invoke.418
- ___75-[NFConnectionHandoverReceiver sendHandoverSelect:delay:completionHandler:]_block_invoke.420
- ___75-[NFConnectionHandoverReceiver sendHandoverSelect:delay:completionHandler:]_block_invoke_2.421
- ___75-[NFConnectionHandoverReceiver sendHandoverSelect:delay:completionHandler:]_block_invoke_3.422
- ___75-[NFSecureElementManagerSession setExpressPassConfig:restoreAuthorization:]_block_invoke.77
- ___76-[NFSecureElementManagerSession restoreAuthorizarionForKeys:onApplet:error:]_block_invoke.80
- ___77-[NFSecureElementManagerSession disableAuthorizationForPasses:authorization:]_block_invoke.83
- ___78-[NFHardwareManager startNdefTagSessionWithBluetoothLESecureOOBData:callback:]_block_invoke.179
- ___79-[NFConnectionHandoverInitiator readerSession:externalReaderFieldNotification:]_block_invoke.247
- ___79-[NFConnectionHandoverReceiver _processDisconnectWithPossibleDiscoveryRestart:]_block_invoke.442
- ___79-[NFSecureElementManagerSession restoreAuthorizationForAllAppletsExcept:error:]_block_invoke.79
- ___82-[NFSecureElementManagerSession getAttackCounterLogForSEID:acknowledgeLogs:error:]_block_invoke.109
- ___85-[NFConnectionHandoverInitiator _processSelectRetry:originalRequest:responseHandler:]_block_invoke.194
- ___88-[NFSecureElementManagerSession getServiceProviderDataForApplet:publicKey:scheme:error:]_block_invoke.89
- ___91-[NFSecureElementManagerSession disableAuthorizationForApplets:andKey:authorization:error:]_block_invoke.82
- ___Block_byref_object_copy_.403
- ___Block_byref_object_dispose_.404
- ___block_literal_global.229
- ___block_literal_global.234
- ___block_literal_global.237
- ___block_literal_global.298
- ___block_literal_global.32
- ___block_literal_global.35
- ___block_literal_global.82
- __unnamed_array_storage.141
- __unnamed_array_storage.143
- __unnamed_array_storage.144
- _objc_msgSend$_start
- _objc_msgSend$_startWithAutoResume:
- _objc_msgSend$felicaStateForSystemCode:withRequestService:withBlockReadList:performSearchServiceCode:completion:
- _objc_msgSend$getLPEMBluetoothLogWithCompletion:
- _objc_msgSend$sharedXPC
CStrings:
+ "\x02\x15"
+ "\x03\x13\"\x12"
+ "%c[%{public}s %{public}s]:%i Assume random in detected version %{public}d"
+ "%c[%{public}s %{public}s]:%i Contains undefined RFU bits but existing feature definition matches"
+ "%c[%{public}s %{public}s]:%i Fail to decode: %@"
+ "%c[%{public}s %{public}s]:%i Failed to encode: %@"
+ "%c[%{public}s %{public}s]:%i Unexpected parameter: %@"
+ "%c[%{public}s %{public}s]:%i autoResume=%{public}d, customBroadcast=%{public}@"
+ "%c[%{public}s %{public}s]:%i customBroadcast=%{public}@"
+ "@"
+ "@\"NFXPCServiceClient\""
+ "B32@0:8C16B20^@24"
+ "Can't update broadcast data unless session is stopped"
+ "Invalid data length"
+ "Invalid data type"
+ "NFWalletPresentation"
+ "NFWalletPresentationInterface"
+ "NFXPCServiceClient"
+ "NFXPCServiceClientDelegate"
+ "PassKit foreground presentment intent"
+ "Presentment intent supression"
+ "Session ineligible"
+ "T@\"NSString\",?,R,C"
+ "TCC access denied"
+ "Tq,N,V_category"
+ "Unable to acquire XPC service"
+ "Vv28@0:8B16@?<v@?@\"NSError\"@\"NSDictionary\">20"
+ "Vv44@0:8@\"NSData\"16@\"NSArray\"24B32@?<v@?@\"NSDictionary\"@\"NSError\">36"
+ "Vv44@0:8@16@24B32@?36"
+ "XPC service client interrupted"
+ "XPC service client invalidated"
+ "_category"
+ "_detectFieldCallback"
+ "_detectTechnologyCallback"
+ "_ecpFrame"
+ "_enterFieldCallback"
+ "_exitFieldCallback"
+ "_exportedInterface"
+ "_exportedObject"
+ "_fieldPresent"
+ "_initCategoryWithType:"
+ "_remoteObjectInterface"
+ "_serviceName"
+ "_startWithAutoResume:customBroadcastData:"
+ "_startWithCustomBroadcastData:"
+ "_xpcClient"
+ "_xpcClientLock"
+ "archivedDataWithRootObject:requiringSecureCoding:error:"
+ "asXPCObject"
+ "bkgTagReadECPOverride"
+ "category"
+ "chRandomData"
+ "checkExpressPassCompatibilityDeprecated:callback:"
+ "com.apple.nfcd.wallet.presentation"
+ "controllerDidDetectPotentialInitiator:field:"
+ "deleteAllAppletsOfType:queueConnection:error:"
+ "deleteAllSPAppletsAndCleanupWithTSM"
+ "deleteAllSPAppletsAndCleanupWithTSMithCompletion:"
+ "deleteAllWalletAppletsAndCleanupWithTSM"
+ "deleteAllWalletAppletsAndCleanupWithTSMWithCompletion:"
+ "felicaStateForSystemCode:withRequestService:performSearchServiceCode:completion:"
+ "fieldNotificationFromXPCObject:"
+ "getAndClearLPEMBluetoothLogWithError:"
+ "getLPEMBluetoothLog:withCompletion:"
+ "initWithService:remoteObjectInterface:exportedInterface:exportedObject:"
+ "initWithService:remoteObjectInterface:exportedInterface:exportedObject:xpcDispatchQueue:"
+ "present"
+ "presentWithCompletion:"
+ "setCategory:"
+ "setWithObjects:"
+ "startAutoResumeOnFieldDisableWithCustomBroadcastData:"
+ "startWithCustomBroadcastData:"
+ "unarchivedArrayOfObjectsOfClasses:fromData:error:"
+ "v24@0:8q16"
+ "validateExpressPassCompatibilityWithConfig:outError:"
- "\x02\x11"
- "\x03\x13!\x12"
- "\x16"
- "@\"NFHardwareManagerXPC\""
- "NFHardwareManagerXPC"
- "NFHardwareManagerXPC interrupted"
- "NFHardwareManagerXPC invalidated"
- "NFHardwareManagerXPCDelegate"
- "Vv52@0:8@\"NSData\"16@\"NSArray\"24@\"NSArray\"32B40@?<v@?@\"NSDictionary\"@\"NSError\">44"
- "Vv52@0:8@16@24@32B40@?44"
- "_start"
- "_startWithAutoResume:"
- "felicaStateForSystemCode:withRequestService:withBlockReadList:performSearchServiceCode:completion:"
- "getLPEMBluetoothLogWithCompletion:"
- "sharedXPC"

```
