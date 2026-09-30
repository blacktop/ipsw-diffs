## SystemStatusUI

> `/System/Library/PrivateFrameworks/SystemStatusUI.framework/SystemStatusUI`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__cstring`
- `__TEXT.__swift5_proto`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_doubleobj`

```diff

-282.0.0.0.0
-  __TEXT.__text: 0xa123c
-  __TEXT.__objc_methlist: 0xaf34
-  __TEXT.__const: 0x3420
+284.1.0.0.0
+  __TEXT.__text: 0xa1fa4
+  __TEXT.__objc_methlist: 0xaf24
+  __TEXT.__const: 0x3870
   __TEXT.__swift5_typeref: 0x2694
   __TEXT.__constg_swiftt: 0x70c
   __TEXT.__cstring: 0x2bba

   __TEXT.__gcc_except_tab: 0xf7c
   __TEXT.__ustring: 0xac
   __TEXT.__oslogstring: 0x581
-  __TEXT.__unwind_info: 0x25c0
+  __TEXT.__unwind_info: 0x25d8
   __TEXT.__eh_frame: 0xec
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_superrefs: 0x390
   __DATA_CONST.__objc_arraydata: 0x300
   __DATA_CONST.__got: 0x1098
-  __AUTH_CONST.__const: 0x1348
+  __AUTH_CONST.__const: 0x1408
   __AUTH_CONST.__cfstring: 0x3ca0
-  __AUTH_CONST.__objc_const: 0x13af8
+  __AUTH_CONST.__objc_const: 0x13b28
   __AUTH_CONST.__objc_arrayobj: 0x300
   __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__objc_doubleobj: 0x1c0
-  __AUTH_CONST.__auth_got: 0xbc0
-  __AUTH.__objc_data: 0x1350
-  __AUTH.__data: 0x2b0
-  __DATA.__objc_ivar: 0x520
-  __DATA.__data: 0x16f0
-  __DATA.__bss: 0x1d38
+  __AUTH_CONST.__auth_got: 0xbd0
+  __AUTH.__objc_data: 0x1238
+  __AUTH.__data: 0x280
+  __DATA.__objc_ivar: 0x528
+  __DATA.__data: 0x16e0
+  __DATA.__bss: 0x1d98
   __DATA.__common: 0x10
-  __DATA_DIRTY.__objc_ivar: 0x530
-  __DATA_DIRTY.__objc_data: 0x2c60
+  __DATA_DIRTY.__objc_ivar: 0x52c
+  __DATA_DIRTY.__objc_data: 0x2d78
+  __DATA_DIRTY.__data: 0x50
   __DATA_DIRTY.__bss: 0x1f0
   __DATA_DIRTY.__common: 0x38
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 4174
-  Symbols:   9091
+  Functions: 4182
+  Symbols:   9103
   CStrings:  625
 
Symbols:
+ -[STUIStatusBarDisplayableContainerView forceAllowCrossfade]
+ -[STUIStatusBarDisplayableContainerView setForceAllowCrossfade:]
+ -[STUIStatusBarDisplayableContainerView wantsCrossfade]
+ -[STUIStatusBarWirelessChargerView _drawChargingInRect:capacityColor:boltColor:level:]
+ -[STUIStatusBarWirelessChargerView _drawDeviceEnabledInRect:]
+ -[STUIStatusBarWirelessChargerView _drawErrorInRect:]
+ -[STUIStatusBarWirelessChargerView _drawOutlineInRect:]
+ _BoltTemplate
+ _CGContextRestoreGState
+ _CGContextSaveGState
+ _OBJC_IVAR_$_STUIStatusBarDisplayableContainerView._forceAllowCrossfade
+ _OBJC_IVAR_$_STUIStatusBarWirelessChargerView._styleAttributes
+ _OuterPillTemplate
+ _PathAt
+ ___45-[STUIStatusBarWirelessChargerView drawRect:]_block_invoke
+ ___BoltTemplate_block_invoke
+ ___ExclamationTemplate_block_invoke
+ ___InnerPillTemplate_block_invoke
+ ___OuterPillTemplate_block_invoke
+ ___SlashCutTemplate_block_invoke
+ ___SlashMarkTemplate_block_invoke
+ _objc_msgSend$_drawChargingInRect:capacityColor:boltColor:level:
+ _objc_msgSend$_drawDeviceEnabledInRect:
+ _objc_msgSend$_drawErrorInRect:
+ _objc_msgSend$_drawOutlineInRect:
+ _objc_msgSend$addClip
+ _objc_msgSend$addCurveToPoint:controlPoint1:controlPoint2:
+ _objc_msgSend$addQuadCurveToPoint:controlPoint:
+ _objc_msgSend$appendPath:
+ _objc_msgSend$applyTransform:
+ _objc_msgSend$forceAllowCrossfade
+ _objc_msgSend$setForceAllowCrossfade:
+ _objc_msgSend$setUsesEvenOddFillRule:
+ _objc_msgSend$systemBackgroundColor
- -[STUIStatusBarWirelessChargerView _drawBodyOutlineInRect:color:]
- -[STUIStatusBarWirelessChargerView _drawBoltInRect:color:]
- -[STUIStatusBarWirelessChargerView _drawExclamationInRect:color:]
- -[STUIStatusBarWirelessChargerView _drawFillInRect:level:color:displayScale:]
- -[STUIStatusBarWirelessChargerView _drawTerminalInRect:color:]
- -[STUIStatusBarWirelessChargerView _fillColor]
- -[STUIStatusBarWirelessChargerView _outlineColor]
- -[STUIStatusBarWirelessChargerView _shouldShowExclamation]
- -[STUIStatusBarWirelessChargerView _shouldShowFill]
- _objc_msgSend$_drawBodyOutlineInRect:color:
- _objc_msgSend$_drawBoltInRect:color:
- _objc_msgSend$_drawExclamationInRect:color:
- _objc_msgSend$_drawFillInRect:level:color:displayScale:
- _objc_msgSend$_drawTerminalInRect:color:
- _objc_msgSend$_fillColor
- _objc_msgSend$_outlineColor
- _objc_msgSend$_shouldShowExclamation
- _objc_msgSend$_shouldShowFill
- _objc_msgSend$bezierPathWithRoundedRect:byRoundingCorners:cornerRadii:
- _objc_msgSend$bezierPathWithRoundedRect:cornerRadius:
- _objc_msgSend$setStroke
- _objc_msgSend$systemGrayColor
```
