## CoreIDCred

> `/System/Library/PrivateFrameworks/CoreIDCred.framework/CoreIDCred`

```diff

-8.36.2.0.0
-  __TEXT.__text: 0x47e08
-  __TEXT.__auth_stubs: 0xd90
-  __TEXT.__objc_methlist: 0x2044
-  __TEXT.__const: 0x36f8
-  __TEXT.__cstring: 0x2026
+8.38.3.0.0
+  __TEXT.__text: 0x48270
+  __TEXT.__auth_stubs: 0xda0
+  __TEXT.__objc_methlist: 0x2054
+  __TEXT.__const: 0x3708
+  __TEXT.__cstring: 0x2046
   __TEXT.__oslogstring: 0x39fc
-  __TEXT.__swift5_typeref: 0xe52
   __TEXT.__constg_swiftt: 0x900
-  __TEXT.__swift5_reflstr: 0x5b6
-  __TEXT.__swift5_fieldmd: 0x790
+  __TEXT.__swift5_typeref: 0xe52
   __TEXT.__swift5_builtin: 0x1b8
+  __TEXT.__swift5_reflstr: 0x5a6
+  __TEXT.__swift5_fieldmd: 0x790
   __TEXT.__swift5_assocty: 0x78
   __TEXT.__swift5_proto: 0x2c8
   __TEXT.__swift5_types: 0xf4
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__swift5_capture: 0x570
+  __TEXT.__swift5_mpenum: 0x28
+  __TEXT.__swift5_capture: 0x590
   __TEXT.__swift_as_entry: 0xd8
   __TEXT.__swift_as_ret: 0xf0
-  __TEXT.__swift5_mpenum: 0x28
-  __TEXT.__unwind_info: 0x18c8
+  __TEXT.__unwind_info: 0x18d8
   __TEXT.__eh_frame: 0x2380
   __TEXT.__objc_classname: 0x2be
-  __TEXT.__objc_methname: 0x414e
-  __TEXT.__objc_methtype: 0xec2
-  __TEXT.__objc_stubs: 0x19c0
+  __TEXT.__objc_methname: 0x41cc
+  __TEXT.__objc_methtype: 0xec6
+  __TEXT.__objc_stubs: 0x19e0
   __DATA_CONST.__got: 0x288
-  __DATA_CONST.__const: 0x9c8
+  __DATA_CONST.__const: 0x9d0
   __DATA_CONST.__objc_classlist: 0xe8
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc38
+  __DATA_CONST.__objc_selrefs: 0xc40
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0xb8
-  __AUTH_CONST.__auth_got: 0x6d0
-  __AUTH_CONST.__const: 0x2358
-  __AUTH_CONST.__cfstring: 0x16c0
-  __AUTH_CONST.__objc_const: 0x3728
+  __AUTH_CONST.__auth_got: 0x6d8
+  __AUTH_CONST.__const: 0x23a8
+  __AUTH_CONST.__cfstring: 0x16e0
+  __AUTH_CONST.__objc_const: 0x3758
   __AUTH.__objc_data: 0x2a8
   __AUTH.__data: 0x1b8
-  __DATA.__objc_ivar: 0x240
-  __DATA.__data: 0xcb8
+  __DATA.__objc_ivar: 0x244
+  __DATA.__data: 0xcc8
   __DATA.__bss: 0x5980
   __DATA_DIRTY.__objc_data: 0x708
   __DATA_DIRTY.__data: 0x88

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 47064E40-8AD6-30C1-8E98-8EF702CB1535
-  Functions: 2379
-  Symbols:   3316
-  CStrings:  1449
+  UUID: 64B3A9FA-D83D-36C7-B978-68F192054742
+  Functions: 2382
+  Symbols:   3321
+  CStrings:  1453
 
Symbols:
+ -[DCCredentialPayload issuerCertificateChain]
+ -[DCCredentialPayload setIssuerCertificateChain:]
+ -[DCCredentialProperties issuerCertificateChain]
+ -[DCCredentialProperties setIssuerCertificateChain:]
+ -[DCPresentmentProposal initWithCredentialIdentifier:presentmentKeyIdentifier:presentmentPublicKey:partition:docType:elements:authACL:readerAuthCertificateData:issuerSignerCertificateData:readerMetadata:readerAnalytics:region:issuingJurisdiction:credentialRevocationInfo:]
+ -[DCPresentmentProposal issuerSignerCertificateData]
+ _OBJC_IVAR_$_DCCredentialPayload._issuerCertificateChain
+ _OBJC_IVAR_$_DCCredentialProperties._issuerCertificateChain
+ _OBJC_IVAR_$_DCPresentmentProposal._issuerSignerCertificateData
+ _block_copy_helper.113
+ _block_copy_helper.119
+ _block_copy_helper.142
+ _block_copy_helper.165
+ _block_copy_helper.227
+ _block_copy_helper.233
+ _block_copy_helper.256
+ _block_copy_helper.279
+ _block_copy_helper.306
+ _block_copy_helper.312
+ _block_copy_helper.354
+ _block_copy_helper.360
+ _block_copy_helper.87
+ _block_descriptor.115
+ _block_descriptor.121
+ _block_descriptor.144
+ _block_descriptor.167
+ _block_descriptor.229
+ _block_descriptor.235
+ _block_descriptor.258
+ _block_descriptor.281
+ _block_descriptor.308
+ _block_descriptor.314
+ _block_descriptor.356
+ _block_descriptor.362
+ _block_descriptor.89
+ _block_destroy_helper.114
+ _block_destroy_helper.120
+ _block_destroy_helper.143
+ _block_destroy_helper.166
+ _block_destroy_helper.228
+ _block_destroy_helper.234
+ _block_destroy_helper.257
+ _block_destroy_helper.280
+ _block_destroy_helper.307
+ _block_destroy_helper.313
+ _block_destroy_helper.355
+ _block_destroy_helper.361
+ _block_destroy_helper.88
+ _kIssuerSignerCertificateData
+ _objc_msgSend$issuerCertificateChain
+ _objc_msgSend$issuerSignerCertificateData
+ _objc_msgSend$setIssuerCertificateChain:
+ _objectdestroy.147Tm
+ _objectdestroy.30Tm
+ _objectdestroy.43Tm
+ _objectdestroy.55Tm
+ _objectdestroy.76Tm
+ _objectdestroy.80Tm
+ _type_layout_string So38DCPresentmentTransportKeySpecificationV
- -[DCCredentialPayload authorityKeyIdentifiers]
- -[DCCredentialPayload setAuthorityKeyIdentifiers:]
- -[DCCredentialProperties authorityKeyIdentifiers]
- -[DCCredentialProperties setAuthorityKeyIdentifiers:]
- -[DCPresentmentProposal initWithCredentialIdentifier:presentmentKeyIdentifier:presentmentPublicKey:partition:docType:elements:authACL:readerAuthCertificateData:readerMetadata:readerAnalytics:region:issuingJurisdiction:credentialRevocationInfo:]
- _OBJC_IVAR_$_DCCredentialPayload._authorityKeyIdentifiers
- _OBJC_IVAR_$_DCCredentialProperties._authorityKeyIdentifiers
- _block_copy_helper.103
- _block_copy_helper.109
- _block_copy_helper.132
- _block_copy_helper.155
- _block_copy_helper.217
- _block_copy_helper.223
- _block_copy_helper.246
- _block_copy_helper.269
- _block_copy_helper.292
- _block_copy_helper.296
- _block_copy_helper.344
- _block_copy_helper.350
- _block_copy_helper.77
- _block_descriptor.105
- _block_descriptor.111
- _block_descriptor.134
- _block_descriptor.157
- _block_descriptor.219
- _block_descriptor.225
- _block_descriptor.248
- _block_descriptor.271
- _block_descriptor.294
- _block_descriptor.298
- _block_descriptor.346
- _block_descriptor.352
- _block_descriptor.79
- _block_destroy_helper.104
- _block_destroy_helper.110
- _block_destroy_helper.133
- _block_destroy_helper.156
- _block_destroy_helper.218
- _block_destroy_helper.224
- _block_destroy_helper.247
- _block_destroy_helper.270
- _block_destroy_helper.293
- _block_destroy_helper.297
- _block_destroy_helper.345
- _block_destroy_helper.351
- _block_destroy_helper.78
- _objc_msgSend$authorityKeyIdentifiers
- _objc_msgSend$setAuthorityKeyIdentifiers:
- _objectdestroy.137Tm
- _objectdestroy.25Tm
- _objectdestroy.38Tm
- _objectdestroy.50Tm
- _objectdestroy.66Tm
- _objectdestroy.70Tm
- _type_layout_string Si4days_t
CStrings:
+ "@128@0:8@16@24@32@40@48@56@64@72@80@88@96@104@112@120"
+ "T@\"NSArray\",&,N,V_issuerCertificateChain"
+ "T@\"NSData\",R,N,V_issuerSignerCertificateData"
+ "_issuerCertificateChain"
+ "_issuerSignerCertificateData"
+ "initWithCredentialIdentifier:presentmentKeyIdentifier:presentmentPublicKey:partition:docType:elements:authACL:readerAuthCertificateData:issuerSignerCertificateData:readerMetadata:readerAnalytics:region:issuingJurisdiction:credentialRevocationInfo:"
+ "issuerCertificateChain"
+ "issuerSignerCertificateData"
+ "setIssuerCertificateChain:"
- "\r"
- "@120@0:8@16@24@32@40@48@56@64@72@80@88@96@104@112"
- "T@\"NSArray\",&,N,V_authorityKeyIdentifiers"
- "_authorityKeyIdentifiers"
- "authorityKeyIdentifiers"
- "initWithCredentialIdentifier:presentmentKeyIdentifier:presentmentPublicKey:partition:docType:elements:authACL:readerAuthCertificateData:readerMetadata:readerAnalytics:region:issuingJurisdiction:credentialRevocationInfo:"
- "setAuthorityKeyIdentifiers:"

```
