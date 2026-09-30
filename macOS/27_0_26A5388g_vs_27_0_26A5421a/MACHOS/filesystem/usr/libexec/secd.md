## secd

> `/usr/libexec/secd`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA.__data`

```diff

-62460.0.55.0.1
-  __TEXT.__text: 0x28a3cc
-  __TEXT.__auth_stubs: 0x40e0
-  __TEXT.__objc_stubs: 0x1d7e0
-  __TEXT.__objc_methlist: 0x15e50
+62460.1.2.0.0
+  __TEXT.__text: 0x28ab4c
+  __TEXT.__auth_stubs: 0x40d0
+  __TEXT.__objc_stubs: 0x1d8a0
+  __TEXT.__objc_methlist: 0x15ea0
   __TEXT.__const: 0x920
-  __TEXT.__objc_classname: 0x24f5
-  __TEXT.__objc_methname: 0x2e47a
-  __TEXT.__objc_methtype: 0xafe1
+  __TEXT.__objc_classname: 0x2506
+  __TEXT.__objc_methname: 0x2e53a
+  __TEXT.__objc_methtype: 0xb011
   __TEXT.__constg_swiftt: 0x274
   __TEXT.__swift5_typeref: 0x35e
   __TEXT.__swift5_reflstr: 0xc7

   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_proto: 0x24
   __TEXT.__swift5_types: 0x20
-  __TEXT.__cstring: 0x218cc
-  __TEXT.__oslogstring: 0x2f97c
+  __TEXT.__cstring: 0x21922
+  __TEXT.__oslogstring: 0x2f9d3
   __TEXT.__swift5_capture: 0x1bc
   __TEXT.__swift_as_entry: 0x40
   __TEXT.__swift_as_ret: 0x3c
   __TEXT.__swift_as_cont: 0x48
   __TEXT.__gcc_except_tab: 0xa0a8
   __TEXT.__dlopen_cstrs: 0xb4
-  __TEXT.__unwind_info: 0x6988
+  __TEXT.__unwind_info: 0x69a0
   __TEXT.__eh_frame: 0xa60
-  __DATA_CONST.__const: 0x15988
-  __DATA_CONST.__cfstring: 0x1b9c0
-  __DATA_CONST.__objc_classlist: 0x908
+  __DATA_CONST.__const: 0x15a08
+  __DATA_CONST.__cfstring: 0x1ba40
+  __DATA_CONST.__objc_classlist: 0x910
   __DATA_CONST.__objc_catlist: 0x68
   __DATA_CONST.__objc_protolist: 0x258
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x68
   __DATA_CONST.__objc_superrefs: 0x810
-  __DATA_CONST.__objc_intobj: 0x1410
+  __DATA_CONST.__objc_intobj: 0x1428
   __DATA_CONST.__objc_arraydata: 0x408
   __DATA_CONST.__objc_dictobj: 0x78
   __DATA_CONST.__objc_arrayobj: 0x360
-  __DATA_CONST.__auth_got: 0x2080
-  __DATA_CONST.__got: 0x1460
+  __DATA_CONST.__auth_got: 0x2078
+  __DATA_CONST.__got: 0x1468
   __DATA_CONST.__auth_ptr: 0x1d8
-  __DATA.__objc_const: 0x23c38
-  __DATA.__objc_selrefs: 0x9810
+  __DATA.__objc_const: 0x23cd0
+  __DATA.__objc_selrefs: 0x9858
   __DATA.__objc_ivar: 0x1ae8
-  __DATA.__objc_data: 0x5d48
+  __DATA.__objc_data: 0x5d98
   __DATA.__data: 0x3098
   __DATA.__thread_vars: 0xc0
   __DATA.__thread_bss: 0x30

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 10030
+  Functions: 10038
   Symbols:   1843
-  CStrings:  16250
+  CStrings:  16268
 
Symbols:
+ _OBJC_CLASS_$_NSURLComponents
- _dispatch_walltime
CStrings:
+ "@40@0:8r*16Q24^@32"
+ "B32@0:8@16Q24"
+ "Deleting non-syncable password-evaluations items from class=%@ with multi-user view=%@"
+ "SecXPCNetworkURL"
+ "allowedURLFromCString:options:error:"
+ "com.apple.password-manager.password-evaluations"
+ "componentsWithString:"
+ "escrowRepairCurrentVersion"
+ "host"
+ "http"
+ "https"
+ "isAllowedURL:options:"
+ "isOctagonExcluded:"
+ "lowercaseString"
+ "scheme"
+ "scheme:isAllowedByOptions:"
+ "setError:code:"
+ "v32@0:8^@16q24"
```
