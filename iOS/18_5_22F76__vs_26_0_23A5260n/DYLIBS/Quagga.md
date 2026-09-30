## Quagga

> `/System/Library/PrivateFrameworks/Quagga.framework/Quagga`

```diff

-210.4.0.0.0
-  __TEXT.__text: 0xed2cc
-  __TEXT.__auth_stubs: 0x1e30
-  __TEXT.__objc_methlist: 0x7d4
-  __TEXT.__const: 0x25090
-  __TEXT.__cstring: 0x4e9a
+226.0.0.0.0
+  __TEXT.__text: 0xee494
+  __TEXT.__auth_stubs: 0x1dc0
+  __TEXT.__objc_methlist: 0x8ac
+  __TEXT.__const: 0x24ff0
+  __TEXT.__cstring: 0x4ef0
   __TEXT.__dlopen_cstrs: 0x43
-  __TEXT.__gcc_except_tab: 0x92e4
-  __TEXT.__oslogstring: 0x665b
-  __TEXT.__unwind_info: 0x3438
+  __TEXT.__gcc_except_tab: 0x90e4
+  __TEXT.__oslogstring: 0x674a
+  __TEXT.__unwind_info: 0x3468
   __TEXT.__objc_classname: 0x86
-  __TEXT.__objc_methname: 0x18f9
-  __TEXT.__objc_methtype: 0x1139
+  __TEXT.__objc_methname: 0x1b40
+  __TEXT.__objc_methtype: 0x1475
   __TEXT.__objc_stubs: 0x7a0
   __DATA_CONST.__got: 0x5a0
   __DATA_CONST.__const: 0x13e8
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x608
+  __DATA_CONST.__objc_selrefs: 0x698
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0xf28
+  __AUTH_CONST.__auth_got: 0xef0
   __AUTH_CONST.__const: 0x7b68
-  __AUTH_CONST.__cfstring: 0x3c60
-  __AUTH_CONST.__objc_const: 0xae0
+  __AUTH_CONST.__cfstring: 0x3ca0
+  __AUTH_CONST.__objc_const: 0xb70
   __DATA.__objc_ivar: 0x20
   __DATA.__data: 0x490
-  __DATA.__bss: 0x310
+  __DATA.__bss: 0x300
   __DATA_DIRTY.__objc_data: 0x190
   __DATA_DIRTY.__data: 0x2b8
-  __DATA_DIRTY.__bss: 0xd48
+  __DATA_DIRTY.__bss: 0xd40
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /System/Library/Frameworks/IOSurface.framework/IOSurface
   - /System/Library/Frameworks/ImageIO.framework/ImageIO
   - /System/Library/Frameworks/Metal.framework/Metal
+  - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/VideoToolbox.framework/VideoToolbox
   - /System/Library/PrivateFrameworks/AppC3D.framework/AppC3D
   - /System/Library/PrivateFrameworks/Espresso.framework/Espresso

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libiconv.2.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D53ED6EE-8877-3958-A150-CF4149C8801F
-  Functions: 3239
-  Symbols:   922
-  CStrings:  2190
+  UUID: 0F617F46-4C5D-36CF-BF46-F2C22A5EF57C
+  Functions: 3256
+  Symbols:   917
+  CStrings:  2233
 
Symbols:
+ __ZNSt3__16localeC1Ev
+ __ZTVNSt3__115basic_streambufIcNS_11char_traitsIcEEEE
+ __ZTVNSt3__115basic_streambufIwNS_11char_traitsIwEEEE
- _CFMakeCollectable
- __ZNSt3__115basic_streambufIcNS_11char_traitsIcEEEC2Ev
- __ZNSt3__115basic_streambufIcNS_11char_traitsIcEEED2Ev
- __ZNSt3__115basic_streambufIwNS_11char_traitsIwEEEC2Ev
- __ZNSt3__115basic_streambufIwNS_11char_traitsIwEEED2Ev
- __Znwm
- _objc_release_x28
- _wmemchr
CStrings:
+ "@\"<MTL4Archive>\"32@0:8@\"NSURL\"16^@24"
+ "@\"<MTL4ArgumentTable>\"32@0:8@\"MTL4ArgumentTableDescriptor\"16^@24"
+ "@\"<MTL4CommandAllocator>\"16@0:8"
+ "@\"<MTL4CommandAllocator>\"32@0:8@\"MTL4CommandAllocatorDescriptor\"16^@24"
+ "@\"<MTL4CommandBuffer>\"16@0:8"
+ "@\"<MTL4CommandQueue>\"16@0:8"
+ "@\"<MTL4CommandQueue>\"32@0:8@\"MTL4CommandQueueDescriptor\"16^@24"
+ "@\"<MTL4Compiler>\"32@0:8@\"MTL4CompilerDescriptor\"16^@24"
+ "@\"<MTL4CounterHeap>\"32@0:8@\"MTL4CounterHeapDescriptor\"16^@24"
+ "@\"<MTL4PipelineDataSetSerializer>\"24@0:8@\"MTL4PipelineDataSetSerializerDescriptor\"16"
+ "@\"<MTLBuffer>\"40@0:8Q16Q24q32"
+ "@\"<MTLFunctionHandle>\"24@0:8@\"<MTL4BinaryFunction>\"16"
+ "@\"<MTLFunctionHandle>\"24@0:8@\"<MTLFunction>\"16"
+ "@\"<MTLTensor>\"32@0:8@\"MTLTensorDescriptor\"16^@24"
+ "@\"<MTLTextureViewPool>\"32@0:8@\"MTLResourceViewPoolDescriptor\"16^@24"
+ "@40@0:8Q16Q24q32"
+ "Failed to allocate pixel rotation session."
+ "Failed to allocate pixel rotation session: %{public}@"
+ "Failed to allocate pixel transfer session."
+ "Failed to allocate pixel transfer session: %{public}@"
+ "Process is not entitled for access to ANE, skipping..."
+ "Process is not entitled for access to ANE, will set fallback device to GPU."
+ "functionHandleWithBinaryFunction:"
+ "functionHandleWithFunction:"
+ "newArchiveWithURL:error:"
+ "newArgumentTableWithDescriptor:error:"
+ "newBufferWithLength:options:placementSparsePageSize:"
+ "newCommandAllocator"
+ "newCommandAllocatorWithDescriptor:error:"
+ "newCommandBuffer"
+ "newCompilerWithDescriptor:error:"
+ "newCounterHeapWithDescriptor:error:"
+ "newMTL4CommandQueue"
+ "newMTL4CommandQueueWithDescriptor:error:"
+ "newPipelineDataSetSerializerWithDescriptor:"
+ "newTensorWithDescriptor:error:"
+ "newTextureViewPoolWithDescriptor:error:"
+ "queryTimestampFrequency"
+ "sizeOfCounterHeapEntry:"
+ "tensorSizeAndAlignWithDescriptor:"
+ "{?=QQ}24@0:8@\"MTLTensorDescriptor\"16"

```
