## HealthBluetoothPeripheral

> `/System/Library/Health/Plugins/HealthBluetoothPeripheral.bundle/HealthBluetoothPeripheral`

```diff

-6200.4.9.0.0
-  __TEXT.__text: 0x39b80
-  __TEXT.__auth_stubs: 0x7f0
-  __TEXT.__objc_stubs: 0x59a0
-  __TEXT.__objc_methlist: 0x3bec
-  __TEXT.__const: 0x230
-  __TEXT.__cstring: 0x1d92
-  __TEXT.__objc_methname: 0x8d6c
-  __TEXT.__oslogstring: 0x410c
-  __TEXT.__objc_classname: 0xaf8
-  __TEXT.__objc_methtype: 0x29d6
-  __TEXT.__gcc_except_tab: 0xb6c
-  __TEXT.__unwind_info: 0xf40
-  __DATA_CONST.__auth_got: 0x408
-  __DATA_CONST.__got: 0x378
-  __DATA_CONST.__const: 0x1178
-  __DATA_CONST.__cfstring: 0x19c0
+6200.5.77.2.6
+  __TEXT.__text: 0x3b94c
+  __TEXT.__auth_stubs: 0x790
+  __TEXT.__objc_stubs: 0x5ba0
+  __TEXT.__objc_methlist: 0x3ccc
+  __TEXT.__const: 0x1a0
+  __TEXT.__cstring: 0x21a0
+  __TEXT.__oslogstring: 0x4344
+  __TEXT.__objc_classname: 0xb32
+  __TEXT.__objc_methname: 0x91db
+  __TEXT.__objc_methtype: 0x2b51
+  __TEXT.__gcc_except_tab: 0xb84
+  __TEXT.__unwind_info: 0x1010
+  __DATA_CONST.__auth_got: 0x3d8
+  __DATA_CONST.__got: 0x3a8
+  __DATA_CONST.__const: 0x11c8
+  __DATA_CONST.__cfstring: 0x1d20
   __DATA_CONST.__objc_classlist: 0x1b8
-  __DATA_CONST.__objc_protolist: 0x160
+  __DATA_CONST.__objc_protolist: 0x170
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x128
-  __DATA_CONST.__objc_intobj: 0x570
-  __DATA.__objc_const: 0x7468
-  __DATA.__objc_selrefs: 0x1f50
-  __DATA.__objc_ivar: 0x570
+  __DATA_CONST.__objc_superrefs: 0x130
+  __DATA_CONST.__objc_intobj: 0x600
+  __DATA.__objc_const: 0x75a0
+  __DATA.__objc_selrefs: 0x2040
+  __DATA.__objc_ivar: 0x57c
   __DATA.__objc_data: 0x1130
-  __DATA.__data: 0x10a0
+  __DATA.__data: 0x1160
   __DATA.__bss: 0x50
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/HealthDaemon.framework/HealthDaemon
   - /System/Library/PrivateFrameworks/HealthDaemonFoundation.framework/HealthDaemonFoundation
   - /System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry
+  - /System/Library/PrivateFrameworks/NearField.framework/NearField
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D7238652-EB37-317D-BC37-9A8E265CF40C
-  Functions: 1554
+  UUID: CEB1D4C0-0B9B-3465-AF8E-68EFCC72C01B
+  Functions: 1623
   Symbols:   404
-  CStrings:  2559
+  CStrings:  2670
 
Symbols:
+ _CBPairingOptionsDistributeIRK
+ _CBPairingOptionsUseMITMAuthentication
+ _HKIsFitnessTrackingEnabled
+ _OBJC_CLASS_$_HDWorkoutAppStateMonitor
+ _OBJC_CLASS_$_NFFieldNotificationECP1_0
+ _OBJC_CLASS_$_NFHardwareManager
+ _OBJC_CLASS_$_NSAssertionHandler
+ _kHKConnectedGymPreferencesSpartanSimNFCSupport
+ _kHKTCCAccessDidChangeNotification
- _OBJC_CLASS_$_HDWatchAppStateMonitor
- _kHKPrivacyPreferencesKeyEnableFitnessTracking
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x10
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x9
CStrings:
+ "%{public}@: Ignoring tag session state change: tag state: %d"
+ "%{public}@: Received a field detect event, but it's not for the active session. Ignoring."
+ "%{public}@: Received a field detect notification, but it's not for the correct technology. Ignoring %@"
+ "%{public}@: Received an NDefTag session end unexpectedly callback, but it's not for the active session. Ignoring."
+ "%{public}@: Received an NDefTag state change callback, but it's not for the active session. Ignoring."
+ "1"
+ "@\"<NFSession>\""
+ "@\"HDWorkoutAppStateMonitor\""
+ "@\"NFHardwareManager\""
+ "Approximate start date should have been calculated"
+ "B32@0:8@\"NSString\"16@?<v@?>24"
+ "B32@0:8@16@?24"
+ "Data Collector should have been setup as part of discovery"
+ "Disabling NFCAlwaysOn for iPhone"
+ "Expected flag field length to be 2 or 3"
+ "Expected to find an aggregator for fitness machine '%@', HKObjectType %@"
+ "Expected to have a fitness machine at this point"
+ "Expected token to be configured"
+ "HDFitnessMachineDataCharacteristicBase.m"
+ "HDFitnessMachineDataCollector.m"
+ "HDFitnessMachineManager.m"
+ "HDFitnessMachineSession.m"
+ "HDGymKitPairingManager.m"
+ "HDHealthServiceCharacteristic.m"
+ "HDHealthServiceManager.m"
+ "HDWorkoutAppStateMonitorDelegate"
+ "Invalid parameter not satisfying: %@"
+ "Must have a start date if we're stopped or paused"
+ "Must have advertising address"
+ "Must have data initialized"
+ "NFFieldDetectSessionDelegate"
+ "NFNdefTagSessionDelegate"
+ "Privacy preference did change. Updating NFC always on preference"
+ "Reset should have been handled in `handleInitialMachineStatusIfNecessary`"
+ "Running or Not Yet Started should have been the first state set. fromState=%@, toState=%@"
+ "_activeFieldSession"
+ "_activeTagSession"
+ "_configureCollectorsAndAggregators"
+ "_copySignedInt:fromData:byteCount:beforeByte:"
+ "_copyUnsignedInt:fromData:byteCount:beforeByte:"
+ "_handleFieldEntered"
+ "_hardwareManager"
+ "_newWorkoutAppStateMonitor"
+ "_queue_handleInfoAfterDiscovery:machineType:"
+ "_queue_handleInitialStateIfNecessary"
+ "_queue_handleReceivedDataCharacteristic:"
+ "_queue_processDataCharacteristic:"
+ "_queue_setDeviceInformation:"
+ "_queue_setMachineState:date:"
+ "autoPairData"
+ "count <= sizeof(int32_t)"
+ "count <= sizeof(uint32_t)"
+ "currentHandler"
+ "daemonDidReceiveRapportEvent:completion:"
+ "endSession"
+ "fieldDetectSession:didDetectField:"
+ "fieldDetectSession:didDetectTechnology:"
+ "fieldDetectSession:didEnterFieldWithNotification:"
+ "fieldDetectSessionDidEndUnexpectedly:"
+ "fieldDetectSessionDidExitField:"
+ "handleFailureInMethod:object:file:lineNumber:description:"
+ "initWithSessionHandler:dataHandler:characteristicsHandler:mfaSuccessHandler:autoPairData:connectionOptions:timeoutInterval:peripheralUUID:"
+ "isIPhone"
+ "kcal/(kg*hr)"
+ "mets"
+ "name.length > 0"
+ "ndefTagSession:didTagStateChange:"
+ "ndefTagSessionDidEndUnexpectedly:"
+ "notificationType"
+ "pairPeer:options:"
+ "samplesMapWereRemoved:anchor:"
+ "serverKey != nil"
+ "setMets:"
+ "sharedHardwareManager"
+ "startFieldDetectSession:"
+ "startNdefTagSessionWithBluetoothLESecureOOBData:callback:"
+ "supportsGymKit"
+ "terminalType"
+ "v24@0:8@\"HDWorkoutAppStateMonitor\"16"
+ "v24@0:8@\"NFFieldDetectSession\"16"
+ "v24@0:8@\"NFNdefTagSession\"16"
+ "v24@?0@\"NFFieldDetectSession\"8@\"NSError\"16"
+ "v24@?0@\"NFNdefTagSession\"8@\"NSError\"16"
+ "v28@0:8@\"NFFieldDetectSession\"16B24"
+ "v28@0:8@\"NFNdefTagSession\"16I24"
+ "v28@0:8@16I24"
+ "v32@0:8@\"NFFieldDetectSession\"16@\"NFFieldNotification\"24"
+ "v32@0:8@\"NFFieldDetectSession\"16@\"NFTechnologyEvent\"24"
+ "v32@0:8@\"NSDictionary\"16@\"NSNumber\"24"
- "@\"HDWatchAppStateMonitor\""
- "HDWatchAppStateMonitorDelegate"
- "UTF8String"
- "_newWatchAppStateMonitor"
- "isAppleWatch"
- "pairPeer:"
- "v24@0:8@\"HDWatchAppStateMonitor\"16"

```
