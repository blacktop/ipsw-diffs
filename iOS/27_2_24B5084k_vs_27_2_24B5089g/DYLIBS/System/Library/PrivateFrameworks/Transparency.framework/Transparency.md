## Transparency

> `/System/Library/PrivateFrameworks/Transparency.framework/Transparency`

```diff

-1766.40.47.0.0
-  __TEXT.__text: 0x7cc38
-  __TEXT.__objc_methlist: 0x4aa0
-  __TEXT.__cstring: 0x30dc
-  __TEXT.__const: 0x4ec0
+1766.40.50.0.0
+  __TEXT.__text: 0x7ce80
+  __TEXT.__objc_methlist: 0x4ad0
+  __TEXT.__cstring: 0x310c
+  __TEXT.__const: 0x4ed0
   __TEXT.__gcc_except_tab: 0x4ec
-  __TEXT.__oslogstring: 0x204b
+  __TEXT.__oslogstring: 0x20db
   __TEXT.__swift5_typeref: 0x10e4
   __TEXT.__swift5_reflstr: 0x9ca
   __TEXT.__swift5_assocty: 0x260

   __TEXT.__swift5_protos: 0xc
   __TEXT.__swift5_acfuncs: 0x1b8
   __TEXT.__swift5_capture: 0x2c4
-  __TEXT.__unwind_info: 0x33c8
+  __TEXT.__unwind_info: 0x33d0
   __TEXT.__eh_frame: 0x3840
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2038
+  __DATA_CONST.__objc_selrefs: 0x2058
   __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_superrefs: 0x180
   __DATA_CONST.__got: 0x660
-  __AUTH_CONST.__const: 0x3ff8
-  __AUTH_CONST.__cfstring: 0x3a80
-  __AUTH_CONST.__objc_const: 0x8020
+  __AUTH_CONST.__const: 0x4018
+  __AUTH_CONST.__cfstring: 0x3aa0
+  __AUTH_CONST.__objc_const: 0x8050
   __AUTH_CONST.__objc_intobj: 0x1e0
   __AUTH_CONST.__auth_got: 0xca0
-  __AUTH.__objc_data: 0x2d8
-  __AUTH.__data: 0x5e8
-  __DATA.__objc_ivar: 0x3b0
-  __DATA.__data: 0x10d0
+  __AUTH.__data: 0x98
+  __DATA.__objc_ivar: 0x3b4
+  __DATA.__data: 0x9f0
   __DATA.__common: 0x10
-  __DATA_DIRTY.__objc_data: 0x1af8
-  __DATA_DIRTY.__data: 0x230
+  __DATA_DIRTY.__objc_data: 0x1dd0
+  __DATA_DIRTY.__data: 0xe58
   __DATA_DIRTY.__bss: 0x910
   __DATA_DIRTY.__common: 0x30
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 3887
-  Symbols:   4335
-  CStrings:  783
+  Functions: 3893
+  Symbols:   4344
+  CStrings:  785
 
Symbols:
+ -[KTQueryOptions queryReason]
+ -[KTQueryOptions setQueryReason:]
+ -[KTVerifierResult showsTreeResetWarning]
+ -[KTVerifierResult updateTreeResetInProgress:]
+ -[KTVerifierResult updateWithStaticKeyEnforcedPeerEnforcement:isFailureIgnoredForDate:]
+ GCC_except_table160
+ GCC_except_table188
+ GCC_except_table221
+ _OBJC_IVAR_$_KTQueryOptions._queryReason
+ ___46-[KTVerifierResult updateTreeResetInProgress:]_block_invoke
+ ___87-[KTVerifierResult updateWithStaticKeyEnforcedPeerEnforcement:isFailureIgnoredForDate:]_block_invoke
+ _objc_msgSend$queryReason
+ _objc_msgSend$setQueryReason:
+ _objc_msgSend$showsTreeResetWarning
+ _objc_msgSend$updateWithStaticKeyEnforcedPeerEnforcement:isFailureIgnoredForDate:
- -[KTVerifierResult updateWithStaticKeyEnforcedPeerEnforcement:]
- GCC_except_table158
- GCC_except_table186
- GCC_except_table219
- ___63-[KTVerifierResult updateWithStaticKeyEnforcedPeerEnforcement:]_block_invoke
- _objc_msgSend$updateWithStaticKeyEnforcedPeerEnforcement:
CStrings:
+ "<KTQueryOptions: flags: %08x timeout: %f reason: %ld>"
+ "queryReason"
+ "updateTreeResetInProgress: %{mask.hash}@ was computed with treeReset=%{BOOL}d, no tree reset is in progress now, uiStatus %{public}@ is stale"
- "<KTQueryOptions: flags: %08x>"
```
