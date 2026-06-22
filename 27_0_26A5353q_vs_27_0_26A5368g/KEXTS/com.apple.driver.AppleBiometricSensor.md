## com.apple.driver.AppleBiometricSensor

> `com.apple.driver.AppleBiometricSensor`

```diff

-288.0.0.0.0
-  __TEXT.__cstring: 0x3402 sha256:738990e12b6c24418255fc36da4b01682fe2ec012a6e175e9838c67c7ea9fb8c
-  __TEXT.__os_log: 0xa877 sha256:4d6dd7558ff103fe63c3b2dd37439a9582c05cd9a5fe7b9bb5f597203b5383a5
+289.0.0.0.0
+  __TEXT.__cstring: 0x33ec sha256:3abac44124e844b8a67f8facf8d801fe879222484a6238058f5f27e981da7605
+  __TEXT.__os_log: 0xa877 sha256:8e58cbd08057abad8460eb9856df4597ec7b47ffc59791c8429564693d580668
   __TEXT.__const: 0x44c sha256:5d6e2a195396b5525f489c6ac5cc943d553e6e8b917f9ab1461f1b34a66b78b4
-  __TEXT_EXEC.__text: 0x2357c sha256:611023dd94a005421520e2d2d766379b531b0ab9322864f2ae604ecbac55a1a8
-  __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x188 sha256:7694b577bb968fbba8ea6c553a0e065dacf4311eb5932f47c4aaddeb6ac9e133
+  __TEXT_EXEC.__text: 0x23534 sha256:2f1c5432f29599ec74fb2c2447c8a1ae7fee4f8088992c5ddcc987f702774a24
+  __TEXT_EXEC.__auth_stubs: 0x5a0 sha256:d36bcbdc34a01704cd7c43a8a410af56d62a67e3acacbec9920fe49818c3d0aa
+  __DATA.__data: 0x188 sha256:9facfbbdd161ef9e5b43c18514883edadeeb5f3eb9d40ca01c89493171d0b7f4
   __DATA.__common: 0x1c8 sha256:b960fb5cb94682dfc4a873035d65f8befdcb9bed0e7db0feb905f0dcf437b38c
-  __DATA_CONST.__mod_init_func: 0x38 sha256:8fa483155985a23c8974ce17ce2a3f4d5dc9d6df1d65c136e3ac3d802e6e7122
-  __DATA_CONST.__mod_term_func: 0x38 sha256:dbd7e5b16cb9dcde097defacac963af48b7eb29aad83f0a2283600bf8ed6996a
-  __DATA_CONST.__const: 0x5ff8 sha256:dfab26104df90199c1065984aa3a85302270f823af3514f0193bb60ac2e9dd75
-  __DATA_CONST.__kalloc_type: 0x3c0 sha256:18803f36de3fc94662f07fe0c343dfe1130bcf4e62978ca7147e0d28d1e3848e
-  __DATA_CONST.__auth_got: 0x2c8 sha256:3f71599bcae73c8b5f2876493893be2505a607c3929c171d88fa6d53dddffba6
-  __DATA_CONST.__got: 0xa0 sha256:fd37dca9ca039690fd92fc1d6917a0712dca2294f7b2bd847739150d84849124
-  UUID: 9524AA6A-CAFF-3D2E-8CE4-3F10F9AB0129
-  Functions: 927
-  Symbols:   2766
-  CStrings:  783
+  __DATA_CONST.__mod_init_func: 0x38 sha256:58eb44f1930deffe2c6d5d1bca43db2e2ff257447e433954610600cdb8d80768
+  __DATA_CONST.__mod_term_func: 0x38 sha256:0ec1a2e09680e1cad29131fb67e4ee4ce494cccfca762f1c9ad35b29a2955564
+  __DATA_CONST.__const: 0x5ff8 sha256:fac48ea961b758ab6eb02fb91e426d130f2f88196efd1152f5bfaa951098174d
+  __DATA_CONST.__kalloc_type: 0x3c0 sha256:5f7683191ff1fc3639f5f98624ac6c8e8905ca15f0065971ac4a92e2e58d5eb5
+  __DATA_CONST.__auth_got: 0x2d0 sha256:059412719aa6a0bb783cc8b0abfeaf297f3748b144ce986de114331da1a18103
+  __DATA_CONST.__got: 0xa0 sha256:b7a5a46949a0ddb0c0ee3bcc4a3d902b9be00555dca36af060134670d884a56b
+  UUID: 5145A42D-0652-3DAB-9F4B-6344E550B3E2
+  Functions: 931
+  Symbols:   2772
+  CStrings:  784
 
Symbols:
+ _IODelay
+ _ZN9AppleMesa15handleInterruptEv.cold.5
+ _ZN9AppleMesa16_handleInterruptEv.cold.5
+ _ZN9AppleMesa16_handleInterruptEv.cold.6
+ _ZN9AppleMesa16_handleInterruptEv.cold.7
+ _ZN9AppleMesa16_handleInterruptEv.cold.8
+ __ZZN9AppleMesa15handleInterruptEvE11_os_log_fmt_2
+ __ZZN9AppleMesa20dispatchCaptureReadyEP18IOMemoryDescriptoryyE21kalloc_type_view_7101
+ __ZZN9AppleMesa20dispatchCaptureReadyEP18IOMemoryDescriptoryyE21kalloc_type_view_7117
+ __ZZZN9AppleMesa16_handleInterruptEvENK3$_0clEvE11_os_log_fmt
+ __ZZZN9AppleMesa16_handleInterruptEvENK3$_0clEvE11_os_log_fmt_0
+ __ZZZN9AppleMesa16_handleInterruptEvENK3$_0clEvE11_os_log_fmt_1
+ __ZZZN9AppleMesa16_handleInterruptEvENK3$_0clEvE11_os_log_fmt_2
+ __block_descriptor_tmp.268
- _ZN9AppleMesa19refreshSensorStatusEb.cold.34
- __ZZN9AppleMesa16_handleInterruptEvE11_os_log_fmt_2
- __ZZN9AppleMesa16_handleInterruptEvE11_os_log_fmt_3
- __ZZN9AppleMesa16_handleInterruptEvE11_os_log_fmt_4
- __ZZN9AppleMesa19refreshSensorStatusEbE11_os_log_fmt_5
- __ZZN9AppleMesa20dispatchCaptureReadyEP18IOMemoryDescriptoryyE21kalloc_type_view_7088
- __ZZN9AppleMesa20dispatchCaptureReadyEP18IOMemoryDescriptoryyE21kalloc_type_view_7104
- __block_descriptor_tmp.269
CStrings:
+ "%s: Corrupted sensor status"
+ "%s: Sensor with patch loaded but in bootROM"
+ "%s: Unexpected reset (watchdog)"
+ "/AppleInternal/Library/BuildRoots/4~CR6kugC-NC27zT8OPQIYIeAQPM7e_EmD8kd94ko/Library/Caches/com.apple.xbs/TemporaryDirectory.cNme6S/Sources/AppleBiometricSensor/ABSLogging.c"
+ "/AppleInternal/Library/BuildRoots/4~CR6kugC-NC27zT8OPQIYIeAQPM7e_EmD8kd94ko/Library/Caches/com.apple.xbs/TemporaryDirectory.cNme6S/Sources/AppleBiometricSensor/AppleMesa.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CR6kugC-NC27zT8OPQIYIeAQPM7e_EmD8kd94ko/Library/Caches/com.apple.xbs/TemporaryDirectory.cNme6S/Sources/AppleBiometricSensor/AppleMesaResources.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CR6kugC-NC27zT8OPQIYIeAQPM7e_EmD8kd94ko/Library/Caches/com.apple.xbs/TemporaryDirectory.cNme6S/Sources/AppleBiometricSensor/AppleSPIBiometricSensor.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CR6kugC-NC27zT8OPQIYIeAQPM7e_EmD8kd94ko/Library/Caches/com.apple.xbs/TemporaryDirectory.cNme6S/Sources/AppleBiometricSensor/AppleSandDollar.cpp"
- "%s: sensor with patch loaded but in bootROM"
- "/AppleInternal/Library/BuildRoots/4~CQl5ugAYQFdV5Yxms2cArq5_LGzJIkSiEezvY0c/Library/Caches/com.apple.xbs/TemporaryDirectory.nwPRcL/Sources/AppleBiometricSensor/ABSLogging.c"
- "/AppleInternal/Library/BuildRoots/4~CQl5ugAYQFdV5Yxms2cArq5_LGzJIkSiEezvY0c/Library/Caches/com.apple.xbs/TemporaryDirectory.nwPRcL/Sources/AppleBiometricSensor/AppleMesa.cpp"
- "/AppleInternal/Library/BuildRoots/4~CQl5ugAYQFdV5Yxms2cArq5_LGzJIkSiEezvY0c/Library/Caches/com.apple.xbs/TemporaryDirectory.nwPRcL/Sources/AppleBiometricSensor/AppleMesaResources.cpp"
- "/AppleInternal/Library/BuildRoots/4~CQl5ugAYQFdV5Yxms2cArq5_LGzJIkSiEezvY0c/Library/Caches/com.apple.xbs/TemporaryDirectory.nwPRcL/Sources/AppleBiometricSensor/AppleSPIBiometricSensor.cpp"
- "/AppleInternal/Library/BuildRoots/4~CQl5ugAYQFdV5Yxms2cArq5_LGzJIkSiEezvY0c/Library/Caches/com.apple.xbs/TemporaryDirectory.nwPRcL/Sources/AppleBiometricSensor/AppleSandDollar.cpp"
- "messagingResult == 0 "

```
