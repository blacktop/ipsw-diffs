## fairplaydeviceidentityd

> `/usr/libexec/fairplaydeviceidentityd`

```diff

-1.18.0.0.0
-  __TEXT.__text: 0x3a94c8
-  __TEXT.__auth_stubs: 0x630
-  __TEXT.__objc_stubs: 0x1a0
-  __TEXT.__const: 0x33221
-  __TEXT.__gcc_except_tab: 0x58
-  __TEXT.__cstring: 0x2b8
-  __TEXT.__oslogstring: 0x245
-  __TEXT.__info_plist: 0x428
-  __TEXT.__objc_methname: 0xef
-  __TEXT.__unwind_info: 0x350
-  __TEXT.__eh_frame: 0x90
-  __DATA_CONST.__auth_got: 0x328
+1.22.0.0.0
+  __TEXT.__text: 0x408368
+  __TEXT.__auth_stubs: 0x3f0
+  __TEXT.__objc_stubs: 0x140
+  __TEXT.__const: 0x331f0
+  __TEXT.__gcc_except_tab: 0xb0
+  __TEXT.__cstring: 0x28f
+  __TEXT.__oslogstring: 0x188
+  __TEXT.__info_plist: 0x431
+  __TEXT.__objc_methname: 0xa9
+  __TEXT.__unwind_info: 0x200
+  __TEXT.__eh_frame: 0x88
+  __DATA_CONST.__auth_got: 0x208
   __DATA_CONST.__got: 0xd8
-  __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__const: 0x20c60
+  __DATA_CONST.__auth_ptr: 0x8
+  __DATA_CONST.__const: 0x225f0
   __DATA_CONST.__cfstring: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_intobj: 0x30
-  __DATA.__objc_selrefs: 0x68
-  __DATA.__data: 0xe30
-  __DATA.__common: 0xdc
+  __DATA_CONST.__objc_intobj: 0x48
+  __DATA.__objc_selrefs: 0x50
+  __DATA.__data: 0xdc8
+  __DATA.__common: 0xf4
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 254
-  Symbols:   191
-  CStrings:  59
+  Functions: 151
+  Symbols:   156
+  CStrings:  45
 
Symbols:
+ _DeviceIdentityCreateHostSignatureWithCompletion
+ _kMAOptionsBAANetworkTimeoutInterval
+ _memset_pattern16
+ _objc_release_x26
+ _objc_retain_x1
+ _objc_retain_x19
+ _objc_retain_x21
+ _ptrace
- _DeviceIdentityCreateHostSignature
- _OBJC_CLASS_$_NSMutableArray
- ___memcpy_chk
- _bzero
- _ccder_blob_decode_bitstring
- _ccder_blob_decode_tag
- _ccder_blob_decode_tl
- _ccder_blob_decode_uint64
- _ccder_blob_encode_tl
- _ccder_decode_rsa_pub_n
- _ccder_sizeof_len
- _ccder_sizeof_tag
- _ccdigest
- _ccdigest_init
- _ccdigest_update
- _ccec_compressed_x962_export_pub
- _ccec_compressed_x962_export_pub_size
- _ccec_compressed_x962_import_pub
- _ccec_cp_256
- _ccec_cp_384
- _ccec_cp_521
- _ccec_export_pub
- _ccec_import_pub
- _ccec_keysize_is_supported
- _ccec_verify
- _ccec_verify_composite
- _ccec_x963_import_pub_size
- _ccrsa_import_pub
- _ccrsa_verify_pkcs1v15_allowshortsigs
- _ccsha1_di
- _ccsha224_di
- _ccsha256_di
- _ccsha384_di
- _ccsha512_di
- _cczp_bitlen
- _difftime
- _memcmp
- _memset
- _objc_alloc
- _objc_autoreleaseReturnValue
- _objc_retain_x8
- _strptime
- _timegm
CStrings:
+ "Failed to obtain host certificates: %!@(MISSING)"
+ "Host Certificate(s) are expired: %!@(MISSING)"
+ "v32@?0@\"NSData\"8@\"NSArray\"16@\"NSError\"24"
- "%!F(MISSING)"
- "%!Y(MISSING)%!m(MISSING)%!d(MISSING)%!H(MISSING)%!M(MISSING)%!S(MISSING)Z"
- "%!y(MISSING)%!m(MISSING)%!d(MISSING)%!H(MISSING)%!M(MISSING)%!S(MISSING)Z"
- "2006-05-31"
- "Failed to copy intermediate certificate."
- "Failed to copy leaf certificate."
- "Failed to fetch host signature: %!@(MISSING)"
- "Failed to get host signature or cert chain."
- "Failed to obtain VM BAA certificates: %!@(MISSING)"
- "Failed to parse certificate set. rc=%!d(MISSING), numCerts=%!z(MISSING)u"
- "Invalid certData"
- "Savage - Factory"
- "Yonkers - Factory"
- "initWithBytes:length:"
- "initWithCapacity:"
- "setObject:atIndexedSubscript:"
- "ucrt"

```
