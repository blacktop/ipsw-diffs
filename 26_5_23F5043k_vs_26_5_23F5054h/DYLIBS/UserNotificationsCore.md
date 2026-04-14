## UserNotificationsCore

> `/System/Library/PrivateFrameworks/UserNotificationsCore.framework/UserNotificationsCore`

```diff

-640.5.22.102.0
-  __TEXT.__text: 0x1f3fb0
+640.5.27.0.0
+  __TEXT.__text: 0x1f5d24
   __TEXT.__auth_stubs: 0x3ac0
   __TEXT.__objc_methlist: 0x7b74
-  __TEXT.__cstring: 0xa663
-  __TEXT.__const: 0x10358
+  __TEXT.__cstring: 0xa6a3
+  __TEXT.__const: 0x10408
   __TEXT.__gcc_except_tab: 0x710
-  __TEXT.__oslogstring: 0xec07
+  __TEXT.__oslogstring: 0xedb7
   __TEXT.__dlopen_cstrs: 0xf4
-  __TEXT.__constg_swiftt: 0x68ac
-  __TEXT.__swift5_typeref: 0x616e
-  __TEXT.__swift5_reflstr: 0x3b13
-  __TEXT.__swift5_fieldmd: 0x456c
+  __TEXT.__constg_swiftt: 0x68d8
+  __TEXT.__swift5_typeref: 0x61b6
+  __TEXT.__swift5_reflstr: 0x3af3
+  __TEXT.__swift5_fieldmd: 0x4564
   __TEXT.__swift5_builtin: 0x154
   __TEXT.__swift5_assocty: 0x498
   __TEXT.__swift5_protos: 0x128
-  __TEXT.__swift5_proto: 0xb0c
+  __TEXT.__swift5_proto: 0xb20
   __TEXT.__swift5_types: 0x520
-  __TEXT.__swift_as_entry: 0x190
-  __TEXT.__swift5_capture: 0x18a4
-  __TEXT.__swift_as_ret: 0x1cc
+  __TEXT.__swift_as_entry: 0x194
+  __TEXT.__swift5_capture: 0x18b4
+  __TEXT.__swift_as_ret: 0x1d4
   __TEXT.__swift5_mpenum: 0x48
-  __TEXT.__unwind_info: 0x5e08
-  __TEXT.__eh_frame: 0x7280
+  __TEXT.__unwind_info: 0x5e70
+  __TEXT.__eh_frame: 0x7440
   __TEXT.__objc_classname: 0x3776
-  __TEXT.__objc_methname: 0x19245
+  __TEXT.__objc_methname: 0x19255
   __TEXT.__objc_methtype: 0x39ff
-  __TEXT.__objc_stubs: 0xfb60
-  __DATA_CONST.__got: 0x15c8
+  __TEXT.__objc_stubs: 0xfb80
+  __DATA_CONST.__got: 0x15e0
   __DATA_CONST.__const: 0x1598
   __DATA_CONST.__objc_classlist: 0x6b0
   __DATA_CONST.__objc_catlist: 0x80
   __DATA_CONST.__objc_protolist: 0x2f0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4998
+  __DATA_CONST.__objc_selrefs: 0x49a0
   __DATA_CONST.__objc_protorefs: 0x178
   __DATA_CONST.__objc_superrefs: 0x200
   __AUTH_CONST.__auth_got: 0x1d70
-  __AUTH_CONST.__const: 0xb058
+  __AUTH_CONST.__const: 0xb0f8
   __AUTH_CONST.__cfstring: 0x6540
   __AUTH_CONST.__objc_const: 0x24928
   __AUTH_CONST.__objc_intobj: 0x108
   __AUTH.__objc_data: 0x10b0
   __AUTH.__data: 0x2de8
   __DATA.__objc_ivar: 0x880
-  __DATA.__data: 0x3c98
-  __DATA.__bss: 0xdf40
+  __DATA.__data: 0x3cd0
+  __DATA.__bss: 0xe1c0
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
-  UUID: F13C801C-A851-32ED-B421-DAAF82E40C88
-  Functions: 9037
-  Symbols:   13273
-  CStrings:  7350
+  UUID: 31400AF6-B066-3BB9-A54E-996EC61871CB
+  Functions: 9053
+  Symbols:   13276
+  CStrings:  7358
 
Symbols:
+ _BPSNanoBulletinShowsCustomSettings
+ _SBUserNotificationAllowedApplicationsKey
+ _associated conformance 21UserNotificationsCore24SourceSelectionPresenterV0D13SelectorErrorOSHAASQ
+ _associated conformance 21UserNotificationsCore24SourceSelectionPresenterV0D22SelectorDismissalErrorOSHAASQ
+ _objc_msgSend$initWithArray:
+ _symbolic SDy__________G 22AccessoryNotifications0A8IdentityO AA0A20SettingsPublicRecordV
+ _symbolic So15BSProcessHandleC011withProcessB0_SS16bundleIdentifierSSSg015scenePersistentF0t
+ _symbolic _____ 21UserNotificationsCore24SourceSelectionPresenterV0D22SelectorDismissalErrorO
+ _symbolic _____y_____G s11_SetStorageC 22AccessoryNotifications0C4TypeO
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 22AccessoryNotifications0D4TypeO
+ _symbolic _____yypG s23_ContiguousArrayStorageC
- _BPSNanoBulletinSendToNotificationCenter
- ___swift_memcpy33_8
- _get_enum_tag_for_layout_string 21UserNotificationsCore24SourceSelectionPresenterV0D13SelectorErrorO
- _symbolic So15BSProcessHandleC011withProcessB0_SSSg25scenePersistentIdentifiert
- _symbolic _____9forOrigin_t 21UserNotificationsCore24SourceSelectionPresenterV6OriginO
- _type_layout_string 21UserNotificationsCore24SourceSelectionPresenterV0D13SelectorErrorO
CStrings:
+ "Accessory not found"
+ "Received remote notification on topic %{public}@ for bundleIdentifier %{public}@ with no perAppToken, allowing."
+ "Source selection dismissed with error. %{public}@"
+ "[%{public}s] Allowing SE Angel to show settings even though we can't determine if it's in the foreground."
+ "[%{public}s] Cannot show settings. App is not in foreground."
+ "[%{public}s] Cannot show settings. System service client should never be nil."
+ "initWithArray:"
+ "isApplicationForeground(_:)"

```
