## ACCHWComponentAuthService

> `/System/Library/PrivateFrameworks/CoreAccessories.framework/XPCServices/ACCHWComponentAuthService.xpc/ACCHWComponentAuthService`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

 1216.2.2.0.0
-  __TEXT.__text: 0x39530
+  __TEXT.__text: 0x39ae8
   __TEXT.__auth_stubs: 0xe20
-  __TEXT.__objc_stubs: 0xe60
-  __TEXT.__objc_methlist: 0x624
-  __TEXT.__const: 0x1e1f3
-  __TEXT.__cstring: 0x1f59
+  __TEXT.__objc_stubs: 0xe80
+  __TEXT.__objc_methlist: 0x66c
+  __TEXT.__const: 0x1e203
+  __TEXT.__cstring: 0x2050
   __TEXT.__objc_classname: 0x9b
-  __TEXT.__objc_methname: 0x1676
+  __TEXT.__objc_methname: 0x1783
   __TEXT.__objc_methtype: 0x607
-  __TEXT.__oslogstring: 0x6675
-  __TEXT.__gcc_except_tab: 0x274
-  __TEXT.__unwind_info: 0x818
-  __DATA_CONST.__const: 0x6978
-  __DATA_CONST.__cfstring: 0x1680
+  __TEXT.__oslogstring: 0x66e6
+  __TEXT.__gcc_except_tab: 0x270
+  __TEXT.__unwind_info: 0x828
+  __DATA_CONST.__const: 0x6a58
+  __DATA_CONST.__cfstring: 0x1780
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__auth_got: 0x720
   __DATA_CONST.__got: 0x138
   __DATA_CONST.__auth_ptr: 0x40
-  __DATA.__objc_const: 0xa70
-  __DATA.__objc_selrefs: 0x5a8
+  __DATA.__objc_const: 0xb10
+  __DATA.__objc_selrefs: 0x5d0
   __DATA.__objc_ivar: 0x60
   __DATA.__objc_data: 0x140
   __DATA.__data: 0x1b8

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1216
-  Symbols:   2780
-  CStrings:  1240
+  Functions: 1225
+  Symbols:   2799
+  CStrings:  1257
 
Symbols:
+ -[ACCHWComponentAuthService authenticateRCAMWithChallenge:completionHandler:updateRegistry:componentIndex:]
+ -[ACCHWComponentAuthService signRCAMChallenge:completionHandler:componentIndex:]
+ GCC_except_table70
+ _ACCUserDefaultsKey_BLEPairingConfigRequestDelayMs
+ _ACCUserDefaultsKey_BLEPairingDisableOOBPPlusFlow
+ _ACCUserDefaultsKey_BLEPairingDontEarlyInfoAsDeviceUID
+ _ACCUserDefaultsKey_BLEPairingIgnoreZeroEarlyInfo
+ _ACCUserDefaultsKey_PlatformIDOverride
+ _ACCUserDefaultsKey_TestCreateBLEPairingOnInductive
+ ___107-[ACCHWComponentAuthService authenticateRCAMWithChallenge:completionHandler:updateRegistry:componentIndex:]_block_invoke
+ ___107-[ACCHWComponentAuthService authenticateRCAMWithChallenge:completionHandler:updateRegistry:componentIndex:]_block_invoke_2
+ _kCFACCUserDefaultsKey_BLEPairingConfigRequestDelayMs
+ _kCFACCUserDefaultsKey_BLEPairingDisableOOBPPlusFlow
+ _kCFACCUserDefaultsKey_BLEPairingDontEarlyInfoAsDeviceUID
+ _kCFACCUserDefaultsKey_BLEPairingIgnoreZeroEarlyInfo
+ _kCFACCUserDefaultsKey_PlatformIDOverride
+ _kCFACCUserDefaultsKey_TestCreateBLEPairingOnInductive
+ _objc_msgSend$createVillanovaNonce:IDSN:challenge:
+ authenticateRCAMWithChallenge:completionHandler:updateRegistry:componentIndex:.RCAMQueue
+ authenticateRCAMWithChallenge:completionHandler:updateRegistry:componentIndex:.onceToken
- GCC_except_table67
CStrings:
+ "(moduleType=%d) %s: cpGetDeviceIDSN failed: ret=%x len=%zu"
+ "BLEPairingConfigRequestDelayMs"
+ "BLEPairingDisableOOBPPlusFlow"
+ "BLEPairingDontEarlyInfoAsDeviceUID"
+ "BLEPairingIgnoreZeroEarlyInfo"
+ "ComponentBusyError"
+ "Flags indicate rcam...do not call cpCopyCertificate()"
+ "PlatformIDOverride"
+ "RCAM"
+ "TestCreateBLEPairingOnInductive"
+ "authenticateRCAMWithChallenge:completionHandler:updateRegistry:"
+ "authenticateRCAMWithChallenge:completionHandler:updateRegistry:componentIndex:"
+ "com.apple.ACCHWComponentAuthService.rcam"
+ "createVillanovaNonce:IDSN:challenge:"
+ "prpc"
+ "signRCAMChallenge:completionHandler:"
+ "signRCAMChallenge:completionHandler:componentIndex:"
```
