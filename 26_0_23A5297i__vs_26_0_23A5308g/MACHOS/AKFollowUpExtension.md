## AKFollowUpExtension

> `/System/Library/PrivateFrameworks/AuthKitUI.framework/PlugIns/AKFollowUpExtension.appex/AKFollowUpExtension`

```diff

-518.1.0.0.0
-  __TEXT.__text: 0x62dc
-  __TEXT.__auth_stubs: 0x410
-  __TEXT.__objc_stubs: 0xf20
-  __TEXT.__objc_methlist: 0x2e4
-  __TEXT.__const: 0x88
-  __TEXT.__gcc_except_tab: 0x294
-  __TEXT.__cstring: 0x5c6
+520.0.0.0.0
+  __TEXT.__text: 0xa420
+  __TEXT.__auth_stubs: 0x260
+  __TEXT.__objc_stubs: 0x1040
+  __TEXT.__objc_methlist: 0x2ec
+  __TEXT.__const: 0x40
+  __TEXT.__gcc_except_tab: 0x5a4
+  __TEXT.__cstring: 0x62c
   __TEXT.__oslogstring: 0x6c8
   __TEXT.__objc_classname: 0x5d
-  __TEXT.__objc_methname: 0xf76
-  __TEXT.__objc_methtype: 0x34d
-  __TEXT.__unwind_info: 0x298
-  __DATA_CONST.__auth_got: 0x218
-  __DATA_CONST.__got: 0x148
-  __DATA_CONST.__const: 0x488
-  __DATA_CONST.__cfstring: 0x200
+  __TEXT.__objc_methname: 0x1080
+  __TEXT.__objc_methtype: 0x35e
+  __TEXT.__dlopen_cstrs: 0x1b
+  __TEXT.__unwind_info: 0x218
+  __DATA_CONST.__auth_got: 0x140
+  __DATA_CONST.__got: 0x188
+  __DATA_CONST.__const: 0x4f0
+  __DATA_CONST.__cfstring: 0x2c0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_intobj: 0x18
   __DATA.__objc_const: 0x3e0
-  __DATA.__objc_selrefs: 0x4b0
+  __DATA.__objc_selrefs: 0x4f8
   __DATA.__objc_ivar: 0x24
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0xc0

   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/UIKit.framework/UIKit
+  - /System/Library/PrivateFrameworks/AAAFoundation.framework/AAAFoundation
   - /System/Library/PrivateFrameworks/AuthKit.framework/AuthKit
   - /System/Library/PrivateFrameworks/AuthKitUI.framework/AuthKitUI
   - /System/Library/PrivateFrameworks/CoreFollowUpUI.framework/CoreFollowUpUI

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5DECA5FB-C838-3E6B-AE71-44F4423C0D25
-  Functions: 152
-  Symbols:   133
-  CStrings:  316
+  UUID: DDC51110-D5A3-3E67-A9DC-63A324769614
+  Functions: 115
+  Symbols:   114
+  CStrings:  339
 
Symbols:
+ _OBJC_CLASS_$_AAAFollowUpAnalyticsInfo
+ _OBJC_CLASS_$_AAFAnalyticsEvent
+ _OBJC_CLASS_$_AKAnalyticsReporterRTC
+ _OBJC_CLASS_$_NSUUID
+ _kAAFClickFollowupEvent
+ _kAKRTCEventCategoryAccountDataAccessRecovery
+ _memcpy
+ _memset
+ _objc_retainAutoreleasedReturnValue
- _objc_claimAutoreleasedReturnValue
- _objc_release_x19
- _objc_release_x20
- _objc_release_x21
- _objc_release_x22
- _objc_release_x23
- _objc_release_x24
- _objc_release_x25
- _objc_release_x26
- _objc_release_x27
- _objc_release_x28
- _objc_release_x8
- _objc_release_x9
- _objc_retain_x1
- _objc_retain_x19
- _objc_retain_x2
- _objc_retain_x20
- _objc_retain_x21
- _objc_retain_x22
- _objc_retain_x23
- _objc_retain_x24
- _objc_retain_x25
- _objc_retain_x26
- _objc_retain_x27
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x8
- _objc_retain_x9
CStrings:
+ "UUID"
+ "UUIDString"
+ "_handleAuthKitAction:forItem:telemetryFlowID:completion:"
+ "_handleURLKey:withAction:forItem:telemetryFlowID:completion:"
+ "_prepareAuthContextForAltDSID:telemetryFlowID:"
+ "analyticsEventWithName:eventCategory:followupAnalyticsData:altDSID:"
+ "application/json"
+ "application/x-apple-plist"
+ "application/x-plist"
+ "application/xml"
+ "rtcAnalyticsReporter"
+ "sendCFUClickedEventWithTelemetryFlowID:altDSID:identifier:"
+ "sendEvent:"
+ "setCfuType:"
+ "setFlowID:"
+ "setTelemetryFlowID:"
+ "softlink:o:fw:CoreFollowUp"
+ "text/plist"
+ "text/x-json"
+ "v40@0:8@16@24@32"
- "_handleAuthKitAction:forItem:completion:"
- "_handleURLKey:withAction:forItem:completion:"
- "_prepareAuthContextForAltDSID:"

```
