## nfcd

> `/usr/libexec/nfcd`

```diff

-  __TEXT.__text: 0x1fa1f4
-  __TEXT.__auth_stubs: 0x17c0
+  __TEXT.__text: 0x1fafcc
+  __TEXT.__auth_stubs: 0x17f0
   __TEXT.__delay_stubs: 0x500
   __TEXT.__delay_helper: 0x16f4
-  __TEXT.__objc_stubs: 0xdbc0
-  __TEXT.__objc_methlist: 0x9d58
-  __TEXT.__const: 0x1384
-  __TEXT.__objc_methname: 0x15490
-  __TEXT.__cstring: 0x226f5
-  __TEXT.__objc_classname: 0x1e0e
-  __TEXT.__objc_methtype: 0x4ec6
-  __TEXT.__oslogstring: 0x1fc1d
-  __TEXT.__unwind_info: 0x2e88
-  __DATA_CONST.__auth_got: 0xc88
-  __DATA_CONST.__got: 0x628
+  __TEXT.__objc_stubs: 0xdd20
+  __TEXT.__objc_methlist: 0x9dd8
+  __TEXT.__const: 0x13a4
+  __TEXT.__objc_methname: 0x156da
+  __TEXT.__cstring: 0x2280e
+  __TEXT.__objc_classname: 0x1e31
+  __TEXT.__objc_methtype: 0x4ee2
+  __TEXT.__oslogstring: 0x1fd16
+  __TEXT.__unwind_info: 0x2eb0
+  __DATA_CONST.__auth_got: 0xca0
+  __DATA_CONST.__got: 0x630
   __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__const: 0x9958
+  __DATA_CONST.__const: 0x9998
   __DATA_CONST.__cfstring: 0x11840
-  __DATA_CONST.__objc_classlist: 0x630
+  __DATA_CONST.__objc_classlist: 0x640
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x398
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x1e8
-  __DATA_CONST.__objc_superrefs: 0x470
+  __DATA_CONST.__objc_superrefs: 0x480
   __DATA_CONST.__objc_intobj: 0x7a28
   __DATA_CONST.__objc_arraydata: 0x1dd8
   __DATA_CONST.__objc_arrayobj: 0x2e8
   __DATA_CONST.__objc_dictobj: 0xfc8
-  __DATA.__objc_const: 0x14bb0
-  __DATA.__objc_selrefs: 0x4ab8
-  __DATA.__objc_ivar: 0x10e0
-  __DATA.__objc_data: 0x3de0
+  __DATA.__objc_const: 0x14e20
+  __DATA.__objc_selrefs: 0x4b18
+  __DATA.__objc_ivar: 0x1108
+  __DATA.__objc_data: 0x3e80
   __DATA.__data: 0x2bf4
-  __DATA.__bss: 0x2a0
+  __DATA.__bss: 0x2c8
   __DATA.__common: 0x12
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /System/Library/PrivateFrameworks/CPMS.framework/CPMS
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreDuetContext.framework/CoreDuetContext
+  - /System/Library/PrivateFrameworks/CoreTime.framework/CoreTime
   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
   - /System/Library/PrivateFrameworks/HID.framework/HID
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration

   - /usr/lib/libTelephonyBasebandDynamic.dylib
   - /usr/lib/libnfshared.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 4221
-  Symbols:   594
-  CStrings:  13815
+  Functions: 4235
+  Symbols:   598
+  CStrings:  13846
 
Sections:
~ __DATA_CONST.__auth_ptr : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__objc_arrayobj : content changed
~ __DATA_CONST.__objc_dictobj : content changed
~ __DATA.__data : content changed
Symbols:
+ _CFAbsoluteTimeGetCurrent
+ _NSSystemClockDidChangeNotification
+ _TMGetReferenceTime
+ _TMIsAutomaticTimeEnabled
CStrings:
+ "%{public}s:%i Cannot add receipt for %{public}@/%{public}@"
+ "%{public}s:%i Could not get reference time"
+ "%{public}s:%i Fetched reference time interval: %.3f, user delta: %.3f, uncertainty: %.3f"
+ "%{public}s:%i Untrusted time source, need to query server"
+ "-[NFPaymentTagReaderDeveloperPresentmentLogger checkAvailabilityForBundleID:teamID:completion:]"
+ "-[NFPaymentTagReaderDeveloperPresentmentReporter _getFirstReportForBundleID:teamID:olderThanTimestampDay:]"
+ "-[NFPaymentTagReaderDeveloperPresentmentReporter checkLocalAvailabilityForBundleID:teamID:]"
+ "-[NFTrustedTimeSource getTime]"
+ "-[NFTrustedTimeSource handleSystemTimeChanged:]"
+ "@40@0:8@16d24Q32"
+ "NFCD built from (B&I) Stockholm_Base-366.8"
+ "NFTrustedTime"
+ "NFTrustedTimeSource"
+ "_cachedReferenceAbsTimeSec"
+ "_cachedReferenceMachTimeSec"
+ "_getFirstReportForBundleID:teamID:olderThanTimestampDay:"
+ "_locationReceivedAfterSessionStart"
+ "_monotonicCounterSeconds"
+ "_observerRegistered"
+ "_refreshTimeSyncSetting:"
+ "_timeSyncSettingCacheTime"
+ "_timeSyncedWithAutoTimeEnabled"
+ "_updateCachedAbsTime:machTime:"
+ "addObserver:selector:name:object:"
+ "convertMachContinuousTicksToSeconds:"
+ "d24@0:8Q16"
+ "fetchDeveloperPaymentReportsForBundleID:teamID:outError:"
+ "handleSystemTimeChanged:"
+ "initWithDate:monotonicCounterSeconds:source:"
+ "initWithTimeIntervalSinceReferenceDate:"
+ "machContinuousTimeSeconds"
+ "removeObserver:"
+ "timeIntervalSinceReferenceDate"
+ "timestampDay"
+ "v32@0:8d16d24"
+ "\xf0Qa"
- "-[NFPaymentTagReaderDeveloperPresentmentReporter _checkLocalAvailabilityForBundleID:teamID:]"
- "I32@0:8@16@24"
- "NFCD built from (B&I) Stockholm_Base-366.6"
- "_checkLocalAvailabilityForBundleID:teamID:"
- "\xf0Aa"

```
