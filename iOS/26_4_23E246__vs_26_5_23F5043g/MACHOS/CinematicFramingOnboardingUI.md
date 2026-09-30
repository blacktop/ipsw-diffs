## CinematicFramingOnboardingUI

> `/Applications/CinematicFramingOnboardingUI.app/CinematicFramingOnboardingUI`

```diff

-665.100.10.0.0
-  __TEXT.__text: 0x11e4
-  __TEXT.__auth_stubs: 0x200
+665.120.3.0.0
+  __TEXT.__text: 0x17b4
+  __TEXT.__auth_stubs: 0x250
   __TEXT.__objc_stubs: 0x880
   __TEXT.__objc_methlist: 0x5f4
-  __TEXT.__const: 0x8
+  __TEXT.__const: 0x18
   __TEXT.__objc_methname: 0x1552
   __TEXT.__objc_classname: 0xda
   __TEXT.__objc_methtype: 0x9d5
-  __TEXT.__cstring: 0x124
-  __TEXT.__unwind_info: 0xf0
-  __DATA_CONST.__auth_got: 0x108
+  __TEXT.__cstring: 0x324
+  __TEXT.__oslogstring: 0x109
+  __TEXT.__unwind_info: 0xf8
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
-  UUID: 9FC050B2-09CF-3719-936C-EA01D7AB4A35
+  UUID: 58496007-9C41-368A-9DD5-0E891D24D9D1
   Functions: 48
-  Symbols:   62
-  CStrings:  311
+  Symbols:   67
+  CStrings:  324
 
Symbols:
+ __os_log_send_and_compose_impl
+ _fig_log_call_emit_and_clean_up_after_send_and_compose
+ _fig_log_emitter_get_os_log_and_send_and_compose_flags_and_os_log_type
+ _fig_note_initialize_category_with_default_work_cf
+ _os_log_type_enabled
Functions:
~ sub_100000eac -> sub_100000f4c : 12 -> 132
~ sub_100001260 -> sub_100001378 : 4 -> 284
~ sub_100001434 -> sub_100001664 : 92 -> 372
~ sub_100001550 -> sub_100001898 : 4 -> 284
~ sub_100001bac -> sub_10000200c : 4 -> 284
~ sub_100001bb4 -> sub_10000212c : 120 -> 368
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
