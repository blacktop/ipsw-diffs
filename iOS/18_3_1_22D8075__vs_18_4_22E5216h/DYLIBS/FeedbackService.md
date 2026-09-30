## FeedbackService

> `/System/Library/PrivateFrameworks/FeedbackService.framework/FeedbackService`

```diff

-139.9.0.0.0
-  __TEXT.__text: 0x790ec
-  __TEXT.__auth_stubs: 0x1470
-  __TEXT.__objc_methlist: 0xda0
-  __TEXT.__const: 0xa798
-  __TEXT.__cstring: 0x3288
+150.8.0.0.0
+  __TEXT.__text: 0x7bc64
+  __TEXT.__auth_stubs: 0x14a0
+  __TEXT.__objc_methlist: 0x10fc
+  __TEXT.__const: 0xa524
+  __TEXT.__cstring: 0x30c8
   __TEXT.__ustring: 0xd8
-  __TEXT.__oslogstring: 0xc6f
+  __TEXT.__oslogstring: 0xcff
   __TEXT.__gcc_except_tab: 0x10c
-  __TEXT.__constg_swiftt: 0x20ac
-  __TEXT.__swift5_typeref: 0x2522
-  __TEXT.__swift5_fieldmd: 0x21e4
-  __TEXT.__swift5_types: 0x2fc
-  __TEXT.__swift5_reflstr: 0x1061
+  __TEXT.__constg_swiftt: 0x20ec
+  __TEXT.__swift5_typeref: 0x2526
+  __TEXT.__swift5_fieldmd: 0x2234
+  __TEXT.__swift5_types: 0x304
+  __TEXT.__swift5_reflstr: 0x1071
   __TEXT.__swift5_proto: 0xa08
-  __TEXT.__swift5_capture: 0x468
-  __TEXT.__swift5_assocty: 0x198
+  __TEXT.__swift5_capture: 0x478
+  __TEXT.__swift5_assocty: 0x180
+  __TEXT.__swift_as_entry: 0x60
+  __TEXT.__swift_as_ret: 0x60
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_builtin: 0x8c
   __TEXT.__swift5_mpenum: 0x3c
-  __TEXT.__unwind_info: 0x2580
-  __TEXT.__eh_frame: 0x2220
+  __TEXT.__unwind_info: 0x2370
+  __TEXT.__eh_frame: 0x2468
   __TEXT.__objc_classname: 0x177
-  __TEXT.__objc_methname: 0x267c
+  __TEXT.__objc_methname: 0x26a5
   __TEXT.__objc_methtype: 0xa1c
   __TEXT.__objc_stubs: 0x15a0
-  __DATA_CONST.__got: 0x3e8
-  __DATA_CONST.__const: 0x578
+  __DATA_CONST.__got: 0x400
+  __DATA_CONST.__const: 0x5a8
   __DATA_CONST.__objc_classlist: 0x120
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8b8
+  __DATA_CONST.__objc_selrefs: 0x9d8
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x60
-  __AUTH_CONST.__auth_got: 0xa48
-  __AUTH_CONST.__auth_ptr: 0x360
-  __AUTH_CONST.__const: 0x4ea8
+  __AUTH_CONST.__auth_got: 0xa60
+  __AUTH_CONST.__auth_ptr: 0x380
+  __AUTH_CONST.__const: 0x5170
   __AUTH_CONST.__cfstring: 0xda0
-  __AUTH_CONST.__objc_const: 0x2d10
-  __AUTH.__objc_data: 0x1d0
-  __AUTH.__data: 0x98
+  __AUTH_CONST.__objc_const: 0x28b8
   __DATA.__objc_ivar: 0xd0
-  __DATA.__data: 0x2260
-  __DATA.__common: 0x120
-  __DATA.__bss: 0x14120
+  __DATA.__data: 0x12a0
+  __DATA.__common: 0x88
+  __DATA.__bss: 0xa3a0
   __DATA_DIRTY.__objc_data: 0x1928
-  __DATA_DIRTY.__data: 0x7e8
-  __DATA_DIRTY.__bss: 0x80
+  __DATA_DIRTY.__data: 0x17f0
+  __DATA_DIRTY.__common: 0x88
+  __DATA_DIRTY.__bss: 0x9e00
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswift_errno.dylib
   - /usr/lib/swift/libswift_math.dylib
   - /usr/lib/swift/libswift_signal.dylib

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 3658
-  Symbols:   673
-  CStrings:  1037
+  Functions: 3470
+  Symbols:   710
+  CStrings:  1031
 
Symbols:
+ _AnalyticsSendEvent
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_enumFn_getEnumTag
+ _swift_cvw_initEnumMetadataMultiPayloadWithLayoutString
+ _swift_cvw_initStructMetadataWithLayoutString
+ _swift_cvw_initWithCopy
+ _swift_cvw_initWithTake
+ _swift_cvw_initializeBufferWithCopyOfBuffer
+ _swift_cvw_multiPayloadEnumGeneric_destructiveInjectEnumTag
+ _swift_cvw_multiPayloadEnumGeneric_getEnumTag
+ _swift_getDynamicType
+ _swift_getTupleTypeMetadata2
- _swift_initEnumMetadataMultiPayload
- _swift_initStructMetadata
- _swift_unknownObjectWeakDestroy
- _swift_unknownObjectWeakInit
- _swift_unknownObjectWeakLoadStrong
CStrings:
+ "Compose in Writing Tools"
+ "Presented interaction from %s. Is presented inline: %{bool}d"
+ "Sent Interaction Presented event with payload: %s"
+ "Unable to send analytics without Interaction: %s"
+ "_remoteEvaluate(action:sceneID:bundleID:showFeedbackForm:)"
+ "com.apple.centralized-feedback.evaluation"
+ "com.apple.centralized-feedback.evaluation."
+ "com.apple.centralized-feedback.evaluation.universal"
+ "featureDomainEnum"
+ "fetch(donationID:)"
+ "generatedContentEnum"
+ "image structured "
+ "image text "
+ "name data "
+ "originalContentEnum"
+ "presentedInteractionWithAnalyticsPayload:featureDomainEventName:completion:"
+ "remoteEvaluateWithRequest:sceneID:bundleID:completion:"
+ "sketch structured "
+ "sketch text "
+ "v40@0:8@\"NSDictionary\"16@\"NSString\"24@?<v@?@\"NSError\">32"
+ "v48@0:8@\"NSData\"16@\"NSString\"24@\"NSString\"32@?<v@?@\"NSData\"@\"NSError\">40"
- "Cannot convert to a StructuredValue"
- "ChatGPT Integration in Siri"
- "Compose with ChatGPT in Writing Tools"
- "Division by zero"
- "Division results in an overflow"
- "Donation is not supported on FCS"
- "Insufficient space allocated to copy string contents"
- "Must take zero or more splits"
- "Range requires lowerBound <= upperBound"
- "Swift/Collection.swift"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/IntegerTypes.swift"
- "Swift/Range.swift"
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
- "invalid Collection: less than 'count' elements in collection"
- "presentedInteractionWithInteractionJSON:completion:"
- "remoteEvaluateWithRequest:completion:"
- "v32@0:8@\"NSData\"16@?<v@?@\"NSData\"@\"NSError\">24"

```
