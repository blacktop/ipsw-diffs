## profiled

> `/usr/libexec/profiled`

```diff

-2242.0.0.0.0
-  __TEXT.__text: 0x983c4
+2253.0.0.0.0
+  __TEXT.__text: 0x98d90
   __TEXT.__auth_stubs: 0x2090
-  __TEXT.__objc_stubs: 0xf2c0
-  __TEXT.__objc_methlist: 0x4af0
-  __TEXT.__gcc_except_tab: 0x10e8
-  __TEXT.__oslogstring: 0xc037
+  __TEXT.__objc_stubs: 0xf3a0
+  __TEXT.__objc_methlist: 0x4b98
+  __TEXT.__gcc_except_tab: 0x126c
+  __TEXT.__oslogstring: 0xc01d
   __TEXT.__cstring: 0x89b3
   __TEXT.__const: 0x68
-  __TEXT.__objc_methname: 0x12d1a
-  __TEXT.__objc_classname: 0xb38
-  __TEXT.__objc_methtype: 0x1ff0
-  __TEXT.__unwind_info: 0x156c
+  __TEXT.__objc_methname: 0x12e26
+  __TEXT.__objc_classname: 0xb36
+  __TEXT.__objc_methtype: 0x1ffc
+  __TEXT.__unwind_info: 0x15c4
   __DATA_CONST.__auth_got: 0x1058
-  __DATA_CONST.__got: 0x1570
-  __DATA_CONST.__const: 0x1aa0
+  __DATA_CONST.__got: 0x1580
+  __DATA_CONST.__const: 0x1af0
   __DATA_CONST.__cfstring: 0x8340
   __DATA_CONST.__objc_classlist: 0x2c8
   __DATA_CONST.__objc_catlist: 0x1e8

   __DATA_CONST.__objc_arraydata: 0x28
   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x71c0
-  __DATA.__objc_selrefs: 0x4150
+  __DATA.__objc_const: 0x70f0
+  __DATA.__objc_selrefs: 0x4178
   __DATA.__objc_protorefs: 0x18
-  __DATA.__objc_classrefs: 0x800
+  __DATA.__objc_classrefs: 0x7f8
   __DATA.__objc_superrefs: 0x140
-  __DATA.__objc_ivar: 0x1ec
+  __DATA.__objc_ivar: 0x1c0
   __DATA.__objc_data: 0x1bd0
   __DATA.__data: 0x4ea
   __DATA.__common: 0x18

   - /usr/lib/liblockdown.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: DE1042F8-680A-3142-AD35-9B58A733078D
-  Functions: 1879
-  Symbols:   1423
-  CStrings:  5817
+  UUID: F5037A0D-85A7-3507-B5C1-BB5012D8AAF8
+  Functions: 1900
+  Symbols:   1424
+  CStrings:  5823
 
Symbols:
+ _MCFeatureCrossSiteTrackingPreventionRelaxedApps
+ _OBJC_CLASS_$_DMCHTTPTransaction
+ _kMDMIsADEProfileKey
+ _objc_retain_x10
- _CFAbsoluteTimeGetCurrent
- _OBJC_CLASS_$_MCHTTPTransaction
- _OBJC_CLASS_$_MCWorkerThread
CStrings:
+ "\x06"
+ "@?"
+ "@?16@0:8"
+ "Failed to remove set aside mdm profile. Error: %{public}@"
+ "T@?,C,N,V_accountValidationCompletionHandler"
+ "T@?,C,N,V_preflightCompletionHandler"
+ "_accountValidationCompletionHandler"
+ "_preflightCompletionHandler"
+ "_preflightWithAccount:completionHandler:"
+ "_preflightWithPreflighter:completionHandler:"
+ "accountValidationCompletionHandler"
+ "initWithURL:method:"
+ "preflightCompletionHandler"
+ "removePostSetupAutoInstallSetAsideProfileWithCompletion:"
+ "removeSetAsideCloudConfigurationProfileWithCompletion:"
+ "setAccountValidationCompletionHandler:"
+ "setIsUserEnrollment:"
+ "setPreflightCompletionHandler:"
- "\x01\x12\x16"
- "Passcode recovery not supported but is marked as allowed. Marking it as not allowed"
- "_policyPreflightComplete"
- "_policyPreflightError"
- "_policyPreflightFeatures"
- "_preflightSema"
- "_preflightWithAccount:"
- "_preflightWithPreflighter:"
- "_validationSema"
- "performSelector:onThread:withObject:waitUntilDone:"
- "theThread"
- "transactionWithURL:method:"

```
