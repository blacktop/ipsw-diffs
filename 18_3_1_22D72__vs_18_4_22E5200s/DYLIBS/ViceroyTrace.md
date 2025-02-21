## ViceroyTrace

> `/System/Library/PrivateFrameworks/AVConference.framework/Frameworks/ViceroyTrace.framework/ViceroyTrace`

```diff

-2100.5.1.1.1
-  __TEXT.__text: 0x9f6c0
-  __TEXT.__auth_stubs: 0xd00
-  __TEXT.__objc_methlist: 0x8194
-  __TEXT.__const: 0x2278
-  __TEXT.__cstring: 0xcccb
-  __TEXT.__oslogstring: 0xb419
-  __TEXT.__gcc_except_tab: 0x350
+2105.5.1.0.0
+  __TEXT.__text: 0xa186c
+  __TEXT.__auth_stubs: 0xd10
+  __TEXT.__objc_methlist: 0x8598
+  __TEXT.__const: 0x2260
+  __TEXT.__cstring: 0xce77
+  __TEXT.__oslogstring: 0xb6b2
+  __TEXT.__gcc_except_tab: 0x3a0
   __TEXT.__dlopen_cstrs: 0xa0
-  __TEXT.__unwind_info: 0x1318
+  __TEXT.__unwind_info: 0x1508
+  __TEXT.__eh_frame: 0x48
   __TEXT.__objc_classname: 0x501
-  __TEXT.__objc_methname: 0x19950
-  __TEXT.__objc_methtype: 0x20b4
-  __TEXT.__objc_stubs: 0xdae0
-  __DATA_CONST.__got: 0x218
-  __DATA_CONST.__const: 0xd20
+  __TEXT.__objc_methname: 0x19c31
+  __TEXT.__objc_methtype: 0x2100
+  __TEXT.__objc_stubs: 0xdd80
+  __DATA_CONST.__got: 0x220
+  __DATA_CONST.__const: 0xce0
   __DATA_CONST.__objc_classlist: 0x1b0
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3d30
+  __DATA_CONST.__objc_selrefs: 0x3e58
   __DATA_CONST.__objc_superrefs: 0x178
   __DATA_CONST.__objc_arraydata: 0x200
-  __AUTH_CONST.__auth_got: 0x690
+  __AUTH_CONST.__auth_got: 0x698
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__const: 0x260
-  __AUTH_CONST.__cfstring: 0xcd20
-  __AUTH_CONST.__objc_const: 0x15868
+  __AUTH_CONST.__cfstring: 0xce60
+  __AUTH_CONST.__objc_const: 0x15358
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_intobj: 0x3d8
   __AUTH_CONST.__objc_arrayobj: 0x60
-  __DATA.__objc_ivar: 0x1e0c
-  __DATA.__data: 0x638
+  __DATA.__objc_ivar: 0x1e28
+  __DATA.__data: 0x648
   __DATA.__bss: 0xe8
   __DATA.__common: 0x21
   __DATA_DIRTY.__objc_data: 0x10e0

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 3492
-  Symbols:   3889
-  CStrings:  6897
+  Functions: 3714
+  Symbols:   4168
+  CStrings:  6956
 
Symbols:
+ _OBJC_CLASS_$_NSCalendar
+ _objc_release_x25
+ _reportingSessionModeFromOperatingMode
+ _sRTCReportingSafeViewScreenSharingClientName
+ _sRTCReportingSafeViewSystemAudioSharingClientName
CStrings:
+ " [%s] %s:%d %@(%p) Changed reportingMode=%d"
+ " [%s] %s:%d %@(%p) Received operatingMode=%d which is not a valid VCSessionReportingMode"
+ " [%s] %s:%d %@(%p) Starting reportingMode=%d"
+ " [%s] %s:%d Changed reportingMode=%d"
+ " [%s] %s:%d Received operatingMode=%d which is not a valid VCSessionReportingMode"
+ " [%s] %s:%d Starting reportingMode=%d"
+ "+[VCDiskUtils createDefaultDirectoryIfNeeded:]"
+ "-[RTCReportingAgent directoryPathForWeeklyIDCache]"
+ "-[RTCReportingAgent setAndSaveWeeklyID:currentWeek:currentYear:cachePath:]"
+ "-[RTCReportingAgent setUpWeeklyRotatingID]"
+ "-[VCAggregatorMultiway updateOperatingMode:]"
+ "@28@0:8i16^{?=@B^{__CFDate}^{__CFString}^{__CFString}B^{__CFString}}20"
+ "@32@0:8@16^{?=@B^{__CFDate}^{__CFString}^{__CFString}B^{__CFString}}24"
+ "ADRTN"
+ "B40@0:8@16q24q32"
+ "CallConnectionTime"
+ "DUID"
+ "ReportingVC [%s] %s:%d Could not create directory"
+ "ReportingVC [%s] %s:%d Could not create directory=%@"
+ "ReportingVC [%s] %s:%d Could not find directory path"
+ "ReportingVC [%s] %s:%d Could not get calendar"
+ "ReportingVC [%s] %s:%d Could not save ID value to cache error=%@"
+ "ReportingVC [%s] %s:%d Invalid operating mode for VCSession=%d"
+ "ReportingWeeklyID"
+ "ReportingWeeklyIDValidityWeek"
+ "ReportingWeeklyIDValidityYear"
+ "SEOPMODE"
+ "SSOPMODE"
+ "SafeViewScreenShare"
+ "T@\"NSString\",C,V_weeklyDUID"
+ "TC,V_segmentReportingMode"
+ "URLByAppendingPathComponent:"
+ "UUID"
+ "_audioOnlyModeDuration"
+ "_callStartReportingMode"
+ "_currentReportingMode"
+ "_deviceUniqueID"
+ "_segmentReportingMode"
+ "_weeklyDUID"
+ "addSessionOperatingModeForCallReport:"
+ "checkIfWeeklyIDIsExpired:currentWeek:currentYear:"
+ "components:fromDate:"
+ "createDefaultCacheDirectoryIfNeeded"
+ "createDefaultDirectoryIfNeeded:"
+ "currentCalendar"
+ "directoryPathForWeeklyIDCache"
+ "fileURLWithPath:isDirectory:"
+ "initCallWithRemoteParticipantID:andWeeklyID:"
+ "initWithContentsOfURL:"
+ "numberWithUnsignedInteger:"
+ "reportingSessionModeFromOperatingMode"
+ "reporting_weeklyID_config.plist"
+ "segmentReportingMode"
+ "setAndSaveWeeklyID:currentWeek:currentYear:cachePath:"
+ "setSegmentReportingMode:"
+ "setUpWeeklyRotatingID"
+ "setWeeklyDUID:"
+ "updateOperatingMode:"
+ "v24@0:8^{?=@B^{__CFDate}^{__CFString}^{__CFString}B^{__CFString}}16"
+ "v48@0:8@16Q24Q32@40"
+ "weekOfYear"
+ "weeklyDUID"
+ "writeToURL:error:"
+ "yearForWeekOfYear"
- "+[VCDiskUtils createDefaultLogDirectoryIfNeeded]"
- "@28@0:8i16^{?=@B^{__CFDate}^{__CFString}^{__CFString}B}20"
- "@32@0:8@16^{?=@B^{__CFDate}^{__CFString}^{__CFString}B}24"
- "initCallWithRemoteParticipantID:"
- "v24@0:8^{?=@B^{__CFDate}^{__CFString}^{__CFString}B}16"

```
