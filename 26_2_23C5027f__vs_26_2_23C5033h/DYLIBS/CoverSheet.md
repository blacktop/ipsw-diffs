## CoverSheet

> `/System/Library/PrivateFrameworks/CoverSheet.framework/CoverSheet`

```diff

-4557.2.2.101.0
-  __TEXT.__text: 0x174f68
+4557.2.5.0.0
+  __TEXT.__text: 0x175100
   __TEXT.__auth_stubs: 0x1420
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x165b4
+  __TEXT.__objc_methlist: 0x165d4
   __TEXT.__const: 0x2c00
   __TEXT.__cstring: 0xa3ef
-  __TEXT.__oslogstring: 0x8fe7
+  __TEXT.__oslogstring: 0x90b3
   __TEXT.__gcc_except_tab: 0xd00
   __TEXT.__ustring: 0xa4
   __TEXT.__dlopen_cstrs: 0x108
-  __TEXT.__unwind_info: 0x41b8
+  __TEXT.__unwind_info: 0x41c0
   __TEXT.__objc_classname: 0x34ce
-  __TEXT.__objc_methname: 0x415d0
+  __TEXT.__objc_methname: 0x41666
   __TEXT.__objc_methtype: 0x9e67
-  __TEXT.__objc_stubs: 0x261c0
+  __TEXT.__objc_stubs: 0x26200
   __DATA_CONST.__got: 0x1590
   __DATA_CONST.__const: 0x2b68
   __DATA_CONST.__objc_classlist: 0x7a8
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x690
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc708
+  __DATA_CONST.__objc_selrefs: 0xc720
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x5e8
   __DATA_CONST.__objc_arraydata: 0x1078
   __AUTH_CONST.__auth_got: 0xa20
   __AUTH_CONST.__const: 0xcc0
   __AUTH_CONST.__cfstring: 0xc500
-  __AUTH_CONST.__objc_const: 0x3cb90
+  __AUTH_CONST.__objc_const: 0x3cbd8
   __AUTH_CONST.__objc_doubleobj: 0x660
   __AUTH_CONST.__objc_arrayobj: 0x1248
   __AUTH_CONST.__objc_intobj: 0x438

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B4ACE50B-3973-38B3-99B0-30B5958575D0
-  Functions: 7212
-  Symbols:   26332
-  CStrings:  14505
+  UUID: 1051398D-96BE-3ECE-8568-11F9C53D1428
+  Functions: 7214
+  Symbols:   26338
+  CStrings:  14511
 
Symbols:
+ -[CSActivityViewController handleEntityWillDismissFromBottomSwipeGesture]
+ -[CSCoverSheetViewController _showChargingSubtitleWithTimeout:dodgingOtherChargeUIs:]
+ GCC_except_table728
+ GCC_except_table739
+ ___85-[CSCoverSheetViewController _showChargingSubtitleWithTimeout:dodgingOtherChargeUIs:]_block_invoke
+ ___block_literal_global.2380
+ _objc_msgSend$_showChargingSubtitleWithTimeout:dodgingOtherChargeUIs:
+ _objc_msgSend$handleActivityWillDismissFromBottomSwipeGesture
- GCC_except_table727
- GCC_except_table738
- ___63-[CSCoverSheetViewController _showChargingSubtitleWithTimeout:]_block_invoke
- ___block_literal_global.2379
Functions:
~ -[CSDateViewComponent _internalPageIndex] : 64 -> 60
~ -[CSCoverSheetViewController _transitionChargingViewToVisible:suppressedByPack:showBattery:animated:] : 2304 -> 2416
~ ___101-[CSCoverSheetViewController _transitionChargingViewToVisible:suppressedByPack:showBattery:animated:]_block_invoke.838 : 380 -> 464
~ -[CSCoverSheetViewController _showChargingSubtitleWithTimeout:] : 324 -> 8
+ -[CSCoverSheetViewController _showChargingSubtitleWithTimeout:dodgingOtherChargeUIs:]
+ -[CSActivityViewController handleEntityWillDismissFromBottomSwipeGesture]
~ -[CSDateViewComponent _internalPageIndexForPageIndex:] : 68 -> 64
~ -[CSDateViewComponent _setValueForInternalPageIndex:hidesTime:constrainsTime:usesCompactTime:] : 148 -> 160
~ -[CSProudLockComponent _setUnsignedIntegerValue:] : 104 -> 116
~ -[CSCoverSheetAppearanceResolver _scaleForTransitionFromScale:toScale:timingFunction:] : 72 -> 68
CStrings:
+ "Abandoned charging estimate flow because of existing modal charge UI"
+ "Abandoned subtitle update because something else is showing"
+ "Early abandoned charging estimate flow because of existing modal charge UI"
+ "_showChargingSubtitleWithTimeout:dodgingOtherChargeUIs:"
+ "handleActivityWillDismissFromBottomSwipeGesture"
+ "handleEntityWillDismissFromBottomSwipeGesture"

```
