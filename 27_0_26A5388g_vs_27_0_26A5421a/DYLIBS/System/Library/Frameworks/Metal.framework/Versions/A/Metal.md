## Metal

> `/System/Library/Frameworks/Metal.framework/Versions/A/Metal`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`

```diff

-382.5.0.0.0
-  __TEXT.__text: 0x1f8a94
-  __TEXT.__objc_methlist: 0x1f834
+382.5.3.0.0
+  __TEXT.__text: 0x1f8be0
+  __TEXT.__objc_methlist: 0x1f844
   __TEXT.__cstring: 0x23f0c
-  __TEXT.__gcc_except_tab: 0xc57c
+  __TEXT.__gcc_except_tab: 0xc588
   __TEXT.__const: 0x2d7b0
   __TEXT.__oslogstring: 0x2400
   __TEXT.__ustring: 0x1be

   __DATA_CONST.__objc_protolist: 0x490
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0x9418
+  __DATA_CONST.__objc_selrefs: 0x9430
   __DATA_CONST.__objc_protorefs: 0x68
   __DATA_CONST.__objc_superrefs: 0xc38
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__got: 0xa68
   __AUTH_CONST.__const: 0x6ed8
   __AUTH_CONST.__cfstring: 0x13640
-  __AUTH_CONST.__objc_const: 0x48480
+  __AUTH_CONST.__objc_const: 0x484a0
   __AUTH_CONST.__weak_auth_got: 0x30
   __AUTH_CONST.__objc_intobj: 0x180
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__auth_got: 0xef8
   __AUTH.__objc_data: 0x4420
-  __DATA.__objc_ivar: 0x235c
+  __DATA.__objc_ivar: 0x2360
   __DATA.__data: 0x4498
   __DATA.__bss: 0x3e4
   __DATA.__common: 0x40

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 13967
-  Symbols:   26249
+  Functions: 13968
+  Symbols:   26254
   CStrings:  4694
 
Symbols:
+ -[MTLShaderValidationConfiguration isShaderValidationEnabled]
+ OBJC_IVAR_$__MTL4MachineLearningCommandEncoder._anePrePowerUpEvent
+ _objc_msgSend$isShaderValidationEnabled
+ _objc_msgSend$leadingDevice
+ _objc_msgSend$waitForANEPrePowerUpEvent:value:
Functions:
+ -[MTLShaderValidationConfiguration isShaderValidationEnabled]
~ __ZN26MTL4MetalScriptBuilderImpl35createShaderValidationConfigurationEP32MTLShaderValidationConfiguration : 356 -> 380
~ -[_MTL4MachineLearningCommandEncoder initWithDevice:] : 152 -> 184
~ -[_MTL4MachineLearningCommandEncoder initWithCommandBuffer:allocator:] : 172 -> 208
~ -[_MTL4MachineLearningCommandEncoder dealloc] : 276 -> 300
~ -[_MTL4MachineLearningCommandEncoder dispatchNetworkWithIntermediatesHeap:] : 564 -> 604
~ -[_MTL4MachineLearningCommandEncoder encodeToCommandQueue:] : 776 -> 872
CStrings:
+ "01:00:42"
+ "Aug 10 2026"
+ "Aug 10 2026 01:00:42"
- "00:41:55"
- "Jul 11 2026"
- "Jul 11 2026 00:41:55"
```
