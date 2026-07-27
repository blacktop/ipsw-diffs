## ProtectedCloudStorage

> `/System/Library/PrivateFrameworks/ProtectedCloudStorage.framework/Versions/A/ProtectedCloudStorage`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__got`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-1188.160.10.0.0
-  __TEXT.__text: 0x72734
+1188.160.11.0.0
+  __TEXT.__text: 0x726c0
   __TEXT.__auth_stubs: 0x1740
-  __TEXT.__objc_methlist: 0x1ee8
+  __TEXT.__objc_methlist: 0x1ef8
   __TEXT.__const: 0x3d0
   __TEXT.__cstring: 0xdf31
-  __TEXT.__oslogstring: 0x3e15
-  __TEXT.__gcc_except_tab: 0x3784
+  __TEXT.__oslogstring: 0x3d85
+  __TEXT.__gcc_except_tab: 0x376c
   __TEXT.__dlopen_cstrs: 0x214
   __TEXT.__unwind_info: 0x18a8
   __TEXT.__objc_classname: 0x314
-  __TEXT.__objc_methname: 0x502c
+  __TEXT.__objc_methname: 0x5043
   __TEXT.__objc_methtype: 0x135d
-  __TEXT.__objc_stubs: 0x41e0
+  __TEXT.__objc_stubs: 0x4200
   __DATA_CONST.__got: 0x5e8
   __DATA_CONST.__const: 0x1690
   __DATA_CONST.__objc_classlist: 0x118
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1518
+  __DATA_CONST.__objc_selrefs: 0x1520
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xf0
   __DATA_CONST.__objc_arraydata: 0x4240

   - /usr/lib/libheimdal-asn1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 2151
-  Symbols:   4294
-  CStrings:  4886
+  Functions: 2152
+  Symbols:   4296
+  CStrings:  4885
 
Symbols:
+ +[PCSAccountsModel inducedFailureEnabled:]
+ _objc_msgSend$inducedFailureEnabled:
Functions:
+ +[PCSAccountsModel inducedFailureEnabled:]
~ _PCSDBRRepairWrappingKeyFromEscrowIdentityOuterBlob : 1928 -> 1772
~ _PCSIdentityGenerateBlobForPasswordChange : 540 -> 268
CStrings:
+ "Failure %@ induced (defaults %@/%@)"
+ "inducedFailureEnabled:"
- "Disallowing repair with escrow identity operation (due to %@/%@)"
- "Injecting error into blob generation (due to %@/%@)"
- "PCSIdentityGenerateBlobForPasswordChange: forceFail = %{BOOL}d"
```
