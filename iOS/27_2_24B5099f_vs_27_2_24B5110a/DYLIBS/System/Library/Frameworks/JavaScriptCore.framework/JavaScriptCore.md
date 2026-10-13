## JavaScriptCore

> `/System/Library/Frameworks/JavaScriptCore.framework/JavaScriptCore`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`

```diff

-625.2.7.1.0
-  __TEXT.__text: 0x22e0700
+625.2.8.10.4
+  __TEXT.__text: 0x22e0e10
   __TEXT.__jsc_int: 0x6bfb8
   __TEXT.__objc_methlist: 0xb9c
   __TEXT.__const: 0xa1034

   __TEXT.__oslogstring: 0xa0f
   __TEXT.__gcc_except_tab: 0x2930
   __TEXT.__ustring: 0x10
-  __TEXT.__unwind_info: 0x20878
+  __TEXT.__unwind_info: 0x20898
   __TEXT.__eh_frame: 0x50
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_superrefs: 0x40
   __DATA_CONST.__jsc_ops: 0x3970
   __DATA_CONST.__got: 0x288
-  __AUTH_CONST.__const: 0x3db70
+  __AUTH_CONST.__const: 0x3dbb8
   __AUTH_CONST.__cfstring: 0x10a0
   __AUTH_CONST.__objc_const: 0xdf8
   __AUTH_CONST.__weak_auth_got: 0x18

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 40099
-  Symbols:   48155
+  Functions: 40107
+  Symbols:   48163
   CStrings:  25837
 
