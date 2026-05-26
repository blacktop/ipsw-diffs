## UserNotificationsCore

> `/System/Library/PrivateFrameworks/UserNotificationsCore.framework/UserNotificationsCore`

```diff

-640.5.32.104.0
-  __TEXT.__text: 0x206b80
+640.6.3.0.0
+  __TEXT.__text: 0x207c54
   __TEXT.__auth_stubs: 0x3b50
-  __TEXT.__objc_methlist: 0x7ba4
-  __TEXT.__cstring: 0xa2e3
-  __TEXT.__const: 0x10748
+  __TEXT.__objc_methlist: 0x7bb4
+  __TEXT.__cstring: 0xa343
+  __TEXT.__const: 0x10788
   __TEXT.__gcc_except_tab: 0x710
-  __TEXT.__oslogstring: 0x10507
+  __TEXT.__oslogstring: 0x106f7
   __TEXT.__dlopen_cstrs: 0xf4
-  __TEXT.__constg_swiftt: 0x6984
+  __TEXT.__constg_swiftt: 0x69a4
   __TEXT.__swift5_typeref: 0x6298
-  __TEXT.__swift5_reflstr: 0x3b33
-  __TEXT.__swift5_fieldmd: 0x45b4
+  __TEXT.__swift5_reflstr: 0x3b43
+  __TEXT.__swift5_fieldmd: 0x45c0
   __TEXT.__swift5_builtin: 0x190
   __TEXT.__swift5_assocty: 0x4e0
   __TEXT.__swift5_protos: 0x128

   __TEXT.__swift5_capture: 0x19a0
   __TEXT.__swift_as_ret: 0x1ec
   __TEXT.__swift5_mpenum: 0x48
-  __TEXT.__unwind_info: 0x5fd0
+  __TEXT.__unwind_info: 0x5fe8
   __TEXT.__eh_frame: 0x7910
   __TEXT.__objc_classname: 0x3796
-  __TEXT.__objc_methname: 0x19295
+  __TEXT.__objc_methname: 0x192b5
   __TEXT.__objc_methtype: 0x39ff
-  __TEXT.__objc_stubs: 0xfb80
+  __TEXT.__objc_stubs: 0xfbc0
   __DATA_CONST.__got: 0x1600
   __DATA_CONST.__const: 0x1598
   __DATA_CONST.__objc_classlist: 0x6b8
   __DATA_CONST.__objc_catlist: 0x80
   __DATA_CONST.__objc_protolist: 0x2f0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x49a8
+  __DATA_CONST.__objc_selrefs: 0x49b8
   __DATA_CONST.__objc_protorefs: 0x178
   __DATA_CONST.__objc_superrefs: 0x200
   __AUTH_CONST.__auth_got: 0x1db8
-  __AUTH_CONST.__const: 0xb340
-  __AUTH_CONST.__cfstring: 0x64e0
-  __AUTH_CONST.__objc_const: 0x24990
+  __AUTH_CONST.__const: 0xb360
+  __AUTH_CONST.__cfstring: 0x6520
+  __AUTH_CONST.__objc_const: 0x249b0
   __AUTH_CONST.__objc_intobj: 0x108
   __AUTH.__objc_data: 0x1120
   __AUTH.__data: 0x2e28
   __DATA.__objc_ivar: 0x880
-  __DATA.__data: 0x3de8
-  __DATA.__bss: 0xe5b0
+  __DATA.__data: 0x3df8
+  __DATA.__bss: 0xe5c0
   __DATA.__common: 0x128
   __DATA_DIRTY.__objc_data: 0x2bd0
-  __DATA_DIRTY.__data: 0x6090
+  __DATA_DIRTY.__data: 0x60b0
   __DATA_DIRTY.__bss: 0x5580
   __DATA_DIRTY.__common: 0x380
   - /System/Library/Frameworks/AccessoryLiveActivities.framework/AccessoryLiveActivities

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 27058F3E-3A18-37BC-B618-004F5E29FE88
-  Functions: 9153
-  Symbols:   13311
-  CStrings:  7403
+  UUID: 3505074C-FB55-3F04-A81B-F93DCCA3E6DE
+  Functions: 9158
+  Symbols:   13334
+  CStrings:  7417
 
Symbols:
+ -[UNCRemoteNotificationServer _queue_bundleIdentifierIsExemptFromTokenValidation:].cold.1
+ -[UNCRemoteNotificationServer _queue_connection:messageHasValidTokenForDelivery:]
+ -[UNCRemoteNotificationServer _queue_connection:messageHasValidTokenForDelivery:].cold.1
+ -[UNCRemoteNotificationServer queue]
+ _OUTLINED_FUNCTION_7
+ __PROTOCOLS__TtC21UserNotificationsCore35NotificationSourceMonitorLSObserver.44
+ ____tokenValidationExemptBundleIdentifiers_block_invoke
+ __tokenValidationExemptBundleIdentifiers.exemptBundleIdentifiers
+ __tokenValidationExemptBundleIdentifiers.onceToken
+ _objc_msgSend$_queue_connection:messageHasValidTokenForDelivery:
+ _objc_msgSend$initWithObjects:
+ _objc_msgSend$publicToken
- -[UNCRemoteNotificationServer _queue_topicIsExemptFromTokenValidation:]
- __PROTOCOLS__TtC21UserNotificationsCore35NotificationSourceMonitorLSObserver.41
- _objc_msgSend$_queue_topicIsExemptFromTokenValidation:
CStrings:
+ "Error removing replicated source %{private}s from store: %{public}@"
+ "Got %ld source updates"
+ "Received remote notification on topic %{public}@ for system token, allowing for bundleIdentifier %{public}@."
+ "Removing replicated source for uninstalled app: %{private}s"
+ "Replicated source removed: %{private}s. Clearing cache and settings."
+ "Resolved %{public}ld sources from %{public}ld identifiers"
+ "SettingsCenterListener delegate is nil, dropping source updates"
+ "_queue_connection:messageHasValidTokenForDelivery:"
+ "com.apple.private.untool.group-override"
+ "com.apple.private.untool.intelligence-override"
+ "initWithObjects:"
+ "listen() called but store is nil"
+ "listen() started, awaiting entry updates"
+ "populateWithSources called with %{public}ld sources"
+ "publicToken"
- "Got %ld source updates."
- "Received remote notification on topic %{public}@ for unknown token, allowing exempt CloudKit topic for bundleIdentifier %{public}@."
- "_queue_topicIsExemptFromTokenValidation:"

```
