## AuthKit

> `/System/Library/PrivateFrameworks/AuthKit.framework/AuthKit`

```diff

-493.458.3.2.0
-  __TEXT.__text: 0xd16d4
+493.460.2.0.0
+  __TEXT.__text: 0xd1ec4
   __TEXT.__auth_stubs: 0xda0
-  __TEXT.__objc_methlist: 0xce9c
+  __TEXT.__objc_methlist: 0xcec4
   __TEXT.__const: 0x22f1
-  __TEXT.__cstring: 0xe1f8
-  __TEXT.__oslogstring: 0x1055f
-  __TEXT.__gcc_except_tab: 0x54b0
+  __TEXT.__cstring: 0xe201
+  __TEXT.__oslogstring: 0x106a4
+  __TEXT.__gcc_except_tab: 0x5480
   __TEXT.__ustring: 0x1b8
   __TEXT.__dlopen_cstrs: 0x16c
-  __TEXT.__unwind_info: 0x3d78
+  __TEXT.__unwind_info: 0x3d90
   __TEXT.__objc_classname: 0x1a7e
-  __TEXT.__objc_methname: 0x203e4
+  __TEXT.__objc_methname: 0x204a6
   __TEXT.__objc_methtype: 0x43ad
-  __TEXT.__objc_stubs: 0xe520
+  __TEXT.__objc_stubs: 0xe580
   __DATA_CONST.__got: 0x9b0
-  __DATA_CONST.__const: 0x5720
+  __DATA_CONST.__const: 0x5770
   __DATA_CONST.__objc_classlist: 0x5c8
   __DATA_CONST.__objc_catlist: 0x88
   __DATA_CONST.__objc_protolist: 0x1e0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6a28
+  __DATA_CONST.__objc_selrefs: 0x6a40
   __DATA_CONST.__objc_protorefs: 0xd8
   __DATA_CONST.__objc_superrefs: 0x398
   __DATA_CONST.__objc_arraydata: 0x1c8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 5903
-  Symbols:   8029
-  CStrings:  9198
+  Functions: 5912
+  Symbols:   8039
+  CStrings:  9204
 
CStrings:
+ "AKAttestationRequestData: signingDataHash: %@, headers: %@"
+ "Allow reprovision for hostname: %{private}@, with keyword:  %{private}@"
+ "No GS keywords returned from idMS, allowing reprovision request for hostname: %{private}@"
+ "Passcode protected: %@ _requirePassword: %@ missingCK: %@"
+ "Reprovision not allowed, the requesting URL is not a GS endpoint."
+ "Reprovision request is not allow for hostname: %{private}@, because it does not contain any keyword from: %{private}@"
+ "T@\"NSData\",R,N,V_signingDataHash"
+ "_attestationDataForRequestData:completion:"
+ "_attestationDataForRequestData:error:"
+ "_handleAnisetteReprovisionWithRequestURL:anisetteController:completion:"
+ "_handleAnisetteURLResponse:forRequest:withCompletion:"
+ "_signingDataHash"
+ "attestationDataForRequestData:error:"
+ "disableDeviceBAA"
+ "disableVMBAA"
+ "grandSlamEndpointIdentifiersWithCompletion:"
+ "gsEndpointIdentifiers"
+ "initWithSigningData:requiredHeaders:"
+ "shouldAllowReprovisionForHostName:completion:"
+ "signingDataHash"
- "AKAttestationRequestData: bodyHash: %@, headers: %@"
- "Exception caught when fetching dcrtRenewalAttempted: %@"
- "Passcode protected: %@"
- "T@\"NSData\",R,N,V_bodyDataHash"
- "_attestationDataForRequest:completion:"
- "_attestationDataForRequest:error:"
- "_bodyDataHash"
- "_handleAnissetteURLResponse:forRequest:withCompletion:"
- "bodyDataHash"
- "dcrtRenewalAttempted"
- "dcrtRenewalAttempted:"
- "deviceBAADisabled"
- "setDCRTRenewalAttempted:forAccount:"
- "vmBAADisabled"

```
