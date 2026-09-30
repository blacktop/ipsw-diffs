## AttentionAwareness

> `/System/Library/PrivateFrameworks/AttentionAwareness.framework/AttentionAwareness`

```diff

-240.40.1.0.0
-  __TEXT.__text: 0x37a8c
-  __TEXT.__auth_stubs: 0x9c0
-  __TEXT.__objc_methlist: 0x2744
+242.100.2.0.0
+  __TEXT.__text: 0x39558
+  __TEXT.__auth_stubs: 0x960
+  __TEXT.__objc_methlist: 0x274c
   __TEXT.__const: 0x160
-  __TEXT.__gcc_except_tab: 0x820
-  __TEXT.__oslogstring: 0x5569
-  __TEXT.__cstring: 0x3989
-  __TEXT.__unwind_info: 0xc80
+  __TEXT.__gcc_except_tab: 0x844
+  __TEXT.__oslogstring: 0x5646
+  __TEXT.__cstring: 0x3f8a
+  __TEXT.__unwind_info: 0xcb0
   __TEXT.__objc_classname: 0x5dc
-  __TEXT.__objc_methname: 0x5248
-  __TEXT.__objc_methtype: 0x1902
-  __TEXT.__objc_stubs: 0x4320
+  __TEXT.__objc_methname: 0x52c0
+  __TEXT.__objc_methtype: 0x191a
+  __TEXT.__objc_stubs: 0x43e0
   __DATA_CONST.__got: 0x210
-  __DATA_CONST.__const: 0xe20
+  __DATA_CONST.__const: 0xe70
   __DATA_CONST.__objc_classlist: 0x118
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xe8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1428
+  __DATA_CONST.__objc_selrefs: 0x1460
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x108
   __DATA_CONST.__objc_arraydata: 0x40
-  __AUTH_CONST.__auth_got: 0x4f8
+  __AUTH_CONST.__auth_got: 0x4c8
   __AUTH_CONST.__const: 0x3c8
-  __AUTH_CONST.__cfstring: 0x1ce0
-  __AUTH_CONST.__objc_const: 0x5088
+  __AUTH_CONST.__cfstring: 0x1d00
+  __AUTH_CONST.__objc_const: 0x50d0
   __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x2d0
-  __DATA.__objc_ivar: 0x544
+  __DATA.__objc_ivar: 0x54c
   __DATA.__data: 0xae0
-  __DATA.__bss: 0x48
+  __DATA.__bss: 0x58
   __DATA_DIRTY.__objc_data: 0x820
   __DATA_DIRTY.__data: 0x4
-  __DATA_DIRTY.__bss: 0x148
+  __DATA_DIRTY.__bss: 0x138
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices
   - /System/Library/PrivateFrameworks/BacklightServices.framework/BacklightServices
+  - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary
+  - /System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams
   - /System/Library/PrivateFrameworks/BiometricKit.framework/BiometricKit
-  - /System/Library/PrivateFrameworks/CarKit.framework/CarKit
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/PowerLog.framework/PowerLog
   - /usr/lib/libAccessibility.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 62967B5F-985F-3639-973D-2A543366933E
+  UUID: AB4FB177-3797-3077-AD3B-DD273AFB2FF0
   Functions: 954
-  Symbols:   3640
-  CStrings:  2336
+  Symbols:   3644
+  CStrings:  2361
 
Symbols:
+ -[BiokitOperation operation:captureInterrupted:]
+ -[CarPlayStateObserver setupBiomeStream]
+ GCC_except_table163
+ GCC_except_table167
+ GCC_except_table182
+ GCC_except_table201
+ GCC_except_table203
+ GCC_except_table227
+ GCC_except_table231
+ GCC_except_table263
+ GCC_except_table287
+ GCC_except_table344
+ GCC_except_table356
+ GCC_except_table375
+ _BiomeLibrary
+ _OBJC_CLASS_$_BMBiomeScheduler
+ _OBJC_IVAR_$_CarPlayStateObserver._scheduler
+ _OBJC_IVAR_$_CarPlayStateObserver._sink
+ _OBJC_IVAR_$_CarPlayStateObserver._stream
+ ___40-[CarPlayStateObserver setupBiomeStream]_block_invoke
+ ___40-[CarPlayStateObserver setupBiomeStream]_block_invoke.27
+ ___Block_byref_object_copy_.1041
+ ___Block_byref_object_copy_.1141
+ ___Block_byref_object_copy_.1652
+ ___Block_byref_object_copy_.2076
+ ___Block_byref_object_copy_.2338
+ ___Block_byref_object_copy_.590
+ ___Block_byref_object_copy_.723
+ ___Block_byref_object_dispose_.1042
+ ___Block_byref_object_dispose_.1142
+ ___Block_byref_object_dispose_.1653
+ ___Block_byref_object_dispose_.2077
+ ___Block_byref_object_dispose_.2339
+ ___Block_byref_object_dispose_.591
+ ___Block_byref_object_dispose_.724
+ ___block_descriptor_40_e8_32s_e22_v16?0"BMStoreEvent"8ls32l8
+ ___block_descriptor_40_e8_32s_e23_v16?0"BPSCompletion"8ls32l8
+ ___block_literal_global.1080
+ ___block_literal_global.1164
+ ___block_literal_global.1590
+ ___block_literal_global.1668
+ ___block_literal_global.2096
+ ___block_literal_global.220
+ ___block_literal_global.2370
+ ___block_literal_global.2739
+ ___block_literal_global.457
+ ___block_literal_global.721
+ ___block_literal_global.877
+ _objc_msgSend$CarPlay
+ _objc_msgSend$Connected
+ _objc_msgSend$DSLPublisher
+ _objc_msgSend$eventBody
+ _objc_msgSend$initWithIdentifier:targetQueue:
+ _objc_msgSend$setupBiomeStream
+ _objc_msgSend$sinkWithCompletion:receiveInput:
+ _objc_msgSend$starting
+ _objc_msgSend$subscribeOn:
+ _sharedManager.manager.1165
+ _sharedManager.onceToken.1163
- -[CarPlayStateObserver getCarPlayState]
- -[CarPlayStateObserver sessionDidConnect:]
- -[CarPlayStateObserver sessionDidDisconnect:]
- GCC_except_table161
- GCC_except_table166
- GCC_except_table181
- GCC_except_table200
- GCC_except_table202
- GCC_except_table226
- GCC_except_table230
- GCC_except_table262
- GCC_except_table286
- GCC_except_table343
- GCC_except_table355
- GCC_except_table374
- _OBJC_CLASS_$_CARSessionStatus
- _OBJC_IVAR_$_CarPlayStateObserver._carSessionStatus
- ___39-[CarPlayStateObserver getCarPlayState]_block_invoke
- ___Block_byref_object_copy_.1031
- ___Block_byref_object_copy_.1130
- ___Block_byref_object_copy_.1630
- ___Block_byref_object_copy_.2045
- ___Block_byref_object_copy_.2313
- ___Block_byref_object_copy_.585
- ___Block_byref_object_copy_.716
- ___Block_byref_object_dispose_.1032
- ___Block_byref_object_dispose_.1131
- ___Block_byref_object_dispose_.1631
- ___Block_byref_object_dispose_.2046
- ___Block_byref_object_dispose_.2314
- ___Block_byref_object_dispose_.586
- ___Block_byref_object_dispose_.717
- ___block_literal_global.1069
- ___block_literal_global.1153
- ___block_literal_global.1568
- ___block_literal_global.1646
- ___block_literal_global.2065
- ___block_literal_global.221
- ___block_literal_global.2345
- ___block_literal_global.2714
- ___block_literal_global.454
- ___block_literal_global.714
- ___block_literal_global.869
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$addSessionObserver:
- _objc_msgSend$currentSession
- _objc_msgSend$getCarPlayState
- _objc_opt_new
- _objc_release_x2
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x4
- _objc_retain_x6
- _objc_retain_x8
- _sharedManager.manager.1154
- _sharedManager.onceToken.1152
CStrings:
+ "%13.5f: Capture %s"
+ "%13.5f: Device %s CarPlay"
+ "%13.5f: Received completion event from Biome: %@"
+ "%30s:%-4d: %13.5f: Capture %s"
+ "%30s:%-4d: %13.5f: Device %s CarPlay"
+ "%30s:%-4d: %13.5f: Received completion event from Biome: %@"
+ "/Library/Caches/com.apple.xbs/4343D605-E015-4B28-B167-E89DA650176A/TemporaryDirectory.kYl32a/Sources/AttentionAwareness/Framework/Client/ClientHelpers.m"
+ "/Library/Caches/com.apple.xbs/4343D605-E015-4B28-B167-E89DA650176A/TemporaryDirectory.kYl32a/Sources/AttentionAwareness/Framework/Client/FrameworkClient.m"
+ "/Library/Caches/com.apple.xbs/4343D605-E015-4B28-B167-E89DA650176A/TemporaryDirectory.kYl32a/Sources/AttentionAwareness/Framework/Client/SimpleFrameworkTypes.m"
+ "/Library/Caches/com.apple.xbs/4343D605-E015-4B28-B167-E89DA650176A/TemporaryDirectory.kYl32a/Sources/AttentionAwareness/Framework/EventFilter/EventFilter.mm"
+ "/Library/Caches/com.apple.xbs/4343D605-E015-4B28-B167-E89DA650176A/TemporaryDirectory.kYl32a/Sources/AttentionAwareness/Framework/Shared/Utils.m"
+ "/Library/Caches/com.apple.xbs/4343D605-E015-4B28-B167-E89DA650176A/TemporaryDirectory.kYl32a/Sources/AttentionAwareness/Framework/XPCService/AVFoundationEngine/AVFoundationEngine.m"
+ "/Library/Caches/com.apple.xbs/4343D605-E015-4B28-B167-E89DA650176A/TemporaryDirectory.kYl32a/Sources/AttentionAwareness/Framework/XPCService/AVFoundationEngine/AVFoundationHelper.m"
+ "/Library/Caches/com.apple.xbs/4343D605-E015-4B28-B167-E89DA650176A/TemporaryDirectory.kYl32a/Sources/AttentionAwareness/Framework/XPCService/CoreService/AttentionAwareService.m"
+ "/Library/Caches/com.apple.xbs/4343D605-E015-4B28-B167-E89DA650176A/TemporaryDirectory.kYl32a/Sources/AttentionAwareness/Framework/XPCService/CoreService/EventStatistics.m"
+ "/Library/Caches/com.apple.xbs/4343D605-E015-4B28-B167-E89DA650176A/TemporaryDirectory.kYl32a/Sources/AttentionAwareness/Framework/XPCService/CoreService/PersistentDataManager.m"
+ "/Library/Caches/com.apple.xbs/4343D605-E015-4B28-B167-E89DA650176A/TemporaryDirectory.kYl32a/Sources/AttentionAwareness/Framework/XPCService/CoreService/RemoteClient.m"
+ "/Library/Caches/com.apple.xbs/4343D605-E015-4B28-B167-E89DA650176A/TemporaryDirectory.kYl32a/Sources/AttentionAwareness/Framework/XPCService/CoreService/SampleLogger.m"
+ "/Library/Caches/com.apple.xbs/4343D605-E015-4B28-B167-E89DA650176A/TemporaryDirectory.kYl32a/Sources/AttentionAwareness/Framework/XPCService/CoreService/Scheduler.m"
+ "/Library/Caches/com.apple.xbs/4343D605-E015-4B28-B167-E89DA650176A/TemporaryDirectory.kYl32a/Sources/AttentionAwareness/Framework/XPCService/Device States/CarPlayStateObserver.m"
+ "/Library/Caches/com.apple.xbs/4343D605-E015-4B28-B167-E89DA650176A/TemporaryDirectory.kYl32a/Sources/AttentionAwareness/Framework/XPCService/Sampling/PearlAVFoundationInterface.m"
+ "/Library/Caches/com.apple.xbs/4343D605-E015-4B28-B167-E89DA650176A/TemporaryDirectory.kYl32a/Sources/AttentionAwareness/Framework/XPCService/Sampling/PearlAttentionSampler.m"
+ "/Library/Caches/com.apple.xbs/4343D605-E015-4B28-B167-E89DA650176A/TemporaryDirectory.kYl32a/Sources/AttentionAwareness/Framework/XPCService/Sampling/PearlBioKitInterface.m"
+ "/Library/Caches/com.apple.xbs/4343D605-E015-4B28-B167-E89DA650176A/TemporaryDirectory.kYl32a/Sources/AttentionAwareness/Framework/XPCService/Streaming/AVFoundationAttentionStreamer.m"
+ "/Library/Caches/com.apple.xbs/4343D605-E015-4B28-B167-E89DA650176A/TemporaryDirectory.kYl32a/Sources/AttentionAwareness/Framework/XPCService/Streaming/PearlAttentionStreamer.m"
+ "/Library/Caches/com.apple.xbs/4343D605-E015-4B28-B167-E89DA650176A/TemporaryDirectory.kYl32a/Sources/AttentionAwareness/Framework/XPCService/Unit Testing/PearlUnitTestSupport.m"
+ "@\"BMBiomeScheduler\""
+ "@\"BMStream\""
+ "@\"BPSSink\""
+ "CONNECTED TO"
+ "CarPlay"
+ "Connected"
+ "DISCONNECTED FROM"
+ "DSLPublisher"
+ "INTERRUPTION ENDED"
+ "WAS INTERRUPTED"
+ "_sink"
+ "_stream"
+ "com.apple.AttentionAwareness.CarPlaySubscription"
+ "eventBody"
+ "initWithIdentifier:targetQueue:"
+ "operation:captureInterrupted:"
+ "setupBiomeStream"
+ "sinkWithCompletion:receiveInput:"
+ "starting"
+ "subscribeOn:"
+ "v16@?0@\"BMStoreEvent\"8"
+ "v16@?0@\"BPSCompletion\"8"
+ "v36@0:8i16^(?={AWFaceDetectMetadata=BdddQdQQ[16f]QfQ{CGRect={CGPoint=dd}{CGSize=dd}}}iiiB)20@28"
- "/Library/Caches/com.apple.xbs/Sources/AttentionAwareness/Framework/Client/ClientHelpers.m"
- "/Library/Caches/com.apple.xbs/Sources/AttentionAwareness/Framework/Client/FrameworkClient.m"
- "/Library/Caches/com.apple.xbs/Sources/AttentionAwareness/Framework/Client/SimpleFrameworkTypes.m"
- "/Library/Caches/com.apple.xbs/Sources/AttentionAwareness/Framework/EventFilter/EventFilter.mm"
- "/Library/Caches/com.apple.xbs/Sources/AttentionAwareness/Framework/Shared/Utils.m"
- "/Library/Caches/com.apple.xbs/Sources/AttentionAwareness/Framework/XPCService/AVFoundationEngine/AVFoundationEngine.m"
- "/Library/Caches/com.apple.xbs/Sources/AttentionAwareness/Framework/XPCService/AVFoundationEngine/AVFoundationHelper.m"
- "/Library/Caches/com.apple.xbs/Sources/AttentionAwareness/Framework/XPCService/CoreService/AttentionAwareService.m"
- "/Library/Caches/com.apple.xbs/Sources/AttentionAwareness/Framework/XPCService/CoreService/EventStatistics.m"
- "/Library/Caches/com.apple.xbs/Sources/AttentionAwareness/Framework/XPCService/CoreService/PersistentDataManager.m"
- "/Library/Caches/com.apple.xbs/Sources/AttentionAwareness/Framework/XPCService/CoreService/RemoteClient.m"
- "/Library/Caches/com.apple.xbs/Sources/AttentionAwareness/Framework/XPCService/CoreService/SampleLogger.m"
- "/Library/Caches/com.apple.xbs/Sources/AttentionAwareness/Framework/XPCService/CoreService/Scheduler.m"
- "/Library/Caches/com.apple.xbs/Sources/AttentionAwareness/Framework/XPCService/Sampling/PearlAVFoundationInterface.m"
- "/Library/Caches/com.apple.xbs/Sources/AttentionAwareness/Framework/XPCService/Sampling/PearlAttentionSampler.m"
- "/Library/Caches/com.apple.xbs/Sources/AttentionAwareness/Framework/XPCService/Sampling/PearlBioKitInterface.m"
- "/Library/Caches/com.apple.xbs/Sources/AttentionAwareness/Framework/XPCService/Streaming/AVFoundationAttentionStreamer.m"
- "/Library/Caches/com.apple.xbs/Sources/AttentionAwareness/Framework/XPCService/Streaming/PearlAttentionStreamer.m"
- "/Library/Caches/com.apple.xbs/Sources/AttentionAwareness/Framework/XPCService/Unit Testing/PearlUnitTestSupport.m"
- "@\"CARSessionStatus\""
- "_carSessionStatus"
- "addSessionObserver:"
- "currentSession"
- "getCarPlayState"
- "v36@0:8i16^(?={AWFaceDetectMetadata=BdddQdQQ[16f]QfQ{CGRect={CGPoint=dd}{CGSize=dd}}}iii)20@28"

```
