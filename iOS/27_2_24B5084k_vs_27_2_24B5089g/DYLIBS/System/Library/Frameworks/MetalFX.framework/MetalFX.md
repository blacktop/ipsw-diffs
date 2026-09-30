## MetalFX

> `/System/Library/Frameworks/MetalFX.framework/MetalFX`

```diff

-40.8.0.0.0
-  __TEXT.__text: 0x7e834
-  __TEXT.__objc_methlist: 0x55f4
-  __TEXT.__gcc_except_tab: 0xc170
+40.9.0.0.0
+  __TEXT.__text: 0x7f000
+  __TEXT.__objc_methlist: 0x56dc
+  __TEXT.__gcc_except_tab: 0xc248
   __TEXT.__const: 0x618
   __TEXT.__cstring: 0x5975
   __TEXT.__ustring: 0x632
-  __TEXT.__unwind_info: 0x1818
+  __TEXT.__unwind_info: 0x1870
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__const: 0x538
   __DATA_CONST.__objc_classlist: 0x170
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0xb8
+  __DATA_CONST.__objc_protolist: 0xc8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x13e8
+  __DATA_CONST.__objc_selrefs: 0x1408
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0xe8
   __DATA_CONST.__objc_arraydata: 0x2ad8
-  __DATA_CONST.__got: 0x2b8
+  __DATA_CONST.__got: 0x2c0
   __AUTH_CONST.__const: 0x600
   __AUTH_CONST.__cfstring: 0x5be0
-  __AUTH_CONST.__objc_const: 0xefd0
+  __AUTH_CONST.__objc_const: 0xf198
   __AUTH_CONST.__weak_auth_got: 0x218
   __AUTH_CONST.__objc_intobj: 0x348
   __AUTH_CONST.__objc_arrayobj: 0x2a78
   __AUTH_CONST.__auth_got: 0x3a8
-  __AUTH.__objc_data: 0x1e0
-  __DATA.__objc_ivar: 0x10c8
-  __DATA.__data: 0x8a0
-  __DATA_DIRTY.__objc_data: 0xc80
+  __DATA.__objc_ivar: 0x10d0
+  __DATA.__data: 0xc0
+  __DATA_DIRTY.__objc_data: 0xe60
+  __DATA_DIRTY.__data: 0x8a0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Metal.framework/Metal

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1893
-  Symbols:   4077
+  Functions: 1902
+  Symbols:   4107
   CStrings:  861
 
Symbols:
+ -[_M4FXTemporalScalingEffectBBR _didCreateComputeCommandEncoder:forEncode:]
+ -[_M4FXTemporalScalingEffectBBR _didCreateRenderCommandEncoder:forEncode:]
+ -[_M4FXTemporalScalingEffectBBR setTracingDelegate:]
+ -[_M4FXTemporalScalingEffectBBR tracingDelegate]
+ -[_MFXTemporalScalingEffectBBR _didCreateBlitCommandEncoder:forEncode:]
+ -[_MFXTemporalScalingEffectBBR _didCreateComputeCommandEncoder:forEncode:]
+ -[_MFXTemporalScalingEffectBBR _didCreateRenderCommandEncoder:forEncode:]
+ -[_MFXTemporalScalingEffectBBR setTracingDelegate:]
+ -[_MFXTemporalScalingEffectBBR tracingDelegate]
+ _OBJC_CLASS_$_MTL4PipelineOptions
+ _OBJC_IVAR_$__M4FXTemporalScalingEffectBBR._tracingDelegate
+ _OBJC_IVAR_$__MFXTemporalScalingEffectBBR._tracingDelegate
+ __OBJC_$_PROP_LIST_MTL4FXEffectTracing
+ __OBJC_$_PROP_LIST_MTLFXEffectTracing
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTL4FXEffectTracing
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTLFXEffectTracing
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTL4FXEffectTracing
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTLFXEffectTracing
+ __OBJC_$_PROTOCOL_REFS_MTL4FXEffectTracing
+ __OBJC_$_PROTOCOL_REFS_MTLFXEffectTracing
+ __OBJC_CLASS_PROTOCOLS_$__MTL4FXEffect
+ __OBJC_CLASS_PROTOCOLS_$__MTLFXEffect
+ __OBJC_LABEL_PROTOCOL_$_MTL4FXEffectTracing
+ __OBJC_LABEL_PROTOCOL_$_MTLFXEffectTracing
+ __OBJC_PROTOCOL_$_MTL4FXEffectTracing
+ __OBJC_PROTOCOL_$_MTLFXEffectTracing
+ __ZN10MFXDevice321createComputePipelineEPU21objcproto10MTLLibrary11objc_objectP8NSStringP25MTLFunctionConstantValuesj
+ __ZN10MFXDevice421createComputePipelineEPU21objcproto10MTLLibrary11objc_objectP8NSStringP25MTLFunctionConstantValuesj
+ _objc_msgSend$newComputePipelineStateWithDescriptor:options:reflection:error:
+ _objc_msgSend$options
+ _objc_msgSend$setOptions:
+ _objc_msgSend$setShaderValidation:
- __ZN10MFXDevice321createComputePipelineEPU21objcproto10MTLLibrary11objc_objectP8NSStringP25MTLFunctionConstantValues
- __ZN10MFXDevice421createComputePipelineEPU21objcproto10MTLLibrary11objc_objectP8NSStringP25MTLFunctionConstantValues
```
