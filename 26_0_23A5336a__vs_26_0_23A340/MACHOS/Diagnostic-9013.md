## Diagnostic-9013

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-9013.appex/Diagnostic-9013`

```diff

 921.0.120.0.0
-  __TEXT.__text: 0x360
-  __TEXT.__auth_stubs: 0x120
-  __TEXT.__objc_stubs: 0xe0
-  __TEXT.__objc_methlist: 0x2c
-  __TEXT.__const: 0x48
-  __TEXT.__cstring: 0x3d
-  __TEXT.__oslogstring: 0x1a
-  __TEXT.__objc_classname: 0xa
-  __TEXT.__objc_methname: 0x89
-  __TEXT.__objc_methtype: 0x13
-  __TEXT.__unwind_info: 0x78
-  __DATA_CONST.__auth_got: 0x98
-  __DATA_CONST.__got: 0x20
-  __DATA_CONST.__const: 0x40
-  __DATA_CONST.__cfstring: 0x20
+  __TEXT.__text: 0x1a48
+  __TEXT.__auth_stubs: 0x1f0
+  __TEXT.__objc_stubs: 0x440
+  __TEXT.__objc_methlist: 0x23c
+  __TEXT.__const: 0x78
+  __TEXT.__cstring: 0x1a8
+  __TEXT.__oslogstring: 0x22f
+  __TEXT.__objc_classname: 0x76
+  __TEXT.__objc_methname: 0x4c6
+  __TEXT.__objc_methtype: 0x184
+  __TEXT.__unwind_info: 0xb8
+  __DATA_CONST.__auth_got: 0x100
+  __DATA_CONST.__got: 0x58
+  __DATA_CONST.__const: 0x48
+  __DATA_CONST.__cfstring: 0x1e0
+  __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_catlist: 0x8
+  __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0x40
-  __DATA.__objc_selrefs: 0x48
+  __DATA_CONST.__objc_intobj: 0x18
+  __DATA.__objc_const: 0x428
+  __DATA.__objc_selrefs: 0x1f0
+  __DATA.__objc_ivar: 0x10
+  __DATA.__objc_data: 0xa0
+  __DATA.__data: 0x120
   __DATA.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F62BFA3B-5899-3DDB-95C1-E88A4DE36C9D
-  Functions: 6
-  Symbols:   31
-  CStrings:  20
+  UUID: 836A9400-26F3-3116-8075-BE071E719F68
+  Functions: 30
+  Symbols:   62
+  CStrings:  164
 
