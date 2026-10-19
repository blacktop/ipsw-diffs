## CMCapture

> `/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`

```diff

 764.42.8.0.0
-  __TEXT.__text: 0x6842a0
-  __TEXT.__objc_methlist: 0x3e180
+  __TEXT.__text: 0x683d14
+  __TEXT.__objc_methlist: 0x3e198
   __TEXT.__const: 0x151800
-  __TEXT.__cstring: 0xb0599
-  __TEXT.__oslogstring: 0x54c86
+  __TEXT.__cstring: 0xb0381
+  __TEXT.__oslogstring: 0x54cfb
   __TEXT.__gcc_except_tab: 0x3c74
   __TEXT.__ustring: 0x6ee
   __TEXT.__dlopen_cstrs: 0x7c9
-  __TEXT.__unwind_info: 0x182f8
+  __TEXT.__unwind_info: 0x182b0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x118f8
+  __DATA_CONST.__const: 0x11920
   __DATA_CONST.__objc_classlist: 0x2048
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x688
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x18e40
+  __DATA_CONST.__objc_selrefs: 0x18e48
   __DATA_CONST.__objc_protorefs: 0x78
   __DATA_CONST.__objc_superrefs: 0x1e78
   __DATA_CONST.__objc_arraydata: 0x3cd8

   __AUTH_CONST.__auth_got: 0x2f28
   __AUTH.__objc_data: 0xf0
   __DATA.__objc_ivar: 0xcbf4
-  __DATA.__data: 0x988
+  __DATA.__data: 0x930
   __DATA.__crash_info: 0x148
   __DATA.__common: 0x1860
   __DATA_DIRTY.__objc_data: 0x141e0
-  __DATA_DIRTY.__data: 0x6678
+  __DATA_DIRTY.__data: 0x66d0
   __DATA_DIRTY.__bss: 0x1260
   __DATA_DIRTY.__common: 0x100
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  Functions: 39454
-  Symbols:   59487
-  CStrings:  22058
+  Functions: 39434
+  Symbols:   59488
+  CStrings:  22046
 
Symbols:
+ -[FigCaptureSessionConfiguration initWithXPCEncoding:clientAuditToken:]
+ -[FigCaptureSourceConfiguration initWithXPCEncoding:clientAuditToken:]
+ ___71-[FigCaptureSessionConfiguration initWithXPCEncoding:clientAuditToken:]_block_invoke
+ ___71-[FigCaptureSessionConfiguration initWithXPCEncoding:clientAuditToken:]_block_invoke_2
+ ___block_descriptor_72_e8_32o_e36_B24?0Q8"NSObject<OS_xpc_object>"16ls32l8
- _FigDepthBlurEffectRenderingMaximumSimulatedAperture
- _FigDepthBlurEffectRenderingMinimumSimulatedAperture
- ___54-[FigCaptureSessionConfiguration initWithXPCEncoding:]_block_invoke
- ___54-[FigCaptureSessionConfiguration initWithXPCEncoding:]_block_invoke_2
CStrings:
+ "<<<< FigCaptureSourceServer >>>> %s: Found matching FigCaptureSource %p for token %d but audit token does not match!"
- "*maximumSimulatedAperture > 0.0f"
- "*minimumSimulatedAperture > 0.0f"
- "0 == (effectiveVersion >> 16 )"
- "Maximum simulated aperture invalid."
- "Minimum simulated aperture invalid."
- "Unsupported SDOFRendering parameters version"
- "Unsupported version of SDOF; cannot re-use v4 struct."
- "maximumSimulatedAperture"
- "minimumSimulatedAperture"
- "minimumSimulatedAperture is NULL"
- "renderingParametersData.bytes"
- "renderingParametersData.length == renderingParameters->header.size"
- "renderingParametersData.length >= sizeof( FigDepthBlurEffectRenderingParametersHeader )"
```
