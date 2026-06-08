## IOGameControllerFamily

> `/System/Library/Extensions/IOGameControllerFamily.kext/IOGameControllerFamily`

```diff

-13.5.1.0.0
+14.0.14.0.0
   __TEXT.__const: 0x480
-  __TEXT.__cstring: 0xeb6
-  __TEXT.__os_log: 0x1b00
-  __TEXT_EXEC.__text: 0x18c64
-  __TEXT_EXEC.__auth_stubs: 0x520
+  __TEXT.__cstring: 0x101c
+  __TEXT.__os_log: 0x1c4a
+  __TEXT_EXEC.__text: 0x1ab48
+  __TEXT_EXEC.__auth_stubs: 0x540
   __DATA.__data: 0xc8
-  __DATA.__common: 0x240
-  __DATA.__bss: 0x10
-  __DATA_CONST.__auth_got: 0x290
+  __DATA.__common: 0x290
+  __DATA.__bss: 0x18
+  __DATA_CONST.__mod_init_func: 0x60
+  __DATA_CONST.__mod_term_func: 0x60
+  __DATA_CONST.__const: 0x5a70
+  __DATA_CONST.__kalloc_type: 0x840
+  __DATA_CONST.__auth_got: 0x2a0
   __DATA_CONST.__got: 0xd8
-  __DATA_CONST.__mod_init_func: 0x50
-  __DATA_CONST.__mod_term_func: 0x50
-  __DATA_CONST.__const: 0x4d30
-  __DATA_CONST.__kalloc_type: 0x7c0
-  UUID: 24CD8E4D-B7A9-3E33-B4C8-1DEA4DFF3954
-  Functions: 622
-  Symbols:   828
-  CStrings:  276
+  UUID: 6953A1F3-6D2F-3862-9964-199229191F3A
+  Functions: 673
+  Symbols:   915
+  CStrings:  298
 
Symbols:
+ _GLOBAL__sub_I_IOGCDynamicDeviceProbe.cpp
+ _GLOBAL__sub_I_IOGCDynamicDeviceProbeUserClient.cpp
+ _ZN32IOGCDynamicDeviceProbeUserClient5startEP9IOService.cold.1
+ _ZN32IOGCDynamicDeviceProbeUserClient5startEP9IOService.cold.2
+ __ZL26IOGCDynamicDeviceProbe_ktv
+ __ZL36IOGCDynamicDeviceProbeUserClient_ktv
+ __ZN12IOUserClient19clientMemoryForTypeEjPjPP18IOMemoryDescriptor
+ __ZN22IOGCDynamicDeviceProbe10gMetaClassE
+ __ZN22IOGCDynamicDeviceProbe10handleOpenEP9IOServicejPv
+ __ZN22IOGCDynamicDeviceProbe10superClassE
+ __ZN22IOGCDynamicDeviceProbe11handleCloseEP9IOServicej
+ __ZN22IOGCDynamicDeviceProbe13markSupportedEP9IOServicejPK12OSDictionary
+ __ZN22IOGCDynamicDeviceProbe15markUnsupportedEP9IOServicej
+ __ZN22IOGCDynamicDeviceProbe4stopEP9IOService
+ __ZN22IOGCDynamicDeviceProbe5probeEP9IOServicePi
+ __ZN22IOGCDynamicDeviceProbe5startEP9IOService
+ __ZN22IOGCDynamicDeviceProbe9MetaClassC1Ev
+ __ZN22IOGCDynamicDeviceProbe9MetaClassC2Ev
+ __ZN22IOGCDynamicDeviceProbe9MetaClassD0Ev
+ __ZN22IOGCDynamicDeviceProbe9MetaClassD1Ev
+ __ZN22IOGCDynamicDeviceProbe9getDeviceEv
+ __ZN22IOGCDynamicDeviceProbe9metaClassE
+ __ZN22IOGCDynamicDeviceProbeC1EPK11OSMetaClass
+ __ZN22IOGCDynamicDeviceProbeC1Ev
+ __ZN22IOGCDynamicDeviceProbeC2EPK11OSMetaClass
+ __ZN22IOGCDynamicDeviceProbeC2Ev
+ __ZN22IOGCDynamicDeviceProbeD0Ev
+ __ZN22IOGCDynamicDeviceProbeD1Ev
+ __ZN22IOGCDynamicDeviceProbeD2Ev
+ __ZN22IOGCDynamicDeviceProbedlEPvm
+ __ZN22IOGCDynamicDeviceProbenwEm
+ __ZN32IOGCDynamicDeviceProbeUserClient10gMetaClassE
+ __ZN32IOGCDynamicDeviceProbeUserClient10superClassE
+ __ZN32IOGCDynamicDeviceProbeUserClient11clientCloseEv
+ __ZN32IOGCDynamicDeviceProbeUserClient12didTerminateEP9IOServicejPb
+ __ZN32IOGCDynamicDeviceProbeUserClient12initWithTaskEP4taskPvj
+ __ZN32IOGCDynamicDeviceProbeUserClient14_userGetDeviceEPS_PvP25IOExternalMethodArguments
+ __ZN32IOGCDynamicDeviceProbeUserClient14externalMethodEjP31IOExternalMethodArgumentsOpaque
+ __ZN32IOGCDynamicDeviceProbeUserClient17_userAcceptDeviceEPS_PvP25IOExternalMethodArguments
+ __ZN32IOGCDynamicDeviceProbeUserClient17_userRejectDeviceEPS_PvP25IOExternalMethodArguments
+ __ZN32IOGCDynamicDeviceProbeUserClient25unserializeInputArgumentsEP25IOExternalMethodArguments
+ __ZN32IOGCDynamicDeviceProbeUserClient40createMemoryDescriptorFromInputArgumentsEP25IOExternalMethodArguments
+ __ZN32IOGCDynamicDeviceProbeUserClient4freeEv
+ __ZN32IOGCDynamicDeviceProbeUserClient4stopEP9IOService
+ __ZN32IOGCDynamicDeviceProbeUserClient5startEP9IOService
+ __ZN32IOGCDynamicDeviceProbeUserClient8_methodsE
+ __ZN32IOGCDynamicDeviceProbeUserClient9MetaClassC1Ev
+ __ZN32IOGCDynamicDeviceProbeUserClient9MetaClassC2Ev
+ __ZN32IOGCDynamicDeviceProbeUserClient9MetaClassD0Ev
+ __ZN32IOGCDynamicDeviceProbeUserClient9MetaClassD1Ev
+ __ZN32IOGCDynamicDeviceProbeUserClient9metaClassE
+ __ZN32IOGCDynamicDeviceProbeUserClientC1EPK11OSMetaClass
+ __ZN32IOGCDynamicDeviceProbeUserClientC1Ev
+ __ZN32IOGCDynamicDeviceProbeUserClientC2EPK11OSMetaClass
+ __ZN32IOGCDynamicDeviceProbeUserClientC2Ev
+ __ZN32IOGCDynamicDeviceProbeUserClientD0Ev
+ __ZN32IOGCDynamicDeviceProbeUserClientD1Ev
+ __ZN32IOGCDynamicDeviceProbeUserClientD2Ev
+ __ZN32IOGCDynamicDeviceProbeUserClientdlEPvm
+ __ZN32IOGCDynamicDeviceProbeUserClientnwEm
+ __ZNK22IOGCDynamicDeviceProbe12getMetaClassEv
+ __ZNK22IOGCDynamicDeviceProbe9MetaClass5allocEv
+ __ZNK32IOGCDynamicDeviceProbeUserClient12getMetaClassEv
+ __ZNK32IOGCDynamicDeviceProbeUserClient9MetaClass5allocEv
+ __ZTV22IOGCDynamicDeviceProbe
+ __ZTV32IOGCDynamicDeviceProbeUserClient
+ __ZTVN22IOGCDynamicDeviceProbe9MetaClassE
+ __ZTVN32IOGCDynamicDeviceProbeUserClient9MetaClassE
+ __ZZN22IOGCDynamicDeviceProbe5probeEP9IOServicePiE11_os_log_fmt
+ __ZZN22IOGCDynamicDeviceProbe5startEP9IOServiceE11_os_log_fmt
+ __ZZN22IOGCDynamicDeviceProbe5startEP9IOServiceE11_os_log_fmt_0
+ __ZZN32IOGCDynamicDeviceProbeUserClient25unserializeInputArgumentsEP25IOExternalMethodArgumentsE11_os_log_fmt
+ __ZZN32IOGCDynamicDeviceProbeUserClient5startEP9IOServiceE11_os_log_fmt
+ __ZZN32IOGCDynamicDeviceProbeUserClient5startEP9IOServiceE11_os_log_fmt_0
+ ____ZN22IOGCDynamicDeviceProbe13markSupportedEP9IOServicejPK12OSDictionary_block_invoke
+ ____ZN22IOGCDynamicDeviceProbe15markUnsupportedEP9IOServicej_block_invoke
+ __block_descriptor_tmp.16
+ __gc_log_dynamic_device
+ _gc_log_dynamic_device.Log
+ _strlen
+ _strncmp
CStrings:
+ "12111112122212121112"
+ "CFBundleIdentifier"
+ "DynamicDevice"
+ "GCSyntheticDevice"
+ "GameControllerClass"
+ "GameControllerSupportedHIDDevice"
+ "IOGCDynamicDeviceProbe"
+ "IOGCDynamicDeviceProbe::probe(<IOHIDDevice %#010llx>)"
+ "IOGCDynamicDeviceProbeUserClient"
+ "IOUserClass"
+ "Privileged"
+ "Rapport"
+ "[%#010llx] <IOHIDDevice %#010llx> already probed."
+ "[%#010llx] Failed to open provider."
+ "[%#010llx] IOGCDynamicDeviceProbe::start(<IOService %#010llx>)"
+ "[%#010llx] IOGCDynamicDeviceProbeUserClient::start(<IOService %#010llx>) for pid %i, %s"
+ "com.apple."
+ "com.apple.private.game-controller.dynamic-device-manager"
+ "dynamic"
+ "mfi"
+ "site.IOGCDynamicDeviceProbe"
+ "site.IOGCDynamicDeviceProbeUserClient"

```
