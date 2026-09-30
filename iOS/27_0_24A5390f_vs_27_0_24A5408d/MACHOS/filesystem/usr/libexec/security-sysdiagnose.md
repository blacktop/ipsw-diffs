## security-sysdiagnose

> `/usr/libexec/security-sysdiagnose`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-62460.0.55.0.1
+62460.2.1.0.0
   __TEXT.__text: 0x3de0
   __TEXT.__auth_stubs: 0x7f0
   __TEXT.__objc_stubs: 0x520
-  __TEXT.__objc_methlist: 0xd0
-  __TEXT.__const: 0x70
+  __TEXT.__objc_methlist: 0xdc
+  __TEXT.__const: 0x68
   __TEXT.__gcc_except_tab: 0x1a8
   __TEXT.__objc_classname: 0x3c
-  __TEXT.__objc_methname: 0x411
-  __TEXT.__objc_methtype: 0x17e
+  __TEXT.__objc_methname: 0x42d
+  __TEXT.__objc_methtype: 0x1a7
   __TEXT.__cstring: 0xe28
   __TEXT.__oslogstring: 0xa8
   __TEXT.__unwind_info: 0xf8

   __DATA_CONST.__auth_got: 0x408
   __DATA_CONST.__got: 0x120
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA.__objc_const: 0x190
-  __DATA.__objc_selrefs: 0x190
+  __DATA.__objc_const: 0x198
+  __DATA.__objc_selrefs: 0x198
   __DATA.__objc_data: 0x50
   __DATA.__data: 0x60
   __DATA.__bss: 0x10

   - /usr/lib/libsqlite3.dylib
   Functions: 34
   Symbols:   175
-  CStrings:  210
+  CStrings:  212
 
CStrings:
+ "resetMetricsForTopic:reply:"
+ "v32@0:8@\"NSString\"16@?<v@?B@\"NSError\">24"
```
