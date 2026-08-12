## TVRemoteUI

> `/System/Library/PrivateFrameworks/TVRemoteUI.framework/TVRemoteUI`

```diff

-627.0.19.0.0
-  __TEXT.__text: 0xd413c
-  __TEXT.__objc_methlist: 0xbc24
+627.0.28.0.0
+  __TEXT.__text: 0xd4628
+  __TEXT.__objc_methlist: 0xbc6c
   __TEXT.__const: 0x2624
-  __TEXT.__cstring: 0x4df1
-  __TEXT.__gcc_except_tab: 0x1d54
-  __TEXT.__oslogstring: 0x5b56
+  __TEXT.__cstring: 0x4de1
+  __TEXT.__gcc_except_tab: 0x1d64
+  __TEXT.__oslogstring: 0x5c26
   __TEXT.__ustring: 0x34
   __TEXT.__dlopen_cstrs: 0xa2
   __TEXT.__constg_swiftt: 0x2e90

   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1908
+  __DATA_CONST.__const: 0x1930
   __DATA_CONST.__objc_classlist: 0x5d8
   __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_protolist: 0x1f0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6bf0
+  __DATA_CONST.__objc_selrefs: 0x6c20
   __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_superrefs: 0x398
   __DATA_CONST.__objc_arraydata: 0x118
   __DATA_CONST.__got: 0xe28
   __AUTH_CONST.__const: 0x2fd0
-  __AUTH_CONST.__cfstring: 0x3900
-  __AUTH_CONST.__objc_const: 0x156c0
+  __AUTH_CONST.__cfstring: 0x38c0
+  __AUTH_CONST.__objc_const: 0x15710
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x240
   __AUTH_CONST.__objc_doubleobj: 0x90

   __AUTH_CONST.__auth_got: 0xf20
   __AUTH.__objc_data: 0x6ab0
   __AUTH.__data: 0x670
-  __DATA.__objc_ivar: 0xbbc
+  __DATA.__objc_ivar: 0xbc4
   __DATA.__data: 0x2590
   __DATA.__bss: 0x2790
   __DATA.__common: 0x4c0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 4931
-  Symbols:   9824
-  CStrings:  1247
+  Functions: 4938
+  Symbols:   9838
+  CStrings:  1248
 
Symbols:
+ -[TVRUIDirectionalControlView didMoveToSuperview]
+ -[TVRUIHintsViewController _hasUserIntentButtonInfo]
+ -[TVRUIHintsViewController _hasVolumeButtonInfo]
+ -[TVRUIResizabilityLayoutManager _occlusionRegionFrame]
+ -[TVRUIResizabilityLayoutManager setShouldAnimateRenderFormatChange:]
+ -[TVRUIResizabilityLayoutManager shouldAnimateRenderFormatChange]
+ GCC_except_table120
+ GCC_except_table188
+ GCC_except_table60
+ GCC_except_table83
+ _OBJC_IVAR_$_TVRUIResizabilityLayoutManager._hasComputedFormat
+ _OBJC_IVAR_$_TVRUIResizabilityLayoutManager._shouldAnimateRenderFormatChange
+ ___51-[TVRUIRemoteViewController viewWillLayoutSubviews]_block_invoke
+ ___block_descriptor_209_e8_32s_e5_v8?0ls32l8
+ _objc_msgSend$_hasUserIntentButtonInfo
+ _objc_msgSend$_hasVolumeButtonInfo
+ _objc_msgSend$_occlusionRegionFrame
+ _objc_msgSend$hostingView
+ _objc_msgSend$setContentInsetsReference:
+ _objc_msgSend$shouldAnimateRenderFormatChange
- GCC_except_table187
- GCC_except_table59
- GCC_except_table66
- GCC_except_table82
- _objc_msgSend$_shouldReverseLayoutDirection
- _objc_msgSend$device:hasCaptionsEnabled:
CStrings:
+ "#directional - toggleControlState mediaControlsAreVisible:%{bool}d landscape:%{bool}d compactWindow:%{bool}d"
+ "No user-intent button geometry for this device, suppressing Siri hint"
+ "No volume-button geometry for this device, suppressing volume hint"
+ "Not starting deviceQueryThresholdTimer - already have an active device"
- "#directional - toggleControlState mediaControlsAreVisible:%{bool}d small:%{bool}d landscape:%{bool}d"
- "alwaysOnCaptions"
- "captions"
```
