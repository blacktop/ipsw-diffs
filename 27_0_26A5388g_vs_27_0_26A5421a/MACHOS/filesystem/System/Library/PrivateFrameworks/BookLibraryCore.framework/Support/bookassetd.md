## bookassetd

> `/System/Library/PrivateFrameworks/BookLibraryCore.framework/Support/bookassetd`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__cfstring`
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
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-2309.0.0.0.0
-  __TEXT.__text: 0xcebe0
+2310.0.0.0.0
+  __TEXT.__text: 0xced88
   __TEXT.__auth_stubs: 0xc00
-  __TEXT.__objc_stubs: 0xb2e0
-  __TEXT.__objc_methlist: 0x5668
+  __TEXT.__objc_stubs: 0xb380
+  __TEXT.__objc_methlist: 0x5670
   __TEXT.__const: 0xa639
   __TEXT.__objc_classname: 0xb95
-  __TEXT.__objc_methname: 0xf746
+  __TEXT.__objc_methname: 0xf7ca
   __TEXT.__cstring: 0x327b
   __TEXT.__objc_methtype: 0x2ded
-  __TEXT.__oslogstring: 0xa0f0
+  __TEXT.__oslogstring: 0xa108
   __TEXT.__gcc_except_tab: 0x1ae4
-  __TEXT.__unwind_info: 0x1648
+  __TEXT.__unwind_info: 0x1650
   __TEXT.__eh_frame: 0x80
-  __DATA_CONST.__const: 0xa2f0
+  __DATA_CONST.__const: 0xa320
   __DATA_CONST.__cfstring: 0x3280
   __DATA_CONST.__objc_classlist: 0x2c0
   __DATA_CONST.__objc_catlist: 0x38

   __DATA_CONST.__got: 0x8d8
   __DATA_CONST.__auth_ptr: 0x8
   __DATA.__objc_const: 0x9e00
-  __DATA.__objc_selrefs: 0x3880
+  __DATA.__objc_selrefs: 0x38b0
   __DATA.__objc_ivar: 0x6a0
   __DATA.__objc_data: 0x1b80
   __DATA.__data: 0x1298

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2148
+  Functions: 2149
   Symbols:   496
-  CStrings:  3978
+  CStrings:  3984
 
CStrings:
+ "(dID=%{public}@) [Purchase-Mgr]: presentingSceneIdentifier: %@, auditToken.length: %lu"
+ "auditToken"
+ "bl_clientInfoForPurchase:auditTokenData:"
+ "callerBundleId"
+ "clientId"
+ "dq_performPurchaseWithRequest:downloadID:uiHostProxy:auditTokenData:completion:"
+ "initWithBytes:length:"
+ "setAuditTokenData:"
- "(dID=%{public}@) [Purchase-Mgr]: presentingSceneIdentifier: %@"
- "dq_performPurchaseWithRequest:downloadID:uiHostProxy:completion:"
```
