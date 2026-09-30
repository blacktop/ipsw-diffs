## PlatformSSO

> `/System/Library/PrivateFrameworks/PlatformSSO.framework/PlatformSSO`

```diff

-483.60.3.0.0
-  __TEXT.__text: 0x59594
+483.60.4.0.0
+  __TEXT.__text: 0x595f4
   __TEXT.__auth_stubs: 0xe70
-  __TEXT.__objc_methlist: 0x32e4
+  __TEXT.__objc_methlist: 0x32fc
   __TEXT.__const: 0x2c8
-  __TEXT.__cstring: 0x8106
-  __TEXT.__oslogstring: 0x2301
+  __TEXT.__cstring: 0x8126
+  __TEXT.__oslogstring: 0x22b1
   __TEXT.__gcc_except_tab: 0x1528
   __TEXT.__dlopen_cstrs: 0x110
   __TEXT.__swift5_typeref: 0xc2

   __TEXT.__unwind_info: 0x1530
   __TEXT.__eh_frame: 0x560
   __TEXT.__objc_classname: 0x3d6
-  __TEXT.__objc_methname: 0x9d9d
+  __TEXT.__objc_methname: 0x9ea5
   __TEXT.__objc_methtype: 0x151a
   __TEXT.__objc_stubs: 0x6f60
   __DATA_CONST.__got: 0x430

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2220
+  __DATA_CONST.__objc_selrefs: 0x2228
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0xc0
   __DATA_CONST.__objc_arraydata: 0x10
   __AUTH_CONST.__auth_got: 0x748
   __AUTH_CONST.__const: 0xc28
-  __AUTH_CONST.__cfstring: 0x3880
-  __AUTH_CONST.__objc_const: 0x81d0
+  __AUTH_CONST.__cfstring: 0x38c0
+  __AUTH_CONST.__objc_const: 0x8230
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0x9b0
-  __DATA.__objc_ivar: 0x348
+  __DATA.__objc_ivar: 0x350
   __DATA.__data: 0x620
   __DATA.__bss: 0x2d0
   __DATA_DIRTY.__objc_data: 0x50

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 50D85D34-B766-35AC-BF00-0D2756C34B9A
-  Functions: 2054
-  Symbols:   7252
-  CStrings:  3156
+  UUID: 3F83B62E-1845-3B19-B2E4-36EEB1E3C7D3
+  Functions: 2056
+  Symbols:   7270
+  CStrings:  3163
 
Symbols:
+ -[POProfile accessKeyReaderIssuerCertificateUUID]
+ -[POProfile accessKeyReaderTerminalCapabilityIdentifier]
+ _OBJC_IVAR_$_POProfile._accessKeyReaderIssuerCertificateUUID
+ _OBJC_IVAR_$_POProfile._accessKeyReaderTerminalCapabilityIdentifier
+ ___29-[POProfile initWithProfile:]_block_invoke.103
+ ___29-[POProfile initWithProfile:]_block_invoke.103.cold.1
+ ___29-[POProfile initWithProfile:]_block_invoke.106
+ ___29-[POProfile initWithProfile:]_block_invoke.106.cold.1
+ ___29-[POProfile initWithProfile:]_block_invoke.93
+ ___29-[POProfile initWithProfile:]_block_invoke.93.cold.1
+ ___29-[POProfile initWithProfile:]_block_invoke.97
+ ___29-[POProfile initWithProfile:]_block_invoke.97.cold.1
+ ___block_literal_global.315
+ _objc_msgSend$accessKeyReaderTerminalCapabilityIdentifier
+ _objc_msgSend$setAccessTokenReaderTerminalCapabilityIdentifier:
- ___29-[POProfile initWithProfile:]_block_invoke.90
- ___29-[POProfile initWithProfile:]_block_invoke.90.cold.1
- ___29-[POProfile initWithProfile:]_block_invoke.94
- ___29-[POProfile initWithProfile:]_block_invoke.94.cold.1
- ___block_literal_global.295
- _objc_msgSend$isNetworkConnectedForRealm:
- _objc_msgSend$isRealmConfiguredForKerberosExtension:
Functions:
~ -[PODeviceConfiguration(POProfile) updateWithProfile:] : 536 -> 568
~ -[POAgentAuthenticationProcess exchangeTGTForStatus:] : 692 -> 388
~ -[POProfile initWithProfile:] : 4284 -> 4612
+ -[POProfile accessKeyReaderIssuerCertificateUUID]
+ -[POProfile accessKeyReaderTerminalCapabilityIdentifier]
~ -[POProfile .cxx_destruct] : 224 -> 248
+ ___29-[POProfile translatePolicy:]_block_invoke.cold.1
- ___29-[POProfile initWithProfile:]_block_invoke.94.cold.1
CStrings:
+ "(#V"
+ "AccessKeyReaderIssuerCertificateUUID"
+ "AccessKeyReaderTerminalCapabilityIdentifier"
+ "T@\"NSData\",R,N,V_accessKeyReaderTerminalCapabilityIdentifier"
+ "T@\"NSString\",R,N,V_accessKeyReaderIssuerCertificateUUID"
+ "_accessKeyReaderIssuerCertificateUUID"
+ "_accessKeyReaderTerminalCapabilityIdentifier"
+ "accessKeyReaderIssuerCertificateUUID"
+ "accessKeyReaderTerminalCapabilityIdentifier"
+ "setAccessTokenReaderTerminalCapabilityIdentifier:"
- "%s kerberos extension = %{public}@, isNetworkConnected = %{public}@ on %@"
- "(#T"
- "-[POAgentAuthenticationProcess exchangeTGTForStatus:]"
- "isNetworkConnectedForRealm:"
- "isRealmConfiguredForKerberosExtension:"

```
