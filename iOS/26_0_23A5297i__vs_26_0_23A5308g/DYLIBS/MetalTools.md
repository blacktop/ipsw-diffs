## MetalTools

> `/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`

```diff

-370.57.0.0.0
-  __TEXT.__text: 0x12c5c4
+370.62.0.0.0
+  __TEXT.__text: 0x12c758
   __TEXT.__auth_stubs: 0xc30
   __TEXT.__objc_methlist: 0x18d0c
-  __TEXT.__cstring: 0x3160a
+  __TEXT.__cstring: 0x3171f
   __TEXT.__const: 0x2f8
   __TEXT.__gcc_except_tab: 0x2b68
   __TEXT.__oslogstring: 0x282e
-  __TEXT.__unwind_info: 0x50b0
+  __TEXT.__unwind_info: 0x50a0
   __TEXT.__objc_classname: 0x2520
   __TEXT.__objc_methname: 0x1e210
-  __TEXT.__objc_methtype: 0x179cd
+  __TEXT.__objc_methtype: 0x179ca
   __TEXT.__objc_stubs: 0x16600
   __DATA_CONST.__got: 0xaf0
   __DATA_CONST.__const: 0x1b28

   __DATA_CONST.__objc_superrefs: 0x640
   __AUTH_CONST.__auth_got: 0x628
   __AUTH_CONST.__const: 0x1d0
-  __AUTH_CONST.__cfstring: 0xe2e0
+  __AUTH_CONST.__cfstring: 0xe300
   __AUTH_CONST.__objc_const: 0x45910
-  __AUTH.__objc_data: 0x50
   __AUTH.__thread_vars: 0x18
   __AUTH.__thread_bss: 0x1
   __DATA.__objc_ivar: 0xfec
   __DATA.__data: 0x3970
   __DATA.__bss: 0x80
-  __DATA_DIRTY.__objc_data: 0x4880
+  __DATA_DIRTY.__objc_data: 0x48d0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: AC582AD7-CD00-399C-901C-6F79D6E2CEF0
+  UUID: 2ABA2E55-A0CC-333F-90FA-329FF0D1AD8C
   Functions: 7667
   Symbols:   24322
-  CStrings:  10876
+  CStrings:  10878
 
Symbols:
+ GCC_except_table49
+ GCC_except_table53
+ ___block_literal_global.1659
+ _getFunctionDescriptorName
- __ZL12newImageDataP22MTL4FunctionDescriptor15MTLFunctionTypeP27MTLDebugInstrumentationDataP17MTLGPUDebugDevice
- ___block_literal_global.1656
CStrings:
+ "%@ Function(%@): A sparse texture is being bound at index %lu to a shader argument with write access enabled. Sparse textures do not support writes from shaders on this platform unless they are placement sparse textures with a sparseTextureTier equal to MTLTextureSparseTier1."
+ "v32@0:8@16q24"
- "v40@0:8Q16Q24q32"

```
