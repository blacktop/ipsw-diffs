## CCPortrait

> `/System/Library/VideoProcessors/CCPortrait.bundle/CCPortrait`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_floatobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-758.0.0.122.2
-  __TEXT.__text: 0x412bc
-  __TEXT.__objc_methlist: 0x2ff4
+761.0.0.0.3
+  __TEXT.__text: 0x415e0
+  __TEXT.__objc_methlist: 0x302c
   __TEXT.__const: 0x2b8
-  __TEXT.__gcc_except_tab: 0x91c
-  __TEXT.__cstring: 0x93ae
+  __TEXT.__gcc_except_tab: 0x928
+  __TEXT.__cstring: 0x941e
   __TEXT.__oslogstring: 0x1e06
-  __TEXT.__unwind_info: 0x9e8
+  __TEXT.__unwind_info: 0xa00
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2a0
+  __DATA_CONST.__const: 0x2b8
   __DATA_CONST.__objc_classlist: 0x188
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1fd8
+  __DATA_CONST.__objc_selrefs: 0x2000
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0xf8
   __DATA_CONST.__objc_arraydata: 0x50
-  __DATA_CONST.__got: 0x3f8
+  __DATA_CONST.__got: 0x400
   __AUTH_CONST.__const: 0xb20
-  __AUTH_CONST.__cfstring: 0x6020
-  __AUTH_CONST.__objc_const: 0x5700
+  __AUTH_CONST.__cfstring: 0x60c0
+  __AUTH_CONST.__objc_const: 0x5730
   __AUTH_CONST.__objc_intobj: 0xba0
   __AUTH_CONST.__objc_floatobj: 0x60
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH_CONST.__auth_got: 0x628
+  __AUTH_CONST.__auth_got: 0x638
   __AUTH.__objc_data: 0x370
-  __DATA.__objc_ivar: 0x3f4
+  __DATA.__objc_ivar: 0x3f8
   __DATA.__data: 0x2b8
-  __DATA.__bss: 0xf8
+  __DATA.__bss: 0x108
   __DATA_DIRTY.__objc_data: 0xbe0
-  __DATA_DIRTY.__bss: 0x108
+  __DATA_DIRTY.__bss: 0xf8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreImage.framework/CoreImage

   - /System/Library/Frameworks/ImageIO.framework/ImageIO
   - /System/Library/Frameworks/Metal.framework/Metal
   - /System/Library/Frameworks/MetalPerformanceShaders.framework/MetalPerformanceShaders
+  - /System/Library/PrivateFrameworks/CMCapture.framework/CMCapture
   - /System/Library/PrivateFrameworks/CMImaging.framework/CMImaging
   - /System/Library/PrivateFrameworks/Espresso.framework/Espresso
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1432
-  Symbols:   439
-  CStrings:  1345
+  Functions: 1437
+  Symbols:   445
+  CStrings:  1350
 
Symbols:
+ _OBJC_CLASS_$_CMInferenceUtils
+ _e5rt_precompiled_compute_op_create_options_set_anef_intermediate_buffer_size_hint
+ _espresso_network_bind_cvpixelbuffer
+ _kEspressoInferenceDeviceANE
+ _kEspressoInferenceDeviceCPU
+ _kEspressoInferenceDeviceGPU
+ _qos_class_self
- _e5rt_precompiled_compute_op_create_options_set_iosurface_memory_pool_id
CStrings:
+ "%@|%@"
+ "1x - ANEDriver intermediate buffer(BSS) size hint"
+ "2x - ANEDriver intermediate buffer(BSS) size hint"
+ "ANE"
+ "CPU"
+ "GPU"
+ "Warning - Failed to set ANEF intermediate buffer size hint"
- "  - Memory pool ID: %llu\n"
- "Warning - Failed to set memory pool ID"
```
