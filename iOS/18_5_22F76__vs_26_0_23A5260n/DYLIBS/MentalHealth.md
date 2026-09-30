## MentalHealth

> `/System/Library/PrivateFrameworks/MentalHealth.framework/MentalHealth`

```diff

-5200.5.1.0.0
-  __TEXT.__text: 0xf9c0
-  __TEXT.__auth_stubs: 0x8b0
-  __TEXT.__objc_methlist: 0xfdc
+6074.1.2.4.0
+  __TEXT.__text: 0xf480
+  __TEXT.__auth_stubs: 0x8c0
+  __TEXT.__objc_methlist: 0xff4
   __TEXT.__const: 0x948
   __TEXT.__oslogstring: 0x5d3
-  __TEXT.__cstring: 0xa1c
+  __TEXT.__cstring: 0xa5c
   __TEXT.__gcc_except_tab: 0x80
   __TEXT.__constg_swiftt: 0x1e4
   __TEXT.__swift5_typeref: 0x114

   __TEXT.__swift5_assocty: 0xd8
   __TEXT.__swift5_proto: 0x74
   __TEXT.__swift5_types: 0x34
-  __TEXT.__unwind_info: 0x628
-  __TEXT.__eh_frame: 0x174
+  __TEXT.__unwind_info: 0x600
+  __TEXT.__eh_frame: 0x110
   __TEXT.__objc_classname: 0x378
-  __TEXT.__objc_methname: 0x1ce3
-  __TEXT.__objc_methtype: 0x539
-  __TEXT.__objc_stubs: 0x1140
-  __DATA_CONST.__got: 0x218
-  __DATA_CONST.__const: 0x448
+  __TEXT.__objc_methname: 0x1def
+  __TEXT.__objc_methtype: 0x547
+  __TEXT.__objc_stubs: 0x1280
+  __DATA_CONST.__got: 0x230
+  __DATA_CONST.__const: 0x428
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x738
+  __DATA_CONST.__objc_selrefs: 0x788
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0xb0
-  __AUTH_CONST.__auth_got: 0x468
+  __AUTH_CONST.__auth_got: 0x470
   __AUTH_CONST.__const: 0x338
-  __AUTH_CONST.__cfstring: 0x860
+  __AUTH_CONST.__cfstring: 0x8c0
   __AUTH_CONST.__objc_const: 0x1da0
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__data: 0x230

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/HealthKit.framework/HealthKit
   - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
-  - /System/Library/PrivateFrameworks/ToneLibrary.framework/ToneLibrary
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftCore.dylib

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_errno.dylib
-  - /usr/lib/swift/libswift_math.dylib
-  - /usr/lib/swift/libswift_signal.dylib
-  - /usr/lib/swift/libswift_stdio.dylib
-  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 714D5235-6594-39A6-8730-338088BE28DA
-  Functions: 522
-  Symbols:   1340
-  CStrings:  588
+  UUID: F9580537-B278-30BA-8291-3F580FBF4013
+  Functions: 523
+  Symbols:   1347
+  CStrings:  605
 
Symbols:
+ +[UNNotificationRequest(HKMentalHealth) _notificationRequestIdentifierForCategoryIdentifier:date:]
+ +[UNNotificationRequest(HKMentalHealth) _stringForEventDate:]
+ +[UNNotificationRequest(HKMentalHealth) hkmh_requestForCategoryIdentifier:date:]
+ _HKMHLocalizedNotificationString
+ _OBJC_CLASS_$_NSDateFormatter
+ _OBJC_CLASS_$_NSLocale
+ _OBJC_CLASS_$_NSTimeZone
+ ___118-[HKMHValenceDistributionSummaryQuery client_deliverValenceDistributionSummaries:clearPending:isFinalBatch:queryUUID:]_block_invoke.290
+ ___53-[HKMHPromptedAssessmentsManager unregisterObserver:]_block_invoke.301
+ ___66-[HKMHValenceSummaryQuery client_deliverValenceSummary:queryUUID:]_block_invoke.289
+ ___75-[HKMHPromptedAssessmentsManager registerObserver:queue:activationHandler:]_block_invoke.298
+ ___78-[HKMHMostPrevalentDomainsQuery client_deliverMostPrevalentDomains:queryUUID:]_block_invoke.289
+ ___86-[HKMHDaySummaryQuery client_deliverDaySummaries:clearPending:isFinalBatch:queryUUID:]_block_invoke.289
+ ___block_literal_global.291
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_MentalHealth
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_MentalHealth
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_MentalHealth
+ _objc_msgSend$_notificationRequestIdentifierForCategoryIdentifier:date:
+ _objc_msgSend$_stringForEventDate:
+ _objc_msgSend$localeWithLocaleIdentifier:
+ _objc_msgSend$localizedUserNotificationStringForKey:arguments:
+ _objc_msgSend$setDateFormat:
+ _objc_msgSend$setLocale:
+ _objc_msgSend$setTimeZone:
+ _objc_msgSend$stringByAppendingFormat:
+ _objc_msgSend$stringFromDate:
+ _objc_msgSend$timeZoneForSecondsFromGMT:
+ _swift_unknownObjectRelease
- +[UNNotificationRequest(HKMentalHealth) hkmh_requestForCategoryIdentifier:]
- ___118-[HKMHValenceDistributionSummaryQuery client_deliverValenceDistributionSummaries:clearPending:isFinalBatch:queryUUID:]_block_invoke.287
- ___53-[HKMHPromptedAssessmentsManager unregisterObserver:]_block_invoke.298
- ___66-[HKMHValenceSummaryQuery client_deliverValenceSummary:queryUUID:]_block_invoke.286
- ___75-[HKMHPromptedAssessmentsManager registerObserver:queue:activationHandler:]_block_invoke.295
- ___78-[HKMHMostPrevalentDomainsQuery client_deliverMostPrevalentDomains:queryUUID:]_block_invoke.286
- ___86-[HKMHDaySummaryQuery client_deliverDaySummaries:clearPending:isFinalBatch:queryUUID:]_block_invoke.286
- ___block_literal_global.288
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_errno_$_MentalHealth
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_math_$_MentalHealth
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_signal_$_MentalHealth
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_stdio_$_MentalHealth
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swift_time_$_MentalHealth
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftsys_time_$_MentalHealth
- __swift_FORCE_LOAD_$_swiftunistd
- __swift_FORCE_LOAD_$_swiftunistd_$_MentalHealth
CStrings:
+ "@32@0:8@16@24"
+ "NOTIFICATION_MENTAL_HEALTH_PERIODIC_PROMPTED_ASSESSMENTS_BODY_IOS"
+ "NOTIFICATION_MENTAL_HEALTH_PERIODIC_PROMPTED_ASSESSMENTS_TITLE"
+ "_%@"
+ "_notificationRequestIdentifierForCategoryIdentifier:date:"
+ "_stringForEventDate:"
+ "en_US_POSIX"
+ "hkmh_requestForCategoryIdentifier:date:"
+ "localeWithLocaleIdentifier:"
+ "localizedUserNotificationStringForKey:arguments:"
+ "setDateFormat:"
+ "setLocale:"
+ "setTimeZone:"
+ "stringByAppendingFormat:"
+ "stringFromDate:"
+ "timeZoneForSecondsFromGMT:"
+ "yyyy-MM-dd_HH:mm"
- "NOTIFICATION_PERIODIC_PROMPTED_ASSESSMENTS_BODY_IOS"
- "NOTIFICATION_PERIODIC_PROMPTED_ASSESSMENTS_TITLE"
- "hkmh_requestForCategoryIdentifier:"

```
