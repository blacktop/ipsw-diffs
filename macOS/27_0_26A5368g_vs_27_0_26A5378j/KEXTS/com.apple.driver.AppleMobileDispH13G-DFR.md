## com.apple.driver.AppleMobileDispH13G-DFR

> `com.apple.driver.AppleMobileDispH13G-DFR`

```diff

   __TEXT.__const: 0x5318
   __TEXT.__cstring: 0xf529
-  __TEXT_EXEC.__text: 0x5bc44
+  __TEXT_EXEC.__text: 0x5bc48
   __TEXT_EXEC.__auth_stubs: 0xe80
   __DATA.__data: 0x1a38
   __DATA.__common: 0x4af0
   __DATA.__bss: 0x9340
   __DATA_CONST.__mod_init_func: 0x148
   __DATA_CONST.__mod_term_func: 0x140
-  __DATA_CONST.__const: 0x10f10
+  __DATA_CONST.__const: 0x10ee8
   __DATA_CONST.__kalloc_type: 0x1480
   __DATA_CONST.__kalloc_var: 0x190
   __DATA_CONST.__auth_got: 0x740
   __DATA_CONST.__got: 0x130
   __DATA_CONST.__auth_ptr: 0x8
-  Functions: 2983
-  Symbols:   3976
+  Functions: 2982
+  Symbols:   3975
   CStrings:  1763
 
Sections:
~ __TEXT.__cstring : content changed
~ __DATA.__data : content changed
~ __DATA_CONST.__mod_init_func : content changed
~ __DATA_CONST.__mod_term_func : content changed
~ __DATA_CONST.__kalloc_type : content changed
~ __DATA_CONST.__kalloc_var : content changed
~ __DATA_CONST.__auth_got : content changed
~ __DATA_CONST.__got : content changed
~ __DATA_CONST.__auth_ptr : content changed
Symbols:
+ __ZN19IOMobileFramebuffer16get_dcp_rolenameEPcj
+ __ZZN12ADPParamFIFO4freeEvE19kalloc_type_view_63
+ __ZZN12ADPParamFIFO4initEP20IOMFBParamFIFODrivermmP11IOMemoryMapE19kalloc_type_view_50
+ __ZZN29IOMobileFramebufferVeryLegacy22record_swap_info_gatedEP18IOMFBSwapIORequest24IOMFBSwapCompletionStateE21kalloc_type_view_6183
+ __ZZN5IOMFB11InputFilterIbEdlEPvmE19kalloc_type_view_85
+ __ZZN5IOMFB11InputFilterIbEnwEmE19kalloc_type_view_85
+ __ZZN5IOMFB11InputFilterIiEdlEPvmE19kalloc_type_view_85
+ __ZZN5IOMFB11InputFilterIiEnwEmE19kalloc_type_view_85
+ __ZZN5IOMFB11TraceBuffer10save_traceEPvE20kalloc_type_view_148
+ __ZZN5IOMFB11TraceBuffer12stop_tracingEvE19kalloc_type_view_47
+ __ZZN5IOMFB11TraceBuffer12stop_tracingEvE19kalloc_type_view_82
+ __ZZN5IOMFB15FeatureSubtitle11instantiateEP9AppleCLCDE19kalloc_type_view_16
+ __ZZN5IOMFB15FeatureSubtitle11instantiateEP9AppleCLCDE19kalloc_type_view_20
+ __ZZN9AppleCLCD18createBlockDriversEvE20kalloc_type_view_636
+ __ZZN9AppleCLCD18createBlockDriversEvE20kalloc_type_view_639
+ __ZZN9AppleCLCD19stop_hardware_gatedEvE20kalloc_type_view_118
- __ZN29IOMobileFramebufferVeryLegacy26genlock_error_notify_gatedEy
- __ZN29IOMobileFramebufferVeryLegacy26set_external_genlock_gatedEbj
- __ZZN12ADPParamFIFO4freeEvE19kalloc_type_view_62
- __ZZN12ADPParamFIFO4initEP20IOMFBParamFIFODrivermmP11IOMemoryMapE19kalloc_type_view_49
- __ZZN29IOMobileFramebufferVeryLegacy22record_swap_info_gatedEP18IOMFBSwapIORequest24IOMFBSwapCompletionStateE21kalloc_type_view_6182
- __ZZN5IOMFB11InputFilterIbEdlEPvmE19kalloc_type_view_84
- __ZZN5IOMFB11InputFilterIbEnwEmE19kalloc_type_view_84
- __ZZN5IOMFB11InputFilterIiEdlEPvmE19kalloc_type_view_84
- __ZZN5IOMFB11InputFilterIiEnwEmE19kalloc_type_view_84
- __ZZN5IOMFB11TraceBuffer10save_traceEPvE20kalloc_type_view_147
- __ZZN5IOMFB11TraceBuffer12stop_tracingEvE19kalloc_type_view_46
- __ZZN5IOMFB11TraceBuffer12stop_tracingEvE19kalloc_type_view_81
- __ZZN5IOMFB15FeatureSubtitle11instantiateEP9AppleCLCDE19kalloc_type_view_15
- __ZZN5IOMFB15FeatureSubtitle11instantiateEP9AppleCLCDE19kalloc_type_view_19
- __ZZN9AppleCLCD18createBlockDriversEvE20kalloc_type_view_635
- __ZZN9AppleCLCD18createBlockDriversEvE20kalloc_type_view_638
- __ZZN9AppleCLCD19stop_hardware_gatedEvE20kalloc_type_view_117
Functions:
+ __ZN19IOMobileFramebuffer16get_dcp_rolenameEPcj
- __ZN29IOMobileFramebufferVeryLegacy40set_temperature_compensation_state_gatedEb
+ __ZN19IOMobileFramebuffer16get_dcp_rolenameEPcj
- __ZN29IOMobileFramebufferVeryLegacy40set_temperature_compensation_state_gatedEb
~ __ZN16AppleDisplayPipe30scaleDisplayToIdleBuffer_gatedEv : 556 -> 548
+ __ZN19IOMobileFramebuffer16get_dcp_rolenameEPcj
- __ZN29IOMobileFramebufferVeryLegacy40set_temperature_compensation_state_gatedEb
~ __ZN18AppleH7DisplayPipe20detectFBFormat_gatedEv : 304 -> 312
+ __ZN19IOMobileFramebuffer16get_dcp_rolenameEPcj
- __ZN29IOMobileFramebufferVeryLegacy40set_temperature_compensation_state_gatedEb
~ __Z15readADPTunablesP16AppleDisplayPipe : 2304 -> 2308
~ __ZN5IOMFB16TableCompensator9GainTable15read_dbsr_tableEPKjjb : 192 -> 208
~ __ZN5IOMFB16TableCompensator15BilerpGainTable9set_tableEjPK18IOMFBLUTTableStatei : 252 -> 248
~ __ZN5IOMFB16TableCompensator9GainTable13new_from_dataEPjmPKNS0_10VersionMapE : 280 -> 264
~ __Z18iomem_core_excludePVvj : 136 -> 140
- __ZN29IOMobileFramebufferVeryLegacy40set_temperature_compensation_state_gatedEb
~ __ZN9MIEDriver15updateBacklightEPjPb : 556 -> 564
~ __ZN9MIEDriver9printRegsEv : 304 -> 296
~ __ZN28IOMFBColorManagerDriver_Impl7Primary4initEP9IOService : 488 -> 484
~ __ZN14IOMFBParamFIFO19setCompletionActionEbPFiP8OSObjectPviES1_S2_ : 300 -> 308
~ __ZN14IOMFBParamFIFO24execute_callbacks_lockedEi : 160 -> 144
~ __ZN5IOMFB21UniformityCompensator3setEPKNS0_5StateE : 1032 -> 1052
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VcDkdk/Sources/IOMobileFramebuffer/Standalone/Src/Algorithm/FxMatrix.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qMwwMh/Sources/IOMobileFramebuffer/Standalone/Src/Algorithm/FxMatrix.cpp"

```
