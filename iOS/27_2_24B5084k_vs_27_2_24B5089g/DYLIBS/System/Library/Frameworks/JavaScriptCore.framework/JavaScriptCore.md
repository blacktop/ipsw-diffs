## JavaScriptCore

> `/System/Library/Frameworks/JavaScriptCore.framework/JavaScriptCore`

```diff

-625.2.4.1.0
-  __TEXT.__text: 0x22ecc94
+625.2.5.10.1
+  __TEXT.__text: 0x22e7bd4
   __TEXT.__jsc_int: 0x6a5b8
   __TEXT.__objc_methlist: 0xb9c
-  __TEXT.__const: 0xa0fe4
+  __TEXT.__const: 0xa1014
   __TEXT.__dlsym_cstr: 0x34
-  __TEXT.__cstring: 0x1275d8
+  __TEXT.__cstring: 0x127838
   __TEXT.__oslogstring: 0xa0f
-  __TEXT.__gcc_except_tab: 0x2918
+  __TEXT.__gcc_except_tab: 0x2930
   __TEXT.__ustring: 0x10
-  __TEXT.__unwind_info: 0x208a8
+  __TEXT.__unwind_info: 0x20888
   __TEXT.__eh_frame: 0x50
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __AUTH_CONST.__objc_const: 0xdf8
   __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__auth_got: 0x1810
-  __AUTH.__objc_data: 0xf0
-  __AUTH.__data: 0x288
+  __AUTH.__objc_data: 0xa0
+  __AUTH.__data: 0x238
   __DATA.__objc_ivar: 0x80
   __DATA.__crash_info: 0x148
-  __DATA.__data: 0x10570
-  __DATA.__common: 0x2d60
+  __DATA.__data: 0x104b0
+  __DATA.__common: 0x2d40
   __DATA_DIRTY.__objc_ivar: 0x8
-  __DATA_DIRTY.__objc_data: 0x280
-  __DATA_DIRTY.__data: 0x13ed8
+  __DATA_DIRTY.__objc_data: 0x2d0
+  __DATA_DIRTY.__data: 0x13ff0
   __DATA_DIRTY.__wtf_config: 0x4000
-  __DATA_DIRTY.__common: 0x485150
+  __DATA_DIRTY.__common: 0x485170
   __DATA_DIRTY.__bss: 0xf650
   - /System/Library/Frameworks/BrowserEngineCore.framework/BrowserEngineCore
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 40106
-  Symbols:   48367
-  CStrings:  25828
+  Functions: 40097
+  Symbols:   48373
+  CStrings:  25836
 
Symbols:
+ __ZN3JSC10AccessCase13createReplaceERNS_2VMEPNS_6JSCellENS_19CacheableIdentifierEiPNS_9StructureEb
+ __ZN3JSC10JSFunction41reifyLazyPropertyForHostOrBuiltinIfNeededERNS_2VMEPNS_14JSGlobalObjectENS_12PropertyNameE
+ __ZN3JSC11MarkedBlock6Handle16specializedSweepILb1ELNS1_9EmptyModeE0ELNS1_9SweepModeE1ELNS1_20SweepDestructionModeE1ELNS1_12ScribbleModeE0ELNS1_18NewlyAllocatedModeE1ELNS1_9MarksModeE1ENS_31JSDestructibleObjectDestroyFuncEEEvPNS_8FreeListES3_S4_S5_S6_S7_S8_RKT6_
+ __ZN3JSC12allocateCellINS_10JSFunctionEEEPvRNS_2VMEm
+ __ZN3JSC15OpGetByIdDirect6decodeEPKh
+ __ZN3JSC17AssemblerDataImplILNS_17AssemblerDataTypeE0EEC1Ev
+ __ZN3JSC22SetPrivateBrandVariant14visitAggregateERNS_19AbstractSlotVisitorE
+ __ZN3JSC23CheckPrivateBrandStatus14visitAggregateERNS_19AbstractSlotVisitorE
+ __ZN3JSC23JSGenericTypedArrayViewINS_13Uint16AdaptorEE20createWithFastVectorEPNS_14JSGlobalObjectEPNS_9StructureEmPv
+ __ZN3JSC23JSGenericTypedArrayViewINS_14Float64AdaptorEE20createWithFastVectorEPNS_14JSGlobalObjectEPNS_9StructureEmPv
+ __ZN3JSC3DFG21newTypedArrayWithSizeINS_23JSGenericTypedArrayViewINS_13Uint16AdaptorEEEEEPcPNS_14JSGlobalObjectERNS_2VMEPNS_9StructureElS5_
+ __ZN3JSC3DFG5Graph26regExpFirstCharacterBitmapEPNS_6RegExpENS_28FirstCharacterFilterPositionE
+ __ZN3JSC3FTL12_GLOBAL__N_112LowerDFGToB315compileIncOrDecEv
+ __ZN3JSC3FTL12_GLOBAL__N_112LowerDFGToB323compileRegExpExecStickyEv
+ __ZN3JSC3FTL12_GLOBAL__N_112LowerDFGToB339compileMaterializeNewArrayWithButterflyEv
+ __ZN3JSC3FTL6Output9operationIPFNS_24ExceptionOperationResultIxEEPNS_14JSGlobalObjectEPNS_6RegExpEPNS_12RegExpObjectEPNS_8JSStringEEEEPNS_2B35ValueET_
+ __ZN3JSC3FTL6Output9operationIPFNS_24ExceptionOperationResultIyEEPNS_14JSGlobalObjectEPNS_9ButterflyExiEEEPNS_2B35ValueET_
+ __ZN3JSC40maximumExecutionCountsBetweenCheckpointsENS_15CountingVariantEPNS_9CodeBlockE
+ __ZN3JSC4Wasm14IPIntGenerator23branchTargetMetadataForERKNS0_16IPIntControlTypeEj
+ __ZN3JSC4Yarr27FirstCharacterBitmapBuilder20collectLatin1MembersEPKNS0_14CharacterClassERN3WTF6BitSetILm256EyEE
+ __ZN3JSC5shiftILNS_7JSArray14ShiftCountModeE0EEEvPNS_14JSGlobalObjectEPNS_8JSObjectEyyyy
+ __ZN3JSC7JSArray12fastIncludesEPNS_14JSGlobalObjectENS_7JSValueEyy
+ __ZN3JSC8JSCalleeC2ERNS_2VMEPNS_7JSScopeEPNS_9StructureE
+ __ZN3JSC9JITMathICINS_15JITNegGeneratorENS_17UnaryArithProfileEE18finalizeInlineCodeERKNS_21MathICGenerationStateERNS_10LinkBufferE
+ __ZN3JSC9Structure11markIfCheapINS_19AbstractSlotVisitorEEEbRT_
+ __ZN3JSCL21functionWasmCalleeIDsEPNS_14JSGlobalObjectEPNS_9CallFrameE
+ __ZN3WTF11PrintStream10atomicallyIZN3JSC11MarkedBlock6Handle16specializedSweepILb1ELNS4_9EmptyModeE0ELNS4_9SweepModeE0ELNS4_20SweepDestructionModeE1ELNS4_12ScribbleModeE0ELNS4_18NewlyAllocatedModeE1ELNS4_9MarksModeE1ENS2_15IsoHeapCellTypeEEEvPNS2_8FreeListES6_S7_S8_S9_SA_SB_RKT6_EUlRS0_E_EEvRKT_
+ __ZN3WTF11PrintStream10atomicallyIZN3JSC11MarkedBlock6Handle16specializedSweepILb1ELNS4_9EmptyModeE0ELNS4_9SweepModeE0ELNS4_20SweepDestructionModeE1ELNS4_12ScribbleModeE0ELNS4_18NewlyAllocatedModeE1ELNS4_9MarksModeE1ENS2_18DefaultDestroyFuncEEEvPNS2_8FreeListES6_S7_S8_S9_SA_SB_RKT6_EUlRS0_E_EEvRKT_
+ __ZN3WTF11PrintStream10atomicallyIZN3JSC11MarkedBlock6Handle16specializedSweepILb1ELNS4_9EmptyModeE0ELNS4_9SweepModeE0ELNS4_20SweepDestructionModeE1ELNS4_12ScribbleModeE0ELNS4_18NewlyAllocatedModeE1ELNS4_9MarksModeE1ENS2_22IsoInlinedHeapCellTypeINS2_8JSStringEE11DestroyFuncEEEvPNS2_8FreeListES6_S7_S8_S9_SA_SB_RKT6_EUlRS0_E_EEvRKT_
+ __ZN3WTF12VectorBufferIN3JSC4Wasm13IPIntLocationELm0ENS_10FastMallocEE5adoptEOS5_
+ __ZN3WTF25ThreadSafeWeakOrStrongPtrIN3JSC4Wasm9BBQCalleeEED2Ev
+ __ZN3WTF6Detail15CallableWrapperIZN3JSC22JSFinalizationRegistry23finalizeUnconditionallyERNS2_2VMENS2_15CollectionScopeEE3$_3vJRNS2_17DeferredWorkTimer6TicketEEE4callESA_
+ __ZN3WTF6Detail15CallableWrapperIZN3JSC22JSFinalizationRegistry23finalizeUnconditionallyERNS2_2VMENS2_15CollectionScopeEE3$_3vJRNS2_17DeferredWorkTimer6TicketEEED0Ev
+ __ZN3WTF6Detail15CallableWrapperIZN3JSC22JSFinalizationRegistry23finalizeUnconditionallyERNS2_2VMENS2_15CollectionScopeEE3$_3vJRNS2_17DeferredWorkTimer6TicketEEED1Ev
+ __ZN3WTF6VectorIN3JSC12GetByVariantELm1ENS_15CrashOnOverflowELm16ENS_10FastMallocEE14shrinkCapacityEm
+ __ZN3WTF8LivenessIN3JSC2B33Air25UnifiedTmpLivenessAdapterEE7Workset6removeEj
+ __ZN3WTF9HashTableIN3JSC3DFG20PromotedHeapLocationENS_12KeyValuePairIS3_NS2_12AvailabilityEEENS_24KeyValuePairKeyExtractorIS6_EENS_11DefaultHashIS3_EENS_7HashMapIS3_S5_SA_NS_10HashTraitsIS3_EENSC_IS5_EENS_15HashTableTraitsELNS_17ShouldValidateKeyE0ENS_10FastMallocEE18KeyValuePairTraitsESD_SH_E5beginEv
+ __ZN3WTF9URLParser13percentDecodeENSt3__14spanIKhLm18446744073709551615EEE
+ __ZN3WTFL16machTimebaseInfoEv
+ __ZNK3JSC10CodeOrigin11stackOffsetEv
+ __ZNK3JSC12StructureSet11markIfCheapINS_19AbstractSlotVisitorEEEvRT_
+ __ZNK3JSC4Wasm11CalleeGroup18calleeIsReferencedERKN3WTF14AbstractLockerEPNS0_6CalleeE
+ __ZNK3JSC4Wasm14IPIntGenerator4failIJPKcjS4_tEEENSt3__110unexpectedIN3WTF6StringEEEDpT_
+ __ZNK3JSC9Structure21findPropertyHashEntryENS_12PropertyNameE
+ __ZNK3WTF29ThreadSafeWeakPtrControlBlock29makeStrongReferenceIfPossibleIN3JSC4Wasm17OMGOSREntryCalleeEEENS_6RefPtrIT_NS_12RawPtrTraitsIS6_EENS_21DefaultRefDerefTraitsIS6_EEEEPKS6_
+ __ZNK3WTF9HashTableIN3JSC3DFG20PromotedHeapLocationES3_NS_17IdentityExtractorENS_11DefaultHashIS3_EENS_10HashTraitsIS3_EES8_NS_10FastMallocEE5beginEv
+ __ZNK3WTF9HashTableIPN3JSC16MarkedVectorBaseES3_NS_17IdentityExtractorENS_11DefaultHashIS3_EENS_10HashTraitsIS3_EES8_NS_10FastMallocEE5beginEv
+ __ZTVN3WTF6Detail15CallableWrapperIZN3JSC22JSFinalizationRegistry23finalizeUnconditionallyERNS2_2VMENS2_15CollectionScopeEE3$_3vJRNS2_17DeferredWorkTimer6TicketEEEE
+ ___PRETTY_FUNCTION__._ZN3JSC17ConservativeRoots14genericAddSpanINS_13DummyMarkHookEEEvPvS3_RT_
+ ___PRETTY_FUNCTION__._ZN3JSC40maximumExecutionCountsBetweenCheckpointsENS_15CountingVariantEPNS_9CodeBlockE
+ ___PRETTY_FUNCTION__._ZNK3WTF20ConcurrentPtrHashSet12containsImplEPv
+ _pas_physical_page_sharing_pool_take_for_page_config
- __ZN3JSC10InByStatus14visitAggregateERNS_19AbstractSlotVisitorE
- __ZN3JSC10JSFunction26reifyLazyBoundNameIfNeededERNS_2VMEPNS_14JSGlobalObjectENS_12PropertyNameE
- __ZN3JSC11MarkedBlock6Handle16specializedSweepILb1ELNS1_9EmptyModeE0ELNS1_9SweepModeE0ELNS1_20SweepDestructionModeE1ELNS1_12ScribbleModeE0ELNS1_18NewlyAllocatedModeE1ELNS1_9MarksModeE1ENS_15IsoHeapCellTypeEEEvPNS_8FreeListES3_S4_S5_S6_S7_S8_RKT6_
- __ZN3JSC11MarkedBlock6Handle16specializedSweepILb1ELNS1_9EmptyModeE0ELNS1_9SweepModeE0ELNS1_20SweepDestructionModeE1ELNS1_12ScribbleModeE0ELNS1_18NewlyAllocatedModeE1ELNS1_9MarksModeE1ENS_22IsoInlinedHeapCellTypeINS_8JSStringEE11DestroyFuncEEEvPNS_8FreeListES3_S4_S5_S6_S7_S8_RKT6_
- __ZN3JSC12PutByVariant10transitionENS_19CacheableIdentifierERKNS_12StructureSetEPNS_9StructureERKNS_26ObjectPropertyConditionSetEi
- __ZN3JSC12allocateCellINS_15JSAsyncFunctionEEEPvRNS_2VMEm
- __ZN3JSC15JSAsyncFunction43createWithInvalidatedReallocationWatchpointERNS_2VMEPNS_14JSGlobalObjectEPNS_18FunctionExecutableEPNS_7JSScopeEPNS_9StructureE
- __ZN3JSC19MacroAssemblerARM6410vectorShl8ENS_8SIMDInfoENS_14ARM64Registers12FPRegisterIDENS_22AbstractMacroAssemblerINS_15ARM64EAssemblerEE12TrustedImm32ES3_
- __ZN3JSC19MacroAssemblerARM6419convertInt32ToFloatENS_14ARM64Registers10RegisterIDENS1_12FPRegisterIDE
- __ZN3JSC22AbstractMacroAssemblerINS_15ARM64EAssemblerEE7commentIJA13_cNS_14ARM64Registers12FPRegisterIDEA17_cNS_11JSValueRegsEA28_cNS_20RegisterAtOffsetListEEEEvDpRKT_
- __ZN3JSC22AbstractMacroAssemblerINS_15ARM64EAssemblerEE7commentIJA30_cEEEvDpRKT_
- __ZN3JSC22AbstractMacroAssemblerINS_15ARM64EAssemblerEE7commentIJA5_cjA4_cNS_4Wasm4TypeEEEEvDpRKT_
- __ZN3JSC22AlignedMemoryAllocator17registerDirectoryERNS_4HeapEPNS_14BlockDirectoryE
- __ZN3JSC25ModuleNamespaceAccessCase6createERNS_2VMEPNS_6JSCellENS_19CacheableIdentifierEPNS_23JSModuleNamespaceObjectEPNS_19JSModuleEnvironmentENS_11ScopeOffsetE
- __ZN3JSC25ModuleNamespaceAccessCaseC2ERNS_2VMEPNS_6JSCellENS_19CacheableIdentifierEPNS_23JSModuleNamespaceObjectEPNS_19JSModuleEnvironmentENS_11ScopeOffsetE
- __ZN3JSC3DFG14ByteCodeParser18handleIteratorOpenEPKNS_15BaseInstructionINS_14JSOpcodeTraitsEEENS_13BytecodeIndexE
- __ZN3JSC3DFG14SpeculativeJIT20speculateStringIdentENS0_4EdgeENS_14ARM64Registers10RegisterIDE
- __ZN3JSC3FTL12_GLOBAL__N_112LowerDFGToB313speculateMiscENS_3DFG4EdgeE
- __ZN3JSC3FTL12_GLOBAL__N_112LowerDFGToB314allocateObjectINS_7JSArrayENS_3DFG19RegisteredStructureEEEPNS_2B35ValueET0_S9_PNS7_10BasicBlockE
- __ZN3JSC3FTL12_GLOBAL__N_112LowerDFGToB319compileStringSubstrEv
- __ZN3JSC3FTL12_GLOBAL__N_112LowerDFGToB320compileDoubleAsInt32Ev
- __ZN3JSC3FTL12_GLOBAL__N_112LowerDFGToB324compileInByIdMegamorphicEv
- __ZN3JSC4Wasm11IPIntCalleeC1ERNS0_30FunctionIPIntMetadataGeneratorENS0_18FunctionSpaceIndexERKNS0_3RTTEONSt3__14pairIPKN3WTF6VectorIDuLm0ENSA_15CrashOnOverflowELm16ENSA_10FastMallocEEENSA_6RefPtrINS0_11NameSectionENSA_12RawPtrTraitsISI_EENSA_21DefaultRefDerefTraitsISI_EEEEEE
- __ZN3JSC4Wasm15TypeInformation15getCanonicalRTTEm
- __ZN3JSCL10copyMemoryEPvPKvm
- __ZN3WTF11PrintStream10atomicallyIZN3JSC11MarkedBlock6Handle16specializedSweepILb1ELNS4_9EmptyModeE0ELNS4_9SweepModeE1ELNS4_20SweepDestructionModeE1ELNS4_12ScribbleModeE0ELNS4_18NewlyAllocatedModeE1ELNS4_9MarksModeE1ENS2_15IsoHeapCellTypeEEEvPNS2_8FreeListES6_S7_S8_S9_SA_SB_RKT6_EUlRS0_E_EEvRKT_
- __ZN3WTF12VectorBufferIN3JSC2B33Air3ArgELm2ENS_10FastMallocEE14allocateBufferILNS_13FailureActionE0EEEbm
- __ZN3WTF20VectorTypeOperationsINSt3__14pairIN3JSC10CodeOriginENS1_10unique_ptrINS3_21SetPrivateBrandStatusENS1_14default_deleteIS6_EEEEEEE4moveEPSA_SC_SC_
- __ZN3WTF6Detail15CallableWrapperIZN3JSC22JSFinalizationRegistry23finalizeUnconditionallyERNS2_2VMENS2_15CollectionScopeEE3$_2vJRNS2_17DeferredWorkTimer6TicketEEE4callESA_
- __ZN3WTF6Detail15CallableWrapperIZN3JSC22JSFinalizationRegistry23finalizeUnconditionallyERNS2_2VMENS2_15CollectionScopeEE3$_2vJRNS2_17DeferredWorkTimer6TicketEEED0Ev
- __ZN3WTF6Detail15CallableWrapperIZN3JSC22JSFinalizationRegistry23finalizeUnconditionallyERNS2_2VMENS2_15CollectionScopeEE3$_2vJRNS2_17DeferredWorkTimer6TicketEEED1Ev
- __ZN3WTF6VectorINS_17CompletionHandlerIFvvEEELm0ENS_15CrashOnOverflowELm16ENS_10FastMallocEE15reserveCapacityILNS_13FailureActionE0EEEbm
- __ZN3WTF6VectorINS_17CompletionHandlerIFvvEEELm0ENS_15CrashOnOverflowELm16ENS_10FastMallocEED2Ev
- __ZN3WTF6VectorINS_3RefI14OpaqueJSStringNS_12RawPtrTraitsIS2_EENS_21DefaultRefDerefTraitsIS2_EEEELm0ENS_15CrashOnOverflowELm16ENS_10FastMallocEED2Ev
- __ZN3WTF7HashMapIPN3JSC6JSCellENS_6VectorINS1_12WriteBarrierINS1_7UnknownENS_14RawValueTraitsIS6_EEEELm0ENS_15CrashOnOverflowELm16ENS_10FastMallocEEENS_11DefaultHashIS3_EENS_10HashTraitsIS3_EENSF_ISC_EENS_15HashTableTraitsELNS_17ShouldValidateKeyE0ESB_E3addISC_EENS_18HashTableAddResultINS_17HashTableIteratorINS_9HashTableIS3_NS_12KeyValuePairIS3_SC_EENS_24KeyValuePairKeyExtractorISQ_EESE_NSK_18KeyValuePairTraitsESG_SB_EES3_SQ_SS_SE_ST_SG_EEEERKS3_OT_
- __ZN3WTF8LivenessIN3JSC2B33Air18TmpLivenessAdapterILNS2_4BankE0ELNS3_3Arg11TemperatureE0EEEE7Workset6removeEj
- __ZN3WTF8LivenessIN3JSC2B33Air18TmpLivenessAdapterILNS2_4BankE1ELNS3_3Arg11TemperatureE0EEEE7Workset6removeEj
- __ZN3WTF9HashTableINSt3__14pairINS_6RefPtrINS_29ThreadSafeWeakPtrControlBlockENS_12RawPtrTraitsIS4_EENS_43ThreadSafeWeakPtrControlBlockRefDerefTraitsEEEPKN3JSC4Wasm14InstanceAnchorEEESE_NS_17IdentityExtractorENS_11DefaultHashISE_EENS_10HashTraitsISE_EESJ_NS_10FastMallocEE20computeBestTableSizeEj
- __ZN3WTF9HashTableIPN3JSC15InlineCallFrameES3_NS_17IdentityExtractorENS_11DefaultHashIS3_EENS_18NullableHashTraitsIS3_EES8_NS_10FastMallocEEC2ERKSA_
- __ZN3WTF9HashTableIPN3JSC3DFG4NodeENS_12KeyValuePairIS4_NS_7HashSetIS4_NS_11DefaultHashIS4_EENS_10HashTraitsIS4_EENS_15HashTableTraitsELNS_17ShouldValidateKeyE0EEEEENS_24KeyValuePairKeyExtractorISE_EES8_NS_7HashMapIS4_SD_S8_SA_NS9_ISD_EESB_LSC_0ENS_10FastMallocEE18KeyValuePairTraitsESA_SJ_E4findINS_22IdentityHashTranslatorISL_S8_EELSC_0ES4_EENS_17HashTableIteratorISM_S4_SE_SG_S8_SL_SA_EERKT1_
- __ZN3WTF9HashTableIPvNS_12KeyValuePairIS1_PFvS1_EEENS_24KeyValuePairKeyExtractorIS5_EENS_11DefaultHashIS1_EENS_7HashMapIS1_S4_S9_NS_10HashTraitsIS1_EENSB_IS4_EENS_15HashTableTraitsELNS_17ShouldValidateKeyE1ENS_10FastMallocEE18KeyValuePairTraitsESC_SG_E6expandEPS5_
- __ZN3WTF9HashTableIjNS_12KeyValuePairIjNS_9RetainPtrI12NSDictionaryEEEENS_24KeyValuePairKeyExtractorIS5_EENS_11DefaultHashIjEENS_7HashMapIjS4_S9_NS_10HashTraitsIjEENSB_IS4_EENS_15HashTableTraitsELNS_17ShouldValidateKeyE0ENS_10FastMallocEE18KeyValuePairTraitsESC_SG_E6expandEPS5_
- __ZN3WTF9toCStringIJN3JSC4Wasm3RTTEEEENS_7CStringEDpRKT_
- __ZNK3WTF20ConcurrentPtrHashSet12containsImplEPv
- __ZNKSt3__114default_deleteIN3WTF19EmbeddedFixedVectorIN3JSC4Wasm11CalleeGroup16OptimizedCalleesENS1_10FastMallocEEEEclB9sqn220106EPS8_
- __ZTVN3WTF6Detail15CallableWrapperIZN3JSC22JSFinalizationRegistry23finalizeUnconditionallyERNS2_2VMENS2_15CollectionScopeEE3$_2vJRNS2_17DeferredWorkTimer6TicketEEEE
CStrings:
+ " max: "
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/bytecode/ExecutionCounter.cpp"
+ "Branch target would discard too many stack values: "
+ "Expected an exported WebAssembly function"
+ "Exported function has no callee group yet"
+ "LValue JSC::FTL::(anonymous namespace)::LowerDFGToB3::emitCodeBasedOnEndiannessBranch(LValue, const F1 &, const F2 &) [F1 = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:21665:45), F2 = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:21671:42)]"
+ "LValue JSC::FTL::(anonymous namespace)::LowerDFGToB3::emitCodeBasedOnEndiannessBranch(LValue, const F1 &, const F2 &) [F1 = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:21702:49), F2 = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:21705:46)]"
+ "LValue JSC::FTL::(anonymous namespace)::LowerDFGToB3::emitCodeBasedOnEndiannessBranch(LValue, const F1 &, const F2 &) [F1 = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:21725:45), F2 = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:21729:42)]"
+ "LValue JSC::FTL::(anonymous namespace)::LowerDFGToB3::emitCodeBasedOnEndiannessBranch(LValue, const F1 &, const F2 &) [F1 = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:21754:45), F2 = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:21758:42)]"
+ "LValue JSC::FTL::(anonymous namespace)::LowerDFGToB3::emitCodeBasedOnEndiannessBranch(LValue, const F1 &, const F2 &) [F1 = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:21783:45), F2 = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:21787:42)]"
+ "TriState JSC::Wasm::CalleeGroup::calleeIsReferenced(const AbstractLocker &, Wasm::Callee *) const"
+ "auto JSC::FTL::(anonymous namespace)::LowerDFGToB3::compileCallOrConstructVarargsSpread()::(anonymous class)::operator()(auto, Node *) const [self:auto = std::reference_wrapper<const WTF::RecursableLambda<(lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:14335:70)>>]"
+ "auto JSC::FTL::(anonymous namespace)::LowerDFGToB3::compileForwardVarargsWithSpread()::(anonymous class)::operator()(auto, Node *, LValue) const [self:auto = std::reference_wrapper<const WTF::RecursableLambda<(lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:15377:47)>>]"
+ "int32_t JSC::maximumExecutionCountsBetweenCheckpoints(CountingVariant, CodeBlock *)"
+ "void JSC::DFG::clobberize(Graph &, Node *, const ReadFunctor &, const WriteFunctor &, const DefFunctor &, const ClobberTopFunctor &) [ReadFunctor = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/dfg/DFGStoreBarrierInsertionPhase.cpp:522:33), WriteFunctor = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/dfg/DFGStoreBarrierInsertionPhase.cpp:537:34), DefFunctor = JSC::DFG::NoOpClobberize, ClobberTopFunctor = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/dfg/DFGClobberize.h:45:47)]"
+ "void JSC::FTL::(anonymous namespace)::LowerDFGToB3::compare(const IntFunctor &, const DoubleFunctor &, C_JITOperation_TT, C_JITOperation_B_GJssJss, S_JITOperation_GJJ) [IntFunctor = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:13753:13), DoubleFunctor = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:13756:13)]"
+ "void JSC::FTL::(anonymous namespace)::LowerDFGToB3::compare(const IntFunctor &, const DoubleFunctor &, C_JITOperation_TT, C_JITOperation_B_GJssJss, S_JITOperation_GJJ) [IntFunctor = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:13767:13), DoubleFunctor = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:13770:13)]"
+ "void JSC::FTL::(anonymous namespace)::LowerDFGToB3::compare(const IntFunctor &, const DoubleFunctor &, C_JITOperation_TT, C_JITOperation_B_GJssJss, S_JITOperation_GJJ) [IntFunctor = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:13781:13), DoubleFunctor = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:13784:13)]"
+ "void JSC::FTL::(anonymous namespace)::LowerDFGToB3::compare(const IntFunctor &, const DoubleFunctor &, C_JITOperation_TT, C_JITOperation_B_GJssJss, S_JITOperation_GJJ) [IntFunctor = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:13795:13), DoubleFunctor = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:13798:13)]"
+ "void JSC::shift(JSGlobalObject *, JSObject *, uint64_t, uint64_t, uint64_t, uint64_t) [shiftCountMode = JSC::JSArray::ShiftCountForShift]"
+ "wasmCalleeIDs"
- "LValue JSC::FTL::(anonymous namespace)::LowerDFGToB3::emitCodeBasedOnEndiannessBranch(LValue, const F1 &, const F2 &) [F1 = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:21659:45), F2 = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:21665:42)]"
- "LValue JSC::FTL::(anonymous namespace)::LowerDFGToB3::emitCodeBasedOnEndiannessBranch(LValue, const F1 &, const F2 &) [F1 = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:21696:49), F2 = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:21699:46)]"
- "LValue JSC::FTL::(anonymous namespace)::LowerDFGToB3::emitCodeBasedOnEndiannessBranch(LValue, const F1 &, const F2 &) [F1 = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:21719:45), F2 = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:21723:42)]"
- "LValue JSC::FTL::(anonymous namespace)::LowerDFGToB3::emitCodeBasedOnEndiannessBranch(LValue, const F1 &, const F2 &) [F1 = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:21748:45), F2 = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:21752:42)]"
- "LValue JSC::FTL::(anonymous namespace)::LowerDFGToB3::emitCodeBasedOnEndiannessBranch(LValue, const F1 &, const F2 &) [F1 = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:21777:45), F2 = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:21781:42)]"
- "ToType WTF::safeCast(FromType) [ToType = unsigned short, FromType = WTF::Checked<unsigned int>]"
- "auto JSC::FTL::(anonymous namespace)::LowerDFGToB3::compileCallOrConstructVarargsSpread()::(anonymous class)::operator()(auto, Node *) const [self:auto = std::reference_wrapper<const WTF::RecursableLambda<(lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:14329:70)>>]"
- "auto JSC::FTL::(anonymous namespace)::LowerDFGToB3::compileForwardVarargsWithSpread()::(anonymous class)::operator()(auto, Node *, LValue) const [self:auto = std::reference_wrapper<const WTF::RecursableLambda<(lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:15371:47)>>]"
- "void JSC::DFG::clobberize(Graph &, Node *, const ReadFunctor &, const WriteFunctor &, const DefFunctor &, const ClobberTopFunctor &) [ReadFunctor = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/dfg/DFGStoreBarrierInsertionPhase.cpp:514:33), WriteFunctor = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/dfg/DFGStoreBarrierInsertionPhase.cpp:529:34), DefFunctor = JSC::DFG::NoOpClobberize, ClobberTopFunctor = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/dfg/DFGClobberize.h:45:47)]"
- "void JSC::FTL::(anonymous namespace)::LowerDFGToB3::compare(const IntFunctor &, const DoubleFunctor &, C_JITOperation_TT, C_JITOperation_B_GJssJss, S_JITOperation_GJJ) [IntFunctor = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:13747:13), DoubleFunctor = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:13750:13)]"
- "void JSC::FTL::(anonymous namespace)::LowerDFGToB3::compare(const IntFunctor &, const DoubleFunctor &, C_JITOperation_TT, C_JITOperation_B_GJssJss, S_JITOperation_GJJ) [IntFunctor = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:13761:13), DoubleFunctor = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:13764:13)]"
- "void JSC::FTL::(anonymous namespace)::LowerDFGToB3::compare(const IntFunctor &, const DoubleFunctor &, C_JITOperation_TT, C_JITOperation_B_GJssJss, S_JITOperation_GJJ) [IntFunctor = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:13775:13), DoubleFunctor = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:13778:13)]"
- "void JSC::FTL::(anonymous namespace)::LowerDFGToB3::compare(const IntFunctor &, const DoubleFunctor &, C_JITOperation_TT, C_JITOperation_B_GJssJss, S_JITOperation_GJJ) [IntFunctor = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:13789:13), DoubleFunctor = (lambda at /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/JavaScriptCore/Source/JavaScriptCore/ftl/FTLLowerDFGToB3.cpp:13792:13)]"
```
