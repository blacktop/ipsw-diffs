## SiriInCall

> `/System/Library/PrivateFrameworks/SiriInCall.framework/SiriInCall`

```diff

 3400.14.1.0.0
-  __TEXT.__text: 0x7b4c
-  __TEXT.__auth_stubs: 0x8b0
+  __TEXT.__text: 0x7d64
   __TEXT.__objc_methlist: 0x158
-  __TEXT.__const: 0x5a8
-  __TEXT.__swift5_typeref: 0x246
+  __TEXT.__const: 0x5d0
+  __TEXT.__swift5_typeref: 0x2a2
   __TEXT.__swift5_fieldmd: 0x16c
   __TEXT.__constg_swiftt: 0x4b0
   __TEXT.__swift5_builtin: 0x64

   __TEXT.__swift5_reflstr: 0xd2
   __TEXT.__oslogstring: 0x455
   __TEXT.__cstring: 0x271
-  __TEXT.__swift5_capture: 0x74
+  __TEXT.__swift5_capture: 0xb4
   __TEXT.__swift_as_entry: 0xc
   __TEXT.__swift_as_ret: 0x8
-  __TEXT.__unwind_info: 0x328
-  __TEXT.__eh_frame: 0x180
-  __TEXT.__objc_classname: 0xbb
-  __TEXT.__objc_methname: 0x619
-  __TEXT.__objc_methtype: 0x1b2
-  __TEXT.__objc_stubs: 0x580
-  __DATA_CONST.__got: 0x140
-  __DATA_CONST.__const: 0xd8
+  __TEXT.__swift_as_cont: 0x14
+  __TEXT.__unwind_info: 0x338
+  __TEXT.__eh_frame: 0x188
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0xd0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x220
   __DATA_CONST.__objc_protorefs: 0x10
-  __AUTH_CONST.__auth_got: 0x460
-  __AUTH_CONST.__const: 0x4d8
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__const: 0x578
   __AUTH_CONST.__objc_const: 0x320
+  __AUTH_CONST.__auth_got: 0x510
   __AUTH.__data: 0x30
-  __DATA.__data: 0x170
+  __DATA.__data: 0x180
   __DATA.__bss: 0x280
   __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0x90

   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
-  - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: C4AAA98D-B0E2-38CE-AA44-864303696CE1
-  Functions: 274
-  Symbols:   342
-  CStrings:  135
+  UUID: 77D00489-EF4A-3A33-961C-59AEDFF66383
+  Functions: 283
+  Symbols:   385
+  CStrings:  29
 
Symbols:
+ ___swift_async_cont_functlets
+ ___swift_closure_destructor
+ ___swift_closure_destructor.17
+ ___swift_closure_destructor.2
+ ___swift_closure_destructor.20
+ ___swift_closure_destructor.23
+ ___swift_closure_destructor.26
+ ___swift_closure_destructor.29
+ ___swift_closure_destructor.32
+ ___swift_closure_destructor.36
+ __swift_implicitisolationactor_to_executor_cast
+ _objc_release_x28
+ _objc_retain_x26
+ _swift_continuation_await
+ _swift_continuation_init
+ _swift_release_n
+ _swift_release_x19
+ _swift_release_x20
+ _swift_release_x22
+ _swift_release_x24
+ _swift_release_x25
+ _swift_release_x26
+ _swift_release_x27
+ _swift_release_x8
+ _swift_retain_n
+ _swift_retain_x19
+ _swift_retain_x2
+ _swift_retain_x20
+ _swift_retain_x22
+ _swift_retain_x23
+ _swift_retain_x24
+ _swift_retain_x25
+ _swift_retain_x27
+ _swift_setDeallocating
+ _symbolic Sb
+ _symbolic SbIegd_
+ _symbolic _____Iegd_ s5Int32V
+ _symbolic _____Iegr_ s5Int32V
+ _symbolic _____yySpy_____Gz_SpySo8NSObjectCSgGSgzSpyypGSgztcG s23_ContiguousArrayStorageC s5UInt8V
+ _symbolic yyc
- __swift_FORCE_LOAD_$_swiftCoreMedia
- __swift_FORCE_LOAD_$_swiftCoreMedia_$_SiriInCall
CStrings:
- "#16@0:8"
- "@\"NSString\"16@0:8"
- "@16@0:8"
- "@24@0:8:16"
- "@32@0:8:16@24"
- "@40@0:8:16@24@32"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "NSObject"
- "Q16@0:8"
- "SiriAnalyticsMessageStream"
- "T#,R"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "TQ,R"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_TtC10SiriInCall15ButterflyBridge"
- "_TtC10SiriInCall25ButterflyRequestProcessor"
- "_TtC10SiriInCall29SiriInCallInstrumentationUtil"
- "activeCallExists"
- "activeConversationForCall:"
- "activeRemoteParticipants"
- "autorelease"
- "avMode"
- "barrierWithCompletion:"
- "callCenter"
- "callState"
- "class"
- "clientMessageStream"
- "conformsToProtocol:"
- "debugDescription"
- "defaultMessageStream"
- "derivedIdentifierForComponentName:fromSourceIdentifier:"
- "description"
- "emitMessage:"
- "emitMessage:timestamp:"
- "enqueueLargeMessageObjectFromPath:assetIdentifier:messageMetadata:completion:"
- "fetchContextsForKeys:forRequestID:includesNearbyDevices:completion:"
- "frontmostAudioOrVideoCall"
- "hash"
- "init"
- "initWithNSUUID:"
- "initWithSerializedBackingStore:"
- "instrumentationUtil"
- "isConversation"
- "isEqual:"
- "isFaceTimeProvider"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "isSystemProvider"
- "isTelephonyProvider"
- "isUplinkMuted"
- "isVideo"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "provider"
- "release"
- "remoteParticipantHandles"
- "requestType"
- "resolvePartialMessage:"
- "resolvePartialMessage:timestamp:"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "self"
- "serializedContextByKey"
- "setCallAppType:"
- "setCallState:"
- "setCallType:"
- "setCancelled:"
- "setComponent:"
- "setEnded:"
- "setEventMetadata:"
- "setExists:"
- "setIsMuted:"
- "setParticipantCountBucket:"
- "setSicId:"
- "setSiriInCallInvocationContext:"
- "setSource:"
- "setStartedOrChanged:"
- "setTarget:"
- "setUuid:"
- "sharedAnalytics"
- "sharedInstance"
- "sharedStream"
- "status"
- "stream"
- "superclass"
- "supportsAudioAndVideo"
- "supportsAudioOnly"
- "v16@?0@\"NSArray\"8"
- "v24@0:8@\"SISchemaTopLevelUnionType\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?>16"
- "v32@0:8@\"SISchemaTopLevelUnionType\"16Q24"
- "v32@0:8@16Q24"
- "v48@0:8@\"NSString\"16@\"NSUUID\"24@\"SISchemaInstrumentationMessage\"32@?<v@?B@\"NSError\">40"
- "v48@0:8@16@24@32@?40"
- "zone"

```
