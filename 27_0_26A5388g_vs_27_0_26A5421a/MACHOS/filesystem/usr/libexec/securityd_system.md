## securityd_system

> `/usr/libexec/securityd_system`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__data`
- `__DATA.__thread_vars`

```diff

-62460.0.55.0.1
-  __TEXT.__text: 0x405a4
+62460.1.2.0.0
+  __TEXT.__text: 0x40bcc
   __TEXT.__auth_stubs: 0x1aa0
-  __TEXT.__objc_stubs: 0x1980
-  __TEXT.__objc_methlist: 0xf0c
+  __TEXT.__objc_stubs: 0x1a80
+  __TEXT.__objc_methlist: 0xf44
   __TEXT.__const: 0x270
-  __TEXT.__objc_classname: 0x2e5
-  __TEXT.__objc_methtype: 0xc82
-  __TEXT.__cstring: 0x863d
-  __TEXT.__objc_methname: 0x1fd0
-  __TEXT.__oslogstring: 0x42d9
+  __TEXT.__objc_classname: 0x2f6
+  __TEXT.__objc_methtype: 0xcb2
+  __TEXT.__cstring: 0x8678
+  __TEXT.__objc_methname: 0x207f
+  __TEXT.__oslogstring: 0x4330
   __TEXT.__gcc_except_tab: 0x304
-  __TEXT.__unwind_info: 0xc50
-  __DATA_CONST.__const: 0xb500
-  __DATA_CONST.__cfstring: 0x7f40
-  __DATA_CONST.__objc_classlist: 0xa0
+  __TEXT.__unwind_info: 0xc68
+  __DATA_CONST.__const: 0xb550
+  __DATA_CONST.__cfstring: 0x7fa0
+  __DATA_CONST.__objc_classlist: 0xa8
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_superrefs: 0x88
   __DATA_CONST.__objc_intobj: 0x90
   __DATA_CONST.__auth_got: 0xd60
-  __DATA_CONST.__got: 0x460
+  __DATA_CONST.__got: 0x470
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA.__objc_const: 0x1b18
-  __DATA.__objc_selrefs: 0x8f8
+  __DATA.__objc_const: 0x1ba8
+  __DATA.__objc_selrefs: 0x948
   __DATA.__objc_ivar: 0xd8
-  __DATA.__objc_data: 0x640
+  __DATA.__objc_data: 0x690
   __DATA.__data: 0x1580
   __DATA.__thread_vars: 0x30
   __DATA.__thread_bss: 0x10

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 1124
-  Symbols:   726
-  CStrings:  2094
+  Functions: 1130
+  Symbols:   728
+  CStrings:  2112
 
Symbols:
+ _NSURLErrorDomain
+ _OBJC_CLASS_$_NSURLComponents
CStrings:
+ "@40@0:8r*16Q24^@32"
+ "B32@0:8@16Q24"
+ "Deleting non-syncable password-evaluations items from class=%@ with multi-user view=%@"
+ "SecXPCNetworkURL"
+ "URL"
+ "allowedURLFromCString:options:error:"
+ "com.apple.password-manager.password-evaluations"
+ "componentsWithString:"
+ "host"
+ "http"
+ "https"
+ "initWithUTF8String:"
+ "isAllowedURL:options:"
+ "lowercaseString"
+ "scheme"
+ "scheme:isAllowedByOptions:"
+ "setError:code:"
+ "v32@0:8^@16q24"
```
