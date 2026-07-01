## securityd

> `/usr/libexec/securityd`

```diff

-  __TEXT.__text: 0x282cfc
+  __TEXT.__text: 0x2839f0
   __TEXT.__auth_stubs: 0x4230
-  __TEXT.__objc_stubs: 0x1d200
-  __TEXT.__objc_methlist: 0x159c8
-  __TEXT.__const: 0x919
-  __TEXT.__cstring: 0x2180d
-  __TEXT.__objc_methname: 0x2d593
-  __TEXT.__oslogstring: 0x2efe2
+  __TEXT.__objc_stubs: 0x1d240
+  __TEXT.__objc_methlist: 0x159d0
+  __TEXT.__const: 0x921
+  __TEXT.__cstring: 0x21835
+  __TEXT.__objc_methname: 0x2d5d9
+  __TEXT.__oslogstring: 0x2f22f
   __TEXT.__swift5_typeref: 0x378
   __TEXT.__swift5_fieldmd: 0x120
   __TEXT.__objc_classname: 0x25d7
-  __TEXT.__objc_methtype: 0xa9f0
+  __TEXT.__objc_methtype: 0xaa08
   __TEXT.__constg_swiftt: 0x274
   __TEXT.__swift5_reflstr: 0xc3
   __TEXT.__swift5_capture: 0x1bc

   __TEXT.__swift5_types: 0x20
   __TEXT.__swift_as_entry: 0x40
   __TEXT.__swift_as_ret: 0x3c
-  __TEXT.__gcc_except_tab: 0xb760
+  __TEXT.__gcc_except_tab: 0xb87c
   __TEXT.__dlopen_cstrs: 0xb4
   __TEXT.__ustring: 0x28
-  __TEXT.__unwind_info: 0x6f48
+  __TEXT.__unwind_info: 0x6f50
   __TEXT.__eh_frame: 0xa58
   __DATA_CONST.__auth_got: 0x2128
   __DATA_CONST.__got: 0x13c0
   __DATA_CONST.__auth_ptr: 0x1d8
-  __DATA_CONST.__const: 0x14768
-  __DATA_CONST.__cfstring: 0x1be40
+  __DATA_CONST.__const: 0x14790
+  __DATA_CONST.__cfstring: 0x1be60
   __DATA_CONST.__objc_classlist: 0x8f8
   __DATA_CONST.__objc_catlist: 0x68
   __DATA_CONST.__objc_protolist: 0x258

   __DATA_CONST.__objc_dictobj: 0x78
   __DATA_CONST.__objc_arrayobj: 0x360
   __DATA.__objc_const: 0x234c8
-  __DATA.__objc_selrefs: 0x9638
+  __DATA.__objc_selrefs: 0x9640
   __DATA.__objc_ivar: 0x1a78
   __DATA.__objc_data: 0x5ca8
   __DATA.__data: 0x30f8

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 9820
+  Functions: 9822
   Symbols:   1867
-  CStrings:  20060
+  CStrings:  20072
 
Sections:
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__swift5_fieldmd : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_capture : content changed
~ __TEXT.__swift5_assocty : content changed
~ __TEXT.__swift5_builtin : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift5_types : content changed
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift_as_ret : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__got : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__objc_dictobj : content changed
~ __DATA_CONST.__objc_arrayobj : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_data : content changed
~ __DATA.__data : content changed
~ __DATA.__bss : content changed
CStrings:
+ "B52@0:8@16@24@32B40^@44"
+ "Couldn't verify signature of TLKShare (%@) that includes tlkOwnershipProof as part of dataForSigning; trying again without tlkOwnershipProof"
+ "Existing TLKShare's ownership proof for peer %@ from self %@ is invalid. Will update TLK Share %@"
+ "Existing TLKShare's signature for peer %@ from self %@ is invalid. Will update TLK Share %@"
+ "Proposed TLKShare(%@) supercedes existing TLKShare(%@)"
+ "Unable to generate TLK ownership proof: %@"
+ "active user: %d"
+ "com.apple.FileProvider.usermanager.sync"
+ "dataForSigning:includeProof:"
+ "onlyDelete: %{BOOL}d, copyCloudAuthToken: %{BOOL}d, copyMobileMail: %{BOOL}d, copyNSURLSession: %{BOOL}d, copyPCS: %{BOOL}d"
+ "unknown service: %@"
+ "verifySignature:verifyingPeer:acceptProoflessSig:error:"
+ "verifySignature:verifyingPeer:ckrecord:acceptProoflessSig:error:"
- "verifySignature:verifyingPeer:ckrecord:error:"
- "verifySignature:verifyingPeer:error:"

```
