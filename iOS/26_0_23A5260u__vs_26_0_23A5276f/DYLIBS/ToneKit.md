## ToneKit

> `/System/Library/PrivateFrameworks/ToneKit.framework/ToneKit`

```diff

-651.0.0.0.0
-  __TEXT.__text: 0x26024
+653.0.0.0.0
+  __TEXT.__text: 0x26100
   __TEXT.__auth_stubs: 0x6c0
   __TEXT.__objc_methlist: 0x33dc
   __TEXT.__const: 0x100
   __TEXT.__gcc_except_tab: 0x21c
-  __TEXT.__cstring: 0x1737
-  __TEXT.__oslogstring: 0xa57
+  __TEXT.__cstring: 0x173f
+  __TEXT.__oslogstring: 0xaa4
   __TEXT.__ustring: 0x9c
   __TEXT.__dlopen_cstrs: 0xb7
   __TEXT.__unwind_info: 0xb10
   __TEXT.__objc_classname: 0x6d7
-  __TEXT.__objc_methname: 0xb00a
-  __TEXT.__objc_methtype: 0x1b37
-  __TEXT.__objc_stubs: 0x80e0
+  __TEXT.__objc_methname: 0xb065
+  __TEXT.__objc_methtype: 0x1b42
+  __TEXT.__objc_stubs: 0x8160
   __DATA_CONST.__got: 0x478
   __DATA_CONST.__const: 0x5b8
   __DATA_CONST.__objc_classlist: 0x118
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2560
+  __DATA_CONST.__objc_selrefs: 0x2570
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x100
   __AUTH_CONST.__auth_got: 0x370
   __AUTH_CONST.__const: 0x120
-  __AUTH_CONST.__cfstring: 0x1200
+  __AUTH_CONST.__cfstring: 0x1220
   __AUTH_CONST.__objc_const: 0x5190
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_intobj: 0x18

   - /System/Library/PrivateFrameworks/ToneLibrary.framework/ToneLibrary
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: FBBFD12E-4BDB-35D1-8D95-CC9C4E8BAC78
+  UUID: 9128A07C-0752-31D4-A735-D4C1592183E2
   Functions: 1028
-  Symbols:   4064
-  CStrings:  2258
+  Symbols:   4068
+  CStrings:  2263
 
Symbols:
+ _OBJC_CLASS_$_MPMusicPlayerApplicationController
+ _objc_msgSend$_toneIdentifierForMediaLibraryItemIdentifier:
+ _objc_msgSend$_toneManager
+ _objc_msgSend$initWithClientIdentifier:queue:
+ _objc_msgSend$selectedMediaIdentifier
+ _objc_msgSend$setDisableAutomaticCanBeNowPlaying:
- _OBJC_CLASS_$_MPMusicPlayerController
- _objc_msgSend$applicationMusicPlayer
Functions:
~ -[TKTonePickerViewController _musicPlayer] : 96 -> 124
~ -[TKTonePickerViewController tonePickerControllerRequestsPresentingVibrationPicker:] : 568 -> 760
CStrings:
+ "@\"MPMusicPlayerApplicationController\""
+ "Presenting vibration picker for corresponding tone identifier: \"%{public}@\"."
+ "ToneKit"
+ "_toneIdentifierForMediaLibraryItemIdentifier:"
+ "initWithClientIdentifier:queue:"
+ "setDisableAutomaticCanBeNowPlaying:"
- "@\"MPMusicPlayerController\""
- "applicationMusicPlayer"

```
