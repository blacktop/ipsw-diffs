## com.apple.driver.AppleARMWatchdogTimer

> `com.apple.driver.AppleARMWatchdogTimer`

```diff

-334.0.3.0.0
-  __TEXT.__cstring: 0x135a
-  __TEXT_EXEC.__text: 0x5378
+334.0.4.0.0
+  __TEXT.__cstring: 0x13ff
+  __TEXT_EXEC.__text: 0x5434
   __TEXT_EXEC.__auth_stubs: 0x530
   __DATA.__data: 0x118
   __DATA.__common: 0xe8

   __DATA_CONST.__kalloc_var: 0x190
   __DATA_CONST.__auth_got: 0x298
   __DATA_CONST.__got: 0xb8
-  Functions: 188
+  Functions: 189
   Symbols:   0
-  CStrings:  126
+  CStrings:  128
 
Functions:
~ __ZN21AppleARMWatchdogTimer5startEP9IOService : 4224 -> 4260
~ __ZN21AppleARMWatchdogTimer20_handlePEHaltRestartEj : 668 -> 768
~ __ZN10IOWatchdog5startEP9IOServiceyy : 1164 -> 1200
+ sub_fffffe0008689d40
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
