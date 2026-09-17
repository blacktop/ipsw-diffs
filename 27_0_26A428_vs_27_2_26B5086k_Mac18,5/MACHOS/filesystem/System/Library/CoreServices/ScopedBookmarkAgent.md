## ScopedBookmarkAgent

> `/System/Library/CoreServices/ScopedBookmarkAgent`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`

```diff

-609.0.0.0.0
-  __TEXT.__text: 0xc29c
+609.1.3.0.0
+  __TEXT.__text: 0xc790
   __TEXT.__auth_stubs: 0xb30
   __TEXT.__objc_stubs: 0xca0
   __TEXT.__objc_methlist: 0x208
-  __TEXT.__gcc_except_tab: 0x10e8
+  __TEXT.__gcc_except_tab: 0x1180
   __TEXT.__const: 0x8c
   __TEXT.__objc_methname: 0xad8
-  __TEXT.__cstring: 0x1224
-  __TEXT.__oslogstring: 0x178c
+  __TEXT.__cstring: 0x12b5
+  __TEXT.__oslogstring: 0x17a4
   __TEXT.__objc_classname: 0x13
   __TEXT.__objc_methtype: 0x15c
-  __TEXT.__unwind_info: 0x4a8
+  __TEXT.__unwind_info: 0x4b8
   __DATA_CONST.__const: 0x170
-  __DATA_CONST.__cfstring: 0x980
+  __DATA_CONST.__cfstring: 0x9a0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x10

   __DATA_CONST.__objc_arraydata: 0x28
   __DATA_CONST.__objc_arrayobj: 0x48
   __DATA_CONST.__auth_got: 0x5a8
-  __DATA_CONST.__got: 0x238
+  __DATA_CONST.__got: 0x240
   __DATA_CONST.__auth_ptr: 0x10
   __DATA.__objc_const: 0x470
   __DATA.__objc_selrefs: 0x348

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 192
-  Symbols:   566
-  CStrings:  437
+  Functions: 199
+  Symbols:   571
+  CStrings:  443
 
Symbols:
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_14
+ _ZL40handle_revocable_copy_bundle_identifiersPU24objcproto13OS_xpc_object8NSObjectS1_13audit_token_t
+ _kCFErrorDomainPOSIX
CStrings:
+ "%s: PID %u not entitled"
+ "com.apple.private.security.files.bookmarks.manage-revocable"
+ "copy-revocable-clients"
+ "copy-revocable-identifiers"
+ "revoke-client"
+ "set-revocable-status"
```
