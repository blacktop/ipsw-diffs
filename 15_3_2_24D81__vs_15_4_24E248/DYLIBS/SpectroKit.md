## SpectroKit

> `/System/Library/PrivateFrameworks/SpectroKit.framework/Versions/A/SpectroKit`

```diff

 10.0.0.0.0
-  __TEXT.__text: 0x6368
+  __TEXT.__text: 0x63b8
   __TEXT.__auth_stubs: 0x2b0
   __TEXT.__objc_methlist: 0x368
   __TEXT.__const: 0x18

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A10BF996-76B7-3DBC-AEE9-BA9DE4C9D461
+  UUID: 5D0294EB-916B-3738-B53A-C0130EC9800A
   Functions: 86
   Symbols:   286
   CStrings:  499
Functions:
~ _serialRead : 264 -> 276
~ _serialSendWithTimeout : 364 -> 384
~ -[Spectro openDevicePath:] : 872 -> 864
~ -[Spectro commandPR:wait:] : 1440 -> 1488
~ -[Spectro PRBandwidthAndApertureOK] : 768 -> 772
~ -[Spectro restoreCR] : 444 -> 448

```
