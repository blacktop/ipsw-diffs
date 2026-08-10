## Metal

> `/System/Library/Frameworks/Metal.framework/Metal`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__weak_got`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-382.5.0.0.0
-  __TEXT.__text: 0x1e6bec
-  __TEXT.__objc_methlist: 0x1eb7c
+382.5.3.0.0
+  __TEXT.__text: 0x1e6d38
+  __TEXT.__objc_methlist: 0x1eb8c
   __TEXT.__cstring: 0x233f9
-  __TEXT.__gcc_except_tab: 0xc3a0
+  __TEXT.__gcc_except_tab: 0xc3ac
   __TEXT.__const: 0x2d790
   __TEXT.__oslogstring: 0x22d6
   __TEXT.__ustring: 0x1be

   __DATA_CONST.__objc_protolist: 0x490
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0x8e68
+  __DATA_CONST.__objc_selrefs: 0x8e80
   __DATA_CONST.__objc_protorefs: 0x68
   __DATA_CONST.__objc_superrefs: 0xc08
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__got: 0xa30
   __AUTH_CONST.__const: 0x4f80
   __AUTH_CONST.__cfstring: 0x12ca0
-  __AUTH_CONST.__objc_const: 0x46bd0
+  __AUTH_CONST.__objc_const: 0x46bf0
   __AUTH_CONST.__weak_auth_got: 0x30
   __AUTH_CONST.__objc_intobj: 0x2b8
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__auth_got: 0xe98
   __AUTH.__objc_data: 0x4380
-  __DATA.__objc_ivar: 0x2230
+  __DATA.__objc_ivar: 0x2234
   __DATA.__data: 0x4498
   __DATA.__bss: 0x37c
   __DATA.__common: 0x40

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 13494
-  Symbols:   25317
+  Functions: 13495
+  Symbols:   25322
   CStrings:  4574
 
Symbols:
+ -[MTLShaderValidationConfiguration isShaderValidationEnabled]
+ _OBJC_IVAR_$__MTL4MachineLearningCommandEncoder._anePrePowerUpEvent
+ _objc_msgSend$isShaderValidationEnabled
+ _objc_msgSend$leadingDevice
+ _objc_msgSend$waitForANEPrePowerUpEvent:value:
Functions:
+ -[MTLShaderValidationConfiguration isShaderValidationEnabled]
~ __ZN26MTL4MetalScriptBuilderImpl35createShaderValidationConfigurationEP32MTLShaderValidationConfiguration : 356 -> 380
~ -[_MTL4MachineLearningCommandEncoder initWithDevice:] : 152 -> 184
~ -[_MTL4MachineLearningCommandEncoder initWithCommandBuffer:allocator:] : 172 -> 208
~ -[_MTL4MachineLearningCommandEncoder dealloc] : 276 -> 300
~ -[_MTL4MachineLearningCommandEncoder dispatchNetworkWithIntermediatesHeap:] : 608 -> 648
~ -[_MTL4MachineLearningCommandEncoder encodeToCommandQueue:] : 788 -> 884
CStrings:
+ "22:35:33"
+ "Aug  3 2026"
+ "Aug  3 2026 22:35:33"
- "23:33:30"
- "Jul 10 2026"
- "Jul 10 2026 23:33:30"
```
