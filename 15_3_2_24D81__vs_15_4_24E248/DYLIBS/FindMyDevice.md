## FindMyDevice

> `/System/Library/PrivateFrameworks/FindMyDevice.framework/Versions/A/FindMyDevice`

```diff

-438.23.10.29.2
-  __TEXT.__text: 0x12a08
+438.24.7.11.24
+  __TEXT.__text: 0x12e08
   __TEXT.__auth_stubs: 0x2e0
-  __TEXT.__objc_methlist: 0x1158
-  __TEXT.__cstring: 0x351f
+  __TEXT.__objc_methlist: 0x1654
+  __TEXT.__cstring: 0x3563
   __TEXT.__const: 0xb0
   __TEXT.__gcc_except_tab: 0x2c4
-  __TEXT.__oslogstring: 0x10fb
-  __TEXT.__unwind_info: 0x4a0
+  __TEXT.__oslogstring: 0x1126
+  __TEXT.__unwind_info: 0x4c0
   __TEXT.__objc_classname: 0x3df
-  __TEXT.__objc_methname: 0x312b
-  __TEXT.__objc_methtype: 0x9e5
-  __TEXT.__objc_stubs: 0x2280
+  __TEXT.__objc_methname: 0x314f
+  __TEXT.__objc_methtype: 0xa11
+  __TEXT.__objc_stubs: 0x22c0
   __DATA_CONST.__got: 0x100
   __DATA_CONST.__const: 0xc38
   __DATA_CONST.__objc_classlist: 0xa8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xaf0
+  __DATA_CONST.__objc_selrefs: 0xc20
   __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_superrefs: 0x90
   __AUTH_CONST.__auth_got: 0x180
   __AUTH_CONST.__const: 0x940
   __AUTH_CONST.__cfstring: 0x3900
-  __AUTH_CONST.__objc_const: 0x4668
+  __AUTH_CONST.__objc_const: 0x3da0
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH.__objc_data: 0x690
   __DATA.__objc_ivar: 0x148

   - /System/Library/PrivateFrameworks/FMCoreLite.framework/Versions/A/FMCoreLite
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 79B93195-4240-353D-A4E6-C583A107D029
-  Functions: 551
-  Symbols:   1915
-  CStrings:  1801
+  UUID: DA3D2665-8484-3CFB-A720-812F061A72B4
+  Functions: 573
+  Symbols:   1939
+  CStrings:  1805
 
Symbols:
+ +[FMDFMMManager sharedInstance].cold.1
+ +[FMNSXPCConnectionCache sharedCache].cold.1
+ -[FMDFMMManager init].cold.1
+ -[FMDFMMManager simulatePushWithPayload:completion:]
+ LogCategory_ALFailureAnalytics.cold.1
+ LogCategory_Accessory.cold.1
+ LogCategory_AccountRatchet.cold.1
+ LogCategory_Automation.cold.1
+ LogCategory_Bluetooth_Session.cold.1
+ LogCategory_DisableLocationDisplay.cold.1
+ LogCategory_Encoder.cold.1
+ LogCategory_Extensions.cold.1
+ LogCategory_Extensions_PlaySound.cold.1
+ LogCategory_Locations.cold.1
+ LogCategory_OwnerAuthentication.cold.1
+ LogCategory_RepairDevice.cold.1
+ LogCategory_SecureLocations.cold.1
+ LogCategory_Traffic.cold.1
+ LogCategory_Unspecified.cold.1
+ __52-[FMDFMMManager simulatePushWithPayload:completion:]_block_invoke.128
+ __52-[FMDFMMManager simulatePushWithPayload:completion:]_block_invoke.cold.1
+ ___52-[FMDFMMManager simulatePushWithPayload:completion:]_block_invoke
+ _kLostModeChangedRestrictedNotification
+ _objc_msgSend$fmipConfiguration
+ _objc_msgSend$simulatePushWithPayload:completion:
- _kLostModeChangedNotification
CStrings:
+ "-[FMDFMMManager simulatePushWithPayload:completion:]"
+ "XPC error for simulatePushWithOptions: %li"
+ "com.apple.private.restrict-post.fmip.lostmode.enable"
+ "simulatePushWithPayload:completion:"
+ "v32@0:8@\"NSDictionary\"16@?<v@?@\"NSError\">24"
- "com.apple.icloud.fmip.lostmode.enable"

```
