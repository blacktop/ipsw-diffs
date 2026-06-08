## com.apple.driver.IOPAudioClientManagerDevice

> `com.apple.driver.IOPAudioClientManagerDevice`

```diff

-340.3.0.0.0
+400.34.0.0.0
   __TEXT.__const: 0x8
-  __TEXT.__cstring: 0xdc6
+  __TEXT.__cstring: 0xd8c
   __TEXT.__os_log: 0x986
-  __TEXT_EXEC.__text: 0x4114
+  __TEXT_EXEC.__text: 0x416c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x60
   __DATA.__bss: 0x8
-  __DATA_CONST.__auth_got: 0x88
-  __DATA_CONST.__got: 0x48
   __DATA_CONST.__mod_init_func: 0x10
   __DATA_CONST.__mod_term_func: 0x10
-  __DATA_CONST.__const: 0xef8
+  __DATA_CONST.__const: 0xf00
   __DATA_CONST.__kalloc_type: 0x80
-  UUID: AB806C5C-048C-387F-8E46-8CD383AEDC37
-  Functions: 162
+  __DATA_CONST.__auth_got: 0x88
+  __DATA_CONST.__got: 0x48
+  UUID: 96BF284C-62E8-35BB-93A4-D0AFB6658FE2
+  Functions: 163
   Symbols:   0
   CStrings:  73
 
CStrings:
+ "ret = _enableClientManagerPowerRequest(inEnable, inDirection) == 0 "
- "ret = setClientManagerPowerRequest({ .state = mClientManagerDeviceConfig.targetPowerState, .direction = inDirection, }) == 0 "

```
