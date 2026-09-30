## Diagnostic-4003

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4003.appex/Diagnostic-4003`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

 1374.2.2.0.0
-  __TEXT.__text: 0x2024
-  __TEXT.__auth_stubs: 0x450
-  __TEXT.__objc_stubs: 0x780
-  __TEXT.__objc_methlist: 0x384
+  __TEXT.__text: 0x23e0
+  __TEXT.__auth_stubs: 0x470
+  __TEXT.__objc_stubs: 0x860
+  __TEXT.__objc_methlist: 0x3bc
   __TEXT.__const: 0x20
   __TEXT.__gcc_except_tab: 0x80
-  __TEXT.__cstring: 0xce
-  __TEXT.__objc_methname: 0x923
+  __TEXT.__cstring: 0x10a
+  __TEXT.__objc_methname: 0x9db
   __TEXT.__oslogstring: 0x214
   __TEXT.__objc_classname: 0x9c
-  __TEXT.__objc_methtype: 0x27e
-  __TEXT.__unwind_info: 0xf8
-  __DATA_CONST.__const: 0x90
-  __DATA_CONST.__cfstring: 0x140
+  __TEXT.__objc_methtype: 0x2aa
+  __TEXT.__unwind_info: 0x100
+  __DATA_CONST.__const: 0xa8
+  __DATA_CONST.__cfstring: 0x220
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_intobj: 0x168
   __DATA_CONST.__objc_floatobj: 0x10
-  __DATA_CONST.__auth_got: 0x238
+  __DATA_CONST.__auth_got: 0x248
   __DATA_CONST.__got: 0x78
-  __DATA.__objc_const: 0x5f0
-  __DATA.__objc_selrefs: 0x2c8
-  __DATA.__objc_ivar: 0x2c
+  __DATA.__objc_const: 0x658
+  __DATA.__objc_selrefs: 0x2f8
+  __DATA.__objc_ivar: 0x34
   __DATA.__objc_data: 0xf0
   __DATA.__data: 0x180
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/DiagnosticsSupport.framework/DiagnosticsSupport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 59
-  Symbols:   104
-  CStrings:  189
+  Functions: 64
+  Symbols:   109
+  CStrings:  207
 
Symbols:
+ _kALSIdentifierInnerFirst
+ _kALSIdentifierInnerSecond
+ _kALSIdentifierPrimary
+ _objc_opt_class
+ _objc_opt_isKindOfClass
+ _objc_setProperty_nonatomic_copy
- _objc_retain_x3
CStrings:
+ "@\"AmbientLightSensorDataInputs\""
+ "@\"NSString\""
+ "InnerFirst"
+ "InnerSecond"
+ "Primary"
+ "T@\"AmbientLightSensorDataInputs\",&,N,V_alsInputs"
+ "T@\"NSString\",C,N,V_identifier"
+ "_alsInputs"
+ "_identifier"
+ "als"
+ "als2a"
+ "als2b"
+ "alsInputs"
+ "containsObject:"
+ "identifier"
+ "setAlsInputs:"
+ "setIdentifier:"
+ "setWithObjects:"
```
