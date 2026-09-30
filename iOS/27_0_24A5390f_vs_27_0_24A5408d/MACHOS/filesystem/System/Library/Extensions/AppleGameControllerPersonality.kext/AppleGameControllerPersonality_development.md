## AppleGameControllerPersonality_development

> `/System/Library/Extensions/AppleGameControllerPersonality.kext/AppleGameControllerPersonality_development`

### Sections with Same Size but Changed Content

- `__DATA.__data`

```diff

-14.0.21.0.0
-  __TEXT.__cstring: 0x24b
-  __TEXT.__os_log: 0x2e3
-  __TEXT_EXEC.__text: 0x1f44
-  __TEXT_EXEC.__auth_stubs: 0x140
+14.0.24.0.0
+  __TEXT.__cstring: 0x2dc
+  __TEXT.__os_log: 0x3a1
+  __TEXT_EXEC.__text: 0x2820
+  __TEXT_EXEC.__auth_stubs: 0x150
   __DATA.__data: 0xc8
-  __DATA.__common: 0x88
-  __DATA.__bss: 0x10
-  __DATA_CONST.__mod_init_func: 0x18
-  __DATA_CONST.__mod_term_func: 0x18
-  __DATA_CONST.__const: 0x1388
-  __DATA_CONST.__kalloc_type: 0xc0
-  __DATA_CONST.__auth_got: 0xa0
-  __DATA_CONST.__got: 0x70
-  Functions: 60
-  Symbols:   370
-  CStrings:  35
+  __DATA.__common: 0xb0
+  __DATA.__bss: 0x18
+  __DATA_CONST.__mod_init_func: 0x20
+  __DATA_CONST.__mod_term_func: 0x20
+  __DATA_CONST.__const: 0x1b20
+  __DATA_CONST.__kalloc_type: 0x100
+  __DATA_CONST.__auth_got: 0xa8
+  __DATA_CONST.__got: 0x80
+  Functions: 79
+  Symbols:   403
+  CStrings:  44
 
Symbols:
+ _GLOBAL__sub_I_SteamControllerUserEventDriver.cpp
+ __ZL34SteamControllerUserEventDriver_ktv
+ __ZN15OSMetaClassBase9_ptmf2ptfEPKS_MS_FvvE
+ __ZN30SteamControllerUserEventDriver10gMetaClassE
+ __ZN30SteamControllerUserEventDriver10superClassE
+ __ZN30SteamControllerUserEventDriver11handleStartEP9IOService
+ __ZN30SteamControllerUserEventDriver17handleInputReportEyjPvm
+ __ZN30SteamControllerUserEventDriver21handleInterruptReportEyP18IOMemoryDescriptor15IOHIDReportTypej
+ __ZN30SteamControllerUserEventDriver21handleInterruptReportEyP18IOMemoryDescriptor15IOHIDReportTypej_vfpthunk_
+ __ZN30SteamControllerUserEventDriver5probeEP9IOServicePi
+ __ZN30SteamControllerUserEventDriver9MetaClassC1Ev
+ __ZN30SteamControllerUserEventDriver9MetaClassC2Ev
+ __ZN30SteamControllerUserEventDriver9MetaClassD0Ev
+ __ZN30SteamControllerUserEventDriver9MetaClassD1Ev
+ __ZN30SteamControllerUserEventDriver9metaClassE
+ __ZN30SteamControllerUserEventDriverC1EPK11OSMetaClass
+ __ZN30SteamControllerUserEventDriverC1Ev
+ __ZN30SteamControllerUserEventDriverC2EPK11OSMetaClass
+ __ZN30SteamControllerUserEventDriverC2Ev
+ __ZN30SteamControllerUserEventDriverD0Ev
+ __ZN30SteamControllerUserEventDriverD1Ev
+ __ZN30SteamControllerUserEventDriverD2Ev
+ __ZN30SteamControllerUserEventDriverdlEPvm
+ __ZN30SteamControllerUserEventDrivernwEm
+ __ZNK30SteamControllerUserEventDriver12getMetaClassEv
+ __ZNK30SteamControllerUserEventDriver9MetaClass5allocEv
+ __ZTV15IORegistryEntry
+ __ZTV30SteamControllerUserEventDriver
+ __ZTVN30SteamControllerUserEventDriver9MetaClassE
+ __ZZN30SteamControllerUserEventDriver11handleStartEP9IOServiceE11_os_log_fmt
+ __ZZN30SteamControllerUserEventDriver17handleInputReportEyjPvmE11_os_log_fmt
+ __ZZN30SteamControllerUserEventDriver17handleInputReportEyjPvmE11_os_log_fmt_0
+ _gIOServicePlane
CStrings:
+ "121111121222121211111112112"
+ "GCIOMatchVirtual"
+ "RegisterService"
+ "SteamControllerUserEventDriver"
+ "SteamControllerUserEventDriver connected; registering service"
+ "SteamControllerUserEventDriver disconnected; terminating"
+ "SteamControllerUserEventDriver::handleStart(<IOHIDInterface %#010llx>)"
+ "bInterfaceNumber"
+ "site.SteamControllerUserEventDriver"
```
