## CMImaging

> `/System/Library/PrivateFrameworks/CMImaging.framework/CMImaging`

```diff

-  __TEXT.__text: 0x1dd8a4
-  __TEXT.__objc_methlist: 0xd31c
+  __TEXT.__text: 0x1da208
+  __TEXT.__objc_methlist: 0xd3bc
   __TEXT.__const: 0x2e40
-  __TEXT.__oslogstring: 0x1526c
-  __TEXT.__cstring: 0x28ae8
+  __TEXT.__oslogstring: 0x1551e
+  __TEXT.__cstring: 0x28b23
   __TEXT.__gcc_except_tab: 0x154c
-  __TEXT.__unwind_info: 0x31d0
-  __TEXT.__eh_frame: 0x6a0
+  __TEXT.__unwind_info: 0x31e0
+  __TEXT.__eh_frame: 0x6e8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x1b0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6218
+  __DATA_CONST.__objc_selrefs: 0x6240
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x4c8
   __DATA_CONST.__objc_arraydata: 0x410
-  __DATA_CONST.__got: 0xc00
+  __DATA_CONST.__got: 0xc48
   __AUTH_CONST.__const: 0x810
-  __AUTH_CONST.__cfstring: 0x6bc0
-  __AUTH_CONST.__objc_const: 0x1f050
+  __AUTH_CONST.__cfstring: 0x6be0
+  __AUTH_CONST.__objc_const: 0x1f118
   __AUTH_CONST.__objc_intobj: 0xba0
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_doubleobj: 0x1130
-  __AUTH_CONST.__auth_got: 0xbf0
-  __AUTH.__objc_data: 0x1e0
+  __AUTH_CONST.__auth_got: 0xc00
   __AUTH.__data: 0x8
-  __DATA.__objc_ivar: 0x17c4
-  __DATA.__data: 0x12d88
-  __DATA.__common: 0x1d0
-  __DATA.__bss: 0x80
-  __DATA_DIRTY.__objc_data: 0x39d0
-  __DATA_DIRTY.__data: 0x8
+  __DATA.__objc_ivar: 0x17d4
+  __DATA.__data: 0x12d90
+  __DATA.__common: 0x1e0
+  __DATA.__bss: 0x70
+  __DATA_DIRTY.__objc_data: 0x3bb0
   __DATA_DIRTY.__common: 0x1b0
-  __DATA_DIRTY.__bss: 0x1d8
+  __DATA_DIRTY.__bss: 0x1e8
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 7581
-  Symbols:   21848
-  CStrings:  6147
+  Functions: 7597
+  Symbols:   21897
+  CStrings:  6155
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH_CONST.__objc_doubleobj : content changed
~ __AUTH.__data : content changed
Symbols:
+ +[CMITIPConfig initialize]
+ -[CMIInferenceExecutionStreamBypass setANEExecutionPriority:]
+ -[CMIInferenceExecutionStreamEspressoV1 aneExecutionPriority]
+ -[CMIInferenceExecutionStreamEspressoV1 setANEExecutionPriority:]
+ -[CMIInferenceExecutionStreamEspressoV1 setAneExecutionPriority:]
+ -[CMIInferenceExecutionStreamEspressoV2 aneExecutionPriority]
+ -[CMIInferenceExecutionStreamEspressoV2 setANEExecutionPriority:]
+ -[CMIInferenceExecutionStreamEspressoV2 setAneExecutionPriority:]
+ -[CMITIPConfig aneExecutionPriorityOverride]
+ -[CMITIPConfig setAneExecutionPriorityOverride:]
+ -[CMITiledInferenceProcessorConfig aneExecutionPriority]
+ -[CMITiledInferenceProcessorConfig setAneExecutionPriority:]
+ GCC_except_table70
+ GCC_except_table93
+ GCC_except_table94
+ _OBJC_IVAR_$_CMIInferenceExecutionStreamEspressoV1._aneExecutionPriority
+ _OBJC_IVAR_$_CMIInferenceExecutionStreamEspressoV2._aneExecutionPriority
+ _OBJC_IVAR_$_CMITIPConfig._aneExecutionPriorityOverride
+ _OBJC_IVAR_$_CMITiledInferenceProcessorConfig._aneExecutionPriority
+ _e5rt_execution_stream_set_ane_execution_priority
+ _espresso_plan_set_priority
+ _gCMITIPConfig
+ _objc_msgSend$aneExecutionPriority
+ _objc_msgSend$aneExecutionPriorityOverride
+ _objc_msgSend$parentNetwork
+ _objc_msgSend$plan
+ _objc_msgSend$setANEExecutionPriority:
+ _objc_msgSend$setAneExecutionPriorityOverride:
- GCC_except_table79
- GCC_except_table89
- GCC_except_table92
CStrings:
+ "-[CMIInferenceExecutionStreamEspressoV1 submitAsyncWithCompletionHandler:]"
+ "<<<< CMISmartStyleUtilitiesV1 >>>> %s: Could not load default biases for cast type %@"
+ "<<<< CMISmartStyleUtilitiesV1 >>>> %s: [SmartStyles] Error: Failed to load %s.plist - falling back to compiled-in version"
+ "<<<< CMITIP >>>> %s: Warning! CMITiledInferenceProcessor is configured with CMIInferenceANEExecutionPriorityHigh — this maps to ANE HW band 2 which should be reserved for streaming inferences. CMITiledInferenceProcessor is used for stills processing and running at high ANE priority will conflict with concurrent streaming inference workloads on the ANE."
+ "<<<< CMITIP >>>> %s: e5rt_execution_stream_set_ane_execution_priority failed, %s."
+ "<<<< CMITIP >>>> %s: e5rt_execution_stream_submit_async_with_timeout failed %s."
+ "<<<< CMITIP >>>> %s: espresso_plan_set_priority failed (%d)"
+ "<<<< CMITIP >>>> %s: setANEExecutionPriority failed (err:%d)"
+ "<<<< CMITIPConfig >>>> %s: CMITIPConfig aneExecutionPriorityOverride:  %lu"
+ "<<<< CMITIPConfig >>>> %s: CMITIPConfig aneSubmitTimeoutMs:            %llu"
+ "<<<< CMITIPConfig >>>> %s: CMITIPConfig shareIntermediates:            %d"
+ "_loadDefaultUserBiasByCastType"
+ "cmitipconfig_trace"
- "+[CMISmartStyleUtilitiesV1 defaultStyleForCastType:]_block_invoke"
- "<<<< CMISmartStyleUtilitiesV1 >>>> %s: Invalid cast type %@"
- "<<<< CMISmartStyleUtilitiesV1 >>>> %s: [SmartStyles] Error: Failed to load RendererTuning.plist - falling back to compiled in version"
- "<<<< CMITIP >>>> %s: CMITIPConfig aneSubmitTimeoutMs:    %llu"
- "<<<< CMITIP >>>> %s: CMITIPConfig shareIntermediates:    %d"
- "<<<< CMITIP >>>> %s: e5rt_execution_stream_execute_sync failed %s."

```
