## SavageCameraInterface

> `/System/Library/PrivateFrameworks/SavageCameraInterface.framework/SavageCameraInterface`

```diff

-10.53.1.0.0
-  __TEXT.__text: 0x1e3c sha256:1c264efb2e327b10116099bee8f1f5bf576406b8bf79523b2dd3c1b24b521b6d
-  __TEXT.__auth_stubs: 0x260 sha256:0af3bded3ade28eb6df73467c2ba2cfd5992f50f90efea553ceeb9db117123f7
-  __TEXT.__const: 0x84 sha256:eaa044a4cb323e77c36eeb8468575367790398505e8a555e93d01e018379cdf9
-  __TEXT.__gcc_except_tab: 0xd4 sha256:c7ac3dd9165160cc4283dee8db86394c7d59ef85f90aeaace04c7b98b62793a7
-  __TEXT.__cstring: 0x4cc sha256:587f712cfcefe23e4f06d186c94ebb3f96a91dc96fe1212301ce2a8270d2b11b
-  __TEXT.__oslogstring: 0x322 sha256:13ff2ff53d77aca70622182868568ccc15603c13550dcdf0dfb2de58cbd088f0
-  __TEXT.__unwind_info: 0xe0 sha256:a68e0a9f4becced07d93bd4a7f9b2b1d7534b6479f1fdbac26e308b6b12071e3
-  __DATA_CONST.__got: 0x50 sha256:5b6fb58e61fa475939767d68a446f97f1bff02c0e5935a3ea8bb51e6515783d8
-  __DATA_CONST.__const: 0x78 sha256:080430d0d867f9f9df4f1fb39ec7c3613f2797f9d348817657b726c8195183be
-  __AUTH_CONST.__auth_got: 0x138 sha256:93211d39970db6627fbeb360c10367f5aa245d32a95ab97345f17b73730ac999
-  __AUTH_CONST.__const: 0x20 sha256:8c24344a3362d243556a0240cc6de35624d38b9a58351122a618f99426968e0a
-  __AUTH_CONST.__cfstring: 0x20 sha256:379b7ace0ce142be36dca6c0efc061511a8c38d99c0d0efbbc03f37d3920a0ca
+10.59.0.0.0
+  __TEXT.__text: 0x28c4 sha256:51fefe8771ecc0b3faa68eda35e48cd2275a7638c43e9635f0cdf3a328e1ee92
+  __TEXT.__const: 0xc0 sha256:708f2fd031a00bd7790a24ad37f36e93ff8be3b52502c77d7240432304844bd0
+  __TEXT.__gcc_except_tab: 0x68 sha256:351b6d6ae0c7b04daf73cbbfa725411bb3e5417ec83b1f03d49e0520d8ea8353
+  __TEXT.__cstring: 0x67e sha256:2340021c38735e58868909cd40d71e2252cb7fe89bd1877b3c54bc4a9fe11e06
+  __TEXT.__oslogstring: 0x422 sha256:85eb75370b8276e534d24a977ef1eeba2b7ad27e20888265a946fe4ad1524de4
+  __TEXT.__unwind_info: 0xc0 sha256:bfdf8c78b212c43d49fc9ef4d04bd35628ca8a7c038315d6eb6513b0f632110a
+  __TEXT.__auth_stubs: 0x0
+  __DATA_CONST.__const: 0x78 sha256:24f9a4a1cb8a5329596e9f0f6b820de9b08a0971db0cd4fb618eb4ec1c66d672
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__const: 0x20 sha256:d2fe87629e8641009f2484405b54412c9a1945cf47952fdf7dfaa815b6cc3036
+  __AUTH_CONST.__cfstring: 0x2c0 sha256:eb76fed97a072df02af01eff6ce420f73ff204747726c5342f9ab589c04e65f6
+  __AUTH_CONST.__weak_auth_got: 0x10 sha256:bd81906b6f4a0e73750f84a5de5ddad8dcb89f255f936061d6c581654bbca786
+  __AUTH_CONST.__auth_got: 0x1b8 sha256:360d579dbd14759b41afdf7fb5e80c0101e15150ae401d59f92a1e32d129f7cb
+  __DATA.__bss: 0x1000 sha256:ad7facb2586fc6e966c004d7d1d16b024f5805ff7cb47c7a85dabd8b48892ca7
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
