## proximitycontrold

> `/usr/libexec/proximitycontrold`

```diff

-208.10.4.0.0
-  __TEXT.__text: 0x1f6c08
+208.10.5.0.0
+  __TEXT.__text: 0x1f73e0
   __TEXT.__auth_stubs: 0x2910
   __TEXT.__objc_stubs: 0x220
-  __TEXT.__objc_methlist: 0x1058
-  __TEXT.__objc_classname: 0x470
-  __TEXT.__objc_methname: 0x642f
-  __TEXT.__objc_methtype: 0x2bda
-  __TEXT.__const: 0x1b188
-  __TEXT.__cstring: 0x14399
-  __TEXT.__swift5_typeref: 0x10f26
-  __TEXT.__swift5_fieldmd: 0x85c0
-  __TEXT.__constg_swiftt: 0xdf48
-  __TEXT.__swift5_reflstr: 0x8433
-  __TEXT.__swift5_builtin: 0x424
+  __TEXT.__objc_methlist: 0x1090
+  __TEXT.__objc_classname: 0x48b
+  __TEXT.__objc_methname: 0x6534
+  __TEXT.__objc_methtype: 0x2d00
+  __TEXT.__const: 0x1b228
+  __TEXT.__cstring: 0x14449
+  __TEXT.__swift5_typeref: 0x10fcc
+  __TEXT.__swift5_fieldmd: 0x85f4
+  __TEXT.__constg_swiftt: 0xdfec
+  __TEXT.__swift5_reflstr: 0x8453
+  __TEXT.__swift5_builtin: 0x438
   __TEXT.__swift5_assocty: 0xc80
   __TEXT.__swift5_protos: 0x328
-  __TEXT.__swift5_proto: 0x1908
-  __TEXT.__swift5_types: 0x7b8
-  __TEXT.__swift5_capture: 0x36b0
+  __TEXT.__swift5_proto: 0x1910
+  __TEXT.__swift5_types: 0x7c0
+  __TEXT.__swift5_capture: 0x36a0
   __TEXT.__swift5_mpenum: 0xc0
-  __TEXT.__unwind_info: 0x6958
+  __TEXT.__unwind_info: 0x6980
   __TEXT.__eh_frame: 0x4ea8
   __DATA_CONST.__auth_got: 0x1490
-  __DATA_CONST.__got: 0xbd0
-  __DATA_CONST.__auth_ptr: 0x2318
-  __DATA_CONST.__const: 0x16060
+  __DATA_CONST.__got: 0xbe8
+  __DATA_CONST.__auth_ptr: 0x2100
+  __DATA_CONST.__const: 0x16070
   __DATA_CONST.__cfstring: 0x400
-  __DATA_CONST.__objc_classlist: 0x368
+  __DATA_CONST.__objc_classlist: 0x370
   __DATA_CONST.__objc_catlist: 0x28
-  __DATA_CONST.__objc_protolist: 0x2e8
+  __DATA_CONST.__objc_protolist: 0x2f8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x178
+  __DATA_CONST.__objc_protorefs: 0x180
   __DATA_CONST.__objc_superrefs: 0x10
-  __DATA.__objc_const: 0x16b40
-  __DATA.__objc_selrefs: 0x1248
+  __DATA.__objc_const: 0x16fc8
+  __DATA.__objc_selrefs: 0x1260
   __DATA.__objc_ivar: 0x54
-  __DATA.__objc_data: 0x28c8
-  __DATA.__data: 0x141b0
-  __DATA.__bss: 0x28540
-  __DATA.__common: 0x500
+  __DATA.__objc_data: 0x29c0
+  __DATA.__data: 0x142d0
+  __DATA.__bss: 0x285d0
+  __DATA.__common: 0x508
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/SwiftUI.framework/SwiftUI
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/Announce.framework/Announce
+  - /System/Library/PrivateFrameworks/BacklightServices.framework/BacklightServices
   - /System/Library/PrivateFrameworks/BannerKit.framework/BannerKit
   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /System/Library/PrivateFrameworks/BaseBoardUI.framework/BaseBoardUI

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 10105
-  Symbols:   1275
-  CStrings:  3635
+  Functions: 10115
+  Symbols:   1277
+  CStrings:  3656
 
Symbols:
+ _OBJC_CLASS_$_BLSBacklight
+ _OBJC_CLASS_$_BLSBacklightChangeEvent
CStrings:
+ "_TtC17proximitycontrold16BacklightMonitor"
+ "backlight:deactivatingWithEvent:"
+ "v48@0:8@\"<BLSBacklightStateObservable>\"16q24@\"NSArray\"32@\"NSArray\"40"
+ "_backlightState"
+ "v28@0:8@\"<BLSBacklightStateObservable>\"16B24"
+ ": backlightState="
+ "addObserver:"
+ "backlight:didCompleteUpdateToState:forEvent:"
+ "v48@0:8@16q24@32@40"
+ "v40@0:8@\"<BLSBacklightStateObservable>\"16q24@\"BLSBacklightChangeEvent\"32"
+ "backlight:didChangeAlwaysOnEnabled:"
+ "backlight(_:didCompleteUpdateTo:for:)"
+ "v40@0:8@16q24@32"
+ "backlight:didCompleteUpdateToState:forEvents:abortedEvents:"
+ "BLSBacklightStateObserving"
+ "backlight:performingEvent:"
+ "backlight"
+ "backlight:activatingWithEvent:"
+ "v32@0:8@\"<BLSBacklightStateObservable>\"16@\"BLSBacklightChangeEvent\"24"
+ "backlightMonitor"
+ "sharedBacklight"
- "SystemMonitor activated"

```
