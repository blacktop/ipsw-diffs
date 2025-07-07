## MetalTools

> `/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`

```diff

-370.54.0.0.0
-  __TEXT.__text: 0x12bb2c
-  __TEXT.__auth_stubs: 0xc20
+370.56.0.0.0
+  __TEXT.__text: 0x12c1d8
+  __TEXT.__auth_stubs: 0xc30
   __TEXT.__objc_methlist: 0x18cb4
-  __TEXT.__cstring: 0x314c5
+  __TEXT.__cstring: 0x3160a
   __TEXT.__const: 0x2f8
-  __TEXT.__gcc_except_tab: 0x2b58
+  __TEXT.__gcc_except_tab: 0x2b68
   __TEXT.__oslogstring: 0x282e
   __TEXT.__unwind_info: 0x50a8
   __TEXT.__objc_classname: 0x2520
-  __TEXT.__objc_methname: 0x1e20e
+  __TEXT.__objc_methname: 0x1e210
   __TEXT.__objc_methtype: 0x179cd
   __TEXT.__objc_stubs: 0x165e0
   __DATA_CONST.__got: 0xae8

   __DATA_CONST.__objc_protolist: 0x4c8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x6120
-  __DATA_CONST.__objc_protorefs: 0xa8
+  __DATA_CONST.__objc_protorefs: 0xa0
   __DATA_CONST.__objc_superrefs: 0x640
-  __AUTH_CONST.__auth_got: 0x620
+  __AUTH_CONST.__auth_got: 0x628
   __AUTH_CONST.__const: 0x1d0
-  __AUTH_CONST.__cfstring: 0xe2c0
-  __AUTH_CONST.__objc_const: 0x45b48
+  __AUTH_CONST.__cfstring: 0xe2e0
+  __AUTH_CONST.__objc_const: 0x45910
   __AUTH.__objc_data: 0x50
   __AUTH.__thread_vars: 0x18
   __AUTH.__thread_bss: 0x1

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9374291F-FE5F-3B2C-8CA4-8A3E45E0A4FE
+  UUID: 549B4C3F-4B8A-3156-ADBF-072A9FEA5606
   Functions: 7660
-  Symbols:   24308
-  CStrings:  10874
+  Symbols:   24307
+  CStrings:  10876
 
Symbols:
+ -[MTL4DebugCompiler validateDynamicLibrary:context:]
+ -[MTLGPUDebugDevice supportsPipelineLibraries]
+ GCC_except_table177
+ GCC_except_table228
+ GCC_except_table238
+ __MTLLibraryTypeString
+ _objc_msgSend$validateDynamicLibrary:context:
- -[MTL4GPUDebugCommandBuffer setUpShaderLoggingPrivateData]
- GCC_except_table180
- GCC_except_table183
- GCC_except_table187
- GCC_except_table189
- GCC_except_table198
- GCC_except_table227
- GCC_except_table237
- GCC_except_table36
- GCC_except_table49
- _OBJC_CLASS_$__MTLLibrary
- __OBJC_PROTOCOL_REFERENCE_$_MTLLibrary
- _objc_msgSend$setUpShaderLoggingPrivateData
CStrings:
+ "(region.origin.x + region.width)(%lu) must be <= mip tail size in tiles(%lu) when mipLevel == texture.firstMipmapInTail(%lu)."
+ "Cannot place resource at offset %lu extending beyond the heap size %llu (required size for region %llu)"
+ "For color attachment %u, the render pipeline's pixelFormat (%s) does not match the framebuffer's pixelFormat (%s)."
+ "bindingIndex (%u) must not be higher than the maxBufferBindCount (%u)."
+ "bindingIndex (%u) must not be higher than the maxSamplerStateCount (%u)."
+ "bindingIndex (%u) must not be higher than the maxTextureBindCount (%u)."
+ "expected a library with type MTLLibraryTypeDynamic, found invalid type: %@"
+ "library is not a MTLLibrary"
+ "region.origin.y(%lu) must be 0 when mipLevel == texture.firstMipmapInTail(%lu)."
+ "region.size.height(%lu) must be 1 when mipLevel == texture.firstMipmapInTail(%lu)."
+ "validateDynamicLibrary:context:"
- "Cannot place resource at offset %lu extending beyond the heap size %lu (required size for region %lu)"
- "bindingIndex (%d) must not be higher than the maxBufferBindCount (%d)."
- "bindingIndex (%d) must not be higher than the maxSamplerStateCount (%d)."
- "bindingIndex (%d) must not be higher than the maxTextureBindCount (%d)."
- "descriptor.name must not be nil"
- "descriptor.options must not be nil"
- "descriptor.source must not be nil"
- "library does not conform to MTLLibrary protocol"
- "library is not a MTLDynamicLibrary"
- "setUpShaderLoggingPrivateData"

```
