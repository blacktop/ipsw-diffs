## libnfrestore.dylib

> `/usr/lib/libnfrestore.dylib`

```diff

-353.3.0.0.0
-  __TEXT.__text: 0x14960
-  __TEXT.__auth_stubs: 0xc30
+354.27.0.0.0
+  __TEXT.__text: 0x14cc0
+  __TEXT.__auth_stubs: 0xc60
   __TEXT.__const: 0x70
-  __TEXT.__cstring: 0x3039
-  __TEXT.__oslogstring: 0x23ed
+  __TEXT.__cstring: 0x3058
+  __TEXT.__oslogstring: 0x2417
   __TEXT.__unwind_info: 0x1f0
   __DATA_CONST.__got: 0xb0
   __DATA_CONST.__const: 0x1c8
-  __AUTH_CONST.__auth_got: 0x618
+  __AUTH_CONST.__auth_got: 0x630
   __AUTH_CONST.__const: 0x180
   __AUTH_CONST.__cfstring: 0x660
   __DATA.__bss: 0x18

   - /usr/lib/libPN548_API.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libnfshared.dylib
-  UUID: CE5C2FFD-6C8A-35E7-8F18-C06E17DDC233
-  Functions: 133
-  Symbols:   380
-  CStrings:  720
+  UUID: 697242F2-B271-319F-9090-E4695A67A0A6
+  Functions: 135
+  Symbols:   388
+  CStrings:  722
 
Symbols:
+ _NFDriverInvalidateProhibitTimer
+ _NFHardwareInterfaceEnableLog
+ _NFHardwareSerialDebugLogEnable
+ _NFHardwareSerialEnableLog
+ _NFRestoreNfcFirmwareNameForController
+ _NfRestoreInvalidateProhibitTimer
+ _memset
+ _strncpy
CStrings:
+ "%s:%i Found exact plist match: %s"
+ "%{public}s:%i Found exact plist match: %s"
+ "((NFHardwareSerialInternal*)(serial->internal))->currentWriteBuffer == ((void*)0)"
+ "SE310S_FW_A0_01_01_2B_rev156564.bin"
+ "SE310S_FW_A0_01_01_CB_rev156588.bin"
+ "SN100V_FW_A3_01_01_AE_rev157440.bin"
+ "SN200V_FW_B1_02_01_AF_rev157437.bin"
+ "SN300V_FW_B0_02_01_64_rev157348.bin"
+ "SN300V_FW_B0_02_01_F2_rev156582.bin"
+ "buffer!=((void*)0)"
+ "devicePath != ((void*)0)"
- "((NFHardwareSerialInternal*)(serial->internal))->currentWriteBuffer == ((void *)0)"
- "SE310S_FW_A0_01_01_20_rev151695.bin"
- "SE310S_FW_A0_01_01_BE_rev150106.bin"
- "SN100V_FW_A3_01_01_AB_rev155589.bin"
- "SN200V_FW_B1_02_01_AC_rev155587.bin"
- "SN300V_FW_B0_02_01_5E_rev156662.bin"
- "SN300V_FW_B0_02_01_EE_rev152118.bin"
- "buffer!=((void *)0)"
- "devicePath != ((void *)0)"

```
