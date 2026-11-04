## AirPlayReceiverKit

> `/System/Library/PrivateFrameworks/AirPlayReceiverKit.framework/AirPlayReceiverKit`

```diff

-1005.13.1.1.0
-  __TEXT.__text: 0x25ec4
+1015.5.1.0.0
+  __TEXT.__text: 0x26230
   __TEXT.__objc_methlist: 0x1464
-  __TEXT.__cstring: 0x8dc3
+  __TEXT.__cstring: 0x8ea1
   __TEXT.__const: 0x82
   __TEXT.__oslogstring: 0x424
-  __TEXT.__gcc_except_tab: 0x774
+  __TEXT.__gcc_except_tab: 0x7e0
   __TEXT.__unwind_info: 0xe70
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1358
+  __DATA_CONST.__objc_selrefs: 0x1368
   __DATA_CONST.__objc_superrefs: 0x48
-  __DATA_CONST.__got: 0x880
+  __DATA_CONST.__got: 0x898
   __AUTH_CONST.__const: 0x390
   __AUTH_CONST.__cfstring: 0x18e0
-  __AUTH_CONST.__objc_const: 0x22b8
+  __AUTH_CONST.__objc_const: 0x22d8
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x370
-  __DATA.__objc_ivar: 0x29c
+  __DATA.__objc_ivar: 0x2a0
   __DATA.__data: 0x560
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 947
-  Symbols:   1573
-  CStrings:  859
+  Functions: 948
+  Symbols:   1577
+  CStrings:  864
 
Symbols:
+ _OBJC_IVAR_$_APRKMediaPlayer._isCurrentInterstitialEventIDAwaitingEvents
+ _kFigEndPointPlaybackSessionKey_LoudnessInfo
+ _kFigEndpointPlaybackSessionProxiedProperty_LoudnessInfo
+ _kFigEndpointPlaybackSessionProxiedProperty_PrefersAudioVideoVariants
Functions:
~ -[APRKMediaPlayer _insertPlayQueueItemWithDictionary:] : 2700 -> 2884
~ -[APRKMediaPlayer _setPropertyWithDictionary:] : 4180 -> 4788
~ -[APRKStreamRenderer videoFrameSize] : 252 -> 296
~ -[APRKMediaPlayer _insertPlayQueueItemWithDictionary:].cold.1 : 56 -> 52
~ -[APRKMediaPlayer _insertPlayQueueItemWithDictionary:].cold.3 : 56 -> 52
~ -[APRKMediaPlayer _insertPlayQueueItemWithDictionary:].cold.6 : 80 -> 76
~ -[APRKMediaPlayer _insertPlayQueueItemWithDictionary:].cold.8 : 40 -> 52
+ -[APRKMediaPlayer _insertPlayQueueItemWithDictionary:].cold.10
CStrings:
+ "1015.5.1"
+ "Applying deferred current interstitial event %@"
+ "Current interstitial event %@ arrived before interstitialEvents; deferring"
+ "LoudnessInfo property set to %@"
+ "LoudnessInfo set to %@"
+ "PrefersAudioVideoVariants property set to %d."
+ "Q\xf0\xc1"
- "1005.13.1.1"
- "Q\xf0\xb1"
```
