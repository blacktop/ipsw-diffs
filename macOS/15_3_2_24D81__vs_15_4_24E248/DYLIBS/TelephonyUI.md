## TelephonyUI

> `/System/iOSSupport/System/Library/PrivateFrameworks/TelephonyUI.framework/Versions/A/TelephonyUI`

```diff

-55.400.141.0.0
-  __TEXT.__text: 0x2ecec
-  __TEXT.__auth_stubs: 0xf10
-  __TEXT.__objc_methlist: 0x315c
+55.500.181.1.1
+  __TEXT.__text: 0x2f278
+  __TEXT.__auth_stubs: 0xef0
+  __TEXT.__objc_methlist: 0x33b8
   __TEXT.__const: 0x978
-  __TEXT.__cstring: 0x1761
+  __TEXT.__cstring: 0x1781
   __TEXT.__oslogstring: 0x4ff
   __TEXT.__gcc_except_tab: 0x48
   __TEXT.__ustring: 0x208
-  __TEXT.__swift5_typeref: 0x280
+  __TEXT.__swift5_typeref: 0x278
   __TEXT.__constg_swiftt: 0x3f8
   __TEXT.__swift5_reflstr: 0x330
   __TEXT.__swift5_fieldmd: 0x1c0

   __TEXT.__swift5_proto: 0xc
   __TEXT.__swift5_types: 0x14
   __TEXT.__swift5_capture: 0x128
+  __TEXT.__swift_as_entry: 0x2c
+  __TEXT.__swift_as_ret: 0x30
   __TEXT.__unwind_info: 0xcf0
-  __TEXT.__eh_frame: 0x400
-  __TEXT.__objc_classname: 0x4c6
-  __TEXT.__objc_methname: 0x9912
+  __TEXT.__eh_frame: 0x468
+  __TEXT.__objc_classname: 0x4c7
+  __TEXT.__objc_methname: 0x9997
   __TEXT.__objc_methtype: 0xfcc
-  __TEXT.__objc_stubs: 0x79e0
+  __TEXT.__objc_stubs: 0x7a60
   __DATA_CONST.__got: 0x650
-  __DATA_CONST.__const: 0x5f0
+  __DATA_CONST.__const: 0x5f8
   __DATA_CONST.__objc_classlist: 0x1b0
   __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x28a0
+  __DATA_CONST.__objc_selrefs: 0x2948
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x110
   __DATA_CONST.__objc_arraydata: 0x60
-  __AUTH_CONST.__auth_got: 0x798
+  __AUTH_CONST.__auth_got: 0x788
   __AUTH_CONST.__const: 0x560
-  __AUTH_CONST.__cfstring: 0x1f80
-  __AUTH_CONST.__objc_const: 0x6120
+  __AUTH_CONST.__cfstring: 0x1fa0
+  __AUTH_CONST.__objc_const: 0x5d60
   __AUTH_CONST.__objc_intobj: 0x120
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_floatobj: 0x20
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x1040
   __AUTH.__data: 0x4c0
-  __DATA.__objc_ivar: 0x2fc
+  __DATA.__objc_ivar: 0x304
   __DATA.__data: 0x400
   __DATA.__bss: 0x5a0
   __DATA.__common: 0x8

   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftIOKit.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 1949FF6E-4B93-3FF1-BCBF-4B4EBED2B7F4
-  Functions: 1402
-  Symbols:   3403
-  CStrings:  2450
+  UUID: DB16BA04-6DDC-3FFC-80C2-FEC427BDDE56
+  Functions: 1414
+  Symbols:   3436
+  CStrings:  2457
 
Symbols:
+ +[TPNumberPadButton loadNumberPadKeyPrototypeView].cold.1
+ +[TPNumberPadKey initialize].cold.1
+ +[TPSimpleNumberPad _numberPadCharacters].cold.1
+ +[TPUIConfiguration defaultFont].cold.1
+ +[TPUIConfiguration screenSize].cold.1
+ +[UIImage(TelephonyUI) fallbackSymbolTypeForCurrentDevice].cold.1
+ +[UIImage(TelephonyUI) genericBusinessLogo].cold.1
+ +[UIImage(TelephonyUI) telephonyUIUnreadIndicatorGlyphImage].cold.1
+ -[TPAlert show].cold.3
+ -[TPInComingCallBottomBarButton titleRectYOffset].cold.1
+ -[TPNumberPad initWithButtons:].cold.1
+ -[TPNumberPad replaceButton:atIndex:].cold.1
+ -[TPPillView badgeImageView]
+ -[TPPillView badgeSymbolName]
+ -[TPPillView setBadgeSymbolName:]
+ -[TPSetPINViewController _updateStatusLabel].cold.1
+ -[TPSetPINViewController _updateStatusLabel].cold.2
+ -[TPSetPINViewController _updateStatusLabel].cold.3
+ -[TPSetPINViewController _updateStatusLabel].cold.4
+ OBJC_IVAR_$_TPPillView._badgeImageView
+ OBJC_IVAR_$_TPPillView._badgeSymbolName
+ TPDefaultLog.cold.1
+ TPIsUnknown.cold.1
+ TPMainScreenScale.cold.1
+ TPPixelCGCeiling.cold.1
+ TPPixelCGFloor.cold.1
+ TPStringForNumberPadCharacter.cold.1
+ ___swift_async_entry_functlets
+ ___swift_async_ret_functlets
+ __imageForRoundedRectProperties.cold.1
+ __imageForRoundedRectProperties.cold.2
+ _objc_msgSend$badgeImageView
+ _objc_msgSend$insertArrangedSubview:atIndex:
+ _objc_msgSend$setCustomSpacing:afterView:
+ _objc_msgSend$systemImageNamed:withConfiguration:
+ _symbolic x______pIeghHrzo_ s5ErrorP
- +[TPTipsHelper donateEventSpeakerUsed]
- __swift_FORCE_LOAD_$_swiftFileProvider
- __swift_FORCE_LOAD_$_swiftFileProvider_$_TelephonyUI
- _symbolic xIegHr_
- _symbolic x______pIegHrzo_ s5ErrorP
CStrings:
+ "T@\"NSString\",C,N,V_badgeSymbolName"
+ "T@\"UIImageView\",R,N,V_badgeImageView"
+ "_badgeImageView"
+ "_badgeSymbolName"
+ "badgeImageView"
+ "badgeSymbolName"
+ "chevron.up.chevron.down"
+ "setBadgeSymbolName:"
- "("
- "donateEventSpeakerUsed"

```
