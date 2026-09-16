## RemindersWidgetExtension

> `/private/var/staged_system_apps/Reminders.app/PlugIns/RemindersWidgetExtension.appex/RemindersWidgetExtension`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_entry`
- `__DATA.__objc_data`

```diff

-4046.11.0.0.0
-  __TEXT.__text: 0xd05d8
-  __TEXT.__auth_stubs: 0x3d80
-  __TEXT.__objc_stubs: 0x840
-  __TEXT.__objc_classname: 0x1a8
-  __TEXT.__const: 0x9374
-  __TEXT.__constg_swiftt: 0x2400
-  __TEXT.__swift5_typeref: 0xc594
-  __TEXT.__cstring: 0x3a69
+4076.0.0.0.0
+  __TEXT.__text: 0xd749c
+  __TEXT.__auth_stubs: 0x3ef0
+  __TEXT.__objc_stubs: 0x980
+  __TEXT.__objc_classname: 0x1e8
+  __TEXT.__const: 0x9604
+  __TEXT.__constg_swiftt: 0x24e0
+  __TEXT.__swift5_typeref: 0xc64e
+  __TEXT.__cstring: 0x3af9
   __TEXT.__swift5_builtin: 0x3c
-  __TEXT.__swift5_reflstr: 0x123a
-  __TEXT.__swift5_fieldmd: 0x1a0c
+  __TEXT.__swift5_reflstr: 0x12aa
+  __TEXT.__swift5_fieldmd: 0x1abc
   __TEXT.__swift5_assocty: 0x1120
-  __TEXT.__swift5_capture: 0x61c
+  __TEXT.__swift5_capture: 0x68c
   __TEXT.__objc_methtype: 0x1d
-  __TEXT.__swift5_proto: 0x52c
-  __TEXT.__swift5_types: 0x264
+  __TEXT.__swift5_proto: 0x550
+  __TEXT.__swift5_types: 0x274
   __TEXT.__swift_as_entry: 0x208
   __TEXT.__swift_as_ret: 0x1d8
   __TEXT.__swift_as_cont: 0x1a8
-  __TEXT.__oslogstring: 0x14aa
+  __TEXT.__oslogstring: 0x17fa
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__objc_methname: 0x64a
-  __TEXT.__swift5_protos: 0x14
-  __TEXT.__unwind_info: 0x3028
-  __TEXT.__eh_frame: 0x2968
-  __DATA_CONST.__const: 0x2a90
-  __DATA_CONST.__objc_classlist: 0x30
+  __TEXT.__objc_methname: 0x757
+  __TEXT.__swift5_protos: 0x18
+  __TEXT.__unwind_info: 0x3110
+  __TEXT.__eh_frame: 0x29e8
+  __DATA_CONST.__const: 0x2bd8
+  __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0x1ec8
-  __DATA_CONST.__got: 0xe00
-  __DATA_CONST.__auth_ptr: 0x1190
-  __DATA.__objc_const: 0x528
-  __DATA.__objc_selrefs: 0x210
+  __DATA_CONST.__auth_got: 0x1f80
+  __DATA_CONST.__got: 0xe28
+  __DATA_CONST.__auth_ptr: 0x1228
+  __DATA.__objc_const: 0x600
+  __DATA.__objc_selrefs: 0x260
   __DATA.__objc_data: 0xf0
-  __DATA.__data: 0x5398
-  __DATA.__common: 0x368
+  __DATA.__data: 0x5580
+  __DATA.__common: 0x370
   - /System/Library/Frameworks/AlarmKit.framework/AlarmKit
   - /System/Library/Frameworks/AppIntents.framework/AppIntents
   - /System/Library/Frameworks/Contacts.framework/Contacts
+  - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/SwiftUI.framework/SwiftUI

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3373
-  Symbols:   235
-  CStrings:  398
+  Functions: 3437
+  Symbols:   239
+  CStrings:  423
 
Symbols:
+ _OBJC_CLASS_$_NSUserDefaults
+ _OBJC_CLASS_$_REMAccount
+ __REMGetLocalizedString
+ _swift_getMetatypeMetadata
CStrings:
+ "%{public}s: configuration names the local account's default list; following the user's default list instead {objectID: %{public}@}"
+ "%{public}s: could not decode record {objectID: %{public}@, error: %{public}s}"
+ "%{public}s: could not encode record {objectID: %{public}@, error: %{public}s}"
+ "%{public}s: dropping a record that could not be decoded {key: %{public}s, error: %{public}s}"
+ "%{public}s: list has been unfetchable past the grace period; using the default list {objectID: %{public}@, failingFor: %{public}f}"
+ "TTRNewWidgetInteractor looked for the list in deactivated accounts {objectID: %{public}s, exists: %{bool,public}d}"
+ "TTRNewWidgetInteractor: could not look for the list in deactivated accounts {objectID: %{public}s, error: %{public}s}"
+ "TTRWidgetListFetchState."
+ "TTRWidgetListFetchState.lastPrune"
+ "Widget presenter: %{public}s is in a deactivated account, so it cannot return; showing the default list {objectID: %{public}@}"
+ "Widget presenter: %{public}s is not expected to return; showing the default list {objectID: %{public}@}"
+ "Widget presenter: %{public}s unavailable but expected to return; showing placeholder instead of the default list {objectID: %{public}@}"
+ "Widget presenter: Could not fetch %{public}s {objectID: %{public}@ error: %{public}s}"
+ "Widget presenter: no list exists to show as the default; showing an empty list"
+ "_TtC24RemindersWidgetExtension28TTRWidgetListFetchStateStore"
+ "custom smart list"
+ "dataForKey:"
+ "dictionaryRepresentation"
+ "fetchAccountsIncludingInactive:error:"
+ "fetchListsWithError:"
+ "firstFailureOfCurrentRun"
+ "inactive"
+ "initWithSuiteName:"
+ "listFetchStateTracker"
+ "localAccountDefaultListID"
+ "objectForKey:"
+ "removeObjectForKey:"
+ "setObject:forKey:"
+ "userDefaults"
- "Widget presenter: Could not fetch custom smart list {customSmartListID: %{public}@ error: %{public}s}"
- "Widget presenter: Could not fetch list {listID: %{public}@ error: %{public}s}"
- "Widget presenter: custom smart list unavailable (likely transient); showing placeholder instead of the default list {customSmartListID: %{public}@}"
- "Widget presenter: list unavailable (likely transient — store loading or revalidating); showing placeholder instead of the default list {listID: %{public}@}"
```
