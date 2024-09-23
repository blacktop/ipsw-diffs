## MusicUI

> `/System/Library/PrivateFrameworks/MusicUI.framework/MusicUI`

```diff

-4024.200.11.0.0
-  __TEXT.__text: 0xce150c
-  __TEXT.__auth_stubs: 0x9e10
+4024.200.15.0.0
+  __TEXT.__text: 0xcf5b44
+  __TEXT.__auth_stubs: 0x9e60
   __TEXT.__objc_methlist: 0xfd0
-  __TEXT.__const: 0x45c74
+  __TEXT.__const: 0x46454
   __TEXT.__gcc_except_tab: 0x70
-  __TEXT.__cstring: 0xfc26
+  __TEXT.__cstring: 0xfdc6
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__constg_swiftt: 0x17f10
-  __TEXT.__swift5_typeref: 0x5e4fc
-  __TEXT.__swift5_builtin: 0x3d4
-  __TEXT.__swift5_reflstr: 0x15b5b
-  __TEXT.__swift5_fieldmd: 0x15174
-  __TEXT.__swift5_assocty: 0x5fd0
-  __TEXT.__swift5_proto: 0x3114
-  __TEXT.__swift5_types: 0x17bc
-  __TEXT.__oslogstring: 0x6ce7
-  __TEXT.__swift5_capture: 0x6a90
+  __TEXT.__constg_swiftt: 0x180ec
+  __TEXT.__swift5_typeref: 0x5ed4c
+  __TEXT.__swift5_builtin: 0x3e8
+  __TEXT.__swift5_reflstr: 0x15ddb
+  __TEXT.__swift5_fieldmd: 0x15398
+  __TEXT.__swift5_assocty: 0x6098
+  __TEXT.__swift5_proto: 0x316c
+  __TEXT.__swift5_types: 0x17ec
+  __TEXT.__oslogstring: 0x6e97
+  __TEXT.__swift5_capture: 0x6b38
   __TEXT.__swift5_protos: 0x180
   __TEXT.__swift5_mpenum: 0x148
-  __TEXT.__unwind_info: 0x1aa70
-  __TEXT.__eh_frame: 0x201cc
+  __TEXT.__unwind_info: 0x1a898
+  __TEXT.__eh_frame: 0x204c4
   __TEXT.__objc_classname: 0x488
-  __TEXT.__objc_methname: 0x5cb6
+  __TEXT.__objc_methname: 0x5cdc
   __TEXT.__objc_methtype: 0x1eda
   __TEXT.__objc_stubs: 0x140
-  __DATA_CONST.__got: 0x2c60
+  __DATA_CONST.__got: 0x2c78
   __DATA_CONST.__const: 0x3f0
-  __DATA_CONST.__objc_classlist: 0x500
+  __DATA_CONST.__objc_classlist: 0x510
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x338
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1848
+  __DATA_CONST.__objc_selrefs: 0x1850
   __DATA_CONST.__objc_protorefs: 0x1d8
-  __AUTH_CONST.__auth_got: 0x4f18
-  __AUTH_CONST.__auth_ptr: 0x8990
-  __AUTH_CONST.__const: 0x2b838
+  __AUTH_CONST.__auth_got: 0x4f40
+  __AUTH_CONST.__auth_ptr: 0x8038
+  __AUTH_CONST.__const: 0x2be28
   __AUTH_CONST.__cfstring: 0x20
-  __AUTH_CONST.__objc_const: 0x139a8
-  __AUTH.__objc_data: 0x21b0
-  __AUTH.__data: 0x9600
-  __DATA.__data: 0x15490
-  __DATA.__bss: 0x43030
-  __DATA.__common: 0x538
-  __DATA_DIRTY.__objc_data: 0x2158
-  __DATA_DIRTY.__data: 0x198f8
-  __DATA_DIRTY.__bss: 0x19d80
-  __DATA_DIRTY.__common: 0x338
+  __AUTH_CONST.__objc_const: 0x13bb8
+  __AUTH.__objc_data: 0x2198
+  __AUTH.__data: 0x94b0
+  __DATA.__data: 0x150d0
+  __DATA.__bss: 0x41c60
+  __DATA.__common: 0x510
+  __DATA_DIRTY.__objc_data: 0x2130
+  __DATA_DIRTY.__data: 0x1a3e0
+  __DATA_DIRTY.__bss: 0x1bc80
+  __DATA_DIRTY.__common: 0x378
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/AuthenticationServices.framework/AuthenticationServices
+  - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/ContactsUI.framework/ContactsUI

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 40177
-  Symbols:   10009
-  CStrings:  3671
+  Functions: 40529
+  Symbols:   10055
+  CStrings:  3694
 
Symbols:
+ _CKAccountChangedNotification
+ _OBJC_CLASS_$_CKContainer
+ _CGRectInset
CStrings:
+ "%!s(MISSING) could not get account status: %!{(MISSING)public}s"
+ "💬 ┃┃ %!s(MISSING) isPerformingDeepLink = %!{(MISSING)bool}d, so skip pulling for appLaunchSheet."
+ "video"
+ "_TtCO7MusicUI15UnifiedMessages9DataStore"
+ "_delegateActionHandler"
+ "accountStatusWithCompletionHandler:"
+ "v24@?0q8@\"NSError\"16"
+ "handleAccountDidChange(_:)"
+ "supportsMusicShareSheet"
+ "fetchCloudKitAccountStatus()"
+ "💬 ┃┃ lastNLSQueryDate UserDefaults: %!{(MISSING)public}f, NSUbiquitousKeyValueStore: %!{(MISSING)public}f"
+ "fullScreenCover"
+ "fetchAccountStatus()"
+ "💬 ⛔ No data store available. Skip performing natural language search query."
+ "💬 Active user changed, resetting %!s(MISSING)"
+ "dataStore"
+ "performAppLaunchRequestIfNeeded()"
+ "cloudAccountStatusController"
+ "_TtC7MusicUI28CloudAccountStatusController"
+ "defaultContainer"
+ "%!s(MISSING) %!s(MISSING)"
+ "presentationStyle"
+ "sheet"
+ "accountStatus"
+ "💬 %!s(MISSING) storing lastNLSQueryDate in NSUbiquitousKeyValueStore: %!{(MISSING)public}ld"
+ "iCloud account status: %!{(MISSING)public}ld"
+ "💬 ⛔ No data store available. Skip setting mliState."
- "observeMLIStateChange()"
- "lightGrayColor"
- "💬 %!{(MISSING)public}s: Could not set MLI State as completed"
- "isPerformingDeepLink"
- "💬 ┃ lastNLSQueryDate UserDefaults: %!{(MISSING)public}f, NSUbiquitousKeyValueStore: %!{(MISSING)public}f"

```
