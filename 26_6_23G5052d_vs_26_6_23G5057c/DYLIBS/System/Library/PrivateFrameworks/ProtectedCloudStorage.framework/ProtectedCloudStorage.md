## ProtectedCloudStorage

> `/System/Library/PrivateFrameworks/ProtectedCloudStorage.framework/ProtectedCloudStorage`

```diff

-  __TEXT.__text: 0x6fddc
+  __TEXT.__text: 0x6fd68
   __TEXT.__auth_stubs: 0x1940
-  __TEXT.__objc_methlist: 0x2020
+  __TEXT.__objc_methlist: 0x2030
   __TEXT.__const: 0x3c8
   __TEXT.__cstring: 0xe097
-  __TEXT.__oslogstring: 0x3e75
-  __TEXT.__gcc_except_tab: 0x3834
+  __TEXT.__oslogstring: 0x3de5
+  __TEXT.__gcc_except_tab: 0x381c
   __TEXT.__dlopen_cstrs: 0x2c5
   __TEXT.__unwind_info: 0x1928
   __TEXT.__objc_classname: 0x326
-  __TEXT.__objc_methname: 0x556e
+  __TEXT.__objc_methname: 0x5585
   __TEXT.__objc_methtype: 0x15ef
-  __TEXT.__objc_stubs: 0x4440
+  __TEXT.__objc_stubs: 0x4460
   __DATA_CONST.__got: 0x678
   __DATA_CONST.__const: 0x2ef0
   __DATA_CONST.__objc_classlist: 0x118
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1650
+  __DATA_CONST.__objc_selrefs: 0x1658
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xf0
   __DATA_CONST.__objc_arraydata: 0x4240

   - /usr/lib/libheimdal-asn1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 2123
-  Symbols:   6455
-  CStrings:  8182
+  Functions: 2124
+  Symbols:   6458
+  CStrings:  8181
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__got : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH.__objc_data : content changed
~ __AUTH.__data : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
~ __DATA_DIRTY.__data : content changed
Symbols:
+ +[PCSAccountsModel inducedFailureEnabled:]
+ _objc_msgSend$inducedFailureEnabled:
Functions:
+ +[PCSAccountsModel inducedFailureEnabled:]
~ _PCSDBRRepairWrappingKeyFromEscrowIdentityOuterBlob : 1872 -> 1724
~ _PCSIdentityGenerateBlobForPasswordChange : 528 -> 264
CStrings:
+ "Failure %@ induced (defaults %@/%@)"
+ "inducedFailureEnabled:"
- "Disallowing repair with escrow identity operation (due to %@/%@)"
- "Injecting error into blob generation (due to %@/%@)"
- "PCSIdentityGenerateBlobForPasswordChange: forceFail = %{BOOL}d"

```
