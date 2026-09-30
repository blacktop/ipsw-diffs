## TrustedPeersHelper

> `/System/Library/Frameworks/Security.framework/XPCServices/TrustedPeersHelper.xpc/TrustedPeersHelper`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_entry`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__swift5_capture`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-62460.2.2.0.0
-  __TEXT.__text: 0x2acff0
+62460.2.3.0.0
+  __TEXT.__text: 0x2ad1e0
   __TEXT.__auth_stubs: 0x24c0
-  __TEXT.__objc_stubs: 0x61c0
-  __TEXT.__objc_methlist: 0x2944
+  __TEXT.__objc_stubs: 0x61a0
+  __TEXT.__objc_methlist: 0x293c
   __TEXT.__const: 0xd700
   __TEXT.__cstring: 0x17d47
   __TEXT.__swift5_typeref: 0x408a
-  __TEXT.__oslogstring: 0xe064
+  __TEXT.__oslogstring: 0xe05b
   __TEXT.__swift5_entry: 0x8
   __TEXT.__objc_classname: 0x14bb
-  __TEXT.__objc_methname: 0x92c1
+  __TEXT.__objc_methname: 0x92b1
   __TEXT.__objc_methtype: 0x2a00
   __TEXT.__constg_swiftt: 0x3cc8
   __TEXT.__swift5_fieldmd: 0x2bf8

   __TEXT.__swift5_capture: 0x5268
   __TEXT.__dlopen_cstrs: 0x1c2
   __TEXT.__swift5_protos: 0x1c
-  __TEXT.__unwind_info: 0x5008
+  __TEXT.__unwind_info: 0x5000
   __TEXT.__eh_frame: 0x7ff0
   __DATA_CONST.__const: 0x14fc8
   __DATA_CONST.__cfstring: 0x1880

   __DATA_CONST.__got: 0xaa8
   __DATA_CONST.__auth_ptr: 0x768
   __DATA.__objc_const: 0x6f90
-  __DATA.__objc_selrefs: 0x1f18
+  __DATA.__objc_selrefs: 0x1f10
   __DATA.__objc_ivar: 0x1fc
   __DATA.__objc_data: 0x2c98
   __DATA.__data: 0x85c0

   - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 8948
+  Functions: 8947
   Symbols:   589
-  CStrings:  3259
+  CStrings:  3258
 
CStrings:
+ "Couldn't verify signature of TLKShare (%@) without tlkOwnershipProof as part of dataForSigning; trying again with tlkOwnershipProof"
+ "verifySignature:verifyingPeer:ckrecord:acceptSigWithProof:error:"
- "Couldn't verify signature of TLKShare (%@) that includes tlkOwnershipProof as part of dataForSigning; trying again without tlkOwnershipProof"
- "dataForSigning:"
- "verifySignature:verifyingPeer:ckrecord:acceptProoflessSig:error:"
```
