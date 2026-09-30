## SiriCrossDeviceArbitration

> `/System/Library/PrivateFrameworks/SiriCrossDeviceArbitration.framework/SiriCrossDeviceArbitration`

```diff

-3510.2.1.0.0
-  __TEXT.__text: 0x2fec8
-  __TEXT.__auth_stubs: 0x830
-  __TEXT.__objc_methlist: 0x3154
+3520.57.1.1.1
+  __TEXT.__text: 0x3070c
+  __TEXT.__auth_stubs: 0x7e0
+  __TEXT.__objc_methlist: 0x313c
+  __TEXT.__const: 0x1ec
   __TEXT.__dlopen_cstrs: 0x118
-  __TEXT.__const: 0x1e8
-  __TEXT.__gcc_except_tab: 0x4f0
-  __TEXT.__oslogstring: 0x50ae
-  __TEXT.__cstring: 0x5b1f
-  __TEXT.__unwind_info: 0xd10
+  __TEXT.__gcc_except_tab: 0x4c8
+  __TEXT.__cstring: 0x5b25
+  __TEXT.__oslogstring: 0x5108
+  __TEXT.__unwind_info: 0xd48
   __TEXT.__objc_classname: 0x62b
-  __TEXT.__objc_methname: 0x8064
-  __TEXT.__objc_methtype: 0x1907
-  __TEXT.__objc_stubs: 0x5f20
-  __DATA_CONST.__got: 0x300
-  __DATA_CONST.__const: 0x1108
+  __TEXT.__objc_methname: 0x8074
+  __TEXT.__objc_methtype: 0x18ea
+  __TEXT.__objc_stubs: 0x5ee0
+  __DATA_CONST.__got: 0x308
+  __DATA_CONST.__const: 0x1090
   __DATA_CONST.__objc_classlist: 0x158
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x1e80
   __DATA_CONST.__objc_superrefs: 0x138
   __DATA_CONST.__objc_arraydata: 0xa8
-  __AUTH_CONST.__auth_got: 0x428
-  __AUTH_CONST.__const: 0x340
-  __AUTH_CONST.__cfstring: 0x2b80
+  __AUTH_CONST.__auth_got: 0x400
+  __AUTH_CONST.__const: 0x320
+  __AUTH_CONST.__cfstring: 0x2be0
   __AUTH_CONST.__objc_const: 0x5498
   __AUTH_CONST.__objc_intobj: 0x1e0
-  __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0xd8
+  __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH.__objc_data: 0x230
   __DATA.__objc_ivar: 0x4f8
   __DATA.__data: 0x5d0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
-  - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
-  - /usr/lib/swift/libswiftCoreImage.dylib
-  - /usr/lib/swift/libswiftCoreLocation.dylib
-  - /usr/lib/swift/libswiftCoreMIDI.dylib
-  - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 0061AA18-A0C6-366A-8BBD-70267C377CF2
-  Functions: 1203
-  Symbols:   4255
-  CStrings:  3004
+  UUID: CE4BC890-3F07-371D-B1E5-2CF7A4C26268
+  Functions: 1200
+  Symbols:   4226
+  CStrings:  3006
 
Symbols:
+ -[SCDACoordinator _decideElection]
+ -[SCDACoordinator _deviceShouldContinue]
+ -[SCDACoordinator _didThisDeviceWin]
+ -[SCDADevice overrideDeviceGroup:]
+ -[SCDAMonitor _resultsSeen:]
+ -[SCDAMonitor flushWaitingCompletionsWithDecision:]
+ -[SCDANotifyStatePublisher initWithName:queue:completion:]
+ GCC_except_table1162
+ GCC_except_table1163
+ GCC_except_table1169
+ GCC_except_table231
+ GCC_except_table237
+ GCC_except_table374
+ GCC_except_table389
+ GCC_except_table444
+ GCC_except_table448
+ GCC_except_table475
+ GCC_except_table519
+ GCC_except_table542
+ GCC_except_table563
+ GCC_except_table625
+ GCC_except_table677
+ GCC_except_table680
+ GCC_except_table694
+ GCC_except_table725
+ GCC_except_table827
+ GCC_except_table923
+ _OBJC_CLASS_$_NSSortDescriptor
+ __OBJC_$_INSTANCE_METHODS_SCDADevice
+ ___31-[SCDACoordinator _enterState:]_block_invoke.249
+ ___34-[SCDACoordinator _decideElection]_block_invoke
+ ___36-[SCDACoordinator _advertiseTrigger]_block_invoke.340
+ ___36-[SCDACoordinator _advertiseTrigger]_block_invoke.343
+ ___36-[SCDACoordinator _advertiseTrigger]_block_invoke.344
+ ___40-[SCDACoordinator _deviceShouldContinue]_block_invoke
+ ___42-[SCDACoordinator _waitWiProx:andExecute:]_block_invoke.383
+ ___51-[SCDACoordinator _endAdvertisingAnalyticsContext:]_block_invoke.193
+ ___51-[SCDAMonitor flushWaitingCompletionsWithDecision:]_block_invoke
+ ___52-[SCDACoordinator _createWaitWiProxTimer:waitBlock:]_block_invoke.382
+ ___58-[SCDANotifyStatePublisher initWithName:queue:completion:]_block_invoke
+ ___89-[SCDACoordinator _advertiseWith:afterDelay:maxInterval:voiceTriggerLatency:thenExecute:]_block_invoke.351
+ ___89-[SCDACoordinator _advertiseWith:afterDelay:maxInterval:voiceTriggerLatency:thenExecute:]_block_invoke.360
+ ___Block_byref_object_copy_.1249
+ ___Block_byref_object_copy_.1702
+ ___Block_byref_object_copy_.820
+ ___Block_byref_object_dispose_.1250
+ ___Block_byref_object_dispose_.1703
+ ___Block_byref_object_dispose_.821
+ ___block_descriptor_32_e27_B32?0"SCDARecord"8Q16^B24l
+ ___block_literal_global.1090
+ ___block_literal_global.1126
+ ___block_literal_global.1333
+ ___block_literal_global.1602
+ ___block_literal_global.1732
+ ___block_literal_global.1865
+ ___block_literal_global.238
+ ___block_literal_global.240
+ ___block_literal_global.2775
+ ___block_literal_global.364
+ ___block_literal_global.381
+ ___block_literal_global.467
+ ___block_literal_global.522
+ ___block_literal_global.650
+ ___block_literal_global.818
+ ___block_literal_global.866
+ _objc_autorelease
+ _objc_msgSend$_decideElection
+ _objc_msgSend$_deviceShouldContinue
+ _objc_msgSend$_didThisDeviceWin
+ _objc_msgSend$_resultsSeen:
+ _objc_msgSend$indexOfObjectPassingTest:
+ _objc_msgSend$initWithName:queue:completion:
+ _objc_msgSend$objectAtIndexedSubscript:
+ _objc_msgSend$sortDescriptorWithKey:ascending:
+ _objc_msgSend$sortedArrayUsingDescriptors:
- -[SCDACoordinator _deviceShouldContinue:]
- -[SCDACoordinator _endAdvertisingWithDeviceProhibitions:]
- -[SCDACoordinator _shouldContinueFor:]
- -[SCDADevice(Internal) overrideDeviceGroup:]
- -[SCDAMonitor _resultSeenWithValue:]
- -[SCDANotifyStatePublisher _getState:withToken:]
- -[SCDANotifyStatePublisher _notifyWithState:]
- -[SCDANotifyStatePublisher _setState:withToken:]
- -[SCDANotifyStatePublisher publishStateWithBlock:]
- GCC_except_table1000
- GCC_except_table1023
- GCC_except_table1044
- GCC_except_table1106
- GCC_except_table217
- GCC_except_table223
- GCC_except_table36
- GCC_except_table480
- GCC_except_table533
- GCC_except_table534
- GCC_except_table540
- GCC_except_table57
- GCC_except_table638
- GCC_except_table743
- GCC_except_table746
- GCC_except_table853
- GCC_except_table868
- GCC_except_table925
- GCC_except_table929
- GCC_except_table956
- __OBJC_$_INSTANCE_METHODS_SCDADevice(Internal)
- ___31-[SCDACoordinator _enterState:]_block_invoke.246
- ___34-[SCDACoordinator _sortedReplies:]_block_invoke
- ___34-[SCDACoordinator _sortedReplies:]_block_invoke_2
- ___36-[SCDACoordinator _advertiseTrigger]_block_invoke.338
- ___36-[SCDACoordinator _advertiseTrigger]_block_invoke.341
- ___36-[SCDACoordinator _advertiseTrigger]_block_invoke.342
- ___41-[SCDACoordinator _deviceShouldContinue:]_block_invoke
- ___42-[SCDACoordinator _waitWiProx:andExecute:]_block_invoke.371
- ___47-[SCDANotifyStatePublisher initWithName:queue:]_block_invoke
- ___50-[SCDANotifyStatePublisher publishStateWithBlock:]_block_invoke
- ___51-[SCDACoordinator _endAdvertisingAnalyticsContext:]_block_invoke.190
- ___52-[SCDACoordinator _createWaitWiProxTimer:waitBlock:]_block_invoke.370
- ___57-[SCDACoordinator _endAdvertisingWithDeviceProhibitions:]_block_invoke
- ___89-[SCDACoordinator _advertiseWith:afterDelay:maxInterval:voiceTriggerLatency:thenExecute:]_block_invoke.349
- ___89-[SCDACoordinator _advertiseWith:afterDelay:maxInterval:voiceTriggerLatency:thenExecute:]_block_invoke.358
- ___Block_byref_object_copy_.1114
- ___Block_byref_object_copy_.1684
- ___Block_byref_object_copy_.2347
- ___Block_byref_object_dispose_.1115
- ___Block_byref_object_dispose_.1685
- ___Block_byref_object_dispose_.2348
- ___block_descriptor_32_e11_q24?0816l
- ___block_descriptor_32_e15_v32?08Q16^B24l
- ___block_descriptor_48_e8_32s40s_e27_v32?0"SCDARecord"8Q16^B24ls32l8s40l8
- ___block_literal_global.1068
- ___block_literal_global.1129
- ___block_literal_global.1162
- ___block_literal_global.1187
- ___block_literal_global.1238
- ___block_literal_global.1554
- ___block_literal_global.1762
- ___block_literal_global.2341
- ___block_literal_global.235
- ___block_literal_global.237
- ___block_literal_global.2710
- ___block_literal_global.362
- ___block_literal_global.365
- ___block_literal_global.369
- ___block_literal_global.442
- ___block_literal_global.498
- ___block_literal_global.770
- __swift_FORCE_LOAD_$_swiftAVFoundation
- __swift_FORCE_LOAD_$_swiftAVFoundation_$_SiriCrossDeviceArbitration
- __swift_FORCE_LOAD_$_swiftCoreAudio
- __swift_FORCE_LOAD_$_swiftCoreAudio_$_SiriCrossDeviceArbitration
- __swift_FORCE_LOAD_$_swiftCoreImage
- __swift_FORCE_LOAD_$_swiftCoreImage_$_SiriCrossDeviceArbitration
- __swift_FORCE_LOAD_$_swiftCoreLocation
- __swift_FORCE_LOAD_$_swiftCoreLocation_$_SiriCrossDeviceArbitration
- __swift_FORCE_LOAD_$_swiftCoreMIDI
- __swift_FORCE_LOAD_$_swiftCoreMIDI_$_SiriCrossDeviceArbitration
- __swift_FORCE_LOAD_$_swiftCoreMedia
- __swift_FORCE_LOAD_$_swiftCoreMedia_$_SiriCrossDeviceArbitration
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$_deviceShouldContinue:
- _objc_msgSend$_endAdvertisingWithDeviceProhibitions:
- _objc_msgSend$_getState:withToken:
- _objc_msgSend$_notifyWithState:
- _objc_msgSend$_resultSeenWithValue:
- _objc_msgSend$_setState:withToken:
- _objc_msgSend$_shouldContinueFor:
- _objc_msgSend$addObjectsFromArray:
- _objc_msgSend$isMyriadMetricsMessage:
- _objc_msgSend$sharedInstance
- _objc_msgSend$sortedArrayUsingComparator:
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x6
- _objc_retain_x8
CStrings:
+ "%s Attempting to register an already registered state published. Exiting."
+ "%s Attempting to unregister an already unregistered state published. Exiting."
+ "%s BTLE starting scan and advertisement of payload at time: %lld %@"
+ "%s Not Publishing State, notify token is invalid."
+ "%s This method has been deprecated; ignoring prohibitedDevices."
+ "-[SCDACoordinator _decideElection]"
+ "-[SCDACoordinator _deviceShouldContinue]"
+ "-[SCDACoordinator _deviceShouldContinue]_block_invoke"
+ "-[SCDACoordinator _didThisDeviceWin]"
+ "-[SCDACoordinator endAdvertisingWithDeviceProhibitions:]_block_invoke"
+ "-[SCDAMonitor _resultsSeen:]"
+ "-[SCDANotifyStatePublisher initWithName:queue:completion:]"
+ "-[SCDANotifyStatePublisher publishState:]_block_invoke"
+ "B32@?0@\"SCDARecord\"8Q16^B24"
+ "_decideElection"
+ "_deviceShouldContinue"
+ "_didThisDeviceWin"
+ "_resultsSeen:"
+ "flushWaitingCompletionsWithDecision:"
+ "indexOfObjectPassingTest:"
+ "initWithName:queue:completion:"
+ "objectAtIndexedSubscript:"
+ "sortDescriptorWithKey:ascending:"
+ "sortedArrayUsingDescriptors:"
- "%s BTLE Emergency Call: No device available to handle this call"
- "%s BTLE EmergencyCallSummary %lu: %@"
- "%s BTLE daemon asked to start advertise at: %lld %@"
- "%s BTLE emergencyCallSummary: %@"
- "%s Failed to get state of %s with token %d (status = %u)."
- "-[SCDACoordinator _deviceShouldContinue:]"
- "-[SCDACoordinator _deviceShouldContinue:]_block_invoke"
- "-[SCDACoordinator _endAdvertisingWithDeviceProhibitions:]"
- "-[SCDACoordinator _shouldContinueFor:]"
- "-[SCDACoordinator _shouldHandleEmergency]_block_invoke"
- "-[SCDAMonitor _resultSeenWithValue:]"
- "-[SCDANotifyStatePublisher _getState:withToken:]"
- "-[SCDANotifyStatePublisher _setState:withToken:]"
- "-[SCDANotifyStatePublisher initWithName:queue:]"
- "B28@0:8Q16i24"
- "B28@0:8^Q16i24"
- "_deviceShouldContinue:"
- "_endAdvertisingWithDeviceProhibitions:"
- "_getState:withToken:"
- "_notifyWithState:"
- "_resultSeenWithValue:"
- "_setState:withToken:"
- "_shouldContinueFor:"
- "addObjectsFromArray:"
- "publishStateWithBlock:"
- "q24@?0@8@16"
- "sortedArrayUsingComparator:"
- "v32@?0@8Q16^B24"

```
