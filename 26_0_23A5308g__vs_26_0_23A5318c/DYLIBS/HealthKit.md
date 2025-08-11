## HealthKit

> `/System/Library/Frameworks/HealthKit.framework/HealthKit`

```diff

-6105.0.0.0.0
-  __TEXT.__text: 0x332420
+6106.1.2.5.0
+  __TEXT.__text: 0x3327b4
   __TEXT.__auth_stubs: 0x36d0
-  __TEXT.__objc_methlist: 0x2f8d4
+  __TEXT.__objc_methlist: 0x2f8f4
   __TEXT.__cstring: 0x34c03
   __TEXT.__const: 0xabfa2
-  __TEXT.__oslogstring: 0xc203
+  __TEXT.__oslogstring: 0xc263
   __TEXT.__gcc_except_tab: 0x4064
   __TEXT.__ustring: 0x78
   __TEXT.__dlopen_cstrs: 0x5da

   __TEXT.__swift_as_ret: 0x14c
   __TEXT.__swift5_protos: 0x4c
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__unwind_info: 0xf8a0
+  __TEXT.__unwind_info: 0xf8b0
   __TEXT.__eh_frame: 0x3fe8
   __TEXT.__objc_classname: 0x8971
-  __TEXT.__objc_methname: 0x5d599
+  __TEXT.__objc_methname: 0x5d60f
   __TEXT.__objc_methtype: 0xbf29
-  __TEXT.__objc_stubs: 0x2b200
+  __TEXT.__objc_stubs: 0x2b240
   __DATA_CONST.__got: 0x1b08
   __DATA_CONST.__const: 0xf460
   __DATA_CONST.__objc_classlist: 0x1aa8
   __DATA_CONST.__objc_catlist: 0x1c0
   __DATA_CONST.__objc_protolist: 0x7f0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x11330
+  __DATA_CONST.__objc_selrefs: 0x11340
   __DATA_CONST.__objc_protorefs: 0x608
   __DATA_CONST.__objc_superrefs: 0x1728
   __DATA_CONST.__objc_arraydata: 0x68e8
   __AUTH_CONST.__auth_got: 0x1b80
-  __AUTH_CONST.__const: 0xbfb8
+  __AUTH_CONST.__const: 0xbff8
   __AUTH_CONST.__cfstring: 0x32080
-  __AUTH_CONST.__objc_const: 0x4fc48
+  __AUTH_CONST.__objc_const: 0x4fc50
   __AUTH_CONST.__objc_intobj: 0x4590
   __AUTH_CONST.__objc_dictobj: 0x488
   __AUTH_CONST.__objc_doubleobj: 0x140

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 2CBA4922-3CDF-3A2B-9478-FECE6B5E8876
-  Functions: 23885
-  Symbols:   60630
-  CStrings:  29739
+  UUID: 7F0CD6A3-FA24-3D9D-8C1E-333C4267A721
+  Functions: 23891
+  Symbols:   60650
+  CStrings:  29742
 
Symbols:
+ -[HKWorkoutSession _runSetupPostClientMirroringStartHandlerWithCompletion:]
+ ___33-[HKHealthStore dropEntitlement:]_block_invoke.635
+ ___36-[HKHealthStore restoreEntitlement:]_block_invoke.636
+ ___41-[HKWorkoutSession connectionInterrupted]_block_invoke.226
+ ___41-[HKWorkoutSession connectionInterrupted]_block_invoke.226.cold.1
+ ___41-[HKWorkoutSession connectionInterrupted]_block_invoke.230
+ ___41-[HKWorkoutSession connectionInterrupted]_block_invoke.232.cold.1
+ ___41-[HKWorkoutSession connectionInterrupted]_block_invoke.233
+ ___45-[HKWorkoutSession client_didGenerateEvents:]_block_invoke.239
+ ___45-[HKWorkoutSession endCurrentActivityOnDate:]_block_invoke.290
+ ___45-[HKWorkoutSession endCurrentActivityOnDate:]_block_invoke.290.cold.1
+ ___47-[HKHealthStoreImplementation dropEntitlement:]_block_invoke.654
+ ___49-[HKWorkoutSession client_didChangeToState:date:]_block_invoke.236
+ ___50-[HKHealthStoreImplementation restoreEntitlement:]_block_invoke.655
+ ___65-[HKWorkoutSession stopMirroringToCompanionDeviceWithCompletion:]_block_invoke.302
+ ___65-[HKWorkoutSession stopMirroringToCompanionDeviceWithCompletion:]_block_invoke.302.cold.1
+ ___66-[HKWorkoutSession startMirroringToCompanionDeviceWithCompletion:]_block_invoke.301
+ ___66-[HKWorkoutSession startMirroringToCompanionDeviceWithCompletion:]_block_invoke.301.cold.1
+ ___68-[HKWorkoutSession beginNewActivityWithConfiguration:date:metadata:]_block_invoke.289
+ ___68-[HKWorkoutSession beginNewActivityWithConfiguration:date:metadata:]_block_invoke.289.cold.1
+ ___70-[HKHealthStore clientRemote_didCreateRemoteSessionWithConfiguration:]_block_invoke_2
+ ___70-[HKHealthStore clientRemote_didCreateRemoteSessionWithConfiguration:]_block_invoke_2.cold.1
+ ___70-[HKWorkoutSession _queue_sendPendingDataUpdateToRemoteWorkoutSession]_block_invoke.307
+ ___70-[HKWorkoutSession _queue_sendPendingDataUpdateToRemoteWorkoutSession]_block_invoke.307.cold.1
+ ___70-[HKWorkoutSession enableAutomaticDetectionForActivityConfigurations:]_block_invoke.285
+ ___70-[HKWorkoutSession enableAutomaticDetectionForActivityConfigurations:]_block_invoke.288
+ ___70-[HKWorkoutSession enableAutomaticDetectionForActivityConfigurations:]_block_invoke.288.cold.1
+ ___70-[HKWorkoutSession enableAutomaticDetectionForActivityConfigurations:]_block_invoke_2.287
+ ___71-[HKWorkoutSession client_didDisconnectFromRemoteWithError:completion:]_block_invoke.262
+ ___75-[HKWorkoutSession _runSetupPostClientMirroringStartHandlerWithCompletion:]_block_invoke
+ ___75-[HKWorkoutSession _runSetupPostClientMirroringStartHandlerWithCompletion:]_block_invoke_2
+ ___75-[HKWorkoutSession _runSetupPostClientMirroringStartHandlerWithCompletion:]_block_invoke_2.cold.1
+ ___76-[HKWorkoutSession stateMachine:didTransition:fromState:toState:date:error:]_block_invoke.275
+ ___76-[HKWorkoutSession stateMachine:didTransition:fromState:toState:date:error:]_block_invoke.275.cold.1
+ ___77-[HKWorkoutSession client_didReceiveDataFromRemoteWorkoutSession:completion:]_block_invoke.251
+ ___84-[HKHealthStoreImplementation clientRemote_didCreateRemoteSessionWithConfiguration:]_block_invoke_2
+ ___84-[HKHealthStoreImplementation clientRemote_didCreateRemoteSessionWithConfiguration:]_block_invoke_2.cold.1
+ ___block_literal_global.235
+ ___block_literal_global.265
+ ___block_literal_global.284
+ ___block_literal_global.631
+ ___block_literal_global.650
+ _objc_msgSend$_runSetupPostClientMirroringStartHandlerWithCompletion:
+ _objc_msgSend$remote_runSetupPostClientMirroringStartHandlerWithCompletion:
- ___33-[HKHealthStore dropEntitlement:]_block_invoke.633
- ___36-[HKHealthStore restoreEntitlement:]_block_invoke.634
- ___41-[HKWorkoutSession connectionInterrupted]_block_invoke.225
- ___41-[HKWorkoutSession connectionInterrupted]_block_invoke.225.cold.1
- ___41-[HKWorkoutSession connectionInterrupted]_block_invoke.229
- ___41-[HKWorkoutSession connectionInterrupted]_block_invoke.231
- ___41-[HKWorkoutSession connectionInterrupted]_block_invoke.231.cold.1
- ___45-[HKWorkoutSession client_didGenerateEvents:]_block_invoke.238
- ___45-[HKWorkoutSession endCurrentActivityOnDate:]_block_invoke.289
- ___45-[HKWorkoutSession endCurrentActivityOnDate:]_block_invoke.289.cold.1
- ___47-[HKHealthStoreImplementation dropEntitlement:]_block_invoke.652
- ___49-[HKWorkoutSession client_didChangeToState:date:]_block_invoke.235
- ___50-[HKHealthStoreImplementation restoreEntitlement:]_block_invoke.653
- ___65-[HKWorkoutSession stopMirroringToCompanionDeviceWithCompletion:]_block_invoke.301
- ___65-[HKWorkoutSession stopMirroringToCompanionDeviceWithCompletion:]_block_invoke.301.cold.1
- ___66-[HKWorkoutSession startMirroringToCompanionDeviceWithCompletion:]_block_invoke.300
- ___66-[HKWorkoutSession startMirroringToCompanionDeviceWithCompletion:]_block_invoke.300.cold.1
- ___68-[HKWorkoutSession beginNewActivityWithConfiguration:date:metadata:]_block_invoke.288
- ___68-[HKWorkoutSession beginNewActivityWithConfiguration:date:metadata:]_block_invoke.288.cold.1
- ___70-[HKWorkoutSession _queue_sendPendingDataUpdateToRemoteWorkoutSession]_block_invoke.306
- ___70-[HKWorkoutSession _queue_sendPendingDataUpdateToRemoteWorkoutSession]_block_invoke.306.cold.1
- ___70-[HKWorkoutSession enableAutomaticDetectionForActivityConfigurations:]_block_invoke.284
- ___70-[HKWorkoutSession enableAutomaticDetectionForActivityConfigurations:]_block_invoke.287
- ___70-[HKWorkoutSession enableAutomaticDetectionForActivityConfigurations:]_block_invoke.287.cold.1
- ___70-[HKWorkoutSession enableAutomaticDetectionForActivityConfigurations:]_block_invoke_2.286
- ___71-[HKWorkoutSession client_didDisconnectFromRemoteWithError:completion:]_block_invoke.261
- ___76-[HKWorkoutSession stateMachine:didTransition:fromState:toState:date:error:]_block_invoke.274
- ___76-[HKWorkoutSession stateMachine:didTransition:fromState:toState:date:error:]_block_invoke.274.cold.1
- ___77-[HKWorkoutSession client_didReceiveDataFromRemoteWorkoutSession:completion:]_block_invoke.250
- ___block_literal_global.264
- ___block_literal_global.283
CStrings:
+ "[mirroring] Post mirroring start handler completed with success %{public}@ and error %{public}@"
+ "_runSetupPostClientMirroringStartHandlerWithCompletion:"
+ "remote_runSetupPostClientMirroringStartHandlerWithCompletion:"

```
