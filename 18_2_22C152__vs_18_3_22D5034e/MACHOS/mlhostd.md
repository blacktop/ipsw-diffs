## mlhostd

> `/usr/libexec/mlhostd`

```diff

-3.4.11.0.0
-  __TEXT.__text: 0x45404
-  __TEXT.__auth_stubs: 0x19f0
+3.5.6.0.0
+  __TEXT.__text: 0x48840
+  __TEXT.__auth_stubs: 0x1a20
   __TEXT.__objc_methlist: 0x38
-  __TEXT.__const: 0xa74
-  __TEXT.__cstring: 0x97db
+  __TEXT.__const: 0xbcc
+  __TEXT.__cstring: 0x984b
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0x2f0
-  __TEXT.__swift5_typeref: 0x6d1
+  __TEXT.__constg_swiftt: 0x30c
+  __TEXT.__swift5_typeref: 0x7db
   __TEXT.__swift5_builtin: 0x64
-  __TEXT.__swift5_reflstr: 0x2d5
-  __TEXT.__swift5_fieldmd: 0x29c
-  __TEXT.__swift5_assocty: 0xd8
-  __TEXT.__swift5_proto: 0x74
-  __TEXT.__swift5_types: 0x38
-  __TEXT.__objc_methname: 0xb7f
-  __TEXT.__oslogstring: 0x22da
-  __TEXT.__objc_classname: 0x1f
-  __TEXT.__objc_methtype: 0x342
-  __TEXT.__swift5_capture: 0x13c
-  __TEXT.__unwind_info: 0x678
-  __TEXT.__eh_frame: 0xb50
-  __DATA_CONST.__auth_got: 0xcf8
-  __DATA_CONST.__got: 0x4a8
-  __DATA_CONST.__auth_ptr: 0x420
-  __DATA_CONST.__const: 0x4dd0
+  __TEXT.__swift5_reflstr: 0x2f2
+  __TEXT.__swift5_fieldmd: 0x2c4
+  __TEXT.__swift5_assocty: 0x108
+  __TEXT.__swift5_proto: 0x8c
+  __TEXT.__swift5_types: 0x3c
+  __TEXT.__objc_methname: 0xc7a
+  __TEXT.__objc_classname: 0x2b
+  __TEXT.__objc_methtype: 0x394
+  __TEXT.__oslogstring: 0x237a
+  __TEXT.__swift5_capture: 0x15c
+  __TEXT.__unwind_info: 0x700
+  __TEXT.__eh_frame: 0xbf0
+  __DATA_CONST.__auth_got: 0xd10
+  __DATA_CONST.__got: 0x4b0
+  __DATA_CONST.__auth_ptr: 0x450
+  __DATA_CONST.__const: 0x4fa8
   __DATA_CONST.__objc_classlist: 0x28
-  __DATA_CONST.__objc_protolist: 0x28
+  __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x18
-  __DATA.__objc_const: 0xae8
-  __DATA.__objc_selrefs: 0x308
+  __DATA_CONST.__objc_protorefs: 0x20
+  __DATA.__objc_const: 0xc10
+  __DATA.__objc_selrefs: 0x340
   __DATA.__objc_data: 0x170
-  __DATA.__data: 0x9f0
-  __DATA.__bss: 0xe80
+  __DATA.__data: 0xab8
+  __DATA.__bss: 0x1180
   __DATA.__common: 0x20
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/ApplePushService.framework/ApplePushService
   - /System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks
   - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary
+  - /System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/LighthouseBackground.framework/LighthouseBackground
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 522
-  Symbols:   687
-  CStrings:  1550
+  Functions: 569
+  Symbols:   695
+  CStrings:  1579
 
Symbols:
+ _$s20LighthouseBackground10TaskStatusO8rawValueACSgSS_tcfC
+ _$s8AllCasess12CaseIterablePTl
+ _$sSYsSERzSS8RawValueSYRtzrlE6encode2toys7Encoder_p_tKF
+ _$sSYsSeRzSS8RawValueSYRtzrlE4fromxs7Decoder_p_tKcfC
+ _$ss12CaseIterableMp
+ _$ss12CaseIterableP8AllCasesAB_SlTn
+ _$ss12CaseIterableP8allCases03AllD0QzvgZTq
+ _$ss21_findStringSwitchCase5cases6stringSiSays06StaticB0VG_SStF
+ _OBJC_CLASS_$_BMPublisherOptions
+ _swift_getObjCClassFromMetadata
- _$sSo13os_log_type_ta0A0E7defaultABvgZ
- _$ss11_SetStorageC8allocate8capacityAByxGSi_tFZ
CStrings:
+ ", groupedChannelsByTopic: "
+ "@\"NSData\"16@0:8"
+ "@\"NSDictionary\"16@0:8"
+ "@28@0:8@\"NSData\"16I24"
+ "@28@0:8@16I24"
+ "BMStoreData"
+ "Creating NSXPCInterface for extension: %s"
+ "Creating XPCConnection for extension: %s"
+ "Currently subscribed to channels: %s for topic: %s and group: %s."
+ "I16@0:8"
+ "Invalid event: %@"
+ "Invalid taskState for message: %@"
+ "No channel options are provided for topic %s. Failed to register new random channel."
+ "SkFOMjZAcld6aC1KVk9xZQ=="
+ "Subscribed to random channel: %s for topic: %s and group: %s."
+ "Subscribing to a random channel on topic %s and group: %s"
+ "Subscribing to all topics and groups with a random channel."
+ "TI,?,R,N"
+ "TI,R,N"
+ "Task %s not found in taskStatusMap"
+ "Task %s was deferred while acquiring process. Exiting early."
+ "Task %s was deferred while opening XPC connection to process. Exiting early."
+ "There are no channels for topic: %s"
+ "There is already one valid channel subscription for topic: %s and group: %s. Skipping new subscription."
+ "Unsubscribing from existing channels: %s for topic: %s and group: %s."
+ "dataVersion"
+ "eventBody"
+ "eventWithData:dataVersion:"
+ "groupedChannelsByTopic"
+ "initWithStartDate:endDate:maxEvents:lastN:reversed:"
+ "json"
+ "jsonDict"
+ "latestDataVersion"
+ "mlhost"
+ "pfl"
+ "publisherWithUseCase:options:"
+ "serialize"
+ "sinkWithCompletion:receiveInput:"
+ "taskName"
+ "taskState"
+ "timestamp"
+ "v16@?0@\"BPSCompletion\"8"
+ "v16@?0@8"
- ", channelsByTopic: "
- "Currently subscribed channels for topic %s: %s"
- "Currently subscribed to channels: %s, for topic %s"
- "No channel options are provided for topic %s. Failed to register new random channel for this topic."
- "Subscribed to channel: %s for topic: %s"
- "Subscribed to random channel: %s for topic: %s"
- "Subscribing to a random channel on topic: %s"
- "Subscribing to all topics and channels"
- "Task was deferred while acquiring process. Exiting early."
- "Task was deferred while opening XPC connection to process. Exiting early."
- "There already exists one valid channel subscription %s for topic: %s. Skipping new subscription."
- "There is no channel for topic: %s"
- "Unsubscribing from all current channels for topic %s and subscribing to a new random channel."
- "channelsByTopic"

```
