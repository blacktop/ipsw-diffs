## Diagnostic-9012

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-9012.appex/Diagnostic-9012`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

 1307.40.66.0.0
-  __TEXT.__text: 0x2bb8
-  __TEXT.__auth_stubs: 0x2f0
-  __TEXT.__objc_stubs: 0xde0
+  __TEXT.__text: 0x2de4
+  __TEXT.__auth_stubs: 0x310
+  __TEXT.__objc_stubs: 0xe40
   __TEXT.__objc_methlist: 0x47c
   __TEXT.__const: 0x80
-  __TEXT.__objc_methname: 0xf44
-  __TEXT.__cstring: 0x25d
+  __TEXT.__objc_methname: 0xf57
+  __TEXT.__cstring: 0x27d
   __TEXT.__objc_classname: 0x58
   __TEXT.__objc_methtype: 0x26f
   __TEXT.__gcc_except_tab: 0x84
-  __TEXT.__oslogstring: 0x16e
+  __TEXT.__oslogstring: 0x1b7
   __TEXT.__dlopen_cstrs: 0x62
   __TEXT.__unwind_info: 0x130
   __DATA_CONST.__const: 0xd8
-  __DATA_CONST.__cfstring: 0x1c0
+  __DATA_CONST.__cfstring: 0x200
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__objc_intobj: 0x78
-  __DATA_CONST.__auth_got: 0x188
-  __DATA_CONST.__got: 0x98
+  __DATA_CONST.__auth_got: 0x198
+  __DATA_CONST.__got: 0xa0
   __DATA.__objc_const: 0x770
-  __DATA.__objc_selrefs: 0x4c8
+  __DATA.__objc_selrefs: 0x4d0
   __DATA.__objc_ivar: 0x58
   __DATA.__objc_data: 0xf0
   __DATA.__data: 0xc0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 82
-  Symbols:   87
-  CStrings:  290
+  Functions: 83
+  Symbols:   90
+  CStrings:  296
 
Symbols:
+ _MGGetBoolAnswer
+ _OBJC_CLASS_$_CRIOServiceController
+ _dispatch_semaphore_signal
Functions:
~ sub_100001ffc : 152 -> 664
+ sub_100003d64
CStrings:
+ "Failed to assert repair_en"
+ "InDiagnosticsMode"
+ "InternalBuild"
+ "Mesa already unlocked"
+ "Mesa unlock not supported"
+ "Waiting for keychord..."
+ "getProtocolVersion"
- "Diagnostics not available"
```
