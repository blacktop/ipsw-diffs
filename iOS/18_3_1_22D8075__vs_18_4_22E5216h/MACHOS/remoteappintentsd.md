## remoteappintentsd

> `/usr/libexec/remoteappintentsd`

```diff

-31.21.0.0.0
-  __TEXT.__text: 0x4938
-  __TEXT.__auth_stubs: 0x850
-  __TEXT.__objc_methlist: 0x2c
-  __TEXT.__const: 0x142
+33.19.0.0.0
+  __TEXT.__text: 0x215c
+  __TEXT.__auth_stubs: 0x440
+  __TEXT.__objc_methlist: 0x14c
+  __TEXT.__const: 0x114
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__cstring: 0x639
+  __TEXT.__cstring: 0x1a2
   __TEXT.__constg_swiftt: 0xb0
-  __TEXT.__swift5_typeref: 0x162
+  __TEXT.__swift5_typeref: 0xed
   __TEXT.__swift5_reflstr: 0x67
   __TEXT.__swift5_fieldmd: 0x6c
-  __TEXT.__oslogstring: 0x25a
-  __TEXT.__objc_methname: 0x1fb
-  __TEXT.__swift5_capture: 0x64
+  __TEXT.__oslogstring: 0x127
   __TEXT.__swift5_proto: 0x4
   __TEXT.__swift5_types: 0xc
-  __TEXT.__objc_classname: 0x6c
+  __TEXT.__objc_classname: 0x5e
+  __TEXT.__objc_methname: 0x1d5
   __TEXT.__objc_methtype: 0xe9
-  __TEXT.__unwind_info: 0x198
-  __TEXT.__eh_frame: 0x130
-  __DATA_CONST.__auth_got: 0x428
-  __DATA_CONST.__got: 0xb8
-  __DATA_CONST.__auth_ptr: 0x70
-  __DATA_CONST.__const: 0x1d8
+  __TEXT.__unwind_info: 0xf0
+  __DATA_CONST.__auth_got: 0x220
+  __DATA_CONST.__got: 0x48
+  __DATA_CONST.__auth_ptr: 0x60
+  __DATA_CONST.__const: 0xb8
   __DATA_CONST.__objc_classlist: 0x18
-  __DATA_CONST.__objc_protolist: 0x60
+  __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x30
-  __DATA.__objc_const: 0x5b0
-  __DATA.__objc_selrefs: 0x58
+  __DATA_CONST.__objc_protorefs: 0x28
+  __DATA.__objc_const: 0x388
+  __DATA.__objc_selrefs: 0xe8
   __DATA.__objc_data: 0xb0
-  __DATA.__data: 0x4b0
+  __DATA.__data: 0x3b0
+  __DATA.__common: 0x20
   __DATA.__bss: 0x80
-  __DATA.__common: 0x18
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AppIntentsServices.framework/AppIntentsServices
   - /System/Library/PrivateFrameworks/LinkServices.framework/LinkServices

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_errno.dylib
   - /usr/lib/swift/libswift_math.dylib
   - /usr/lib/swift/libswift_signal.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 106
-  Symbols:   199
-  CStrings:  111
+  Functions: 49
+  Symbols:   119
+  CStrings:  73
 
Symbols:
+ _$s18AppIntentsServices24ActorTransactionDelegateP29willBeginLongRunningOperationyyAA0deK0VYbFTq
+ _$s18AppIntentsServices25ActorTransactionOperationV2id10Foundation4UUIDVvg
+ _$s18AppIntentsServices25ActorTransactionOperationV4nameSSvg
+ _$s18AppIntentsServices25ActorTransactionOperationVMa
+ _objc_release_x23
+ _objc_release_x24
+ _objc_retain_x21
- _$s10Foundation4UUIDV10uuidStringSSvg
- _$s18AppIntentsServices06RemoteaB8ListenerC5start19transactionDelegateyAA016ActorTransactionH0_p_tF
- _$s18AppIntentsServices06RemoteaB8ListenerCACycfc
- _$s18AppIntentsServices06RemoteaB8ListenerCMa
- _$s18AppIntentsServices0A25NotificationEventRegistryC9dumpStateyyFZ
- _$s18AppIntentsServices15RemoteFileStoreC15MaintenanceTaskO8registeryyFZ
- _$s18AppIntentsServices24ActorTransactionDelegateP29willBeginLongRunningOperationyy10Foundation4UUIDVYbFTq
- _$s6Darwin7SIG_IGNyys5Int32VXCvg
- _$s8Dispatch0A13WorkItemFlagsVMa
- _$s8Dispatch0A13WorkItemFlagsVMn
- _$s8Dispatch0A13WorkItemFlagsVs10SetAlgebraAAMc
- _$s8Dispatch0A3QoSV11unspecifiedACvgZ
- _$s8Dispatch0A3QoSV13userInitiatedACvgZ
- _$s8Dispatch0A3QoSVMa
- _$s8Dispatch0A9PredicateO7onQueueyACSo17OS_dispatch_queueCcACmFWC
- _$s8Dispatch0A9PredicateOMa
- _$s8Dispatch25_dispatchPreconditionTestySbAA0A9PredicateOF
- _$sSD4KeysV11descriptionSSvg
- _$sSKsSS7ElementRtzrlE6joined9separatorS2S_tF
- _$sSS10FoundationE36_unconditionallyBridgeFromObjectiveCySSSo8NSStringCSgFZ
- _$sSS7cStringSSSPys4Int8VG_tcfC
- _$sSa034_makeUniqueAndReserveCapacityIfNotB0yyFyXl_Ts5
- _$sSa12_endMutationyyFyXl_Ts5
- _$sSa16_createNewBuffer14bufferIsUnique15minimumCapacity13growForAppendySb_SiSbtFyXl_Ts5
- _$sSa37_appendElementAssumeUniqueAndCapacity_03newB0ySi_xntFyXl_Ts5
- _$sSayxGSKsMc
- _$sSayxGSTsMc
- _$sScA15unownedExecutorScevgTj
- _$sScP8rawValues5UInt8Vvg
- _$sScPMa
- _$sSo17OS_dispatch_queueC8DispatchE10AttributesVMa
- _$sSo17OS_dispatch_queueC8DispatchE10AttributesVMn
- _$sSo17OS_dispatch_queueC8DispatchE10AttributesVs10SetAlgebraACMc
- _$sSo17OS_dispatch_queueC8DispatchE20AutoreleaseFrequencyO8workItemyA2EmFWC
- _$sSo17OS_dispatch_queueC8DispatchE20AutoreleaseFrequencyOMa
- _$sSo17OS_dispatch_queueC8DispatchE5label3qos10attributes20autoreleaseFrequency6targetABSS_AC0D3QoSVAbCE10AttributesVAbCE011AutoreleaseI0OABSgtcfC
- _$sSo18OS_dispatch_sourceC8DispatchE16makeSignalSource6signal5queueSo0a1_b1_c1_H0_ps5Int32V_So0a1_b1_I0CSgtFZ
- _$sSo18OS_dispatch_sourceP8DispatchE15setEventHandler3qos5flags7handleryAC0D3QoSV_AC0D13WorkItemFlagsVyyXBSgtF
- _$sSo18OS_dispatch_sourceP8DispatchE8activateyyF
- _$sSw10copyMemory4fromySW_tF
- _$sSwys5UInt8VSicis
- _$ss10SetAlgebraPyxqd__ncSTRd__7ElementQyd__ACRtzlufCTj
- _$ss17_assertionFailure__4file4line5flagss5NeverOs12StaticStringV_A2HSus6UInt32VtF
- _$ss18_fatalErrorMessage__4file4line5flagss5NeverOs12StaticStringV_A2HSus6UInt32VtF
- _LNAppNotificationEventListenerMachServiceNameSuffix
- _NSTemporaryDirectory
- _OBJC_CLASS_$_NSXPCListener
- _OBJC_CLASS_$_OS_dispatch_queue
- _OBJC_CLASS_$_OS_dispatch_source
- __Block_copy
- __Block_release
- __NSConcreteStackBlock
- __set_user_dir_suffix
- __swift_FORCE_LOAD_$_swiftFileProvider
- __xpc_event_key_name
- _dispatch_main
- _objc_allocWithZone
- _objc_release
- _objc_release_x22
- _objc_release_x26
- _objc_release_x27
- _objc_release_x28
- _objc_retain_x23
- _objc_retain_x8
- _qos_class_self
- _signal
- _swift_beginAccess
- _swift_bridgeObjectRelease_n
- _swift_bridgeObjectRetain_n
- _swift_deallocObject
- _swift_endAccess
- _swift_getObjCClassFromMetadata
- _swift_getObjCClassMetadata
- _swift_getTypeByMangledNameInContextInMetadataState2
- _swift_retain
- _swift_task_alloc
- _swift_task_create
- _swift_task_dealloc
- _swift_task_switch
- _swift_weakDestroy
- _swift_weakInit
- _swift_weakLoadStrong
- _xpc_dictionary_create_reply
- _xpc_dictionary_get_bool
- _xpc_dictionary_get_string
- _xpc_dictionary_send_reply
- _xpc_set_event_stream_handler
CStrings:
+ "remoteappintentsd."
- "%s received SIGUSR2, dumping state"
- "%s: Starting Event Listener: %s"
- "%s: waiting for initial Rapport event"
- "Bootstrapping listener with QoS class: %s"
- "Failed to reply to Rapport wake event: %s"
- "Fatal error"
- "Insufficient space allocated to copy string contents"
- "Long running transactions: %s"
- "OS_xpc_object"
- "QOS_CLASS_BACKGROUND"
- "QOS_CLASS_DEFAULT"
- "QOS_CLASS_UNSPECIFIED"
- "QOS_CLASS_USER_INITIATED"
- "QOS_CLASS_USER_INTERACTIVE"
- "QOS_CLASS_UTILITY"
- "Received Rapport wake event for: %s"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.initialize with negative count"
- "UnsafeMutablePointer.moveInitialize with negative count"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "UnsafeMutableRawPointer.initializeMemory with negative count"
- "com.apple.RemoteAppIntentsDaemon.rapport.internal"
- "com.apple.rapport.matching"
- "com.apple.remoteappintentsd"
- "initWithMachServiceName:"
- "invalid Collection: less than 'count' elements in collection"
- "remoteappintentsd-operation-"
- "replyRequired"
- "setDelegate:"
- "v16@?0@\"<OS_xpc_object>\"8"
- "v8@?0"

```
