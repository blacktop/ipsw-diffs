## Diagnostic-9013

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-9013.appex/Diagnostic-9013`

```diff

-921.120.4.0.0
-  __TEXT.__text: 0x1ac4
-  __TEXT.__auth_stubs: 0x210
-  __TEXT.__objc_stubs: 0x440
+1291.0.0.502.1
+  __TEXT.__text: 0x8d4
+  __TEXT.__auth_stubs: 0x180
+  __TEXT.__objc_stubs: 0x2e0
   __TEXT.__objc_methlist: 0x22c
-  __TEXT.__const: 0x70
-  __TEXT.__cstring: 0x1c5
-  __TEXT.__oslogstring: 0x214
-  __TEXT.__objc_classname: 0x76
-  __TEXT.__objc_methname: 0x4b4
-  __TEXT.__objc_methtype: 0x184
-  __TEXT.__unwind_info: 0xc0
-  __DATA_CONST.__auth_got: 0x110
-  __DATA_CONST.__got: 0x58
-  __DATA_CONST.__const: 0x48
-  __DATA_CONST.__cfstring: 0x200
+  __TEXT.__const: 0x60
+  __TEXT.__cstring: 0xb8
+  __TEXT.__oslogstring: 0x33
+  __TEXT.__objc_classname: 0x74
+  __TEXT.__objc_methname: 0x3ca
+  __TEXT.__objc_methtype: 0x16c
+  __TEXT.__unwind_info: 0x90
+  __DATA_CONST.__const: 0x40
+  __DATA_CONST.__cfstring: 0xc0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x3f8
-  __DATA.__objc_selrefs: 0x1f0
-  __DATA.__objc_ivar: 0xc
+  __DATA_CONST.__auth_got: 0xc8
+  __DATA_CONST.__got: 0x48
+  __DATA.__objc_const: 0x3c8
+  __DATA.__objc_selrefs: 0x1b8
+  __DATA.__objc_ivar: 0x8
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0x120
   __DATA.__bss: 0x20

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 39028B5C-9CE5-3E2E-B061-4448EE34625E
-  Functions: 33
-  Symbols:   64
-  CStrings:  163
+  UUID: BEE78F64-75F8-3020-B2C5-FDB4C7C99475
+  Functions: 19
+  Symbols:   52
+  CStrings:  118
 
Symbols:
+ _OBJC_CLASS_$_CRBatteryController
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x2
+ _objc_retain_x8
- _CRErrorDomain
- _NSLocalizedDescriptionKey
- _OBJC_CLASS_$_CRSmcController
- _OBJC_CLASS_$_NSError
- _objc_opt_class
- _objc_opt_isKindOfClass
- _objc_release
- _objc_release_x23
- _objc_release_x24
- _objc_release_x25
- _objc_release_x26
- _objc_release_x27
- _objc_release_x28
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
- _objc_retain_x22
CStrings:
+ "convertError:"
+ "openGasgauge:"
+ "q24@0:8@16"
+ "setupSMC:"
+ "sharedInstance"
- "@\"CRSmcController\""
- "B32@0:8^I16^@24"
- "BMFL"
- "Enable Gasgauge Manufacturing Lock successfully"
- "Faild to open SMC service, error: %d"
- "Failed to lock Gasgauge, rval: %@"
- "Failed to open SMC port, error: %@"
- "Failed to open SMC service, error: %d"
- "Failed to probe gasgauge status, error: %@"
- "Failed to read SMC key %@, error: %d"
- "Failed to read SMC key: %@, error: %d"
- "Failed to write SMC key %@, error: %d"
- "Gasgauge already locked, exiting..."
- "Gasgauge is locked"
- "Gasgauge is unlocked"
- "Gasgauge locking not required, exiting..."
- "Locking gasgauge..."
- "No input buffer provided for SMC port"
- "SMC controller: %@"
- "SMC key %@ is not available"
- "SMC key %@ is not avalible"
- "T@\"CRSmcController\",R,N,V_smcCtrl"
- "_smcCtrl"
- "closeAppleSMC:"
- "currentGasgaugeLockStatus"
- "doGgLock: %d"
- "errorWithDomain:code:userInfo:"
- "intValue"
- "isSMCKeyAvailable:keyName:"
- "numberWithBool:"
- "openAppleSMC:withRetry:"
- "openSmcAndConfirmKeyAvailable:outError:"
- "previousGasgaugeLockStatus"
- "readSMCKey:keyName:rval:"
- "rval: 0x%X"
- "smcCtrl"
- "stringWithFormat:"
- "writeSMCKey:keyName:data:size:"

```
