## libSoftwareUpdateSSO.dylib

> `/usr/lib/libSoftwareUpdateSSO.dylib`

```diff

-1329.80.16.0.0
-  __TEXT.__text: 0x2734
-  __TEXT.__auth_stubs: 0x2a0
-  __TEXT.__objc_methlist: 0x25c
+1487.101.2.0.0
+  __TEXT.__text: 0x2a70
+  __TEXT.__auth_stubs: 0x290
+  __TEXT.__objc_methlist: 0x3b8
   __TEXT.__const: 0x60
-  __TEXT.__cstring: 0x2a7
-  __TEXT.__oslogstring: 0x536
-  __TEXT.__unwind_info: 0xe0
+  __TEXT.__cstring: 0x286
+  __TEXT.__oslogstring: 0x58f
+  __TEXT.__unwind_info: 0xe8
   __TEXT.__objc_classname: 0x9d
-  __TEXT.__objc_methname: 0xb9c
+  __TEXT.__objc_methname: 0xbcb
   __TEXT.__objc_methtype: 0x2e6
-  __TEXT.__objc_stubs: 0x940
-  __DATA_CONST.__got: 0xa8
+  __TEXT.__objc_stubs: 0x9c0
+  __DATA_CONST.__got: 0xb0
   __DATA_CONST.__const: 0x88
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2a8
+  __DATA_CONST.__objc_selrefs: 0x368
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x158
-  __AUTH_CONST.__const: 0x150
-  __AUTH_CONST.__cfstring: 0x360
-  __AUTH_CONST.__objc_const: 0x8c8
+  __AUTH_CONST.__auth_got: 0x150
+  __AUTH_CONST.__const: 0xf0
+  __AUTH_CONST.__cfstring: 0x480
+  __AUTH_CONST.__objc_const: 0x650
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0x44
   __DATA.__data: 0x120
-  __DATA.__bss: 0x50
+  __DATA.__bss: 0x20
   - /System/Library/Frameworks/AuthenticationServices.framework/Versions/A/AuthenticationServices
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/Security.framework/Versions/A/Security
   - /System/Library/PrivateFrameworks/IASUtilitiesCore.framework/Versions/A/IASUtilitiesCore
+  - /System/Library/PrivateFrameworks/SoftwareUpdateCoreSupport.framework/Versions/A/SoftwareUpdateCoreSupport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1A346D25-1106-3BFC-8440-DA7F37F6A940
-  Functions: 71
-  Symbols:   295
-  CStrings:  270
+  UUID: D1C9B733-ADD0-38A8-BED8-12501A7E19F7
+  Functions: 67
+  Symbols:   286
+  CStrings:  290
 
Symbols:
+ -[SoftwareUpdateSSO initWithOptions:].cold.1
+ _MAClientLog.clientLoggers
+ _MAClientLog.cold.1
+ _MAClientLog.onceToken
+ _OBJC_CLASS_$_SUCore
+ __MAClientLog
+ ____MAClientLog_block_invoke
+ _objc_msgSend$UTF8String
+ _objc_msgSend$objectForKey:
+ _objc_msgSend$sharedCore
+ _objc_msgSend$useDomain:
- SoftwareUpdateSSOlogDebug.infoDebug
- SoftwareUpdateSSOlogDebug.logDebugOnce
- SoftwareUpdateSSOlogError.infoError
- SoftwareUpdateSSOlogError.logErrorOnce
- SoftwareUpdateSSOlogFault.infoFault
- SoftwareUpdateSSOlogFault.logFaultOnce
- SoftwareUpdateSSOlogInfo.infoLog
- SoftwareUpdateSSOlogInfo.logInfoOnce
- _NSLog
- _SoftwareUpdateSSOlogDebug
- _SoftwareUpdateSSOlogError
- _SoftwareUpdateSSOlogFault
- _SoftwareUpdateSSOlogInfo
- ___SoftwareUpdateSSOlogDebug_block_invoke
- ___SoftwareUpdateSSOlogError_block_invoke
- ___SoftwareUpdateSSOlogFault_block_invoke
- ___SoftwareUpdateSSOlogInfo_block_invoke
- __block_literal_global.10
- __block_literal_global.4
- __block_literal_global.7
CStrings:
+ "Attempt to extract DAW token from response"
+ "Auto"
+ "AutoSet"
+ "AutoStager"
+ "Brain"
+ "DEFAULT"
+ "Invalid interactivity level was passed in: %@"
+ "KeyManager"
+ "Manifest"
+ "PushNotification"
+ "SSO"
+ "SecureMA"
+ "Successfully retrieved response from authenticator"
+ "UTF8String"
+ "Using default interactivity level(0)"
+ "V2"
+ "com.apple.MobileAsset"
+ "objectForKey:"
+ "sharedCore"
+ "useDomain:"
- "Attempt to extract DAW token from response\n"
- "Debug"
- "Error"
- "Fault"
- "Invalid interactivity level was passed in: %@\n"
- "Notice"
- "Successfully retrieved response from authenticator\n"
- "Using default interactivity level(0)\n"
- "com.apple.SoftwareUpdateSSO"

```
