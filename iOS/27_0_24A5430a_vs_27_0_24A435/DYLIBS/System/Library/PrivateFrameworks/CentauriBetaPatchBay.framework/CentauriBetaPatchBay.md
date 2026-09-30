## CentauriBetaPatchBay

> `/System/Library/PrivateFrameworks/CentauriBetaPatchBay.framework/CentauriBetaPatchBay`

```diff

 26.72.12.0.0
-  __TEXT.__text: 0xe60
-  __TEXT.__const: 0x20
+  __TEXT.__text: 0xf10
+  __TEXT.__const: 0x34
   __TEXT.__cstring: 0x10a
   __TEXT.__oslogstring: 0x24a
   __TEXT.__unwind_info: 0x88

   __AUTH_CONST.__auth_got: 0x0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   Functions: 28
-  Symbols:   48
+  Symbols:   49
   CStrings:  34
 
Symbols:
+ _MGIsDeviceOfType
Functions:
~ _getGpioConfigType : 16 -> 140
~ _CentauriBetaPatchBayCopyData : 796 -> 848
```
