## HealthRecordsPluginBundle

> `/System/Library/Health/Plugins/HealthRecordsPluginBundle.bundle/HealthRecordsPluginBundle`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_classlist`
- `__DATA.__objc_data`

```diff

-7027.0.72.2.7
-  __TEXT.__text: 0x440
-  __TEXT.__auth_stubs: 0xd0
-  __TEXT.__objc_stubs: 0x140
-  __TEXT.__objc_methlist: 0x28c
-  __TEXT.__objc_classname: 0x93
-  __TEXT.__objc_methname: 0x3b4
-  __TEXT.__objc_methtype: 0x1e2
-  __TEXT.__unwind_info: 0x90
+7027.1.36.2.7
+  __TEXT.__text: 0x710
+  __TEXT.__auth_stubs: 0x160
+  __TEXT.__objc_stubs: 0x240
+  __TEXT.__objc_methlist: 0x2cc
+  __TEXT.__objc_classname: 0xc6
+  __TEXT.__objc_methname: 0x4f3
+  __TEXT.__objc_methtype: 0x212
+  __TEXT.__const: 0x8
+  __TEXT.__cstring: 0xf
+  __TEXT.__oslogstring: 0x63
+  __TEXT.__unwind_info: 0xa8
+  __DATA_CONST.__cfstring: 0x20
   __DATA_CONST.__objc_classlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x30
+  __DATA_CONST.__objc_catlist: 0x8
+  __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0x70
-  __DATA_CONST.__got: 0xe0
-  __DATA.__objc_const: 0x310
-  __DATA.__objc_selrefs: 0x158
+  __DATA_CONST.__auth_got: 0xb8
+  __DATA_CONST.__got: 0x130
+  __DATA.__objc_const: 0x3d8
+  __DATA.__objc_selrefs: 0x1a8
   __DATA.__objc_data: 0x50
-  __DATA.__data: 0x240
+  __DATA.__data: 0x2a0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/HealthKit.framework/HealthKit
+  - /System/Library/PrivateFrameworks/HealthAppServices.framework/HealthAppServices
   - /System/Library/PrivateFrameworks/HealthDaemon.framework/HealthDaemon
+  - /System/Library/PrivateFrameworks/HealthDaemonFoundation.framework/HealthDaemonFoundation
   - /System/Library/PrivateFrameworks/HealthOntologyDaemon.framework/HealthOntologyDaemon
   - /System/Library/PrivateFrameworks/HealthRecordsPlugin.framework/HealthRecordsPlugin
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 12
-  Symbols:   48
-  CStrings:  83
+  Functions: 17
+  Symbols:   68
+  CStrings:  99
 
Symbols:
+ _HDClinicalAccountEntityPropertySignedClinicalDataIssuerROWID
+ _HDClinicalAccountEntityPropertyUserEnabled
+ _HKLogHealthRecordsCategory
+ _OBJC_CLASS_$_HDClinicalAccountEntity
+ _OBJC_CLASS_$_HDClinicalHealthLinkSyncEntity
+ _OBJC_CLASS_$_HDSQLiteComparisonPredicate
+ _OBJC_CLASS_$_HDSQLiteCompoundPredicate
+ _OBJC_CLASS_$_HDSQLiteNullPredicate
+ _OBJC_CLASS_$_NSDictionary
+ _OBJC_CLASS_$_NSNumber
+ __HKInitializeLogging
+ ___CFConstantStringClassReference
+ ___kCFBooleanTrue
+ __os_log_error_impl
+ _objc_release_x22
+ _objc_release_x23
+ _objc_release_x24
+ _objc_release_x25
+ _objc_retain_x8
+ _os_log_type_enabled
CStrings:
+ "%{public}@: Profile is nil."
+ "@\"NSDictionary\"24@0:8@\"HKAnalyticsDataSource\"16"
+ "DailyAnalytics"
+ "Failed to count CHR accounts for the daily event with error %{public}@"
+ "HealthAppDailyAnalyticsContributing"
+ "countOfObjectsWithPredicate:healthDatabase:error:"
+ "database"
+ "dictionaryWithObjects:forKeys:count:"
+ "isNullPredicateWithProperty:"
+ "isOnboardedCHR"
+ "makeIHAGatedDailyAnalyticsPayloadWithDataSource:"
+ "makeUnrestrictedDailyAnalyticsPayloadWithDataSource:"
+ "numberWithBool:"
+ "predicateMatchingAllPredicates:"
+ "predicateWithProperty:equalToValue:"
+ "profile"
```
