## JavaScriptCore

> `/System/Library/Frameworks/JavaScriptCore.framework/JavaScriptCore`

```diff

-616.1.27.10.16
-  __TEXT.__text: 0x15c12f8
-  __TEXT.__auth_stubs: 0x2bd0
+616.2.9.10.10
+  __TEXT.__text: 0x15bf060
+  __TEXT.__auth_stubs: 0x2bb0
   __TEXT.__objc_methlist: 0x950
-  __TEXT.__const: 0x7d128
-  __TEXT.__cstring: 0xb6617
+  __TEXT.__const: 0x7d138
+  __TEXT.__cstring: 0xb6731
   __TEXT.__gcc_except_tab: 0x1d14
   __TEXT.__oslogstring: 0x41e
   __TEXT.__unwind_info: 0x1e64

   __DATA_CONST.__objc_const: 0xd28
   __DATA_CONST.__objc_selrefs: 0x860
   __DATA_CONST.__jsc_ops: 0x2d90
-  __AUTH_CONST.__const: 0x36d60
+  __AUTH_CONST.__const: 0x36d30
   __AUTH_CONST.__cfstring: 0xfa0
   __AUTH_CONST.__objc_const: 0x438
-  __AUTH_CONST.__auth_got: 0x15f8
+  __AUTH_CONST.__auth_got: 0x15e8
   __AUTH.__objc_data: 0xa0
   __AUTH.__data: 0xa0
   __DATA.__objc_protorefs: 0x8

   __DATA_DIRTY.__const: 0x40
   __DATA_DIRTY.__objc_ivar: 0x8
   __DATA_DIRTY.__objc_data: 0x2d0
-  __DATA_DIRTY.__data: 0x16710
+  __DATA_DIRTY.__data: 0x16708
   __DATA_DIRTY.__common: 0x1002c
-  __DATA_DIRTY.__bss: 0x2be9
+  __DATA_DIRTY.__bss: 0x2be1
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1890F375-1B2D-3A46-89D9-248BA17D371A
-  Functions: 36044
-  Symbols:   71969
-  CStrings:  18484
+  UUID: D250A74C-172C-3E9F-B01E-AFBC990928B3
+  Functions: 36013
+  Symbols:   71919
+  CStrings:  18487
 
Symbols:
+ _.memset_pattern.398
+ _.memset_pattern.402
+ __ZN3JSC14SourceProvider17sourceURLStrippedEv
+ __ZN3JSC16RegExpGlobalData20resetResultFromCacheEPNS_14JSGlobalObjectEPNS_6RegExpEPNS_8JSStringENS_11MatchResultEON3WTF6VectorIiLm0ENS8_15CrashOnOverflowELm16ENS8_10FastMallocEEE
+ __ZN3JSC18StringReplaceCache3setERKN3WTF6StringEPNS_6RegExpEPNS_20JSImmutableButterflyENS_11MatchResultERKNS1_6VectorIiLm0ENS1_15CrashOnOverflowELm16ENS1_10FastMallocEEE
+ __ZN3JSC25ModuleNamespaceAccessCaseC2ERNS_2VMEPNS_6JSCellENS_19CacheableIdentifierEPNS_23JSModuleNamespaceObjectEPNS_19JSModuleEnvironmentENS_11ScopeOffsetE
+ __ZN3JSC30WatchpointsOnStructureStubInfo35ensureReferenceAndInstallWatchpointERNSt3__110unique_ptrIS0_NS1_14default_deleteIS0_EEEEPNS_9CodeBlockEPNS_17StructureStubInfoERKNS_23ObjectPropertyConditionE
+ __ZN3JSC41generateConditionsForPrototypePropertyHitERNS_2VMEPNS_6JSCellEPNS_14JSGlobalObjectEPNS_9StructureEPNS_8JSObjectEPN3WTF17UniquedStringImplE
+ __ZN3JSC9CodeBlock16canGetCodeOriginENS_13CallSiteIndexE
+ __ZN3WTF11ThreadGroup6createEv
+ __ZN3WTF21ThreadSafeWeakHashSetINS_11ThreadGroupEE3addIS1_LPv0EEEvRKT_
+ __ZN3WTF3RefINS_11ThreadGroupENS_12RawPtrTraitsIS1_EEED2Ev
+ __ZN3WTF9HashTableIPKNS_11ThreadGroupENS_12KeyValuePairIS3_NS_6RefPtrINS_29ThreadSafeWeakPtrControlBlockENS_12RawPtrTraitsIS6_EENS_43ThreadSafeWeakPtrControlBlockRefDerefTraitsEEEEENS_24KeyValuePairKeyExtractorISB_EENS_11DefaultHashIS3_EENS_7HashMapIS3_SA_SF_NS_10HashTraitsIS3_EENSH_ISA_EENS_15HashTableTraitsEE18KeyValuePairTraitsESI_E15deallocateTableEPSB_
+ __ZN3WTF9HashTableIPKNS_11ThreadGroupENS_12KeyValuePairIS3_NS_6RefPtrINS_29ThreadSafeWeakPtrControlBlockENS_12RawPtrTraitsIS6_EENS_43ThreadSafeWeakPtrControlBlockRefDerefTraitsEEEEENS_24KeyValuePairKeyExtractorISB_EENS_11DefaultHashIS3_EENS_7HashMapIS3_SA_SF_NS_10HashTraitsIS3_EENSH_ISA_EENS_15HashTableTraitsEE18KeyValuePairTraitsESI_E6rehashEjPSB_
+ __ZN3WTF9HashTableIPKNS_11ThreadGroupENS_12KeyValuePairIS3_NS_6RefPtrINS_29ThreadSafeWeakPtrControlBlockENS_12RawPtrTraitsIS6_EENS_43ThreadSafeWeakPtrControlBlockRefDerefTraitsEEEEENS_24KeyValuePairKeyExtractorISB_EENS_11DefaultHashIS3_EENS_7HashMapIS3_SA_SF_NS_10HashTraitsIS3_EENSH_ISA_EENS_15HashTableTraitsEE18KeyValuePairTraitsESI_E8removeIfIZNKS_21ThreadSafeWeakHashSetIS1_E6valuesEvEUlRT_E_EEbRKSR_
+ __ZNK3JSC26ObjectPropertyConditionSet17slotBaseConditionEv
+ ___PRETTY_FUNCTION__._ZN3JSC14constructArrayILNS_21AllocationFailureModeE0EEEPNS_7JSArrayERNS_25ObjectInitializationScopeEPNS_9StructureEj
+ ___PRETTY_FUNCTION__._ZN3JSC9CodeBlock33newExceptionHandlingCallSiteIndexENS_13CallSiteIndexE
- _.memset_pattern.403
- __ZN3JSC14constructArrayERNS_25ObjectInitializationScopeEPNS_9StructureEj
- __ZN3JSC16RegExpGlobalData20resetResultFromCacheEPNS_14JSGlobalObjectEPNS_6RegExpEPNS_8JSStringEON3WTF6VectorIiLm0ENS7_15CrashOnOverflowELm16ENS7_10FastMallocEEE
- __ZN3JSC18StringReplaceCache3setERKN3WTF6StringEPNS_6RegExpEPNS_20JSImmutableButterflyERKNS1_6VectorIiLm0ENS1_15CrashOnOverflowELm16ENS1_10FastMallocEEE
- __ZN3JSC18StringReplaceCache5EntryD1Ev
- __ZN3JSC18StringReplaceCache5EntryaSEOS1_
- __ZN3JSC19MacroAssemblerARM648lshift64ENS_22AbstractMacroAssemblerINS_15ARM64EAssemblerEE12TrustedImm32ENS_14ARM64Registers10RegisterIDE
- __ZN3JSC23JSGenericTypedArrayViewINS_12Uint8AdaptorEE16setFromArrayLikeEPNS_14JSGlobalObjectEmNS_7JSValueE
- __ZN3JSC25ModuleNamespaceAccessCase6createERNS_2VMEPNS_6JSCellENS_19CacheableIdentifierEPNS_23JSModuleNamespaceObjectEPNS_19JSModuleEnvironmentENS_11ScopeOffsetE
- __ZN3JSC29constructArrayNegativeIndexedEPNS_14JSGlobalObjectEPNS_22ArrayAllocationProfileEPKNS_7JSValueEjS4_
- __ZN3JSC34appropriateOptimizingGetByFunctionENS_9GetByKindE
- __ZN3JSC41generateConditionsForPrototypePropertyHitERNS_2VMEPNS_6JSCellEPNS_14JSGlobalObjectEPNS_9StructureEPNS_8JSObjectEPN3WTF17UniquedStringImplENS_17PropertyCondition4KindE
- __ZN3JSC4Yarr12ByteCompiler10checkInputEj
- __ZN3JSC4Yarr12ByteCompiler12uncheckInputEj
- __ZN3JSC4Yarr12ByteCompiler16haveCheckedInputEj
- __ZN3JSC4Yarr12ByteCompiler21assertionWordBoundaryEbNS0_14MatchDirectionEj
- __ZN3JSC4Yarr12ByteCompiler25assertionDotStarEnclosureEbb
- __ZN3JSC4Yarr12ByteCompiler26alternativeBodyDisjunctionEb
- __ZN3JSC4Yarr12ByteCompiler26atomParenthesesTerminalEndEjjN3WTF7CheckedIjNS2_15CrashOnOverflowEEES5_NS0_14QuantifierTypeE
- __ZN3JSC4Yarr12ByteCompiler28atomParenthesesTerminalBeginEjNS0_14MatchDirectionEbjjj
- __ZN3JSC7JSArray26eagerlyInitializeButterflyERNS_25ObjectInitializationScopeEPS0_j
- __ZN3JSCL13actionForCellERNS_2VMEPNS_6JSCellE
- __ZN3WTF6RefPtrINS_14AtomStringImplENS_12RawPtrTraitsIS1_EENS_21DefaultRefDerefTraitsIS1_EEEaSEPS1_
- __ZN3WTF6VectorIN3JSC13SnippetParams5ValueELm0ENS_15CrashOnOverflowELm16ENS_10FastMallocEE14appendSlowCaseILNS_13FailureActionE0ERNS1_14ARM64Registers10RegisterIDEEEbOT0_
- __ZN3WTF6VectorIN3JSC14ARM64Registers10RegisterIDELm0ENS_15CrashOnOverflowELm16ENS_10FastMallocEE14appendSlowCaseILNS_13FailureActionE0ERS3_EEbOT0_
- __ZN3WTF6VectorIN3JSC14ARM64Registers12FPRegisterIDELm0ENS_15CrashOnOverflowELm16ENS_10FastMallocEE14appendSlowCaseILNS_13FailureActionE0ES3_EEbOT0_
- __ZN3WTF6VectorIN3JSC4Yarr8ByteTermELm0ENS_15CrashOnOverflowELm16ENS_10FastMallocEE14appendSlowCaseILNS_13FailureActionE0ERS3_EEbOT0_
- __ZN3WTF6VectorINSt3__110shared_ptrINS_11ThreadGroupEEELm0ENS_15CrashOnOverflowELm16ENS_10FastMallocEE14expandCapacityILNS_13FailureActionE0EEEPS4_mSA_
- __ZN3WTF7HashMapIPNS_11ThreadGroupENSt3__18weak_ptrIS1_EENS_11DefaultHashIS2_EENS_10HashTraitsIS2_EENS8_IS5_EENS_15HashTableTraitsEE3addIS5_EENS_18HashTableAddResultINS_17HashTableIteratorINS_9HashTableIS2_NS_12KeyValuePairIS2_S5_EENS_24KeyValuePairKeyExtractorISI_EES7_NSC_18KeyValuePairTraitsES9_EES2_SI_SK_S7_SL_S9_EEEEOS2_OT_
- __ZN3WTF7HashMapIPNS_11ThreadGroupENSt3__18weak_ptrIS1_EENS_11DefaultHashIS2_EENS_10HashTraitsIS2_EENS8_IS5_EENS_15HashTableTraitsEE6removeERKS2_
- __ZN3WTF9HashTableIPNS_11ThreadGroupENS_12KeyValuePairIS2_NSt3__18weak_ptrIS1_EEEENS_24KeyValuePairKeyExtractorIS7_EENS_11DefaultHashIS2_EENS_7HashMapIS2_S6_SB_NS_10HashTraitsIS2_EENSD_IS6_EENS_15HashTableTraitsEE18KeyValuePairTraitsESE_E6rehashEjPS7_
- __ZNK3JSC17JSArrayBufferView10isDetachedEv
- __ZNK3JSC8JSObject21findPropertyHashEntryENS_12PropertyNameE
- __ZNKSt3__119__shared_weak_count13__get_deleterERKSt9type_info
- __ZNSt3__110unique_ptrIN3JSC4Wasm8Worklist6ThreadENS_14default_deleteIS4_EEED1B7v160006Ev
- __ZNSt3__110unique_ptrIN3JSC4Yarr18PatternDisjunctionENS_14default_deleteIS3_EEEaSB7v160006EDn
- __ZNSt3__119__shared_weak_count4lockEv
- __ZNSt3__119__shared_weak_countD2Ev
- __ZNSt3__120__shared_ptr_emplaceIN3WTF11ThreadGroupENS1_13FastAllocatorIS2_EEE16__on_zero_sharedEv
- __ZNSt3__120__shared_ptr_emplaceIN3WTF11ThreadGroupENS1_13FastAllocatorIS2_EEE21__on_zero_shared_weakEv
- __ZNSt3__120__shared_ptr_emplaceIN3WTF11ThreadGroupENS1_13FastAllocatorIS2_EEED0Ev
- __ZNSt3__120__shared_ptr_emplaceIN3WTF11ThreadGroupENS1_13FastAllocatorIS2_EEED1Ev
- __ZNSt3__120__throw_bad_weak_ptrB7v160006Ev
- __ZTVNSt3__120__shared_ptr_emplaceIN3WTF11ThreadGroupENS1_13FastAllocatorIS2_EEEE
- ___PRETTY_FUNCTION__._ZN3JSC14constructArrayERNS_25ObjectInitializationScopeEPNS_9StructureEj
CStrings:
+ "/AppleInternal/Library/BuildRoots/7cbd30cc-6919-11ee-a253-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/include/c++/v1/__algorithm/clamp.h"
+ "/AppleInternal/Library/BuildRoots/7cbd30cc-6919-11ee-a253-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/include/c++/v1/__algorithm/pop_heap.h"
+ "/AppleInternal/Library/BuildRoots/7cbd30cc-6919-11ee-a253-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/include/c++/v1/__algorithm/sift_down.h"
+ "/AppleInternal/Library/BuildRoots/7cbd30cc-6919-11ee-a253-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/include/c++/v1/__memory/construct_at.h"
+ "/AppleInternal/Library/BuildRoots/7cbd30cc-6919-11ee-a253-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/include/c++/v1/__string/char_traits.h"
+ "/AppleInternal/Library/BuildRoots/7cbd30cc-6919-11ee-a253-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/include/c++/v1/__tree"
+ "/AppleInternal/Library/BuildRoots/7cbd30cc-6919-11ee-a253-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/include/c++/v1/__utility/unreachable.h"
+ "/AppleInternal/Library/BuildRoots/7cbd30cc-6919-11ee-a253-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/include/c++/v1/array"
+ "/AppleInternal/Library/BuildRoots/7cbd30cc-6919-11ee-a253-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/include/c++/v1/optional"
+ "/AppleInternal/Library/BuildRoots/7cbd30cc-6919-11ee-a253-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/include/c++/v1/span"
+ "/AppleInternal/Library/BuildRoots/7cbd30cc-6919-11ee-a253-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/include/c++/v1/string"
+ "/AppleInternal/Library/BuildRoots/7cbd30cc-6919-11ee-a253-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/local/include/wtf/Assertions.h"
+ "/AppleInternal/Library/BuildRoots/7cbd30cc-6919-11ee-a253-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/local/include/wtf/ConcurrentPtrHashSet.h"
+ "/AppleInternal/Library/BuildRoots/7cbd30cc-6919-11ee-a253-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/local/include/wtf/Deque.h"
+ "/AppleInternal/Library/BuildRoots/7cbd30cc-6919-11ee-a253-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/local/include/wtf/IndexMap.h"
+ "/AppleInternal/Library/BuildRoots/7cbd30cc-6919-11ee-a253-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/local/include/wtf/Liveness.h"
+ "/AppleInternal/Library/BuildRoots/7cbd30cc-6919-11ee-a253-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/local/include/wtf/LockAlgorithmInlines.h"
+ "/AppleInternal/Library/BuildRoots/7cbd30cc-6919-11ee-a253-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/local/include/wtf/NaturalLoops.h"
+ "/AppleInternal/Library/BuildRoots/7cbd30cc-6919-11ee-a253-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/local/include/wtf/ObjectIdentifier.h"
+ "/AppleInternal/Library/BuildRoots/7cbd30cc-6919-11ee-a253-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/local/include/wtf/RedBlackTree.h"
+ "/AppleInternal/Library/BuildRoots/7cbd30cc-6919-11ee-a253-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/local/include/wtf/SinglyLinkedListWithTail.h"
+ "/AppleInternal/Library/BuildRoots/7cbd30cc-6919-11ee-a253-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/local/include/wtf/StdLibExtras.h"
+ "/AppleInternal/Library/BuildRoots/7cbd30cc-6919-11ee-a253-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/local/include/wtf/ThreadSafeWeakHashSet.h"
+ "/AppleInternal/Library/BuildRoots/7cbd30cc-6919-11ee-a253-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/local/include/wtf/ThreadSpecific.h"
+ "/AppleInternal/Library/BuildRoots/7cbd30cc-6919-11ee-a253-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/local/include/wtf/text/StringBuilder.h"
+ "/AppleInternal/Library/BuildRoots/7cbd30cc-6919-11ee-a253-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/local/include/wtf/text/StringConcatenate.h"
+ "/Library/Caches/com.apple.xbs/Sources/WTF/Source/WTF/wtf/ThreadSafeWeakHashSet.h"
+ "JSArray *JSC::constructArray(ObjectInitializationScope &, Structure *, unsigned int) [failureMode = JSC::AllocationFailureMode::Assert]"
+ "LValue JSC::FTL::(anonymous namespace)::LowerDFGToB3::emitCodeBasedOnEndiannessBranch(LValue, const F1 &, const F2 &) [F1 = (lambda at /Library/Caches/com.apple.xbs/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:17565:45), F2 = (lambda at /Library/Caches/com.apple.xbs/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:17571:42)]"
+ "LValue JSC::FTL::(anonymous namespace)::LowerDFGToB3::emitCodeBasedOnEndiannessBranch(LValue, const F1 &, const F2 &) [F1 = (lambda at /Library/Caches/com.apple.xbs/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:17602:49), F2 = (lambda at /Library/Caches/com.apple.xbs/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:17605:46)]"
+ "LValue JSC::FTL::(anonymous namespace)::LowerDFGToB3::emitCodeBasedOnEndiannessBranch(LValue, const F1 &, const F2 &) [F1 = (lambda at /Library/Caches/com.apple.xbs/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:17625:45), F2 = (lambda at /Library/Caches/com.apple.xbs/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:17629:42)]"
+ "LValue JSC::FTL::(anonymous namespace)::LowerDFGToB3::emitCodeBasedOnEndiannessBranch(LValue, const F1 &, const F2 &) [F1 = (lambda at /Library/Caches/com.apple.xbs/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:17654:45), F2 = (lambda at /Library/Caches/com.apple.xbs/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:17658:42)]"
+ "Structure_seenProperties"
+ "auto JSC::FTL::(anonymous namespace)::LowerDFGToB3::compileCallOrConstructVarargsSpread()::(anonymous class)::operator()(auto, Node *) const [self:auto = std::reference_wrapper<const WTF::RecursableLambda<(lambda at /Library/Caches/com.apple.xbs/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:11649:70)>>]"
+ "auto JSC::FTL::(anonymous namespace)::LowerDFGToB3::compileForwardVarargsWithSpread()::(anonymous class)::operator()(auto, Node *, LValue) const [self:auto = std::reference_wrapper<const WTF::RecursableLambda<(lambda at /Library/Caches/com.apple.xbs/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:12693:47)>>]"
+ "void JSC::FTL::(anonymous namespace)::LowerDFGToB3::compare(const IntFunctor &, const DoubleFunctor &, C_JITOperation_TT, C_JITOperation_B_GJssJss, S_JITOperation_GJJ) [IntFunctor = (lambda at /Library/Caches/com.apple.xbs/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:11068:13), DoubleFunctor = (lambda at /Library/Caches/com.apple.xbs/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:11071:13)]"
+ "void JSC::FTL::(anonymous namespace)::LowerDFGToB3::compare(const IntFunctor &, const DoubleFunctor &, C_JITOperation_TT, C_JITOperation_B_GJssJss, S_JITOperation_GJJ) [IntFunctor = (lambda at /Library/Caches/com.apple.xbs/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:11082:13), DoubleFunctor = (lambda at /Library/Caches/com.apple.xbs/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:11085:13)]"
+ "void JSC::FTL::(anonymous namespace)::LowerDFGToB3::compare(const IntFunctor &, const DoubleFunctor &, C_JITOperation_TT, C_JITOperation_B_GJssJss, S_JITOperation_GJJ) [IntFunctor = (lambda at /Library/Caches/com.apple.xbs/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:11096:13), DoubleFunctor = (lambda at /Library/Caches/com.apple.xbs/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:11099:13)]"
+ "void JSC::FTL::(anonymous namespace)::LowerDFGToB3::compare(const IntFunctor &, const DoubleFunctor &, C_JITOperation_TT, C_JITOperation_B_GJssJss, S_JITOperation_GJJ) [IntFunctor = (lambda at /Library/Caches/com.apple.xbs/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:11110:13), DoubleFunctor = (lambda at /Library/Caches/com.apple.xbs/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:11113:13)]"
+ "void WTF::ThreadSafeWeakHashSet<WTF::ThreadGroup>::add(const U &) [T = WTF::ThreadGroup, U = WTF::ThreadGroup]"
- "/AppleInternal/Library/BuildRoots/514cd921-593e-11ee-8d01-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/include/c++/v1/__algorithm/clamp.h"
- "/AppleInternal/Library/BuildRoots/514cd921-593e-11ee-8d01-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/include/c++/v1/__algorithm/pop_heap.h"
- "/AppleInternal/Library/BuildRoots/514cd921-593e-11ee-8d01-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/include/c++/v1/__algorithm/sift_down.h"
- "/AppleInternal/Library/BuildRoots/514cd921-593e-11ee-8d01-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/include/c++/v1/__memory/construct_at.h"
- "/AppleInternal/Library/BuildRoots/514cd921-593e-11ee-8d01-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/include/c++/v1/__string/char_traits.h"
- "/AppleInternal/Library/BuildRoots/514cd921-593e-11ee-8d01-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/include/c++/v1/__tree"
- "/AppleInternal/Library/BuildRoots/514cd921-593e-11ee-8d01-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/include/c++/v1/__utility/unreachable.h"
- "/AppleInternal/Library/BuildRoots/514cd921-593e-11ee-8d01-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/include/c++/v1/array"
- "/AppleInternal/Library/BuildRoots/514cd921-593e-11ee-8d01-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/include/c++/v1/optional"
- "/AppleInternal/Library/BuildRoots/514cd921-593e-11ee-8d01-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/include/c++/v1/span"
- "/AppleInternal/Library/BuildRoots/514cd921-593e-11ee-8d01-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/include/c++/v1/string"
- "/AppleInternal/Library/BuildRoots/514cd921-593e-11ee-8d01-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/local/include/wtf/Assertions.h"
- "/AppleInternal/Library/BuildRoots/514cd921-593e-11ee-8d01-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/local/include/wtf/ConcurrentPtrHashSet.h"
- "/AppleInternal/Library/BuildRoots/514cd921-593e-11ee-8d01-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/local/include/wtf/Deque.h"
- "/AppleInternal/Library/BuildRoots/514cd921-593e-11ee-8d01-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/local/include/wtf/IndexMap.h"
- "/AppleInternal/Library/BuildRoots/514cd921-593e-11ee-8d01-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/local/include/wtf/Liveness.h"
- "/AppleInternal/Library/BuildRoots/514cd921-593e-11ee-8d01-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/local/include/wtf/LockAlgorithmInlines.h"
- "/AppleInternal/Library/BuildRoots/514cd921-593e-11ee-8d01-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/local/include/wtf/NaturalLoops.h"
- "/AppleInternal/Library/BuildRoots/514cd921-593e-11ee-8d01-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/local/include/wtf/ObjectIdentifier.h"
- "/AppleInternal/Library/BuildRoots/514cd921-593e-11ee-8d01-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/local/include/wtf/RedBlackTree.h"
- "/AppleInternal/Library/BuildRoots/514cd921-593e-11ee-8d01-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/local/include/wtf/SinglyLinkedListWithTail.h"
- "/AppleInternal/Library/BuildRoots/514cd921-593e-11ee-8d01-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/local/include/wtf/StdLibExtras.h"
- "/AppleInternal/Library/BuildRoots/514cd921-593e-11ee-8d01-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/local/include/wtf/ThreadSafeWeakHashSet.h"
- "/AppleInternal/Library/BuildRoots/514cd921-593e-11ee-8d01-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/local/include/wtf/ThreadSpecific.h"
- "/AppleInternal/Library/BuildRoots/514cd921-593e-11ee-8d01-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/local/include/wtf/text/StringBuilder.h"
- "/AppleInternal/Library/BuildRoots/514cd921-593e-11ee-8d01-0697ca55970a/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.0.Internal.sdk/usr/local/include/wtf/text/StringConcatenate.h"
- "JSArray *JSC::constructArray(ObjectInitializationScope &, Structure *, unsigned int)"
- "LValue JSC::FTL::(anonymous namespace)::LowerDFGToB3::emitCodeBasedOnEndiannessBranch(LValue, const F1 &, const F2 &) [F1 = (lambda at /Library/Caches/com.apple.xbs/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:17562:45), F2 = (lambda at /Library/Caches/com.apple.xbs/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:17568:42)]"
- "LValue JSC::FTL::(anonymous namespace)::LowerDFGToB3::emitCodeBasedOnEndiannessBranch(LValue, const F1 &, const F2 &) [F1 = (lambda at /Library/Caches/com.apple.xbs/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:17599:49), F2 = (lambda at /Library/Caches/com.apple.xbs/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:17602:46)]"
- "LValue JSC::FTL::(anonymous namespace)::LowerDFGToB3::emitCodeBasedOnEndiannessBranch(LValue, const F1 &, const F2 &) [F1 = (lambda at /Library/Caches/com.apple.xbs/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:17622:45), F2 = (lambda at /Library/Caches/com.apple.xbs/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:17626:42)]"
- "LValue JSC::FTL::(anonymous namespace)::LowerDFGToB3::emitCodeBasedOnEndiannessBranch(LValue, const F1 &, const F2 &) [F1 = (lambda at /Library/Caches/com.apple.xbs/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:17651:45), F2 = (lambda at /Library/Caches/com.apple.xbs/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:17655:42)]"
- "auto JSC::FTL::(anonymous namespace)::LowerDFGToB3::compileCallOrConstructVarargsSpread()::(anonymous class)::operator()(auto, Node *) const [self:auto = std::reference_wrapper<const WTF::RecursableLambda<(lambda at /Library/Caches/com.apple.xbs/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:11646:70)>>]"
- "auto JSC::FTL::(anonymous namespace)::LowerDFGToB3::compileForwardVarargsWithSpread()::(anonymous class)::operator()(auto, Node *, LValue) const [self:auto = std::reference_wrapper<const WTF::RecursableLambda<(lambda at /Library/Caches/com.apple.xbs/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:12690:47)>>]"
- "void JSC::FTL::(anonymous namespace)::LowerDFGToB3::compare(const IntFunctor &, const DoubleFunctor &, C_JITOperation_TT, C_JITOperation_B_GJssJss, S_JITOperation_GJJ) [IntFunctor = (lambda at /Library/Caches/com.apple.xbs/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:11065:13), DoubleFunctor = (lambda at /Library/Caches/com.apple.xbs/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:11068:13)]"
- "void JSC::FTL::(anonymous namespace)::LowerDFGToB3::compare(const IntFunctor &, const DoubleFunctor &, C_JITOperation_TT, C_JITOperation_B_GJssJss, S_JITOperation_GJJ) [IntFunctor = (lambda at /Library/Caches/com.apple.xbs/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:11079:13), DoubleFunctor = (lambda at /Library/Caches/com.apple.xbs/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:11082:13)]"
- "void JSC::FTL::(anonymous namespace)::LowerDFGToB3::compare(const IntFunctor &, const DoubleFunctor &, C_JITOperation_TT, C_JITOperation_B_GJssJss, S_JITOperation_GJJ) [IntFunctor = (lambda at /Library/Caches/com.apple.xbs/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:11093:13), DoubleFunctor = (lambda at /Library/Caches/com.apple.xbs/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:11096:13)]"
- "void JSC::FTL::(anonymous namespace)::LowerDFGToB3::compare(const IntFunctor &, const DoubleFunctor &, C_JITOperation_TT, C_JITOperation_B_GJssJss, S_JITOperation_GJJ) [IntFunctor = (lambda at /Library/Caches/com.apple.xbs/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:11107:13), DoubleFunctor = (lambda at /Library/Caches/com.apple.xbs/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:11110:13)]"

```
