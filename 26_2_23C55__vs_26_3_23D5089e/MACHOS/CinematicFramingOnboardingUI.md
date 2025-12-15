## CinematicFramingOnboardingUI

> `/Applications/CinematicFramingOnboardingUI.app/CinematicFramingOnboardingUI`

```diff

-664.62.12.0.0
-  __TEXT.__text: 0x1008
-  __TEXT.__auth_stubs: 0x1e0
+665.80.6.0.0
+  __TEXT.__text: 0x15c4
+  __TEXT.__auth_stubs: 0x250
   __TEXT.__objc_stubs: 0x880
   __TEXT.__objc_methlist: 0x5f4
-  __TEXT.__const: 0x8
+  __TEXT.__const: 0x18
   __TEXT.__objc_methname: 0x1552
   __TEXT.__objc_classname: 0xda
   __TEXT.__objc_methtype: 0x9d5
-  __TEXT.__cstring: 0x124
-  __TEXT.__unwind_info: 0xc8
-  __DATA_CONST.__auth_got: 0xf8
+  __TEXT.__cstring: 0x324
+  __TEXT.__oslogstring: 0x109
+  __TEXT.__unwind_info: 0xd0
+  __DATA_CONST.__auth_got: 0x130
   __DATA_CONST.__got: 0x88
   __DATA_CONST.__const: 0xa8
-  __DATA_CONST.__cfstring: 0x280
+  __DATA_CONST.__cfstring: 0x2c0
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA.__objc_ivar: 0x24
   __DATA.__objc_data: 0xf0
   __DATA.__data: 0x120
+  __DATA.__common: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /System/Library/PrivateFrameworks/SpringBoardUIServices.framework/SpringBoardUIServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C0F527F0-7921-3F74-87C7-8FB12944BB9E
+  UUID: 9DBA0267-7EB2-3676-BC8D-3B31394C3E42
   Functions: 48
-  Symbols:   60
-  CStrings:  311
+  Symbols:   67
+  CStrings:  324
 
Symbols:
+ __os_log_send_and_compose_impl
+ _fig_log_call_emit_and_clean_up_after_send_and_compose
+ _fig_log_emitter_get_os_log_and_send_and_compose_flags_and_os_log_type
+ _fig_note_initialize_category_with_default_work_cf
+ _objc_retain_x1
+ _objc_retain_x2
+ _os_log_type_enabled
Functions:
~ sub_100000eac -> sub_100000f4c : 12 -> 132
~ sub_10000122c -> sub_100001344 : 4 -> 280
~ sub_1000013ec -> sub_100001618 : 88 -> 364
~ sub_100001500 -> sub_100001840 : 4 -> 280
~ sub_100001b08 -> sub_100001f5c : 4 -> 280
~ sub_100001b10 -> sub_100002078 : 112 -> 356
CStrings:
+ "-[CinematicFramingRemoteAlertViewController configureWithContext:completion:]_block_invoke"
+ "-[CinematicFramingRemoteAlertViewController dismissRemoteAlert]_block_invoke_2"
+ "-[CinematicFramingRemoteAlertViewController handleControlCenterButton:]"
+ "-[CinematicFramingRemoteAlertViewController parameterForKey:fromUserInfo:requiredClass:]"
+ "-[CinematicFramingRemoteAlertViewController welcomeControllerDidDisappear:]_block_invoke"
+ "<<<< CinematicFramingRemoteAlertViewController >>>> %s: Failed to get remoteVCProxy: %{public}@"
+ "<<<< CinematicFramingRemoteAlertViewController >>>> %s: Missing or malformed value for %@: %@"
+ "<<<< CinematicFramingRemoteAlertViewController >>>> %s: called for %@ (%@)"
+ "cinematicframingremotealertviewcontroller_trace"
+ "com.apple.cameracapture"
+ "com.apple.coremedia"

```
