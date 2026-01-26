## com.apple.driver.AppleThunderboltUSBUpAdapter

> `com.apple.driver.AppleThunderboltUSBUpAdapter`

```diff

-128.80.6.0.0
-  __TEXT.__cstring: 0x1902
-  __TEXT.__os_log: 0x1605
-  __TEXT_EXEC.__text: 0x9e48
+128.80.7.0.0
+  __TEXT.__cstring: 0x1901
+  __TEXT.__os_log: 0x1604
+  __TEXT_EXEC.__text: 0x9fe8
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x1e8
   __DATA.__common: 0x38

   __DATA_CONST.__mod_term_func: 0x8
   __DATA_CONST.__const: 0x7a8
   __DATA_CONST.__kalloc_type: 0x40
-  UUID: A2D26077-600C-3A3B-B147-158CC5985225
+  UUID: 1B71908D-6130-3FB6-BFC9-93655981FA5F
   Functions: 53
   Symbols:   0
   CStrings:  141
Functions:
~ __ZN28AppleThunderboltUSBUpAdapter5startEP9IOService : 8132 -> 8120
~ __ZN28AppleThunderboltUSBUpAdapter16activateInternalEP28IOThunderboltDispatchContext : 5212 -> 5272
~ __ZN28AppleThunderboltUSBUpAdapter18deactivateInternalEP28IOThunderboltDispatchContext : 4008 -> 4028
~ __ZN28AppleThunderboltUSBUpAdapter4wakeEv : 316 -> 392
~ __ZN28AppleThunderboltUSBUpAdapter5sleepEv : 328 -> 460
~ __ZN28AppleThunderboltUSBUpAdapter7messageEjP9IOServicePv : 1048 -> 1188
CStrings:
+ "%lldus AppleThunderboltUSBUpAdapter<%p>::message - type = 0x%x calling activatesync\n"
- "%lldus AppleThunderboltUSBUpAdapter<%p>::message - type = 0x%x calling activateAsync\n"

```
