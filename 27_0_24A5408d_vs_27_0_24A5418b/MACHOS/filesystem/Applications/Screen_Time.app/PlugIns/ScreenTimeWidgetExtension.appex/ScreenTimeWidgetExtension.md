## ScreenTimeWidgetExtension

> `/Applications/Screen Time.app/PlugIns/ScreenTimeWidgetExtension.appex/ScreenTimeWidgetExtension`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_entry`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA.__objc_const`
- `__DATA.__objc_data`

```diff

-655.0.101.0.0
-  __TEXT.__text: 0x41704
-  __TEXT.__auth_stubs: 0x1e60
-  __TEXT.__objc_stubs: 0xc40
+655.0.106.0.0
+  __TEXT.__text: 0x4a1f8
+  __TEXT.__auth_stubs: 0x1fe0
+  __TEXT.__objc_stubs: 0xe00
   __TEXT.__objc_methlist: 0x338
-  __TEXT.__const: 0x20c8
-  __TEXT.__constg_swiftt: 0xbec
-  __TEXT.__swift5_typeref: 0x3cb8
+  __TEXT.__const: 0x2198
+  __TEXT.__constg_swiftt: 0xbfc
+  __TEXT.__swift5_typeref: 0x3d4e
   __TEXT.__swift5_builtin: 0x3c
   __TEXT.__swift5_reflstr: 0x5e4
   __TEXT.__swift5_fieldmd: 0x7d4
   __TEXT.__swift5_assocty: 0x218
   __TEXT.__swift5_proto: 0x9c
   __TEXT.__swift5_types: 0xa4
-  __TEXT.__objc_methtype: 0x35a
+  __TEXT.__objc_methtype: 0x39a
   __TEXT.__swift5_protos: 0x10
-  __TEXT.__swift_as_entry: 0x24
-  __TEXT.__swift_as_ret: 0x30
-  __TEXT.__swift_as_cont: 0x40
-  __TEXT.__swift5_capture: 0x428
-  __TEXT.__cstring: 0x4d3
+  __TEXT.__swift_as_entry: 0x4c
+  __TEXT.__swift_as_ret: 0x6c
+  __TEXT.__swift_as_cont: 0xa4
+  __TEXT.__swift5_capture: 0x478
+  __TEXT.__cstring: 0x4c3
   __TEXT.__objc_classname: 0x227
-  __TEXT.__objc_methname: 0xd35
-  __TEXT.__oslogstring: 0xf25
+  __TEXT.__objc_methname: 0xe15
+  __TEXT.__oslogstring: 0x11d5
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0xa08
-  __TEXT.__eh_frame: 0x928
-  __DATA_CONST.__const: 0x1438
+  __TEXT.__unwind_info: 0xb70
+  __TEXT.__eh_frame: 0x1058
+  __DATA_CONST.__const: 0x1550
   __DATA_CONST.__cfstring: 0x20
   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__auth_got: 0xf38
-  __DATA_CONST.__got: 0x638
-  __DATA_CONST.__auth_ptr: 0x5f8
+  __DATA_CONST.__auth_got: 0xff8
+  __DATA_CONST.__got: 0x6a0
+  __DATA_CONST.__auth_ptr: 0x600
   __DATA.__objc_const: 0xdc8
-  __DATA.__objc_selrefs: 0x448
+  __DATA.__objc_selrefs: 0x4b8
   __DATA.__objc_data: 0x478
-  __DATA.__data: 0x1970
+  __DATA.__data: 0x19b0
   __DATA.__bss: 0x1170
   __DATA.__common: 0x18
+  - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/Charts.framework/Charts
   - /System/Library/Frameworks/CoreData.framework/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/Frameworks/WidgetKit.framework/WidgetKit
   - /System/Library/PrivateFrameworks/Categories.framework/Categories
-  - /System/Library/PrivateFrameworks/FeatureFlags.framework/FeatureFlags
+  - /System/Library/PrivateFrameworks/FamilyCircle.framework/FamilyCircle
   - /System/Library/PrivateFrameworks/ScreenTimeCore.framework/ScreenTimeCore
+  - /System/Library/PrivateFrameworks/ScreenTimeSettingsServices.framework/ScreenTimeSettingsServices
   - /System/Library/PrivateFrameworks/ScreenTimeUI.framework/ScreenTimeUI
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 912
-  Symbols:   231
-  CStrings:  300
+  Functions: 978
+  Symbols:   237
+  CStrings:  328
 
Symbols:
+ _OBJC_CLASS_$_ACAccountStore
+ _OBJC_CLASS_$_FAFetchFamilyCircleRequest
+ _STShouldHideBundleIdentifierFromUI
+ _objc_release_x9
+ _swift_continuation_throwingResume
+ _swift_continuation_throwingResumeWithError
+ _swift_setDeallocating
- _swift_allocBox
CStrings:
+ "Current user is migrated to new Screen Time, always using Device Activity."
+ "Failed to create ScreenTimeSettings for remote user: %{public}@"
+ "Failed to fetch ScreenTimeSettings for family member: %{public}@"
+ "Failed to fetch family"
+ "Failed to fetch family member DSID or altDSID"
+ "Failed to fetch family: %{public}@"
+ "Failed to fetch local user"
+ "Failed to find family member with dsid: %{private}s"
+ "Failed to initialize ScreenTimeSettings for current user: %{public}@"
+ "Failed to load ScreenTimeSettings for me: %{public}@"
+ "Family member missing altDSID."
+ "No local user found."
+ "No local user settings provided. Returning nil user."
+ "aa_altDSID"
+ "aa_firstName"
+ "aa_lastName"
+ "aa_personID"
+ "aa_primaryAppleAccount"
+ "aa_primaryAppleAccountWithCompletion:"
+ "aa_primaryEmail"
+ "defaultStore"
+ "firstName"
+ "isGuardian"
+ "lastName"
+ "longLongValue"
+ "me"
+ "startRequestWithCompletionHandler:"
+ "v24@?0@\"ACAccount\"8@\"NSError\"16"
+ "v24@?0@\"FAFamilyCircle\"8@\"NSError\"16"
- "couldn't fetch local user"
```
