## PrivateCloudCompute

> `/System/Library/PrivateFrameworks/PrivateCloudCompute.framework/PrivateCloudCompute`

```diff

-2230.18.0.0.0
-  __TEXT.__text: 0x5cdcc
-  __TEXT.__auth_stubs: 0xf30
-  __TEXT.__objc_methlist: 0x20
-  __TEXT.__const: 0x6bdc
-  __TEXT.__cstring: 0x25c7
-  __TEXT.__swift5_typeref: 0x1691
-  __TEXT.__constg_swiftt: 0x1130
-  __TEXT.__swift5_reflstr: 0x1b2a
-  __TEXT.__swift5_fieldmd: 0x20bc
-  __TEXT.__swift5_proto: 0x69c
-  __TEXT.__swift5_types: 0x1e4
+2250.18.1.0.0
+  __TEXT.__text: 0x53a84
+  __TEXT.__auth_stubs: 0xfe0
+  __TEXT.__objc_methlist: 0x124
+  __TEXT.__const: 0x7522
+  __TEXT.__cstring: 0x23b1
+  __TEXT.__swift5_typeref: 0x18f5
+  __TEXT.__oslogstring: 0xe1
+  __TEXT.__constg_swiftt: 0x12e0
+  __TEXT.__swift5_reflstr: 0x1c1f
+  __TEXT.__swift5_fieldmd: 0x2290
+  __TEXT.__swift5_types: 0x214
+  __TEXT.__swift_as_entry: 0xbc
+  __TEXT.__swift_as_ret: 0xc4
+  __TEXT.__swift5_proto: 0x72c
   __TEXT.__swift5_assocty: 0x120
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__oslogstring: 0xe1
   __TEXT.__swift5_capture: 0x224
   __TEXT.__swift5_protos: 0x10
-  __TEXT.__unwind_info: 0x1fc0
-  __TEXT.__eh_frame: 0x2778
-  __TEXT.__objc_methname: 0x539
-  __DATA_CONST.__got: 0x248
-  __DATA_CONST.__const: 0xb8
+  __TEXT.__unwind_info: 0x1cf0
+  __TEXT.__eh_frame: 0x2838
+  __TEXT.__objc_methname: 0x54a
+  __DATA_CONST.__got: 0x278
+  __DATA_CONST.__const: 0xc8
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x100
+  __DATA_CONST.__objc_selrefs: 0x108
   __DATA_CONST.__objc_protorefs: 0x10
-  __AUTH_CONST.__auth_got: 0x798
-  __AUTH_CONST.__auth_ptr: 0x378
-  __AUTH_CONST.__const: 0x3a00
+  __AUTH_CONST.__auth_got: 0x7f0
+  __AUTH_CONST.__auth_ptr: 0x380
+  __AUTH_CONST.__const: 0x3ab0
   __AUTH_CONST.__objc_const: 0x4c8
-  __AUTH.__objc_data: 0x238
-  __AUTH.__data: 0x3c0
-  __DATA.__data: 0x1160
-  __DATA.__bss: 0xb600
-  __DATA.__common: 0x18
+  __AUTH.__objc_data: 0x48
+  __AUTH.__data: 0x1d0
+  __DATA.__data: 0x1240
+  __DATA.__bss: 0xc000
   __DATA_DIRTY.__objc_data: 0x78
-  __DATA_DIRTY.__data: 0xbb0
-  __DATA_DIRTY.__bss: 0x1580
+  __DATA_DIRTY.__data: 0xfa8
+  __DATA_DIRTY.__bss: 0x1d80
+  __DATA_DIRTY.__common: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AtomicsInternal.framework/AtomicsInternal
+  - /System/Library/PrivateFrameworks/CloudAttestation.framework/CloudAttestation
   - /System/Library/PrivateFrameworks/FeatureFlags.framework/FeatureFlags
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCryptoTokenKit.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 2642
-  Symbols:   195
-  CStrings:  302
+  Functions: 2512
+  Symbols:   207
+  CStrings:  293
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCryptoTokenKit
+ _swift_allocateGenericValueMetadataWithLayoutString
+ _swift_generic_assignWithCopy
+ _swift_generic_assignWithTake
+ _swift_generic_destroy
+ _swift_generic_initWithCopy
+ _swift_generic_initWithTake
+ _swift_generic_initializeBufferWithCopyOfBuffer
+ _swift_getTupleTypeMetadata2
+ _swift_initEnumMetadataMultiPayloadWithLayoutString
+ _swift_initEnumMetadataSinglePayloadWithLayoutString
+ _swift_initStructMetadataWithLayoutString
+ _swift_multiPayloadEnumGeneric_destructiveInjectEnumTag
+ _swift_multiPayloadEnumGeneric_getEnumTag
+ _swift_singlePayloadEnumGeneric_destructiveInjectEnumTag
+ _swift_singlePayloadEnumGeneric_getEnumTag
+ _swift_task_reportUnexpectedExecutor
- _swift_allocateGenericValueMetadata
- _swift_getTupleTypeLayout2
- _swift_initEnumMetadataMultiPayload
- _swift_initEnumMetadataSinglePayload
- _swift_initStructMetadata
CStrings:
+ "Bug in PrivateCloudCompute adopter code!\n\nTrustedRequest.Response can only create a single AsyncIterator. Creating multiple\nAsyncIterators would lead to undefined behavior when iterating the iterators in\nparallel and is therefore forbidden."
+ "Bug in PrivateCloudCompute adopter code!\n\nTrustedRequest.Response.AsyncIterator is not Sendable and therefore must not\nbe invoked concurrently."
+ "enforceWorkloadParametersFiltering"
+ "https://gateway-oblivious.apple.com/pcc/bag-uat"
+ "https://ropes-uat.apple.com"
+ "prewarmRequest(workloadType:workloadParameters:bundleIdentifier:featureIdentifier:runOnEventStream:)"
+ "prewarmRequestWithWorkloadType:workloadParameters:bundleIdentifier:featureIdentifier:runOnEventStream:completion:"
+ "privacyProxyFailed"
+ "privacyProxyFeatureDisabled"
+ "privacyProxyInvalidAuthentication"
+ "privacyProxyInvalidConfigData"
+ "privacyProxyInvalidConfigDataSign"
+ "privacyProxyInvalidParam"
+ "privacyProxyInvalidRequest"
+ "privacyProxyInvalidUserTier"
+ "privacyProxyIpcFailed"
+ "privacyProxyNetworkFailure"
+ "privacyProxyPermissionDenied"
+ "privacyProxyRateLimited"
+ "privacyProxyServerFailure"
+ "publicKey expiry "
+ "ropes-uat.apple.com"
+ "routingGroupAlias"
+ "uat"
+ "v60@0:8@\"NSString\"16@\"NSDictionary\"24@\"NSString\"32@\"NSString\"40B48@?<v@?>52"
+ "v60@0:8@16@24@32@40B48@?52"
- "Bug in PrivateCloudCompute adopter code!\n\nTrustedRequest.Reponse can only create a single AsyncIterator. Creating multiple\nAsyncIterators would lead to undefined behavior when iterating the iterators in\nparallel and is therefore forbidden."
- "Bug in PrivateCloudCompute adopter code!\n\nTrustedRequest.Reponse.AsyncIterator is not Sendable and therefore must not\nbe invoked concurrently."
- "Division by zero"
- "Division results in an overflow"
- "Insufficient space allocated to copy string contents"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/IntegerTypes.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "TC2RequestParameters"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.initialize with negative count"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "allowedWorkloadParameters"
- "failedToFetchPrivateAccessTokens"
- "input-token-count-interval-end-open"
- "input-token-count-interval-start-closed"
- "invalid Collection: less than 'count' elements in collection"
- "max-allowed-output-tokens-interval-end-open"
- "max-allowed-output-tokens-interval-start-closed"
- "pipelineArguments"
- "prefetchRequestTimeout"
- "prewarmRequest(workloadType:workloadParameters:bundleIdentifier:featureIdentifier:)"
- "prewarmRequestWithWorkloadType:workloadParameters:bundleIdentifier:featureIdentifier:completion:"
- "rateLimitRequestTimeout"
- "trustedRequestFirstPayloadChunkTimeout"
- "uniqueNodeIdentifier"
- "useStructedTrustedRequest"
- "v56@0:8@\"NSString\"16@\"NSDictionary\"24@\"NSString\"32@\"NSString\"40@?<v@?>48"
- "v56@0:8@16@24@32@40@?48"

```
