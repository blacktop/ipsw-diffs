## SEService

> `/System/Library/PrivateFrameworks/SEService.framework/SEService`

```diff

-64.20.2.0.0
-  __TEXT.__text: 0xf3628
-  __TEXT.__auth_stubs: 0x1c80
-  __TEXT.__objc_methlist: 0x3a6c
-  __TEXT.__const: 0x15ce0
-  __TEXT.__oslogstring: 0x2377
-  __TEXT.__cstring: 0x8015
+64.22.0.0.0
+  __TEXT.__text: 0xf3914
+  __TEXT.__auth_stubs: 0x1c70
+  __TEXT.__objc_methlist: 0x3a7c
+  __TEXT.__const: 0x15cd0
+  __TEXT.__oslogstring: 0x23a7
+  __TEXT.__cstring: 0x8035
   __TEXT.__gcc_except_tab: 0x1eec
   __TEXT.__dlopen_cstrs: 0x64
   __TEXT.__constg_swiftt: 0x3108

   __TEXT.__unwind_info: 0x4a50
   __TEXT.__eh_frame: 0x530c
   __TEXT.__objc_classname: 0xcff
-  __TEXT.__objc_methname: 0x8ae7
+  __TEXT.__objc_methname: 0x8b07
   __TEXT.__objc_methtype: 0x2b37
-  __TEXT.__objc_stubs: 0x4860
+  __TEXT.__objc_stubs: 0x48a0
   __DATA_CONST.__got: 0x658
   __DATA_CONST.__const: 0x16a8
   __DATA_CONST.__objc_classlist: 0x2e8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x120
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1a38
+  __DATA_CONST.__objc_selrefs: 0x1a48
   __DATA_CONST.__objc_protorefs: 0xa0
   __DATA_CONST.__objc_superrefs: 0xf8
   __DATA_CONST.__objc_arraydata: 0xe8
-  __AUTH_CONST.__auth_got: 0xe50
+  __AUTH_CONST.__auth_got: 0xe48
   __AUTH_CONST.__const: 0x9060
-  __AUTH_CONST.__cfstring: 0x4340
+  __AUTH_CONST.__cfstring: 0x4360
   __AUTH_CONST.__objc_const: 0x7ec0
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_dictobj: 0x118

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 27BD1E88-D435-39A9-9398-7F07BB2B4802
-  Functions: 6412
-  Symbols:   6179
-  CStrings:  3370
+  UUID: FDCDD523-EC5A-32A1-881E-68C8EED33356
+  Functions: 6413
+  Symbols:   6182
+  CStrings:  3375
 
Symbols:
+ +[SEEndPoint endpointWithPublicKeyIdentifier:appletIdentifier:revocationAttestation:error:]
+ -[SESNFCAppSettingsContext sendNotification:]
+ ___block_literal_global.92
+ _objc_msgSend$UTF8String
+ _objc_msgSend$sendNotification:
- +[SEEndPoint revokedEndpointWithPublicKeyIdentifier:appletIdentifier:revocationAttestation:error:]
- ___block_literal_global.89
- _objc_retain_x10
CStrings:
+ "Could not post domain change notification \"%s\": %u"
+ "Nil input to endpointWithPublicKeyIdentifier"
+ "UTF8String"
+ "com.apple.seserviced.default.app.change"
+ "endpointWithPublicKeyIdentifier:appletIdentifier:revocationAttestation:error:"
+ "sendNotification:"
- "Nil input to revokedEndpointWithPublicKeyIdentifier"
- "revokedEndpointWithPublicKeyIdentifier:appletIdentifier:revocationAttestation:error:"

```
