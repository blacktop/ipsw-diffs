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
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-3892.100.1.0.0
-  __TEXT.__text: 0x82f18
+3896.100.1.2.1
+  __TEXT.__text: 0x82eb8
   __TEXT.__auth_stubs: 0x11d0
   __TEXT.__lazy_helpers: 0xfc
   __TEXT.__objc_stubs: 0xa940
   __TEXT.__objc_methlist: 0x61bc
   __TEXT.__const: 0x270
-  __TEXT.__gcc_except_tab: 0xe5b0
-  __TEXT.__cstring: 0x3a7e
-  __TEXT.__objc_methname: 0xf154
+  __TEXT.__gcc_except_tab: 0xe5d4
+  __TEXT.__cstring: 0x3a89
+  __TEXT.__objc_methname: 0xf03c
   __TEXT.__objc_classname: 0xb94
   __TEXT.__objc_methtype: 0x2f57
   __TEXT.__oslogstring: 0xf76e
-  __TEXT.__unwind_info: 0x2de8
-  __DATA_CONST.__const: 0x15c8
-  __DATA_CONST.__cfstring: 0x1da0
+  __TEXT.__unwind_info: 0x2df0
+  __DATA_CONST.__const: 0x15c0
+  __DATA_CONST.__cfstring: 0x1dc0
   __DATA_CONST.__objc_classlist: 0x238
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x130

   __DATA_CONST.__auth_got: 0x900
   __DATA_CONST.__got: 0x7a0
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA.__objc_const: 0x8e38
+  __DATA.__objc_const: 0x8cf8
   __DATA.__objc_selrefs: 0x3718
-  __DATA.__objc_ivar: 0x6f8
+  __DATA.__objc_ivar: 0x6d0
   __DATA.__objc_data: 0x1630
   __DATA.__lazy_load_got: 0x18
   __DATA.__data: 0xe4c

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 2073
+  Functions: 2074
   Symbols:   516
-  CStrings:  3852
+  CStrings:  3843
 
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
