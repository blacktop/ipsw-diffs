## MessagesCloudSync

> `/System/Library/PrivateFrameworks/MessagesCloudSync.framework/MessagesCloudSync`

```diff

-1402.400.131.2.6
-  __TEXT.__text: 0x111ea4
-  __TEXT.__auth_stubs: 0x1f20
-  __TEXT.__objc_methlist: 0x610
-  __TEXT.__const: 0x7490
-  __TEXT.__cstring: 0x4ad1
-  __TEXT.__constg_swiftt: 0x2b20
-  __TEXT.__swift5_typeref: 0x267c
+1402.500.128.2.2
+  __TEXT.__text: 0xe048c
+  __TEXT.__auth_stubs: 0x1ef0
+  __TEXT.__objc_methlist: 0xb28
+  __TEXT.__const: 0x82d0
+  __TEXT.__cstring: 0x46e1
+  __TEXT.__constg_swiftt: 0x2b28
+  __TEXT.__swift5_typeref: 0x2680
   __TEXT.__swift5_builtin: 0x154
   __TEXT.__swift5_reflstr: 0x2b0a
   __TEXT.__swift5_fieldmd: 0x3138
   __TEXT.__swift5_assocty: 0x5a0
-  __TEXT.__oslogstring: 0x4a64
+  __TEXT.__oslogstring: 0x4a94
   __TEXT.__swift5_proto: 0x724
   __TEXT.__swift5_types: 0x2d0
-  __TEXT.__swift5_capture: 0xed0
+  __TEXT.__swift5_capture: 0xe10
   __TEXT.__swift5_mpenum: 0x58
   __TEXT.__swift5_protos: 0x8c
-  __TEXT.__unwind_info: 0x3c20
-  __TEXT.__eh_frame: 0x9524
+  __TEXT.__swift_as_entry: 0x3f8
+  __TEXT.__swift_as_ret: 0x478
+  __TEXT.__unwind_info: 0x34b0
+  __TEXT.__eh_frame: 0x935c
   __TEXT.__objc_classname: 0x195
-  __TEXT.__objc_methname: 0x2852
+  __TEXT.__objc_methname: 0x2876
   __TEXT.__objc_methtype: 0x55f
   __TEXT.__objc_stubs: 0x4a0
-  __DATA_CONST.__got: 0x780
-  __DATA_CONST.__const: 0x1b0
+  __DATA_CONST.__got: 0x790
+  __DATA_CONST.__const: 0x178
   __DATA_CONST.__objc_classlist: 0x110
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x100
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xd58
+  __DATA_CONST.__objc_selrefs: 0xe20
   __DATA_CONST.__objc_protorefs: 0x88
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0xf98
-  __AUTH_CONST.__auth_ptr: 0xa90
-  __AUTH_CONST.__const: 0x8678
+  __AUTH_CONST.__auth_got: 0xf80
+  __AUTH_CONST.__auth_ptr: 0xad0
+  __AUTH_CONST.__const: 0x86b0
   __AUTH_CONST.__cfstring: 0x60
-  __AUTH_CONST.__objc_const: 0x2db8
+  __AUTH_CONST.__objc_const: 0x24c8
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH.__objc_data: 0x3a8
+  __AUTH.__objc_data: 0x320
   __AUTH.__data: 0x578
   __DATA.__objc_ivar: 0x8
-  __DATA.__data: 0x1a98
-  __DATA.__bss: 0x9bf0
-  __DATA.__common: 0x18
+  __DATA.__data: 0x1920
+  __DATA.__bss: 0x90f0
+  __DATA.__common: 0x10
   __DATA_DIRTY.__objc_data: 0x588
-  __DATA_DIRTY.__data: 0x23b8
-  __DATA_DIRTY.__bss: 0x2b80
-  __DATA_DIRTY.__common: 0x260
+  __DATA_DIRTY.__data: 0x25f0
+  __DATA_DIRTY.__bss: 0x3680
+  __DATA_DIRTY.__common: 0x268
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreData.framework/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 4198
-  Symbols:   403
-  CStrings:  1514
+  Functions: 3667
+  Symbols:   414
+  CStrings:  1492
 
Symbols:
+ _objc_retain_x1
+ _swift_allocateGenericValueMetadataWithLayoutString
+ _swift_enumFn_getEnumTag
+ _swift_generic_assignWithCopy
+ _swift_generic_assignWithTake
+ _swift_generic_destroy
+ _swift_generic_initWithCopy
+ _swift_generic_initWithTake
+ _swift_generic_initializeBufferWithCopyOfBuffer
+ _swift_generic_instantiateLayoutString
+ _swift_initEnumMetadataMultiPayloadWithLayoutString
+ _swift_initEnumMetadataSinglePayloadWithLayoutString
+ _swift_initStructMetadataWithLayoutString
+ _swift_multiPayloadEnumGeneric_destructiveInjectEnumTag
+ _swift_multiPayloadEnumGeneric_getEnumTag
+ _swift_singlePayloadEnumGeneric_destructiveInjectEnumTag
+ _swift_singlePayloadEnumGeneric_getEnumTag
- __swift_FORCE_LOAD_$_swiftFileProvider
- _objc_release_x9
- _swift_allocateGenericValueMetadata
- _swift_initEnumMetadataMultiPayload
- _swift_initEnumMetadataSinglePayload
- _swift_initStructMetadata
CStrings:
+ "Tried to kick off %s, while another sync was in progress. See above for active sync handle. Not setting completed sync date or resetting sync state and status."
+ "initWithSenderInfo:time:timeRead:timeDelivered:timePlayed:subject:body:bodyData:attributes:fileTransferGUIDs:flags:guid:messageID:account:accountID:service:handle:roomName:unformattedID:countryCode:expireState:balloonBundleID:payloadData:expressiveSendStyleID:timeExpressiveSendPlayed:bizIntent:locale:biaReferenceID:errorType:threadIdentifier:syndicationRanges:syncedSyndicationRanges:partCount:dateEdited:dateRecovered:scheduleType:scheduleState:"
+ "isRelayChatBotEnabled"
- "Can't construct Array with count < 0"
- "Division by zero"
- "Division results in an overflow"
- "Fatal error"
- "Insufficient space allocated to copy string contents"
- "Negative value is not representable"
- "Not enough bits to represent the passed value"
- "Swift/Array.swift"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/IntegerTypes.swift"
- "Swift/Integers.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "Tried to kick off %s, while %s was in progress. Not setting completed sync date or resetting sync state and status."
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.initialize with negative count"
- "UnsafeMutablePointer.moveInitialize with negative count"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "initWithSenderInfo:time:timeRead:timeDelivered:timePlayed:subject:body:bodyData:attributes:fileTransferGUIDs:flags:guid:messageID:account:accountID:service:handle:roomName:unformattedID:countryCode:expireState:balloonBundleID:payloadData:expressiveSendStyleID:timeExpressiveSendPlayed:bizIntent:locale:biaReferenceID:errorType:threadIdentifier:syndicationRanges:syncedSyndicationRanges:partCount:dateEdited:scheduleType:scheduleState:"
- "invalid Collection: less than 'count' elements in collection"

```
