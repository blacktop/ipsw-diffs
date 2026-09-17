## endpointsecurityd

> `/usr/libexec/endpointsecurityd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-657.1.1.0.0
-  __TEXT.__text: 0xa370
-  __TEXT.__auth_stubs: 0x8b0
+657.40.26.0.0
+  __TEXT.__text: 0xa9a0
+  __TEXT.__auth_stubs: 0x900
   __TEXT.__objc_stubs: 0xa20
   __TEXT.__objc_methlist: 0x2e4
-  __TEXT.__gcc_except_tab: 0x228
+  __TEXT.__gcc_except_tab: 0x23c
+  __TEXT.__cstring: 0x20ba
   __TEXT.__const: 0x30
-  __TEXT.__cstring: 0x1fb4
   __TEXT.__objc_methname: 0x93a
   __TEXT.__objc_classname: 0x5c
   __TEXT.__objc_methtype: 0x27f
   __TEXT.__oslogstring: 0x216
-  __TEXT.__unwind_info: 0x368
+  __TEXT.__unwind_info: 0x380
   __DATA_CONST.__const: 0x388
   __DATA_CONST.__cfstring: 0x6a0
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x18
-  __DATA_CONST.__auth_got: 0x470
-  __DATA_CONST.__got: 0x180
+  __DATA_CONST.__auth_got: 0x498
+  __DATA_CONST.__got: 0x188
+  __DATA_CONST.__auth_ptr: 0x8
   __DATA.__objc_const: 0x3f0
   __DATA.__objc_selrefs: 0x370
   __DATA.__objc_ivar: 0xc

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 165
-  Symbols:   198
-  CStrings:  384
+  Functions: 169
+  Symbols:   204
+  CStrings:  393
 
Symbols:
+ ___chkstk_darwin
+ _abort
+ _fputc
+ _fwrite
+ _strnlen
+ _vfprintf
CStrings:
+ "EndpointSecurity disabled via es_disable boot-arg; nothing to serve"
+ "EndpointSecurity disabled via es_disable boot-arg; skipping early boot"
+ "Slice::subslice invalid range"
+ "index out of range"
+ "kern.bootargs"
+ "panic: "
+ "self.exists()"
+ "sliceFrom: invalid range"
+ "unsafeCoerce"
```
