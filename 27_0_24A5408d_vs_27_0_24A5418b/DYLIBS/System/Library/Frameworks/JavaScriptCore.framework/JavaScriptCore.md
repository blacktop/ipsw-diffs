## JavaScriptCore

> `/System/Library/Frameworks/JavaScriptCore.framework/JavaScriptCore`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`

```diff

-625.1.29.10.3
-  __TEXT.__text: 0x23cda3c
+625.1.29.10.25
+  __TEXT.__text: 0x23cab0c
   __TEXT.__jsc_int: 0x691b8
   __TEXT.__objc_methlist: 0xb9c
   __TEXT.__const: 0xa2664

   __TEXT.__oslogstring: 0xa0f
   __TEXT.__gcc_except_tab: 0x2964
   __TEXT.__ustring: 0x10
-  __TEXT.__unwind_info: 0x1fd98
+  __TEXT.__unwind_info: 0x1fd80
   __TEXT.__eh_frame: 0x50
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 39720
-  Symbols:   48009
+  Functions: 39714
+  Symbols:   48008
   CStrings:  25802
 
Symbols:
+ __ZN3JSC3DFG5Graph33canDoFastSpreadWithStructureCheckEPNS0_4NodeE
+ __ZN3WTF22setSDKAlignedBehaviorsENS_6BitSetILm109EjEE
+ __ZZN3JSC3DFG19AbstractInterpreterINS0_20InPlaceAbstractStateEE12executeEdgesEPNS0_4NodeEENKUlRNS0_4EdgeEE_clES7_
- __ZN3JSC3DFG12_GLOBAL__N_126StoreBarrierInsertionPhaseILNS1_9PhaseModeE0EE15considerBarrierENS0_4EdgeES5_
- __ZN3WTF22setSDKAlignedBehaviorsENS_6BitSetILm108EjEE
- __ZN3WTFL24sdkAlignedBehaviorsValueEv
- __ZNK3WTF9HashTableIPN3JSC3DFG4NodeES4_NS_17IdentityExtractorENS_11DefaultHashIS4_EENS_10HashTraitsIS4_EES9_NS_10FastMallocEE8containsINS_22IdentityHashTranslatorIS9_S7_EELNS_17ShouldValidateKeyE0ES4_EEbRKT1_
CStrings:
+ "LValue JSC::FTL::(anonymous namespace)::LowerDFGToB3::emitCodeBasedOnEndiannessBranch(LValue, const F1 &, const F2 &) [F1 = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:21457:45), F2 = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:21463:42)]"
+ "LValue JSC::FTL::(anonymous namespace)::LowerDFGToB3::emitCodeBasedOnEndiannessBranch(LValue, const F1 &, const F2 &) [F1 = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:21494:49), F2 = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:21497:46)]"
+ "LValue JSC::FTL::(anonymous namespace)::LowerDFGToB3::emitCodeBasedOnEndiannessBranch(LValue, const F1 &, const F2 &) [F1 = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:21517:45), F2 = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:21521:42)]"
+ "LValue JSC::FTL::(anonymous namespace)::LowerDFGToB3::emitCodeBasedOnEndiannessBranch(LValue, const F1 &, const F2 &) [F1 = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:21546:45), F2 = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:21550:42)]"
+ "LValue JSC::FTL::(anonymous namespace)::LowerDFGToB3::emitCodeBasedOnEndiannessBranch(LValue, const F1 &, const F2 &) [F1 = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:21575:45), F2 = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:21579:42)]"
+ "auto JSC::FTL::(anonymous namespace)::LowerDFGToB3::compileCallOrConstructVarargsSpread()::(anonymous class)::operator()(auto, Node *) const [self:auto = std::reference_wrapper<const WTF::RecursableLambda<(lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:14330:70)>>]"
+ "auto JSC::FTL::(anonymous namespace)::LowerDFGToB3::compileForwardVarargsWithSpread()::(anonymous class)::operator()(auto, Node *, LValue) const [self:auto = std::reference_wrapper<const WTF::RecursableLambda<(lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:15372:47)>>]"
+ "void JSC::DFG::clobberize(Graph &, Node *, const ReadFunctor &, const WriteFunctor &, const DefFunctor &, const ClobberTopFunctor &) [ReadFunctor = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/dfg/DFGStoreBarrierInsertionPhase.cpp:514:33), WriteFunctor = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/dfg/DFGStoreBarrierInsertionPhase.cpp:529:34), DefFunctor = JSC::DFG::NoOpClobberize, ClobberTopFunctor = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/dfg/DFGClobberize.h:45:47)]"
+ "void JSC::FTL::(anonymous namespace)::LowerDFGToB3::compare(const IntFunctor &, const DoubleFunctor &, C_JITOperation_TT, C_JITOperation_B_GJssJss, S_JITOperation_GJJ) [IntFunctor = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:13729:13), DoubleFunctor = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:13732:13)]"
+ "void JSC::FTL::(anonymous namespace)::LowerDFGToB3::compare(const IntFunctor &, const DoubleFunctor &, C_JITOperation_TT, C_JITOperation_B_GJssJss, S_JITOperation_GJJ) [IntFunctor = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:13743:13), DoubleFunctor = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:13746:13)]"
+ "void JSC::FTL::(anonymous namespace)::LowerDFGToB3::compare(const IntFunctor &, const DoubleFunctor &, C_JITOperation_TT, C_JITOperation_B_GJssJss, S_JITOperation_GJJ) [IntFunctor = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:13757:13), DoubleFunctor = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:13760:13)]"
+ "void JSC::FTL::(anonymous namespace)::LowerDFGToB3::compare(const IntFunctor &, const DoubleFunctor &, C_JITOperation_TT, C_JITOperation_B_GJssJss, S_JITOperation_GJJ) [IntFunctor = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:13771:13), DoubleFunctor = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:13774:13)]"
- "LValue JSC::FTL::(anonymous namespace)::LowerDFGToB3::emitCodeBasedOnEndiannessBranch(LValue, const F1 &, const F2 &) [F1 = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:21454:45), F2 = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:21460:42)]"
- "LValue JSC::FTL::(anonymous namespace)::LowerDFGToB3::emitCodeBasedOnEndiannessBranch(LValue, const F1 &, const F2 &) [F1 = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:21491:49), F2 = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:21494:46)]"
- "LValue JSC::FTL::(anonymous namespace)::LowerDFGToB3::emitCodeBasedOnEndiannessBranch(LValue, const F1 &, const F2 &) [F1 = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:21514:45), F2 = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:21518:42)]"
- "LValue JSC::FTL::(anonymous namespace)::LowerDFGToB3::emitCodeBasedOnEndiannessBranch(LValue, const F1 &, const F2 &) [F1 = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:21543:45), F2 = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:21547:42)]"
- "LValue JSC::FTL::(anonymous namespace)::LowerDFGToB3::emitCodeBasedOnEndiannessBranch(LValue, const F1 &, const F2 &) [F1 = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:21572:45), F2 = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:21576:42)]"
- "auto JSC::FTL::(anonymous namespace)::LowerDFGToB3::compileCallOrConstructVarargsSpread()::(anonymous class)::operator()(auto, Node *) const [self:auto = std::reference_wrapper<const WTF::RecursableLambda<(lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:14327:70)>>]"
- "auto JSC::FTL::(anonymous namespace)::LowerDFGToB3::compileForwardVarargsWithSpread()::(anonymous class)::operator()(auto, Node *, LValue) const [self:auto = std::reference_wrapper<const WTF::RecursableLambda<(lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:15369:47)>>]"
- "void JSC::DFG::clobberize(Graph &, Node *, const ReadFunctor &, const WriteFunctor &, const DefFunctor &, const ClobberTopFunctor &) [ReadFunctor = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/dfg/DFGStoreBarrierInsertionPhase.cpp:502:33), WriteFunctor = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/dfg/DFGStoreBarrierInsertionPhase.cpp:517:34), DefFunctor = JSC::DFG::NoOpClobberize, ClobberTopFunctor = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/dfg/DFGClobberize.h:45:47)]"
- "void JSC::FTL::(anonymous namespace)::LowerDFGToB3::compare(const IntFunctor &, const DoubleFunctor &, C_JITOperation_TT, C_JITOperation_B_GJssJss, S_JITOperation_GJJ) [IntFunctor = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:13726:13), DoubleFunctor = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:13729:13)]"
- "void JSC::FTL::(anonymous namespace)::LowerDFGToB3::compare(const IntFunctor &, const DoubleFunctor &, C_JITOperation_TT, C_JITOperation_B_GJssJss, S_JITOperation_GJJ) [IntFunctor = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:13740:13), DoubleFunctor = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:13743:13)]"
- "void JSC::FTL::(anonymous namespace)::LowerDFGToB3::compare(const IntFunctor &, const DoubleFunctor &, C_JITOperation_TT, C_JITOperation_B_GJssJss, S_JITOperation_GJJ) [IntFunctor = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:13754:13), DoubleFunctor = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:13757:13)]"
- "void JSC::FTL::(anonymous namespace)::LowerDFGToB3::compare(const IntFunctor &, const DoubleFunctor &, C_JITOperation_TT, C_JITOperation_B_GJssJss, S_JITOperation_GJJ) [IntFunctor = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:13768:13), DoubleFunctor = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:13771:13)]"
```
