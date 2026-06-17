## com.apple.driver.AppleStockholmControl

> `com.apple.driver.AppleStockholmControl`

```diff

-370.33.1.0.0
-  __TEXT.__cstring: 0x45e8 sha256:da0725a8beb0fa84f6aa8c55fd78b13866649aec0076f51eb32e942d31b2309a
+366.6.0.0.0
+  __TEXT.__cstring: 0x4027 sha256:0b60e33df14b4f0db9ca2413ef1377d3b3d151a45ae9d3dd145c848312743c81
   __TEXT.__const: 0x30 sha256:702e01896a7c7374678900589827e3777a6315663dc1cdd5d52bd1e92f356580
-  __TEXT_EXEC.__text: 0x14a48 sha256:b968f26dae47888abad3ef7974996818919388852178fa646bd8ae40742cf8c9
+  __TEXT_EXEC.__text: 0x12898 sha256:d97a62d8517258ff7b0238203ec7fe69816a3b19af52db4ec5c632206436b2ae
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x219 sha256:daf083f6923aa902113832d198dc75e9844436801fc7c84ad413a2df3de091a2
+  __DATA.__data: 0x219 sha256:de273c00d98cca0cbfa2bc59950c5b4cb956f287cf41bc5dda6ddb8242d11c7e
   __DATA.__common: 0x17e sha256:3f563c929f3f5f09a38a776a4c4f86088d0654bf9132492e141a384945cb293a
-  __DATA_CONST.__mod_init_func: 0x30 sha256:e37b2181649cdf48dab4edf78424bbb3fcb4453940308084b6f673e4f86af8e7
-  __DATA_CONST.__mod_term_func: 0x30 sha256:7773abf18ade641d88a0cd99a1695759017ee73a6fc67d34a7413048ec4cb1ce
-  __DATA_CONST.__const: 0x2f78 sha256:7baa8799a916a34adacba13bdf0d447a34a428ef892875e7b240a61ea00613c3
-  __DATA_CONST.__kalloc_type: 0x180 sha256:abf82f56ab2d117e3d179104b09beb14df92d5377952e933f2086a2a728b81a1
-  __DATA_CONST.__auth_got: 0x280 sha256:0bf2e995d4a6998ada1055e1ad4a821e55ffd2b39cc4394dbc5fbafe4a1d7058
-  __DATA_CONST.__got: 0x80 sha256:e7328a9689be65f3c89bc986e43af07ef9f2e634db82fa06d6d95645f2b823bd
-  UUID: D645F530-5587-307C-9D48-A1FAC252A38B
-  Functions: 239
-  Symbols:   743
-  CStrings:  454
+  __DATA_CONST.__auth_got: 0x278 sha256:fb71e9265d57a6a90ae9e1fea6aab358e311155f6c038bfb5727c0f48a914aaa
+  __DATA_CONST.__got: 0x80 sha256:1111eebccf31296c24314ebac81fd5f0f0900cdd60375080188102b02e0d625e
+  __DATA_CONST.__mod_init_func: 0x30 sha256:eedf59b6e2998d355b6ca7e2506e91593d62fdd10c2688050041ae60724ab6cd
+  __DATA_CONST.__mod_term_func: 0x30 sha256:5bce6efaaf15501f5066a05bbee456e5a156fed97b419cec2aa27d58662d4427
+  __DATA_CONST.__const: 0x2f08 sha256:b4785759a4444f6d393f0e7e9b8d8a244a2db572d0d0f34826b77bd1209fe390
+  __DATA_CONST.__kalloc_type: 0x180 sha256:cf93555f2e6cb28b5e5d5bc29abac44ff545eb2655e64244be1cceb0b67ebe16
+  UUID: 9046B8BA-7142-35ED-BA8D-0E5CE5CBF042
+  Functions: 231
+  Symbols:   735
+  CStrings:  417
 
Symbols:
+ .str.70
+ .str.71
+ .str.90
+ .str.96
+ .str.97
+ __ZN21AppleStockholmControl16_startForMesaSEPEP9IOService
+ __ZN31AppleStockholmControlUserClient5dummyEP8OSObjectPvP25IOExternalMethodArguments
+ __func__._ZN21AppleStockholmControl17sendFollowerResetEv
+ _mach_absolute_time
- .str.104
- .str.105
- .str.124
- .str.130
- .str.131
- __ZN18AppleStockholmSPMI13setPowerStateEb
- __ZN21AppleStockholmControl12toggleEnableEy
- __ZN21AppleStockholmControl16getBootStopStateEPy
- __ZN21AppleStockholmControl21setSEBootMeasurementsEb
- __ZN21AppleStockholmControl23setNFCCBootMeasurementsEb
- __ZN21AppleStockholmControl25_bootStopInterruptHandlerEP22IOInterruptEventSourcei
- __ZN31AppleStockholmControlUserClient16extBootStopStateEP8OSObjectPvP25IOExternalMethodArguments
- __ZN31AppleStockholmControlUserClient18extSetEnableToggleEP8OSObjectPvP25IOExternalMethodArguments
- __ZN31AppleStockholmControlUserClient24extSetSEBootMeasurementsEP8OSObjectPvP25IOExternalMethodArguments
- __ZN31AppleStockholmControlUserClient26extSetNFCCBootMeasurementsEP8OSObjectPvP25IOExternalMethodArguments
- _continuoustime_to_absolutetime
- _mach_continuous_time
CStrings:
+ "1211111212221212121111111212"
+ "ERR: %s::%s:%d NFCC model is 0x%x\n"
+ "WARN: %s::%s:%d Error overriding NFCC to 0x%x in EDT\n"
+ "WARN: %s::%s:%d overriding NFCC to 0x%x in EDT\n"
+ "WARN: %s::%s:%d overriding secondary to 0x%x\n"
+ "[%llu] %s::%s:%d Hammerfest NFCC model"
+ "[%llu] ERR: %s::%s:%d NFCC model is 0x%x"
+ "[%llu] WARN: %s::%s:%d Error overriding NFCC to 0x%x in EDT"
+ "[%llu] WARN: %s::%s:%d overriding NFCC to 0x%x in EDT"
+ "[%llu] WARN: %s::%s:%d overriding secondary to 0x%x"
- "12111112122212121211111111112112"
- "2025 Primary"
- "2025 Secondary"
- "BootMeasurements"
- "ERR: %s::%s:%d %s model is 0x%x\n"
- "ERR: %s::%s:%d Error : failed to de-assert enable !\n"
- "ERR: %s::%s:%d Error : failed to re-assert enable !\n"
- "ERR: %s::%s:%d Error: boot stop is toggled while disabled !.\n"
- "ERR: %s::%s:%d External load switch drain override set\n"
- "ERR: %s::%s:%d Failed to create interrupt source\n"
- "ERR: %s::%s:%d Invalid parameter to get command\n"
- "ERR: %s::%s:%d could not find boot measurement function\n"
- "ERR: %s::%s:%d could not find boot stop function\n"
- "Error : invalid parameter count : in=%d, out=%d\n"
- "SOMETHINGSOMETHINGSOMETHING"
- "WARN: %s::%s:%d Error overriding model to 0x%x in EDT\n"
- "WARN: %s::%s:%d Warning: boot stop is toggled.\n"
- "WARN: %s::%s:%d overriding %s to 0x%x in EDT\n"
- "[%llu] %s::%s:%d Boot stop get returned %d (error 0x%x)"
- "[%llu] %s::%s:%d Boot stop not supported"
- "[%llu] %s::%s:%d Enabling boot stop interrupt."
- "[%llu] %s::%s:%d power toggle = %llu"
- "[%llu] ERR: %s::%s:%d %s model is 0x%x"
- "[%llu] ERR: %s::%s:%d Error : failed to de-assert enable !"
- "[%llu] ERR: %s::%s:%d Error : failed to re-assert enable !"
- "[%llu] ERR: %s::%s:%d Error: boot stop is toggled while disabled !."
- "[%llu] ERR: %s::%s:%d External load switch drain override set"
- "[%llu] ERR: %s::%s:%d Failed to create interrupt source"
- "[%llu] ERR: %s::%s:%d Invalid parameter to get command"
- "[%llu] ERR: %s::%s:%d could not find boot measurement function"
- "[%llu] ERR: %s::%s:%d could not find boot stop function"
- "[%llu] WARN: %s::%s:%d Error overriding model to 0x%x in EDT"
- "[%llu] WARN: %s::%s:%d Warning: boot stop is toggled."
- "[%llu] WARN: %s::%s:%d overriding %s to 0x%x in EDT"
- "_bootStopInterruptHandler"
- "function-boot_measurements"
- "function-boot_stop_state"
- "function-se_boot_measurements"
- "getBootStopState"
- "nfc.externalLoadSwitchDrain"
- "secondary"
- "setNFCCBootMeasurements"
- "setSEBootMeasurements"
- "support_boot_measurements"
- "support_bootstop-interrupts"
- "support_bootstop_state"
- "toggleEnable"

```
