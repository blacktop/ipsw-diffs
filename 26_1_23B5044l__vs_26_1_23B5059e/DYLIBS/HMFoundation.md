## HMFoundation

> `/System/Library/PrivateFrameworks/HMFoundation.framework/HMFoundation`

```diff

-892.0.0.0.0
-  __TEXT.__text: 0x88294
-  __TEXT.__auth_stubs: 0x21a0
-  __TEXT.__objc_methlist: 0x78c4
+893.0.0.0.0
+  __TEXT.__text: 0x88560
+  __TEXT.__auth_stubs: 0x21b0
+  __TEXT.__objc_methlist: 0x78fc
   __TEXT.__const: 0x2658
   __TEXT.__dlopen_cstrs: 0xf8
-  __TEXT.__cstring: 0x30aa
+  __TEXT.__cstring: 0x30af
   __TEXT.__swift5_typeref: 0x9e3
   __TEXT.__swift5_capture: 0x600
   __TEXT.__swift_as_entry: 0x168

   __TEXT.__oslogstring: 0x4213
   __TEXT.__gcc_except_tab: 0x1c68
   __TEXT.__ustring: 0x8
-  __TEXT.__unwind_info: 0x2ee8
+  __TEXT.__unwind_info: 0x2ef8
   __TEXT.__eh_frame: 0x2e98
-  __TEXT.__objc_classname: 0x110d
-  __TEXT.__objc_methname: 0xc84b
-  __TEXT.__objc_methtype: 0x27b4
-  __TEXT.__objc_stubs: 0x9320
+  __TEXT.__objc_classname: 0x111e
+  __TEXT.__objc_methname: 0xc8d3
+  __TEXT.__objc_methtype: 0x27d7
+  __TEXT.__objc_stubs: 0x93e0
   __DATA_CONST.__got: 0x7f0
   __DATA_CONST.__const: 0x1658
   __DATA_CONST.__objc_classlist: 0x460
   __DATA_CONST.__objc_catlist: 0xa8
-  __DATA_CONST.__objc_protolist: 0x1b0
+  __DATA_CONST.__objc_protolist: 0x1b8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3118
-  __DATA_CONST.__objc_protorefs: 0x28
+  __DATA_CONST.__objc_selrefs: 0x3140
+  __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x380
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__auth_got: 0x10e0
+  __AUTH_CONST.__auth_got: 0x10e8
   __AUTH_CONST.__const: 0x21d8
   __AUTH_CONST.__cfstring: 0x4b60
-  __AUTH_CONST.__objc_const: 0xe3c8
+  __AUTH_CONST.__objc_const: 0xe3f0
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x1130

   __AUTH.__thread_vars: 0x18
   __AUTH.__thread_bss: 0x8
   __DATA.__objc_ivar: 0x198
-  __DATA.__data: 0x2430
+  __DATA.__data: 0x2490
   __DATA.__bss: 0x514
   __DATA_DIRTY.__objc_ivar: 0x5b0
   __DATA_DIRTY.__objc_data: 0x1a40

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: BB337C48-2F32-3B7E-B27D-C09418E537C5
-  Functions: 3458
-  Symbols:   9418
-  CStrings:  4613
+  UUID: 932CBD67-7EFA-3C24-8EA3-45B12A0FA3DA
+  Functions: 3461
+  Symbols:   9436
+  CStrings:  4621
 
Symbols:
+ -[NSData(FastEncoding) hmf_readFastEncodableObjectAtOffset:]
+ -[NSMutableData(FastEncoding) hmf_appendFastEncodableObject:]
+ _HMFObjectInstanceKey
+ _NSClassFromString
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_HMFFastEncodable
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HMFFastEncodable
+ __OBJC_$_PROTOCOL_REFS_HMFFastEncodable
+ __OBJC_LABEL_PROTOCOL_$_HMFFastEncodable
+ __OBJC_PROTOCOL_$_HMFFastEncodable
+ __OBJC_PROTOCOL_REFERENCE_$_HMFFastEncodable
+ ___block_literal_global.142
+ _objc_msgSend$allKeysForObject:
+ _objc_msgSend$hmf_appendFastEncodableObject:
+ _objc_msgSend$hmf_encodeForFastEncoder
+ _objc_msgSend$hmf_readFastEncodableObjectAtOffset:
+ _objc_msgSend$initWithFastEncodedData:
+ _objc_msgSend$numberWithUnsignedLong:
- ___block_literal_global.136
Functions:
+ -[NSData(FastEncoding) hmf_readFastEncodableObjectAtOffset:]
~ -[NSData(FastEncoding) hmf_readObjectAtOffset:] : 896 -> 924
+ -[NSMutableData(FastEncoding) hmf_appendFastEncodableObject:]
~ -[NSMutableData(FastEncoding) hmf_appendObject:] : 364 -> 420
~ -[HMFKeyValueDatabase _syncWithoutTimerHandling:] : 564 -> 672
+ _HMFObjectInstanceKey
CStrings:
+ "@\"NSData\"16@0:8"
+ "@24@0:8@\"NSData\"16"
+ "HMFFastEncodable"
+ "Unexpected object type %@ (%@) in hmf_appendObject"
+ "allKeysForObject:"
+ "hmf_appendFastEncodableObject:"
+ "hmf_encodeForFastEncoder"
+ "hmf_readFastEncodableObjectAtOffset:"
+ "initWithFastEncodedData:"
- "Unexpected object type %@ in hmf_appendObject"

```
