## ACCHWComponentAuthService

> `/System/Library/PrivateFrameworks/CoreAccessories.framework/XPCServices/ACCHWComponentAuthService.xpc/ACCHWComponentAuthService`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`
- `__TEXT.__objc_methtype`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1203.0.0.0.0
-  __TEXT.__text: 0x3958c
+1210.0.0.502.1
+  __TEXT.__text: 0x39518
   __TEXT.__auth_stubs: 0xe20
   __TEXT.__objc_stubs: 0xe60
-  __TEXT.__objc_methlist: 0x61c
+  __TEXT.__objc_methlist: 0x624
   __TEXT.__const: 0x19b63
   __TEXT.__cstring: 0x1f3d
   __TEXT.__objc_classname: 0x9b

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 1216
-  Symbols:   2756
+  Symbols:   2757
   CStrings:  1239
 
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
~ _mfi4Auth_protocol_handle_AuthCert : 6940 -> 6808
CStrings:
+ "+[ACCHWComponentAuthService _verifyModuleFDR:forModuleType:]"
- "-[ACCHWComponentAuthService _verifyModuleFDR:forModuleType:]"
```
