## usbctelemetryd

> `/usr/libexec/usbctelemetryd`

```diff

-4.0.0.0.0
-  __TEXT.__text: 0xcc8
+5.0.0.0.0
+  __TEXT.__text: 0x10f4
   __TEXT.__auth_stubs: 0x220
-  __TEXT.__objc_stubs: 0x1e0
-  __TEXT.__objc_methlist: 0xb0
-  __TEXT.__cstring: 0x1c5
-  __TEXT.__oslogstring: 0xd1
-  __TEXT.__objc_classname: 0x14
-  __TEXT.__objc_methname: 0x1e0
-  __TEXT.__objc_methtype: 0x81
-  __TEXT.__unwind_info: 0x90
+  __TEXT.__objc_stubs: 0x200
+  __TEXT.__objc_methlist: 0xf0
+  __TEXT.__cstring: 0x2dd
+  __TEXT.__oslogstring: 0xac
+  __TEXT.__objc_classname: 0x28
+  __TEXT.__objc_methname: 0x203
+  __TEXT.__objc_methtype: 0x82
+  __TEXT.__unwind_info: 0x98
   __DATA_CONST.__auth_got: 0x118
-  __DATA_CONST.__got: 0x30
-  __DATA_CONST.__cfstring: 0x360
-  __DATA_CONST.__objc_classlist: 0x8
+  __DATA_CONST.__got: 0x40
+  __DATA_CONST.__cfstring: 0x580
+  __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0x200
-  __DATA.__objc_selrefs: 0x98
-  __DATA.__objc_ivar: 0x28
-  __DATA.__objc_data: 0x50
+  __DATA.__objc_const: 0x2a0
+  __DATA.__objc_selrefs: 0xa0
+  __DATA.__objc_ivar: 0x18
+  __DATA.__objc_data: 0xf0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0259D21D-7637-313B-8049-6897F3950080
-  Functions: 22
+  UUID: 777B312D-41D7-3D8E-BFBA-E9E78B8947D1
+  Functions: 26
   Symbols:   47
-  CStrings:  108
+  CStrings:  140
 
Symbols:
+ _objc_retain_x19
- __os_log_impl
CStrings:
+ "@28@0:8I16@20"
+ "@36@0:8I16I20@24C32"
+ "ACParseSuccessful"
+ "ACReadError"
+ "AppleHPM"
+ "AppleHPMType3"
+ "AppleHPMType6"
+ "AutoLoadError"
+ "BootStage"
+ "CPROReadError"
+ "ErrorCode"
+ "ErrorCount"
+ "ErrorDevice"
+ "ErrorInstructionOffset"
+ "LastReset"
+ "OTPACParseError"
+ "OTPErrorOffset"
+ "SIDReadError"
+ "SRAMACParseError"
+ "StringTableLoadedFromAC"
+ "VendorZoneError"
+ "com.apple.usbctelemetryd.reset_reasons_type6"
+ "createWithBusService:andLogger:"
+ "getEventName"
+ "initializeWithHPMDeviceService:andHPMInterfaceService:andLogger:atRid:"
- "AppleHPMManager"
- "Not matching on non Type-3 Devices!\n"
- "^{__CFDictionary=}"
- "create"
- "dataDict"
- "hpmBusDict"
- "hpmDeviceDict"
- "hpmInterfaceDict"
- "i28@0:8I16@20"
- "initialize:withLogger:"

```
