## WebGPU

> `/System/Library/PrivateFrameworks/WebGPU.framework/WebGPU`

```diff

-625.2.7.1.0
-  __TEXT.__text: 0x241f50
-  __TEXT.__objc_methlist: 0x200
+625.2.8.10.4
+  __TEXT.__text: 0x2416c8
+  __TEXT.__objc_methlist: 0x614
   __TEXT.__const: 0x1f94
-  __TEXT.__gcc_except_tab: 0xa9b8
+  __TEXT.__gcc_except_tab: 0xaa4c
   __TEXT.__swift5_typeref: 0x7d8
-  __TEXT.__cstring: 0x3e44c
+  __TEXT.__cstring: 0x3e46c
   __TEXT.__constg_swiftt: 0xb7c
   __TEXT.__swift5_fieldmd: 0x400
   __TEXT.__swift5_builtin: 0xdc

   __TEXT.__swift5_types: 0x4c
   __TEXT.__swift5_protos: 0x50
   __TEXT.__swift5_types2: 0x4
-  __TEXT.__unwind_info: 0x4768
+  __TEXT.__unwind_info: 0x47d0
   __TEXT.__eh_frame: 0xfe8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x2b10
   __DATA_CONST.__objc_classlist: 0x18
+  __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb08
+  __DATA_CONST.__objc_selrefs: 0xcb0
+  __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__got: 0x2d0
   __AUTH_CONST.__const: 0x4d18
   __AUTH_CONST.__cfstring: 0x3a60
-  __AUTH_CONST.__objc_const: 0x658
+  __AUTH_CONST.__objc_const: 0xc50
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__auth_got: 0xa20
   __AUTH.__objc_data: 0xf0
   __AUTH.__data: 0x108
   __DATA.__objc_ivar: 0x60
-  __DATA.__data: 0x150
+  __DATA.__data: 0x330
   __DATA.__common: 0x90
   __DATA_DIRTY.__bss: 0x128
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  Functions: 3649
-  Symbols:   4108
+  Functions: 3651
+  Symbols:   4140
   CStrings:  2757
 
Symbols:
+ GCC_except_table115
+ GCC_except_table127
+ GCC_except_table98
+ __OBJC_$_PROP_LIST_MTLAllocation
+ __OBJC_$_PROP_LIST_MTLBuffer
+ __OBJC_$_PROP_LIST_MTLResource
+ __OBJC_$_PROP_LIST_MTLTexture
+ __OBJC_$_PROP_LIST_NSObject
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTLAllocation
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTLBuffer
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTLResource
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTLTexture
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTLAllocation
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTLBuffer
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTLResource
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTLTexture
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject
+ __OBJC_$_PROTOCOL_REFS_MTLAllocation
+ __OBJC_$_PROTOCOL_REFS_MTLBuffer
+ __OBJC_$_PROTOCOL_REFS_MTLResource
+ __OBJC_$_PROTOCOL_REFS_MTLTexture
+ __OBJC_LABEL_PROTOCOL_$_MTLAllocation
+ __OBJC_LABEL_PROTOCOL_$_MTLBuffer
+ __OBJC_LABEL_PROTOCOL_$_MTLResource
+ __OBJC_LABEL_PROTOCOL_$_MTLTexture
+ __OBJC_LABEL_PROTOCOL_$_NSObject
+ __OBJC_PROTOCOL_$_MTLAllocation
+ __OBJC_PROTOCOL_$_MTLBuffer
+ __OBJC_PROTOCOL_$_MTLResource
+ __OBJC_PROTOCOL_$_MTLTexture
+ __OBJC_PROTOCOL_$_NSObject
+ __OBJC_PROTOCOL_REFERENCE_$_MTLBuffer
+ __OBJC_PROTOCOL_REFERENCE_$_MTLTexture
+ __ZN3WTF6VectorIN6WebGPU5Queue23ProvisionalTextureClearELm0ENS_15CrashOnOverflowELm16ENS_10FastMallocEED1Ev
+ __ZN6WebGPU14CommandEncoder19addResidentResourceEPU22objcproto11MTLResource11objc_object
+ __ZN6WebGPU14CommandEncoder20clearTextureIfNeededERK20WGPUImageCopyTexturemRKNS_6DeviceEPU32objcproto21MTLBlitCommandEncoder11objc_objectPKS0_
+ __ZN6WebGPU14CommandEncoder20clearTextureIfNeededERNS_7TextureEmmRKNS_6DeviceEPU32objcproto21MTLBlitCommandEncoder11objc_objectPKS0_
- GCC_except_table101
- GCC_except_table126
- GCC_except_table130
- GCC_except_table134
- GCC_except_table46
- __ZN6WebGPU14CommandEncoder20clearTextureIfNeededERK20WGPUImageCopyTexturemRKNS_6DeviceEPU32objcproto21MTLBlitCommandEncoder11objc_object
- __ZN6WebGPU14CommandEncoder20clearTextureIfNeededERNS_7TextureEmmRKNS_6DeviceEPU32objcproto21MTLBlitCommandEncoder11objc_object
CStrings:
+ "21.0.0 (clang-2100.3.34.1) [+internal-os]"
+ "static void WebGPU::CommandEncoder::clearTextureIfNeeded(Texture &, NSUInteger, NSUInteger, const Device &, __strong id<MTLBlitCommandEncoder>, const CommandEncoder * _Nullable)"
- "21.0.0 (clang-2100.4.1.1) [+internal-os]"
- "static void WebGPU::CommandEncoder::clearTextureIfNeeded(Texture &, NSUInteger, NSUInteger, const Device &, __strong id<MTLBlitCommandEncoder>)"
```
