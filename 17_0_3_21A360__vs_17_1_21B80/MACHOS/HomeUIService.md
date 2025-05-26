## HomeUIService

> `/Applications/HomeUIService.app/HomeUIService`

```diff

-803.3.7.1.5
-  __TEXT.__text: 0x5b400
-  __TEXT.__auth_stubs: 0x7c0
-  __TEXT.__objc_stubs: 0xd840
-  __TEXT.__objc_methlist: 0x5308
-  __TEXT.__objc_methname: 0x13662
-  __TEXT.__cstring: 0x6f52
-  __TEXT.__objc_classname: 0x12f7
-  __TEXT.__objc_methtype: 0x38da
+825.2.8.1.1
+  __TEXT.__text: 0x5cb54
+  __TEXT.__auth_stubs: 0x7d0
+  __TEXT.__objc_stubs: 0xdb40
+  __TEXT.__objc_methlist: 0x54c0
+  __TEXT.__objc_methname: 0x13d60
+  __TEXT.__cstring: 0x7289
+  __TEXT.__objc_classname: 0x1314
+  __TEXT.__objc_methtype: 0x3a3b
   __TEXT.__const: 0xc0
-  __TEXT.__oslogstring: 0x5b61
-  __TEXT.__gcc_except_tab: 0x7f4
+  __TEXT.__oslogstring: 0x5c77
+  __TEXT.__gcc_except_tab: 0x858
   __TEXT.__dlopen_cstrs: 0x52
-  __TEXT.__unwind_info: 0x1630
-  __DATA_CONST.__auth_got: 0x3f0
+  __TEXT.__unwind_info: 0x1680
+  __DATA_CONST.__auth_got: 0x3f8
   __DATA_CONST.__got: 0x3d8
-  __DATA_CONST.__const: 0x2980
-  __DATA_CONST.__cfstring: 0x3760
+  __DATA_CONST.__const: 0x29f0
+  __DATA_CONST.__cfstring: 0x3800
   __DATA_CONST.__objc_classlist: 0x378
   __DATA_CONST.__objc_catlist: 0x20
-  __DATA_CONST.__objc_protolist: 0x190
+  __DATA_CONST.__objc_protolist: 0x198
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_intobj: 0xc48
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__objc_arraydata: 0xa0
   __DATA_CONST.__objc_arrayobj: 0x60
-  __DATA.__objc_const: 0xe9d8
-  __DATA.__objc_selrefs: 0x3dc8
+  __DATA.__objc_const: 0xef40
+  __DATA.__objc_selrefs: 0x3e98
   __DATA.__objc_protorefs: 0x20
-  __DATA.__objc_classrefs: 0x888
+  __DATA.__objc_classrefs: 0x890
   __DATA.__objc_superrefs: 0x320
-  __DATA.__objc_ivar: 0x5b8
+  __DATA.__objc_ivar: 0x5f0
   __DATA.__objc_data: 0x22b0
-  __DATA.__data: 0x12c0
+  __DATA.__data: 0x1320
   __DATA.__bss: 0xa8
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2223
-  Symbols:   473
-  CStrings:  4531
+  Functions: 2264
+  Symbols:   475
+  CStrings:  4613
 
Symbols:
+ _HMSetupAccessoryProgressAsString
+ _OBJC_CLASS_$_NSHashTable
CStrings:
+ "\x06\x16\x15"
+ "%s old phase: %@ new phase: %@"
+ "%s received progress update: %@"
+ "%s received stagingRequestUUID that does not match"
+ "-[HSProximityCardHostViewController _updatePairingStatusIfNecessary:phase:]"
+ "-[HSSetupStateMachineCHIPPartnerConfiguration didUpdateProgress:forStagingRequestUUID:]"
+ "-[HSSetupStateMachineCHIPPartnerConfiguration setPhase:]"
+ "@\"HFDiscoveredAccessory\"16@0:8"
+ "@\"HFSetupAccessoryResult\""
+ "@\"HFSetupAccessoryResult\"16@0:8"
+ "@\"HFSetupPairingContext\"16@0:8"
+ "@\"HMAccessorySetupCompletedInfo\""
+ "@\"HMAccessorySetupCompletedInfo\"16@0:8"
+ "@\"HMHome\"16@0:8"
+ "@\"MTSSystemCommissionerPairing\""
+ "@\"NSHashTable\""
+ "@\"NSSet\"16@0:8"
+ "@\"NSTimer\""
+ "Accessory not found fatal timeout timer fired"
+ "Accessory not found soft timeout timer fired %@"
+ "HFSetupAutomaticDiscoveryPairingController can't handle changing the setup result (payload) after pairing has already started. Set the setup result before calling -startWithHome:, and create a new pairing controller if you need to change it later. Current phase = %@"
+ "HFSetupPairingController"
+ "HSSetupStateMachineConfiguration.m"
+ "Received setup result: %@"
+ "T@\"<HFSetupPairingObserver>\",&,V_pairingObserver"
+ "T@\"HFDiscoveredAccessory\",&,N,V_discoveredAccessoryToPair"
+ "T@\"HFDiscoveredAccessory\",R,N"
+ "T@\"HFSetupAccessoryResult\",&,N"
+ "T@\"HFSetupAccessoryResult\",&,N,V_setupResult"
+ "T@\"HFSetupPairingContext\",R,N"
+ "T@\"HFSetupPairingContext\",W,N,V_context"
+ "T@\"HMAccessorySetupCompletedInfo\",R,N"
+ "T@\"HMAccessorySetupCompletedInfo\",R,N,V_completedInfo"
+ "T@\"HMSetupAccessoryDescription\",&,N,V_setupDescription"
+ "T@\"MTSSystemCommissionerPairing\",&,N,V_currentPairing"
+ "T@\"NSDate\",&,N,V_phaseStartDate"
+ "T@\"NSHashTable\",&,N,V_pairingObservers"
+ "T@\"NSString\",&,N,V_statusDescription"
+ "T@\"NSString\",&,N,V_statusTitle"
+ "T@\"NSTimer\",&,N,V_accessoryNotFoundFatalTimeoutTimer"
+ "T@\"NSTimer\",&,N,V_accessoryNotFoundSoftTimeoutTimer"
+ "The 'accessory not found' fatal timeout timer should only fire if we remain in the 'discoverAccessories' phase for too long, but instead, we're in the %@ phase"
+ "The 'accessory not found' soft timeout timer should only fire if we remain in the 'discoverAccessories' phase for too long, but instead, we're in the %@ phase"
+ "Updating status title: \"%@\" description: \"%@\""
+ "_accessoryNotFoundFatalTimeoutTimer"
+ "_accessoryNotFoundSoftTimeoutTimer"
+ "_completedInfo"
+ "_currentPairing"
+ "_discoveredAccessoryToPair"
+ "_pairingObservers"
+ "_phaseStartDate"
+ "_setupDescription"
+ "_setupResult"
+ "_statusDescription"
+ "_statusTitle"
+ "_updatePairingStatusIfNecessary:phase:"
+ "_updateStatusTextAndNotifyDelegate:"
+ "a"
+ "accessoryDiscoveryFatalTimeout"
+ "accessoryDiscoverySoftTimeout"
+ "accessoryNotFoundFatalTimeoutTimer"
+ "accessoryNotFoundSoftTimeoutTimer"
+ "currentPairing"
+ "getStatusTitle:statusDescription:forPairingPhase:phaseStartDate:discoveredAccessory:setupResult:context:setupError:"
+ "hmf_isEqualToUUID:"
+ "isUnknownGuest"
+ "notifyDelegateOfPairingFailureWithError:"
+ "pairingObservers"
+ "phaseStartDate"
+ "processThirdPartyAccessorySetupProgressChange:currentPhase:context:discoveredAccessory:setupResult:callerClass:"
+ "setAccessoryNotFoundFatalTimeoutTimer:"
+ "setAccessoryNotFoundSoftTimeoutTimer:"
+ "setCurrentPairing:"
+ "setDiscoveredAccessoryToPair:"
+ "setPairingObservers:"
+ "setPhaseStartDate:"
+ "setRawSetupPayloadString:"
+ "setSetupDescription:"
+ "setStatusDescription:"
+ "setStatusTitle:"
+ "stageCHIPAccessory Accessory Discovery Timed Out"
+ "supportsSetupPayloadRetry"
+ "updatePairingStatus:phase:"
+ "v24@0:8@\"<HFSetupPairingObserver>\"16"
+ "v24@0:8@\"HFSetupAccessoryResult\"16"
+ "weakObjectsHashTable"
- "\a"
- "+"
- "-[HSProximityCardHostViewController _updatePairingStatusIfNecessary:]"
- "_updatePairingStatusIfNecessary:"
- "updatePairingStatus:"

```
