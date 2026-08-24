## com.apple.driver.AppleSPMIPMU

> `com.apple.driver.AppleSPMIPMU`

```diff

-1372.0.1.0.0
-  __TEXT.__const: 0x36
-  __TEXT.__cstring: 0x2c0d
-  __TEXT_EXEC.__text: 0xd614
+1372.0.3.0.0
+  __TEXT.__const: 0x16
+  __TEXT.__cstring: 0x2c1e
+  __TEXT_EXEC.__text: 0xd5a4
   __TEXT_EXEC.__auth_stubs: 0x4d0
   __DATA.__data: 0x320
   __DATA.__common: 0xe8
Functions:
~ __ZN18AppleDialogSPMIPMU13setPropertiesEP8OSObject : 4420 -> 4408
~ __ZN21AppleDialogSPMIPMURTC20_readRTCUpcountTicksEv : 956 -> 856
CStrings:
+ "%s::handleStart: %s _pmuNub: %p ** configuration not found ** built 21:39:19 Aug 11 2026\n"
+ "%s::handleStart: ro=%d nvram=%d helper=%d %s _pmuNub: %p 0x%04x:0x%04x-0x%04x built 21:39:19 Aug 11 2026\n"
+ "%s::start: %s _pmuNub: %p ** configuration not found ** built 21:39:20 Aug 11 2026\n"
+ "%s::start: %s _pmuNub: %p built 21:39:20 Aug 11 2026\n"
+ "Failed to read info-leg_scrpad\n"
+ "Failed to read info-rtc\n"
+ "Failed to read info-rtc_alarm_ctrl\n"
+ "Failed to read info-rtc_alarm_ctrl_en_mask\n"
+ "Failed to read info-rtc_alarm_event\n"
+ "Failed to read info-rtc_alarm_mask\n"
+ "Failed to read info-rtc_alarm_monitor_mask\n"
+ "Failed to read info-rtc_alarm_offset\n"
+ "Failed to read info-rtc_irq_mask_offset\n"
+ "PMU-LPM: LPEM control dictionary is uninitialized\n"
+ "RTC count backward detected (%08llXh -> %08llXh), or (%llu us -> %llu us)!\n"
+ "RTC upcountTicks=%08llx, regs=%02x:%02x:%02x:%02x:%02x:%02x (%x)\n"
+ "Read RTC offset from leg_scrpad\n"
+ "ULPM error (%x)\n"
+ "Unsupported Clock Offset Count (%hu)\n"
- "%s::%s upcountTicks=%08llx %02x:%02x:%02x:%02x:%02x:%02x (%x)\n"
- "%s::handleStart: %s _pmuNub: %p ** configuration not found ** built 21:21:11 Jul 14 2026\n"
- "%s::handleStart: ro=%d nvram=%d helper=%d %s _pmuNub: %p 0x%04x:0x%04x-0x%04x built 21:21:11 Jul 14 2026\n"
- "%s::start: %s _pmuNub: %p ** configuration not found ** built 21:21:12 Jul 14 2026\n"
- "%s::start: %s _pmuNub: %p built 21:21:12 Jul 14 2026\n"
- "Failed to read info-leg_scrpad"
- "Failed to read info-rtc"
- "Failed to read info-rtc_alarm_ctrl"
- "Failed to read info-rtc_alarm_ctrl_en_mask"
- "Failed to read info-rtc_alarm_event"
- "Failed to read info-rtc_alarm_mask"
- "Failed to read info-rtc_alarm_monitor_mask"
- "Failed to read info-rtc_alarm_offset"
- "Failed to read info-rtc_irq_mask_offset"
- "PMU-LPM: LPEM control dictionary is uninitialized"
- "RTC count backward detected (%08llXh -> %08llXh), or (%llu us -> %llu us)!"
- "Read RTC offset from leg_scrpad"
- "ULPM error (%x)"
- "Unsupported Clock Offset Count (%hu)"
```
