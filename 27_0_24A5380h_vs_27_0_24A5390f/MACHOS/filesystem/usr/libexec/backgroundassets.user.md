## backgroundassets.user

> `/usr/libexec/backgroundassets.user`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift5_capture`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`
- `__DATA.__data`
- `__DATA.__bss`
- `__DATA.__common`

```diff

-274.0.0.0.0
-  __TEXT.__text: 0x5a17c
+279.0.1.0.0
+  __TEXT.__text: 0x5a458
   __TEXT.__auth_stubs: 0x1900
-  __TEXT.__objc_stubs: 0x7840
-  __TEXT.__objc_methlist: 0x3544
+  __TEXT.__objc_stubs: 0x7800
+  __TEXT.__objc_methlist: 0x352c
   __TEXT.__const: 0x1ac8
   __TEXT.__objc_classname: 0x84e
   __TEXT.__objc_methtype: 0x19b2
-  __TEXT.__oslogstring: 0x6c83
-  __TEXT.__cstring: 0x41a0
-  __TEXT.__objc_methname: 0x9cc4
+  __TEXT.__oslogstring: 0x6db3
+  __TEXT.__cstring: 0x41e0
+  __TEXT.__objc_methname: 0x9c6e
   __TEXT.__gcc_except_tab: 0x14fc
   __TEXT.__dlopen_cstrs: 0x5a
   __TEXT.__constg_swiftt: 0x428

   __TEXT.__unwind_info: 0x1448
   __TEXT.__eh_frame: 0x4f8
   __DATA_CONST.__const: 0x1f20
-  __DATA_CONST.__cfstring: 0x24c0
+  __DATA_CONST.__cfstring: 0x2520
   __DATA_CONST.__objc_classlist: 0x1a8
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xc0

   __DATA_CONST.__auth_got: 0xc90
   __DATA_CONST.__got: 0x5c0
   __DATA_CONST.__auth_ptr: 0x360
-  __DATA.__objc_const: 0x5a40
-  __DATA.__objc_selrefs: 0x21b8
+  __DATA.__objc_const: 0x5a30
+  __DATA.__objc_selrefs: 0x21a8
   __DATA.__objc_ivar: 0x3b8
   __DATA.__objc_data: 0x1210
   __DATA.__data: 0x12e0

   - /usr/lib/swift/libswiftos.dylib
   Functions: 1944
   Symbols:   696
-  CStrings:  2609
+  CStrings:  2613
 
CStrings:
+ "Asset pack management info: %@\n"
+ "DownloadID"
+ "Poking the scheduler because at least one download event remains undelivered to the application with the bundle identifier “%{public}@”…"
+ "Poking the scheduler because at least one download for the application with the bundle identifier “%{public}@” was promoted to the foreground…"
+ "Poking the scheduler…"
+ "Was foreground download: %@\n"
- "TB,V_wasForegroundDownload"
- "setWasForegroundDownload:"
```
