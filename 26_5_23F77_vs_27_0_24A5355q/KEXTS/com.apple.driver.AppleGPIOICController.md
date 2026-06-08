## com.apple.driver.AppleGPIOICController

> `com.apple.driver.AppleGPIOICController`

```diff

-61.80.1.0.0
-  __TEXT.__cstring: 0xf82
+65.0.0.0.0
+  __TEXT.__cstring: 0xf8a
   __TEXT.__const: 0x13b
   __TEXT.__os_log: 0xd9
-  __TEXT_EXEC.__text: 0xba00
+  __TEXT_EXEC.__text: 0xbabc
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x150
   __DATA.__bss: 0x18
-  __DATA_CONST.__auth_got: 0x210
-  __DATA_CONST.__got: 0x80
   __DATA_CONST.__mod_init_func: 0x28
   __DATA_CONST.__mod_term_func: 0x28
   __DATA_CONST.__const: 0x2688
   __DATA_CONST.__kalloc_type: 0x200
   __DATA_CONST.__kalloc_var: 0xf0
-  UUID: 2DA65C38-5B15-3146-92FA-F9769225E611
+  __DATA_CONST.__auth_got: 0x210
+  __DATA_CONST.__got: 0x80
+  UUID: B85E0152-C856-3656-A254-87170ABAB339
   Functions: 294
   Symbols:   0
   CStrings:  114
Functions:
~ __ZN16AppleT8006GPIOIC15claimWakeEventsEv -> sub_fffffe0008c07030 : 2088 -> 2084
~ sub_fffffe000897bcb8 -> sub_fffffe0008c07884 : 1436 -> 1416
~ __ZN16AppleT8101GPIOIC20callPlatformFunctionEPK8OSSymbolbPvS3_S3_S3_ -> sub_fffffe0008c09ba4 : 2864 -> 2844
~ sub_fffffe000897f844 -> sub_fffffe0008c0b3e8 : 764 -> 800
~ sub_fffffe000897fbf4 -> sub_fffffe0008c0b7bc : 296 -> 356
~ __ZN21AppleGPIOICController5startEP9IOService -> sub_fffffe0008c0c4fc : 3932 -> 4088
~ __ZN19AppleS5L8960XGPIOIC20callPlatformFunctionEPK8OSSymbolbPvS3_S3_S3_ -> sub_fffffe0008c0fc40 : 2864 -> 2844
CStrings:
+ "%s: Marked %u pins in '%s' node as ASC only \n"
+ "/arm-io"
+ "ie-fix"
- "/arm-io/gpio"
- "/arm-io/gpio0"
- "no-restore-use-gpio-alias"

```
