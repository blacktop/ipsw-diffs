## iconservicesagent

> `/System/Library/CoreServices/iconservicesagent`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-793.1.7.0.0
-  __TEXT.__text: 0x7874
-  __TEXT.__auth_stubs: 0x650
-  __TEXT.__objc_stubs: 0x1a20
-  __TEXT.__objc_methlist: 0x54c
+793.1.10.0.0
+  __TEXT.__text: 0x74ac
+  __TEXT.__auth_stubs: 0x640
+  __TEXT.__objc_stubs: 0x1a40
+  __TEXT.__objc_methlist: 0x53c
   __TEXT.__const: 0x68
-  __TEXT.__cstring: 0x7ce
-  __TEXT.__oslogstring: 0xcb9
-  __TEXT.__gcc_except_tab: 0x1c8
+  __TEXT.__cstring: 0x7c5
+  __TEXT.__oslogstring: 0xca1
+  __TEXT.__gcc_except_tab: 0x2d8
   __TEXT.__objc_classname: 0xd8
-  __TEXT.__objc_methtype: 0x449
-  __TEXT.__objc_methname: 0x186c
-  __TEXT.__unwind_info: 0x278
+  __TEXT.__objc_methtype: 0x426
+  __TEXT.__objc_methname: 0x184f
+  __TEXT.__unwind_info: 0x298
   __DATA_CONST.__const: 0x320
-  __DATA_CONST.__cfstring: 0xa80
+  __DATA_CONST.__cfstring: 0xa40
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x28

   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x28
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA_CONST.__auth_got: 0x338
+  __DATA_CONST.__auth_got: 0x330
   __DATA_CONST.__got: 0x1e0
-  __DATA.__objc_const: 0xa90
+  __DATA.__objc_const: 0xa88
   __DATA.__objc_selrefs: 0x800
   __DATA.__objc_ivar: 0x64
   __DATA.__objc_data: 0x1e0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 133
-  Symbols:   173
-  CStrings:  535
+  Functions: 140
+  Symbols:   172
+  CStrings:  533
 
Symbols:
- _objc_retain_x28
CStrings:
+ "%@"
+ "B24@?0@\"NSURL\"8@\"NSError\"16"
+ "CacheContents"
+ "Error enumerating store contents: %@"
+ "Failed to assemble diagnostics bundle"
+ "Failed to produce UUID from store entry name: %@"
+ "Failed to produce image from store unit for UUID %@"
+ "Image collection had errors during diagnostics bundle: %@"
+ "UUID %@ failed to produce store unit"
+ "UUIDString"
+ "com.apple.iconservices.diagnostics"
+ "localizedDescription"
- "Failed to copy cache contents"
- "Failed to create archive directory"
- "Failed to create bundle directory"
- "Failed to write dump.txt"
- "Icon cache not found"
- "Image encoding had errors during diagnostics archive: %@"
- "Image encoding had errors during minimal diagnostics archive: %@"
- "Index"
- "Minimal diagnostics archive collection requires an internal build"
- "Store"
- "collectMinimalDiagnosticsArchiveWithReply:"
- "fileExistsAtPath:"
- "minimal diagnostics archive collection"
- "v24@0:8@?<v@?@\"NSURL\"@\"NSError\">16"
```
