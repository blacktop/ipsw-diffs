## ViceroyTrace

> `/System/Library/PrivateFrameworks/AVConference.framework/Frameworks/ViceroyTrace.framework/ViceroyTrace`

```diff

-2145.53.2.0.0
-  __TEXT.__text: 0xacbe4
-  __TEXT.__auth_stubs: 0xd60
+2145.57.1.0.0
+  __TEXT.__text: 0xad0ac
+  __TEXT.__auth_stubs: 0xd90
   __TEXT.__objc_methlist: 0x8cb0
   __TEXT.__const: 0x2478
-  __TEXT.__cstring: 0xe81f
-  __TEXT.__oslogstring: 0xc59e
-  __TEXT.__gcc_except_tab: 0x3b4
+  __TEXT.__cstring: 0xe8a7
+  __TEXT.__oslogstring: 0xc5ce
+  __TEXT.__gcc_except_tab: 0x3d4
   __TEXT.__dlopen_cstrs: 0xa0
-  __TEXT.__unwind_info: 0x1690
+  __TEXT.__unwind_info: 0x16a8
   __TEXT.__eh_frame: 0x48
   __TEXT.__objc_classname: 0x599
-  __TEXT.__objc_methname: 0x1b941
-  __TEXT.__objc_methtype: 0x240f
-  __TEXT.__objc_stubs: 0xeca0
+  __TEXT.__objc_methname: 0x1ba09
+  __TEXT.__objc_methtype: 0x2423
+  __TEXT.__objc_stubs: 0xecc0
   __DATA_CONST.__got: 0x238
-  __DATA_CONST.__const: 0xd68
+  __DATA_CONST.__const: 0xd88
   __DATA_CONST.__objc_classlist: 0x1d0
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4288
+  __DATA_CONST.__objc_selrefs: 0x4290
   __DATA_CONST.__objc_superrefs: 0x1a0
   __DATA_CONST.__objc_arraydata: 0x220
-  __AUTH_CONST.__auth_got: 0x6c0
+  __AUTH_CONST.__auth_got: 0x6d8
   __AUTH_CONST.__const: 0x280
-  __AUTH_CONST.__cfstring: 0xdce0
-  __AUTH_CONST.__objc_const: 0x16718
+  __AUTH_CONST.__cfstring: 0xdd20
+  __AUTH_CONST.__objc_const: 0x16778
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_intobj: 0x480
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH.__objc_data: 0x1e0
-  __DATA.__objc_ivar: 0x1ff4
-  __DATA.__data: 0x670
+  __DATA.__objc_ivar: 0x2000
+  __DATA.__data: 0x738
   __DATA.__bss: 0x78
   __DATA.__common: 0x1
   __DATA_DIRTY.__objc_data: 0x1040

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 3AC1DE67-9709-329D-B628-EA9B95F230DE
-  Functions: 3942
-  Symbols:   12980
-  CStrings:  9209
+  UUID: 32FF3AAE-B514-3356-965B-EF5188A364F9
+  Functions: 3951
+  Symbols:   13008
+  CStrings:  9220
 
Symbols:
+ -[VCAggregatorMultiway processABCSymptomsForSliceStatus:currentSegmentName:isRemoteStatus:]
+ -[VCAggregatorMultiway processSliceStatusFailedABCSymptom:isRemoteStatus:]
+ -[VCAggregatorMultiway processSliceStatusFailedABCSymptom:isRemoteStatus:].cold.1
+ -[VCAggregatorMultiway processSliceStatusNotReceivedABCSymptom:isRemoteStatus:]
+ -[VCAggregatorMultiway processSliceStatusNotReceivedABCSymptom:isRemoteStatus:].cold.1
+ GCC_except_table240
+ GCC_except_table40
+ _OBJC_IVAR_$_RTCReportingAgent._onceSendFinalizedEventToken
+ _OBJC_IVAR_$_VCAggregatorMultiway._hasReportedSliceStatusFailedRemoteSymptom
+ _OBJC_IVAR_$_VCAggregatorMultiway._hasReportedSliceStatusNotReceivedRemoteSymptom
+ _VCReporting_FlushReportingSession
+ _VCReporting_FlushReportingSession.cold.1
+ __MergedGlobals.1002
+ ___43-[RTCReportingAgent sendLastFinalizedEvent]_block_invoke
+ ___43-[RTCReportingAgent sendLastFinalizedEvent]_block_invoke.cold.1
+ ___VCReporting_FlushReportingSession_block_invoke
+ ___VCReporting_FlushReportingSession_block_invoke_2
+ ___VCReporting_FlushReportingSession_block_invoke_3
+ ___block_literal_global.517
+ ___block_literal_global.526
+ ___block_literal_global.609
+ ___reportingSetUserInfo_block_invoke.522
+ ___reportingSetUserInfo_block_invoke.523
+ ___reportingSetUserInfo_block_invoke.523.cold.1
+ _gVRTraceLevelLock
+ _objc_msgSend$processABCSymptomsForSliceStatus:currentSegmentName:isRemoteStatus:
+ _objc_msgSend$processSliceStatusFailedABCSymptom:isRemoteStatus:
+ _objc_msgSend$processSliceStatusNotReceivedABCSymptom:isRemoteStatus:
+ _objc_msgSend$terminateSessionWithCompletion:
+ _pthread_rwlock_rdlock
+ _pthread_rwlock_unlock
+ _pthread_rwlock_wrlock
- -[VCAggregatorMultiway processSliceStatusABCSymptoms:currentSegmentName:]
- -[VCAggregatorMultiway processSliceStatusFailedABCSymptom:]
- -[VCAggregatorMultiway processSliceStatusFailedABCSymptom:].cold.1
- -[VCAggregatorMultiway processSliceStatusNotReceivedABCSymptom:]
- -[VCAggregatorMultiway processSliceStatusNotReceivedABCSymptom:].cold.1
- GCC_except_table39
- __MergedGlobals.1000
- ___block_literal_global.514
- ___block_literal_global.523
- ___block_literal_global.607
- ___reportingSetUserInfo_block_invoke.519
- ___reportingSetUserInfo_block_invoke.520
- ___reportingSetUserInfo_block_invoke.520.cold.1
- _objc_msgSend$processSliceStatusABCSymptoms:currentSegmentName:
- _objc_msgSend$processSliceStatusFailedABCSymptom:
- _objc_msgSend$processSliceStatusNotReceivedABCSymptom:
CStrings:
+ "-[RTCReportingAgent sendLastFinalizedEvent]_block_invoke"
+ "-[VCAggregatorMultiway processSliceStatusFailedABCSymptom:isRemoteStatus:]"
+ "-[VCAggregatorMultiway processSliceStatusNotReceivedABCSymptom:isRemoteStatus:]"
+ "ReportingVC [%s] %s:%d Flushing queue timed out"
+ "SliceInterfaceFailedRemote"
+ "SliceInterfaceNotReceivedRemote"
+ "VCReporting_FlushReportingSession"
+ "[79B]"
+ "_hasReportedSliceStatusFailedRemoteSymptom"
+ "_hasReportedSliceStatusNotReceivedRemoteSymptom"
+ "_onceSendFinalizedEventToken"
+ "processABCSymptomsForSliceStatus:currentSegmentName:isRemoteStatus:"
+ "processSliceStatusFailedABCSymptom:isRemoteStatus:"
+ "processSliceStatusNotReceivedABCSymptom:isRemoteStatus:"
+ "terminateSessionWithCompletion:"
+ "v36@0:8@\"NSString\"16@\"NSString\"24B32"
+ "v36@0:8@16@24B32"
- "-[RTCReportingAgent sendLastFinalizedEvent]"
- "-[VCAggregatorMultiway processSliceStatusFailedABCSymptom:]"
- "-[VCAggregatorMultiway processSliceStatusNotReceivedABCSymptom:]"
- "[77B]"
- "processSliceStatusABCSymptoms:currentSegmentName:"
- "processSliceStatusFailedABCSymptom:"
- "processSliceStatusNotReceivedABCSymptom:"
- "v32@0:8@\"NSString\"16@\"NSString\"24"

```
