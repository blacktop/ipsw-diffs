## ScreenTimeWidgetIntentsExtension

> `/System/Library/CoreServices/Screen Time.app/Contents/PlugIns/ScreenTimeWidgetIntentsExtension.appex/Contents/MacOS/ScreenTimeWidgetIntentsExtension`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_builtin`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA.__objc_const`
- `__DATA.__objc_data`

```diff

-649.0.0.0.0
-  __TEXT.__text: 0x6158
-  __TEXT.__auth_stubs: 0x740
-  __TEXT.__objc_stubs: 0x4a0
+655.0.405.0.0
+  __TEXT.__text: 0xab00
+  __TEXT.__auth_stubs: 0xa10
+  __TEXT.__objc_stubs: 0x620
   __TEXT.__objc_methlist: 0x338
-  __TEXT.__const: 0x568
-  __TEXT.__swift5_typeref: 0x2fc
+  __TEXT.__const: 0x628
+  __TEXT.__swift5_typeref: 0x38e
   __TEXT.__swift5_fieldmd: 0x1cc
-  __TEXT.__constg_swiftt: 0x564
+  __TEXT.__constg_swiftt: 0x574
   __TEXT.__swift5_protos: 0x10
   __TEXT.__objc_classname: 0x267
-  __TEXT.__objc_methname: 0x8d5
-  __TEXT.__objc_methtype: 0x31a
-  __TEXT.__oslogstring: 0x314
+  __TEXT.__objc_methname: 0x965
+  __TEXT.__objc_methtype: 0x33a
+  __TEXT.__oslogstring: 0x424
   __TEXT.__cstring: 0x18a
-  __TEXT.__swift5_capture: 0x68
+  __TEXT.__swift5_capture: 0xc8
   __TEXT.__swift5_types: 0x30
+  __TEXT.__swift_as_entry: 0x1c
+  __TEXT.__swift_as_ret: 0x24
+  __TEXT.__swift_as_cont: 0x2c
   __TEXT.__swift5_reflstr: 0x12a
   __TEXT.__swift5_proto: 0x1c
   __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_builtin: 0x14
-  __TEXT.__unwind_info: 0x218
-  __DATA_CONST.__const: 0x350
+  __TEXT.__unwind_info: 0x318
+  __TEXT.__eh_frame: 0x418
+  __DATA_CONST.__const: 0x440
   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__auth_got: 0x3a8
-  __DATA_CONST.__got: 0xd8
-  __DATA_CONST.__auth_ptr: 0xd8
+  __DATA_CONST.__auth_got: 0x510
+  __DATA_CONST.__got: 0x138
+  __DATA_CONST.__auth_ptr: 0xf0
   __DATA.__objc_const: 0xdc8
-  __DATA.__objc_selrefs: 0x260
+  __DATA.__objc_selrefs: 0x2c0
   __DATA.__objc_data: 0x478
-  __DATA.__data: 0x778
+  __DATA.__data: 0x7b8
   __DATA.__common: 0x8
   __DATA.__bss: 0x180
+  - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/CoreData.framework/Versions/A/CoreData
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/Intents.framework/Versions/A/Intents
+  - /System/Library/PrivateFrameworks/FamilyCircle.framework/Versions/A/FamilyCircle
   - /System/Library/PrivateFrameworks/ScreenTimeCore.framework/Versions/A/ScreenTimeCore
+  - /System/Library/PrivateFrameworks/ScreenTimeSettingsServices.framework/Versions/A/ScreenTimeSettingsServices
   - /System/iOSSupport/System/Library/Frameworks/UIKit.framework/Versions/A/UIKit
   - /System/iOSSupport/System/Library/PrivateFrameworks/ScreenTimeUI.framework/Versions/A/ScreenTimeUI
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 172
-  Symbols:   151
-  CStrings:  165
+  Functions: 222
+  Symbols:   175
+  CStrings:  183
 
Symbols:
+ _OBJC_CLASS_$_ACAccountStore
+ _OBJC_CLASS_$_FAFetchFamilyCircleRequest
+ _objc_release_x9
+ _objc_retain_x25
+ _objc_retain_x26
+ _objc_retain_x27
+ _swift_allocError
+ _swift_bridgeObjectRetain_n
+ _swift_continuation_await
+ _swift_continuation_init
+ _swift_continuation_throwingResume
+ _swift_continuation_throwingResumeWithError
+ _swift_initStackObject
+ _swift_release_x24
+ _swift_release_x26
+ _swift_release_x27
+ _swift_release_x28
+ _swift_retain_x21
+ _swift_retain_x24
+ _swift_retain_x25
+ _swift_retain_x28
+ _swift_task_alloc
+ _swift_task_create
+ _swift_task_dealloc
+ _swift_task_switch
+ _swift_unknownObjectRelease
- _swift_endAccess
- _swift_retain_x22
CStrings:
+ "Failed to fetch ScreenTimeSettings for family member: %{public}@"
+ "Failed to fetch family"
+ "Failed to fetch family member DSID or altDSID"
+ "Failed to fetch local user"
+ "Failed to initialize ScreenTimeSettings for current user: %{public}@"
+ "No local user found."
+ "aa_firstName"
+ "aa_lastName"
+ "aa_personID"
+ "aa_primaryAppleAccount"
+ "altDSID"
+ "defaultStore"
+ "firstName"
+ "isGuardian"
+ "lastName"
+ "longLongValue"
+ "me"
+ "startRequestWithCompletionHandler:"
+ "v24@?0@\"FAFamilyCircle\"8@\"NSError\"16"
- "couldn't fetch local user"
```
