## RelevanceServices

> `/System/Library/PrivateFrameworks/RelevanceServices.framework/RelevanceServices`

```diff

 217.11.0.0.0
-  __TEXT.__text: 0xb668
+  __TEXT.__text: 0xdd1c
   __TEXT.__objc_methlist: 0x268
-  __TEXT.__const: 0x874
-  __TEXT.__cstring: 0x5d2
-  __TEXT.__swift5_typeref: 0x216
-  __TEXT.__swift5_capture: 0x20
-  __TEXT.__oslogstring: 0xa9
-  __TEXT.__constg_swiftt: 0x1d4
-  __TEXT.__swift5_fieldmd: 0x288
-  __TEXT.__swift5_types: 0x28
-  __TEXT.__swift5_reflstr: 0x2e2
+  __TEXT.__const: 0xa24
+  __TEXT.__cstring: 0x853
+  __TEXT.__constg_swiftt: 0x2ec
+  __TEXT.__swift5_typeref: 0x2e2
+  __TEXT.__swift5_builtin: 0x3c
+  __TEXT.__swift5_types: 0x38
+  __TEXT.__swift5_fieldmd: 0x320
+  __TEXT.__swift5_reflstr: 0x350
+  __TEXT.__oslogstring: 0x18f
+  __TEXT.__swift5_capture: 0x78
+  __TEXT.__swift5_protos: 0xc
+  __TEXT.__swift5_proto: 0x54
+  __TEXT.__swift_as_entry: 0x8
+  __TEXT.__swift_as_ret: 0x8
   __TEXT.__swift5_assocty: 0x60
-  __TEXT.__swift5_builtin: 0x28
-  __TEXT.__swift5_proto: 0x50
-  __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x3d0
+  __TEXT.__unwind_info: 0x498
+  __TEXT.__eh_frame: 0x120
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x100
-  __DATA_CONST.__objc_classlist: 0x28
+  __DATA_CONST.__const: 0x110
+  __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1b8
+  __DATA_CONST.__objc_selrefs: 0x1d8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__got: 0x170
-  __AUTH_CONST.__const: 0x498
+  __DATA_CONST.__got: 0x188
+  __AUTH_CONST.__const: 0x6e8
   __AUTH_CONST.__cfstring: 0x20
-  __AUTH_CONST.__objc_const: 0x588
-  __AUTH_CONST.__auth_got: 0x4d8
+  __AUTH_CONST.__objc_const: 0x680
+  __AUTH_CONST.__auth_got: 0x590
   __AUTH.__objc_data: 0x3b0
-  __AUTH.__data: 0xd0
-  __DATA.__data: 0x358
-  __DATA.__common: 0x30
+  __AUTH.__data: 0x180
+  __DATA.__data: 0x390
+  __DATA.__common: 0x78
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics

   - /usr/lib/swift/libswiftSynchronization.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 375
-  Symbols:   321
-  CStrings:  43
+  Functions: 444
+  Symbols:   365
+  CStrings:  60
 
Symbols:
+ _CFNotificationCenterPostNotification
+ _MobileGestalt_get_deviceSupportsAudioIntelligence
+ _OBJC_CLASS_$_NSHashTable
+ _OBJC_CLASS_$__TtCs12_SwiftObject
+ _OBJC_METACLASS_$__TtCs12_SwiftObject
+ _RSDeviceSupportsAudioIntelligence
+ _RSDeviceSupportsAudioIntelligence._supported
+ _RSDeviceSupportsAudioIntelligence.onceToken
+ __DATA__TtC17RelevanceServices36AudioUnderstandingSettingsController
+ __IVARS__TtC17RelevanceServices36AudioUnderstandingSettingsController
+ __METACLASS_DATA__TtC17RelevanceServices36AudioUnderstandingSettingsController
+ ___RSDeviceSupportsAudioIntelligence_block_invoke
+ ___swift_async_entry_functlets
+ ___swift_async_ret_functlets
+ _free
+ _objc_msgSend$addObject:
+ _objc_msgSend$allObjects
+ _objc_msgSend$removeObject:
+ _objc_msgSend$weakObjectsHashTable
+ _objc_release_x27
+ _swift_conformsToProtocol2
+ _swift_coroFrameAlloc
+ _swift_deallocClassInstance
+ _swift_getForeignTypeMetadata
+ _swift_release_x24
+ _swift_retain_x19
+ _swift_retain_x24
+ _swift_retain_x25
+ _swift_task_alloc
+ _swift_task_create
+ _swift_task_dealloc
+ _symbolic $s17RelevanceServices26AudioUnderstandingSettingsP
+ _symbolic $s17RelevanceServices34AudioUnderstandingSettingsObserverP
+ _symbolic SS
+ _symbolic ScA_pSg
+ _symbolic ScPSg
+ _symbolic _____ 17RelevanceServices15ShazamAnalyticsV
+ _symbolic _____ 17RelevanceServices27AudioUnderstandingAnalyticsV
+ _symbolic _____ 17RelevanceServices36AudioUnderstandingSettingsControllerC
+ _symbolic _____ So39NHSSPrivacyDefaultsMicrophonePermissionV
+ _symbolic ______p 17RelevanceServices34AudioUnderstandingSettingsObserverP
+ _symbolic _____ySo11NSHashTableCyyXlGG 15Synchronization5MutexVAARi_zrlE
+ _symbolic x
+ _symbolic ytIeAgHr_
CStrings:
+ "MusicDetectedSeconds"
+ "MusicDetectionOptedIn"
+ "Sent AudioUnderstanding activation. type=%{public}s, enabled=%{bool,public}d, activeMinutes=%{public}ld, detectedMinutes=%{public}ld."
+ "Sent music detection duration. seconds=%ld, permission=%{public}s."
+ "audioBufferEnabled"
+ "audioIntelligence"
+ "audioUnderstanding"
+ "audioUnderstandingController"
+ "audioUnderstandingSecure"
+ "com.apple.RelevancePlatform.AudioUnderstanding"
+ "com.apple.RelevancePlatform.AudioUnderstandingPrefsDidChange"
+ "com.apple.RelevancePlatform.MindPalaceActiveStateDidChange"
+ "com.apple.RelevancePlatform.MindPalaceGlobalEnabledDidChange"
+ "com.apple.Shazam.MusicRecognition.MusicDetectionDuration"
+ "com.apple.audioUnderstanding.activation"
+ "com.apple.relevanced.AudioIntelligenceAvailabilityQueue"
+ "instantShazam"
```
