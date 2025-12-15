## com.apple.driver.AppleThunderboltNHI

> `com.apple.driver.AppleThunderboltNHI`

```diff

-817.60.2.0.0
-  __TEXT.__cstring: 0xbc66
+817.80.4.0.0
+  __TEXT.__cstring: 0xbc5d
   __TEXT.__const: 0x28a20
-  __TEXT.__os_log: 0x7273
-  __TEXT_EXEC.__text: 0x3bbfc
+  __TEXT.__os_log: 0x726a
+  __TEXT_EXEC.__text: 0x3bcac
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x280
   __DATA.__common: 0x478

   __DATA_CONST.__const: 0x69a8
   __DATA_CONST.__kalloc_type: 0x740
   __DATA_CONST.__kalloc_var: 0x460
-  UUID: 30121035-B159-3095-89B6-9805FCE64D74
+  UUID: F3EFE1EB-7922-3F64-B6D0-9CC1A984A699
   Functions: 947
   Symbols:   0
   CStrings:  988
Functions:
~ __ZN30AppleThunderboltNHIGenericACIO17enableEmbeddedCPUEb : 8344 -> 8412
~ __ZN30AppleThunderboltNHIGenericACIO24setARMIODevicePowerStateEN16AppleARMIODevice16DevicePowerStateEj : 1936 -> 1972
~ __ZN30AppleThunderboltNHIGenericACIO17enablePowerDomainEjb : 1188 -> 1260
CStrings:
+ "%lldus AppleThunderboltGenericHAL(%d)<%p>::processSetPMState -  dispatchAsync( processSetPMState)\n"
+ "22:44:12"
+ "Dec  5 2025"
- "%lldus AppleThunderboltGenericHAL(%d)<%p>::systemWillShutdown -  dispatchAsync( processSystemWillShutdown)\n"
- "20:53:59"
- "Nov 18 2025"

```
