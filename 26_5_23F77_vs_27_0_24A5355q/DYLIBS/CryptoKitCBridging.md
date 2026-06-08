## CryptoKitCBridging

> `/System/Library/PrivateFrameworks/CryptoKitCBridging.framework/CryptoKitCBridging`

```diff

-324.100.35.0.0
-  __TEXT.__text: 0x2064
-  __TEXT.__auth_stubs: 0x460
+381.0.0.0.0
+  __TEXT.__text: 0x2044
   __TEXT.__objc_methlist: 0x1f8
   __TEXT.__const: 0x40
   __TEXT.__cstring: 0x23
   __TEXT.__unwind_info: 0xe8
-  __TEXT.__objc_classname: 0x40
-  __TEXT.__objc_methname: 0x3b1
-  __TEXT.__objc_methtype: 0x33b
-  __TEXT.__objc_stubs: 0x240
-  __DATA_CONST.__got: 0x40
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x130
   __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__auth_got: 0x238
+  __DATA_CONST.__got: 0x40
   __AUTH_CONST.__objc_const: 0x368
+  __AUTH_CONST.__auth_got: 0x248
   __DATA.__objc_ivar: 0x18
   __DATA_DIRTY.__objc_data: 0x140
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/Security.framework/Security
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 55E6BFB6-3D83-378E-85DF-10C45D001611
+  UUID: 217C5421-42ED-3871-9DD4-2881B0513861
   Functions: 55
-  Symbols:   226
-  CStrings:  76
+  Symbols:   228
+  CStrings:  1
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_release_x23
+ _objc_retain
+ _objc_retain_x2
+ _objc_retain_x4
- _objc_retain_x21
- _objc_retain_x22
- _objc_retain_x25
Functions:
~ _ccrng_generate_bridge -> +[CKCBCorecryptoECPoint groupOrderByteCountForCP:] : 36 -> 44
~ +[CKCBCorecryptoECPoint groupOrderByteCountForCP:] -> _ccrng_generate_bridge : 48 -> 36
~ _keyIsCompactRepresentable : 344 -> 340
~ -[CKCBCorecryptoECScalar x963Representation] : 652 -> 636
~ -[CKCBCorecryptoECScalar initWithRandomScalarInGroup:] : 204 -> 196
~ -[CKCBCorecryptoECScalar initWithData:inGroup:reduction:corecryptoError:] : 336 -> 340
~ -[CKCBCorecryptoECScalar serializedBigEndianScalar] : 280 -> 276
CStrings:
- "@16@0:8"
- "@20@0:8B16"
- "@24@0:8^{__SecAccessControl=}16"
- "@24@0:8^{ccec_cp=QQ^{cczp_funcs}[1Q]}16"
- "@24@0:8^{ccec_pub_ctx=^{ccec_cp}[0{ccec_projective_point=[1Q]}]}16"
- "@32@0:8@16^i24"
- "@32@0:8@16^{ccec_cp=QQ^{cczp_funcs}[1Q]}24"
- "@32@0:8^Q16^{ccec_cp=QQ^{cczp_funcs}[1Q]}24"
- "@32@0:8^{ccec_affine_point=[1Q]}16^{ccec_cp=QQ^{cczp_funcs}[1Q]}24"
- "@32@0:8^{ccss_shamir_parameters=I{cczp=QQ^{cczp_funcs}[1Q]}}16^{ccss_shamir_share=^{cczp}I[0Q]}24"
- "@36@0:8^{ccss_shamir_parameters=I{cczp=QQ^{cczp_funcs}[1Q]}}16I24@28"
- "@44@0:8@16^{ccec_cp=QQ^{cczp_funcs}[1Q]}24B32^i36"
- "B24@0:8@16"
- "CKCBCorecryptoECPoint"
- "CKCBCorecryptoECScalar"
- "CKSSShare"
- "I16@0:8"
- "Q"
- "Q24@0:8^{ccec_cp=QQ^{cczp_funcs}[1Q]}16"
- "SEPUtils"
- "T^{ccec_affine_point=[1Q]},R,N,V_point"
- "T^{ccec_cp=QQ^{cczp_funcs}[1Q]},R,N,V_group"
- "Tr^Q,R,N,V_corecryptoScalar"
- "^{ccec_affine_point=[1Q]}"
- "^{ccec_affine_point=[1Q]}16@0:8"
- "^{ccec_cp=QQ^{cczp_funcs}[1Q]}"
- "^{ccec_cp=QQ^{cczp_funcs}[1Q]}16@0:8"
- "^{ccss_shamir_share=^{cczp}I[0Q]}"
- "^{ccss_shamir_share=^{cczp}I[0Q]}16@0:8"
- "_corecryptoScalar"
- "_group"
- "_newZeroingDataWithBytes:length:"
- "_point"
- "_share"
- "_share_size"
- "add:corecryptoError:"
- "bytes"
- "compressedx962PointByteCountForCurveParameters:"
- "corecryptoScalar"
- "dataFromACL:"
- "dataWithLength:"
- "dealloc"
- "group"
- "groupOrderByteCountForCP:"
- "init"
- "initFromPublicKeyBytes:inGroup:compressed:corecryptoError:"
- "initPoint:onGroup:"
- "initWithData:inGroup:reduction:corecryptoError:"
- "initWithGeneratorForCP:"
- "initWithLength:"
- "initWithParams:share:"
- "initWithParams:x:y:"
- "initWithPublicKey:"
- "initWithRandomScalarInGroup:"
- "initWithScalarPointer:forGroup:"
- "initWithx963Representation:group:"
- "inverseModOrder"
- "isEqual:"
- "length"
- "mapToCurve_SSWU_RandomOracle"
- "multiply:corecryptoError:"
- "mutableBytes"
- "point"
- "pointAllocationSizeForGroup:"
- "r^Q"
- "r^Q16@0:8"
- "scalarAllocationSizeForGroup:"
- "serializedBigEndianScalar"
- "serializedPublicKey:"
- "share"
- "sub:corecryptoError:"
- "v16@0:8"
- "x"
- "x963Representation"
- "y"

```
