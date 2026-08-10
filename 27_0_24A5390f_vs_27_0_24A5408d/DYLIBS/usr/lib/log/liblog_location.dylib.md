## liblog_location.dylib

> `/usr/lib/log/liblog_location.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH_CONST.__objc_dictobj`
- `__DATA_DIRTY.__objc_data`

```diff

-3183.0.0.0.0
+3185.0.6.0.1
   __TEXT.__text: 0x6940
   __TEXT.__objc_methlist: 0x350
-  __TEXT.__const: 0x60
+  __TEXT.__const: 0x70
   __TEXT.__gcc_except_tab: 0x34
-  __TEXT.__cstring: 0x483c
+  __TEXT.__cstring: 0x4874
   __TEXT.__unwind_info: 0x148
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xad8
+  __DATA_CONST.__const: 0xae0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x390

   __DATA_CONST.__objc_arraydata: 0x110
   __DATA_CONST.__got: 0x88
   __AUTH_CONST.__const: 0x80
-  __AUTH_CONST.__cfstring: 0x54c0
+  __AUTH_CONST.__cfstring: 0x54e0
   __AUTH_CONST.__objc_const: 0xf8
   __AUTH_CONST.__weak_auth_got: 0x8
   __AUTH_CONST.__objc_dictobj: 0x168

   - /usr/lib/libobjc.A.dylib
   Functions: 86
   Symbols:   507
-  CStrings:  685
+  CStrings:  686
 
CStrings:
+ "CLLocationProvider_Type::kNotificationGnssFailureStatus"
```
