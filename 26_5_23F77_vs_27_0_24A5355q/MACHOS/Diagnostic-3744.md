## Diagnostic-3744

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-3744.appex/Diagnostic-3744`

```diff

-1066.122.1.0.0
-  __TEXT.__text: 0xa84
-  __TEXT.__auth_stubs: 0x150
+1351.0.0.0.0
+  __TEXT.__text: 0xa18
+  __TEXT.__auth_stubs: 0x170
   __TEXT.__objc_stubs: 0x400
   __TEXT.__objc_methlist: 0x2c
   __TEXT.__const: 0x18
-  __TEXT.__gcc_except_tab: 0x54
+  __TEXT.__gcc_except_tab: 0x5c
   __TEXT.__cstring: 0x131
   __TEXT.__objc_classname: 0x1d
   __TEXT.__objc_methname: 0x22b
   __TEXT.__objc_methtype: 0x21
   __TEXT.__unwind_info: 0x80
-  __DATA_CONST.__auth_got: 0xb8
-  __DATA_CONST.__got: 0x50
   __DATA_CONST.__const: 0x28
   __DATA_CONST.__cfstring: 0x200
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_intobj: 0x60
+  __DATA_CONST.__auth_got: 0xc8
+  __DATA_CONST.__got: 0x50
   __DATA.__objc_const: 0x90
   __DATA.__objc_selrefs: 0x108
   __DATA.__objc_data: 0x50

   - /System/Library/PrivateFrameworks/DiagnosticsSupport.framework/DiagnosticsSupport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B7B37623-BCD9-3C0B-BEBE-D9C19FA418B0
+  UUID: 215C2B06-EBEC-3CDD-9752-5D7BFD517D24
   Functions: 6
-  Symbols:   43
+  Symbols:   45
   CStrings:  72
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x21
+ _objc_retain_x8
- _objc_retain
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x20
Functions:
~ sub_100000be8 : 240 -> 236
~ sub_100000cd8 -> sub_100000cd4 : 1092 -> 1056
~ sub_100001134 -> sub_10000110c : 1104 -> 1040
~ sub_100001584 -> sub_10000151c : 232 -> 228

```
