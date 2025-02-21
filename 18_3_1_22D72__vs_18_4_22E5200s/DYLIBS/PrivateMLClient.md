## PrivateMLClient

> `/System/Library/PrivateFrameworks/PrivateMLClient.framework/PrivateMLClient`

```diff

-109.0.0.0.0
-  __TEXT.__text: 0xbbdc4
-  __TEXT.__auth_stubs: 0x1630
-  __TEXT.__const: 0x60c8
-  __TEXT.__cstring: 0x2721
-  __TEXT.__swift5_typeref: 0x113a
-  __TEXT.__oslogstring: 0x131d
-  __TEXT.__constg_swiftt: 0x14f4
-  __TEXT.__swift5_fieldmd: 0x1bb8
-  __TEXT.__swift5_types: 0x18c
-  __TEXT.__swift5_reflstr: 0x18d5
-  __TEXT.__swift5_proto: 0x55c
-  __TEXT.__swift5_assocty: 0x208
+113.705.1.0.0
+  __TEXT.__text: 0x90024
+  __TEXT.__auth_stubs: 0x17e0
+  __TEXT.__const: 0x6c70
+  __TEXT.__cstring: 0x2901
+  __TEXT.__swift5_typeref: 0x151c
+  __TEXT.__oslogstring: 0x182d
+  __TEXT.__constg_swiftt: 0x1784
+  __TEXT.__swift5_fieldmd: 0x1e7c
+  __TEXT.__swift5_types: 0x1bc
+  __TEXT.__swift5_reflstr: 0x1b65
+  __TEXT.__swift5_capture: 0xc60
+  __TEXT.__swift5_proto: 0x600
+  __TEXT.__swift_as_entry: 0x54
+  __TEXT.__swift_as_ret: 0x60
+  __TEXT.__swift5_assocty: 0x250
   __TEXT.__swift5_builtin: 0x50
   __TEXT.__swift5_mpenum: 0x20
   __TEXT.__swift5_protos: 0x10
-  __TEXT.__swift5_capture: 0xbf4
-  __TEXT.__unwind_info: 0x2340
-  __TEXT.__eh_frame: 0x3fc8
+  __TEXT.__unwind_info: 0x2290
+  __TEXT.__eh_frame: 0x4758
   __TEXT.__objc_methname: 0xb9
-  __DATA_CONST.__got: 0x268
-  __DATA_CONST.__const: 0xb0
-  __DATA_CONST.__objc_classlist: 0x38
+  __DATA_CONST.__got: 0x2e0
+  __DATA_CONST.__const: 0x1d8
+  __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x50
-  __AUTH_CONST.__auth_got: 0xb18
-  __AUTH_CONST.__auth_ptr: 0x648
-  __AUTH_CONST.__const: 0x3810
-  __AUTH_CONST.__objc_const: 0xa90
-  __AUTH.__objc_data: 0x1e0
-  __AUTH.__data: 0x27c0
-  __DATA.__data: 0x1748
-  __DATA.__bss: 0xa500
-  __DATA.__common: 0x540
-  __DATA_DIRTY.__objc_data: 0x50
-  __DATA_DIRTY.__data: 0x3f0
+  __AUTH_CONST.__auth_got: 0xbf0
+  __AUTH_CONST.__auth_ptr: 0x6c0
+  __AUTH_CONST.__const: 0x3a80
+  __AUTH_CONST.__objc_const: 0xd10
+  __AUTH.__objc_data: 0x190
+  __AUTH.__data: 0xc28
+  __DATA.__data: 0x10a0
+  __DATA.__bss: 0x8880
+  __DATA.__common: 0x488
+  __DATA_DIRTY.__objc_data: 0x140
+  __DATA_DIRTY.__data: 0x3228
+  __DATA_DIRTY.__bss: 0x3100
+  __DATA_DIRTY.__common: 0x180
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCryptoTokenKit.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 3023
-  Symbols:   182
-  CStrings:  428
+  Functions: 2996
+  Symbols:   205
+  CStrings:  486
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCryptoTokenKit
+ __swift_stdlib_bridgeErrorToNSError
+ _objc_retain_x26
+ _swift_allocateGenericValueMetadataWithLayoutString
+ _swift_defaultActor_deallocate
+ _swift_defaultActor_destroy
+ _swift_defaultActor_initialize
+ _swift_enumFn_getEnumTag
+ _swift_errorRetain
+ _swift_generic_assignWithCopy
+ _swift_generic_assignWithTake
+ _swift_generic_destroy
+ _swift_generic_initWithCopy
+ _swift_generic_initWithTake
+ _swift_generic_initializeBufferWithCopyOfBuffer
+ _swift_getExistentialTypeMetadata
+ _swift_getObjCClassMetadata
+ _swift_getTupleTypeMetadata3
+ _swift_initEnumMetadataMultiPayloadWithLayoutString
+ _swift_initEnumMetadataSingleCaseWithLayoutString
+ _swift_initStructMetadataWithLayoutString
+ _swift_isUniquelyReferenced_nonNull_bridgeObject
+ _swift_multiPayloadEnumGeneric_destructiveInjectEnumTag
+ _swift_multiPayloadEnumGeneric_getEnumTag
+ _swift_setDeallocating
- _objc_release_x9
- _objc_retain_x8
- _swift_allocateGenericValueMetadata
- _swift_getTupleTypeLayout3
- _swift_initEnumMetadataMultiPayload
- _swift_initEnumMetadataSingleCase
- _swift_initStructMetadata
CStrings:
+ " isSelfAttention:"
+ "$defaultActor"
+ "%s Overriding workload parameters.inference-id=[%s]"
+ ".RichVariableBinding"
+ ".imageTokenizationOptions"
+ "Basic Task Task was cancelled."
+ "BasicTask defer complete."
+ "Cached PrivateMLResponse failed to generate cacheKey"
+ "Cancelling basic task"
+ "Create PrivateMLClientCloudComputeConnection."
+ "DYNAMIC"
+ "Error: basicTask failed %@"
+ "Finished basicTask"
+ "No BasicTask available to cancel."
+ "No BasicTask available."
+ "No Cached PrivateMLResponse "
+ "No generateCacheKey no inference-id"
+ "PMLCCM: Cancelled timeout and return cached connection - %ld"
+ "PMLCCM: Timeout connection cancelled."
+ "PMLCCM: cancelCacheKey ConnectionQueue is empty %s"
+ "PMLCCM: cancelCacheKey ConnectionQueue timeout nil! %s"
+ "PMLCCM: connection queue count:"
+ "PMLCCM: deqeue is nil %s"
+ "PMLCCM: dequeue ConnectionQueue is empty %s"
+ "PMLCCM: dequeue timeout ConnectionQueue is empty %s"
+ "PMLCCM: dequeue timeoutQueue is empty %s"
+ "PMLCCM: enqueued existing connection %s Count:%ld"
+ "PMLCCM: enqueued new connection %s"
+ "PMLCCM: immimentDelay set to %u"
+ "PMLCCM: start sleep."
+ "PMLCCM: timed out connection was not used."
+ "PMLCCM: timeout queue created and added."
+ "PMLCCM: timeout queue exists and added. Count:%ld"
+ "PMLCCM: timeout queue has not been initialized!"
+ "PMLCCM: wakeup."
+ "PrivateCloudComputePrivatedMLClientTransport prewarm - default"
+ "PrivateCloudComputePrivatedMLClientTransport prewarm - failed pccc connection"
+ "PrivateMLClient/PrivateMLClientCloudComputeConnection.swift"
+ "Running No Cached Connection."
+ "STATIC"
+ "Start streaming output."
+ "Start waiting on inputstream."
+ "Succeded in creating privateMLResponse."
+ "Using Cached Connection."
+ "_TtC15PrivateMLClient32PrivateMLClientConnectionManager"
+ "_TtC15PrivateMLClient37PrivateMLClientCloudComputeConnection"
+ "_imageTokenizationOption"
+ "_imageTokenizerName"
+ "_inferenceID"
+ "_tokenizerVersion"
+ "basicTask"
+ "completionBlockTest is nil."
+ "components"
+ "conectionDict"
+ "content_text"
+ "delay"
+ "generateCacheKey no adaptor"
+ "generateCacheKey no apple-featureid"
+ "generateCacheKey no model"
+ "image_tokenization_option"
+ "image_tokenizer_name"
+ "inference_id"
+ "inputContinuation"
+ "inputStream"
+ "is_self_attention"
+ "key"
+ "num_sub_images_max"
+ "num_sub_images_min"
+ "outputContinuation"
+ "outputStream"
+ "patch_width_in_pixel"
+ "private-client-cloud-compute-connection"
+ "private-client-connection-manager"
+ "request environment promptInfo "
+ "resolution_width_in_pixel"
+ "rich_variable"
+ "rich_variable_bindings"
+ "sendProtoAndReturnPrivateMLResponse construct privateMLResponse."
+ "text"
+ "tie-cloudboard-apple-com"
+ "tiling_strategy"
+ "timeoutDict"
+ "timeout_secs"
+ "tokenizer_version"
+ "withPrivateMLRequest: Attempting to dequeue a connection."
+ "workloadParameterInferenceIdOverride"
- "%s creating proto payload for private ML request"
- "%s invoking user's body"
- "%s proto payload %ld/%ld: %{private}s"
- "%s proto payload %ld/%ld: %{public}s"
- "%s writing serialized private ML request"
- "Can't construct Array with count < 0"
- "Division by zero"
- "Division results in an overflow"
- "Insufficient space allocated to copy string contents"
- "Swift/Array.swift"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/IntegerTypes.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawBufferPointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.initialize with negative count"
- "UnsafeMutableRawBufferPointer.copyMemory source has too many elements"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "invalid Collection: less than 'count' elements in collection"
- "preFetch"
- "requestIdentifier=%{public, signpost.description=attribute,public}s) workload=%{public, signpost.description=attribute,public}s)"
- "unable to convert to json: "

```
