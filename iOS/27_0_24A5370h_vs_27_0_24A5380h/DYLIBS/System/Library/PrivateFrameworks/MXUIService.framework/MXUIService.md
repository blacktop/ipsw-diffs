## MXUIService

> `/System/Library/PrivateFrameworks/MXUIService.framework/MXUIService`

```diff

-  __TEXT.__text: 0x94c8
-  __TEXT.__objc_methlist: 0xb04
-  __TEXT.__const: 0x140
-  __TEXT.__cstring: 0x917
-  __TEXT.__oslogstring: 0x87a
+  __TEXT.__text: 0xa0f4
+  __TEXT.__objc_methlist: 0xb24
+  __TEXT.__const: 0xe8
+  __TEXT.__cstring: 0x93b
+  __TEXT.__oslogstring: 0x87b
   __TEXT.__unwind_info: 0x1d8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1a8
+  __DATA_CONST.__const: 0x178
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x960
+  __DATA_CONST.__objc_selrefs: 0x990
   __DATA_CONST.__objc_superrefs: 0x28
-  __DATA_CONST.__got: 0x188
+  __DATA_CONST.__got: 0x198
   __AUTH_CONST.__const: 0x60
-  __AUTH_CONST.__cfstring: 0x380
-  __AUTH_CONST.__objc_const: 0x17a0
+  __AUTH_CONST.__cfstring: 0x3c0
+  __AUTH_CONST.__objc_const: 0x17c8
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x230
-  __DATA.__objc_ivar: 0xa8
+  __DATA.__objc_ivar: 0xac
   __DATA.__data: 0x300
   __DATA.__common: 0x90
   __DATA.__bss: 0x30

   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/UIKit.framework/UIKit
+  - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
   - /System/Library/PrivateFrameworks/BannerKit.framework/BannerKit
   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /System/Library/PrivateFrameworks/BaseBoardUI.framework/BaseBoardUI
   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
+  - /System/Library/PrivateFrameworks/IconServices.framework/IconServices
   - /System/Library/PrivateFrameworks/MXUIServiceClient.framework/MXUIServiceClient
   - /System/Library/PrivateFrameworks/PlatterKit.framework/PlatterKit
   - /System/Library/PrivateFrameworks/SpringBoardUIServices.framework/SpringBoardUIServices

   - /System/Library/PrivateFrameworks/UIFoundation.framework/UIFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 209
-  Symbols:   906
-  CStrings:  127
+  Functions: 211
+  Symbols:   918
+  CStrings:  131
 
Sections:
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH.__objc_data : content changed
~ __DATA.__data : content changed
Symbols:
+ -[MXUIServiceBanner deriveDeviceSymbol]
+ -[MXUIService_BannerUIDelegate showReceiverEnabledBanner:completionHandler:]
+ -[MXUIService_BannerUIDelegate showSpeakerEnabledBanner:completionHandler:]
+ _OBJC_CLASS_$_ISSymbol
+ _OBJC_CLASS_$_UTType
+ _OBJC_IVAR_$_MXUIServiceBanner._bannerStyle
+ _UIFontWeightRegular
+ _objc_msgSend$_typeOfCurrentDevice
+ _objc_msgSend$deriveDeviceSymbol
+ _objc_msgSend$identifier
+ _objc_msgSend$name
+ _objc_msgSend$symbolForTypeIdentifier:error:
- -[MXUIService_BannerUIDelegate showAudioMovedBanner:completionHandler:]
- _UIFontWeightSemibold
CStrings:
+ "-MXUIServiceBanner- %s: Audio moved banner styles require Jindo path — skipping non-Jindo layout"
+ "AUDIO_MOVED_TO_RECEIVER"
+ "iPhone"
+ "speaker.wave.3.fill"
- "-MXUIServiceBanner- %s: MXBannerStyleAudioMoved requires Jindo path — skipping non-Jindo layout"
- "speaker.wave.3"

```
