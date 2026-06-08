## AirPlaySenderService

> `/System/Library/PrivateFrameworks/AirPlaySenderKit.framework/XPCServices/AirPlaySenderService.xpc/AirPlaySenderService`

```diff

-950.7.1.0.0
-  __TEXT.__text: 0x84f4
-  __TEXT.__auth_stubs: 0xae0
-  __TEXT.__objc_stubs: 0x240
-  __TEXT.__objc_methlist: 0xb0
+980.58.1.11.1
+  __TEXT.__text: 0x9764
+  __TEXT.__auth_stubs: 0xb80
+  __TEXT.__objc_stubs: 0x280
+  __TEXT.__objc_methlist: 0xc8
   __TEXT.__const: 0x78
-  __TEXT.__cstring: 0x1eff
+  __TEXT.__cstring: 0x20e6
   __TEXT.__gcc_except_tab: 0x7c
-  __TEXT.__objc_methname: 0x1ef
-  __TEXT.__objc_classname: 0x15
+  __TEXT.__objc_methname: 0x22b
+  __TEXT.__objc_classname: 0x12
   __TEXT.__objc_methtype: 0xa1
-  __TEXT.__unwind_info: 0x238
-  __DATA_CONST.__auth_got: 0x580
-  __DATA_CONST.__got: 0x1a0
-  __DATA_CONST.__const: 0x6f0
-  __DATA_CONST.__cfstring: 0xe0
+  __TEXT.__unwind_info: 0x278
+  __DATA_CONST.__const: 0x760
+  __DATA_CONST.__cfstring: 0x140
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
+  __DATA_CONST.__auth_got: 0x5d0
+  __DATA_CONST.__got: 0x1c8
   __DATA.__objc_const: 0x138
-  __DATA.__objc_selrefs: 0xa8
+  __DATA.__objc_selrefs: 0xb8
   __DATA.__objc_ivar: 0x14
   __DATA.__objc_data: 0x50
-  __DATA.__data: 0x110
+  __DATA.__data: 0x128
   __DATA.__bss: 0x98
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 260D694C-EE82-3E81-8C35-58D68E5602A1
-  Functions: 253
-  Symbols:   238
-  CStrings:  240
+  UUID: 8D79ADC5-AAC2-3A3B-9C94-A3E8904D8D81
+  Functions: 290
+  Symbols:   253
+  CStrings:  259
 
Symbols:
+ _APSLogUtilsGetSharedLogCategory
+ _CFDictionaryGetDouble
+ _CFDictionarySetDouble
+ _CMTimeMakeWithSeconds
+ _FigEndpointManagerGetCMBaseObject
+ _FigEndpointPlaybackSessionGetCMBaseObject
+ __FigIsNotCurrentDispatchQueue
+ _kAPEndpointCreationOption_SenderSessionFactory
+ _kAPEndpointManagerProperty_SenderSessionFactory
+ _kFigEndpointPlaybackSessionKey_ContentLocation
+ _kFigEndpointPlaybackSessionKey_Rate
+ _kFigEndpointPlaybackSessionKey_UUID
+ _malloc_type_malloc
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x8
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
- _objc_retain_x22
CStrings:
+ "### [%{ptr}] media sender: get playback info timed out\n"
+ "-[APSKServerSession performPlaybackActionFromXPCParams:]"
+ "-[APSKServerSession setPlaybackInfoInReply:]"
+ "APMediaSenderPerformPlaybackAction_block_invoke"
+ "CFDictionaryRef sender_copyPlaybackInfoInternal(APMediaSenderRef)"
+ "MediaURL"
+ "Not running on expected queue at %s:%d"
+ "OSStatus createEndpointForNetworkAddress(APMediaSenderRef, CFStringRef, FigEndpointRef *)"
+ "OSStatus createEndpointForNetworkAddress(APMediaSenderRef, CFStringRef, FigEndpointRef *)_block_invoke"
+ "PlaybackRate"
+ "SeekTime"
+ "performPlaybackActionFromXPCParams:"
+ "playbackAction"
+ "playbackInfo"
+ "playbackInfoCompletionCallback"
+ "playbackParams"
+ "sender_copyPlaybackInfoInternal"
+ "setPlaybackInfoInReply:"
- "OSStatus createEndpointForNetworkAddress(CFStringRef, FigEndpointRef *)"
- "OSStatus createEndpointForNetworkAddress(CFStringRef, FigEndpointRef *)_block_invoke"

```
