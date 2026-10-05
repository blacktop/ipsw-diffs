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
- `__TEXT.__swift5_types`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-62460.40.56.502.1
-  __TEXT.__text: 0x267540
+62460.40.74.0.0
+  __TEXT.__text: 0x268358
   __TEXT.__auth_stubs: 0x4340
-  __TEXT.__objc_stubs: 0x1da60
-  __TEXT.__objc_methlist: 0x15ec0
+  __TEXT.__objc_stubs: 0x1db60
+  __TEXT.__objc_methlist: 0x15f30
   __TEXT.__const: 0x910
-  __TEXT.__cstring: 0x22bde
-  __TEXT.__objc_methname: 0x2e77f
-  __TEXT.__oslogstring: 0x2ff32
+  __TEXT.__cstring: 0x22c4d
+  __TEXT.__objc_methname: 0x2e916
+  __TEXT.__oslogstring: 0x2ff6b
   __TEXT.__swift5_typeref: 0x372
   __TEXT.__swift5_fieldmd: 0x120
   __TEXT.__objc_classname: 0x2577
-  __TEXT.__objc_methtype: 0xb0cf
+  __TEXT.__objc_methtype: 0xb0f7
   __TEXT.__constg_swiftt: 0x274
   __TEXT.__swift5_reflstr: 0xc3
   __TEXT.__swift5_capture: 0x1bc

   __TEXT.__swift_as_ret: 0x3c
   __TEXT.__swift_as_cont: 0x48
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__gcc_except_tab: 0xa124
+  __TEXT.__gcc_except_tab: 0xa12c
   __TEXT.__ustring: 0x28
-  __TEXT.__unwind_info: 0x7cd0
+  __TEXT.__unwind_info: 0x7cf0
   __TEXT.__eh_frame: 0xa60
-  __DATA_CONST.__const: 0x14a28
-  __DATA_CONST.__cfstring: 0x1c760
+  __DATA_CONST.__const: 0x14ab8
+  __DATA_CONST.__cfstring: 0x1c780
   __DATA_CONST.__objc_classlist: 0x910
   __DATA_CONST.__objc_catlist: 0x68
   __DATA_CONST.__objc_protolist: 0x268

   __DATA_CONST.__auth_got: 0x21b0
   __DATA_CONST.__got: 0x1558
   __DATA_CONST.__auth_ptr: 0x1d8
-  __DATA.__objc_const: 0x23d18
-  __DATA.__objc_selrefs: 0x98d8
-  __DATA.__objc_ivar: 0x1aec
+  __DATA.__objc_const: 0x23d80
+  __DATA.__objc_selrefs: 0x9918
+  __DATA.__objc_ivar: 0x1af4
   __DATA.__objc_data: 0x5d98
   __DATA.__data: 0x31b8
   __DATA.__thread_vars: 0xc0

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 9922
+  Functions: 9934
   Symbols:   1895
-  CStrings:  16443
+  CStrings:  16459
 
CStrings:
+ "-[CuttlefishXPCWrapper notifyPeerTrustEstablishedWithSpecificUser:reply:]_block_invoke"
+ "@\"CKKSLocalResetOperation\""
+ "@?24@0:8@?16"
+ "B32@0:8^@16q24"
+ "T@\"CKKSLocalResetOperation\",&,V_lastLocalResetOperation"
+ "T@\"OTMetricsSessionData\",&,V_watchedFlowSessionMetrics"
+ "_lastLocalResetOperation"
+ "_watchedFlowSessionMetrics"
+ "claimWatchedFlowSessionMetrics"
+ "lastLocalResetOperation"
+ "notifyPeerTrustEstablishedWithSpecificUser:reply:"
+ "octagon: failed to notify TPH of trust establishment: %@"
+ "releaseWatchedFlowSessionMetrics:"
+ "setLastLocalResetOperation:"
+ "setWatchedFlowSessionMetrics:"
+ "watchedFlowSessionMetrics"
+ "wrapReplyReleasingWatchedFlowSessionMetrics:"
- "v32@0:8^@16q24"
```
