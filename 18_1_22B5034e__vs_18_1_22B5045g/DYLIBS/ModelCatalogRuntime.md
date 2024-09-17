## ModelCatalogRuntime

> `/System/Library/PrivateFrameworks/ModelCatalogRuntime.framework/ModelCatalogRuntime`

```diff

-153.513.100.0.0
-  __TEXT.__text: 0x286b4
-  __TEXT.__auth_stubs: 0x15c0
+153.521.1.0.0
+  __TEXT.__text: 0x21680
+  __TEXT.__auth_stubs: 0x1330
   __TEXT.__objc_methlist: 0x12c
-  __TEXT.__const: 0x630
-  __TEXT.__swift5_typeref: 0x6c6
-  __TEXT.__swift5_fieldmd: 0x1bc
-  __TEXT.__constg_swiftt: 0x474
-  __TEXT.__cstring: 0xe66
-  __TEXT.__swift5_builtin: 0x28
-  __TEXT.__swift5_reflstr: 0x190
-  __TEXT.__swift5_assocty: 0x68
-  __TEXT.__oslogstring: 0x1346
+  __TEXT.__const: 0x460
+  __TEXT.__swift5_typeref: 0x63a
+  __TEXT.__swift5_fieldmd: 0x190
+  __TEXT.__constg_swiftt: 0x3e4
+  __TEXT.__cstring: 0xc66
+  __TEXT.__oslogstring: 0xda6
+  __TEXT.__swift5_builtin: 0x14
+  __TEXT.__swift5_reflstr: 0x160
   __TEXT.__swift5_protos: 0x14
-  __TEXT.__swift5_proto: 0x34
-  __TEXT.__swift5_types: 0x34
-  __TEXT.__swift5_capture: 0x2c8
-  __TEXT.__unwind_info: 0x770
-  __TEXT.__eh_frame: 0xab8
+  __TEXT.__swift5_types: 0x2c
+  __TEXT.__swift5_capture: 0x2b8
+  __TEXT.__swift5_proto: 0x1c
+  __TEXT.__swift5_assocty: 0x38
+  __TEXT.__unwind_info: 0x660
+  __TEXT.__eh_frame: 0x930
   __TEXT.__objc_classname: 0x2d
-  __TEXT.__objc_methname: 0x7f0
+  __TEXT.__objc_methname: 0x668
   __TEXT.__objc_methtype: 0xe9
-  __DATA_CONST.__got: 0x310
+  __DATA_CONST.__got: 0x210
   __DATA_CONST.__const: 0x90
-  __DATA_CONST.__objc_classlist: 0x20
+  __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x220
+  __DATA_CONST.__objc_selrefs: 0x180
   __DATA_CONST.__objc_protorefs: 0x20
-  __AUTH_CONST.__auth_got: 0xae0
-  __AUTH_CONST.__auth_ptr: 0x390
-  __AUTH_CONST.__const: 0xae8
-  __AUTH_CONST.__objc_const: 0x6d8
+  __AUTH_CONST.__auth_got: 0x998
+  __AUTH_CONST.__auth_ptr: 0x2a0
+  __AUTH_CONST.__const: 0xa70
+  __AUTH_CONST.__objc_const: 0x648
   __AUTH.__objc_data: 0x1a0
   __AUTH.__data: 0x98
-  __DATA.__data: 0x3e8
-  __DATA.__bss: 0x500
+  __DATA.__data: 0x338
   __DATA.__common: 0x10
+  __DATA.__bss: 0x200
   __DATA_DIRTY.__objc_data: 0xd8
-  __DATA_DIRTY.__data: 0x488
-  __DATA_DIRTY.__common: 0x61
+  __DATA_DIRTY.__data: 0x378
+  __DATA_DIRTY.__common: 0x49
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 740
-  Symbols:   168
-  CStrings:  279
+  Functions: 620
+  Symbols:   160
+  CStrings:  227
 
Symbols:
- _objc_retain_x26
- _OBJC_CLASS_$_FLFollowUpItem
- _OBJC_CLASS_$_FLFollowUpAction
- _OBJC_CLASS_$_FLFollowUpController
- _swift_willThrowTypedImpl
- _FLUserInfoPropertyDontDisplayDate
- _OBJC_CLASS_$_NSUserDefaults
- _OBJC_CLASS_$_FLFollowUpNotification
CStrings:
- "setActions:"
- "setUserInfo:"
- "userDefaultsOutOfStorageStateOverrideKey set to NO, setting remainingSpaceRequired to: %!l(MISSING)lu"
- "Additional Space Required"
- "It has only been %!f(MISSING) seconds since we have last posted a CFU, which does not exceed the minimum interval of %!f(MISSING) seconds. Not posting CFU"
- "com.apple.modelcatalog.out-of-space-cfu"
- "postFollowUpItem:error:"
- "settings-navigation://com.apple.Settings.General/STORAGE_MGMT"
- "Received new availability: %!s(MISSING)"
- "Found subscription: %!s(MISSING) with out of space status - new remaining space required: %!l(MISSING)lu"
- "Could not initialize UserDefaults with suite name: %!s(MISSING)"
- "Posted new CFU with item: %!@(MISSING)"
- "setUniqueIdentifier:"
- "setDisplayStyle:"
- "setNotification:"
- "com.apple.modelcatalog.post-out-of-storage-cfu"
- "initWithClientIdentifier:"
- "com.apple.modelcatalog.corefollowup"
- " to download. Some features will be limited until enough space is available."
- "notification"
- "setValue:forKey:"
- "Will attempt to post out of storage CFU with remaining space required: %!l(MISSING)lu"
- "Manage iPhone Storage"
- "Checking if any of %!l(MISSING)d subscriptions are out of space"
- "Could not clear out of storage CFUs with error: %!@(MISSING)"
- "Device has enough space. Cleared any pending OOS CFUs"
- "pendingFollowUpItems:"
- "setActivateAction:"
- "initWithSuiteName:"
- "Persisted new last post date of %!s(MISSING) to user defaults"
- "_TtC19ModelCatalogRuntime15FollowUpManager"
- "setInformativeText:"
- "Running checkAndNotifyForOutOfStorageStatus..."
- "GMS Unavailable - Device is never capable of enabling GM, bailing early"
- "Starting to listen for changes to availability"
- "setTitle:"
- "OutOfStorageStateOverride"
- "GMS Unavailable - Device currently cannot enable GM due to ineligibility. Clearing and bailing early"
- "Unable to fetch asset size for subscription: %!s(MISSING) with error: %!@(MISSING)"
- "uniqueIdentifier"
- "setExpirationDate:"
- "Cleared any pending OOS CFUs"
- "clearPendingFollowUpItemsWithUniqueIdentifiers:error:"
- "userDefaultsOutOfStorageStateOverrideKey set to YES, setting remainingSpaceRequired to: %!l(MISSING)lu"
- "com.apple.modelcatalog"
- "objectForKey:"
- "GMS Unavailable for the following reasons: %!s(MISSING)"
- "valueForKeyPath:"
- "Apple Intelligence requires an additional "
- "actionWithLabel:url:"
- "Already have pending OOS CFU, skipping"
- "Could not post out of storage CFU with error: %!@(MISSING)"

```
