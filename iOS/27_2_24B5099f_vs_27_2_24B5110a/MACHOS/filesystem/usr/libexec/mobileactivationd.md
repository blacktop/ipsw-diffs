## mobileactivationd

> `usr/libexec/mobileactivationd`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1145.40.5.502.1
-  __TEXT.__text: 0x34b39c
+1145.40.5.0.4
+  __TEXT.__text: 0x34b490
   __TEXT.__auth_stubs: 0x12f0
-  __TEXT.__objc_stubs: 0x3240
-  __TEXT.__objc_methlist: 0x112c
+  __TEXT.__objc_stubs: 0x3260
+  __TEXT.__objc_methlist: 0x113c
   __TEXT.__const: 0x60b63
-  __TEXT.__cstring: 0xf13f
-  __TEXT.__objc_methname: 0x4044
+  __TEXT.__cstring: 0xf17e
+  __TEXT.__objc_methname: 0x4084
   __TEXT.__oslogstring: 0xf47
   __TEXT.__objc_classname: 0x1a4
   __TEXT.__objc_methtype: 0x1061

   __TEXT.__unwind_info: 0x17b8
   __TEXT.__eh_frame: 0xa0
   __DATA_CONST.__const: 0x1c528
-  __DATA_CONST.__cfstring: 0xd620
+  __DATA_CONST.__cfstring: 0xd6a0
   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x48

   __DATA_CONST.__auth_got: 0x988
   __DATA_CONST.__got: 0x4b8
   __DATA_CONST.__auth_ptr: 0x80
-  __DATA.__objc_const: 0x1900
-  __DATA.__objc_selrefs: 0x10c0
-  __DATA.__objc_ivar: 0xfc
+  __DATA.__objc_const: 0x1930
+  __DATA.__objc_selrefs: 0x10c8
+  __DATA.__objc_ivar: 0x100
   __DATA.__objc_data: 0x320
   __DATA.__data: 0x1d60
   __DATA.__common: 0xb20

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1664
-  Symbols:   4063
-  CStrings:  3081
+  Functions: 1666
+  Symbols:   4067
+  CStrings:  3088
 
Symbols:
+ -[DeviceType is_home_accessory]
+ OBJC_IVAR_$_DeviceType._is_home_accessory
+ _is_home_accessory
+ _objc_msgSend$is_home_accessory
Functions:
~ -[DeviceType init] : 2212 -> 2232
+ -[DeviceType ucrt_enforced]
+ _has_internal_diagnostics
~ _producttype_supports_missing_emac : 8 -> 128
~ _device_supports_missing_emac : 40 -> 64
CStrings:
+ "1145.40.5.0.4"
+ "Absinthe/2.0 iOS Device Activator (MobileActivation-1145.40.5.0.4 built on Oct  3 2026 at 22:24:14)"
+ "AudioAccessory11,1"
+ "HomeAccessory"
+ "HomeAccessory17,1"
+ "HomeAccessory17,2"
+ "TB,R,N,V_is_home_accessory"
+ "_is_home_accessory"
+ "iOS Device Activator (MobileActivation-1145.40.5.0.4)"
+ "is_home_accessory"
- "1145.40.5.502.1"
- "Absinthe/2.0 iOS Device Activator (MobileActivation-1145.40.5.502.1 built on Sep 28 2026 at 21:08:25)"
- "iOS Device Activator (MobileActivation-1145.40.5.502.1)"
```
