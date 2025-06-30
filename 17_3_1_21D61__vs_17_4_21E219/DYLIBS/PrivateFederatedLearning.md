## PrivateFederatedLearning

> `/System/Library/PrivateFrameworks/PrivateFederatedLearning.framework/PrivateFederatedLearning`

```diff

-211.0.0.0.0
-  __TEXT.__text: 0x24c24
-  __TEXT.__auth_stubs: 0x780
-  __TEXT.__objc_methlist: 0x2820
+214.0.0.0.0
+  __TEXT.__text: 0x24d64
+  __TEXT.__auth_stubs: 0x7a0
+  __TEXT.__objc_methlist: 0x287c
   __TEXT.__const: 0x388
-  __TEXT.__cstring: 0x2c9c
+  __TEXT.__cstring: 0x2c53
   __TEXT.__oslogstring: 0x1d30
   __TEXT.__gcc_except_tab: 0x224
   __TEXT.__ustring: 0x1e
-  __TEXT.__unwind_info: 0x878
-  __TEXT.__objc_classname: 0x70f
-  __TEXT.__objc_methname: 0x4d47
+  __TEXT.__unwind_info: 0x890
+  __TEXT.__objc_classname: 0x72d
+  __TEXT.__objc_methname: 0x4db1
   __TEXT.__objc_methtype: 0xaff
-  __TEXT.__objc_stubs: 0x4180
+  __TEXT.__objc_stubs: 0x41c0
   __DATA_CONST.__got: 0xb0
   __DATA_CONST.__const: 0x4f8
-  __DATA_CONST.__objc_classlist: 0x200
+  __DATA_CONST.__objc_classlist: 0x208
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x5038
-  __DATA_CONST.__objc_selrefs: 0x13e8
+  __DATA_CONST.__objc_const: 0x50d8
+  __DATA_CONST.__objc_selrefs: 0x1400
+  __DATA_CONST.__objc_protorefs: 0x10
+  __DATA_CONST.__objc_classrefs: 0x350
+  __DATA_CONST.__objc_superrefs: 0x1a0
   __DATA_CONST.__objc_arraydata: 0x130
-  __AUTH_CONST.__objc_const: 0x1c98
-  __AUTH_CONST.__cfstring: 0x2d00
+  __AUTH_CONST.__objc_const: 0x1d28
+  __AUTH_CONST.__cfstring: 0x2c40
   __AUTH_CONST.__const: 0x1a0
   __AUTH_CONST.__objc_intobj: 0x108
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x78
-  __AUTH_CONST.__auth_got: 0x3d8
-  __AUTH.__objc_data: 0x1400
-  __DATA.__objc_protorefs: 0x10
-  __DATA.__objc_classrefs: 0x348
-  __DATA.__objc_superrefs: 0x198
-  __DATA.__objc_ivar: 0x284
+  __AUTH_CONST.__auth_got: 0x3e8
+  __AUTH.__objc_data: 0x1450
+  __DATA.__objc_ivar: 0x288
   __DATA.__data: 0x600
-  __DATA.__bss: 0xc8
+  __DATA.__bss: 0xd8
   __DATA.__common: 0x10
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 43E96910-7D23-3EEC-94F7-C5C822DC9AE6
-  Functions: 965
-  Symbols:   3533
-  CStrings:  2057
+  UUID: 75D103E4-5E75-36A9-8651-84BFEE58FEA8
+  Functions: 972
+  Symbols:   3565
+  CStrings:  2052
 
Symbols:
+ +[FedStatsCohortQueryDeviceType cohortInstance]
+ -[FedStatsCohortQueryDeviceType .cxx_destruct]
+ -[FedStatsCohortQueryDeviceType cohortKeyForParameters:possibleError:]
+ -[FedStatsCohortQueryDeviceType deviceType]
+ -[FedStatsCohortQueryDeviceType initWithDeviceType:]
+ -[FedStatsCohortQueryDeviceType setDeviceType:]
+ _OBJC_CLASS_$_FedStatsCohortQueryDeviceType
+ _OBJC_IVAR_$_FedStatsCohortQueryDeviceType._deviceType
+ _OBJC_METACLASS_$_FedStatsCohortQueryDeviceType
+ __OBJC_$_CLASS_METHODS_FedStatsCohortQueryDeviceType
+ __OBJC_$_INSTANCE_METHODS_FedStatsCohortQueryDeviceType
+ __OBJC_$_INSTANCE_VARIABLES_FedStatsCohortQueryDeviceType
+ __OBJC_$_PROP_LIST_FedStatsCohortQueryDeviceType
+ __OBJC_CLASS_PROTOCOLS_$_FedStatsCohortQueryDeviceType
+ __OBJC_CLASS_RO_$_FedStatsCohortQueryDeviceType
+ __OBJC_METACLASS_RO_$_FedStatsCohortQueryDeviceType
+ ___47+[FedStatsCohortQueryDeviceType cohortInstance]_block_invoke
+ __unnamed_array_storage.432
+ __unnamed_array_storage.435
+ __unnamed_array_storage.439
+ _cohortInstance.cohortInstance
+ _cohortInstance.onceToken
+ _objc_msgSend$deviceType
+ _objc_msgSend$initWithDeviceType:
+ _objc_setProperty_atomic
+ _sharedInstance.onceToken.151
+ _uname
- __unnamed_array_storage.431
- __unnamed_array_storage.433
- __unnamed_array_storage.437
- _sharedInstance.onceToken.168
CStrings:
+ "FedStatsCohortQueryDeviceType"
+ "T@\"NSString\",&,V_deviceType"
+ "T@\"NSString\",?,R,C"
+ "_deviceType"
+ "accessedPropertyDirectly"
+ "deviceType"
+ "gestureAssessment"
+ "initWithDeviceType:"
+ "livenessAssessment"
+ "property"
+ "setDeviceType:"
- "choice"
- "completedSetup"
- "enabled"
- "firstUpdate"
- "firstUpdateAnyGesture"
- "flowType"
- "inputMode"
- "numberSearchQueriesRun"
- "pillClicked"
- "resultPosition"
- "wasPositiveEngagement"

```
