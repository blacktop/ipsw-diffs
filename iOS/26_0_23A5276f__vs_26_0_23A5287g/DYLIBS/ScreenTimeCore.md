## ScreenTimeCore

> `/System/Library/PrivateFrameworks/ScreenTimeCore.framework/ScreenTimeCore`

```diff

-580.0.0.0.0
-  __TEXT.__text: 0xb1858
-  __TEXT.__auth_stubs: 0x1530
-  __TEXT.__objc_methlist: 0x8528
+588.0.0.0.0
+  __TEXT.__text: 0xb1c28
+  __TEXT.__auth_stubs: 0x1540
+  __TEXT.__objc_methlist: 0x8570
   __TEXT.__const: 0x1c50
-  __TEXT.__cstring: 0x9e98
+  __TEXT.__cstring: 0x9f08
   __TEXT.__oslogstring: 0x9a2c
   __TEXT.__gcc_except_tab: 0x1c88
   __TEXT.__constg_swiftt: 0x824

   __TEXT.__swift5_assocty: 0xc0
   __TEXT.__swift5_proto: 0x188
   __TEXT.__swift5_types: 0x90
-  __TEXT.__swift5_capture: 0x150
+  __TEXT.__swift5_capture: 0x160
   __TEXT.__swift_as_entry: 0x14
   __TEXT.__swift_as_ret: 0x18
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x2ab8
-  __TEXT.__eh_frame: 0xc50
-  __TEXT.__objc_classname: 0x1801
-  __TEXT.__objc_methname: 0x15b63
-  __TEXT.__objc_methtype: 0x238e
-  __TEXT.__objc_stubs: 0xcfc0
+  __TEXT.__unwind_info: 0x2ae0
+  __TEXT.__eh_frame: 0xc78
+  __TEXT.__objc_classname: 0x182a
+  __TEXT.__objc_methname: 0x15c3d
+  __TEXT.__objc_methtype: 0x23cc
+  __TEXT.__objc_stubs: 0xd000
   __DATA_CONST.__got: 0xb40
   __DATA_CONST.__const: 0x1998
-  __DATA_CONST.__objc_classlist: 0x5d0
+  __DATA_CONST.__objc_classlist: 0x5d8
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x1d0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x47d0
+  __DATA_CONST.__objc_selrefs: 0x47d8
   __DATA_CONST.__objc_protorefs: 0x108
-  __DATA_CONST.__objc_superrefs: 0x450
+  __DATA_CONST.__objc_superrefs: 0x458
   __DATA_CONST.__objc_arraydata: 0x250
-  __AUTH_CONST.__auth_got: 0xaa8
-  __AUTH_CONST.__const: 0x16c8
-  __AUTH_CONST.__cfstring: 0x8720
-  __AUTH_CONST.__objc_const: 0xfbc0
+  __AUTH_CONST.__auth_got: 0xab0
+  __AUTH_CONST.__const: 0x16f0
+  __AUTH_CONST.__cfstring: 0x87a0
+  __AUTH_CONST.__objc_const: 0xfcf8
   __AUTH_CONST.__objc_intobj: 0x168
   __AUTH_CONST.__objc_arrayobj: 0x180
   __AUTH_CONST.__objc_dictobj: 0xc8
-  __AUTH.__objc_data: 0x2ef8
+  __AUTH.__objc_data: 0x2f48
   __AUTH.__data: 0x240
-  __DATA.__objc_ivar: 0x5d4
+  __DATA.__objc_ivar: 0x5dc
   __DATA.__data: 0x1a08
   __DATA.__bss: 0x30b0
   __DATA.__common: 0x68

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 7CCFA9E0-DAEA-3509-9B39-C11D74741A21
-  Functions: 4295
-  Symbols:   11460
-  CStrings:  6724
+  UUID: 43419C4D-8A5A-3DFE-B4E4-58EA3AA1459A
+  Functions: 4304
+  Symbols:   11485
+  CStrings:  6738
 
Symbols:
+ +[STScreenTimePopulationCoreAnalyticsEvent description]
+ -[STScreenTimePopulationCoreAnalyticsEvent initWithIsScreenTimeEnabled:isShareAcrossDevicesEnabled:]
+ -[STScreenTimePopulationCoreAnalyticsEvent isScreenTimeEnabled]
+ -[STScreenTimePopulationCoreAnalyticsEvent isShareAcrossDevicesEnabled]
+ -[STScreenTimePopulationCoreAnalyticsEvent name]
+ -[STScreenTimePopulationCoreAnalyticsEvent payload]
+ _OBJC_CLASS_$_STScreenTimePopulationCoreAnalyticsEvent
+ _OBJC_IVAR_$_STScreenTimePopulationCoreAnalyticsEvent._isScreenTimeEnabled
+ _OBJC_IVAR_$_STScreenTimePopulationCoreAnalyticsEvent._isShareAcrossDevicesEnabled
+ _OBJC_METACLASS_$_STScreenTimePopulationCoreAnalyticsEvent
+ __OBJC_$_CLASS_METHODS_STScreenTimePopulationCoreAnalyticsEvent
+ __OBJC_$_INSTANCE_METHODS_STScreenTimePopulationCoreAnalyticsEvent
+ __OBJC_$_INSTANCE_VARIABLES_STScreenTimePopulationCoreAnalyticsEvent
+ __OBJC_$_PROP_LIST_STScreenTimePopulationCoreAnalyticsEvent
+ __OBJC_CLASS_PROTOCOLS_$_STScreenTimePopulationCoreAnalyticsEvent
+ __OBJC_CLASS_RO_$_STScreenTimePopulationCoreAnalyticsEvent
+ __OBJC_METACLASS_RO_$_STScreenTimePopulationCoreAnalyticsEvent
+ _objc_msgSend$isScreenTimeEnabled
+ _objc_msgSend$isShareAcrossDevicesEnabled
CStrings:
+ "@24@0:8B16B20"
+ "DailyScreenTimePopulation"
+ "STScreenTimePopulationCoreAnalyticsEvent"
+ "TB,R,V_isScreenTimeEnabled"
+ "TB,R,V_isShareAcrossDevicesEnabled"
+ "WaitForAuth"
+ "_isScreenTimeEnabled"
+ "_isShareAcrossDevicesEnabled"
+ "com.apple.ScreenTime.dailyScreenTimePopulation"
+ "fetchAllWebApplicationHistory:profileIdentifier:clientBundleURLWrapper:replyHandler:"
+ "fetchHistoryDuringInterval:webApplication:profileIdentifier:clientBundleURLWrapper:replyHandler:"
+ "initWithIsScreenTimeEnabled:isShareAcrossDevicesEnabled:"
+ "isScreenTimeEnabled"
+ "isShareAcrossDevicesEnabled"
+ "loadEncodedSettingsForEncodedUser:withEncodedDefaults:completion:"
+ "saveEncodedDefaults:forEncodedUser:completion:"
+ "saveEncodedSettings:forEncodedUser:completion:"
+ "v40@0:8@\"NSData\"16@\"NSData\"24@?<v@?@\"NSData\"@\"NSError\">32"
+ "v40@0:8@\"NSData\"16@\"NSData\"24@?<v@?@\"NSError\">32"
+ "v48@0:8@\"NSString\"16@\"NSString\"24@\"NSSecurityScopedURLWrapper\"32@?<v@?@\"NSSet\"@\"NSError\">40"
+ "v56@0:8@\"NSDateInterval\"16@\"NSString\"24@\"NSString\"32@\"NSSecurityScopedURLWrapper\"40@?<v@?@\"NSSet\"@\"NSError\">48"
- "WaitForPasscode"
- "clearEncodedSettingsDefaultsWithCompletion:"
- "fetchAllWebApplicationHistory:profileIdentifier:replyHandler:"
- "fetchHistoryDuringInterval:webApplication:profileIdentifier:replyHandler:"
- "loadEncodedSettingsDefaultsWithCompletion:"
- "loadEncodedSettingsForEncodedUser:completion:"
- "saveEncodedSettings:completion:"
- "saveEncodedSettingsDefaults:completion:"
- "v24@0:8@?<v@?@\"NSData\"@\"NSError\">16"
- "v32@0:8@\"NSData\"16@?<v@?@\"NSData\"@\"NSError\">24"
- "v32@0:8@\"NSData\"16@?<v@?@\"NSError\">24"
- "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"NSSet\"@\"NSError\">32"
- "v48@0:8@\"NSDateInterval\"16@\"NSString\"24@\"NSString\"32@?<v@?@\"NSSet\"@\"NSError\">40"

```
