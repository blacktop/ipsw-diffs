## PowerlogCore

> `/System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__cstring`
- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__got`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_nlclslist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-  __TEXT.__text: 0xe6704
+  __TEXT.__text: 0xe69a4
   __TEXT.__auth_stubs: 0x1ac0
   __TEXT.__objc_methlist: 0x8ad8
   __TEXT.__const: 0x1b70
   __TEXT.__cstring: 0x3d012
-  __TEXT.__oslogstring: 0x7ef8
+  __TEXT.__oslogstring: 0x7f93
   __TEXT.__gcc_except_tab: 0x2944
-  __TEXT.__unwind_info: 0x3030
+  __TEXT.__unwind_info: 0x3038
   __TEXT.__objc_classname: 0x90f
   __TEXT.__objc_methname: 0x1319e
   __TEXT.__objc_methtype: 0x1917

   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libsystemstats.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 4633
+  Functions: 4635
   Symbols:   8806
-  CStrings:  17555
+  CStrings:  17558
 
Functions:
~ -[PLSubmissions handleDRConfigUpdate:error:] : 676 -> 976
+ ___44-[PLSubmissions handleDRConfigUpdate:error:]_block_invoke.112
~ -[PLSubmissions taskingModeSetup] : 1532 -> 1552
+ -[PLSubmissions handleDRConfigUpdate:error:].cold.2
CStrings:
+ "Correcting MSS cycle interval from DRConfig: %llu cycles"
+ "DRConfig cancelled, scheduling task mode exit..."
+ "Failed to correct MSS cycle interval to %llu: %d"
```
