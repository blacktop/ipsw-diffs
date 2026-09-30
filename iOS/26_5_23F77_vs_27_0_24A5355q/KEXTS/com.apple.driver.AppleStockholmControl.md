## com.apple.driver.AppleStockholmControl

> `com.apple.driver.AppleStockholmControl`

```diff

-365.3.1.0.0
-  __TEXT.__cstring: 0x4920 sha256:5d82195391c0f2d851208e454db8c92e4e71e20a850d134daeb013d4be55746f
-  __TEXT.__const: 0x30 sha256:702e01896a7c7374678900589827e3777a6315663dc1cdd5d52bd1e92f356580
-  __TEXT_EXEC.__text: 0x14760 sha256:285b357c8e471cd5f76cce42f571ce80c5eb5dbe8bca961644dbfc7ae329941d
+370.33.1.0.0
+  __TEXT.__cstring: 0x47ee sha256:6edf0da39fe94c2fdd7cf557c5d2a84bb66cf7ab554340d4347100022a4b6ebe
+  __TEXT.__const: 0x50 sha256:a16e2dcb8153cfbc0efc3d304f758f779116a6b74db2d76bb7ece3f8fe3eae17
+  __TEXT_EXEC.__text: 0x14d58 sha256:4588828a67640480317b1f11d23e6b29df5b51559367ecd1d6026243473a9b96
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x219 sha256:71a1112148c3b79465123aa4d22911451352c71f21f5391e3a566397c2ea5054
-  __DATA.__common: 0x1a6 sha256:ba69447e82193d9e86e12bb13937b2d962b1c8ed6590381a1d66e1e9a86888b3
-  __DATA_CONST.__auth_got: 0x298 sha256:25d6b3a0acb7e3c7fc17db7da68345fbb5ec376db3791504886631884cced00f
-  __DATA_CONST.__got: 0x88 sha256:df8cbf29850d1c650f61ed2fc39032d0a7390071c569ffd2eeb5ba5626ab7110
-  __DATA_CONST.__mod_init_func: 0x30 sha256:3684cc7bc643f276810cfb4cde9072e928acfdafff54f2ecde948b7ad2f43f9f
-  __DATA_CONST.__mod_term_func: 0x30 sha256:0f22b11e91e2bf5440d391de46c69485a3b843cbffc9fcbeeae74843265917d4
-  __DATA_CONST.__const: 0x22d8 sha256:0e95649b9a87edd8bf227047f14214e10bf55bba6cd36678ef0e62bbea5a1c5b
-  __DATA_CONST.__kalloc_type: 0x1c0 sha256:e027d9198f5beed0ffe88928dbca40957b75af707af20daa42ce695efa97255a
-  UUID: 941B34EA-658B-3F27-9C33-08888435777C
-  Functions: 249
+  __DATA.__data: 0x219 sha256:3d191d84bbb3427e55a95795abe927e9c1a3fde4f54f1a3808822f479533486b
+  __DATA.__common: 0x17e sha256:3f563c929f3f5f09a38a776a4c4f86088d0654bf9132492e141a384945cb293a
+  __DATA_CONST.__mod_init_func: 0x30 sha256:cf1c0193004d2279fc0cf51198e85acc84cb51bb0ff2bb49030a9b0f25fb1200
+  __DATA_CONST.__mod_term_func: 0x30 sha256:ae106aa3bad97d08cd229b1ee98ec829e85969c08ebebe762ff5077c3e5adad7
+  __DATA_CONST.__const: 0x1d58 sha256:4565e74ea23d964b8b0c1ac22d9a0b9c9230a7466b52e5c1bd09a8bb0cb9ff0c
+  __DATA_CONST.__kalloc_type: 0x180 sha256:968a26dbbcfd3dd5926f4c7367763cb34c1046db9a038ffb5daf05bed2177490
+  __DATA_CONST.__auth_got: 0x280 sha256:6f5ebeddfba9539451052e8f0f0ae029123a1c6c988d7d01eca3f3867dc4104a
+  __DATA_CONST.__got: 0x80 sha256:70668c687424813277924cb4b1ea4e8f791007600369f218792454d45f528268
+  UUID: B168D376-D712-3691-BFB3-3C94161447C2
+  Functions: 239
   Symbols:   0
-  CStrings:  471
+  CStrings:  467
 
CStrings:
+ "12111112122212121211111111112112"
+ "121111121222121212111111112221221112"
+ "2025 Primary"
+ "2025 Secondary"
+ "BootMeasurements"
+ "ERR: %s::%s:%d %s model is 0x%x\n"
+ "ERR: %s::%s:%d Error : failed to de-assert enable !\n"
+ "ERR: %s::%s:%d Error : failed to re-assert enable !\n"
+ "ERR: %s::%s:%d Error: boot stop is toggled while disabled !.\n"
+ "ERR: %s::%s:%d External load switch drain override set\n"
+ "ERR: %s::%s:%d Failed to create interrupt source\n"
+ "ERR: %s::%s:%d Invalid parameter to get command\n"
+ "ERR: %s::%s:%d could not find boot measurement function\n"
+ "ERR: %s::%s:%d could not find boot stop function\n"
+ "Error : invalid parameter count : in=%d, out=%d\n"
+ "SOMETHINGSOMETHINGSOMETHING"
+ "WARN: %s::%s:%d Error overriding model to 0x%x in EDT\n"
+ "WARN: %s::%s:%d Warning: boot stop is toggled.\n"
+ "WARN: %s::%s:%d overriding %s to 0x%x in EDT\n"
+ "[%llu] %s::%s:%d Boot stop get returned %d (error 0x%x)"
+ "[%llu] %s::%s:%d Boot stop not supported"
+ "[%llu] %s::%s:%d Enabling boot stop interrupt."
+ "[%llu] %s::%s:%d power toggle = %llu"
+ "[%llu] ERR: %s::%s:%d %s model is 0x%x"
+ "[%llu] ERR: %s::%s:%d Error : failed to de-assert enable !"
+ "[%llu] ERR: %s::%s:%d Error : failed to re-assert enable !"
+ "[%llu] ERR: %s::%s:%d Error: boot stop is toggled while disabled !."
+ "[%llu] ERR: %s::%s:%d External load switch drain override set"
+ "[%llu] ERR: %s::%s:%d Failed to create interrupt source"
+ "[%llu] ERR: %s::%s:%d Invalid parameter to get command"
+ "[%llu] ERR: %s::%s:%d could not find boot measurement function"
+ "[%llu] ERR: %s::%s:%d could not find boot stop function"
+ "[%llu] WARN: %s::%s:%d Error overriding model to 0x%x in EDT"
+ "[%llu] WARN: %s::%s:%d Warning: boot stop is toggled."
+ "[%llu] WARN: %s::%s:%d overriding %s to 0x%x in EDT"
+ "_bootStopInterruptHandler"
+ "function-boot_measurements"
+ "function-boot_stop_state"
+ "function-se_boot_measurements"
+ "getBootStopState"
+ "nfc.externalLoadSwitchDrain"
+ "secondary"
+ "setNFCCBootMeasurements"
+ "setSEBootMeasurements"
+ "support_boot_measurements"
+ "support_bootstop-interrupts"
+ "support_bootstop_state"
+ "toggleEnable"
- "1211111212221212121111111122212211112"
- "121111121222121212111111121112"
- "AppleMesaSEPDriver"
- "AppleMesaSEPDriverInterface"
- "AppleStockholmSPMINotification"
- "ERR: %s::%s:%d Failed to find SEP Driver\n"
- "ERR: %s::%s:%d Failed to init _spmiNotification\n"
- "ERR: %s::%s:%d NFCC model is 0x%x\n"
- "ERR: %s::%s:%d No wakes due to missing %s driver\n"
- "ERR: %s::%s:%d could not find SEP service\n"
- "ERR: %s::%s:%d could not find wake reason function\n"
- "ERR: %s::%s:%d could not register for matching SEP service\n"
- "ERR: %s::%s:%d failed starting _spmiNotification\n"
- "ERR: %s::%s:%d failed to attach _spmiNotification\n"
- "ERR: %s::%s:%d failed to check wake reason: %x\n"
- "ERR: %s::%s:%d failed to kick off Mesa: %x\n"
- "WARN: %s::%s:%d Error overriding NFCC to 0x%x in EDT\n"
- "WARN: %s::%s:%d got 2 wake stockholm functions\n"
- "WARN: %s::%s:%d overriding NFCC to 0x%x in EDT\n"
- "WARN: %s::%s:%d overriding secondary to 0x%x\n"
- "[%llu] %s::%s:%d Hammerfest NFCC model"
- "[%llu] %s::%s:%d Hammerfest in semi-off mode - publish a notification for the daemon"
- "[%llu] %s::%s:%d _spmiNotification destroyed"
- "[%llu] %s::%s:%d data were received prior to open - push to the user"
- "[%llu] %s::%s:%d power is enabled for Hammerfest - interrupts are enabled already"
- "[%llu] %s::%s:%d started _spmiNotification"
- "[%llu] ERR: %s::%s:%d Failed to find SEP Driver"
- "[%llu] ERR: %s::%s:%d Failed to init _spmiNotification"
- "[%llu] ERR: %s::%s:%d NFCC model is 0x%x"
- "[%llu] ERR: %s::%s:%d No wakes due to missing %s driver"
- "[%llu] ERR: %s::%s:%d could not find SEP service"
- "[%llu] ERR: %s::%s:%d could not find wake reason function"
- "[%llu] ERR: %s::%s:%d could not register for matching SEP service"
- "[%llu] ERR: %s::%s:%d failed starting _spmiNotification"
- "[%llu] ERR: %s::%s:%d failed to attach _spmiNotification"
- "[%llu] ERR: %s::%s:%d failed to check wake reason: %x"
- "[%llu] ERR: %s::%s:%d failed to kick off Mesa: %x"
- "[%llu] WARN: %s::%s:%d Error overriding NFCC to 0x%x in EDT"
- "[%llu] WARN: %s::%s:%d got 2 wake stockholm functions"
- "[%llu] WARN: %s::%s:%d overriding NFCC to 0x%x in EDT"
- "[%llu] WARN: %s::%s:%d overriding secondary to 0x%x"
- "_serviceMatchedHandler"
- "_startForMesaSEP"
- "function-wake_stockholm"
- "function-wake_stockholm_soc"
- "hammerfest-data-available-event"
- "mesa"
- "setPowerState"
- "site.AppleStockholmSPMINotification"
- "support_wake_stockholm"
- "support_wake_stockholm_soc"
- "wake"

```
