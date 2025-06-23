## MetalTools

> `/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`

```diff

-370.50.4.0.0
-  __TEXT.__text: 0x12a2f4
+370.54.0.0.0
+  __TEXT.__text: 0x12bb2c
   __TEXT.__auth_stubs: 0xc20
-  __TEXT.__objc_methlist: 0x18bcc
-  __TEXT.__cstring: 0x31343
-  __TEXT.__const: 0x308
-  __TEXT.__gcc_except_tab: 0x2b50
+  __TEXT.__objc_methlist: 0x18cb4
+  __TEXT.__cstring: 0x314c5
+  __TEXT.__const: 0x2f8
+  __TEXT.__gcc_except_tab: 0x2b58
   __TEXT.__oslogstring: 0x282e
-  __TEXT.__unwind_info: 0x5040
+  __TEXT.__unwind_info: 0x50a8
   __TEXT.__objc_classname: 0x2520
-  __TEXT.__objc_methname: 0x1e11b
-  __TEXT.__objc_methtype: 0x1795d
-  __TEXT.__objc_stubs: 0x164e0
+  __TEXT.__objc_methname: 0x1e20e
+  __TEXT.__objc_methtype: 0x179cd
+  __TEXT.__objc_stubs: 0x165e0
   __DATA_CONST.__got: 0xae8
   __DATA_CONST.__const: 0x1b28
   __DATA_CONST.__objc_classlist: 0x748
   __DATA_CONST.__objc_protolist: 0x4c8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x60e8
+  __DATA_CONST.__objc_selrefs: 0x6120
   __DATA_CONST.__objc_protorefs: 0xa8
   __DATA_CONST.__objc_superrefs: 0x640
   __AUTH_CONST.__auth_got: 0x620
   __AUTH_CONST.__const: 0x1d0
-  __AUTH_CONST.__cfstring: 0xe2a0
-  __AUTH_CONST.__objc_const: 0x45aa8
+  __AUTH_CONST.__cfstring: 0xe2c0
+  __AUTH_CONST.__objc_const: 0x45b48
   __AUTH.__objc_data: 0x50
   __AUTH.__thread_vars: 0x18
   __AUTH.__thread_bss: 0x1
-  __DATA.__objc_ivar: 0xfe4
+  __DATA.__objc_ivar: 0xfec
   __DATA.__data: 0x3970
   __DATA.__bss: 0x80
   __DATA_DIRTY.__objc_data: 0x4880

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 98E77F70-116E-3CD5-B080-92DFB2F2F3CE
-  Functions: 7641
-  Symbols:   24259
-  CStrings:  10853
+  UUID: 9374291F-FE5F-3B2C-8CA4-8A3E45E0A4FE
+  Functions: 7660
+  Symbols:   24308
+  CStrings:  10874
 
Symbols:
+ -[MTL4DebugCommandBuffer resolveCounterHeap:withRange:intoBuffer:waitFence:updateFence:]
+ -[MTL4GPUDebugCommandBuffer setResidencyForBufferRange:]
+ -[MTL4GPUDebugComputeCommandEncoder blitChildrenWrappersBufferFromAcceleratrionStructure:toAccelerationStructure:]
+ -[MTL4GPUDebugComputeCommandEncoder eventID]
+ -[MTL4GPUDebugComputeCommandEncoder resetCommandsInBuffer:withRange:]
+ -[MTL4GPUDebugComputeCommandEncoder retrieveBufferFromBufferRange:]
+ -[MTL4GPUDebugRenderCommandEncoder eventID]
+ -[MTL4GPUDebugRenderCommandEncoder setObjectThreadgroupMemoryLength:atIndex:]
+ -[MTL4ToolsCommandBuffer resolveCounterHeap:withRange:intoBuffer:waitFence:updateFence:]
+ -[MTLDebugComputeCommandEncoder validateComputeFunctionArgumentsCommon]
+ -[MTLDebugComputeCommandEncoder validateComputeFunctionArgumentsCommon].cold.1
+ -[MTLDebugComputeCommandEncoder validateComputeFunctionArgumentsCommon].cold.2
+ -[MTLDebugComputeCommandEncoder validateComputeFunctionArgumentsCommon].cold.3
+ -[MTLDebugDevice functionHandleWithBinaryFunction:]
+ -[MTLDebugRenderCommandEncoder _validateTessellationWithMetal4]
+ -[MTLGPUDebugDevice newArchiveWithURL:error:]
+ -[MTLGPUDebugRenderCommandEncoder setObjectThreadgroupMemoryLength:atIndex:]
+ -[MTLGPUDebugRenderCommandEncoder setTessellationFactorBuffer:offset:instanceStride:]
+ -[MTLToolsDevice newUnwrappedMTL4CompilerDescriptor:]
+ -[MTLToolsDevice supportsAtomicFloat]
+ GCC_except_table180
+ GCC_except_table183
+ GCC_except_table187
+ GCC_except_table198
+ GCC_except_table204
+ GCC_except_table208
+ GCC_except_table227
+ GCC_except_table237
+ GCC_except_table36
+ _MTLArgumentTypeToString
+ _OBJC_IVAR_$_MTL4GPUDebugRenderCommandEncoder._objectThreadgroup
+ _OBJC_IVAR_$_MTLGPUDebugRenderCommandEncoder._objectThreadgroup
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTL4CompilerSPI
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTL4CompilerSPI
+ ___block_literal_global.1656
+ ___newDebugFunctionHandleWithBinaryFunction_block_invoke
+ ___newDebugFunctionHandleWithFunction_block_invoke
+ ___newDebugFunctionHandle_block_invoke
+ _newDebugFunctionHandle
+ _newDebugFunctionHandleWithBinaryFunction
+ _newDebugFunctionHandleWithFunction
+ _objc_msgSend$_validateTessellationWithMetal4
+ _objc_msgSend$eventID
+ _objc_msgSend$newUnwrappedMTL4CompilerDescriptor:
+ _objc_msgSend$resolveCounterHeap:withRange:intoBuffer:waitFence:updateFence:
+ _objc_msgSend$retrieveBufferFromBufferRange:
+ _objc_msgSend$setResidencyForBufferRange:
+ _objc_msgSend$supportsAtomicFloat
+ _objc_msgSend$validateComputeFunctionArgumentsCommon
- -[MTLToolsDevice newUnwrappedMTL4LinkedFunctions:]
- GCC_except_table175
- GCC_except_table179
- GCC_except_table182
- GCC_except_table186
- GCC_except_table197
- GCC_except_table206
- GCC_except_table226
- GCC_except_table236
- GCC_except_table53
- GCC_except_table81
- GCC_except_table91
- _OBJC_CLASS_$_MTLLogicalToPhysicalColorAttachmentMapSPI
- __ZL20argumentTypeToString15MTLArgumentType
- __ZL20argumentTypeToString22MTLArgumentTypePrivate
- __ZL32validateComputeFunctionArgumentsPU19objcproto9MTLDevice11objc_objectP8NSStringS2_P7NSArrayP24MTLDebugFunctionArgumentmS6_mS6_myS6_mmmb
- __ZL32validateComputeFunctionArgumentsPU19objcproto9MTLDevice11objc_objectP8NSStringS2_P7NSArrayP24MTLDebugFunctionArgumentmS6_mS6_myS6_mmmb.cold.1
- __ZL32validateComputeFunctionArgumentsPU19objcproto9MTLDevice11objc_objectP8NSStringS2_P7NSArrayP24MTLDebugFunctionArgumentmS6_mS6_myS6_mmmb.cold.2
- __ZL32validateComputeFunctionArgumentsPU19objcproto9MTLDevice11objc_objectP8NSStringS2_P7NSArrayP24MTLDebugFunctionArgumentmS6_mS6_myS6_mmmb.cold.3
- ___block_literal_global.1657
CStrings:
+ "%@ Function(%@): %s binding at index %lu for %@ cannot be null."
+ "%@ Function(%@): %s binding at index %lu for %@ should have been set with setAddress:atIndex:."
+ "%@ Function(%@): %s binding at index %lu for %@ should have been set with setResource:atBufferIndex:."
+ "%@ Function(%@): %s binding at index %lu for %@ was never set."
+ "%@ Function(%@): missing %s binding at index %lu for %@. %@."
+ "%@ Function(%@): missing sampler binding at index %lu for %@. %@."
+ "%@ Function(%@): missing texture binding at index %lu for %@. %@."
+ "-[MTL4DebugCommandBuffer resolveCounterHeap:withRange:intoBuffer:waitFence:updateFence:]"
+ "-[MTLDebugRenderCommandEncoder _validateTessellationWithMetal4]"
+ "-[MTLDebugRenderCommandEncoder setColorAttachmentMap:]"
+ "@32@0:8{MTL4BufferRange=QQ}16"
+ "Argument table only supports %lu buffer bindings"
+ "Argument table only supports %lu sampler bindings"
+ "Argument table only supports %lu texture bindings"
+ "Metal 4 does not support raytracing with software emulation."
+ "No argument table set for %@ stage"
+ "Pipeline states created with a MTL4Compiler or MTL4Archive do not support tessellation."
+ "Set Color Attachment Map Validation"
+ "Tessellation Pipeline Validation"
+ "_objectThreadgroup"
+ "_validateTessellationWithMetal4"
+ "buffer.bufferAddress must not be nil."
+ "dst_buffer"
+ "dst_descriptor_buffer"
+ "eventID"
+ "instance_count"
+ "instance_offset"
+ "instance_stride"
+ "newUnwrappedMTL4CompilerDescriptor:"
+ "resolveCounterHeap:withRange:intoBuffer:waitFence:updateFence:"
+ "retrieveBufferFromBufferRange:"
+ "setResidencyForBufferRange:"
+ "supportsAtomicFloat"
+ "v32@0:8{MTL4BufferRange=QQ}16"
+ "v72@0:8@\"<MTL4CounterHeap>\"16{_NSRange=QQ}24{MTL4BufferRange=QQ}40@\"<MTLFence>\"56@\"<MTLFence>\"64"
+ "v72@0:8@16{_NSRange=QQ}24{MTL4BufferRange=QQ}40@56@64"
+ "validateComputeFunctionArgumentsCommon"
- "%@ Function(%@): %@ binding at index %lu for %@ cannot be null."
- "%@ Function(%@): %@ binding at index %lu for %@ should have been set with setAddress:atIndex:."
- "%@ Function(%@): %@ binding at index %lu for %@ should have been set with setResource:atBufferIndex:."
- "%@ Function(%@): %@ binding at index %lu for %@ was never set."
- "%@ Function(%@): missing %@ binding at index %lu for %@. Argument table only supports %lu buffer bindings."
- "%@ Function(%@): missing sampler binding at index %lu for %@. Argument table only supports %lu sampler bindings."
- "%@ Function(%@): missing texture binding at index %lu for %@. Argument table only supports %lu texture bindings."
- "@\"MTLLogicalToPhysicalColorAttachmentMapSPI\""
- "copy_and_unwrap_mtl4_acceleration_structure_descriptor_buffer"
- "instanceAccelerationStructure"
- "local memory"
- "mapping should not be nil."
- "newUnwrappedMTL4LinkedFunctions:"
- "primitiveAccelerationStructure"
- "threadgroupMemory"
- "v24@0:8@\"MTLLogicalToPhysicalColorAttachmentMapSPI\"16"
- "visibleFunctionTable"

```
