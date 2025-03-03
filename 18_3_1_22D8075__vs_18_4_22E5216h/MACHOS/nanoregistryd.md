## nanoregistryd

> `/usr/libexec/nanoregistryd`

```diff

-989.4.9.0.0
-  __TEXT.__text: 0xf7d4c
+989.19.0.0.0
+  __TEXT.__text: 0xfd530
   __TEXT.__auth_stubs: 0x10a0
-  __TEXT.__objc_stubs: 0x10a00
-  __TEXT.__objc_methlist: 0xbd80
-  __TEXT.__const: 0x688
-  __TEXT.__gcc_except_tab: 0x24fc
-  __TEXT.__objc_methname: 0x1b6ba
-  __TEXT.__cstring: 0xd1dd
-  __TEXT.__oslogstring: 0x13a88
-  __TEXT.__objc_classname: 0x2168
-  __TEXT.__objc_methtype: 0x490b
+  __TEXT.__objc_stubs: 0x10ce0
+  __TEXT.__objc_methlist: 0xd6e4
+  __TEXT.__const: 0x678
+  __TEXT.__gcc_except_tab: 0x2638
+  __TEXT.__objc_methname: 0x1bcaf
+  __TEXT.__cstring: 0xd71b
+  __TEXT.__oslogstring: 0x149ba
+  __TEXT.__objc_classname: 0x21a5
+  __TEXT.__objc_methtype: 0x492e
   __TEXT.__dlopen_cstrs: 0xef
   __TEXT.__ustring: 0x4ac
-  __TEXT.__unwind_info: 0x38d8
+  __TEXT.__unwind_info: 0x39e8
   __DATA_CONST.__auth_got: 0x860
-  __DATA_CONST.__got: 0xc50
+  __DATA_CONST.__got: 0xc78
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x4a38
-  __DATA_CONST.__cfstring: 0xba80
-  __DATA_CONST.__objc_classlist: 0x7a0
+  __DATA_CONST.__const: 0x4b50
+  __DATA_CONST.__cfstring: 0xbb20
+  __DATA_CONST.__objc_classlist: 0x7a8
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x220
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_superrefs: 0x3d0
-  __DATA_CONST.__objc_intobj: 0xdb0
+  __DATA_CONST.__objc_intobj: 0xde0
   __DATA_CONST.__objc_doubleobj: 0xb0
   __DATA_CONST.__objc_arraydata: 0x470
   __DATA_CONST.__objc_dictobj: 0x168
   __DATA_CONST.__objc_arrayobj: 0x1f8
-  __DATA.__objc_const: 0x1bf88
-  __DATA.__objc_selrefs: 0x5960
-  __DATA.__objc_ivar: 0x1140
-  __DATA.__objc_data: 0x4c40
+  __DATA.__objc_const: 0x19810
+  __DATA.__objc_selrefs: 0x5d20
+  __DATA.__objc_ivar: 0x1170
+  __DATA.__objc_data: 0x4c90
   __DATA.__data: 0x19d8
   __DATA.__bss: 0x4a8
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  Functions: 5594
-  Symbols:   684
-  CStrings:  8479
+  Functions: 5692
+  Symbols:   689
+  CStrings:  8589
 
Symbols:
+ _NRAdvertisingInfoFromPayload
+ _NRBridgeAdvertisingVersionKey
+ _NRDevicePairingErrorDomain
+ _NRDevicePairingErrorOriginalCBUUIDKey
+ _NRDevicePairingErrorOriginalNRUUIDKey
+ _OBJC_CLASS_$_NRDevicePairingProperties
- _fmod
CStrings:
+ "\nUnderlying: %@ (%ld)"
+ "\v\x13\x11"
+ "\x13\x12"
+ "%s NetworkRelay identifier: %@"
+ "%s bluetooth identifier: %@"
+ "%s calling startPairing for migration on candidate %@"
+ "%s discovered a migration candidate with NetworkRelay identifier %{public}@. Requesting migration."
+ "%s discovered an unexpected migration candidate with NetworkRelay identifier %{public}@, looking for %{public}@"
+ "%s got error: %@"
+ "%s iAmACompanionDevice %{BOOL}d"
+ "%s iAmACompanionDevice %{BOOL}d, %{public}@"
+ "%s identifier: %{public}@ error:%{public}@"
+ "%s network relay migration candidate found, requesting migration"
+ "%s network relay migration candidate not found yet, start scanning with network relay identifier %{public}@"
+ "%s networkRelayDeviceIdentifier %{public}@, nanoRegistryDeviceIdentifier %{public}@"
+ "%s networkRelayDeviceIdentifier %{public}@, nanoRegistryDeviceIdentifier %{public}@, diff %{public}@"
+ "%s no network relay identifier to start scan"
+ "-[EPSagaTransactionPairing _networkRelayMigrationPairing]"
+ "-[EPSagaTransactionPairing _networkRelayMigrationUnpairing]"
+ "-[EPSagaTransactionPairing _requestMigrationAndPairWithCandidateWithNetworkRelayIdentifier:]_block_invoke"
+ "-[EPSagaTransactionPairing _requestMigrationAndPairWithCandidateWithNetworkRelayIdentifier:]_block_invoke_2"
+ "-[EPSagaTransactionPairing discoveredMigrationCandidateWithNetworkRelayIdentifier:]"
+ "-[EPSagaTransactionPairing networkRelayPairingCompletedWithIdentifier:error:]"
+ "-[EPSagaTransactionUpdateNRDeviceWithNewNetworkRelayDevice beginTransactionWithRoutingSlipEntry:serviceRegistry:]"
+ "-[EPSagaTransactionUpdateNRDeviceWithNewNetworkRelayDevice beginTransactionWithRoutingSlipEntry:serviceRegistry:]_block_invoke"
+ "-[NRPairingDaemon receivedMigrationAuthenticationRequest]"
+ "-[NetworkRelayAgent abortCurrentPairing]"
+ "-[NetworkRelayAgent migrationPairWithCandidateWithBluetoothIdentifier:completion:]"
+ "-[NetworkRelayAgent requestMigrationFromCandidateWithNetworkRelayIdentifier:completion:]"
+ "-[NetworkRelayAgent resetMigrationPairingManager]"
+ "-[NetworkRelayAgent startScanningForMigrationCandidatesWithNetworkRelayIdentifiers:]"
+ "137"
+ "?\x02"
+ "Activated NRDevicePairingManager for migration without any error"
+ "Activating NRDevicePairingManager for migration"
+ "Auth method request from migration candidate with NetworkRelay identifier: %@ completed with error %@"
+ "Calling localPairingAddPairedDeviceWithInfoBlock with key = %{BOOL}d"
+ "Candidate discovered: %@ (bluetooth UUID %@)"
+ "Candidate lost: %@ (bluetooth UUID %@)"
+ "Candidate with identifier %{public}@ is ready to accept PIN request (no auth request pending): %{BOOL}d"
+ "Duplicate candidate discovered with different bluetooth UUID:- previous %@ (%@), new %@ (%@)"
+ "Duplicate candidate discovered with identical bluetooth UUID:- previous %@, new %@"
+ "E6F0AB1C-320C-4941-9948-D2EAE7BA9A51"
+ "EPMigrationAutoTrigger: A NetworkRelay migration candidate was discovered"
+ "EPSagaTransactionUpdateNRDeviceWithNewNetworkRelayDevice"
+ "Error = device already paired at NetworkRelay, should unpair and try again"
+ "Failed to activate NRDevicePairingManager for migration with error %{public}@"
+ "IDSLocalPairingStopForDevice %@ completed with error %@, calling IDSLocalPairingAddPairedDeviceWithInfo (localPairingAddPairedDeviceWithInfoBlock) with key = %{BOOL}d"
+ "Migration candidate discovered: %@ (NetworkRelay UUID %@, Bluetooth UUID %@)"
+ "Migration candidate lost: %@ (CBUUID %@)"
+ "Migration discovery started"
+ "NRPairingReportSubreasonNetworkRelayPairingFailed"
+ "NanoRegistry-989.19"
+ "NetworkRelay reported ghost NetworkRelay device with identifier %@, unpairing"
+ "NetworkRelayIdentifier for device with Bluetooth identifier %@ is %{public}@"
+ "NetworkRelayPair: Ghost device UUID %@ matches paired NR device %@"
+ "NetworkRelayPairing is enabled, start scanning for migratable Watches using NetworkRelay"
+ "NetworkRelayPairing is enabled, stop scanning for migratable Watches using NetworkRelay"
+ "Niling pairing manager after external invalidation"
+ "Not retry pairing since unpairing ghost NetworkRelay device failed"
+ "Pairing using PIN auth data with candidate with identifier = %{public}@ (%{public}@) started with error %{public}@"
+ "Previously paired Bluetooth identifiers: %{public}@"
+ "Received a request to start scanning for different set of migration candidates, resetting the current scanning manager"
+ "Received a request to start scanning for same set of migration candidates, no-op"
+ "Recently lost candidate %@ is not equal to the one in identifier/candidate map %@"
+ "Recently lost candidate %@ is not in identifier/candidate map"
+ "Removing lost candidate %@ from identifier/candidate map"
+ "Requesting auth method %lu from migration candidate with NetworkRelay identifier: %@"
+ "Restart pushing candidates after previous pairing manager went away"
+ "Restart scanning after previous pairing manager went away"
+ "Retry pairing after unpaired ghost NetworkRelay device"
+ "Scanning manager for migration invalidated with %@"
+ "Start migration discovery failed with error %{public}@"
+ "Starting migration discovery"
+ "T@\"NetworkRelayAgent\",&,N,V_networkRelayAgent"
+ "TB,R,N,V_iAmACompanionDevice"
+ "TB,R,N,V_useNetworkRelayPairing"
+ "Unable to locate migration candidate with NetworkRelay identifier: %@"
+ "Unable to locate migration candidate with bluetooth identifier: %@"
+ "Unpairing ghost NetworkRelay device with Network Relay Identifier %{public}@ completed with error %{public}@"
+ "[Checking for NetworkRelay migration] Migratable device with ID %{public}@ should use NetworkRelay = %{BOOL}d"
+ "[Checking for direct BT migration] Migratable device with ID %{public}@ should use NetworkRelay = %{BOOL}d"
+ "[Push-New] requestAuthMethodForDevice on %{public}@ completed with error = %{public}@"
+ "[Push] Not calling requestAuthMethodForDevice with method %lu on an already requested candidate %@"
+ "[Push] recently pushed candidate has PIN request pending"
+ "[Push] requestAuthMethodForDevice on %{public}@ completed with error = %{public}@"
+ "_authRequestPendingIdentifiers"
+ "_deviceCollection:diffToUpdateNetworkRelayId:ofDevice:"
+ "_directBluetoothMigrationPairing"
+ "_directBluetoothMigrationUnpairing"
+ "_iAmACompanionDevice"
+ "_migrationCandidates"
+ "_migrationPairingManager"
+ "_migrationScanIdentifiers"
+ "_networkRelayMigrationPairing"
+ "_networkRelayMigrationUnpairing"
+ "_notifyDelegatesOfPreviouslyPairedBluetoothIdentifiers:"
+ "_pairWithCandidate:withPreSharedAuthData:isAltAccountPairing:"
+ "_pendingIsAltAccountPairing"
+ "_pendingPINPairingCandidateIdentifier"
+ "_pendingPreSharedPairingCandidateIdentifier"
+ "_requestMigrationAndPairWithCandidateWithNetworkRelayIdentifier:"
+ "_requestPINPairingForCandidateWithIdentifier:"
+ "_shouldSilentlyRetryNetworkRelayPairingForError:"
+ "abortCurrentPairing"
+ "authMethod"
+ "cancelPairing"
+ "com.apple.nanoregistry.networkrelaypairing-report"
+ "createUpdateNetworkRelayDiff"
+ "discoveredMigrationCandidateWithNetworkRelayIdentifier:"
+ "duration"
+ "initWithHumanReadableName:"
+ "lostMigrationCandidateWithBluetoothIdentifier:"
+ "migrationCandidates"
+ "migrationPairWithCandidateWithBluetoothIdentifier:completion:"
+ "networkRelayAgent"
+ "networkRelayPairFoundPreviouslyPairedBluetoothIdentifiers:"
+ "newlyPairedNetworkRelayID"
+ "passPINAuthDataToPairingCandidate:isAltAccountPairing:"
+ "receivedMigrationAuthenticationRequest"
+ "reportNetworkRelayPairingResultWithAuthMethod:resultError:timeElapsed:"
+ "requestMigrationFromCandidateWithNetworkRelayIdentifier:completion:"
+ "requestPreSharedAuthForCandidateWithIdentifier:preSharedAuthData:isAltAccountPairing:"
+ "resetMigrationPairingManager"
+ "setIsAltAccountPairing:"
+ "setMigrationPairing:"
+ "setNetworkRelayAgent:"
+ "setNrDeviceIdentifiers:"
+ "startNetworkRelayWatchScanWithCompletion:"
+ "startScanningForMigrationCandidatesWithNetworkRelayIdentifiers:"
+ "stopScanningForMigrationCandidates"
+ "unpairDevice:queue:withCompletion:"
+ "updateDeviceNetworkRelay"
+ "useNetworkRelayPairing"
+ "v24@0:8@\"NSSet\"16"
+ "v40@0:8Q16@24d32"
+ "xpcStartAdvertisingForMigration"
+ "xpcStopAdvertisingForMigration"
- "\a\x13"
- "45"
- "?\x01"
- "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"
- "C"
- "Candidate discovered: %@"
- "Candidate lost: %@"
- "IDSLocalPairingStopForDevice %@ completed with error %@, calling IDSLocalPairingAddPairedDeviceWithInfo with key = %{BOOL}d"
- "Invalid Advertising Payload %@"
- "Invalid Advertising Payload %@ - %@ %@ %@ %@"
- "NanoRegistry-989.4.9"
- "Requested authentication method completed with error = %{public}@"
- "Tried to get rep of string rather than string-character"
- "[Push] requestAuthMethodForDevice completed with error = %{public}@"
- "_identifierDataFromName:"
- "_pairWithCandidate:withPreSharedAuthData:"
- "_pendingPairingCandidateIdentifier"
- "c"
- "f"
- "initWithAdvertisingIdentifier:pairingStrategy:deviceSize:enclosureMaterial:"
- "m"
- "n"
- "passPINAuthDataToPairingCandidate:"
- "rangeOfString:"
- "requestPreSharedAuthForCandidateWithIdentifier:preSharedAuthData:"
- "s"
- "unpairDevice:withCompletion:"
- "v"

```
