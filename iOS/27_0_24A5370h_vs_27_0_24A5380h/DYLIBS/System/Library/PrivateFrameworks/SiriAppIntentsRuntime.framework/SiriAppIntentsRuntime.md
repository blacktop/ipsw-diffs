## SiriAppIntentsRuntime

> `/System/Library/PrivateFrameworks/SiriAppIntentsRuntime.framework/SiriAppIntentsRuntime`

```diff

-  __TEXT.__text: 0x7982c
+  __TEXT.__text: 0x7c728
   __TEXT.__objc_methlist: 0x3e8
-  __TEXT.__const: 0x26e8
-  __TEXT.__cstring: 0x13d1
-  __TEXT.__constg_swiftt: 0xc24
-  __TEXT.__swift5_typeref: 0x1297
-  __TEXT.__swift5_reflstr: 0xc86
-  __TEXT.__swift5_fieldmd: 0x8d4
-  __TEXT.__oslogstring: 0x305d
+  __TEXT.__const: 0x2798
+  __TEXT.__cstring: 0x1431
+  __TEXT.__constg_swiftt: 0xc9c
+  __TEXT.__swift5_typeref: 0x12f3
+  __TEXT.__swift5_reflstr: 0xcf6
+  __TEXT.__swift5_fieldmd: 0x940
+  __TEXT.__oslogstring: 0x32dd
   __TEXT.__swift5_builtin: 0x3c
-  __TEXT.__swift5_types: 0xac
+  __TEXT.__swift5_types: 0xb4
   __TEXT.__swift_as_entry: 0x1c0
-  __TEXT.__swift_as_ret: 0x178
-  __TEXT.__swift_as_cont: 0x2e4
-  __TEXT.__swift5_proto: 0x100
-  __TEXT.__swift5_capture: 0x16e8
+  __TEXT.__swift_as_ret: 0x170
+  __TEXT.__swift_as_cont: 0x2cc
+  __TEXT.__swift5_proto: 0x104
+  __TEXT.__swift5_capture: 0x1758
   __TEXT.__swift5_assocty: 0x98
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x19f0
-  __TEXT.__eh_frame: 0x4668
+  __TEXT.__unwind_info: 0x1a10
+  __TEXT.__eh_frame: 0x4670
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x120
-  __DATA_CONST.__objc_classlist: 0x68
+  __DATA_CONST.__const: 0x170
+  __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x430
+  __DATA_CONST.__objc_selrefs: 0x438
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x4288
-  __AUTH_CONST.__objc_const: 0xc18
-  __AUTH_CONST.__auth_got: 0x1840
-  __AUTH.__objc_data: 0xa60
-  __AUTH.__data: 0xba8
-  __DATA.__data: 0xd28
-  __DATA.__bss: 0x1f00
-  __DATA.__common: 0x198
+  __AUTH_CONST.__const: 0x4378
+  __AUTH_CONST.__objc_const: 0xcc8
+  __AUTH_CONST.__auth_got: 0x1888
+  __AUTH.__objc_data: 0xa0
+  __AUTH.__data: 0x570
+  __DATA.__data: 0x7e8
+  __DATA.__bss: 0x1400
+  __DATA.__common: 0x88
+  __DATA_DIRTY.__objc_data: 0x9c0
+  __DATA_DIRTY.__data: 0xd28
+  __DATA_DIRTY.__bss: 0xb80
+  __DATA_DIRTY.__common: 0x110
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/IntelligenceFlowPlannerSupport.framework/IntelligenceFlowPlannerSupport
   - /System/Library/PrivateFrameworks/IntelligenceFlowRuntime.framework/IntelligenceFlowRuntime
   - /System/Library/PrivateFrameworks/IntelligencePlatformLibrary.framework/IntelligencePlatformLibrary
+  - /System/Library/PrivateFrameworks/IntelligencePlatformLibrary_AppleInternal.framework/IntelligencePlatformLibrary_AppleInternal
   - /System/Library/PrivateFrameworks/InternalSwiftProtobuf.framework/InternalSwiftProtobuf
   - /System/Library/PrivateFrameworks/LoggingSupport.framework/LoggingSupport
   - /System/Library/PrivateFrameworks/ProactiveDaemonSupport.framework/ProactiveDaemonSupport

   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
-  - /usr/lib/swift/libswiftRegexBuilder.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2753
-  Symbols:   212
-  CStrings:  320
+  Functions: 2792
+  Symbols:   214
+  CStrings:  330
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__swift5_builtin : content changed
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift5_assocty : content changed
~ __TEXT.__swift5_protos : content changed
~ __TEXT.__swift5_mpenum : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
Symbols:
+ _swift_allocBox
+ _swift_release_x12
+ _swift_task_addCancellationHandler
+ _swift_task_removeCancellationHandler
- _swift_deallocPartialClassInstance
- _swift_isaMask
CStrings:
+ "%{public}s ✅ Connection accepted via code signing fallback (identity verified at resume)"
+ "No matching token-generation request for plannerID: "
+ "SiriAppIntentsDaemon: skipping RemoteXPC listener (customer build)"
+ "SiriAppIntentsDaemon: startup complete kind=summary internalBuild=%{bool}d"
+ "SiriHeliosTokenGenerationReplay"
+ "TokenGeneration stream fetch failed: "
+ "TokenGenerationStreamHandler.fetchEvents: kind=summary plannerID=%s matched=%ld"
+ "TokenGenerationStreamHandler.fetchEvents: kind=summary status=failed plannerID=%s error=%s"
+ "XPCServer: FeatureStore event stream created, beginning live delivery to client"
+ "XPCServer: fetchSessionEvents yielding %ld message(s) for session %s"
+ "XPCServer: startStreaming — creating FeatureStore event stream"
+ "[Replay] No matching token-generation request for plannerID: %s"
+ "[Replay] Stream returned payload (%ld chars) for requestIdentifier: %s"
+ "[Replay] TokenGeneration stream fetch failed: %@"
+ "[Replay] TokenGeneration stream unavailable for plannerID: %s"
+ "[Replay] invalidPlannerID rejected by stream handler: %s"
+ "fetchEvents(plannerID:requestTimestamp:)"
+ "fetchPlannerToolsByType: unrecognised plannerType '%s'"
- "%{public}s Connection rejected: no bundle ID provided"
- "No Execute Request signpost found for plannerID: "
- "[ReplayExport] tgtool not available, skipping replay payload fetch"
- "[Replay] No Execute Request signpost found for plannerID: %s"
- "[Replay] tgtool failed: %@"
- "[Replay] tgtool returned %ld characters for requestIdentifier: %s"
- "kind=parseFailed fetchRawInferenceEventData plannerID=%s outputLen=%ld lineCount=%ld parseFailures=%ld"
- "tgtool replay list failed: "

```
