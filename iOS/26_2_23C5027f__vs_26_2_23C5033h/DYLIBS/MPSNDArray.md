## MPSNDArray

> `/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNDArray.framework/MPSNDArray`

```diff

-129.1.5.0.0
-  __TEXT.__text: 0x10695c
+129.2.0.0.0
+  __TEXT.__text: 0x106e88
   __TEXT.__auth_stubs: 0xac0
-  __TEXT.__objc_methlist: 0x6a84
+  __TEXT.__objc_methlist: 0x6aac
   __TEXT.__const: 0x83c18
-  __TEXT.__gcc_except_tab: 0x3ea4
-  __TEXT.__cstring: 0xdb90
+  __TEXT.__gcc_except_tab: 0x3f1c
+  __TEXT.__cstring: 0xdcd0
   __TEXT.__unwind_info: 0x1878
   __TEXT.__eh_frame: 0x68
   __TEXT.__objc_classname: 0x1c59
-  __TEXT.__objc_methname: 0x6c21
-  __TEXT.__objc_methtype: 0x1ea9
-  __TEXT.__objc_stubs: 0x32c0
+  __TEXT.__objc_methname: 0x6c90
+  __TEXT.__objc_methtype: 0x1ec3
+  __TEXT.__objc_stubs: 0x32e0
   __DATA_CONST.__got: 0x2e8
   __DATA_CONST.__const: 0xedb0
   __DATA_CONST.__objc_classlist: 0x848
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1540
+  __DATA_CONST.__objc_selrefs: 0x1558
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x820
   __AUTH_CONST.__auth_got: 0x570
   __AUTH_CONST.__const: 0x3fe0
-  __AUTH_CONST.__cfstring: 0x6bc0
-  __AUTH_CONST.__objc_const: 0xe888
+  __AUTH_CONST.__cfstring: 0x6be0
+  __AUTH_CONST.__objc_const: 0xe8b8
   __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0x6a8
+  __DATA.__objc_ivar: 0x6ac
   __DATA.__data: 0x9c4
   __DATA.__bss: 0x5d8
   __DATA_DIRTY.__objc_data: 0x5280

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2BCE6060-B04E-3BFF-93FE-B9A09C6C69A6
-  Functions: 2237
-  Symbols:   7533
-  CStrings:  3657
+  UUID: 7FD8F60A-2FEA-3615-A7E6-1986FEA92548
+  Functions: 2240
+  Symbols:   7540
+  CStrings:  3670
 
Symbols:
+ -[MPSNDArrayQuantizedScaledDotProductAttention initWithDevice:kernelType:maskType:qQuantizationDescriptor:kQuantizationDescriptor:vQuantizationDescriptor:]
+ -[MPSNDArrayQuantizedScaledDotProductAttention initWithDevice:kernelType:maskType:qQuantizationDescriptor:kQuantizationDescriptor:vQuantizationDescriptor:sourceCount:]
+ -[MPSNDArrayScaledDotProductAttention initWithDevice:kernelType:maskType:]
+ -[MPSNDArrayScaledDotProductAttention initWithDevice:kernelType:maskType:sourceCount:]
+ -[MPSNDArrayScaledDotProductAttention maskType]
+ -[MPSNDArrayScaledDotProductAttention setMaskType:]
+ GCC_except_table30
+ GCC_except_table38
+ GCC_except_table53
+ GCC_except_table55
+ GCC_except_table62
+ GCC_except_table63
+ ___block_literal_global.178
+ ___block_literal_global.181
+ ___block_literal_global.184
+ ___block_literal_global.223
+ _objc_msgSend$initWithDevice:kernelType:maskType:qQuantizationDescriptor:kQuantizationDescriptor:vQuantizationDescriptor:
+ _objc_msgSend$initWithDevice:kernelType:maskType:qQuantizationDescriptor:kQuantizationDescriptor:vQuantizationDescriptor:sourceCount:
+ _objc_msgSend$initWithDevice:kernelType:maskType:sourceCount:
+ _objc_msgSend$maskType
- -[MPSNDArrayQuantizedScaledDotProductAttention initWithDevice:kernelType:qQuantizationDescriptor:kQuantizationDescriptor:vQuantizationDescriptor:]
- -[MPSNDArrayQuantizedScaledDotProductAttention initWithDevice:kernelType:qQuantizationDescriptor:kQuantizationDescriptor:vQuantizationDescriptor:sourceCount:]
- -[MPSNDArrayScaledDotProductAttention initWithDevice:kernelType:sourceCount:]
- GCC_except_table29
- GCC_except_table50
- ___block_literal_global.170
- ___block_literal_global.173
- ___block_literal_global.176
- ___block_literal_global.215
- _objc_msgSend$initWithDevice:kernelType:qQuantizationDescriptor:kQuantizationDescriptor:vQuantizationDescriptor:
- _objc_msgSend$initWithDevice:kernelType:qQuantizationDescriptor:kQuantizationDescriptor:vQuantizationDescriptor:sourceCount:
- _objc_msgSend$initWithDevice:kernelType:sourceCount:
CStrings:
+ " -maskType "
+ "-dstTranspose 0 "
+ "@32@0:8@16i24i28"
+ "@40@0:8@16i24i28Q32"
+ "@56@0:8@16i24i28@32@40@48"
+ "@64@0:8@16i24i28@32@40@48Q56"
+ "MPSNDArraySDPAMaskCausal"
+ "MPSNDArraySDPAMaskRandom"
+ "SDPA: Batches=%lu, PromptSize=%lu, Contexts=%lu, Heads=%lu, Features=%lu, Q Datatype: %s, K Datatype: %s, V Datatype: %s, Mask Type: %lu, Dest Datatype: %s\t"
+ "SDPA: Batches=%lu, PromptSize=%lu, Contexts=%lu, Heads=%lu, Features=%lu, Q Datatype: %s, K Datatype: %s, V Datatype: %s, Mask(MPSNDArraySDPAMaskRandom) Datatype: %s, Dest Datatype: %s\t"
+ "Source tensor data type should be fp16 or fp32 when it is not quantized"
+ "Ti,N,V_maskType"
+ "_maskType"
+ "error: unsupported scaled dot product attention mask type"
+ "initWithDevice:kernelType:maskType:"
+ "initWithDevice:kernelType:maskType:qQuantizationDescriptor:kQuantizationDescriptor:vQuantizationDescriptor:"
+ "initWithDevice:kernelType:maskType:qQuantizationDescriptor:kQuantizationDescriptor:vQuantizationDescriptor:sourceCount:"
+ "initWithDevice:kernelType:maskType:sourceCount:"
+ "maskType"
+ "setMaskType:"
- "@36@0:8@16i24Q28"
- "@52@0:8@16i24@28@36@44"
- "@60@0:8@16i24@28@36@44Q52"
- "SDPA: Batches=%lu, PromptSize=%lu, Contexts=%lu, Heads=%lu, Features=%lu, Q Datatype: %s, K Datatype: %s, V Datatype: %s, Mask Datatype: %s, Dest Datatype: %s\t"
- "Source tensor data type should be fp16 or fp32 when is it not quantized"
- "initWithDevice:kernelType:qQuantizationDescriptor:kQuantizationDescriptor:vQuantizationDescriptor:"
- "initWithDevice:kernelType:qQuantizationDescriptor:kQuantizationDescriptor:vQuantizationDescriptor:sourceCount:"
- "initWithDevice:kernelType:sourceCount:"

```
