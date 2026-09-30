## libnfrestore.dylib

> `/usr/lib/libnfrestore.dylib`

```diff

-363.10.0.0.0
-  __TEXT.__text: 0xd6d8
-  __TEXT.__auth_stubs: 0x9b0
+364.20.0.0.0
+  __TEXT.__text: 0xd5c4
+  __TEXT.__auth_stubs: 0x950
   __TEXT.__const: 0x88
-  __TEXT.__cstring: 0x21ee
-  __TEXT.__oslogstring: 0x194e
+  __TEXT.__cstring: 0x21c4
+  __TEXT.__oslogstring: 0x18fe
   __TEXT.__unwind_info: 0x118
-  __DATA_CONST.__got: 0x80
+  __DATA_CONST.__got: 0x78
   __DATA_CONST.__const: 0x30
-  __AUTH_CONST.__auth_got: 0x4d8
-  __AUTH_CONST.__cfstring: 0x6e0
+  __AUTH_CONST.__auth_got: 0x4a8
+  __AUTH_CONST.__cfstring: 0x6c0
   __DATA.__bss: 0x18
   __DATA.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libPN548_API.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libnfshared.dylib
-  UUID: 54A78641-11A8-306C-B315-4FE0CFF1C1A6
-  Functions: 52
-  Symbols:   191
-  CStrings:  556
+  UUID: 7153A2DC-7F8E-39AF-8DBF-85FD7A05970C
+  Functions: 53
+  Symbols:   184
+  CStrings:  551
 
Symbols:
+ _NFDriverGetGlobalError
+ _NFDriverHWSettingsSetup
+ _NFDriverUpdateGlobalError
- _NFDriverConfigurRSTNDelay
- _NFDriverConfigureI2CForLPM
- _NFDriverInvalidateProhibitTimer
- _NFGetProductType
- _NFProductIsMac
- _NFProductIsPad
- _NFProductIsVision
- ___sprintf_chk
- _nfc_err
- _sprintf
CStrings:
+ "%s:%i Currently running version 0x%04X, rev %d"
+ "%s:%i Failed to configure EDT settings : 0x%x"
+ "%s:%i Failed to configure HW Settings: %d"
+ "%s:%i Feature not supported"
+ "%{public}s:%i Currently running version 0x%04X, rev %d"
+ "%{public}s:%i Failed to configure EDT settings : 0x%x"
+ "%{public}s:%i Failed to configure HW Settings: %d"
+ "%{public}s:%i Feature not supported"
+ "0123456789ABCDEF"
+ "NfRestoreInvalidateProhibitTimer"
+ "SE310S_FW_A0_01_01_37_rev170509.bin"
+ "SN200V_FURY_FW_B1_02_01_AF_rev171073.bin"
+ "SN200V_FURY_FW_B1_02_01_FA_rev149466.bin"
+ "SN300V_FW_B0_02_01_7E_rev171089.bin"
+ "SN300V_FW_B0_02_01_FC_rev167600.bin"
+ "_NFRestoreConfigureHWSettings"
+ "nfrestore: %s\n"
- "%s:%i Configuring I2C for LPM..."
- "%s:%i Configuring RSTN delay..."
- "%s:%i Failed to configure I2C for LPM.."
- "%s:%i Failed to configure I2C for LPM: %d"
- "%s:%i Failed to configure RSTN delay.."
- "%s:%i Failed to configure RSTN delay: %d"
- "%{public}s:%i Configuring I2C for LPM..."
- "%{public}s:%i Configuring RSTN delay..."
- "%{public}s:%i Failed to configure I2C for LPM.."
- "%{public}s:%i Failed to configure I2C for LPM: %d"
- "%{public}s:%i Failed to configure RSTN delay.."
- "%{public}s:%i Failed to configure RSTN delay: %d"
- "0x%02X "
- "LogAPI"
- "SE310S_FW_A0_01_01_33_rev165162.bin"
- "SN200V_FURY_FW_B1_02_01_A9_rev169850.bin"
- "SN200V_FURY_FW_B1_02_01_FA_rev170017.bin"
- "SN300V_FW_B0_02_01_74_rev167804.bin"
- "SN300V_FW_B0_02_01_C9_rev167976.bin"
- "_NFRestoreConfigureI2CForLPM"
- "_NFRestoreConfigureRSTNDelay"

```
