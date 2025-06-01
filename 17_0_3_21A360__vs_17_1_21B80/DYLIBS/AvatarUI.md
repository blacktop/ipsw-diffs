## AvatarUI

> `/System/Library/PrivateFrameworks/AvatarUI.framework/AvatarUI`

```diff

-333.6.0.0.0
-  __TEXT.__text: 0xbc058
-  __TEXT.__auth_stubs: 0xde0
-  __TEXT.__objc_methlist: 0x10320
+337.0.0.0.0
+  __TEXT.__text: 0xbc090
+  __TEXT.__auth_stubs: 0xe00
+  __TEXT.__objc_methlist: 0x102e0
   __TEXT.__const: 0x3d8
   __TEXT.__cstring: 0x40eb
   __TEXT.__gcc_except_tab: 0x12d4
   __TEXT.__dlopen_cstrs: 0xb0
   __TEXT.__oslogstring: 0x47
-  __TEXT.__unwind_info: 0x387c
-  __TEXT.__objc_classname: 0x2bd1
-  __TEXT.__objc_methname: 0x2aae8
-  __TEXT.__objc_methtype: 0x81f7
-  __TEXT.__objc_stubs: 0x1b620
-  __DATA_CONST.__got: 0x2a0
+  __TEXT.__unwind_info: 0x3878
+  __TEXT.__objc_classname: 0x2bd3
+  __TEXT.__objc_methname: 0x2a9e6
+  __TEXT.__objc_methtype: 0x81e5
+  __TEXT.__objc_stubs: 0x1b600
+  __DATA_CONST.__got: 0x2a8
   __DATA_CONST.__const: 0x3078
   __DATA_CONST.__objc_classlist: 0x888
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x3d0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x3be10
-  __DATA_CONST.__objc_selrefs: 0x7e10
+  __DATA_CONST.__objc_const: 0x3bda0
+  __DATA_CONST.__objc_selrefs: 0x7de8
   __DATA_CONST.__objc_arraydata: 0x288
   __AUTH_CONST.__cfstring: 0x3f60
   __AUTH_CONST.__objc_const: 0x6e78

   __AUTH_CONST.__objc_doubleobj: 0xb0
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x78
-  __AUTH_CONST.__auth_got: 0x700
+  __AUTH_CONST.__auth_got: 0x710
   __AUTH.__objc_data: 0x4ba0
   __DATA.__objc_protorefs: 0x40
-  __DATA.__objc_classrefs: 0xb70
+  __DATA.__objc_classrefs: 0xb68
   __DATA.__objc_superrefs: 0x708
-  __DATA.__objc_ivar: 0x15c4
+  __DATA.__objc_ivar: 0x15bc
   __DATA.__data: 0x3068
   __DATA.__bss: 0x88
   __DATA_DIRTY.__objc_data: 0x9b0

   - /System/Library/Frameworks/AVKit.framework/AVKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
+  - /System/Library/Frameworks/CoreMedia.framework/CoreMedia
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/CoreText.framework/CoreText
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 13E43946-D3F0-30CD-98DF-15655F77DF21
-  Functions: 5902
-  Symbols:   21514
-  CStrings:  8571
+  UUID: 90AE62DE-7945-3C4A-BB49-6A8FD228F4DF
+  Functions: 5896
+  Symbols:   21501
+  CStrings:  8561
 
Symbols:
+ -[AVTPaddleView attachVideoController:]
+ -[AVTSplashScreenViewController detachVideoController]
+ -[AVTUIEnvironment deviceIsVision]
+ _CMTimeMakeWithSeconds
+ _CMTimeRangeFromTimeToTime
+ _OBJC_IVAR_$_AVTUIEnvironment._deviceIsVision
+ _kCMTimeZero
+ _objc_msgSend$deviceIsVision
+ _objc_msgSend$initWithPlayerItem:
+ _objc_msgSend$setLoopTimeRange:
- -[AVTPaddleView attachVideoController:looper:]
- -[AVTPaddleView looper]
- -[AVTPaddleView setLooper:]
- -[AVTSplashScreenViewController detachVideoControllerAndLooper]
- -[AVTSplashScreenViewController playerLooper]
- -[AVTSplashScreenViewController primaryVideoLooper]
- -[AVTSplashScreenViewController secondaryPlayerLooper]
- -[AVTSplashScreenViewController setPlayerLooper:]
- -[AVTSplashScreenViewController setSecondaryPlayerLooper:]
- _OBJC_CLASS_$_AVPlayerLooper
- _OBJC_IVAR_$_AVTPaddleView._looper
- _OBJC_IVAR_$_AVTSplashScreenViewController._playerLooper
- _OBJC_IVAR_$_AVTSplashScreenViewController._secondaryPlayerLooper
- _objc_msgSend$playerLooper
- _objc_msgSend$playerLooperWithPlayer:templateItem:
- _objc_msgSend$setPlayerLooper:
- _objc_msgSend$setSecondaryPlayerLooper:
CStrings:
+ ")"
+ "6\x14"
+ "TB,R,N,V_deviceIsVision"
+ "_deviceIsVision"
+ "attachVideoController:"
+ "detachVideoController"
+ "deviceIsVision"
+ "initWithPlayerItem:"
+ "setLoopTimeRange:"
- "7\x14"
- "@\"AVPlayerLooper\""
- "T@\"AVPlayerLooper\",&,N,V_looper"
- "T@\"AVPlayerLooper\",&,N,V_playerLooper"
- "T@\"AVPlayerLooper\",&,N,V_secondaryPlayerLooper"
- "T@\"AVPlayerLooper\",R,N"
- "_looper"
- "_playerLooper"
- "_secondaryPlayerLooper"
- "attachVideoController:looper:"
- "detachVideoControllerAndLooper"
- "looper"
- "playerLooper"
- "playerLooperWithPlayer:templateItem:"
- "primaryVideoLooper"
- "secondaryPlayerLooper"
- "setLooper:"
- "setPlayerLooper:"
- "setSecondaryPlayerLooper:"

```
