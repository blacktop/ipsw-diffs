## CTFollowUpExtension

> `/System/Library/Frameworks/CoreTelephony.framework/PlugIns/CTFollowUpExtension.appex/CTFollowUpExtension`

```diff

-13187.6.0.0.0
-  __TEXT.__text: 0x1768
-  __TEXT.__auth_stubs: 0x230
-  __TEXT.__objc_stubs: 0x5a0
-  __TEXT.__objc_methlist: 0x50
+13466.3.0.0.0
+  __TEXT.__text: 0x1bd0
+  __TEXT.__auth_stubs: 0x240
+  __TEXT.__objc_stubs: 0x660
+  __TEXT.__objc_methlist: 0x74
   __TEXT.__const: 0x40
-  __TEXT.__cstring: 0x303
-  __TEXT.__oslogstring: 0x141
-  __TEXT.__objc_classname: 0x1e
-  __TEXT.__objc_methname: 0x4b0
-  __TEXT.__objc_methtype: 0x5c
-  __TEXT.__unwind_info: 0x90
-  __DATA_CONST.__auth_got: 0x120
-  __DATA_CONST.__got: 0xa0
+  __TEXT.__cstring: 0x517
+  __TEXT.__oslogstring: 0x222
+  __TEXT.__objc_classname: 0x1c
+  __TEXT.__objc_methname: 0x594
+  __TEXT.__objc_methtype: 0x6a
+  __TEXT.__unwind_info: 0xa0
   __DATA_CONST.__const: 0x68
-  __DATA_CONST.__cfstring: 0x440
+  __DATA_CONST.__cfstring: 0x5c0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_intobj: 0x78
+  __DATA_CONST.__auth_got: 0x128
+  __DATA_CONST.__got: 0xb0
   __DATA.__objc_const: 0xb8
-  __DATA.__objc_selrefs: 0x178
+  __DATA.__objc_selrefs: 0x1a8
   __DATA.__objc_ivar: 0x4
   __DATA.__objc_data: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B814CE29-613F-30CD-937E-9B09DB0F8F66
-  Functions: 15
-  Symbols:   65
-  CStrings:  134
+  UUID: 1AE65DE6-458A-3748-90C7-A0D2DC6AD10D
+  Functions: 16
+  Symbols:   68
+  CStrings:  167
 
Symbols:
+ _OBJC_CLASS_$_NSCharacterSet
+ _OBJC_CLASS_$_NSString
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x8
- _objc_retain
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x22
- _objc_retain_x25
- _objc_retain_x26
CStrings:
+ ""
+ "DeviceModel"
+ "Followup did open QS enrollment prefs url %@ with success %d error %@"
+ "Followup did open QS websheet incomplete info prefs url %@ with success %d error %@"
+ "Followup did open plan available prefs url %@ with success %d error %@"
+ "PhoneNumber"
+ "URLQueryAllowedCharacterSet"
+ "com.followup.available"
+ "com.followup.qs-enrollment"
+ "com.followup.qs-no-wifi"
+ "com.followup.qs-websheet-incomplete-info"
+ "handleCellularPlanAvailable:"
+ "handleQuickSwitchEnrollmentItem:sliding:"
+ "handleQuickSwitchWebsheetIncompleteInfoItem:selectedAction:"
+ "no"
+ "prefs:root=MOBILE_DATA_SETTINGS_ID&path=CELLULAR&client=com.apple.CommCenter&type=quickSwitch&flow=enroll&sliding=%@"
+ "prefs:root=MOBILE_DATA_SETTINGS_ID&path=CELLULAR&client=com.apple.CommCenter&type=quickSwitch&flow=followUp&phoneNumber=%@&deviceModel=%@"
+ "prefs:root=MOBILE_DATA_SETTINGS_ID&path=CELLULAR/SIM_CONFIGURATION_SETTINGS&client=com.apple.CommCenter&type=simConfig&action=1"
+ "stringByAddingPercentEncodingWithAllowedCharacters:"
+ "stringWithFormat:"
+ "v28@0:8@16B24"
+ "yes"

```
