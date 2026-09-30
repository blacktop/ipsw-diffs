## UserNotificationsCore

> `/System/Library/PrivateFrameworks/UserNotificationsCore.framework/UserNotificationsCore`

```diff

-579.2.3.0.0
-  __TEXT.__text: 0x1944ac
-  __TEXT.__auth_stubs: 0x3030
-  __TEXT.__objc_methlist: 0x6238
-  __TEXT.__const: 0xb700
-  __TEXT.__cstring: 0xc6f7
+579.2.8.0.0
+  __TEXT.__text: 0x196d3c
+  __TEXT.__auth_stubs: 0x3080
+  __TEXT.__objc_methlist: 0x6250
+  __TEXT.__const: 0xb7d0
+  __TEXT.__cstring: 0xc8b7
   __TEXT.__gcc_except_tab: 0x6d4
-  __TEXT.__oslogstring: 0xbf28
+  __TEXT.__oslogstring: 0xc128
   __TEXT.__dlopen_cstrs: 0xf4
-  __TEXT.__constg_swiftt: 0x5324
-  __TEXT.__swift5_typeref: 0x4e2c
-  __TEXT.__swift5_reflstr: 0x2ec7
-  __TEXT.__swift5_fieldmd: 0x3950
+  __TEXT.__constg_swiftt: 0x5428
+  __TEXT.__swift5_typeref: 0x4ee8
+  __TEXT.__swift5_reflstr: 0x2ef7
+  __TEXT.__swift5_fieldmd: 0x39b4
   __TEXT.__swift5_builtin: 0x140
   __TEXT.__swift5_assocty: 0x3c0
-  __TEXT.__swift5_capture: 0x147c
-  __TEXT.__swift5_protos: 0xf0
-  __TEXT.__swift5_proto: 0x928
-  __TEXT.__swift5_types: 0x440
+  __TEXT.__swift5_capture: 0x14cc
+  __TEXT.__swift5_protos: 0xf4
+  __TEXT.__swift5_proto: 0x930
+  __TEXT.__swift5_types: 0x44c
   __TEXT.__swift5_mpenum: 0x58
-  __TEXT.__unwind_info: 0x53b8
-  __TEXT.__eh_frame: 0x4e40
-  __TEXT.__objc_classname: 0xe12
-  __TEXT.__objc_methname: 0x15611
-  __TEXT.__objc_methtype: 0x30ca
-  __TEXT.__objc_stubs: 0xc920
-  __DATA_CONST.__got: 0xfc8
+  __TEXT.__unwind_info: 0x5418
+  __TEXT.__eh_frame: 0x4e38
+  __TEXT.__objc_classname: 0xe15
+  __TEXT.__objc_methname: 0x156cc
+  __TEXT.__objc_methtype: 0x30d6
+  __TEXT.__objc_stubs: 0xc980
+  __DATA_CONST.__got: 0xfd0
   __DATA_CONST.__const: 0x1510
-  __DATA_CONST.__objc_classlist: 0x5c8
+  __DATA_CONST.__objc_classlist: 0x5e0
   __DATA_CONST.__objc_catlist: 0x80
   __DATA_CONST.__objc_protolist: 0x2a8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3fc8
+  __DATA_CONST.__objc_selrefs: 0x3ff8
   __DATA_CONST.__objc_protorefs: 0x158
   __DATA_CONST.__objc_superrefs: 0x1e8
-  __AUTH_CONST.__auth_got: 0x1828
-  __AUTH_CONST.__auth_ptr: 0xe90
-  __AUTH_CONST.__const: 0x9430
-  __AUTH_CONST.__cfstring: 0x5540
-  __AUTH_CONST.__objc_const: 0x22b70
+  __AUTH_CONST.__auth_got: 0x1850
+  __AUTH_CONST.__auth_ptr: 0xe68
+  __AUTH_CONST.__const: 0x9560
+  __AUTH_CONST.__cfstring: 0x55e0
+  __AUTH_CONST.__objc_const: 0x23490
   __AUTH_CONST.__objc_intobj: 0x108
   __AUTH.__objc_data: 0x70
-  __AUTH.__data: 0x330
-  __DATA.__objc_ivar: 0x848
-  __DATA.__data: 0x3560
-  __DATA.__bss: 0xc980
-  __DATA.__common: 0x198
-  __DATA_DIRTY.__objc_data: 0x3358
+  __AUTH.__data: 0x538
+  __DATA.__objc_ivar: 0x84c
+  __DATA.__data: 0x35d0
+  __DATA.__bss: 0xc990
+  __DATA.__common: 0x1a0
+  __DATA_DIRTY.__objc_data: 0x3360
   __DATA_DIRTY.__data: 0x71f0
   __DATA_DIRTY.__bss: 0x3900
   __DATA_DIRTY.__common: 0x250

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 8273
-  Symbols:   3538
-  CStrings:  5847
+  Functions: 8306
+  Symbols:   3545
+  CStrings:  5878
 
Symbols:
+ _UNSStringFromPipelineState
+ _swift_stdlib_random
CStrings:
+ "Reaping notifications for %!{(MISSING)private}s; app settings were cleared"
+ "summarizationSetting"
+ "setTaskCompleted"
+ "_TtC21UserNotificationsCore4Fuzz"
+ "classification.classifyUserNotification"
+ "settingsDefinedReaper"
+ "setTaskExpiredWithRetryAfter:error:"
+ "summarization.summarizeUserNotification"
+ "[%!s(MISSING)] Delaying closure by %!f(MISSING)s."
+ "failed"
+ "_TtC21UserNotificationsCore21SettingsDefinedReaper"
+ "[%!{(MISSING)public}@] Saving notification %!{(MISSING)public}@: %!{(MISSING)BOOL}d [ hasAlertContent: %!{(MISSING)BOOL}d, shouldPresentAlert: %!{(MISSING)BOOL}d settingsShouldSave: %!{(MISSING)BOOL}d pipelineState: %!{(MISSING)public}@]"
+ "com.apple.usernotifications.fuzz-timer"
+ "[%!{(MISSING)public}s] Could not determine summarization setting."
+ "Reaping notifications for %!{(MISSING)private}s; app setting was disabled"
+ "Using fuzz of %!f(MISSING)s. [%!f(MISSING)...%!f(MISSING)]"
+ "doubleForKey:"
+ "completed"
+ "Ignoring enablement check for non-receiver (%!s(MISSING))."
+ "Telling repository (%!s(MISSING)) to remove all notifications for %!s(MISSING)."
+ "overrideDataRetentionAge"
+ "Telling repository (%!s(MISSING)) to remove notifications store for %!s(MISSING)."
+ "recordValidationTest"
+ "\x06\x11"
+ "_recordValidationTest"
+ "@?16@0:8"
+ "[%!s(MISSING)] Running."
+ "@?"
+ "setRecordValidationTest:"
+ "pending"
+ "_TtC21UserNotificationsCoreP33_D8424875FA4EB0AF855935A789961EF232SettingsDefinedReaperClientProxy"
+ "T@?,C,N,V_recordValidationTest"
- "[%!{(MISSING)public}@] Saving notification %!{(MISSING)public}@: %!{(MISSING)BOOL}d [ hasAlertContent: %!{(MISSING)BOOL}d, shouldPresentAlert: %!{(MISSING)BOOL}d settingsShouldSave: %!{(MISSING)BOOL}d]"

```
