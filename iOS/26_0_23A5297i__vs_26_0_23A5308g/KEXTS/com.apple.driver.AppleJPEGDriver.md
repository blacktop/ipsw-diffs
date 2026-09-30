## com.apple.driver.AppleJPEGDriver

> `com.apple.driver.AppleJPEGDriver`

```diff

-7.7.1.0.0
-  __TEXT.__cstring: 0x2750
-  __TEXT.__os_log: 0x89a4
-  __TEXT.__const: 0x34d4
-  __TEXT_EXEC.__text: 0x29eac
+7.7.2.0.0
+  __TEXT.__cstring: 0x2829
+  __TEXT.__os_log: 0x8c84
+  __TEXT.__const: 0x3684
+  __TEXT_EXEC.__text: 0x2aa54
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x2208
-  __DATA.__common: 0x358
+  __DATA.__common: 0x380
   __DATA.__bss: 0x1
   __DATA_CONST.__auth_got: 0x340
   __DATA_CONST.__got: 0x98
-  __DATA_CONST.__mod_init_func: 0xa8
-  __DATA_CONST.__mod_term_func: 0xa8
-  __DATA_CONST.__const: 0x4578
-  __DATA_CONST.__kalloc_type: 0xb40
-  UUID: 1095EEF4-3593-3A62-932A-532B1FAF0288
-  Functions: 1596
+  __DATA_CONST.__mod_init_func: 0xb0
+  __DATA_CONST.__mod_term_func: 0xb0
+  __DATA_CONST.__const: 0x4700
+  __DATA_CONST.__kalloc_type: 0xb80
+  UUID: 56BF938B-1EB0-3107-9532-E5FFFA9E8647
+  Functions: 1629
   Symbols:   0
-  CStrings:  490
+  CStrings:  502
 
CStrings:
+ "AppleJPEGDriver: %s(): Device has only 1 clock index in the EDT (type = 0x%x, hardware version = 0x%x)\n"
+ "AppleJPEGDriver: %s(): Error! enableDeviceClock(en = %u, idx = %u) returned %d\n"
+ "AppleJPEGDriver: %s(): Error! enablePsdService(en = %u) returned %d\n"
+ "AppleJPEGDriver: %s(): Error! function-set_perf_state_floor failed to set perf to %d! (result = %d)\n"
+ "AppleJPEGDriver: %s(): Skipping HW version check [0x%x (reg), 0x%x (EDT)]\n"
+ "AppleJPEGDriver: %s, ERROR: specified core %d doesn't exist on this device\n"
+ "AppleJPEGDriver: %s, ERROR: specified core doesn't exist on this platform\n"
+ "AppleJPEGDriver: %s: running on specified core: %d\n"
+ "AppleJPEGDriver: ** %s[%p] : 'jpeg-disableWorkaround' boot-arg detected: %u\n"
+ "AppleJPEGDriver: ** %s[%p] : 'jpeg-fsim' boot-arg detected: %u\n"
+ "AppleJPEGDriver: ** %s[%p] : 'jpeg-log' boot-arg detected: 0x%x\n"
+ "AppleJPEGDriver: - %s : running on core w/ least workload: %d\n"
+ "BorageFunctions"
+ "jpeg-fsim"
+ "parseBootArgs"
+ "singleClockIndexDevice"
+ "site.BorageFunctions"
+ "uint32_t AppleJPEGDriver::assign_codec_gated(JpegRequest *)"
+ "virtual bool BorageFunctions::setupAXIRegisterOffset(uint32_t, uint64_t)"
- "AppleJPEGDriver: %s() :: WARNING: function-set_perf_state_floor did not set perf to %d! (result = %d)\n"
- "AppleJPEGDriver: %s(): Enter enableDeviceClockWrapper(en = %u, idx = %u)\n"
- "AppleJPEGDriver: %s(): Error! Call failed (enable = %u, index = %u) with %d\n"
- "AppleJPEGDriver: %s(): Skipping call to enableDeviceClockLowLevel(en = %u, idx = %u)\n"
- "AppleJPEGDriver: %s(): enableDeviceClock(en = %u, idx = %u) returned %d\n"
- "AppleJPEGDriver: %s(): enablePsdService(en = %u) returned %d\n"
- "AppleJPEGDriver: ** %s[%p] : JPEG decoder driver logging is enabled [0x%x]\n"

```
