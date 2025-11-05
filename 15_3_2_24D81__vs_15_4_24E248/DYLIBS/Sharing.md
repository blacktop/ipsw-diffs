## Sharing

> `/System/Library/PrivateFrameworks/Sharing.framework/Versions/A/Sharing`

```diff

-2060.40.21.0.0
-  __TEXT.__text: 0x318074
-  __TEXT.__auth_stubs: 0x4360
-  __TEXT.__objc_methlist: 0xfa48
-  __TEXT.__cstring: 0x2ad45
-  __TEXT.__const: 0x1885c
-  __TEXT.__gcc_except_tab: 0x300c
-  __TEXT.__oslogstring: 0x93ce
-  __TEXT.__dlopen_cstrs: 0x398
+2060.50.171.1.2
+  __TEXT.__text: 0x30dd88
+  __TEXT.__auth_stubs: 0x43d0
+  __TEXT.__objc_methlist: 0x11b2c
+  __TEXT.__cstring: 0x2b245
+  __TEXT.__const: 0x1880c
+  __TEXT.__gcc_except_tab: 0x3150
+  __TEXT.__oslogstring: 0x970e
+  __TEXT.__dlopen_cstrs: 0x3f5
   __TEXT.__ustring: 0x18
-  __TEXT.__swift5_typeref: 0x6de3
+  __TEXT.__swift5_typeref: 0x6df5
   __TEXT.__constg_swiftt: 0x5a3c
   __TEXT.__swift5_reflstr: 0x2e4a
   __TEXT.__swift5_fieldmd: 0x54c4
   __TEXT.__swift5_builtin: 0x17c
   __TEXT.__swift5_assocty: 0xc98
-  __TEXT.__swift5_capture: 0x1954
+  __TEXT.__swift5_capture: 0x17d4
   __TEXT.__swift5_protos: 0x28
   __TEXT.__swift5_proto: 0x1738
   __TEXT.__swift5_types: 0x754
+  __TEXT.__swift_as_entry: 0x2bc
+  __TEXT.__swift_as_ret: 0x2c4
   __TEXT.__swift5_mpenum: 0xa8
-  __TEXT.__unwind_info: 0xb6b0
-  __TEXT.__eh_frame: 0xa1a8
-  __TEXT.__objc_classname: 0x1b4d
-  __TEXT.__objc_methname: 0x252fc
-  __TEXT.__objc_methtype: 0x520d
-  __TEXT.__objc_stubs: 0x14020
-  __DATA_CONST.__got: 0xff0
-  __DATA_CONST.__const: 0x2c88
-  __DATA_CONST.__objc_classlist: 0x768
+  __TEXT.__unwind_info: 0xb6d8
+  __TEXT.__eh_frame: 0xa398
+  __TEXT.__objc_classname: 0x1bae
+  __TEXT.__objc_methname: 0x25fe4
+  __TEXT.__objc_methtype: 0x5332
+  __TEXT.__objc_stubs: 0x14820
+  __DATA_CONST.__got: 0xfe8
+  __DATA_CONST.__const: 0x2c60
+  __DATA_CONST.__objc_classlist: 0x778
   __DATA_CONST.__objc_catlist: 0x28
-  __DATA_CONST.__objc_protolist: 0x2e0
+  __DATA_CONST.__objc_protolist: 0x2e8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7918
+  __DATA_CONST.__objc_selrefs: 0x7ef8
   __DATA_CONST.__objc_protorefs: 0x198
   __DATA_CONST.__objc_classrefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x500
-  __DATA_CONST.__objc_arraydata: 0x2e8
-  __AUTH_CONST.__auth_got: 0x21c8
-  __AUTH_CONST.__const: 0x12ca0
-  __AUTH_CONST.__cfstring: 0x10d80
-  __AUTH_CONST.__objc_const: 0x32370
-  __AUTH_CONST.__objc_intobj: 0x438
-  __AUTH_CONST.__objc_dictobj: 0x3e8
+  __DATA_CONST.__objc_superrefs: 0x510
+  __DATA_CONST.__objc_arraydata: 0x2f8
+  __AUTH_CONST.__auth_got: 0x2200
+  __AUTH_CONST.__const: 0x12860
+  __AUTH_CONST.__cfstring: 0x11380
+  __AUTH_CONST.__objc_const: 0x2f548
+  __AUTH_CONST.__objc_intobj: 0x450
+  __AUTH_CONST.__objc_dictobj: 0x410
   __AUTH_CONST.__objc_arrayobj: 0x78
-  __AUTH.__objc_data: 0x5db0
-  __AUTH.__data: 0x2a68
-  __DATA.__objc_ivar: 0x1f08
-  __DATA.__data: 0xa9b0
-  __DATA.__bss: 0x2eef0
+  __AUTH.__objc_data: 0x5db8
+  __AUTH.__data: 0x2a58
+  __DATA.__objc_ivar: 0x1f54
+  __DATA.__data: 0xaa10
+  __DATA.__bss: 0x2ef40
   __DATA.__common: 0x110
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/Combine.framework/Versions/A/Combine

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: B9104069-0F14-3BF8-882B-1145D90AD08B
-  Functions: 17522
-  Symbols:   20729
-  CStrings:  16369
+  UUID: 3B9149BA-2723-32B7-B4BB-0AAC7E3A5CF0
+  Functions: 18223
+  Symbols:   22388
+  CStrings:  16617
 
Symbols:
+ +[SFActivityAdvertiser sharedAdvertiser].cold.1
+ +[SFAuthenticationHintsProvider sharedInstance].cold.1
+ +[SFAutoUnlockManager userDefaults].cold.1
+ +[SFBLEClient sharedClient].cold.1
+ +[SFBLEDevice setRSSIEstimatorInfo:].cold.1
+ +[SFBLEDevice setRSSIEstimatorInfo:].cold.2
+ +[SFBLEDevice setRSSIEstimatorInfo:].cold.3
+ +[SFCollaborationItem collaborationItemForFileURL:itemProvider:activityItem:defaultCollaboration:managedFileURL:].cold.1
+ +[SFCollaborationItemInspector inspectActivityItemValue:activityItem:service:shouldInspectFiles:managedFileURL:isURLProviderSupported:].cold.1
+ +[SFCollaborationUserDefaults sharedDefaults].cold.1
+ +[SFCollaborationUtilities loadMetadataForFileURL:completionHandler:].cold.1
+ +[SFCollaborationUtilities requestSharedURLForCollaborationItem:collaborationService:completionHandler:].cold.4
+ +[SFCompanionManager serviceManager].cold.1
+ +[SFCompanionXPCManager initialize].cold.1
+ +[SFCompanionXPCManager sharedManager].cold.1
+ +[SFContinuityScanManager sharedManager].cold.1
+ +[SFDeviceAssetQuery deviceWantsH264].cold.1
+ +[SFHeadphoneProduct airPodsMax].cold.1
+ +[SFHeadphoneProduct airPodsPro].cold.1
+ +[SFHeadphoneProduct airPodsSecondGeneration].cold.1
+ +[SFHeadphoneProduct airPods].cold.1
+ +[SFHeadphoneProduct b453].cold.1
+ +[SFHeadphoneProduct b463].cold.1
+ +[SFHeadphoneProduct b465].cold.1
+ +[SFHeadphoneProduct b487].cold.1
+ +[SFHeadphoneProduct b494].cold.1
+ +[SFHeadphoneProduct b498].cold.1
+ +[SFHeadphoneProduct b507].cold.1
+ +[SFHeadphoneProduct b607].cold.1
+ +[SFHeadphoneProduct b688].cold.1
+ +[SFHeadphoneProduct b698].cold.1
+ +[SFHeadphoneProduct b768e].cold.1
+ +[SFHeadphoneProduct b768m].cold.1
+ +[SFHeadphoneProduct beatsFlex].cold.1
+ +[SFHeadphoneProduct beatsSoloPro].cold.1
+ +[SFHeadphoneProduct beatsSolo].cold.1
+ +[SFHeadphoneProduct beatsStudio].cold.1
+ +[SFHeadphoneProduct beatsX].cold.1
+ +[SFHeadphoneProduct powerBeats3].cold.1
+ +[SFHeadphoneProduct powerBeats4].cold.1
+ +[SFHeadphoneProduct powerBeatsPro].cold.1
+ +[SFShareSheetSessionModeTestingSnapshot supportsSecureCoding]
+ +[SFShareSheetSessionTestingSnapshot _itemDescriptions:match:]
+ +[SFShareSheetSessionTestingSnapshot _jsonifyItems:]
+ +[SFShareSheetSessionTestingSnapshot codableDataStringForItem:]
+ +[SFShareSheetSessionTestingSnapshot codableItemFromDescription:]
+ +[SFShareSheetSessionTestingSnapshot codableItemFromDescription:].cold.1
+ +[SFShareSheetSessionTestingSnapshot codableItemFromDescription:].cold.2
+ +[SFShareSheetSessionTestingSnapshot codableItemFromDescription:].cold.3
+ +[SFShareSheetSessionTestingSnapshot codableItemFromDescription:].cold.4
+ +[SFShareSheetSessionTestingSnapshot dateFormatter]
+ +[SFShareSheetSessionTestingSnapshot dateFormatter].cold.1
+ +[SFShareSheetSessionTestingSnapshot descriptionForItem:]
+ +[SFShareSheetSessionTestingSnapshot loadSnapshotFromURL:error:]
+ +[SFShareSheetSessionTestingSnapshot loadSnapshotFromURL:error:].cold.1
+ +[SFShareSheetSessionTestingSnapshot loadSnapshotFromURL:error:].cold.2
+ +[SFShareSheetSessionTestingSnapshot snapshotsDirectory]
+ +[SFShareSheetSessionTestingSnapshot supportsSecureCoding]
+ +[SFUnlockManager sharedUnlockManager].cold.1
+ -[SFAirDropAction triggerAction].cold.1
+ -[SFAirDropDiscoveryController isStoreDemoMode].cold.1
+ -[SFAppleIDClient _ensureAuthXPCStarted].cold.1
+ -[SFAppleIDClient _ensureXPCStarted].cold.1
+ -[SFAppleIDClient _interrupted].cold.1
+ -[SFAppleIDClient _invalidate].cold.1
+ -[SFAppleIDClient _invalidated].cold.1
+ -[SFAppleIDClient _invalidated].cold.2
+ -[SFAppleIDClient copyIdentityForAppleID:withCompletion:].cold.1
+ -[SFAppleIDClient dealloc].cold.1
+ -[SFAppleIDClient myAccountWithCompletion:].cold.1
+ -[SFAppleIDIdentity certificateExpired].cold.1
+ -[SFAppleIDIdentity copyCertificateWithType:].cold.1
+ -[SFAppleIDIdentity copyCertificateWithType:].cold.2
+ -[SFAppleIDIdentity copyCertificateWithType:].cold.3
+ -[SFAppleIDIdentity copyCertificateWithType:].cold.4
+ -[SFAppleIDIdentity copyCertificateWithType:].cold.5
+ -[SFAppleIDIdentity copyPrivateKey].cold.1
+ -[SFAppleIDIdentity copyPrivateKey].cold.2
+ -[SFAppleIDIdentity copyPrivateKey].cold.3
+ -[SFAppleIDIdentity copyPrivateKey].cold.4
+ -[SFAppleIDIdentity intermediateCertificateExpired].cold.1
+ -[SFAppleIDIdentity isInvalid].cold.1
+ -[SFAppleIDIdentity isInvalid].cold.2
+ -[SFAppleIDIdentity isInvalid].cold.3
+ -[SFAppleIDIdentity isInvalid].cold.4
+ -[SFAppleIDIdentity isInvalid].cold.5
+ -[SFAppleIDIdentity isInvalid].cold.6
+ -[SFAppleIDIdentity needsRenewal].cold.1
+ -[SFAppleIDIdentity needsRenewal].cold.2
+ -[SFAppleIDValidationRecord needsUpdate].cold.1
+ -[SFAppleIDValidationRecord needsUpdate].cold.2
+ -[SFAppleIDValidationRecord needsUpdate].cold.3
+ -[SFAppleIDValidationRecord needsUpdate].cold.4
+ -[SFApproveDiscovery _discoveryDeviceChanged:].cold.1
+ -[SFApproveDiscovery _discoveryDeviceChanged:].cold.2
+ -[SFApproveDiscovery _discoveryDeviceChanged:].cold.3
+ -[SFApproveDiscovery _discoveryFoundDevice:].cold.1
+ -[SFApproveDiscovery _discoveryFoundDevice:].cold.2
+ -[SFApproveDiscovery _discoveryFoundDevice:].cold.3
+ -[SFApproveDiscovery _discoveryFoundDevice:].cold.4
+ -[SFApproveDiscovery _discoveryLostDevice:].cold.1
+ -[SFApproveDiscovery _discoveryLostDevice:].cold.2
+ -[SFApproveDiscovery _discoveryLostDevice:].cold.3
+ -[SFApproveDiscovery _invalidated].cold.1
+ -[SFAuthenticateAccountsService _activate].cold.1
+ -[SFAuthenticateAccountsService _handleInfoExchange:responseHandler:].cold.1
+ -[SFAuthenticateAccountsService _handleRequest:flags:session:responseHandler:].cold.1
+ -[SFAuthenticateAccountsService _handleRequest:flags:session:responseHandler:].cold.2
+ -[SFAuthenticateAccountsService _handleSessionStarted:].cold.1
+ -[SFAuthenticateAccountsService _handleSessionStarted:].cold.2
+ -[SFAuthenticateAccountsService _handleSessionStarted:].cold.3
+ -[SFAuthenticateAccountsService _invalidate].cold.1
+ -[SFAuthenticateAccountsService _sfServiceStart].cold.1
+ -[SFAuthenticateAccountsService _shouldSignInAccountsInInfoRequest:].cold.1
+ -[SFAuthenticateAccountsService _validateConfiguration].cold.1
+ -[SFAuthenticateAccountsService _validateConfiguration].cold.2
+ -[SFAuthenticateAccountsService _validateConfiguration].cold.3
+ -[SFAuthenticateAccountsService setConfiguration:].cold.1
+ -[SFAuthenticateAccountsSession _handleShowTermsUI:responseHandler:].cold.1
+ -[SFAuthenticateAccountsSession _presentiCloudTermsUIWithAccount:].cold.1
+ -[SFAuthenticateAccountsSession _reportError:].cold.1
+ -[SFAuthenticateAccountsSession _runFinish].cold.1
+ -[SFAuthenticateAccountsSession _runInfoExchangeRequest].cold.1
+ -[SFAuthenticateAccountsSession _runInfoExchangeRequest].cold.2
+ -[SFAuthenticateAccountsSession _runInfoExchangeRequest].cold.3
+ -[SFAuthenticateAccountsSession _runInfoExchangeRequest].cold.4
+ -[SFAuthenticateAccountsSession _runInfoExchangeResponse:error:].cold.1
+ -[SFAuthenticateAccountsSession _runInfoExchange].cold.1
+ -[SFAuthenticateAccountsSession _runRepairCDP].cold.1
+ -[SFAuthenticateAccountsSession _runSFSessionStart].cold.1
+ -[SFAuthenticateAccountsSession _validateiCloudAccountTerms].cold.1
+ -[SFAuthenticateAccountsSession dealloc].cold.1
+ -[SFBLEAdvertiser _activateWithCompletion:].cold.1
+ -[SFBLEAdvertiser dealloc].cold.1
+ -[SFBLEAdvertiser dealloc].cold.2
+ -[SFBLEConnection dealloc].cold.1
+ -[SFBLEConnection dealloc].cold.2
+ -[SFBLEPipe dealloc].cold.1
+ -[SFBLEScanner _activateWithCompletion:].cold.1
+ -[SFBLEScanner _startTimeoutIfNeeded].cold.1
+ -[SFBLEScanner dealloc].cold.1
+ -[SFBLEScanner dealloc].cold.2
+ -[SFBLEScanner dealloc].cold.3
+ -[SFBLEScanner dealloc].cold.4
+ -[SFBLEScanner dealloc].cold.5
+ -[SFBLEScanner dealloc].cold.6
+ -[SFBLEScanner dealloc].cold.7
+ -[SFBLEScanner setPayloadFilterData:mask:].cold.1
+ -[SFBluetoothPairingSession _activate].cold.1
+ -[SFBluetoothPairingSession dealloc].cold.1
+ -[SFClient _ensureXPCStarted].cold.1
+ -[SFClient _interrupted].cold.1
+ -[SFClient _interrupted].cold.2
+ -[SFClient _invalidate].cold.1
+ -[SFClient _invalidated].cold.1
+ -[SFClient _invalidated].cold.2
+ -[SFClient dealloc].cold.1
+ -[SFCollaborationCloudSharingResult initWithCollaborationItemIdentifier:sharingURL:share:existingShare:error:mailResult:].cold.1
+ -[SFCollaborationItem workQueue].cold.1
+ -[SFContinuityRemoteSession _run].cold.1
+ -[SFContinuityRemoteSession _run].cold.2
+ -[SFContinuityRemoteSession _run].cold.3
+ -[SFContinuityRemoteSession _sfSessionStart].cold.1
+ -[SFContinuityRemoteSession dealloc].cold.1
+ -[SFCoordinatedAlertRequest _ensureXPCStarted].cold.1
+ -[SFCoordinatedAlertRequest _interrupted].cold.1
+ -[SFCoordinatedAlertRequest _invalidate].cold.1
+ -[SFCoordinatedAlertRequest _invalidated].cold.1
+ -[SFCoordinatedAlertRequest _invalidated].cold.2
+ -[SFCoordinatedAlertRequest _start].cold.1
+ -[SFCoordinatedAlertRequest _start].cold.2
+ -[SFCoordinatedAlertRequest _start].cold.3
+ -[SFCoordinatedAlertRequest _start].cold.4
+ -[SFCoordinatedAlertRequest dealloc].cold.1
+ -[SFCoordinatedAlertRequest dealloc].cold.2
+ -[SFDevice updateWithBLEDevice:].cold.1
+ -[SFDeviceAssetManager addQueryResultToLocalCache:url:isFallback:].cold.1
+ -[SFDeviceAssetManager clearQueryResultFromLocalCache:].cold.1
+ -[SFDeviceAssetManager getAssetBundleForDeviceQuery:withRequestConfiguration:].cold.1
+ -[SFDeviceAssetManager hardcodedMappedProducts].cold.1
+ -[SFDeviceAssetManager onqueue_executeNextMAQueryForTask:].cold.1
+ -[SFDeviceAssetManager onqueue_manuallyFindFallbackAssetBundleMatchingQuery:withCompletionHandler:].cold.1
+ -[SFDeviceAssetManager onqueue_manuallyFindFallbackAssetBundleMatchingQuery:withCompletionHandler:].cold.2
+ -[SFDeviceAssetManager purgeAssetsMatchingQuery:].cold.1
+ -[SFDeviceDiscovery _activateWithCompletion:].cold.1
+ -[SFDeviceDiscovery _activateWithCompletion:].cold.2
+ -[SFDeviceDiscovery _activateWithCompletion:].cold.3
+ -[SFDeviceDiscovery _ensureXPCStarted].cold.1
+ -[SFDeviceDiscovery _ensureXPCStarted].cold.2
+ -[SFDeviceDiscovery _ensureXPCStarted].cold.3
+ -[SFDeviceDiscovery _ensureXPCStarted].cold.4
+ -[SFDeviceDiscovery _interrupted].cold.1
+ -[SFDeviceDiscovery _interrupted].cold.2
+ -[SFDeviceDiscovery _invalidated].cold.1
+ -[SFDeviceDiscovery _invalidated].cold.2
+ -[SFDeviceDiscovery _retryConsole].cold.1
+ -[SFDeviceDiscovery _timeoutTimerFired].cold.1
+ -[SFDeviceDiscovery dealloc].cold.1
+ -[SFDeviceOperationCDPSetup _activate].cold.1
+ -[SFDeviceOperationCDPSetup _complete:].cold.1
+ -[SFDeviceOperationCDPSetup _runCDPApprovalServerStart].cold.1
+ -[SFDeviceOperationCDPSetup _runCDPSetupRequest].cold.1
+ -[SFDeviceOperationCNJSetup _handleCompletedEventWithError:].cold.1
+ -[SFDeviceOperationCNJSetup _showCaptiveSheet:].cold.1
+ -[SFDeviceOperationCNJSetup showWebSheet].cold.1
+ -[SFDeviceOperationHandlerCDPSetup _activate].cold.1
+ -[SFDeviceOperationHandlerCDPSetup _activate].cold.2
+ -[SFDeviceOperationHandlerCDPSetup _handleCDPSetupRequest:responseHandler:].cold.1
+ -[SFDeviceOperationHandlerCDPSetup _handleCDPSetupRequest:responseHandler:].cold.2
+ -[SFDeviceOperationHandlerCDPSetup _handleCDPSetupRequest:responseHandler:].cold.3
+ -[SFDeviceOperationHandlerCDPSetup _handleCDPSetupRequest:responseHandler:].cold.4
+ -[SFDeviceOperationHandlerCDPSetup cdpContext:promptForICSCWithIsNumeric:numericLength:isRandom:validator:].cold.1
+ -[SFDeviceOperationHandlerCDPSetup cdpContext:promptForInteractiveAuthenticationWithCompletion:].cold.1
+ -[SFDeviceOperationHandlerCDPSetup cdpContext:promptForLocalSecretWithCompletion:].cold.1
+ -[SFDeviceOperationHandlerCDPSetup cdpContext:promptForRemoteSecretWithDevices:offeringRemoteApproval:validator:].cold.1
+ -[SFDeviceOperationHandlerCNJSetup _handleCaptiveJoinRequestWithResponseHandler:reachabilityError:].cold.1
+ -[SFDeviceOperationHandlerCNJSetup _runReachability:responseHandler:].cold.1
+ -[SFDeviceOperationHandlerWiFiSetup _activate].cold.1
+ -[SFDeviceOperationHandlerWiFiSetup _cleanupOldWiFiNetworks].cold.1
+ -[SFDeviceOperationHandlerWiFiSetup _cleanupOldWiFiNetworks].cold.2
+ -[SFDeviceOperationHandlerWiFiSetup _completeError:].cold.1
+ -[SFDeviceOperationHandlerWiFiSetup _completeError:].cold.2
+ -[SFDeviceOperationHandlerWiFiSetup _completeError:].cold.3
+ -[SFDeviceOperationHandlerWiFiSetup _completeError:].cold.4
+ -[SFDeviceOperationHandlerWiFiSetup _completeError:].cold.5
+ -[SFDeviceOperationHandlerWiFiSetup _completeError:].cold.6
+ -[SFDeviceOperationHandlerWiFiSetup _handleRequestBonjourTestDone:responseHandler:].cold.1
+ -[SFDeviceOperationHandlerWiFiSetup _handleRequestBonjourTestStart:responseHandler:].cold.1
+ -[SFDeviceOperationHandlerWiFiSetup _handleRequestBonjourTestStart:responseHandler:].cold.2
+ -[SFDeviceOperationHandlerWiFiSetup _handleWiFiSetupRequest:responseHandler:].cold.1
+ -[SFDeviceOperationHandlerWiFiSetup _handleWiFiSetupRequest:responseHandler:].cold.2
+ -[SFDeviceOperationHandlerWiFiSetup _runJoinStart:].cold.1
+ -[SFDeviceOperationHandlerWiFiSetup _runJoinStart:].cold.2
+ -[SFDeviceOperationHandlerWiFiSetup _runReachabilityStart].cold.1
+ -[SFDeviceOperationHandlerWiFiSetup _runReachabilityStart].cold.2
+ -[SFDeviceOperationHandlerWiFiSetup _runReachabilityStart].cold.3
+ -[SFDeviceOperationHandlerWiFiSetup _runScanResults:error:channel:].cold.1
+ -[SFDeviceOperationHandlerWiFiSetup _runScanStart:].cold.1
+ -[SFDeviceOperationHandlerWiFiSetup createWiFiRetryMetricEventForIPAssign:duration:]
+ -[SFDeviceOperationWiFiSetup _activate2].cold.1
+ -[SFDeviceOperationWiFiSetup _activate2].cold.2
+ -[SFDeviceOperationWiFiSetup _activate2].cold.3
+ -[SFDeviceOperationWiFiSetup _activate2].cold.4
+ -[SFDeviceOperationWiFiSetup _activate2].cold.5
+ -[SFDeviceOperationWiFiSetup _activate].cold.1
+ -[SFDeviceOperationWiFiSetup _activate].cold.2
+ -[SFDeviceOperationWiFiSetup _activate].cold.3
+ -[SFDeviceOperationWiFiSetup _activate].cold.4
+ -[SFDeviceOperationWiFiSetup _bonjourTestFoundDevice:].cold.1
+ -[SFDeviceOperationWiFiSetup _bonjourTestFoundDevice:].cold.2
+ -[SFDeviceOperationWiFiSetup _bonjourTestStart].cold.1
+ -[SFDeviceOperationWiFiSetup _setupResponse:inResponse:].cold.1
+ -[SFDeviceOperationWiFiSetup _setupResponse:inResponse:].cold.2
+ -[SFDeviceOperationWiFiSetup createRequestFromWiFiConfig].cold.1
+ -[SFDeviceOperationWiFiSetup createRequestFromWiFiConfig].cold.2
+ -[SFDeviceRepairService _handleFinishRequest:responseHandler:].cold.1
+ -[SFDeviceRepairService _handleGetProblemsRequest:responseHandler:].cold.1
+ -[SFDeviceRepairService _handleGetProblemsRequest:responseHandler:].cold.2
+ -[SFDeviceRepairService _handleGetProblemsRequest:responseHandler:].cold.3
+ -[SFDeviceRepairService _handleGetProblemsRequest:responseHandler:].cold.4
+ -[SFDeviceRepairService _handleSessionEnded:].cold.1
+ -[SFDeviceRepairService _handleSessionStarted:].cold.1
+ -[SFDeviceRepairService _handleSessionStarted:].cold.2
+ -[SFDeviceRepairService _invalidate].cold.1
+ -[SFDeviceRepairService _sfServiceStart].cold.1
+ -[SFDeviceRepairService activate].cold.1
+ -[SFDeviceRepairSession _reportError:isPreflight:].cold.1
+ -[SFDeviceRepairSession _reportRepairResultMetrics:].cold.1
+ -[SFDeviceRepairSession _runCDPSetup].cold.1
+ -[SFDeviceRepairSession _runFinish].cold.1
+ -[SFDeviceRepairSession _runGetProblems].cold.1
+ -[SFDeviceRepairSession _runPairVerify].cold.1
+ -[SFDeviceRepairSession _runPreflightWiFiEarly].cold.1
+ -[SFDeviceRepairSession _runPreflightWiFiEarly].cold.2
+ -[SFDeviceRepairSession _runPreflightWiFiFull].cold.1
+ -[SFDeviceRepairSession _runPreflightWiFiFull].cold.2
+ -[SFDeviceRepairSession _runSFSessionStart].cold.1
+ -[SFDeviceRepairSession _runWiFiSetup].cold.1
+ -[SFDeviceRepairSession _runWiFiSetup].cold.2
+ -[SFDeviceRepairSession _runWiFiSetup].cold.3
+ -[SFDeviceRepairSession _runWiFiSetup].cold.4
+ -[SFDeviceRepairSession _runWiFiSetup].cold.5
+ -[SFDeviceRepairSession dealloc].cold.1
+ -[SFDeviceSetupAppleTVService _activate].cold.1
+ -[SFDeviceSetupAppleTVService _handleBasicConfigRequest:responseHandler:].cold.1
+ -[SFDeviceSetupAppleTVService _handleBasicConfigRequest:responseHandler:].cold.2
+ -[SFDeviceSetupAppleTVService _handleBasicConfigRequest:responseHandler:].cold.3
+ -[SFDeviceSetupAppleTVService _handleFinishRequest:responseHandler:].cold.1
+ -[SFDeviceSetupAppleTVService _handleFinishRequest:responseHandler:].cold.2
+ -[SFDeviceSetupAppleTVService _handlePreAuthRequest:responseHandler:].cold.1
+ -[SFDeviceSetupAppleTVService _handlePreAuthRequest:responseHandler:].cold.2
+ -[SFDeviceSetupAppleTVService _handlePreAuthRequest:responseHandler:].cold.3
+ -[SFDeviceSetupAppleTVService _handlePreAuthRequest:responseHandler:].cold.4
+ -[SFDeviceSetupAppleTVService _handlePreAuthRequest:responseHandler:].cold.5
+ -[SFDeviceSetupAppleTVService _handlePreAuthRequest:responseHandler:].cold.6
+ -[SFDeviceSetupAppleTVService _handleSessionStarted:].cold.1
+ -[SFDeviceSetupAppleTVService _handleSessionStarted:].cold.2
+ -[SFDeviceSetupAppleTVService _invalidate].cold.1
+ -[SFDeviceSetupAppleTVService _sfServiceStart].cold.1
+ -[SFDeviceSetupAppleTVService dealloc].cold.1
+ -[SFDeviceSetupAppleTVSession _reportErrorMetrics:errorLabel:isFatal:].cold.1
+ -[SFDeviceSetupAppleTVSession _reportMainMetrics:errorLabel:userWaitSeconds:].cold.1
+ -[SFDeviceSetupAppleTVSession _runBasicConfigRequest].cold.1
+ -[SFDeviceSetupAppleTVSession _runBasicConfigRequest].cold.10
+ -[SFDeviceSetupAppleTVSession _runBasicConfigRequest].cold.11
+ -[SFDeviceSetupAppleTVSession _runBasicConfigRequest].cold.12
+ -[SFDeviceSetupAppleTVSession _runBasicConfigRequest].cold.13
+ -[SFDeviceSetupAppleTVSession _runBasicConfigRequest].cold.2
+ -[SFDeviceSetupAppleTVSession _runBasicConfigRequest].cold.3
+ -[SFDeviceSetupAppleTVSession _runBasicConfigRequest].cold.4
+ -[SFDeviceSetupAppleTVSession _runBasicConfigRequest].cold.5
+ -[SFDeviceSetupAppleTVSession _runBasicConfigRequest].cold.6
+ -[SFDeviceSetupAppleTVSession _runBasicConfigRequest].cold.7
+ -[SFDeviceSetupAppleTVSession _runBasicConfigRequest].cold.8
+ -[SFDeviceSetupAppleTVSession _runBasicConfigRequest].cold.9
+ -[SFDeviceSetupAppleTVSession _runBasicConfigResponse:error:].cold.1
+ -[SFDeviceSetupAppleTVSession _runBasicConfigResponse:error:].cold.2
+ -[SFDeviceSetupAppleTVSession _runBasicConfig].cold.1
+ -[SFDeviceSetupAppleTVSession _runCDPSetup].cold.1
+ -[SFDeviceSetupAppleTVSession _runFinish:].cold.1
+ -[SFDeviceSetupAppleTVSession _runPreAuthRequest].cold.1
+ -[SFDeviceSetupAppleTVSession _runPreAuthRequest].cold.2
+ -[SFDeviceSetupAppleTVSession _runPreAuthRequest].cold.3
+ -[SFDeviceSetupAppleTVSession _runPreAuthRequest].cold.4
+ -[SFDeviceSetupAppleTVSession _runPreAuthRequest].cold.5
+ -[SFDeviceSetupAppleTVSession _runPreAuthResponse:error:].cold.1
+ -[SFDeviceSetupAppleTVSession _runPreAuthResponse:error:].cold.2
+ -[SFDeviceSetupAppleTVSession _runPreAuthResponse:error:].cold.3
+ -[SFDeviceSetupAppleTVSession _runPreAuthResponse:error:].cold.4
+ -[SFDeviceSetupAppleTVSession _runPreAuth].cold.1
+ -[SFDeviceSetupAppleTVSession _runPreflightWiFi].cold.1
+ -[SFDeviceSetupAppleTVSession _runPreflightWiFi].cold.2
+ -[SFDeviceSetupAppleTVSession _runPreflightWiFi].cold.3
+ -[SFDeviceSetupAppleTVSession _runPreflightiTunes].cold.1
+ -[SFDeviceSetupAppleTVSession _runSFSessionStart].cold.1
+ -[SFDeviceSetupAppleTVSession dealloc].cold.1
+ -[SFDeviceSetupServiceiOS _completed:].cold.1
+ -[SFDeviceSetupServiceiOS _handleAppEventReceived:].cold.1
+ -[SFDeviceSetupServiceiOS _handleSessionSecured:].cold.1
+ -[SFDeviceSetupServiceiOS _handleSessionSecured:].cold.2
+ -[SFDeviceSetupServiceiOS _handleSessionSecured:].cold.3
+ -[SFDeviceSetupServiceiOS _handleSessionStarted:].cold.1
+ -[SFDeviceSetupServiceiOS _handleSessionStarted:].cold.2
+ -[SFDeviceSetupServiceiOS _handleSessionStarted:].cold.3
+ -[SFDeviceSetupServiceiOS _handleSessionStarted:].cold.4
+ -[SFDeviceSetupServiceiOS _handleSessionStarted:].cold.5
+ -[SFDeviceSetupServiceiOS _handleSetupActionRequest:responseHandler:].cold.1
+ -[SFDeviceSetupServiceiOS _handleSetupActionRequest:responseHandler:].cold.2
+ -[SFDeviceSetupServiceiOS _handleSetupActionSuspend].cold.1
+ -[SFDeviceSetupServiceiOS _invalidated].cold.1
+ -[SFDeviceSetupServiceiOS _invalidated].cold.2
+ -[SFDeviceSetupServiceiOS _receivedObject:flags:].cold.1
+ -[SFDeviceSetupServiceiOS _receivedObject:flags:].cold.2
+ -[SFDeviceSetupServiceiOS _receivedObject:flags:].cold.3
+ -[SFDeviceSetupServiceiOS _receivedObject:flags:].cold.4
+ -[SFDeviceSetupServiceiOS _runResumeIfNeeded].cold.1
+ -[SFDeviceSetupServiceiOS _runResumeIfNeeded].cold.2
+ -[SFDeviceSetupServiceiOS _runResumeIfNeeded].cold.3
+ -[SFDeviceSetupServiceiOS _runResumeIfNeeded].cold.4
+ -[SFDeviceSetupServiceiOS _runResumeIfNeeded].cold.5
+ -[SFDeviceSetupServiceiOS _run].cold.1
+ -[SFDeviceSetupServiceiOS _sfServiceStart].cold.1
+ -[SFDeviceSetupServiceiOS dealloc].cold.1
+ -[SFDeviceSetupServiceiOS sendObject:].cold.1
+ -[SFDeviceSetupServiceiOS sendObject:].cold.2
+ -[SFDeviceSetupServiceiOS sendObject:].cold.3
+ -[SFDeviceSetupSessioniOS _completedWithError:].cold.1
+ -[SFDeviceSetupSessioniOS _completedWithError:].cold.2
+ -[SFDeviceSetupSessioniOS _handleSetupActionRequest:responseHandler:].cold.1
+ -[SFDeviceSetupSessioniOS _handleSetupActionRequest:responseHandler:].cold.2
+ -[SFDeviceSetupSessioniOS _handleSetupActionSoftwareUpdate].cold.1
+ -[SFDeviceSetupSessioniOS _handleSetupActionSoftwareUpdate].cold.2
+ -[SFDeviceSetupSessioniOS _handleSetupActionSoftwareUpdate].cold.3
+ -[SFDeviceSetupSessioniOS _handleSetupPeerSuspended].cold.1
+ -[SFDeviceSetupSessioniOS _handleSetupResumeFoundDevice:].cold.1
+ -[SFDeviceSetupSessioniOS _handleSetupResumeFoundDevice:].cold.2
+ -[SFDeviceSetupSessioniOS _receivedObject:flags:].cold.1
+ -[SFDeviceSetupSessioniOS _receivedObject:flags:].cold.2
+ -[SFDeviceSetupSessioniOS _receivedObject:flags:].cold.3
+ -[SFDeviceSetupSessioniOS _receivedObject:flags:].cold.4
+ -[SFDeviceSetupSessioniOS _receivedObject:flags:].cold.5
+ -[SFDeviceSetupSessioniOS _receivedObject:flags:].cold.6
+ -[SFDeviceSetupSessioniOS _runCoreCDPSetup].cold.1
+ -[SFDeviceSetupSessioniOS _runPreAuthPairSetup].cold.1
+ -[SFDeviceSetupSessioniOS _runResume].cold.1
+ -[SFDeviceSetupSessioniOS _runSFSessionActivated].cold.1
+ -[SFDeviceSetupSessioniOS _runSFSessionStart].cold.1
+ -[SFDeviceSetupSessioniOS _run].cold.1
+ -[SFDeviceSetupSessioniOS _run].cold.2
+ -[SFDeviceSetupSessioniOS _run].cold.3
+ -[SFDeviceSetupSessioniOS _run].cold.4
+ -[SFDeviceSetupSessioniOS _run].cold.5
+ -[SFDeviceSetupSessioniOS _run].cold.6
+ -[SFDeviceSetupSessioniOS _run].cold.7
+ -[SFDeviceSetupSessioniOS _sendConfigInfo].cold.1
+ -[SFDeviceSetupSessioniOS _sendConfigInfo].cold.2
+ -[SFDeviceSetupSessioniOS _sendConfigInfo].cold.3
+ -[SFDeviceSetupSessioniOS _sendConfigInfo].cold.4
+ -[SFDeviceSetupSessioniOS _sendConfigInfo].cold.5
+ -[SFDeviceSetupSessioniOS _sendConfigInfo].cold.6
+ -[SFDeviceSetupSessioniOS _sendConfigInfo].cold.7
+ -[SFDeviceSetupSessioniOS _sendConfigInfo].cold.8
+ -[SFDeviceSetupSessioniOS _sendPreAuthInfo].cold.1
+ -[SFDeviceSetupSessioniOS _sendPreAuthInfo].cold.2
+ -[SFDeviceSetupSessioniOS _sendPreAuthInfo].cold.3
+ -[SFDeviceSetupSessioniOS _sendPreAuthInfo].cold.4
+ -[SFDeviceSetupSessioniOS _sendPreAuthInfo].cold.5
+ -[SFDeviceSetupSessioniOS dealloc].cold.1
+ -[SFDeviceSetupWHAService _handleInfoExchange:responseHandler:].cold.1
+ -[SFDeviceSetupWHAService _handleInfoExchange:responseHandler:].cold.2
+ -[SFDeviceSetupWHAService _handleRequest:flags:session:responseHandler:].cold.1
+ -[SFDeviceSetupWHAService _handleRequest:flags:session:responseHandler:].cold.2
+ -[SFDeviceSetupWHAService _handleSessionStarted:].cold.1
+ -[SFDeviceSetupWHAService _handleSessionStarted:].cold.2
+ -[SFDeviceSetupWHAService _sfServiceStart].cold.1
+ -[SFDeviceSetupWHAService dealloc].cold.1
+ -[SFDeviceSetupWHASession _reportError:].cold.1
+ -[SFDeviceSetupWHASession _runCDPSetup].cold.1
+ -[SFDeviceSetupWHASession _runFinish].cold.1
+ -[SFDeviceSetupWHASession _runInfoExchangeRequest].cold.1
+ -[SFDeviceSetupWHASession _runInfoExchangeResponse:error:].cold.1
+ -[SFDeviceSetupWHASession _runInfoExchange].cold.1
+ -[SFDeviceSetupWHASession _runSFSessionStart].cold.1
+ -[SFDeviceSetupWHASession dealloc].cold.1
+ -[SFDiagnostics _ensureXPCStarted].cold.1
+ -[SFDiagnostics _interrupted].cold.1
+ -[SFDiagnostics _invalidate].cold.1
+ -[SFDiagnostics _invalidated].cold.1
+ -[SFDiagnostics _invalidated].cold.2
+ -[SFDiagnostics dealloc].cold.1
+ -[SFNFCTagReaderUIController _activateWithCompletion:].cold.1
+ -[SFNFCTagReaderUIController _ensureXPCStarted].cold.1
+ -[SFNFCTagReaderUIController _ensureXPCStarted].cold.2
+ -[SFNFCTagReaderUIController _interrupted].cold.1
+ -[SFNFCTagReaderUIController _invalidated].cold.1
+ -[SFNFCTagReaderUIController _invalidated].cold.2
+ -[SFNFCTagReaderUIController _nfcTagScannedCount].cold.1
+ -[SFNFCTagReaderUIController uiActivatedWithCompletion:].cold.1
+ -[SFNFCTagReaderUIController uiInvalidatedWithCompletion:].cold.1
+ -[SFPINPairSession _activate].cold.1
+ -[SFPINPairSession _activate].cold.2
+ -[SFPINPairSession _activate].cold.3
+ -[SFPINPairSession _activate].cold.4
+ -[SFPINPairSession _clientHeartbeatSend].cold.1
+ -[SFPINPairSession _clientPairSetup:start:].cold.1
+ -[SFPINPairSession _clientPairSetup:start:].cold.2
+ -[SFPINPairSession _clientPairSetup:start:].cold.3
+ -[SFPINPairSession _clientPairSetup:start:].cold.4
+ -[SFPINPairSession _clientPairSetup:start:].cold.5
+ -[SFPINPairSession _clientPairVerify:start:].cold.1
+ -[SFPINPairSession _clientPairVerify:start:].cold.2
+ -[SFPINPairSession _clientPairVerify:start:].cold.3
+ -[SFPINPairSession _clientPairVerify:start:].cold.4
+ -[SFPINPairSession _clientPairVerify:start:].cold.5
+ -[SFPINPairSession _clientRun].cold.1
+ -[SFPINPairSession _clientRun].cold.2
+ -[SFPINPairSession _clientRun].cold.3
+ -[SFPINPairSession _clientRun].cold.4
+ -[SFPINPairSession _clientSFSessionStart].cold.1
+ -[SFPINPairSession _clientTryPIN:].cold.1
+ -[SFPINPairSession _clientTryPIN:].cold.2
+ -[SFPINPairSession _handleServerRequest:].cold.1
+ -[SFPINPairSession _handleServerRequest:].cold.2
+ -[SFPINPairSession _handleServerRequest:].cold.3
+ -[SFPINPairSession _hearbeatTimer].cold.1
+ -[SFPINPairSession _hearbeatTimer].cold.2
+ -[SFPINPairSession _invalidate].cold.1
+ -[SFPINPairSession dealloc].cold.1
+ -[SFPINPairSession handleServerPairSetup:reset:].cold.1
+ -[SFPINPairSession handleServerPairSetup:reset:].cold.2
+ -[SFPINPairSession handleServerPairVerify:reset:].cold.1
+ -[SFPINPairSession handleServerPairVerify:reset:].cold.2
+ -[SFPasswordSharingService __activateCalled].cold.1
+ -[SFPasswordSharingService __invalidateCalled].cold.1
+ -[SFPasswordSharingService __testReceivedObject:withFlags:].cold.1
+ -[SFPasswordSharingService _handleReceivedPassword:].cold.1
+ -[SFPasswordSharingService _handleReceivedPassword:].cold.2
+ -[SFPasswordSharingService _handleReceivedPassword:].cold.3
+ -[SFPasswordSharingService _handleReceivedPassword:].cold.4
+ -[SFPasswordSharingService _handleReceivedPassword:].cold.5
+ -[SFPasswordSharingService _handleSessionStarted:].cold.1
+ -[SFPasswordSharingService _passInfoToDelegate:].cold.1
+ -[SFPasswordSharingService _promptUserWithInfo:message:].cold.1
+ -[SFPasswordSharingService _receivedObject:flags:].cold.1
+ -[SFPasswordSharingService _receivedObject:flags:].cold.2
+ -[SFPasswordSharingService _receivedObject:flags:].cold.3
+ -[SFPasswordSharingService _runServiceStart].cold.1
+ -[SFPasswordSharingService _sendPasswordDeclinedWithError:].cold.1
+ -[SFPasswordSharingService _sendPasswordDeclinedWithError:].cold.2
+ -[SFPasswordSharingService _sendPasswordDeclinedWithError:].cold.3
+ -[SFPasswordSharingService _sendPasswordReceived].cold.1
+ -[SFPasswordSharingService _sendPasswordReceived].cold.2
+ -[SFPasswordSharingService _sendPasswordReceived].cold.3
+ -[SFPasswordSharingService dealloc].cold.1
+ -[SFPasswordSharingService disabledViaConfig].cold.1
+ -[SFPasswordSharingSession _completedWithError:].cold.1
+ -[SFPasswordSharingSession _completedWithError:].cold.2
+ -[SFPasswordSharingSession _completedWithError:].cold.3
+ -[SFPasswordSharingSession _receivedObject:flags:].cold.1
+ -[SFPasswordSharingSession _receivedObject:flags:].cold.2
+ -[SFPasswordSharingSession _runPasswordShareReceiveResponse:].cold.1
+ -[SFPasswordSharingSession _runPasswordShareReceiveResponse:].cold.2
+ -[SFPasswordSharingSession _runPasswordShareReceiveResponse:].cold.3
+ -[SFPasswordSharingSession _runPasswordShareReceiveResponse:].cold.4
+ -[SFPasswordSharingSession _runPasswordShareSendInfo].cold.1
+ -[SFPasswordSharingSession _runPasswordShareSendInfo].cold.2
+ -[SFPasswordSharingSession _runPasswordShareSendInfo].cold.3
+ -[SFPasswordSharingSession _runPasswordShareSendInfo].cold.4
+ -[SFPasswordSharingSession _runPasswordShareSendInfo].cold.5
+ -[SFPasswordSharingSession _runPasswordShare].cold.1
+ -[SFPasswordSharingSession _runSFSessionStart].cold.1
+ -[SFPasswordSharingSession dealloc].cold.1
+ -[SFProxHandoffService _activateWithCompletion:].cold.1
+ -[SFProxHandoffService _activated].cold.1
+ -[SFProxHandoffService _activated].cold.2
+ -[SFProxHandoffService _completedWithError:].cold.1
+ -[SFProxHandoffService _serviceStart].cold.1
+ -[SFProxHandoffService dealloc].cold.1
+ -[SFProximityClient _dismissContentForDevice:completion:].cold.1
+ -[SFProximityClient _dismissContentForDevice:completion:].cold.2
+ -[SFProximityClient _ensureXPCStarted].cold.1
+ -[SFProximityClient _interrupted].cold.1
+ -[SFProximityClient _invalidate].cold.1
+ -[SFProximityClient _invalidate].cold.2
+ -[SFProximityClient _invalidated].cold.1
+ -[SFProximityClient _invalidated].cold.2
+ -[SFProximityClient _stopSuppressingDevice:completion:].cold.1
+ -[SFProximityClient _stopSuppressingDevice:completion:].cold.2
+ -[SFProximityClient _suppressDevice:completion:].cold.1
+ -[SFProximityClient _suppressDevice:completion:].cold.2
+ -[SFProximityClient _updateContent:forDevice:completion:].cold.1
+ -[SFProximityClient dealloc].cold.1
+ -[SFProximityClient proximityClientDeviceDidUntriggerHandler:].cold.1
+ -[SFProximityClient proximityClientDeviceEnteredImmediate:].cold.1
+ -[SFProximityClient proximityClientDeviceEnteredNearby:].cold.1
+ -[SFProximityClient proximityClientDeviceExitedImmediate:].cold.1
+ -[SFProximityClient proximityClientDeviceExitedNearby:].cold.1
+ -[SFProximityClient proximityClientDeviceUpdated:rssi:state:].cold.1
+ -[SFProximityClient proximityClientDeviceWasDismissedHandler:reason:].cold.1
+ -[SFProximityClient proximityClientDeviceWasSelectedHandler:].cold.1
+ -[SFProximityClient proximityClientDeviceWillTriggerHandler:].cold.1
+ -[SFRemoteAutoFillScanAction performWithCompletion:].cold.1
+ -[SFRemoteAutoFillService _activateWithCompletion:].cold.1
+ -[SFRemoteAutoFillService _activateWithCompletion:].cold.2
+ -[SFRemoteAutoFillService _activated].cold.1
+ -[SFRemoteAutoFillService _activated].cold.2
+ -[SFRemoteAutoFillService _activated].cold.3
+ -[SFRemoteAutoFillService _activated].cold.4
+ -[SFRemoteAutoFillService _completedWithError:].cold.1
+ -[SFRemoteAutoFillService _discoveryStart].cold.1
+ -[SFRemoteAutoFillService _serviceHandleReceivedContextRequest:handler:].cold.1
+ -[SFRemoteAutoFillService _serviceHandleReceivedCredentialRequest:handler:].cold.1
+ -[SFRemoteAutoFillService _serviceHandleReceivedCredentialRequest:handler:].cold.2
+ -[SFRemoteAutoFillService _serviceHandleReceivedCredentialRequest:handler:].cold.3
+ -[SFRemoteAutoFillService _serviceHandleReceivedRequest:handler:].cold.1
+ -[SFRemoteAutoFillService _serviceHandleReceivedRequest:handler:].cold.2
+ -[SFRemoteAutoFillService _serviceHandleReceivedRequest:handler:].cold.3
+ -[SFRemoteAutoFillService _serviceHidePIN].cold.1
+ -[SFRemoteAutoFillService _serviceSessionEnded:withError:].cold.1
+ -[SFRemoteAutoFillService _serviceSessionStarted:].cold.1
+ -[SFRemoteAutoFillService _serviceSessionStarted:].cold.2
+ -[SFRemoteAutoFillService _serviceStart].cold.1
+ -[SFRemoteAutoFillService dealloc].cold.1
+ -[SFRemoteAutoFillService setBundleID:].cold.1
+ -[SFRemoteAutoFillService setUrlString:].cold.1
+ -[SFRemoteAutoFillService startRequestingAutoFill].cold.1
+ -[SFRemoteAutoFillService startRequestingAutoFill].cold.2
+ -[SFRemoteAutoFillService stopRequestingAutoFill].cold.1
+ -[SFRemoteAutoFillService stopRequestingAutoFill].cold.2
+ -[SFRemoteAutoFillService updateURLForVisualScanning].cold.1
+ -[SFRemoteAutoFillSession _completedWithError:].cold.1
+ -[SFRemoteAutoFillSession _completedWithError:].cold.2
+ -[SFRemoteAutoFillSession _handleContextRequestResponse:error:].cold.1
+ -[SFRemoteAutoFillSession _handleContextRequestResponse:error:].cold.2
+ -[SFRemoteAutoFillSession _handleContextRequestResponse:error:].cold.3
+ -[SFRemoteAutoFillSession _handleContextRequestResponse:error:].cold.4
+ -[SFRemoteAutoFillSession _handleContextRequestResponse:error:].cold.5
+ -[SFRemoteAutoFillSession _handleContextRequestResponse:error:].cold.6
+ -[SFRemoteAutoFillSession _handleContextRequestResponse:error:].cold.7
+ -[SFRemoteAutoFillSession _handleContextRequestResponse:error:].cold.8
+ -[SFRemoteAutoFillSession _handleContextRequestResponse:error:].cold.9
+ -[SFRemoteAutoFillSession _handlePasswordPickerResponse:password:error:].cold.1
+ -[SFRemoteAutoFillSession _handlePasswordPickerResponse:password:error:].cold.2
+ -[SFRemoteAutoFillSession _handlePasswordPickerResponse:password:error:].cold.3
+ -[SFRemoteAutoFillSession _handlePasswordPickerResponse:password:error:].cold.4
+ -[SFRemoteAutoFillSession _handleSendCredentialsResponse:error:].cold.1
+ -[SFRemoteAutoFillSession _handleSendCredentialsResponse:error:].cold.2
+ -[SFRemoteAutoFillSession _receivedObject:flags:].cold.1
+ -[SFRemoteAutoFillSession _receivedObject:flags:].cold.2
+ -[SFRemoteAutoFillSession _receivedObject:flags:].cold.3
+ -[SFRemoteAutoFillSession _runContextRequest].cold.1
+ -[SFRemoteAutoFillSession _runPairContacts].cold.1
+ -[SFRemoteAutoFillSession _runPairHomeKit].cold.1
+ -[SFRemoteAutoFillSession _runPairVerify].cold.1
+ -[SFRemoteAutoFillSession _runPairVisual].cold.1
+ -[SFRemoteAutoFillSession _runSendCredentials].cold.1
+ -[SFRemoteAutoFillSession _runSendCredentials].cold.2
+ -[SFRemoteAutoFillSession _runSessionStart].cold.1
+ -[SFRemoteAutoFillSession dealloc].cold.1
+ -[SFRemoteAutoFillSessionHelper _activateWithCompletion:].cold.1
+ -[SFRemoteAutoFillSessionHelper _activateWithCompletion:].cold.2
+ -[SFRemoteAutoFillSessionHelper _ensureXPCStarted].cold.1
+ -[SFRemoteAutoFillSessionHelper _interrupted].cold.1
+ -[SFRemoteAutoFillSessionHelper _invalidate].cold.1
+ -[SFRemoteAutoFillSessionHelper _invalidated].cold.1
+ -[SFRemoteAutoFillSessionHelper _invalidated].cold.2
+ -[SFRemoteAutoFillSessionHelper autoFillDismissUserNotification].cold.1
+ -[SFRemoteAutoFillSessionHelper autoFillPairingSucceeded:completion:].cold.1
+ -[SFRemoteAutoFillSessionHelper autoFillPromptForPIN:throttleSeconds:].cold.1
+ -[SFRemoteAutoFillSessionHelper clientDismissUserNotification].cold.1
+ -[SFRemoteAutoFillSessionHelper clientPairingSucceeded:completion:].cold.1
+ -[SFRemoteAutoFillSessionHelper clientPromptForPIN:throttleSeconds:].cold.1
+ -[SFRemoteHotspotDevice handoffActive]
+ -[SFRemoteHotspotDevice setHandoffActive:]
+ -[SFRemoteInteractionSession _activateWithCompletion:].cold.1
+ -[SFRemoteInteractionSession _activateWithCompletion:].cold.2
+ -[SFRemoteInteractionSession _ensureXPCStarted].cold.1
+ -[SFRemoteInteractionSession _interrupted].cold.1
+ -[SFRemoteInteractionSession _invalidate].cold.1
+ -[SFRemoteInteractionSession _invalidated].cold.1
+ -[SFRemoteInteractionSession _invalidated].cold.2
+ -[SFRemoteInteractionSession _sessionHandleEvent:].cold.1
+ -[SFRemoteInteractionSession _sessionHandleEvent:].cold.2
+ -[SFRemoteInteractionSession _sessionHandleEvent:].cold.3
+ -[SFRemoteInteractionSession _sessionHandleEvent:].cold.4
+ -[SFRemoteInteractionSession _sessionHandleEvent:].cold.5
+ -[SFRemoteInteractionSession _sessionHandleEvent:].cold.6
+ -[SFRemoteInteractionSession _sessionHandleEvent:].cold.7
+ -[SFRemoteInteractionSession _sessionHandleEvent:].cold.8
+ -[SFRemoteInteractionSession _sessionSendPayload:].cold.1
+ -[SFRemoteInteractionSession _sessionSendPayload:].cold.2
+ -[SFRemoteInteractionSession _sessionSendPayload:].cold.3
+ -[SFRemoteInteractionSession remoteInteractionSessionRemoteTextEvent:].cold.1
+ -[SFRemoteInteractionSession remoteInteractionSessionTextSessionDidBegin:].cold.1
+ -[SFRemoteInteractionSession remoteInteractionSessionTextSessionDidChange:].cold.1
+ -[SFRemoteInteractionSession remoteInteractionSessionTextSessionDidEnd:].cold.1
+ -[SFRemoteTextInputClient _fireEventHandlerWithPayload:].cold.1
+ -[SFRemoteTextInputClient _fireEventHandlerWithPayload:].cold.2
+ -[SFRemoteTextInputClient _handleSessionEvent:forSession:].cold.1
+ -[SFRemoteTextInputClient _handleSessionEvent:forSession:].cold.2
+ -[SFRemoteTextInputClient _handleSessionEvent:forSession:].cold.3
+ -[SFRemoteTextInputClient _handleSessionEvent:forSession:].cold.4
+ -[SFRemoteTextInputClient _handleSessionEvent:forSession:].cold.5
+ -[SFRemoteTextInputClient currentPayload].cold.1
+ -[SFRemoteTextInputClient currentPayload].cold.2
+ -[SFRemoteTextInputClient dealloc].cold.1
+ -[SFRemoteTextInputClient handleTextActionPayload:].cold.1
+ -[SFRemoteTextInputClient handleTextInputData:].cold.1
+ -[SFRemoteTextInputClient handleTextInputData:].cold.2
+ -[SFRemoteTextInputClient handleTextInputData:].cold.3
+ -[SFRemoteTextInputClient handleTextInputData:].cold.4
+ -[SFRemoteTextInputClient handleTextInputData:].cold.5
+ -[SFRemoteTextInputClient handleUsername:password:].cold.1
+ -[SFRemoteTextInputClient handleUsername:password:].cold.2
+ -[SFRemoteTextInputClient handleUsername:password:].cold.3
+ -[SFRemoteTextInputClient performTextOperations:].cold.1
+ -[SFService _sendToPeer:type:unencryptedObject:].cold.1
+ -[SFService _sendToPeer:type:unencryptedObject:].cold.2
+ -[SFService dealloc].cold.1
+ -[SFService serviceReceivedResponse:].cold.1
+ -[SFServiceSession _receivedResponseID:object:flags:].cold.1
+ -[SFServiceSession _receivedResponseID:object:flags:].cold.2
+ -[SFServiceSession dealloc].cold.1
+ -[SFServiceSession pairSetup:start:].cold.1
+ -[SFServiceSession pairSetup:start:].cold.2
+ -[SFServiceSession pairSetup:start:].cold.3
+ -[SFServiceSession pairVerify:start:].cold.1
+ -[SFServiceSession pairVerify:start:].cold.2
+ -[SFServiceSession pairVerify:start:].cold.3
+ -[SFServiceSession receivedEncryptedData:type:].cold.1
+ -[SFServiceSession receivedStartRequest:].cold.1
+ -[SFServiceSession receivedUnencryptedData:type:].cold.1
+ -[SFServiceSession sendEncryptedObject:].cold.1
+ -[SFServiceSession sendEncryptedObject:].cold.2
+ -[SFServiceSession sendEncryptedObject:].cold.3
+ -[SFServiceSession sendEncryptedObject:].cold.4
+ -[SFServiceSession sendEncryptedObject:].cold.5
+ -[SFSession _appleIDAddProof:error:].cold.1
+ -[SFSession _pairSetup:start:].cold.1
+ -[SFSession _pairSetup:start:].cold.2
+ -[SFSession _pairSetupTryPIN:].cold.1
+ -[SFSession _pairVerify:start:].cold.1
+ -[SFSession _pairVerify:start:].cold.2
+ -[SFSession _pairVerify:start:].cold.3
+ -[SFSession _sendFrameType:object:].cold.1
+ -[SFSession _sendFrameType:object:].cold.2
+ -[SFSession _sessionReceivedEncryptedData:type:].cold.1
+ -[SFSession _sessionReceivedResponseID:object:flags:].cold.1
+ -[SFSession _sessionReceivedResponseID:object:flags:].cold.2
+ -[SFSession _sessionReceivedUnencryptedData:type:].cold.1
+ -[SFSession _sessionReceivedUnencryptedData:type:].cold.2
+ -[SFSession dealloc].cold.1
+ -[SFSession sessionReceivedResponse:].cold.1
+ -[SFSession(CNJ) sendExternalIO:].cold.1
+ -[SFSessionCache _ensureStarted].cold.1
+ -[SFSessionCache _sessionWasInterrupted:].cold.1
+ -[SFSessionCache _sessionWasInvalidated:].cold.1
+ -[SFShareSheetService canShareFileURL:completion:]
+ -[SFShareSheetService shareSheetSessionEndedWithTestingSnapshot:]
+ -[SFShareSheetSessionManager canShareFileURL:completion:]
+ -[SFShareSheetSessionManager shareSheetSessionEndedWithTestingSnapshot:]
+ -[SFShareSheetSessionModeTestingSnapshot .cxx_destruct]
+ -[SFShareSheetSessionModeTestingSnapshot actionActivities]
+ -[SFShareSheetSessionModeTestingSnapshot encodeWithCoder:]
+ -[SFShareSheetSessionModeTestingSnapshot finalItemsByActivity]
+ -[SFShareSheetSessionModeTestingSnapshot hasSameResults:]
+ -[SFShareSheetSessionModeTestingSnapshot initWithCoder:]
+ -[SFShareSheetSessionModeTestingSnapshot initWithJSONInfo:]
+ -[SFShareSheetSessionModeTestingSnapshot initWithPlaceholderItems:]
+ -[SFShareSheetSessionModeTestingSnapshot isEqual:]
+ -[SFShareSheetSessionModeTestingSnapshot jsonInfo]
+ -[SFShareSheetSessionModeTestingSnapshot peopleSuggestionActivityTypes]
+ -[SFShareSheetSessionModeTestingSnapshot placeholderItemDescriptions]
+ -[SFShareSheetSessionModeTestingSnapshot setActionActivities:]
+ -[SFShareSheetSessionModeTestingSnapshot setFinalItemsByActivity:]
+ -[SFShareSheetSessionModeTestingSnapshot setPeopleSuggestionActivityTypes:]
+ -[SFShareSheetSessionModeTestingSnapshot setPlaceholderItemDescriptions:]
+ -[SFShareSheetSessionModeTestingSnapshot setShareActivities:]
+ -[SFShareSheetSessionModeTestingSnapshot setVisibleActionActivities:]
+ -[SFShareSheetSessionModeTestingSnapshot setVisibleShareActivities:]
+ -[SFShareSheetSessionModeTestingSnapshot shareActivities]
+ -[SFShareSheetSessionModeTestingSnapshot updateFromSnapshot:]
+ -[SFShareSheetSessionModeTestingSnapshot updateWithDiscoveredShareActivities:visibleShareActivities:actionActivities:visibleActionActivities:]
+ -[SFShareSheetSessionModeTestingSnapshot updateWithFinalItems:forActivityType:]
+ -[SFShareSheetSessionModeTestingSnapshot updateWithPeopleSuggestionActivityTypes:]
+ -[SFShareSheetSessionModeTestingSnapshot visibleActionActivities]
+ -[SFShareSheetSessionModeTestingSnapshot visibleShareActivities]
+ -[SFShareSheetSessionTestingSnapshot .cxx_destruct]
+ -[SFShareSheetSessionTestingSnapshot applicationBundleID]
+ -[SFShareSheetSessionTestingSnapshot checkSystemAppsAvailability]
+ -[SFShareSheetSessionTestingSnapshot currentProcessHasAppRecordEntitlement]
+ -[SFShareSheetSessionTestingSnapshot currentProcessHasAppRecordEntitlement].cold.1
+ -[SFShareSheetSessionTestingSnapshot currentProcessHasExtensionDiscoveryEntitlements]
+ -[SFShareSheetSessionTestingSnapshot currentProcessHasExtensionDiscoveryEntitlements].cold.1
+ -[SFShareSheetSessionTestingSnapshot discoverInstalledExtensions]
+ -[SFShareSheetSessionTestingSnapshot encodeWithCoder:]
+ -[SFShareSheetSessionTestingSnapshot filename]
+ -[SFShareSheetSessionTestingSnapshot hasSamePreconditions:]
+ -[SFShareSheetSessionTestingSnapshot hasSameResults:]
+ -[SFShareSheetSessionTestingSnapshot initWithCoder:]
+ -[SFShareSheetSessionTestingSnapshot initWithItems:applicationBundleID:pid:]
+ -[SFShareSheetSessionTestingSnapshot initWithJSONInfo:]
+ -[SFShareSheetSessionTestingSnapshot installedExtensions]
+ -[SFShareSheetSessionTestingSnapshot isEqual:]
+ -[SFShareSheetSessionTestingSnapshot itemDescriptions]
+ -[SFShareSheetSessionTestingSnapshot jsonInfo]
+ -[SFShareSheetSessionTestingSnapshot modeKeyForCollaboration:]
+ -[SFShareSheetSessionTestingSnapshot modeSnapshotForCollaboration:]
+ -[SFShareSheetSessionTestingSnapshot modeSnapshots]
+ -[SFShareSheetSessionTestingSnapshot pid]
+ -[SFShareSheetSessionTestingSnapshot setInstalledExtensions:]
+ -[SFShareSheetSessionTestingSnapshot setModeSnapshots:]
+ -[SFShareSheetSessionTestingSnapshot setSystemAppsAvailable:]
+ -[SFShareSheetSessionTestingSnapshot systemAppsAvailable]
+ -[SFShareSheetSessionTestingSnapshot timestamp]
+ -[SFShareSheetSessionTestingSnapshot updateFromSnapshot:]
+ -[SFShareSheetSessionTestingSnapshot updateModeSnapshot:forCollaboration:]
+ -[SFShareSheetSessionTestingSnapshot updatePreconditionsIfNeeded]
+ -[SFShareSheetSessionTestingSnapshot updateWithDiscoveredShareActivities:visibleShareActivities:actionActivities:visibleActionActivities:forCollaboration:]
+ -[SFShareSheetSessionTestingSnapshot updateWithFinalItems:forActivityType:forCollaboration:]
+ -[SFShareSheetSessionTestingSnapshot updateWithPeopleSuggestionActivityTypes:forCollaboration:]
+ -[SFShareSheetSessionTestingSnapshot updateWithPlaceholderItems:collaborationItem:supportsCollaboration:supportsSendCopy:]
+ -[SFShareSheetSessionTestingSnapshot writeSnapshotWithCompletionHandler:]
+ -[SFShareSheetSessionTestingSnapshot writeSnapshotWithCompletionHandler:].cold.1
+ -[SFShareSheetSessionTestingSnapshot writeSnapshotWithCompletionHandler:].cold.2
+ -[SFSiriClient _activate].cold.1
+ -[SFSiriClient _invalidate].cold.1
+ -[SFSiriWordTimingPlayer _processNextWord].cold.1
+ -[SFSystemService _sfServiceStart].cold.1
+ -[SFSystemSession _runSFSessionStart].cold.1
+ -[SFSystemSession _run].cold.1
+ -[SFSystemSession _run].cold.2
+ -[SFSystemSession getProfilesWithCompletion:].cold.1
+ -[SFSystemSession getSystemInfoWithCompletion:].cold.1
+ -[SFSystemSession installProfileWithData:completion:].cold.1
+ -[SFSystemSession rebootSystemWithCompletion:].cold.1
+ -[SFSystemSession removeProfileWithIdentifier:completion:].cold.1
+ -[SFUserAlert _ensureXPCStarted].cold.1
+ -[SFUserAlert _ensureXPCStarted].cold.2
+ -[SFUserAlert _interrupted].cold.1
+ -[SFUserAlert _invalidate].cold.1
+ -[SFUserAlert _invalidated].cold.1
+ -[SFUserAlert _presentBanner].cold.1
+ -[SFUserAlert createNotificationBanner].cold.1
+ -[SFUserAlert createNotificationBanner].cold.2
+ -[SFUserAlert createNotificationBanner].cold.3
+ -[SFUserAlert createNotificationBanner].cold.4
+ -[SFUserAlert createNotification].cold.1
+ -[SFUserAlert createNotification].cold.2
+ -[SFUserAlert createNotification].cold.3
+ -[SFUserAlert userNotificationCenter:didActivateNotification:].cold.1
+ -[SFUserAlert userNotificationCenter:didActivateNotification:].cold.2
+ -[SFUserAlert userNotificationCenter:didActivateNotification:].cold.3
+ -[SFUserAlert userNotificationDictionaryResponse:].cold.1
+ -[SFUserAlert userNotificationResponse:].cold.1
+ -[SFWiFiHealthMonitor _activate].cold.1
+ -[SFWiFiHealthMonitor _invalidate].cold.1
+ -[SFWiFiHealthMonitor _update].cold.1
+ -[SFWirelessSettingsController isAirDropMDMRestricted]
+ -[SFXPCClient dealloc].cold.1
+ -[SFXPCClient onqueue_getRemoteObjectProxyOnQueue:].cold.1
+ ExtensionFoundationLibrary.cold.1
+ ExtensionFoundationLibraryCore.frameworkLibrary
+ GCC_except_table140
+ GCC_except_table146
+ GCC_except_table148
+ GCC_except_table239
+ GCC_except_table246
+ GCC_except_table268
+ GCC_except_table271
+ GCC_except_table70
+ OBJC_IVAR_$_SFDeviceOperationHandlerWiFiSetup._ipAssignSecs
+ OBJC_IVAR_$_SFDeviceOperationHandlerWiFiSetup._ipAssignStartTicks
+ OBJC_IVAR_$_SFDeviceOperationHandlerWiFiSetup._ipAssigned
+ OBJC_IVAR_$_SFRemoteHotspotDevice._handoffActive
+ OBJC_IVAR_$_SFShareSheetSessionModeTestingSnapshot._actionActivities
+ OBJC_IVAR_$_SFShareSheetSessionModeTestingSnapshot._finalItemsByActivity
+ OBJC_IVAR_$_SFShareSheetSessionModeTestingSnapshot._peopleSuggestionActivityTypes
+ OBJC_IVAR_$_SFShareSheetSessionModeTestingSnapshot._placeholderItemDescriptions
+ OBJC_IVAR_$_SFShareSheetSessionModeTestingSnapshot._shareActivities
+ OBJC_IVAR_$_SFShareSheetSessionModeTestingSnapshot._visibleActionActivities
+ OBJC_IVAR_$_SFShareSheetSessionModeTestingSnapshot._visibleShareActivities
+ OBJC_IVAR_$_SFShareSheetSessionTestingSnapshot._applicationBundleID
+ OBJC_IVAR_$_SFShareSheetSessionTestingSnapshot._installedExtensions
+ OBJC_IVAR_$_SFShareSheetSessionTestingSnapshot._itemDescriptions
+ OBJC_IVAR_$_SFShareSheetSessionTestingSnapshot._modeSnapshots
+ OBJC_IVAR_$_SFShareSheetSessionTestingSnapshot._pid
+ OBJC_IVAR_$_SFShareSheetSessionTestingSnapshot._systemAppsAvailable
+ OBJC_IVAR_$_SFShareSheetSessionTestingSnapshot._timestamp
+ OBJC_IVAR_$_SFWirelessSettingsController._isAirDropMDMRestricted
+ SFAWDEnsureInitialized.cold.1
+ SFAWDSubmit.cold.1
+ SFAWDSubmit.cold.2
+ SFAWDSubmit.cold.3
+ SFAWDSubmit.cold.4
+ SFAWDSubmit.cold.5
+ SFAWDSubmit.cold.6
+ SFAirDropUrlSchemeIsSupported.cold.1
+ SFAppleIDAddCertificateToKeychain.cold.1
+ SFAppleIDAddCertificateToKeychain.cold.2
+ SFAppleIDAddCertificateToKeychain.cold.3
+ SFAppleIDAddCertificateToKeychain.cold.4
+ SFAppleIDAddCertificateToKeychain.cold.5
+ SFAppleIDAddCertificateToKeychain.cold.6
+ SFAppleIDAddCertificateToKeychain.cold.7
+ SFAppleIDCertificateAndKeyCounts.cold.1
+ SFAppleIDCertificateAndKeyCounts.cold.2
+ SFAppleIDCreateCertificateRequestPEMStringForKeyPair.cold.1
+ SFAppleIDCreateCertificateRequestPEMStringForKeyPair.cold.2
+ SFAppleIDVerifyCertificateChain.cold.1
+ SFAppleIDVerifyCertificateChain.cold.2
+ SFAppleIDVerifyCertificateChain.cold.3
+ SFBrowserCreate.cold.2
+ SFBrowserGetTypeID.cold.1
+ SFDashboardClient.cold.1
+ SFDeviceIsVirtualMachine.cold.1
+ SFDeviceModel.cold.1
+ SFDeviceModelCodeGet.cold.1
+ SFDeviceProductVersion.cold.1
+ SFDeviceSetupAppleTVLocationAuthorizationInfo.cold.1
+ SFDeviceSetupAppleTVLocationAuthorizationInfo.cold.2
+ SFDeviceSetupDeviceInfo.cold.1
+ SFDeviceSetupDeviceInfo.cold.2
+ SFDeviceSetupDeviceInfo.cold.3
+ SFDeviceSetupHomeKitCurrentUserIdentifiers.cold.1
+ SFDeviceSetupHomeKitInfo.cold.1
+ SFDeviceSetupHomeKitInfo.cold.2
+ SFDeviceSetupHomeKitInfo.cold.3
+ SFDeviceSetupHomeKitInfo.cold.4
+ SFDeviceSetupHomeKitInfo.cold.5
+ SFDeviceSetupSiriInfo.cold.1
+ SFDeviceSetupSiriInfo.cold.2
+ SFDeviceSetupSiriInfo.cold.3
+ SFDeviceSetupSiriInfo.cold.4
+ SFDeviceSetupSiriInfo.cold.5
+ SFDeviceSetupSiriInfo.cold.6
+ SFHighPriorityQueue.cold.1
+ SFHighPriorityQueue.cold.2
+ SFIsAllowedAirDropCredentialClient.cold.1
+ SFIsRunningUnitTests.cold.1
+ SFNodeCreate.cold.1
+ SFNodeCreateCopy.cold.1
+ SFNodeGetTypeID.cold.1
+ SFOperationGetTypeID.cold.1
+ SFShouldLogSensitiveDescriptions.cold.1
+ SFStoreDemoMode.cold.1
+ _CFAllocatorGetDefault
+ _ExtensionFoundationLibrary
+ _OBJC_$_PROP_LIST_SFPeopleSuggestionProxy.282
+ _OBJC_CLASS_$_SFShareSheetSessionModeTestingSnapshot
+ _OBJC_CLASS_$_SFShareSheetSessionTestingSnapshot
+ _OBJC_METACLASS_$_SFShareSheetSessionModeTestingSnapshot
+ _OBJC_METACLASS_$_SFShareSheetSessionTestingSnapshot
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_16
+ _OUTLINED_FUNCTION_17
+ _OUTLINED_FUNCTION_18
+ _OUTLINED_FUNCTION_19
+ _OUTLINED_FUNCTION_20
+ _OUTLINED_FUNCTION_21
+ _OUTLINED_FUNCTION_22
+ _OUTLINED_FUNCTION_23
+ _OUTLINED_FUNCTION_24
+ _OUTLINED_FUNCTION_25
+ _OUTLINED_FUNCTION_26
+ _OUTLINED_FUNCTION_27
+ _OUTLINED_FUNCTION_28
+ _OUTLINED_FUNCTION_29
+ _OUTLINED_FUNCTION_30
+ _OUTLINED_FUNCTION_31
+ _OUTLINED_FUNCTION_32
+ _OUTLINED_FUNCTION_33
+ _OUTLINED_FUNCTION_34
+ _OUTLINED_FUNCTION_35
+ _OUTLINED_FUNCTION_36
+ _OUTLINED_FUNCTION_37
+ _OUTLINED_FUNCTION_38
+ _OUTLINED_FUNCTION_39
+ _OUTLINED_FUNCTION_40
+ _PROTOCOLS_SFXPCInvocation.8
+ _SFAuthenticationErrorCodeDomain
+ _SFAuthenticationErrorCodeToString
+ _SFBluetoothStateToString
+ _SFDeviceSetupHomeKitCurrentUserInfoFromAllHomes.cold.1
+ _SFFilterStringsAndWebURLsFromList
+ _SFOperationCreateInternal.cold.2
+ _SFSupportsNetworkConnection
+ _SecTaskCopyValueForEntitlement
+ _SecTaskCreateFromSelf
+ _SecTaskCreateWithAuditToken
+ __106-[SFAirDropClassroomTransferManager updateTransferWithIdentifier:withState:information:completionHandler:]_block_invoke.123
+ __106-[SFAirDropClassroomTransferManager updateTransferWithIdentifier:withState:information:completionHandler:]_block_invoke.123.cold.1
+ __109-[SFAuthenticateAccountsService _validateiCloudCredentialsWithRequest:unvalidatedResponse:completionHandler:]_block_invoke.252
+ __120-[SFDeviceAssetManager onqueue_findAssetBundleForAssetQuery:ucat:queryType:fallback:retryAttempt:withCompletionHandler:]_block_invoke_2.730
+ __142-[SFShareSheetSessionModeTestingSnapshot updateWithDiscoveredShareActivities:visibleShareActivities:actionActivities:visibleActionActivities:]_block_invoke.123
+ __23-[SFSession _fetchInfo]_block_invoke.cold.1
+ __23-[SFSession _fetchInfo]_block_invoke.cold.2
+ __23-[SFSession _fetchInfo]_block_invoke.cold.3
+ __25-[SFService _interrupted]_block_invoke.426
+ __26-[SFSessionCache activate]_block_invoke.cold.1
+ __27-[SFSystemService activate]_block_invoke.cold.1
+ __27-[SFSystemSession activate]_block_invoke.cold.1
+ __27-[SFUserAlert _invalidated]_block_invoke.cold.1
+ __28-[SFSessionCache clearCache]_block_invoke.cold.1
+ __28-[SFSessionCache invalidate]_block_invoke.cold.1
+ __28-[SFWiFiHealthMonitor reset]_block_invoke.cold.1
+ __29-[SFSystemService invalidate]_block_invoke.cold.1
+ __29-[SFSystemSession invalidate]_block_invoke.cold.1
+ __29-[SFUserAlert _presentBanner]_block_invoke.cold.1
+ __30-[SFService _ensureXPCStarted]_block_invoke.409
+ __31-[SFDeviceDiscovery invalidate]_block_invoke.cold.1
+ __31-[SFDeviceSetupSessioniOS _run]_block_invoke.cold.1
+ __31-[SFPowerSourceMonitor _update]_block_invoke.137
+ __32-[SFApproveDiscovery invalidate]_block_invoke.cold.1
+ __32-[SFBLEScanner _btSessionUsable]_block_invoke.cold.1
+ __32-[SFBonjourNearBy _startBrowser]_block_invoke.156
+ __33-[SFDeviceDiscovery _interrupted]_block_invoke.cold.1
+ __33-[SFDeviceRepairService activate]_block_invoke.162
+ __33-[SFDeviceRepairService activate]_block_invoke.cold.1
+ __33-[SFDeviceRepairSession activate]_block_invoke.cold.1
+ __33-[SFSession _setupMessageSession]_block_invoke.315
+ __33-[SFSession _setupMessageSession]_block_invoke.319
+ __33-[SFSession _setupMessageSession]_block_invoke_2.320
+ __33-[SFUserAlert _postNotification:]_block_invoke.cold.1
+ __34-[SFDeviceDiscovery _retryConsole]_block_invoke.cold.1
+ __34-[SFDeviceSetupSessioniOS tryPIN:]_block_invoke.cold.1
+ __34-[SFProxHandoffService invalidate]_block_invoke.cold.1
+ __34-[SFRemoteAutoFillSession tryPIN:]_block_invoke.cold.1
+ __34-[SFService pairSetupTryPIN:peer:]_block_invoke.cold.1
+ __34-[SFSiriWordTimingPlayer activate]_block_invoke.cold.1
+ __34-[SFSystemService _sfServiceStart]_block_invoke.133
+ __34-[SFSystemService _sfServiceStart]_block_invoke.137
+ __34-[SFSystemService _sfServiceStart]_block_invoke.137.cold.1
+ __34-[SFSystemService _sfServiceStart]_block_invoke.137.cold.2
+ __35-[SFBonjourNearBy _startAdvertiser]_block_invoke.147
+ __35-[SFCoordinatedAlertRequest _start]_block_invoke.149
+ __35-[SFCoordinatedAlertRequest _start]_block_invoke_2.cold.1
+ __35-[SFDeviceRepairSession _runFinish]_block_invoke.cold.1
+ __35-[SFDeviceRepairSession _runFinish]_block_invoke_2.cold.1
+ __35-[SFDeviceRepairSession invalidate]_block_invoke.cold.1
+ __35-[SFDeviceSetupServiceiOS activate]_block_invoke.cold.1
+ __35-[SFDeviceSetupSessioniOS activate]_block_invoke.cold.1
+ __35-[SFDeviceSetupWHAService activate]_block_invoke.cold.1
+ __35-[SFDeviceSetupWHASession activate]_block_invoke.cold.1
+ __35-[SFPasswordSharingSession tryPIN:]_block_invoke.cold.1
+ __35-[SFRemoteAutoFillSession activate]_block_invoke.cold.1
+ __35-[SFRemoteAutoFillSession activate]_block_invoke.cold.2
+ __35-[SFRemoteTextInputClient activate]_block_invoke.cold.1
+ __36-[SFDeviceDiscovery fastScanCancel:]_block_invoke.cold.1
+ __36-[SFPasswordSharingService activate]_block_invoke.cold.1
+ __36-[SFPasswordSharingService activate]_block_invoke.cold.2
+ __36-[SFPasswordSharingSession _runPair]_block_invoke.cold.1
+ __36-[SFPasswordSharingSession _runPair]_block_invoke.cold.2
+ __36-[SFPasswordSharingSession activate]_block_invoke.cold.1
+ __36-[SFServiceSession pairSetup:start:]_block_invoke.937
+ __36-[SFSiriWordTimingPlayer invalidate]_block_invoke.cold.1
+ __37-[SFDeviceDiscovery fastScanTrigger:]_block_invoke.cold.1
+ __37-[SFDeviceDiscovery setDeviceFilter:]_block_invoke.cold.1
+ __37-[SFDeviceOperationCNJSetup activate]_block_invoke.cold.1
+ __37-[SFDeviceRepairSession _runCDPSetup]_block_invoke.cold.1
+ __37-[SFDeviceSetupServiceiOS invalidate]_block_invoke.cold.1
+ __37-[SFDeviceSetupSessioniOS invalidate]_block_invoke.cold.1
+ __37-[SFDeviceSetupWHAService invalidate]_block_invoke.cold.1
+ __37-[SFDeviceSetupWHASession _runFinish]_block_invoke.cold.1
+ __37-[SFDeviceSetupWHASession _runFinish]_block_invoke.cold.2
+ __37-[SFDeviceSetupWHASession invalidate]_block_invoke.cold.1
+ __37-[SFProxHandoffService _serviceStart]_block_invoke.cold.1
+ __37-[SFProxHandoffService _serviceStart]_block_invoke_2.cold.1
+ __37-[SFProxHandoffService _serviceStart]_block_invoke_3.cold.1
+ __37-[SFProxHandoffService _serviceStart]_block_invoke_4.cold.1
+ __37-[SFProxHandoffService _serviceStart]_block_invoke_5.cold.1
+ __37-[SFProxHandoffService _serviceStart]_block_invoke_6.cold.1
+ __37-[SFProxHandoffService _serviceStart]_block_invoke_6.cold.2
+ __37-[SFRemoteAutoFillService invalidate]_block_invoke.cold.1
+ __37-[SFRemoteAutoFillSession invalidate]_block_invoke.cold.1
+ __37-[SFRemoteTextInputClient invalidate]_block_invoke.cold.1
+ __37-[SFService _activateWithCompletion:]_block_invoke.327
+ __37-[SFService pairSetupWithFlags:peer:]_block_invoke.cold.1
+ __37-[SFService sendToPeer:flags:object:]_block_invoke.cold.1
+ __37-[SFSession _activateWithCompletion:]_block_invoke.166
+ __37-[SFSystemSession _runSFSessionStart]_block_invoke.cold.1
+ __37-[SFSystemSession _runSFSessionStart]_block_invoke_2.cold.1
+ __37-[SFSystemSession _runSFSessionStart]_block_invoke_2.cold.2
+ __38-[SFAppleIDClient myAccountWithError:]_block_invoke.cold.1
+ __38-[SFDeviceDiscovery _ensureXPCStarted]_block_invoke.291
+ __38-[SFDeviceRepairSession _runWiFiSetup]_block_invoke.cold.1
+ __38-[SFPasswordSharingService invalidate]_block_invoke.cold.1
+ __38-[SFPasswordSharingSession invalidate]_block_invoke.cold.1
+ __38-[SFRemoteAutoFillSession _runPairPIN]_block_invoke.cold.1
+ __38-[SFRemoteAutoFillSession _runPairPIN]_block_invoke.cold.2
+ __38-[SFRemoteAutoFillSession _runPairPIN]_block_invoke.cold.3
+ __38-[SFRemoteAutoFillSession _runPairPIN]_block_invoke.cold.4
+ __38-[SFSystemSession _runPairVerifyStart]_block_invoke.cold.1
+ __38-[SFSystemSession _runPairVerifyStart]_block_invoke.cold.2
+ __39-[SFBonjourEndpoint _handleUUIDHeaders]_block_invoke.129
+ __39-[SFContinuityRemoteSession invalidate]_block_invoke.cold.1
+ __39-[SFDeviceOperationCNJSetup invalidate]_block_invoke.cold.1
+ __39-[SFDeviceOperationWiFiSetup _activate]_block_invoke.cold.1
+ __39-[SFDeviceRepairSession _runPairVerify]_block_invoke.cold.1
+ __39-[SFDeviceRepairSession _runPairVerify]_block_invoke.cold.2
+ __39-[SFDeviceRepairSession _runPairVerify]_block_invoke.cold.3
+ __39-[SFDeviceSetupAppleTVSession activate]_block_invoke.cold.1
+ __39-[SFDeviceSetupWHASession _runCDPSetup]_block_invoke.cold.1
+ __39-[SFServiceSession pairSetupWithFlags:]_block_invoke.920
+ __39-[SFXPCClient onqueue_ensureXPCStarted]_block_invoke.128
+ __40-[SFAutoUnlockManager attemptAutoUnlock]_block_invoke.524
+ __40-[SFAutoUnlockManager attemptAutoUnlock]_block_invoke.528
+ __40-[SFDeviceAssetManager logNetworkStatus]_block_invoke.599
+ __40-[SFDeviceAssetManager logNetworkStatus]_block_invoke.606
+ __40-[SFDeviceOperationWiFiSetup _activate2]_block_invoke.238
+ __40-[SFDeviceRepairService _sfServiceStart]_block_invoke.176
+ __40-[SFDeviceRepairService _sfServiceStart]_block_invoke.180
+ __40-[SFDeviceRepairService _sfServiceStart]_block_invoke.180.cold.1
+ __40-[SFDeviceRepairSession _runGetProblems]_block_invoke.cold.1
+ __40-[SFDeviceSetupSessioniOS sendAppEvent:]_block_invoke.cold.1
+ __40-[SFNFCTagReaderUIController invalidate]_block_invoke.cold.1
+ __40-[SFRemoteAutoFillService _serviceStart]_block_invoke.241
+ __40-[SFRemoteAutoFillService _serviceStart]_block_invoke.245
+ __40-[SFRemoteAutoFillService _serviceStart]_block_invoke.245.cold.1
+ __40-[SFRemoteAutoFillService _serviceStart]_block_invoke.250
+ __40-[SFRemoteAutoFillService _serviceStart]_block_invoke.250.cold.1
+ __40-[SFRemoteAutoFillService _serviceStart]_block_invoke_2.254
+ __40-[SFRemoteAutoFillService _serviceStart]_block_invoke_2.254.cold.1
+ __40-[SFRemoteAutoFillService _serviceStart]_block_invoke_2.254.cold.2
+ __40-[SFRemoteAutoFillService _serviceStart]_block_invoke_2.254.cold.3
+ __40-[SFRemoteAutoFillService _serviceStart]_block_invoke_2.cold.1
+ __40-[SFSession _serviceInitiatedPairSetup:]_block_invoke.cold.1
+ __40-[SFSession(CNJ) registerForExternalIO:]_block_invoke.cold.1
+ __40-[SFSession(CNJ) registerForExternalIO:]_block_invoke.cold.2
+ __40-[SFShareSheetService _ensureXPCStarted]_block_invoke.124
+ __41-[SFAuthenticateAccountsSession activate]_block_invoke.cold.1
+ __41-[SFDeviceOperationCNJSetup _startClient]_block_invoke.155
+ __41-[SFDeviceOperationCNJSetup _startClient]_block_invoke.155.cold.1
+ __41-[SFDeviceSetupAppleTVSession invalidate]_block_invoke.cold.1
+ __41-[SFDeviceSetupWHASession _runPairVerify]_block_invoke.cold.1
+ __41-[SFDeviceSetupWHASession _runPairVerify]_block_invoke.cold.2
+ __41-[SFNFCTagReaderUIController setPurpose:]_block_invoke.cold.1
+ __41-[SFNFCTagReaderUIController setPurpose:]_block_invoke_2.cold.1
+ __41-[SFPINPairSession _clientSFSessionStart]_block_invoke.187
+ __41-[SFPINPairSession _clientSFSessionStart]_block_invoke.187.cold.1
+ __41-[SFPINPairSession _clientSFSessionStart]_block_invoke.cold.1
+ __41-[SFPINPairSession _clientSFSessionStart]_block_invoke_2.cold.1
+ __41-[SFPINPairSession _clientSFSessionStart]_block_invoke_3.cold.1
+ __41-[SFPINPairSession _clientSFSessionStart]_block_invoke_3.cold.2
+ __41-[SFRemoteAutoFillSession _runPairVerify]_block_invoke.cold.1
+ __41-[SFRemoteAutoFillSession _runPairVerify]_block_invoke.cold.2
+ __41-[SFRemoteAutoFillSession _runPairVerify]_block_invoke.cold.3
+ __41-[SFRemoteAutoFillSession _runPairVerify]_block_invoke.cold.4
+ __41-[SFRemoteAutoFillSession _runPairVisual]_block_invoke.cold.1
+ __41-[SFRemoteAutoFillSession _runPairVisual]_block_invoke.cold.2
+ __41-[SFRemoteAutoFillSession _runPairVisual]_block_invoke.cold.3
+ __41-[SFRemoteAutoFillSession _runPairVisual]_block_invoke.cold.4
+ __42-[SFClient repairDevice:flags:completion:]_block_invoke.cold.1
+ __42-[SFDeviceSetupServiceiOS _sfServiceStart]_block_invoke.185
+ __42-[SFDeviceSetupServiceiOS _sfServiceStart]_block_invoke.199
+ __42-[SFDeviceSetupServiceiOS _sfServiceStart]_block_invoke.203
+ __42-[SFDeviceSetupServiceiOS _sfServiceStart]_block_invoke.203.cold.1
+ __42-[SFDeviceSetupServiceiOS _sfServiceStart]_block_invoke.208
+ __42-[SFDeviceSetupServiceiOS _sfServiceStart]_block_invoke.208.cold.1
+ __42-[SFDeviceSetupServiceiOS _sfServiceStart]_block_invoke.213
+ __42-[SFDeviceSetupServiceiOS _sfServiceStart]_block_invoke.213.cold.1
+ __42-[SFDeviceSetupServiceiOS _sfServiceStart]_block_invoke.cold.1
+ __42-[SFDeviceSetupServiceiOS _sfServiceStart]_block_invoke_2.190
+ __42-[SFDeviceSetupServiceiOS _sfServiceStart]_block_invoke_2.190.cold.1
+ __42-[SFDeviceSetupServiceiOS _sfServiceStart]_block_invoke_2.215
+ __42-[SFDeviceSetupServiceiOS _sfServiceStart]_block_invoke_2.215.cold.1
+ __42-[SFDeviceSetupServiceiOS _sfServiceStart]_block_invoke_2.215.cold.2
+ __42-[SFDeviceSetupServiceiOS _sfServiceStart]_block_invoke_2.cold.1
+ __42-[SFDeviceSetupServiceiOS _sfServiceStart]_block_invoke_3.cold.1
+ __42-[SFDeviceSetupWHAService _sfServiceStart]_block_invoke.164
+ __42-[SFDeviceSetupWHAService _sfServiceStart]_block_invoke.168
+ __42-[SFDeviceSetupWHAService _sfServiceStart]_block_invoke.172
+ __42-[SFRemoteAutoFillService _discoveryStart]_block_invoke.205
+ __42-[SFRemoteAutoFillService _discoveryStart]_block_invoke.209
+ __42-[SFRemoteAutoFillService _discoveryStart]_block_invoke.209.cold.1
+ __42-[SFRemoteAutoFillService _discoveryStart]_block_invoke_2.212
+ __42-[SFRemoteAutoFillService _discoveryStart]_block_invoke_2.212.cold.1
+ __42-[SFRemoteAutoFillService _discoveryStart]_block_invoke_3.cold.1
+ __42-[SFRemoteAutoFillService _discoveryStart]_block_invoke_3.cold.2
+ __42-[SFRemoteAutoFillService _discoveryStart]_block_invoke_3.cold.3
+ __42-[SFRemoteAutoFillSession _runPairHomeKit]_block_invoke.cold.1
+ __42-[SFRemoteAutoFillSession _runPairHomeKit]_block_invoke.cold.2
+ __42-[SFRemoteAutoFillSession _runPairHomeKit]_block_invoke.cold.3
+ __42-[SFRemoteAutoFillSession _runPairHomeKit]_block_invoke.cold.4
+ __42-[SFRemoteInteractionSession _interrupted]_block_invoke.cold.1
+ __43-[SFAuthenticateAccountsSession _runFinish]_block_invoke.cold.1
+ __43-[SFAuthenticateAccountsSession _runFinish]_block_invoke.cold.2
+ __43-[SFAuthenticateAccountsSession _runFinish]_block_invoke_2.cold.1
+ __43-[SFAuthenticateAccountsSession invalidate]_block_invoke.cold.1
+ __43-[SFDeviceRepairSession _runSFSessionStart]_block_invoke.191
+ __43-[SFDeviceSetupAppleTVSession _runCDPSetup]_block_invoke.cold.1
+ __43-[SFDeviceSetupSessioniOS _runCoreCDPSetup]_block_invoke_2.cold.1
+ __43-[SFPINPairSession _clientPairSetup:start:]_block_invoke.cold.1
+ __43-[SFRemoteAutoFillSession _runPairContacts]_block_invoke.cold.1
+ __43-[SFRemoteAutoFillSession _runPairContacts]_block_invoke.cold.2
+ __43-[SFRemoteAutoFillSession _runPairContacts]_block_invoke.cold.3
+ __43-[SFRemoteAutoFillSession _runPairContacts]_block_invoke.cold.4
+ __43-[SFRemoteAutoFillSession _runSessionStart]_block_invoke.169
+ __43-[SFRemoteAutoFillSession _runSessionStart]_block_invoke.169.cold.1
+ __43-[SFRemoteAutoFillSession _runSessionStart]_block_invoke.177
+ __43-[SFRemoteAutoFillSession _runSessionStart]_block_invoke.181
+ __43-[SFRemoteAutoFillSession _runSessionStart]_block_invoke.181.cold.1
+ __43-[SFRemoteAutoFillSession _runSessionStart]_block_invoke.181.cold.2
+ __43-[SFRemoteAutoFillSession _runSessionStart]_block_invoke.cold.1
+ __43-[SFRemoteAutoFillSession _runSessionStart]_block_invoke_2.cold.1
+ __43-[SFUnlockManager disableUnlockWithDevice:]_block_invoke.144
+ __44-[SFAppleIDClient _myAccountWithCompletion:]_block_invoke_2.cold.1
+ __44-[SFAuthenticationManager isEnabledForType:]_block_invoke.383
+ __44-[SFClient activateAssertionWithIdentifier:]_block_invoke.cold.1
+ __44-[SFClient activateAssertionWithIdentifier:]_block_invoke.cold.2
+ __44-[SFContinuityRemoteSession _sfSessionStart]_block_invoke.cold.1
+ __44-[SFContinuityRemoteSession _sfSessionStart]_block_invoke_2.cold.1
+ __44-[SFContinuityRemoteSession _sfSessionStart]_block_invoke_2.cold.2
+ __44-[SFDeviceOperationHandlerCNJSetup activate]_block_invoke.cold.1
+ __44-[SFDeviceOperationHandlerCNJSetup activate]_block_invoke.cold.2
+ __44-[SFPINPairSession _clientPairVerify:start:]_block_invoke.cold.1
+ __44-[SFPasswordSharingService _runServiceStart]_block_invoke.185
+ __44-[SFPasswordSharingService _runServiceStart]_block_invoke.189
+ __44-[SFPasswordSharingService _runServiceStart]_block_invoke.189.cold.1
+ __44-[SFPasswordSharingService _runServiceStart]_block_invoke.194
+ __44-[SFPasswordSharingService _runServiceStart]_block_invoke.194.cold.1
+ __44-[SFPasswordSharingService _runServiceStart]_block_invoke.cold.1
+ __44-[SFPasswordSharingService _runServiceStart]_block_invoke_2.196
+ __44-[SFPasswordSharingService _runServiceStart]_block_invoke_2.196.cold.1
+ __44-[SFPasswordSharingService _runServiceStart]_block_invoke_2.196.cold.2
+ __44-[SFPasswordSharingService _runServiceStart]_block_invoke_2.cold.1
+ __44-[WPBonjourNearBy _listenForSFBonjourEvents]_block_invoke.130
+ __44-[WPBonjourNearBy _listenForSFBonjourEvents]_block_invoke.144
+ __44-[WPBonjourNearBy _listenForSFBonjourEvents]_block_invoke.145
+ __44-[WPBonjourNearBy _listenForSFBonjourEvents]_block_invoke.155
+ __44-[WPBonjourNearBy _listenForSFBonjourEvents]_block_invoke.161
+ __44-[WPBonjourNearBy _listenForSFBonjourEvents]_block_invoke.167
+ __45-[SFApproveDiscovery _discoveryEnsureStarted]_block_invoke.131
+ __45-[SFApproveDiscovery _discoveryEnsureStarted]_block_invoke.135
+ __45-[SFApproveDiscovery _discoveryEnsureStarted]_block_invoke.135.cold.1
+ __45-[SFApproveDiscovery _discoveryEnsureStarted]_block_invoke_2.137
+ __45-[SFApproveDiscovery activateWithCompletion:]_block_invoke.cold.1
+ __45-[SFDeviceDiscovery _activateWithCompletion:]_block_invoke.206
+ __45-[SFDeviceOperationHandlerWiFiSetup activate]_block_invoke.cold.1
+ __45-[SFDeviceRepairService invalidateWithFlags:]_block_invoke.cold.1
+ __45-[SFDeviceRepairService invalidateWithFlags:]_block_invoke.cold.2
+ __45-[SFDeviceSetupSessioniOS _runSFSessionStart]_block_invoke.194
+ __45-[SFDeviceSetupSessioniOS _runSFSessionStart]_block_invoke.198
+ __45-[SFDeviceSetupSessioniOS _runSFSessionStart]_block_invoke.198.cold.1
+ __45-[SFDeviceSetupSessioniOS _runSFSessionStart]_block_invoke.cold.1
+ __45-[SFDeviceSetupSessioniOS _runSFSessionStart]_block_invoke_2.cold.1
+ __45-[SFDeviceSetupSessioniOS _runSFSessionStart]_block_invoke_3.cold.1
+ __45-[SFDeviceSetupWHASession _runSFSessionStart]_block_invoke.153
+ __45-[SFDeviceSetupWHASession _runSFSessionStart]_block_invoke.cold.1
+ __45-[SFProximityClient requestScannerTimerReset]_block_invoke.cold.1
+ __45-[SFProximityClient requestScannerTimerReset]_block_invoke.cold.2
+ __45-[SFRemoteAutoFillSessionHelper _interrupted]_block_invoke.cold.1
+ __45-[SFSystemSession getProfilesWithCompletion:]_block_invoke.167
+ __46-[SFAirDropTransfer setUpProgressToBroadcast:]_block_invoke.152
+ __46-[SFAuthenticateAccountsSession _runRepairCDP]_block_invoke.cold.1
+ __46-[SFAuthenticateAccountsSession _runRepairCDP]_block_invoke.cold.2
+ __46-[SFAutoUnlockManager mockedAttemptAutoUnlock]_block_invoke.503
+ __46-[SFAutoUnlockManager mockedAttemptAutoUnlock]_block_invoke.510
+ __46-[SFAutoUnlockManager mockedAttemptAutoUnlock]_block_invoke.511
+ __46-[SFDeviceDiscovery triggerEnhancedDiscovery:]_block_invoke.cold.1
+ __46-[SFDeviceOperationHandlerCDPSetup _handleCDP]_block_invoke_2.cold.1
+ __46-[SFDeviceOperationHandlerCDPSetup _repairCDP]_block_invoke_2.cold.1
+ __46-[SFDeviceOperationHandlerCDPSetup invalidate]_block_invoke.cold.1
+ __46-[SFDeviceOperationHandlerCNJSetup invalidate]_block_invoke.cold.1
+ __46-[SFDeviceOperationHandlerWiFiSetup _activate]_block_invoke.436
+ __46-[SFDeviceSetupAppleTVService _sfServiceStart]_block_invoke.151
+ __46-[SFDeviceSetupAppleTVService _sfServiceStart]_block_invoke.155
+ __46-[SFPasswordSharingSession _runSFSessionStart]_block_invoke.143
+ __46-[SFPasswordSharingSession _runSFSessionStart]_block_invoke.143.cold.1
+ __46-[SFPasswordSharingSession _runSFSessionStart]_block_invoke.151
+ __46-[SFPasswordSharingSession _runSFSessionStart]_block_invoke.155
+ __46-[SFPasswordSharingSession _runSFSessionStart]_block_invoke.155.cold.1
+ __46-[SFPasswordSharingSession _runSFSessionStart]_block_invoke.155.cold.2
+ __46-[SFPasswordSharingSession _runSFSessionStart]_block_invoke.cold.1
+ __46-[SFPasswordSharingSession _runSFSessionStart]_block_invoke_2.cold.1
+ __46-[SFRemoteAutoFillService _systemMonitorStart]_block_invoke_2.cold.1
+ __46-[SFRemoteAutoFillService _systemMonitorStart]_block_invoke_3.cold.1
+ __46-[SFRemoteAutoFillService _systemMonitorStart]_block_invoke_3.cold.2
+ __46-[SFRemoteAutoFillSessionHelper serverTryPIN:]_block_invoke.cold.1
+ __47-[SFAuthenticateAccountsSession _runPairVerify]_block_invoke.cold.1
+ __47-[SFAuthenticateAccountsSession _runPairVerify]_block_invoke.cold.2
+ __47-[SFDeviceOperationHandlerWiFiSetup invalidate]_block_invoke.cold.1
+ __47-[SFDeviceOperationWiFiSetup _bonjourTestStart]_block_invoke.263
+ __47-[SFDeviceOperationWiFiSetup _bonjourTestStart]_block_invoke.274
+ __47-[SFDeviceRepairService _handleSessionStarted:]_block_invoke.242
+ __47-[SFDeviceSetupSessioniOS _runPreAuthPairSetup]_block_invoke.cold.1
+ __47-[SFNFCTagReaderUIController _ensureXPCStarted]_block_invoke.151
+ __47-[SFNFCTagReaderUIController _ensureXPCStarted]_block_invoke.173
+ __47-[SFNFCTagReaderUIController _ensureXPCStarted]_block_invoke.173.cold.1
+ __47-[SFNFCTagReaderUIController _ensureXPCStarted]_block_invoke_2.176
+ __47-[SFNFCTagReaderUIController _ensureXPCStarted]_block_invoke_2.176.cold.1
+ __47-[SFNFCTagReaderUIController _ensureXPCStarted]_block_invoke_2.cold.1
+ __47-[SFNFCTagReaderUIController _ensureXPCStarted]_block_invoke_2.cold.2
+ __47-[SFSystemSession getSystemInfoWithCompletion:]_block_invoke.159
+ __48-[SFAppleIDClient copyIdentityForAppleID:error:]_block_invoke.cold.1
+ __48-[SFAppleIDClient copyIdentityForAppleID:error:]_block_invoke.cold.2
+ __48-[SFAppleIDClient copyIdentityForAppleID:error:]_block_invoke.cold.3
+ __48-[SFAuthenticateAccountsService _sfServiceStart]_block_invoke.174
+ __48-[SFAuthenticateAccountsService _sfServiceStart]_block_invoke.178
+ __48-[SFAuthenticateAccountsService _sfServiceStart]_block_invoke.182
+ __48-[SFCompanionXPCManager onQueue_setupConnection]_block_invoke.354
+ __48-[SFDeviceOperationCDPSetup _runCDPSetupRequest]_block_invoke.cold.1
+ __48-[SFDeviceOperationCDPSetup _runCDPSetupRequest]_block_invoke.cold.2
+ __48-[SFSessionCache sendWithFlags:object:toDevice:]_block_invoke_2.cold.1
+ __49-[SFDeviceAssetManager purgeAssetsMatchingQuery:]_block_invoke.cold.1
+ __49-[SFDeviceSetupAppleTVSession _runSFSessionStart]_block_invoke.222
+ __49-[SFDeviceSetupAppleTVSession _runSFSessionStart]_block_invoke.235
+ __49-[SFDeviceSetupAppleTVSession _runSFSessionStart]_block_invoke_3.cold.1
+ __49-[SFNFCTagReaderUIController _nfcTagScannedCount]_block_invoke.cold.1
+ __50-[SFWiFiHealthMonitor _wifiStatusChangedInternal:]_block_invoke.cold.1
+ __51-[SFAuthenticateAccountsSession _runSFSessionStart]_block_invoke.173
+ __51-[SFAuthenticateAccountsSession _runSFSessionStart]_block_invoke.180
+ __51-[SFAuthenticateAccountsSession _runSFSessionStart]_block_invoke.cold.1
+ __51-[SFDeviceOperationHandlerWiFiSetup _runJoinStart:]_block_invoke.cold.1
+ __52-[SFContinuityRemoteSession activateWithCompletion:]_block_invoke.cold.1
+ __52-[SFDeviceSetupSessioniOS _handleSetupPeerSuspended]_block_invoke.341
+ __52-[SFDeviceSetupSessioniOS _handleSetupPeerSuspended]_block_invoke.341.cold.1
+ __52-[SFRemoteAutoFillScanAction performWithCompletion:]_block_invoke.cold.1
+ __52-[SFRemoteAutoFillScanAction performWithCompletion:]_block_invoke.cold.2
+ __52-[SFUserAlert _handleResponseForNotification:flags:]_block_invoke.129
+ __52-[SFUserAlert _handleResponseForNotification:flags:]_block_invoke.130
+ __53-[SFDeviceSetupAppleTVService _handleSessionStarted:]_block_invoke.196
+ __53-[SFSession _pairSetupWithFlags:completion:isServer:]_block_invoke.360
+ __53-[SFSystemSession installProfileWithData:completion:]_block_invoke.181
+ __54+[SFRemoteAutoFillScanAction actionForURL:completion:]_block_invoke.cold.1
+ __54-[SFDeviceAssetManager onqueue_sharingManagementAsset]_block_invoke.752
+ __54-[SFDeviceSetupAppleTVSession _runPairSetupWithFlags:]_block_invoke.cold.1
+ __54-[SFNFCTagReaderUIController _activateWithCompletion:]_block_invoke.144
+ __54-[SFNFCTagReaderUIController _activateWithCompletion:]_block_invoke.144.cold.1
+ __54-[SFNFCTagReaderUIController _activateWithCompletion:]_block_invoke.144.cold.2
+ __54-[SFNFCTagReaderUIController _activateWithCompletion:]_block_invoke.cold.1
+ __54-[SFRemoteInteractionSession _activateWithCompletion:]_block_invoke.136
+ __54-[SFRemoteInteractionSession _activateWithCompletion:]_block_invoke.143
+ __54-[SFRemoteInteractionSession _activateWithCompletion:]_block_invoke.147
+ __55+[SFPasswordSharingService passwordSharingAvailability]_block_invoke.cold.1
+ __55-[SFDeviceOperationCDPSetup _runCDPApprovalServerStart]_block_invoke_2.cold.1
+ __57-[SFDeviceAssetManager onqueue_purgeAssetsMatchingQuery:]_block_invoke.cold.1
+ __57-[SFDeviceAssetManager onqueue_purgeAssetsMatchingQuery:]_block_invoke.cold.2
+ __57-[SFDeviceAssetManager onqueue_purgeAssetsMatchingQuery:]_block_invoke_2.cold.1
+ __58-[SFAppleIDClient _copyIdentityForAppleID:withCompletion:]_block_invoke_2.cold.1
+ __58-[SFAppleIDClient _copyIdentityForAppleID:withCompletion:]_block_invoke_2.cold.2
+ __58-[SFAppleIDClient _copyIdentityForAppleID:withCompletion:]_block_invoke_2.cold.3
+ __58-[SFDeviceAssetManager onqueue_executeNextMAQueryForTask:]_block_invoke.cold.1
+ __58-[SFDeviceOperationHandlerWiFiSetup _runIP4AvailableStart]_block_invoke.501
+ __58-[SFDeviceOperationHandlerWiFiSetup _runIP4AvailableStart]_block_invoke.501.cold.1
+ __58-[SFDeviceOperationHandlerWiFiSetup _runIP4AvailableStart]_block_invoke.507
+ __58-[SFDeviceOperationHandlerWiFiSetup _runIP4AvailableStart]_block_invoke.507.cold.1
+ __58-[SFDeviceOperationHandlerWiFiSetup _runIP4AvailableStart]_block_invoke.511
+ __58-[SFDeviceOperationHandlerWiFiSetup _runIP4AvailableStart]_block_invoke.511.cold.1
+ __58-[SFDeviceOperationHandlerWiFiSetup _runIP4AvailableStart]_block_invoke.cold.1
+ __58-[SFDeviceOperationHandlerWiFiSetup _runReachabilityStart]_block_invoke.cold.1
+ __58-[SFDeviceOperationHandlerWiFiSetup _runReachabilityStart]_block_invoke.cold.2
+ __58-[SFDeviceSetupAppleTVSession _videoSubscriberAccountData]_block_invoke.cold.1
+ __58-[SFDeviceSetupAppleTVSession _videoSubscriberAccountData]_block_invoke.cold.2
+ __58-[SFUnlockManager unlockStateForDevice:completionHandler:]_block_invoke.167
+ __58-[SFUnlockManager unlockStateForDevice:completionHandler:]_block_invoke.174
+ __58-[SFUnlockManager unlockStateForDevice:completionHandler:]_block_invoke_2.168
+ __59-[SFAutoUnlockManager authPromptInfoWithCompletionHandler:]_block_invoke.628
+ __59-[SFAutoUnlockManager enableAutoUnlockWithDevice:passcode:]_block_invoke.447
+ __59-[SFAutoUnlockManager enableAutoUnlockWithDevice:passcode:]_block_invoke.454
+ __60-[SFAutoUnlockManager autoUnlockStateWithCompletionHandler:]_block_invoke.618
+ __60-[SFAutoUnlockManager autoUnlockStateWithCompletionHandler:]_block_invoke.622
+ __60-[SFCompanionXPCManager unlockManagerWithCompletionHandler:]_block_invoke.372
+ __61-[SFAppleIDClient _copyCertificateForAppleID:withCompletion:]_block_invoke.223
+ __61-[SFAppleIDClient _copyCertificateForAppleID:withCompletion:]_block_invoke.223.cold.1
+ __61-[SFAppleIDClient _copyCertificateForAppleID:withCompletion:]_block_invoke.223.cold.2
+ __61-[SFAppleIDClient _copyCertificateForAppleID:withCompletion:]_block_invoke.223.cold.3
+ __61-[SFSessionCache _sessionWithDevice:activate:withCompletion:]_block_invoke.160
+ __61-[SFSessionCache _sessionWithDevice:activate:withCompletion:]_block_invoke.167
+ __61-[SFSessionCache _sessionWithDevice:activate:withCompletion:]_block_invoke_2.161
+ __61-[SFSessionCache _sessionWithDevice:activate:withCompletion:]_block_invoke_3.cold.1
+ __61-[SFSessionCache _sessionWithDevice:activate:withCompletion:]_block_invoke_3.cold.2
+ __62-[SFActivityAdvertiser advertiseAdvertisementPayload:options:]_block_invoke.134
+ __62-[SFActivityAdvertiser advertiseAdvertisementPayload:options:]_block_invoke.134.cold.1
+ __62-[SFActivityAdvertiser advertiseAdvertisementPayload:options:]_block_invoke.134.cold.2
+ __62-[SFBonjourNearBy _handleConnection:isAdvToBrowserConnection:]_block_invoke.178
+ __62-[SFBonjourNearBy _handleConnection:isAdvToBrowserConnection:]_block_invoke.185
+ __62-[SFBonjourNearBy _handleConnection:isAdvToBrowserConnection:]_block_invoke.185.cold.1
+ __62-[SFBonjourNearBy _handleConnection:isAdvToBrowserConnection:]_block_invoke.185.cold.2
+ __62-[SFDeviceRepairService _handleFinishRequest:responseHandler:]_block_invoke.cold.1
+ __64-[SFDeviceAssetManager variantsMatchingQuery:completionHandler:]_block_invoke.cold.1
+ __65-[SFCompanionXPCManager streamsForMessage:withCompletionHandler:]_block_invoke.365
+ __65-[SFDeviceDiscovery triggerEnhancedDiscovery:useCase:completion:]_block_invoke.cold.1
+ __66-[SFRemoteAutoFillSessionHelper serverUserNotificationDidDismiss:]_block_invoke.cold.1
+ __67-[SFAuthenticationManager receivedApproveRequestForSessionID:info:]_block_invoke.467
+ __67-[SFAuthenticationManager receivedApproveRequestForSessionID:info:]_block_invoke_2.468
+ __67-[SFAuthenticationManager receivedApproveRequestForSessionID:info:]_block_invoke_2.468.cold.1
+ __67-[SFAuthenticationManager receivedApproveRequestForSessionID:info:]_block_invoke_3.469
+ __67-[SFAuthenticationManager receivedApproveRequestForSessionID:info:]_block_invoke_3.469.cold.1
+ __67-[SFRemoteAutoFillSessionHelper serverUserNotificationDidActivate:]_block_invoke.cold.1
+ __67-[SFUnlockManager establishStashBagWithManifest:completionHandler:]_block_invoke.161
+ __68-[SFAutoUnlockManager disableAutoUnlockForDevice:completionHandler:]_block_invoke.467
+ __68-[SFDeviceAssetManager onqueue_updateMetaDataWithCompletionHandler:]_block_invoke.629
+ __69-[SFAuthenticateAccountsService _handleInfoExchange:responseHandler:]_block_invoke.243
+ __69-[SFAuthenticateAccountsService _handleInfoExchange:responseHandler:]_block_invoke.243.cold.1
+ __69-[SFDeviceOperationHandlerCNJSetup _runReachability:responseHandler:]_block_invoke.cold.1
+ __69-[SFDeviceOperationHandlerCNJSetup _runReachability:responseHandler:]_block_invoke.cold.2
+ __69-[SFDeviceOperationHandlerCNJSetup _runReachability:responseHandler:]_block_invoke.cold.3
+ __69-[SFDeviceOperationHandlerCNJSetup _runReachability:responseHandler:]_block_invoke.cold.4
+ __70-[SFAutoUnlockManager eligibleAutoUnlockDevicesWithCompletionHandler:]_block_invoke.418
+ __70-[SFAutoUnlockManager eligibleAutoUnlockDevicesWithCompletionHandler:]_block_invoke.423
+ __70-[SFAutoUnlockManager eligibleAutoUnlockDevicesWithCompletionHandler:]_block_invoke_2.419
+ __70-[SFRemoteAutoFillSessionHelper serverDidPickUsername:password:error:]_block_invoke.cold.1
+ __71-[SFDeviceAssetManager onqueue_updateSharingManagementAssetIfNecessary]_block_invoke.636
+ __71-[SFDeviceAssetManager onqueue_updateSharingManagementAssetIfNecessary]_block_invoke.636.cold.1
+ __71-[SFDeviceAssetManager onqueue_updateSharingManagementAssetIfNecessary]_block_invoke_2.637
+ __71-[SFSessionCache sendRequestWithFlags:object:responseHandler:toDevice:]_block_invoke_2.cold.1
+ __72-[SFAuthenticationManager listEligibleDevicesForType:completionHandler:]_block_invoke.398
+ __72-[SFDeviceAssetManager onqueue_variantsMatchingQuery:completionHandler:]_block_invoke.652
+ __72-[SFDeviceAssetManager onqueue_variantsMatchingQuery:completionHandler:]_block_invoke_2.653
+ __73-[SFAuthenticationManager listCandidateDevicesForType:completionHandler:]_block_invoke.403
+ __74-[SFDeviceAssetManager mappedProductTypeForProductType:completionHandler:]_block_invoke.cold.1
+ __77-[SFCompanionXPCManager remoteHotspotSessionForClient:withCompletionHandler:]_block_invoke.376
+ __78-[SFDeviceAssetManager getAssetBundleForDeviceQuery:withRequestConfiguration:]_block_invoke.cold.1
+ __81-[SFUnlockManager enableUnlockWithDevice:fromKey:withPasscode:completionHandler:]_block_invoke.133
+ __81-[SFUnlockManager enableUnlockWithDevice:fromKey:withPasscode:completionHandler:]_block_invoke.140
+ __81-[SFUnlockManager enableUnlockWithDevice:fromKey:withPasscode:completionHandler:]_block_invoke_2.134
+ __84-[SFAuthenticationHintsProvider authenticateAccountWithAppleID:password:completion:]_block_invoke.166
+ __84-[SFAuthenticationHintsProvider authenticateAccountWithAppleID:password:completion:]_block_invoke.168
+ __87-[SFCompanionXPCManager serviceManagerProxyForIdentifier:client:withCompletionHandler:]_block_invoke.361
+ __99-[SFDeviceOperationHandlerCNJSetup _handleCaptiveJoinRequestWithResponseHandler:reachabilityError:]_block_invoke_2.cold.1
+ __MergedGlobals
+ __OBJC_$_CLASS_METHODS_SFShareSheetSessionModeTestingSnapshot
+ __OBJC_$_CLASS_METHODS_SFShareSheetSessionTestingSnapshot
+ __OBJC_$_CLASS_PROP_LIST_SFShareSheetSessionModeTestingSnapshot
+ __OBJC_$_CLASS_PROP_LIST_SFShareSheetSessionTestingSnapshot
+ __OBJC_$_INSTANCE_METHODS_SFShareSheetSessionModeTestingSnapshot
+ __OBJC_$_INSTANCE_METHODS_SFShareSheetSessionTestingSnapshot
+ __OBJC_$_INSTANCE_VARIABLES_SFShareSheetSessionModeTestingSnapshot
+ __OBJC_$_INSTANCE_VARIABLES_SFShareSheetSessionTestingSnapshot
+ __OBJC_$_PROP_LIST_SFShareSheetSessionModeTestingSnapshot
+ __OBJC_$_PROP_LIST_SFShareSheetSessionTestingSnapshot
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SFActivityItemsService
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SFActivityItemsService
+ __OBJC_$_PROTOCOL_REFS_SFActivityItemsService
+ __OBJC_CLASS_PROTOCOLS_$_SFShareSheetSessionModeTestingSnapshot
+ __OBJC_CLASS_PROTOCOLS_$_SFShareSheetSessionTestingSnapshot
+ __OBJC_CLASS_RO_$_SFShareSheetSessionModeTestingSnapshot
+ __OBJC_CLASS_RO_$_SFShareSheetSessionTestingSnapshot
+ __OBJC_LABEL_PROTOCOL_$_SFActivityItemsService
+ __OBJC_METACLASS_RO_$_SFShareSheetSessionModeTestingSnapshot
+ __OBJC_METACLASS_RO_$_SFShareSheetSessionTestingSnapshot
+ __OBJC_PROTOCOL_$_SFActivityItemsService
+ __SFAWDEnsureInitialized_block_invoke.cold.1
+ __SFAWDEnsureInitialized_block_invoke.cold.2
+ __SFAppleIDClientCopyCertificateInfo_block_invoke.299
+ __SFAppleIDClientCopyCertificate_block_invoke.293
+ __SFAppleIDClientCopyIdentity_block_invoke.303
+ __SFAppleIDClientCopyMyAccountInfo_block_invoke.306
+ __SFAppleIDCreateKeyPair_block_invoke.182
+ __SFAppleIDParseValidationRecordData_block_invoke.193
+ __SFAppleIDVerifyCertificateChain_block_invoke.199
+ __SFAppleIDVerifyCertificateChain_block_invoke.cold.1
+ __SFCurrentAppIconData_block_invoke.570
+ ___142-[SFShareSheetSessionModeTestingSnapshot updateWithDiscoveredShareActivities:visibleShareActivities:actionActivities:visibleActionActivities:]_block_invoke
+ ___142-[SFShareSheetSessionModeTestingSnapshot updateWithDiscoveredShareActivities:visibleShareActivities:actionActivities:visibleActionActivities:]_block_invoke_2
+ ___142-[SFShareSheetSessionModeTestingSnapshot updateWithDiscoveredShareActivities:visibleShareActivities:actionActivities:visibleActionActivities:]_block_invoke_3
+ ___46-[SFShareSheetSessionTestingSnapshot jsonInfo]_block_invoke
+ ___51+[SFShareSheetSessionTestingSnapshot dateFormatter]_block_invoke
+ ___53-[SFShareSheetSessionTestingSnapshot hasSameResults:]_block_invoke
+ ___55-[SFShareSheetSessionTestingSnapshot initWithJSONInfo:]_block_invoke
+ ___57-[SFShareSheetSessionManager canShareFileURL:completion:]_block_invoke
+ ___57-[SFShareSheetSessionTestingSnapshot updateFromSnapshot:]_block_invoke
+ ___75-[SFShareSheetSessionTestingSnapshot currentProcessHasAppRecordEntitlement]_block_invoke
+ ___85-[SFShareSheetSessionTestingSnapshot currentProcessHasExtensionDiscoveryEntitlements]_block_invoke
+ ___ExtensionFoundationLibraryCore_block_invoke
+ ___block_descriptor_40_e8_32bs_e18_v16?0"NSNumber"8l
+ ___block_descriptor_40_e8_32s_e39_v32?0"<SFShareSheetActivity>"8Q16^B24l
+ ___block_descriptor_40_e8_32s_e39_v32?0"NSString"8"NSDictionary"16^B24l
+ ___block_descriptor_40_e8_32s_e65_v32?0"NSString"8"SFShareSheetSessionModeTestingSnapshot"16^B24l
+ ___block_descriptor_48_e8_32s40bs_e30_v16?0"NSObject<OS_nw_path>"8l
+ ___block_descriptor_48_e8_32s40r_e65_v32?0"NSString"8"SFShareSheetSessionModeTestingSnapshot"16^B24l
+ ___block_descriptor_48_e8_32s40s_e65_v32?0"NSString"8"SFShareSheetSessionModeTestingSnapshot"16^B24l
+ ___getSWCollaborationMetadataForDocumentURLSymbolLoc_block_invoke
+ ___getSWPerformActionForDocumentURLSymbolLoc_block_invoke
+ ___get_EXQueryClass_block_invoke
+ ___get_EXQueryControllerClass_block_invoke
+ ___swift_async_entry_functlets
+ ___swift_async_ret_functlets
+ ___swift_project_boxed_opaque_existential_0
+ __block_descriptor_tmp.303
+ __block_descriptor_tmp.314
+ __block_descriptor_tmp.369
+ __block_literal_global.1005
+ __block_literal_global.1151
+ __block_literal_global.1155
+ __block_literal_global.1167
+ __block_literal_global.127
+ __block_literal_global.129
+ __block_literal_global.138
+ __block_literal_global.153
+ __block_literal_global.159
+ __block_literal_global.166
+ __block_literal_global.168
+ __block_literal_global.180
+ __block_literal_global.182
+ __block_literal_global.188
+ __block_literal_global.189
+ __block_literal_global.205
+ __block_literal_global.216
+ __block_literal_global.220
+ __block_literal_global.226
+ __block_literal_global.230
+ __block_literal_global.232
+ __block_literal_global.236
+ __block_literal_global.240
+ __block_literal_global.244
+ __block_literal_global.246
+ __block_literal_global.252
+ __block_literal_global.257
+ __block_literal_global.265
+ __block_literal_global.269
+ __block_literal_global.278
+ __block_literal_global.281
+ __block_literal_global.287
+ __block_literal_global.291
+ __block_literal_global.301
+ __block_literal_global.318
+ __block_literal_global.324
+ __block_literal_global.339
+ __block_literal_global.344
+ __block_literal_global.346
+ __block_literal_global.372
+ __block_literal_global.376
+ __block_literal_global.381
+ __block_literal_global.382
+ __block_literal_global.383
+ __block_literal_global.389
+ __block_literal_global.397
+ __block_literal_global.402
+ __block_literal_global.415
+ __block_literal_global.417
+ __block_literal_global.419
+ __block_literal_global.422
+ __block_literal_global.424
+ __block_literal_global.426
+ __block_literal_global.429
+ __block_literal_global.434
+ __block_literal_global.436
+ __block_literal_global.459
+ __block_literal_global.461
+ __block_literal_global.471
+ __block_literal_global.474
+ __block_literal_global.483
+ __block_literal_global.488
+ __block_literal_global.509
+ __block_literal_global.513
+ __block_literal_global.517
+ __block_literal_global.521
+ __block_literal_global.532
+ __block_literal_global.534
+ __block_literal_global.536
+ __block_literal_global.696
+ __block_literal_global.698
+ __block_literal_global.750
+ __block_literal_global.754
+ __block_literal_global.758
+ __block_literal_global.759
+ __block_literal_global.763
+ __block_literal_global.768
+ __block_literal_global.782
+ __block_literal_global.810
+ __block_literal_global.867
+ __block_literal_global.871
+ __block_literal_global.877
+ __block_literal_global.881
+ __block_literal_global.888
+ __block_literal_global.895
+ __block_literal_global.900
+ __block_literal_global.971
+ __block_literal_global.975
+ __block_literal_global.982
+ __get_EXQueryClass_block_invoke.cold.1
+ __get_EXQueryControllerClass_block_invoke.cold.1
+ __notificationResponseHandler_block_invoke.cold.1
+ _audit_stringExtensionFoundation
+ _get_EXQueryClass
+ _kSFOperationAirDropMDMRestrictedKey
+ _nw_path_get_status
+ _nw_path_monitor_cancel
+ _nw_path_monitor_create_with_type
+ _nw_path_monitor_set_queue
+ _nw_path_monitor_set_update_handler
+ _nw_path_monitor_start
+ _objc_msgSend$URLByAppendingPathExtension:
+ _objc_msgSend$_itemDescriptions:match:
+ _objc_msgSend$_jsonifyItems:
+ _objc_msgSend$actionActivities
+ _objc_msgSend$applicationBundleID
+ _objc_msgSend$applicationState
+ _objc_msgSend$canShareFileURL:
+ _objc_msgSend$canShareFileURL:completion:
+ _objc_msgSend$checkSystemAppsAvailability
+ _objc_msgSend$codableDataStringForItem:
+ _objc_msgSend$createWiFiRetryMetricEventForIPAssign:duration:
+ _objc_msgSend$currentProcessHasAppRecordEntitlement
+ _objc_msgSend$currentProcessHasExtensionDiscoveryEntitlements
+ _objc_msgSend$dataWithJSONObject:options:error:
+ _objc_msgSend$dateFormatter
+ _objc_msgSend$descriptionForItem:
+ _objc_msgSend$discoverInstalledExtensions
+ _objc_msgSend$executeQueries:
+ _objc_msgSend$extensionPointIdentifier
+ _objc_msgSend$filename
+ _objc_msgSend$finalItemsByActivity
+ _objc_msgSend$handoffActive
+ _objc_msgSend$hasSamePreconditions:
+ _objc_msgSend$hasSameResults:
+ _objc_msgSend$initWithData:encoding:
+ _objc_msgSend$initWithExtensionPointIdentifier:
+ _objc_msgSend$initWithJSONInfo:
+ _objc_msgSend$initWithPlaceholderItems:
+ _objc_msgSend$installedExtensions
+ _objc_msgSend$isEqualToDate:
+ _objc_msgSend$isEqualToSet:
+ _objc_msgSend$isInstalled
+ _objc_msgSend$itemDescriptions
+ _objc_msgSend$jsonInfo
+ _objc_msgSend$keyEnumerator
+ _objc_msgSend$longValue
+ _objc_msgSend$modeKeyForCollaboration:
+ _objc_msgSend$modeSnapshotForCollaboration:
+ _objc_msgSend$modeSnapshots
+ _objc_msgSend$peopleSuggestionActivityTypes
+ _objc_msgSend$pid
+ _objc_msgSend$placeholderItemDescriptions
+ _objc_msgSend$processIdentifier
+ _objc_msgSend$setActionActivities:
+ _objc_msgSend$setFinalItemsByActivity:
+ _objc_msgSend$setInstalledExtensions:
+ _objc_msgSend$setModeSnapshots:
+ _objc_msgSend$setPeopleSuggestionActivityTypes:
+ _objc_msgSend$setPlaceholderItemDescriptions:
+ _objc_msgSend$setShareActivities:
+ _objc_msgSend$setSystemAppsAvailable:
+ _objc_msgSend$setVisibleActionActivities:
+ _objc_msgSend$setVisibleShareActivities:
+ _objc_msgSend$shareActivities
+ _objc_msgSend$shareSheetSessionEndedWithTestingSnapshot:
+ _objc_msgSend$snapshotsDirectory
+ _objc_msgSend$systemAppsAvailable
+ _objc_msgSend$timestamp
+ _objc_msgSend$updateFromSnapshot:
+ _objc_msgSend$updateModeSnapshot:forCollaboration:
+ _objc_msgSend$updateWithDiscoveredShareActivities:visibleShareActivities:actionActivities:visibleActionActivities:
+ _objc_msgSend$updateWithFinalItems:forActivityType:
+ _objc_msgSend$updateWithPeopleSuggestionActivityTypes:
+ _objc_msgSend$visibleActionActivities
+ _objc_msgSend$visibleShareActivities
+ _sandbox_check_by_audit_token
+ _symbolic Sccy___________pG 10Foundation3URLV s5ErrorP
+ airdrop_log.cold.1
+ airdrop_nw_log.cold.1
+ airdrop_ui_log.cold.1
+ asset_log.cold.1
+ asset_metadata_log.cold.1
+ authenticate_accounts_log.cold.1
+ authentications_log.cold.1
+ auto_unlock_log.cold.1
+ b389_log.cold.1
+ block_copy_helper.103
+ block_copy_helper.136
+ block_copy_helper.143
+ block_copy_helper.149
+ block_copy_helper.15
+ block_copy_helper.205
+ block_copy_helper.211
+ block_copy_helper.22
+ block_copy_helper.259
+ block_copy_helper.26
+ block_copy_helper.265
+ block_copy_helper.28
+ block_copy_helper.280
+ block_copy_helper.287
+ block_copy_helper.293
+ block_copy_helper.315
+ block_copy_helper.32
+ block_copy_helper.321
+ block_copy_helper.336
+ block_copy_helper.349
+ block_copy_helper.361
+ block_copy_helper.373
+ block_copy_helper.388
+ block_copy_helper.39
+ block_copy_helper.395
+ block_copy_helper.401
+ block_copy_helper.413
+ block_copy_helper.430
+ block_copy_helper.437
+ block_copy_helper.46
+ block_copy_helper.470
+ block_copy_helper.477
+ block_copy_helper.483
+ block_copy_helper.495
+ block_copy_helper.507
+ block_copy_helper.519
+ block_copy_helper.52
+ block_copy_helper.534
+ block_copy_helper.541
+ block_copy_helper.576
+ block_copy_helper.591
+ block_copy_helper.598
+ block_copy_helper.604
+ block_copy_helper.61
+ block_copy_helper.616
+ block_copy_helper.645
+ block_copy_helper.652
+ block_copy_helper.658
+ block_copy_helper.670
+ block_copy_helper.685
+ block_copy_helper.692
+ block_copy_helper.698
+ block_copy_helper.76
+ block_copy_helper.82
+ block_copy_helper.89
+ block_copy_helper.96
+ block_descriptor.105
+ block_descriptor.138
+ block_descriptor.145
+ block_descriptor.151
+ block_descriptor.17
+ block_descriptor.207
+ block_descriptor.213
+ block_descriptor.24
+ block_descriptor.261
+ block_descriptor.267
+ block_descriptor.28
+ block_descriptor.282
+ block_descriptor.289
+ block_descriptor.295
+ block_descriptor.30
+ block_descriptor.317
+ block_descriptor.323
+ block_descriptor.338
+ block_descriptor.34
+ block_descriptor.351
+ block_descriptor.363
+ block_descriptor.375
+ block_descriptor.390
+ block_descriptor.397
+ block_descriptor.403
+ block_descriptor.41
+ block_descriptor.415
+ block_descriptor.432
+ block_descriptor.439
+ block_descriptor.472
+ block_descriptor.479
+ block_descriptor.48
+ block_descriptor.485
+ block_descriptor.497
+ block_descriptor.509
+ block_descriptor.521
+ block_descriptor.536
+ block_descriptor.54
+ block_descriptor.543
+ block_descriptor.578
+ block_descriptor.593
+ block_descriptor.600
+ block_descriptor.606
+ block_descriptor.618
+ block_descriptor.63
+ block_descriptor.647
+ block_descriptor.654
+ block_descriptor.660
+ block_descriptor.672
+ block_descriptor.687
+ block_descriptor.694
+ block_descriptor.700
+ block_descriptor.78
+ block_descriptor.84
+ block_descriptor.91
+ block_descriptor.98
+ block_destroy_helper.104
+ block_destroy_helper.137
+ block_destroy_helper.144
+ block_destroy_helper.150
+ block_destroy_helper.16
+ block_destroy_helper.206
+ block_destroy_helper.212
+ block_destroy_helper.23
+ block_destroy_helper.260
+ block_destroy_helper.266
+ block_destroy_helper.27
+ block_destroy_helper.281
+ block_destroy_helper.288
+ block_destroy_helper.29
+ block_destroy_helper.294
+ block_destroy_helper.316
+ block_destroy_helper.322
+ block_destroy_helper.33
+ block_destroy_helper.337
+ block_destroy_helper.350
+ block_destroy_helper.362
+ block_destroy_helper.374
+ block_destroy_helper.389
+ block_destroy_helper.396
+ block_destroy_helper.40
+ block_destroy_helper.402
+ block_destroy_helper.414
+ block_destroy_helper.431
+ block_destroy_helper.438
+ block_destroy_helper.47
+ block_destroy_helper.471
+ block_destroy_helper.478
+ block_destroy_helper.484
+ block_destroy_helper.496
+ block_destroy_helper.508
+ block_destroy_helper.520
+ block_destroy_helper.53
+ block_destroy_helper.535
+ block_destroy_helper.542
+ block_destroy_helper.577
+ block_destroy_helper.592
+ block_destroy_helper.599
+ block_destroy_helper.605
+ block_destroy_helper.617
+ block_destroy_helper.62
+ block_destroy_helper.646
+ block_destroy_helper.653
+ block_destroy_helper.659
+ block_destroy_helper.671
+ block_destroy_helper.686
+ block_destroy_helper.693
+ block_destroy_helper.699
+ block_destroy_helper.77
+ block_destroy_helper.83
+ block_destroy_helper.90
+ block_destroy_helper.97
+ browser_log.cold.1
+ callbackRoutingDict.cold.1
+ charging_events_log.cold.1
+ charging_log.cold.1
+ copyLocalizedStringForKeyInStringsFile.cold.1
+ createSFNodeKindsFromXPCArray.cold.1
+ createXPCArrayFromSFNodeKinds.cold.1
+ currentProcessHasAppRecordEntitlement.hasEntitlement
+ currentProcessHasAppRecordEntitlement.onceToken
+ currentProcessHasExtensionDiscoveryEntitlements.hasEntitlements
+ currentProcessHasExtensionDiscoveryEntitlements.onceToken
+ daemon_log.cold.1
+ dateFormatter.formatter
+ dateFormatter.onceToken
+ framework_log.cold.1
+ gelato_sharing_log.cold.1
+ getOrderedProtocols.cold.1
+ getOrderedTypes.cold.1
+ getProtocolForServiceType.cold.1
+ getSWCollaborationMetadataForDocumentURLSymbolLoc.ptr
+ getSWPerformActionForDocumentURLSymbolLoc.ptr
+ getServiceTypeForProtocol.cold.1
+ getSharingFrameworkBundle.cold.1
+ get_EXQueryClass.softClass
+ get_EXQueryControllerClass.softClass
+ handoff_log.cold.1
+ initACAccountStore.cold.1
+ initAFPreferences.cold.1
+ initAFPreferencesTypeToSiriEnabled.cold.1
+ initAKAccountManager.cold.1
+ initAKAppleIDAuthenticationContext.cold.1
+ initAKAppleIDAuthenticationController.cold.1
+ initAWDServerConnection.cold.1
+ initAnalyticsSendEvent.cold.1
+ initBTDeviceAddressFromString.cold.1
+ initBTDeviceFromIdentifier.cold.1
+ initBTDeviceGetAddressString.cold.1
+ initBTDeviceGetConnectedServices.cold.1
+ initBTDeviceGetName.cold.1
+ initBTDeviceGetPairingStatus.cold.1
+ initBTDeviceIsTemporaryPaired.cold.1
+ initBTSessionAttachWithQueue.cold.1
+ initBTSessionDetachWithQueue.cold.1
+ initCBCentralManager.cold.1
+ initCBUUID.cold.1
+ initCDPContext.cold.1
+ initCDPStateController.cold.1
+ initCFPhoneNumberCreate.cold.1
+ initCFPhoneNumberCreateString.cold.1
+ initCLCopyAppsUsingLocation.cold.1
+ initCLLocationManager.cold.1
+ initCNContact.cold.1
+ initCNContactFetchRequest.cold.1
+ initCNContactFormatter.cold.1
+ initCNContactStore.cold.1
+ initCNContactsUserDefaults.cold.1
+ initDictionaries.cold.1
+ initFLFollowUpController.cold.1
+ initHMHomeManager.cold.1
+ initHMHomeManagerConfiguration.cold.1
+ initIDSService.cold.1
+ initMAAsset.cold.1
+ initMAAssetQuery.cold.1
+ initMADownloadOptions.cold.1
+ initMKBDeviceUnlockedSinceBoot.cold.1
+ initNEConfigurationManager.cold.1
+ initNSImage.cold.1
+ initOBBundle.cold.1
+ initPFVideoComplement.cold.1
+ initPNCopyBestGuessNormalizedNumberForCountry.cold.1
+ initRTIDataPayload.cold.1
+ initRTIInputSystemDataPayload.cold.1
+ initRTIInputSystemService.cold.1
+ initRTIInputSystemSourceSession.cold.1
+ initRTITextOperations.cold.1
+ initSCDynamicStoreCopyConsoleUser.cold.1
+ initSCDynamicStoreCopyValue.cold.1
+ initSFSharablePassword.cold.1
+ initSKDevice.cold.1
+ initSKSetupCaptiveNetworkJoinClient.cold.1
+ initSKSetupCaptiveNetworkJoinServer.cold.1
+ initTMIsAutomaticTimeEnabled.cold.1
+ initTMIsAutomaticTimeZoneEnabled.cold.1
+ initVSAccountSerializationCenter.cold.1
+ initVTIsHardwareDecodeSupported.cold.1
+ initValASAttributeContentVersion.cold.1
+ initValCBAdvertisementDataChannel.cold.1
+ initValCBAdvertisementDataDeviceAddress.cold.1
+ initValCBAdvertisementDataLocalNameKey.cold.1
+ initValCBAdvertisementDataManufacturerDataKey.cold.1
+ initValCBAdvertisementDataSaturated.cold.1
+ initValCBAdvertisementDataServiceDataKey.cold.1
+ initValCBCentralManagerScanOptionActive.cold.1
+ initValCBCentralManagerScanOptionAllowDuplicatesKey.cold.1
+ initValCBCentralManagerScanOptionIsPrivilegedDaemonKey.cold.1
+ initValCBCentralManagerScanOptionScanInterval.cold.1
+ initValCBCentralManagerScanOptionScanWindow.cold.1
+ initValCNContactEmailAddressesKey.cold.1
+ initValCNContactInstantMessageAddressesKey.cold.1
+ initValCNContactPhoneNumbersKey.cold.1
+ initValHMAccessoryCategoryTypeAppleTV.cold.1
+ initValHMAccessoryCategoryTypeHomePod.cold.1
+ initValOBPrivacyPrivacyPaneIdentifier.cold.1
+ initValRTIServiceSharingName.cold.1
+ initValSFSharablePasswordURLSchemeForAirDrop.cold.1
+ initValTIKeyboardOutputInfoTypePasswordStr.cold.1
+ initValTIKeyboardOutputInfoTypeUsernameStr.cold.1
+ initValWPNearbyKeyConnectLatencyCritical.cold.1
+ initValWPNearbyKeyDeviceAddress.cold.1
+ initValWPNearbyKeyManufacturerData.cold.1
+ initValWPNearbyKeyPaired.cold.1
+ initValWPNearbyKeyRSSI.cold.1
+ initValWPNearbyKeyUseCaseList.cold.1
+ initValWPNearbyLEPipeCapable.cold.1
+ initValWPPairingKeyAccessoryStatusDecrypted.cold.1
+ initValWPPairingKeyAdvertisingChannel.cold.1
+ initValWPPairingKeyDeviceAddress.cold.1
+ initWPAWDL.cold.1
+ initWPClient.cold.1
+ initWPNearby.cold.1
+ initWPPairing.cold.1
+ keypath_get.41Tm
+ log_submit_log.cold.1
+ notificationResponseHandler.cold.1
+ objectdestroy.111Tm
+ objectdestroy.215Tm
+ objectdestroy.257Tm
+ objectdestroy.26Tm
+ objectdestroy.353Tm
+ objectdestroy.419Tm
+ paired_unlock_log.cold.1
+ people_ui_log.cold.1
+ remote_log.cold.1
+ share_sheet_log.cold.1
+ sharingHUDLog.cold.1
+ sharingXPCHelperLog.cold.1
+ sharing_persistent_log.cold.1
+ sharing_ui_log.cold.1
+ streams_log.cold.1
+ tethering_log.cold.1
+ utilities_log.cold.1
- GCC_except_table139
- GCC_except_table147
- GCC_except_table241
- GCC_except_table248
- GCC_except_table266
- GCC_except_table270
- _OBJC_$_PROP_LIST_SFPeopleSuggestionProxy.279
- _PROTOCOLS_SFXPCInvocation.14
- _SFBLEPayloadTypeToString
- _SFFilterStringsFromList
- _SFKAuthenticationErrorDomain
- __106-[SFAirDropClassroomTransferManager updateTransferWithIdentifier:withState:information:completionHandler:]_block_invoke.120
- __106-[SFAirDropClassroomTransferManager updateTransferWithIdentifier:withState:information:completionHandler:]_block_invoke.120.cold.1
- __109-[SFAuthenticateAccountsService _validateiCloudCredentialsWithRequest:unvalidatedResponse:completionHandler:]_block_invoke.249
- __120-[SFDeviceAssetManager onqueue_findAssetBundleForAssetQuery:ucat:queryType:fallback:retryAttempt:withCompletionHandler:]_block_invoke_2.727
- __25-[SFService _interrupted]_block_invoke.423
- __30-[SFService _ensureXPCStarted]_block_invoke.406
- __31-[SFPowerSourceMonitor _update]_block_invoke.134
- __32-[SFBonjourNearBy _startBrowser]_block_invoke.153
- __33-[SFDeviceRepairService activate]_block_invoke.159
- __33-[SFSession _setupMessageSession]_block_invoke.312
- __33-[SFSession _setupMessageSession]_block_invoke.316
- __33-[SFSession _setupMessageSession]_block_invoke_2.317
- __34-[SFSystemService _sfServiceStart]_block_invoke.130
- __34-[SFSystemService _sfServiceStart]_block_invoke.134
- __35-[SFBonjourNearBy _startAdvertiser]_block_invoke.144
- __35-[SFCoordinatedAlertRequest _start]_block_invoke.146
- __36-[SFServiceSession pairSetup:start:]_block_invoke.934
- __37-[SFService _activateWithCompletion:]_block_invoke.324
- __37-[SFSession _activateWithCompletion:]_block_invoke.163
- __38-[SFDeviceDiscovery _ensureXPCStarted]_block_invoke.288
- __39-[SFBonjourEndpoint _handleUUIDHeaders]_block_invoke.126
- __39-[SFServiceSession pairSetupWithFlags:]_block_invoke.917
- __39-[SFXPCClient onqueue_ensureXPCStarted]_block_invoke.125
- __40-[SFAutoUnlockManager attemptAutoUnlock]_block_invoke.521
- __40-[SFAutoUnlockManager attemptAutoUnlock]_block_invoke.525
- __40-[SFDeviceAssetManager logNetworkStatus]_block_invoke.596
- __40-[SFDeviceAssetManager logNetworkStatus]_block_invoke.603
- __40-[SFDeviceOperationWiFiSetup _activate2]_block_invoke.235
- __40-[SFDeviceRepairService _sfServiceStart]_block_invoke.173
- __40-[SFDeviceRepairService _sfServiceStart]_block_invoke.177
- __40-[SFRemoteAutoFillService _serviceStart]_block_invoke.238
- __40-[SFRemoteAutoFillService _serviceStart]_block_invoke.242
- __40-[SFRemoteAutoFillService _serviceStart]_block_invoke.247
- __40-[SFRemoteAutoFillService _serviceStart]_block_invoke_2.251
- __40-[SFShareSheetService _ensureXPCStarted]_block_invoke.119
- __41-[SFDeviceOperationCNJSetup _startClient]_block_invoke.152
- __41-[SFPINPairSession _clientSFSessionStart]_block_invoke.184
- __42-[SFDeviceSetupServiceiOS _sfServiceStart]_block_invoke.182
- __42-[SFDeviceSetupServiceiOS _sfServiceStart]_block_invoke.196
- __42-[SFDeviceSetupServiceiOS _sfServiceStart]_block_invoke.200
- __42-[SFDeviceSetupServiceiOS _sfServiceStart]_block_invoke.205
- __42-[SFDeviceSetupServiceiOS _sfServiceStart]_block_invoke.210
- __42-[SFDeviceSetupServiceiOS _sfServiceStart]_block_invoke_2.187
- __42-[SFDeviceSetupServiceiOS _sfServiceStart]_block_invoke_2.212
- __42-[SFDeviceSetupWHAService _sfServiceStart]_block_invoke.161
- __42-[SFDeviceSetupWHAService _sfServiceStart]_block_invoke.165
- __42-[SFDeviceSetupWHAService _sfServiceStart]_block_invoke.169
- __42-[SFRemoteAutoFillService _discoveryStart]_block_invoke.202
- __42-[SFRemoteAutoFillService _discoveryStart]_block_invoke.206
- __42-[SFRemoteAutoFillService _discoveryStart]_block_invoke_2.209
- __43-[SFDeviceRepairSession _runSFSessionStart]_block_invoke.188
- __43-[SFRemoteAutoFillSession _runSessionStart]_block_invoke.166
- __43-[SFRemoteAutoFillSession _runSessionStart]_block_invoke.174
- __43-[SFRemoteAutoFillSession _runSessionStart]_block_invoke.178
- __43-[SFUnlockManager disableUnlockWithDevice:]_block_invoke.141
- __44-[SFAuthenticationManager isEnabledForType:]_block_invoke.377
- __44-[SFPasswordSharingService _runServiceStart]_block_invoke.182
- __44-[SFPasswordSharingService _runServiceStart]_block_invoke.186
- __44-[SFPasswordSharingService _runServiceStart]_block_invoke.191
- __44-[SFPasswordSharingService _runServiceStart]_block_invoke_2.193
- __44-[WPBonjourNearBy _listenForSFBonjourEvents]_block_invoke.121
- __44-[WPBonjourNearBy _listenForSFBonjourEvents]_block_invoke.138
- __44-[WPBonjourNearBy _listenForSFBonjourEvents]_block_invoke.142
- __44-[WPBonjourNearBy _listenForSFBonjourEvents]_block_invoke.152
- __44-[WPBonjourNearBy _listenForSFBonjourEvents]_block_invoke.158
- __44-[WPBonjourNearBy _listenForSFBonjourEvents]_block_invoke.164
- __45-[SFApproveDiscovery _discoveryEnsureStarted]_block_invoke.128
- __45-[SFApproveDiscovery _discoveryEnsureStarted]_block_invoke.132
- __45-[SFApproveDiscovery _discoveryEnsureStarted]_block_invoke_2.134
- __45-[SFDeviceDiscovery _activateWithCompletion:]_block_invoke.203
- __45-[SFDeviceSetupSessioniOS _runSFSessionStart]_block_invoke.191
- __45-[SFDeviceSetupSessioniOS _runSFSessionStart]_block_invoke.195
- __45-[SFDeviceSetupWHASession _runSFSessionStart]_block_invoke.150
- __45-[SFSystemSession getProfilesWithCompletion:]_block_invoke.164
- __46-[SFAirDropTransfer setUpProgressToBroadcast:]_block_invoke.149
- __46-[SFAutoUnlockManager mockedAttemptAutoUnlock]_block_invoke.500
- __46-[SFAutoUnlockManager mockedAttemptAutoUnlock]_block_invoke.507
- __46-[SFAutoUnlockManager mockedAttemptAutoUnlock]_block_invoke.508
- __46-[SFDeviceOperationHandlerWiFiSetup _activate]_block_invoke.433
- __46-[SFDeviceSetupAppleTVService _sfServiceStart]_block_invoke.148
- __46-[SFDeviceSetupAppleTVService _sfServiceStart]_block_invoke.152
- __46-[SFPasswordSharingSession _runSFSessionStart]_block_invoke.140
- __46-[SFPasswordSharingSession _runSFSessionStart]_block_invoke.148
- __46-[SFPasswordSharingSession _runSFSessionStart]_block_invoke.152
- __47-[SFDeviceOperationWiFiSetup _bonjourTestStart]_block_invoke.260
- __47-[SFDeviceOperationWiFiSetup _bonjourTestStart]_block_invoke.271
- __47-[SFDeviceRepairService _handleSessionStarted:]_block_invoke.239
- __47-[SFNFCTagReaderUIController _ensureXPCStarted]_block_invoke.148
- __47-[SFNFCTagReaderUIController _ensureXPCStarted]_block_invoke.170
- __47-[SFNFCTagReaderUIController _ensureXPCStarted]_block_invoke_2.173
- __47-[SFSystemSession getSystemInfoWithCompletion:]_block_invoke.156
- __48-[SFAuthenticateAccountsService _sfServiceStart]_block_invoke.171
- __48-[SFAuthenticateAccountsService _sfServiceStart]_block_invoke.175
- __48-[SFAuthenticateAccountsService _sfServiceStart]_block_invoke.179
- __48-[SFCompanionXPCManager onQueue_setupConnection]_block_invoke.351
- __49-[SFDeviceSetupAppleTVSession _runSFSessionStart]_block_invoke.211
- __49-[SFDeviceSetupAppleTVSession _runSFSessionStart]_block_invoke.224
- __51-[SFAuthenticateAccountsSession _runSFSessionStart]_block_invoke.167
- __51-[SFAuthenticateAccountsSession _runSFSessionStart]_block_invoke.177
- __52-[SFDeviceSetupSessioniOS _handleSetupPeerSuspended]_block_invoke.338
- __52-[SFUserAlert _handleResponseForNotification:flags:]_block_invoke.126
- __52-[SFUserAlert _handleResponseForNotification:flags:]_block_invoke.127
- __53-[SFDeviceSetupAppleTVService _handleSessionStarted:]_block_invoke.193
- __53-[SFSession _pairSetupWithFlags:completion:isServer:]_block_invoke.357
- __53-[SFSystemSession installProfileWithData:completion:]_block_invoke.178
- __54-[SFDeviceAssetManager onqueue_sharingManagementAsset]_block_invoke.749
- __54-[SFNFCTagReaderUIController _activateWithCompletion:]_block_invoke.141
- __54-[SFRemoteInteractionSession _activateWithCompletion:]_block_invoke.130
- __54-[SFRemoteInteractionSession _activateWithCompletion:]_block_invoke.140
- __54-[SFRemoteInteractionSession _activateWithCompletion:]_block_invoke.144
- __58-[SFDeviceOperationHandlerWiFiSetup _runIP4AvailableStart]_block_invoke.496
- __58-[SFUnlockManager unlockStateForDevice:completionHandler:]_block_invoke.164
- __58-[SFUnlockManager unlockStateForDevice:completionHandler:]_block_invoke.171
- __58-[SFUnlockManager unlockStateForDevice:completionHandler:]_block_invoke_2.165
- __59-[SFAutoUnlockManager authPromptInfoWithCompletionHandler:]_block_invoke.625
- __59-[SFAutoUnlockManager enableAutoUnlockWithDevice:passcode:]_block_invoke.444
- __59-[SFAutoUnlockManager enableAutoUnlockWithDevice:passcode:]_block_invoke.448
- __60-[SFAutoUnlockManager autoUnlockStateWithCompletionHandler:]_block_invoke.615
- __60-[SFAutoUnlockManager autoUnlockStateWithCompletionHandler:]_block_invoke.619
- __60-[SFCompanionXPCManager unlockManagerWithCompletionHandler:]_block_invoke.369
- __61-[SFAppleIDClient _copyCertificateForAppleID:withCompletion:]_block_invoke.220
- __61-[SFSessionCache _sessionWithDevice:activate:withCompletion:]_block_invoke.157
- __61-[SFSessionCache _sessionWithDevice:activate:withCompletion:]_block_invoke.164
- __61-[SFSessionCache _sessionWithDevice:activate:withCompletion:]_block_invoke_2.158
- __62-[SFActivityAdvertiser advertiseAdvertisementPayload:options:]_block_invoke.131
- __62-[SFActivityAdvertiser advertiseAdvertisementPayload:options:]_block_invoke.131.cold.1
- __62-[SFActivityAdvertiser advertiseAdvertisementPayload:options:]_block_invoke.131.cold.2
- __62-[SFBonjourNearBy _handleConnection:isAdvToBrowserConnection:]_block_invoke.175
- __62-[SFBonjourNearBy _handleConnection:isAdvToBrowserConnection:]_block_invoke.179
- __62-[SFBonjourNearBy _handleConnection:isAdvToBrowserConnection:]_block_invoke.179.cold.1
- __62-[SFBonjourNearBy _handleConnection:isAdvToBrowserConnection:]_block_invoke.182.cold.2
- __65-[SFCompanionXPCManager streamsForMessage:withCompletionHandler:]_block_invoke.362
- __67-[SFAuthenticationManager receivedApproveRequestForSessionID:info:]_block_invoke.461
- __67-[SFAuthenticationManager receivedApproveRequestForSessionID:info:]_block_invoke_2.462
- __67-[SFAuthenticationManager receivedApproveRequestForSessionID:info:]_block_invoke_2.462.cold.1
- __67-[SFAuthenticationManager receivedApproveRequestForSessionID:info:]_block_invoke_3.463
- __67-[SFAuthenticationManager receivedApproveRequestForSessionID:info:]_block_invoke_3.463.cold.1
- __67-[SFUnlockManager establishStashBagWithManifest:completionHandler:]_block_invoke.158
- __68-[SFAutoUnlockManager disableAutoUnlockForDevice:completionHandler:]_block_invoke.464
- __68-[SFDeviceAssetManager onqueue_updateMetaDataWithCompletionHandler:]_block_invoke.626
- __69-[SFAuthenticateAccountsService _handleInfoExchange:responseHandler:]_block_invoke.240
- __70-[SFAutoUnlockManager eligibleAutoUnlockDevicesWithCompletionHandler:]_block_invoke.412
- __70-[SFAutoUnlockManager eligibleAutoUnlockDevicesWithCompletionHandler:]_block_invoke.420
- __70-[SFAutoUnlockManager eligibleAutoUnlockDevicesWithCompletionHandler:]_block_invoke_2.416
- __71-[SFDeviceAssetManager onqueue_updateSharingManagementAssetIfNecessary]_block_invoke.633
- __71-[SFDeviceAssetManager onqueue_updateSharingManagementAssetIfNecessary]_block_invoke.633.cold.1
- __71-[SFDeviceAssetManager onqueue_updateSharingManagementAssetIfNecessary]_block_invoke_2.634
- __72-[SFAuthenticationManager listEligibleDevicesForType:completionHandler:]_block_invoke.392
- __72-[SFDeviceAssetManager onqueue_variantsMatchingQuery:completionHandler:]_block_invoke.649
- __72-[SFDeviceAssetManager onqueue_variantsMatchingQuery:completionHandler:]_block_invoke_2.650
- __73-[SFAuthenticationManager listCandidateDevicesForType:completionHandler:]_block_invoke.397
- __77-[SFCompanionXPCManager remoteHotspotSessionForClient:withCompletionHandler:]_block_invoke.373
- __81-[SFUnlockManager enableUnlockWithDevice:fromKey:withPasscode:completionHandler:]_block_invoke.130
- __81-[SFUnlockManager enableUnlockWithDevice:fromKey:withPasscode:completionHandler:]_block_invoke.137
- __81-[SFUnlockManager enableUnlockWithDevice:fromKey:withPasscode:completionHandler:]_block_invoke_2.131
- __84-[SFAuthenticationHintsProvider authenticateAccountWithAppleID:password:completion:]_block_invoke.163
- __84-[SFAuthenticationHintsProvider authenticateAccountWithAppleID:password:completion:]_block_invoke.165
- __87-[SFCompanionXPCManager serviceManagerProxyForIdentifier:client:withCompletionHandler:]_block_invoke.358
- __99+[SFCollaborationUtilities _processRemainingActivityItems:toFinalActivityItems:onQueue:completion:]_block_invoke_2.cold.1
- __SFAppleIDClientCopyCertificateInfo_block_invoke.296
- __SFAppleIDClientCopyCertificate_block_invoke.290
- __SFAppleIDClientCopyIdentity_block_invoke.300
- __SFAppleIDClientCopyMyAccountInfo_block_invoke.303
- __SFAppleIDCreateKeyPair_block_invoke.179
- __SFAppleIDParseValidationRecordData_block_invoke.190
- __SFAppleIDVerifyCertificateChain_block_invoke.196
- __SFCurrentAppIconData_block_invoke.560
- ___58-[SFDeviceOperationHandlerWiFiSetup _runIP4AvailableStart]_block_invoke_2
- __block_descriptor_tmp.300
- __block_descriptor_tmp.311
- __block_descriptor_tmp.366
- __block_literal_global.1137
- __block_literal_global.1141
- __block_literal_global.1153
- __block_literal_global.122
- __block_literal_global.124
- __block_literal_global.135
- __block_literal_global.150
- __block_literal_global.156
- __block_literal_global.160
- __block_literal_global.165
- __block_literal_global.177
- __block_literal_global.183
- __block_literal_global.185
- __block_literal_global.190
- __block_literal_global.213
- __block_literal_global.217
- __block_literal_global.223
- __block_literal_global.224
- __block_literal_global.229
- __block_literal_global.233
- __block_literal_global.237
- __block_literal_global.241
- __block_literal_global.243
- __block_literal_global.247
- __block_literal_global.249
- __block_literal_global.264
- __block_literal_global.268
- __block_literal_global.271
- __block_literal_global.277
- __block_literal_global.284
- __block_literal_global.290
- __block_literal_global.298
- __block_literal_global.313
- __block_literal_global.321
- __block_literal_global.335
- __block_literal_global.369
- __block_literal_global.373
- __block_literal_global.378
- __block_literal_global.379
- __block_literal_global.380
- __block_literal_global.386
- __block_literal_global.391
- __block_literal_global.396
- __block_literal_global.409
- __block_literal_global.411
- __block_literal_global.413
- __block_literal_global.416
- __block_literal_global.418
- __block_literal_global.420
- __block_literal_global.423
- __block_literal_global.428
- __block_literal_global.430
- __block_literal_global.453
- __block_literal_global.456
- __block_literal_global.458
- __block_literal_global.464
- __block_literal_global.465
- __block_literal_global.480
- __block_literal_global.485
- __block_literal_global.503
- __block_literal_global.510
- __block_literal_global.514
- __block_literal_global.518
- __block_literal_global.529
- __block_literal_global.531
- __block_literal_global.533
- __block_literal_global.693
- __block_literal_global.695
- __block_literal_global.739
- __block_literal_global.743
- __block_literal_global.748
- __block_literal_global.751
- __block_literal_global.752
- __block_literal_global.755
- __block_literal_global.757
- __block_literal_global.779
- __block_literal_global.807
- __block_literal_global.844
- __block_literal_global.858
- __block_literal_global.863
- __block_literal_global.864
- __block_literal_global.868
- __block_literal_global.874
- __block_literal_global.885
- __block_literal_global.968
- __block_literal_global.972
- __block_literal_global.979
- __block_literal_global.999
- _getCBAdvertisementDataChannel
- _getCBAdvertisementDataDeviceAddress
- _getCBAdvertisementDataLocalNameKey
- _getCBAdvertisementDataManufacturerDataKey
- _getCBAdvertisementDataSaturated
- _getCBAdvertisementDataServiceDataKey
- _getCBCentralManagerScanOptionActive
- _getCBCentralManagerScanOptionAllowDuplicatesKey
- _getCBCentralManagerScanOptionIsPrivilegedDaemonKey
- _getCBCentralManagerScanOptionScanInterval
- _getCBCentralManagerScanOptionScanWindow
- _getCBUUIDClass
- _getCNContactsUserDefaultsClass
- _getWPPairingKeyAccessoryStatusDecrypted
- _getWPPairingKeyDeviceAddress
- _initSWCollaborationMetadataForDocumentURL
- _initSWPerformActionForDocumentURL
- _objc_msgSend$services
- _softLinkCFPhoneNumberCreate
- _softLinkCFPhoneNumberCreateString
- _softLinkPNCopyBestGuessNormalizedNumberForCountry
- _softLinkSWCollaborationMetadataForDocumentURL
- _softLinkSWPerformActionForDocumentURL
- block_copy_helper.100
- block_copy_helper.107
- block_copy_helper.12
- block_copy_helper.140
- block_copy_helper.147
- block_copy_helper.153
- block_copy_helper.209
- block_copy_helper.215
- block_copy_helper.23
- block_copy_helper.25
- block_copy_helper.263
- block_copy_helper.269
- block_copy_helper.275
- block_copy_helper.290
- block_copy_helper.302
- block_copy_helper.31
- block_copy_helper.314
- block_copy_helper.329
- block_copy_helper.341
- block_copy_helper.347
- block_copy_helper.353
- block_copy_helper.36
- block_copy_helper.368
- block_copy_helper.37
- block_copy_helper.380
- block_copy_helper.386
- block_copy_helper.392
- block_copy_helper.404
- block_copy_helper.416
- block_copy_helper.431
- block_copy_helper.449
- block_copy_helper.467
- block_copy_helper.48
- block_copy_helper.484
- block_copy_helper.496
- block_copy_helper.502
- block_copy_helper.508
- block_copy_helper.520
- block_copy_helper.535
- block_copy_helper.553
- block_copy_helper.571
- block_copy_helper.583
- block_copy_helper.59
- block_copy_helper.595
- block_copy_helper.610
- block_copy_helper.622
- block_copy_helper.634
- block_copy_helper.646
- block_copy_helper.65
- block_copy_helper.663
- block_copy_helper.678
- block_copy_helper.690
- block_copy_helper.696
- block_copy_helper.702
- block_copy_helper.71
- block_copy_helper.714
- block_copy_helper.726
- block_copy_helper.743
- block_copy_helper.755
- block_copy_helper.761
- block_copy_helper.767
- block_copy_helper.779
- block_copy_helper.794
- block_copy_helper.80
- block_copy_helper.806
- block_copy_helper.812
- block_copy_helper.818
- block_copy_helper.86
- block_copy_helper.93
- block_descriptor.102
- block_descriptor.109
- block_descriptor.14
- block_descriptor.142
- block_descriptor.149
- block_descriptor.155
- block_descriptor.211
- block_descriptor.217
- block_descriptor.25
- block_descriptor.265
- block_descriptor.27
- block_descriptor.271
- block_descriptor.277
- block_descriptor.292
- block_descriptor.304
- block_descriptor.316
- block_descriptor.33
- block_descriptor.331
- block_descriptor.343
- block_descriptor.349
- block_descriptor.355
- block_descriptor.370
- block_descriptor.38
- block_descriptor.382
- block_descriptor.388
- block_descriptor.39
- block_descriptor.394
- block_descriptor.406
- block_descriptor.418
- block_descriptor.433
- block_descriptor.451
- block_descriptor.469
- block_descriptor.486
- block_descriptor.498
- block_descriptor.50
- block_descriptor.504
- block_descriptor.510
- block_descriptor.522
- block_descriptor.537
- block_descriptor.555
- block_descriptor.573
- block_descriptor.585
- block_descriptor.597
- block_descriptor.61
- block_descriptor.612
- block_descriptor.624
- block_descriptor.636
- block_descriptor.648
- block_descriptor.665
- block_descriptor.67
- block_descriptor.680
- block_descriptor.692
- block_descriptor.698
- block_descriptor.704
- block_descriptor.716
- block_descriptor.728
- block_descriptor.73
- block_descriptor.745
- block_descriptor.757
- block_descriptor.763
- block_descriptor.769
- block_descriptor.781
- block_descriptor.796
- block_descriptor.808
- block_descriptor.814
- block_descriptor.82
- block_descriptor.820
- block_descriptor.88
- block_descriptor.95
- block_destroy_helper.101
- block_destroy_helper.108
- block_destroy_helper.13
- block_destroy_helper.141
- block_destroy_helper.148
- block_destroy_helper.154
- block_destroy_helper.210
- block_destroy_helper.216
- block_destroy_helper.24
- block_destroy_helper.26
- block_destroy_helper.264
- block_destroy_helper.270
- block_destroy_helper.276
- block_destroy_helper.291
- block_destroy_helper.303
- block_destroy_helper.315
- block_destroy_helper.32
- block_destroy_helper.330
- block_destroy_helper.342
- block_destroy_helper.348
- block_destroy_helper.354
- block_destroy_helper.369
- block_destroy_helper.37
- block_destroy_helper.38
- block_destroy_helper.381
- block_destroy_helper.387
- block_destroy_helper.393
- block_destroy_helper.405
- block_destroy_helper.417
- block_destroy_helper.432
- block_destroy_helper.450
- block_destroy_helper.468
- block_destroy_helper.485
- block_destroy_helper.49
- block_destroy_helper.497
- block_destroy_helper.503
- block_destroy_helper.509
- block_destroy_helper.521
- block_destroy_helper.536
- block_destroy_helper.554
- block_destroy_helper.572
- block_destroy_helper.584
- block_destroy_helper.596
- block_destroy_helper.60
- block_destroy_helper.611
- block_destroy_helper.623
- block_destroy_helper.635
- block_destroy_helper.647
- block_destroy_helper.66
- block_destroy_helper.664
- block_destroy_helper.679
- block_destroy_helper.691
- block_destroy_helper.697
- block_destroy_helper.703
- block_destroy_helper.715
- block_destroy_helper.72
- block_destroy_helper.727
- block_destroy_helper.744
- block_destroy_helper.756
- block_destroy_helper.762
- block_destroy_helper.768
- block_destroy_helper.780
- block_destroy_helper.795
- block_destroy_helper.807
- block_destroy_helper.81
- block_destroy_helper.813
- block_destroy_helper.819
- block_destroy_helper.87
- block_destroy_helper.94
- keypath_get.45Tm
- objectdestroy.115Tm
- objectdestroy.219Tm
- objectdestroy.267Tm
- objectdestroy.30Tm
- objectdestroy.396Tm
- objectdestroy.473Tm
CStrings:
+ "\t<NSURL (non-file, scheme: %@)>\n"
+ "%@ Requesting can share for file %@"
+ "%@ Share Sheet did disappear with testing snapshot: %@"
+ "/AppleInternal/Library/BuildRoots/5f17400b-fd8b-11ef-934c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Sharing/Framework/Date+Additions.swift"
+ "/AppleInternal/Library/BuildRoots/5f17400b-fd8b-11ef-934c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Sharing/Framework/SFAirDrop.TransferIdentifier.swift"
+ "/AppleInternal/Library/BuildRoots/5f17400b-fd8b-11ef-934c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Sharing/Framework/SFAirDropClient.swift"
+ "/AppleInternal/Library/BuildRoots/5f17400b-fd8b-11ef-934c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Sharing/Framework/SFAirDropUserDefaults.swift"
+ "/AppleInternal/Library/BuildRoots/5f17400b-fd8b-11ef-934c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Sharing/Framework/SFCodableCGImage.swift"
+ "/AppleInternal/Library/BuildRoots/5f17400b-fd8b-11ef-934c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Sharing/Framework/SFCommon.swift"
+ "/AppleInternal/Library/BuildRoots/5f17400b-fd8b-11ef-934c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Sharing/Framework/SFProgressTask.swift"
+ "/AppleInternal/Library/BuildRoots/5f17400b-fd8b-11ef-934c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Sharing/Framework/SFSecurityScopedURL.swift"
+ "/AppleInternal/Library/BuildRoots/5f17400b-fd8b-11ef-934c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Sharing/Framework/SFUserDefaults.swift"
+ "/AppleInternal/Library/BuildRoots/5f17400b-fd8b-11ef-934c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Sharing/Framework/XPC/SFClientIdentity.swift"
+ "/AppleInternal/Library/BuildRoots/5f17400b-fd8b-11ef-934c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Sharing/Framework/XPC/SFXPCAsyncSequence.swift"
+ "/AppleInternal/Library/BuildRoots/5f17400b-fd8b-11ef-934c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Sharing/Framework/XPC/SFXPCBlock.swift"
+ "/AppleInternal/Library/BuildRoots/5f17400b-fd8b-11ef-934c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Sharing/Framework/XPC/SFXPCConnection.swift"
+ "/AppleInternal/Library/BuildRoots/5f17400b-fd8b-11ef-934c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Sharing/Framework/XPC/SFXPCListener.swift"
+ "/System/Library/Frameworks/ExtensionFoundation.framework/Contents/MacOS/ExtensionFoundation"
+ "<%@: %p, name: %@, identifier: %@, battery life: %d, network type: %@, signal strength: %d, group: %ld, model %@, has duplicates: %s, supports companion link: %s, os supports auto hotspot %s, cellular slicing enabled %s, handoff active: %s>"
+ "@20@0:8B16"
+ "@32@0:8@16d24"
+ "@36@0:8@16@24i32"
+ "AirDropMDMRestricted"
+ "Attempted to update snapshot from snapshot for a different Share Sheet instance. Ignoring"
+ "B24@0:8@\"NSURL\"16"
+ "Cannot issue sandbox extension for URL:%{sensitive}@"
+ "CaptiveMismatchOnly"
+ "Class get_EXQueryClass(void)_block_invoke"
+ "Class get_EXQueryControllerClass(void)_block_invoke"
+ "DCTProtocolDataAndTelephony"
+ "DCTProtocolTelephony"
+ "FindMyActionExtendedRange"
+ "FindMyActionExtendedRangeLE2M"
+ "FindMyActionExtendedRangeTransient"
+ "FindMyPlaySoundExtendedRange"
+ "HandoffActive"
+ "IPAssign"
+ "IPAssignTimedOut"
+ "Item %@ could not be archived to data: %@"
+ "Item could not be recreated due to invalid type %@"
+ "Item could not be recreated due to lack of type"
+ "Item of type %@ could not be recreated due to invalid data"
+ "Item of type %@ could not be unarchived from data: %@"
+ "Item provider %@ does not contain a separate send copy representation. Passing in the provider unchanged"
+ "Mac15,14"
+ "Mac16,1"
+ "Mac16,12"
+ "Mac16,13"
+ "Mac16,5"
+ "Mac16,6"
+ "Mac16,7"
+ "Mac16,8"
+ "Mac16,9"
+ "NSPreviewRepresentableActivityItem"
+ "NSSharingServiceItemSource"
+ "NoWiFiPassword"
+ "Path Monitor init failed\n"
+ "Reachability check detected mismatch. Skipping captive join"
+ "Read Share Sheet snapshot FAIL {error: %@}"
+ "Read Share Sheet snapshot SUCCESS {url: %@}"
+ "SFActivityItemsService"
+ "SFAuthenticationErrorCodeApproveAuthenticationFailed"
+ "SFAuthenticationErrorCodeApproveDenied"
+ "SFAuthenticationErrorCodeApproveFailedToPost"
+ "SFAuthenticationErrorCodeBluetoothDisabled"
+ "SFAuthenticationErrorCodeCancelled"
+ "SFAuthenticationErrorCodeCommunicationFailed"
+ "SFAuthenticationErrorCodeDeviceLocked"
+ "SFAuthenticationErrorCodeEscrowSecretExpired"
+ "SFAuthenticationErrorCodeFaceIDDisabled"
+ "SFAuthenticationErrorCodeIncorrectPasscode"
+ "SFAuthenticationErrorCodeInternal"
+ "SFAuthenticationErrorCodeLockDeviceIsAlreadyUnlocked"
+ "SFAuthenticationErrorCodeLockUnarmed"
+ "SFAuthenticationErrorCodeLostModeEnabled"
+ "SFAuthenticationErrorCodeMDMLocked"
+ "SFAuthenticationErrorCodeMalformedRequest"
+ "SFAuthenticationErrorCodeNetworkNotConnected"
+ "SFAuthenticationErrorCodeNotEnabled"
+ "SFAuthenticationErrorCodeNotEnoughMotion"
+ "SFAuthenticationErrorCodeNotInGuestMode"
+ "SFAuthenticationErrorCodeNotUnlockedRecently"
+ "SFAuthenticationErrorCodeOffWrist"
+ "SFAuthenticationErrorCodeOutOfRange"
+ "SFAuthenticationErrorCodePasscodeDisabled"
+ "SFAuthenticationErrorCodePeerBeforeFirstUnlock"
+ "SFAuthenticationErrorCodePeerBiolocked"
+ "SFAuthenticationErrorCodePeerDeviceNotNearby"
+ "SFAuthenticationErrorCodeRangingTimeout"
+ "SFAuthenticationErrorCodeRegionLocked"
+ "SFAuthenticationErrorCodeSleepModeOn"
+ "SFAuthenticationErrorCodeTimeOutReached"
+ "SFAuthenticationErrorCodeUnlockedBeforeKey"
+ "SFAuthenticationErrorCodeUnsupportedRemoteDevice"
+ "SFAuthenticationErrorCodeUnsupportedService"
+ "SFAuthenticationErrorCodeWatchBluetoothDisabled"
+ "SFAuthenticationErrorCodeWifiDisabled"
+ "SFAuthenticationErrorCodeWristDetectionDisabled"
+ "SFShareSheetSessionModeTestingSnapshot"
+ "SFShareSheetSessionTestingSnapshot"
+ "SFShareSheetSessionTestingSnapshot.m"
+ "ShareSheetSnapshot-%@-%@"
+ "ShareSheetTestingSnapshots"
+ "Sharing/SFShareSheetService/canShareFileURL:completion:"
+ "Sharing/SFShareSheetService/shareSheetSessionEndedWithTestingSnapshot:"
+ "SofrwareUpdateOutboxControllerAuth"
+ "SoftwareUpdateBTWake"
+ "Starting Path Monitor: %{public}@"
+ "T@\"NSArray\",C,N,V_actionActivities"
+ "T@\"NSArray\",C,N,V_installedExtensions"
+ "T@\"NSArray\",C,N,V_peopleSuggestionActivityTypes"
+ "T@\"NSArray\",C,N,V_placeholderItemDescriptions"
+ "T@\"NSArray\",C,N,V_shareActivities"
+ "T@\"NSArray\",C,N,V_visibleActionActivities"
+ "T@\"NSArray\",C,N,V_visibleShareActivities"
+ "T@\"NSArray\",R,C,N,V_itemDescriptions"
+ "T@\"NSDate\",R,N,V_timestamp"
+ "T@\"NSDictionary\",C,N,V_finalItemsByActivity"
+ "T@\"NSDictionary\",C,N,V_modeSnapshots"
+ "T@\"NSDictionary\",C,N,V_systemAppsAvailable"
+ "T@\"NSString\",R,C,N,V_applicationBundleID"
+ "TB,R,V_isAirDropMDMRestricted"
+ "TB,V_handoffActive"
+ "Ti,R,N,V_pid"
+ "UIActivityItemSource"
+ "UIActivityItemsSource"
+ "URL is not a fileURL: %{sensitive}@"
+ "URLByAppendingPathExtension:"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/5f17400b-fd8b-11ef-934c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Sharing/Framework/SFTokenBucket.m:142 : Don't use init on SFTokenBucketWithDups"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/5f17400b-fd8b-11ef-934c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Sharing/Framework/SFTokenBucket.m:25 : Don't use init on SFTokenBucket"
+ "Waiting for IP assignment (timeout: %i seconds)\n"
+ "Waiting for IPv4 (timeout: %i seconds)\n"
+ "WiFi password missing, Failing.\n"
+ "Write Share Sheet snapshot FAIL {error: %@}"
+ "Write Share Sheet snapshot SUCCESS {url: %@}"
+ "_EXQuery"
+ "_EXQueryController"
+ "_actionActivities"
+ "_applicationBundleID"
+ "_finalItemsByActivity"
+ "_handoffActive"
+ "_installedExtensions"
+ "_ipAssignSecs"
+ "_ipAssignStartTicks"
+ "_ipAssigned"
+ "_isAirDropMDMRestricted"
+ "_itemDescriptions"
+ "_itemDescriptions:match:"
+ "_jsonifyItems:"
+ "_modeSnapshots"
+ "_peopleSuggestionActivityTypes"
+ "_pid"
+ "_placeholderItemDescriptions"
+ "_shareActivities"
+ "_systemAppsAvailable"
+ "_timestamp"
+ "_visibleActionActivities"
+ "_visibleShareActivities"
+ "actionActivities"
+ "activityItemURL:%{private}@ is not shareable by client."
+ "activityViewController:itemForActivityType:"
+ "activityViewControllerPlaceholderItem:"
+ "activityViewControllerPlaceholderItems:"
+ "applicationBundleID"
+ "applicationState"
+ "canShareFileURL:"
+ "canShareFileURL:completion:"
+ "checkSystemAppsAvailability"
+ "codableDataString"
+ "codableDataStringForItem:"
+ "codableItemFromDescription:"
+ "collaborate"
+ "com.apple.extensionkit.host.extension-point-identifiers"
+ "com.apple.private.coreservices.canmaplsdatabase"
+ "com.apple.security.app-sandbox"
+ "com.apple.security.network.client"
+ "com.apple.services"
+ "com.apple.share-services"
+ "com.apple.ui-services"
+ "createWiFiRetryMetricEventForIPAssign:duration:"
+ "currentProcessHasAppRecordEntitlement"
+ "currentProcessHasExtensionDiscoveryEntitlements"
+ "dataWithJSONObject:options:error:"
+ "dateFormatter"
+ "descriptionForItem:"
+ "discoverInstalledExtensions"
+ "executeQueries:"
+ "extensionPointIdentifier"
+ "filename"
+ "finalItemsByActivity"
+ "handoffActive"
+ "hasSamePreconditions:"
+ "hasSameResults:"
+ "initWithData:encoding:"
+ "initWithExtensionPointIdentifier:"
+ "initWithItems:applicationBundleID:pid:"
+ "initWithJSONInfo:"
+ "initWithPlaceholderItems:"
+ "inputSession:documentStateDidChange:withMergeResult:"
+ "installedExtensions"
+ "isAirDropMDMRestricted"
+ "isEqualToDate:"
+ "isEqualToSet:"
+ "isInstalled"
+ "item"
+ "itemDescriptions"
+ "json"
+ "jsonInfo"
+ "keyEnumerator"
+ "longValue"
+ "modeKeyForCollaboration:"
+ "modeSnapshotForCollaboration:"
+ "modeSnapshots"
+ "path: %{public}@"
+ "peopleSuggestionActivityTypes"
+ "placeholderItemDescriptions"
+ "representedActivityItem"
+ "sendCopy"
+ "serviceOptionsDidChange:"
+ "setActionActivities:"
+ "setFinalItemsByActivity:"
+ "setHandoffActive:"
+ "setInstalledExtensions:"
+ "setModeSnapshots:"
+ "setPeopleSuggestionActivityTypes:"
+ "setPlaceholderItemDescriptions:"
+ "setShareActivities:"
+ "setSystemAppsAvailable:"
+ "setVisibleActionActivities:"
+ "setVisibleShareActivities:"
+ "shareActivities"
+ "shareSheetSessionEndedWithTestingSnapshot:"
+ "sharingServicePicker:itemForSharingServiceName:"
+ "sharingServicePickerPlaceholderItem:"
+ "snapshotsDirectory"
+ "softlink:r:path:/System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation"
+ "systemAppsAvailable"
+ "updateFromSnapshot:"
+ "updateModeSnapshot:forCollaboration:"
+ "updatePreconditionsIfNeeded"
+ "updateWithDiscoveredShareActivities:visibleShareActivities:actionActivities:visibleActionActivities:"
+ "updateWithDiscoveredShareActivities:visibleShareActivities:actionActivities:visibleActionActivities:forCollaboration:"
+ "updateWithFinalItems:forActivityType:"
+ "updateWithFinalItems:forActivityType:forCollaboration:"
+ "updateWithPeopleSuggestionActivityTypes:"
+ "updateWithPeopleSuggestionActivityTypes:forCollaboration:"
+ "updateWithPlaceholderItems:collaborationItem:supportsCollaboration:supportsSendCopy:"
+ "usbAudioConnected"
+ "v16@?0@\"NSObject<OS_nw_path>\"8"
+ "v24@0:8@\"RTIServiceOptions\"16"
+ "v24@0:8@\"SFShareSheetSessionTestingSnapshot\"16"
+ "v32@0:8@\"NSURL\"16@?<v@?@\"NSNumber\">24"
+ "v32@?0@\"<SFShareSheetActivity>\"8Q16^B24"
+ "v32@?0@\"NSString\"8@\"NSDictionary\"16^B24"
+ "v32@?0@\"NSString\"8@\"SFShareSheetSessionModeTestingSnapshot\"16^B24"
+ "v40@0:8@\"RTIInputSystemSession\"16@\"RTIDocumentState\"24Q32"
+ "v40@0:8@16@24B32B36"
+ "v40@0:8@16@24Q32"
+ "v52@0:8@16@24@32@40B48"
+ "visibleActionActivities"
+ "visibleShareActivities"
+ "void *ExtensionFoundationLibrary(void)"
+ "void soft_SWCollaborationMetadataForDocumentURL(NSURL *__strong, void (^__strong)(_SWCollaborationMetadata * _Nullable __strong, NSError * _Nullable __strong))"
+ "void soft_SWPerformActionForDocumentURL(NSURL *__strong, SWAction *__strong, void (^__strong)(_SWActionResponse * _Nullable __strong, NSError * _Nullable __strong))"
+ "writeSnapshotWithCompletionHandler:"
+ "yyyy-MM-dd'T'HH:mm:ssZZZZZ"
- "-[SFDeviceOperationHandlerWiFiSetup _runIP4AvailableStart]_block_invoke_2"
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/Sharing/Framework/Date+Additions.swift"
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/Sharing/Framework/SFAirDrop.TransferIdentifier.swift"
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/Sharing/Framework/SFAirDropClient.swift"
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/Sharing/Framework/SFAirDropUserDefaults.swift"
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/Sharing/Framework/SFCodableCGImage.swift"
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/Sharing/Framework/SFCommon.swift"
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/Sharing/Framework/SFProgressTask.swift"
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/Sharing/Framework/SFSecurityScopedURL.swift"
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/Sharing/Framework/SFUserDefaults.swift"
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/Sharing/Framework/XPC/SFClientIdentity.swift"
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/Sharing/Framework/XPC/SFXPCAsyncSequence.swift"
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/Sharing/Framework/XPC/SFXPCBlock.swift"
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/Sharing/Framework/XPC/SFXPCConnection.swift"
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/Sharing/Framework/XPC/SFXPCListener.swift"
- "<%@: %p, name: %@, identifier: %@, battery life: %d, network type: %@, signal strength: %d, group: %ld, model %@, has duplicates: %s, supports companion link: %s, os supports auto hotspot %s, cellular slicing enabled %s>"
- "Cannot issue sandbox extension for URL:%@"
- "Division by zero"
- "Division results in an overflow"
- "Failed to load item provider %@, falling back to original item provider"
- "Insufficient space allocated to copy string contents"
- "Must take zero or more splits"
- "Range requires lowerBound <= upperBound"
- "SFAuthenticationErrorApproveAuthenticationFailed"
- "SFAuthenticationErrorApproveDenied"
- "SFAuthenticationErrorApproveFailedToPost"
- "SFAuthenticationErrorBluetoothDisabled"
- "SFAuthenticationErrorCancelled"
- "SFAuthenticationErrorCommunicationFailed"
- "SFAuthenticationErrorDeviceLocked"
- "SFAuthenticationErrorEscrowSecretExpired"
- "SFAuthenticationErrorFaceIDDisabled"
- "SFAuthenticationErrorIncorrectPasscode"
- "SFAuthenticationErrorInternal"
- "SFAuthenticationErrorLockDeviceIsAlreadyUnlocked"
- "SFAuthenticationErrorLockUnarmed"
- "SFAuthenticationErrorLostModeEnabled"
- "SFAuthenticationErrorMDMLocked"
- "SFAuthenticationErrorMalformedRequest"
- "SFAuthenticationErrorNetworkNotConnected"
- "SFAuthenticationErrorNotEnabled"
- "SFAuthenticationErrorNotEnoughMotion"
- "SFAuthenticationErrorNotUnlockedRecently"
- "SFAuthenticationErrorOffWrist"
- "SFAuthenticationErrorOutOfRange"
- "SFAuthenticationErrorPasscodeDisabled"
- "SFAuthenticationErrorPeerBeforeFirstUnlock"
- "SFAuthenticationErrorPeerBiolocked"
- "SFAuthenticationErrorPeerDeviceNotNearby"
- "SFAuthenticationErrorRangingTimeout"
- "SFAuthenticationErrorRegionLocked"
- "SFAuthenticationErrorSleepModeOn"
- "SFAuthenticationErrorTimeOutReached"
- "SFAuthenticationErrorUnlockedBeforeKey"
- "SFAuthenticationErrorUnsupportedRemoteDevice"
- "SFAuthenticationErrorUnsupportedService"
- "SFAuthenticationErrorWatchBluetoothDisabled"
- "SFAuthenticationErrorWifiDisabled"
- "SFAuthenticationErrorWristDetectionDisabled"
- "Swift/Collection.swift"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/IntegerTypes.swift"
- "Swift/Range.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawBufferPointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "URL is not a fileURL: %{private}@"
- "Unexpectedly found nil while unwrapping an Optional value"
- "Unimplemented at /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/Sharing/Framework/SFTokenBucket.m:142 : Don't use init on SFTokenBucketWithDups"
- "Unimplemented at /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/Sharing/Framework/SFTokenBucket.m:25 : Don't use init on SFTokenBucket"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.initialize with negative count"
- "UnsafeMutablePointer.moveInitialize with negative count"
- "UnsafeMutableRawBufferPointer.copyMemory source has too many elements"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "Waiting for IPv4 (timeout: 10s)\n"
- "invalid Collection: less than 'count' elements in collection"

```
