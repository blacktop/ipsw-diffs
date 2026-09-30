## SafetyMonitor

> `/System/Library/PrivateFrameworks/SafetyMonitor.framework/SafetyMonitor`

```diff

 1062.0.1.0.1
-  __TEXT.__text: 0x72c6c
-  __TEXT.__auth_stubs: 0x1250
-  __TEXT.__objc_methlist: 0x4d54
+  __TEXT.__text: 0x73084
+  __TEXT.__auth_stubs: 0x1270
+  __TEXT.__objc_methlist: 0x4d64
   __TEXT.__const: 0x1380
   __TEXT.__dlopen_cstrs: 0x60
-  __TEXT.__cstring: 0xbf20
+  __TEXT.__cstring: 0xbf90
   __TEXT.__swift5_typeref: 0x4a2
-  __TEXT.__oslogstring: 0x4345
+  __TEXT.__oslogstring: 0x448f
   __TEXT.__constg_swiftt: 0x450
   __TEXT.__swift5_reflstr: 0x2be
   __TEXT.__swift5_fieldmd: 0x3ec

   __TEXT.__swift5_protos: 0x4
   __TEXT.__ustring: 0xd34
   __TEXT.__gcc_except_tab: 0xf70
-  __TEXT.__unwind_info: 0x17f0
+  __TEXT.__unwind_info: 0x17f8
   __TEXT.__eh_frame: 0x9dc
   __TEXT.__objc_classname: 0x9e4
-  __TEXT.__objc_methname: 0xc60c
+  __TEXT.__objc_methname: 0xc621
   __TEXT.__objc_methtype: 0x2166
-  __TEXT.__objc_stubs: 0x5860
-  __DATA_CONST.__got: 0x4b8
+  __TEXT.__objc_stubs: 0x58e0
+  __DATA_CONST.__got: 0x4c8
   __DATA_CONST.__const: 0x1480
   __DATA_CONST.__objc_classlist: 0x268
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x120
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2288
+  __DATA_CONST.__objc_selrefs: 0x2290
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x1a8
-  __AUTH_CONST.__auth_got: 0x938
+  __AUTH_CONST.__auth_got: 0x948
   __AUTH_CONST.__const: 0xa10
-  __AUTH_CONST.__cfstring: 0x4f00
+  __AUTH_CONST.__cfstring: 0x4f40
   __AUTH_CONST.__objc_const: 0x8290
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0x11c0

   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreRoutine.framework/CoreRoutine
   - /System/Library/PrivateFrameworks/CoreTime.framework/CoreTime
+  - /System/Library/PrivateFrameworks/Fitness.framework/Fitness
   - /System/Library/PrivateFrameworks/GeoServices.framework/GeoServices
   - /System/Library/PrivateFrameworks/IDS.framework/IDS
   - /System/Library/PrivateFrameworks/IDSFoundation.framework/IDSFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: F0315D5D-BD83-3AC0-9E58-0672254EEF9F
-  Functions: 2184
-  Symbols:   5688
-  CStrings:  3997
+  UUID: 9A438798-3262-31AA-85E2-829697D8B96D
+  Functions: 2185
+  Symbols:   5696
+  CStrings:  4009
 
Symbols:
+ +[SMFeatureFlags zelkovaKahanaEnabled]
+ _FIIsWorkoutSafetyCheckInEnabled
+ _objc_msgSend$alwaysOnPromptCount
+ _objc_msgSend$checkInRemindersPreviouslyEnabled
+ _objc_msgSend$isMessagesAppInstalled
+ _objc_msgSend$zelkovaKahanaEnabled
+ _os_variant_has_internal_content
Functions:
~ +[SMMobileSMSPreferencesUtilities showCheckInRemindersTip] : 8 -> 996
~ +[SMSessionMonitorContext isWorkoutTriggerCategory:] : 24 -> 16
+ +[SMFeatureFlags zelkovaKahanaEnabled]
CStrings:
+ "%@, %@, Check In Reminders is currently enabled, do not show tip"
+ "%@, %@, Check In reminders was previously enabled, do not show tip"
+ "%@, %@, Fewer than %d workout-bound sessions completed, do not show tip"
+ "%@, %@, Messages app is not installed, do not show tip"
+ "%@, %@, Show tip"
+ "%@, %@, zelkovaKahana is not enabled, do not show tip"
+ "SMTriggerCategoryWorkoutNoMovementHeadsetInEar"
+ "SMTriggerCategoryWorkoutNoMovementHeadsetOutOfEar"
+ "Zelkova_Kahana"
+ "zelkovaKahanaEnabled"

```
