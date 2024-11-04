## SummarizationKit

> `/System/Library/PrivateFrameworks/SummarizationKit.framework/SummarizationKit`

```diff

-1.2.1.0.0
-  __TEXT.__text: 0x10f804
-  __TEXT.__auth_stubs: 0x3060
-  __TEXT.__const: 0x56a2
-  __TEXT.__cstring: 0x5204
-  __TEXT.__constg_swiftt: 0x1c80
-  __TEXT.__swift5_typeref: 0x1a5a
-  __TEXT.__swift5_reflstr: 0x26ad
-  __TEXT.__swift5_fieldmd: 0x1d58
+1.2.4.0.0
+  __TEXT.__text: 0x114d70
+  __TEXT.__auth_stubs: 0x31e0
+  __TEXT.__const: 0x57b8
+  __TEXT.__cstring: 0x52b4
+  __TEXT.__constg_swiftt: 0x1e04
+  __TEXT.__swift5_typeref: 0x1b32
+  __TEXT.__swift5_reflstr: 0x27eb
+  __TEXT.__swift5_fieldmd: 0x1e24
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_assocty: 0x278
-  __TEXT.__oslogstring: 0x31c3
-  __TEXT.__swift5_capture: 0x1498
-  __TEXT.__swift5_proto: 0x418
-  __TEXT.__swift5_types: 0x19c
-  __TEXT.__swift5_protos: 0x50
-  __TEXT.__unwind_info: 0x3e50
-  __TEXT.__eh_frame: 0x8af0
+  __TEXT.__oslogstring: 0x3303
+  __TEXT.__swift5_capture: 0x14f0
+  __TEXT.__swift5_proto: 0x428
+  __TEXT.__swift5_types: 0x1a4
+  __TEXT.__swift5_protos: 0x54
+  __TEXT.__unwind_info: 0x3f20
+  __TEXT.__eh_frame: 0x8c40
   __TEXT.__objc_classname: 0x18
-  __TEXT.__objc_methname: 0x4b3
+  __TEXT.__objc_methname: 0x4d1
   __TEXT.__objc_methtype: 0x46
-  __DATA_CONST.__got: 0x858
+  __DATA_CONST.__got: 0x8b8
   __DATA_CONST.__const: 0x268
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1b8
+  __DATA_CONST.__objc_selrefs: 0x1c0
   __DATA_CONST.__objc_protorefs: 0x10
-  __AUTH_CONST.__auth_got: 0x1830
+  __AUTH_CONST.__auth_got: 0x18f0
   __AUTH_CONST.__auth_ptr: 0xb58
-  __AUTH_CONST.__const: 0x4f80
-  __AUTH_CONST.__objc_const: 0x18a0
+  __AUTH_CONST.__const: 0x5268
+  __AUTH_CONST.__objc_const: 0x1988
   __AUTH.__objc_data: 0x2b8
-  __AUTH.__data: 0x2b78
-  __DATA.__data: 0x2490
-  __DATA.__bss: 0x6ac8
-  __DATA.__common: 0x478
+  __AUTH.__data: 0x2b98
+  __DATA.__data: 0x26a8
+  __DATA.__bss: 0x6be8
+  __DATA.__common: 0x4b0
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CryptoKit.framework/CryptoKit

   - /System/Library/PrivateFrameworks/IntelligencePlatformLibrary.framework/IntelligencePlatformLibrary
   - /System/Library/PrivateFrameworks/InternalSwiftProtobuf.framework/InternalSwiftProtobuf
   - /System/Library/PrivateFrameworks/ModelCatalog.framework/ModelCatalog
+  - /System/Library/PrivateFrameworks/ProactiveDaemonSupport.framework/ProactiveDaemonSupport
   - /System/Library/PrivateFrameworks/PromptKit.framework/PromptKit
   - /System/Library/PrivateFrameworks/Sage.framework/Sage
   - /System/Library/PrivateFrameworks/TextComposer.framework/TextComposer

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftRegexBuilder.dylib
+  - /usr/lib/swift/libswiftSynchronization.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 4998
-  Symbols:   269
-  CStrings:  664
+  Functions: 5051
+  Symbols:   273
+  CStrings:  675
 
Symbols:
+ _objc_retain_x2
+ _swift_runtimeSupportsNoncopyableTypes
+ _swift_weakDestroy
+ _swift_weakInit
+ _swift_weakLoadStrong
CStrings:
+ "@unknown case for SummarizationClient.TextAssistantSummarizationOptions.Source; received %!{(MISSING)public}s"
+ "Evicted session from cache for [useCaseIdentifier: %!{(MISSING)public}s, clientApplicationIdentifier: %!{(MISSING)public}s, clientProcessIdentifier: %!{(MISSING)public}d]"
+ "Image content type encountered when reducing PromptCompletion candidate"
+ "Returning session from cache for [requestIdentifier: %!{(MISSING)public}s, useCaseIdentifier: %!{(MISSING)public}s, clientApplicationIdentifier: %!{(MISSING)public}s, clientProcessIdentifier: %!{(MISSING)public}d]"
+ "SessionCache.cacheCleanup"
+ "^(?i).*\\breacted .+ to your photo\\.$"
+ "^(?i)\\w+ your message:.*$"
+ "^(?i)\\w+ your photo\\.$"
+ "_sessionCacheTTL"
+ "gmsCallCount"
+ "initWithDomain:code:userInfo:"
+ "inputChunkCount"
+ "overestimatedTruncatedInputTokensCount"
+ "retryCount"
+ "sessionCache"
+ "shouldCacheSession"
- "Returning prewarmed session from cache for [requestIdentifier: %!{(MISSING)public}s, useCaseIdentifier: %!{(MISSING)public}s, clientApplicationIdentifier: %!{(MISSING)public}s, clientProcessIdentifier: %!{(MISSING)public}d]"
- "_isCombinedSafetyAdapterEnabled"
- "_safetyRejectionPlaceHolder"
- "isCombinedSafetyAdapterEnabled"
- "prewarmedSessions"

```
