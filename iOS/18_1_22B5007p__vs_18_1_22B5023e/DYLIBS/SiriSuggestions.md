## SiriSuggestions

> `/System/Library/PrivateFrameworks/SiriSuggestions.framework/SiriSuggestions`

```diff

-3400.118.1.0.0
-  __TEXT.__text: 0x19b3c0
-  __TEXT.__auth_stubs: 0x4aa0
-  __TEXT.__const: 0xa244
-  __TEXT.__cstring: 0x6859
-  __TEXT.__swift5_typeref: 0x5284
-  __TEXT.__swift5_fieldmd: 0x3908
-  __TEXT.__constg_swiftt: 0x51f0
-  __TEXT.__swift5_reflstr: 0x2e4f
-  __TEXT.__swift5_capture: 0x698
-  __TEXT.__oslogstring: 0x7515
+3401.8.1.0.0
+  __TEXT.__text: 0x19cc50
+  __TEXT.__auth_stubs: 0x4b10
+  __TEXT.__const: 0xa2f4
+  __TEXT.__cstring: 0x6a59
+  __TEXT.__swift5_typeref: 0x5270
+  __TEXT.__swift5_fieldmd: 0x3950
+  __TEXT.__constg_swiftt: 0x520c
+  __TEXT.__swift5_reflstr: 0x2ecf
+  __TEXT.__swift5_capture: 0x6b8
+  __TEXT.__oslogstring: 0x7645
   __TEXT.__swift5_builtin: 0x50
   __TEXT.__swift5_assocty: 0x180
   __TEXT.__swift5_protos: 0x128
-  __TEXT.__swift5_proto: 0x8c8
+  __TEXT.__swift5_proto: 0x8d4
   __TEXT.__swift5_types: 0x4bc
   __TEXT.__swift5_mpenum: 0x1c
-  __TEXT.__unwind_info: 0x6460
-  __TEXT.__eh_frame: 0x11fb8
+  __TEXT.__unwind_info: 0x6568
+  __TEXT.__eh_frame: 0x122a8
   __TEXT.__objc_classname: 0x64
-  __TEXT.__objc_methname: 0xd1a
+  __TEXT.__objc_methname: 0xdb3
   __TEXT.__objc_methtype: 0x1cf
-  __DATA_CONST.__got: 0x1140
-  __DATA_CONST.__const: 0x318
+  __DATA_CONST.__got: 0x1190
+  __DATA_CONST.__const: 0x358
   __DATA_CONST.__objc_classlist: 0x6b0
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x380
+  __DATA_CONST.__objc_selrefs: 0x3a0
   __DATA_CONST.__objc_protorefs: 0x38
-  __AUTH_CONST.__auth_got: 0x2550
-  __AUTH_CONST.__auth_ptr: 0x1430
-  __AUTH_CONST.__const: 0x4bf0
-  __AUTH_CONST.__objc_const: 0xb9d0
-  __AUTH.__objc_data: 0x230
-  __AUTH.__data: 0x2a68
-  __DATA.__data: 0x2d68
-  __DATA.__bss: 0x84a0
-  __DATA.__common: 0xc0
+  __AUTH_CONST.__auth_got: 0x2588
+  __AUTH_CONST.__auth_ptr: 0x1438
+  __AUTH_CONST.__const: 0x4cc0
+  __AUTH_CONST.__objc_const: 0xba80
+  __AUTH.__objc_data: 0x260
+  __AUTH.__data: 0x2080
+  __DATA.__data: 0x2b48
+  __DATA.__bss: 0x7f20
+  __DATA.__common: 0x68
   __DATA_DIRTY.__objc_data: 0x7c8
-  __DATA_DIRTY.__data: 0x89c0
-  __DATA_DIRTY.__bss: 0x4c80
-  __DATA_DIRTY.__common: 0x168
+  __DATA_DIRTY.__data: 0x9660
+  __DATA_DIRTY.__bss: 0x5400
+  __DATA_DIRTY.__common: 0x1c8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 7929
-  Symbols:   3211
-  CStrings:  1394
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 8030
+  Symbols:   3266
+  CStrings:  1414
 
Symbols:
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
- _swift_taskGroup_destroy
- _swift_taskGroup_initialize
- _swift_willThrowTypedImpl
CStrings:
+ "Dialog created for suggestionId: %!s(MISSING). \n SpokenDialog: %!s(MISSING). \n DisplayDialog: %!s(MISSING)"
+ "Engagement logging failed, AppIntentIdentifier is nil"
+ "Failed to decorate %!s(MISSING) exampleUtterance=%!s(MISSING) with using CATTemplate: %!s(MISSING). Error: %!s(MISSING)"
+ "Logging engagement for Action: %!s(MISSING)"
+ "Logging engagement for AppIntent filter: %!s(MISSING)"
+ "Logging engagement for INIntent typeName from SuggestionsIntent: %!s(MISSING)"
+ "Logging engagement for full INIntent object: %!s(MISSING)"
+ "Suggestions#TriggerPhraseDecorator"
+ "SuggestionsIntent: %!s(MISSING) is not supported for logging"
+ "[InternalXPCServicesClient] Calling XPCService log"
+ "[InternalXPCServicesClient] Calling XPCService logEngagement"
+ "[InternalXPCServicesClient] XPCService log encountered error: %!@(MISSING)"
+ "_TtC15SiriSuggestions25ExampleUtteranceDecorator"
+ "appendTriggerPhrase"
+ "deviceUsesCompactVoiceTrigger"
+ "log(from:deliveryVehicle:generationId:)"
+ "logEngagement(for:with:invocationType:)"
+ "logEngagementFor:with:invocationType:featureConfig:with:"
+ "logFrom:deliveryVehicle:generationId:featureConfig:with:"
+ "sectionId"
+ "templateId"
+ "triggerPhraseDecorator"
+ "typeName"
+ "usesCompactVoiceTrigger"
+ "utteranceWithTriggerPhrase"
+ "v16@?0@\"NSError\"8"
+ "v56@0:8@\"NSData\"16@\"NSData\"24@\"NSUUID\"32@\"NSData\"40@?<v@?@\"NSError\">48"
+ "v56@0:8@\"NSData\"16@\"NSUUID\"24@\"NSData\"32@\"NSData\"40@?<v@?@\"NSError\">48"
+ "v56@0:8@16@24@32@40@?48"
+ "window processor starts processing new task."
- "Dialog created for %!s(MISSING)"
- "Engagement logging failed, IntentIdentifier is nil"
- "Failed to decorate isSpeakable=%!{(MISSING)bool}d hintText=%!s(MISSING) with Hints preamble: %!s(MISSING)"
- "Hints text is nil, no need to decorate it with preamble."
- "Intent: %!s(MISSING) is not supported for logging"
- "Pull suggestions mapped to intent: %!s(MISSING)"
- "Submitting engagement for Action: %!s(MISSING)"
- "Submitting engagement for Filter: %!s(MISSING)"
- "_TtC15SiriSuggestions26SiriHintsPreambleDecorator"
- "window processor started"

```
