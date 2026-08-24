## com.apple.driver.AppleDisplayCrossbar

> `com.apple.driver.AppleDisplayCrossbar`

```diff

-417.0.3.0.0
-  __TEXT.__const: 0x1a4
-  __TEXT.__cstring: 0x4cc7
-  __TEXT.__os_log: 0x689b
-  __TEXT_EXEC.__text: 0x3dd80
+417.1.3.0.0
+  __TEXT.__const: 0x1d0
+  __TEXT.__cstring: 0x4f5a
+  __TEXT.__os_log: 0x6a1c
+  __TEXT_EXEC.__text: 0x3f93c
   __TEXT_EXEC.__auth_stubs: 0x630
   __DATA.__data: 0xc4
-  __DATA.__common: 0x4e8
-  __DATA_CONST.__mod_init_func: 0xf0
-  __DATA_CONST.__mod_term_func: 0xf0
-  __DATA_CONST.__const: 0x17d78
-  __DATA_CONST.__kalloc_type: 0x7c0
+  __DATA.__common: 0x510
+  __DATA_CONST.__mod_init_func: 0xf8
+  __DATA_CONST.__mod_term_func: 0xf8
+  __DATA_CONST.__const: 0x18d38
+  __DATA_CONST.__kalloc_type: 0x800
   __DATA_CONST.__kalloc_var: 0xa0
   __DATA_CONST.__auth_got: 0x318
   __DATA_CONST.__got: 0xf8
-  Functions: 2158
-  Symbols:   2442
-  CStrings:  814
+  Functions: 2256
+  Symbols:   2491
+  CStrings:  843
 
Symbols:
+ _GLOBAL__sub_I_AppleT8132DPTXPort.cpp
+ _ZN18AppleT8132DPTXPort11handleStartEP9IOService
+ __ZL22AppleT8132DPTXPort_ktv
+ __ZN13AppleDPTXPort19pllSetPllaDcoCfgAnaEj
+ __ZN13AppleDPTXPort25pllSetFreqinitDcoFineInitEj
+ __ZN18AppleT8132DPTXPort10gMetaClassE
+ __ZN18AppleT8132DPTXPort10handleStopEP9IOService
+ __ZN18AppleT8132DPTXPort10superClassE
+ __ZN18AppleT8132DPTXPort11handleStartEP9IOService
+ __ZN18AppleT8132DPTXPort25pllSetFreqinitDcoFineInitEj
+ __ZN18AppleT8132DPTXPort26pllSetPllaClkoutVregBypassEb
+ __ZN18AppleT8132DPTXPort27handleSetPllCoreCfgTunablesEv
+ __ZN18AppleT8132DPTXPort9MetaClassC1Ev
+ __ZN18AppleT8132DPTXPort9MetaClassC2Ev
+ __ZN18AppleT8132DPTXPort9MetaClassD0Ev
+ __ZN18AppleT8132DPTXPort9MetaClassD1Ev
+ __ZN18AppleT8132DPTXPort9metaClassE
+ __ZN18AppleT8132DPTXPortC1EPK11OSMetaClass
+ __ZN18AppleT8132DPTXPortC1Ev
+ __ZN18AppleT8132DPTXPortC2EPK11OSMetaClass
+ __ZN18AppleT8132DPTXPortC2Ev
+ __ZN18AppleT8132DPTXPortD0Ev
+ __ZN18AppleT8132DPTXPortD1Ev
+ __ZN18AppleT8132DPTXPortD2Ev
+ __ZN18AppleT8132DPTXPortdlEPvm
+ __ZN18AppleT8132DPTXPortnwEm
+ __ZN29AppleDisplayConnectionManager13updatePeerUFPEP25IODPSwitchAllocationStateP22AppleDisplayConnectionP10IODPTXPortS5_
+ __ZNK13AppleDPTXPort18getPclkdrvSelValueEv
+ __ZNK13AppleDPTXPort20getSingleEndedClkoutEv
+ __ZNK18AppleT6050DPTXPort20getSingleEndedClkoutEv
+ __ZNK18AppleT8122DPTXPort12getFuseValueEP16AppleARMIODevicePKcPj
+ __ZNK18AppleT8132DPTXPort12getMetaClassEv
+ __ZNK18AppleT8132DPTXPort9MetaClass5allocEv
+ __ZTV18AppleT8132DPTXPort
+ __ZTVN18AppleT8132DPTXPort9MetaClassE
+ __ZThn136_N18AppleT8132DPTXPortD0Ev
+ __ZThn136_N18AppleT8132DPTXPortD1Ev
+ __ZThn144_N18AppleT8132DPTXPortD0Ev
+ __ZThn144_N18AppleT8132DPTXPortD1Ev
+ __ZThn152_N18AppleT8132DPTXPortD0Ev
+ __ZThn152_N18AppleT8132DPTXPortD1Ev
+ __ZThn160_N18AppleT8132DPTXPortD0Ev
+ __ZThn160_N18AppleT8132DPTXPortD1Ev
+ __ZZN18AppleT8132DPTXPort11handleStartEP9IOServiceE11_os_log_fmt
+ __ZZN18AppleT8132DPTXPort11handleStartEP9IOServiceE11_os_log_fmt_0
+ __ZZN18AppleT8132DPTXPort27handleSetPllCoreCfgTunablesEvE11_os_log_fmt
+ __ZZN18AppleT8132DPTXPort27handleSetPllCoreCfgTunablesEvE11_os_log_fmt_0
+ __ZZN18AppleT8132DPTXPort27handleSetPllCoreCfgTunablesEvE11_os_log_fmt_1
+ __ZZN18AppleT8132DPTXPort27handleSetPllCoreCfgTunablesEvE11_os_log_fmt_2
+ __ZZN18AppleT8132DPTXPort27handleSetPllCoreCfgTunablesEvE11_os_log_fmt_3
+ __ZZN18AppleT8132DPTXPort27handleSetPllCoreCfgTunablesEvE11_os_log_fmt_4
- __ZN13AppleDPTXPort18getPclkdrvSelValueEv
- ___ZN29AppleDisplayConnectionManager27setDisplayConnectionMappingEP7OSArrayb_block_invoke_3
CStrings:
+ "1211111212221212111112222211111111111122222222222222222222222222222222222222222222222222222222222222222211111112121221"
+ "AppleT8132DPTXPort"
+ "DCDADJ"
+ "DCDADJ = %x\n"
+ "DCOCFG"
+ "DCOCFG = %x RODCO_ENCAP_EFUSE = %x RODCO_BIASADJ_EFUSE = %x\n"
+ "DLFCFG"
+ "DLFCFG = %x\n"
+ "DTCCAL"
+ "DTCCAL = %x\n"
+ "DTCVREG"
+ "DTCVREG = %x\n"
+ "IOAV[%d] %s<0x%llx>::%s: DCDADJ = %x\n"
+ "IOAV[%d] %s<0x%llx>::%s: DCOCFG = %x RODCO_ENCAP_EFUSE = %x RODCO_BIASADJ_EFUSE = %x\n"
+ "IOAV[%d] %s<0x%llx>::%s: DLFCFG = %x\n"
+ "IOAV[%d] %s<0x%llx>::%s: DTCCAL = %x\n"
+ "IOAV[%d] %s<0x%llx>::%s: DTCVREG = %x\n"
+ "IOAV[%d] %s<0x%llx>::%s: RODCOROLEAKCOMP = %x\n"
+ "RODCOROLEAKCOMP"
+ "RODCOROLEAKCOMP = %x\n"
+ "auto connect must be disabled for seamless update\n"
+ "disconnect ufp(%d,%d) from dfp(%d,%d)\n"
+ "disconnect ufp(%d,%d) from ufp(%d,%d) seamlessly\n"
+ "handleSetPllCoreCfgTunables"
+ "no available peer pipe for rearrangement\n"
+ "no available ufp peer found seamlessly\n"
+ "rearrange only support single pipe\n"
+ "site.AppleT8132DPTXPort"
+ "testOnly with success\n"
```
