## com.apple.driver.AppleDisplayCrossbar

> `com.apple.driver.AppleDisplayCrossbar`

```diff

-417.1.4.0.0
+417.40.10.0.0
   __TEXT.__const: 0x2d0
-  __TEXT.__cstring: 0x52d6
-  __TEXT.__os_log: 0x6b69
-  __TEXT_EXEC.__text: 0x43a24
+  __TEXT.__cstring: 0x5318
+  __TEXT.__os_log: 0x6ca0
+  __TEXT_EXEC.__text: 0x445cc
   __TEXT_EXEC.__auth_stubs: 0x640
   __DATA.__data: 0xc4
   __DATA.__common: 0x538
   __DATA_CONST.__mod_init_func: 0x100
   __DATA_CONST.__mod_term_func: 0x100
-  __DATA_CONST.__const: 0x19d80
+  __DATA_CONST.__const: 0x19e50
   __DATA_CONST.__kalloc_type: 0x840
   __DATA_CONST.__kalloc_var: 0xa0
   __DATA_CONST.__auth_got: 0x320
   __DATA_CONST.__got: 0xf8
-  Functions: 2361
-  Symbols:   2556
-  CStrings:  877
+  Functions: 2348
+  Symbols:   2573
+  CStrings:  881
 
Symbols:
+ __ZN13AppleDPTXPort18setPclkdrvSelValueEb
+ __ZN13AppleDPTXPort26didChangeLinkConfigurationEv
+ __ZN13AppleDPTXPort27phyEnableTxaLdoLowPowerModeEv
+ __ZN13AppleDPTXPort27willChangeLinkConfigurationEv
+ __ZN18AppleT8122DPTXPort18setPclkdrvSelValueEb
+ __ZN18AppleT8122DPTXPort19pllSetPllaDcoCfgAnaEj
+ __ZN18AppleT8122DPTXPort23handleSetPllTopTunablesEv
+ __ZN18AppleT8122DPTXPort25handleSetPhyLanesTunablesEv
+ __ZN18AppleT8122DPTXPort25pllSetFreqinitDcoFineInitEj
+ __ZN18AppleT8122DPTXPort27handleSetPllCoreCfgTunablesEv
+ __ZN18AppleT8122DPTXPort27phyEnableTxaLdoLowPowerModeEv
+ __ZNK20AppleDisplayCrossbar20hasAvailablePeerUFPsEP25IODPSwitchAllocationStatePK10IODPTXPort
+ __ZNK25AppleT602XDisplayCrossbar20hasAvailablePeerUFPsEP25IODPSwitchAllocationStatePK10IODPTXPort
+ __ZNK25AppleT6050DisplayCrossbar20hasAvailablePeerUFPsEP25IODPSwitchAllocationStatePK10IODPTXPort
+ __ZThn144_N13AppleDPTXPort26didChangeLinkConfigurationEv
+ __ZThn144_N13AppleDPTXPort27willChangeLinkConfigurationEv
+ __ZZN13AppleDPTXPort26didChangeLinkConfigurationEvE11_os_log_fmt
+ __ZZN13AppleDPTXPort27willChangeLinkConfigurationEvE11_os_log_fmt
+ __ZZN18AppleT8122DPTXPort27handleSetPllCoreCfgTunablesEvE11_os_log_fmt
+ __ZZN18AppleT8122DPTXPort27handleSetPllCoreCfgTunablesEvE11_os_log_fmt_0
+ __ZZN18AppleT8122DPTXPort27handleSetPllCoreCfgTunablesEvE11_os_log_fmt_1
+ __ZZN18AppleT8122DPTXPort27handleSetPllCoreCfgTunablesEvE11_os_log_fmt_2
+ __ZZN18AppleT8122DPTXPort27handleSetPllCoreCfgTunablesEvE11_os_log_fmt_3
+ ___ZNK25AppleT602XDisplayCrossbar20hasAvailablePeerUFPsEP25IODPSwitchAllocationStatePK10IODPTXPort_block_invoke
+ ____ZNK25AppleT602XDisplayCrossbar20hasAvailablePeerUFPsEP25IODPSwitchAllocationStatePK10IODPTXPort_block_invoke
+ ____ZNK25AppleT6050DisplayCrossbar20hasAvailablePeerUFPsEP25IODPSwitchAllocationStatePK10IODPTXPort_block_invoke
- __ZN10IODPTXPort26didChangeLinkConfigurationEv
- __ZN10IODPTXPort27willChangeLinkConfigurationEv
- __ZN18AppleT8132DPTXPort10phyPowerUpEv
- __ZNK20AppleDisplayCrossbar20hasAvailablePeerUFPsEPK10IODPTXPort
- __ZNK25AppleT602XDisplayCrossbar20hasAvailablePeerUFPsEPK10IODPTXPort
- __ZNK25AppleT6050DisplayCrossbar20hasAvailablePeerUFPsEPK10IODPTXPort
- __ZThn144_N10IODPTXPort26didChangeLinkConfigurationEv
- __ZThn144_N10IODPTXPort27willChangeLinkConfigurationEv
- ____ZNK25AppleT602XDisplayCrossbar20hasAvailablePeerUFPsEPK10IODPTXPort_block_invoke
CStrings:
+ "IOAV[%d] %s<0x%llx>::%s: ret=0x%08x"
+ "didChangeLinkConfiguration"
+ "ret=0x%08x"
+ "willChangeLinkConfiguration"
```
