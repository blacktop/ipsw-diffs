## HearingSettings

> `/System/Library/PreferenceBundles/HearingSettings.bundle/HearingSettings`

```diff

-456.6.1.0.0
-  __TEXT.__text: 0x2311c
+456.6.2.0.0
+  __TEXT.__text: 0x23a3c
   __TEXT.__auth_stubs: 0x7a0
-  __TEXT.__objc_stubs: 0x5860
+  __TEXT.__objc_stubs: 0x5920
   __TEXT.__objc_methlist: 0x1a18
   __TEXT.__const: 0xc8
-  __TEXT.__gcc_except_tab: 0x538
-  __TEXT.__objc_methname: 0x6b87
-  __TEXT.__cstring: 0x2aec
+  __TEXT.__gcc_except_tab: 0x590
+  __TEXT.__objc_methname: 0x6c26
+  __TEXT.__cstring: 0x2ba7
   __TEXT.__oslogstring: 0x66
   __TEXT.__objc_classname: 0x5a3
   __TEXT.__objc_methtype: 0x155d
-  __TEXT.__dlopen_cstrs: 0x174
-  __TEXT.__unwind_info: 0x850
+  __TEXT.__dlopen_cstrs: 0x1bd
+  __TEXT.__unwind_info: 0x870
   __DATA_CONST.__auth_got: 0x3e0
-  __DATA_CONST.__got: 0x418
-  __DATA_CONST.__const: 0x9a0
-  __DATA_CONST.__cfstring: 0x2b00
+  __DATA_CONST.__got: 0x428
+  __DATA_CONST.__const: 0x9e0
+  __DATA_CONST.__cfstring: 0x2b60
   __DATA_CONST.__objc_classlist: 0xf8
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_intobj: 0x78
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA.__objc_const: 0x3be0
-  __DATA.__objc_selrefs: 0x1b60
+  __DATA.__objc_selrefs: 0x1b88
   __DATA.__objc_ivar: 0x1b0
   __DATA.__objc_data: 0x9b0
   __DATA.__data: 0x720
-  __DATA.__bss: 0x68
+  __DATA.__bss: 0x88
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CallKit.framework/CallKit

   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/HealthKit.framework/HealthKit
   - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
   - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
   - /System/Library/Frameworks/UIKit.framework/UIKit

   - /System/Library/PrivateFrameworks/AudiogramIngestion.framework/AudiogramIngestion
   - /System/Library/PrivateFrameworks/BluetoothManager.framework/BluetoothManager
   - /System/Library/PrivateFrameworks/HearingCore.framework/HearingCore
+  - /System/Library/PrivateFrameworks/HearingModeService_Private.framework/HearingModeService_Private
   - /System/Library/PrivateFrameworks/HearingUI.framework/HearingUI
   - /System/Library/PrivateFrameworks/HearingUtilities.framework/HearingUtilities
   - /System/Library/PrivateFrameworks/MediaExperience.framework/MediaExperience

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 651
-  Symbols:   366
-  CStrings:  1803
+  Functions: 662
+  Symbols:   368
+  CStrings:  1816
 
Symbols:
+ _HKFeatureIdentifierHearingAid
+ _OBJC_CLASS_$_HMHealthKitUtilities
CStrings:
+ "HKHealthStore"
+ "HKObjectType"
+ "HKSampleQuery"
+ "PersonalAudioFeatureAudiogramDescription"
+ "PersonalAudioFeatureNoAudiogramDescription"
+ "audiogramSampleType"
+ "executeQuery:"
+ "getRegionSupportStatusForFeatureID:"
+ "initWithSampleType:predicate:limit:sortDescriptors:resultsHandler:"
+ "isHealthDataAvailable"
+ "softlink:r:path:/System/Library/Frameworks/HealthKit.framework/HealthKit"
+ "v32@?0@\"HKSampleQuery\"8@\"NSArray\"16@\"NSError\"24"
+ "waveform.path"

```
