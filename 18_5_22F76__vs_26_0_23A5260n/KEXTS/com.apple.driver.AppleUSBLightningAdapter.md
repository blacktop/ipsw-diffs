## com.apple.driver.AppleUSBLightningAdapter

> `com.apple.driver.AppleUSBLightningAdapter`

```diff

-64.0.0.0.0
+68.0.0.0.0
   __TEXT.__const: 0x8
-  __TEXT.__cstring: 0x1185
-  __TEXT.__os_log: 0xa8b
-  __TEXT_EXEC.__text: 0x5c1c
+  __TEXT.__cstring: 0x1316
+  __TEXT.__os_log: 0xdbe
+  __TEXT_EXEC.__text: 0x6a80
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc4
   __DATA.__common: 0x60
-  __DATA_CONST.__auth_got: 0x140
-  __DATA_CONST.__got: 0xa0
+  __DATA.__bss: 0x2
+  __DATA_CONST.__auth_got: 0x1a8
+  __DATA_CONST.__got: 0xa8
   __DATA_CONST.__mod_init_func: 0x10
   __DATA_CONST.__mod_term_func: 0x10
-  __DATA_CONST.__const: 0xe38
+  __DATA_CONST.__const: 0xe98
   __DATA_CONST.__kalloc_type: 0x80
-  UUID: 86FD28A9-1DB1-31C4-8B31-453A78971430
-  Functions: 107
+  UUID: 1BA16BBB-B596-3294-8044-667CE934861D
+  Functions: 110
   Symbols:   0
-  CStrings:  161
+  CStrings:  179
 
CStrings:
+ "%s::%s(): Implicitly marking transport as user authorized...\n"
+ "%s::%s(): Matched on USB2 transport service... (transport: %s)\n"
+ "%s::%s(): Received active state change for USB2 transport... (transportActive: %s)\n"
+ "%s::%s(): Received authorization state change for USB2 transport... (authorizationStatus: %d [%s], transportRestricted: %s)\n"
+ "%s::%s(): Registering for USB2 transport notifications...\n"
+ "%s::%s(): Registering for interest notifications on USB2 transport service... (transport: %s)\n"
+ "%s::%s(): Toggling ACC_PWR for %d ms...\n"
+ "%s::%s(): USB2 transport has been unrestricted!\n"
+ "%s::%s(): USB2 transport has been user authorized!\n"
+ "%s::%s(): Updated user authorization timestamp for USB2! (m_explicitUserAuthorizationTimestampS: %llu)\n"
+ "%s::%s(): auxpRearPortControlAccPower: %d\n"
+ "%s::%s(): currentSystemUptimeS: %llu, m_explicitUserAuthorizationTimestampS: %llu\n"
+ "1211111212221212111111211111212222222211221111111212211112222221222212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112111111222111122"
+ "B24@?0^{IOService=^^?i^{ExpansionData}^{OSDictionary}^{OSDictionary}^{ExpansionData}^{IOService}i^{IOService}[2I]QQ^{IOServicePM}B^vi^{IOInterruptSource}}8^{IONotifier=^^?i}16"
+ "NO"
+ "YES"
+ "[ERROR] %s::%s(): Failed to create ACC_PWR toggle timer!\n"
+ "start_block_invoke"
+ "start_block_invoke_2"
+ "v16@?0^{IOTimerEventSource=^^?i^{IOEventSource}^{OSObject}^?B^{IOWorkLoop}^v^{ExpansionData}^vQ^{ExpansionData}}8"
- "%s::%s(): auxpRearPortControlAccPower %s\n"
- "1211111212221212111111211111212222222211221111111212211112222221222212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112212112111111222"

```
