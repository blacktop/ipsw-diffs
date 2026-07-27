## WebContentRestrictions

> `/System/Library/PrivateFrameworks/WebContentRestrictions.framework/Versions/A/WebContentRestrictions`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__got`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-39.160.2.0.0
-  __TEXT.__text: 0xe1fc
+39.160.4.0.0
+  __TEXT.__text: 0xe274
   __TEXT.__auth_stubs: 0x990
   __TEXT.__objc_methlist: 0x670
   __TEXT.__const: 0x630
-  __TEXT.__cstring: 0x1051
+  __TEXT.__cstring: 0x1071
   __TEXT.__gcc_except_tab: 0x84
   __TEXT.__oslogstring: 0x2b6
   __TEXT.__swift5_typeref: 0x10c

   __DATA_CONST.__objc_arraydata: 0x78
   __AUTH_CONST.__auth_got: 0x4d8
   __AUTH_CONST.__const: 0x549
-  __AUTH_CONST.__cfstring: 0x10c0
+  __AUTH_CONST.__cfstring: 0x10e0
   __AUTH_CONST.__objc_const: 0xb20
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_intobj: 0x60

   - /usr/lib/swift/libswiftos.dylib
   Functions: 330
   Symbols:   1020
-  CStrings:  461
+  CStrings:  462
 
Functions:
~ -[WCRBrowserEngineClient _reloadConfiguration] : 704 -> 824
CStrings:
+ "Unloading bloom filter"
```
