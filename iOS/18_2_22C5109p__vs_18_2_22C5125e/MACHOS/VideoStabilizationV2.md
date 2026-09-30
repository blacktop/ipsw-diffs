## VideoStabilizationV2

> `/System/Library/VideoProcessors/VideoStabilizationV2.bundle/VideoStabilizationV2`

```diff

-587.60.6.0.0
-  __TEXT.__text: 0x56e9c
-  __TEXT.__auth_stubs: 0xcd0
-  __TEXT.__objc_stubs: 0x2f20
-  __TEXT.__objc_methlist: 0x10b8
-  __TEXT.__objc_classname: 0x1d5
-  __TEXT.__objc_methname: 0x5033
+587.60.10.122.3
+  __TEXT.__text: 0x5739c
+  __TEXT.__auth_stubs: 0xcf0
+  __TEXT.__objc_stubs: 0x2f40
+  __TEXT.__objc_methlist: 0x10c8
+  __TEXT.__objc_classname: 0x1d4
+  __TEXT.__objc_methname: 0x5058
   __TEXT.__objc_methtype: 0x14ae
   __TEXT.__const: 0x690
-  __TEXT.__oslogstring: 0xcc23
-  __TEXT.__cstring: 0x8d93
+  __TEXT.__oslogstring: 0xcd90
+  __TEXT.__cstring: 0x8ddf
   __TEXT.__gcc_except_tab: 0x494
-  __TEXT.__unwind_info: 0x538
-  __DATA_CONST.__auth_got: 0x678
+  __TEXT.__unwind_info: 0x540
+  __DATA_CONST.__auth_got: 0x688
   __DATA_CONST.__got: 0x730
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x238

   __DATA_CONST.__objc_arraydata: 0x2718
   __DATA_CONST.__objc_dictobj: 0x960
   __DATA_CONST.__objc_arrayobj: 0x1680
-  __DATA.__objc_const: 0x4ce0
-  __DATA.__objc_selrefs: 0xe00
-  __DATA.__objc_ivar: 0x430
+  __DATA.__objc_const: 0x4d28
+  __DATA.__objc_selrefs: 0xe08
+  __DATA.__objc_ivar: 0x434
   __DATA.__objc_data: 0x460
   __DATA.__data: 0x300
   __DATA.__common: 0x60

   - /System/Library/PrivateFrameworks/CMImaging.framework/CMImaging
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 514
-  Symbols:   1798
-  CStrings:  2640
+  Functions: 516
+  Symbols:   1805
+  CStrings:  2646
 
Symbols:
+ -[VISProcessorV2 willStartProcessingBuffer:withStatus:]
+ OBJC_IVAR_$_VISProcessorV2._shouldCallStartProcessingBufferDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_VISWrapperDelegate
+ __sampleBufferImagePreStabilizationCallback
+ _objc_msgSend$willStartProcessingBuffer:withStatus:
+ _objc_opt_respondsToSelector
+ _objc_retainAutoreleasedReturnValue
+ _sbp_gvs_setPostOutputCallback
- _sbp_gvs_setOutputCallback
CStrings:
+ "\x014"
+ "!"
+ "<<<< GyroVideoStabilizationV2 >>>> %!s(MISSING): Notify - inputSampleBuffer = %!p(MISSING), inputPixelBuffer = %!p(MISSING) - status = %!d(MISSING)"
+ "<<<< GyroVideoStabilizationV2 >>>> %!s(MISSING): Pre-Stabilization callback entry - refconf = %!p(MISSING), status = %!d(MISSING), inputSampleBuffer = %!p(MISSING), inputPixelBuffer = %!p(MISSING)"
+ "<<<< GyroVideoStabilizationV2 >>>> %!s(MISSING): Unable to set pre-video stabilization sample buffer processor callback"
+ "_sampleBufferImagePreStabilizationCallback"
+ "_shouldCallStartProcessingBufferDelegate"
+ "sbp_gvs_setPostOutputCallback"
+ "sbp_gvs_setPreOutputCallback"
+ "willStartProcessingBuffer:withStatus:"
- "\x01\x13\x11"
- "T@\"<VISProcessorDelegate>\",W,N,V_delegate"
- "sbp_gvs_setOutputCallback"

```
