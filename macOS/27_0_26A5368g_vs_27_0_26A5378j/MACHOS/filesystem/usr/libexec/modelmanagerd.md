## modelmanagerd

> `/usr/libexec/modelmanagerd`

```diff

-  __TEXT.__text: 0x1a95dc
-  __TEXT.__auth_stubs: 0x39d0
+  __TEXT.__text: 0x1afd64
+  __TEXT.__auth_stubs: 0x3a20
   __TEXT.__objc_stubs: 0x700
   __TEXT.__objc_methlist: 0x1c0
   __TEXT.__const: 0x6676
   __TEXT.__swift5_typeref: 0x2867
-  __TEXT.__cstring: 0x1de0
-  __TEXT.__oslogstring: 0x94e9
-  __TEXT.__swift5_capture: 0x21b4
+  __TEXT.__cstring: 0x1e50
+  __TEXT.__oslogstring: 0x9709
+  __TEXT.__swift5_capture: 0x23b4
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0x2d3c
+  __TEXT.__constg_swiftt: 0x2d5c
   __TEXT.__swift5_builtin: 0x3c
-  __TEXT.__swift5_reflstr: 0x2543
-  __TEXT.__swift5_fieldmd: 0x2184
+  __TEXT.__swift5_reflstr: 0x25e3
+  __TEXT.__swift5_fieldmd: 0x21b4
   __TEXT.__swift5_types: 0x1d0
   __TEXT.__objc_classname: 0xb90
   __TEXT.__objc_methname: 0x1923
   __TEXT.__objc_methtype: 0x395
-  __TEXT.__swift_as_entry: 0x910
-  __TEXT.__swift_as_ret: 0xa70
+  __TEXT.__swift_as_entry: 0x918
+  __TEXT.__swift_as_ret: 0xa7c
   __TEXT.__swift_as_cont: 0x1168
   __TEXT.__swift5_proto: 0x314
   __TEXT.__swift5_protos: 0x94
   __TEXT.__swift5_assocty: 0x1b8
-  __TEXT.__unwind_info: 0x6520
-  __TEXT.__eh_frame: 0x15534
-  __DATA_CONST.__const: 0x7948
+  __TEXT.__unwind_info: 0x65f8
+  __TEXT.__eh_frame: 0x156f4
+  __DATA_CONST.__const: 0x7f78
   __DATA_CONST.__objc_classlist: 0x1c0
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x38
-  __DATA_CONST.__auth_got: 0x1cf0
-  __DATA_CONST.__got: 0xf10
+  __DATA_CONST.__auth_got: 0x1d18
+  __DATA_CONST.__got: 0xf08
   __DATA_CONST.__auth_ptr: 0xd30
   __DATA.__objc_const: 0x43c8
   __DATA.__objc_selrefs: 0x2a0
   __DATA.__objc_data: 0x700
-  __DATA.__data: 0x6308
-  __DATA.__common: 0x5d0
+  __DATA.__data: 0x6348
+  __DATA.__common: 0x618
   __DATA.__bss: 0x52c0
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices

   - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 8782
-  Symbols:   1616
-  CStrings:  1163
+  Functions: 8926
+  Symbols:   1620
+  CStrings:  1173
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__const : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__swift5_entry : content changed
~ __TEXT.__swift5_builtin : content changed
~ __TEXT.__swift5_types : content changed
~ __TEXT.__swift_as_cont : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift5_protos : content changed
~ __TEXT.__swift5_assocty : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__auth_ptr : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_selrefs : content changed
~ __DATA.__objc_data : content changed
~ __DATA.__bss : content changed
Symbols:
+ _$s20ModelManagerServices16RemoteIPCRequestO07ExecuteD16StreamingRequestV17useCaseIdentifierSSSgvg
+ _$s20ModelManagerServices16RemoteIPCRequestO07ExecuteD7RequestV17useCaseIdentifierSSSgvg
+ _$ss15ContinuousClockV3nowAB7InstantVvg
+ _$ss15ContinuousClockV7InstantV8duration2tos8DurationVAD_tF
+ _$ss15ContinuousClockVABycfC
+ _$ss8DurationV11descriptionSSvg
- _swift_runtimeSupportsNoncopyableTypes
- _swift_willThrowTypedImpl
CStrings:
+ "Aborting in-flight unload of re-acquired asset %s before dispatch"
+ "Created session %s on behalf of pid %d with priority %s, task priority %s"
+ "EchoFullBudgetBundleID"
+ "EchoFullBudgetSecondInstanceBundleID"
+ "Foreground group %s is blocked behind background slot-holder %s; preempting its requests %s"
+ "HostFullBudgetBundleID"
+ "Prewarm request %s: task priority %s, process priority %s"
+ "Skipping foreground asset claim for session %s: bundle not yet resolved"
+ "Skipping full prewarm for session %s: already prewarmed and all assets loaded"
+ "Skipping prewarmBundle for session %s: already prewarmed and assets are loaded"
+ "prewarmBundle completed for session %s in %s"
- "Created session %s on behalf of pid %d with priority %s"

```
