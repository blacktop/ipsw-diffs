## MetricMeasurement

> `/System/Library/PrivateFrameworks/MetricMeasurement.framework/MetricMeasurement`

```diff

-294.0.2.0.0
-  __TEXT.__text: 0x1b270
+294.40.2.0.0
+  __TEXT.__text: 0x1b74c
   __TEXT.__auth_stubs: 0x8a0
-  __TEXT.__objc_methlist: 0x26fc
+  __TEXT.__objc_methlist: 0x2744
   __TEXT.__const: 0x268
-  __TEXT.__cstring: 0x2255
+  __TEXT.__cstring: 0x236f
   __TEXT.__gcc_except_tab: 0x5b4
   __TEXT.__oslogstring: 0x77e
   __TEXT.__ustring: 0x34
-  __TEXT.__unwind_info: 0x8f8
+  __TEXT.__unwind_info: 0x900
   __TEXT.__objc_classname: 0x594
-  __TEXT.__objc_methname: 0x471e
+  __TEXT.__objc_methname: 0x4846
   __TEXT.__objc_methtype: 0xfe9
-  __TEXT.__objc_stubs: 0x3dc0
+  __TEXT.__objc_stubs: 0x3f80
   __DATA_CONST.__got: 0x270
-  __DATA_CONST.__const: 0x5d0
+  __DATA_CONST.__const: 0x5f8
   __DATA_CONST.__objc_classlist: 0x160
   __DATA_CONST.__objc_nlclslist: 0x8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1448
+  __DATA_CONST.__objc_selrefs: 0x14b8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x100
   __AUTH_CONST.__auth_got: 0x460
   __AUTH_CONST.__const: 0x140
-  __AUTH_CONST.__cfstring: 0x2380
-  __AUTH_CONST.__objc_const: 0x5678
+  __AUTH_CONST.__cfstring: 0x2440
+  __AUTH_CONST.__objc_const: 0x56d8
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH.__objc_data: 0xcd0
   __DATA.__objc_ivar: 0x16c

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpmsample.dylib
   - /usr/lib/libsysmon.dylib
-  UUID: 12D6ACE4-7A48-3D81-96D9-5BBD07958353
-  Functions: 816
-  Symbols:   3078
-  CStrings:  1754
+  UUID: 43CC2767-FDDA-3E0A-B351-7013EAD75EA6
+  Functions: 824
+  Symbols:   3109
+  CStrings:  1781
 
Symbols:
+ +[MXMOSSignpostSampleTag animationGPUTimeP90]
+ +[MXMOSSignpostSampleTag animationNumberOfOffscreenPassesP90]
+ +[MXMOSSignpostSampleTag animationRenderGPUTimeP90]
+ +[MXMOSSignpostSampleTag animationRenderTimeP90]
+ +[MXMOSSignpostSampleTag animationUpdateTimeP90]
+ +[MXMUnitFrame passes]
+ -[MXMOSSignpostProbe _addAnimationRenderStatsToData:fromSignpostAnimationInterval:]
+ GCC_except_table33
+ GCC_except_table49
+ GCC_except_table51
+ ___83-[MXMOSSignpostProbe _addAnimationRenderStatsToData:fromSignpostAnimationInterval:]_block_invoke
+ ___block_descriptor_56_e8_32s40s48s_e73_v32?0"MXMOSSignpostSampleTag"8"NSUnit"16"SignpostSupportValueStats"24ls32l8s40l8s48l8
+ _objc_msgSend$_addAnimationRenderStatsToData:fromSignpostAnimationInterval:
+ _objc_msgSend$animationGPUTimeP90
+ _objc_msgSend$animationNumberOfOffscreenPassesP90
+ _objc_msgSend$animationRenderGPUTimeP90
+ _objc_msgSend$animationRenderTimeP90
+ _objc_msgSend$animationUpdateTimeP90
+ _objc_msgSend$frameStatisticsForDisplayID:
+ _objc_msgSend$gpuTime
+ _objc_msgSend$offscreenPassCount
+ _objc_msgSend$p90
+ _objc_msgSend$passes
+ _objc_msgSend$renderAndGPUTime
+ _objc_msgSend$renderTime
+ _objc_msgSend$updateTime
- GCC_except_table28
- GCC_except_table44
CStrings:
+ "_addAnimationRenderStatsToData:fromSignpostAnimationInterval:"
+ "animationGPUTimeP90"
+ "animationNumberOfOffscreenPassesP90"
+ "animationRenderGPUTimeP90"
+ "animationRenderTimeP90"
+ "animationUpdateTimeP90"
+ "frameStatisticsForDisplayID:"
+ "gpuTime"
+ "offscreenPassCount"
+ "os_signpost.animation.gpu.time.p90"
+ "os_signpost.animation.offscreen_pass.number.p90"
+ "os_signpost.animation.render.time.p90"
+ "os_signpost.animation.render_gpu.time.p90"
+ "os_signpost.animation.update.time.p90"
+ "p90"
+ "passes"
+ "renderAndGPUTime"
+ "renderTime"
+ "updateTime"
+ "v32@?0@\"MXMOSSignpostSampleTag\"8@\"NSUnit\"16@\"SignpostSupportValueStats\"24"

```
