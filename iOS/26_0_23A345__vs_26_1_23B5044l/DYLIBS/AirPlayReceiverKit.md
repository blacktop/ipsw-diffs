## AirPlayReceiverKit

> `/System/Library/PrivateFrameworks/AirPlayReceiverKit.framework/AirPlayReceiverKit`

```diff

-890.79.1.2.0
-  __TEXT.__text: 0x24218
+920.5.1.11.1
+  __TEXT.__text: 0x2446c
   __TEXT.__auth_stubs: 0xd10
   __TEXT.__objc_methlist: 0x13c4
-  __TEXT.__cstring: 0x869c
+  __TEXT.__cstring: 0x8792
   __TEXT.__const: 0x52
   __TEXT.__gcc_except_tab: 0x47c
-  __TEXT.__unwind_info: 0xaa8
+  __TEXT.__unwind_info: 0xab0
   __TEXT.__objc_classname: 0x248
   __TEXT.__objc_methname: 0x4fac
   __TEXT.__objc_methtype: 0x112c
   __TEXT.__objc_stubs: 0x35e0
-  __DATA_CONST.__got: 0x7d0
-  __DATA_CONST.__const: 0x888
+  __DATA_CONST.__got: 0x7d8
+  __DATA_CONST.__const: 0x890
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_superrefs: 0x48
   __AUTH_CONST.__auth_got: 0x698
   __AUTH_CONST.__const: 0x390
-  __AUTH_CONST.__cfstring: 0x17e0
+  __AUTH_CONST.__cfstring: 0x1820
   __AUTH_CONST.__objc_const: 0x21a8
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0x370
   __DATA.__objc_ivar: 0x284
   __DATA.__data: 0x500
-  __DATA.__bss: 0x48
+  __DATA.__bss: 0x4c
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7E9C2D4E-948D-364B-A3B1-C1FB21F7EC3F
-  Functions: 896
-  Symbols:   3130
-  CStrings:  1960
+  UUID: 7A5B58AA-3A9D-3E8E-BB00-4158BDB30D06
+  Functions: 898
+  Symbols:   3137
+  CStrings:  1967
 
Symbols:
+ -[APRKMediaPlayer _insertPlayQueueItemWithDictionary:].cold.9
+ GCC_except_table92
+ _APRKAlternateBonjourBrowsingEnabledNotification
+ ___73-[APRKStreamRenderingManager _startReceiverServerWithSupportedModesMask:]_block_invoke_3
+ ___73-[APRKStreamRenderingManager _startReceiverServerWithSupportedModesMask:]_block_invoke_3.cold.1
+ ___block_literal_global.125
+ __startReceiverServerWithSupportedModesMask:.notifyDisabledToken
+ __startReceiverServerWithSupportedModesMask:.notifyEnabledToken
+ _kFigEndpointPlaybackSessionKey_SupportsIntegratedTimeline
- +[APRKStreamRenderingManager setListeningForAlternateBonjourBrowsing:].cold.2
- GCC_except_table91
- __startReceiverServerWithSupportedModesMask:.notifyOnceToken
Functions:
~ -[APRKMediaPlayer _insertPlayQueueItemWithDictionary:] : 2248 -> 2388
~ +[APRKStreamRenderingManager setListeningForAlternateBonjourBrowsing:] : 224 -> 364
~ ___73-[APRKStreamRenderingManager _startReceiverServerWithSupportedModesMask:]_block_invoke : 176 -> 280
+ ___73-[APRKStreamRenderingManager _startReceiverServerWithSupportedModesMask:]_block_invoke_3
+ -[APRKMediaPlayer _insertPlayQueueItemWithDictionary:].cold.9
- +[APRKStreamRenderingManager setListeningForAlternateBonjourBrowsing:].cold.2
+ ___73-[APRKStreamRenderingManager _startReceiverServerWithSupportedModesMask:]_block_invoke_3.cold.1
CStrings:
+ "-[APRKStreamRenderingManager _startReceiverServerWithSupportedModesMask:]_block_invoke_3"
+ "920.5.1.11.1"
+ "APRKAlternateBonjourBrowsingEnabled"
+ "APRKAlternateBonjourBrowsingNotificationQueue"
+ "SupportsIntegratedTimeline"
+ "com.apple.airplay.alternatebonjourbrowsingenabled"
+ "integratedTimeline not supported on this platform"
- "890.79.1.2"
- "APRKAlternateBonjourBrowsingDisabledNotificationQueue"

```
