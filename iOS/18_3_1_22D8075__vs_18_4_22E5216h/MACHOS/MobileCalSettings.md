## MobileCalSettings

> `/System/Library/PreferenceBundles/MobileCalSettings.bundle/MobileCalSettings`

```diff

-2970.4.1.0.0
-  __TEXT.__text: 0xe1f8
-  __TEXT.__auth_stubs: 0x850
-  __TEXT.__objc_stubs: 0x26a0
-  __TEXT.__objc_methlist: 0xa78
-  __TEXT.__objc_methname: 0x38d4
-  __TEXT.__objc_classname: 0x32e
-  __TEXT.__objc_methtype: 0xccc
-  __TEXT.__const: 0x3ce
-  __TEXT.__cstring: 0x1615
-  __TEXT.__oslogstring: 0x274
+2970.5.8.0.0
+  __TEXT.__text: 0xe5e8
+  __TEXT.__auth_stubs: 0x840
+  __TEXT.__objc_stubs: 0x27e0
+  __TEXT.__objc_methlist: 0x104c
+  __TEXT.__objc_methname: 0x3a68
+  __TEXT.__objc_classname: 0x348
+  __TEXT.__objc_methtype: 0xd1c
+  __TEXT.__const: 0x3ee
+  __TEXT.__cstring: 0x1455
+  __TEXT.__oslogstring: 0x2f9
   __TEXT.__constg_swiftt: 0x9c
   __TEXT.__swift5_typeref: 0x151
   __TEXT.__swift5_fieldmd: 0x48

   __TEXT.__swift5_assocty: 0x60
   __TEXT.__swift5_proto: 0x30
   __TEXT.__swift5_types: 0xc
-  __TEXT.__unwind_info: 0x390
-  __DATA_CONST.__auth_got: 0x430
-  __DATA_CONST.__got: 0x3a0
+  __TEXT.__unwind_info: 0x3b8
+  __DATA_CONST.__auth_got: 0x428
+  __DATA_CONST.__got: 0x3f0
   __DATA_CONST.__auth_ptr: 0x100
-  __DATA_CONST.__const: 0x568
-  __DATA_CONST.__cfstring: 0x12e0
+  __DATA_CONST.__const: 0x5c8
+  __DATA_CONST.__cfstring: 0x10a0
   __DATA_CONST.__objc_classlist: 0xb8
-  __DATA_CONST.__objc_protolist: 0x40
+  __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0xa0
   __DATA_CONST.__objc_intobj: 0x198
   __DATA_CONST.__objc_arraydata: 0x90
   __DATA_CONST.__objc_arrayobj: 0x48
-  __DATA.__objc_const: 0x25f8
-  __DATA.__objc_selrefs: 0xc70
-  __DATA.__objc_ivar: 0x120
+  __DATA.__objc_const: 0x1c60
+  __DATA.__objc_selrefs: 0xfd8
+  __DATA.__objc_ivar: 0x12c
   __DATA.__objc_data: 0x790
-  __DATA.__data: 0x410
+  __DATA.__data: 0x470
   __DATA.__bss: 0x610
   __DATA.__common: 0x8
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/SwiftUI.framework/SwiftUI
   - /System/Library/Frameworks/UIKit.framework/UIKit
+  - /System/Library/PrivateFrameworks/AppProtection.framework/AppProtection
+  - /System/Library/PrivateFrameworks/AppProtectionUI.framework/AppProtectionUI
   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
   - /System/Library/PrivateFrameworks/CalendarDatabase.framework/CalendarDatabase
   - /System/Library/PrivateFrameworks/CalendarFoundation.framework/CalendarFoundation

   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftNaturalLanguage.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 284
-  Symbols:   339
-  CStrings:  897
+  Functions: 307
+  Symbols:   347
+  CStrings:  908
 
Symbols:
+ _OBJC_CLASS_$_APApplication
+ _OBJC_CLASS_$_APBaseShieldView
+ _OBJC_CLASS_$_APGuard
+ _UIApplicationDidBecomeActiveNotification
+ _UIApplicationDidEnterBackgroundNotification
+ _UIApplicationWillEnterForegroundNotification
+ _UIApplicationWillResignActiveNotification
+ __UIApplicationDeactivationReasonUserInfoKey
+ __UIApplicationDidRemoveDeactivationReasonNotification
+ __UIApplicationWillAddDeactivationReasonNotification
- __swift_FORCE_LOAD_$_swiftFileProvider
- _swift_bridgeObjectRelease_n
CStrings:
+ "\x0f\x01\x13\x11"
+ "@\"APApplication\""
+ "@\"APBaseShieldView\""
+ "@32@0:8@16Q24"
+ "APBaseShieldViewDelegate"
+ "Events 2 Weeks Back"
+ "Failed to authenticate for locked calendar settings. Error :%@"
+ "Failed to cancel authenticate for locked calendar settings. Error :%@"
+ "Month Sync Title"
+ "_applicationDidBecomeActive"
+ "_applicationDidEnterBackground"
+ "_applicationDidEnterForeground"
+ "_applicationDidRemoveDeactivationReasonNotification:"
+ "_applicationDidResignActive"
+ "_applicationWillAddDeactivationReasonNotification:"
+ "_authenticateIfRequired"
+ "_cancelAuthentication"
+ "_isActive"
+ "_localeSpecificLocalizedMonthSyncTitleWithBundle:months:"
+ "_restrictToShield"
+ "abortOngoingAuthWithCompletion:"
+ "applicationWithBundleIdentifier:"
+ "authenticateForSubject:completion:"
+ "bounds"
+ "calApplication"
+ "initWithApplication:"
+ "isLocked"
+ "longLongValue"
+ "setHidden:"
+ "setShieldStyle:"
+ "sharedGuard"
+ "shieldView"
+ "shieldViewUnlockButtonPressed:"
+ "v20@?0B8@\"NSError\"12"
+ "v24@0:8@\"APBaseShieldView\"16"
+ "viewDidLoad"
- "\x0f\x01\x12"
- "1 Month Sync Title"
- "1 Month Sync Title (iPad)"
- "1 Month Sync Title Override"
- "1 Month Sync Title Override (iPad)"
- "2 Weeks Sync Title (iPad)"
- "3 Month Sync Title"
- "3 Months Sync Title (iPad)"
- "6 Month Sync Title"
- "6 Months Sync Title (iPad)"
- "Events %ld Month Back"
- "Events %ld Weeks Back"
- "No Limit (iPad)"
- "One month sync override title"
- "One month sync override title (iPad)"
- "Should Override One Month Sync Title"
- "Should Override One Month Sync Title (iPad)"
- "Sync Specifier Name (iPad)"
- "Time Zone Override (iPad)"
- "_localeSpecificLocalizedOneMonthSyncTitleWithBundle:"
- "_localeSpecificLocalizedSixMonthsSyncTitleWithBundle:"
- "_localeSpecificLocalizedThreeMonthsSyncTitleWithBundle:"
- "_localizedOneMonthSyncTitleOverrideInBundle:"
- "false"
- "true"

```
