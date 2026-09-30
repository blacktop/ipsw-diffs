## CoreIDVAccountNotificationPlugin

> `/System/Library/Accounts/Notification/CoreIDVAccountNotificationPlugin.bundle/CoreIDVAccountNotificationPlugin`

```diff

-7.37.0.0.0
-  __TEXT.__text: 0x253c
+7.40.1.0.0
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
-  CStrings:  37
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
- "6_EE11InvalidatorE"
- "7CGSCCUpdateResultE"
- "__ZN4llvm13CallGraphNode15replaceCallEdgeERNS_8CallBaseES2_PS0_"
- "__ZN4llvm13CallGraphNode19removeAnyCallEdgeToEPS0_"
- "__ZN4llvm13DirectedGraphINS_7DDGNodeENS_7DDGEdgeEE10removeNodeERS1_"
- "__ZN4llvm15AnalysisManagerINS_4LoopEJRNS_27LoopStandardAnalysisResultsEEE10invalidateERS1_RKNS_17PreservedAnalysesE"
- "__ZN4llvm15AnalysisManagerINS_4LoopEJRNS_27LoopStandardAnalysisResultsEEE13getResultImplEPNS_11AnalysisKeyERS1_S3_"
- "__ZN4llvm15AnalysisManagerINS_4LoopEJRNS_27LoopStandardAnalysisResultsEEE5clearERS1_NS_9StringRefE"
- "__ZN4llvm15callDefaultCtorINS_20CycleInfoWrapperPassEEEPNS_4PassEv"
- "__ZN4llvm15callDefaultCtorINS_30GPUFunctionAnalysisWrapperPassEEEPNS_4PassEv"
- "__ZN4llvm16GenericCycleInfoINS_17GenericSSAContextINS_8FunctionEEEE28moveTopLevelCycleToNewParentEPNS_12GenericCycleIS3_EES7_"
- "__ZN4llvm16GenericCycleInfoINS_17GenericSSAContextINS_8FunctionEEEE7computeERS2_"
- "__ZN4llvm20ConstantFoldConstantEPKNS_8ConstantERKNS_10DataLayoutEPKNS_17TargetLibraryInfoE"
- "__ZN4llvm20getBestSimplifyQueryINS_8FunctionEJEEEKNS_13SimplifyQueryERNS_15AnalysisManagerIT_JDpT0_EEERS1_"
- "__ZN4llvm22RecomputeGlobalsAAPass3runERNS_6ModuleERNS_15AnalysisManagerIS1_JEEE"
- "__ZN4llvm23ConstantFoldInstructionEPNS_11InstructionERKNS_10DataLayoutEPKNS_17TargetLibraryInfoE"
- "__ZN4llvm25ConstantFoldLoadFromConstEPNS_8ConstantEPNS_4TypeERKNS_5APIntERKNS_10DataLayoutE"
- "__ZN4llvm26PointerMayBeCapturedBeforeEPKNS_5ValueEbbPKNS_11InstructionEPKNS_13DominatorTreeEbjPKNS_8LoopInfoE"
- "__ZN4llvm30AbstractDependenceGraphBuilderINS_19DataDependenceGraphEE14createPiBlocksEv"
- "__ZN4llvm30AbstractDependenceGraphBuilderINS_19DataDependenceGraphEE22sortNodesTopologicallyEv"
- "__ZN4llvm9CallGraph19getOrInsertFunctionEPKNS_8FunctionE"
- "__ZN4llvm9CallGraph24removeFunctionFromModuleEPNS_13CallGraphNodeE"
- "__ZN4llvm9CallGraphC1ERNS_6ModuleE"
- "__ZN4llvm9CallGraphD1Ev"
- "__ZNK4llvm12GenericCycleINS_17GenericSSAContextINS_8FunctionEEEE19getCyclePredecessorEv"
- "__ZNK4llvm15AnalysisManagerINS_4LoopEJRNS_27LoopStandardAnalysisResultsEEE19getCachedResultImplEPNS_11AnalysisKeyERS1_"
- "__ZNK4llvm16GenericCycleInfoINS_17GenericSSAContextINS_8FunctionEEEE5printERNS_11raw_ostreamE"
- "__ZNK4llvm21DominanceFrontierBaseINS_10BasicBlockELb0EE13compareDomSetERNSt3__13setIPS1_NS3_4lessIS5_EENS3_9allocatorIS5_EEEERKSA_"
- "__ZNK4llvm21DominanceFrontierBaseINS_10BasicBlockELb0EE5printERNS_11raw_ostreamE"
- "__ZNK4llvm8LoopBaseINS_10BasicBlockENS_4LoopEE11isLoopLatchEPKS1_"
- "__ZNK4llvm8LoopBaseINS_10BasicBlockENS_4LoopEE13getExitBlocksERNS_15SmallVectorImplIPS1_EE"
- "__ZNK4llvm8LoopBaseINS_10BasicBlockENS_4LoopEE13isLoopExitingEPKS1_"
- "__ZNK4llvm8LoopBaseINS_10BasicBlockENS_4LoopEE15getExitingBlockEv"
- "__ZNK4llvm8LoopBaseINS_10BasicBlockENS_4LoopEE15getNumBackEdgesEv"
- "__ZNK4llvm8LoopBaseINS_10BasicBlockENS_4LoopEE16getExitingBlocksERNS_15SmallVectorImplIPS1_EE"
- "seINS_10BasicBlockEE9calculateERKNS_17DominatorTreeBaseIS1_Lb0EEEPKNS_15DomTreeNodeBaseIS1_EE"
- "tDependenceGraphBuilderINS_19DataDependenceGraphEE24createAndConnectRootNodeEv"

```
