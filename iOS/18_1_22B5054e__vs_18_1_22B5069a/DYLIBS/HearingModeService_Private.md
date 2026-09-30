## HearingModeService_Private

> `/System/Library/PrivateFrameworks/HearingModeService_Private.framework/HearingModeService_Private`

```diff

-21.13.3.1.3
-  __TEXT.__text: 0x100b0
-  __TEXT.__auth_stubs: 0x480
-  __TEXT.__objc_methlist: 0x848
+21.16.1.4.0
+  __TEXT.__text: 0xff04
+  __TEXT.__auth_stubs: 0x490
+  __TEXT.__objc_methlist: 0x83c
   __TEXT.__const: 0x86
-  __TEXT.__gcc_except_tab: 0x50c
-  __TEXT.__cstring: 0x47c0
-  __TEXT.__unwind_info: 0x470
-  __TEXT.__objc_classname: 0x137
-  __TEXT.__objc_methname: 0x3122
-  __TEXT.__objc_methtype: 0x804
-  __TEXT.__objc_stubs: 0x2c40
-  __DATA_CONST.__got: 0x1d0
-  __DATA_CONST.__const: 0x7f8
+  __TEXT.__gcc_except_tab: 0x4d8
+  __TEXT.__cstring: 0x4755
+  __TEXT.__unwind_info: 0x460
+  __TEXT.__objc_classname: 0x135
+  __TEXT.__objc_methname: 0x3168
+  __TEXT.__objc_methtype: 0x823
+  __TEXT.__objc_stubs: 0x2d20
+  __DATA_CONST.__got: 0x1d8
+  __DATA_CONST.__const: 0x808
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc18
+  __DATA_CONST.__objc_selrefs: 0xc48
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x28
-  __AUTH_CONST.__auth_got: 0x250
+  __AUTH_CONST.__auth_got: 0x258
   __AUTH_CONST.__const: 0x140
-  __AUTH_CONST.__cfstring: 0x3c0
-  __AUTH_CONST.__objc_const: 0x18c8
+  __AUTH_CONST.__cfstring: 0x3e0
+  __AUTH_CONST.__objc_const: 0x18e8
   __AUTH_CONST.__objc_doubleobj: 0x80
   __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0xa8
+  __DATA.__objc_ivar: 0xb0
   __DATA.__data: 0x380
   __DATA_DIRTY.__objc_data: 0x140
   __DATA_DIRTY.__data: 0x150
   __DATA_DIRTY.__bss: 0x50
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
+  - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/HealthKit.framework/HealthKit
   - /System/Library/Frameworks/UserNotifications.framework/UserNotifications

   - /System/Library/PrivateFrameworks/ToneLibrary.framework/ToneLibrary
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 260
-  Symbols:   403
-  CStrings:  962
+  Functions: 257
+  Symbols:   402
+  CStrings:  974
 
Symbols:
+ _HMOcclusionResultIsOverallPassing
+ _OBJC_CLASS_$_LSApplicationWorkspace
CStrings:
+ "-[HMDeviceManager _diagnosticDataReceived:identifier:isInternal:]"
+ "-[HMHealthKitUtilities _startAudiogramQuery]"
+ "-[HMOcclusionNotification _showHearingProtectionOcclusionNotification:]"
+ "-[HMOcclusionNotification _showHearingProtectionOcclusionNotification:]_block_invoke"
+ "-[HMOcclusionNotification presentCleaningInfoArticle]"
+ "ActiveNotificationNotShown"
+ "CleaningAlertNotShown"
+ "PlacardNotShown"
+ "Presenting AirPods Cleaning Info Article"
+ "URL string is malformed"
+ "URLWithString:"
+ "_audiogramQueryInProgress"
+ "_btAddress"
+ "_diagnosticDataReceived:identifier:isInternal:"
+ "_showHearingProtectionOcclusionNotification:"
+ "cloudRecordLoaded"
+ "defaultWorkspace"
+ "executing audiogram query on HealthStore"
+ "https://support.apple.com/120409?cid=mc-ols-airpods-article_120409-settings_ui-08232024"
+ "initWithString:"
+ "openSensitiveURL:withOptions:"
+ "presentCleaningInfoArticle"
+ "setCloudRecordLoaded:"
+ "showHearingProtectionOcclusionNotification:forAddress:"
+ "submitMetricsForOcclusionPolicy"
+ "v28@0:8I16@20"
+ "v36@0:8@16@24B32"
- "\x02"
- "### Unable to set occlusionIndicationShown, device record not found for identifier: %!@(MISSING)"
- "-[HMDeviceManager _diagnosticDataReceived:identifier:]"
- "-[HMDeviceManager _occlusionIndicationShownForDeviceIdentifier:featureID:type:action:]"
- "-[HMOcclusionNotification showHearingProtectionOcclusionNotification:]"
- "-[HMOcclusionNotification showHearingProtectionOcclusionNotification:]_block_invoke"
- "-[HMServiceXPCConnection clientSetOcclusionIndicationShownForDeviceIdentifier:featureID:type:action:]"
- "-[HMServiceXPCConnection clientSetOcclusionIndicationShownForDeviceIdentifier:featureID:type:action:]_block_invoke"
- "NoIndication"
- "OcclusionIndicationShown with UUID: %!@(MISSING), type: %!s(MISSING), feature: %!s(MISSING), action: %!s(MISSING)"
- "_diagnosticDataReceived:identifier:"
- "_occlusionIndicationShownForDeviceIdentifier:featureID:type:action:"
- "clientSetOcclusionIndicationShownForDeviceIdentifier:featureID:type:action:"
- "occlusionIndicationShownForDeviceIdentifier:featureID:type:action:"
- "showHearingProtectionOcclusionNotification:"

```
