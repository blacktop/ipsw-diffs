## trustd

> `/usr/libexec/trustd`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__objc_methtype`
- `__TEXT.__constg_swiftt`
- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-62460.40.56.502.1
-  __TEXT.__text: 0x5908c
-  __TEXT.__auth_stubs: 0x23d0
-  __TEXT.__objc_stubs: 0x33a0
-  __TEXT.__objc_methlist: 0xe14
+62460.40.74.0.0
+  __TEXT.__text: 0x59a08
+  __TEXT.__auth_stubs: 0x23c0
+  __TEXT.__objc_stubs: 0x3400
+  __TEXT.__objc_methlist: 0xe2c
   __TEXT.__const: 0xde20
   __TEXT.__dlopen_cstrs: 0x54
   __TEXT.__objc_classname: 0x1b4
-  __TEXT.__objc_methname: 0x3003
+  __TEXT.__objc_methname: 0x307d
   __TEXT.__objc_methtype: 0xc6b
   __TEXT.__constg_swiftt: 0x38
   __TEXT.__swift5_typeref: 0x17

   __TEXT.__swift5_fieldmd: 0x1c
   __TEXT.__swift5_types: 0x4
   __TEXT.__gcc_except_tab: 0xae0
-  __TEXT.__cstring: 0x6139
-  __TEXT.__oslogstring: 0x5d96
-  __TEXT.__unwind_info: 0x13c8
-  __DATA_CONST.__const: 0x3de8
-  __DATA_CONST.__cfstring: 0x5dc0
+  __TEXT.__cstring: 0x621e
+  __TEXT.__oslogstring: 0x5f18
+  __TEXT.__unwind_info: 0x13e0
+  __DATA_CONST.__const: 0x3e70
+  __DATA_CONST.__cfstring: 0x5ea0
   __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x28

   __DATA_CONST.__objc_arraydata: 0x100
   __DATA_CONST.__objc_arrayobj: 0x60
   __DATA_CONST.__objc_dictobj: 0x190
-  __DATA_CONST.__auth_got: 0x11f8
-  __DATA_CONST.__got: 0x930
+  __DATA_CONST.__auth_got: 0x11f0
+  __DATA_CONST.__got: 0x908
   __DATA_CONST.__auth_ptr: 0x18
-  __DATA.__objc_const: 0x1750
-  __DATA.__objc_selrefs: 0xe68
-  __DATA.__objc_ivar: 0xd0
+  __DATA.__objc_const: 0x1780
+  __DATA.__objc_selrefs: 0xe88
+  __DATA.__objc_ivar: 0xd4
   __DATA.__objc_data: 0x5b8
   __DATA.__data: 0x400
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  Functions: 1204
-  Symbols:   889
-  CStrings:  2216
+  Functions: 1210
+  Symbols:   884
+  CStrings:  2240
 
Symbols:
+ _CCDigest
+ _CCDigestGetOutputSize
+ _NSURLErrorFailingURLErrorKey
+ _SecKeyVerifySignature
+ _freeaddrinfo
+ _getaddrinfo
+ _kSecKeyAlgorithmECDSASignatureMessageX962SHA1
+ _kSecKeyAlgorithmECDSASignatureMessageX962SHA256
+ _kSecKeyAlgorithmECDSASignatureMessageX962SHA384
+ _kSecKeyAlgorithmRSASignatureMessagePKCS1v15SHA1
+ _kSecKeyAlgorithmRSASignatureMessagePKCS1v15SHA256
+ _kSecKeyAlgorithmRSASignatureMessagePKCS1v15SHA384
+ _readdir
- _CC_SHA224
- _CC_SHA256
- _CC_SHA384
- _CC_SHA512
- _CFPropertyListCreateXMLData
- _CFURLCreateDataAndPropertiesFromResource
- _CSSMOID_ECDSA_WithSHA1
- _CSSMOID_ECDSA_WithSHA256
- _CSSMOID_ECDSA_WithSHA384
- _CSSMOID_SHA1WithRSA
- _CSSMOID_SHA256WithRSA
- _CSSMOID_SHA384WithRSA
- _NSURLErrorFailingURLStringErrorKey
- _SecDigestCreate
- _inet_pton
- _readdir_r
- _xpc_transaction_begin
- _xpc_transaction_end
CStrings:
+ "0.4.0.194112.1.4"
+ "0.4.0.194112.1.5"
+ "CAIssuerSSRFBadPortAlt"
+ "CAIssuerSSRFBadPortSvc"
+ "OCSPExtraSingleResponses"
+ "OCSPResponse: duplicate certID, preferring revoked"
+ "OCSPResponse: more than %d certificates in the response"
+ "OCSPResponse: no request to scope the validity interval to"
+ "OCSPSSRFBadPortAlt"
+ "OCSPSSRFBadPortSvc"
+ "TB,V_responseTooLarge"
+ "Unable to get data from \"%s\": %@"
+ "UseSSRFLiteralEnforcement"
+ "UseSSRFPortEnforcement"
+ "_responseTooLarge"
+ "cancel"
+ "com.apple.trustd.analytics"
+ "dataWithContentsOfURL:options:error:"
+ "ocspcache"
+ "ocspcache: no request to scope the cache write to, not caching"
+ "response does not answer the request, not caching"
+ "response for taskId %@ from %@ passed %d bytes, cancelling"
+ "responseTooLarge"
+ "setResponseTooLarge:"
+ "skipping SSRF-denied destination for %@ (buckets 0x%x)"
- "Unable to get data from \"%s\": error %ld"
```
