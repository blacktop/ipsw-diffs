## AssistantBridgeSettings

> `/System/Library/NanoPreferenceBundles/General/AssistantBridgeSettings.bundle/AssistantBridgeSettings`

```diff

-3405.30.3.11.5
-  __TEXT.__text: 0x6d74
-  __TEXT.__auth_stubs: 0x440
-  __TEXT.__objc_stubs: 0x14a0
-  __TEXT.__objc_methlist: 0x664
+3500.74.4.1.2
+  __TEXT.__text: 0x803c
+  __TEXT.__auth_stubs: 0x470
+  __TEXT.__objc_stubs: 0x18e0
+  __TEXT.__objc_methlist: 0x79c
   __TEXT.__const: 0x30
   __TEXT.__gcc_except_tab: 0x9c
-  __TEXT.__objc_methname: 0x1a77
-  __TEXT.__cstring: 0xe41
+  __TEXT.__objc_methname: 0x1f9b
+  __TEXT.__cstring: 0x1068
   __TEXT.__oslogstring: 0x367
   __TEXT.__ustring: 0x4
-  __TEXT.__objc_classname: 0x13e
-  __TEXT.__objc_methtype: 0x2d4
+  __TEXT.__objc_classname: 0x174
+  __TEXT.__objc_methtype: 0x30f
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__unwind_info: 0x260
-  __DATA_CONST.__auth_got: 0x230
-  __DATA_CONST.__got: 0x1c0
-  __DATA_CONST.__const: 0x3a0
-  __DATA_CONST.__cfstring: 0xac0
-  __DATA_CONST.__objc_classlist: 0x40
+  __TEXT.__unwind_info: 0x2a8
+  __DATA_CONST.__auth_got: 0x248
+  __DATA_CONST.__got: 0x1c8
+  __DATA_CONST.__const: 0x3f8
+  __DATA_CONST.__cfstring: 0xca0
+  __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x38
+  __DATA_CONST.__objc_superrefs: 0x40
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x8f0
-  __DATA.__objc_selrefs: 0x700
-  __DATA.__objc_ivar: 0x4c
-  __DATA.__objc_data: 0x280
+  __DATA.__objc_const: 0xa48
+  __DATA.__objc_selrefs: 0x828
+  __DATA.__objc_ivar: 0x5c
+  __DATA.__objc_data: 0x2d0
   __DATA.__data: 0xc0
   __DATA.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/NanoResourceGrabber.framework/NanoResourceGrabber
   - /System/Library/PrivateFrameworks/OnBoardingKit.framework/OnBoardingKit
   - /System/Library/PrivateFrameworks/Preferences.framework/Preferences
+  - /System/Library/PrivateFrameworks/RelevanceServicesCompanion.framework/RelevanceServicesCompanion
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/VoiceTrigger.framework/VoiceTrigger
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 166EDC1C-1E1B-31EF-92CA-888A34178C6E
-  Functions: 151
-  Symbols:   153
-  CStrings:  515
+  UUID: D9415D2D-F045-388D-BB17-6241001DDD56
+  Functions: 181
+  Symbols:   159
+  CStrings:  596
 
Symbols:
+ _CFNotificationCenterAddObserver
+ _CFNotificationCenterRemoveEveryObserver
+ _OBJC_CLASS_$_AssistantBridgeConsiderateVolumeProfileController
+ _OBJC_CLASS_$_RSConsiderateVolumeSettingsController
+ _OBJC_METACLASS_$_AssistantBridgeConsiderateVolumeProfileController
+ __os_feature_enabled_impl
CStrings:
+ "2"
+ "27EC88C0-A142-4C22-BCEB-4B6A90B5184F"
+ "@\"NSMutableArray\""
+ "@\"RSConsiderateVolumeSettingsController\""
+ "AssistantBridgeConsiderateVolumeProfileController"
+ "AssistantConsiderateVolumeProfile"
+ "B32@?0@\"PSSpecifier\"8Q16^B24"
+ "CONSIDERATE_VOLUME_FOOTER"
+ "CONSIDERATE_VOLUME_GROUP_ID"
+ "CONSIDERATE_VOLUME_PROFILE_DEFAULT"
+ "CONSIDERATE_VOLUME_PROFILE_DEFAULT_ID"
+ "CONSIDERATE_VOLUME_PROFILE_GROUP_ID"
+ "CONSIDERATE_VOLUME_PROFILE_ID"
+ "CONSIDERATE_VOLUME_PROFILE_LOUDER"
+ "CONSIDERATE_VOLUME_PROFILE_LOUDER_ID"
+ "CONSIDERATE_VOLUME_PROFILE_QUIETER"
+ "CONSIDERATE_VOLUME_PROFILE_QUIETER_ID"
+ "CONSIDERATE_VOLUME_SLIDER_ID"
+ "CONSIDERATE_VOLUME_SWITCH_ID"
+ "RelevancePlatform"
+ "T@\"NSMutableArray\",&,N,V_originalConsiderateVolumeSpecifiers"
+ "T@\"RSConsiderateVolumeSettingsController\",&,N,V_considerateVolumeSettingsController"
+ "T@\"RSConsiderateVolumeSettingsController\",&,N,V_settingsController"
+ "VOICE_VOLUME_FOOTER"
+ "_considerateVolumeSettingsController"
+ "_originalConsiderateVolumeSpecifiers"
+ "_settingsController"
+ "_siriConsiderateVolumeSupported"
+ "arrayWithArray:"
+ "beginUpdates"
+ "considerateVolume"
+ "considerateVolumeProfileValue"
+ "considerateVolumeSettingsController"
+ "endUpdates"
+ "getUserProfileForCategory:"
+ "indexOfSpecifier:"
+ "indexOfSpecifierID:"
+ "indexesOfObjectsPassingTest:"
+ "insertObject:atIndex:"
+ "insertSpecifier:atIndex:animated:"
+ "integerValue"
+ "isEnabledForCategory:"
+ "numberWithInteger:"
+ "objectsAtIndexes:"
+ "originalConsiderateVolumeSpecifiers"
+ "prefsDidChangeNotification"
+ "reloadSpecifierID:"
+ "reloadSpecifierID:animated:"
+ "removeSpecifierID:"
+ "removeSpecifierID:animated:"
+ "setConsiderateVolumeSettingsController:"
+ "setEnabled:forCategory:"
+ "setOriginalConsiderateVolumeSpecifiers:"
+ "setSelectedSpecifier:animated:"
+ "setSelectedSpecifier:settings:animated:"
+ "setSettingsController:"
+ "setUseConsiderateVolume:"
+ "setUserProfile:forCategory:"
+ "setUserProfileFromSpecifierID:"
+ "settingsController"
+ "specifierForSelectedPhraseTypeInSettings:"
+ "updateSpecifiers:forConsiderateVolumeEnabled:"
+ "updateSpecifiersForConsiderateVolumeEnabled:"
+ "useConsiderateVolume"
+ "userProfile"
+ "watchHasConsiderateVolume"

```
