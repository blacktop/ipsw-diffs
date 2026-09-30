## FindMyWidgetItems

> `/System/Applications/FindMy.app/Contents/PlugIns/FindMyWidgetItems.appex/Contents/MacOS/FindMyWidgetItems`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_entry`
- `__DATA_CONST.__objc_classlist`
- `__DATA.__objc_const`
- `__DATA.__objc_data`

```diff

-470.20.6.14.30
-  __TEXT.__text: 0x317ac
-  __TEXT.__auth_stubs: 0x2510
-  __TEXT.__objc_stubs: 0x260
-  __TEXT.__const: 0x25a4
-  __TEXT.__constg_swiftt: 0xbf4
-  __TEXT.__swift5_typeref: 0x2992
-  __TEXT.__swift5_builtin: 0x50
-  __TEXT.__swift5_reflstr: 0x8b7
-  __TEXT.__swift5_fieldmd: 0xa18
-  __TEXT.__swift5_assocty: 0x330
-  __TEXT.__swift5_proto: 0xfc
-  __TEXT.__swift5_types: 0xdc
+470.21.6.16.27
+  __TEXT.__text: 0x267c8
+  __TEXT.__auth_stubs: 0x1d90
+  __TEXT.__objc_stubs: 0xa0
+  __TEXT.__cstring: 0x870
+  __TEXT.__const: 0x1ec4
+  __TEXT.__constg_swiftt: 0xb1c
+  __TEXT.__swift5_typeref: 0x26a0
+  __TEXT.__swift5_reflstr: 0x7d7
+  __TEXT.__swift5_fieldmd: 0x938
+  __TEXT.__swift5_builtin: 0x3c
+  __TEXT.__swift5_proto: 0xa4
+  __TEXT.__swift5_types: 0xc8
   __TEXT.__objc_classname: 0xb1
-  __TEXT.__objc_methname: 0x16c
-  __TEXT.__oslogstring: 0x34e
-  __TEXT.__swift_as_entry: 0x80
-  __TEXT.__swift_as_ret: 0x84
-  __TEXT.__swift_as_cont: 0x8c
-  __TEXT.__cstring: 0x990
-  __TEXT.__objc_methtype: 0x75
-  __TEXT.__swift5_capture: 0x1e0
+  __TEXT.__objc_methname: 0x70
+  __TEXT.__objc_methtype: 0x30
+  __TEXT.__oslogstring: 0x24e
+  __TEXT.__swift_as_entry: 0x38
+  __TEXT.__swift_as_ret: 0x3c
+  __TEXT.__swift_as_cont: 0x44
+  __TEXT.__swift5_assocty: 0x248
+  __TEXT.__swift5_capture: 0x17c
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0xe30
-  __TEXT.__eh_frame: 0xe1c
-  __DATA_CONST.__const: 0x1038
+  __TEXT.__unwind_info: 0xae8
+  __TEXT.__eh_frame: 0x7c4
+  __DATA_CONST.__const: 0xee8
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0x1290
-  __DATA_CONST.__got: 0x618
-  __DATA_CONST.__auth_ptr: 0xb38
+  __DATA_CONST.__auth_got: 0xed0
+  __DATA_CONST.__got: 0x478
+  __DATA_CONST.__auth_ptr: 0x810
   __DATA.__objc_const: 0x1d0
-  __DATA.__objc_selrefs: 0x98
+  __DATA.__objc_selrefs: 0x28
   __DATA.__objc_data: 0xa0
-  __DATA.__data: 0x1d88
-  __DATA.__common: 0x120
+  __DATA.__data: 0x1858
+  __DATA.__common: 0xf0
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/AppIntents.framework/Versions/A/AppIntents
   - /System/Library/Frameworks/CoreGraphics.framework/Versions/A/CoreGraphics

   - /System/Library/PrivateFrameworks/FindMyBase.framework/Versions/A/FindMyBase
   - /System/Library/PrivateFrameworks/FindMyCore.framework/Versions/A/FindMyCore
   - /System/Library/PrivateFrameworks/FindMyFeatureFlags.framework/Versions/A/FindMyFeatureFlags
-  - /System/Library/PrivateFrameworks/SPOwner.framework/Versions/A/SPOwner
   - /System/iOSSupport/System/Library/Frameworks/SwiftUI.framework/Versions/A/SwiftUI
   - /System/iOSSupport/System/Library/Frameworks/UIKit.framework/Versions/A/UIKit
   - /System/iOSSupport/System/Library/Frameworks/WidgetKit.framework/Versions/A/WidgetKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 952
-  Symbols:   183
-  CStrings:  121
+  Functions: 769
+  Symbols:   169
+  CStrings:  88
 
Symbols:
+ __swiftEmptySetSingleton
+ _objc_release_x25
+ _objc_retain_x26
+ _objc_retain_x27
+ _swift_setDeallocating
- _OBJC_CLASS_$_NSError
- _OBJC_CLASS_$_SPApplicationBeacon
- _OBJC_CLASS_$_SPOwnerSession
- _OBJC_CLASS_$_SPSimpleBeaconContext
- _SPBeaconTypeAccessory
- _SPBeaconTypeDurian
- __Block_copy
- __Block_release
- _bzero
- _objc_release
- _objc_release_x28
- _objc_retain_x23
- _swift_arrayInitWithCopy
- _swift_arrayInitWithTakeBackToFront
- _swift_arrayInitWithTakeFrontToBack
- _swift_release_x12
- _swift_retain_x2
- _swift_retain_x20
- _swift_unknownObjectRelease
CStrings:
- "%s"
- "%s - appBeacons.count: %{public}ld"
- "%s - compactMap %s"
- "%s - did receive fetchWithOptions: %s"
- "%s - error: %{public}@"
- "%s - ids: %{public}s"
- "%s - result: %s"
- "%s - will call fetchWithOptions: %s"
- "Fatal error"
- "FindMyWidgetItems/WidgetItemEntity.swift"
- "ITEM_ENTITY_TITLE"
- "WidgetItemEntityQuery"
- "batteryLevel"
- "com.apple.findmy"
- "com.findmy.itementity"
- "connected"
- "customDefaultResult()"
- "destination"
- "fetchModels(options:)"
- "fmipItemContext"
- "fmipItemContextForBeaconUUIDs:"
- "identifier"
- "initWithDomain:code:userInfo:"
- "isAppleAudioAccessory"
- "name"
- "owner"
- "privateApplicationBeacons(context:)"
- "role"
- "roleEmoji"
- "startUpdatingApplicationBeaconsWithContext:collectionDifference:completion:"
- "type"
- "v20@?0B8@\"NSError\"12"
- "v24@?0@\"NSOrderedCollectionDifference\"8@\"NSError\"16"
```
