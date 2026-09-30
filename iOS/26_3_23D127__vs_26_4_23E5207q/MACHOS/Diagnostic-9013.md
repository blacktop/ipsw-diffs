## Diagnostic-9013

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-9013.appex/Diagnostic-9013`

```diff

-921.80.171.0.1
-  __TEXT.__text: 0x1ad8
-  __TEXT.__auth_stubs: 0x200
-  __TEXT.__objc_stubs: 0x460
-  __TEXT.__objc_methlist: 0x23c
-  __TEXT.__const: 0x78
-  __TEXT.__cstring: 0x1dd
-  __TEXT.__oslogstring: 0x22f
+921.100.255.0.0
+  __TEXT.__text: 0x16b8
+  __TEXT.__auth_stubs: 0x1f0
+  __TEXT.__objc_stubs: 0x3a0
+  __TEXT.__objc_methlist: 0x22c
+  __TEXT.__const: 0x70
+  __TEXT.__cstring: 0x190
+  __TEXT.__oslogstring: 0x167
   __TEXT.__objc_classname: 0x76
-  __TEXT.__objc_methname: 0x4d6
+  __TEXT.__objc_methname: 0x4a4
   __TEXT.__objc_methtype: 0x184
-  __TEXT.__unwind_info: 0xb8
-  __DATA_CONST.__auth_got: 0x108
-  __DATA_CONST.__got: 0x58
+  __TEXT.__unwind_info: 0xb0
+  __DATA_CONST.__auth_got: 0x100
+  __DATA_CONST.__got: 0x50
   __DATA_CONST.__const: 0x48
-  __DATA_CONST.__cfstring: 0x220
+  __DATA_CONST.__cfstring: 0x1c0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x428
-  __DATA.__objc_selrefs: 0x1f8
-  __DATA.__objc_ivar: 0x10
+  __DATA.__objc_const: 0x3f8
+  __DATA.__objc_selrefs: 0x1e8
+  __DATA.__objc_ivar: 0xc
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0x120
   __DATA.__bss: 0x20

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E7806736-B5F9-30A4-8579-FCAA9AA2E184
-  Functions: 30
-  Symbols:   63
-  CStrings:  169
+  UUID: 0D6415AC-000C-36CD-8E6F-767F91E8F6F6
+  Functions: 31
+  Symbols:   61
+  CStrings:  152
 
Symbols:
+ _objc_release
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
+ _objc_retain_x22
- _OBJC_CLASS_$_CRSmcController
- _objc_claimAutoreleasedReturnValue
- _objc_release_x27
- _objc_release_x28
- _objc_retain_x2
- _objc_retain_x8
CStrings:
- "Failed to probe gasgauge status, error: %@"
- "Gasgauge already locked, exiting..."
- "Gasgauge locking not required, exiting..."
- "Locking gasgauge..."
- "SMC controller: %@"
- "TB,R,N,V_ggReset"
- "_ggReset"
- "currentGasgaugeLockStatus"
- "doGgLock: %d, doGgReset: %d"
- "ggReset"
- "ggReset: %@"
- "numberWithBool:"
- "previousGasgaugeLockStatus"
- "shouldResetLifeTimeTemp"

```
