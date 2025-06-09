## HAENotifications

> `/System/Library/PrivateFrameworks/HAENotifications.framework/HAENotifications`

```diff

-747.607.0.0.0
-  __TEXT.__text: 0xd5a0
-  __TEXT.__auth_stubs: 0x600
+814.1.0.0.0
+  __TEXT.__text: 0xd5b4
+  __TEXT.__auth_stubs: 0x610
   __TEXT.__objc_methlist: 0xc34
   __TEXT.__const: 0x148
-  __TEXT.__cstring: 0xed8
+  __TEXT.__cstring: 0xec7
   __TEXT.__oslogstring: 0x159d
   __TEXT.__gcc_except_tab: 0x28
-  __TEXT.__unwind_info: 0x380
+  __TEXT.__unwind_info: 0x388
   __TEXT.__objc_classname: 0x1d7
-  __TEXT.__objc_methname: 0x2247
+  __TEXT.__objc_methname: 0x223c
   __TEXT.__objc_methtype: 0x70f
-  __TEXT.__objc_stubs: 0x2020
-  __DATA_CONST.__got: 0x390
+  __TEXT.__objc_stubs: 0x2000
+  __DATA_CONST.__got: 0x388
   __DATA_CONST.__const: 0x250
   __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9e0
+  __DATA_CONST.__objc_selrefs: 0x9d8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x70
-  __AUTH_CONST.__auth_got: 0x310
+  __AUTH_CONST.__auth_got: 0x318
   __AUTH_CONST.__const: 0x298
-  __AUTH_CONST.__cfstring: 0x10c0
+  __AUTH_CONST.__cfstring: 0x10a0
   __AUTH_CONST.__objc_const: 0x1c30
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH.__objc_data: 0xf0

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
   - /System/Library/PrivateFrameworks/AudioDataAnalysis.framework/AudioDataAnalysis
-  - /System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams
+  - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary
   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
   - /System/Library/PrivateFrameworks/GeoServices.framework/GeoServices
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/MediaExperience.framework/MediaExperience
   - /System/Library/PrivateFrameworks/NanoPreferencesSync.framework/NanoPreferencesSync
   - /System/Library/PrivateFrameworks/PersonalAudio.framework/PersonalAudio
-  - /System/Library/PrivateFrameworks/PowerLog.framework/PowerLog
   - /System/Library/PrivateFrameworks/ToneLibrary.framework/ToneLibrary
   - /usr/lib/libAudioStatistics.dylib
   - /usr/lib/libIOAccessoryManager.dylib
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B4D54D09-2DB6-3B3A-838D-9DEC83F338D3
+  UUID: E6F71DC8-BB0A-3D3D-B524-20926D568457
   Functions: 308
-  Symbols:   1424
-  CStrings:  936
+  Symbols:   1417
+  CStrings:  933
 
Symbols:
+ _BiomeLibrary
+ _OBJC_CLASS_$_BMDiscoverabilitySignals
+ ___55-[HAENHealthKitStore saveNotificationEventToHealthKit:]_block_invoke.301
+ ___55-[HAENHealthKitStore saveNotificationEventToHealthKit:]_block_invoke.301.cold.1
+ _objc_msgSend$Discoverability
+ _objc_msgSend$Signals
+ _objc_msgSend$initWithContentIdentifier:context:osBuild:userInfo:
- _OBJC_CLASS_$_BMDiscoverabilitySignalEvent
- _OBJC_CLASS_$_BMStreams
- ___55-[HAENHealthKitStore saveNotificationEventToHealthKit:]_block_invoke.298
- ___55-[HAENHealthKitStore saveNotificationEventToHealthKit:]_block_invoke.298.cold.1
- _objc_msgSend$bundleIdentifier
- _objc_msgSend$discoverabilitySignal
- _objc_msgSend$initWithIdentifier:bundleID:context:
- _objc_msgSend$mainBundle
CStrings:
+ "Discoverability"
+ "Signals"
+ "initWithContentIdentifier:context:osBuild:userInfo:"
- "bundleIdentifier"
- "com.apple.Health"
- "discoverabilitySignal"
- "initWithIdentifier:bundleID:context:"
- "mainBundle"

```
