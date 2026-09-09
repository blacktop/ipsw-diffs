## Diagnostic-4007

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4007.appex/Diagnostic-4007`

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
-  __TEXT.__text: 0x1cc4
-  __TEXT.__auth_stubs: 0x440
-  __TEXT.__objc_stubs: 0x660
-  __TEXT.__objc_methlist: 0x324
-  __TEXT.__const: 0x18
+  __TEXT.__text: 0x1fe8
+  __TEXT.__auth_stubs: 0x480
+  __TEXT.__objc_stubs: 0x760
+  __TEXT.__objc_methlist: 0x36c
+  __TEXT.__const: 0x20
   __TEXT.__gcc_except_tab: 0x80
-  __TEXT.__cstring: 0xb4
-  __TEXT.__objc_methname: 0x7a6
-  __TEXT.__oslogstring: 0x172
+  __TEXT.__cstring: 0xe1
+  __TEXT.__objc_methname: 0x868
+  __TEXT.__oslogstring: 0x1ad
   __TEXT.__objc_classname: 0x76
-  __TEXT.__objc_methtype: 0x239
-  __TEXT.__unwind_info: 0xe8
-  __DATA_CONST.__const: 0x90
-  __DATA_CONST.__cfstring: 0x120
+  __TEXT.__objc_methtype: 0x25d
+  __TEXT.__unwind_info: 0xf8
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
-  __DATA.__objc_selrefs: 0x288
-  __DATA.__objc_ivar: 0x20
+  __DATA.__objc_const: 0x5a8
+  __DATA.__objc_selrefs: 0x2c0
+  __DATA.__objc_ivar: 0x28
   __DATA.__objc_data: 0xf0
   __DATA.__data: 0x120
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/DiagnosticsSupport.framework/DiagnosticsSupport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 53
-  Symbols:   101
-  CStrings:  166
+  Functions: 60
+  Symbols:   107
+  CStrings:  184
 
Symbols:
+ _kGyroIdentifierPrimary
+ _kGyroIdentifierSecondary
+ _objc_opt_class
+ _objc_opt_isKindOfClass
+ _objc_release_x24
+ _objc_setProperty_nonatomic_copy
CStrings:
+ "@\"GyroSensorDataInputs\""
+ "@\"NSString\""
+ "Could not resolve target gyroscope service for product: %@"
+ "Primary"
+ "Secondary"
+ "T@\"GyroSensorDataInputs\",&,N,V_gyroInputs"
+ "T@\"NSString\",C,N,V_identifier"
+ "_gyroInputs"
+ "_identifier"
+ "containsObject:"
+ "gyro"
+ "gyroInputs"
+ "gyro_1"
+ "identifier"
+ "setGyroInputs:"
+ "setIdentifier:"
+ "setWithObjects:"
+ "targetProduct"
```
