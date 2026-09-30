## PrivateCloudCompute

> `/System/Library/PrivateFrameworks/PrivateCloudCompute.framework/PrivateCloudCompute`

```diff

-34.100.1.0.0
-  __TEXT.__text: 0x5d1ac
-  __TEXT.__auth_stubs: 0xf60
+40.200.12.0.0
+  __TEXT.__text: 0x59a84
+  __TEXT.__auth_stubs: 0xf20
   __TEXT.__objc_methlist: 0x20
-  __TEXT.__const: 0x69cc
-  __TEXT.__cstring: 0x2590
-  __TEXT.__swift5_typeref: 0x1588
-  __TEXT.__constg_swiftt: 0x120c
-  __TEXT.__swift5_reflstr: 0x19f3
+  __TEXT.__const: 0x680c
+  __TEXT.__cstring: 0x2730
+  __TEXT.__swift5_typeref: 0x1648
+  __TEXT.__constg_swiftt: 0x11e4
+  __TEXT.__swift5_reflstr: 0x1afa
   __TEXT.__swift5_fieldmd: 0x1f0c
-  __TEXT.__swift5_proto: 0x684
+  __TEXT.__swift5_proto: 0x660
   __TEXT.__swift5_types: 0x1e0
-  __TEXT.__swift5_builtin: 0x14
-  __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__swift5_assocty: 0x180
+  __TEXT.__swift5_builtin: 0x28
+  __TEXT.__swift5_mpenum: 0x10
+  __TEXT.__swift5_assocty: 0x108
   __TEXT.__oslogstring: 0x100
-  __TEXT.__swift5_capture: 0x244
+  __TEXT.__swift5_capture: 0x224
   __TEXT.__swift5_protos: 0x14
-  __TEXT.__unwind_info: 0x1fb8
-  __TEXT.__eh_frame: 0x2b98
+  __TEXT.__unwind_info: 0x1f18
+  __TEXT.__eh_frame: 0x2718
   __TEXT.__objc_methname: 0x52a
   __DATA_CONST.__got: 0x238
-  __DATA_CONST.__const: 0x80
-  __DATA_CONST.__objc_classlist: 0x40
+  __DATA_CONST.__const: 0xb8
+  __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xf8
   __DATA_CONST.__objc_protorefs: 0x10
-  __AUTH_CONST.__auth_got: 0x7b0
+  __AUTH_CONST.__auth_got: 0x790
   __AUTH_CONST.__auth_ptr: 0x380
-  __AUTH_CONST.__const: 0x3e00
-  __AUTH_CONST.__objc_const: 0x750
-  __AUTH.__objc_data: 0x3a0
-  __AUTH.__data: 0xe10
-  __DATA.__data: 0x14a8
-  __DATA.__bss: 0xc600
-  __DATA.__common: 0x30
+  __AUTH_CONST.__const: 0x3978
+  __AUTH_CONST.__objc_const: 0x630
+  __AUTH.__objc_data: 0x2d8
+  __AUTH.__data: 0xa80
+  __DATA.__data: 0x12c0
+  __DATA.__bss: 0xc000
+  __DATA.__common: 0x10
+  __DATA_DIRTY.__objc_data: 0x28
+  __DATA_DIRTY.__data: 0x3d0
+  __DATA_DIRTY.__bss: 0x380
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/PrivateFrameworks/AtomicsInternal.framework/AtomicsInternal
   - /System/Library/PrivateFrameworks/FeatureFlags.framework/FeatureFlags
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib

   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 2696
-  Symbols:   191
-  CStrings:  311
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 2601
+  Symbols:   195
+  CStrings:  310
 
Symbols:
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
+ _swift_initStackObject
+ _swift_setDeallocating
- _objc_retain
- _swift_continuation_await
- _swift_continuation_init
CStrings:
+ "Bug in PrivateCloudCompute adopter code!\n\nTrustedRequest.Reponse can only create a single AsyncIterator. Creating multiple\nAsyncIterators would lead to undefined behavior when iterating the iterators in\nparallel and is therefore forbidden."
+ "Bug in PrivateCloudCompute adopter code!\n\nTrustedRequest.Reponse.AsyncIterator is not Sendable and therefore must not\nbe invoked concurrently."
+ "PrivateCloudCompute/TrustedRequest.swift"
+ "failedToFetchPrivateAccessTokens"
+ "failedToLoadKeyData"
+ "failedToValidateAllAttestations"
+ "invalidAttestationBundle"
+ "invalidResponseUUID"
+ "missingAttestationBundle"
+ "rateLimitUnmatchedRequestStorageTimeout"
+ "receivedErrorCode"
+ "responseSummaryIndicatesFailure"
+ "responseSummaryIndicatesInvalidRequest"
+ "responseSummaryIndicatesUnauthenticated"
- "PrivateCloudCompute/TC2ClientRequest.swift"
- "TC2AttestationVerifierKind"
- "TC2NetworkHandlerKind"
- "TC2TokenProviderKind"
- "_TtC19PrivateCloudCompute16TC2ClientRequest"
- "_TtC19PrivateCloudCompute23TC2ClientRequestFactory"
- "attestationVerifier"
- "failure decoding TrustedCloudComputeError"
- "forceStubTokenProvider"
- "nw"
- "send(data:isComplete:)"
- "stream"
- "stub"
- "tokenProvider"
- "verifier"

```
