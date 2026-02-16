## DefaultCallingAppsSettings

> `/System/Library/Settings/DefaultApps/DefaultCallingAppsSettings.plugin/DefaultCallingAppsSettings`

```diff

-383.400.1.0.0
-  __TEXT.__text: 0x173c4
-  __TEXT.__auth_stubs: 0xe20
+383.500.61.0.0
+  __TEXT.__text: 0x18f10
+  __TEXT.__auth_stubs: 0xe70
+  __TEXT.__objc_stubs: 0xa20
   __TEXT.__objc_methlist: 0x47c
-  __TEXT.__const: 0xbe2
-  __TEXT.__swift5_typeref: 0x79b
-  __TEXT.__swift5_capture: 0x240
+  __TEXT.__const: 0xc42
+  __TEXT.__swift5_typeref: 0x7c5
+  __TEXT.__swift5_capture: 0x27c
   __TEXT.__swift5_reflstr: 0x383
   __TEXT.__swift5_assocty: 0xf8
-  __TEXT.__constg_swiftt: 0x5b8
+  __TEXT.__constg_swiftt: 0x5a8
   __TEXT.__swift5_fieldmd: 0x2e8
-  __TEXT.__cstring: 0x124f
-  __TEXT.__oslogstring: 0x5c2
-  __TEXT.__objc_methname: 0xe98
+  __TEXT.__cstring: 0xe7f
+  __TEXT.__oslogstring: 0xa52
   __TEXT.__swift5_proto: 0x50
   __TEXT.__swift5_types: 0x34
+  __TEXT.__objc_methtype: 0x176
+  __TEXT.__objc_classname: 0x270
+  __TEXT.__objc_methname: 0x1119
   __TEXT.__swift5_builtin: 0x14
-  __TEXT.__objc_classname: 0x6d
-  __TEXT.__objc_methtype: 0x120
-  __TEXT.__swift_as_entry: 0x3c
-  __TEXT.__swift_as_ret: 0x40
+  __TEXT.__swift_as_entry: 0x38
+  __TEXT.__swift_as_ret: 0x3c
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x650
-  __TEXT.__eh_frame: 0x9dc
-  __DATA_CONST.__auth_got: 0x710
-  __DATA_CONST.__got: 0x208
-  __DATA_CONST.__auth_ptr: 0x3f0
-  __DATA_CONST.__const: 0x818
+  __TEXT.__unwind_info: 0x660
+  __TEXT.__eh_frame: 0x9d4
+  __DATA_CONST.__auth_got: 0x740
+  __DATA_CONST.__got: 0x210
+  __DATA_CONST.__auth_ptr: 0x3e8
+  __DATA_CONST.__const: 0x908
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA.__objc_const: 0x818
-  __DATA.__objc_selrefs: 0x4d0
+  __DATA.__objc_selrefs: 0x4e0
   __DATA.__objc_data: 0x618
   __DATA.__data: 0x730
   __DATA.__bss: 0xac8

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 326F31FD-F12D-3427-A9EE-9A63E048B321
-  Functions: 452
-  Symbols:   178
-  CStrings:  325
+  UUID: 3F485B00-140F-31F6-9417-F2922F67CBB3
+  Functions: 462
+  Symbols:   180
+  CStrings:  344
 
Symbols:
+ _NSOSStatusErrorDomain
+ _OBJC_CLASS_$_NSError
+ _dispatch_group_create
+ _dispatch_group_enter
+ _dispatch_group_leave
- _objc_retain_x1
- _objc_retain_x24
- _objc_retain_x9
CStrings:
+ "%s: Current default dialer app: '%s' (id: %s)"
+ "%s: DefaultCallingAppsModel.defaultCallingApp is NIL - no default calling app is currently set in the system. Returning empty string to show nothing selected in UI."
+ "DefaultCallingAppsModel"
+ "If you have multiple calling apps, you can change the default."
+ "LaunchServicesActor.fetchAvailableApps() - Fetching available apps for: %s"
+ "LaunchServicesActor.fetchAvailableApps() - Returning %ld available apps"
+ "NONE FOUND (will use FaceTime)"
+ "Setting default calling app DONE, all providers notified"
+ "Setting default calling app to %s STARTED"
+ "Setting default dialer app DONE"
+ "Setting default dialer app DONE, all providers notified"
+ "Setting default dialer app to %s STARTED"
+ "code"
+ "com.TelephonySettings.defaultAppsFetch"
+ "domain"
+ "fetchDefaultAppSync - CRITICAL: iPhone has no default calling app - THIS SHOULD BE IMPOSSIBLE!"
+ "fetchDefaultAppSync - Corrupted Launch Services record (no bundleID)"
+ "fetchDefaultAppSync - Dialer has no default, returning nil (model should default to .facetime)"
+ "fetchDefaultAppSync - Launch Services framework error: %@"
+ "fetchDefaultAppSync - _handleNoDefaultRecordApp evaluating no-default state for type: %s"
+ "fetchDefaultAppSync - found app: %s"
+ "fetchDefaultAppSync - found relay calling app: %s"
+ "fetchDefaultAppSync - iPad with no default, returning .none"
+ "fetchDefaultAppSync - no default set (error -10814), we will check _handleNoDefaultRecordApp next"
+ "fetchDefaultAppSync - no default set (nil record), we will check _handleNoDefaultRecordApp next"
+ "fetchDefaultAppSync(for: %s) - START"
+ "init() - Default apps fetched, starting remaining initialization"
+ "init() - Initialization complete (async work continues in background)"
+ "init() - Initialization started"
+ "initializeApps() async - DONE"
+ "initializeApps() async - Data fetched successfully, defaultCallingApp: %s, defaultDialerApp: %s"
+ "initializeApps() async - START"
+ "initializeApps() async - Updating properties on main actor"
+ "initializeApps() async - canChangeDialerApp from LS: %{bool}d"
+ "setDefaultCallingApp called with NIL - user wants to clear default calling app"
- "%s: Current default dialier app: '%s' (id: %s)"
- "Couldn't fetch default %{public}s app: missing workspace or bundle ID"
- "Couldn't fetch default %{public}s app: no defaultApplication exists"
- "Couldn’t fetch default %{public}s app: %@"
- "DEFAULT CALLING APPS MODEL: Setting default calling app DONE, all providers notified"
- "DEFAULT CALLING APPS MODEL: Setting default calling app to %s STARTED"
- "DEFAULT CALLING APPS MODEL: Setting default dialer app DONE"
- "DEFAULT CALLING APPS MODEL: Setting default dialer app DONE, all providers notified"
- "DEFAULT CALLING APPS MODEL: Setting default dialer app to %s STARTED"
- "Fetched nil defaultApp for category %{public}s"
- "Fetching LaunchServices backed default app for %{public}s"
- "Fetching default app for %{public}s"
- "We are on iPad, returning None for default calling app"

```
