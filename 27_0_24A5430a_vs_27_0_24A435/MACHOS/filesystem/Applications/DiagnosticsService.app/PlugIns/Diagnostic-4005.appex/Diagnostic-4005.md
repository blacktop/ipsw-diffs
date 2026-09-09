## Diagnostic-4005

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4005.appex/Diagnostic-4005`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

 1374.2.2.0.0
-  __TEXT.__text: 0x1c80
-  __TEXT.__auth_stubs: 0x440
-  __TEXT.__objc_stubs: 0x640
-  __TEXT.__objc_methlist: 0x324
-  __TEXT.__const: 0x18
+  __TEXT.__text: 0x1fa4
+  __TEXT.__auth_stubs: 0x480
+  __TEXT.__objc_stubs: 0x740
+  __TEXT.__objc_methlist: 0x36c
+  __TEXT.__const: 0x20
   __TEXT.__gcc_except_tab: 0x80
-  __TEXT.__cstring: 0xb4
-  __TEXT.__objc_methname: 0x7b9
-  __TEXT.__oslogstring: 0x17a
+  __TEXT.__cstring: 0xe3
+  __TEXT.__objc_methname: 0x888
+  __TEXT.__oslogstring: 0x1b9
   __TEXT.__objc_classname: 0x88
-  __TEXT.__objc_methtype: 0x239
-  __TEXT.__unwind_info: 0xe8
-  __DATA_CONST.__const: 0x90
-  __DATA_CONST.__cfstring: 0x120
+  __TEXT.__objc_methtype: 0x266
+  __TEXT.__unwind_info: 0x100
+  __DATA_CONST.__const: 0xa0
+  __DATA_CONST.__cfstring: 0x1c0
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_intobj: 0x168
-  __DATA_CONST.__auth_got: 0x230
+  __DATA_CONST.__auth_got: 0x250
   __DATA_CONST.__got: 0x70
-  __DATA.__objc_const: 0x540
-  __DATA.__objc_selrefs: 0x280
-  __DATA.__objc_ivar: 0x20
+  __DATA.__objc_const: 0x5a8
+  __DATA.__objc_selrefs: 0x2b8
+  __DATA.__objc_ivar: 0x28
   __DATA.__objc_data: 0xf0
   __DATA.__data: 0x120
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/DiagnosticsSupport.framework/DiagnosticsSupport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 53
-  Symbols:   101
-  CStrings:  165
+  Functions: 60
+  Symbols:   107
+  CStrings:  183
 
Symbols:
+ _kAccelIdentifierPrimary
+ _kAccelIdentifierSecondary
+ _objc_opt_class
+ _objc_opt_isKindOfClass
+ _objc_release_x24
+ _objc_setProperty_nonatomic_copy
CStrings:
+ "@\"AccelerometerSensorDataInputs\""
+ "@\"NSString\""
+ "Could not resolve target accelerometer service for product: %@"
+ "Primary"
+ "Secondary"
+ "T@\"AccelerometerSensorDataInputs\",&,N,V_accelInputs"
+ "T@\"NSString\",C,N,V_identifier"
+ "_accelInputs"
+ "_identifier"
+ "accel"
+ "accelInputs"
+ "accel_1"
+ "containsObject:"
+ "identifier"
+ "setAccelInputs:"
+ "setIdentifier:"
+ "setWithObjects:"
+ "targetProduct"
```
