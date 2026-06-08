## SavageCameraInterface

> `/System/Library/PrivateFrameworks/SavageCameraInterface.framework/SavageCameraInterface`

```diff

-10.53.1.0.0
-  __TEXT.__text: 0x1e3c
-  __TEXT.__auth_stubs: 0x260
-  __TEXT.__const: 0x84
-  __TEXT.__gcc_except_tab: 0xd4
-  __TEXT.__cstring: 0x4cc
-  __TEXT.__oslogstring: 0x322
-  __TEXT.__unwind_info: 0xe0
-  __DATA_CONST.__got: 0x50
+10.59.0.0.0
+  __TEXT.__text: 0x28c4
+  __TEXT.__const: 0xc0
+  __TEXT.__gcc_except_tab: 0x68
+  __TEXT.__cstring: 0x67e
+  __TEXT.__oslogstring: 0x422
+  __TEXT.__unwind_info: 0xc0
+  __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x78
-  __AUTH_CONST.__auth_got: 0x138
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x20
-  __AUTH_CONST.__cfstring: 0x20
+  __AUTH_CONST.__cfstring: 0x2c0
+  __AUTH_CONST.__weak_auth_got: 0x10
+  __AUTH_CONST.__auth_got: 0x1b8
+  __DATA.__bss: 0x1000
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
+  - /usr/lib/libFDR.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 4BBB113C-AE55-382D-97E1-8B07D578033D
-  Functions: 17
-  Symbols:   86
-  CStrings:  63
+  UUID: 7A3B51EE-58EC-3C67-99D7-E1DBF268F6E0
+  Functions: 18
+  Symbols:   107
+  CStrings:  117
 
Symbols:
+ _AMFDRCreateInstanceString
+ _AMFDRModuleCreateSignedCSR
+ _CFCopyDescription
+ _CFDataCreate
+ _CFDataGetTypeID
+ _CFDictionaryAddValue
+ _CFDictionaryContainsKey
+ _CFDictionaryCreateMutable
+ _CFDictionaryGetValue
+ _CFDictionaryGetValueIfPresent
+ _CFDictionarySetValue
+ _CFErrorCopyDescription
+ _CFRetain
+ _CFStringCreateWithFormat
+ _CFStringGetCString
+ _IORegistryEntryCreateCFProperty
+ __ZL14libFDRCallback18AMFDRCryptoVersionPK8__CFDataPS2_Pv
+ __ZL22CreateAuthICDeviceInfoPPK14__CFDictionary
+ __ZL9logString
+ ___block_descriptor_tmp.25
+ _kCFBooleanFalse
+ _kCFBooleanTrue
+ _kCFTypeDictionaryKeyCallBacks
+ _kCFTypeDictionaryValueCallBacks
+ _malloc_type_calloc
+ _snprintf
- GCC_except_table10
- GCC_except_table11
- GCC_except_table5
- GCC_except_table6
- _SavageCamInterfaceForgetISPFirmware
- ___block_descriptor_tmp.3
CStrings:
+ "\n AuthIC DAT File: %s \n"
+ " %02X "
+ " %s Releasing certificationOptions \n"
+ "%@-%@"
+ "%s \n"
+ "%s [CSR]: %s \n"
+ "%s [DAT File]: %s \n"
+ "%s [Output]: %s \n"
+ "%s [error]: %s \n"
+ "%s moduleDataInstanceStr: %s \n"
+ "%s: Could not find AppleCamera service\n"
+ "Auth challenge received from libFDR:--------------\n"
+ "AuthChallenge"
+ "Callback did not receive the input context. \n"
+ "CertifyChallengeSupport128b"
+ "CertifyComponentAttributesCriticalProductionMode"
+ "CertifyRawECDSASignature"
+ "CertifyRawPublicKey"
+ "CreateAuthICDATFile"
+ "CreateAuthICDeviceInfo"
+ "GetAuthICChallenge"
+ "No C string description available."
+ "ProvisioningMAC"
+ "RearCameraAuthICAuthResponse"
+ "RearCameraAuthICChipID"
+ "RearCameraAuthICMNS"
+ "RearCameraAuthICNonce"
+ "RearCameraAuthICProductionMode"
+ "RearCameraAuthICPubKey"
+ "RearCameraAuthICPubKeyHmac"
+ "RearCameraAuthICSignedCSR"
+ "RearCameraAuthICUID"
+ "SavageCamInterfaceRef"
+ "camChannel"
+ "pData"
+ "sensorType"
+ "villanova"
- "%s: Did we miss a sensor in the switch..case ??\n"
- "SavageCamInterfaceForgetISPFirmware"
- "SavageCamInterfaceSensorPreFusing"
- "SavageCamInterfaceSensorPrePersonalize"

```
