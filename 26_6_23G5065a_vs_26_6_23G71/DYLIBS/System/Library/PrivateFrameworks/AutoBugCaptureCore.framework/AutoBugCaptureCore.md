## AutoBugCaptureCore

> `/System/Library/PrivateFrameworks/AutoBugCaptureCore.framework/AutoBugCaptureCore`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
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
-  __TEXT.__text: 0x7f120
+  __TEXT.__text: 0x7f274
   __TEXT.__auth_stubs: 0xfc0
   __TEXT.__objc_methlist: 0x5f7c
-  __TEXT.__cstring: 0x51d4
+  __TEXT.__cstring: 0x5235
   __TEXT.__const: 0x290
   __TEXT.__oslogstring: 0xf086
   __TEXT.__gcc_except_tab: 0x11b4
   __TEXT.__ustring: 0x8
   __TEXT.diag_actions: 0x5dcf
-  __TEXT.__unwind_info: 0x1950
+  __TEXT.__unwind_info: 0x1948
   __TEXT.__objc_classname: 0xa08
   __TEXT.__objc_methname: 0xe71d
   __TEXT.__objc_methtype: 0x23cb

   __DATA_CONST.__objc_selrefs: 0x3710
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x1f0
-  __DATA_CONST.__objc_arraydata: 0x628
+  __DATA_CONST.__objc_arraydata: 0x6b8
   __AUTH_CONST.__auth_got: 0x7f0
   __AUTH_CONST.__const: 0x620
-  __AUTH_CONST.__cfstring: 0x6bc0
+  __AUTH_CONST.__cfstring: 0x6c80
   __AUTH_CONST.__objc_const: 0xc888
-  __AUTH_CONST.__objc_dictobj: 0x5a0
+  __AUTH_CONST.__objc_dictobj: 0x690
   __AUTH_CONST.__objc_intobj: 0x2d0
-  __AUTH_CONST.__objc_arrayobj: 0x450
+  __AUTH_CONST.__objc_arrayobj: 0x4b0
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH.__objc_data: 0x1400
   __DATA.__objc_ivar: 0x68c

   - /usr/lib/libobjc.A.dylib
   Functions: 2258
   Symbols:   5614
-  CStrings:  4925
+  CStrings:  4931
 
Functions:
~ +[CaseDampeningExceptions allowDampeningExceptionFor:] : 1876 -> 1964
~ -[SystemProperties init] : 1520 -> 1516
~ -[DiagnosticsController addSpecialProjectsDiagnosticActions:] : 56 -> 312
CStrings:
+ "Proxima"
+ "Thread"
+ "WiFi Watchdog"
+ "com.apple.DiagnosticExtensions.ConnectivityDE"
+ "proxima"
+ "proxima-diags"
```
