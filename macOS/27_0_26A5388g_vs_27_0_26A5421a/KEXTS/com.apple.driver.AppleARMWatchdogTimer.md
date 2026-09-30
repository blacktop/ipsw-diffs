## com.apple.driver.AppleARMWatchdogTimer

> `com.apple.driver.AppleARMWatchdogTimer`

```diff

-334.0.3.0.0
-  __TEXT.__cstring: 0x15d8
-  __TEXT_EXEC.__text: 0x5dec
+334.0.4.0.0
+  __TEXT.__cstring: 0x167d
+  __TEXT_EXEC.__text: 0x5ea8
   __TEXT_EXEC.__auth_stubs: 0x590
   __DATA.__data: 0x118
   __DATA.__common: 0x110

   __DATA_CONST.__kalloc_var: 0x190
   __DATA_CONST.__auth_got: 0x2c8
   __DATA_CONST.__got: 0xc0
-  Functions: 219
-  Symbols:   702
-  CStrings:  145
+  Functions: 220
+  Symbols:   703
+  CStrings:  147
 
Symbols:
+ __ZNK10IOWatchdog34getNestedPanicAPWDPromotionEnabledEv
+ __ZZN21AppleARMWatchdogTimer5startEP9IOServiceE20kalloc_type_view_376
+ __ZZN21AppleARMWatchdogTimer5startEP9IOServiceE20kalloc_type_view_381
+ __ZZN21AppleARMWatchdogTimer5startEP9IOServiceE20kalloc_type_view_383
+ __ZZN21AppleARMWatchdogTimer5startEP9IOServiceE20kalloc_type_view_404
+ __ZZN21AppleARMWatchdogTimer5startEP9IOServiceE20kalloc_type_view_409
- __ZZN21AppleARMWatchdogTimer5startEP9IOServiceE20kalloc_type_view_358
- __ZZN21AppleARMWatchdogTimer5startEP9IOServiceE20kalloc_type_view_363
- __ZZN21AppleARMWatchdogTimer5startEP9IOServiceE20kalloc_type_view_365
- __ZZN21AppleARMWatchdogTimer5startEP9IOServiceE20kalloc_type_view_386
- __ZZN21AppleARMWatchdogTimer5startEP9IOServiceE20kalloc_type_view_391
Functions:
~ __ZN21AppleARMWatchdogTimer5startEP9IOService : 4648 -> 4684
~ __ZN21AppleARMWatchdogTimer20_handlePEHaltRestartEj : 712 -> 812
~ __ZN10IOWatchdog5startEP9IOServiceyy : 1484 -> 1520
+ __ZNK10IOWatchdog34getNestedPanicAPWDPromotionEnabledEv
CStrings:
+ "AppleARMWatchdogTimer::start: _wdtBaseAddress: %#lx _wdtResetCount=%#x _SMCWatchdogAvailable=%d\n"
+ "wdog: Nested panic detected: APWD promotion disabled, system will reset shortly...\n"
+ "wdog: Nested panic detected: attempting to promote this panic to an APWD report...\n"
+ "wdog: panic chipreset\n"
+ "wdog: restart\n"
- "AppleARMWatchdogTimer::start: _wdtBaseAddress: %#lx _wdtResetCount=%#x _useSMCEnforcedWatchdog=%d\n"
- "wdog panic (attempt %d)\n"
- "wdog restart\n"
```
