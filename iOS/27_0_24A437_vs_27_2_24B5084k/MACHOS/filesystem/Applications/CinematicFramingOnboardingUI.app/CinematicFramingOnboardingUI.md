## CinematicFramingOnboardingUI

> `/Applications/CinematicFramingOnboardingUI.app/CinematicFramingOnboardingUI`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__const`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-764.22.13.0.0
-  __TEXT.__text: 0xfbc
-  __TEXT.__auth_stubs: 0x1e0
+764.40.4.122.1
+  __TEXT.__text: 0x157c
+  __TEXT.__auth_stubs: 0x250
   __TEXT.__objc_stubs: 0x880
   __TEXT.__objc_methlist: 0x5f4
-  __TEXT.__const: 0x8
+  __TEXT.__const: 0x18
   __TEXT.__objc_methname: 0x1552
   __TEXT.__objc_classname: 0xd6
   __TEXT.__objc_methtype: 0x9d5
-  __TEXT.__cstring: 0x128
-  __TEXT.__unwind_info: 0xd8
+  __TEXT.__cstring: 0x328
+  __TEXT.__oslogstring: 0x109
+  __TEXT.__unwind_info: 0xe0
   __DATA_CONST.__const: 0xa8
-  __DATA_CONST.__cfstring: 0x280
+  __DATA_CONST.__cfstring: 0x2c0
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
-  __DATA_CONST.__auth_got: 0xf8
+  __DATA_CONST.__auth_got: 0x130
   __DATA_CONST.__got: 0x88
   __DATA.__objc_const: 0x730
   __DATA.__objc_selrefs: 0x4f0
   __DATA.__objc_ivar: 0x24
   __DATA.__objc_data: 0xf0
   __DATA.__data: 0x120
+  __DATA.__common: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 48
-  Symbols:   60
-  CStrings:  292
+  Symbols:   67
+  CStrings:  303
 
Symbols:
+ __os_log_send_and_compose_impl
+ _fig_log_call_emit_and_clean_up_after_send_and_compose
+ _fig_log_emitter_get_os_log_and_send_and_compose_flags_and_os_log_type
+ _fig_note_initialize_category_with_default_work_cf
+ _objc_retain_x1
+ _objc_retain_x2
+ _os_log_type_enabled
Functions:
~ sub_100000ea0 -> sub_100000f40 : 12 -> 120
~ sub_100001214 -> sub_100001320 : 4 -> 280
~ sub_1000013c8 -> sub_1000015e8 : 76 -> 352
~ sub_1000014c4 -> sub_1000017f8 : 4 -> 280
~ sub_100001aa8 -> sub_100001ef0 : 4 -> 280
~ sub_100001ab0 -> sub_10000200c : 100 -> 360
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
