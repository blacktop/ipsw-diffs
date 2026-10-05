## ANECompiler

> `/System/Library/PrivateFrameworks/ANECompiler.framework/ANECompiler`

```diff

-10.202.4.0.0
-  __TEXT.__text: 0x1c4cec0
+10.203.3.0.0
+  __TEXT.__text: 0x1c4f180
   __TEXT.__init_offsets: 0x8
-  __TEXT.__const: 0xc6ebe
-  __TEXT.__cstring: 0x122f67
-  __TEXT.__oslogstring: 0x20dda
-  __TEXT.__gcc_except_tab: 0xd7314
-  __TEXT.__unwind_info: 0x82218
+  __TEXT.__const: 0xc710e
+  __TEXT.__cstring: 0x123517
+  __TEXT.__oslogstring: 0x210b5
+  __TEXT.__gcc_except_tab: 0xd7524
+  __TEXT.__unwind_info: 0x822d0
   __TEXT.__eh_frame: 0x2be4
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x5608
   __DATA_CONST.__weak_got: 0x18
   __DATA_CONST.__got: 0x1f0
-  __AUTH_CONST.__const: 0xb2b00
+  __AUTH_CONST.__const: 0xb2c00
   __AUTH_CONST.__cfstring: 0xa040
   __AUTH_CONST.__weak_auth_got: 0x50
   __AUTH_CONST.__auth_got: 0x1250

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libncurses.5.4.dylib
-  Functions: 122967
-  Symbols:   160760
-  CStrings:  27501
+  Functions: 122995
+  Symbols:   160796
+  CStrings:  27540
 
Symbols:
+ __ZN14Layer2TDMapper11SourceLayerC2IRNSt3__16vectorIPK12ZinIrOpLayerNS2_9allocatorIS6_EEEEEEOT_
+ __ZN6MirOpt29RemoveStaleCopiesBeforeConcatEP21ZinIrControlFlowGraphRK15ZinIrParametersb
+ __ZN6MirOpt29SinkNoOpTransposesBelowConcatEP21ZinIrControlFlowGraphRK15ZinIrParametersR16ZinTransformInfob
+ __ZN6MirOptL10PinsLayoutEPK11ZinIrTensor
+ __ZNK22ZinMirLatencyLegalizer38IsChainPreservingChannelSplitCandidateEP11ZinANELayerm
+ __ZNK23ZinIrCompilerParameters24IsProcedureInExclaveListERKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE
+ __ZNKSt3__110__function6__funcIZN6MirOpt29RemoveStaleCopiesBeforeConcatEP21ZinIrControlFlowGraphRK15ZinIrParametersbE3$_0F11ZinIrStatusP17ZinIrOpLayerGraphRK11RawOrSharedI12ZinIrOpLayerEEE11target_typeEv
+ __ZNKSt3__110__function6__funcIZN6MirOpt29RemoveStaleCopiesBeforeConcatEP21ZinIrControlFlowGraphRK15ZinIrParametersbE3$_0F11ZinIrStatusP17ZinIrOpLayerGraphRK11RawOrSharedI12ZinIrOpLayerEEE6targetERKSt9type_info
+ __ZNKSt3__110__function6__funcIZN6MirOpt29RemoveStaleCopiesBeforeConcatEP21ZinIrControlFlowGraphRK15ZinIrParametersbE3$_0F11ZinIrStatusP17ZinIrOpLayerGraphRK11RawOrSharedI12ZinIrOpLayerEEE7__cloneEPNS0_6__baseISH_EE
+ __ZNKSt3__110__function6__funcIZN6MirOpt29RemoveStaleCopiesBeforeConcatEP21ZinIrControlFlowGraphRK15ZinIrParametersbE3$_0F11ZinIrStatusP17ZinIrOpLayerGraphRK11RawOrSharedI12ZinIrOpLayerEEE7__cloneEv
+ __ZNKSt3__110__function6__funcIZN6MirOpt29SinkNoOpTransposesBelowConcatEP21ZinIrControlFlowGraphRK15ZinIrParametersR16ZinTransformInfobE3$_0F11ZinIrStatusP17ZinIrOpLayerGraphRK11RawOrSharedI12ZinIrOpLayerEEE11target_typeEv
+ __ZNKSt3__110__function6__funcIZN6MirOpt29SinkNoOpTransposesBelowConcatEP21ZinIrControlFlowGraphRK15ZinIrParametersR16ZinTransformInfobE3$_0F11ZinIrStatusP17ZinIrOpLayerGraphRK11RawOrSharedI12ZinIrOpLayerEEE6targetERKSt9type_info
+ __ZNKSt3__110__function6__funcIZN6MirOpt29SinkNoOpTransposesBelowConcatEP21ZinIrControlFlowGraphRK15ZinIrParametersR16ZinTransformInfobE3$_0F11ZinIrStatusP17ZinIrOpLayerGraphRK11RawOrSharedI12ZinIrOpLayerEEE7__cloneEPNS0_6__baseISJ_EE
+ __ZNKSt3__110__function6__funcIZN6MirOpt29SinkNoOpTransposesBelowConcatEP21ZinIrControlFlowGraphRK15ZinIrParametersR16ZinTransformInfobE3$_0F11ZinIrStatusP17ZinIrOpLayerGraphRK11RawOrSharedI12ZinIrOpLayerEEE7__cloneEv
+ __ZNSt3__110__function6__funcIZN6MirOpt29RemoveStaleCopiesBeforeConcatEP21ZinIrControlFlowGraphRK15ZinIrParametersbE3$_0F11ZinIrStatusP17ZinIrOpLayerGraphRK11RawOrSharedI12ZinIrOpLayerEEE18destroy_deallocateEv
+ __ZNSt3__110__function6__funcIZN6MirOpt29RemoveStaleCopiesBeforeConcatEP21ZinIrControlFlowGraphRK15ZinIrParametersbE3$_0F11ZinIrStatusP17ZinIrOpLayerGraphRK11RawOrSharedI12ZinIrOpLayerEEE7destroyEv
+ __ZNSt3__110__function6__funcIZN6MirOpt29RemoveStaleCopiesBeforeConcatEP21ZinIrControlFlowGraphRK15ZinIrParametersbE3$_0F11ZinIrStatusP17ZinIrOpLayerGraphRK11RawOrSharedI12ZinIrOpLayerEEED0Ev
+ __ZNSt3__110__function6__funcIZN6MirOpt29RemoveStaleCopiesBeforeConcatEP21ZinIrControlFlowGraphRK15ZinIrParametersbE3$_0F11ZinIrStatusP17ZinIrOpLayerGraphRK11RawOrSharedI12ZinIrOpLayerEEED1Ev
+ __ZNSt3__110__function6__funcIZN6MirOpt29RemoveStaleCopiesBeforeConcatEP21ZinIrControlFlowGraphRK15ZinIrParametersbE3$_0F11ZinIrStatusP17ZinIrOpLayerGraphRK11RawOrSharedI12ZinIrOpLayerEEEclEOSB_SG_
+ __ZNSt3__110__function6__funcIZN6MirOpt29SinkNoOpTransposesBelowConcatEP21ZinIrControlFlowGraphRK15ZinIrParametersR16ZinTransformInfobE3$_0F11ZinIrStatusP17ZinIrOpLayerGraphRK11RawOrSharedI12ZinIrOpLayerEEE18destroy_deallocateEv
+ __ZNSt3__110__function6__funcIZN6MirOpt29SinkNoOpTransposesBelowConcatEP21ZinIrControlFlowGraphRK15ZinIrParametersR16ZinTransformInfobE3$_0F11ZinIrStatusP17ZinIrOpLayerGraphRK11RawOrSharedI12ZinIrOpLayerEEE7destroyEv
+ __ZNSt3__110__function6__funcIZN6MirOpt29SinkNoOpTransposesBelowConcatEP21ZinIrControlFlowGraphRK15ZinIrParametersR16ZinTransformInfobE3$_0F11ZinIrStatusP17ZinIrOpLayerGraphRK11RawOrSharedI12ZinIrOpLayerEEED0Ev
+ __ZNSt3__110__function6__funcIZN6MirOpt29SinkNoOpTransposesBelowConcatEP21ZinIrControlFlowGraphRK15ZinIrParametersR16ZinTransformInfobE3$_0F11ZinIrStatusP17ZinIrOpLayerGraphRK11RawOrSharedI12ZinIrOpLayerEEED1Ev
+ __ZNSt3__110__function6__funcIZN6MirOpt29SinkNoOpTransposesBelowConcatEP21ZinIrControlFlowGraphRK15ZinIrParametersR16ZinTransformInfobE3$_0F11ZinIrStatusP17ZinIrOpLayerGraphRK11RawOrSharedI12ZinIrOpLayerEEEclEOSD_SI_
+ __ZNSt3__16vectorIPK12ZinIrOpLayerNS_9allocatorIS3_EEE18__insert_with_sizeB9fqe220106INS_17_ClassicAlgPolicyENS_11__wrap_iterIPPS1_EESC_EENS9_IPS3_EENS9_IPKS3_EET0_T1_l
+ __ZNSt3__16vectorIPK12ZinIrOpLayerNS_9allocatorIS3_EEE7reserveEm
+ __ZTINSt3__110__function6__funcIZN6MirOpt29RemoveStaleCopiesBeforeConcatEP21ZinIrControlFlowGraphRK15ZinIrParametersbE3$_0F11ZinIrStatusP17ZinIrOpLayerGraphRK11RawOrSharedI12ZinIrOpLayerEEEE
+ __ZTINSt3__110__function6__funcIZN6MirOpt29SinkNoOpTransposesBelowConcatEP21ZinIrControlFlowGraphRK15ZinIrParametersR16ZinTransformInfobE3$_0F11ZinIrStatusP17ZinIrOpLayerGraphRK11RawOrSharedI12ZinIrOpLayerEEEE
+ __ZTIZN6MirOpt29RemoveStaleCopiesBeforeConcatEP21ZinIrControlFlowGraphRK15ZinIrParametersbE3$_0
+ __ZTIZN6MirOpt29SinkNoOpTransposesBelowConcatEP21ZinIrControlFlowGraphRK15ZinIrParametersR16ZinTransformInfobE3$_0
+ __ZTSNSt3__110__function6__funcIZN6MirOpt29RemoveStaleCopiesBeforeConcatEP21ZinIrControlFlowGraphRK15ZinIrParametersbE3$_0F11ZinIrStatusP17ZinIrOpLayerGraphRK11RawOrSharedI12ZinIrOpLayerEEEE
+ __ZTSNSt3__110__function6__funcIZN6MirOpt29SinkNoOpTransposesBelowConcatEP21ZinIrControlFlowGraphRK15ZinIrParametersR16ZinTransformInfobE3$_0F11ZinIrStatusP17ZinIrOpLayerGraphRK11RawOrSharedI12ZinIrOpLayerEEEE
+ __ZTSZN6MirOpt29RemoveStaleCopiesBeforeConcatEP21ZinIrControlFlowGraphRK15ZinIrParametersbE3$_0
+ __ZTSZN6MirOpt29SinkNoOpTransposesBelowConcatEP21ZinIrControlFlowGraphRK15ZinIrParametersR16ZinTransformInfobE3$_0
+ __ZTVNSt3__110__function6__funcIZN6MirOpt29RemoveStaleCopiesBeforeConcatEP21ZinIrControlFlowGraphRK15ZinIrParametersbE3$_0F11ZinIrStatusP17ZinIrOpLayerGraphRK11RawOrSharedI12ZinIrOpLayerEEEE
+ __ZTVNSt3__110__function6__funcIZN6MirOpt29SinkNoOpTransposesBelowConcatEP21ZinIrControlFlowGraphRK15ZinIrParametersR16ZinTransformInfobE3$_0F11ZinIrStatusP17ZinIrOpLayerGraphRK11RawOrSharedI12ZinIrOpLayerEEEE
CStrings:
+ "ANEC Internal Error: failed to lower layers created by the no-op transpose sink"
+ "ANEC Internal Error: failed to move mir info off a stale concat copy"
+ "ANEC Internal Error: failed to remove a stale concat copy"
+ "ANEC Internal Error: failed to sink no-op transposes below concat"
+ "Exclave context switch SW workaround does not support bonded mode yet."
+ "Latency Splitting %s together with its consumer %s into %zu parts to preserve chaining."
+ "Latency Splitting %s: chain-preserving channel split with consumer %s into %zu parts failed, falling back to producer-only channel split."
+ "MIR Prepare Layers: Remove stale copies before concat failed!\n"
+ "MIR Prepare Layers: Sink no-op transposes below concat failed!\n"
+ "MX-tiled format not supported in SplitNEConvLayer split-offset alignment"
+ "Requires extended macho format (--use-extended-macho-format). Cannot compile with --use-extended-macho-format=false for this target."
+ "Should not split a grouped conv layer by input channel"
+ "Should not split a quantized conv layer by input channel"
+ "UpdateDTIDs: ANE index out of range"
+ "UpdateDTIDs: producer TID not found in old->new TID map (producer was not remapped before its consumer)."
+ "[MirOpt::RemoveStaleCopiesBeforeConcat] kept %s: %s"
+ "[MirOpt::RemoveStaleCopiesBeforeConcat] removed %s feeding %s"
+ "[MirOpt::SinkNoOpTransposesBelowConcat] sank %zu no-op transposes below %s; concat axis %d -> %d"
+ "[MirOpt::SinkNoOpTransposesBelowConcat] skipped %s: %s"
+ "after_remove_stale_copies_before_concat"
+ "after_sink_noop_transposes_below_concat"
+ "concat tensor carries an isolation axis"
+ "concat tensor pins custom strides or interleave"
+ "copy is not fed by a no-op transpose: "
+ "copy is not single-in single-out"
+ "copy tensor pins custom strides or interleave"
+ "fewer than 2 inputs"
+ "input is not a copy: "
+ "inputs do not share one dimension map"
+ "permutation leaves the concat axis unchanged"
+ "producer has other consumers"
+ "producer is a NoOp, copy is still required"
+ "producer pins L2 but the concat family does not fit in L2"
+ "producer tensor already has a parent"
+ "producer tensor pins custom strides or interleave"
+ "sink_noop_tr"
+ "transpose is not a single 2-way swap"
+ "transpose is not single-in single-out"
+ "transpose tensor pins custom strides or interleave"
```
