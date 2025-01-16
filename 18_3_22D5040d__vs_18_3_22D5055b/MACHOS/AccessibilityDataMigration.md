## AccessibilityDataMigration

> `/System/Library/DataClassMigrators/AccessibilityDataMigration.migrator/AccessibilityDataMigration`

```diff

-3148.7.14.1.0
-  __TEXT.__text: 0x858c
+3148.7.15.1.0
+  __TEXT.__text: 0x8720
   __TEXT.__auth_stubs: 0x5e0
-  __TEXT.__objc_stubs: 0x20a0
-  __TEXT.__objc_methlist: 0x368
+  __TEXT.__objc_stubs: 0x2180
+  __TEXT.__objc_methlist: 0x374
   __TEXT.__const: 0xb0
   __TEXT.__gcc_except_tab: 0x58
-  __TEXT.__cstring: 0x13aa
-  __TEXT.__oslogstring: 0x702
-  __TEXT.__objc_methname: 0x1ec7
+  __TEXT.__cstring: 0x13e8
+  __TEXT.__oslogstring: 0x73a
+  __TEXT.__objc_methname: 0x1f8c
   __TEXT.__objc_classname: 0x1a
   __TEXT.__objc_methtype: 0x44
   __TEXT.__unwind_info: 0x180
   __DATA_CONST.__auth_got: 0x300
-  __DATA_CONST.__got: 0x1e0
+  __DATA_CONST.__got: 0x1f0
   __DATA_CONST.__const: 0xb8
-  __DATA_CONST.__cfstring: 0x1340
+  __DATA_CONST.__cfstring: 0x1360
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_arraydata: 0x188
   __DATA_CONST.__objc_dictobj: 0x140
   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA.__objc_const: 0xd0
-  __DATA.__objc_selrefs: 0x880
+  __DATA.__objc_selrefs: 0x8b8
   __DATA.__objc_ivar: 0x4
   __DATA.__objc_data: 0x50
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 81
-  Symbols:   167
-  CStrings:  471
+  Functions: 82
+  Symbols:   169
+  CStrings:  480
 
Symbols:
+ _AXSDSettingsEventSourceDataMigrator
+ _OBJC_CLASS_$_AXSDSettingsEvent
CStrings:
+ "Sound Recognition was on but has no sounds, turning off"
+ "_AccessibilityMigration__TurnOffSoundRecognitionNoSounds_18.3"
+ "_turnOffSoundRecognitionIfNoSoundsEnabled"
+ "enabledKShotDetectorIdentifiers"
+ "enabledSoundDetectionTypes"
+ "initWithState:source:"
+ "registerSettingsEvent:"
+ "setSoundDetectionState:source:"
+ "soundDetectionState"

```
