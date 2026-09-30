## AskToCore

> `/System/Library/PrivateFrameworks/AskToCore.framework/AskToCore`

```diff

-37.1.0.0.0
-  __TEXT.__text: 0x1f054
-  __TEXT.__auth_stubs: 0xfb0
-  __TEXT.__objc_methlist: 0x488
-  __TEXT.__const: 0x11fc
-  __TEXT.__cstring: 0x1609
-  __TEXT.__swift5_typeref: 0x5e9
-  __TEXT.__oslogstring: 0x92e
-  __TEXT.__swift5_reflstr: 0x5ce
-  __TEXT.__swift5_assocty: 0xf0
-  __TEXT.__constg_swiftt: 0x6ac
-  __TEXT.__swift5_fieldmd: 0x73c
-  __TEXT.__swift5_builtin: 0x50
+40.0.0.0.0
+  __TEXT.__text: 0x2058c
+  __TEXT.__auth_stubs: 0xfc0
+  __TEXT.__objc_methlist: 0x4b8
+  __TEXT.__const: 0x156c
+  __TEXT.__cstring: 0x1ca9
+  __TEXT.__swift5_typeref: 0x6a9
+  __TEXT.__oslogstring: 0xa0e
+  __TEXT.__swift5_reflstr: 0x5fe
+  __TEXT.__swift5_assocty: 0x138
+  __TEXT.__constg_swiftt: 0x944
+  __TEXT.__swift5_fieldmd: 0x808
+  __TEXT.__swift5_builtin: 0x8c
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__swift5_proto: 0x104
-  __TEXT.__swift5_types: 0x7c
-  __TEXT.__swift5_protos: 0x18
+  __TEXT.__swift5_proto: 0x14c
+  __TEXT.__swift5_types: 0xa8
+  __TEXT.__swift5_protos: 0x1c
   __TEXT.__swift5_capture: 0x30
-  __TEXT.__unwind_info: 0x988
-  __TEXT.__eh_frame: 0x998
+  __TEXT.__unwind_info: 0x998
+  __TEXT.__eh_frame: 0x958
   __TEXT.__objc_classname: 0x3b
-  __TEXT.__objc_methname: 0xa31
+  __TEXT.__objc_methname: 0x9f8
   __TEXT.__objc_methtype: 0x100
   __DATA_CONST.__got: 0x1d8
-  __DATA_CONST.__const: 0x1a0
-  __DATA_CONST.__objc_classlist: 0x30
+  __DATA_CONST.__const: 0x1c8
+  __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x368
+  __DATA_CONST.__objc_selrefs: 0x358
   __DATA_CONST.__objc_protorefs: 0x40
-  __AUTH_CONST.__auth_got: 0x7d8
-  __AUTH_CONST.__auth_ptr: 0x270
-  __AUTH_CONST.__const: 0xe78
-  __AUTH_CONST.__objc_const: 0xed0
-  __AUTH.__objc_data: 0x558
-  __AUTH.__data: 0x2a8
-  __DATA.__data: 0x790
-  __DATA.__bss: 0x1e00
-  __DATA.__common: 0xf0
+  __AUTH_CONST.__auth_got: 0x7e0
+  __AUTH_CONST.__auth_ptr: 0x288
+  __AUTH_CONST.__const: 0xfd0
+  __AUTH_CONST.__objc_const: 0x1148
+  __AUTH.__objc_data: 0x70
+  __AUTH.__data: 0x4a8
+  __DATA.__data: 0x810
+  __DATA.__bss: 0x2600
+  __DATA.__common: 0x108
+  __DATA_DIRTY.__objc_data: 0x4d8
+  __DATA_DIRTY.__data: 0x188
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 815
-  Symbols:   192
-  CStrings:  372
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 832
+  Symbols:   199
+  CStrings:  415
 
Symbols:
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
- _OBJC_CLASS_$_NSString
CStrings:
+ "Error archiving ATQuestion %!@(MISSING)"
+ "Logging request journey metric with checkpoint %!{(MISSING)public}s"
+ "Logging request send metric"
+ "Logging response journey metric with checkpoint %!{(MISSING)public}s"
+ "Logging response send metric"
+ "Not initializing ATQuestion (coder had nil value for key \"data\")"
+ "Not initializing ATQuestion (nil value for key \"data\")"
+ "Not initializing ATQuestion (unarchiver had nil value for key \"value\")"
+ "_TtC9AskToCoreP33_FFF05204D7DDE95B20550B814A9FA4F812JourneyEvent"
+ "_TtC9AskToCoreP33_FFF05204D7DDE95B20550B814A9FA4F819RequestJourneyEvent"
+ "_TtC9AskToCoreP33_FFF05204D7DDE95B20550B814A9FA4F820ResponseJourneyEvent"
+ "allApproversHaveIDSAvailabilityConfirmed"
+ "architectureVersion"
+ "askToResponseSendComplete"
+ "askToSendComplete"
+ "checkpoint"
+ "clientCalledIntoAskToToSendRequest"
+ "com.apple.family.AskTo.ResponseJourney"
+ "com.apple.family.AskTo.SendJourney"
+ "confirmedProcessInAllowList"
+ "daemonCallSucceeded"
+ "daemonReceivedSendCall"
+ "daemonReceivedSendCallFromClient"
+ "finishedPeopleCanSendChecks"
+ "gotMessagesPayload"
+ "gotMessagesPayloadFromExtension"
+ "iMessageEnabledConfirmed"
+ "iMessageHasEmailHandleConfirmed"
+ "killSwitchFalseConfirmed"
+ "mappedResponseToScreenTimeAnswer"
+ "messagesSendSPIReturnedTrue"
+ "name"
+ "passedUnsupportedEndpointsChecks"
+ "peopleDaemonReceivedCanSendCall"
+ "peopleFamilyCircleFetchSucceeded"
+ "peopleFamilyCircleHasApprovers"
+ "peopleFamilyCircleHasRequester"
+ "performedAllResponseTasks"
+ "platformSupportedConfirmed"
+ "questionTopic"
+ "recipientGroupHasSendDestinationsConfirmed"
+ "resolvedRecipientGroup"
+ "responseSenderConfirmedPayloadHasResponse"
+ "responseTaskConfirmedPayloadHasResponse"
+ "screenTimeCallSucceeded"
+ "send(question:to:)"
+ "sendWithQuestion:to:completionHandler:"
+ "updatedLocalMessagesDatabaseWithResponse"
+ "userTappedAnswerChoice"
+ "userTappedOptionsButton"
+ "v36@0:8@\"_TtC5AskTo10ATQuestion\"16s24@?<v@?@\"NSArray\"@\"NSError\">28"
+ "validSendDestinationsConfirmed"
- "canSendWithValidDestinations()"
- "canSendWithValidDestinationsWithCompletionHandler:"
- "sendRequest(_:to:)"
- "sendRequest:to:completionHandler:"
- "stringGUID"
- "v20@?0B8@\"NSError\"12"
- "v24@0:8@?16"
- "v24@0:8@?<v@?B@\"NSError\">16"
- "v36@0:8@\"_TtC9AskToCore9ATPayload\"16s24@?<v@?@\"NSArray\"@\"NSError\">28"

```
