## AutoBugCaptureCore

> `/System/Library/PrivateFrameworks/AutoBugCaptureCore.framework/Versions/A/AutoBugCaptureCore`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__got`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

 411.160.2.0.0
-  __TEXT.__text: 0x81258
+  __TEXT.__text: 0x813d4
   __TEXT.__auth_stubs: 0xe50
   __TEXT.__objc_methlist: 0x5b9c
-  __TEXT.__cstring: 0x4e56
+  __TEXT.__cstring: 0x4eb7
   __TEXT.__const: 0x290
   __TEXT.__oslogstring: 0xe40a
   __TEXT.__gcc_except_tab: 0x1190

   __DATA_CONST.__objc_selrefs: 0x3470
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x1e0
-  __DATA_CONST.__objc_arraydata: 0x628
+  __DATA_CONST.__objc_arraydata: 0x6b8
   __AUTH_CONST.__auth_got: 0x738
   __AUTH_CONST.__const: 0x1ee0
-  __AUTH_CONST.__cfstring: 0x6840
+  __AUTH_CONST.__cfstring: 0x6900
   __AUTH_CONST.__objc_const: 0xb968
-  __AUTH_CONST.__objc_dictobj: 0x5a0
+  __AUTH_CONST.__objc_dictobj: 0x690
   __AUTH_CONST.__objc_intobj: 0x2d0
-  __AUTH_CONST.__objc_arrayobj: 0x450
+  __AUTH_CONST.__objc_arrayobj: 0x4b0
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH.__objc_data: 0x8e8
   __DATA.__objc_ivar: 0x630

   - /usr/lib/libobjc.A.dylib
   Functions: 2261
   Symbols:   5501
-  CStrings:  4671
+  CStrings:  4677
 
Functions:
~ -[SystemProperties init] : 1584 -> 1580
~ +[CaseDampeningExceptions allowDampeningExceptionFor:] : 1936 -> 2036
~ -[DiagnosticsController addSpecialProjectsDiagnosticActions:] : 60 -> 344
CStrings:
+ "Proxima"
+ "Thread"
+ "WiFi Watchdog"
+ "com.apple.DiagnosticExtensions.ConnectivityDE"
+ "proxima"
+ "proxima-diags"
```
