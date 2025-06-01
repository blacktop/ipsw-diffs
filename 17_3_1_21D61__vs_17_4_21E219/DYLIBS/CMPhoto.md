## CMPhoto

> `/System/Library/PrivateFrameworks/CMPhoto.framework/CMPhoto`

```diff

-252.1.0.0.0
-  __TEXT.__text: 0xdbe70
-  __TEXT.__auth_stubs: 0x2f60
+254.8.0.0.0
+  __TEXT.__text: 0xe1484
+  __TEXT.__auth_stubs: 0x2ff0
   __TEXT.__objc_methlist: 0x390
-  __TEXT.__const: 0xa5d0
-  __TEXT.__cstring: 0x4efe
-  __TEXT.__gcc_except_tab: 0x104
+  __TEXT.__const: 0xbec0
+  __TEXT.__cstring: 0x5010
+  __TEXT.__gcc_except_tab: 0xe4
   __TEXT.__oslogstring: 0x168
-  __TEXT.__unwind_info: 0x18dc
-  __TEXT.__eh_frame: 0x88
+  __TEXT.__unwind_info: 0x18e4
+  __TEXT.__eh_frame: 0x50
   __TEXT.__objc_classname: 0x54
   __TEXT.__objc_methname: 0x1b3f
   __TEXT.__objc_methtype: 0xa63
   __TEXT.__objc_stubs: 0x1b00
-  __DATA_CONST.__got: 0xff0
-  __DATA_CONST.__const: 0x1de0
+  __DATA_CONST.__got: 0xff8
+  __DATA_CONST.__const: 0x1ea0
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0xaa0
   __DATA_CONST.__objc_selrefs: 0x720
+  __DATA_CONST.__objc_classrefs: 0xf8
+  __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__cfstring: 0x4b40
-  __AUTH_CONST.__const: 0x7d8
+  __AUTH_CONST.__cfstring: 0x4d80
+  __AUTH_CONST.__const: 0x7f8
   __AUTH_CONST.__objc_intobj: 0xf0
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_const: 0x48
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH_CONST.__auth_got: 0x17c8
+  __AUTH_CONST.__auth_got: 0x1810
   __AUTH.__objc_data: 0x50
-  __DATA.__objc_classrefs: 0xf8
-  __DATA.__objc_superrefs: 0x20
   __DATA.__objc_ivar: 0x110
-  __DATA.__data: 0x330
+  __DATA.__data: 0x920
   __DATA.__bss: 0x438
   __DATA.__common: 0x40
-  __DATA_DIRTY.__const: 0xa48
+  __DATA_DIRTY.__const: 0xa08
   __DATA_DIRTY.__objc_const: 0x120
   __DATA_DIRTY.__objc_data: 0xf0
-  __DATA_DIRTY.__data: 0x830
+  __DATA_DIRTY.__data: 0x810
   __DATA_DIRTY.__bss: 0x468
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/ColorSync.framework/ColorSync

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 0D551775-68D4-330B-9737-06627851DA14
-  Functions: 2144
-  Symbols:   6348
-  CStrings:  1740
+  UUID: EA7CA3FB-45FC-3BE7-BAE8-2376F457E0EE
+  Functions: 2163
+  Symbols:   6402
+  CStrings:  1785
 
Symbols:
+ GCC_except_table4
+ GCC_except_table8
+ _CFStringCreateWithCString
+ _CGBitmapContextGetData
+ _CGColorSpaceSupportsOutput
+ _CGImageCreateCopyWithColorSpace
+ _CGImageGetAlphaInfo
+ _CGImageGetBitmapInfo
+ _CGImageGetBitsPerComponent
+ _CMPhotoApplyDeltaPixelBuffer
+ _CMPhotoApplyMagmaMap
+ _CMPhotoCompare
+ _CMPhotoCompareCopySupportedMetricList
+ _CMPhotoCompareMethodToStringCopy
+ _CMPhotoComputePSNRHVSForPixelBuffer
+ _CMPhotoCreateDeltaPixelBuffer
+ _CMPhotoCreatePixelBufferFromCGImage
+ _CMPhotoExtensionIsPNG
+ _CMPhotoGetDecodeAccelerationModeOverride
+ _CMPhotoGetEncodeAccelerationModeOverride
+ _JxlDecoderSetParallelRunner
+ _JxlThreadParallelRunner
+ _JxlThreadParallelRunnerCreate
+ _JxlThreadParallelRunnerDestroy
+ _LUT_compand_9b_to_8b_diff
+ _LUT_expand_8b_to_9b_diff
+ _MapMagma
+ __ZNKSt3__16vectorINS_6threadENS_9allocatorIS1_EEE20__throw_length_errorB8ue170006Ev
+ __ZNSt12length_errorC1B8ue170006EPKc
+ __ZNSt3__110unique_ptrINS_15__thread_structENS_14default_deleteIS1_EEE5resetB8ue170006EPS1_
+ __ZNSt3__110unique_ptrINS_5tupleIJNS0_INS_15__thread_structENS_14default_deleteIS2_EEEEZ18EncodeFrameThreadsE3$_0iiiEEENS3_IS7_EEED1B8ue170006Ev
+ __ZNSt3__114__thread_proxyB8ue170006INS_5tupleIJNS_10unique_ptrINS_15__thread_structENS_14default_deleteIS3_EEEEZ18EncodeFrameThreadsE3$_0iiiEEEEEPvS9_
+ __ZNSt3__119__allocate_at_leastB8ue170006INS_9allocatorINS_6threadEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__120__throw_length_errorB8ue170006EPKc
+ __ZNSt3__16vectorINS_6threadENS_9allocatorIS1_EEE11__vallocateB8ue170006Em
+ __ZNSt3__16vectorINS_6threadENS_9allocatorIS1_EEE16__destroy_vectorclB8ue170006Ev
+ __ZSt28__throw_bad_array_new_lengthB8ue170006v
+ ___block_descriptor_tmp.45
+ ___block_descriptor_tmp.47
+ __addHEIFItemIfNeeded
+ __addItemPropertiesIfNeeded
+ __copyAndNormalizeArrayToPixelBuffer
+ __copyAndNormalizePixelBufferToPixelBuffer
+ __findMaxSNRThatMakesSense
+ __getPixelBufferFromCMPhotoImageType
+ __isMobileGestaltVirtualDevice
+ __isProResEncoderAvailable
+ __limitMaxSNR
+ _calc_psnrhvs
+ _csf_cb420
+ _csf_cr420
+ _csf_y
+ _kCMPhotoCompareOption_BlockSize
+ _kCMPhotoCompareOption_BlockStride
+ _kCMPhotoCompareOption_DiffImageType
+ _kCMPhotoCompareOption_HistogramSize
+ _kCMPhotoCompareOption_MonitorDistance
+ _kCMPhotoCompareOption_MonitorResolutionX
+ _kCMPhotoCompareOption_MonitorWidth
+ _kCMPhotoCompareOption_OutputPixelFormat
+ _kCMPhotoCompareOption_UseMagma
+ _kCMPhotoCompareOption_UseMinMaxForDiffMap
+ _kCMPhotoCompareResult_Edges
+ _kCMPhotoCompareResult_FlipWeightedPercentiles
+ _kCMPhotoCompareResult_Histogram
+ _kCMPhotoCompareResult_Max
+ _kCMPhotoCompareResult_Min
+ _kCMPhotoPixelDiffOption_Max
+ _kCMPhotoPixelDiffOption_Min
+ _kCMPhotoPixelDiffOption_Mode
+ _kCMPhotoPixelDiffOutput_Max
+ _kCMPhotoPixelDiffOutput_Min
+ _od_bin_fdct8
+ _od_bin_fdct8x8
- GCC_except_table14
- GCC_except_table15
- GCC_except_table5
- _CMPhotoComputePSNRForPixelBufferWithEdges
- __ZNKSt3__16vectorINS_6threadENS_9allocatorIS1_EEE20__throw_length_errorB7v160006Ev
- __ZNSt12length_errorC1B7v160006EPKc
- __ZNSt3__110unique_ptrINS_15__thread_structENS_14default_deleteIS1_EEE5resetB7v160006EPS1_
- __ZNSt3__110unique_ptrINS_5tupleIJNS0_INS_15__thread_structENS_14default_deleteIS2_EEEEZ18EncodeFrameThreadsE3$_0iiiEEENS3_IS7_EEED1B7v160006Ev
- __ZNSt3__114__thread_proxyB7v160006INS_5tupleIJNS_10unique_ptrINS_15__thread_structENS_14default_deleteIS3_EEEEZ18EncodeFrameThreadsE3$_0iiiEEEEEPvS9_
- __ZNSt3__119__allocate_at_leastB7v160006INS_9allocatorINS_6threadEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__120__throw_length_errorB7v160006EPKc
- __ZNSt3__128__exception_guard_exceptionsINS_6vectorINS_6threadENS_9allocatorIS2_EEE16__destroy_vectorEED2B7v160006Ev
- __ZNSt3__16vectorINS_6threadENS_9allocatorIS1_EEE11__vallocateB7v160006Em
- __ZNSt3__16vectorINS_6threadENS_9allocatorIS1_EEE16__destroy_vectorclB7v160006Ev
- __ZNSt3__16vectorINS_6threadENS_9allocatorIS1_EEED2B7v160006Ev
- __ZSt28__throw_bad_array_new_lengthB7v160006v
- ____getAccelerationModeOverride_block_invoke
- ___block_descriptor_tmp.3
- ___clang_call_terminate
- ___cxa_begin_catch
- __getAccelerationModeOverride.onceToken
- __getVTCompressionSessionPriorityOverride.onceToken
- __getVTSessionPriority
- __onceCheckUseCodecSessionPool
- __onceCheckVTCompressionSessionPriority
- __sessionPoolEnabled.onceToken
- __shouldUseSessionPool.onceToken
CStrings:
+ "BlockSize"
+ "BlockStride"
+ "Edges"
+ "FlipWeightedPercentiles"
+ "Histogram"
+ "HistogramSize"
+ "InputSize"
+ "Invalid"
+ "IsVirtualDevice"
+ "MSE"
+ "MSSSIM"
+ "MSSSIMWANG"
+ "Max"
+ "Min"
+ "Mode"
+ "MonitorDistance"
+ "MonitorWidth"
+ "PSNR"
+ "PSNR_HVS"
+ "SSIM"
+ "Unrecognized"
+ "UseMagma"
+ "UseMinMaxForDiffMap"
+ "WPSNR"
+ "apng"
+ "diffImageType"
+ "monitorResolutionX"
+ "png"
- "LossLess"

```