Symbols:
+ _CRErrorDomain
+ _NSLocalizedDescriptionKey
+ _OBJC_CLASS_$_BatteryGasgaugeController
+ _OBJC_CLASS_$_BatteryGasgaugeControllerInputs
+ _OBJC_CLASS_$_CRSmcController
+ _OBJC_CLASS_$_DKDiagnosticController
+ _OBJC_CLASS_$_NSConstantIntegerNumber
+ _OBJC_CLASS_$_NSDictionary
+ _OBJC_CLASS_$_NSError
+ _OBJC_CLASS_$_NSNull
+ _OBJC_CLASS_$_NSNumber
+ _OBJC_CLASS_$_NSObject
+ _OBJC_METACLASS_$_BatteryGasgaugeController
+ _OBJC_METACLASS_$_BatteryGasgaugeControllerInputs
+ _OBJC_METACLASS_$_DKDiagnosticController
+ _OBJC_METACLASS_$_NSObject
+ ___stack_chk_fail
+ ___stack_chk_guard
+ __objc_empty_cache
+ __os_log_impl
+ _objc_opt_class
+ _objc_opt_isKindOfClass
+ _objc_release_x21
+ _objc_release_x22
+ _objc_release_x23
+ _objc_release_x24
+ _objc_release_x25
+ _objc_release_x26
+ _objc_release_x27
+ _objc_retain_x21
+ _objc_storeStrong
CStrings:
+ "#16@0:8"
+ "%s"
+ "%s: %@, %@"
+ "-[BatteryGasgaugeController setupWithInputs:responder:]"
+ "-[BatteryGasgaugeController start]"
+ ".cxx_destruct"
+ "@\"BatteryGasgaugeControllerInputs\""
+ "@\"CRSmcController\""
+ "@\"NSNumber\"32@0:8@\"<DKDiagnosticInputs>\"16^@24"
+ "@\"NSString\"16@0:8"
+ "@24@0:8:16"
+ "@32@0:8:16@24"
+ "@32@0:8@16^@24"
+ "@40@0:8:16@24@32"
+ "B"
+ "B16@0:8"
+ "B24@0:8#16"
+ "B24@0:8:16"
+ "B24@0:8@\"NSDictionary\"16"
+ "B24@0:8@\"Protocol\"16"
+ "B24@0:8@16"
+ "B24@0:8^@16"
+ "B32@0:8^I16^@24"
+ "BMFL"
+ "BOOLFromKey:defaultValue:failed:"
+ "BatteryGasgaugeController"
+ "BatteryGasgaugeControllerInputs"
+ "DKControllerAdaptor"
+ "DKDiagnosticInputs"
+ "Enable Gasgauge Manufacturing Lock successfully"
+ "Faild to open SMC service, error: %d"
+ "Failed to lock Gasgauge, rval: %@"
+ "Failed to open SMC port, error: %@"
+ "Failed to open SMC service, error: %d"
+ "Failed to probe gasgauge status, error: %@"
+ "Failed to read SMC key %@, error: %d"
+ "Failed to read SMC key: %@, error: %d"
+ "Failed to write SMC key %@, error: %d"
+ "Gasgauge already locked, exiting..."
+ "Gasgauge is locked"
+ "Gasgauge is unlocked"
+ "Gasgauge locking not required, exiting..."
+ "Lock"
+ "Locking gasgauge..."
+ "NO"
+ "NSObject"
+ "No input buffer provided for SMC port"
+ "Q16@0:8"
+ "SMC controller: %@"
+ "SMC key %@ is not available"
+ "SMC key %@ is not avalible"
+ "T#,R"
+ "T@\"BatteryGasgaugeControllerInputs\",&,N,V_inputs"
+ "T@\"CRSmcController\",R,N,V_smcCtrl"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",R,C"
+ "TB,R,N,V_ggLock"
+ "TB,R,N,V_ggReset"
+ "TQ,R"
+ "Vv16@0:8"
+ "YES"
+ "^{_NSZone=}16@0:8"
+ "_ggLock"
+ "_ggReset"
+ "_inputs"
+ "_smcCtrl"
+ "autorelease"
+ "cancel"
+ "class"
+ "closeAppleSMC:"
+ "code"
+ "conformsToProtocol:"
+ "debugDescription"
+ "description"
+ "dictionaryWithObjects:forKeys:count:"
+ "doGgLock: %d, doGgReset: %d"
+ "error"
+ "errorCode"
+ "errorWithDomain:code:userInfo:"
+ "ggLock"
+ "ggLock: %@"
+ "ggReset"
+ "ggReset: %@"
+ "hash"
+ "inputs"
+ "intValue"
+ "isEqual:"
+ "isGasgaugeLocked:"
+ "isKindOfClass:"
+ "isMemberOfClass:"
+ "isProxy"
+ "isSMCKeyAvailable:keyName:"
+ "lockGasgauge:"
+ "null"
+ "numberWithInteger:"
+ "openAppleSMC:withRetry:"
+ "openSmcAndConfirmKeyAvailable:outError:"
+ "performSelector:"
+ "performSelector:withObject:"
+ "performSelector:withObject:withObject:"
+ "q"
+ "readSMCKey:keyName:rval:"
+ "release"
+ "respondsToSelector:"
+ "result"
+ "retain"
+ "retainCount"
+ "runWithInputs:results:"
+ "rval: 0x%X"
+ "self"
+ "setData:"
+ "setFinished:"
+ "setInputs:"
+ "setStatusCode:"
+ "setupWithInputs:responder:"
+ "shouldResetLifeTimeTemp"
+ "smcCtrl"
+ "start"
+ "stringWithFormat:"
+ "superclass"
+ "v16@0:8"
+ "v24@0:8@16"
+ "v32@0:8@16@24"
+ "validateAndInitializeParameters:"
+ "validateAndInitializePredicates:"
+ "validateAndInitializeSpecifications:"
+ "writeSMCKey:keyName:data:size:"
+ "zone"

```
