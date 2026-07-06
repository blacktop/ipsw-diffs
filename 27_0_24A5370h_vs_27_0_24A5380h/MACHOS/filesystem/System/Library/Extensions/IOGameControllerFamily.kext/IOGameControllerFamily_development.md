## IOGameControllerFamily_development

> `/System/Library/Extensions/IOGameControllerFamily.kext/IOGameControllerFamily_development`

```diff

   __TEXT.__const: 0x480
-  __TEXT.__cstring: 0x279e
-  __TEXT.__os_log: 0x901a
-  __TEXT_EXEC.__text: 0x2a5c0
+  __TEXT.__cstring: 0x27de
+  __TEXT.__os_log: 0x90fa
+  __TEXT_EXEC.__text: 0x2a93c
   __TEXT_EXEC.__auth_stubs: 0x540
   __DATA.__data: 0xc8
   __DATA.__common: 0x2b8

   __DATA_CONST.__const: 0x62b8
   __DATA_CONST.__kalloc_type: 0x880
   __DATA_CONST.__auth_got: 0x2a0
-  __DATA_CONST.__got: 0xd8
-  Functions: 991
-  Symbols:   2172
-  CStrings:  614
+  __DATA_CONST.__got: 0xe0
+  Functions: 993
+  Symbols:   2178
+  CStrings:  619
 
Sections:
~ __DATA.__data : content changed
~ __DATA_CONST.__mod_init_func : content changed
~ __DATA_CONST.__mod_term_func : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__kalloc_type : content changed
Symbols:
+ _ZN22IOGCDynamicDeviceProbe9preflightEP11IOHIDDevice
+ __ZN17IOHIDEventService9metaClassE
+ __ZN22IOGCDynamicDeviceProbe9preflightEP11IOHIDDevice
+ __ZZN22IOGCDynamicDeviceProbe5probeEP9IOServicePiE11_os_log_fmt_3
+ __ZZN22IOGCDynamicDeviceProbe9preflightEP11IOHIDDeviceE11_os_log_fmt
+ __ZZN22IOGCDynamicDeviceProbe9preflightEP11IOHIDDeviceE11_os_log_fmt_1
Functions:
~ __ZN16PSVR2SenseDevice26handleBluetoothInputReportEyyjPvm : 332 -> 328
~ __ZN40PSVR2SenseDeviceHIDEventServerUserClient18_userGetPropertiesEPS_PvP25IOExternalMethodArguments : 3824 -> 4128
~ __ZN22IOGCDynamicDeviceProbe5probeEP9IOServicePi : 1748 -> 2000
~ __ZN22IOGCDynamicDeviceProbe5startEP9IOService : 1124 -> 876
~ ____ZN22IOGCDynamicDeviceProbe15markUnsupportedEP9IOServicej_block_invoke : 584 -> 316
+ __ZN22IOGCDynamicDeviceProbe9preflightEP11IOHIDDevice
~ ____ZN22IOGCDynamicDeviceProbe13markSupportedEP9IOServicejPK12OSDictionary_block_invoke : 348 -> 356
~ __ZN32IOGCDynamicDeviceProbeUserClient17_userRejectDeviceEPS_PvP25IOExternalMethodArguments : 232 -> 264
~ __ZN32IOGCDynamicDeviceProbeUserClient17_userAcceptDeviceEPS_PvP25IOExternalMethodArguments : 236 -> 268
+ _ZN16IOGCCommandQueue11asyncActionEPFiP8OSObjectPvES2_NS_12AsyncOptionsEPPNS_12ContinuationE.cold.3
CStrings:
+ "GameControllerCategory"
+ "GameControllerEligible"
+ "GameControllerSupport"
+ "IOGCDynamicDeviceProbe not matching on <IOHIDDevice %#010llx> ineligible device."
+ "[%#010llx] <IOHIDDevice %#010llx> matched by other driver."
+ "[%#010llx] <IOHIDDevice %#010llx> probe previously completed and returned %d"
+ "[%#010llx] IOGCDynamicDeviceProbe::handleClose(<IOService %#010llx>)"
+ "[%#010llx] IOGCDynamicDeviceProbe::handleOpen(<IOService %#010llx>)"
+ "[%#010llx] IOGCDynamicDeviceProbe::markSupported(<IOService %#010llx>)"
+ "[%#010llx] IOGCDynamicDeviceProbe::markUnsupported(<IOService %#010llx>)"
+ "deviceInterface"
- "GameControllerClass"
- "[%#010llx] <IOHIDDevice %#010llx> already probed."
- "[%#010llx] IOGCInspectionService::handleClose(<IOService %#010llx>)"
- "[%#010llx] IOGCInspectionService::handleOpen(<IOService %#010llx>)"
- "[%#010llx] IOGCInspectionService::markSupported(<IOService %#010llx>)"
- "[%#010llx] IOGCInspectionService::markUnsupported(<IOService %#010llx>)"

```
