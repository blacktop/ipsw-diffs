## Visage

> `/System/Library/PrivateFrameworks/Visage.framework/Visage`

```diff

-238.0.31.0.0
-  __TEXT.__text: 0x98960
+238.40.1.0.0
+  __TEXT.__text: 0x98e0c
   __TEXT.__auth_stubs: 0x1b00
   __TEXT.__objc_methlist: 0x44f4
   __TEXT.__const: 0x2fb0
-  __TEXT.__gcc_except_tab: 0xf484
+  __TEXT.__gcc_except_tab: 0xf504
   __TEXT.__cstring: 0x5471
-  __TEXT.__oslogstring: 0x5a05
-  __TEXT.__unwind_info: 0x35f0
+  __TEXT.__oslogstring: 0x5a78
+  __TEXT.__unwind_info: 0x3608
   __TEXT.__objc_classname: 0x9be
-  __TEXT.__objc_methname: 0xb50e
+  __TEXT.__objc_methname: 0xb5d2
   __TEXT.__objc_methtype: 0x2381
-  __TEXT.__objc_stubs: 0x7a80
+  __TEXT.__objc_stubs: 0x7b20
   __DATA_CONST.__got: 0x7d8
   __DATA_CONST.__const: 0x2f8
   __DATA_CONST.__objc_classlist: 0x320
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x26e0
+  __DATA_CONST.__objc_selrefs: 0x2708
   __DATA_CONST.__objc_superrefs: 0x1d8
   __DATA_CONST.__objc_arraydata: 0xf8
   __AUTH_CONST.__auth_got: 0xd90

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B2519F36-6296-3A7E-ACAC-1D0B200730FE
-  Functions: 3005
-  Symbols:   9655
-  CStrings:  4224
+  UUID: 4E8CEB9F-4926-330D-8EAB-4DB6CEE8667F
+  Functions: 3009
+  Symbols:   9668
+  CStrings:  4230
 
Symbols:
+ GCC_except_table107
+ GCC_except_table123
+ __ZN2vg6shared18createMetalTextureEPU19objcproto9MTLDevice11objc_objectRKNS0_22MetalTextureCreateInfoE.cold.1
+ __ZN2vg6shared25createMetalRenderPipelineEPU21objcproto10MTLLibrary11objc_objectRKNS0_29MetalRenderPipelineDescriptorE
+ __ZN2vg6shared25createMetalRenderPipelineEPU21objcproto10MTLLibrary11objc_objectRKNS0_29MetalRenderPipelineDescriptorE.cold.1
+ __ZN2vg6shared41computeNonUniformMetalDispatchThreadsSizeEPU34objcproto23MTLComputePipelineState11objc_objectDv2_ts
+ _objc_msgSend$newRenderPipelineStateWithDescriptor:options:reflection:error:
+ _objc_msgSend$setMaxVertexAmplificationCount:
+ _objc_msgSend$setSupportIndirectCommandBuffers:
+ _objc_msgSend$setWriteMask:
+ _objc_msgSend$textureCubeDescriptorWithPixelFormat:size:mipmapped:
- GCC_except_table121
- GCC_except_table85
Functions:
~ __ZN2vg6shared18createMetalTextureEPU19objcproto9MTLDevice11objc_objectRKNS0_22MetalTextureCreateInfoE : 340 -> 460
+ __ZN2vg6shared25createMetalRenderPipelineEPU21objcproto10MTLLibrary11objc_objectRKNS0_29MetalRenderPipelineDescriptorE
+ __ZN2vg6shared17linearPixelFormatE14MTLPixelFormat
+ __ZN2vg6shared18createMetalTextureEPU19objcproto9MTLDevice11objc_objectRKNS0_35MetalTextureCreateFromIOSurfaceInfoE.cold.2
+ __ZN2vg6shared29createMetalTileRenderPipelineEPU21objcproto10MTLLibrary11objc_objectP25MTLFunctionConstantValuesP8NSString14MTLPixelFormatS7_.cold.1
CStrings:
+ "Failed to create texture %@. Requested a cube texture with incompatible texture type or mismatched cube side size."
+ "newRenderPipelineStateWithDescriptor:options:reflection:error:"
+ "setMaxVertexAmplificationCount:"
+ "setSupportIndirectCommandBuffers:"
+ "setWriteMask:"
+ "textureCubeDescriptorWithPixelFormat:size:mipmapped:"

```
