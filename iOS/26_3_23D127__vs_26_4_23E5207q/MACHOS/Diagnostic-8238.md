## Diagnostic-8238

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8238.appex/Diagnostic-8238`

```diff

-1399.9.0.0.0
-  __TEXT.__text: 0xdfc
-  __TEXT.__auth_stubs: 0x260
+1416.1.0.0.0
+  __TEXT.__text: 0xe30
+  __TEXT.__auth_stubs: 0x250
   __TEXT.__objc_stubs: 0x260
   __TEXT.__objc_methlist: 0x274
   __TEXT.__cstring: 0x6c

   __TEXT.__objc_methname: 0x416
   __TEXT.__oslogstring: 0x1fa
   __TEXT.__unwind_info: 0xd8
-  __DATA_CONST.__auth_got: 0x140
+  __DATA_CONST.__auth_got: 0x138
   __DATA_CONST.__got: 0x10
   __DATA_CONST.__const: 0x40
   __DATA_CONST.__cfstring: 0x20

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 571445D6-15F5-3488-A1DD-0FDDE2700F24
+  UUID: 20E04A17-2408-3E90-A350-4672D7BA61C7
   Functions: 24
-  Symbols:   53
+  Symbols:   52
   CStrings:  119
 
Symbols:
+ _objc_release
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x21
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x2
- _objc_retain_x22
- _objc_retain_x3

```
