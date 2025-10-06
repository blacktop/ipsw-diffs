## remindd

> `/usr/libexec/remindd`

```diff

-981.0.0.0.0
-  __TEXT.__text: 0x7417ac
+1004.0.0.0.0
+  __TEXT.__text: 0x743ac8
   __TEXT.__auth_stubs: 0x5510
   __TEXT.__objc_stubs: 0xf960
   __TEXT.__objc_methlist: 0x8610
   __TEXT.__const: 0x1fad4
-  __TEXT.__objc_methname: 0x20f9a
+  __TEXT.__objc_methname: 0x2103c
   __TEXT.__objc_classname: 0x148e
   __TEXT.__objc_methtype: 0x3638
   __TEXT.__gcc_except_tab: 0x1aa4
-  __TEXT.__cstring: 0x5a890
+  __TEXT.__cstring: 0x5a7f0
   __TEXT.__oslogstring: 0x1a5a2
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__swift5_typeref: 0x12b7b
+  __TEXT.__swift5_typeref: 0x12b91
   __TEXT.__swift5_fieldmd: 0x98d4
   __TEXT.__constg_swiftt: 0xab98
   __TEXT.__swift5_builtin: 0x320
   __TEXT.__swift5_reflstr: 0xb7ed
   __TEXT.__swift5_assocty: 0x20f8
-  __TEXT.__swift5_capture: 0x5ba0
+  __TEXT.__swift5_capture: 0x5bf8
   __TEXT.__swift5_protos: 0x23c
   __TEXT.__swift5_proto: 0x16bc
   __TEXT.__swift5_types: 0x980
   __TEXT.__swift5_mpenum: 0xac
-  __TEXT.__unwind_info: 0x12580
-  __TEXT.__eh_frame: 0x1e600
+  __TEXT.__unwind_info: 0x126a0
+  __TEXT.__eh_frame: 0x1e6e0
   __DATA_CONST.__auth_got: 0x2a98
   __DATA_CONST.__got: 0x17f8
   __DATA_CONST.__auth_ptr: 0x990
-  __DATA_CONST.__const: 0x222b0
+  __DATA_CONST.__const: 0x223b8
   __DATA_CONST.__cfstring: 0x4c40
   __DATA_CONST.__objc_classlist: 0xa60
   __DATA_CONST.__objc_catlist: 0x168

   __DATA_CONST.__objc_dictobj: 0x140
   __DATA_CONST.__objc_doubleobj: 0x20
   __DATA.__objc_const: 0x1ce00
-  __DATA.__objc_selrefs: 0x7398
+  __DATA.__objc_selrefs: 0x73b8
   __DATA.__objc_protorefs: 0x218
-  __DATA.__objc_classrefs: 0xdb0
+  __DATA.__objc_classrefs: 0xdc0
   __DATA.__objc_superrefs: 0x138
   __DATA.__objc_ivar: 0x42c
   __DATA.__objc_data: 0x74f0
-  __DATA.__data: 0x23d60
+  __DATA.__data: 0x23d90
   __DATA.__objc_stublist: 0x28
   __DATA.__bss: 0x21c30
   __DATA.__common: 0x8f0

   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /System/Library/PrivateFrameworks/TCC.framework/TCC
   - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
+  - /System/Library/PrivateFrameworks/UnifiedAssetFramework.framework/UnifiedAssetFramework
   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
   - /System/Library/PrivateFrameworks/iCalendar.framework/iCalendar
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 1247FD3E-95EC-35F7-86F3-727A14628824
-  Functions: 26754
-  Symbols:   2804
-  CStrings:  12152
+  UUID: B3A3203F-E73D-3B94-9339-3C10AA4D3552
+  Functions: 26765
+  Symbols:   2806
+  CStrings:  12157
 
Symbols:
+ _$s19ReminderKitInternal16RDIDispatchQueueC07utilityE0So17OS_dispatch_queueCvau
+ _OBJC_CLASS_$_UAFAssetSetManager
+ _OBJC_CLASS_$_UAFAssetSetSubscription
- _$sSD4KeysV11descriptionSSvg
CStrings:
+ "com.apple.reminders.grocery"
+ "com.apple.siri.understanding"
+ "initWithName:assetSets:usageAliases:expires:"
+ "subscribe:subscriptions:queue:completion:"
+ "subscribeSiriAssets: Cannot load modelInfo for %{public}s: %@"
+ "subscribeSiriAssets: Failed to UAFAssetSetManager.subscribe %{public}s with error: %@"
+ "subscribeSiriAssets: Failed to UAFAssetSetManager.unsubscribe %{public}s with error: %@"
+ "subscribeSiriAssets: siriEmeddngLocale is nil: %{public}s"
+ "subscribeSiriAssets: skip download for siriEmeddngLocale: %{public}s"
+ "subscriptionsForSubscriber:"
+ "unsubscribe:subscriptionNames:queue:completion:"
- "Fetched customSmartLists(for:in:) that contain duplicated smart lists {keys: %{public}s}"
- "Fetched topLevelListsAndGroups that contain duplicated lists {keys: %{public}s}"
- "os_transaction INIT {name: com.apple.remindd.RDGroceryOperationQueue.handleIncompleteOperationQueueItems}"
- "os_transaction INIT {name: com.apple.remindd.RDTemplateOperationQueue.handleIncompleteOperationQueueItems}"
- "os_transaction RELEASE {name: com.apple.remindd.RDGroceryOperationQueue.handleIncompleteOperationQueueItems}"
- "os_transaction RELEASE {name: com.apple.remindd.RDTemplateOperationQueue.handleIncompleteOperationQueueItems}"

```
