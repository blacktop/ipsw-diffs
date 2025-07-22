## FramePacing

> `/System/Library/PrivateFrameworks/FramePacing.framework/FramePacing`

```diff

-4.0.19.0.0
-  __TEXT.__text: 0x5c8c
+4.0.22.0.0
+  __TEXT.__text: 0x5cb4
   __TEXT.__auth_stubs: 0x410
   __TEXT.__objc_methlist: 0x180
   __TEXT.__const: 0x110
-  __TEXT.__cstring: 0x27e
-  __TEXT.__oslogstring: 0x39cb
+  __TEXT.__cstring: 0x2cd
+  __TEXT.__oslogstring: 0x39f9
   __TEXT.__unwind_info: 0x1a8
   __TEXT.__objc_classname: 0x89
   __TEXT.__objc_methname: 0x7bd

   __DATA_CONST.__objc_superrefs: 0x20
   __AUTH_CONST.__auth_got: 0x210
   __AUTH_CONST.__const: 0x320
-  __AUTH_CONST.__cfstring: 0xa0
+  __AUTH_CONST.__cfstring: 0xc0
   __AUTH_CONST.__objc_const: 0xb60
   __DATA.__objc_ivar: 0xe8
   __DATA.__data: 0x18

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: AE69DAEC-29BA-389A-8942-303440A5B8BF
+  UUID: 9C9A5DBD-8E71-3B0F-BF6A-CC8DB0C9DFED
   Functions: 132
   Symbols:   510
-  CStrings:  225
+  CStrings:  228
 
Symbols:
+ _.str.93
+ ___block_literal_global.144
+ ___block_literal_global.150
+ ___block_literal_global.152
+ ___block_literal_global.28
+ ___block_literal_global.31
+ ___block_literal_global.50
+ ___block_literal_global.69
+ ___block_literal_global.78
+ ___block_literal_global.90
- _.str.89
- ___block_literal_global.140
- ___block_literal_global.142
- ___block_literal_global.148
- ___block_literal_global.24
- ___block_literal_global.27
- ___block_literal_global.46
- ___block_literal_global.65
- ___block_literal_global.74
- ___block_literal_global.86
Functions:
~ ____FPCheckEnvironmentVariablesAndDefaultsForConfiguration_block_invoke : 1524 -> 1580
~ ___142+[FPCAMetalLayerState drawableLifetimeEnd:imageQueueID:drawableID:drawableFinishedTime:wasPresented:targetCPUDeadline:targetPresentationTime:]_block_invoke : 3044 -> 3028
CStrings:
+ "METAL_PERFORMANCE_PER_FRAME_SIGNPOSTS"
+ "MetalPerformancePerFrameSignpostsEnabled"
+ "Signpost ID is CAMetalLayer ID\nCommand Buffer Count = %{public, name=command_buffer_count}u\nIn-Flight Total End-to-end = %{public, name=inflight_end_to_end_total_ms}.3fms\nIn-Flight CPU End-to-end = %{public, name=inflight_end_to_end_cpu_ms}.3fms\nIn-Flight GPU End-to-end = %{public, name=inflight_end_to_end_gpu_ms}.3fms\nTotal On-GPU Time = %{public, name=inflight_on_gpu_ms}.3fms\nWait to land on glass = %{public, name=inflight_wait_for_glass_ms}.3fms\nDrawable ID = %{public, name=drawable_id}#llx\n%{public, signpost.description:begin_time}llu %{public, signpost.description:end_time}llu"
- "Signpost ID is CAMetalLayer ID\nCommand Buffer Count = %{public, name=command_buffer_count}u\nIn-Flight Total End-to-end = %{public, name=inflight_end_to_end_total_ms}.3fms\nIn-Flight CPU End-to-end = %{public, name=inflight_end_to_end_cpu_ms}.3fms\nIn-Flight GPU End-to-end = %{public, name=inflight_end_to_end_gpu_ms}.3fms\nTotal On-GPU Time = %{public, name=inflight_on_gpu_ms}.3fms\nWait to land on glass = %{public, name=inflight_wait_for_glass_ms}.3fms\n%{public, signpost.description:begin_time}llu %{public, signpost.description:end_time}llu"

```
