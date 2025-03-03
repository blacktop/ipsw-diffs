## akd

> `/System/Library/PrivateFrameworks/AuthKit.framework/akd`

```diff

-493.458.3.2.0
-  __TEXT.__text: 0x1a3de4
-  __TEXT.__auth_stubs: 0x1fb0
-  __TEXT.__objc_stubs: 0x187e0
-  __TEXT.__objc_methlist: 0xab64
+493.460.2.0.0
+  __TEXT.__text: 0x1b4e10
+  __TEXT.__auth_stubs: 0x1fd0
+  __TEXT.__objc_stubs: 0x187a0
+  __TEXT.__objc_methlist: 0xab6c
   __TEXT.__const: 0x31a0
-  __TEXT.__cstring: 0xb853
-  __TEXT.__objc_classname: 0x1899
-  __TEXT.__objc_methname: 0x22802
+  __TEXT.__cstring: 0xb893
+  __TEXT.__objc_classname: 0x1897
+  __TEXT.__objc_methname: 0x22879
   __TEXT.__objc_methtype: 0x5c3d
-  __TEXT.__gcc_except_tab: 0x2364
-  __TEXT.__oslogstring: 0x20dc8
-  __TEXT.__dlopen_cstrs: 0xb8
-  __TEXT.__swift5_typeref: 0x218d
+  __TEXT.__gcc_except_tab: 0x231c
+  __TEXT.__oslogstring: 0x20f68
+  __TEXT.__dlopen_cstrs: 0x5a
+  __TEXT.__swift5_typeref: 0x2193
   __TEXT.__swift5_fieldmd: 0xd34
   __TEXT.__constg_swiftt: 0x14e8
   __TEXT.__swift5_reflstr: 0xbd0

   __TEXT.__swift_as_entry: 0x38c
   __TEXT.__swift_as_ret: 0x440
   __TEXT.__swift5_protos: 0x38
-  __TEXT.__unwind_info: 0x59b0
-  __TEXT.__eh_frame: 0x8708
-  __DATA_CONST.__auth_got: 0xfe8
+  __TEXT.__unwind_info: 0x5ec0
+  __TEXT.__eh_frame: 0x9070
+  __DATA_CONST.__auth_got: 0xff8
   __DATA_CONST.__got: 0x1760
-  __DATA_CONST.__auth_ptr: 0x5d0
-  __DATA_CONST.__const: 0xda30
-  __DATA_CONST.__cfstring: 0x6ec0
+  __DATA_CONST.__auth_ptr: 0x618
+  __DATA_CONST.__const: 0xda40
+  __DATA_CONST.__cfstring: 0x6ea0
   __DATA_CONST.__objc_classlist: 0x728
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x2e0

   __DATA_CONST.__objc_protorefs: 0x120
   __DATA_CONST.__objc_superrefs: 0x3c8
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA_CONST.__objc_intobj: 0x300
+  __DATA_CONST.__objc_intobj: 0x318
   __DATA_CONST.__objc_arraydata: 0x2c0
   __DATA_CONST.__objc_arrayobj: 0x48
   __DATA_CONST.__linkguard: 0x3e
   __DATA_CONST.__objc_dictobj: 0x118
-  __DATA.__objc_const: 0x23158
-  __DATA.__objc_selrefs: 0x77c8
-  __DATA.__objc_ivar: 0x9f4
+  __DATA.__objc_const: 0x23180
+  __DATA.__objc_selrefs: 0x77c0
+  __DATA.__objc_ivar: 0x9f8
   __DATA.__objc_data: 0x5470
-  __DATA.__data: 0x45e8
-  __DATA.__bss: 0x2820
+  __DATA.__data: 0x45f8
+  __DATA.__bss: 0x2800
   __DATA.__common: 0x114
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/Combine.framework/Combine

   - /System/Library/PrivateFrameworks/IDSFoundation.framework/IDSFoundation
   - /System/Library/PrivateFrameworks/MDMClientLibrary.framework/MDMClientLibrary
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
+  - /System/Library/PrivateFrameworks/MobileActivation.framework/MobileActivation
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/PlugInKit.framework/PlugInKit
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 7589
-  Symbols:   1412
-  CStrings:  9748
+  Functions: 7591
+  Symbols:   1414
+  CStrings:  9750
 
Symbols:
+ _$sSO16debugDescriptionSSvg
+ _$sSq16debugDescriptionSSvg
+ _MAEIssueDCRTWithCompletion
+ _swift_cvw_allocateGenericValueMetadataWithLayoutString
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_initWithCopy
+ _swift_cvw_initializeBufferWithCopyOfBuffer
+ _swift_cvw_instantiateLayoutString
- _SecCertificateCopyExtensionValue
- _swift_allocateGenericValueMetadataWithLayoutString
- _swift_generic_assignWithCopy
- _swift_generic_assignWithTake
- _swift_generic_destroy
- _swift_generic_initWithCopy
- _swift_generic_initializeBufferWithCopyOfBuffer
- _swift_generic_instantiateLayoutString
CStrings:
+ "-[AKAppleIDAuthenticationService dealloc]"
+ "-[AKAppleIDAuthenticationService endProximityAuthenticationForContext:completion:]"
+ "@48@0:8@\"AKClient\"16@\"AKAppleIDAuthenticationContext\"24@\"SKSetupAppleIDSignInServer\"32@?<v@?@\"NSDictionary\"@\"NSError\">40"
+ "@48@0:8@16@24@32@?40"
+ "AKAttestationRequestData: signingDataHash: %@, headers: %@"
+ "Anisette succeeded, but BAA failed. This is not expected. Not blocking for error: %@"
+ "Began proximity authentication with service provider: %@ and active prox auth token: %@"
+ "Calling to end authentication for service provider: %@ with token: %@"
+ "Ended proximity authentication with error: %@"
+ "Ended proximity authentication with results: %s"
+ "Ended proximity authentication without results or an error"
+ "Forcing cancel error for potential buy flow"
+ "Not ending authentication because token does not match current server: %s != %s"
+ "Nullifying active prox auth token: %@"
+ "T@\"NSData\",R,N,V_signingDataHash"
+ "Token matches current server, ending proximity authentication: %s"
+ "_activeProximityAuthenticationToken"
+ "_getDCRTWithContext:completion:"
+ "_signingDataHash"
+ "endAuthenticationWithToken:"
+ "initWithSigningData:requiredHeaders:"
+ "sessionWithInitialMessage:secretDelegate:circleDelegate:dsid:altDSID:flowID:deviceSessionID:error:"
+ "sessionWithSecretDelegate:dsid:altDSID:flowID:deviceSessionID:error:"
+ "signingDataHash"
- "\v"
- "AKAttestationRequestData: bodyHash: %@, headers: %@"
- "Current DCRT missing required OID:%@, renew DCRT"
- "Internal: Override config from internal build: %@"
- "MAEIssueDCRTWithCompletion"
- "OID %@ is missing in the certificate"
- "OID %@ is present in the certificate"
- "Renewed DCRT also missing required OID:%@, returning error %ld"
- "T@\"NSData\",R,N,V_bodyDataHash"
- "_bodyDataHash"
- "_getDCRTWithContext:renewDCRT:completion:"
- "_issueDCRT:completion:"
- "_renewDCRTWithContext:completion:"
- "baa-cache-config"
- "bodyDataHash"
- "dcrtRenewalAttempted:"
- "kMAOptionsBAAOIDKeyUsageProperties"
- "kMAOptionsIgnoreExistingDCRT"
- "requiredOIDPresentInCertificates:"
- "setDCRTRenewalAttempted:forAccount:"
- "softlink:r:path:/System/Library/PrivateFrameworks/MobileActivation.framework/MobileActivation"
- "v48@0:8@\"AKClient\"16@\"AKAppleIDAuthenticationContext\"24@\"SKSetupAppleIDSignInServer\"32@?<v@?@\"NSDictionary\"@\"NSError\">40"

```
