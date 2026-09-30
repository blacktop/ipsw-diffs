## JavaScriptCore

> `/System/Library/Frameworks/JavaScriptCore.framework/JavaScriptCore`

```diff

-621.2.5.10.10
-  __TEXT.__text: 0x184bd6c
+621.3.6.10.1
+  __TEXT.__text: 0x185686c
   __TEXT.__jsc_int: 0x7e260
   __TEXT.__auth_stubs: 0x2d90
   __TEXT.__objc_methlist: 0xb9c
-  __TEXT.__const: 0x8b6f8
-  __TEXT.__cstring: 0xd8075
+  __TEXT.__const: 0x8b708
+  __TEXT.__cstring: 0xd7ff4
   __TEXT.__gcc_except_tab: 0x235c
   __TEXT.__oslogstring: 0x5bd
   __TEXT.__unwind_info: 0x21e8

   __AUTH.__data: 0xa0
   __DATA.__objc_ivar: 0x80
   __DATA.__data: 0x370
-  __DATA.__bss: 0x153a
-  __DATA.__common: 0x1db8
+  __DATA.__bss: 0x1542
+  __DATA.__common: 0x1dc8
   __DATA_DIRTY.__objc_ivar: 0x8
   __DATA_DIRTY.__objc_data: 0x2d0
   __DATA_DIRTY.__data: 0x16ac8
   __DATA_DIRTY.__common: 0x1037c
-  __DATA_DIRTY.__bss: 0x3288
+  __DATA_DIRTY.__bss: 0x3270
   - /System/Library/Frameworks/BrowserEngineCore.framework/BrowserEngineCore
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E32426AF-6411-3260-BE0B-BE0AD12E23C8
-  Functions: 41702
-  Symbols:   84237
-  CStrings:  19908
+  UUID: 7D5C6566-108A-3751-A2F1-E6F78BE5996C
+  Functions: 41707
+  Symbols:   84244
+  CStrings:  19915
 
Symbols:
+ __MergedGlobals.34
+ __ZN3JSC11jsSubstringEPNS_14JSGlobalObjectEPNS_8JSStringEjj
+ __ZN3JSC14JSGlobalObject24canDeclareGlobalFunctionERKNS_10IdentifierE
+ __ZN3JSC18tryJSSubstringImplERNS_2VMEPNS_14JSGlobalObjectEPNS_8JSStringEjj
+ __ZN3JSC3DFG13SSACalculator11newVariableEv
+ __ZN3JSC3DFG15AvailabilityMap16filterByLivenessERNS0_5GraphENS_10CodeOriginE
+ __ZN3JSC3DFG15AvailabilityMap5clearEv
+ __ZN3JSC3DFG9runAndLogINS0_28OSRAvailabilityAnalysisPhaseIZNS0_30performOSRAvailabilityAnalysisERNS0_5GraphEE3$_0ZNS0_30performOSRAvailabilityAnalysisES4_E3$_1EEEEbRT_
+ __ZN3WTF7HashMapIN3JSC3DFG20PromotedHeapLocationENS2_12AvailabilityENS_11DefaultHashIS3_EENS_10HashTraitsIS3_EENS7_IS4_EENS_15HashTableTraitsELNS_17ShouldValidateKeyE0EE3addIS4_EENS_18HashTableAddResultINS_17HashTableIteratorINS_9HashTableIS3_NS_12KeyValuePairIS3_S4_EENS_24KeyValuePairKeyExtractorISI_EES6_NSC_18KeyValuePairTraitsES8_LSB_0EEES3_SI_SK_S6_SL_S8_EEEERKS3_OT_
+ __ZN3WTF9toCStringIJA36_cN3JSC3DFG12AvailabilityEA51_cS4_A6_cNS3_15AvailabilityMapEEEENS_7CStringEDpRKT_
+ __ZN3WTF9toCStringIJA38_cN3JSC3DFG12AvailabilityEA33_cS4_A58_cNS3_15AvailabilityMapEEEENS_7CStringEDpRKT_
+ __ZNK3JSC3DFG15AvailabilityMap20validateAvailabilityERNS0_5GraphEPNS0_4NodeE
+ __ZZN3JSC3DFG30LocalOSRAvailabilityCalculator11executeNodeEPNS0_4NodeEENK3$_0clENS_7OperandE
+ __ZZN3JSC4Wasm18JSEntrypointCallee23calleeSaveRegistersImplEvE14initializeFlag
+ __ZZN3JSC4Wasm18JSEntrypointCallee23calleeSaveRegistersImplEvE19calleeSaveRegisters
+ __ZZNK3JSC13PropertyTable15forEachPropertyIZNS_9Structure15forEachPropertyIZNS_21globalFuncCloneObjectEPNS_14JSGlobalObjectEPNS_9CallFrameEE3$_0EEvRNS_2VMERKT_EUlSD_E_EEvSD_ENKUlPSC_E_clIjEEDaSF_
+ _pas_debug_heap_malloc_compact
+ _pas_debug_heap_memalign_compact
+ _pas_debug_heap_realloc_compact
- __MergedGlobals.28
- __ZN3JSC11SymbolTable8containsERKNS_18ConcurrentJSLockerEPN3WTF17UniquedStringImplE
- __ZN3JSC14JSGlobalObject19canDeclareGlobalVarERKNS_10IdentifierE
- __ZN3JSC20StrictEvalActivation6createERNS_2VMEPNS_9StructureEPNS_7JSScopeE
- __ZN3JSC3DFG15AvailabilityMapaSERKS1_
- __ZN3JSC3DFG19uncheckedUseKindForENS0_11FlushFormatE
- __ZN3JSC3DFG9resultForENS0_11FlushFormatE
- __ZN3JSC4Wasm6Thunks9singletonEv
- __ZN3WTF6VectorIN3JSC4Yarr22YarrPatternConstructor26UnresolvedForwardReferenceELm0ENS_15CrashOnOverflowELm16ENS_10FastMallocEE14appendSlowCaseILNS_13FailureActionE0ES4_EEbOT0_
- __ZN3WTF7CodePtrILNS_6PtrTagE45961ELNS_18FunctionAttributesE0EEC1IN3JSC24ExceptionOperationResultIPNS5_4Wasm18JSEntrypointCalleeEEEJPvPNS5_9CallFrameEPNS5_19WebAssemblyFunctionEEEEPFT_DpT0_E
- __ZN3WTF7CodePtrILNS_6PtrTagE45961ELNS_18FunctionAttributesE0EEC1IN3JSC24ExceptionOperationResultIxEEJPvPNS5_9CallFrameEEEEPFT_DpT0_E
- __ZNK3JSC14JSGlobalObject29strictEvalActivationStructureEv
- __ZNK3JSC15BaseInstructionINS_14JSOpcodeTraitsEE2asINS_12OpTryGetByIdEEET_v
- __ZNK3WTF7HashMapINS_6RefPtrINS_17UniquedStringImplENS_15PackedPtrTraitsIS2_EENS_21DefaultRefDerefTraitsIS2_EEEEN3JSC24VariableEnvironmentEntryENS8_17IdentifierRepHashENS_10HashTraitsINS1_IS2_NS_12RawPtrTraitsIS2_EES6_EEEENS8_34VariableEnvironmentEntryHashTraitsENS_15HashTableTraitsELNS_17ShouldValidateKeyE0EE5beginEv
- __ZZN3JSC4Wasm23createJSToWasmJITSharedEvENK3$_0clEv
- ___PRETTY_FUNCTION__._ZN3JSC11Interpreter11executeEvalEPNS_14EvalExecutableENS_7JSValueEPNS_7JSScopeE
CStrings:
+ " and local flushed availability "
+ " disagree on which DFG node the same stack slot holds in "
+ ") but corresponding local doesn't exist or match ("
+ "./dfg/DFGAvailabilityMap.cpp"
+ "/AppleInternal/Library/BuildRoots/4~B2u3ugCy99ild0-JyUofanj0wJJZuh-waK-eeI8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/Assertions.h"
+ "/AppleInternal/Library/BuildRoots/4~B2u3ugCy99ild0-JyUofanj0wJJZuh-waK-eeI8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/ConcurrentPtrHashSet.h"
+ "/AppleInternal/Library/BuildRoots/4~B2u3ugCy99ild0-JyUofanj0wJJZuh-waK-eeI8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/Deque.h"
+ "/AppleInternal/Library/BuildRoots/4~B2u3ugCy99ild0-JyUofanj0wJJZuh-waK-eeI8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/Dominators.h"
+ "/AppleInternal/Library/BuildRoots/4~B2u3ugCy99ild0-JyUofanj0wJJZuh-waK-eeI8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/FastBitVector.h"
+ "/AppleInternal/Library/BuildRoots/4~B2u3ugCy99ild0-JyUofanj0wJJZuh-waK-eeI8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/HashTable.h"
+ "/AppleInternal/Library/BuildRoots/4~B2u3ugCy99ild0-JyUofanj0wJJZuh-waK-eeI8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/IndexMap.h"
+ "/AppleInternal/Library/BuildRoots/4~B2u3ugCy99ild0-JyUofanj0wJJZuh-waK-eeI8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/JSONValues.h"
+ "/AppleInternal/Library/BuildRoots/4~B2u3ugCy99ild0-JyUofanj0wJJZuh-waK-eeI8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/LazyRef.h"
+ "/AppleInternal/Library/BuildRoots/4~B2u3ugCy99ild0-JyUofanj0wJJZuh-waK-eeI8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/LazyUniqueRef.h"
+ "/AppleInternal/Library/BuildRoots/4~B2u3ugCy99ild0-JyUofanj0wJJZuh-waK-eeI8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/Liveness.h"
+ "/AppleInternal/Library/BuildRoots/4~B2u3ugCy99ild0-JyUofanj0wJJZuh-waK-eeI8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/LockAlgorithmInlines.h"
+ "/AppleInternal/Library/BuildRoots/4~B2u3ugCy99ild0-JyUofanj0wJJZuh-waK-eeI8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/Markable.h"
+ "/AppleInternal/Library/BuildRoots/4~B2u3ugCy99ild0-JyUofanj0wJJZuh-waK-eeI8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/NaturalLoops.h"
+ "/AppleInternal/Library/BuildRoots/4~B2u3ugCy99ild0-JyUofanj0wJJZuh-waK-eeI8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/RedBlackTree.h"
+ "/AppleInternal/Library/BuildRoots/4~B2u3ugCy99ild0-JyUofanj0wJJZuh-waK-eeI8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/RefCounted.h"
+ "/AppleInternal/Library/BuildRoots/4~B2u3ugCy99ild0-JyUofanj0wJJZuh-waK-eeI8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/SinglyLinkedListWithTail.h"
+ "/AppleInternal/Library/BuildRoots/4~B2u3ugCy99ild0-JyUofanj0wJJZuh-waK-eeI8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/StdLibExtras.h"
+ "/AppleInternal/Library/BuildRoots/4~B2u3ugCy99ild0-JyUofanj0wJJZuh-waK-eeI8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/ThreadSafeWeakHashSet.h"
+ "/AppleInternal/Library/BuildRoots/4~B2u3ugCy99ild0-JyUofanj0wJJZuh-waK-eeI8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/ThreadSpecific.h"
+ "/AppleInternal/Library/BuildRoots/4~B2u3ugCy99ild0-JyUofanj0wJJZuh-waK-eeI8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/TrailingArray.h"
+ "/AppleInternal/Library/BuildRoots/4~B2u3ugCy99ild0-JyUofanj0wJJZuh-waK-eeI8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/WeakPtr.h"
+ "/AppleInternal/Library/BuildRoots/4~B2u3ugCy99ild0-JyUofanj0wJJZuh-waK-eeI8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/text/StringBuilder.h"
+ "/AppleInternal/Library/BuildRoots/4~B2u3ugCy99ild0-JyUofanj0wJJZuh-waK-eeI8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/text/StringConcatenate.h"
+ "/AppleInternal/Library/BuildRoots/4~B2u3ugCy99ild0-JyUofanj0wJJZuh-waK-eeI8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/text/StringImpl.h"
+ "LValue JSC::FTL::(anonymous namespace)::LowerDFGToB3::emitCodeBasedOnEndiannessBranch(LValue, const F1 &, const F2 &) [F1 = (lambda at /Library/Caches/com.apple.xbs/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:18422:45), F2 = (lambda at /Library/Caches/com.apple.xbs/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:18428:42)]"
+ "LValue JSC::FTL::(anonymous namespace)::LowerDFGToB3::emitCodeBasedOnEndiannessBranch(LValue, const F1 &, const F2 &) [F1 = (lambda at /Library/Caches/com.apple.xbs/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:18459:49), F2 = (lambda at /Library/Caches/com.apple.xbs/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:18462:46)]"
+ "LValue JSC::FTL::(anonymous namespace)::LowerDFGToB3::emitCodeBasedOnEndiannessBranch(LValue, const F1 &, const F2 &) [F1 = (lambda at /Library/Caches/com.apple.xbs/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:18482:45), F2 = (lambda at /Library/Caches/com.apple.xbs/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:18486:42)]"
+ "LValue JSC::FTL::(anonymous namespace)::LowerDFGToB3::emitCodeBasedOnEndiannessBranch(LValue, const F1 &, const F2 &) [F1 = (lambda at /Library/Caches/com.apple.xbs/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:18511:45), F2 = (lambda at /Library/Caches/com.apple.xbs/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:18515:42)]"
+ "LValue JSC::FTL::(anonymous namespace)::LowerDFGToB3::emitCodeBasedOnEndiannessBranch(LValue, const F1 &, const F2 &) [F1 = (lambda at /Library/Caches/com.apple.xbs/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:18540:45), F2 = (lambda at /Library/Caches/com.apple.xbs/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:18544:42)]"
+ "Materialization flushed availability "
+ "Materialization should be flushed ("
+ "argument type cannot be a V128 or exnref"
+ "auto JSC::FTL::(anonymous namespace)::LowerDFGToB3::compileCallOrConstructVarargsSpread()::(anonymous class)::operator()(auto, Node *) const [self:auto = std::reference_wrapper<const WTF::RecursableLambda<(lambda at /Library/Caches/com.apple.xbs/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:12128:70)>>]"
+ "auto JSC::FTL::(anonymous namespace)::LowerDFGToB3::compileForwardVarargsWithSpread()::(anonymous class)::operator()(auto, Node *, LValue) const [self:auto = std::reference_wrapper<const WTF::RecursableLambda<(lambda at /Library/Caches/com.apple.xbs/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:13170:47)>>]"
+ "bool JSC::DFG::OSRAvailabilityAnalysisPhase<(lambda at ./dfg/DFGOSRAvailabilityAnalysisPhase.cpp:204:31), (lambda at ./dfg/DFGOSRAvailabilityAnalysisPhase.cpp:205:31)>::run() [HeadFunctor = (lambda at ./dfg/DFGOSRAvailabilityAnalysisPhase.cpp:204:31), TailFunctor = (lambda at ./dfg/DFGOSRAvailabilityAnalysisPhase.cpp:205:31)]"
+ "bool JSC::DFG::OSRAvailabilityAnalysisPhase<(lambda at ./dfg/DFGOSRAvailabilityAnalysisPhase.cpp:219:31), (lambda at ./dfg/DFGOSRAvailabilityAnalysisPhase.cpp:220:31)>::run() [HeadFunctor = (lambda at ./dfg/DFGOSRAvailabilityAnalysisPhase.cpp:219:31), TailFunctor = (lambda at ./dfg/DFGOSRAvailabilityAnalysisPhase.cpp:220:31)]"
+ "heapPair.value.hasNode()"
+ "void JSC::DFG::AvailabilityMap::validateAvailability(Graph &, Node *) const"
+ "void JSC::DFG::PreciseLocalClobberizeAdaptor<(lambda at ./dfg/DFGPutStackSinkingPhase.cpp:109:42), (lambda at ./dfg/DFGPutStackSinkingPhase.cpp:117:41), (lambda at ./dfg/DFGPutStackSinkingPhase.cpp:127:25)>::def(HeapLocation, LazyNode) [ReadFunctor = (lambda at ./dfg/DFGPutStackSinkingPhase.cpp:109:42), WriteFunctor = (lambda at ./dfg/DFGPutStackSinkingPhase.cpp:117:41), DefFunctor = (lambda at ./dfg/DFGPutStackSinkingPhase.cpp:127:25)]"
+ "void JSC::DFG::PreciseLocalClobberizeAdaptor<(lambda at ./dfg/DFGPutStackSinkingPhase.cpp:109:42), (lambda at ./dfg/DFGPutStackSinkingPhase.cpp:117:41), (lambda at ./dfg/DFGPutStackSinkingPhase.cpp:127:25)>::write(AbstractHeap) [ReadFunctor = (lambda at ./dfg/DFGPutStackSinkingPhase.cpp:109:42), WriteFunctor = (lambda at ./dfg/DFGPutStackSinkingPhase.cpp:117:41), DefFunctor = (lambda at ./dfg/DFGPutStackSinkingPhase.cpp:127:25)]"
+ "void JSC::DFG::PreciseLocalClobberizeAdaptor<(lambda at ./dfg/DFGPutStackSinkingPhase.cpp:286:42), (lambda at ./dfg/DFGPutStackSinkingPhase.cpp:295:41), (lambda at ./dfg/DFGPutStackSinkingPhase.cpp:306:25)>::def(HeapLocation, LazyNode) [ReadFunctor = (lambda at ./dfg/DFGPutStackSinkingPhase.cpp:286:42), WriteFunctor = (lambda at ./dfg/DFGPutStackSinkingPhase.cpp:295:41), DefFunctor = (lambda at ./dfg/DFGPutStackSinkingPhase.cpp:306:25)]"
+ "void JSC::DFG::PreciseLocalClobberizeAdaptor<(lambda at ./dfg/DFGPutStackSinkingPhase.cpp:286:42), (lambda at ./dfg/DFGPutStackSinkingPhase.cpp:295:41), (lambda at ./dfg/DFGPutStackSinkingPhase.cpp:306:25)>::write(AbstractHeap) [ReadFunctor = (lambda at ./dfg/DFGPutStackSinkingPhase.cpp:286:42), WriteFunctor = (lambda at ./dfg/DFGPutStackSinkingPhase.cpp:295:41), DefFunctor = (lambda at ./dfg/DFGPutStackSinkingPhase.cpp:306:25)]"
+ "void JSC::DFG::PreciseLocalClobberizeAdaptor<(lambda at ./dfg/DFGPutStackSinkingPhase.cpp:488:42), (lambda at ./dfg/DFGPutStackSinkingPhase.cpp:520:41), (lambda at ./dfg/DFGPutStackSinkingPhase.cpp:534:25)>::def(HeapLocation, LazyNode) [ReadFunctor = (lambda at ./dfg/DFGPutStackSinkingPhase.cpp:488:42), WriteFunctor = (lambda at ./dfg/DFGPutStackSinkingPhase.cpp:520:41), DefFunctor = (lambda at ./dfg/DFGPutStackSinkingPhase.cpp:534:25)]"
+ "void JSC::DFG::PreciseLocalClobberizeAdaptor<(lambda at ./dfg/DFGPutStackSinkingPhase.cpp:488:42), (lambda at ./dfg/DFGPutStackSinkingPhase.cpp:520:41), (lambda at ./dfg/DFGPutStackSinkingPhase.cpp:534:25)>::write(AbstractHeap) [ReadFunctor = (lambda at ./dfg/DFGPutStackSinkingPhase.cpp:488:42), WriteFunctor = (lambda at ./dfg/DFGPutStackSinkingPhase.cpp:520:41), DefFunctor = (lambda at ./dfg/DFGPutStackSinkingPhase.cpp:534:25)]"
+ "void JSC::DFG::SSACalculator::computePhis(const Invocable<Node *(Variable *, BasicBlock *)> auto &) [functor:auto = (lambda at ./dfg/DFGPutStackSinkingPhase.cpp:389:13)]"
+ "void JSC::DFG::clobberize(Graph &, Node *, const ReadFunctor &, const WriteFunctor &, const DefFunctor &, const ClobberTopFunctor &) [ReadFunctor = (lambda at /Library/Caches/com.apple.xbs/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:1905:41), WriteFunctor = (lambda at /Library/Caches/com.apple.xbs/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:1905:59), DefFunctor = (lambda at /Library/Caches/com.apple.xbs/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:1905:77), ClobberTopFunctor = (lambda at /Library/Caches/com.apple.xbs/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:1901:39)]"
+ "void JSC::DFG::clobberize(Graph &, Node *, const ReadFunctor &, const WriteFunctor &, const DefFunctor &, const ClobberTopFunctor &) [ReadFunctor = JSC::DFG::ReadMethodClobberize<JSC::DFG::PreciseLocalClobberizeAdaptor<(lambda at ./dfg/DFGPutStackSinkingPhase.cpp:109:42), (lambda at ./dfg/DFGPutStackSinkingPhase.cpp:117:41), (lambda at ./dfg/DFGPutStackSinkingPhase.cpp:127:25)>>, WriteFunctor = JSC::DFG::WriteMethodClobberize<JSC::DFG::PreciseLocalClobberizeAdaptor<(lambda at ./dfg/DFGPutStackSinkingPhase.cpp:109:42), (lambda at ./dfg/DFGPutStackSinkingPhase.cpp:117:41), (lambda at ./dfg/DFGPutStackSinkingPhase.cpp:127:25)>>, DefFunctor = JSC::DFG::DefMethodClobberize<JSC::DFG::PreciseLocalClobberizeAdaptor<(lambda at ./dfg/DFGPutStackSinkingPhase.cpp:109:42), (lambda at ./dfg/DFGPutStackSinkingPhase.cpp:117:41), (lambda at ./dfg/DFGPutStackSinkingPhase.cpp:127:25)>>, ClobberTopFunctor = (lambda at ./dfg/DFGClobberize.h:45:47)]"
+ "void JSC::DFG::clobberize(Graph &, Node *, const ReadFunctor &, const WriteFunctor &, const DefFunctor &, const ClobberTopFunctor &) [ReadFunctor = JSC::DFG::ReadMethodClobberize<JSC::DFG::PreciseLocalClobberizeAdaptor<(lambda at ./dfg/DFGPutStackSinkingPhase.cpp:286:42), (lambda at ./dfg/DFGPutStackSinkingPhase.cpp:295:41), (lambda at ./dfg/DFGPutStackSinkingPhase.cpp:306:25)>>, WriteFunctor = JSC::DFG::WriteMethodClobberize<JSC::DFG::PreciseLocalClobberizeAdaptor<(lambda at ./dfg/DFGPutStackSinkingPhase.cpp:286:42), (lambda at ./dfg/DFGPutStackSinkingPhase.cpp:295:41), (lambda at ./dfg/DFGPutStackSinkingPhase.cpp:306:25)>>, DefFunctor = JSC::DFG::DefMethodClobberize<JSC::DFG::PreciseLocalClobberizeAdaptor<(lambda at ./dfg/DFGPutStackSinkingPhase.cpp:286:42), (lambda at ./dfg/DFGPutStackSinkingPhase.cpp:295:41), (lambda at ./dfg/DFGPutStackSinkingPhase.cpp:306:25)>>, ClobberTopFunctor = (lambda at ./dfg/DFGClobberize.h:45:47)]"
+ "void JSC::DFG::clobberize(Graph &, Node *, const ReadFunctor &, const WriteFunctor &, const DefFunctor &, const ClobberTopFunctor &) [ReadFunctor = JSC::DFG::ReadMethodClobberize<JSC::DFG::PreciseLocalClobberizeAdaptor<(lambda at ./dfg/DFGPutStackSinkingPhase.cpp:488:42), (lambda at ./dfg/DFGPutStackSinkingPhase.cpp:520:41), (lambda at ./dfg/DFGPutStackSinkingPhase.cpp:534:25)>>, WriteFunctor = JSC::DFG::WriteMethodClobberize<JSC::DFG::PreciseLocalClobberizeAdaptor<(lambda at ./dfg/DFGPutStackSinkingPhase.cpp:488:42), (lambda at ./dfg/DFGPutStackSinkingPhase.cpp:520:41), (lambda at ./dfg/DFGPutStackSinkingPhase.cpp:534:25)>>, DefFunctor = JSC::DFG::DefMethodClobberize<JSC::DFG::PreciseLocalClobberizeAdaptor<(lambda at ./dfg/DFGPutStackSinkingPhase.cpp:488:42), (lambda at ./dfg/DFGPutStackSinkingPhase.cpp:520:41), (lambda at ./dfg/DFGPutStackSinkingPhase.cpp:534:25)>>, ClobberTopFunctor = (lambda at ./dfg/DFGClobberize.h:45:47)]"
+ "void JSC::FTL::(anonymous namespace)::LowerDFGToB3::compare(const IntFunctor &, const DoubleFunctor &, C_JITOperation_TT, C_JITOperation_B_GJssJss, S_JITOperation_GJJ) [IntFunctor = (lambda at /Library/Caches/com.apple.xbs/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:11527:13), DoubleFunctor = (lambda at /Library/Caches/com.apple.xbs/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:11530:13)]"
+ "void JSC::FTL::(anonymous namespace)::LowerDFGToB3::compare(const IntFunctor &, const DoubleFunctor &, C_JITOperation_TT, C_JITOperation_B_GJssJss, S_JITOperation_GJJ) [IntFunctor = (lambda at /Library/Caches/com.apple.xbs/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:11541:13), DoubleFunctor = (lambda at /Library/Caches/com.apple.xbs/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:11544:13)]"
+ "void JSC::FTL::(anonymous namespace)::LowerDFGToB3::compare(const IntFunctor &, const DoubleFunctor &, C_JITOperation_TT, C_JITOperation_B_GJssJss, S_JITOperation_GJJ) [IntFunctor = (lambda at /Library/Caches/com.apple.xbs/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:11555:13), DoubleFunctor = (lambda at /Library/Caches/com.apple.xbs/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:11558:13)]"
+ "void JSC::FTL::(anonymous namespace)::LowerDFGToB3::compare(const IntFunctor &, const DoubleFunctor &, C_JITOperation_TT, C_JITOperation_B_GJssJss, S_JITOperation_GJJ) [IntFunctor = (lambda at /Library/Caches/com.apple.xbs/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:11569:13), DoubleFunctor = (lambda at /Library/Caches/com.apple.xbs/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:11572:13)]"
- "./wasm/js/JSWebAssemblyException.cpp"
- "/AppleInternal/Library/BuildRoots/0263bece-26fb-11f0-a3b0-4ac8e0bcf05b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/wtf/Assertions.h"
- "/AppleInternal/Library/BuildRoots/0263bece-26fb-11f0-a3b0-4ac8e0bcf05b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/wtf/ConcurrentPtrHashSet.h"
- "/AppleInternal/Library/BuildRoots/0263bece-26fb-11f0-a3b0-4ac8e0bcf05b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/wtf/Deque.h"
- "/AppleInternal/Library/BuildRoots/0263bece-26fb-11f0-a3b0-4ac8e0bcf05b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/wtf/Dominators.h"
- "/AppleInternal/Library/BuildRoots/0263bece-26fb-11f0-a3b0-4ac8e0bcf05b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/wtf/FastBitVector.h"
- "/AppleInternal/Library/BuildRoots/0263bece-26fb-11f0-a3b0-4ac8e0bcf05b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/wtf/HashTable.h"
- "/AppleInternal/Library/BuildRoots/0263bece-26fb-11f0-a3b0-4ac8e0bcf05b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/wtf/IndexMap.h"
- "/AppleInternal/Library/BuildRoots/0263bece-26fb-11f0-a3b0-4ac8e0bcf05b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/wtf/JSONValues.h"
- "/AppleInternal/Library/BuildRoots/0263bece-26fb-11f0-a3b0-4ac8e0bcf05b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/wtf/LazyRef.h"
- "/AppleInternal/Library/BuildRoots/0263bece-26fb-11f0-a3b0-4ac8e0bcf05b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/wtf/LazyUniqueRef.h"
- "/AppleInternal/Library/BuildRoots/0263bece-26fb-11f0-a3b0-4ac8e0bcf05b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/wtf/Liveness.h"
- "/AppleInternal/Library/BuildRoots/0263bece-26fb-11f0-a3b0-4ac8e0bcf05b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/wtf/LockAlgorithmInlines.h"
- "/AppleInternal/Library/BuildRoots/0263bece-26fb-11f0-a3b0-4ac8e0bcf05b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/wtf/Markable.h"
- "/AppleInternal/Library/BuildRoots/0263bece-26fb-11f0-a3b0-4ac8e0bcf05b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/wtf/NaturalLoops.h"
- "/AppleInternal/Library/BuildRoots/0263bece-26fb-11f0-a3b0-4ac8e0bcf05b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/wtf/RedBlackTree.h"
- "/AppleInternal/Library/BuildRoots/0263bece-26fb-11f0-a3b0-4ac8e0bcf05b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/wtf/RefCounted.h"
- "/AppleInternal/Library/BuildRoots/0263bece-26fb-11f0-a3b0-4ac8e0bcf05b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/wtf/SinglyLinkedListWithTail.h"
- "/AppleInternal/Library/BuildRoots/0263bece-26fb-11f0-a3b0-4ac8e0bcf05b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/wtf/StdLibExtras.h"
- "/AppleInternal/Library/BuildRoots/0263bece-26fb-11f0-a3b0-4ac8e0bcf05b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/wtf/ThreadSafeWeakHashSet.h"
- "/AppleInternal/Library/BuildRoots/0263bece-26fb-11f0-a3b0-4ac8e0bcf05b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/wtf/ThreadSpecific.h"
- "/AppleInternal/Library/BuildRoots/0263bece-26fb-11f0-a3b0-4ac8e0bcf05b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/wtf/TrailingArray.h"
- "/AppleInternal/Library/BuildRoots/0263bece-26fb-11f0-a3b0-4ac8e0bcf05b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/wtf/WeakPtr.h"
- "/AppleInternal/Library/BuildRoots/0263bece-26fb-11f0-a3b0-4ac8e0bcf05b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/wtf/text/StringBuilder.h"
- "/AppleInternal/Library/BuildRoots/0263bece-26fb-11f0-a3b0-4ac8e0bcf05b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/wtf/text/StringConcatenate.h"
- "/AppleInternal/Library/BuildRoots/0263bece-26fb-11f0-a3b0-4ac8e0bcf05b/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/wtf/text/StringImpl.h"
- "JSValue JSC::JSWebAssemblyException::getArg(JSGlobalObject *, unsigned int) const"
- "LValue JSC::FTL::(anonymous namespace)::LowerDFGToB3::emitCodeBasedOnEndiannessBranch(LValue, const F1 &, const F2 &) [F1 = (lambda at /Library/Caches/com.apple.xbs/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:18421:45), F2 = (lambda at /Library/Caches/com.apple.xbs/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:18427:42)]"
- "LValue JSC::FTL::(anonymous namespace)::LowerDFGToB3::emitCodeBasedOnEndiannessBranch(LValue, const F1 &, const F2 &) [F1 = (lambda at /Library/Caches/com.apple.xbs/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:18458:49), F2 = (lambda at /Library/Caches/com.apple.xbs/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:18461:46)]"
- "LValue JSC::FTL::(anonymous namespace)::LowerDFGToB3::emitCodeBasedOnEndiannessBranch(LValue, const F1 &, const F2 &) [F1 = (lambda at /Library/Caches/com.apple.xbs/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:18481:45), F2 = (lambda at /Library/Caches/com.apple.xbs/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:18485:42)]"
- "LValue JSC::FTL::(anonymous namespace)::LowerDFGToB3::emitCodeBasedOnEndiannessBranch(LValue, const F1 &, const F2 &) [F1 = (lambda at /Library/Caches/com.apple.xbs/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:18510:45), F2 = (lambda at /Library/Caches/com.apple.xbs/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:18514:42)]"
- "LValue JSC::FTL::(anonymous namespace)::LowerDFGToB3::emitCodeBasedOnEndiannessBranch(LValue, const F1 &, const F2 &) [F1 = (lambda at /Library/Caches/com.apple.xbs/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:18539:45), F2 = (lambda at /Library/Caches/com.apple.xbs/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:18543:42)]"
- "auto JSC::FTL::(anonymous namespace)::LowerDFGToB3::compileCallOrConstructVarargsSpread()::(anonymous class)::operator()(auto, Node *) const [self:auto = std::reference_wrapper<const WTF::RecursableLambda<(lambda at /Library/Caches/com.apple.xbs/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:12127:70)>>]"
- "auto JSC::FTL::(anonymous namespace)::LowerDFGToB3::compileForwardVarargsWithSpread()::(anonymous class)::operator()(auto, Node *, LValue) const [self:auto = std::reference_wrapper<const WTF::RecursableLambda<(lambda at /Library/Caches/com.apple.xbs/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:13169:47)>>]"
- "bool JSC::DFG::OSRAvailabilityAnalysisPhase<(lambda at ./dfg/DFGOSRAvailabilityAnalysisPhase.cpp:201:31), (lambda at ./dfg/DFGOSRAvailabilityAnalysisPhase.cpp:202:31)>::run() [HeadFunctor = (lambda at ./dfg/DFGOSRAvailabilityAnalysisPhase.cpp:201:31), TailFunctor = (lambda at ./dfg/DFGOSRAvailabilityAnalysisPhase.cpp:202:31)]"
- "bool JSC::DFG::OSRAvailabilityAnalysisPhase<(lambda at ./dfg/DFGOSRAvailabilityAnalysisPhase.cpp:216:31), (lambda at ./dfg/DFGOSRAvailabilityAnalysisPhase.cpp:217:31)>::run() [HeadFunctor = (lambda at ./dfg/DFGOSRAvailabilityAnalysisPhase.cpp:216:31), TailFunctor = (lambda at ./dfg/DFGOSRAvailabilityAnalysisPhase.cpp:217:31)]"
- "void JSC::DFG::PreciseLocalClobberizeAdaptor<(lambda at ./dfg/DFGPutStackSinkingPhase.cpp:108:42), (lambda at ./dfg/DFGPutStackSinkingPhase.cpp:116:41), (lambda at ./dfg/DFGPutStackSinkingPhase.cpp:126:25)>::def(HeapLocation, LazyNode) [ReadFunctor = (lambda at ./dfg/DFGPutStackSinkingPhase.cpp:108:42), WriteFunctor = (lambda at ./dfg/DFGPutStackSinkingPhase.cpp:116:41), DefFunctor = (lambda at ./dfg/DFGPutStackSinkingPhase.cpp:126:25)]"
- "void JSC::DFG::PreciseLocalClobberizeAdaptor<(lambda at ./dfg/DFGPutStackSinkingPhase.cpp:108:42), (lambda at ./dfg/DFGPutStackSinkingPhase.cpp:116:41), (lambda at ./dfg/DFGPutStackSinkingPhase.cpp:126:25)>::write(AbstractHeap) [ReadFunctor = (lambda at ./dfg/DFGPutStackSinkingPhase.cpp:108:42), WriteFunctor = (lambda at ./dfg/DFGPutStackSinkingPhase.cpp:116:41), DefFunctor = (lambda at ./dfg/DFGPutStackSinkingPhase.cpp:126:25)]"
- "void JSC::DFG::PreciseLocalClobberizeAdaptor<(lambda at ./dfg/DFGPutStackSinkingPhase.cpp:284:42), (lambda at ./dfg/DFGPutStackSinkingPhase.cpp:293:41), (lambda at ./dfg/DFGPutStackSinkingPhase.cpp:304:25)>::def(HeapLocation, LazyNode) [ReadFunctor = (lambda at ./dfg/DFGPutStackSinkingPhase.cpp:284:42), WriteFunctor = (lambda at ./dfg/DFGPutStackSinkingPhase.cpp:293:41), DefFunctor = (lambda at ./dfg/DFGPutStackSinkingPhase.cpp:304:25)]"
- "void JSC::DFG::PreciseLocalClobberizeAdaptor<(lambda at ./dfg/DFGPutStackSinkingPhase.cpp:284:42), (lambda at ./dfg/DFGPutStackSinkingPhase.cpp:293:41), (lambda at ./dfg/DFGPutStackSinkingPhase.cpp:304:25)>::write(AbstractHeap) [ReadFunctor = (lambda at ./dfg/DFGPutStackSinkingPhase.cpp:284:42), WriteFunctor = (lambda at ./dfg/DFGPutStackSinkingPhase.cpp:293:41), DefFunctor = (lambda at ./dfg/DFGPutStackSinkingPhase.cpp:304:25)]"
- "void JSC::DFG::PreciseLocalClobberizeAdaptor<(lambda at ./dfg/DFGPutStackSinkingPhase.cpp:486:42), (lambda at ./dfg/DFGPutStackSinkingPhase.cpp:518:41), (lambda at ./dfg/DFGPutStackSinkingPhase.cpp:532:25)>::def(HeapLocation, LazyNode) [ReadFunctor = (lambda at ./dfg/DFGPutStackSinkingPhase.cpp:486:42), WriteFunctor = (lambda at ./dfg/DFGPutStackSinkingPhase.cpp:518:41), DefFunctor = (lambda at ./dfg/DFGPutStackSinkingPhase.cpp:532:25)]"
- "void JSC::DFG::PreciseLocalClobberizeAdaptor<(lambda at ./dfg/DFGPutStackSinkingPhase.cpp:486:42), (lambda at ./dfg/DFGPutStackSinkingPhase.cpp:518:41), (lambda at ./dfg/DFGPutStackSinkingPhase.cpp:532:25)>::write(AbstractHeap) [ReadFunctor = (lambda at ./dfg/DFGPutStackSinkingPhase.cpp:486:42), WriteFunctor = (lambda at ./dfg/DFGPutStackSinkingPhase.cpp:518:41), DefFunctor = (lambda at ./dfg/DFGPutStackSinkingPhase.cpp:532:25)]"
- "void JSC::DFG::SSACalculator::computePhis(const Invocable<Node *(Variable *, BasicBlock *)> auto &) [functor:auto = (lambda at ./dfg/DFGPutStackSinkingPhase.cpp:387:13)]"
- "void JSC::DFG::clobberize(Graph &, Node *, const ReadFunctor &, const WriteFunctor &, const DefFunctor &, const ClobberTopFunctor &) [ReadFunctor = (lambda at /Library/Caches/com.apple.xbs/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:1904:41), WriteFunctor = (lambda at /Library/Caches/com.apple.xbs/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:1904:59), DefFunctor = (lambda at /Library/Caches/com.apple.xbs/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:1904:77), ClobberTopFunctor = (lambda at /Library/Caches/com.apple.xbs/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:1900:39)]"
- "void JSC::DFG::clobberize(Graph &, Node *, const ReadFunctor &, const WriteFunctor &, const DefFunctor &, const ClobberTopFunctor &) [ReadFunctor = JSC::DFG::ReadMethodClobberize<JSC::DFG::PreciseLocalClobberizeAdaptor<(lambda at ./dfg/DFGPutStackSinkingPhase.cpp:108:42), (lambda at ./dfg/DFGPutStackSinkingPhase.cpp:116:41), (lambda at ./dfg/DFGPutStackSinkingPhase.cpp:126:25)>>, WriteFunctor = JSC::DFG::WriteMethodClobberize<JSC::DFG::PreciseLocalClobberizeAdaptor<(lambda at ./dfg/DFGPutStackSinkingPhase.cpp:108:42), (lambda at ./dfg/DFGPutStackSinkingPhase.cpp:116:41), (lambda at ./dfg/DFGPutStackSinkingPhase.cpp:126:25)>>, DefFunctor = JSC::DFG::DefMethodClobberize<JSC::DFG::PreciseLocalClobberizeAdaptor<(lambda at ./dfg/DFGPutStackSinkingPhase.cpp:108:42), (lambda at ./dfg/DFGPutStackSinkingPhase.cpp:116:41), (lambda at ./dfg/DFGPutStackSinkingPhase.cpp:126:25)>>, ClobberTopFunctor = (lambda at ./dfg/DFGClobberize.h:45:47)]"
- "void JSC::DFG::clobberize(Graph &, Node *, const ReadFunctor &, const WriteFunctor &, const DefFunctor &, const ClobberTopFunctor &) [ReadFunctor = JSC::DFG::ReadMethodClobberize<JSC::DFG::PreciseLocalClobberizeAdaptor<(lambda at ./dfg/DFGPutStackSinkingPhase.cpp:284:42), (lambda at ./dfg/DFGPutStackSinkingPhase.cpp:293:41), (lambda at ./dfg/DFGPutStackSinkingPhase.cpp:304:25)>>, WriteFunctor = JSC::DFG::WriteMethodClobberize<JSC::DFG::PreciseLocalClobberizeAdaptor<(lambda at ./dfg/DFGPutStackSinkingPhase.cpp:284:42), (lambda at ./dfg/DFGPutStackSinkingPhase.cpp:293:41), (lambda at ./dfg/DFGPutStackSinkingPhase.cpp:304:25)>>, DefFunctor = JSC::DFG::DefMethodClobberize<JSC::DFG::PreciseLocalClobberizeAdaptor<(lambda at ./dfg/DFGPutStackSinkingPhase.cpp:284:42), (lambda at ./dfg/DFGPutStackSinkingPhase.cpp:293:41), (lambda at ./dfg/DFGPutStackSinkingPhase.cpp:304:25)>>, ClobberTopFunctor = (lambda at ./dfg/DFGClobberize.h:45:47)]"
- "void JSC::DFG::clobberize(Graph &, Node *, const ReadFunctor &, const WriteFunctor &, const DefFunctor &, const ClobberTopFunctor &) [ReadFunctor = JSC::DFG::ReadMethodClobberize<JSC::DFG::PreciseLocalClobberizeAdaptor<(lambda at ./dfg/DFGPutStackSinkingPhase.cpp:486:42), (lambda at ./dfg/DFGPutStackSinkingPhase.cpp:518:41), (lambda at ./dfg/DFGPutStackSinkingPhase.cpp:532:25)>>, WriteFunctor = JSC::DFG::WriteMethodClobberize<JSC::DFG::PreciseLocalClobberizeAdaptor<(lambda at ./dfg/DFGPutStackSinkingPhase.cpp:486:42), (lambda at ./dfg/DFGPutStackSinkingPhase.cpp:518:41), (lambda at ./dfg/DFGPutStackSinkingPhase.cpp:532:25)>>, DefFunctor = JSC::DFG::DefMethodClobberize<JSC::DFG::PreciseLocalClobberizeAdaptor<(lambda at ./dfg/DFGPutStackSinkingPhase.cpp:486:42), (lambda at ./dfg/DFGPutStackSinkingPhase.cpp:518:41), (lambda at ./dfg/DFGPutStackSinkingPhase.cpp:532:25)>>, ClobberTopFunctor = (lambda at ./dfg/DFGClobberize.h:45:47)]"
- "void JSC::FTL::(anonymous namespace)::LowerDFGToB3::compare(const IntFunctor &, const DoubleFunctor &, C_JITOperation_TT, C_JITOperation_B_GJssJss, S_JITOperation_GJJ) [IntFunctor = (lambda at /Library/Caches/com.apple.xbs/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:11526:13), DoubleFunctor = (lambda at /Library/Caches/com.apple.xbs/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:11529:13)]"
- "void JSC::FTL::(anonymous namespace)::LowerDFGToB3::compare(const IntFunctor &, const DoubleFunctor &, C_JITOperation_TT, C_JITOperation_B_GJssJss, S_JITOperation_GJJ) [IntFunctor = (lambda at /Library/Caches/com.apple.xbs/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:11540:13), DoubleFunctor = (lambda at /Library/Caches/com.apple.xbs/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:11543:13)]"
- "void JSC::FTL::(anonymous namespace)::LowerDFGToB3::compare(const IntFunctor &, const DoubleFunctor &, C_JITOperation_TT, C_JITOperation_B_GJssJss, S_JITOperation_GJJ) [IntFunctor = (lambda at /Library/Caches/com.apple.xbs/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:11554:13), DoubleFunctor = (lambda at /Library/Caches/com.apple.xbs/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:11557:13)]"
- "void JSC::FTL::(anonymous namespace)::LowerDFGToB3::compare(const IntFunctor &, const DoubleFunctor &, C_JITOperation_TT, C_JITOperation_B_GJssJss, S_JITOperation_GJJ) [IntFunctor = (lambda at /Library/Caches/com.apple.xbs/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:11568:13), DoubleFunctor = (lambda at /Library/Caches/com.apple.xbs/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:11571:13)]"

```
