## IAPAuthentication

> `/System/Library/PrivateFrameworks/IAPAuthentication.framework/IAPAuthentication`

```diff

-2173.80.2.0.0
-  __TEXT.__text: 0x3090
+2176.100.2.0.0
+  __TEXT.__text: 0x3080
   __TEXT.__auth_stubs: 0x3d0
   __TEXT.__const: 0x53999
-  __TEXT.__cstring: 0x1048
+  __TEXT.__cstring: 0x1087
   __TEXT.__unwind_info: 0x110
   __DATA_CONST.__got: 0x68
   __DATA_CONST.__const: 0x7b8

   - /System/Library/Frameworks/Security.framework/Security
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
-  UUID: 5DA98167-9DB1-3F85-9DA6-031670F569CF
-  Functions: 53
-  Symbols:   265
+  UUID: 3FDCFEB6-C5C5-30F7-AE1B-958BF3E68DE2
+  Functions: 54
+  Symbols:   267
   CStrings:  108
 
Symbols:
+ _OUTLINED_FUNCTION_0
Functions:
~ _IapAuthChallengeVerify : 1852 -> 1844
~ _IapAuthCertVerifyAuthVersion : 1288 -> 1280
~ _IapAuthCertSerial : 496 -> 488
~ _PrintSerialNumberBytes : 272 -> 268
+ _OUTLINED_FUNCTION_0
~ _IapAuthChallengeVerify.cold.1 : 40 -> 28
~ _IapAuthCertSerial.cold.1 : 20 -> 24
CStrings:
+ "/Library/Caches/com.apple.xbs/DE23EDA2-E688-488B-A1E6-B625658C365D/TemporaryDirectory.To2EnX/Sources/IAPFramework/IAPAuthentication/IAPSecurity.c"
- "/Library/Caches/com.apple.xbs/Sources/IAPFramework/IAPAuthentication/IAPSecurity.c"

```
