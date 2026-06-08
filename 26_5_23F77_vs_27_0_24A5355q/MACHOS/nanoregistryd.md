## nanoregistryd

> `/usr/libexec/nanoregistryd`

```diff

-1027.32.0.0.0
-  __TEXT.__text: 0x110e40
-  __TEXT.__auth_stubs: 0x10d0
-  __TEXT.__objc_stubs: 0x10e40
-  __TEXT.__objc_methlist: 0xd934
-  __TEXT.__const: 0x698
-  __TEXT.__gcc_except_tab: 0x2470
-  __TEXT.__objc_methname: 0x1c2ef
-  __TEXT.__cstring: 0xdcd5
-  __TEXT.__oslogstring: 0x15b25
-  __TEXT.__objc_classname: 0x225b
-  __TEXT.__objc_methtype: 0x4a78
+1070.0.0.0.0
+  __TEXT.__text: 0x1003d0
+  __TEXT.__auth_stubs: 0x1100
+  __TEXT.__objc_stubs: 0x10fe0
+  __TEXT.__objc_methlist: 0xdacc
+  __TEXT.__const: 0x69a
+  __TEXT.__gcc_except_tab: 0x1cd8
+  __TEXT.__objc_methname: 0x1c595
+  __TEXT.__cstring: 0xe041
+  __TEXT.__oslogstring: 0x1609d
+  __TEXT.__objc_classname: 0x21b9
+  __TEXT.__objc_methtype: 0x4baf
   __TEXT.__dlopen_cstrs: 0xef
   __TEXT.__ustring: 0x4ac
-  __TEXT.__unwind_info: 0x4290
-  __DATA_CONST.__auth_got: 0x878
-  __DATA_CONST.__got: 0xc88
-  __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x4a40
-  __DATA_CONST.__cfstring: 0xbe00
-  __DATA_CONST.__objc_classlist: 0x7c8
+  __TEXT.__unwind_info: 0x3a68
+  __DATA_CONST.__const: 0x4ba0
+  __DATA_CONST.__cfstring: 0xbfc0
+  __DATA_CONST.__objc_classlist: 0x7e8
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x220
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x40
-  __DATA_CONST.__objc_superrefs: 0x3d8
-  __DATA_CONST.__objc_intobj: 0xde0
+  __DATA_CONST.__objc_superrefs: 0x3e0
+  __DATA_CONST.__objc_intobj: 0xe10
   __DATA_CONST.__objc_doubleobj: 0xb0
-  __DATA_CONST.__objc_arraydata: 0x470
+  __DATA_CONST.__objc_arraydata: 0x478
   __DATA_CONST.__objc_dictobj: 0x168
-  __DATA_CONST.__objc_arrayobj: 0x1f8
-  __DATA.__objc_const: 0x19f98
-  __DATA.__objc_selrefs: 0x5e20
-  __DATA.__objc_ivar: 0x11cc
-  __DATA.__objc_data: 0x4dd0
+  __DATA_CONST.__objc_arrayobj: 0x210
+  __DATA_CONST.__auth_got: 0x890
+  __DATA_CONST.__got: 0xc90
+  __DATA_CONST.__auth_ptr: 0x10
+  __DATA.__objc_const: 0x1a360
+  __DATA.__objc_selrefs: 0x5e80
+  __DATA.__objc_ivar: 0x11dc
+  __DATA.__objc_data: 0x4f10
   __DATA.__data: 0x19d8
-  __DATA.__bss: 0x488
+  __DATA.__bss: 0x4b8
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/SOS.framework/SOS
+  - /System/Library/PrivateFrameworks/SecurePairing.framework/SecurePairing
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /System/Library/PrivateFrameworks/UIKitServices.framework/UIKitServices

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  UUID: 9B700FC4-951B-3986-A042-F1215FC68C95
-  Functions: 5781
-  Symbols:   694
-  CStrings:  10214
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswiftos.dylib
+  UUID: 0D612026-E391-3F2A-90A9-0EB70FC2B97D
+  Functions: 5823
+  Symbols:   705
+  CStrings:  10287
 
Symbols:
+ _NRDevicePropertyDeviceGroup
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swiftos
+ _objc_claimAutoreleasedReturnValue
+ _objc_opt_self
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x6
- _IDSGetPairedDevicesWithCompletionBlock
CStrings:
+ "%@: %lu bytes"
+ "%s no-op, not actively pairing (Bluetooth UUID: %@)"
+ "%s: Skipping daemon normalization for active device %{public}@"
+ "%s: Timeout"
+ "%s: skipping %{public}@"
+ "%{public}s: Reverting back to %@"
+ "-[EPSagaTransactionPairing networkRelayPairingCompletedWithIdentifier:pairingOptionsFromPeer:error:]"
+ "-[EPSagaTransactionSendUnpairMessage setRemoteUnpairTimeout]_block_invoke"
+ "-[NRNetworkRelayPair networkRelayPairingCompletedWithIdentifier:pairingOptionsFromPeer:error:]_block_invoke"
+ "-[NRPairingDaemon _updateDeviceGroupForDevice:]"
+ "-[NRPairingDaemon _updateDeviceGroupForDevicesInCollection:]"
+ "-[NRPairingDaemon normalizeDaemonStateWithBlock:]_block_invoke"
+ "-[NRPairingDaemon xpcGizmoOOBAdvertiseAndPairWithName:operationHasBegun:]"
+ "2"
+ "31"
+ "7a471c2e-14ac-402e-b969-fa47726556fa"
+ "@32@0:8@16^B24"
+ "AdvertisingIdentifierSeed"
+ "ArrowChipID"
+ "Build Configuration: NANOREGISTRY_VISION 0"
+ "Device with ID %{public}@ has no device group, assuming Watch!"
+ "DeviceEnclosureMaterial"
+ "DeviceSupportsAlwaysOnTime"
+ "DeviceSupportsBrook"
+ "DeviceSupportsEnvironmentalDosimetry"
+ "DeviceSupportsFloorCounting"
+ "DeviceSupportsHeartHealthAlerts"
+ "DeviceSupportsRaiseToSpeak"
+ "DeviceSupportsSiriSpeaks"
+ "EPMobileAssetAutoTrigger: No v2 asset found; falling back to v1"
+ "EPMobileAssetAutoTrigger: Purging orphaned v1 asset %{public}@"
+ "EPMobileAssetAutoTrigger: v1 asset %{public}@ failed to be purged with result %lu and error %{public}@"
+ "EPMobileAssetAutoTrigger: v1 asset %{public}@ purged successfully"
+ "EPSagaOperandData"
+ "Failure to deserialize global state plist: %{public}@"
+ "Failure to serialize global state plist: %{public}@"
+ "Failure to write global state plist: %{public}@"
+ "Generating a new advertising seed"
+ "GlobalState.plist"
+ "HomeButtonType"
+ "MarketingProductName"
+ "Migrated advertising seed"
+ "Migrated tracker identifier"
+ "Migrated tracker state"
+ "NRPBRemotePairingOptions"
+ "NRPairingReportSubreasonSecurePairingFailure"
+ "NRPrivateGlobalState"
+ "NRPropertiesCoding"
+ "NRTermsAcknowledgementRegistryService: Device locked, deferring load of terms event log."
+ "NRTermsAcknowledgementRegistryService: Error reading terms event log: %@. Creating new NRTermsEventCollection."
+ "NRTermsAcknowledgementRegistryService: Error unarchiving terms event log: %@. Creating new NRTermsEventCollection."
+ "NanoRegistry-1070"
+ "Not implemented on platform"
+ "Not updating Device Group for %@"
+ "Pairing flow no longer active, not requesting PreShared auth (advertised name: %{public}@ (identifier %{public}@)"
+ "SecureElement"
+ "SecurePairing"
+ "SupportsRotateToWake"
+ "T@\"NSData\",R,N,V_data"
+ "TB,N,V_isPairing"
+ "TB,R,N,V_securePairing"
+ "TestDarwinNotification"
+ "UDID changed and ignoreUDIDChanged is set but not honored — unsupported configuration (VM %{BOOL}d, Internal %{BOOL}d)"
+ "UDID changed but ignoreUDIDChanged is set on internal VM — reporting no change"
+ "Watch"
+ "WatchSupportsAutoPlaylistPlayback"
+ "WatchSupportsMusicStreaming"
+ "_currentPairingAttemptSupportsSecurePairing"
+ "_isPairing"
+ "_networkRelayAgentPairingCompletedWithIdentifier:pairingOptionsFromPeer:error:"
+ "_notifyDelegatesOfPairingCompletionWithIdentifier:pairingOptionsFromPeer:error:"
+ "_securePairing"
+ "_updateDeviceGroupForDevice:"
+ "_updateDeviceGroupForDevicesInCollection:"
+ "_upsertDeviceDiscoveredBy:pairingID:advertisedName:deviceGroup:bluetoothDeviceID:rssiValue:withBlock:"
+ "a781cb9f-7992-4ee7-a6ba-723b6fb0b65e"
+ "createDeviceFromNetworkRelayDiscoveryWithAdvertisementName:deviceGroup:bluetoothIdentifier:withRSSI:withBlock:"
+ "createDeviceFromPairingRequest:discoveredBy:deviceGroup:withBlock:"
+ "createUnpairTransactionsWithCompletion: Updating DeviceGroup for devices in %{public}@"
+ "createUnpairTransactionsWithCompletion: Vision device %{public}@ missing data store path, but allowing persistence for pairing"
+ "currentPairingAttemptSupportsSecurePairing"
+ "dataWithContentsOfURL:"
+ "deviceGroup"
+ "downloadAsset:fromQuery:catalogDownloadError:userInitiated:completion:"
+ "electionOutcomeChanged: statusCode=%lu"
+ "getCanPairAnotherWatchWithCompletion:"
+ "iPhone"
+ "ignoreUDIDChanged"
+ "magicSwitch.advertisingSeed"
+ "networkRelayPairingCompletedWithIdentifier:pairingOptionsFromPeer:error:"
+ "peripheral:didCompleteChannelSoundingSession:"
+ "peripheral:didReceiveChannelSoundingProcedureResults:error:"
+ "propertyListWithData:options:format:error:"
+ "purgeInstalledV1AssetsForAssetType:"
+ "restoreTracker.identifier"
+ "restoreTracker.state"
+ "scanCollectionForAlertsConfiguration"
+ "securePairing"
+ "securePairingError"
+ "sendXPCPairingPeerInfo:"
+ "sendXPCPairingPeerInfo: %@"
+ "setIsPairing:"
+ "sigUsr2"
+ "stringsTables"
+ "unpackProperties:"
+ "unpackProperties:thisIsAllOfThem:"
+ "unpairStaleArchivedDevicesWithCompletion: Vision device %@ in setup during NR restart, but allowing persistence for pairing"
+ "v24@0:8@\"NSDictionary\"16"
+ "v24@0:8@?<v@?@\"NSUUID\">16"
+ "v40@0:8@\"CBPeripheral\"16@\"CBChannelSoundingProcedureResults\"24@\"NSError\"32"
+ "v40@0:8@\"NSString\"16@\"NSDictionary\"24@?<v@?@\"NSError\">32"
+ "v40@0:8@\"NSUUID\"16@\"NSDictionary\"24@\"NSError\"32"
+ "v48@0:8@\"NSString\"16Q24q32@?<v@?@\"NSUUID\">40"
+ "v48@0:8@16Q24q32@?40"
+ "v52@0:8@16@24@32B40@?44"
+ "v56@0:8@16q24@32@40@?48"
+ "v72@0:8Q16@24@32q40@48q56@?64"
+ "xpcAdvertisingIdentifierSeedWithCompletion:"
+ "xpcGizmoOOBAdvertiseAndPairWithName: advertisedName=%{public}@, options=%{public}@"
+ "xpcGizmoOOBAdvertiseAndPairWithName:withOptions:operationHasBegun:"
+ "xpcGizmoPasscodeAdvertiseAndPairWithName: advertisedName=%{public}@, options=%{public}@"
+ "xpcGizmoPasscodeAdvertiseAndPairWithName:withOptions:operationHasBegun:"
+ "xpcPairingPeerInfo:"
+ "xpcSetAdvertisingIdentifierSeed:"
+ "{?=\"currentPairingAttemptSupportsSecurePairing\"b1}"
- "%{public}s: Pref sync failed."
- "%{public}s:Reverting back to %@"
- "+[EPSagaTransactionSetDaemonsEnabled getNormalDaemonValueWith:serviceRegistry:forceEnableWhenPairedOrActive:completion:]_block_invoke_2"
- "-[EPSagaTransactionPairing networkRelayPairingCompletedWithIdentifier:error:]"
- "/bfa1LxXd7G1WqHujpjsdA"
- "0dnM19zBqLw5ZPhIo4GEkg"
- "282f1ee6-a144-4106-affb-2bdb5b59fd0d"
- "380"
- "4D8XW4YwJI7QvyPhv1TEdw"
- "AtmPEO/j+Pdr8+WKxv4Aaw"
- "C16@0:8"
- "CnoPCMssOh+xPJJo6pvnog"
- "Deleting %@"
- "EPSagaTransactionSendUnpairMessage: Timeout"
- "Error %@ deleting %@"
- "GizmoOOB: Deferring pairing client proxy removal."
- "GizmoOOB: Removing pairing client proxy."
- "GizmoPasscode: Deferring pairing client proxy removal."
- "GizmoPasscode: removing pairing client proxy."
- "H+r3Nk8ByXIY9ub/M8broA"
- "IDS returned paired devices: %{public}@"
- "IDS returned paired devices: nil"
- "IDSGetPairedDevices"
- "JwLB44/jEB8aFDpXQ16Tuw"
- "Localizable-tinker"
- "NanoRegistry-1027.32"
- "Not implemented on watch"
- "PTQ+ABwag03BwO/CKvIK/A"
- "SaW+DA+cbiqDHrex8MTABA"
- "T@\"NRPreferences\",&,V_preferences"
- "TR6Z82EVZEKMVUdHfkhDmQ"
- "_deleteSharingPathWithPairingID:"
- "_networkRelayAgentPairingCompletedWithIdentifier:error:"
- "_notifyDelegatesOfPairingCompletionWithIdentifier:error:"
- "_preferences"
- "_unpackProperties:"
- "_upsertDeviceDiscoveredBy:pairingID:advertisedName:bluetoothDeviceID:rssiValue:withBlock:"
- "com.apple.sharing"
- "createDeviceFromNetworkRelayDiscoveryWithAdvertisementName:bluetoothIdentifier:withRSSI:withBlock:"
- "createDeviceFromPairingRequest:discoveredBy:withBlock:"
- "getCanPairAnotherDeviceWithCompletion:"
- "j8/Omm6s1lsmTDFsXjsBfA"
- "j9Th5smJpdztHwc+i39zIg"
- "nK4D+jDUuTGFFwRFPC2lWg"
- "networkRelayPairingCompletedWithIdentifier:error:"
- "nhGhVMyvrWYe9U2ltAUImg"
- "nmOy2K5HzAAs2QNAi8wR+Q"
- "pairingVersionFromAdvertisedName:"
- "preferences"
- "q24@0:8@16"
- "resetWatchStateForNewPairing"
- "scanCollectionForUpdateModeDevices"
- "setPreferences:"
- "v20@0:8C16"
- "v32@0:8@\"NSUUID\"16@\"NSError\"24"
- "v40@0:8@\"NSString\"16Q24@?<v@?@\"NSUUID\">32"
- "v64@0:8Q16@24@32@40q48@?56"
- "xRyzf9zFE/ycr/wJPweZvQ"
- "xpcGizmoOOBAdvertiseAndPairWithName: advertisedName=%{public}@"
- "xpcGizmoOOBAdvertiseAndPairWithName: advertisedName=%{public}@ Starting..."
- "xpcGizmoPasscodeAdvertiseAndPairWithName: advertisedName=%{public}@"
- "xpcGizmoPasscodeAdvertiseAndPairWithName: advertisedName=%{public}@ Starting..."
- "xpcGizmoPasscodeAdvertiseAndPairWithName:operationHasBegun:"

```
