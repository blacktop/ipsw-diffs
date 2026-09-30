## CloudServices

> `/System/Library/PrivateFrameworks/CloudServices.framework/CloudServices`

```diff

-638.40.5.0.0
-  __TEXT.__text: 0x1dd60
-  __TEXT.__auth_stubs: 0xa10
+638.40.8.0.0
+  __TEXT.__text: 0x1de40
+  __TEXT.__auth_stubs: 0x9c0
   __TEXT.__objc_methlist: 0x10ec
   __TEXT.__const: 0xc90
-  __TEXT.__cstring: 0x1bb8
+  __TEXT.__cstring: 0x1b51
   __TEXT.__gcc_except_tab: 0x59c
-  __TEXT.__oslogstring: 0x203d
-  __TEXT.__unwind_info: 0x6b8
+  __TEXT.__oslogstring: 0x1ef9
+  __TEXT.__unwind_info: 0x6a0
   __TEXT.__objc_classname: 0x15f
-  __TEXT.__objc_methname: 0x3634
-  __TEXT.__objc_methtype: 0xae4
-  __TEXT.__objc_stubs: 0x27e0
-  __DATA_CONST.__got: 0x238
+  __TEXT.__objc_methname: 0x361f
+  __TEXT.__objc_methtype: 0xa93
+  __TEXT.__objc_stubs: 0x2820
+  __DATA_CONST.__got: 0x210
   __DATA_CONST.__const: 0xac0
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xd70
+  __DATA_CONST.__objc_selrefs: 0xd78
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x40
   __DATA_CONST.__objc_arraydata: 0x30
-  __AUTH_CONST.__auth_got: 0x518
+  __AUTH_CONST.__auth_got: 0x4f0
   __AUTH_CONST.__auth_ptr: 0x10
   __AUTH_CONST.__const: 0xc0
-  __AUTH_CONST.__cfstring: 0x19e0
+  __AUTH_CONST.__cfstring: 0x19a0
   __AUTH_CONST.__objc_const: 0x22e8
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_arrayobj: 0x48

   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 676
-  Symbols:   444
-  CStrings:  1211
+  Functions: 673
+  Symbols:   434
+  CStrings:  1199
 
Symbols:
- _kSecAttrKeyClassPrivate
- _kCFAllocatorNull
- _ccrsa_export_priv
- _kSecAttrKeyType
- _CFDataCreateWithBytesNoCopy
- _kSecAttrKeyClass
- ___memcpy_chk
- _kSecAttrKeyTypeRSA
- _ccrsa_export_priv_size
- _SecKeyCreateWithData
CStrings:
+ "@32@0:8@16^{ccrsa_full_ctx=QQ^{cczp_funcs}[1Q]}24"
+ "Error decoding recovery record"
+ "derivePassword"
+ "dataUsingEncoding:"
+ "salt_len (%!z(MISSING)u) out of bounds (0,%!z(MISSING)u]"
+ "failed to serialize escrow data"
+ "Escrow data too long (%!z(MISSING)u)"
+ "encodedEscrowRecordWithPublicKeyBytes:error:"
+ "srpResponseForEscrowBlob:withFullCCKey:"
- "initWithDSID:escrowRecordContents:recoveryPassphrase:recordID:recordLabel:"
- "Escrow data too long"
- "Could not generate key"
- "@56@0:8@16@24@32@40@48"
- "Escrow data too long: %!l(MISSING)u"
- "failed to extra bytes of priv key"
- "CKVR_SRP_SALT_LEN %!d(MISSING) != packet_salt_len %!z(MISSING)u"
- "failed to create data buffer"
- "recoveryPassphrase could not be converted to cstring"
- "error serializing escrow data: %!@(MISSING)"
- "cannot create key"
- "ccses->salt_len %!d(MISSING) != salt_len %!z(MISSING)d"
- "srpResponseForEscrowBlob:withKey:withFullCCKey:"
- "could not create priv key: %!@(MISSING)"
- "@40@0:8@16^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}24^{ccrsa_full_ctx=QQ^{cczp_funcs}[1Q]}32"
- "initWithRequest:"

```
