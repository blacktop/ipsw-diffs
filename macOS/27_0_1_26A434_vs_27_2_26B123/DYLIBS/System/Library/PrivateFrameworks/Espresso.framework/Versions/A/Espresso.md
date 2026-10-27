## Espresso

> `/System/Library/PrivateFrameworks/Espresso.framework/Versions/A/Espresso`

```diff

-3600.56.2.0.0
-  __TEXT.__text: 0xc7cd3c
+3605.3.2.0.0
+  __TEXT.__text: 0xc7d184
   __TEXT.__objc_methlist: 0x322c
   __TEXT.__const: 0x5db1a
-  __TEXT.__cstring: 0x4ef52
-  __TEXT.__gcc_except_tab: 0xcd59c
-  __TEXT.__oslogstring: 0x89dd
-  __TEXT.__unwind_info: 0x2b858
+  __TEXT.__cstring: 0x4f021
+  __TEXT.__gcc_except_tab: 0xcd650
+  __TEXT.__oslogstring: 0x8a00
+  __TEXT.__unwind_info: 0x2b868
   __TEXT.__eh_frame: 0x52c
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_arraydata: 0x148
   __DATA_CONST.__got: 0xa70
   __AUTH_CONST.__const: 0x9d618
-  __AUTH_CONST.__cfstring: 0x9bc0
+  __AUTH_CONST.__cfstring: 0x9be0
   __AUTH_CONST.__objc_const: 0x8b90
   __AUTH_CONST.__weak_auth_got: 0xc0
   __AUTH_CONST.__objc_intobj: 0x318

   __AUTH.__thread_bss: 0x400
   __DATA.__objc_ivar: 0x5b8
   __DATA.__data: 0x4c8
-  __DATA.__bss: 0x65a0
+  __DATA.__bss: 0x65b0
   __DATA.__common: 0x2c
   __DATA_DIRTY.__objc_data: 0x190
   __DATA_DIRTY.__data: 0x90

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 34294
-  Symbols:   54937
-  CStrings:  10235
+  Symbols:   54939
+  CStrings:  10240
 
Symbols:
+ GCC_except_table3733
+ GCC_except_table6802
Functions:
~ sub_1a04280c8 -> sub_1984280c8 : 2848 -> 3592
~ __ZN13EspressoLight13espresso_plan11add_networkEPKc23espresso_storage_type_tNSt3__110shared_ptrIN8Espresso3netEEE : 4720 -> 4864
~ __ZL22adjust_espresso_engineR17espresso_engine_tRi : 268 -> 480
~ __ZN8Espresso23report_benchmark_resultENS_16benchmark_resultERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_S9_S9_S9_S9_ : 4064 -> 4068
~ __ZN8Espresso8hardware17supports_platformENS_8platformE : 300 -> 496
~ __ZN8Espresso14MPSGraphEngine8compiler17__forward_segmentERKNSt3__110shared_ptrINS_14abstract_batchEEEiRKNS_26net_compiler_segment_based9segment_tE : 2480 -> 2656
~ __ZN8Espresso3AOT26ReplacePixelBufferByTensorERKN3MIL9IRProgramERKNSt3__112basic_stringIcNS5_11char_traitsIcEENS5_9allocatorIcEEEE : 8920 -> 8856
~ __ZN8Espresso3AOT16UpdateFunctionIOERN3MIL7Builder15FunctionBuilderERKNSt3__113unordered_mapINS5_12basic_stringIcNS5_11char_traitsIcEENS5_9allocatorIcEEEEPKNS1_11IRValueTypeENS5_4hashISC_EENS5_8equal_toISC_EENSA_INS5_4pairIKSC_SF_EEEEEERKNS5_6vectorISF_NSA_ISF_EEEE : 12376 -> 12108
~ __ZN12_GLOBAL__N_131UpdateFunctionInputTensorBufferERN3MIL7Builder15FunctionBuilderERN8Espresso13MILTranslator13NameGeneratorERKNSt3__112basic_stringIcNS8_11char_traitsIcEENS8_9allocatorIcEEEEPKNS0_23IRTensorBufferValueTypeE : 4824 -> 4772
~ __ZN12_GLOBAL__N_132UpdateFunctionOutputTensorBufferERN3MIL7Builder15FunctionBuilderERN8Espresso13MILTranslator13NameGeneratorEmRKNSt3__112basic_stringIcNS8_11char_traitsIcEENS8_9allocatorIcEEEEPKNS0_23IRTensorBufferValueTypeE : 4272 -> 4224
~ __ZN8Espresso3AOT6DTrees10convAneFfmERKNS1_16CostModelFeatureE : 104 -> 132
~ __ZN8Espresso3AOT6DTrees10convAneFflERKNS1_16CostModelFeatureE : 104 -> 132
~ __ZN8Espresso13MILTranslator18EIRLayerTranslator15CompileInternalEmmRNSt3__13mapINS2_12basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEPKN3MIL11IRValueTypeENS2_4lessIS9_EENS7_INS2_4pairIKS9_SD_EEEEEEONS2_6vectorIS9_NS7_IS9_EEEE : 18096 -> 18092
CStrings:
+ "3605.3.2"
+ "MPSGraph tensor shape is missing or has unexpected rank (expected "
+ "VM gate: passing through engine=%d"
+ "[MPSGraphEngine] null MPSNDArray for input blob: "
+ "[MPSGraphEngine] null MPSNDArray for output blob: "
+ "espresso.enable_ane_runtime_in_vm"
- "3600.56.2"
```
