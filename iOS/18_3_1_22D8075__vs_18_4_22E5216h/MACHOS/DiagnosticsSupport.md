## DiagnosticsSupport

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8441.appex/Frameworks/DiagnosticsSupport.framework/DiagnosticsSupport`

```diff

-820.82.2.0.0
-  __TEXT.__text: 0xe31c
+820.100.56.0.0
+  __TEXT.__text: 0xe230
   __TEXT.__auth_stubs: 0x980
-  __TEXT.__objc_methlist: 0xd7c
+  __TEXT.__objc_methlist: 0xda0
   __TEXT.__const: 0x1f0
   __TEXT.__cstring: 0x9fd
   __TEXT.__oslogstring: 0xd79
-  __TEXT.__gcc_except_tab: 0x12c
-  __TEXT.__unwind_info: 0x390
+  __TEXT.__gcc_except_tab: 0x128
+  __TEXT.__unwind_info: 0x3a0
   __TEXT.__objc_classname: 0x1a6
   __TEXT.__objc_methname: 0x2617
   __TEXT.__objc_methtype: 0x59d

   __AUTH_CONST.__auth_got: 0x4d0
   __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__cfstring: 0xe60
-  __AUTH_CONST.__objc_const: 0x1b18
+  __AUTH_CONST.__objc_const: 0x1ae0
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x18

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 361
-  Symbols:   1097
+  Functions: 359
+  Symbols:   1099
   CStrings:  849
 
Symbols:
+ +[DSDateFormatter sharedFormatter].cold.1
+ +[DSTestAutomation sharedInstance].cold.1
+ -[DSIOHIDDevice _sharedSerialQueue].cold.1
+ DiagnosticLogHandleForCategory.cold.1
- _OUTLINED_FUNCTION_4

```
