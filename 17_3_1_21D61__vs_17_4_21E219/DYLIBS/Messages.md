## Messages

> `/System/Library/Frameworks/Messages.framework/Messages`

```diff

-1262.400.41.2.3
-  __TEXT.__text: 0x25798
-  __TEXT.__auth_stubs: 0x8d0
-  __TEXT.__objc_methlist: 0x343c
-  __TEXT.__const: 0x338
+1262.500.151.2.4
+  __TEXT.__text: 0x25e10
+  __TEXT.__auth_stubs: 0x8e0
+  __TEXT.__objc_methlist: 0x351c
+  __TEXT.__const: 0x358
   __TEXT.__gcc_except_tab: 0xfc
-  __TEXT.__cstring: 0x19e3
+  __TEXT.__cstring: 0x1a88
   __TEXT.__oslogstring: 0xb72
   __TEXT.__dlopen_cstrs: 0x17e
-  __TEXT.__unwind_info: 0xb08
-  __TEXT.__objc_classname: 0x6ca
-  __TEXT.__objc_methname: 0x9df3
-  __TEXT.__objc_methtype: 0x2974
-  __TEXT.__objc_stubs: 0x6740
+  __TEXT.__unwind_info: 0xb18
+  __TEXT.__objc_classname: 0x6de
+  __TEXT.__objc_methname: 0x9fc9
+  __TEXT.__objc_methtype: 0x298a
+  __TEXT.__objc_stubs: 0x6980
   __DATA_CONST.__got: 0x218
   __DATA_CONST.__const: 0x5d0
-  __DATA_CONST.__objc_classlist: 0x108
+  __DATA_CONST.__objc_classlist: 0x110
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x5d38
-  __DATA_CONST.__objc_selrefs: 0x1fb0
+  __DATA_CONST.__objc_const: 0x5de8
+  __DATA_CONST.__objc_selrefs: 0x2040
+  __DATA_CONST.__objc_protorefs: 0x20
+  __DATA_CONST.__objc_classrefs: 0x2f0
+  __DATA_CONST.__objc_superrefs: 0xf8
   __DATA_CONST.__objc_arraydata: 0x30
-  __AUTH_CONST.__objc_const: 0x1030
-  __AUTH_CONST.__cfstring: 0x14c0
+  __AUTH_CONST.__objc_const: 0x10c0
+  __AUTH_CONST.__cfstring: 0x15e0
   __AUTH_CONST.__const: 0x2a0
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_doubleobj: 0x40
-  __AUTH_CONST.__auth_got: 0x478
-  __AUTH.__objc_data: 0x820
-  __DATA.__objc_protorefs: 0x20
-  __DATA.__objc_classrefs: 0x2e8
-  __DATA.__objc_superrefs: 0xf0
-  __DATA.__objc_ivar: 0x344
+  __AUTH_CONST.__auth_got: 0x480
+  __AUTH.__objc_data: 0x870
+  __DATA.__objc_ivar: 0x350
   __DATA.__data: 0xa68
   __DATA.__bss: 0xf8
   __DATA_DIRTY.__objc_data: 0x230

   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
   - /System/Library/Frameworks/VisionKit.framework/VisionKit
+  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/IMCore.framework/IMCore
   - /System/Library/PrivateFrameworks/IMSharedUI.framework/IMSharedUI
   - /System/Library/PrivateFrameworks/IMSharedUtilities.framework/IMSharedUtilities

   - /System/Library/PrivateFrameworks/VisionKitCore.framework/VisionKitCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1291
-  Symbols:   4478
-  CStrings:  2145
+  Functions: 1308
+  Symbols:   4542
+  CStrings:  2183
 
Symbols:
+ +[MSStickerUsageEvent autoSourceType]
+ +[MSStickerUsageEvent effectTypeForMediaPayload:]
+ +[MSStickerUsageEvent effectTypeForSticker:]
+ +[MSStickerUsageEvent effectTypeFromVKCStickerEffectType:]
+ +[MSStickerUsageEvent isPreferredRepresentationAnimated:]
+ +[MSStickerUsageEvent stickerTypeFromExternalURI:]
+ -[MSStickerUsageEvent effectType]
+ -[MSStickerUsageEvent initWithMediaPayload:]
+ -[MSStickerUsageEvent initWithSticker:]
+ -[MSStickerUsageEvent send]
+ -[MSStickerUsageEvent setEffectType:]
+ -[MSStickerUsageEvent setSourceType:]
+ -[MSStickerUsageEvent setStickerType:]
+ -[MSStickerUsageEvent setUsageType:]
+ -[MSStickerUsageEvent sourceType]
+ -[MSStickerUsageEvent stickerType]
+ -[MSStickerUsageEvent usageType]
+ -[MSStickerView _sendStickerUsageAnalyticsForDragAndDrop]
+ GCC_except_table45
+ _AnalyticsSendEvent
+ _OBJC_CLASS_$_MSStickerUsageEvent
+ _OBJC_IVAR_$_MSStickerUsageEvent._effectType
+ _OBJC_IVAR_$_MSStickerUsageEvent._sourceType
+ _OBJC_IVAR_$_MSStickerUsageEvent._stickerType
+ _OBJC_IVAR_$_MSStickerUsageEvent._usageType
+ _OBJC_METACLASS_$_MSStickerUsageEvent
+ __OBJC_$_CLASS_METHODS_MSStickerUsageEvent
+ __OBJC_$_INSTANCE_METHODS_MSStickerUsageEvent
+ __OBJC_$_INSTANCE_VARIABLES_MSStickerUsageEvent
+ __OBJC_$_PROP_LIST_MSStickerUsageEvent
+ __OBJC_CLASS_RO_$_MSStickerUsageEvent
+ __OBJC_METACLASS_RO_$_MSStickerUsageEvent
+ ___58-[MSStickerView dragInteraction:itemsForBeginningSession:]_block_invoke.160
+ ___60-[_MSMessageAppContext _requestSnapshotThatFits:completion:]_block_invoke.91
+ ___69-[_MSMessageAppContext _prepareForPresentationWithCompletionHandler:]_block_invoke.99
+ ___84-[_MSMessageAppContext _canSendMessage:conversationState:associatedText:completion:]_block_invoke.77
+ ___block_literal_global.127
+ _objc_msgSend$_sendStickerUsageAnalyticsForDragAndDrop
+ _objc_msgSend$autoSourceType
+ _objc_msgSend$effectType
+ _objc_msgSend$effectTypeForMediaPayload:
+ _objc_msgSend$effectTypeForSticker:
+ _objc_msgSend$effectTypeFromVKCStickerEffectType:
+ _objc_msgSend$initWithMediaPayload:
+ _objc_msgSend$isPreferredRepresentationAnimated:
+ _objc_msgSend$numberWithInteger:
+ _objc_msgSend$send
+ _objc_msgSend$setEffectType:
+ _objc_msgSend$setSourceType:
+ _objc_msgSend$setStickerType:
+ _objc_msgSend$setUsageType:
+ _objc_msgSend$sourceType
+ _objc_msgSend$stickerType
+ _objc_msgSend$stickerTypeFromExternalURI:
+ _objc_msgSend$usageType
- -[MSMessagesAppViewController(CompactOrExpandedPresentation) _percentExpanded]
- GCC_except_table44
- _OBJC_IVAR_$_MSMessagesAppViewController.__percentExpanded
- ___58-[MSStickerView dragInteraction:itemsForBeginningSession:]_block_invoke.159
- ___60-[_MSMessageAppContext _requestSnapshotThatFits:completion:]_block_invoke.90
- ___69-[_MSMessageAppContext _prepareForPresentationWithCompletionHandler:]_block_invoke.98
- ___84-[_MSMessageAppContext _canSendMessage:conversationState:associatedText:completion:]_block_invoke.76
- ___block_literal_global.126
- ___block_literal_global.5
CStrings:
+ "MSStickerUsageEvent"
+ "T@\"NSArray\",?,R,C,N"
+ "T@\"NSString\",?,R,C"
+ "Tq,N,V_effectType"
+ "Tq,N,V_sourceType"
+ "Tq,N,V_stickerType"
+ "Tq,N,V_usageType"
+ "_effectType"
+ "_sendStickerUsageAnalyticsForDragAndDrop"
+ "_sourceType"
+ "_stickerType"
+ "_usageType"
+ "autoSourceType"
+ "com.apple.visualintelligence.stickerUsage"
+ "effectType"
+ "effectTypeForMediaPayload:"
+ "effectTypeForSticker:"
+ "effectTypeFromVKCStickerEffectType:"
+ "initWithMediaPayload:"
+ "isPreferredRepresentationAnimated:"
+ "numberWithInteger:"
+ "q24@0:8Q16"
+ "send"
+ "setEffectType:"
+ "setSourceType:"
+ "setStickerType:"
+ "setUsageType:"
+ "sourceType"
+ "sticker:///emoji/"
+ "sticker:///memoji/"
+ "sticker:///third_party/"
+ "sticker:///user/"
+ "stickerType"
+ "stickerTypeFromExternalURI:"
+ "usageSource"
+ "usageType"
+ "v24@0:8q16"
- "Td,R,N,V__percentExpanded"
- "__percentExpanded"

```
