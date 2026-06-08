## EDPSecurity

> `/System/Library/PrivateFrameworks/EDPSecurity.framework/EDPSecurity`

```diff

 17.0.0.0.0
-  __TEXT.__text: 0xec04
-  __TEXT.__auth_stubs: 0xbb0
+  __TEXT.__text: 0xeaf0
   __TEXT.__objc_methlist: 0xdc
-  __TEXT.__const: 0xbb8
+  __TEXT.__const: 0xba8
   __TEXT.__gcc_except_tab: 0x160
   __TEXT.__cstring: 0xb5
-  __TEXT.__swift5_typeref: 0x276
+  __TEXT.__swift5_typeref: 0x26e
   __TEXT.__constg_swiftt: 0x44c
   __TEXT.__swift5_reflstr: 0x392
   __TEXT.__swift5_fieldmd: 0x2d4

   __TEXT.__swift5_types: 0x3c
   __TEXT.__swift5_mpenum: 0x10
   __TEXT.__swift5_capture: 0x20
-  __TEXT.__unwind_info: 0x4a0
-  __TEXT.__eh_frame: 0x868
-  __TEXT.__objc_classname: 0x120
-  __TEXT.__objc_methname: 0x597
-  __TEXT.__objc_methtype: 0xe7
-  __TEXT.__objc_stubs: 0x5a0
-  __DATA_CONST.__got: 0x1e0
+  __TEXT.__unwind_info: 0x490
+  __TEXT.__eh_frame: 0x788
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0xe8
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x180
-  __AUTH_CONST.__auth_got: 0x5e8
+  __DATA_CONST.__got: 0x1e8
   __AUTH_CONST.__const: 0x5dc
   __AUTH_CONST.__cfstring: 0x80
   __AUTH_CONST.__objc_const: 0x6e8
+  __AUTH_CONST.__auth_got: 0x638
   __AUTH.__objc_data: 0x190
   __AUTH.__data: 0x6b0
   __DATA.__objc_ivar: 0x14
-  __DATA.__data: 0x200
+  __DATA.__data: 0x1f0
   __DATA.__common: 0x40
   __DATA.__bss: 0x1000
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 37AD4A83-CA18-3773-B4CF-C5BE233F84D1
-  Functions: 368
-  Symbols:   378
-  CStrings:  99
+  UUID: BA0DC318-CCD9-3CBA-9C9F-B0132647EDA2
+  Functions: 365
+  Symbols:   389
+  CStrings:  13
 
Symbols:
+ ___swift_closure_destructor
+ ___swift_closure_destructor.2
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x2
+ _swift_release_x19
+ _swift_release_x20
+ _swift_release_x21
+ _swift_release_x22
+ _swift_release_x23
+ _swift_release_x25
+ _swift_release_x26
+ _swift_release_x27
+ _swift_release_x28
+ _swift_release_x8
+ _swift_retain_x19
+ _swift_retain_x2
+ _swift_retain_x20
+ _swift_retain_x21
+ _swift_retain_x22
+ _swift_retain_x8
- ___swift_allocate_boxed_opaque_existential_1
- _objc_release
- _objc_retain_x19
- _objc_retain_x26
- _objc_retain_x27
- _swift_allocBox
- _swift_bridgeObjectRelease_n
- _swift_bridgeObjectRetain_n
- _swift_stdlib_isStackAllocationSafe
- _symbolic _____Sg 10Foundation17URLResourceValuesV
CStrings:
- ".cxx_destruct"
- "@\"NSArray\""
- "@\"NSData\""
- "@\"NSError\""
- "@\"SignatureResponse\"20@?0@\"NSData\"8I16"
- "@16@0:8"
- "@32@0:8^{__SecIdentity=}16^@24"
- "@36@0:8@16B24^@28"
- "@44@0:8@16I24^{__SecIdentity=}28^@36"
- "@56@0:8@16@24@32@?40^@48"
- "B"
- "B16@0:8"
- "EDPUtilities"
- "OIDString"
- "SignatureResponse"
- "T@\"NSArray\",&,N,VcertificateChain"
- "T@\"NSData\",&,N,Vsignature"
- "T@\"NSData\",&,N,VvalidatedData"
- "T@\"NSError\",&,N,Verror"
- "TB,N,VisTrusted"
- "ValidationResponse"
- "_TtC11EDPSecurity12FileMeasurer"
- "_TtC11EDPSecurity13PackageSigner"
- "_TtC11EDPSecurity16PackageValidator"
- "_TtC11EDPSecurity16ResourceManifest"
- "_TtC11EDPSecurity22PackageStaticValidator"
- "addProtectedAttribute:"
- "additionalResources"
- "algorithm"
- "allObjects"
- "calculateSignerInfoDigest:"
- "certificateChain"
- "code"
- "createSignature:withCertChain:withTime:withRemoteHandler:withError:"
- "createTrustObjectWithPolicies:error:"
- "dataContent"
- "decodeMessageSecurityObject:options:error:"
- "defaultManager"
- "dictionaryWithObjects:forKeys:count:"
- "digestAlgorithmWithSignatureAlgorithm:error:"
- "domain"
- "embeddedContent"
- "encodeMessageSecurityObject:"
- "error"
- "errorWithDomain:code:userInfo:"
- "fileExistsAtPath:"
- "firstObject"
- "getCertificateChain:withError:"
- "hashingAlgorithms"
- "init"
- "initWithCertificate:signatureAlgorithm:error:"
- "initWithDataContent:isDetached:signer:additionalCertificates:error:"
- "initWithEmbeddedContent:"
- "initWithSigningTime:"
- "isEqualToString:"
- "isTrusted"
- "manifest"
- "measurer"
- "nextObject"
- "numberWithUnsignedInt:"
- "objectAtIndexedSubscript:"
- "resources"
- "reverseObjectEnumerator"
- "setCertificateChain:"
- "setError:"
- "setIsTrusted:"
- "setSignature:"
- "setSignerPolicies:"
- "setValidatedData:"
- "setVerifySignatures:"
- "setVerifySigners:"
- "signDigest:algorithm:identity:error:"
- "signature"
- "signatureAlgorithm"
- "signatureData"
- "signers"
- "signingTime"
- "supportedMeasurementAlgorithms"
- "trustedIdentity"
- "url"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@16"
- "validateSignature:requireTrust:withError:"
- "validatedData"
- "version"

```
