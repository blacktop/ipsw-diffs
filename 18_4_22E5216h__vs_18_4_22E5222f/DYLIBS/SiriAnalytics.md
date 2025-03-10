## SiriAnalytics

> `/System/Library/PrivateFrameworks/SiriAnalytics.framework/SiriAnalytics`

```diff

-3404.70.1.0.0
-  __TEXT.__text: 0xbdf44
+3404.73.1.0.0
+  __TEXT.__text: 0xbd850
   __TEXT.__auth_stubs: 0x24e0
-  __TEXT.__objc_methlist: 0x2230
+  __TEXT.__objc_methlist: 0x2208
   __TEXT.__const: 0x6170
-  __TEXT.__cstring: 0xa160
+  __TEXT.__cstring: 0xa0c0
   __TEXT.__constg_swiftt: 0x3014
   __TEXT.__swift5_typeref: 0x2725
   __TEXT.__swift5_builtin: 0x17c

   __TEXT.__swift5_protos: 0x60
   __TEXT.__swift5_mpenum: 0x70
   __TEXT.__swift5_capture: 0x76c
-  __TEXT.__oslogstring: 0x10d6
-  __TEXT.__gcc_except_tab: 0x3cc
-  __TEXT.__unwind_info: 0x3840
+  __TEXT.__oslogstring: 0x1116
+  __TEXT.__gcc_except_tab: 0x3bc
+  __TEXT.__unwind_info: 0x3820
   __TEXT.__eh_frame: 0x5698
   __TEXT.__objc_classname: 0x5ed
-  __TEXT.__objc_methname: 0x50e7
-  __TEXT.__objc_methtype: 0x128b
-  __TEXT.__objc_stubs: 0x34c0
+  __TEXT.__objc_methname: 0x4fff
+  __TEXT.__objc_methtype: 0x1255
+  __TEXT.__objc_stubs: 0x33e0
   __DATA_CONST.__got: 0x770
-  __DATA_CONST.__const: 0x1070
+  __DATA_CONST.__const: 0x1020
   __DATA_CONST.__objc_classlist: 0x2e8
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0xe8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x14f8
+  __DATA_CONST.__objc_selrefs: 0x14c8
   __DATA_CONST.__objc_protorefs: 0x68
   __DATA_CONST.__objc_superrefs: 0xf0
   __AUTH_CONST.__auth_got: 0x1280
-  __AUTH_CONST.__auth_ptr: 0xa68
+  __AUTH_CONST.__auth_ptr: 0xc40
   __AUTH_CONST.__const: 0x5390
   __AUTH_CONST.__cfstring: 0x1c60
-  __AUTH_CONST.__objc_const: 0x60f8
+  __AUTH_CONST.__objc_const: 0x60d8
   __AUTH.__objc_data: 0x370
   __AUTH.__data: 0x6d8
-  __DATA.__objc_ivar: 0x22c
+  __DATA.__objc_ivar: 0x228
   __DATA.__data: 0x1ec0
   __DATA.__common: 0x110
   __DATA.__bss: 0x5990

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 5161
-  Symbols:   2352
-  CStrings:  2230
+  Functions: 5155
+  Symbols:   2346
+  CStrings:  2222
 
CStrings:
+ "%s Remote message resolution not available."
+ "%s Resolver: %@ did not resolve message: %@, dropping."
+ "%s Resolver: %@ resolved message: %@"
+ "%s Using resolver: %@ for message: %@"
+ "-[SiriAnalyticsMessageResolutionPipeline resolveMessage:completion:]"
+ "-[SiriAnalyticsMessageResolutionPipeline resolveMessage:completion:]_block_invoke"
+ "-[SiriAnalyticsXPCConnectionHandler resolveMessages:completion:]"
+ "_messageResolution"
+ "initWithInternalTelemetry:sensitiveConditionsObservers:messageResolution:preprocessor:metastore:scheduler:dataPolicyObserver:"
+ "resolveAndEmitMessage:isolatedStreamUUID:"
+ "v32@?0@\"<SiriAnalyticsMessageResolver>\"8Q16^B24"
- "%s Message resolver: %@ timed out after %lu seconds and failed to resolve message: %@"
- "%s Resolved message: %@"
- "-[SiriAnalyticsMessageResolutionPipeline _continueResolutionWithMessage:resolvers:currentResolverIndex:resolversApplied:completion:]"
- "-[SiriAnalyticsMessageResolutionPipeline _continueResolutionWithMessage:resolvers:currentResolverIndex:resolversApplied:completion:]_block_invoke_2"
- "-[SiriAnalyticsMessageResolutionPipeline resolveMessage:timestamp:completion:]_block_invoke"
- "@\"NSMutableArray\""
- "@24@0:8@?16"
- "_clientMessageStream"
- "_continueResolutionWithMessage:resolvers:currentResolverIndex:resolversApplied:completion:"
- "_discardResolutionTimer:"
- "_resolutionTimers"
- "_startResolutionTimerWithElapsed:"
- "handler:unresolvedMessagesReceived:"
- "initWithInternalTelemetry:sensitiveConditionsObservers:clientMessageStream:preprocessor:metastore:scheduler:dataPolicyObserver:"
- "objectAtIndex:"
- "removeObject:"
- "resolveMessage:timestamp:completion:"
- "v32@?0@\"SiriAnalyticsTimeAnnotatedMessage\"8Q16^B24"
- "v56@0:8@16@24Q32Q40@?48"

```
