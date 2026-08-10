## WiFiPolicy

> `/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__cstring`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__weak_got`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-1070.61.0.0.0
-  __TEXT.__text: 0xe2d0c
+1070.62.0.0.0
+  __TEXT.__text: 0xe2d8c
   __TEXT.__objc_methlist: 0x13d18
   __TEXT.__const: 0x868
   __TEXT.__cstring: 0x25d0b
-  __TEXT.__oslogstring: 0x54ee
+  __TEXT.__oslogstring: 0x550e
   __TEXT.__gcc_except_tab: 0x190c
   __TEXT.__dlopen_cstrs: 0xa8
   __TEXT.__ustring: 0x82

   __DATA_CONST.__objc_protolist: 0x118
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0xaf18
+  __DATA_CONST.__objc_selrefs: 0xaf20
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x4e0
   __DATA_CONST.__objc_arraydata: 0x1510
   __DATA_CONST.__got: 0xbb8
   __AUTH_CONST.__const: 0x600
-  __AUTH_CONST.__cfstring: 0x20da0
+  __AUTH_CONST.__cfstring: 0x20dc0
   __AUTH_CONST.__objc_const: 0x25980
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_intobj: 0x1aa0
   __AUTH_CONST.__objc_arrayobj: 0x450
   __AUTH_CONST.__objc_dictobj: 0x190
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH_CONST.__auth_got: 0xed8
+  __AUTH_CONST.__auth_got: 0xee0
   __AUTH.__objc_data: 0x6b8
   __DATA.__objc_ivar: 0x2568
   __DATA.__data: 0x1ca0

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 7206
-  Symbols:   15645
-  CStrings:  5320
+  Symbols:   15647
+  CStrings:  5322
 
Symbols:
+ _MGGetStringAnswer
+ _objc_msgSend$setWiFiChipset:
Functions:
~ -[WiFiDiagnosticReporter initABCReporter] : 96 -> 224
CStrings:
+ "%s: Set WiFi chipset for ABC: %@"
+ "WifiChipset"
```
