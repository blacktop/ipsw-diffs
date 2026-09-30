## systemservicemonitord

> `/usr/libexec/systemservicemonitord`

```diff

-3.100.6.0.0
-  __TEXT.__text: 0x58d8
-  __TEXT.__auth_stubs: 0x830
-  __TEXT.__const: 0x66
-  __TEXT.__cstring: 0x20f
-  __TEXT.__swift5_typeref: 0x92
-  __TEXT.__oslogstring: 0x6c6
+3.100.13.0.0
+  __TEXT.__text: 0x1924c
+  __TEXT.__auth_stubs: 0xe50
+  __TEXT.__objc_methlist: 0x104
+  __TEXT.__const: 0x328
+  __TEXT.__cstring: 0x77d
+  __TEXT.__constg_swiftt: 0x348
+  __TEXT.__swift5_typeref: 0x272
+  __TEXT.__swift5_reflstr: 0x147
+  __TEXT.__swift5_fieldmd: 0x1b4
+  __TEXT.__oslogstring: 0xe28
+  __TEXT.__swift5_capture: 0x190
+  __TEXT.__swift5_proto: 0x10
+  __TEXT.__swift5_types: 0x28
+  __TEXT.__objc_classname: 0x17
+  __TEXT.__objc_methname: 0x14f
+  __TEXT.__objc_methtype: 0xad
+  __TEXT.__swift_as_entry: 0x70
+  __TEXT.__swift_as_ret: 0x58
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__swift5_capture: 0x34
-  __TEXT.__constg_swiftt: 0x60
-  __TEXT.__swift5_fieldmd: 0x30
-  __TEXT.__swift5_types: 0xc
-  __TEXT.__unwind_info: 0x128
-  __TEXT.__eh_frame: 0x80
-  __DATA_CONST.__auth_got: 0x418
-  __DATA_CONST.__got: 0x158
-  __DATA_CONST.__auth_ptr: 0x48
-  __DATA_CONST.__const: 0x258
+  __TEXT.__unwind_info: 0x7c0
+  __TEXT.__eh_frame: 0x1a50
+  __DATA_CONST.__auth_got: 0x728
+  __DATA_CONST.__got: 0x228
+  __DATA_CONST.__auth_ptr: 0xe0
+  __DATA_CONST.__const: 0x508
+  __DATA_CONST.__objc_classlist: 0x30
+  __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__data: 0xb8
-  __DATA.__bss: 0x18
-  __DATA.__common: 0x50
+  __DATA_CONST.__objc_protorefs: 0x10
+  __DATA.__objc_const: 0xa18
+  __DATA.__objc_selrefs: 0xb0
+  __DATA.__objc_data: 0x50
+  __DATA.__data: 0x950
+  __DATA.__bss: 0x240
+  __DATA.__common: 0x70
+  - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/PrivateFrameworks/RemoteXPC.framework/RemoteXPC
   - /System/Library/PrivateFrameworks/SystemServiceMonitor.framework/SystemServiceMonitor
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_errno.dylib
   - /usr/lib/swift/libswift_math.dylib
   - /usr/lib/swift/libswift_signal.dylib

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 79
-  Symbols:   190
-  CStrings:  39
+  Functions: 404
+  Symbols:   326
+  CStrings:  142
 
Symbols:
+ _$s10Foundation4UUIDV10uuidStringSSvg
+ _$s10Foundation4UUIDVACycfC
+ _$s10Foundation4UUIDVMa
+ _$s20SystemServiceMonitor0B0V5StateOMn
+ _$s20SystemServiceMonitor0abC5ErrorO010duplicatedB0yA2CmFWC
+ _$s20SystemServiceMonitor0abC5ErrorO03xpcD0yACSScACmFWC
+ _$s20SystemServiceMonitor0abC5ErrorO10unexpectedyACSScACmFWC
+ _$s20SystemServiceMonitor0abC5ErrorO19serviceNotAvailableyA2CmFWC
+ _$s20SystemServiceMonitor0abC5ErrorO22serviceSessionNotReadyyA2CmFWC
+ _$s20SystemServiceMonitor0abC5ErrorO7timeoutyACSdcACmFWC
+ _$s20SystemServiceMonitor0abC5ErrorOs23CustomStringConvertibleAAMc
+ _$s20SystemServiceMonitor12NotificationO11StateUpdateV13asCodableEnumSe_SEpvg
+ _$s20SystemServiceMonitor12NotificationO11StateUpdateV5state16serviceIdentiferAeA0B0V0E0O_SStcfC
+ _$s20SystemServiceMonitor12NotificationO11StateUpdateVMa
+ _$s20SystemServiceMonitor12NotificationOAA14XPCConvertibleAAMc
+ _$s20SystemServiceMonitor12NotificationOMa
+ _$s20SystemServiceMonitor13QueryResponseV05EmptyE0VAA14XPCConvertibleAAMc
+ _$s20SystemServiceMonitor14ReportResponseV05ErrorE0V12errorMessageAESS_tcfC
+ _$s20SystemServiceMonitor14ReportResponseV05ErrorE0VMa
+ _$s20SystemServiceMonitor14ReportResponseV05ErrorE0VSEAAMc
+ _$s20SystemServiceMonitor14XPCConvertibleP5asXPC7replyToSo13OS_xpc_object_pSoAF_pSg_tKFTj
+ _$s20SystemServiceMonitor14XPCConvertiblePAAE5asXPC7replyToSo13OS_xpc_object_pSoAF_pSg_tKF
+ _$s20SystemServiceMonitor15RequestResponseV010StateFetchE0VAA0E15MessageProtocolAAMc
+ _$s20SystemServiceMonitor15RequestResponseV05ErrorE0V12errorMessageAESS_tcfC
+ _$s20SystemServiceMonitor15RequestResponseV05ErrorE0VMa
+ _$s20SystemServiceMonitor15RequestResponseV05ErrorE0VSEAAMc
+ _$s20SystemServiceMonitor15RequestResponseV0B4ListV0B4InfoV10identifier5state11xpcEndpointAGSS_AA0B0V5StateO3XPC11XPCEndpointVSgtcfC
+ _$s20SystemServiceMonitor15RequestResponseV0B4ListVAA0E15MessageProtocolAAMc
+ _$s20SystemServiceMonitor20NotificationResponseV011AcknowledgeE0VAA14XPCConvertibleAAMc
+ _$s20SystemServiceMonitor20NotificationResponseV011AcknowledgeE0VMa
+ _$s20SystemServiceMonitor20NotificationResponseV011AcknowledgeE0VMn
+ _$s20SystemServiceMonitor20NotificationResponseV011AcknowledgeE0VSeAAMc
+ _$s20SystemServiceMonitor5QueryO4PingV9sessionIdAESS_tcfC
+ _$s20SystemServiceMonitor6ReportO04PingD0V11cachedStateAA0B0V0G0Ovg
+ _$s20SystemServiceMonitor6ReportO04PingD0VMa
+ _$s20SystemServiceMonitor7RequestO0B4ListVAEycfC
+ _$s20SystemServiceMonitor7RequestO0B4WaitV7timeoutSdvg
+ _$s20SystemServiceMonitor7RequestO0B4WaitVAEycfC
+ _$s20SystemServiceMonitor7RequestO10StateFetchV17serviceIdentifierAESS_tcfC
+ _$s20SystemServiceMonitor7RequestO10StateFetchV17serviceIdentifierAESS_tcfcfA_
+ _$s20SystemServiceMonitor7RequestO10StateFetchV17serviceIdentifierSSvg
+ _$s20SystemServiceMonitor7RequestO10StateFetchVMa
+ _$s20SystemServiceMonitor7RequestO2eeoiySbAC_ACtFZ
+ _$s3XPC0A16_TYPE_DICTIONARYs13OpaquePointerVvg
+ _$s3XPC10XPCSessionC22setCancellationHandleryyyAA12XPCRichErrorVcFTj
+ _$s3XPC10XPCSessionC8sendSyncyAA18XPCReceivedMessageVxKSERzlFTj
+ _$s3XPC10XPCSessionCMn
+ _$s3XPC11XPCEndpointVMa
+ _$s3XPC11XPCEndpointVMn
+ _$s3XPC11XPCListenerC11targetQueue7options22incomingSessionHandlerACSo17OS_dispatch_queueCSg_AC21InitializationOptionsVAC08IncomingG7RequestC8DecisionVAMctcfc
+ _$s3XPC11XPCListenerC22IncomingSessionRequestC6accept22incomingMessageHandler012cancellationI0AE8DecisionV_AA10XPCSessionCtSE_pSgAA011XPCReceivedH0Vc_yAA12XPCRichErrorVcSgtFTj
+ _$s3XPC11XPCListenerC8endpointAA11XPCEndpointVvg
+ _$s3XPC11XPCListenerCMn
+ _$s3XPC12XPCRichErrorVMn
+ _$s3XPC18XPCReceivedMessageV13detachHandoffyyF
+ _$s3XPC18XPCReceivedMessageV5replyyyxSERzlF
+ _$s3XPC18XPCReceivedMessageVMa
+ _$s3XPC18XPCReceivedMessageVMn
+ _$sBoWV
+ _$sSS10FoundationE8EncodingV4utf8ACvgZ
+ _$sSS10FoundationE8EncodingVMa
+ _$sSS4hash4intoys6HasherVz_tF
+ _$sSS6appendyySSF
+ _$sSSN
+ _$sSSSysMc
+ _$sSa034_makeUniqueAndReserveCapacityIfNotB0yyFyXl_Ts5
+ _$sSa16_createNewBuffer14bufferIsUnique15minimumCapacity13growForAppendySb_SiSbtFyXl_Ts5
+ _$sSa37_appendElementAssumeUniqueAndCapacity_03newB0ySi_xntFyXl_Ts5
+ _$sSbN
+ _$sScA15unownedExecutorScevgTj
+ _$sScA15unownedExecutorScevgTq
+ _$sScAMp
+ _$sScM6sharedScMvgZ
+ _$sScMMa
+ _$sScMScAsWP
+ _$sScP8rawValues5UInt8Vvg
+ _$sScPMa
+ _$sSo13os_log_type_ta0A0E5debugABvgZ
+ _$sSo17OS_dispatch_queueC8DispatchE20AutoreleaseFrequencyO8workItemyA2EmFWC
+ _$sSo28OS_dispatch_queue_concurrentC8DispatchE10AttributesVMa
+ _$sSo28OS_dispatch_queue_concurrentC8DispatchE10AttributesVMn
+ _$sSo28OS_dispatch_queue_concurrentC8DispatchE10AttributesVs10SetAlgebraACMc
+ _$sSo28OS_dispatch_queue_concurrentC8DispatchE5label3qos10attributes20autoreleaseFrequency6targetABSS_AC0E3QoSVAbCE10AttributesVSo0a1_b1_C0CACE011AutoreleaseJ0OANSgtcfC
+ _$sSy10FoundationE7cString5usingSays4Int8VGSgSSAAE8EncodingV_tF
+ _$ss10_HashTableV12previousHole6beforeAB6BucketVAF_tF
+ _$ss11_StringGutsV4growyySiF
+ _$ss12_ArrayBufferV19_getElementSlowPathyyXlSiFyXl_Ts5
+ _$ss12_ArrayBufferV20_consumeAndCreateNew14bufferIsUnique15minimumCapacity13growForAppendAByxGSb_SiSbtFyXl_Ts5
+ _$ss15ContiguousArrayV034_makeUniqueAndReserveCapacityIfNotD0yyFyXl_Ts5
+ _$ss15ContiguousArrayV12_endMutationyyFyXl_Ts5
+ _$ss15ContiguousArrayV15reserveCapacityyySiFyXl_Ts5
+ _$ss15ContiguousArrayV36_reserveCapacityAssumingUniqueBuffer8oldCountySi_tFyXl_Ts5
+ _$ss15ContiguousArrayV37_appendElementAssumeUniqueAndCapacity_03newD0ySi_xntFyXl_Ts5
+ _$ss15ContinuousClockV7InstantVMa
+ _$ss15ContinuousClockV7InstantVs0C8ProtocolsMc
+ _$ss15ContinuousClockVABycfC
+ _$ss15ContinuousClockVMa
+ _$ss15ContinuousClockVs0B0sMc
+ _$ss15InstantProtocolP8advanced2byx8DurationQz_tFTj
+ _$ss18_CocoaArrayWrapperV8endIndexSivg
+ _$ss18_DictionaryStorageC4copy8originalAByxq_Gs05__RawaB0C_tFZ
+ _$ss18_DictionaryStorageC6resize8original8capacity4moveAByxq_Gs05__RawaB0C_SiSbtFZ
+ _$ss18_DictionaryStorageC8allocate8capacityAByxq_GSi_tFZ
+ _$ss18_DictionaryStorageCMn
+ _$ss23CustomStringConvertibleP11descriptionSSvgTj
+ _$ss26DefaultStringInterpolationV06appendC0yyxlF
+ _$ss27_stringCompareWithSmolCheck__9expectingSbs11_StringGutsV_ADs01_G16ComparisonResultOtF
+ _$ss53KEY_TYPE_OF_DICTIONARY_VIOLATES_HASHABLE_REQUIREMENTSys5NeverOypXpF
+ _$ss5ClockP3now7InstantQzvgTj
+ _$ss5ClockP5sleep5until9tolerancey7InstantQz_8DurationQzSgtYaKFTj
+ _$ss5ClockP5sleep5until9tolerancey7InstantQz_8DurationQzSgtYaKFTjTu
+ _$ss5ErrorMp
+ _$ss6HasherV5_hash4seed_S2i_s6UInt64VtFZ
+ _$ss6HasherV5_seedABSi_tcfC
+ _$ss6HasherV9_finalizeSiyF
+ _$ss6UInt64VN
+ _$sytN
+ _OBJC_CLASS_$_NSRunLoop
+ _OBJC_CLASS_$_OS_dispatch_queue_concurrent
+ _OBJC_CLASS_$_OS_xpc_remote_connection
+ _OBJC_CLASS_$__TtCs12_SwiftObject
+ _OBJC_METACLASS_$__TtCs12_SwiftObject
+ __objc_empty_cache
+ __swiftEmptyDictionarySingleton
+ __swift_stdlib_bridgeErrorToNSError
+ _bzero
+ _objc_msgSend
+ _objc_release
+ _objc_release_x22
+ _objc_release_x23
+ _objc_release_x24
+ _objc_release_x27
+ _objc_release_x28
+ _objc_retain
+ _objc_retain_x23
+ _objc_retain_x25
+ _objc_retain_x26
+ _objc_retain_x28
+ _swift_beginAccess
+ _swift_bridgeObjectRetain_n
+ _swift_deallocClassInstance
+ _swift_defaultActor_deallocate
+ _swift_defaultActor_destroy
+ _swift_defaultActor_initialize
+ _swift_deletedMethodError
+ _swift_dynamicCastObjCClass
+ _swift_endAccess
+ _swift_errorRetain
+ _swift_getErrorValue
+ _swift_getSingletonMetadata
+ _swift_isUniquelyReferenced_nonNull_bridgeObject
+ _swift_release_n
+ _swift_retain_n
+ _swift_task_alloc
+ _swift_task_create
+ _swift_task_dealloc
+ _swift_task_switch
+ _swift_unknownObjectRetain_n
+ _swift_updateClassMetadata2
+ _swift_willThrowTypedImpl
+ _xpc_dictionary_create_reply
+ _xpc_dictionary_set_string
+ _xpc_remote_connection_activate
+ _xpc_remote_connection_create_remote_service_listener
+ _xpc_remote_connection_send_message_with_reply_sync
+ _xpc_remote_connection_set_event_handler
+ _xpc_remote_connection_set_target_queue
- _$s20SystemServiceMonitor0B0V5StateO5readyyA2EmFWC
- _$s20SystemServiceMonitor0B0V5StateO6failedyA2EmFWC
- _$s20SystemServiceMonitor10CodableXPCC3xpcACSo03OS_F7_object_p_tcfC
- _$s20SystemServiceMonitor10CodableXPCCMa
- _$s20SystemServiceMonitor13QueryResponseV05EmptyE0VSeAAMc
- _$s20SystemServiceMonitor13QueryResponseVAA21XPCConverterProvidingAAMc
- _$s20SystemServiceMonitor13QueryResponseVMa
- _$s20SystemServiceMonitor14XPCConvertiblePAAE5asXPC_4intoSo13OS_xpc_object_px_SoAF_pSgtKFZ
- _$s20SystemServiceMonitor15RequestResponseV0B4ListV0B4InfoV10identifier5state11xpcEndpointAGSS_AA0B0V5StateOAA10CodableXPCCtcfC
- _$s20SystemServiceMonitor15RequestResponseV0B4ListVSEAAMc
- _$s20SystemServiceMonitor15RequestResponseVAA21XPCConverterProvidingAAMc
- _$s20SystemServiceMonitor15RequestResponseVMa
- _$s20SystemServiceMonitor21XPCConverterProvidingPAAE4from3xpc6asTypeqd__So03OS_G7_object_p_qd__mtKSeRd__lFZ
- _$s20SystemServiceMonitor21XPCConverterProvidingPAAE5asXPC_7replyToSo13OS_xpc_object_pSE_p_SoAF_ptKFZ
- _$s20SystemServiceMonitor5QueryO4PingVAEycfC
- _$s3XPC11XPCListenerC22IncomingSessionRequestC6accept22incomingMessageHandler012cancellationI0AE8DecisionVSE_pSgAA011XPCReceivedH0Vc_yAA12XPCRichErrorVcSgtFTj
- _$s3XPC12XPCRichErrorVs0C0AAMc
- _$sSo9OS_os_logC0B0E7defaultABvgZ
- _$ss27_diagnoseUnexpectedEnumCase4types5NeverOxm_tlF
- _$ss5ErrorP10FoundationE20localizedDescriptionSSvg
- _OBJC_CLASS_$_OS_os_log
- _dispatch_main
- _objc_retain_x19
- _objc_retain_x8
- _swift_errorInMain
- _swift_stdlib_random
- _swift_unexpectedError
- _xpc_connection_activate
- _xpc_connection_create_listener
- _xpc_connection_set_event_handler
- _xpc_connection_set_target_queue
CStrings:
+ "#16@0:8"
+ "$defaultActor"
+ "@\"NSString\"16@0:8"
+ "@16@0:8"
+ "@24@0:8:16"
+ "@32@0:8:16@24"
+ "@40@0:8:16@24@32"
+ "B16@0:8"
+ "B24@0:8#16"
+ "B24@0:8:16"
+ "B24@0:8@\"Protocol\"16"
+ "B24@0:8@16"
+ "Didn't find the record. Waiting for 1 second..."
+ "ErrorMessage"
+ "Failed to create & send a request response. "
+ "Failed to handle the received report. Error: "
+ "Failed to parse the response"
+ "Failed to register the remote XPC connection: Duplicate UUID"
+ "Failed to unregister the remote XPC connection: UUID not found"
+ "NSObject"
+ "OS_xpc_object"
+ "Q16@0:8"
+ "Received request from invalid client, missing entitlement ("
+ "Service database does not have consistent result when quried by id and by token"
+ "SessionUUID"
+ "Shouldn't even try to handle the unsupported request"
+ "T#,R"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",R,C"
+ "TQ,R"
+ "The allow request entitlement is set to 'NO'"
+ "The service identifier is empty"
+ "The session has already been activated"
+ "Vv16@0:8"
+ "[🔴] Failed to add the new service (%s) to the database upon receiving the 'Ping Response'. Error: %@"
+ "[🔴] Failed to remove the servie with token (%llu) from the service database. Error: %@"
+ "[🔴] Failed to send the 'StateUpdate' notification (through RemoteXPC) for service: %s. Error: %@."
+ "[🔴] Failed to send the 'StateUpdate' notification (through XPC) for service: %s. Error: %@."
+ "[🔴] Query Publisher: failed to get the descriptor when handling 'ADD' event."
+ "[🔴] Query Publisher: the descriptor doesn't contain valid 'sessionUUID' key."
+ "[🔴] failed to activate the service session: %@"
+ "[🔴] 👀 Query: failed to create the Ping query. Error: %@"
+ "[🔴] 👓 Remote Request: %s"
+ "[🔴] 👓 Remote Request: failed to create the error response"
+ "[🔴] 👓 Request: %s"
+ "[🔴] 👨\u200d🔧 Service Request: cannot parse the service request"
+ "[🔴] 👨\u200d🔧 Service Request: the received request is not support %s"
+ "[🔴] 🔖 Report: %s"
+ "[🔴] 🔗 Remote Request: RemoteXPC server got unexpected event: %s"
+ "[🔴] 🔗 Remote Request: Unexpected XPC: %s"
+ "[🔴] 🔗 Remote Request: failed to register the new remote client (id: %s) to the service: %s."
+ "[🔴] 🔗 Remote Request: failed to unregister the remote client (id: %s) from the service: %s."
+ "[🔴] 🔗 Remote Request: received error remote connection."
+ "[🔴] 🔗 Remote Request: received error remote event from the connected client."
+ "[🔴] 🔗 Service Request: request client connection is gone. Reason: %s"
+ "[🔵] 🔗 Remote Request: got incoming remote client connection."
+ "[🟡] 'ServiceList': failed to get the service info for service '%s'. Ignored the service."
+ "[🟡] Cannot remove the service with token (%llu) from the service database. Already removed?"
+ "[🟢] Successfully acitvated the service session for: %s with initial state: %s"
+ "[🟢] Successfully added a new the service record for (%s) to the database upon receiving the 'Ping Response'."
+ "[🟢] Successfully remove the service (%s) from the database."
+ "[🟢] 👓 Request: received 'ServiceList' request."
+ "[🟢] 👓 Request: received 'serviceWait' request."
+ "[🟢] 👓 Request: received 'stateFetch' request."
+ "[🟢] 👨\u200d🔧 Service Request: received StateFetch request and replied with the current state: %s"
+ "^{_NSZone=}16@0:8"
+ "_TtC21systemservicemonitord11QueryServer"
+ "_TtC21systemservicemonitord12ReportServer"
+ "_TtC21systemservicemonitord13RequestServer"
+ "_TtC21systemservicemonitord14ServiceSession"
+ "_TtC21systemservicemonitord15ServiceDatabase"
+ "_TtCC21systemservicemonitord15ServiceDatabase7Service"
+ "activated"
+ "asynRemoteRequestQueue"
+ "autorelease"
+ "class"
+ "com.apple.ssm.async.request.queue"
+ "com.apple.systemservicemonitor.request.remote"
+ "conformsToProtocol:"
+ "debugDescription"
+ "description"
+ "failed to convert the received XPC event to a Reques. Error: "
+ "hash"
+ "identifier"
+ "isEqual:"
+ "isKindOfClass:"
+ "isMemberOfClass:"
+ "isProxy"
+ "listener"
+ "mainRunLoop"
+ "performSelector:"
+ "performSelector:withObject:"
+ "performSelector:withObject:withObject:"
+ "publisher"
+ "queue"
+ "received report from invalid client, missing entitlement ("
+ "received supported request "
+ "received unsupported request"
+ "release"
+ "remoteListener"
+ "remoteXPCConnectionMap"
+ "requestListener"
+ "respondsToSelector:"
+ "retain"
+ "retainCount"
+ "run"
+ "self"
+ "serviceDatabase"
+ "servicesLookup"
+ "session"
+ "state"
+ "superclass"
+ "tokenServiceLookup"
+ "xpcEventToken"
+ "xpcListener"
+ "xpcSessions"
+ "zone"
+ "🔗 Query Publisher: Received ADD event from subscriber (token: %llu)"
- "[🔴] Failed to parse Request event"
- "[🔴] 👓 Request: Received request from invalid client, missing entitlement (%s)"
- "[🔴] 👓 Request: The allow request entitlement is set to 'NO'"
- "[🔴] 👓 Request: invalid request."
- "[🔴] 🔖 Report: received invalid report"
- "[🔴] 🔖 Report: received report from invalid client, missing entitlement (%s)"
- "[🟡] 👓 Request: received unsupport request %s."
- "[🟡] 🖥️ Reqeust: unsupported message: %s"
- "[🟢] 👓 Request: received 'ServiceList' request"
- "[🟢] 👓 Request: received 'serviceWait' request"
- "com.apple.denali"
- "com.apple.dummySerivce"
- "com.apple.ssm.service.reques"
- "systemservicemonitord/main.swift"
- "🖥️ Reqeust: received state fetch event"

```
