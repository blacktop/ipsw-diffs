## WiFiAnalytics

> `/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics`

```diff

-610.5.0.0.0
-  __TEXT.__text: 0xefc74
+680.21.0.0.0
+  __TEXT.__text: 0xf00a4
   __TEXT.__auth_stubs: 0xf70
-  __TEXT.__objc_methlist: 0xc244
+  __TEXT.__objc_methlist: 0xc23c
   __TEXT.__const: 0x2b8
-  __TEXT.__cstring: 0xde8c
-  __TEXT.__oslogstring: 0xb05b
+  __TEXT.__cstring: 0xdef9
+  __TEXT.__oslogstring: 0xb182
   __TEXT.__swift5_typeref: 0x128
   __TEXT.__constg_swiftt: 0x178
   __TEXT.__swift5_reflstr: 0x61

   __TEXT.__unwind_info: 0x1c50
   __TEXT.__eh_frame: 0x670
   __TEXT.__objc_classname: 0xaaf
-  __TEXT.__objc_methname: 0x19025
+  __TEXT.__objc_methname: 0x19046
   __TEXT.__objc_methtype: 0x3487
-  __TEXT.__objc_stubs: 0x8de0
+  __TEXT.__objc_stubs: 0x8e00
   __DATA_CONST.__got: 0x638
   __DATA_CONST.__const: 0x1968
   __DATA_CONST.__objc_classlist: 0x2d8
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6b80
+  __DATA_CONST.__objc_selrefs: 0x6b88
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x238
   __DATA_CONST.__objc_arraydata: 0xf0
   __AUTH_CONST.__auth_got: 0x7c8
   __AUTH_CONST.__auth_ptr: 0x30
   __AUTH_CONST.__const: 0x1350
-  __AUTH_CONST.__cfstring: 0xb120
+  __AUTH_CONST.__cfstring: 0xb160
   __AUTH_CONST.__objc_const: 0x10dc8
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_arrayobj: 0x180
   __AUTH.__objc_data: 0x3b8
   __DATA.__objc_ivar: 0xc70
   __DATA.__data: 0x1f8
-  __DATA.__common: 0x11d0
-  __DATA.__bss: 0x10
+  __DATA.__common: 0x11e0
+  __DATA.__bss: 0x18
   __DATA_DIRTY.__objc_data: 0x1a90
   __DATA_DIRTY.__data: 0xa0
   __DATA_DIRTY.__bss: 0xd8
-  __DATA_DIRTY.__common: 0x28
+  __DATA_DIRTY.__common: 0x18
   - /System/Library/Frameworks/CoreData.framework/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 4581
-  Symbols:   5900
-  CStrings:  8229
+  Functions: 4580
+  Symbols:   5898
+  CStrings:  8241
 
Symbols:
+ _WALogCategoryDeviceStoreHandle
- _WAInitLogging
- _WALogCategoryDefault
CStrings:
+ "%!{(MISSING)public}s::%!d(MISSING):Initing AnalyticsStoreMOHandler with AnalyticsProcessorMigrationCapable - this should only be proc wifianalyticsd"
+ "%!{(MISSING)public}s::%!d(MISSING):Migration not enabled on this process.. bailing!"
+ "%!{(MISSING)public}s::%!d(MISSING):Store at URL %!@(MISSING) may need migration"
+ "%!{(MISSING)public}s::%!d(MISSING):WADeviceAnalyticsClient version: %!s(MISSING)"
+ "%!{(MISSING)public}s::%!d(MISSING):WiFiClient version: %!s(MISSING)"
+ "%!{(MISSING)public}s::%!d(MISSING):deleted %!@(MISSING)"
+ "%!{(MISSING)public}s::%!d(MISSING):failed to create wifianalytics tmp directory (%!@(MISSING)) with error %!@(MISSING)"
+ "%!{(MISSING)public}s::%!d(MISSING):failed to delete %!@(MISSING) with error %!@(MISSING)"
+ "%!{(MISSING)public}s::%!d(MISSING):nil wifianalyticsTmpDirectory"
+ "+[WAUtil wifianalyticsTmpDirectory]"
+ "-[WAClient _initPrivate]"
+ "/var/log/com.apple.wifi.analytics"
+ "/var/tmp/com.apple.wifianalyticsd"
+ "AnalyticsStoreDump"
+ "DeviceStore"
+ "WiFiAnalytics-680.21 Oct 16 2024 13:46:58"
+ "WiFiAnalytics-680.21 Oct 16 2024 13:47:00"
+ "fileURLWithPath:isDirectory:"
+ "removeItemAtURL:error:"
+ "wifianalytics_%!@(MISSING)_%!l(MISSING)u.json"
- "%!{(MISSING)public}s::%!d(MISSING):Incompatible store at URL %!@(MISSING)"
- "%!{(MISSING)public}s::%!d(MISSING):Initting AnalyticsStoreMOHandler with AnalyticsProcessorMigrationCapable - this should only be proc wifianalyticsd"
- "%!{(MISSING)public}s::%!d(MISSING):Will not migrate incompatible store.. bailing!"
- "-[WAClient wifianalyticsTmpDirectory]"
- "/var/tmp/com.apple.wifianalyticsd/wifianalytics"
- "com.apple.wifianalyticsd/AnalyticsStoreDump"
- "temporaryDirectory"
- "void KeepDbEmptyErrorMsg(void)"

```
