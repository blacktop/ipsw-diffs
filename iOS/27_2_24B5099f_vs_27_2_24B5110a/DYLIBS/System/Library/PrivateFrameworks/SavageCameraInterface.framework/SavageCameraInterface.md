## SavageCameraInterface

> `/System/Library/PrivateFrameworks/SavageCameraInterface.framework/SavageCameraInterface`

```diff

-10.61.0.0.0
-  __TEXT.__text: 0x2a58
-  __TEXT.__const: 0xc0
+10.66.0.0.0
+  __TEXT.__text: 0x38e0
+  __TEXT.__const: 0xd0
   __TEXT.__gcc_except_tab: 0x68
-  __TEXT.__cstring: 0x67e
-  __TEXT.__oslogstring: 0x4a4
-  __TEXT.__unwind_info: 0xc8
+  __TEXT.__cstring: 0x88b
+  __TEXT.__oslogstring: 0x6bb
+  __TEXT.__unwind_info: 0xd0
   __TEXT.__auth_stubs: 0x0
-  __DATA_CONST.__const: 0x78
+  __DATA_CONST.__const: 0x808
   __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x20
-  __AUTH_CONST.__cfstring: 0x2c0
+  __AUTH_CONST.__cfstring: 0x2e0
   __AUTH_CONST.__weak_auth_got: 0x10
-  __AUTH_CONST.__auth_got: 0x1b8
+  __AUTH_CONST.__auth_got: 0x210
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libFDR.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 18
-  Symbols:   100
-  CStrings:  97
+  Functions: 20
+  Symbols:   115
+  CStrings:  136
 
Symbols:
+ _CFEqual
+ _CFStringCreateWithCString
+ _IORegistryEntryFromPath
+ _SavageCamInterfaceCheckPersonalizationStatus
+ _SavageCamInterfaceExtractUID
+ __ZL19kDeviceChannelsInfo
+ __ZZ28SavageCamInterfaceExtractUIDE7yeidTag
+ _close
+ _free
+ _fstat
+ _glob
+ _globfree
+ _malloc_type_malloc
+ _open
+ _read
CStrings:
+ "%02x"
+ "%s: Extracted UID = %s from %s\n"
+ "%s: Failed to extract UID from %s File\n"
+ "%s: Failed to open %s\n"
+ "%s: Failed to read %s\n"
+ "%s: IOReg UID property for %s channel : %s = %s\n"
+ "%s: Malformed or unexpected-length 'yeid' value, returning\n"
+ "%s: No %s File found or not permitted to read\n"
+ "%s: No current UID published in IORegistry for %s\n"
+ "%s: Re-personalization detection is not supported for this Platform\n"
+ "%s: Unable to read platform ID from /arm-io/isp : node missing, property missing, or access denied)\n"
+ "%s: channel=%s personalizationState=%s\n"
+ "/private/preboot/*/usr/standalone/firmware/%s"
+ "FRONT_CAMERA"
+ "FRONT_CAMERA_RENO"
+ "FRONT_CAMERA_SWIDE"
+ "FRONT_INFRARED"
+ "IODeviceTree:/arm-io/isp"
+ "NO_CAMERA"
+ "NeedsPersonalization"
+ "Personalized"
+ "REAR_CAMERA"
+ "REAR_CAMERA_SWIDE"
+ "REAR_CAMERA_TELE"
+ "REAR_INFRARED"
+ "REAR_JASPER"
+ "Savage/SavagePatch.DER"
+ "SavageCamInterfaceCheckPersonalizationStatus"
+ "SavageCamInterfaceExtractUID"
+ "SavageUID"
+ "UNKNOWN_CHANNEL"
+ "Unknown"
+ "Yonkers/YonkersPatch.DER"
+ "YonkersIR/YonkersIR1Patch.DER"
+ "YonkersIR/YonkersIR2Patch.DER"
+ "YonkersIR1UID"
+ "YonkersIR2UID"
+ "YonkersUID"
+ "sensor-type"
```
