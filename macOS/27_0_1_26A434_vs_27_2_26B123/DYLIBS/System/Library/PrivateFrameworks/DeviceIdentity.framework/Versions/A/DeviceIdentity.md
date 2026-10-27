## DeviceIdentity

> `/System/Library/PrivateFrameworks/DeviceIdentity.framework/Versions/A/DeviceIdentity`

```diff

-1145.0.2.0.0
-  __TEXT.__text: 0x20e0c
-  __TEXT.__objc_methlist: 0x444
-  __TEXT.__cstring: 0x45a4
+1145.40.5.0.4
+  __TEXT.__text: 0x20e38
+  __TEXT.__objc_methlist: 0x454
+  __TEXT.__cstring: 0x45d1
   __TEXT.__gcc_except_tab: 0xe90
   __TEXT.__const: 0x1059a
   __TEXT.__ustring: 0x4

   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x638
+  __DATA_CONST.__objc_selrefs: 0x640
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA_CONST.__objc_arraydata: 0x5f8
+  __DATA_CONST.__objc_arraydata: 0x600
   __DATA_CONST.__got: 0x278
   __AUTH_CONST.__const: 0x2b0
-  __AUTH_CONST.__cfstring: 0x4860
-  __AUTH_CONST.__objc_const: 0x730
+  __AUTH_CONST.__cfstring: 0x48a0
+  __AUTH_CONST.__objc_const: 0x760
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_intobj: 0x1f8
   __AUTH_CONST.__auth_got: 0x460
   __AUTH_CONST.__auth_ptr: 0x0
   __AUTH.__data: 0x10
-  __DATA.__objc_ivar: 0x54
-  __DATA.__data: 0xf8
+  __DATA.__objc_ivar: 0x58
+  __DATA.__data: 0x88
   __DATA.__bss: 0xa8
   __DATA_DIRTY.__objc_data: 0xa0
-  __DATA_DIRTY.__data: 0x10
+  __DATA_DIRTY.__data: 0x80
   __DATA_DIRTY.__bss: 0x68
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CryptoTokenKit.framework/Versions/A/CryptoTokenKit

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbootpolicy.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 360
-  Symbols:   1238
-  CStrings:  714
+  Functions: 361
+  Symbols:   1240
+  CStrings:  716
 
Symbols:
+ -[DeviceTypeDeviceIdentity is_home_accessory]
+ OBJC_IVAR_$_DeviceTypeDeviceIdentity._is_home_accessory
+ _OUTLINED_FUNCTION_19
+ _OUTLINED_FUNCTION_20
+ _OUTLINED_FUNCTION_28
+ _OUTLINED_FUNCTION_37
+ _OUTLINED_FUNCTION_43
+ _OUTLINED_FUNCTION_47
- _OUTLINED_FUNCTION_12
- _OUTLINED_FUNCTION_15
- _OUTLINED_FUNCTION_22
- _OUTLINED_FUNCTION_39
- _OUTLINED_FUNCTION_46
- _OUTLINED_FUNCTION_48
Functions:
~ -[DeviceTypeDeviceIdentity init] : 2132 -> 2152
+ -[DeviceTypeDeviceIdentity ucrt_enforced]
~ _X509ExtensionParseBasicConstraints : 208 -> 212
~ _X509ChainBuildPathPartial : 484 -> 496
CStrings:
+ "ACCHWComponentAuthService"
+ "HomeAccessory"
+ "macOS Device Activator (MobileActivation-1145.40.5.0.4)"
- "macOS Device Activator (MobileActivation-1145.0.2)"
```
