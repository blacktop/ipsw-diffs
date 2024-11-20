## AccessibilitySettings

> `/System/Library/PreferenceBundles/AccessibilitySettings.bundle/AccessibilitySettings`

```diff

-1773.3.3.0.0
-  __TEXT.__text: 0x161c50
-  __TEXT.__auth_stubs: 0x4310
-  __TEXT.__objc_stubs: 0x225e0
+1773.3.5.0.0
+  __TEXT.__text: 0x161d34
+  __TEXT.__auth_stubs: 0x42f0
+  __TEXT.__objc_stubs: 0x22620
   __TEXT.__objc_methlist: 0x11c24
-  __TEXT.__const: 0x1a20
+  __TEXT.__const: 0x1a10
   __TEXT.__gcc_except_tab: 0x3284
-  __TEXT.__objc_methname: 0x30b81
-  __TEXT.__cstring: 0x1749c
+  __TEXT.__objc_methname: 0x30ba3
+  __TEXT.__cstring: 0x1748c
   __TEXT.__oslogstring: 0x379d
-  __TEXT.__objc_classname: 0x3f0b
+  __TEXT.__objc_classname: 0x3f0c
   __TEXT.__objc_methtype: 0x5dae
   __TEXT.__dlopen_cstrs: 0x236
   __TEXT.__ustring: 0x2e

   __TEXT.__swift5_capture: 0x14c
   __TEXT.__unwind_info: 0x5110
   __TEXT.__eh_frame: 0x170
-  __DATA_CONST.__auth_got: 0x2198
+  __DATA_CONST.__auth_got: 0x2188
   __DATA_CONST.__got: 0x2158
   __DATA_CONST.__auth_ptr: 0x4b0
   __DATA_CONST.__const: 0x4ba8

   __DATA_CONST.__objc_floatobj: 0x20
   __DATA_CONST.__objc_dictobj: 0xa78
   __DATA.__objc_const: 0x1ed18
-  __DATA.__objc_selrefs: 0xb4e8
+  __DATA.__objc_selrefs: 0xb4f0
   __DATA.__objc_ivar: 0xd54
   __DATA.__objc_data: 0x8c60
   __DATA.__data: 0x2b52

   - /usr/lib/swift/libswiftunistd.dylib
   Functions: 7689
   Symbols:   18305
-  CStrings:  12543
+  CStrings:  12544
 
Symbols:
+ -[VoiceOverDuckingSliderCell _currentDuckingValue]
+ -[VoiceOverDuckingSliderCell _setCurrentDuckingValue:]
+ -[VoiceOverDuckingSliderCell _updateRightLabelWithValue:]
+ -[VoiceOverDuckingSliderCell accessibilityDecrement]
+ -[VoiceOverDuckingSliderCell accessibilityIncrementOrDecrement:]
+ -[VoiceOverDuckingSliderCell accessibilityIncrement]
+ -[VoiceOverDuckingSliderCell accessibilityLabel]
+ -[VoiceOverDuckingSliderCell accessibilityValue]
+ -[VoiceOverDuckingSliderCell handleSliderBeingDragged:]
+ -[VoiceOverDuckingSliderCell handleSliderDidFinishDrag:]
+ -[VoiceOverDuckingSliderCell initWithStyle:reuseIdentifier:specifier:]
+ -[VoiceOverDuckingSliderCell initialValue]
+ -[VoiceOverDuckingSliderCell maximumValue]
+ -[VoiceOverDuckingSliderCell minimumValue]
+ _OBJC_CLASS_$_VoiceOverDuckingSliderCell
+ _OBJC_METACLASS_$_VoiceOverDuckingSliderCell
+ __OBJC_$_INSTANCE_METHODS_VoiceOverDuckingSliderCell
+ __OBJC_CLASS_RO_$_VoiceOverDuckingSliderCell
+ __OBJC_METACLASS_RO_$_VoiceOverDuckingSliderCell
+ ___57-[VoiceOverDuckingSliderCell _updateRightLabelWithValue:]_block_invoke
+ _objc_msgSend$_currentDuckingValue
+ _objc_msgSend$_setCurrentDuckingValue:
+ _objc_msgSend$setVoiceOverMediaDuckingAmount:
+ _objc_msgSend$voiceOverMediaDuckingAmount
- -[VoiceOverVolumeSliderCell _currentVolumeValue]
- -[VoiceOverVolumeSliderCell _setCurrentVolumeValue:]
- -[VoiceOverVolumeSliderCell _updateRightLabelWithValue:]
- -[VoiceOverVolumeSliderCell accessibilityDecrement]
- -[VoiceOverVolumeSliderCell accessibilityIncrementOrDecrement:]
- -[VoiceOverVolumeSliderCell accessibilityIncrement]
- -[VoiceOverVolumeSliderCell accessibilityLabel]
- -[VoiceOverVolumeSliderCell accessibilityValue]
- -[VoiceOverVolumeSliderCell handleSliderBeingDragged:]
- -[VoiceOverVolumeSliderCell handleSliderDidFinishDrag:]
- -[VoiceOverVolumeSliderCell initWithStyle:reuseIdentifier:specifier:]
- -[VoiceOverVolumeSliderCell initialValue]
- -[VoiceOverVolumeSliderCell maximumValue]
- -[VoiceOverVolumeSliderCell minimumValue]
- _OBJC_CLASS_$_VoiceOverVolumeSliderCell
- _OBJC_METACLASS_$_VoiceOverVolumeSliderCell
- _VOSVoiceOverSetVolume
- _VOSVoiceOverVolume
- __OBJC_$_INSTANCE_METHODS_VoiceOverVolumeSliderCell
- __OBJC_CLASS_RO_$_VoiceOverVolumeSliderCell
- __OBJC_METACLASS_RO_$_VoiceOverVolumeSliderCell
- ___56-[VoiceOverVolumeSliderCell _updateRightLabelWithValue:]_block_invoke
- _objc_msgSend$_currentVolumeValue
- _objc_msgSend$_setCurrentVolumeValue:
CStrings:
+ "DUCKING_AMOUNT"
+ "VoiceOverDuckingSliderCell"
+ "_currentDuckingValue"
+ "_setCurrentDuckingValue:"
+ "setVoiceOverMediaDuckingAmount:"
+ "voiceOverMediaDuckingAmount"
- "VOICEOVER_SPEECH_VOLUME"
- "VoiceOverVolumeSliderCell"
- "_currentVolumeValue"
- "_setCurrentVolumeValue:"
- "voiceOverMediaDuckingVolume"

```
