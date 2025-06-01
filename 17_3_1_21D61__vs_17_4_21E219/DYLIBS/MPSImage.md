## MPSImage

> `/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSImage.framework/MPSImage`

```diff

-127.1.3.0.0
-  __TEXT.__text: 0x3f1a4
-  __TEXT.__auth_stubs: 0x650
-  __TEXT.__objc_methlist: 0x226c
-  __TEXT.__const: 0x2cb98
-  __TEXT.__gcc_except_tab: 0xf6c
-  __TEXT.__cstring: 0x13073
-  __TEXT.__unwind_info: 0xa20
-  __TEXT.__eh_frame: 0x18c
-  __TEXT.__objc_classname: 0x570
-  __TEXT.__objc_methname: 0x4899
-  __TEXT.__objc_methtype: 0x1422
-  __TEXT.__objc_stubs: 0x1b00
-  __DATA_CONST.__got: 0xa8
-  __DATA_CONST.__const: 0x23a60
-  __DATA_CONST.__objc_classlist: 0x200
+127.4.8.0.0
+  __TEXT.__text: 0x43cc0
+  __TEXT.__auth_stubs: 0x630
+  __TEXT.__objc_methlist: 0x2344
+  __TEXT.__const: 0x2cc10
+  __TEXT.__gcc_except_tab: 0x118c
+  __TEXT.__cstring: 0x131cd
+  __TEXT.__unwind_info: 0x9f8
+  __TEXT.__eh_frame: 0x38
+  __TEXT.__objc_classname: 0x58d
+  __TEXT.__objc_methname: 0x49e3
+  __TEXT.__objc_methtype: 0x143d
+  __TEXT.__objc_stubs: 0x1b40
+  __DATA_CONST.__got: 0xa0
+  __DATA_CONST.__const: 0x2a260
+  __DATA_CONST.__objc_classlist: 0x208
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x3008
-  __DATA_CONST.__objc_selrefs: 0xc70
+  __DATA_CONST.__objc_const: 0x30f8
+  __DATA_CONST.__objc_selrefs: 0xcb0
+  __DATA_CONST.__objc_classrefs: 0xb8
+  __DATA_CONST.__objc_superrefs: 0x200
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__objc_const: 0x0
-  __AUTH_CONST.__cfstring: 0x12020
+  __AUTH_CONST.__const: 0x20
+  __AUTH_CONST.__objc_const: 0x90
+  __AUTH_CONST.__cfstring: 0x12120
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__auth_got: 0x338
-  __DATA.__objc_classrefs: 0xb8
-  __DATA.__objc_superrefs: 0x1f8
-  __DATA.__objc_ivar: 0x3e8
-  __DATA.__bss: 0x50
-  __DATA_DIRTY.__const: 0x23010
+  __AUTH_CONST.__auth_got: 0x328
+  __AUTH.__objc_data: 0x50
+  __DATA.__objc_ivar: 0x3fc
+  __DATA.__bss: 0x60
+  __DATA_DIRTY.__const: 0x287c0
   __DATA_DIRTY.__objc_const: 0x1dd0
   __DATA_DIRTY.__objc_data: 0x1400
-  __DATA_DIRTY.__bss: 0x20
+  __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOSurface.framework/IOSurface

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E0D68B77-4286-3437-9F73-5D4C61F74987
-  Functions: 890
-  Symbols:   289
-  CStrings:  5549
+  UUID: 1ED671C6-D114-3E59-BAB7-CF6BC621D28A
+  Functions: 879
+  Symbols:   288
+  CStrings:  5583
 
Symbols:
+ _OBJC_CLASS_$_MPSImageStatisticsMinMaxMean
+ _OBJC_METACLASS_$_MPSImageStatisticsMinMaxMean
+ __ZN10MPSLibrary19CreateUberShaderKeyEP8NSStringRK23MPSFunctionConstantListyPFPU22objcproto11MTLFunction11objc_objectPU21objcproto10MTLLibrary11objc_objectPK13MPSKernelInfoS4_RK33MPSFunctionConstructorExtraParamsPP7NSErrorEy30MPSThreadGroupSizeMultipleType24MPSDriverCompilerOptionsP18MPSKernelDAGObjectS1_mP20MPSKernelUserDAGInfoP7NSArrayIS6_E
+ __ZN12MPSAutoCache14GetTempTextureEPK12MPSPixelInfoPK7MTLSizeP20MTLTextureDescriptorbP19TextureSizeAndAlignb
+ _objc_retain_x2
+ _objc_retain_x26
- __ZN10MPSLibrary19CreateUberShaderKeyEP8NSStringRK23MPSFunctionConstantListyPFPU22objcproto11MTLFunction11objc_objectPU21objcproto10MTLLibrary11objc_objectPK13MPSKernelInfoS4_RK33MPSFunctionConstructorExtraParamsPP7NSErrorEy30MPSThreadGroupSizeMultipleType24MPSDriverCompilerOptionsP18MPSKernelDAGObjectS1_m
- __ZN12MPSAutoCache14GetTempTextureEPK12MPSPixelInfoPK7MTLSizeP20MTLTextureDescriptorbP19TextureSizeAndAlign
- __ZNSt20bad_array_new_lengthC1Ev
- __ZNSt20bad_array_new_lengthD1Ev
- _objc_retain_x23
- _objc_retain_x24
- _objc_retain_x28
CStrings:
+ "@\"<MTLFunction>\""
+ "Failed to create passThrough library %@"
+ "MPSImageStatistics.stride.x"
+ "MPSImageStatistics.stride.y"
+ "MPSImageStatisticsMinMaxMean"
+ "T,N,V_strides"
+ "T@\"<MTLBuffer>\",&,N,V_colorConversionData"
+ "T@\"<MTLFunction>\",&,N,V_colorConversionFunction"
+ "[[visible]] float4 __attribute__((__always_inline__)) color_conversion(float4 v, constant void* data){return v;}"
+ "_colorConversionData"
+ "_colorConversionFunction"
+ "_defaultConversion"
+ "_strides"
+ "clipRect width should be 3 or more"
+ "colorConversionData"
+ "colorConversionFunction"
+ "color_conversion"
+ "device"
+ "filterInfo %d + srcStyle %d >= %d"
+ "localizedDescription"
+ "newFunctionWithName:"
+ "newLibraryWithSource:options:error:"
+ "reduce_statistics_final"
+ "reduce_statistics_intermediate"
+ "setColorConversionData:"
+ "setColorConversionFunction:"
+ "setStrides:"
+ "strides"
+ "v24@0:816"
- "_%@"
- "setProtectionOptions:"
- "stringByAppendingString:"

```
