## PlatformSSOCore

> `/System/Library/PrivateFrameworks/PlatformSSOCore.framework/PlatformSSOCore`

```diff

-483.60.3.0.0
-  __TEXT.__text: 0x8e850
+483.60.4.0.0
+  __TEXT.__text: 0x8ec0c
   __TEXT.__auth_stubs: 0x1ae0
-  __TEXT.__objc_methlist: 0x5f10
+  __TEXT.__objc_methlist: 0x5f58
   __TEXT.__const: 0x17a4
-  __TEXT.__cstring: 0xa516
+  __TEXT.__cstring: 0xa528
   __TEXT.__oslogstring: 0x19e7
   __TEXT.__gcc_except_tab: 0x7f8
   __TEXT.__dlopen_cstrs: 0xa6

   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_proto: 0x40
   __TEXT.__swift5_types: 0x34
-  __TEXT.__unwind_info: 0x1fe8
+  __TEXT.__unwind_info: 0x1ff8
   __TEXT.__eh_frame: 0x5b8
   __TEXT.__objc_classname: 0xd3d
-  __TEXT.__objc_methname: 0xc8f3
+  __TEXT.__objc_methname: 0xcad3
   __TEXT.__objc_methtype: 0x28de
-  __TEXT.__objc_stubs: 0x7040
+  __TEXT.__objc_stubs: 0x7060
   __DATA_CONST.__got: 0x918
   __DATA_CONST.__const: 0x2448
   __DATA_CONST.__objc_classlist: 0x4b0
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2af0
+  __DATA_CONST.__objc_selrefs: 0x2b20
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x1e0
   __DATA_CONST.__objc_arraydata: 0x58
   __AUTH_CONST.__auth_got: 0xd80
   __AUTH_CONST.__const: 0x780
   __AUTH_CONST.__cfstring: 0x7480
-  __AUTH_CONST.__objc_const: 0x141b8
+  __AUTH_CONST.__objc_const: 0x14228
   __AUTH_CONST.__objc_intobj: 0x1c8
   __AUTH_CONST.__objc_doubleobj: 0x30
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH.__objc_data: 0x33b0
   __AUTH.__data: 0x180
-  __DATA.__objc_ivar: 0x614
+  __DATA.__objc_ivar: 0x61c
   __DATA.__data: 0x1050
   __DATA.__bss: 0xd31
   __DATA.__common: 0x88

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 8764CEA0-E517-39F7-B809-EA78D11399B8
-  Functions: 3603
-  Symbols:   11957
-  CStrings:  5079
+  UUID: A03870E6-5A71-3BB1-8AEB-3FCD1CF6199C
+  Functions: 3612
+  Symbols:   11978
+  CStrings:  5091
 
Symbols:
+ -[PODeviceConfiguration _accessTokenReaderIssuerCertificateData]
+ -[PODeviceConfiguration accessKeyReaderIssuerCertificate]
+ -[PODeviceConfiguration accessTokenReaderTerminalCapabilityIdentifier]
+ -[PODeviceConfiguration setAccessKeyReaderIssuerCertificate:]
+ -[PODeviceConfiguration setAccessTokenReaderTerminalCapabilityIdentifier:]
+ -[PODeviceConfiguration set_accessTokenReaderIssuerCertificateData:]
+ _AKSGetKeyBagStats
+ _OBJC_IVAR_$_PODeviceConfiguration.__accessTokenReaderIssuerCertificateData
+ _OBJC_IVAR_$_PODeviceConfiguration._accessTokenReaderTerminalCapabilityIdentifier
+ _OUTLINED_FUNCTION_75
+ ___38-[PODeviceConfiguration initWithData:]_block_invoke.184
+ ___block_literal_global.472
+ _objc_msgSend$accessTokenReaderTerminalCapabilityIdentifier
+ _seconds_to_day
- ___38-[PODeviceConfiguration initWithData:]_block_invoke.180
- ___block_literal_global.456
CStrings:
+ "AKSGetKeyBagStats"
+ "T@\"NSData\",&,N,V__accessTokenReaderIssuerCertificateData"
+ "T@\"NSData\",C,N,V_accessTokenReaderTerminalCapabilityIdentifier"
+ "T^{__SecCertificate=}"
+ "__accessTokenReaderIssuerCertificateData"
+ "_accessTokenReaderIssuerCertificateData"
+ "_accessTokenReaderTerminalCapabilityIdentifier"
+ "accessKeyReaderIssuerCertificate"
+ "accessTokenReaderTerminalCapabilityIdentifier"
+ "setAccessKeyReaderIssuerCertificate:"
+ "setAccessTokenReaderTerminalCapabilityIdentifier:"
+ "set_accessTokenReaderIssuerCertificateData:"

```
