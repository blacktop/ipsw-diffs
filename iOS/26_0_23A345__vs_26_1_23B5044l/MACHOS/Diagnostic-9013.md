## Diagnostic-9013

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-9013.appex/Diagnostic-9013`

```diff

-921.0.120.0.0
-  __TEXT.__text: 0x1a48
-  __TEXT.__auth_stubs: 0x1f0
-  __TEXT.__objc_stubs: 0x440
+921.40.47.0.0
+  __TEXT.__text: 0x1740
+  __TEXT.__auth_stubs: 0x1e0
+  __TEXT.__objc_stubs: 0x3a0
   __TEXT.__objc_methlist: 0x23c
-  __TEXT.__const: 0x78
+  __TEXT.__const: 0x70
   __TEXT.__cstring: 0x1a8
-  __TEXT.__oslogstring: 0x22f
+  __TEXT.__oslogstring: 0x186
   __TEXT.__objc_classname: 0x76
   __TEXT.__objc_methname: 0x4c6
   __TEXT.__objc_methtype: 0x184
-  __TEXT.__unwind_info: 0xb8
-  __DATA_CONST.__auth_got: 0x100
+  __TEXT.__unwind_info: 0xb0
+  __DATA_CONST.__auth_got: 0xf8
   __DATA_CONST.__got: 0x58
   __DATA_CONST.__const: 0x48
   __DATA_CONST.__cfstring: 0x1e0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 836A9400-26F3-3116-8075-BE071E719F68
-  Functions: 30
-  Symbols:   62
-  CStrings:  164
+  UUID: 508E74CF-02DC-3C57-BD13-F66196CA142E
+  Functions: 29
+  Symbols:   61
+  CStrings:  159
 
Symbols:
- _objc_release_x27
Functions:
~ sub_100001268 : 880 -> 260
+ sub_100001fa0
- sub_10000222c
- sub_100002448
CStrings:
- "Failed to probe gasgauge status, error: %@"
- "Gasgauge already locked, exiting..."
- "Gasgauge locking not required, exiting..."
- "Locking gasgauge..."
- "doGgLock: %d, doGgReset: %d"

```
