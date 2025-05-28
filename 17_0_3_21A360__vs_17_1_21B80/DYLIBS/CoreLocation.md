## CoreLocation

> `/System/Library/Frameworks/CoreLocation.framework/CoreLocation`

```diff

-2886.1.7.0.0
-  __TEXT.__text: 0x10acbc
+2890.0.8.0.5
+  __TEXT.__text: 0x10b154
   __TEXT.__auth_stubs: 0x17e0
-  __TEXT.__objc_methlist: 0x7dec
-  __TEXT.__const: 0x2458
-  __TEXT.__gcc_except_tab: 0x6f88
-  __TEXT.__oslogstring: 0x1d3a1
-  __TEXT.__cstring: 0x1625b
+  __TEXT.__objc_methlist: 0x7dfc
+  __TEXT.__const: 0x2460
+  __TEXT.__gcc_except_tab: 0x6fb4
+  __TEXT.__oslogstring: 0x1d6e7
+  __TEXT.__cstring: 0x16263
   __TEXT.__ustring: 0x750
-  __TEXT.__unwind_info: 0x4228
+  __TEXT.__unwind_info: 0x4238
   __TEXT.__eh_frame: 0x38
   __TEXT.__objc_classname: 0x11b6
-  __TEXT.__objc_methname: 0x17148
+  __TEXT.__objc_methname: 0x17170
   __TEXT.__objc_methtype: 0x578f
   __TEXT.__objc_stubs: 0xba80
   __DATA_CONST.__got: 0x198

   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0xefe8
-  __DATA_CONST.__objc_selrefs: 0x44c8
+  __DATA_CONST.__objc_selrefs: 0x44d0
   __DATA_CONST.__objc_arraydata: 0x58
   __AUTH_CONST.__const: 0x2a88
-  __AUTH_CONST.__cfstring: 0x86a0
+  __AUTH_CONST.__cfstring: 0x86e0
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_const: 0x45a8
   __AUTH_CONST.__objc_doubleobj: 0x10

   __DATA.__objc_classrefs: 0x538
   __DATA.__objc_superrefs: 0x440
   __DATA.__objc_ivar: 0x8e0
-  __DATA.__data: 0xf68
+  __DATA.__data: 0xf88
   __DATA.__common: 0x150
-  __DATA.__bss: 0x300
+  __DATA.__bss: 0x2f8
   __DATA_DIRTY.__objc_ivar: 0x58
   __DATA_DIRTY.__objc_data: 0x7d0
   __DATA_DIRTY.__data: 0x88
   __DATA_DIRTY.__common: 0x68
-  __DATA_DIRTY.__bss: 0x1ba8
+  __DATA_DIRTY.__bss: 0x1bb8
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreData.framework/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libxml2.2.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 4019
+  Functions: 4020
   Symbols:   911
-  CStrings:  7458
+  CStrings:  7464
 
CStrings:
+ "02:21:57"
+ "CL: CLBackgroundActivitySession #backgroundActivitySession"
+ "CL: CLClearLocationAuthorization"
+ "CL: CLLocationUpdater #locationUpdater"
+ "CL: CLMonitor #monitor"
+ "CL: CLMonitorConfiguration #monitor"
+ "CLTSP,processData,input,tripSegmentID,%{public}s,modeOfTransport,%{public}ld,sparseLocationsCount,%{public}d,startTime,%{public}.1lf,endTime,%{public}.1lf,crumbDuration,%{public}.lf"
+ "CLTSP,too long trip segment,%{public}.lf,seconds"
+ "Oct 10 2023"
+ "initWithName:path:onQueue:eventHandler:"
+ "kCLConnectionMessageLocationUpdaterEndDateKey"
+ "kCLConnectionMessageLocationUpdaterStartDateKey"
+ "kCLConnectionMessageTranscriptFetchCenterLatitudeKey"
+ "kCLConnectionMessageTranscriptFetchCenterLongitudeKey"
+ "{\"msg%{public}.0s\":\"#locationUpdater historicalUpdaterWithCenter:radius:dateInterval:sampleCount:queue:handler: created\", \"updater\":\"%{public}p\"}"
+ "{\"msg%{public}.0s\":\"#locationUpdater historicalUpdaterWithDateInterval:sampleCount:sampleCount:queue:handler: created\", \"updater\":\"%{public}p\"}"
+ "{\"msg%{public}.0s\":\"#locationUpdater liveUpdaterWithConfiguration:queue:handler: created\", \"updater\":\"%{public}p\"}"
+ "{\"msg%{public}.0s\":\"CLBackgroundActivitySession #backgroundActivitySession\", \"event\":%{public, location:escape_only}s, \"_cmd\":%{public, location:escape_only}@, \"self\":\"%{public}p\", \"manager\":\"%{public}p\"}"
+ "{\"msg%{public}.0s\":\"CLBackgroundActivitySession #backgroundActivitySession\", \"event\":%{public, location:escape_only}s, \"_cmd\":%{public, location:escape_only}@, \"self\":\"%{public}p\", \"message\":%{public, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"CLBackgroundActivitySession #backgroundActivitySession\", \"event\":%{public, location:escape_only}s, \"_cmd\":%{public, location:escape_only}@, \"self\":\"%{public}p\"}"
+ "{\"msg%{public}.0s\":\"CLClearLocationAuthorization\", \"event\":%{public, location:escape_only}s, \"bundleId\":%{public, location:escape_only}@, \"bundlePath\":%{public, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"CLLocationManager\", \"event\":%{public, location:escape_only}s, \"_cmd\":%{public, location:escape_only}@, \"self\":\"%{public}p\", \"clientKey\":%{public, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"CLLocationUpdater #locationUpdater\", \"event\":%{public, location:escape_only}s, \"_cmd\":%{public, location:escape_only}@, \"self\":\"%{public}p\", \"message\":%{public, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"CLLocationUpdater #locationUpdater\", \"event\":%{public, location:escape_only}s, \"_cmd\":%{public, location:escape_only}@, \"self\":\"%{public}p\", \"name\":%{public, location:escape_only}s, \"messagePayload\":%{private, location:escape_only}@, \"manager\":\"%{public}p\"}"
+ "{\"msg%{public}.0s\":\"CLLocationUpdater #locationUpdater\", \"event\":%{public, location:escape_only}s, \"_cmd\":%{public, location:escape_only}@, \"self\":\"%{public}p\", \"payload\":%{private, location:escape_only}@, \"isStationary\":%{public}hhd}"
+ "{\"msg%{public}.0s\":\"CLLocationUpdater #locationUpdater\", \"event\":%{public, location:escape_only}s, \"_cmd\":%{public, location:escape_only}@, \"self\":\"%{public}p\", \"payload\":%{private, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"CLLocationUpdater #locationUpdater\", \"event\":%{public, location:escape_only}s, \"_cmd\":%{public, location:escape_only}@, \"self\":\"%{public}p\"}"
+ "{\"msg%{public}.0s\":\"CLMonitor #monitor\", \"event\":%{public, location:escape_only}s, \"_cmd\":%{public, location:escape_only}@, \"self\":\"%{public}p\", \"identifier\":%{public, location:escape_only}@, \"assumedState\":%{public, location:CLMonitoringState}lld}"
+ "{\"msg%{public}.0s\":\"CLMonitor #monitor\", \"event\":%{public, location:escape_only}s, \"_cmd\":%{public, location:escape_only}@, \"self\":\"%{public}p\", \"identifier\":%{public, location:escape_only}@, \"event\":%{public, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"CLMonitor #monitor\", \"event\":%{public, location:escape_only}s, \"_cmd\":%{public, location:escape_only}@, \"self\":\"%{public}p\", \"identifier\":%{public, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"CLMonitor #monitor\", \"event\":%{public, location:escape_only}s, \"_cmd\":%{public, location:escape_only}@, \"self\":\"%{public}p\", \"name\":%{public, location:escape_only}@, \"authIdentity\":%{private, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"CLMonitor #monitor\", \"event\":%{public, location:escape_only}s, \"_cmd\":%{public, location:escape_only}@, \"self\":\"%{public}p\", \"name\":%{public, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"CLMonitor #monitor\", \"event\":%{public, location:escape_only}s, \"_cmd\":%{public, location:escape_only}@, \"self\":\"%{public}p\"}"
+ "{\"msg%{public}.0s\":\"CLMonitorConfiguration #monitor\", \"event\":%{public, location:escape_only}s, \"_cmd\":%{public, location:escape_only}@, \"self\":\"%{public}p\", \"attributes\":%{private, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"CLMonitorConfiguration #monitor\", \"event\":%{public, location:escape_only}s, \"_cmd\":%{public, location:escape_only}@, \"self\":\"%{public}p\", \"name\":%{public, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"CLMonitorConfiguration #monitor\", \"event\":%{public, location:escape_only}s, \"_cmd\":%{public, location:escape_only}@, \"self\":\"%{public}p\"}"
- "+[CLLocationUpdater _historicalUpdaterWithCenter:radius:dateInterval:sampleCount:queue:handler:]"
- "17:19:39"
- "CL: CLBackgroundActivitySession"
- "CL: CLLocationUpdater"
- "CL: CLMonitor"
- "CL: CLMonitorConfiguration"
- "CLTSP,processData,input,tripSegmentID,%{public}s,modeOfTransport,%{public}ld,sparseLocationsCount,%{public}d,startTime,%{public}.1lf,endTime,%{public}.1lf"
- "Sep 30 2023"
- "kCLConnectionMessageLocationUpdaterDateIntervalKey"
- "kCLConnectionMessageTranscriptFetchCenterKey"
- "{\"msg%{public}.0s\":\"#identityValidation registration payload\", \"payload\":%{public, location:escape_only}s}"
- "{\"msg%{public}.0s\":\"#locationUpdater historicalUpdaterWithDateInterval:sampleCount:sampleCount:queue:handler: created\", \"self\":\"%{public}p\"}"
- "{\"msg%{public}.0s\":\"#locationUpdater liveUpdaterWithConfiguration:queue:handler: created\", \"self\":\"%{public}p\"}"
- "{\"msg%{public}.0s\":\"CLBackgroundActivitySession\", \"event\":%{public, location:escape_only}s, \"_cmd\":%{public, location:escape_only}@, \"self\":\"%{public}p\", \"manager\":\"%{public}p\"}"
- "{\"msg%{public}.0s\":\"CLBackgroundActivitySession\", \"event\":%{public, location:escape_only}s, \"_cmd\":%{public, location:escape_only}@, \"self\":\"%{public}p\", \"message\":%{public, location:escape_only}s}"
- "{\"msg%{public}.0s\":\"CLBackgroundActivitySession\", \"event\":%{public, location:escape_only}s, \"_cmd\":%{public, location:escape_only}@, \"self\":\"%{public}p\"}"
- "{\"msg%{public}.0s\":\"CLLocationUpdater\", \"event\":%{public, location:escape_only}s, \"_cmd\":%{public, location:escape_only}@, \"self\":\"%{public}p\", \"message\":%{public, location:escape_only}s}"
- "{\"msg%{public}.0s\":\"CLLocationUpdater\", \"event\":%{public, location:escape_only}s, \"_cmd\":%{public, location:escape_only}@, \"self\":\"%{public}p\", \"name\":%{public, location:escape_only}s, \"messagePayload\":%{private, location:escape_only}@, \"manager\":\"%{public}p\"}"
- "{\"msg%{public}.0s\":\"CLLocationUpdater\", \"event\":%{public, location:escape_only}s, \"_cmd\":%{public, location:escape_only}@, \"self\":\"%{public}p\", \"payload\":%{private, location:escape_only}@, \"isStationary\":%{public}hhd}"
- "{\"msg%{public}.0s\":\"CLLocationUpdater\", \"event\":%{public, location:escape_only}s, \"_cmd\":%{public, location:escape_only}@, \"self\":\"%{public}p\", \"payload\":%{private, location:escape_only}@}"
- "{\"msg%{public}.0s\":\"CLLocationUpdater\", \"event\":%{public, location:escape_only}s, \"_cmd\":%{public, location:escape_only}@, \"self\":\"%{public}p\"}"
- "{\"msg%{public}.0s\":\"CLMonitor\", \"event\":%{public, location:escape_only}s, \"_cmd\":%{public, location:escape_only}@, \"self\":\"%{public}p\", \"identifier\":%{public, location:escape_only}@, \"assumedState\":%{public, location:CLMonitoringState}lld}"
- "{\"msg%{public}.0s\":\"CLMonitor\", \"event\":%{public, location:escape_only}s, \"_cmd\":%{public, location:escape_only}@, \"self\":\"%{public}p\", \"identifier\":%{public, location:escape_only}@, \"event\":%{public, location:escape_only}@}"
- "{\"msg%{public}.0s\":\"CLMonitor\", \"event\":%{public, location:escape_only}s, \"_cmd\":%{public, location:escape_only}@, \"self\":\"%{public}p\", \"identifier\":%{public, location:escape_only}@}"
- "{\"msg%{public}.0s\":\"CLMonitor\", \"event\":%{public, location:escape_only}s, \"_cmd\":%{public, location:escape_only}@, \"self\":\"%{public}p\", \"name\":%{public, location:escape_only}@, \"authIdentity\":%{private, location:escape_only}@}"
- "{\"msg%{public}.0s\":\"CLMonitor\", \"event\":%{public, location:escape_only}s, \"_cmd\":%{public, location:escape_only}@, \"self\":\"%{public}p\", \"name\":%{public, location:escape_only}s}"
- "{\"msg%{public}.0s\":\"CLMonitor\", \"event\":%{public, location:escape_only}s, \"_cmd\":%{public, location:escape_only}@, \"self\":\"%{public}p\"}"
- "{\"msg%{public}.0s\":\"CLMonitorConfiguration\", \"event\":%{public, location:escape_only}s, \"_cmd\":%{public, location:escape_only}@, \"self\":\"%{public}p\", \"attributes\":%{private, location:escape_only}@}"
- "{\"msg%{public}.0s\":\"CLMonitorConfiguration\", \"event\":%{public, location:escape_only}s, \"_cmd\":%{public, location:escape_only}@, \"self\":\"%{public}p\", \"name\":%{public, location:escape_only}@}"
- "{\"msg%{public}.0s\":\"CLMonitorConfiguration\", \"event\":%{public, location:escape_only}s, \"_cmd\":%{public, location:escape_only}@, \"self\":\"%{public}p\"}"

```
