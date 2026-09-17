## RemindersWidgetExtension

> `/System/Applications/Reminders.app/Contents/PlugIns/RemindersWidgetExtension.appex/Contents/MacOS/RemindersWidgetExtension`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift5_entry`
- `__TEXT.__swift_as_cont`
- `__DATA.__objc_data`

```diff

-4046.21.0.0.0
-  __TEXT.__text: 0x7a908
-  __TEXT.__auth_stubs: 0x28a0
-  __TEXT.__objc_stubs: 0x6e0
-  __TEXT.__objc_classname: 0x1a8
-  __TEXT.__const: 0x3544
-  __TEXT.__swift5_typeref: 0x4868
-  __TEXT.__swift5_fieldmd: 0x1030
-  __TEXT.__constg_swiftt: 0x129c
-  __TEXT.__objc_methname: 0x4b1
+4076.0.0.0.0
+  __TEXT.__text: 0x81900
+  __TEXT.__auth_stubs: 0x2a60
+  __TEXT.__objc_stubs: 0x820
+  __TEXT.__objc_classname: 0x1e8
+  __TEXT.__const: 0x37d4
+  __TEXT.__swift5_typeref: 0x4922
+  __TEXT.__swift5_fieldmd: 0x10e0
+  __TEXT.__constg_swiftt: 0x137c
+  __TEXT.__objc_methname: 0x5ce
   __TEXT.__objc_methtype: 0x2c
-  __TEXT.__swift5_reflstr: 0xa1f
+  __TEXT.__swift5_reflstr: 0xa8f
   __TEXT.__swift5_builtin: 0x3c
-  __TEXT.__oslogstring: 0x1265
-  __TEXT.__swift5_capture: 0x4e8
-  __TEXT.__cstring: 0x7e8
+  __TEXT.__oslogstring: 0x15b5
+  __TEXT.__swift5_capture: 0x558
+  __TEXT.__cstring: 0x878
   __TEXT.__swift5_assocty: 0x5b8
-  __TEXT.__swift5_protos: 0x14
-  __TEXT.__swift5_proto: 0x164
-  __TEXT.__swift5_types: 0x140
+  __TEXT.__swift5_protos: 0x18
+  __TEXT.__swift5_proto: 0x188
+  __TEXT.__swift5_types: 0x150
   __TEXT.__swift_as_entry: 0x78
   __TEXT.__swift_as_ret: 0xa0
   __TEXT.__swift5_entry: 0x8
   __TEXT.__swift_as_cont: 0xe4
-  __TEXT.__unwind_info: 0x17a0
-  __TEXT.__eh_frame: 0x17c8
-  __DATA_CONST.__const: 0x1a40
-  __DATA_CONST.__objc_classlist: 0x30
+  __TEXT.__unwind_info: 0x1888
+  __TEXT.__eh_frame: 0x1848
+  __DATA_CONST.__const: 0x1b88
+  __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0x1458
-  __DATA_CONST.__got: 0x9f0
-  __DATA_CONST.__auth_ptr: 0xb38
-  __DATA.__objc_const: 0x528
-  __DATA.__objc_selrefs: 0x1b8
+  __DATA_CONST.__auth_got: 0x1538
+  __DATA_CONST.__got: 0xa20
+  __DATA_CONST.__auth_ptr: 0xbf0
+  __DATA.__objc_const: 0x600
+  __DATA.__objc_selrefs: 0x208
   __DATA.__objc_data: 0xf0
-  __DATA.__data: 0x2c18
-  __DATA.__common: 0x58
+  __DATA.__data: 0x2e00
+  __DATA.__common: 0x60
   - /System/Library/Frameworks/AppIntents.framework/Versions/A/AppIntents
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/Contacts.framework/Versions/A/Contacts
+  - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/Versions/A/CoreGraphics
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/NotificationCenter.framework/Versions/A/NotificationCenter

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1625
-  Symbols:   153
-  CStrings:  176
+  Functions: 1693
+  Symbols:   159
+  CStrings:  201
 
Symbols:
+ _OBJC_CLASS_$_NSUserDefaults
+ _OBJC_CLASS_$_REMAccount
+ _REMListBadgeEmblemDefault
+ __REMGetLocalizedString
+ _swift_allocError
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
