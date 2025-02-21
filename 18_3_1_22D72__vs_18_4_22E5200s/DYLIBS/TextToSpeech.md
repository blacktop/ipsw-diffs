## TextToSpeech

> `/System/Library/PrivateFrameworks/TextToSpeech.framework/TextToSpeech`

```diff

-632.6.2.0.0
-  __TEXT.__text: 0x1bb280
-  __TEXT.__auth_stubs: 0x3a60
-  __TEXT.__objc_methlist: 0x4c70
-  __TEXT.__gcc_except_tab: 0x2f8c
-  __TEXT.__const: 0x2afc8
-  __TEXT.__cstring: 0x8446
-  __TEXT.__oslogstring: 0x3559
+641.1.3.0.0
+  __TEXT.__text: 0x1a1644
+  __TEXT.__auth_stubs: 0x3a20
+  __TEXT.__objc_methlist: 0x501c
+  __TEXT.__gcc_except_tab: 0x2f2c
+  __TEXT.__const: 0x2c4b8
+  __TEXT.__cstring: 0x80f6
+  __TEXT.__oslogstring: 0x3579
   __TEXT.__dlopen_cstrs: 0x408
   __TEXT.__ustring: 0x318
-  __TEXT.__swift5_typeref: 0x353c
+  __TEXT.__swift5_typeref: 0x3556
   __TEXT.__swift5_capture: 0x1490
   __TEXT.__swift5_reflstr: 0x2355
   __TEXT.__swift5_assocty: 0x5b0

   __TEXT.__swift5_mpenum: 0xd4
   __TEXT.__swift5_proto: 0x8c4
   __TEXT.__swift5_types: 0x3d8
+  __TEXT.__swift_as_entry: 0x2dc
+  __TEXT.__swift_as_ret: 0x320
   __TEXT.__swift5_protos: 0x38
-  __TEXT.__unwind_info: 0x7208
-  __TEXT.__eh_frame: 0x7b64
+  __TEXT.__unwind_info: 0x69c8
+  __TEXT.__eh_frame: 0x7a18
   __TEXT.__objc_classname: 0x684
   __TEXT.__objc_methname: 0xd0ef
   __TEXT.__objc_methtype: 0x1884
   __TEXT.__objc_stubs: 0x9a80
-  __DATA_CONST.__got: 0xa10
-  __DATA_CONST.__const: 0x1f58
+  __DATA_CONST.__got: 0xa30
+  __DATA_CONST.__const: 0x1f70
   __DATA_CONST.__objc_classlist: 0x2c0
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3330
+  __DATA_CONST.__objc_selrefs: 0x33c8
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x118
   __DATA_CONST.__objc_arraydata: 0x13d0
-  __AUTH_CONST.__auth_got: 0x1d48
-  __AUTH_CONST.__auth_ptr: 0xc40
-  __AUTH_CONST.__const: 0xc940
+  __AUTH_CONST.__auth_got: 0x1d28
+  __AUTH_CONST.__auth_ptr: 0xc48
+  __AUTH_CONST.__const: 0xcaa0
   __AUTH_CONST.__cfstring: 0x7200
-  __AUTH_CONST.__objc_const: 0x9d70
+  __AUTH_CONST.__objc_const: 0x96d0
   __AUTH_CONST.__objc_arrayobj: 0xf48
   __AUTH_CONST.__objc_intobj: 0x258
   __AUTH_CONST.__objc_doubleobj: 0x30

   __AUTH.__objc_data: 0x2070
   __AUTH.__data: 0x1988
   __DATA.__objc_ivar: 0x52c
-  __DATA.__data: 0x2500
-  __DATA.__bss: 0x12740
+  __DATA.__data: 0x2558
+  __DATA.__bss: 0x12610
   __DATA.__common: 0x158
   __DATA_DIRTY.__objc_data: 0xaf8
-  __DATA_DIRTY.__data: 0x610
-  __DATA_DIRTY.__bss: 0x728
+  __DATA_DIRTY.__data: 0x640
+  __DATA_DIRTY.__bss: 0x848
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 9688
-  Symbols:   1394
-  CStrings:  4283
+  Functions: 9174
+  Symbols:   1403
+  CStrings:  4265
 
Symbols:
+ _swift_allocateGenericValueMetadataWithLayoutString
+ _swift_enumFn_getEnumTag
+ _swift_generic_assignWithCopy
+ _swift_generic_assignWithTake
+ _swift_generic_destroy
+ _swift_generic_initWithCopy
+ _swift_generic_initWithTake
+ _swift_generic_initializeBufferWithCopyOfBuffer
+ _swift_generic_instantiateLayoutString
+ _swift_getExistentialTypeMetadata
+ _swift_getFunctionTypeMetadata0
+ _swift_initEnumMetadataMultiPayloadWithLayoutString
+ _swift_initEnumMetadataSinglePayloadWithLayoutString
+ _swift_initStructMetadataWithLayoutString
+ _swift_multiPayloadEnumGeneric_destructiveInjectEnumTag
+ _swift_multiPayloadEnumGeneric_getEnumTag
+ _swift_singlePayloadEnumGeneric_destructiveInjectEnumTag
+ _swift_singlePayloadEnumGeneric_getEnumTag
- _objc_release_x10
- _objc_retain_x10
- _strcmp
- _swift_allocateGenericValueMetadata
- _swift_getTupleTypeLayout
- _swift_getTupleTypeLayout2
- _swift_initEnumMetadataMultiPayload
- _swift_initEnumMetadataSinglePayload
- _swift_initStructMetadata
CStrings:
+ " to "
+ "Buffers for utterance: %{private}s"
+ "Buffers for utterances: %{private}s"
+ "Enqueue utterance: %{private}s"
+ "Enqueue utterances: %{private}s"
+ "^\\s*?(?<punctuation>[.,:;!?)])\\s*"
+ "name param "
- "@"
- "Buffers for utterance: %s"
- "Buffers for utterances: %s"
- "Can't construct Array with count < 0"
- "Division by zero"
- "Division results in an overflow"
- "Enqueue utterance: %s"
- "Enqueue utterances: %s"
- "Insufficient space allocated to copy string contents"
- "Swift/Array.swift"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/IntegerTypes.swift"
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
- "^\\s*?(?<punctuation>[.,:;!?)])"
- "invalid Collection: less than 'count' elements in collection"

```
