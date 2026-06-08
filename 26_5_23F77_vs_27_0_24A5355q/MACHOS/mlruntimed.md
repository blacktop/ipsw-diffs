## mlruntimed

> `/usr/libexec/mlruntimed`

```diff

-111.1.0.0.0
-  __TEXT.__text: 0x23a4
-  __TEXT.__auth_stubs: 0x4c0
-  __TEXT.__objc_stubs: 0x920
-  __TEXT.__objc_methlist: 0x42c
+113.0.0.0.0
+  __TEXT.__text: 0x18a8
+  __TEXT.__auth_stubs: 0x480
+  __TEXT.__objc_stubs: 0x660
+  __TEXT.__objc_methlist: 0x3b4
   __TEXT.__const: 0x80
-  __TEXT.__oslogstring: 0x354
-  __TEXT.__cstring: 0x135
-  __TEXT.__objc_classname: 0xb6
-  __TEXT.__objc_methname: 0xa6d
-  __TEXT.__objc_methtype: 0x36e
-  __TEXT.__gcc_except_tab: 0x50
-  __TEXT.__unwind_info: 0x110
-  __DATA_CONST.__auth_got: 0x270
-  __DATA_CONST.__got: 0x140
+  __TEXT.__oslogstring: 0x32c
+  __TEXT.__cstring: 0xcf
+  __TEXT.__objc_methname: 0x846
+  __TEXT.__objc_classname: 0xa3
+  __TEXT.__objc_methtype: 0x318
+  __TEXT.__gcc_except_tab: 0x2c
+  __TEXT.__unwind_info: 0xe8
   __DATA_CONST.__const: 0xe8
-  __DATA_CONST.__cfstring: 0xc0
+  __DATA_CONST.__cfstring: 0x40
   __DATA_CONST.__objc_classlist: 0x20
-  __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x18
-  __DATA.__objc_const: 0x808
-  __DATA.__objc_selrefs: 0x328
+  __DATA_CONST.__auth_got: 0x250
+  __DATA_CONST.__got: 0xd0
+  __DATA.__objc_const: 0x780
+  __DATA.__objc_selrefs: 0x260
   __DATA.__objc_ivar: 0x2c
   __DATA.__objc_data: 0x140
   __DATA.__data: 0x180

   - /System/Library/PrivateFrameworks/MLRuntime.framework/MLRuntime
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/Trial.framework/Trial
-  - /System/Library/PrivateFrameworks/TrialProto.framework/TrialProto
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B2AA0256-369C-3E2E-8B36-A4605BAF1889
-  Functions: 57
-  Symbols:   125
-  CStrings:  215
+  UUID: 32071E6F-6E3D-3AF7-ADE2-6B571389D535
+  Functions: 50
+  Symbols:   107
+  CStrings:  177
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x22
+ _objc_retain_x3
- _NSCocoaErrorDomain
- _NSInvalidArgumentException
- _NSLocalizedDescriptionKey
- _OBJC_CLASS_$_DESServiceAccess
- _OBJC_CLASS_$_MLRTrialDediscoTaskResult
- _OBJC_CLASS_$_NSDictionary
- _OBJC_CLASS_$_NSError
- _OBJC_CLASS_$_NSException
- _OBJC_CLASS_$_NSNumber
- _OBJC_CLASS_$_TRIClient
- _OBJC_CLASS_$_TRIPBListValue
- _OBJC_CLASS_$_TRIPBStruct
- _OBJC_CLASS_$_TRIPBValue
- _kDESDistributedEvaluationErrorDomain
- _objc_autorelease
- _objc_exception_throw
- _objc_opt_class
- _objc_opt_isKindOfClass
- _objc_release_x24
- _objc_release_x25
- _objc_retain
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x23
CStrings:
- "@20@0:8B16"
- "MLRTestUtils"
- "Unexpected type in obj"
- "Unknown identifier = %@"
- "addObject:"
- "clientWithIdentifier:"
- "dictionaryWithObjects:forKeys:count:"
- "donateJSONResult may only be called by internal tool."
- "donateJSONResult:identifier:completion:"
- "doubleValue"
- "errorWithDomain:code:userInfo:"
- "exceptionWithName:reason:userInfo:"
- "fields"
- "hasMLRCtlEntitlement:"
- "initWithJSONResult:identifier:"
- "mlr_listValueWithNSArray:"
- "mlr_structWithDictionary:"
- "mlr_valueWithBoolValue:"
- "mlr_valueWithNullValue"
- "mlr_valueWithObject:"
- "obj=%@"
- "objectForKeyedSubscript:"
- "setBoolValue:"
- "setListValue:"
- "setNullValue:"
- "setNumberValue:"
- "setObject:forKeyedSubscript:"
- "setStringValue:"
- "setStructValue:"
- "start donating result=%@, identifier=%@"
- "submitWithTRIClient:error:"
- "v40@0:8@\"NSDictionary\"16@\"NSString\"24@?<v@?@\"NSError\">32"
- "v40@0:8@16@24@?32"
- "valuesArray"

```
