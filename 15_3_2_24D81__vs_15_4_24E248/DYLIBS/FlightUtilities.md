## FlightUtilities

> `/System/Library/PrivateFrameworks/FlightUtilities.framework/Versions/A/FlightUtilities`

```diff

-155.0.0.0.0
-  __TEXT.__text: 0xe7c8
+155.2.0.0.0
+  __TEXT.__text: 0xe704
   __TEXT.__auth_stubs: 0x390
-  __TEXT.__objc_methlist: 0x12b0
+  __TEXT.__objc_methlist: 0x15bc
   __TEXT.__const: 0x114
   __TEXT.__ustring: 0x5c
-  __TEXT.__cstring: 0x36a
+  __TEXT.__cstring: 0x382
   __TEXT.__gcc_except_tab: 0x4c
-  __TEXT.__unwind_info: 0x4b8
+  __TEXT.__unwind_info: 0x4b0
   __TEXT.__objc_classname: 0x24a
   __TEXT.__objc_methname: 0x45be
   __TEXT.__objc_methtype: 0xb0f

   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1250
+  __DATA_CONST.__objc_selrefs: 0x13b0
   __DATA_CONST.__objc_superrefs: 0x70
   __AUTH_CONST.__auth_got: 0x1d8
   __AUTH_CONST.__const: 0x1b0
-  __AUTH_CONST.__cfstring: 0x8e0
-  __AUTH_CONST.__objc_const: 0x2fa8
+  __AUTH_CONST.__cfstring: 0x900
+  __AUTH_CONST.__objc_const: 0x29f8
   __AUTH_CONST.__objc_doubleobj: 0x50
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0x668

   - /System/Library/PrivateFrameworks/TemplateKit.framework/Versions/A/TemplateKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: DAE4BB45-56A0-3C24-81FA-2CFEDEA1BED1
-  Functions: 400
+  UUID: B32493A0-42C3-395F-A686-398014D7A1D5
+  Functions: 399
   Symbols:   1333
-  CStrings:  1165
+  CStrings:  1167
 
Symbols:
+ __68-[FUFlightViewController loadFlightWithFlightCode:airlineCode:date:]_block_invoke.21
- __68-[FUFlightViewController loadFlightWithFlightCode:airlineCode:date:]_block_invoke.18
Functions:
~ -[FUFlightViewController initWithSFFlight:leg:style:delegate:] : 504 -> 596
~ -[FUFlightViewController initWithFlightCode:airlineCode:] : 496 -> 504
~ -[FUFlightViewController loadFlightWithFlightCode:airlineCode:date:] : 596 -> 592
~ ___68-[FUFlightViewController loadFlightWithFlightCode:airlineCode:date:]_block_invoke : 128 -> 132
~ -[FUFlightViewController setDisplayStyle:] : 112 -> 104
~ -[FUFlightViewController viewDidLoad] : 476 -> 492
~ -[FULabel setText:] : 220 -> 216
~ -[FULabel setAttributedText:] : 256 -> 252
~ -[FUFlightInfoView setupLabelStylesWithStyle:] : 1712 -> 1708
~ -[FUFlightInfoView setFlight:legIndex:multiFlights:spotlightMode:] : 604 -> 580
~ -[FUFlightInfoView updateDelayInfo] : 1364 -> 1372
~ -[FUFlightInfoView updateFlightTerminalInfo] : 2240 -> 2232
~ -[FUFlightInfoView updateFlightDates] : 2388 -> 2332
~ -[FUFlightInfoView updateFlightStatus] : 1940 -> 1856
- sub_1b976e964
~ -[FUFlightView setShowInfoPanel:] : 140 -> 136
~ -[FUFlightView absoluteLegIndex] : 508 -> 504
~ -[FUFlightView setFlights:selectedFlight:selectedLeg:] : 2012 -> 2004
~ -[FUFlightView updateBackForwardButtons:animated:] : 344 -> 340
~ -[FUFlightView updateMargins] : 576 -> 500
~ -[FUFlightView addTrack:] : 216 -> 208
~ -[FUFlightView fitMap:] : 1196 -> 1188
~ -[FUFlightProgressView enableBlur:] : 336 -> 340
~ -[FUDotIndicator setProvider:] : 156 -> 152
~ -[FUDotIndicator mouseExited:] : 24 -> 28
~ -[FUDotIndicator mouseUp:] : 220 -> 224
CStrings:
+ "com.apple.SiriNCService"

```
