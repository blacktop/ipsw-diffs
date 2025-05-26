## MessageSecurity

> `/System/Library/PrivateFrameworks/MessageSecurity.framework/MessageSecurity`

```diff

-101.40.6.0.0
-  __TEXT.__text: 0x34be0
-  __TEXT.__auth_stubs: 0xe80
-  __TEXT.__objc_methlist: 0x19b8
-  __TEXT.__const: 0x7e0
-  __TEXT.__gcc_except_tab: 0x4e8
-  __TEXT.__cstring: 0x3257
-  __TEXT.__oslogstring: 0x533
+101.100.4.0.0
+  __TEXT.__text: 0x35b70
+  __TEXT.__auth_stubs: 0xea0
+  __TEXT.__objc_methlist: 0x19c0
+  __TEXT.__const: 0x7f0
+  __TEXT.__gcc_except_tab: 0x5c8
+  __TEXT.__cstring: 0x33c7
+  __TEXT.__oslogstring: 0x646
   __TEXT.__swift5_typeref: 0x136
   __TEXT.__swift5_capture: 0x10
   __TEXT.__constg_swiftt: 0x218

   __TEXT.__swift5_types: 0x34
   __TEXT.__swift5_builtin: 0x8c
   __TEXT.__swift5_proto: 0x4
-  __TEXT.__unwind_info: 0x1708
-  __TEXT.__eh_frame: 0x8a0
+  __TEXT.__unwind_info: 0x1648
+  __TEXT.__eh_frame: 0x808
   __TEXT.__objc_classname: 0x2b3
-  __TEXT.__objc_methname: 0x3ca8
-  __TEXT.__objc_methtype: 0x1668
+  __TEXT.__objc_methname: 0x3d02
+  __TEXT.__objc_methtype: 0x1690
   __TEXT.__objc_stubs: 0x2640
   __DATA_CONST.__got: 0x210
-  __DATA_CONST.__const: 0x3e70
+  __DATA_CONST.__const: 0x3ec0
   __DATA_CONST.__objc_classlist: 0xd8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x3548
-  __DATA_CONST.__objc_selrefs: 0xd48
+  __DATA_CONST.__objc_selrefs: 0xd50
+  __DATA_CONST.__objc_protorefs: 0x18
+  __DATA_CONST.__objc_classrefs: 0x138
+  __DATA_CONST.__objc_superrefs: 0xa8
   __AUTH_CONST.__cfstring: 0x2420
   __AUTH_CONST.__objc_const: 0x0
-  __AUTH_CONST.__const: 0x148
+  __AUTH_CONST.__const: 0x248
   __AUTH_CONST.__auth_ptr: 0x10
-  __AUTH_CONST.__auth_got: 0x750
+  __AUTH_CONST.__auth_got: 0x760
   __AUTH.__objc_data: 0x0
-  __DATA.__objc_protorefs: 0x18
-  __DATA.__objc_classrefs: 0x138
-  __DATA.__objc_superrefs: 0xa8
   __DATA.__objc_ivar: 0x1a4
   __DATA.__data: 0x1068
   __DATA.__bss: 0x1a0
   __DATA.__common: 0x2711
-  __DATA_DIRTY.__const: 0xac0
+  __DATA_DIRTY.__const: 0xae0
   __DATA_DIRTY.__objc_const: 0xaf0
   __DATA_DIRTY.__objc_data: 0xa38
   __DATA_DIRTY.__data: 0x80

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 1680
-  Symbols:   3831
-  CStrings:  1194
+  Functions: 1682
+  Symbols:   3861
+  CStrings:  1219
 
Symbols:
+ -[MSCMSSignerInfo initWithCertificate:signatureAlgorithm:useIssuerAndSerialNumber:error:]
+ GCC_except_table39
+ ___61+[MSCMSSignedData decodeMessageSecurityObject:options:error:]_block_invoke
+ ___61+[MSCMSSignedData decodeMessageSecurityObject:options:error:]_block_invoke.114
+ ___61+[MSCMSSignedData decodeMessageSecurityObject:options:error:]_block_invoke.117
+ ___block_descriptor_56_e8_32s40r48r_e15_v32?08Q16^B24lr40l8r48l8s32l8
+ ___block_descriptor_64_e8_32s40r48r56r_e15_v32?08Q16^B24lr40l8r48l8r56l8s32l8
+ ___block_literal_global.113
+ ___block_literal_global.116
+ ___block_literal_global.119
+ ___block_literal_global.154
+ ___block_literal_global.202
+ ___block_literal_global.40
+ ___block_literal_global.45
+ ___block_literal_global.48
+ ___block_literal_global.55
+ ___block_literal_global.59
+ ___findCertificateByIssuerAndSerialNumber_block_invoke.38
+ ___findCertificateByIssuerAndSerialNumber_block_invoke.43
+ ___findCertificateByIssuerAndSerialNumber_block_invoke.46
+ ___findCertificateByIssuerAndSerialNumber_block_invoke_2
+ ___findCertificateBySubjectKeyID_block_invoke.57
+ ___findCertificateBySubjectKeyID_block_invoke_2
+ _objc_retain_x13
- GCC_except_table16
- GCC_except_table33
- GCC_except_table38
- ___block_literal_global.132
- ___block_literal_global.180
- _swift_unknownObjectRelease_n
- _swift_unknownObjectRetain_n
CStrings:
+ "@44@0:8^{__SecCertificate=}16@24B32^@36"
+ "BundledIssuer"
+ "BundledIssuer = %{mask.hash}@"
+ "BundledSKID"
+ "BundledSKID = %{mask.hash}@"
+ "BundledSN"
+ "BundledSN = %{mask.hash}@"
+ "Fatal error"
+ "Negative value is not representable"
+ "No certificates in SignedData"
+ "Not enough bits to represent the passed value"
+ "QueryIssuer"
+ "QueryIssuer = %{mask.hash}@"
+ "QuerySKID"
+ "QuerySKID = %{mask.hash}@"
+ "QuerySN"
+ "QuerySN = %{mask.hash}@"
+ "Swift/Integers.swift"
+ "Swift/UnsafePointer.swift"
+ "T@\"NSString\",?,R,C"
+ "UnsafeMutablePointer.initialize overlapping range"
+ "UnsafeMutablePointer.moveInitialize with negative count"
+ "initWithCertificate:signatureAlgorithm:useIssuerAndSerialNumber:error:"
+ "skipping non-certificate CertificateChoice at %u"
+ "unable to parse certificate at %u"

```
