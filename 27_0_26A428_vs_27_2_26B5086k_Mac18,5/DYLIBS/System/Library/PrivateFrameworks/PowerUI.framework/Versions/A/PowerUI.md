## PowerUI

> `/System/Library/PrivateFrameworks/PowerUI.framework/Versions/A/PowerUI`

```diff

-753.0.16.0.0
-  __TEXT.__text: 0xc5ed8
-  __TEXT.__objc_methlist: 0x1bbac
+753.40.6.0.0
+  __TEXT.__text: 0xc6068
+  __TEXT.__objc_methlist: 0x1bbc4
   __TEXT.__const: 0x6b8
-  __TEXT.__cstring: 0xd9b3
-  __TEXT.__oslogstring: 0xc010
-  __TEXT.__gcc_except_tab: 0xe08
+  __TEXT.__cstring: 0xda06
+  __TEXT.__oslogstring: 0xc084
+  __TEXT.__gcc_except_tab: 0xe0c
   __TEXT.__dlopen_cstrs: 0x62
-  __TEXT.__unwind_info: 0x2638
+  __TEXT.__unwind_info: 0x2640
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x638
+  __DATA_CONST.__const: 0x640
   __DATA_CONST.__objc_classlist: 0x378
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x52c0
+  __DATA_CONST.__objc_selrefs: 0x52d0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x340
   __DATA_CONST.__objc_arraydata: 0x70d8
   __DATA_CONST.__got: 0x4f0
   __AUTH_CONST.__const: 0x1810
-  __AUTH_CONST.__cfstring: 0xc660
+  __AUTH_CONST.__cfstring: 0xc6e0
   __AUTH_CONST.__objc_const: 0x35e30
   __AUTH_CONST.__objc_intobj: 0x9d8
   __AUTH_CONST.__objc_arrayobj: 0x498

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 10027
-  Symbols:   16554
-  CStrings:  2720
+  Functions: 10029
+  Symbols:   16559
+  CStrings:  2725
 
Symbols:
+ -[PowerUIIBLMNotificationManager displayUnusualDrainNotification]
+ -[PowerUIIBLMNotificationManager postIBLMNotificationWithTitleKey:bodyKey:identifier:category:]
+ -[PowerUISmartChargeManager loadDefaultsIsInitialLoad:]
+ GCC_except_table5
+ __95-[PowerUIIBLMNotificationManager postIBLMNotificationWithTitleKey:bodyKey:identifier:category:]_block_invoke
+ ___95-[PowerUIIBLMNotificationManager postIBLMNotificationWithTitleKey:bodyKey:identifier:category:]_block_invoke
+ _kIBLMUnusualDrainNotification
+ _objc_msgSend$loadDefaultsIsInitialLoad:
+ _objc_msgSend$postIBLMNotificationWithTitleKey:bodyKey:identifier:category:
- -[PowerUISmartChargeManager loadDefaults]
- __64-[PowerUIIBLMNotificationManager displayIBLMEngagedNotification]_block_invoke
- ___64-[PowerUIIBLMNotificationManager displayIBLMEngagedNotification]_block_invoke
- _objc_msgSend$loadDefaults
CStrings:
+ "IBLM-UnusualDrain"
+ "POWERUI_ADAPTIVE_POWER_FIRST_TIME_BODY"
+ "POWERUI_ADAPTIVE_POWER_FIRST_TIME_TITLE"
+ "POWERUI_ADAPTIVE_POWER_UNUSUAL_DRAIN_BODY"
+ "POWERUI_ADAPTIVE_POWER_UNUSUAL_DRAIN_TITLE"
+ "Posting onboarding Adaptive Power notification"
+ "Posting unusual-drain Adaptive Power notification"
+ "Reloading defaults due to defaults-changed notification"
+ "com.apple.osi.iblm.unusualDrainNotification"
+ "unusualDrainIBLMCategory"
- "/System/Library/UserNotifications/Bundles/com.apple.osintelligence.notifications.bundle"
- "ADAPTIVE_POWER_FIRST_TIME_BODY"
- "ADAPTIVE_POWER_FIRST_TIME_TITLE"
- "Localizable-IBLM"
- "Posting First time IBLM notification"
```
