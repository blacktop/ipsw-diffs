## SiriMessagesFlow

> `/System/Library/PrivateFrameworks/SiriMessagesFlow.framework/SiriMessagesFlow`

```diff

-3401.23.2.0.0
-  __TEXT.__text: 0x3b5090
-  __TEXT.__auth_stubs: 0x7900
+3402.35.1.0.0
+  __TEXT.__text: 0x3c657c
+  __TEXT.__auth_stubs: 0x7cb0
   __TEXT.__objc_methlist: 0x50
-  __TEXT.__const: 0xf854
-  __TEXT.__cstring: 0xe067
-  __TEXT.__constg_swiftt: 0xd118
-  __TEXT.__swift5_typeref: 0x66fb
-  __TEXT.__swift5_builtin: 0x348
-  __TEXT.__swift5_reflstr: 0x7deb
-  __TEXT.__swift5_fieldmd: 0x8f5c
-  __TEXT.__swift5_assocty: 0x1160
-  __TEXT.__swift5_proto: 0xb58
-  __TEXT.__swift5_types: 0x690
-  __TEXT.__swift5_capture: 0x2984
-  __TEXT.__oslogstring: 0x235cf
-  __TEXT.__swift5_protos: 0x168
+  __TEXT.__const: 0xfa04
+  __TEXT.__cstring: 0xe177
+  __TEXT.__constg_swiftt: 0xd2b0
+  __TEXT.__swift5_typeref: 0x6865
+  __TEXT.__swift5_builtin: 0x334
+  __TEXT.__swift5_reflstr: 0x7f6b
+  __TEXT.__swift5_fieldmd: 0x9288
+  __TEXT.__swift5_assocty: 0x1178
+  __TEXT.__swift5_proto: 0xb60
+  __TEXT.__swift5_types: 0x69c
+  __TEXT.__swift5_capture: 0x29a4
+  __TEXT.__oslogstring: 0x23b9f
+  __TEXT.__swift5_protos: 0x16c
   __TEXT.__swift5_mpenum: 0x84
-  __TEXT.__unwind_info: 0xd128
-  __TEXT.__eh_frame: 0x24494
+  __TEXT.__unwind_info: 0xd1d8
+  __TEXT.__eh_frame: 0x2473c
   __TEXT.__objc_classname: 0x111
-  __TEXT.__objc_methname: 0x3b70
+  __TEXT.__objc_methname: 0x3bab
   __TEXT.__objc_methtype: 0x32c
-  __DATA_CONST.__got: 0x1f70
+  __DATA_CONST.__got: 0x2088
   __DATA_CONST.__const: 0x238
-  __DATA_CONST.__objc_classlist: 0x5a0
+  __DATA_CONST.__objc_classlist: 0x5b0
   __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x14e0
+  __DATA_CONST.__objc_selrefs: 0x14f0
   __DATA_CONST.__objc_protorefs: 0x78
-  __AUTH_CONST.__auth_got: 0x3c80
-  __AUTH_CONST.__auth_ptr: 0x25c8
-  __AUTH_CONST.__const: 0x104a0
-  __AUTH_CONST.__objc_const: 0xcd10
-  __AUTH.__objc_data: 0x1f28
-  __AUTH.__data: 0x11640
-  __DATA.__data: 0x6b78
-  __DATA.__bss: 0x13300
+  __AUTH_CONST.__auth_got: 0x3e58
+  __AUTH_CONST.__auth_ptr: 0x2488
+  __AUTH_CONST.__const: 0x106a0
+  __AUTH_CONST.__objc_const: 0xce78
+  __AUTH.__objc_data: 0x1f78
+  __AUTH.__data: 0x11920
+  __DATA.__data: 0x6c58
+  __DATA.__bss: 0x13390
   __DATA.__common: 0xa20
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /System/Library/PrivateFrameworks/FeatureFlags.framework/FeatureFlags
   - /System/Library/PrivateFrameworks/GenerativeModels.framework/GenerativeModels
   - /System/Library/PrivateFrameworks/IMCore.framework/IMCore
+  - /System/Library/PrivateFrameworks/IntelligenceFlow.framework/IntelligenceFlow
   - /System/Library/PrivateFrameworks/LinkMetadata.framework/LinkMetadata
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/MediaRemote.framework/MediaRemote

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 16630
-  Symbols:   8423
-  CStrings:  4221
+  Functions: 16755
+  Symbols:   8508
+  CStrings:  4256
 
Symbols:
+ _OBJC_CLASS_$_NSPropertyListSerialization
+ _bzero
+ _swift_getKeyPath
CStrings:
+ "#LocationComponent Fail to serialize punchout into SpeakableString"
+ "#LocationComponent locationURL is nil"
+ "#LocationComponent punchout dictionary is nil"
+ "#MessagesFlowDelegatePlugin SiriKitContactResolving Running CRR with queries: %!s(MISSING)"
+ "#MessagesFlowDelegatePlugin SiriKitContactResolving.resolveContacts Failed with error: %!@(MISSING)"
+ "#MessagesFlowDelegatePlugin received a client action parse: %!s(MISSING)"
+ "#MessagesFlowDelegatePlugin unexpected client action toolId: %!s(MISSING)"
+ "#SendMessageHandleIntentFlowStrategy can not support app intent responses"
+ "#SendMessageShimFlow adding INPerson: %!@(MISSING)"
+ "#SendMessageShimFlow converted to: %!@(MISSING)"
+ "#SendMessageShimFlow converting %!s(MISSING)"
+ "#SendMessageShimFlow extractingParameters from ClientAction %!s(MISSING)"
+ "#SendMessageShimFlow pushing SendMessageFlow"
+ "#SendMessageShimFlow recipeint TypedPerson.toString: %!s(MISSING)"
+ "#SendMessageShimFlow recipeints TypedPerson count: %!l(MISSING)d with values %!s(MISSING)"
+ "#ShareThisFlow found Siri generated response result to share"
+ "#SiriGeneratedResponseProvider: fetchSiriGeneratedResults cannot find a match for common_FormattedString entity in SRR"
+ "#SiriGeneratedResponseProvider: fetchSiriGeneratedResults failed to find a match for common_FormattedString entity in SRR"
+ "#SiriGeneratedResponseProvider: fetchSiriGeneratedResults found foundMatchPlural/needsDisambiguation %!s(MISSING)"
+ "#SiriGeneratedResponseProvider: fetchSiriGeneratedResults found multiple matches with %!s(MISSING)"
+ "#SiriGeneratedResponseProvider: fetchSiriGeneratedResults foundMatch with %!s(MISSING)"
+ "#SpokenReplyOfferFlowStrategy update dimissal settings"
+ "_TtC16SiriMessagesFlow19SendMessageShimFlow"
+ "_TtC16SiriMessagesFlow29SiriGeneratedResponseProvider"
+ "attachmentContainsDefiniteReference: %!s(MISSING)"
+ "buttonPunchoutAction"
+ "clientAction"
+ "com.apple.generativeassistanttools.GenerativeAssistantExtension"
+ "dataWithPropertyList:format:options:error:"
+ "generatedResponseProvider"
+ "hasLocationPunchout"
+ "isolatedID"
+ "locationPunchout"
+ "location_smart_reply"
+ "montara"
+ "newMessage"
+ "payloadPrompt"
+ "setPunchOutUri:"
+ "toWho"
+ "toWithColon"
- "#SiriKitContactResolving CRR returned no result, returning person as is"
- "#SiriKitContactResolving Resolved person with CRR: %!@(MISSING)"
- "#SiriKitContactResolving Running CRR with query: %!s(MISSING)"
- "#SiriKitContactResolving error invoking CRR to resolve "
- "SiriMessagesFlow/MessagesContactResolutionUtils.swift"

```
