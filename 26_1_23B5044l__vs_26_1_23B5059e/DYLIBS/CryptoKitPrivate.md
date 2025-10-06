## CryptoKitPrivate

> `/System/Library/PrivateFrameworks/CryptoKitPrivate.framework/CryptoKitPrivate`

```diff

-324.40.3.0.0
-  __TEXT.__text: 0x8cc20
-  __TEXT.__auth_stubs: 0x1ed0
-  __TEXT.__objc_methlist: 0x994
+324.40.4.0.0
+  __TEXT.__text: 0x8cf60
+  __TEXT.__auth_stubs: 0x1ee0
+  __TEXT.__objc_methlist: 0x9e4
   __TEXT.__const: 0x4df0
   __TEXT.__cstring: 0x2445
-  __TEXT.__swift5_typeref: 0x1546
-  __TEXT.__swift5_reflstr: 0x1d1b
+  __TEXT.__swift5_typeref: 0x1520
+  __TEXT.__swift5_reflstr: 0x1d3b
   __TEXT.__swift5_assocty: 0x2f8
-  __TEXT.__constg_swiftt: 0x205c
-  __TEXT.__swift5_fieldmd: 0x22d4
+  __TEXT.__constg_swiftt: 0x2084
+  __TEXT.__swift5_fieldmd: 0x2304
   __TEXT.__swift5_builtin: 0x140
   __TEXT.__swift5_proto: 0x28c
   __TEXT.__swift5_types: 0x290

   __TEXT.__swift5_capture: 0x70
   __TEXT.__swift5_mpenum: 0x18
   __TEXT.__unwind_info: 0x19e0
-  __TEXT.__eh_frame: 0x4788
+  __TEXT.__eh_frame: 0x46a8
   __TEXT.__objc_classname: 0x1a9
-  __TEXT.__objc_methname: 0x1364
-  __TEXT.__objc_methtype: 0x4ad
-  __TEXT.__objc_stubs: 0x7e0
+  __TEXT.__objc_methname: 0x1490
+  __TEXT.__objc_methtype: 0x498
+  __TEXT.__objc_stubs: 0x840
   __DATA_CONST.__got: 0x4b0
   __DATA_CONST.__const: 0xb0
   __DATA_CONST.__objc_classlist: 0x138
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x460
+  __DATA_CONST.__objc_selrefs: 0x488
   __DATA_CONST.__objc_superrefs: 0x78
-  __AUTH_CONST.__auth_got: 0xf70
+  __AUTH_CONST.__auth_got: 0xf78
   __AUTH_CONST.__const: 0x4198
   __AUTH_CONST.__cfstring: 0x80
-  __AUTH_CONST.__objc_const: 0x21d8
+  __AUTH_CONST.__objc_const: 0x2208
   __AUTH.__objc_data: 0x860
   __AUTH.__data: 0x598
-  __DATA.__objc_ivar: 0x8c
-  __DATA.__data: 0x17e8
+  __DATA.__objc_ivar: 0x90
+  __DATA.__data: 0x17c8
   __DATA.__bss: 0x4b00
   __DATA.__common: 0x100
-  __DATA_DIRTY.__objc_data: 0x9a0
+  __DATA_DIRTY.__objc_data: 0x9c8
   __DATA_DIRTY.__data: 0xd58
   __DATA_DIRTY.__common: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 0B965C6F-43F6-352F-9227-62D5A930F716
-  Functions: 2121
-  Symbols:   1458
-  CStrings:  497
+  UUID: 6DC7B776-8965-38D7-A031-575192B771FF
+  Functions: 2135
+  Symbols:   1463
+  CStrings:  504
 
Symbols:
+ +[ATHMAwaitingActivation verifyAndGetKeyIDFromKeyCommitmentsData:numBuckets:deploymentID:]
+ -[ATHMAwaitingActivation activateWithResponseData:error:]
+ -[ATHMAwaitingActivation initWithKeyCommitmentsData:nbuckets:deploymentID:error:]
+ -[ATHMPresentation deploymentID]
+ -[ATHMTestServer initWithNumBuckets:deploymentID:error:]
+ -[ATHMTestServer respondWithRequestData:metadata:error:]
+ _OBJC_IVAR_$_ATHMPresentation._deploymentID
+ _objc_msgSend$getKeyIDWithKeyCommitmentsData:
+ _objc_msgSend$initWithKeyCommitmentsData:numBuckets:deploymentID:error:
+ _objc_msgSend$initWithNumBuckets:deploymentID:
+ _objc_msgSend$numBuckets
+ _objc_msgSend$verifyWithKeyCommitmentsData:numBuckets:deploymentID:
+ _objc_retain_x10
+ _symbolic _____y______y_____GG 16CryptoKitPrivate4ATHMO13TokenResponseV AA04CoreA11HashToCurveV 0aB04P256O
+ _symbolic _____y______y_____GG 16CryptoKitPrivate4ATHMO6ClientV AA04CoreA11HashToCurveV 0aB04P256O
+ _symbolic _____y______y_____GG 16CryptoKitPrivate4ATHMO6ServerV AA04CoreA11HashToCurveV 0aB04P256O
+ _symbolic _____y_____y_____GG s23_ContiguousArrayStorageC 16CryptoKitPrivate04CoreD11GroupScalarV 0dE04P256O
- +[ATHMAwaitingActivation verifyKeyCommitmentsData:]
- -[ATHMAwaitingActivation activateWithResponseData:nbuckets:error:]
- -[ATHMAwaitingActivation initWithKeyCommitmentsData:error:]
- -[ATHMTestServer initWithError:]
- -[ATHMTestServer respondWithRequestData:metadata:nbuckets:error:]
- _objc_msgSend$initWithKeyCommitmentsData:error:
- _objc_msgSend$verifyWithKeyCommitmentsData:
- _symbolic Say_____y_____GG 16CryptoKitPrivate04CoreA11GroupScalarV 0aB04P384O
- _symbolic _____y______y_____GG 16CryptoKitPrivate4ATHMO13TokenResponseV AA04CoreA11HashToCurveV 0aB04P384O
- _symbolic _____y______y_____GG 16CryptoKitPrivate4ATHMO6ClientV AA04CoreA11HashToCurveV 0aB04P384O
- _symbolic _____y______y_____GG 16CryptoKitPrivate4ATHMO6ServerV AA04CoreA11HashToCurveV 0aB04P384O
- _symbolic _____y_____y_____GG 16CryptoKitPrivate6ProverV AA04CoreA11HashToCurveV 0aB04P384O
- _symbolic _____y_____y_____GG s23_ContiguousArrayStorageC 16CryptoKitPrivate04CoreD11GroupScalarV 0dE04P384O
CStrings:
+ "@\"NSString\""
+ "@32@0:8q16@24"
+ "@40@0:8@16Q24@32"
+ "@40@0:8Q16@24^@32"
+ "@48@0:8@16Q24@32^@40"
+ "@48@0:8@16q24@32^@40"
+ "B40@0:8@16q24@32"
+ "CryptoKitPrivate.ATHMServer"
+ "T@\"NSString\",R,N,V_deploymentID"
+ "TokenResponseProof"
+ "_deploymentID"
+ "deploymentID"
+ "getKeyIDWithKeyCommitmentsData:"
+ "initWithKeyCommitmentsData:nbuckets:deploymentID:error:"
+ "initWithKeyCommitmentsData:numBuckets:deploymentID:error:"
+ "initWithNumBuckets:deploymentID:"
+ "initWithNumBuckets:deploymentID:error:"
+ "numBuckets"
+ "respondWithRequestData:metadata:error:"
+ "verifyAndGetKeyIDFromKeyCommitmentsData:numBuckets:deploymentID:"
+ "verifyWithKeyCommitmentsData:numBuckets:deploymentID:"
- "@48@0:8@16@24q32^@40"
- "ATHMV1-P384-SHA384-KeyCommitments"
- "ATHMV1-P384-SHA384-TokenResponseProof"
- "B24@0:8@16"
- "HashToGroup-ATHMV1-P384-SHA384-generatorH"
- "activateWithResponseData:nbuckets:error:"
- "initWithError:"
- "initWithKeyCommitmentsData:error:"
- "q40@0:8@16q24^@32"
- "verifyKeyCommitmentsData:"
- "verifyWithKeyCommitmentsData:"

```
