## WatchConnectivity

> `/System/Library/Frameworks/WatchConnectivity.framework/WatchConnectivity`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__DATA.__data`

```diff

-223.100.4.0.0
-  __TEXT.__text: 0x2702c
+224.100.1.0.0
+  __TEXT.__text: 0x2712c
   __TEXT.__objc_methlist: 0x1f80
   __TEXT.__const: 0x158
-  __TEXT.__cstring: 0x3523
+  __TEXT.__cstring: 0x3534
   __TEXT.__oslogstring: 0x23ae
   __TEXT.__gcc_except_tab: 0x7e4
   __TEXT.__unwind_info: 0xa50

   __AUTH_CONST.__cfstring: 0x10c0
   __AUTH_CONST.__objc_const: 0x3d30
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH_CONST.__auth_got: 0x4a0
-  __AUTH.__objc_data: 0x2d0
+  __AUTH_CONST.__auth_got: 0x4a8
   __DATA.__objc_ivar: 0x1dc
   __DATA.__data: 0x540
-  __DATA.__bss: 0xb0
-  __DATA_DIRTY.__objc_data: 0x3c0
-  __DATA_DIRTY.__bss: 0x80
+  __DATA.__bss: 0x20
+  __DATA_DIRTY.__objc_data: 0x690
+  __DATA_DIRTY.__bss: 0x110
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 924
+  Functions: 930
   Symbols:   1966
   CStrings:  506
 
Symbols:
+ _CFNumberCompare
- _mallocOrAbort
CStrings:
+ "!_moa_size || _moa_result"
+ "!_roa_size || _roa_result"
- "!newSize || result"
- "!size || result"
```
