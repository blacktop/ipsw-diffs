## PhotosUIEdit

> `/System/Library/PrivateFrameworks/PhotosUIEdit.framework/PhotosUIEdit`

```diff

-916.45.110.0.0
-  __TEXT.__text: 0xdb72c
-  __TEXT.__objc_methlist: 0x49bc
-  __TEXT.__const: 0x7778
-  __TEXT.__swift5_typeref: 0x13140
+916.51.202.0.0
+  __TEXT.__text: 0xdc024
+  __TEXT.__objc_methlist: 0x49fc
+  __TEXT.__const: 0x7798
+  __TEXT.__swift5_typeref: 0x13148
   __TEXT.__constg_swiftt: 0x311c
   __TEXT.__swift5_reflstr: 0x287b
   __TEXT.__swift5_assocty: 0x680
   __TEXT.__swift5_fieldmd: 0x21d0
   __TEXT.__swift5_builtin: 0x140
-  __TEXT.__swift5_proto: 0x254
+  __TEXT.__swift5_proto: 0x258
   __TEXT.__swift5_types: 0x1e4
-  __TEXT.__cstring: 0x6037
+  __TEXT.__cstring: 0x60ac
   __TEXT.__swift5_capture: 0x1168
   __TEXT.__swift_as_entry: 0x6c
   __TEXT.__swift_as_ret: 0x90
   __TEXT.__swift_as_cont: 0x154
-  __TEXT.__oslogstring: 0x4333
+  __TEXT.__oslogstring: 0x438d
   __TEXT.__swift5_mpenum: 0x28
   __TEXT.__swift5_protos: 0x14
-  __TEXT.__gcc_except_tab: 0x678
-  __TEXT.__unwind_info: 0x50e0
-  __TEXT.__eh_frame: 0x2b34
+  __TEXT.__gcc_except_tab: 0x690
+  __TEXT.__unwind_info: 0x5118
+  __TEXT.__eh_frame: 0x2b64
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x21c0
+  __DATA_CONST.__const: 0x21e8
   __DATA_CONST.__objc_classlist: 0x3d0
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0xb8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3d48
+  __DATA_CONST.__objc_selrefs: 0x3d78
   __DATA_CONST.__objc_protorefs: 0x40
   __DATA_CONST.__objc_superrefs: 0x188
   __DATA_CONST.__objc_arraydata: 0x70
-  __DATA_CONST.__got: 0x1650
+  __DATA_CONST.__got: 0x1658
   __AUTH_CONST.__const: 0x5820
-  __AUTH_CONST.__cfstring: 0x3e40
-  __AUTH_CONST.__objc_const: 0xabc8
+  __AUTH_CONST.__cfstring: 0x3ee0
+  __AUTH_CONST.__objc_const: 0xac58
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__auth_got: 0x2408
   __AUTH.__objc_data: 0x8b8
   __AUTH.__data: 0xc18
-  __DATA.__objc_ivar: 0x4d4
-  __DATA.__data: 0x2890
+  __DATA.__objc_ivar: 0x4e4
+  __DATA.__data: 0x2898
   __DATA.__objc_stublist: 0x8
   __DATA.__common: 0x50
   __DATA_DIRTY.__objc_data: 0x24b8

   - /System/Library/PrivateFrameworks/PhotosEditing.framework/PhotosEditing
   - /System/Library/PrivateFrameworks/PhotosFormats.framework/PhotosFormats
   - /System/Library/PrivateFrameworks/PhotosGenerativeServices.framework/PhotosGenerativeServices
+  - /System/Library/PrivateFrameworks/PhotosRendering.framework/PhotosRendering
   - /System/Library/PrivateFrameworks/PhotosSpatialMediaCore.framework/PhotosSpatialMediaCore
   - /System/Library/PrivateFrameworks/PhotosSpatialMediaEditing.framework/PhotosSpatialMediaEditing
   - /System/Library/PrivateFrameworks/PhotosSwiftUICore.framework/PhotosSwiftUICore

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 7036
-  Symbols:   4944
-  CStrings:  1130
+  Functions: 7043
+  Symbols:   4957
+  CStrings:  1137
 
Symbols:
+ +[PEAdjustmentPreset _sanitizedCompositionForCompositionController:autoType:]
+ +[PEEditAIToolCompletedEventBuilder sendEventForCleanupTool:requestDuration:result:guardrailReasons:generativeModel:interactionMode:userSelectedInteractionMode:modelResolution:]
+ +[PEEditAIToolCompletedEventBuilder sendEventForTool:requestDuration:result:guardrailReasons:sourceTab:interactionCount:generativeModel:interactionMode:userSelectedInteractionMode:modelResolution:]
+ -[PEAdjustmentPreset _deserializedComposition]
+ -[PEAdjustmentPreset _serializeComposition:autoType:includeSidecar:]
+ -[PEAdjustmentPreset _serializeDeferredComposition]
+ -[PEAdjustmentPreset initWithCompositionControllerDeferringSerialization:asset:]
+ -[PECleanupSegmentAnalyzer ciContext]
+ -[PECleanupSegmentAnalyzer setCiContext:]
+ GCC_except_table1001
+ GCC_except_table1013
+ GCC_except_table1128
+ GCC_except_table1239
+ GCC_except_table1240
+ GCC_except_table1241
+ GCC_except_table1279
+ GCC_except_table1292
+ GCC_except_table402
+ GCC_except_table428
+ GCC_except_table439
+ GCC_except_table459
+ GCC_except_table473
+ GCC_except_table731
+ GCC_except_table753
+ GCC_except_table909
+ GCC_except_table920
+ GCC_except_table928
+ GCC_except_table988
+ GCC_except_table992
+ _OBJC_IVAR_$_PEAdjustmentPreset._deferredAutoType
+ _OBJC_IVAR_$_PEAdjustmentPreset._deferredSerialization
+ _OBJC_IVAR_$_PEAdjustmentPreset._deferredSourceAssetUUID
+ _OBJC_IVAR_$_PECleanupSegmentAnalyzer._ciContext
+ ___80-[PEAdjustmentPreset initWithCompositionControllerDeferringSerialization:asset:]_block_invoke
+ ___block_descriptor_40_e8_32w_e5_v8?0lw32l8
+ _associated conformance 12PhotosUIEdit24CompositionMediaProvider33_6B0A8C9A6CD579A51EF3C64FC30C5F82LLC0A7Editing0aD9ProvidingAA11Observation10Observable
+ _kCIContextName
- +[PEEditAIToolCompletedEventBuilder sendEventForCleanupTool:requestDuration:result:guardrailReasons:generativeModel:interactionMode:userSelectedInteractionMode:]
- +[PEEditAIToolCompletedEventBuilder sendEventForTool:requestDuration:result:guardrailReasons:sourceTab:interactionCount:generativeModel:interactionMode:userSelectedInteractionMode:]
- -[PEAdjustmentPreset _serializeCompositionController:includeSidecar:]
- GCC_except_table1006
- GCC_except_table1121
- GCC_except_table1232
- GCC_except_table1233
- GCC_except_table1234
- GCC_except_table1272
- GCC_except_table1285
- GCC_except_table423
- GCC_except_table434
- GCC_except_table454
- GCC_except_table468
- GCC_except_table724
- GCC_except_table746
- GCC_except_table902
- GCC_except_table913
- GCC_except_table921
- GCC_except_table971
- GCC_except_table981
- GCC_except_table987
- _OUTLINED_FUNCTION_280
- _OUTLINED_FUNCTION_281
CStrings:
+ "PEAdjustmentPreset failed to serialize deferred composition, keeping it in memory"
+ "PECleanupSegmentAnalyzer"
+ "PENoUpsellRateLimitErrorMessage"
+ "PESerializationUtility sidecar data could not be loaded: %{public}@"
+ "composition"
+ "isEditAIEligible"
+ "modelResolution"
+ "outAutoType"
- "PESerializationUtility sidecar data could not be loaded: %@"
```
