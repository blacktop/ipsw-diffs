## nsurlsessiond

> `/usr/libexec/nsurlsessiond`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
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
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-3892.100.1.0.0
-  __TEXT.__text: 0x63828
+3896.100.1.1.1
+  __TEXT.__text: 0x637d0
   __TEXT.__auth_stubs: 0xf00
   __TEXT.__lazy_helpers: 0xfc
   __TEXT.__objc_stubs: 0x8b00
   __TEXT.__objc_methlist: 0x31bc
   __TEXT.__const: 0x260
-  __TEXT.__gcc_except_tab: 0xc5e4
-  __TEXT.__objc_methname: 0xb61d
+  __TEXT.__gcc_except_tab: 0xc604
+  __TEXT.__objc_methname: 0xb505
   __TEXT.__objc_classname: 0x4e5
-  __TEXT.__cstring: 0x3266
+  __TEXT.__cstring: 0x3271
   __TEXT.__objc_methtype: 0x2030
   __TEXT.__oslogstring: 0xdfab
-  __TEXT.__unwind_info: 0x2148
-  __DATA_CONST.__const: 0x1340
-  __DATA_CONST.__cfstring: 0x1440
+  __TEXT.__unwind_info: 0x2150
+  __DATA_CONST.__const: 0x1338
+  __DATA_CONST.__cfstring: 0x1460
   __DATA_CONST.__objc_classlist: 0xd8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xe8

   __DATA_CONST.__auth_got: 0x798
   __DATA_CONST.__got: 0x618
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA.__objc_const: 0x4528
+  __DATA.__objc_const: 0x43e8
   __DATA.__objc_selrefs: 0x2a08
-  __DATA.__objc_ivar: 0x420
+  __DATA.__objc_ivar: 0x3f8
   __DATA.__objc_data: 0x870
   __DATA.__lazy_load_got: 0x18
   __DATA.__data: 0xae4

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 1138
+  Functions: 1139
   Symbols:   438
-  CStrings:  2980
+  CStrings:  2971
 
CStrings:
+ "atsContext"
- "_deleteAllSessionsForBundleIDStmt"
- "_deleteEntriesForSessionStmt"
- "_deleteSessionStmt"
- "_getAllSessionsStmt"
- "_insertOrUpdateSessionConfigurationStmt"
- "_insertOrUpdateSessionOptionsStmt"
- "_selectEntriesStmt"
- "_selectSessionConfigurationStmt"
- "_selectSessionOptionsStmt"
- "_selectUniqueBundleIDsStmt"
```
