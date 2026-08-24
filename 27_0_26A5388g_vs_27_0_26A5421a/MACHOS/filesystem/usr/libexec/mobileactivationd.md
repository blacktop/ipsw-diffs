## mobileactivationd

> `/usr/libexec/mobileactivationd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__cstring`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1145.0.1.0.0
-  __TEXT.__text: 0x661f4
+1145.0.2.0.0
+  __TEXT.__text: 0x662c4
   __TEXT.__auth_stubs: 0x1190
   __TEXT.__objc_stubs: 0x24c0
   __TEXT.__objc_methlist: 0x8ec
-  __TEXT.__const: 0x14553
+  __TEXT.__const: 0x18be3
   __TEXT.__gcc_except_tab: 0x12c0
   __TEXT.__objc_methname: 0x2879
   __TEXT.__oslogstring: 0x143f

   __TEXT.__ustring: 0x4
   __TEXT.__dlopen_cstrs: 0x267
   __TEXT.__unwind_info: 0xde8
-  __DATA_CONST.__const: 0x6220
+  __DATA_CONST.__const: 0x6670
   __DATA_CONST.__cfstring: 0xa4e0
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_catlist: 0x18

   - /usr/lib/libbootpolicy.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 1447
-  Symbols:   3537
+  Symbols:   3558
   CStrings:  2498
 
Symbols:
+ _ApplePlatformBootstrapRootCAG1
+ _ApplePlatformBootstrapRootCAG1PublicKey
+ _ApplePlatformBootstrapRootCAG1SKID
+ _ApplePlatformBootstrapRootCAG1SPKI
+ _ApplePlatformBootstrapRootCAG1_public_key
+ _ApplePlatformBootstrapRootCAG1_skid
+ _ApplePlatformBootstrapRootCAG1_spki
+ _ApplePlatformDeveloperRootCAG1
+ _ApplePlatformDeveloperRootCAG1PublicKey
+ _ApplePlatformDeveloperRootCAG1SKID
+ _ApplePlatformDeveloperRootCAG1SPKI
+ _ApplePlatformDeveloperRootCAG1_public_key
+ _ApplePlatformDeveloperRootCAG1_skid
+ _ApplePlatformDeveloperRootCAG1_spki
+ _ApplePlatformMultipurposeRootCAG1
+ _ApplePlatformMultipurposeRootCAG1PublicKey
+ _ApplePlatformMultipurposeRootCAG1SKID
+ _ApplePlatformMultipurposeRootCAG1SPKI
+ _ApplePlatformMultipurposeRootCAG1_public_key
+ _ApplePlatformMultipurposeRootCAG1_skid
+ _ApplePlatformMultipurposeRootCAG1_spki
Functions:
~ _lockcrypto_decode_error : 668 -> 708
~ _lockcrypto_decode_pem : 624 -> 664
~ _lockcrypto_decode_pems : 776 -> 840
~ _OUTLINED_FUNCTION_8 : 8 -> 12
~ _OUTLINED_FUNCTION_9 : 12 -> 28
~ _OUTLINED_FUNCTION_10 : 16 -> 8
~ _OUTLINED_FUNCTION_11 : 28 -> 16
~ _OUTLINED_FUNCTION_21 : 12 -> 20
~ _OUTLINED_FUNCTION_22 : 20 -> 12
~ _LibSer_SEPControl_Deserialize : 160 -> 200
~ _LibSer_SEPControlResponse_Deserialize : 64 -> 88
CStrings:
+ "1145.0.2"
+ "Absinthe/2.0 macOS Device Activator (MobileActivation-1145.0.2 built on Aug 10 2026 at 01:08:15)"
+ "macOS Device Activator (MobileActivation-1145.0.2)"
- "1145.0.1"
- "Absinthe/2.0 macOS Device Activator (MobileActivation-1145.0.1 built on Jul 10 2026 at 22:43:51)"
- "macOS Device Activator (MobileActivation-1145.0.1)"
```
