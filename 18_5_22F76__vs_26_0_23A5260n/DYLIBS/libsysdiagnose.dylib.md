## libsysdiagnose.dylib

> `/usr/lib/libsysdiagnose.dylib`

```diff

-1438.120.9.0.0
-  __TEXT.__text: 0x2f34
+1512.0.0.0.0
+  __TEXT.__text: 0x2fbc
   __TEXT.__auth_stubs: 0x4e0
   __TEXT.__objc_methlist: 0xe0
   __TEXT.__oslogstring: 0x1f8
-  __TEXT.__cstring: 0x574
+  __TEXT.__cstring: 0x58e
   __TEXT.__const: 0x38
   __TEXT.__gcc_except_tab: 0x60
-  __TEXT.__unwind_info: 0xf0
+  __TEXT.__unwind_info: 0xf8
   __TEXT.__objc_classname: 0xf
   __TEXT.__objc_methname: 0x701
   __TEXT.__objc_methtype: 0xd9

   __DATA_CONST.__objc_selrefs: 0x220
   __AUTH_CONST.__auth_got: 0x280
   __AUTH_CONST.__const: 0x60
-  __AUTH_CONST.__cfstring: 0x520
+  __AUTH_CONST.__cfstring: 0x540
   __AUTH_CONST.__objc_const: 0x90
   __AUTH_CONST.__objc_intobj: 0x60
   __DATA_DIRTY.__objc_data: 0x50

   - /System/Library/PrivateFrameworks/OSAnalytics.framework/OSAnalytics
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B6341E2A-BBA3-382F-A357-695D776ABD0D
-  Functions: 36
-  Symbols:   284
-  CStrings:  201
+  UUID: 30CFF3C8-52E6-359C-BD81-0846DB7775A5
+  Functions: 38
+  Symbols:   288
+  CStrings:  203
 
Symbols:
+ +[Libsysdiagnose addErrorString:withCode:forError:]
+ GCC_except_table19
+ GCC_except_table8
+ ___83+[Libsysdiagnose sendSysdiagnoseRequest:withMetrics:withError:withProgressHandler:]_block_invoke.93
+ ___Block_byref_object_copy_.86
+ ___Block_byref_object_dispose_.87
+ ___block_literal_global.126
+ ___block_literal_global.145
+ _objc_msgSend$addErrorString:withCode:forError:
+ _safeFetchErrorStr
+ _safeFetchStr
- +[Libsysdiagnose addErrorString:WithCode:forError:]
- GCC_except_table17
- GCC_except_table7
- ___83+[Libsysdiagnose sendSysdiagnoseRequest:withMetrics:withError:withProgressHandler:]_block_invoke.97
- ___Block_byref_object_copy_.89
- ___Block_byref_object_dispose_.90
- ___block_literal_global.130
- ___block_literal_global.149
- _objc_msgSend$addErrorString:WithCode:forError:
CStrings:
+ ""
+ "%@ (%@)"
+ "EXTENDED_ERROR_DATA"
+ "addErrorString:withCode:forError:"
- "%s"
- "addErrorString:WithCode:forError:"

```
