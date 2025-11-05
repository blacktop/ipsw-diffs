## HearingCore

> `/System/Library/PrivateFrameworks/HearingCore.framework/Versions/A/HearingCore`

```diff

-456.6.3.0.0
-  __TEXT.__text: 0x69a8
-  __TEXT.__auth_stubs: 0x530
-  __TEXT.__objc_methlist: 0x670
+456.8.7.0.0
+  __TEXT.__text: 0x6c84
+  __TEXT.__auth_stubs: 0x540
+  __TEXT.__objc_methlist: 0x6b0
   __TEXT.__const: 0x88
-  __TEXT.__cstring: 0xa60
+  __TEXT.__cstring: 0xa95
   __TEXT.__oslogstring: 0x120
   __TEXT.__gcc_except_tab: 0xf4
-  __TEXT.__unwind_info: 0x2d0
+  __TEXT.__unwind_info: 0x2b0
   __TEXT.__objc_classname: 0x7e
-  __TEXT.__objc_methname: 0x1337
-  __TEXT.__objc_methtype: 0x2b1
-  __TEXT.__objc_stubs: 0x11a0
-  __DATA_CONST.__got: 0x140
+  __TEXT.__objc_methname: 0x13fa
+  __TEXT.__objc_methtype: 0x2cc
+  __TEXT.__objc_stubs: 0x12e0
+  __DATA_CONST.__got: 0x150
   __DATA_CONST.__const: 0xb8
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5e8
+  __DATA_CONST.__objc_selrefs: 0x628
   __DATA_CONST.__objc_superrefs: 0x30
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0x2a8
+  __AUTH_CONST.__auth_got: 0x2b0
   __AUTH_CONST.__const: 0x630
-  __AUTH_CONST.__cfstring: 0xa60
+  __AUTH_CONST.__cfstring: 0xb00
   __AUTH_CONST.__objc_const: 0x8c8
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0x1e0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C2F35FA6-F92F-3AB1-9DE8-3C9196D9FBDD
-  Functions: 213
-  Symbols:   686
-  CStrings:  488
+  UUID: EC39058F-2B03-321F-B375-674A087B3DC9
+  Functions: 243
+  Symbols:   730
+  CStrings:  507
 
Symbols:
+ +[HCSettings additionalInfoForPrefenceUpdate]
+ +[HCUtilities bluetoothManagerQueue].cold.1
+ +[HCUtilities currentProcessIsAXUIServer].cold.1
+ +[HCUtilities currentProcessIsCarousel].cold.1
+ +[HCUtilities currentProcessIsHealth].cold.1
+ +[HCUtilities currentProcessIsHeard].cold.1
+ +[HCUtilities currentProcessIsInCallService].cold.1
+ +[HCUtilities currentProcessIsPreferences].cold.1
+ +[HCUtilities currentProcessIsRTTExternsion].cold.1
+ +[HCUtilities currentProcessIsSpringBoard].cold.1
+ +[HCUtilities currentProcessIsSystemApp].cold.1
+ +[HCUtilities isInternalInstall].cold.1
+ +[HCUtilities supportsLEA2].cold.1
+ -[HCSettings keysMonitoredForUpdates]
+ -[HCSettings saveUpdateInfoIfNeededForPreferenceKey:toDomain:]
+ -[HCSettings shouldSaveUpdateInfoForPreferenceKey:]
+ -[NSNumber(HearingCore) localizedFormat].cold.1
+ CSInitializeLogging.cold.1
+ HAInitializeLogging.cold.1
+ HCApplicationGetMainBundleIdentifier.cold.1
+ HCHPInitializeLogging.cold.1
+ HCLogHearingHandoff.cold.1
+ HCLogHearingLiveListen.cold.1
+ HCLogHearingNearby.cold.1
+ HCLogHearingNearbyIDS.cold.1
+ HCLogHearingXPC.cold.1
+ HCLogSoundMeter.cold.1
+ HCProcessGetName.cold.1
+ HearingInitializeLogging.cold.1
+ PAInitializeLogging.cold.1
+ _OBJC_CLASS_$_NSDate
+ _OBJC_CLASS_$_NSDateFormatter
+ __OBJC_$_CLASS_METHODS_HCSettings
+ _objc_msgSend$additionalInfoForPrefenceUpdate
+ _objc_msgSend$currentProcessIsHeard
+ _objc_msgSend$currentProcessIsPreferences
+ _objc_msgSend$keysMonitoredForUpdates
+ _objc_msgSend$now
+ _objc_msgSend$saveUpdateInfoIfNeededForPreferenceKey:toDomain:
+ _objc_msgSend$setDateFormat:
+ _objc_msgSend$setValue:forKey:
+ _objc_msgSend$shouldSaveUpdateInfoForPreferenceKey:
+ _objc_msgSend$stringFromDate:
+ _objc_opt_new
CStrings:
+ "Other"
+ "Preferences"
+ "SpringBoard"
+ "_UpdateInfo"
+ "additionalInfoForPrefenceUpdate"
+ "keysMonitoredForUpdates"
+ "now"
+ "saveUpdateInfoIfNeededForPreferenceKey:toDomain:"
+ "setDateFormat:"
+ "setValue:forKey:"
+ "shouldSaveUpdateInfoForPreferenceKey:"
+ "stringFromDate:"
+ "v32@0:8@16^{__CFString=}24"
+ "yyyy-MM-dd"

```
