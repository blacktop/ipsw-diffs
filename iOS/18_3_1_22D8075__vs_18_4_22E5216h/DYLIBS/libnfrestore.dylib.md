## libnfrestore.dylib

> `/usr/lib/libnfrestore.dylib`

```diff

-353.4.0.0.0
-  __TEXT.__text: 0x17e40
-  __TEXT.__auth_stubs: 0xcb0
+354.25.0.0.0
+  __TEXT.__text: 0x180e0
+  __TEXT.__auth_stubs: 0xcd0
   __TEXT.__const: 0x70
-  __TEXT.__cstring: 0x3879
-  __TEXT.__oslogstring: 0x28b8
-  __TEXT.__unwind_info: 0x220
+  __TEXT.__cstring: 0x3822
+  __TEXT.__oslogstring: 0x28e2
+  __TEXT.__unwind_info: 0x218
   __DATA_CONST.__got: 0xb0
   __DATA_CONST.__const: 0x218
-  __AUTH_CONST.__auth_got: 0x658
+  __AUTH_CONST.__auth_got: 0x668
   __AUTH_CONST.__auth_ptr: 0x10
   __AUTH_CONST.__const: 0x120
-  __AUTH_CONST.__cfstring: 0x960
+  __AUTH_CONST.__cfstring: 0x940
   __DATA.__bss: 0x18
   __DATA.__common: 0x28
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libPN548_API.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libnfshared.dylib
-  Functions: 150
-  Symbols:   376
-  CStrings:  780
+  Functions: 151
+  Symbols:   382
+  CStrings:  777
 
Symbols:
+ _NFDriverInvalidateProhibitTimer
+ _NFHardwareInterfaceEnableLog
+ _NFHardwareSerialDebugLogEnable
+ _NFHardwareSerialEnableLog
+ _NfRestoreInvalidateProhibitTimer
+ _memset
+ _strncpy
- _CFPreferencesSetAppValue
CStrings:
+ "%s:%i Found exact plist match: %s"
+ "%{public}s:%i Found exact plist match: %s"
+ "((NFHardwareSerialInternal*)(serial->internal))->currentWriteBuffer == ((void*)0)"
+ "SE310S_FW_A0_01_01_2B_rev156564.bin"
+ "SE310S_FW_A0_01_01_CB_rev156588.bin"
+ "SN100V_FW_A3_01_01_AE_rev157440.bin"
+ "SN200V_FURY_FW_B1_02_01_A7_rev157243.bin"
+ "SN200V_FW_B1_02_01_AF_rev157437.bin"
+ "SN300V_FW_B0_02_01_64_rev157348.bin"
+ "SN300V_FW_B0_02_01_F2_rev156582.bin"
+ "buffer!=((void*)0)"
+ "devicePath != ((void*)0)"
- "((NFHardwareSerialInternal*)(serial->internal))->currentWriteBuffer == ((void *)0)"
- "FailForwardDetectedTimestamp"
- "FailForwardInProgress"
- "FailForwardLastAttemptTimestamp"
- "FailForwardNeeded"
- "SE310S_FW_A0_01_01_20_rev151695.bin"
- "SE310S_FW_A0_01_01_BE_rev150106.bin"
- "SN100V_FW_A3_01_01_AB_rev155589.bin"
- "SN200V_FURY_FW_B1_02_01_A2_rev150255.bin"
- "SN200V_FW_B1_02_01_AC_rev155587.bin"
- "SN300V_FW_B0_02_01_5E_rev156662.bin"
- "SN300V_FW_B0_02_01_EE_rev152118.bin"
- "buffer!=((void *)0)"
- "com.apple.nfcacd"
- "devicePath != ((void *)0)"

```
