## securityd

> `/usr/libexec/securityd`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-62460.2.2.0.0
-  __TEXT.__text: 0x26ccb4
+62460.2.3.0.0
+  __TEXT.__text: 0x26cad8
   __TEXT.__auth_stubs: 0x4340
-  __TEXT.__objc_stubs: 0x1d9c0
-  __TEXT.__objc_methlist: 0x15ea0
+  __TEXT.__objc_stubs: 0x1d9a0
+  __TEXT.__objc_methlist: 0x15e98
   __TEXT.__const: 0x910
-  __TEXT.__cstring: 0x22791
-  __TEXT.__objc_methname: 0x2e68f
-  __TEXT.__oslogstring: 0x2feb3
+  __TEXT.__cstring: 0x227a6
+  __TEXT.__objc_methname: 0x2e67f
+  __TEXT.__oslogstring: 0x2feaa
   __TEXT.__swift5_typeref: 0x372
   __TEXT.__swift5_fieldmd: 0x120
   __TEXT.__objc_classname: 0x2559

   __TEXT.__swift_as_entry: 0x40
   __TEXT.__swift_as_ret: 0x3c
   __TEXT.__swift_as_cont: 0x48
-  __TEXT.__gcc_except_tab: 0xa074
+  __TEXT.__gcc_except_tab: 0xa078
   __TEXT.__dlopen_cstrs: 0xb4
   __TEXT.__ustring: 0x28
-  __TEXT.__unwind_info: 0x6a70
+  __TEXT.__unwind_info: 0x6a68
   __TEXT.__eh_frame: 0xa60
-  __DATA_CONST.__const: 0x149b8
-  __DATA_CONST.__cfstring: 0x1c520
+  __DATA_CONST.__const: 0x149c0
+  __DATA_CONST.__cfstring: 0x1c540
   __DATA_CONST.__objc_classlist: 0x910
   __DATA_CONST.__objc_catlist: 0x68
   __DATA_CONST.__objc_protolist: 0x260

   __DATA_CONST.__got: 0x1530
   __DATA_CONST.__auth_ptr: 0x1d8
   __DATA.__objc_const: 0x23cd8
-  __DATA.__objc_selrefs: 0x98a8
+  __DATA.__objc_selrefs: 0x98a0
   __DATA.__objc_ivar: 0x1ae8
   __DATA.__objc_data: 0x5d98
   __DATA.__data: 0x3150

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 9918
+  Functions: 9917
   Symbols:   1890
   CStrings:  16411
 
CStrings:
+ "Couldn't verify signature of TLKShare (%@) without tlkOwnershipProof as part of dataForSigning; trying again with tlkOwnershipProof"
+ "PhotoRevocationCheck"
+ "verifySignature:verifyingPeer:acceptSigWithProof:error:"
+ "verifySignature:verifyingPeer:ckrecord:acceptSigWithProof:error:"
- "Couldn't verify signature of TLKShare (%@) that includes tlkOwnershipProof as part of dataForSigning; trying again without tlkOwnershipProof"
- "dataForSigning"
- "verifySignature:verifyingPeer:acceptProoflessSig:error:"
- "verifySignature:verifyingPeer:ckrecord:acceptProoflessSig:error:"
```
