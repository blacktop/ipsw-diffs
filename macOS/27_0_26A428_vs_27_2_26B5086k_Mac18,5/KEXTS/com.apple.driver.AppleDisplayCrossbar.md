## com.apple.driver.AppleDisplayCrossbar

> `com.apple.driver.AppleDisplayCrossbar`

```diff

-417.1.4.0.0
+417.40.5.0.2
   __TEXT.__const: 0x2d0
-  __TEXT.__cstring: 0x52d6
-  __TEXT.__os_log: 0x6b69
-  __TEXT_EXEC.__text: 0x3f678
+  __TEXT.__cstring: 0x532f
+  __TEXT.__os_log: 0x6c8a
+  __TEXT_EXEC.__text: 0x40bf4
   __TEXT_EXEC.__auth_stubs: 0x640
   __DATA.__data: 0xc4
   __DATA.__common: 0x538
   __DATA_CONST.__mod_init_func: 0x100
   __DATA_CONST.__mod_term_func: 0x100
-  __DATA_CONST.__const: 0x19d80
+  __DATA_CONST.__const: 0x19de0
   __DATA_CONST.__kalloc_type: 0x840
   __DATA_CONST.__kalloc_var: 0xa0
   __DATA_CONST.__auth_got: 0x320
   __DATA_CONST.__got: 0xf8
-  Functions: 2361
-  Symbols:   2556
-  CStrings:  877
+  Functions: 2371
+  Symbols:   2580
+  CStrings:  882
 
Symbols:
+ _ZN18AppleT8132DPTXPort10pllPowerUpEv
+ __ZN18AppleT8132DPTXPort10pllPowerUpEv
+ __ZN18AppleT8132DPTXPort11activatePhyEv
+ __ZN18AppleT8132DPTXPort11setLinkRateEh
+ __ZN18AppleT8132DPTXPort14handleActivateEv
+ __ZN18AppleT8132DPTXPort18phySetHalfLinkRateEb
+ __ZN18AppleT8132DPTXPort19pllSetPllaDcoCfgAnaEj
+ __ZN18AppleT8132DPTXPort21phySetActiveLaneCountEj
+ __ZN18AppleT8132DPTXPort21pllConfigureFrequencyEyPb
+ __ZN18AppleT8132DPTXPort23handleSetPllTopTunablesEv
+ __ZN18AppleT8132DPTXPort25handleSetPhyLanesTunablesEv
+ __ZN18AppleT8132DPTXPort26didChangeLinkConfigurationEv
+ __ZN18AppleT8132DPTXPort27willChangeLinkConfigurationEv
+ __ZNK20AppleDisplayCrossbar20hasAvailablePeerUFPsEP25IODPSwitchAllocationStatePK10IODPTXPort
+ __ZNK25AppleT602XDisplayCrossbar20hasAvailablePeerUFPsEP25IODPSwitchAllocationStatePK10IODPTXPort
+ __ZNK25AppleT6050DisplayCrossbar20hasAvailablePeerUFPsEP25IODPSwitchAllocationStatePK10IODPTXPort
+ __ZThn144_N18AppleT8132DPTXPort11setLinkRateEh
+ __ZThn144_N18AppleT8132DPTXPort26didChangeLinkConfigurationEv
+ __ZThn144_N18AppleT8132DPTXPort27willChangeLinkConfigurationEv
+ __ZZN18AppleT8132DPTXPort10pllPowerUpEvE11_os_log_fmt
+ __ZZN18AppleT8132DPTXPort10pllPowerUpEvE11_os_log_fmt_0
+ __ZZN18AppleT8132DPTXPort10pllPowerUpEvE11_os_log_fmt_1
+ __ZZN18AppleT8132DPTXPort11setLinkRateEhE11_os_log_fmt
+ __ZZN18AppleT8132DPTXPort26didChangeLinkConfigurationEvE11_os_log_fmt
+ __ZZN18AppleT8132DPTXPort27willChangeLinkConfigurationEvE11_os_log_fmt
+ ___ZNK25AppleT602XDisplayCrossbar20hasAvailablePeerUFPsEP25IODPSwitchAllocationStatePK10IODPTXPort_block_invoke
+ ____ZNK25AppleT602XDisplayCrossbar20hasAvailablePeerUFPsEP25IODPSwitchAllocationStatePK10IODPTXPort_block_invoke
+ ____ZNK25AppleT6050DisplayCrossbar20hasAvailablePeerUFPsEP25IODPSwitchAllocationStatePK10IODPTXPort_block_invoke
- __ZNK20AppleDisplayCrossbar20hasAvailablePeerUFPsEPK10IODPTXPort
- __ZNK25AppleT602XDisplayCrossbar20hasAvailablePeerUFPsEPK10IODPTXPort
- __ZNK25AppleT6050DisplayCrossbar20hasAvailablePeerUFPsEPK10IODPTXPort
- ____ZNK25AppleT602XDisplayCrossbar20hasAvailablePeerUFPsEPK10IODPTXPort_block_invoke
CStrings:
+ "AppleT8132DPTXPort.cpp"
+ "IOAV[%d] %s<0x%llx>::%s: ret=0x%08x"
+ "didChangeLinkConfiguration"
+ "ret=0x%08x"
+ "willChangeLinkConfiguration"
```
