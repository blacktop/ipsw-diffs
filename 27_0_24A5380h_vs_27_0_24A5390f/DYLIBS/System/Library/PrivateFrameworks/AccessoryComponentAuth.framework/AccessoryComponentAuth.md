## AccessoryComponentAuth

> `/System/Library/PrivateFrameworks/AccessoryComponentAuth.framework/AccessoryComponentAuth`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH.__objc_data`
- `__DATA.__data`

```diff

-1203.0.0.0.0
-  __TEXT.__text: 0x1240c
-  __TEXT.__objc_methlist: 0x4e4
+1210.0.0.502.1
+  __TEXT.__text: 0x1241c
+  __TEXT.__objc_methlist: 0x4ec
   __TEXT.__const: 0xd700
   __TEXT.__cstring: 0x14b6
   __TEXT.__oslogstring: 0x11d7

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 479
-  Symbols:   1579
+  Symbols:   1580
   CStrings:  338
 
Symbols:
+ +[ACCHWComponentAuthService _findFDRCertData:forModuleType:withAuthParams:hasDeviceCert:withError:]
+ +[ACCHWComponentAuthService _validateDeviceAndFDRCert:forModuleType:withAuthParams:]
+ +[ACCHWComponentAuthService _verifyModuleFDR:forModuleType:]
+ __OBJC_$_CLASS_METHODS_ACCHWComponentAuthService
- -[ACCHWComponentAuthService _findFDRCertData:forModuleType:withAuthParams:hasDeviceCert:withError:]
- -[ACCHWComponentAuthService _validateDeviceAndFDRCert:forModuleType:withAuthParams:]
- -[ACCHWComponentAuthService _verifyModuleFDR:forModuleType:]
Functions:
~ -[ACCHWComponentAuthService _authenticateModuleWithChallenge:completionHandler:moduleType:updateRegistry:updateUIProperty:logToAnalytics:componentIndex:] : 10520 -> 10536
CStrings:
+ "+[ACCHWComponentAuthService _verifyModuleFDR:forModuleType:]"
- "-[ACCHWComponentAuthService _verifyModuleFDR:forModuleType:]"
```
