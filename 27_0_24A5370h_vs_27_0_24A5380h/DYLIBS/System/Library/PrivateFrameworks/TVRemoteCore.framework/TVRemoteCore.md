## TVRemoteCore

> `/System/Library/PrivateFrameworks/TVRemoteCore.framework/TVRemoteCore`

```diff

-  __TEXT.__text: 0x4834c
+  __TEXT.__text: 0x483e4
   __TEXT.__objc_methlist: 0x64d0
   __TEXT.__const: 0x2a0
   __TEXT.__oslogstring: 0x6b0e
-  __TEXT.__cstring: 0x3798
+  __TEXT.__cstring: 0x3784
   __TEXT.__gcc_except_tab: 0xafc
   __TEXT.__unwind_info: 0x1230
   __TEXT.__objc_stubs: 0x0

   __DATA_CONST.__objc_arraydata: 0x120
   __DATA_CONST.__got: 0x4f0
   __AUTH_CONST.__const: 0x480
-  __AUTH_CONST.__cfstring: 0x4ac0
+  __AUTH_CONST.__cfstring: 0x4aa0
   __AUTH_CONST.__objc_const: 0x9f88
   __AUTH_CONST.__objc_intobj: 0x288
   __AUTH_CONST.__objc_arrayobj: 0x60

   - /usr/lib/libobjc.A.dylib
   Functions: 2137
   Symbols:   7191
-  CStrings:  1899
+  CStrings:  1897
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__got : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_doubleobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH.__objc_data : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
Functions:
~ -[TVRCAnalytics logConnectionStatus:type:reason:] : 312 -> 304
~ -[TVRCDevice _deviceUpdatedState:] : 3740 -> 3884
~ -[TVRCDeviceState description] : 720 -> 716
~ -[TVRCDeviceState detailedDescription] : 748 -> 744
~ -[TVRCHIDSession _commandForButtonEvent:] : 100 -> 96
~ -[TVRCHIDTouchSession _invalidateWithCompletion:] : 436 -> 452
~ -[TVRCHIDTouchSession sendTouchEvent:completion:] : 584 -> 620
~ -[TVRCMediaEventsManager _captionSettingForButtonEvent:] : 100 -> 96
~ -[TVRCRapportMediaEventsManager _captionSettingForButtonEvent:] : 100 -> 96
~ -[TVRCRPCompanionLinkClientWrapper _updateAttentionState:] : 368 -> 360
~ -[TVRCRPCompanionLinkClientWrapper _commandForButtonEvent:] : 100 -> 96
~ ___63-[TVRCRPCompanionLinkClientWrapper _handleSideEffectsForEvent:]_block_invoke : 1456 -> 1452
CStrings:
- "ActivateScreenSaver"

```
