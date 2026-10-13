## SpotlightServices

> `/System/Library/PrivateFrameworks/SpotlightServices.framework/SpotlightServices`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`

```diff

-2465.1.7.0.0
-  __TEXT.__text: 0x15c264
-  __TEXT.__objc_methlist: 0xe648
-  __TEXT.__const: 0x2e38
+2465.1.9.0.0
+  __TEXT.__text: 0x15c6b4
+  __TEXT.__objc_methlist: 0xe688
+  __TEXT.__const: 0x2e48
   __TEXT.__cstring: 0x3a99a
   __TEXT.__gcc_except_tab: 0x5058
-  __TEXT.__oslogstring: 0xbc0b
+  __TEXT.__oslogstring: 0xbd0b
   __TEXT.__ustring: 0x892
   __TEXT.__dlopen_cstrs: 0x12f
   __TEXT.__swift5_typeref: 0x1e8

   __TEXT.__swift5_proto: 0xc
   __TEXT.__swift5_types: 0x18
   __TEXT.__swift5_capture: 0xa4
-  __TEXT.__unwind_info: 0x4070
+  __TEXT.__unwind_info: 0x4090
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8dd0
+  __DATA_CONST.__objc_selrefs: 0x8df8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x428
   __DATA_CONST.__objc_arraydata: 0x4778
   __DATA_CONST.__got: 0x1c40
   __AUTH_CONST.__const: 0x2b80
-  __AUTH_CONST.__cfstring: 0x36c60
+  __AUTH_CONST.__cfstring: 0x36c80
   __AUTH_CONST.__objc_const: 0x181f0
   __AUTH_CONST.__objc_intobj: 0x4788
   __AUTH_CONST.__objc_arrayobj: 0xc90

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 6461
-  Symbols:   11509
-  CStrings:  7943
+  Functions: 6468
+  Symbols:   11513
+  CStrings:  7947
 
Symbols:
+ +[SPKQuery appScopeBundleIdentifiers]
+ +[SPKQuery isAllowedUnderAppScopeInContext:]
+ -[SPSearchQueryContext appScopeBundleIdentifier]
+ -[SPSearchQueryContext appScopeEntity]
+ -[SPSearchQueryContext isAppScopedSearch]
+ GCC_except_table39
- GCC_except_table22
- GCC_except_table37
CStrings:
+ "(unresolved)"
+ "[qid=%lu][AppScope] %{public}@ is in a multi-producer domain but declares no appScopeBundleIdentifiers — denying under app scope %{public}@ rather than leaking."
+ "[qid=%lu][AppScope] Bundle ID: %{public}@"
+ "[qid=%lu][AppScope] Detected app-scoped search"
```
