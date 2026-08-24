## HomeKitMatter

> `/System/Library/PrivateFrameworks/HomeKitMatter.framework/Versions/A/HomeKitMatter`

```diff

-1490.2.0.0.0
-  __TEXT.__text: 0x186758
-  __TEXT.__objc_methlist: 0xa6ec
-  __TEXT.__const: 0x250
+1493.1.5.4.1
+  __TEXT.__text: 0x18f1a8
+  __TEXT.__objc_methlist: 0xabf4
+  __TEXT.__const: 0x280
   __TEXT.__dlopen_cstrs: 0x58
-  __TEXT.__gcc_except_tab: 0x2f44
-  __TEXT.__cstring: 0x6924
-  __TEXT.__oslogstring: 0x498af
+  __TEXT.__gcc_except_tab: 0x3070
+  __TEXT.__cstring: 0x6b01
+  __TEXT.__oslogstring: 0x4b788
   __TEXT.__ustring: 0x68
-  __TEXT.__unwind_info: 0x2f78
+  __TEXT.__unwind_info: 0x30f8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0xb78
-  __DATA_CONST.__objc_classlist: 0x430
+  __DATA_CONST.__objc_classlist: 0x458
   __DATA_CONST.__objc_catlist: 0x50
-  __DATA_CONST.__objc_protolist: 0x130
+  __DATA_CONST.__objc_protolist: 0x138
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6b50
-  __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x2f0
+  __DATA_CONST.__objc_selrefs: 0x6e50
+  __DATA_CONST.__objc_protorefs: 0x18
+  __DATA_CONST.__objc_superrefs: 0x310
   __DATA_CONST.__objc_arraydata: 0x240
-  __DATA_CONST.__got: 0x938
-  __AUTH_CONST.__const: 0x55d0
-  __AUTH_CONST.__cfstring: 0x6960
-  __AUTH_CONST.__objc_const: 0xf9b8
+  __DATA_CONST.__got: 0x970
+  __AUTH_CONST.__const: 0x56d0
+  __AUTH_CONST.__cfstring: 0x6ba0
+  __AUTH_CONST.__objc_const: 0x102c8
   __AUTH_CONST.__objc_intobj: 0x16b0
   __AUTH_CONST.__objc_arrayobj: 0x168
   __AUTH_CONST.__objc_doubleobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x1d60
-  __DATA.__objc_ivar: 0xafc
-  __DATA.__data: 0xe40
-  __DATA.__bss: 0x478
-  __DATA_DIRTY.__objc_data: 0xc80
+  __AUTH.__objc_data: 0x1e50
+  __DATA.__objc_ivar: 0xb70
+  __DATA.__data: 0xea0
+  __DATA.__bss: 0x498
+  __DATA_DIRTY.__objc_data: 0xd20
   __DATA_DIRTY.__bss: 0xa0
   - /System/Library/Frameworks/CoreBluetooth.framework/Versions/A/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /System/Library/PrivateFrameworks/UARPKit.framework/Versions/A/UARPKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 4395
-  Symbols:   10045
-  CStrings:  5415
+  Functions: 4509
+  Symbols:   10330
+  CStrings:  5536
 
Symbols:
+ +[HMMTRBackgroundCommissionableNodeScanController logCategory]
+ +[HMMTRBeaconProtectionKey bpkFromMatterFabricRawIPK:compressedFabricId:error:]
+ +[HMMTRBeaconProtectionKey compressedFabricIdFromRootPublicKey:fabricID:error:]
+ +[HMMTRExclusiveServerActionQueue logCategory]
+ +[HMMTRUtilities nfcPairingSimulationMode]
+ -[HMMTRAccessoryServer _attemptDeferredMatterCommissioning]
+ -[HMMTRAccessoryServer _discoveredDiscriminator:matchesOnboardingSetupPayload:]
+ -[HMMTRAccessoryServer _handleNFCDeferredSetupFailure:attempt:completion:]
+ -[HMMTRAccessoryServer _performNFCDeferredSetupAttempt:completion:]
+ -[HMMTRAccessoryServer _stopDeferredMatterCommissioning]
+ -[HMMTRAccessoryServer beginDeferredMatterCommissioningWithOnboardingURL:]
+ -[HMMTRAccessoryServer commissioning:succeededForNodeID:metrics:context:]
+ -[HMMTRAccessoryServer completeNFCDeferredSetupWithCompletion:]
+ -[HMMTRAccessoryServer deferredMatterAttemptInFlight]
+ -[HMMTRAccessoryServer deferredMatterOnboardingURL]
+ -[HMMTRAccessoryServer deferredSetupInProgress]
+ -[HMMTRAccessoryServer exclusivePairingQueue]
+ -[HMMTRAccessoryServer handleDiscoveredCommissionableNodeDiscriminator:]
+ -[HMMTRAccessoryServer isCommissionedOverNFCWithoutPower]
+ -[HMMTRAccessoryServer markNFCDeferredSetupNotNecessary]
+ -[HMMTRAccessoryServer nfcDeferredSetupCompletion]
+ -[HMMTRAccessoryServer nfcDeferredSetupInProgress]
+ -[HMMTRAccessoryServer nfcDeferredSetupNotNecessary]
+ -[HMMTRAccessoryServer routeUncertifiedAccessoryPromptThroughHUISWithCompletion:]
+ -[HMMTRAccessoryServer setDeferredMatterAttemptInFlight:]
+ -[HMMTRAccessoryServer setDeferredMatterOnboardingURL:]
+ -[HMMTRAccessoryServer setExclusivePairingQueue:]
+ -[HMMTRAccessoryServer setIsCommissionedOverNFCWithoutPower:]
+ -[HMMTRAccessoryServer setNfcDeferredSetupCompletion:]
+ -[HMMTRAccessoryServer setNfcDeferredSetupInProgress:]
+ -[HMMTRAccessoryServer setNfcDeferredSetupNotNecessary:]
+ -[HMMTRAccessoryServerBrowser _addDiscoveredAccessoryServerWithNodeID:fabricUUID:deferredMatterOnboardingURL:]
+ -[HMMTRAccessoryServerBrowser _cleanupDisappearedBackgroundNodesOverBLE]
+ -[HMMTRAccessoryServerBrowser _discoveredAccessoryServersDidChange]
+ -[HMMTRAccessoryServerBrowser _dispatchHandleHomeAddedAccessoryWithNodeID:fabricUUID:localControl:deferredMatterOnboardingURL:]
+ -[HMMTRAccessoryServerBrowser _forgetPresentCommissionableNodeDiscriminatorsIfScanningStopped]
+ -[HMMTRAccessoryServerBrowser _keyForDiscriminator:vendorID:productID:]
+ -[HMMTRAccessoryServerBrowser _prepareBackgroundNodesForBLEDiscovery]
+ -[HMMTRAccessoryServerBrowser _recordBackgroundDiscoveredNodeWithDiscriminator:vendorID:productID:deviceName:overBLE:]
+ -[HMMTRAccessoryServerBrowser _replayPresentCommissionableNodeDiscriminatorsToServer:]
+ -[HMMTRAccessoryServerBrowser backgroundCommissionableNodeScanControllerStartScan:]
+ -[HMMTRAccessoryServerBrowser backgroundCommissionableNodeScanControllerStopScan:]
+ -[HMMTRAccessoryServerBrowser backgroundScanController]
+ -[HMMTRAccessoryServerBrowser exclusivePairingQueue]
+ -[HMMTRAccessoryServerBrowser handleHomeAddedAccessoryWithNodeID:fabricUUID:localControl:deferredMatterOnboardingURL:]
+ -[HMMTRAccessoryServerBrowser replayPresentCommissionableNodeDiscriminatorsToServer:]
+ -[HMMTRAccessoryServerBrowser requestedBackgroundScan]
+ -[HMMTRAccessoryServerBrowser setRequestedBackgroundScan:]
+ -[HMMTRAccessoryServerBrowser startBackgroundCommissionableNodeScan]
+ -[HMMTRAccessoryServerBrowser stopBackgroundCommissionableNodeScan]
+ -[HMMTRAccessorySetupPayload setSupportsNFCPairing:]
+ -[HMMTRAccessorySetupPayload supportsNFCPairing]
+ -[HMMTRBackgroundCommissionableNodeScanController .cxx_destruct]
+ -[HMMTRBackgroundCommissionableNodeScanController _evaluate]
+ -[HMMTRBackgroundCommissionableNodeScanController deferredPairingServerIdentifiers]
+ -[HMMTRBackgroundCommissionableNodeScanController delegate]
+ -[HMMTRBackgroundCommissionableNodeScanController handleUpdatedAccessoryServerDeferredPairingState:inDeferredPairingState:]
+ -[HMMTRBackgroundCommissionableNodeScanController handleUpdatedDiscoveredAccessoryServers:]
+ -[HMMTRBackgroundCommissionableNodeScanController initWithQueue:delegate:]
+ -[HMMTRBackgroundCommissionableNodeScanController queue]
+ -[HMMTRBackgroundCommissionableNodeScanController scanRequested]
+ -[HMMTRBackgroundCommissionableNodeScanController setScanRequested:]
+ -[HMMTRBackgroundDiscoveredNode .cxx_destruct]
+ -[HMMTRBackgroundDiscoveredNode blePending]
+ -[HMMTRBackgroundDiscoveredNode deviceName]
+ -[HMMTRBackgroundDiscoveredNode discriminator]
+ -[HMMTRBackgroundDiscoveredNode initWithDiscriminator:vendorID:productID:deviceName:overBLE:]
+ -[HMMTRBackgroundDiscoveredNode overBLE]
+ -[HMMTRBackgroundDiscoveredNode productID]
+ -[HMMTRBackgroundDiscoveredNode setBlePending:]
+ -[HMMTRBackgroundDiscoveredNode vendorID]
+ -[HMMTRExclusiveServerActionQueue .cxx_destruct]
+ -[HMMTRExclusiveServerActionQueue _cancelServer:]
+ -[HMMTRExclusiveServerActionQueue _enqueueAndDequeueServer:block:]
+ -[HMMTRExclusiveServerActionQueue _enqueueAtFrontAndDequeueServer:block:]
+ -[HMMTRExclusiveServerActionQueue _finishServer:]
+ -[HMMTRExclusiveServerActionQueue _popNextLiveEntryBlock]
+ -[HMMTRExclusiveServerActionQueue cancelServer:]
+ -[HMMTRExclusiveServerActionQueue currentServer]
+ -[HMMTRExclusiveServerActionQueue enqueueServer:block:]
+ -[HMMTRExclusiveServerActionQueue enqueueServerAtFront:block:]
+ -[HMMTRExclusiveServerActionQueue init]
+ -[HMMTRExclusiveServerActionQueue pendingEntries]
+ -[HMMTRExclusiveServerActionQueue queue]
+ -[HMMTRExclusiveServerActionQueue serverDidFinishAction:]
+ -[HMMTRExclusiveServerActionQueue setCurrentServer:]
+ -[HMMTRExclusiveServerActionQueueEntry .cxx_destruct]
+ -[HMMTRExclusiveServerActionQueueEntry block]
+ -[HMMTRExclusiveServerActionQueueEntry initWithServer:block:]
+ -[HMMTRExclusiveServerActionQueueEntry server]
+ -[HMMTROperationalCertificateIssuer adminSubject]
+ -[HMMTROperationalCertificateIssuer initWithRemoteDelegate:fabricID:adminSubject:]
+ -[HMMTROperationalCertificateIssuer initWithRootKeyPair:rootCertificate:fabricID:adminSubject:]
+ GCC_except_table1002
+ GCC_except_table1066
+ GCC_except_table1072
+ GCC_except_table1074
+ GCC_except_table1196
+ GCC_except_table1264
+ GCC_except_table1310
+ GCC_except_table1318
+ GCC_except_table1377
+ GCC_except_table1414
+ GCC_except_table1451
+ GCC_except_table1478
+ GCC_except_table1674
+ GCC_except_table1717
+ GCC_except_table1871
+ GCC_except_table1872
+ GCC_except_table1873
+ GCC_except_table1876
+ GCC_except_table1896
+ GCC_except_table1897
+ GCC_except_table1898
+ GCC_except_table1899
+ GCC_except_table1900
+ GCC_except_table1903
+ GCC_except_table1906
+ GCC_except_table1907
+ GCC_except_table1908
+ GCC_except_table1909
+ GCC_except_table1910
+ GCC_except_table1911
+ GCC_except_table1912
+ GCC_except_table1971
+ GCC_except_table1977
+ GCC_except_table2065
+ GCC_except_table2180
+ GCC_except_table2182
+ GCC_except_table2212
+ GCC_except_table2222
+ GCC_except_table2224
+ GCC_except_table2280
+ GCC_except_table2326
+ GCC_except_table2351
+ GCC_except_table2422
+ GCC_except_table2709
+ GCC_except_table2713
+ GCC_except_table2717
+ GCC_except_table2775
+ GCC_except_table2808
+ GCC_except_table2854
+ GCC_except_table2856
+ GCC_except_table2887
+ GCC_except_table2888
+ GCC_except_table2889
+ GCC_except_table2912
+ GCC_except_table2913
+ GCC_except_table2914
+ GCC_except_table2915
+ GCC_except_table2916
+ GCC_except_table2918
+ GCC_except_table2928
+ GCC_except_table2930
+ GCC_except_table2941
+ GCC_except_table2962
+ GCC_except_table2977
+ GCC_except_table2983
+ GCC_except_table2998
+ GCC_except_table3001
+ GCC_except_table3005
+ GCC_except_table3020
+ GCC_except_table3023
+ GCC_except_table3027
+ GCC_except_table3029
+ GCC_except_table3056
+ GCC_except_table3065
+ GCC_except_table3070
+ GCC_except_table3082
+ GCC_except_table3135
+ GCC_except_table3136
+ GCC_except_table3519
+ GCC_except_table3545
+ GCC_except_table3546
+ GCC_except_table3547
+ GCC_except_table3551
+ GCC_except_table3560
+ GCC_except_table3576
+ GCC_except_table3591
+ GCC_except_table3660
+ GCC_except_table3661
+ GCC_except_table3690
+ GCC_except_table3729
+ GCC_except_table3733
+ GCC_except_table3741
+ GCC_except_table3761
+ GCC_except_table3764
+ GCC_except_table3806
+ GCC_except_table3808
+ GCC_except_table3810
+ GCC_except_table3829
+ GCC_except_table3831
+ GCC_except_table3852
+ GCC_except_table3929
+ GCC_except_table3976
+ GCC_except_table3996
+ GCC_except_table4019
+ GCC_except_table4023
+ GCC_except_table4038
+ GCC_except_table4039
+ GCC_except_table4040
+ GCC_except_table4046
+ GCC_except_table4058
+ GCC_except_table4095
+ GCC_except_table4117
+ GCC_except_table4160
+ GCC_except_table4166
+ GCC_except_table4169
+ GCC_except_table4255
+ GCC_except_table4256
+ GCC_except_table4314
+ GCC_except_table4317
+ GCC_except_table4381
+ GCC_except_table4441
+ GCC_except_table4445
+ GCC_except_table4451
+ GCC_except_table4455
+ GCC_except_table4489
+ GCC_except_table560
+ GCC_except_table564
+ GCC_except_table593
+ GCC_except_table599
+ GCC_except_table601
+ GCC_except_table605
+ GCC_except_table762
+ GCC_except_table763
+ GCC_except_table820
+ GCC_except_table821
+ GCC_except_table822
+ GCC_except_table895
+ GCC_except_table937
+ GCC_except_table988
+ GCC_except_table992
+ GCC_except_table994
+ GCC_except_table996
+ GCC_except_table998
+ OBJC_IVAR_$_HMMTRAccessoryServer._deferredMatterAttemptInFlight
+ OBJC_IVAR_$_HMMTRAccessoryServer._deferredMatterOnboardingURL
+ OBJC_IVAR_$_HMMTRAccessoryServer._exclusivePairingQueue
+ OBJC_IVAR_$_HMMTRAccessoryServer._isCommissionedOverNFCWithoutPower
+ OBJC_IVAR_$_HMMTRAccessoryServer._nfcDeferredSetupCompletion
+ OBJC_IVAR_$_HMMTRAccessoryServer._nfcDeferredSetupInProgress
+ OBJC_IVAR_$_HMMTRAccessoryServer._nfcDeferredSetupNotNecessary
+ OBJC_IVAR_$_HMMTRAccessoryServerBrowser._backgroundDiscoveredNodes
+ OBJC_IVAR_$_HMMTRAccessoryServerBrowser._backgroundScanController
+ OBJC_IVAR_$_HMMTRAccessoryServerBrowser._exclusivePairingQueue
+ OBJC_IVAR_$_HMMTRAccessoryServerBrowser._presentCommissionableNodeDiscriminators
+ OBJC_IVAR_$_HMMTRAccessoryServerBrowser._requestedBackgroundScan
+ OBJC_IVAR_$_HMMTRAccessorySetupPayload._supportsNFCPairing
+ OBJC_IVAR_$_HMMTRBackgroundCommissionableNodeScanController._deferredPairingServerIdentifiers
+ OBJC_IVAR_$_HMMTRBackgroundCommissionableNodeScanController._delegate
+ OBJC_IVAR_$_HMMTRBackgroundCommissionableNodeScanController._queue
+ OBJC_IVAR_$_HMMTRBackgroundCommissionableNodeScanController._scanRequested
+ OBJC_IVAR_$_HMMTRBackgroundDiscoveredNode._blePending
+ OBJC_IVAR_$_HMMTRBackgroundDiscoveredNode._deviceName
+ OBJC_IVAR_$_HMMTRBackgroundDiscoveredNode._discriminator
+ OBJC_IVAR_$_HMMTRBackgroundDiscoveredNode._overBLE
+ OBJC_IVAR_$_HMMTRBackgroundDiscoveredNode._productID
+ OBJC_IVAR_$_HMMTRBackgroundDiscoveredNode._vendorID
+ OBJC_IVAR_$_HMMTRExclusiveServerActionQueue._currentServer
+ OBJC_IVAR_$_HMMTRExclusiveServerActionQueue._pendingEntries
+ OBJC_IVAR_$_HMMTRExclusiveServerActionQueue._queue
+ OBJC_IVAR_$_HMMTRExclusiveServerActionQueueEntry._block
+ OBJC_IVAR_$_HMMTRExclusiveServerActionQueueEntry._server
+ OBJC_IVAR_$_HMMTROperationalCertificateIssuer._adminSubject
+ _MTRCommissioningSessionTransportType
+ _MTRUnpoweredInitialPhase
+ _NSLocalizedDescriptionKey
+ _OBJC_CLASS_$_CoreHAPHKDF
+ _OBJC_CLASS_$_HAPAccessoryPairingRequest
+ _OBJC_CLASS_$_HMMTRBackgroundCommissionableNodeScanController
+ _OBJC_CLASS_$_HMMTRBackgroundDiscoveredNode
+ _OBJC_CLASS_$_HMMTRBeaconProtectionKey
+ _OBJC_CLASS_$_HMMTRExclusiveServerActionQueue
+ _OBJC_CLASS_$_HMMTRExclusiveServerActionQueueEntry
+ _OBJC_METACLASS_$_HMMTRBackgroundCommissionableNodeScanController
+ _OBJC_METACLASS_$_HMMTRBackgroundDiscoveredNode
+ _OBJC_METACLASS_$_HMMTRBeaconProtectionKey
+ _OBJC_METACLASS_$_HMMTRExclusiveServerActionQueue
+ _OBJC_METACLASS_$_HMMTRExclusiveServerActionQueueEntry
+ __127-[HMMTRAccessoryServerBrowser _dispatchHandleHomeAddedAccessoryWithNodeID:fabricUUID:localControl:deferredMatterOnboardingURL:]_block_invoke
+ __46-[HMMTRAccessoryServer _reportPairingComplete]_block_invoke
+ __67-[HMMTRAccessoryServer _performNFCDeferredSetupAttempt:completion:]_block_invoke
+ __OBJC_$_CLASS_METHODS_HMMTRBackgroundCommissionableNodeScanController
+ __OBJC_$_CLASS_METHODS_HMMTRBeaconProtectionKey
+ __OBJC_$_CLASS_METHODS_HMMTRExclusiveServerActionQueue
+ __OBJC_$_INSTANCE_METHODS_HMMTRBackgroundCommissionableNodeScanController
+ __OBJC_$_INSTANCE_METHODS_HMMTRBackgroundDiscoveredNode
+ __OBJC_$_INSTANCE_METHODS_HMMTRExclusiveServerActionQueue
+ __OBJC_$_INSTANCE_METHODS_HMMTRExclusiveServerActionQueueEntry
+ __OBJC_$_INSTANCE_VARIABLES_HMMTRBackgroundCommissionableNodeScanController
+ __OBJC_$_INSTANCE_VARIABLES_HMMTRBackgroundDiscoveredNode
+ __OBJC_$_INSTANCE_VARIABLES_HMMTRExclusiveServerActionQueue
+ __OBJC_$_INSTANCE_VARIABLES_HMMTRExclusiveServerActionQueueEntry
+ __OBJC_$_PROP_LIST_HMMTRBackgroundCommissionableNodeScanController
+ __OBJC_$_PROP_LIST_HMMTRBackgroundDiscoveredNode
+ __OBJC_$_PROP_LIST_HMMTRExclusiveServerActionQueue
+ __OBJC_$_PROP_LIST_HMMTRExclusiveServerActionQueueEntry
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_HMMTRBackgroundCommissionableNodeScanControllerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HMMTRBackgroundCommissionableNodeScanControllerDelegate
+ __OBJC_$_PROTOCOL_REFS_HMMTRBackgroundCommissionableNodeScanControllerDelegate
+ __OBJC_CLASS_RO_$_HMMTRBackgroundCommissionableNodeScanController
+ __OBJC_CLASS_RO_$_HMMTRBackgroundDiscoveredNode
+ __OBJC_CLASS_RO_$_HMMTRBeaconProtectionKey
+ __OBJC_CLASS_RO_$_HMMTRExclusiveServerActionQueue
+ __OBJC_CLASS_RO_$_HMMTRExclusiveServerActionQueueEntry
+ __OBJC_LABEL_PROTOCOL_$_HMMTRBackgroundCommissionableNodeScanControllerDelegate
+ __OBJC_METACLASS_RO_$_HMMTRBackgroundCommissionableNodeScanController
+ __OBJC_METACLASS_RO_$_HMMTRBackgroundDiscoveredNode
+ __OBJC_METACLASS_RO_$_HMMTRBeaconProtectionKey
+ __OBJC_METACLASS_RO_$_HMMTRExclusiveServerActionQueue
+ __OBJC_METACLASS_RO_$_HMMTRExclusiveServerActionQueueEntry
+ __OBJC_PROTOCOL_$_HMMTRBackgroundCommissionableNodeScanControllerDelegate
+ __OBJC_PROTOCOL_REFERENCE_$_HAPAccessoryServerDelegate
+ ___123-[HMMTRBackgroundCommissionableNodeScanController handleUpdatedAccessoryServerDeferredPairingState:inDeferredPairingState:]_block_invoke
+ ___127-[HMMTRAccessoryServerBrowser _dispatchHandleHomeAddedAccessoryWithNodeID:fabricUUID:localControl:deferredMatterOnboardingURL:]_block_invoke
+ ___46+[HMMTRExclusiveServerActionQueue logCategory]_block_invoke
+ ___48-[HMMTRAccessoryServer startPairingWithRequest:]_block_invoke
+ ___49-[HMMTRExclusiveServerActionQueue _cancelServer:]_block_invoke
+ ___49-[HMMTRExclusiveServerActionQueue _finishServer:]_block_invoke
+ ___56-[HMMTRAccessoryServer markNFCDeferredSetupNotNecessary]_block_invoke
+ ___59-[HMMTRAccessoryServer _attemptDeferredMatterCommissioning]_block_invoke
+ ___62+[HMMTRBackgroundCommissionableNodeScanController logCategory]_block_invoke
+ ___63-[HMMTRAccessoryServer completeNFCDeferredSetupWithCompletion:]_block_invoke
+ ___66-[HMMTRExclusiveServerActionQueue _enqueueAndDequeueServer:block:]_block_invoke
+ ___67-[HMMTRAccessoryServer _performNFCDeferredSetupAttempt:completion:]_block_invoke
+ ___67-[HMMTRAccessoryServerBrowser stopBackgroundCommissionableNodeScan]_block_invoke
+ ___68-[HMMTRAccessoryServerBrowser startBackgroundCommissionableNodeScan]_block_invoke
+ ___72-[HMMTRAccessoryServer handleDiscoveredCommissionableNodeDiscriminator:]_block_invoke
+ ___73-[HMMTRExclusiveServerActionQueue _enqueueAtFrontAndDequeueServer:block:]_block_invoke
+ ___74-[HMMTRAccessoryServer _handleNFCDeferredSetupFailure:attempt:completion:]_block_invoke
+ ___74-[HMMTRAccessoryServer beginDeferredMatterCommissioningWithOnboardingURL:]_block_invoke
+ ___85-[HMMTRAccessoryServerBrowser replayPresentCommissionableNodeDiscriminatorsToServer:]_block_invoke
+ ___91-[HMMTRBackgroundCommissionableNodeScanController handleUpdatedDiscoveredAccessoryServers:]_block_invoke
+ ___block_descriptor_49_e8_32s40w_e5_v8?0l
+ ___block_descriptor_56_e8_32bs40w_e20_v20?0B8"NSError"12l
+ ___block_descriptor_64_e8_32s40s48bs56w_e8_v12?0B8l
+ ___block_descriptor_65_e8_32s40s48s56s_e5_v8?0l
+ ___block_descriptor_72_e8_32s40s48s56r64w_e29_v16?0"MTRDeviceController"8l
+ _kNFCDeferredSetupRetryDelays
+ _objc_msgSend$_addDiscoveredAccessoryServerWithNodeID:fabricUUID:deferredMatterOnboardingURL:
+ _objc_msgSend$_attemptDeferredMatterCommissioning
+ _objc_msgSend$_cancelServer:
+ _objc_msgSend$_cleanupDisappearedBackgroundNodesOverBLE
+ _objc_msgSend$_discoveredAccessoryServersDidChange
+ _objc_msgSend$_discoveredDiscriminator:matchesOnboardingSetupPayload:
+ _objc_msgSend$_dispatchHandleHomeAddedAccessoryWithNodeID:fabricUUID:localControl:deferredMatterOnboardingURL:
+ _objc_msgSend$_enqueueAndDequeueServer:block:
+ _objc_msgSend$_enqueueAtFrontAndDequeueServer:block:
+ _objc_msgSend$_evaluate
+ _objc_msgSend$_finishServer:
+ _objc_msgSend$_forgetPresentCommissionableNodeDiscriminatorsIfScanningStopped
+ _objc_msgSend$_handleNFCDeferredSetupFailure:attempt:completion:
+ _objc_msgSend$_keyForDiscriminator:vendorID:productID:
+ _objc_msgSend$_performNFCDeferredSetupAttempt:completion:
+ _objc_msgSend$_popNextLiveEntryBlock
+ _objc_msgSend$_prepareBackgroundNodesForBLEDiscovery
+ _objc_msgSend$_recordBackgroundDiscoveredNodeWithDiscriminator:vendorID:productID:deviceName:overBLE:
+ _objc_msgSend$_replayPresentCommissionableNodeDiscriminatorsToServer:
+ _objc_msgSend$_stopDeferredMatterCommissioning
+ _objc_msgSend$accessoryDeferredMatterOnboardingPayloadForNodeID:fabricUUID:
+ _objc_msgSend$accessoryIsUserConfigurationReadyForNodeID:fabricUUID:
+ _objc_msgSend$adminSubject
+ _objc_msgSend$backgroundCommissionableNodeScanControllerStartScan:
+ _objc_msgSend$backgroundCommissionableNodeScanControllerStopScan:
+ _objc_msgSend$backgroundScanController
+ _objc_msgSend$beginDeferredMatterCommissioningWithOnboardingURL:
+ _objc_msgSend$blePending
+ _objc_msgSend$block
+ _objc_msgSend$cancelServer:
+ _objc_msgSend$commissioning:succeededForNodeID:metrics:
+ _objc_msgSend$currentServer
+ _objc_msgSend$deferredMatterAttemptInFlight
+ _objc_msgSend$deferredMatterOnboardingURL
+ _objc_msgSend$deferredPairingServerIdentifiers
+ _objc_msgSend$deferredSetupInProgress
+ _objc_msgSend$deviceName
+ _objc_msgSend$enqueueServer:block:
+ _objc_msgSend$enqueueServerAtFront:block:
+ _objc_msgSend$exclusivePairingQueue
+ _objc_msgSend$handleDiscoveredCommissionableNodeDiscriminator:
+ _objc_msgSend$handleUpdatedAccessoryServerDeferredPairingState:inDeferredPairingState:
+ _objc_msgSend$handleUpdatedDiscoveredAccessoryServers:
+ _objc_msgSend$hkdfSHA256DeriveKeyFromIKM:salt:info:outputByteCount:error:
+ _objc_msgSend$hkdfSHA512DeriveKeyFromIKM:salt:info:outputByteCount:error:
+ _objc_msgSend$hmf_fastEncodedSizeForObject:
+ _objc_msgSend$initWithDiscriminator:vendorID:productID:deviceName:overBLE:
+ _objc_msgSend$initWithQueue:delegate:
+ _objc_msgSend$initWithServer:block:
+ _objc_msgSend$insertObject:atIndex:
+ _objc_msgSend$intersectSet:
+ _objc_msgSend$isCommissionedOverNFCWithoutPower
+ _objc_msgSend$linkType
+ _objc_msgSend$nfcDeferredSetupCompletion
+ _objc_msgSend$nfcDeferredSetupInProgress
+ _objc_msgSend$nfcDeferredSetupNotNecessary
+ _objc_msgSend$nfcPairingSimulationMode
+ _objc_msgSend$overBLE
+ _objc_msgSend$pendingEntries
+ _objc_msgSend$productVariant
+ _objc_msgSend$removeObjectAtIndex:
+ _objc_msgSend$replayPresentCommissionableNodeDiscriminatorsToServer:
+ _objc_msgSend$requestedBackgroundScan
+ _objc_msgSend$routeUncertifiedAccessoryPromptThroughHUISWithCompletion:
+ _objc_msgSend$routeUncertifiedMatterAccessoryPrompt:completion:
+ _objc_msgSend$scanRequested
+ _objc_msgSend$serverDidFinishAction:
+ _objc_msgSend$setBlePending:
+ _objc_msgSend$setChipFabricID:
+ _objc_msgSend$setCurrentServer:
+ _objc_msgSend$setDeferredMatterAttemptInFlight:
+ _objc_msgSend$setDeferredMatterOnboardingURL:
+ _objc_msgSend$setExclusivePairingQueue:
+ _objc_msgSend$setIsCommissionedOverNFCWithoutPower:
+ _objc_msgSend$setNfcDeferredSetupCompletion:
+ _objc_msgSend$setNfcDeferredSetupInProgress:
+ _objc_msgSend$setNfcDeferredSetupNotNecessary:
+ _objc_msgSend$setRequestedBackgroundScan:
+ _objc_msgSend$setScanRequested:
+ _objc_msgSend$setSupportsNFCPairing:
+ _objc_msgSend$setWithCapacity:
+ _objc_msgSend$startBackgroundCommissionableNodeScan
+ _objc_msgSend$stopBackgroundCommissionableNodeScan
+ _objc_msgSend$subdataWithRange:
+ _objc_msgSend$supportsNFCPairing
+ logCategory._hmf_once_t1243
+ logCategory._hmf_once_t724
+ logCategory._hmf_once_v1244
+ logCategory._hmf_once_v725
- -[HMMTRAccessoryServerBrowser _dispatchHandleHomeAddedAccessoryWithNodeID:fabricUUID:localControl:]
- -[HMMTROperationalCertificateIssuer initWithRemoteDelegate:fabricID:]
- -[HMMTROperationalCertificateIssuer initWithRootKeyPair:rootCertificate:fabricID:]
- GCC_except_table1021
- GCC_except_table1027
- GCC_except_table1029
- GCC_except_table1151
- GCC_except_table1219
- GCC_except_table1265
- GCC_except_table1273
- GCC_except_table1324
- GCC_except_table1332
- GCC_except_table1406
- GCC_except_table1433
- GCC_except_table1629
- GCC_except_table1672
- GCC_except_table1826
- GCC_except_table1827
- GCC_except_table1828
- GCC_except_table1831
- GCC_except_table1851
- GCC_except_table1852
- GCC_except_table1853
- GCC_except_table1854
- GCC_except_table1855
- GCC_except_table1858
- GCC_except_table1861
- GCC_except_table1862
- GCC_except_table1863
- GCC_except_table1864
- GCC_except_table1865
- GCC_except_table1866
- GCC_except_table1867
- GCC_except_table1926
- GCC_except_table1934
- GCC_except_table2022
- GCC_except_table2137
- GCC_except_table2139
- GCC_except_table2169
- GCC_except_table2179
- GCC_except_table2181
- GCC_except_table2237
- GCC_except_table2283
- GCC_except_table2308
- GCC_except_table2379
- GCC_except_table2649
- GCC_except_table2653
- GCC_except_table2744
- GCC_except_table2789
- GCC_except_table2791
- GCC_except_table2822
- GCC_except_table2823
- GCC_except_table2824
- GCC_except_table2846
- GCC_except_table2847
- GCC_except_table2848
- GCC_except_table2849
- GCC_except_table2850
- GCC_except_table2851
- GCC_except_table2852
- GCC_except_table2853
- GCC_except_table2863
- GCC_except_table2865
- GCC_except_table2876
- GCC_except_table2896
- GCC_except_table2932
- GCC_except_table2935
- GCC_except_table2939
- GCC_except_table2954
- GCC_except_table2957
- GCC_except_table2961
- GCC_except_table2963
- GCC_except_table2982
- GCC_except_table2991
- GCC_except_table2996
- GCC_except_table3008
- GCC_except_table3061
- GCC_except_table3062
- GCC_except_table3442
- GCC_except_table3443
- GCC_except_table3444
- GCC_except_table3448
- GCC_except_table3454
- GCC_except_table3457
- GCC_except_table3473
- GCC_except_table3488
- GCC_except_table3556
- GCC_except_table3586
- GCC_except_table3617
- GCC_except_table3621
- GCC_except_table3629
- GCC_except_table3648
- GCC_except_table3651
- GCC_except_table3693
- GCC_except_table3695
- GCC_except_table3716
- GCC_except_table3718
- GCC_except_table3739
- GCC_except_table3816
- GCC_except_table3863
- GCC_except_table3883
- GCC_except_table3907
- GCC_except_table3911
- GCC_except_table3926
- GCC_except_table3927
- GCC_except_table3928
- GCC_except_table3934
- GCC_except_table3941
- GCC_except_table3982
- GCC_except_table4004
- GCC_except_table4047
- GCC_except_table4056
- GCC_except_table4142
- GCC_except_table4143
- GCC_except_table4200
- GCC_except_table4203
- GCC_except_table4267
- GCC_except_table4327
- GCC_except_table4333
- GCC_except_table4337
- GCC_except_table4341
- GCC_except_table4375
- GCC_except_table715
- GCC_except_table716
- GCC_except_table773
- GCC_except_table774
- GCC_except_table775
- GCC_except_table848
- GCC_except_table890
- GCC_except_table941
- GCC_except_table947
- GCC_except_table949
- GCC_except_table951
- GCC_except_table953
- GCC_except_table957
- __99-[HMMTRAccessoryServerBrowser _dispatchHandleHomeAddedAccessoryWithNodeID:fabricUUID:localControl:]_block_invoke
- ___99-[HMMTRAccessoryServerBrowser _dispatchHandleHomeAddedAccessoryWithNodeID:fabricUUID:localControl:]_block_invoke
- ___block_descriptor_64_e8_32s40s48r56w_e29_v16?0"MTRDeviceController"8l
- _objc_msgSend$_addDiscoveredAccessoryServerWithNodeID:fabricUUID:
- _objc_msgSend$_dispatchHandleHomeAddedAccessoryWithNodeID:fabricUUID:localControl:
- logCategory._hmf_once_t1180
- logCategory._hmf_once_t703
- logCategory._hmf_once_v1181
- logCategory._hmf_once_v704
CStrings:
+ "%@-%@-%@"
+ "Accessory for nodeID %@ is not user configuration ready; skipping"
+ "Accessory server already exists for node %@, fabric %@; skipping creation (matter onboarding %@)"
+ "Accessory with node ID %@ was added to home with fabric %@, for local control: %@ with Matter onboarding payload: %{private}@"
+ "Adding server with deferred onboarding URL for nodeID %@"
+ "Attempting deferred Matter commissioning"
+ "Cancelling holder server %{public}@ (pending=%lu)"
+ "Cannot parse deferred Matter onboarding payload %{public}@: %{public}@"
+ "CompressedFabric"
+ "Deferred Matter commissioning attempt already in flight; ignoring"
+ "Deferred Matter commissioning attempt failed; replaying present commissionable nodes to retry"
+ "Discovered commissionable node matches deferred Matter onboarding discriminator %@; attempting commissioning"
+ "Failed to update vendorID to %{public}@ and productID to %{public}@ after deferred Matter commissioning with error domain: %{public}@ code: %ld"
+ "GroupKey v1.0"
+ "HK Matter Privacy v1 BPK"
+ "HK Matter Privacy v1 TLK"
+ "HMMTRBeaconProtectionKeyErrorDomain"
+ "Marking NFC deferred setup as not necessary"
+ "Matter raw IPK must be 16 bytes (got %lu)"
+ "NFC commissioning completed (unpowered: %{bool}d) for node %@"
+ "NFC deferred setup already completed system-commissioner pairing (commissioningID set); treating repeat attempt as success without re-pairing"
+ "NFC deferred setup already in progress, skipping"
+ "NFC deferred setup attempt %lu of %lu"
+ "NFC deferred setup failed: %@ context: %@"
+ "NFC deferred setup not necessary (accessory completed via prox-pairing path); skipping without invoking completion"
+ "NFC deferred setup succeeded"
+ "NFC deferred setup: ACL update failed: %@"
+ "NFC deferred setup: ACL update succeeded"
+ "NFC deferred setup: all %lu attempts exhausted"
+ "NFC deferred setup: no device controller, failing permanently"
+ "NFC deferred setup: scheduling retry in %.0fs (attempt %lu failed)"
+ "NFC deferred setup: system commissioner fabric failed: %@"
+ "NFC deferred setup: system commissioner fabric installed successfully"
+ "NFC deferred setup: system commissioner feature disabled, completing after ACL"
+ "NFC pairing simulation (%{public}@): linkType=NFC, unpowered=%{bool}d for node %@"
+ "No delegate/queue to attach for deferred-onboarding node %@; system commissioner pairing will not run"
+ "Notifying deferred Matter paired accessory server and persisting server data"
+ "Pruned deferred pairing targets to discovered set (%lu -> %lu)"
+ "Removed %lu pending entries for server %{public}@ (pending=%lu)"
+ "Removing NFC server %@ from discovered list after pairing complete"
+ "Requesting background commissionable node scan start"
+ "Requesting background commissionable node scan stop"
+ "Server %{public}@ acquired slot from FIFO (pending=%lu)"
+ "Server %{public}@ acquired slot immediately (pending=%lu)"
+ "Server %{public}@ called serverDidFinishAction: while not holding slot (current=%{public}@); ignoring"
+ "Server %{public}@ deferred pairing state -> %d (targets=%lu)"
+ "Server %{public}@ enqueued at front behind holder %{public}@ (pending=%lu)"
+ "Server %{public}@ enqueued behind %{public}@ (pending=%lu)"
+ "Server %{public}@ released slot (pending=%lu)"
+ "Skipping deferred Matter commissioning attempt: already completed"
+ "Skipping pending entry whose server was deallocated (pending=%lu)"
+ "Starting NFC deferred setup (ACL + system commissioner fabric)"
+ "Starting background commissionable node scan"
+ "Stopping background commissionable node scan"
+ "Stored deferred Matter onboarding URL %{private}@; awaiting commissionable-node discovery"
+ "Successfully updated vendorID to %{public}@ and productID to %{public}@ after deferred Matter commissioning"
+ "Unable to create server for deferred Matter onboarding of node %@"
+ "Vendor ID %{public}@ and product ID %{public}@ not updated after deferred Matter commissioning because both are not available"
+ "[%{public}@] Accessory for nodeID %@ is not user configuration ready; skipping"
+ "[%{public}@] Accessory server already exists for node %@, fabric %@; skipping creation (matter onboarding %@)"
+ "[%{public}@] Accessory with node ID %@ was added to home with fabric %@, for local control: %@ with Matter onboarding payload: %{private}@"
+ "[%{public}@] Adding server with deferred onboarding URL for nodeID %@"
+ "[%{public}@] Attempting deferred Matter commissioning"
+ "[%{public}@] Cancelling holder server %{public}@ (pending=%lu)"
+ "[%{public}@] Cannot parse deferred Matter onboarding payload %{public}@: %{public}@"
+ "[%{public}@] Deferred Matter commissioning attempt already in flight; ignoring"
+ "[%{public}@] Deferred Matter commissioning attempt failed; replaying present commissionable nodes to retry"
+ "[%{public}@] Discovered commissionable node matches deferred Matter onboarding discriminator %@; attempting commissioning"
+ "[%{public}@] Failed to update vendorID to %{public}@ and productID to %{public}@ after deferred Matter commissioning with error domain: %{public}@ code: %ld"
+ "[%{public}@] Marking NFC deferred setup as not necessary"
+ "[%{public}@] NFC commissioning completed (unpowered: %{bool}d) for node %@"
+ "[%{public}@] NFC deferred setup already completed system-commissioner pairing (commissioningID set); treating repeat attempt as success without re-pairing"
+ "[%{public}@] NFC deferred setup already in progress, skipping"
+ "[%{public}@] NFC deferred setup attempt %lu of %lu"
+ "[%{public}@] NFC deferred setup failed: %@ context: %@"
+ "[%{public}@] NFC deferred setup not necessary (accessory completed via prox-pairing path); skipping without invoking completion"
+ "[%{public}@] NFC deferred setup succeeded"
+ "[%{public}@] NFC deferred setup: ACL update failed: %@"
+ "[%{public}@] NFC deferred setup: ACL update succeeded"
+ "[%{public}@] NFC deferred setup: all %lu attempts exhausted"
+ "[%{public}@] NFC deferred setup: no device controller, failing permanently"
+ "[%{public}@] NFC deferred setup: scheduling retry in %.0fs (attempt %lu failed)"
+ "[%{public}@] NFC deferred setup: system commissioner fabric failed: %@"
+ "[%{public}@] NFC deferred setup: system commissioner fabric installed successfully"
+ "[%{public}@] NFC deferred setup: system commissioner feature disabled, completing after ACL"
+ "[%{public}@] NFC pairing simulation (%{public}@): linkType=NFC, unpowered=%{bool}d for node %@"
+ "[%{public}@] No delegate/queue to attach for deferred-onboarding node %@; system commissioner pairing will not run"
+ "[%{public}@] Notifying deferred Matter paired accessory server and persisting server data"
+ "[%{public}@] Pruned deferred pairing targets to discovered set (%lu -> %lu)"
+ "[%{public}@] Removed %lu pending entries for server %{public}@ (pending=%lu)"
+ "[%{public}@] Removing NFC server %@ from discovered list after pairing complete"
+ "[%{public}@] Requesting background commissionable node scan start"
+ "[%{public}@] Requesting background commissionable node scan stop"
+ "[%{public}@] Server %{public}@ acquired slot from FIFO (pending=%lu)"
+ "[%{public}@] Server %{public}@ acquired slot immediately (pending=%lu)"
+ "[%{public}@] Server %{public}@ called serverDidFinishAction: while not holding slot (current=%{public}@); ignoring"
+ "[%{public}@] Server %{public}@ deferred pairing state -> %d (targets=%lu)"
+ "[%{public}@] Server %{public}@ enqueued at front behind holder %{public}@ (pending=%lu)"
+ "[%{public}@] Server %{public}@ enqueued behind %{public}@ (pending=%lu)"
+ "[%{public}@] Server %{public}@ released slot (pending=%lu)"
+ "[%{public}@] Skipping deferred Matter commissioning attempt: already completed"
+ "[%{public}@] Skipping pending entry whose server was deallocated (pending=%lu)"
+ "[%{public}@] Starting NFC deferred setup (ACL + system commissioner fabric)"
+ "[%{public}@] Starting background commissionable node scan"
+ "[%{public}@] Stopping background commissionable node scan"
+ "[%{public}@] Stored deferred Matter onboarding URL %{private}@; awaiting commissionable-node discovery"
+ "[%{public}@] Successfully updated vendorID to %{public}@ and productID to %{public}@ after deferred Matter commissioning"
+ "[%{public}@] Unable to create server for deferred Matter onboarding of node %@"
+ "[%{public}@] Vendor ID %{public}@ and product ID %{public}@ not updated after deferred Matter commissioning because both are not available"
+ "[%{public}@] beginDeferredMatterCommissioningWithOnboardingURL called twice; ignoring duplicate URL %{private}@"
+ "beginDeferredMatterCommissioningWithOnboardingURL called twice; ignoring duplicate URL %{private}@"
+ "block"
+ "compressedFabricId must be 8 bytes (got %lu)"
+ "deferredMatterOnboardingURL"
+ "delegate"
+ "hmmtr.bg.scan.controller"
+ "hmmtr.exclusiveserveractionqueue"
+ "online"
+ "queue"
+ "rootPublicKey must be a 65-byte uncompressed P-256 point (leading 0x04 + X || Y) or a 64-byte X || Y; got %lu bytes"
+ "server"
+ "simulateNFCPairing"
+ "\xb1\x91\x91"
+ "\xf0\xd2\xf0\xf0\xf01\xf0a"
- "Accessory with node ID %@ was added to home with fabric %@, for local control: %@"
- "[%{public}@] Accessory with node ID %@ was added to home with fabric %@, for local control: %@"
- "\x91\x91\x91"
```
