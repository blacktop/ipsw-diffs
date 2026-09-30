## MediaControls

> `/System/Library/PrivateFrameworks/MediaControls.framework/MediaControls`

```diff

-4026.200.11.0.0
-  __TEXT.__text: 0x217f30
-  __TEXT.__objc_methlist: 0x15d94
-  __TEXT.__cstring: 0x6f64
+4026.200.15.0.0
+  __TEXT.__text: 0x218310
+  __TEXT.__objc_methlist: 0x15de4
+  __TEXT.__cstring: 0x6f74
   __TEXT.__ustring: 0x28
-  __TEXT.__const: 0xbcd4
+  __TEXT.__const: 0xbd04
   __TEXT.__gcc_except_tab: 0x1598
   __TEXT.__oslogstring: 0x86d9
   __TEXT.__dlopen_cstrs: 0x64

   __TEXT.__swift_as_ret: 0x34
   __TEXT.__swift_as_cont: 0x6c
   __TEXT.__swift5_assocty: 0x390
-  __TEXT.__unwind_info: 0xaa10
+  __TEXT.__unwind_info: 0xaa18
   __TEXT.__eh_frame: 0x18b8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x3080
+  __DATA_CONST.__const: 0x3090
   __DATA_CONST.__objc_classlist: 0x9b8
   __DATA_CONST.__objc_catlist: 0xa8
   __DATA_CONST.__objc_protolist: 0x480
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa7c8
+  __DATA_CONST.__objc_selrefs: 0xa7e8
   __DATA_CONST.__objc_protorefs: 0xa8
   __DATA_CONST.__objc_superrefs: 0x608
   __DATA_CONST.__objc_arraydata: 0x1e8
   __DATA_CONST.__got: 0x18a8
   __AUTH_CONST.__const: 0xab98
-  __AUTH_CONST.__cfstring: 0x51e0
-  __AUTH_CONST.__objc_const: 0x44780
+  __AUTH_CONST.__cfstring: 0x5200
+  __AUTH_CONST.__objc_const: 0x44848
   __AUTH_CONST.__objc_intobj: 0x2b8
   __AUTH_CONST.__objc_arrayobj: 0x138
   __AUTH_CONST.__objc_doubleobj: 0xf0
   __AUTH_CONST.__objc_dictobj: 0x140
-  __AUTH_CONST.__auth_got: 0x2028
-  __AUTH.__objc_data: 0x3880
-  __AUTH.__data: 0x1238
+  __AUTH_CONST.__auth_got: 0x2030
+  __AUTH.__objc_data: 0x82a8
+  __AUTH.__data: 0x34d8
   __DATA.__objc_ivar: 0x18d4
-  __DATA.__data: 0x4218
-  __DATA.__common: 0x8b0
-  __DATA_DIRTY.__objc_data: 0x72c8
-  __DATA_DIRTY.__data: 0x33b8
-  __DATA_DIRTY.__bss: 0x28a0
-  __DATA_DIRTY.__common: 0xa00
+  __DATA.__data: 0x4d68
+  __DATA.__common: 0x1250
+  __DATA_DIRTY.__objc_data: 0x28a0
+  __DATA_DIRTY.__data: 0x5b8
+  __DATA_DIRTY.__bss: 0x3f0
+  __DATA_DIRTY.__common: 0x60
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/AVRouting.framework/AVRouting

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 14458
-  Symbols:   17647
-  CStrings:  1623
+  Functions: 14463
+  Symbols:   17664
+  CStrings:  1624
 
Symbols:
+ +[UIFont(MRUDefaults) mru_ambientSubtitleFontForAxis:]
+ +[UIFont(MRUDefaults) mru_ambientTimeFontForAxis:]
+ +[UIFont(MRUDefaults) mru_ambientTitleFontForAxis:]
+ -[MRUAmbientNowPlayingView prefersAltLayout]
+ -[MRUAmbientNowPlayingVolumeControlsView maximumValueViewStyleForSlider:]
+ -[MRUCAPackageView(MRUVisualStylingProviderAdditions) mru_applyBlendColor:alpha:]
+ -[MRUVisualStylingProvider applyBlendStyle:toView:traitCollection:]
+ -[UIView(MRUVisualStylingProviderAdditions) mru_applyBlendColor:alpha:]
+ _CGColorGetAlpha
+ _MRUAmbientNowPlayingSliderStretchLimit
+ _MRUAmbientNowPlayingTimeControlsBottomInsetForLayoutAxis
+ _MRUAmbientNowPlayingVerticalLayoutSliderToTimeLabelSpacing
+ _MRUAmbientNowPlayingVerticalLayoutTimeControlsBottomInset
+ _MRUAmbientNowPlayingVerticalLayoutTransportControlsButtonSize
+ _MRUAmbientNowPlayingVerticalLayoutTransportControlsCenterOffset
+ _MRUAmbientNowPlayingVerticalLayoutTransportControlsPackageScale
+ _objc_msgSend$applyBlendStyle:toView:traitCollection:
+ _objc_msgSend$maximumValueViewStyleForSlider:
+ _objc_msgSend$minimumValueViewStyleForSlider:
+ _objc_msgSend$mru_ambientSubtitleFontForAxis:
+ _objc_msgSend$mru_ambientTimeFontForAxis:
+ _objc_msgSend$mru_ambientTitleFontForAxis:
+ _objc_msgSend$mru_applyBlendColor:alpha:
+ _objc_msgSend$prefersAltLayout
- +[UIFont(MRUDefaults) mru_ambientSubtitleFont]
- +[UIFont(MRUDefaults) mru_ambientTimeFont]
- +[UIFont(MRUDefaults) mru_ambientTitleFont]
- -[MRUNowPlayingTimeControlsView timeLabelsAlpha]
- _objc_msgSend$mru_ambientSubtitleFont
- _objc_msgSend$mru_ambientTimeFont
- _objc_msgSend$mru_ambientTitleFont
CStrings:
+ "AmbientVertical"
```
