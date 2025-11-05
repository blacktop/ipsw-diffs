## com.apple.driver.DCPAVFamilyProxy

> `com.apple.driver.DCPAVFamilyProxy`

```diff

-350.80.2.0.0
-  __TEXT.__const: 0x278
-  __TEXT.__cstring: 0x247d
-  __TEXT.__os_log: 0x129d
-  __TEXT_EXEC.__text: 0x17094
+358.100.35.0.0
+  __TEXT.__const: 0x260
+  __TEXT.__cstring: 0x2478
+  __TEXT.__os_log: 0x12a1
+  __TEXT_EXEC.__text: 0x16e60
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x308
   __DATA.__bss: 0x8
-  __DATA_CONST.__auth_got: 0x2f8
+  __DATA_CONST.__auth_got: 0x300
   __DATA_CONST.__got: 0x118
   __DATA_CONST.__mod_init_func: 0x98
   __DATA_CONST.__mod_term_func: 0x98
-  __DATA_CONST.__const: 0xd1f0
+  __DATA_CONST.__const: 0xd1d0
   __DATA_CONST.__kalloc_type: 0x4c0
   __DATA_CONST.__kalloc_var: 0x3c0
-  UUID: 89F24B59-BB4F-3E05-BF81-A18947BD378D
-  Functions: 808
-  Symbols:   1602
+  UUID: 5EFF8679-552C-39C6-AC05-400C4BAE41C8
+  Functions: 883
+  Symbols:   1694
   CStrings:  285
 
Symbols:
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_16
+ _OUTLINED_FUNCTION_17
+ _OUTLINED_FUNCTION_18
+ _OUTLINED_FUNCTION_19
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_20
+ _OUTLINED_FUNCTION_21
+ _OUTLINED_FUNCTION_22
+ _OUTLINED_FUNCTION_23
+ _OUTLINED_FUNCTION_24
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ _ZN10DCPAVProxy15validateMessageEPKN8DCPAVIPC7MessageEm.cold.1
+ _ZN10DCPAVProxy15validateMessageEPKN8DCPAVIPC7MessageEm.cold.2
+ _ZN10DCPAVProxy15validateMessageEPKN8DCPAVIPC7MessageEm.cold.3
+ _ZN10DCPAVProxy15validateMessageEPKN8DCPAVIPC7MessageEm.cold.4
+ _ZN10DCPAVProxy15validateMessageEPKN8DCPAVIPC7MessageEm.cold.5
+ _ZN10DCPAVProxy15validateMessageEPKN8DCPAVIPC7MessageEm.cold.6
+ _ZN18DCPAVCECController13addCECServiceEv.cold.1
+ _ZN18DCPAVCECController13addCECServiceEv.cold.2
+ _ZN18DCPAVCECController13addCECServiceEv.cold.3
+ _ZN18DCPAVCECController16removeCECServiceEv.cold.1
+ _ZN18DCPAVSACController21_registerSACAggressorEP29DCPAVRemoteSACControllerProxyjjPKyPKj.cold.3
+ _ZN18DCPAVSACController21_registerSACAggressorEP29DCPAVRemoteSACControllerProxyjjPKyPKj.cold.4
+ _ZN20DCPAVControllerProxy20getDefaultPowerStateEv.cold.1
+ _ZN20DCPAVControllerProxy21getVirtualDisplayModeEv.cold.1
+ _ZN20DCPAVControllerProxy22waitForPowerChangeDoneEv.cold.1
+ _ZN20DCPAVControllerProxy30getParticipatesPowerManagementEv.cold.1
+ _ZN24DCPAVAudioInterfaceProxy10handleOpenEP9IOServicejPv.cold.1
+ _ZN24DCPAVAudioInterfaceProxy5startEP9IOService.cold.1
+ _ZN24DCPAVAudioInterfaceProxy5startEP9IOService.cold.2
+ _ZN24DCPAVAudioInterfaceProxy5startEP9IOService.cold.3
+ _ZN24DCPAVAudioInterfaceProxy5startEP9IOService.cold.4
+ _ZN24DCPAVAudioInterfaceProxy5startEP9IOService.cold.5
+ _ZN24DCPAVAudioInterfaceProxy5startEP9IOService.cold.6
+ _ZN26DCPAVRemotePowerController21_setRemoteDevicePowerEP25DCPAVPowerControllerProxyjj.cold.2
+ _ZN26DCPAVRemotePowerController21_setRemoteDevicePowerEP25DCPAVPowerControllerProxyjj.cold.3
+ __ZN22DCPAVCECInterfaceProxy17getEDIDAttributesEv
+ __ZN22DCPAVCECInterfaceProxy18handleEDIDCallbackEPS_PKN8DCPAVIPC7MessageE
+ __ZThn1560_N22DCPAVCECInterfaceProxy17getEDIDAttributesEv
+ ___ZN24DCPAVAudioInterfaceProxy13setPowerStateEmP9IOService_block_invoke.cold.1
+ _bzero
- __ZN22DCPAVCECInterfaceProxy12setHPDStatusEb
- __ZN22DCPAVCECInterfaceProxy18getPhysicalAddressEv
- __ZN22DCPAVCECInterfaceProxy18setPhysicalAddressEt
- __ZN22DCPAVCECInterfaceProxy27handleAddressChangeCallbackEPS_PKN8DCPAVIPC7MessageE
- __ZThn1560_N22DCPAVCECInterfaceProxy12setHPDStatusEb
- __ZThn1560_N22DCPAVCECInterfaceProxy18getPhysicalAddressEv
- __ZThn1560_N22DCPAVCECInterfaceProxy18setPhysicalAddressEt
CStrings:
+ "EDIDCallback"
+ "IOAV[%d] %s<0x%llx>::%s: warning: out-of-order termination _cecInterface(0x%llx) != terminatedService(0x%llx)\n"
+ "warning: out-of-order termination _cecInterface(0x%llx) != terminatedService(0x%llx)\n"
- "AddressChangeCallback"
- "IOAV[%d] %s<0x%llx>::%s: warning: unexpected _cecInterface(0x%llx) != terminatedService(0x%llx) (ignored)\n"
- "warning: unexpected _cecInterface(0x%llx) != terminatedService(0x%llx) (ignored)\n"

```
