## com.apple.driver.AppleStockholmControl

> `com.apple.driver.AppleStockholmControl`

```diff

-365.3.1.0.0
-  __TEXT.__cstring: 0x4920
-  __TEXT.__const: 0x30
-  __TEXT_EXEC.__text: 0x14760
+370.33.1.0.0
+  __TEXT.__cstring: 0x47ee
+  __TEXT.__const: 0x50
+  __TEXT_EXEC.__text: 0x14d58
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x219
-  __DATA.__common: 0x1a6
-  __DATA_CONST.__auth_got: 0x298
-  __DATA_CONST.__got: 0x88
+  __DATA.__common: 0x17e
   __DATA_CONST.__mod_init_func: 0x30
   __DATA_CONST.__mod_term_func: 0x30
-  __DATA_CONST.__const: 0x22d8
-  __DATA_CONST.__kalloc_type: 0x1c0
-  UUID: 941B34EA-658B-3F27-9C33-08888435777C
-  Functions: 249
+  __DATA_CONST.__const: 0x1d58
+  __DATA_CONST.__kalloc_type: 0x180
+  __DATA_CONST.__auth_got: 0x280
+  __DATA_CONST.__got: 0x80
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
