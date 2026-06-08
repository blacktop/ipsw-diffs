## libNFC_HAL.dylib

> `/usr/lib/libNFC_HAL.dylib`

```diff

-365.3.1.0.0
-  __TEXT.__text: 0x19274
-  __TEXT.__auth_stubs: 0x7c0
-  __TEXT.__const: 0x130
-  __TEXT.__cstring: 0x2e37
-  __TEXT.__oslogstring: 0x257d
-  __TEXT.__unwind_info: 0x258
-  __DATA_CONST.__got: 0x70
+370.33.1.0.0
+  __TEXT.__text: 0x180a0
+  __TEXT.__const: 0x120
+  __TEXT.__cstring: 0x2e33
+  __TEXT.__oslogstring: 0x2570
+  __TEXT.__unwind_info: 0x250
+  __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x268
-  __AUTH_CONST.__auth_got: 0x3e0
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x100
-  __AUTH_CONST.__cfstring: 0x380
-  __DATA_DIRTY.__data: 0x1
+  __AUTH_CONST.__cfstring: 0x360
+  __AUTH_CONST.__auth_got: 0x0
+  __DATA_DIRTY.__data: 0x2
   __DATA_DIRTY.__bss: 0x248
   __DATA_DIRTY.__common: 0x28
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libnfshared.dylib
-  UUID: 93AF3F23-E5B9-37D4-A4D4-03630F9D2800
-  Functions: 180
-  Symbols:   275
-  CStrings:  674
+  UUID: 4F7610C1-9281-3BAF-983F-158A631B4D0C
+  Functions: 178
+  Symbols:   273
+  CStrings:  676
 
Symbols:
+ _NFHardwareGPIOSetPowerToggle
+ _NFHardwareInterfaceSetPowerToggle
+ _postAnalyticsResetTimingEvent
- _NFHardwareInterfaceIsHammerfestAlive
- _NFHardwareInterfaceRead
- _NFHardwareInterfaceReadAbort
- _NFHardwareInterfaceWrite
- _NFHardwareSerialIsHammerfestAlive
CStrings:
+ "%s:%i enable toggle=%llu"
+ "%{public}s:%i enable toggle=%llu"
+ "NFHardwareGPIOSetPowerToggle"
+ "_phTmlNfc_PowerToggle"
+ "download_mode"
+ "download_mode_no_ven"
+ "normal_mode"
+ "normal_mode_no_ven"
+ "power_off"
+ "spmi_follower_reset"
- "%s:%i Using blocking socket for relay"
- "%{public}s:%i Using blocking socket for relay"
- "NFHardwareInterfaceRead"
- "NFHardwareSerialIsHammerfestAlive"
- "hammerfest-data-available-event"
- "nfc,secondary,spmi"
- "phTmlNfc_ConfigureTestParams"

```
