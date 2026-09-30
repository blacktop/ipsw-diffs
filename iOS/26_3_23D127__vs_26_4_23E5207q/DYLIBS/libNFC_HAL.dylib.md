## libNFC_HAL.dylib

> `/usr/lib/libNFC_HAL.dylib`

```diff

-363.10.0.0.0
-  __TEXT.__text: 0x18f04
+364.20.0.0.0
+  __TEXT.__text: 0x19274
   __TEXT.__auth_stubs: 0x7c0
-  __TEXT.__const: 0x120
-  __TEXT.__cstring: 0x2de5
-  __TEXT.__oslogstring: 0x2521
-  __TEXT.__unwind_info: 0x240
+  __TEXT.__const: 0x130
+  __TEXT.__cstring: 0x2e37
+  __TEXT.__oslogstring: 0x257d
+  __TEXT.__unwind_info: 0x258
   __DATA_CONST.__got: 0x70
   __DATA_CONST.__const: 0x268
   __AUTH_CONST.__auth_got: 0x3e0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libnfshared.dylib
-  UUID: 54DAB3E9-293F-3F86-89D7-FF932C79EEA2
-  Functions: 176
+  UUID: F114986D-1F35-333C-A2F3-5BC69CC0CAA5
+  Functions: 180
   Symbols:   275
   CStrings:  674
 
Symbols:
+ _NFHardwareCopyHWConfigTLVs
+ _NFHardwareCopyRFConfigTLVs
+ _phTmlNfc_ConfigureTestParams
- _NFHardwareGetRFConfigTLVs
- _NFHardwareSupportedSecureTimersInOff
- _phOsalNfc_GetMemory
CStrings:
+ "%s:%i SPMI registers -- 0x%02X = 0x%02X, 0x%02X = 0x%02X, 0x%02X = 0x%02X, 0x%02X = 0x%02X, 0x%02X = 0x%02X"
+ "%s:%i Unmapped SPMI register 0x%02X = 0x%02X"
+ "%{public}s:%i SPMI registers -- 0x%02X = 0x%02X, 0x%02X = 0x%02X, 0x%02X = 0x%02X, 0x%02X = 0x%02X, 0x%02X = 0x%02X"
+ "%{public}s:%i Unmapped SPMI register 0x%02X = 0x%02X"
+ "NFHardwareCopyHWConfigTLVs"
+ "NFHardwareCopyRFConfigTLVs"
+ "_NFHardwareCopyConfigTLV"
+ "hw-config-tlvs"
+ "phTmlNfc_ConfigureTestParams"
- "%s:%i Creating IONotificationPort for %s"
- "%s:%i Invalid timer"
- "%{public}s:%i Creating IONotificationPort for %s"
- "%{public}s:%i Invalid timer"
- "NFHardwareGetRFConfigTLVs"
- "NFHardwareSupportedSecureTimersInOff"
- "_NFHardwareGetRFConfigTLV"
- "_phOsalNfc_Timer_ClearTimer"
- "se-lpem-enabled"

```