Symbols:
+ __ZN3WTF20MainThreadDispatcher13dispatchAfterENS_7SecondsEONS_8FunctionIFvvEEE
+ __ZN3WTF6Detail15CallableWrapperIZNS_20MainThreadDispatcher13dispatchAfterENS_7SecondsEONS_8FunctionIFvvEEEE3$_0vJEE4callEv
+ __ZN3WTF6Detail15CallableWrapperIZNS_20MainThreadDispatcher13dispatchAfterENS_7SecondsEONS_8FunctionIFvvEEEE3$_0vJEED0Ev
+ __ZN3WTF6Detail15CallableWrapperIZNS_20MainThreadDispatcher13dispatchAfterENS_7SecondsEONS_8FunctionIFvvEEEE3$_0vJEED1Ev
+ __ZN3WTF6Detail15CallableWrapperIZNS_7RunLoop13scheduleTimerENS_7SecondsEONS_8FunctionIFvvEEEE3$_0vJEE4callEv
+ __ZN3WTF6Detail15CallableWrapperIZNS_7RunLoop13scheduleTimerENS_7SecondsEONS_8FunctionIFvvEEEE3$_0vJEED0Ev
+ __ZN3WTF6Detail15CallableWrapperIZNS_7RunLoop13scheduleTimerENS_7SecondsEONS_8FunctionIFvvEEEE3$_0vJEED1Ev
+ __ZN3WTF7RunLoop13scheduleTimerENS_7SecondsEONS_8FunctionIFvvEEE
+ __ZN3WTF9WorkQueue13dispatchAfterENS_7SecondsEONS_8FunctionIFvvEEE
+ __ZTVN3WTF6Detail15CallableWrapperIZNS_20MainThreadDispatcher13dispatchAfterENS_7SecondsEONS_8FunctionIFvvEEEE3$_0vJEEE
+ __ZTVN3WTF6Detail15CallableWrapperIZNS_7RunLoop13scheduleTimerENS_7SecondsEONS_8FunctionIFvvEEEE3$_0vJEEE
+ __ZThn24_N3WTF20SuspendableWorkQueue13dispatchAfterENS_7SecondsEONS_8FunctionIFvvEEE
+ __ZThn24_N3WTF9WorkQueue13dispatchAfterENS_7SecondsEONS_8FunctionIFvvEEE
- __ZN3WTF6Detail15CallableWrapperIZNS_7RunLoop13dispatchAfterENS_7SecondsEONS_8FunctionIFvvEEEE3$_0vJEE4callEv
- __ZN3WTF6Detail15CallableWrapperIZNS_7RunLoop13dispatchAfterENS_7SecondsEONS_8FunctionIFvvEEEE3$_0vJEED0Ev
- __ZN3WTF6Detail15CallableWrapperIZNS_7RunLoop13dispatchAfterENS_7SecondsEONS_8FunctionIFvvEEEE3$_0vJEED1Ev
- __ZTVN3WTF6Detail15CallableWrapperIZNS_7RunLoop13dispatchAfterENS_7SecondsEONS_8FunctionIFvvEEEE3$_0vJEEE
- ___PRETTY_FUNCTION__._ZN3WTF7RunLoop13dispatchAfterENS_7SecondsEONS_8FunctionIFvvEEE
CStrings:
+ "LValue JSC::FTL::(anonymous namespace)::LowerDFGToB3::emitCodeBasedOnEndiannessBranch(LValue, const F1 &, const F2 &) [F1 = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:21722:45), F2 = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:21728:42)]"
+ "LValue JSC::FTL::(anonymous namespace)::LowerDFGToB3::emitCodeBasedOnEndiannessBranch(LValue, const F1 &, const F2 &) [F1 = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:21759:49), F2 = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:21762:46)]"
+ "LValue JSC::FTL::(anonymous namespace)::LowerDFGToB3::emitCodeBasedOnEndiannessBranch(LValue, const F1 &, const F2 &) [F1 = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:21782:45), F2 = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:21786:42)]"
+ "LValue JSC::FTL::(anonymous namespace)::LowerDFGToB3::emitCodeBasedOnEndiannessBranch(LValue, const F1 &, const F2 &) [F1 = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:21811:45), F2 = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:21815:42)]"
+ "LValue JSC::FTL::(anonymous namespace)::LowerDFGToB3::emitCodeBasedOnEndiannessBranch(LValue, const F1 &, const F2 &) [F1 = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:21840:45), F2 = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:21844:42)]"
+ "Ref<RunLoop::DispatchTimer> WTF::RunLoop::scheduleTimer(Seconds, Function<void ()> &&)"
+ "auto JSC::FTL::(anonymous namespace)::LowerDFGToB3::compileCallOrConstructVarargsSpread()::(anonymous class)::operator()(auto, Node *) const [self:auto = std::reference_wrapper<const WTF::RecursableLambda<(lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:14392:70)>>]"
+ "auto JSC::FTL::(anonymous namespace)::LowerDFGToB3::compileForwardVarargsWithSpread()::(anonymous class)::operator()(auto, Node *, LValue) const [self:auto = std::reference_wrapper<const WTF::RecursableLambda<(lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:15434:47)>>]"
+ "decltype(auto) JSC::Wasm::BBQJITImpl::BBQJIT::emitCheckAndPrepareAndMaterializePointerApply(Value, uint64_t, uint32_t, uint8_t, Functor &&) [Functor = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/wasm/WasmBBQJIT64.cpp:3592:123)]"
+ "decltype(auto) JSC::Wasm::BBQJITImpl::BBQJIT::emitCheckAndPrepareAndMaterializePointerApply(Value, uint64_t, uint32_t, uint8_t, Functor &&) [Functor = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/wasm/WasmBBQJIT64.cpp:3605:114)]"
+ "decltype(auto) JSC::Wasm::BBQJITImpl::BBQJIT::emitCheckAndPrepareAndMaterializePointerApply(Value, uint64_t, uint32_t, uint8_t, Functor &&) [Functor = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/wasm/WasmBBQJIT64.cpp:4048:107)]"
+ "decltype(auto) JSC::Wasm::BBQJITImpl::BBQJIT::emitCheckAndPrepareAndMaterializePointerApply(Value, uint64_t, uint32_t, uint8_t, Functor &&) [Functor = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/wasm/WasmBBQJIT64.cpp:4065:160)]"
+ "void JSC::DFG::clobberize(Graph &, Node *, const ReadFunctor &, const WriteFunctor &, const DefFunctor &, const ClobberTopFunctor &) [ReadFunctor = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/dfg/DFGSpeculativeJIT.cpp:2351:43), WriteFunctor = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/dfg/DFGSpeculativeJIT.cpp:2351:61), DefFunctor = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/dfg/DFGSpeculativeJIT.cpp:2351:79), ClobberTopFunctor = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/dfg/DFGSpeculativeJIT.cpp:2342:35)]"
+ "void JSC::DFG::clobberize(Graph &, Node *, const ReadFunctor &, const WriteFunctor &, const DefFunctor &, const ClobberTopFunctor &) [ReadFunctor = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/dfg/DFGSpeculativeJIT.cpp:2393:66), WriteFunctor = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/dfg/DFGSpeculativeJIT.cpp:2393:84), DefFunctor = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/dfg/DFGSpeculativeJIT.cpp:2393:102), ClobberTopFunctor = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/dfg/DFGSpeculativeJIT.cpp:2389:39)]"
+ "void JSC::DFG::clobberize(Graph &, Node *, const ReadFunctor &, const WriteFunctor &, const DefFunctor &, const ClobberTopFunctor &) [ReadFunctor = JSC::DFG::NoOpClobberize, WriteFunctor = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/dfg/DFGArgumentsEliminationPhase.cpp:556:21), DefFunctor = JSC::DFG::NoOpClobberize, ClobberTopFunctor = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/dfg/DFGClobberize.h:45:47)]"
+ "void JSC::DFG::clobberize(Graph &, Node *, const ReadFunctor &, const WriteFunctor &, const DefFunctor &, const ClobberTopFunctor &) [ReadFunctor = JSC::DFG::NoOpClobberize, WriteFunctor = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/dfg/DFGArgumentsEliminationPhase.cpp:723:25), DefFunctor = JSC::DFG::NoOpClobberize, ClobberTopFunctor = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/dfg/DFGClobberize.h:45:47)]"
+ "void JSC::FTL::(anonymous namespace)::LowerDFGToB3::compare(const IntFunctor &, const DoubleFunctor &, C_JITOperation_TT, C_JITOperation_B_GJssJss, S_JITOperation_GJJ) [IntFunctor = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:13810:13), DoubleFunctor = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:13813:13)]"
+ "void JSC::FTL::(anonymous namespace)::LowerDFGToB3::compare(const IntFunctor &, const DoubleFunctor &, C_JITOperation_TT, C_JITOperation_B_GJssJss, S_JITOperation_GJJ) [IntFunctor = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:13824:13), DoubleFunctor = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:13827:13)]"
+ "void JSC::FTL::(anonymous namespace)::LowerDFGToB3::compare(const IntFunctor &, const DoubleFunctor &, C_JITOperation_TT, C_JITOperation_B_GJssJss, S_JITOperation_GJJ) [IntFunctor = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:13838:13), DoubleFunctor = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:13841:13)]"
+ "void JSC::FTL::(anonymous namespace)::LowerDFGToB3::compare(const IntFunctor &, const DoubleFunctor &, C_JITOperation_TT, C_JITOperation_B_GJssJss, S_JITOperation_GJJ) [IntFunctor = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:13852:13), DoubleFunctor = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:13855:13)]"
- "LValue JSC::FTL::(anonymous namespace)::LowerDFGToB3::emitCodeBasedOnEndiannessBranch(LValue, const F1 &, const F2 &) [F1 = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:21668:45), F2 = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:21674:42)]"
- "LValue JSC::FTL::(anonymous namespace)::LowerDFGToB3::emitCodeBasedOnEndiannessBranch(LValue, const F1 &, const F2 &) [F1 = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:21705:49), F2 = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:21708:46)]"
- "LValue JSC::FTL::(anonymous namespace)::LowerDFGToB3::emitCodeBasedOnEndiannessBranch(LValue, const F1 &, const F2 &) [F1 = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:21728:45), F2 = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:21732:42)]"
- "LValue JSC::FTL::(anonymous namespace)::LowerDFGToB3::emitCodeBasedOnEndiannessBranch(LValue, const F1 &, const F2 &) [F1 = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:21757:45), F2 = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:21761:42)]"
- "LValue JSC::FTL::(anonymous namespace)::LowerDFGToB3::emitCodeBasedOnEndiannessBranch(LValue, const F1 &, const F2 &) [F1 = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:21786:45), F2 = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:21790:42)]"
- "Ref<RunLoop::DispatchTimer> WTF::RunLoop::dispatchAfter(Seconds, Function<void ()> &&)"
- "auto JSC::FTL::(anonymous namespace)::LowerDFGToB3::compileCallOrConstructVarargsSpread()::(anonymous class)::operator()(auto, Node *) const [self:auto = std::reference_wrapper<const WTF::RecursableLambda<(lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:14338:70)>>]"
- "auto JSC::FTL::(anonymous namespace)::LowerDFGToB3::compileForwardVarargsWithSpread()::(anonymous class)::operator()(auto, Node *, LValue) const [self:auto = std::reference_wrapper<const WTF::RecursableLambda<(lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:15380:47)>>]"
- "decltype(auto) JSC::Wasm::BBQJITImpl::BBQJIT::emitCheckAndPrepareAndMaterializePointerApply(Value, uint64_t, uint32_t, uint8_t, Functor &&) [Functor = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/wasm/WasmBBQJIT64.cpp:3548:123)]"
- "decltype(auto) JSC::Wasm::BBQJITImpl::BBQJIT::emitCheckAndPrepareAndMaterializePointerApply(Value, uint64_t, uint32_t, uint8_t, Functor &&) [Functor = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/wasm/WasmBBQJIT64.cpp:3561:114)]"
- "decltype(auto) JSC::Wasm::BBQJITImpl::BBQJIT::emitCheckAndPrepareAndMaterializePointerApply(Value, uint64_t, uint32_t, uint8_t, Functor &&) [Functor = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/wasm/WasmBBQJIT64.cpp:4004:107)]"
- "decltype(auto) JSC::Wasm::BBQJITImpl::BBQJIT::emitCheckAndPrepareAndMaterializePointerApply(Value, uint64_t, uint32_t, uint8_t, Functor &&) [Functor = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/wasm/WasmBBQJIT64.cpp:4021:160)]"
- "void JSC::DFG::clobberize(Graph &, Node *, const ReadFunctor &, const WriteFunctor &, const DefFunctor &, const ClobberTopFunctor &) [ReadFunctor = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/dfg/DFGSpeculativeJIT.cpp:2345:43), WriteFunctor = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/dfg/DFGSpeculativeJIT.cpp:2345:61), DefFunctor = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/dfg/DFGSpeculativeJIT.cpp:2345:79), ClobberTopFunctor = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/dfg/DFGSpeculativeJIT.cpp:2336:35)]"
- "void JSC::DFG::clobberize(Graph &, Node *, const ReadFunctor &, const WriteFunctor &, const DefFunctor &, const ClobberTopFunctor &) [ReadFunctor = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/dfg/DFGSpeculativeJIT.cpp:2387:66), WriteFunctor = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/dfg/DFGSpeculativeJIT.cpp:2387:84), DefFunctor = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/dfg/DFGSpeculativeJIT.cpp:2387:102), ClobberTopFunctor = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/dfg/DFGSpeculativeJIT.cpp:2383:39)]"
- "void JSC::DFG::clobberize(Graph &, Node *, const ReadFunctor &, const WriteFunctor &, const DefFunctor &, const ClobberTopFunctor &) [ReadFunctor = JSC::DFG::NoOpClobberize, WriteFunctor = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/dfg/DFGArgumentsEliminationPhase.cpp:514:21), DefFunctor = JSC::DFG::NoOpClobberize, ClobberTopFunctor = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/dfg/DFGClobberize.h:45:47)]"
- "void JSC::DFG::clobberize(Graph &, Node *, const ReadFunctor &, const WriteFunctor &, const DefFunctor &, const ClobberTopFunctor &) [ReadFunctor = JSC::DFG::NoOpClobberize, WriteFunctor = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/dfg/DFGArgumentsEliminationPhase.cpp:681:25), DefFunctor = JSC::DFG::NoOpClobberize, ClobberTopFunctor = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/dfg/DFGClobberize.h:45:47)]"
- "void JSC::FTL::(anonymous namespace)::LowerDFGToB3::compare(const IntFunctor &, const DoubleFunctor &, C_JITOperation_TT, C_JITOperation_B_GJssJss, S_JITOperation_GJJ) [IntFunctor = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:13756:13), DoubleFunctor = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:13759:13)]"
- "void JSC::FTL::(anonymous namespace)::LowerDFGToB3::compare(const IntFunctor &, const DoubleFunctor &, C_JITOperation_TT, C_JITOperation_B_GJssJss, S_JITOperation_GJJ) [IntFunctor = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:13770:13), DoubleFunctor = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:13773:13)]"
- "void JSC::FTL::(anonymous namespace)::LowerDFGToB3::compare(const IntFunctor &, const DoubleFunctor &, C_JITOperation_TT, C_JITOperation_B_GJssJss, S_JITOperation_GJJ) [IntFunctor = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:13784:13), DoubleFunctor = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:13787:13)]"
- "void JSC::FTL::(anonymous namespace)::LowerDFGToB3::compare(const IntFunctor &, const DoubleFunctor &, C_JITOperation_TT, C_JITOperation_B_GJssJss, S_JITOperation_GJJ) [IntFunctor = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:13798:13), DoubleFunctor = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:13801:13)]"
```
