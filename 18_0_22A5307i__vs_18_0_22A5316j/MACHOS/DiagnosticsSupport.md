## DiagnosticsSupport

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8441.appex/Frameworks/DiagnosticsSupport.framework/DiagnosticsSupport`

```diff

-782.0.0.0.0
-  __TEXT.__text: 0xe1cc
-  __TEXT.__auth_stubs: 0x970
-  __TEXT.__objc_methlist: 0xd74
+795.0.0.0.0
+  __TEXT.__text: 0xe31c
+  __TEXT.__auth_stubs: 0x980
+  __TEXT.__objc_methlist: 0xd7c
   __TEXT.__const: 0x1f0
   __TEXT.__cstring: 0x9fd
-  __TEXT.__oslogstring: 0xd45
-  __TEXT.__gcc_except_tab: 0x128
+  __TEXT.__oslogstring: 0xd79
+  __TEXT.__gcc_except_tab: 0x12c
   __TEXT.__unwind_info: 0x390
-  __TEXT.__objc_classname: 0x1a4
-  __TEXT.__objc_methname: 0x25f5
+  __TEXT.__objc_classname: 0x1a6
+  __TEXT.__objc_methname: 0x2617
   __TEXT.__objc_methtype: 0x59d
   __TEXT.__objc_stubs: 0x2080
   __DATA_CONST.__got: 0x178

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb48
+  __DATA_CONST.__objc_selrefs: 0xb50
   __DATA_CONST.__objc_superrefs: 0x80
   __DATA_CONST.__objc_arraydata: 0x18
-  __AUTH_CONST.__auth_got: 0x4c8
+  __AUTH_CONST.__auth_got: 0x4d0
   __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__cfstring: 0xe60
-  __AUTH_CONST.__objc_const: 0x1ae8
+  __AUTH_CONST.__objc_const: 0x1b18
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x618
-  __DATA.__objc_ivar: 0x118
+  __DATA.__objc_ivar: 0x11c
   __DATA.__data: 0x60
   __DATA.__bss: 0x30
   __DATA_DIRTY.__objc_data: 0x78

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 360
-  Symbols:   1094
-  CStrings:  844
+  Functions: 361
+  Symbols:   1097
+  CStrings:  849
 
Symbols:
+ -[DSLogLine stringFromFieldAtIndex:]
+ -[DSTextFile initWithFilePath:withBufferSize:].cold.1
+ -[DSThermalLogLine reason]
+ GCC_except_table2
+ OBJC_IVAR_$_DSThermalLogLine._reason
+ _objc_msgSend$stringFromFieldAtIndex:
+ _objc_unsafeClaimAutoreleasedReturnValue
- -[DSLogLine nilableStringFromFieldAtIndex:]
- -[DSTextFile init]
- GCC_except_table3
- _objc_msgSend$nilableStringFromFieldAtIndex:
CStrings:
+ "!"
+ "Could not parse header for %!@(MISSING) error: %!@(MISSING)"
+ "Failed to init handle for file at path %!@(MISSING)"
+ "T@\"NSString\",R,N,V_reason"
+ "_reason"
+ "reason"
+ "stringFromFieldAtIndex:"
- "Could not parse header for %!@(MISSING)"
- "nilableStringFromFieldAtIndex:"

```
