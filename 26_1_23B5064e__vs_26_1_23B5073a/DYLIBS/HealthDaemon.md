## HealthDaemon

> `/System/Library/PrivateFrameworks/HealthDaemon.framework/HealthDaemon`

```diff

-6200.2.12.0.0
-  __TEXT.__text: 0x792128
+6200.2.14.2.5
+  __TEXT.__text: 0x79276c
   __TEXT.__auth_stubs: 0x4820
-  __TEXT.__objc_methlist: 0x43b1c
+  __TEXT.__objc_methlist: 0x43b2c
   __TEXT.__const: 0x1df7c
   __TEXT.__dlopen_cstrs: 0x15b
   __TEXT.__cstring: 0x7d130

   __TEXT.__swift5_proto: 0x100
   __TEXT.__swift5_protos: 0x1c
   __TEXT.__swift5_capture: 0x5c4
-  __TEXT.__oslogstring: 0x41aee
+  __TEXT.__oslogstring: 0x41dab
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_assocty: 0xf0
   __TEXT.__swift_as_entry: 0x48

   __TEXT.__unwind_info: 0x1cd30
   __TEXT.__eh_frame: 0x2310
   __TEXT.__objc_classname: 0xc5c3
-  __TEXT.__objc_methname: 0x8ec70
-  __TEXT.__objc_methtype: 0x16b56
-  __TEXT.__objc_stubs: 0x50560
+  __TEXT.__objc_methname: 0x8ecac
+  __TEXT.__objc_methtype: 0x16b61
+  __TEXT.__objc_stubs: 0x50580
   __DATA_CONST.__got: 0x5668
   __DATA_CONST.__const: 0x1d2a0
   __DATA_CONST.__objc_classlist: 0x29d8
   __DATA_CONST.__objc_catlist: 0x4c0
   __DATA_CONST.__objc_protolist: 0x9b0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x19ef0
+  __DATA_CONST.__objc_selrefs: 0x19ef8
   __DATA_CONST.__objc_protorefs: 0x1d8
   __DATA_CONST.__objc_superrefs: 0x1d88
   __DATA_CONST.__objc_arraydata: 0x84a0
   __AUTH_CONST.__auth_got: 0x2428
   __AUTH_CONST.__const: 0x10018
   __AUTH_CONST.__cfstring: 0x3d5e0
-  __AUTH_CONST.__objc_const: 0x7d948
+  __AUTH_CONST.__objc_const: 0x7d968
   __AUTH_CONST.__objc_arrayobj: 0x1ed8
   __AUTH_CONST.__objc_intobj: 0x3e58
   __AUTH_CONST.__objc_doubleobj: 0x3c0

   __DATA.__data: 0x81c8
   __DATA.__common: 0x64
   __DATA.__bss: 0x18c0
-  __DATA_DIRTY.__objc_ivar: 0xe80
+  __DATA_DIRTY.__objc_ivar: 0xe84
   __DATA_DIRTY.__objc_data: 0xe2e0
   __DATA_DIRTY.__data: 0x210
   __DATA_DIRTY.__bss: 0x3d0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: CE312F8F-AA13-31A6-BA5D-B8B20C7D8607
-  Functions: 34764
-  Symbols:   103903
-  CStrings:  44264
+  UUID: 739AE653-2ED7-3510-BE86-2B554F9AB378
+  Functions: 34766
+  Symbols:   103908
+  CStrings:  44274
 
Symbols:
+ -[HDMirroredWorkoutSessionServer _flushPendingClientUpdates]
+ ___51-[HDMirroredWorkoutSessionServer _flushPendingData]_block_invoke_2
+ ___block_descriptor_64_e8_32s40s48s56bs_e51_v32?0"NSDictionary"8"NSDictionary"16"NSError"24ls32l8s40l8s48l8s56l8
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e28_v24?0"NSData"8"NSError"16ls32l8s40l8s48l8s56l8s64l8
+ _objc_msgSend$_flushPendingClientUpdates
- ___block_descriptor_48_e8_32s40bs_e51_v32?0"NSDictionary"8"NSDictionary"16"NSError"24ls32l8s40l8
- ___block_descriptor_56_e8_32s40s48bs_e28_v24?0"NSData"8"NSError"16ls32l8s40l8s48l8
Functions:
~ -[HDActiveDataAggregator _aggregateForAllDevicesForCollector:date:mode:options:] : 392 -> 444
~ ___80-[HDActiveDataAggregator _aggregateForAllDevicesForCollector:date:mode:options:]_block_invoke : 20 -> 100
~ -[HDMirroredWorkoutSessionServer _executeClientDataUpdate:completion:] : 376 -> 400
~ ___67-[HDMirroredWorkoutSessionServer didDisconnectFromRemoteWithError:]_block_invoke : 308 -> 512
~ -[HDMirroredWorkoutSessionServer _enqueueClientUpdate:launchClient:waitForClientSetup:] : 888 -> 712
+ -[HDMirroredWorkoutSessionServer _flushPendingClientUpdates]
~ -[HDMirroredWorkoutSessionServer _flushPendingData] : 456 -> 592
~ ___51-[HDMirroredWorkoutSessionServer _flushPendingData]_block_invoke : 548 -> 632
+ ___51-[HDMirroredWorkoutSessionServer _flushPendingData]_block_invoke_2
~ -[HDMirroredWorkoutSessionServer runSetupPostClientMirroringStartHandler] : 644 -> 332
~ -[HDRapportMessenger sendRequest:data:completion:] : 780 -> 816
~ ___50-[HDRapportMessenger sendRequest:data:completion:]_block_invoke : 772 -> 984
~ ___61-[HDRapportMessenger _handleIncomingRequest:responseHandler:]_block_invoke : 220 -> 264
~ ___61-[HDRapportMessenger _handleIncomingRequest:responseHandler:]_block_invoke_2 : 384 -> 600
CStrings:
+ "[mirroring] %{public}@: %ld current pending client updates"
+ "[mirroring] %{public}@: Completing %ld data updates from client: %{public}@"
+ "[mirroring] %{public}@: Disconnecting before mirroring start handler called. Flushing all client and pending data updates"
+ "[mirroring] %{public}@: Flushing %ld pending data to client: %{public}@."
+ "[mirroring] %{public}@: Force Flushing of failed pending data updates during teardown for client %{public}@"
+ "[mirroring] %{public}@: Mirroring session not configured, not executing %ld client updates"
+ "[mirroring] %{public}@: Received response for request [%{public}@] %{public}@ (%lu bytes)"
+ "[mirroring] %{public}@: Responding to request [%{public}@] %{public}@ (%lu bytes)"
+ "_flushPendingClientUpdates"
+ "_lock_isTearingDown"
+ "_lock_postMirroringClientStartHandlerCalled"
+ "service:account:inviteDroppedForSessionID:fromID:context:error:"
+ "v64@0:8@\"IDSService\"16@\"IDSAccount\"24@\"NSString\"32@\"NSString\"40@\"NSData\"48@\"NSError\"56"
- "_postMirroringClientStartHandlerCalled"
- "service:account:inviteDroppedForSessionID:fromID:error:"
- "v56@0:8@\"IDSService\"16@\"IDSAccount\"24@\"NSString\"32@\"NSString\"40@\"NSError\"48"

```
