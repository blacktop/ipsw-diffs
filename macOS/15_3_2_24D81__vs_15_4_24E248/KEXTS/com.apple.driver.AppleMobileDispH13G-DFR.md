## com.apple.driver.AppleMobileDispH13G-DFR

> `com.apple.driver.AppleMobileDispH13G-DFR`

```diff

-398.4.0.0.0
-  __TEXT.__const: 0x4ac8
-  __TEXT.__cstring: 0xd3a1
+399.26.7.0.0
+  __TEXT.__const: 0x4a50
+  __TEXT.__cstring: 0xd33f
   __TEXT.__ustring: 0x12
-  __TEXT_EXEC.__text: 0x505bc
+  __TEXT_EXEC.__text: 0x522cc
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x1a00
   __DATA.__common: 0x750

   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x148
   __DATA_CONST.__mod_term_func: 0x140
-  __DATA_CONST.__const: 0xf5e8
+  __DATA_CONST.__const: 0xf608
   __DATA_CONST.__kalloc_type: 0x1600
   __DATA_CONST.__kalloc_var: 0x190
-  UUID: E6BB71C5-FAA0-34A1-A929-C6C32F7C6E2F
-  Functions: 2661
-  Symbols:   3705
-  CStrings:  1513
+  UUID: 0F84AF7C-E203-3F07-87EE-14621186D184
+  Functions: 2629
+  Symbols:   3724
+  CStrings:  1509
 
Symbols:
+ _ZN18AppleH7DisplayPipe11getBlendCRCEv.cold.1
+ _ZN18AppleH7DisplayPipe14read_clear_irqEv.cold.2
+ _ZN18AppleH7DisplayPipe14read_clear_irqEv.cold.3
+ _ZN18AppleH7DisplayPipe15interruptFilterEP8OSObjectP28IOFilterInterruptEventSource.cold.2
+ _ZN18AppleH7DisplayPipe15interruptFilterEP8OSObjectP28IOFilterInterruptEventSource.cold.3
+ _ZN18AppleH7DisplayPipe16disableInterruptEjb.cold.2
+ _ZN18AppleH7DisplayPipe16initDefaultStateEv.cold.1
+ _ZN18AppleH7DisplayPipe16initDefaultStateEv.cold.2
+ _ZN18AppleH7DisplayPipe16initDefaultStateEv.cold.3
+ _ZN18AppleH7DisplayPipe16initDefaultStateEv.cold.4
+ _ZN18AppleH7DisplayPipe18getFrontendVersionEv.cold.1
+ _ZN18AppleH7DisplayPipe19readTunableRegisterEj.cold.1
+ _ZN18AppleH7DisplayPipe19verify_spds_versionEv.cold.1
+ _ZN18AppleH7DisplayPipe20detectFBFormat_gatedEv.cold.1
+ _ZN18AppleH7DisplayPipe22interruptHandler_gatedEP8OSObjectPvS2_S2_S2_.cold.3
+ _ZN18AppleH7DisplayPipe22interruptHandler_gatedEP8OSObjectPvS2_S2_S2_.cold.4
+ _ZN18AppleH7DisplayPipe31is_passthrough_programmed_gatedEv.cold.1
+ _ZN18AppleH7DisplayPipe8clearVBIEv.cold.1
+ __ZN25IOMobileFramebufferLegacy16swap_get_currentEPj
+ __ZN25IOMobileFramebufferLegacy22dropAbortedSwaps_gatedEb
+ __ZN25IOMobileFramebufferLegacy27swap_cancel_all_get_currentEPj
- _ZN5IOMFB13ALSSHandlerV19send_dataEyj.cold.1
- _ZN5IOMFB17TempComp2DHandler3setEPK19IOMFB_2D_Temp_StatePKvj.cold.1
- _ZN5IOMFB21UniformityCompensator17reload_2duc_calibEPNS_12UPIOSvcProxyEjj.cold.1
- __ZN25IOMobileFramebufferLegacy18record_hw_err_intsEj
- __ZN25IOMobileFramebufferLegacy22dropAbortedSwaps_gatedEv
CStrings:
- "\"IOMFB %s: missing support for version %d\\n\" @%s:%d"
- "IOMFBTunableADPRegister::UNKNOWN"
- "linear"
- "tiled"

```
