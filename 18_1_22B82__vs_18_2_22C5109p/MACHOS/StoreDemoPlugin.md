## StoreDemoPlugin

> `/System/Library/SpringBoardPlugins/StoreDemoPlugin.servicebundle/StoreDemoPlugin`

```diff

-1445.40.14.0.0
-  __TEXT.__text: 0xb8e0
+1445.60.30.0.1
+  __TEXT.__text: 0xb750
   __TEXT.__auth_stubs: 0x690
-  __TEXT.__objc_stubs: 0x27c0
-  __TEXT.__objc_methlist: 0xb28
+  __TEXT.__objc_stubs: 0x2720
+  __TEXT.__objc_methlist: 0xaf8
   __TEXT.__const: 0xb0
   __TEXT.__gcc_except_tab: 0x184
-  __TEXT.__oslogstring: 0x12e2
-  __TEXT.__cstring: 0xdc8
+  __TEXT.__oslogstring: 0x12ab
+  __TEXT.__cstring: 0xda2
   __TEXT.__objc_classname: 0x17a
-  __TEXT.__objc_methname: 0x2b4e
+  __TEXT.__objc_methname: 0x2aef
   __TEXT.__objc_methtype: 0x4a5
-  __TEXT.__unwind_info: 0x310
+  __TEXT.__unwind_info: 0x300
   __DATA_CONST.__auth_got: 0x358
-  __DATA_CONST.__got: 0x210
+  __DATA_CONST.__got: 0x218
   __DATA_CONST.__const: 0x3f0
-  __DATA_CONST.__cfstring: 0xb40
+  __DATA_CONST.__cfstring: 0xb20
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x38

   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA.__objc_const: 0x14f0
-  __DATA.__objc_selrefs: 0xbf0
+  __DATA.__objc_selrefs: 0xbc0
   __DATA.__objc_ivar: 0x88
   __DATA.__objc_data: 0x280
   __DATA.__data: 0x2a0

   - /System/Library/PrivateFrameworks/Sleep.framework/Sleep
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /System/Library/PrivateFrameworks/SpringBoardUI.framework/SpringBoardUI
+  - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 301
-  Symbols:   193
-  CStrings:  817
+  Functions: 299
+  Symbols:   194
+  CStrings:  811
 
Symbols:
+ _OBJC_CLASS_$_UIDevice
CStrings:
+ "%!s(MISSING) - iPad does not support Sleep Alarms"
+ "-[MSDAlarmManager getCurrentSleepAlarms]"
+ "Disabling alarm %!{(MISSING)public}@"
+ "currentDevice"
+ "disableAlarms"
+ "readBoolValueForFeatureFlag:"
+ "updateAlarm:"
+ "userInterfaceIdiom"
- " alarm mismatch. delete the alarm"
- "/var/mobile/Library/Application Support/ScreenSaverManager/.bundleAlarms.plist"
- "Alarm read in compareWithDefaultAlarms is : %!{(MISSING)public}@"
- "File  %!{(MISSING)public}@ does not exist."
- "_readBoolValueForFeatureFlag:"
- "alarmID"
- "compareWithDefaultAlarms:"
- "disableAlarm"
- "getCurrentAlarms"
- "initWithContentsOfFile:"
- "removeAlarm:"
- "saveAlarms:"
- "saveBundleAlarms"
- "writeToFile:atomically:"

```
