## com.apple.driver.AppleThunderboltUSBDownAdapter

> `com.apple.driver.AppleThunderboltUSBDownAdapter`

```diff

-122.0.0.0.0
+124.0.0.0.0
   __TEXT.__cstring: 0x2e6
-  __TEXT_EXEC.__text: 0x10d0
+  __TEXT.__os_log: 0x283
+  __TEXT_EXEC.__text: 0x1378
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x38
-  __DATA_CONST.__auth_got: 0x78
-  __DATA_CONST.__got: 0x28
+  __DATA_CONST.__auth_got: 0x80
+  __DATA_CONST.__got: 0x30
   __DATA_CONST.__mod_init_func: 0x8
   __DATA_CONST.__mod_term_func: 0x8
   __DATA_CONST.__const: 0xbc8
   __DATA_CONST.__kalloc_type: 0x40
-  UUID: 2C6EB55F-59D0-3C68-B75E-3961B30B79B7
+  UUID: FBD445B0-4D36-3A96-A9B3-396E7251057E
   Functions: 33
-  Symbols:   406
-  CStrings:  13
+  Symbols:   417
+  CStrings:  22
 
Symbols:
+ __ZZN30AppleThunderboltUSBDownAdapter13enableAdapterEbE11_os_log_fmt
+ __ZZN30AppleThunderboltUSBDownAdapter15createResourcesEvE11_os_log_fmt
+ __ZZN30AppleThunderboltUSBDownAdapter20setThunderboltClientEP28AppleThunderboltUSBUpAdapterE11_os_log_fmt
+ __ZZN30AppleThunderboltUSBDownAdapter4freeEvE11_os_log_fmt
+ __ZZN30AppleThunderboltUSBDownAdapter5startEP9IOServiceE11_os_log_fmt
+ __ZZN30AppleThunderboltUSBDownAdapter5startEP9IOServiceE11_os_log_fmt_0
+ __ZZN30AppleThunderboltUSBDownAdapter8finalizeEjE11_os_log_fmt
+ __ZZN30AppleThunderboltUSBDownAdapter9earlyWakeEvE11_os_log_fmt
+ __ZZN30AppleThunderboltUSBDownAdapter9lateSleepEvE11_os_log_fmt
+ __os_log_default
+ __os_log_internal
Functions:
~ __ZN30AppleThunderboltUSBDownAdapter5startEP9IOService : 964 -> 1148
~ __ZN30AppleThunderboltUSBDownAdapter8finalizeEj : 320 -> 392
~ __ZN30AppleThunderboltUSBDownAdapter4freeEv : 252 -> 336
~ __ZN30AppleThunderboltUSBDownAdapter15createResourcesEv : 236 -> 328
~ __ZN30AppleThunderboltUSBDownAdapter20setThunderboltClientEP28AppleThunderboltUSBUpAdapter : 452 -> 464
~ __ZN30AppleThunderboltUSBDownAdapter13enableAdapterEb : 564 -> 640
~ __ZN30AppleThunderboltUSBDownAdapter9lateSleepEv : 272 -> 352
~ __ZN30AppleThunderboltUSBDownAdapter9earlyWakeEv : 272 -> 352

```
