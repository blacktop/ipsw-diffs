## CoreIDVAccountNotificationPlugin

> `/System/Library/Accounts/Notification/CoreIDVAccountNotificationPlugin.bundle/CoreIDVAccountNotificationPlugin`

```diff

-7.37.0.0.0
-  __TEXT.__text: 0x253c
+7.100.1.0.0
+  __TEXT.__text: 0x238c
   __TEXT.__auth_stubs: 0x420
   __TEXT.__objc_methlist: 0x50
   __TEXT.__const: 0xe2

   __TEXT.__oslogstring: 0x205
   __TEXT.__swift5_types: 0x8
   __TEXT.__swift5_capture: 0x30
-  __TEXT.__unwind_info: 0xd0
+  __TEXT.__unwind_info: 0xd8
   __TEXT.__objc_classname: 0x26
   __TEXT.__objc_methname: 0x3dc
   __TEXT.__objc_methtype: 0x1f3
   __DATA_CONST.__got: 0x30
-  __DATA_CONST.__const: 0x40
+  __DATA_CONST.__const: 0x80
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x98
   __DATA_CONST.__objc_protorefs: 0x18
   __AUTH_CONST.__auth_got: 0x210
-  __AUTH_CONST.__auth_ptr: 0x20
+  __AUTH_CONST.__auth_ptr: 0x18
   __AUTH_CONST.__const: 0x118
   __AUTH_CONST.__objc_const: 0x568
   __AUTH.__objc_data: 0x190

   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
   Functions: 45
-  Symbols:   65
-  CStrings:  119
+  Symbols:   73
+  CStrings:  0
 
Symbols:
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
CStrings:
- "BuildICmp"
- "LVMBuildIntCast"
- "_LLVMAddCase"
- "_LLVMAddGlobalInAddressSpace"
- "_LLVMArrayType"
- "_LLVMBuildAShr"
- "_LLVMBuildAdd"
- "_LLVMBuildAlloca"
- "_LLVMBuildAnd"
- "_LLVMBuildBr"
- "_LLVMBuildCall"
- "_LLVMBuildCondBr"
- "_LLVMBuildExtractElement"
- "_LLVMBuildExtractValue"
- "_LLVMBuildFAdd"
- "_LLVMBuildFCmp"
- "_LLVMBuildFDiv"
- "_LLVMBuildFMul"
- "_LLVMBuildFNeg"
- "_LLVMBuildFPCast"
- "_LLVMBuildFRem"
- "_LLVMBuildFSub"
- "_LLVMBuildInsertElement"
- "_LLVMBuildInsertValue"
- "_LLVMBuildLShr"
- "_LLVMBuildMul"
- "_LLVMBuildNeg"
- "_LLVMBuildNot"
- "_LLVMBuildOr"
- "_LLVMBuildPhi"
- "_LLVMBuildRet"
- "_LLVMBuildRetVoid"
- "_LLVMBuildSDiv"
- "_LLVMBuildSRem"
- "_LLVMBuildSelect"
- "_LLVMBuildShl"
- "_LLVMBuildShuffleVector"
- "_LLVMBuildSub"
- "_LLVMBuildSwitch"
- "_LLVMBuildUDiv"
- "_LLVMBuildURem"
- "_LLVMBuildXor"
- "_LLVMClearInsertionPosition"
- "_LLVMConstAllOnes"
- "_LLVMConstArray"
- "_LLVMConstInt"
- "_LLVMConstNull"
- "_LLVMConstReal"
- "_LLVMConstVector"
- "_LLVMContextCreate"
- "_LLVMContextDispose"
- "_LLVMCountParamTypes"
- "_LLVMCreateEnumAttribute"
- "_LLVMCreateMemoryBufferWithContentsOfFile"
- "_LLVMCreateMemoryBufferWithMemoryRange"
- "_LLVMCreateMemoryBufferWithMemoryRangeCopy"
- "_LLVMDisposeBuilder"
- "_LLVMDisposeMemoryBuffer"
- "_LLVMDisposeModule"
- "_LLVMDoubleTypeInContext"
- "_LLVMFloatTypeInContext"
- "_LLVMFunctionType"
- "_LLVMGetBufferSize"
- "_LLVMGetBufferStart"
- "_LLVMGetElementType"
- "_LLVMGetEnumAttributeKindForName"
- "_LLVMGetInsertBlock"
- "_LLVMGetIntTypeWidth"
- "_LLVMGetStructName"
- "_LLVMGetTarget"
- "_LLVMGetTypeByName"
- "_LLVMGetTypeKind"
- "_LLVMGetUndef"
- "_LLVMGetVectorSize"
- "_LLVMHalfTypeInContext"
- "_LLVMInt16TypeInContext"
- "_LLVMInt1TypeInContext"
- "_LLVMInt32TypeInContext"
- "_LLVMInt64TypeInContext"
- "_LLVMInt8TypeInContext"
- "_LLVMIntTypeInContext"
- "_LLVMMDNodeInContext"
- "_LLVMMDStringInContext"
- "_LLVMModuleCreateWithNameInContext"
- "_LLVMPointerType"
- "_LLVMSetCurrentDebugLocation"
- "_LLVMSetDataLayout"
- "_LLVMSetGlobalConstant"
- "_LLVMSetInitializer"
- "_LLVMSetTarget"
- "_LLVMStructCreateNamed"
- "_LLVMStructTypeInContext"
- "_LLVMTypeOf"
- "_LLVMVectorType"
- "_LLVMVoidTypeInContext"
- "_ZNK4llvm12StructLayout26getElementContainingOffsetEy"
- "__ZN4llvm10DataLayout5clearEv"
- "__ZN4llvm10DataLayout5resetENS_9StringRefE"
- "__ZN4llvm10DataLayoutD1Ev"
- "__ZN4llvm8Constant19handleOperandChangeEPNS_5ValueES2_"
- "__ZN4llvm9DIBuilder13replaceArraysERPNS_15DICompositeTypeENS_24MDTupleTypedArrayWrapperINS_6DINodeEEES6_"
- "__ZN4llvm9DIBuilder15createArrayTypeEyjPNS_6DITypeENS_24MDTupleTypedArrayWrapperINS_6DINodeEEENS_12PointerUnionIJPNS_12DIExpressionEPNS_10DIVariableEEEESB_SB_SB_"
- "__ZN4llvm9DIBuilder19createTempMacroFileEPNS_11DIMacroFileEjPNS_6DIFileE"
- "__ZN4llvm9DIBuilder19replaceVTableHolderERPNS_15DICompositeTypeEPNS_6DITypeE"
- "__ZN4llvm9DIBuilder20createArtificialTypeEPNS_6DITypeE"
- "__ZN4llvm9DIBuilder8finalizeEv"
- "__ZN4llvm9DIBuilderC1ERNS_6ModuleEbPNS_13DICompileUnitE"
- "__ZNK4llvm10DataLayout14getPointerSizeEj"
- "__ZNK4llvm10DataLayout15getABITypeAlignEPNS_4TypeE"
- "__ZNK4llvm10DataLayout15getStructLayoutEPNS_10StructTypeE"
- "__ZNK4llvm10DataLayout19getPointerAlignElemEj"
- "__ZNK4llvm10DataLayout22getIndexTypeSizeInBitsEPNS_4TypeE"
- "__ZNK4llvm10DataLayout22getPointerABIAlignmentEj"
- "__ZNK4llvm10DataLayout24getPointerTypeSizeInBitsEPNS_4TypeE"
- "__ZNK4llvm12ConstantExpr16getAsInstructionEPNS_11InstructionE"
- "__ZNK4llvm22ConstantDataSequential19getElementAsAPFloatEj"
- "__ZNK4llvm22ConstantDataSequential8isStringEj"
- "__ZNK4llvm22ConstantDataSequential9isCStringEv"
- "m22ConstantDataSequential19getElementAsIntegerEj"

```
