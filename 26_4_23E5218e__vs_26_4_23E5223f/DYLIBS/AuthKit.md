## AuthKit

> `/System/Library/PrivateFrameworks/AuthKit.framework/AuthKit`

```diff

-525.475.16.0.0
-  __TEXT.__text: 0x196d5c
-  __TEXT.__auth_stubs: 0xc60
-  __TEXT.__objc_methlist: 0xefbc
+525.475.18.0.0
+  __TEXT.__text: 0x197484
+  __TEXT.__auth_stubs: 0xc80
+  __TEXT.__objc_methlist: 0xefec
   __TEXT.__const: 0x6a48
-  __TEXT.__cstring: 0x1076e
+  __TEXT.__cstring: 0x107a2
   __TEXT.__gcc_except_tab: 0xa798
-  __TEXT.__oslogstring: 0x13cce
+  __TEXT.__oslogstring: 0x13e2c
   __TEXT.__dlopen_cstrs: 0x305
   __TEXT.__ustring: 0x300
-  __TEXT.__unwind_info: 0x4538
+  __TEXT.__unwind_info: 0x4548
   __TEXT.__objc_classname: 0x1e34
-  __TEXT.__objc_methname: 0x2510d
-  __TEXT.__objc_methtype: 0x496b
-  __TEXT.__objc_stubs: 0x10b80
+  __TEXT.__objc_methname: 0x251c9
+  __TEXT.__objc_methtype: 0x49aa
+  __TEXT.__objc_stubs: 0x10bc0
   __DATA_CONST.__got: 0xad0
-  __DATA_CONST.__const: 0xa6a8
+  __DATA_CONST.__const: 0xa6b8
   __DATA_CONST.__objc_classlist: 0x6b8
   __DATA_CONST.__objc_catlist: 0x88
   __DATA_CONST.__objc_protolist: 0x208
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x78c0
+  __DATA_CONST.__objc_selrefs: 0x78e0
   __DATA_CONST.__objc_protorefs: 0xe0
   __DATA_CONST.__objc_superrefs: 0x438
   __DATA_CONST.__objc_arraydata: 0x2e8
-  __AUTH_CONST.__auth_got: 0x640
+  __AUTH_CONST.__auth_got: 0x650
   __AUTH_CONST.__const: 0x1410
-  __AUTH_CONST.__cfstring: 0x11540
-  __AUTH_CONST.__objc_const: 0x28280
+  __AUTH_CONST.__cfstring: 0x11580
+  __AUTH_CONST.__objc_const: 0x282b0
   __AUTH_CONST.__objc_intobj: 0x300
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_dictobj: 0x410
   __AUTH.__objc_data: 0x2ad0
-  __DATA.__objc_ivar: 0x1158
+  __DATA.__objc_ivar: 0x115c
   __DATA.__data: 0x1900
   __DATA.__bss: 0x6f8
   __DATA_DIRTY.__objc_data: 0x1860

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 64B36112-2C9B-3EEF-96EC-4D987145BC64
-  Functions: 5770
-  Symbols:   21829
-  CStrings:  12813
+  UUID: 56DD3F45-AE93-3F78-8C6F-5B6955210607
+  Functions: 5774
+  Symbols:   21843
+  CStrings:  12832
 
Symbols:
+ +[AKSecurityHelper secKeyCopyExternalRepresentationOfKey:error:]
+ +[AKSecurityHelper secKeyCopyPublicKeyFromRefKey:error:]
+ -[AKBAAAttestationData clientOrHostExcludesBAA]
+ -[AKBAAAttestationData setClientOrHostExcludesBAA:]
+ _AKBAATokenExclusionProcessBagConfigKey
+ _OBJC_IVAR_$_AKBAAAttestationData._clientOrHostExcludesBAA
+ _SecKeyCopyExternalRepresentation
+ _SecKeyCopyPublicKey
+ _objc_msgSend$ak_attestationErrorWithCode:underlyingError:
+ _objc_msgSend$clientOrHostExcludesBAA
CStrings:
+ "@32@0:8^{__SecKey=}16^@24"
+ "Exporting key to external representation"
+ "Extracting public key from private key"
+ "Failed to export key to external representation: %@"
+ "Failed to export key to external representation: unknown error"
+ "Failed to extract public key from private key"
+ "Process or host is exempted from BAA. Not generating BAA headers."
+ "Successfully exported key data (%lu bytes)"
+ "TB,V_clientOrHostExcludesBAA"
+ "^{__SecKey=}32@0:8^{__SecKey=}16^@24"
+ "_clientOrHostExcludesBAA"
+ "baa-token-exclusion-process"
+ "clientOrHostExcludesBAA"
+ "secKeyCopyExternalRepresentationOfKey:error:"
+ "secKeyCopyPublicKeyFromRefKey:error:"
+ "setClientOrHostExcludesBAA:"

```
