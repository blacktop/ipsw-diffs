## Diagnostic-9013

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-9013.appex/Diagnostic-9013`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

 1307.2.4.0.0
-  __TEXT.__text: 0x8e4
-  __TEXT.__auth_stubs: 0x180
-  __TEXT.__objc_stubs: 0x2e0
+  __TEXT.__text: 0xd68
+  __TEXT.__auth_stubs: 0x1e0
+  __TEXT.__objc_stubs: 0x380
   __TEXT.__objc_methlist: 0x22c
-  __TEXT.__const: 0x60
-  __TEXT.__cstring: 0xb8
-  __TEXT.__oslogstring: 0x33
+  __TEXT.__const: 0x70
+  __TEXT.__cstring: 0xed
+  __TEXT.__oslogstring: 0x10d
   __TEXT.__objc_classname: 0x74
-  __TEXT.__objc_methname: 0x3ca
+  __TEXT.__objc_methname: 0x3da
   __TEXT.__objc_methtype: 0x16c
-  __TEXT.__unwind_info: 0x88
+  __TEXT.__unwind_info: 0x98
   __DATA_CONST.__const: 0x40
-  __DATA_CONST.__cfstring: 0xc0
+  __DATA_CONST.__cfstring: 0x100
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA_CONST.__auth_got: 0xc8
+  __DATA_CONST.__auth_got: 0xf8
   __DATA_CONST.__got: 0x48
   __DATA.__objc_const: 0x3c8
-  __DATA.__objc_selrefs: 0x1b8
+  __DATA.__objc_selrefs: 0x1c0
   __DATA.__objc_ivar: 0x8
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0x120

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 19
-  Symbols:   52
-  CStrings:  112
+  Functions: 23
+  Symbols:   58
+  CStrings:  122
 
Symbols:
+ _objc_release_x23
+ _objc_release_x24
+ _objc_release_x25
+ _objc_release_x26
+ _objc_release_x27
+ _objc_release_x28
CStrings:
+ "Bat GG status converted: %ld"
+ "Failed to open gasgauge, error: %@"
+ "Failed to probe gasgauge status, error: %@"
+ "Gasgauge already locked, exiting..."
+ "Gasgauge locking not required, exiting..."
+ "Locking gasgauge..."
+ "currentGasgaugeLockStatus"
+ "doGgLock: %d"
+ "numberWithBool:"
+ "previousGasgaugeLockStatus"
```
