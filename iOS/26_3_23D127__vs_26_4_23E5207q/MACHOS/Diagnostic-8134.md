## Diagnostic-8134

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8134.appex/Diagnostic-8134`

```diff

-1066.80.3.0.0
-  __TEXT.__text: 0x308
-  __TEXT.__auth_stubs: 0xe0
+1066.100.26.0.0
+  __TEXT.__text: 0x3dc
+  __TEXT.__auth_stubs: 0x100
   __TEXT.__objc_stubs: 0x220
   __TEXT.__objc_methlist: 0x1dc
   __TEXT.__objc_classname: 0x5a
   __TEXT.__objc_methname: 0x395
   __TEXT.__objc_methtype: 0x115
   __TEXT.__cstring: 0x46
-  __TEXT.__unwind_info: 0x78
-  __DATA_CONST.__auth_got: 0x78
+  __TEXT.__unwind_info: 0x88
+  __DATA_CONST.__auth_got: 0x88
   __DATA_CONST.__got: 0x28
   __DATA_CONST.__cfstring: 0x80
   __DATA_CONST.__objc_classlist: 0x10

   - /System/Library/PrivateFrameworks/EnhancedLogging.framework/EnhancedLogging
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7C95A608-4450-31F7-A943-00F8D49030D5
+  UUID: 0A22FFB6-758A-3B06-A8D3-8A65603B3CE8
   Functions: 12
-  Symbols:   33
+  Symbols:   35
   CStrings:  86
 
Symbols:
+ _objc_release
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
- _objc_claimAutoreleasedReturnValue
Functions:
~ sub_100000c20 : 12 -> 64
~ sub_100000c34 -> sub_100000c68 : 12 -> 64
~ sub_100000c88 -> sub_100000cf0 : 552 -> 600
~ sub_100000ec0 -> sub_100000f58 : 20 -> 80

```
