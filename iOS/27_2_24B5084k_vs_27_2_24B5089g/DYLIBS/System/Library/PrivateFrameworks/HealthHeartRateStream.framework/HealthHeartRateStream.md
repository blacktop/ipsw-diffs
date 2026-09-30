## HealthHeartRateStream

> `/System/Library/PrivateFrameworks/HealthHeartRateStream.framework/HealthHeartRateStream`

```diff

-7027.1.36.2.7
-  __TEXT.__text: 0x5aff0
+7027.1.45.2.4
+  __TEXT.__text: 0x5d27c
   __TEXT.__objc_methlist: 0x36c
-  __TEXT.__const: 0x3850
-  __TEXT.__constg_swiftt: 0x19c0
-  __TEXT.__swift5_typeref: 0x1262
-  __TEXT.__swift5_reflstr: 0x150a
-  __TEXT.__swift5_fieldmd: 0x15b0
+  __TEXT.__const: 0x38c0
+  __TEXT.__constg_swiftt: 0x19f4
+  __TEXT.__swift5_typeref: 0x12ca
+  __TEXT.__swift5_reflstr: 0x154a
+  __TEXT.__swift5_fieldmd: 0x1614
   __TEXT.__swift5_builtin: 0x50
-  __TEXT.__oslogstring: 0x2084
-  __TEXT.__swift5_capture: 0x720
-  __TEXT.__cstring: 0xaa2
-  __TEXT.__swift5_proto: 0x1d8
-  __TEXT.__swift5_types: 0x174
+  __TEXT.__oslogstring: 0x2324
+  __TEXT.__swift5_capture: 0x770
+  __TEXT.__cstring: 0xb22
+  __TEXT.__swift5_proto: 0x1e0
+  __TEXT.__swift5_types: 0x178
   __TEXT.__swift5_protos: 0x6c
   __TEXT.__swift5_assocty: 0xc0
   __TEXT.__swift_as_entry: 0x114
   __TEXT.__swift_as_ret: 0x104
   __TEXT.__swift_as_cont: 0x1d8
-  __TEXT.__unwind_info: 0x2258
-  __TEXT.__eh_frame: 0x250c
+  __TEXT.__unwind_info: 0x2280
+  __TEXT.__eh_frame: 0x2644
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2d0
+  __DATA_CONST.__const: 0x2e0
   __DATA_CONST.__objc_classlist: 0x138
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x330
+  __DATA_CONST.__objc_selrefs: 0x338
   __DATA_CONST.__objc_protorefs: 0x48
-  __DATA_CONST.__got: 0x338
-  __AUTH_CONST.__const: 0x3500
+  __DATA_CONST.__got: 0x340
+  __AUTH_CONST.__const: 0x3690
   __AUTH_CONST.__cfstring: 0x20
-  __AUTH_CONST.__objc_const: 0x2648
-  __AUTH_CONST.__auth_got: 0xa68
-  __AUTH.__objc_data: 0x898
-  __AUTH.__data: 0x1c18
-  __DATA.__data: 0x12d8
-  __DATA.__common: 0x50
+  __AUTH_CONST.__objc_const: 0x26a8
+  __AUTH_CONST.__auth_got: 0xa78
+  __AUTH.__objc_data: 0x2b8
+  __AUTH.__data: 0x1188
+  __DATA.__data: 0xee8
+  __DATA.__common: 0x18
+  __DATA_DIRTY.__objc_data: 0x5f0
+  __DATA_DIRTY.__data: 0xee0
+  __DATA_DIRTY.__bss: 0x380
+  __DATA_DIRTY.__common: 0x38
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AudioAccessoryServices.framework/AudioAccessoryServices

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2419
-  Symbols:   882
-  CStrings:  189
+  Functions: 2459
+  Symbols:   891
+  CStrings:  193
 
Symbols:
+ ___swift_closure_destructor.12Tm
+ _associated conformance 21HealthHeartRateStream17MockRapportClientC12RegistrationOSHAASQ
+ _objc_msgSend$setInterruptionHandler:
+ _swift_getFunctionTypeMetadata0
+ _symbolic So11PDRRegistryC
+ _symbolic _____ 21HealthHeartRateStream17MockRapportClientC12RegistrationO
+ _symbolic _____ySaySSGSgG 15Synchronization5MutexVAARi_zrlE
+ _symbolic _____ySay_____GG 15Synchronization5MutexVAARi_zrlE 21HealthHeartRateStream17MockRapportDeviceC
+ _symbolic _____yShy_____GG 15Synchronization5MutexVAARi_zrlE 21HealthHeartRateStream17MockRapportClientC12RegistrationO
+ _symbolic _____ySiG 15Synchronization5MutexVAARi_zrlE
+ _symbolic _____y_____SgG 15Synchronization5MutexVAARi_zrlE So14RPControlFlagsV
+ _symbolic _____yyyYbcSgG 15Synchronization5MutexVAARi_zrlE
+ _symbolic ytIeghr_
- ___swift_assign_boxed_opaque_existential_1
- ___swift_closure_destructor.15Tm
- _symbolic Say_____G 21HealthHeartRateStream17MockRapportDeviceC
- _symbolic _____ySDySS______pGG 15Synchronization5MutexVAARi_zrlE 21HealthHeartRateStream22RapportDeviceInterfaceP
CStrings:
+ "HealthHeartRateStream.RegistryPairedWatchMonitor"
+ "Rapport interrupted; snapshot now"
+ "Rapport snapshot:"
+ "RemoteHeartRateStreamListener with identifier %s received filtered heart rate: { timestamp: %{public}s, bpm: %{private}f, confidence: %{public}s, deviceType: %{public}s }"
+ "RemoteHeartRateStreamListener with identifier %s received unfiltered heart rate: { timestamp: %{public}s, bpm: %{private}f, confidence: %{public}s, deviceType: %{public}s }"
+ "[%{public}s] Received handleFilteredHeartRate { timestamp: %{public}s, bpm: %{private}f, confidence: %{public}s, deviceType: %{public}s }"
+ "[%{public}s] Received handleOneSecondStreamingHeartRate { timestamp: %{public}s, bpm: %{private}f, confidence: %{public}s, deviceType: %{public}s }"
+ "[%{public}s] sessionId %s Received filtered heart rate: { timestamp: %{public}s, bpm: %{private}f, confidence: %{public}s, deviceType: %{public}s }"
+ "[%{public}s] sessionId %s Received request %{public}s with keys: %{public}s."
+ "[%{public}s] sessionId %s Received unfiltered heart rate: { timestamp: %{public}s, bpm: %{private}f, confidence: %{public}s, deviceType: %{public}s }"
+ "[HeartRateDeviceProvider-AirPods] Received device: %{private}s"
+ "[HeartRateDeviceProvider-AudioAccessory] Active HRM device at activation: %{private}s"
+ "[HeartRateDeviceProvider-AudioAccessory] Received device: %{private}s from AASystemStateMonitor - aaActiveHRMDeviceChangedHandler"
+ "[HeartRateDeviceProvider-BLE] HRCBluetoothLESourceObserverDelegate: Device list received. Devices: %{private}s"
+ "[HeartRateDeviceProvider-Discovery] %{public}s %ld watch(es) — %{private}s"
+ "[HeartRateDeviceProvider] %{public}s devices updated: %ld device(s) - %{private}s"
+ "[HeartRateDeviceProvider] Apple Watch change detected, active device: %{private}s"
- "RemoteHeartRateStreamListener with identifier %s received filtered heart rate: %s."
- "RemoteHeartRateStreamListener with identifier %s received unfiltered heart rate: %s."
- "[%{public}s] Received handleFilteredHeartRate %@."
- "[%{public}s] Received handleOneSecondStreamingHeartRate %@."
- "[%{public}s] sessionId %s Received filtered heart rate: %s."
- "[%{public}s] sessionId %s Received request requestDictionary: %s."
- "[%{public}s] sessionId %s Received unfiltered heart rate: %s."
- "[HeartRateDeviceProvider-AirPods] Received device: %s"
- "[HeartRateDeviceProvider-AudioAccessory] Active HRM device at activation: %s"
- "[HeartRateDeviceProvider-AudioAccessory] Received device: %s from AASystemStateMonitor - aaActiveHRMDeviceChangedHandler"
- "[HeartRateDeviceProvider-BLE] HRCBluetoothLESourceObserverDelegate: Device list received. Devices: %s"
- "[HeartRateDeviceProvider] %s devices updated: %ld device(s) - %s"
- "[HeartRateDeviceProvider] Apple Watch change detected, active device: %s"
```
