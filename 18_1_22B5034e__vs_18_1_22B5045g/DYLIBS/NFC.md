## NFC

> `/System/Library/CoreAccessories/PlugIns/Transports/NFC.transport/NFC`

```diff

-1025.40.1.0.0
-  __TEXT.__text: 0xa0a8
+1025.40.2.0.0
+  __TEXT.__text: 0xa128
   __TEXT.__auth_stubs: 0x790
   __TEXT.__objc_methlist: 0x230
-  __TEXT.__cstring: 0xbfd
-  __TEXT.__const: 0x1390
+  __TEXT.__cstring: 0xc82
+  __TEXT.__const: 0x14b8
   __TEXT.__oslogstring: 0x17a2
   __TEXT.__gcc_except_tab: 0x1a8
   __TEXT.__dlopen_cstrs: 0xc2

   __TEXT.__objc_methtype: 0x394
   __TEXT.__objc_stubs: 0xde0
   __DATA_CONST.__got: 0x180
-  __DATA_CONST.__const: 0x838
+  __DATA_CONST.__const: 0x898
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0x38
   __AUTH_CONST.__auth_got: 0x3d8
   __AUTH_CONST.__const: 0x120
-  __AUTH_CONST.__cfstring: 0xde0
+  __AUTH_CONST.__cfstring: 0xea0
   __AUTH_CONST.__objc_const: 0x8b8
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x50

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 126
-  Symbols:   568
-  CStrings:  481
+  Functions: 127
+  Symbols:   582
+  CStrings:  487
 
Symbols:
+ _ACCUserDefaultsKey_PretendNFCAuthFailed
+ _colorWashTable0x91Size
+ _kCFACCUserDefaultsKey_PretendNFCAuthTimeout
+ _colorWashTable0x91
+ _kCFACCUserDefaultsKey_SkipNFCAuth
+ _ACCUserDefaultsKey_DontSkipInductiveAuthOnCTA
+ _kCFACCUserDefaultsKey_PretendNFCAuthFailed
+ _ACCUserDefaultsKey_InductiveAuthPretendMatchRxID
+ _kCFACCUserDefaultsKey_DontSkipInductiveAuthOnCTA
+ _ACCUserDefaultsKey_SkipNFCAuth
+ _ACCUserDefaultsKey_ForceT56RelaySupport
+ _kCFACCUserDefaultsKey_InductiveAuthPretendMatchRxID
+ _kCFACCUserDefaultsKey_ForceT56RelaySupport
+ _ACCUserDefaultsKey_PretendNFCAuthTimeout
CStrings:
+ "PretendNFCAuthTimeout"
+ "InductiveAuthPretendMatchRxID"
+ "ForceT56RelaySupport"
+ "DontSkipInductiveAuthOnCTA"
+ "SkipNFCAuth"
+ "PretendNFCAuthFailed"

```
