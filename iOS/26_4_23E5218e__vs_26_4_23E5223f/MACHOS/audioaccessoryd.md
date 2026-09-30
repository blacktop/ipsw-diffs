## audioaccessoryd

> `/usr/libexec/audioaccessoryd`

```diff

-34.27.1.0.0
-  __TEXT.__text: 0x23ea90
-  __TEXT.__auth_stubs: 0x2c30
-  __TEXT.__objc_stubs: 0x1d6c0
-  __TEXT.__objc_methlist: 0xdae4
+34.28.1.0.0
+  __TEXT.__text: 0x23d6a4
+  __TEXT.__auth_stubs: 0x2c20
+  __TEXT.__objc_stubs: 0x1d540
+  __TEXT.__objc_methlist: 0xda0c
   __TEXT.__const: 0x4210
-  __TEXT.__gcc_except_tab: 0x5b6c
-  __TEXT.__cstring: 0x53343
-  __TEXT.__objc_classname: 0x1003
-  __TEXT.__objc_methname: 0x2a4a5
-  __TEXT.__objc_methtype: 0x3e79
+  __TEXT.__gcc_except_tab: 0x5b70
+  __TEXT.__cstring: 0x52e83
+  __TEXT.__objc_classname: 0xff3
+  __TEXT.__objc_methname: 0x2a2d5
+  __TEXT.__objc_methtype: 0x3e59
   __TEXT.__dlopen_cstrs: 0x5a
   __TEXT.__oslogstring: 0x919a
   __TEXT.__ustring: 0x10

   __TEXT.__swift5_capture: 0x1a28
   __TEXT.__swift5_protos: 0x14
   __TEXT.__swift5_mpenum: 0x14
-  __TEXT.__unwind_info: 0x6cc0
+  __TEXT.__unwind_info: 0x6c48
   __TEXT.__eh_frame: 0x1ca0
-  __DATA_CONST.__auth_got: 0x1628
-  __DATA_CONST.__got: 0xd70
+  __DATA_CONST.__auth_got: 0x1620
+  __DATA_CONST.__got: 0xd68
   __DATA_CONST.__auth_ptr: 0x580
-  __DATA_CONST.__const: 0xba68
-  __DATA_CONST.__cfstring: 0xb2c0
-  __DATA_CONST.__objc_classlist: 0x380
+  __DATA_CONST.__const: 0xb9a0
+  __DATA_CONST.__cfstring: 0xb260
+  __DATA_CONST.__objc_classlist: 0x378
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x170
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x80
-  __DATA_CONST.__objc_superrefs: 0x200
+  __DATA_CONST.__objc_superrefs: 0x1f8
   __DATA_CONST.__objc_intobj: 0x318
   __DATA_CONST.__objc_arraydata: 0x2f8
   __DATA_CONST.__objc_dictobj: 0x500
   __DATA_CONST.__objc_arrayobj: 0x48
   __DATA_CONST.__objc_doubleobj: 0x40
-  __DATA.__objc_const: 0x1d680
-  __DATA.__objc_selrefs: 0x8b38
-  __DATA.__objc_ivar: 0x1740
-  __DATA.__objc_data: 0x3020
-  __DATA.__data: 0x4d00
-  __DATA.__bss: 0x6b80
+  __DATA.__objc_const: 0x1d548
+  __DATA.__objc_selrefs: 0x8ad8
+  __DATA.__objc_ivar: 0x172c
+  __DATA.__objc_data: 0x2fd0
+  __DATA.__data: 0x4c90
+  __DATA.__bss: 0x6b70
   __DATA.__common: 0x3a0
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox

   - /System/Library/PrivateFrameworks/PowerLog.framework/PowerLog
   - /System/Library/PrivateFrameworks/PowerUI.framework/PowerUI
   - /System/Library/PrivateFrameworks/Rapport.framework/Rapport
-  - /System/Library/PrivateFrameworks/SensingPredictServices.framework/SensingPredictServices
   - /System/Library/PrivateFrameworks/SetupAssistant.framework/SetupAssistant
   - /System/Library/PrivateFrameworks/Sharing.framework/Sharing
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 110458AA-02F8-3344-AEBA-8904E40B6197
-  Functions: 11039
-  Symbols:   1286
-  CStrings:  17068
+  UUID: CDD92576-AB8B-311E-AB44-B2F99BF39E7D
+  Functions: 11001
+  Symbols:   1284
+  CStrings:  17021
 
Symbols:
+ _OBJC_CLASS_$_OSEligibilityQuery
- _BiomeLibrary
- _OBJC_CLASS_$_BMDiscoverabilitySignals
- _OBJC_CLASS_$_SPContextMonitor
CStrings:
+ "### OSEligibility check failed: %{error}"
+ "-[SR3PRoutingDaemon _checkThoriumEligibility]"
+ "Feature not available in this region"
+ "HeadphoneFeatureQueryWithBtAddress: Not eligible (not EU region)"
+ "PrefEUCheck: %s -> %s"
+ "SR3PEUCheckSkip"
+ "_checkThoriumEligibility"
+ "answer"
+ "connectedCBDeviceUpdate: Not eligible (not EU region)"
+ "initWithDomain:error:"
- "-[AAContextManager _ensureStartedContextMonitorWithCompletion:]"
- "-[AAContextManager _ensureStartedContextMonitorWithCompletion:]_block_invoke"
- "-[AAContextManager _ensureStartedContextMonitorWithCompletion:]_block_invoke_2"
- "-[AAContextManager _ensureStartedContextMonitorWithCompletion:]_block_invoke_3"
- "-[AAContextManager _ensureStartedContextMonitorWithCompletion:]_block_invoke_4"
- "-[AAContextManager _notifyTips:]"
- "-[AAContextManager _requestSensingPredictionInfo:spl:]"
- "-[AAContextManager _requestSensingPredictionInfo:spl:]_block_invoke"
- "-[AAContextManager _wxDeviceFound:]"
- "-[AAContextManager _wxDeviceLost:]"
- "-[AAContextManager _wxDiscoveryEnsureStarted]"
- "-[AAContextManager _wxDiscoveryEnsureStarted]_block_invoke_5"
- "-[AAContextManager activate]"
- "@\"SPContextMonitor\""
- "AAContextManager"
- "AAContextManger"
- "AAContextManger Concert Venue and AirPods Nearyby Tip already shown"
- "AAContextManger Wx discovery start"
- "Activate: %@\n"
- "ConcertVenueAirPodsInEarTipShown"
- "ConcertVenueAirPodsNearbyTipShown"
- "Connected Audio Wx Device: identifier %@, productID: %d subType %d"
- "Context Monitor interrupted\n"
- "Context Monitor invalidated\n"
- "Context changed, %@ fusedState %s\n"
- "Device %@ not found in connected devices"
- "Discoverability"
- "EventVenue"
- "EventVenueWithNoise"
- "I24@0:8B16B20"
- "Signals"
- "Wx Device lost: %@ %@ productID %d"
- "_concertVenueAirPodsInEarTipShown"
- "_concertVenueAirPodsNearybyTipShown"
- "_contextMonitor"
- "_contextSignalUpdated:withFusedState:"
- "_ensureStartedContextMonitorWithCompletion error: %{error}"
- "_ensureStartedContextMonitorWithCompletion:"
- "_generateContextChangedFlags:spl:"
- "_notifyTips:"
- "_notifyTips: context %d\n"
- "_requestSensingPredictionInfo venueRequested %d splRequested %d\n"
- "_requestSensingPredictionInfo:spl:"
- "_setConcertVenueAirPodsInEarTipShown"
- "_setConcertVenueAirPodsNearybyTipShown"
- "_validateDeviceInfo: Device %@ not found in connected devices"
- "com.apple.AudioAccessoryServices.user-reach-loud-environment"
- "initWithContentIdentifier:context:osBuild:userInfo:"
- "locationCategory"
- "noiseLevel"
- "setContextChangeFlags:"
- "setContextSignalUpdatedHandler:"
- "sharedContextManager"
- "v20@?0I8@\"SPContext\"12"

```
