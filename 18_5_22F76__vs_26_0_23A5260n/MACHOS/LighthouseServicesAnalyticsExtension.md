## LighthouseServicesAnalyticsExtension

> `/System/Library/ExtensionKit/Extensions/LighthouseServicesAnalyticsExtension.appex/LighthouseServicesAnalyticsExtension`

```diff

-1.0.10.0.0
-  __TEXT.__text: 0x73a8
-  __TEXT.__auth_stubs: 0x860
-  __TEXT.__const: 0x3ea
-  __TEXT.__cstring: 0x3a5
-  __TEXT.__objc_methname: 0xa5
+1.0.15.0.0
+  __TEXT.__text: 0x8b14
+  __TEXT.__auth_stubs: 0x970
+  __TEXT.__const: 0x42a
+  __TEXT.__cstring: 0x3d1
+  __TEXT.__objc_methname: 0xe4
   __TEXT.__swift5_entry: 0x8
   __TEXT.__constg_swiftt: 0x84
-  __TEXT.__swift5_typeref: 0x1e3
-  __TEXT.__swift5_fieldmd: 0x10c
-  __TEXT.__swift5_reflstr: 0x1f1
+  __TEXT.__swift5_typeref: 0x205
+  __TEXT.__swift5_fieldmd: 0x1b4
+  __TEXT.__swift5_reflstr: 0x2ea
   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_capture: 0x24
-  __TEXT.__oslogstring: 0x197
+  __TEXT.__oslogstring: 0x419
   __TEXT.__swift5_proto: 0x3c
   __TEXT.__swift5_types: 0x10
-  __TEXT.__swift_as_entry: 0x10
-  __TEXT.__swift_as_ret: 0x10
-  __TEXT.__unwind_info: 0x1c0
-  __TEXT.__eh_frame: 0x248
-  __DATA_CONST.__auth_got: 0x430
-  __DATA_CONST.__got: 0x118
+  __TEXT.__swift_as_entry: 0x14
+  __TEXT.__swift_as_ret: 0x18
+  __TEXT.__unwind_info: 0x208
+  __TEXT.__eh_frame: 0x2c8
+  __DATA_CONST.__auth_got: 0x4b8
+  __DATA_CONST.__got: 0x158
   __DATA_CONST.__auth_ptr: 0x1d8
-  __DATA_CONST.__const: 0x470
+  __DATA_CONST.__const: 0x548
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_selrefs: 0x38
+  __DATA.__objc_selrefs: 0x58
   __DATA.__data: 0x128
-  __DATA.__bss: 0x7c0
+  __DATA.__bss: 0x7d0
   __DATA.__common: 0x18
   - /System/Library/Frameworks/Accounts.framework/Accounts
+  - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/TabularData.framework/TabularData
   - /System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/LighthouseBackground.framework/LighthouseBackground

   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
-  - /usr/lib/swift/libswiftCryptoTokenKit.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_errno.dylib
-  - /usr/lib/swift/libswift_math.dylib
-  - /usr/lib/swift/libswift_signal.dylib
-  - /usr/lib/swift/libswift_stdio.dylib
-  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 417AC3C7-1C53-393A-BC53-2956AEC0A3FD
-  Functions: 125
-  Symbols:   105
-  CStrings:  39
+  UUID: 74301C8E-A3E0-3E0C-8E2C-D2F4BEE4D905
+  Functions: 137
+  Symbols:   108
+  CStrings:  61
 
Symbols:
+ _OBJC_CLASS_$_NSUserDefaults
+ __swift_FORCE_LOAD_$_swiftCoreImage
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ _objc_release_x23
+ _objc_retain_x19
+ _objc_retain_x21
+ _objc_retain_x24
+ _objc_retain_x28
+ _objc_retain_x8
+ _swift_allocError
+ _swift_arrayDestroy
+ _swift_setDeallocating
- __swift_FORCE_LOAD_$_swiftCryptoTokenKit
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftunistd
- _objc_retain_x27
- _swift_bridgeObjectRelease_n
- _swift_bridgeObjectRetain_n
CStrings:
+ "\n %s"
+ "%s has already run, exiting early."
+ "Attempting to use both allowStorefronts and skipStorefronts, exiting early."
+ "Context in doWork: %@"
+ "Context in shouldRun: %@"
+ "Device's storefront %s is in the allow list."
+ "Device's storefront %s is not in the skip list."
+ "Encountered error when querying connection: %@. Exiting early."
+ "Execution state saved for task: %s"
+ "Failed to instantiate userDefaults with suiteName: %s, exiting early."
+ "No data was returned from the query, exiting early"
+ "Storefront %s is in the skip list, exiting early."
+ "Storefront %s is not in the allow list, exiting early."
+ "Unable to determine storefront, exiting early."
+ "allowStorefronts"
+ "ams_storefront"
+ "boolForKey:"
+ "com.apple.LighthouseServicesAnalytics"
+ "com.apple.lighthouse.LighthouseServicesAnalyticsExtension:MLHost:"
+ "failedToInstantiateUserDefaults"
+ "hasAlreadyRun"
+ "initWithSuiteName:"
+ "malformedQuery"
+ "noDataReturned"
+ "setBothAllowAndSkipListForStorefronts"
+ "setValue:forKey:"
+ "storefrontIsInSkipList"
+ "storefrontIsNotInAllowList"
+ "unableToDetermineStorefront"
+ "unexpectedErrorOccurred"
- "Context: %@"
- "Encountered error when querying connection. Exiting early."
- "SQL analyzer error: Table not found"
- "attempting to access columns which are not permitted in this access credential"
- "attempting to access tables which are not permitted in this access credential"
- "attemptingToAccessNonExistentTable"
- "com.apple.lighthouse.LighthouseServicesAnalyticsExtension:MLHost:1:"
- "unable to open database file"

```
