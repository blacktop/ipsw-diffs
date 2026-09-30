## LighthouseServicesAnalyticsExtension

> `/System/Library/ExtensionKit/Extensions/LighthouseServicesAnalyticsExtension.appex/LighthouseServicesAnalyticsExtension`

```diff

-1.0.15.0.0
-  __TEXT.__text: 0x8c70
-  __TEXT.__auth_stubs: 0x980
-  __TEXT.__const: 0x4de
-  __TEXT.__cstring: 0x411
-  __TEXT.__objc_methname: 0xe4
+1.1.1.0.0
+  __TEXT.__text: 0x46b4
+  __TEXT.__auth_stubs: 0x4b0
+  __TEXT.__const: 0x13a
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0x84
-  __TEXT.__swift5_typeref: 0x205
-  __TEXT.__swift5_fieldmd: 0x1b4
-  __TEXT.__swift5_reflstr: 0x2ea
-  __TEXT.__swift5_assocty: 0x30
-  __TEXT.__swift5_capture: 0x24
-  __TEXT.__oslogstring: 0x419
-  __TEXT.__swift5_proto: 0x3c
-  __TEXT.__swift5_types: 0x10
-  __TEXT.__swift_as_entry: 0x14
-  __TEXT.__swift_as_ret: 0x18
-  __TEXT.__unwind_info: 0x208
-  __TEXT.__eh_frame: 0x2c8
-  __DATA_CONST.__auth_got: 0x4c0
-  __DATA_CONST.__got: 0x158
-  __DATA_CONST.__auth_ptr: 0x1d8
-  __DATA_CONST.__const: 0x500
+  __TEXT.__constg_swiftt: 0x28
+  __TEXT.__swift5_typeref: 0x93
+  __TEXT.__swift5_fieldmd: 0x10
+  __TEXT.__swift5_reflstr: 0xe
+  __TEXT.__swift5_assocty: 0x18
+  __TEXT.__oslogstring: 0x2f9
+  __TEXT.__cstring: 0x45
+  __TEXT.__objc_methname: 0x30
+  __TEXT.__swift5_proto: 0x8
+  __TEXT.__swift5_types: 0x4
+  __TEXT.__swift_as_entry: 0x18
+  __TEXT.__swift_as_ret: 0x1c
+  __TEXT.__unwind_info: 0x130
+  __TEXT.__eh_frame: 0x238
+  __DATA_CONST.__auth_got: 0x258
+  __DATA_CONST.__got: 0xa0
+  __DATA_CONST.__auth_ptr: 0x90
+  __DATA_CONST.__const: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_selrefs: 0x58
-  __DATA.__data: 0x128
-  __DATA.__bss: 0x7d0
+  __DATA.__objc_selrefs: 0x18
+  __DATA.__data: 0x68
+  __DATA.__bss: 0x110
   __DATA.__common: 0x18
-  - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
-  - /System/Library/Frameworks/TabularData.framework/TabularData
   - /System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices
-  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/LighthouseBackground.framework/LighthouseBackground
   - /System/Library/PrivateFrameworks/LighthouseServicesAnalyticsFramework.framework/LighthouseServicesAnalyticsFramework
-  - /System/Library/PrivateFrameworks/PrivateFederatedLearning.framework/PrivateFederatedLearning
+  - /System/Library/PrivateFrameworks/OnDeviceStorage.framework/OnDeviceStorage
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: B8F7F8F2-2BAD-36F3-9BA5-8895F17F44B3
-  Functions: 137
-  Symbols:   100
-  CStrings:  62
+  UUID: 0DD01219-F53B-3442-870D-298C3703ABBA
+  Functions: 50
+  Symbols:   63
+  CStrings:  22
 
Symbols:
+ _swift_allocBox
- _AnalyticsSendEventLazy
- _OBJC_CLASS_$_ACAccountStore
- _OBJC_CLASS_$_FedStatsDataEncoder
- _OBJC_CLASS_$_NSNumber
- _OBJC_CLASS_$_NSObject
- _OBJC_CLASS_$_NSString
- __Block_copy
- __Block_release
- __NSConcreteStackBlock
- ___chkstk_darwin
- ___stack_chk_fail
- ___stack_chk_guard
- __swiftEmptyDictionarySingleton
- _bzero
- _objc_autoreleaseReturnValue
- _objc_opt_self
- _objc_release_x22
- _objc_release_x26
- _objc_release_x28
- _objc_release_x8
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x21
- _objc_retain_x23
- _objc_retain_x28
- _os_variant_has_internal_diagnostics
- _swift_arrayDestroy
- _swift_arrayInitWithCopy
- _swift_cvw_assignWithCopy
- _swift_cvw_assignWithTake
- _swift_cvw_destroy
- _swift_cvw_initWithCopy
- _swift_cvw_initializeBufferWithCopyOfBuffer
- _swift_deallocObject
- _swift_getObjCClassMetadata
- _swift_initStackObject
- _swift_retain
- _swift_setDeallocating
- _swift_willThrow
CStrings:
+ "%s has already run"
+ "An unknown error occurred while querying: %@"
+ "Error occurred while querying: %@"
+ "Error occurred while uploading rows: %@"
+ "Failed to create an upload config: %@"
+ "Failed to get DSID: %@"
+ "Failed to instantiate UserDefaults with suiteName: %s"
+ "Failed to instantiate UserDefaults(%s"
+ "Failed to load AnalyticsExtensionConfig"
+ "Loaded AnalyticsExtensionConfig: %s"
+ "No data was returned for the query"
+ "Retrieved %ld rows from query"
+ "Storefront check failed: %@"
+ "Successfully executed query and uploaded to transport"
+ "Unknown error occurred while uploading rows: %@"
- "\n %s"
- "%s has already run, exiting early."
- "@\"NSDictionary\"8@?0"
- "AnalyticsExtensionConfig("
- "Attempting to use both allowStorefronts and skipStorefronts, exiting early."
- "Configuration: %s"
- "Context in doWork: %@"
- "Couldn't find dediscoParameters, exiting early."
- "DeDisco taskConfig: %s"
- "Device's storefront %s is in the allow list."
- "Device's storefront %s is not in the skip list."
- "Duration: %s"
- "Encountered error when opening connection. Exiting early."
- "Encountered error when querying connection: %@. Exiting early."
- "Encountered error without specific handling logic: %@"
- "Failed to instantiate userDefaults with suiteName: %s, exiting early."
- "Failed to load config, exiting early."
- "Invalid AMS DSID, exiting early."
- "No data was returned from the query, exiting early"
- "Storefront %s is in the skip list, exiting early."
- "Storefront %s is not in the allow list, exiting early."
- "Unable to determine storefront, exiting early."
- "allowStorefronts"
- "ams_DSID"
- "ams_activeiTunesAccount"
- "ams_sharedAccountStore"
- "ams_storefront"
- "attemptingToAccessColumnsNotInAccessCredential"
- "attemptingToAccessNonExistentDatabase"
- "attemptingToAccessTablesNotInAccessCredential"
- "cancelled"
- "com.apple.LighthouseServicesAnalytics.QueryMetrics"
- "com.apple.lighthouse.LighthouseServicesAnalyticsExtension"
- "com.apple.lighthouse.LighthouseServicesAnalyticsExtension:MLHost:"
- "deDiscoEncodingKeyHadNoMatchInRow"
- "encodeDataAndRecord:dataTypeContent:metadata:baseKey:errorOut:"
- "errorOpeningConnection"
- "errorQueryingConnection"
- "failedToInstantiateUserDefaults"
- "failedToLoadConfig"
- "hasAlreadyRun"
- "initWithLongLong:"
- "initWithString:"
- "invalidAMSDSID"
- "malformedQuery"
- "missingDeDiscoParameters"
- "noDataReturned"
- "setBothAllowAndSkipListForStorefronts"
- "storefrontIsInSkipList"
- "storefrontIsNotInAllowList"
- "stringValue"
- "tableUsedInSelectIsNotInFromClause"
- "unableToDetermineStorefront"
- "unexpectedErrorOccurred"
- "unexpectedFieldType"

```
