## NetworkServiceProxy

> `/System/Library/PrivateFrameworks/NetworkServiceProxy.framework/NetworkServiceProxy`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-980.0.0.0.0
-  __TEXT.__text: 0x631cc
-  __TEXT.__objc_methlist: 0x5fec
+985.0.0.0.0
+  __TEXT.__text: 0x63560
+  __TEXT.__objc_methlist: 0x601c
   __TEXT.__const: 0x370
   __TEXT.__gcc_except_tab: 0x64
-  __TEXT.__cstring: 0x5acb
+  __TEXT.__cstring: 0x5ae2
   __TEXT.__oslogstring: 0x32c4
   __TEXT.__unwind_info: 0x1228
   __TEXT.__objc_stubs: 0x0

   __DATA_CONST.__objc_classlist: 0x220
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x29d8
+  __DATA_CONST.__objc_selrefs: 0x29f8
   __DATA_CONST.__objc_superrefs: 0x208
   __DATA_CONST.__objc_arraydata: 0x48
   __DATA_CONST.__got: 0x468
   __AUTH_CONST.__const: 0x160
-  __AUTH_CONST.__cfstring: 0x51a0
-  __AUTH_CONST.__objc_const: 0x80a0
+  __AUTH_CONST.__cfstring: 0x51c0
+  __AUTH_CONST.__objc_const: 0x80e0
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x28

   __DATA.__data: 0x268
   __DATA.__common: 0x1
   __DATA.__bss: 0x10
-  __DATA_DIRTY.__objc_ivar: 0x2d8
+  __DATA_DIRTY.__objc_ivar: 0x2dc
   __DATA_DIRTY.__objc_data: 0xf0
   __DATA_DIRTY.__bss: 0x98
   __DATA_DIRTY.__common: 0x20

   - /System/Library/PrivateFrameworks/SymptomDiagnosticReporter.framework/SymptomDiagnosticReporter
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
-  - /usr/lib/libboringssl.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2124
-  Symbols:   4056
-  CStrings:  1222
+  Functions: 2128
+  Symbols:   4061
+  CStrings:  1223
 
Symbols:
+ -[NSPPrivacyProxyConfiguration hasMaxRebootFetchesPerDay]
+ -[NSPPrivacyProxyConfiguration maxRebootFetchesPerDay]
+ -[NSPPrivacyProxyConfiguration setHasMaxRebootFetchesPerDay:]
+ -[NSPPrivacyProxyConfiguration setMaxRebootFetchesPerDay:]
+ _objc_msgSend$setMaxRebootFetchesPerDay:
CStrings:
+ "maxRebootFetchesPerDay"
```
