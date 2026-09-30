## Safety

> `/System/Library/Health/FeedItemPlugins/Safety.healthplugin/Safety`

```diff

-5132.0.0.0.0
-  __TEXT.__text: 0x80798
-  __TEXT.__auth_stubs: 0x26e0
-  __TEXT.__objc_methlist: 0x5ac
-  __TEXT.__const: 0x3934
-  __TEXT.__cstring: 0x4725
-  __TEXT.__swift5_typeref: 0x11a0
-  __TEXT.__swift5_fieldmd: 0x104c
+5200.1.3.0.0
+  __TEXT.__text: 0x81dec
+  __TEXT.__auth_stubs: 0x27c0
+  __TEXT.__objc_methlist: 0x58c
+  __TEXT.__const: 0x3924
+  __TEXT.__cstring: 0x4745
+  __TEXT.__swift5_typeref: 0x11a2
+  __TEXT.__swift5_fieldmd: 0x1058
   __TEXT.__constg_swiftt: 0x2844
-  __TEXT.__swift5_reflstr: 0x1378
+  __TEXT.__swift5_reflstr: 0x1398
   __TEXT.__swift5_builtin: 0xb4
   __TEXT.__swift5_assocty: 0x238
-  __TEXT.__swift5_capture: 0xa28
-  __TEXT.__oslogstring: 0x1dcb
+  __TEXT.__swift5_capture: 0xa38
+  __TEXT.__oslogstring: 0x1fbb
   __TEXT.__swift5_protos: 0x24
   __TEXT.__swift5_proto: 0x300
   __TEXT.__swift5_types: 0x168
-  __TEXT.__unwind_info: 0x1920
+  __TEXT.__unwind_info: 0x1940
   __TEXT.__eh_frame: 0x470
   __TEXT.__objc_classname: 0x12f
-  __TEXT.__objc_methname: 0x233c
+  __TEXT.__objc_methname: 0x23d7
   __TEXT.__objc_methtype: 0x444
-  __DATA_CONST.__got: 0x958
-  __DATA_CONST.__const: 0xe0
+  __DATA_CONST.__got: 0x9b8
+  __DATA_CONST.__const: 0x120
   __DATA_CONST.__objc_classlist: 0x138
-  __DATA_CONST.__objc_catlist2: 0x30
+  __DATA_CONST.__objc_catlist2: 0x28
   __DATA_CONST.__objc_protolist: 0xd0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9c8
+  __DATA_CONST.__objc_selrefs: 0x9f0
   __DATA_CONST.__objc_protorefs: 0x68
-  __AUTH_CONST.__auth_got: 0x1370
-  __AUTH_CONST.__auth_ptr: 0xaf0
-  __AUTH_CONST.__const: 0x2120
-  __AUTH_CONST.__objc_const: 0x3538
-  __AUTH.__objc_data: 0x17e0
+  __AUTH_CONST.__auth_got: 0x13e0
+  __AUTH_CONST.__auth_ptr: 0xb08
+  __AUTH_CONST.__const: 0x2148
+  __AUTH_CONST.__objc_const: 0x3508
+  __AUTH.__objc_data: 0x17c0
   __AUTH.__data: 0x708
   __DATA.__data: 0xff8
   __DATA.__objc_stublist: 0xa0
   __DATA.__common: 0x150
   __DATA.__bss: 0x3400
-  __DATA_DIRTY.__objc_data: 0x1250
-  __DATA_DIRTY.__data: 0x2578
+  __DATA_DIRTY.__objc_data: 0x1268
+  __DATA_DIRTY.__data: 0x25d8
   __DATA_DIRTY.__common: 0x230
   __DATA_DIRTY.__bss: 0x1c80
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /System/Library/PrivateFrameworks/OnBoardingKit.framework/OnBoardingKit
   - /System/Library/PrivateFrameworks/Preferences.framework/Preferences
   - /System/Library/PrivateFrameworks/SOS.framework/SOS
+  - /System/Library/PrivateFrameworks/SiriAnalytics.framework/SiriAnalytics
   - /System/Library/PrivateFrameworks/UIFoundation.framework/UIFoundation
   - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftWebKit.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2199
-  Symbols:   261
-  CStrings:  985
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 2202
+  Symbols:   277
+  CStrings:  995
 
Symbols:
+ _OBJC_CLASS_$_HKCategorySample
+ _OBJC_CLASS_$_HKMCPregnancyDatesFactory
+ _OBJC_CLASS_$_HKQuery
+ _OBJC_CLASS_$_HKQueryDescriptor
+ _OBJC_CLASS_$_HKSampleQuery
+ _OBJC_CLASS_$_HKSampleType
+ _OBJC_CLASS_$_NSSortDescriptor
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
+ _swift_getTupleTypeMetadata3
CStrings:
+ "[%!{(MISSING)public}s] Past pregnancy physiological washout date has either not passed or is over 90 days ago. Not showing Review Health Checklist tile."
+ "[%!{(MISSING)public}s] Past pregnancy physiological washout date was nil. Not showing review Health Checklist tile"
+ "[%!{(MISSING)public}s] Review Health Checklist tile has been viewed since past pregnancy physiological washout date. Not re-surfacing tile."
+ "[%!{(MISSING)public}s] Samples were nil. No need to provide a date."
+ "[%!{(MISSING)public}s] Showing Health Checklist Update Tile since physiological washout has ended"
+ "[MedicalID] presentation context controller nil"
+ "calculatePhysiologicalWashoutFromPregnancySample:"
+ "endDate"
+ "feedItemRelevanceInDays"
+ "initWithSampleType:predicate:"
+ "predicateForSamplesWithStartDate:endDate:options:"
+ "pregnancyType"
+ "showSensitiveLogItems"
+ "sortDescriptorsForMostRecentSamples"
- "Found cached Medical ID for MedicalIDViewController"
- "No Medical ID found for MedicalIDViewController"
- "setIsEditingAvailable:"
- "setIsSecondaryProfileMedicalID:"

```
