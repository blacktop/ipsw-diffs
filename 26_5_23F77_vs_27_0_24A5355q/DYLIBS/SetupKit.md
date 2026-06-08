## SetupKit

> `/System/Library/PrivateFrameworks/SetupKit.framework/SetupKit`

```diff

-830.22.0.0.0
-  __TEXT.__text: 0x2968c
-  __TEXT.__auth_stubs: 0x820
+900.25.0.0.0
+  __TEXT.__text: 0x28e78
   __TEXT.__objc_methlist: 0x2378
-  __TEXT.__const: 0x1ca
+  __TEXT.__const: 0x1d2
   __TEXT.__constg_swiftt: 0x28
   __TEXT.__swift5_typeref: 0x6
   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_types: 0x4
-  __TEXT.__gcc_except_tab: 0xf24
-  __TEXT.__cstring: 0x7428
+  __TEXT.__gcc_except_tab: 0xeec
+  __TEXT.__cstring: 0x762e
   __TEXT.__oslogstring: 0x113
-  __TEXT.__unwind_info: 0xa90
-  __TEXT.__objc_classname: 0x3eb
-  __TEXT.__objc_methname: 0x394d
-  __TEXT.__objc_methtype: 0xb69
-  __TEXT.__objc_stubs: 0x2ce0
-  __DATA_CONST.__got: 0x1e0
-  __DATA_CONST.__const: 0xf10
+  __TEXT.__unwind_info: 0xa10
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0xff0
   __DATA_CONST.__objc_classlist: 0x110
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xe68
+  __DATA_CONST.__objc_selrefs: 0xe88
   __DATA_CONST.__objc_superrefs: 0xb0
-  __DATA_CONST.__objc_arraydata: 0x30
-  __AUTH_CONST.__auth_got: 0x420
+  __DATA_CONST.__objc_arraydata: 0x48
+  __DATA_CONST.__got: 0x1e8
   __AUTH_CONST.__const: 0x7d8
   __AUTH_CONST.__cfstring: 0xb40
-  __AUTH_CONST.__objc_const: 0x4ba0
-  __AUTH_CONST.__objc_arrayobj: 0x90
-  __AUTH_CONST.__objc_intobj: 0x168
-  __AUTH.__objc_data: 0xaa0
+  __AUTH_CONST.__objc_const: 0x4c20
+  __AUTH_CONST.__objc_arrayobj: 0xa8
+  __AUTH_CONST.__objc_intobj: 0x1b0
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__data: 0x20
-  __DATA.__objc_ivar: 0x490
+  __DATA.__objc_ivar: 0x4a0
   __DATA.__data: 0xc90
   __DATA.__bss: 0x68
+  __DATA_DIRTY.__objc_data: 0xaa0
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 7A9C6D9A-3174-36A2-B2A3-F46FA07E4DB2
-  Functions: 952
-  Symbols:   3214
-  CStrings:  1853
+  UUID: 21E8EFDF-5B5C-386E-8234-BEDA2E11C0A9
+  Functions: 954
+  Symbols:   3233
+  CStrings:  981
 
Symbols:
+ -[SKSetupAppleIDSignInServer _bleServerAcceptConnection:]
+ -[SKSetupCaptiveNetworkJoinServer _bleServerAcceptConnection:]
+ -[SKSetupFieldDiagnosticsServer _bleServerAcceptConnection:]
+ -[SKSetupMacSetupServer _bleServerAcceptConnection:]
+ -[SKSetupOSUpdateServer _bleServerAcceptConnection:]
+ -[SKSetupSIMTransferServer _bleServerAcceptConnection:]
+ -[SKStepWiFiSetupServerCW _runJoinStart:tryNumber:maxTries:]
+ -[SKStepWiFiSetupServerCW _runScanStart:tryNumber:maxTries:]
+ GCC_except_table419
+ GCC_except_table457
+ GCC_except_table547
+ GCC_except_table752
+ GCC_except_table759
+ GCC_except_table766
+ GCC_except_table769
+ GCC_except_table803
+ GCC_except_table809
+ GCC_except_table813
+ GCC_except_table876
+ _OBJC_CLASS_$_NSSet
+ _OBJC_IVAR_$_SKStepWiFiSetupServerCW._joinMaxTries
+ _OBJC_IVAR_$_SKStepWiFiSetupServerCW._joinTryNumber
+ _OBJC_IVAR_$_SKStepWiFiSetupServerCW._scanMaxTries
+ _OBJC_IVAR_$_SKStepWiFiSetupServerCW._scanTryNumber
+ ___31-[SKStepWiFiSetupServerCW _run]_block_invoke
+ ___31-[SKStepWiFiSetupServerCW _run]_block_invoke_2
+ ___52-[SKSetupMacSetupServer _bleServerAcceptConnection:]_block_invoke
+ ___52-[SKSetupOSUpdateServer _bleServerAcceptConnection:]_block_invoke
+ ___55-[SKSetupSIMTransferServer _bleServerAcceptConnection:]_block_invoke
+ ___57-[SKSetupAppleIDSignInServer _bleServerAcceptConnection:]_block_invoke
+ ___60-[SKSetupFieldDiagnosticsServer _bleServerAcceptConnection:]_block_invoke
+ ___60-[SKStepWiFiSetupServerCW _runJoinStart:tryNumber:maxTries:]_block_invoke
+ ___60-[SKStepWiFiSetupServerCW _runJoinStart:tryNumber:maxTries:]_block_invoke_2
+ ___60-[SKStepWiFiSetupServerCW _runScanStart:tryNumber:maxTries:]_block_invoke
+ ___60-[SKStepWiFiSetupServerCW _runScanStart:tryNumber:maxTries:]_block_invoke.101
+ ___62-[SKSetupCaptiveNetworkJoinServer _bleServerAcceptConnection:]_block_invoke
+ ___73-[SKConnection _sendRequestID:request:options:sendEntry:responseHandler:]_block_invoke.225
+ ___77-[SKSetupCaptiveNetworkJoinServer _networkRelaySetupRequest:responseHandler:]_block_invoke.191
+ ___77-[SKSetupCaptiveNetworkJoinServer _networkRelaySetupRequest:responseHandler:]_block_invoke_2.193
+ ___Block_byref_object_copy_.1504
+ ___Block_byref_object_copy_.1755
+ ___Block_byref_object_copy_.2197
+ ___Block_byref_object_copy_.247
+ ___Block_byref_object_copy_.425
+ ___Block_byref_object_copy_.598
+ ___Block_byref_object_copy_.84
+ ___Block_byref_object_copy_.908
+ ___Block_byref_object_dispose_.1505
+ ___Block_byref_object_dispose_.1756
+ ___Block_byref_object_dispose_.2198
+ ___Block_byref_object_dispose_.248
+ ___Block_byref_object_dispose_.426
+ ___Block_byref_object_dispose_.599
+ ___Block_byref_object_dispose_.85
+ ___Block_byref_object_dispose_.909
+ ___block_descriptor_60_e8_32s40r_e5_v8?0lr40l8s32l8
+ ___block_literal_global.1053
+ ___block_literal_global.108
+ ___block_literal_global.1106
+ ___block_literal_global.1151
+ ___block_literal_global.132
+ ___block_literal_global.153
+ ___block_literal_global.16.2493
+ ___block_literal_global.1643
+ ___block_literal_global.1874
+ ___block_literal_global.19.1876
+ ___block_literal_global.195
+ ___block_literal_global.202
+ ___block_literal_global.21.1878
+ ___block_literal_global.23.1050
+ ___block_literal_global.23.1880
+ ___block_literal_global.235
+ ___block_literal_global.2353
+ ___block_literal_global.2395
+ ___block_literal_global.242
+ ___block_literal_global.2500
+ ___block_literal_global.254
+ ___block_literal_global.282
+ ___block_literal_global.286
+ ___block_literal_global.339
+ ___block_literal_global.34.1852
+ ___block_literal_global.342
+ ___block_literal_global.361
+ ___block_literal_global.44
+ ___block_literal_global.46
+ ___block_literal_global.47.1857
+ ___block_literal_global.497
+ ___block_literal_global.50.1846
+ ___block_literal_global.53.1843
+ ___block_literal_global.643
+ ___block_literal_global.75
+ ___block_literal_global.78
+ ___block_literal_global.899
+ ___block_literal_global.93
+ ___block_literal_global.97
+ ___block_literal_global.984
+ ___logger_block_invoke.2374
+ _dispatch_after
+ _dispatch_time
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$_bleServerAcceptConnection:
+ _objc_msgSend$_runJoinStart:tryNumber:maxTries:
+ _objc_msgSend$_runScanStart:tryNumber:maxTries:
+ _objc_msgSend$setIncludeProperties:
+ _objc_msgSend$setWithArray:
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x8
+ _objc_retain_x9
+ _sCUOSLogCreateOnce_logger.2354
+ _sCUOSLogHandle_logger.2355
- -[SKSetupAppleIDSignInServer _bleServerAcceptConnecton:]
- -[SKSetupCaptiveNetworkJoinServer _bleServerAcceptConnecton:]
- -[SKSetupFieldDiagnosticsServer _bleServerAcceptConnecton:]
- -[SKSetupMacSetupServer _bleServerAcceptConnecton:]
- -[SKSetupOSUpdateServer _bleServerAcceptConnecton:]
- -[SKSetupSIMTransferServer _bleServerAcceptConnecton:]
- -[SKStepWiFiSetupServerCW _runJoinStart:]
- -[SKStepWiFiSetupServerCW _runScanStart:]
- GCC_except_table417
- GCC_except_table455
- GCC_except_table545
- GCC_except_table750
- GCC_except_table757
- GCC_except_table764
- GCC_except_table767
- GCC_except_table801
- GCC_except_table807
- GCC_except_table811
- GCC_except_table874
- ___41-[SKStepWiFiSetupServerCW _runJoinStart:]_block_invoke
- ___41-[SKStepWiFiSetupServerCW _runJoinStart:]_block_invoke_2
- ___41-[SKStepWiFiSetupServerCW _runScanStart:]_block_invoke
- ___41-[SKStepWiFiSetupServerCW _runScanStart:]_block_invoke_2
- ___51-[SKSetupMacSetupServer _bleServerAcceptConnecton:]_block_invoke
- ___51-[SKSetupOSUpdateServer _bleServerAcceptConnecton:]_block_invoke
- ___54-[SKSetupSIMTransferServer _bleServerAcceptConnecton:]_block_invoke
- ___56-[SKSetupAppleIDSignInServer _bleServerAcceptConnecton:]_block_invoke
- ___59-[SKSetupFieldDiagnosticsServer _bleServerAcceptConnecton:]_block_invoke
- ___61-[SKSetupCaptiveNetworkJoinServer _bleServerAcceptConnecton:]_block_invoke
- ___73-[SKConnection _sendRequestID:request:options:sendEntry:responseHandler:]_block_invoke.226
- ___77-[SKSetupCaptiveNetworkJoinServer _networkRelaySetupRequest:responseHandler:]_block_invoke.192
- ___77-[SKSetupCaptiveNetworkJoinServer _networkRelaySetupRequest:responseHandler:]_block_invoke_2.194
- ___Block_byref_object_copy_.1517
- ___Block_byref_object_copy_.1762
- ___Block_byref_object_copy_.2181
- ___Block_byref_object_copy_.244
- ___Block_byref_object_copy_.430
- ___Block_byref_object_copy_.605
- ___Block_byref_object_copy_.85
- ___Block_byref_object_copy_.912
- ___Block_byref_object_dispose_.1518
- ___Block_byref_object_dispose_.1763
- ___Block_byref_object_dispose_.2182
- ___Block_byref_object_dispose_.245
- ___Block_byref_object_dispose_.431
- ___Block_byref_object_dispose_.606
- ___Block_byref_object_dispose_.86
- ___Block_byref_object_dispose_.913
- ___block_literal_global.1057
- ___block_literal_global.109
- ___block_literal_global.1108
- ___block_literal_global.1153
- ___block_literal_global.133
- ___block_literal_global.154
- ___block_literal_global.16.2478
- ___block_literal_global.1657
- ___block_literal_global.1868
- ___block_literal_global.19.1870
- ___block_literal_global.196
- ___block_literal_global.203
- ___block_literal_global.21.1872
- ___block_literal_global.23.1054
- ___block_literal_global.23.1874
- ___block_literal_global.2340
- ___block_literal_global.236
- ___block_literal_global.2382
- ___block_literal_global.243
- ___block_literal_global.2486
- ___block_literal_global.251
- ___block_literal_global.283
- ___block_literal_global.287
- ___block_literal_global.337
- ___block_literal_global.34.1846
- ___block_literal_global.343
- ___block_literal_global.362
- ___block_literal_global.45
- ___block_literal_global.45.1110
- ___block_literal_global.47.1851
- ___block_literal_global.496
- ___block_literal_global.50.1840
- ___block_literal_global.53.1837
- ___block_literal_global.651
- ___block_literal_global.76
- ___block_literal_global.79
- ___block_literal_global.903
- ___block_literal_global.95
- ___block_literal_global.98
- ___block_literal_global.989
- ___logger_block_invoke.2361
- _objc_msgSend$_bleServerAcceptConnecton:
- _objc_release_x10
- _objc_retain_x27
- _objc_retain_x28
- _sCUOSLogCreateOnce_logger.2341
- _sCUOSLogHandle_logger.2342
CStrings:
+ "### Join start failed: channel=%d, try=%d/%d, error=%@"
+ "### Scan start failed: channel=%d, try=%d/%d, error=%@"
+ "-[SKSetupAppleIDSignInServer _bleServerAcceptConnection:]"
+ "-[SKSetupCaptiveNetworkJoinServer _bleServerAcceptConnection:]"
+ "-[SKSetupFieldDiagnosticsServer _bleServerAcceptConnection:]"
+ "-[SKSetupMacSetupServer _bleServerAcceptConnection:]"
+ "-[SKSetupSIMTransferServer _bleServerAcceptConnection:]"
+ "-[SKStepWiFiSetupServerCW _runJoinStart:tryNumber:maxTries:]"
+ "-[SKStepWiFiSetupServerCW _runJoinStart:tryNumber:maxTries:]_block_invoke"
+ "-[SKStepWiFiSetupServerCW _runJoinStart:tryNumber:maxTries:]_block_invoke_2"
+ "-[SKStepWiFiSetupServerCW _runScanStart:tryNumber:maxTries:]"
+ "-[SKStepWiFiSetupServerCW _runScanStart:tryNumber:maxTries:]_block_invoke"
+ "Delaying before join retry: 1 second"
+ "Delaying before scan retry: 1 second"
+ "Join SSID '%@...', channel %d, EAP %s/%s, PW %s, PSK %s, Home %s, try=%d/%d"
+ "JoinNoChannelDelay"
+ "Scan: channel=%d, try=%d/%d"
+ "ScanNoChannelDelay"
+ "\xf0\xd1"
- "#16@0:8"
- "-[SKSetupAppleIDSignInServer _bleServerAcceptConnecton:]"
- "-[SKSetupCaptiveNetworkJoinServer _bleServerAcceptConnecton:]"
- "-[SKSetupFieldDiagnosticsServer _bleServerAcceptConnecton:]"
- "-[SKSetupMacSetupServer _bleServerAcceptConnecton:]"
- "-[SKSetupSIMTransferServer _bleServerAcceptConnecton:]"
- "-[SKStepWiFiSetupServerCW _runJoinStart:]"
- "-[SKStepWiFiSetupServerCW _runJoinStart:]_block_invoke"
- "-[SKStepWiFiSetupServerCW _runJoinStart:]_block_invoke_2"
- "-[SKStepWiFiSetupServerCW _runScanStart:]"
- "-[SKStepWiFiSetupServerCW _runScanStart:]_block_invoke"
- ".cxx_destruct"
- "@"
- "@\"<CUMessaging>\""
- "@\"<CUMessaging>\"16@0:8"
- "@\"<CUReadWriteRequestable>\""
- "@\"CBAdvertiser\""
- "@\"CBConnection\""
- "@\"CBServer\""
- "@\"CUBonjourAdvertiser\""
- "@\"CUBonjourBrowser\""
- "@\"CUBonjourDevice\""
- "@\"CUEnvironment\""
- "@\"CUEnvironment\"16@0:8"
- "@\"CUMessageSession\""
- "@\"CUMessageSessionServer\""
- "@\"CUNANEndpoint\""
- "@\"CUNANPublisher\""
- "@\"CUNANSubscriber\""
- "@\"CUPairingSession\""
- "@\"CUPairingStream\""
- "@\"CUReachabilityMonitor\""
- "@\"CWFActivity\""
- "@\"CWFInterface\""
- "@\"CWFScanResult\""
- "@\"FLFollowUpController\""
- "@\"NRDeviceIdentifier\""
- "@\"NRDeviceManager\""
- "@\"NRDeviceMonitor\""
- "@\"NSData\""
- "@\"NSDictionary\""
- "@\"NSError\""
- "@\"NSMutableArray\""
- "@\"NSMutableDictionary\""
- "@\"NSNumber\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_dispatch_queue>\"16@0:8"
- "@\"NSObject<OS_dispatch_source>\""
- "@\"NSObject<SKStepable>\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSURL\""
- "@\"SKConnection\""
- "@\"SKDevice\""
- "@\"SKSetupBase\""
- "@\"SKSetupBase\"16@0:8"
- "@\"SKSetupCaptiveNetworkJoinServer\""
- "@16@0:8"
- "@20@0:8i16"
- "@24@0:8:16"
- "@24@0:8@16"
- "@24@0:8^{LogCategory=ii*I**i^{LogCategory}^{LogOutput}^{LogOutput}QQII*^{LogCategoryPrivate}}16"
- "@28@0:8i16@20"
- "@28@0:8i16I20i24"
- "@32@0:8:16@24"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "@64@0:8r^v16Q24r^v32Q40Q48^@56"
- "@?"
- "@?16@0:8"
- "@?<v@?>16@0:8"
- "@?<v@?@\"NSError\">16@0:8"
- "@?<v@?i@\"NSString\">16@0:8"
- "@?<v@?iIi>16@0:8"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B24@0:8^@16"
- "C16@0:8"
- "CUActivatable"
- "CUAuthenticatableClient"
- "CUAuthenticatableServer"
- "CUEnvironmentable"
- "CULabelable"
- "CUMessaging"
- "I"
- "I16@0:8"
- "NRDeviceMonitorDelegate"
- "NSObject"
- "Q16@0:8"
- "S"
- "S16@0:8"
- "SKAuthenticationPresentEvent"
- "SKAuthenticationRequestEvent"
- "SKAuthenticationResponseEvent"
- "SKCaptiveContext"
- "SKDevice"
- "SKEvent"
- "SKEventBasicConfigUpdated"
- "SKEventCaptiveNetworkPresent"
- "SKEventRegistration"
- "SKRequestEntry"
- "SKRequestRegistration"
- "SKSendEntry"
- "SKSetupBase"
- "SKStepable"
- "SSID"
- "T#,R"
- "T@\"<CUMessaging>\",&,N"
- "T@\"<CUMessaging>\",&,N,V_skMessaging"
- "T@\"CBConnection\",&,N,V_bleConnection"
- "T@\"CUEnvironment\",&,N"
- "T@\"CUEnvironment\",&,N,V_environment"
- "T@\"CUMessageSession\",R,N"
- "T@\"NSData\",C,N,V_authTagOverride"
- "T@\"NSData\",C,N,V_eventData"
- "T@\"NSData\",C,N,V_nearbyActionExtraData"
- "T@\"NSData\",C,N,V_pskData"
- "T@\"NSDictionary\",C,N,V_clientConfig"
- "T@\"NSDictionary\",C,N,V_options"
- "T@\"NSDictionary\",C,N,V_outClientConfig"
- "T@\"NSDictionary\",C,N,V_outServerConfig"
- "T@\"NSDictionary\",C,N,V_request"
- "T@\"NSDictionary\",C,N,V_serverConfig"
- "T@\"NSDictionary\",R,C,N,V_basicConfig"
- "T@\"NSError\",R,C,N,V_error"
- "T@\"NSNumber\",&,N,V_xidObj"
- "T@\"NSObject<OS_dispatch_queue>\",&,N"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_dispatchQueue"
- "T@\"NSObject<OS_dispatch_source>\",&,N,V_timer"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",C,N"
- "T@\"NSString\",C,N,V_eventID"
- "T@\"NSString\",C,N,V_identifier"
- "T@\"NSString\",C,N,V_label"
- "T@\"NSString\",C,N,V_password"
- "T@\"NSString\",C,N,V_requestID"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,C,N,V_captiveInterfaceIdentifier"
- "T@\"NSString\",R,C,N,V_captiveSSID"
- "T@\"NSString\",R,C,N,V_password"
- "T@\"NSURL\",R,C,N,V_captiveURL"
- "T@\"SKDevice\",&,N,V_blePeerDevice"
- "T@\"SKDevice\",&,N,V_peerDevice"
- "T@\"SKSetupBase\",W,N"
- "T@\"SKSetupBase\",W,N,V_skSetupObject"
- "T@\"SKSetupCaptiveNetworkJoinServer\",&,N,V_server"
- "T@?,C,N"
- "T@?,C,N,V_authCompletionHandler"
- "T@?,C,N,V_authHidePasswordHandler"
- "T@?,C,N,V_authPromptHandler"
- "T@?,C,N,V_authShowPasswordHandler"
- "T@?,C,N,V_completion"
- "T@?,C,N,V_errorHandler"
- "T@?,C,N,V_eventHandler"
- "T@?,C,N,V_handler"
- "T@?,C,N,V_invalidationHandler"
- "T@?,C,N,V_overallCompletionHandler"
- "T@?,C,N,V_pairSetupConfigHandler"
- "T@?,C,N,V_passwordTypeChangedHandler"
- "T@?,C,N,V_receivedEventHandler"
- "T@?,C,N,V_receivedRequestHandler"
- "T@?,C,N,V_responseHandler"
- "T@?,C,N,V_sendDataHandler"
- "T@?,C,N,V_skCompletionHandler"
- "T@?,C,N,V_stateChangedHandler"
- "TB,N,V_clientMode"
- "TB,N,V_conditionalPersistent"
- "TB,N,V_persistentPairing"
- "TB,N,V_preventAppleWiFi"
- "TB,N,V_reversePairing"
- "TB,N,V_skipWifi"
- "TB,N,V_useSecondTrigger"
- "TC,N,V_nearbyActionType"
- "TI,N,V_bluetoothUseCase"
- "TI,N,V_controlFlags"
- "TI,N,V_xid"
- "TI,R,N,V_pairingFlags"
- "TQ,N,V_queueTicks"
- "TQ,N,V_sendTicks"
- "TQ,R"
- "TS,N,V_blePSM"
- "Td,R,N,V_metricTotalSeconds"
- "Td,R,N,V_metricWiFiSetupSeconds"
- "Ti,N"
- "Ti,N,V_mode"
- "Ti,N,V_passwordType"
- "Ti,N,V_setupType"
- "Ti,N,V_state"
- "Ti,R,N,V_eventType"
- "Ti,R,N,V_passwordType"
- "Ti,R,N,V_throttleSeconds"
- "UTF8String"
- "Vv16@0:8"
- "^{LogCategory=ii*I**i^{LogCategory}^{LogOutput}^{LogOutput}QQII*^{LogCategoryPrivate}}"
- "^{_NSZone=}16@0:8"
- "^{__WiFiManagerClient=}"
- "_abortRequestsWithError:"
- "_activate"
- "_activateBLEWithCompletion:"
- "_activateCalled"
- "_activateCompletion"
- "_activateNANContinueWithError:"
- "_activateNANWithCompletion:"
- "_activateOOBWithCompletion:"
- "_activateWithCompletion:"
- "_addStep:"
- "_authCompletionHandler"
- "_authHidePasswordHandler"
- "_authPromptHandler"
- "_authShowPasswordHandler"
- "_authTagOverride"
- "_authThrottleDeadlineTicks"
- "_authThrottleTimer"
- "_awdlAdvertiser"
- "_awdlAdvertiserPeerStarted"
- "_awdlBrowser"
- "_awdlName"
- "_awdlPeerDevice"
- "_awdlTimer"
- "_basicConfig"
- "_bleAdvertisePSM"
- "_bleAdvertiser"
- "_bleAdvertiserEnsureStarted"
- "_bleAdvertiserEnsureStopped"
- "_bleAdvertiserShouldRun"
- "_bleConnection"
- "_blePSM"
- "_blePeerDevice"
- "_bleServer"
- "_bleServerAcceptConnecton:"
- "_bleServerEnsureStarted"
- "_bleServerEnsureStopped"
- "_bluetoothUseCase"
- "_bonjourAdvertiser"
- "_bonjourBrowser"
- "_bonjourTestID"
- "_bonjourTimeoutTimer"
- "_bonjourTimer"
- "_captiveDetectedNotificationUpdate:"
- "_captiveDetectedNotifyToken"
- "_captiveInterfaceIdentifier"
- "_captiveNetworkCookie"
- "_captiveNetworkIPAssign:"
- "_captiveNetworkInterfaceName"
- "_captiveNetworkLoginDone"
- "_captiveNetworkLoginInfo:cookie:responseHandler:"
- "_captiveNetworkLoginRequest:responseHandler:"
- "_captiveNetworkProbeEnsureStopped"
- "_captiveNetworkProbeRequest:responseHandler:"
- "_captiveNetworkProbeResult:responseHandler:"
- "_captiveNetworkProbingSuccess"
- "_captiveNetworkWebSheetActive"
- "_captiveNetworkWebSheetCompleted"
- "_captiveProbeRequest"
- "_captiveProbeResponse:"
- "_captiveSSID"
- "_captiveURL"
- "_cfuCleared"
- "_cfuController"
- "_cfuEnsuredStarted"
- "_cfuEnsuredStopped"
- "_clientConfig"
- "_clientConnectCompleted:"
- "_clientConnectStart"
- "_clientConnectStartBLE"
- "_clientError:"
- "_clientMode"
- "_clientPairSetupCompleted:"
- "_clientPairSetupContinueWithData:"
- "_clientPairSetupPromptWithFlags:passwordType:throttleSeconds:"
- "_clientPairSetupStart"
- "_clientPairSetupStartReverse"
- "_clientPairVerifyCompleted:"
- "_clientPairVerifyStart"
- "_clientPairVerifyWithData:"
- "_clientRun"
- "_completeWithError:"
- "_completed"
- "_completedStep:error:"
- "_completion"
- "_conditionalPersistent"
- "_connectionEnded:"
- "_connectionStartWithSKConnection:clientMode:completeOnFailure:completion:"
- "_controlFlags"
- "_dispatchQueue"
- "_environment"
- "_error"
- "_errorHandler"
- "_eventData"
- "_eventHandler"
- "_eventID"
- "_eventType"
- "_frameHeader"
- "_handleAcceptBLEConnection:"
- "_handleAcceptCommon:"
- "_handleAcceptNANData:endpoint:"
- "_handleRequestBasicConfig:responseHandler:"
- "_handleRequestBonjourTestDone:responseHandler:"
- "_handleRequestBonjourTestStart:responseHandler:"
- "_handleRequestWiFiSetup:responseHandler:"
- "_handler"
- "_identifier"
- "_internetReachabilityEnabled"
- "_internetReachabilityMonitor"
- "_invalidate"
- "_invalidateCalled"
- "_invalidateCore"
- "_invalidateCore:"
- "_invalidateDone"
- "_invalidateSteps"
- "_invalidateWithError:"
- "_invalidated"
- "_invalidationHandler"
- "_label"
- "_mainAuthTagLength"
- "_mainStream"
- "_messageSessionServer"
- "_messageSessionTemplate"
- "_metricTotalSeconds"
- "_metricWiFiSetupSeconds"
- "_mode"
- "_nanEndpoint"
- "_nanEndpointID"
- "_nanPublisher"
- "_nanPublisherEnsureStarted"
- "_nanPublisherEnsureStopped"
- "_nanSubscriber"
- "_nearbyActionExtraData"
- "_nearbyActionType"
- "_networkRelayAWDLStartRequest:responseHandler:"
- "_networkRelayDeviceEnsureStopped"
- "_networkRelayEnsureStopped"
- "_networkRelayPeerIPStr"
- "_networkRelayProxyInterface"
- "_networkRelaySetupRequest:responseHandler:"
- "_networkRelayTimer"
- "_nrDeviceIdentifier"
- "_nrDeviceManager"
- "_nrDeviceMonitor"
- "_oobEnsureStarted"
- "_options"
- "_outClientConfig"
- "_outServerConfig"
- "_overallCompletionHandler"
- "_pairSetupConfig:"
- "_pairSetupConfigHandler"
- "_pairSetupInvalidate"
- "_pairSetupSession"
- "_pairVerifyInvalidate"
- "_pairVerifySession"
- "_pairingFlags"
- "_password"
- "_passwordType"
- "_passwordTypeChangedHandler"
- "_peerDevice"
- "_persistentPairing"
- "_postEvent:"
- "_prepareSteps"
- "_prepareStepsOSRecovery"
- "_preventAppleWiFi"
- "_processSends"
- "_pskData"
- "_pskPrepareClientMode:"
- "_queueTicks"
- "_readRequested"
- "_receiveCompletion:"
- "_receiveStart:"
- "_receivedEvent:"
- "_receivedEventHandler"
- "_receivedEventID:event:options:"
- "_receivedHeader:body:"
- "_receivedHeader:encryptedObjectData:"
- "_receivedHeader:unencryptedObjectData:"
- "_receivedObject:"
- "_receivedRequest:"
- "_receivedRequestHandler"
- "_receivedRequestID:request:options:responseHandler:"
- "_receivedResponse:"
- "_receivingHeader"
- "_registeredEvents"
- "_registeredRequests"
- "_reportEvent:"
- "_reportEventType:"
- "_request"
- "_requestID"
- "_requestable"
- "_requests"
- "_responseHandler"
- "_responseReceived"
- "_reversePairing"
- "_run"
- "_runAWDLFoundDevice:"
- "_runAWDLFoundTimerStart"
- "_runAWDLStart"
- "_runBasicConfigStart"
- "_runCaptiveNetworkLoginResponse:"
- "_runCaptiveNetworkLoginStart"
- "_runDefault"
- "_runDetected"
- "_runInit"
- "_runInternetReachabilityStart"
- "_runJoinStart:"
- "_runNetworkRelayPeerStart"
- "_runNetworkRelaySelfStart"
- "_runScanResults:error:channel:"
- "_runScanStart:"
- "_runState"
- "_runSteps"
- "_runUserRequest"
- "_runWiFiSetupStart"
- "_scanResult"
- "_sendArray"
- "_sendDataHandler"
- "_sendEventID:data:xid:options:completion:"
- "_sendFrameType:body:"
- "_sendFrameType:unencryptedObject:"
- "_sendHeaderData:bodyData:completion:"
- "_sendRequestID:request:options:sendEntry:responseHandler:"
- "_sendResponse:error:xid:requestID:completion:"
- "_sendTicks"
- "_server"
- "_serverAccept"
- "_serverAcceptBLE"
- "_serverConfig"
- "_serverError:"
- "_serverPairSetupCompleted:"
- "_serverPairSetupContinueWithData:start:"
- "_serverPairVerifyCompleted:"
- "_serverPairVerifyContinueWithData:start:"
- "_serverRun"
- "_setupConnectionCommon:"
- "_setupMessageSession"
- "_setupType"
- "_showPasswordCalled"
- "_skCnx"
- "_skCompletionHandler"
- "_skMessaging"
- "_skSetupObject"
- "_skipWifi"
- "_startBonjourTestTicks"
- "_startTicks"
- "_startTimer"
- "_state"
- "_stateChangedHandler"
- "_stepArray"
- "_stepCurrent"
- "_stepDone"
- "_stepError"
- "_tearDownMessageSession"
- "_throttleSeconds"
- "_timeoutForSendEntry:"
- "_timeoutForXID:"
- "_timeoutTimer"
- "_timer"
- "_ucat"
- "_ucatBase"
- "_update"
- "_updateExternalState"
- "_useSecondTrigger"
- "_wifiChannel"
- "_wifiDirected"
- "_wifiEAPConfig"
- "_wifiEAPTrustExceptions"
- "_wifiHomeNetwork"
- "_wifiInterface"
- "_wifiKeepAliveActivity"
- "_wifiKeepAliveEnsureStarted"
- "_wifiKeepAliveEnsureStopped"
- "_wifiKeepAliveInterface"
- "_wifiManager"
- "_wifiPSK"
- "_wifiPassword"
- "_wifiSSID"
- "_xid"
- "_xidLast"
- "_xidObj"
- "activate"
- "activateWithCompletion:"
- "addObject:"
- "addStep:"
- "appendData:"
- "arrayWithObjects:count:"
- "associateWithParameters:reply:"
- "authCompletionHandler"
- "authHidePasswordHandler"
- "authPromptHandler"
- "authShowPasswordHandler"
- "authTagLength"
- "authTagOverride"
- "autorelease"
- "basicConfig"
- "bleConnection"
- "bleListeningPSM"
- "blePSM"
- "blePeerDevice"
- "bluetoothUseCase"
- "bufferData"
- "bundleWithIdentifier:"
- "bundleWithURL:"
- "bytes"
- "captiveInterfaceIdentifier"
- "captiveSSID"
- "captiveURL"
- "checkWiFiAndReturnError:"
- "class"
- "clearPendingFollowUpItemsWithUniqueIdentifiers:completion:"
- "clientConfig"
- "clientMode"
- "code"
- "completion"
- "conditionalPersistent"
- "conformsToProtocol:"
- "controlFlags"
- "copy"
- "copySharedDeviceManager"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "currentKnownNetworkProfile"
- "currentLocale"
- "d"
- "d16@0:8"
- "data"
- "dealloc"
- "debugDescription"
- "decryptData:aadBytes:aadLength:error:"
- "deregisterEventID:completionHandler:"
- "deregisterRequestID:completionHandler:"
- "deriveKeyWithSaltPtr:saltLen:infoPtr:infoLen:keyLen:error:"
- "deriveKeyWithSaltPtr:saltLen:infoPtr:infoLen:keyLen:outputKeyPtr:"
- "description"
- "descriptionWithLevel:"
- "deviceHasUnpairedBluetooth:"
- "deviceInfoDidChange:deviceInfo:"
- "deviceIsAsleepDidChange:isAsleep:"
- "deviceIsClassCConnectedDidChange:isClassCConnected:"
- "deviceIsCloudConnectedDidChange:isCloudConnected:"
- "deviceIsConnectedDidChange:isConnected:"
- "deviceIsEnabledDidChange:isEnabled:"
- "deviceIsNearbyDidChange:isNearby:"
- "deviceIsRegisteredDidChange:isRegistered:"
- "deviceLinkTypeDidChange:linkType:"
- "deviceLinkTypeDidChange:linkType:linkSubtype:"
- "devicePluggedInStateDidChange:pluggedIn:"
- "deviceProxyServiceInterfaceNameDidChange:interfaceName:"
- "deviceThermalPressureLevelDidChange:thermalPressureLevel:"
- "deviceUsesAPLDidChange:usesAPL:"
- "dictionary"
- "dictionaryWithObjects:forKeys:count:"
- "dispatchQueue"
- "encryptData:aadData:error:"
- "enumerateKeysAndObjectsUsingBlock:"
- "environment"
- "error"
- "errorHandler"
- "errorWithDomain:code:userInfo:"
- "eventData"
- "eventHandler"
- "eventID"
- "eventType"
- "firstObject"
- "flags"
- "handler"
- "hash"
- "i16@0:8"
- "identifier"
- "indexOfObject:"
- "init"
- "initFileURLWithPath:isDirectory:"
- "initWithBasicConfig:"
- "initWithBytes:length:"
- "initWithCaptiveURL:interfaceIdentifier:ssid:"
- "initWithClientIdentifier:"
- "initWithContentsOfFile:"
- "initWithDeviceIdentifier:delegate:queue:"
- "initWithDictionary:"
- "initWithEventType:"
- "initWithEventType:error:"
- "initWithLength:"
- "initWithLogCategory:"
- "initWithPassword:"
- "initWithPasswordType:pairingFlags:throttleSeconds:"
- "initWithPasswordType:password:"
- "initWithString:"
- "initWithUTF8String:"
- "invalidate"
- "invalidationHandler"
- "isConnected"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "label"
- "length"
- "linkSubtype"
- "linkType"
- "localeIdentifier"
- "localizations"
- "localizedStringForKey:value:table:"
- "messageSessionTemplate"
- "metricTotalSeconds"
- "metricWiFiSetupSeconds"
- "mode"
- "mutableBytes"
- "name"
- "nearbyActionExtraData"
- "nearbyActionFlags"
- "nearbyActionType"
- "networkName"
- "newEphemeralDeviceIdentifier"
- "nrDeviceIdentifier"
- "numberWithInt:"
- "numberWithUnsignedInt:"
- "numberWithUnsignedInteger:"
- "objectForKeyedSubscript:"
- "openStreamWithName:error:"
- "options"
- "outClientConfig"
- "outServerConfig"
- "overallCompletionHandler"
- "pairSetupConfigHandler"
- "pairingFlags"
- "passwordType"
- "passwordTypeChangedHandler"
- "pathForResource:ofType:inDirectory:forLocalization:"
- "peerDevice"
- "performScanWithParameters:reply:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "persistentPairing"
- "pinTypeActual"
- "popFirstObject"
- "postEvent:"
- "postEventType:"
- "postFollowUpItem:completion:"
- "preferredLanguages"
- "preferredLocalizationsFromArray:forPreferences:"
- "prepareWithName:isClient:pskData:error:"
- "preventAppleWiFi"
- "proxyServiceInterfaceName"
- "pskData"
- "queueTicks"
- "readWithRequest:"
- "receivedData:"
- "receivedEventHandler"
- "receivedRequestHandler"
- "registerDevice:properties:operationalproperties:queue:completionBlock:"
- "registerEventID:options:eventHandler:completionHandler:"
- "registerRequestID:options:requestHandler:completionHandler:"
- "release"
- "removeAllObjects"
- "removeObjectAtIndex:"
- "reportEvent:"
- "reportEventType:"
- "request"
- "requestID"
- "reset"
- "resetWithCompletionHandler:"
- "respondsToSelector:"
- "responseHandler"
- "retain"
- "retainCount"
- "reversePairing"
- "self"
- "sendDataHandler"
- "sendEventID:data:xid:options:completion:"
- "sendEventID:event:options:completion:"
- "sendEventID:eventMessage:options:completionHandler:"
- "sendMessageData:endpoint:completionHandler:"
- "sendRequestID:request:options:responseHandler:"
- "sendRequestID:requestMessage:options:responseHandler:"
- "sendTicks"
- "serverConfig"
- "setAcceptHandler:"
- "setActions:"
- "setAdvertiseFlags:"
- "setAllowedLinkSubtypes:"
- "setAllowedLinkTypes:"
- "setAuthCompletionHandler:"
- "setAuthHidePasswordHandler:"
- "setAuthPromptHandler:"
- "setAuthShowPasswordHandler:"
- "setAuthTagOverride:"
- "setAwdlAddressData:"
- "setBleConnection:"
- "setBleListenPSM:"
- "setBlePSM:"
- "setBlePeerDevice:"
- "setBluetoothUseCase:"
- "setChangeFlags:"
- "setChannel:"
- "setChannels:"
- "setClientConfig:"
- "setClientMode:"
- "setCompletion:"
- "setCompletionHandler:"
- "setConditionalPersistent:"
- "setConnectTimeoutSeconds:"
- "setConnectionFlags:"
- "setControlFlags:"
- "setDataArray:"
- "setDeregisterRequestHandler:"
- "setDeviceChangedHandler:"
- "setDeviceFoundHandler:"
- "setDispatchQueue:"
- "setDomain:"
- "setEndpointFoundHandler:"
- "setEnvironment:"
- "setErrorHandler:"
- "setEventData:"
- "setEventHandler:"
- "setEventID:"
- "setFixedPIN:"
- "setFlags:"
- "setGroupIdentifier:"
- "setHandler:"
- "setHidePINHandler:"
- "setIdentifier:"
- "setInterfaceName:"
- "setInvalidationHandler:"
- "setLabel:"
- "setLength:"
- "setMaxLength:"
- "setMinLength:"
- "setMode:"
- "setName:"
- "setNearbyActionAuthTagData:"
- "setNearbyActionExtraData:"
- "setNearbyActionFlags:"
- "setNearbyActionType:"
- "setObject:forKeyedSubscript:"
- "setOptions:"
- "setOutClientConfig:"
- "setOutOfBandKey:"
- "setOutServerConfig:"
- "setOverallCompletionHandler:"
- "setPairSetupConfigHandler:"
- "setPassword:"
- "setPasswordType:"
- "setPasswordTypeChangedHandler:"
- "setPeerDevice:"
- "setPersistentPairing:"
- "setPinType:"
- "setPort:"
- "setPreventAppleWiFi:"
- "setPromptForPINHandler:"
- "setProxyCapability:"
- "setProxyProviderRequiresWiFi:"
- "setPskData:"
- "setQueueTicks:"
- "setReceiveHandler:"
- "setReceivedEventHandler:"
- "setReceivedRequestHandler:"
- "setRegisterRequestHandler:"
- "setRequest:"
- "setRequestID:"
- "setResponseHandler:"
- "setReversePairing:"
- "setSSID:"
- "setScanResult:"
- "setSendDataHandler:"
- "setSendRequestHandler:"
- "setSendTicks:"
- "setServer:"
- "setServerConfig:"
- "setServiceType:"
- "setSessionType:"
- "setSetupType:"
- "setShowPINHandlerEx:"
- "setSkCompletionHandler:"
- "setSkMessaging:"
- "setSkSetupObject:"
- "setSkipWifi:"
- "setState:"
- "setStateChangedHandler:"
- "setTimeout:"
- "setTimer:"
- "setTitle:"
- "setTxtDictionary:"
- "setUniqueIdentifier:"
- "setUrl:"
- "setUseCase:"
- "setUseSecondTrigger:"
- "setXid:"
- "setXidObj:"
- "setupType"
- "skCompletionHandler"
- "skMessaging"
- "skSetupObject"
- "skipWifi"
- "state"
- "stateChangedHandler"
- "stringByAppendingString:"
- "stringWithUTF8String:"
- "subdataWithRange:"
- "superclass"
- "templateSession"
- "throttleSeconds"
- "timer"
- "tryPIN:"
- "tryPassword:"
- "unregisterDevice:"
- "unsignedIntValue"
- "updatePasswordType:"
- "useSecondTrigger"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8C16"
- "v20@0:8I16"
- "v20@0:8S16"
- "v20@0:8i16"
- "v24@0:8@\"<CUMessaging>\"16"
- "v24@0:8@\"CUEnvironment\"16"
- "v24@0:8@\"NRDeviceMonitor\"16"
- "v24@0:8@\"NSObject<OS_dispatch_queue>\"16"
- "v24@0:8@\"NSString\"16"
- "v24@0:8@\"SKSetupBase\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?>16"
- "v24@0:8@?<v@?@\"NSError\">16"
- "v24@0:8@?<v@?i@\"NSString\">16"
- "v24@0:8@?<v@?iIi>16"
- "v24@0:8Q16"
- "v28@0:8@\"NRDeviceMonitor\"16B24"
- "v28@0:8@\"NRDeviceMonitor\"16C24"
- "v28@0:8@\"NRDeviceMonitor\"16i24"
- "v28@0:8@16B24"
- "v28@0:8@16C24"
- "v28@0:8@16i24"
- "v28@0:8C16@20"
- "v28@0:8I16i20i24"
- "v28@0:8i16@?20"
- "v32@0:8@\"NRDeviceMonitor\"16@\"NRDeviceInfo\"24"
- "v32@0:8@\"NRDeviceMonitor\"16@\"NSString\"24"
- "v32@0:8@\"NRDeviceMonitor\"16C24C28"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSError\">24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v32@0:8@16C24C28"
- "v32@0:8r^{?=C[3C]}16@24"
- "v36@0:8@16@24i32"
- "v36@0:8@16I24@?28"
- "v40@0:8@16@24@32"
- "v40@0:8@16@24@?32"
- "v40@0:8@16B24B28@?32"
- "v48@0:8@\"NSString\"16@\"NSDictionary\"24@\"NSDictionary\"32@?<v@?@\"NSDictionary\"@\"NSDictionary\"@\"NSError\">40"
- "v48@0:8@\"NSString\"16@\"NSDictionary\"24@\"NSDictionary\"32@?<v@?@\"NSError\">40"
- "v48@0:8@\"NSString\"16@\"NSDictionary\"24@?<v@?@\"NSString\"@\"NSDictionary\"@\"NSDictionary\">32@?<v@?@\"NSError\">40"
- "v48@0:8@\"NSString\"16@\"NSDictionary\"24@?<v@?@\"NSString\"@\"NSDictionary\"@\"NSDictionary\"@?<v@?@\"NSDictionary\"@\"NSDictionary\"@\"NSError\"@?<v@?@\"NSError\">>>32@?<v@?@\"NSError\">40"
- "v48@0:8@16@24@32@?40"
- "v48@0:8@16@24@?32@?40"
- "v52@0:8@16@24I32@36@?44"
- "v56@0:8@16@24@32@40@?48"
- "writeWithRequest:"
- "xid"
- "xidObj"
- "zone"
- "{?=\"frameType\"C\"frameLen\"[3C]}"
- "\xf0\xb1"

```
