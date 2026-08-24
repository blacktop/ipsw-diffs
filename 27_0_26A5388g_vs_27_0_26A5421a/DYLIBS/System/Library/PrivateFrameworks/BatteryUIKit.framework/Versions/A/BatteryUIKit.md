## BatteryUIKit

> `/System/Library/PrivateFrameworks/BatteryUIKit.framework/Versions/A/BatteryUIKit`

```diff

-2027.0.1.0.0
-  __TEXT.__text: 0x4448
-  __TEXT.__objc_methlist: 0x4c0
-  __TEXT.__const: 0x48
-  __TEXT.__oslogstring: 0x243
-  __TEXT.__cstring: 0x5a1
-  __TEXT.__gcc_except_tab: 0xa8
-  __TEXT.__unwind_info: 0x198
+2027.0.2.0.0
+  __TEXT.__text: 0x538c
+  __TEXT.__objc_methlist: 0x538
+  __TEXT.__const: 0x58
+  __TEXT.__oslogstring: 0x342
+  __TEXT.__cstring: 0x639
+  __TEXT.__gcc_except_tab: 0x12c
+  __TEXT.__unwind_info: 0x1d8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__const: 0x20
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4a0
+  __DATA_CONST.__objc_selrefs: 0x558
   __DATA_CONST.__objc_superrefs: 0x18
-  __DATA_CONST.__got: 0xe0
+  __DATA_CONST.__got: 0x108
   __AUTH_CONST.__const: 0xc0
-  __AUTH_CONST.__cfstring: 0x8e0
+  __AUTH_CONST.__cfstring: 0xa40
   __AUTH_CONST.__objc_const: 0x7b8
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xf0

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 131
-  Symbols:   392
-  CStrings:  87
+  Functions: 145
+  Symbols:   435
+  CStrings:  101
 
Symbols:
+ -[BUIImage _assetNamed:]
+ -[BUIImage _drawAssetNamed:inRect:color:]
+ -[BUIImage _drawModernPercentageForLevel:charging:pluggedIn:atAnchor:]
+ -[BUIImage _legacyImagesForBattery:]
+ -[BUIImage _mirrorRect:rightToLeft:]
+ -[BUIImage _modernBatteryImageForLevel:charging:pluggedIn:noBattery:needsReplacement:lowPowerMode:showPercentage:useRed:]
+ -[BUIImage _modernImagesForBattery:]
+ -[BUIImage _punchHaloWithAssetNamed:inRect:]
+ -[BUIImage _rectForSize:centeredAt:]
+ -[BUIImage _tintedImage:color:]
+ GCC_except_table40
+ _NSFontAttributeName
+ _NSFontWeightRegular
+ _NSForegroundColorAttributeName
+ _NSRectFill
+ _OBJC_CLASS_$_NSFont
+ ___NSArray0__struct
+ __os_log_error_impl
+ _objc_exception_rethrow
+ _objc_msgSend$_assetNamed:
+ _objc_msgSend$_drawAssetNamed:inRect:color:
+ _objc_msgSend$_drawModernPercentageForLevel:charging:pluggedIn:atAnchor:
+ _objc_msgSend$_legacyImagesForBattery:
+ _objc_msgSend$_mirrorRect:rightToLeft:
+ _objc_msgSend$_modernBatteryImageForLevel:charging:pluggedIn:noBattery:needsReplacement:lowPowerMode:showPercentage:useRed:
+ _objc_msgSend$_modernImagesForBattery:
+ _objc_msgSend$_punchHaloWithAssetNamed:inRect:
+ _objc_msgSend$_rectForSize:centeredAt:
+ _objc_msgSend$_tintedImage:color:
+ _objc_msgSend$addClip
+ _objc_msgSend$bezierPathWithRoundedRect:xRadius:yRadius:
+ _objc_msgSend$colorWithWhite:alpha:
+ _objc_msgSend$drawAtPoint:withAttributes:
+ _objc_msgSend$fill
+ _objc_msgSend$restoreGraphicsState
+ _objc_msgSend$saveGraphicsState
+ _objc_msgSend$secondaryLabelColor
+ _objc_msgSend$sizeWithAttributes:
+ _objc_msgSend$systemFontOfSize:weight:
+ _objc_msgSend$systemRedColor
+ _objc_msgSend$systemYellowColor
+ _objc_msgSend$whiteColor
+ _objc_terminate
CStrings:
+ "%ld"
+ "Low Power Mode"
+ "Modern Style"
+ "Show Percentage"
+ "[BUIImage _legacyImagesForBattery:%@]"
+ "[BUIImage _modernBatteryImageForLevel:%f charging:%d pluggedIn:%d noBattery:%d needsReplacement:%d lowPowerMode:%d showPercentage:%d useRed:%d]"
+ "[BUIImage _modernBatteryImageForLevel:] drawing failed: %{public}@"
+ "[BUIImage _modernImagesForBattery:%@]"
+ "battery-alert"
+ "battery-bolt"
+ "battery-bolt-mask"
+ "battery-cap"
+ "battery-missing"
+ "battery-plug"
+ "battery-plug-mask"
- "[BUIImage _imagesForBattery:%@]"
```
