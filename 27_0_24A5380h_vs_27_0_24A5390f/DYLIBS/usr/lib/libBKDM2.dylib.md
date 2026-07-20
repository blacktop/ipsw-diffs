## libBKDM2.dylib

> `/usr/lib/libBKDM2.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-980.0.0.0.10
-  __TEXT.__text: 0x7c434
-  __TEXT.__objc_methlist: 0x5d2c
+980.0.18.0.0
+  __TEXT.__text: 0x7cabc
+  __TEXT.__objc_methlist: 0x5d84
   __TEXT.__const: 0xd7b8
-  __TEXT.__cstring: 0x703d
-  __TEXT.__oslogstring: 0x465c
-  __TEXT.__gcc_except_tab: 0x177c
+  __TEXT.__cstring: 0x7041
+  __TEXT.__oslogstring: 0x4720
+  __TEXT.__gcc_except_tab: 0x17c0
   __TEXT.__ustring: 0x11c
-  __TEXT.__unwind_info: 0xe10
+  __TEXT.__unwind_info: 0xe20
   __TEXT.__eh_frame: 0x50
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_classlist: 0xe0
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3d28
+  __DATA_CONST.__objc_selrefs: 0x3d58
   __DATA_CONST.__objc_superrefs: 0xc0
   __DATA_CONST.__objc_arraydata: 0x4a8
-  __DATA_CONST.__got: 0x448
+  __DATA_CONST.__got: 0x450
   __AUTH_CONST.__const: 0xc08
   __AUTH_CONST.__cfstring: 0x65a0
-  __AUTH_CONST.__objc_const: 0x9948
-  __AUTH_CONST.__objc_intobj: 0x3f0
+  __AUTH_CONST.__objc_const: 0x9a28
+  __AUTH_CONST.__objc_intobj: 0x3d8
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__objc_arrayobj: 0x168
-  __AUTH_CONST.__auth_got: 0x728
+  __AUTH_CONST.__auth_got: 0x730
   __AUTH.__objc_data: 0x1e0
-  __DATA.__objc_ivar: 0xab0
+  __DATA.__objc_ivar: 0xac8
   __DATA.__data: 0x880
   __DATA.__bss: 0x49
   __DATA_DIRTY.__objc_data: 0x6e0

   - /usr/lib/libSystemHealth.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2895
-  Symbols:   5346
-  CStrings:  1607
+  Functions: 2904
+  Symbols:   5367
+  CStrings:  1608
 
Symbols:
+ -[BLFrameDebugExtra processFrameDebugData:withHeader:dict:]
+ -[BLFrameDebugExtraEisp processFrameDebugData:withHeader:dict:]
+ -[PearlCoreAnalytics analyzeSecureFaceDetectCoachingStatus:]
+ -[PearlCoreAnalytics analyzeSecureFaceDetectFrameMeta:fromCameraID:faceDetected:]
+ -[PearlCoreAnalytics analyzeSecureFrameMeta:fromCameraID:faceDetected:]
+ -[PearlCoreAnalytics deviceThermalState]
+ -[PearlCoreAnalyticsEnrollEvent deviceThermalState]
+ -[PearlCoreAnalyticsEnrollEvent setDeviceThermalState:]
+ -[PearlCoreAnalyticsMatchEvent deviceThermalState]
+ -[PearlCoreAnalyticsMatchEvent setDeviceThermalState:]
+ GCC_except_table16
+ _OBJC_CLASS_$_NSProcessInfo
+ _OBJC_IVAR_$_PearlCoreAnalytics._secureEnrollEvent
+ _OBJC_IVAR_$_PearlCoreAnalytics._secureEnrollEventValid
+ _OBJC_IVAR_$_PearlCoreAnalytics._secureMatchEvent
+ _OBJC_IVAR_$_PearlCoreAnalytics._secureMatchEventValid
+ _OBJC_IVAR_$_PearlCoreAnalyticsEnrollEvent._deviceThermalState
+ _OBJC_IVAR_$_PearlCoreAnalyticsMatchEvent._deviceThermalState
+ ___63-[BLFrameDebugExtraEisp processFrameDebugData:withHeader:dict:]_block_invoke
+ _dispatch_suspend
+ _objc_msgSend$analyzeSecureFaceDetectCoachingStatus:
+ _objc_msgSend$analyzeSecureFaceDetectFrameMeta:fromCameraID:faceDetected:
+ _objc_msgSend$analyzeSecureFrameMeta:fromCameraID:faceDetected:
+ _objc_msgSend$deviceThermalState
+ _objc_msgSend$processFrameDebugData:withHeader:dict:
+ _objc_msgSend$processInfo
+ _objc_msgSend$secureFaceDetectRequestType
+ _objc_msgSend$setDeviceThermalState:
+ _objc_msgSend$thermalState
- -[BLFrameDebugExtra processFrameDebugData:forSeqType:withDict:]
- -[BLFrameDebugExtraEisp processFrameDebugData:forSeqType:withDict:]
- -[PearlCoreAnalytics analyzeSecureFrameMeta:faceDetected:]
- GCC_except_table12
- _OUTLINED_FUNCTION_59
- ___67-[BLFrameDebugExtraEisp processFrameDebugData:forSeqType:withDict:]_block_invoke
- _objc_msgSend$analyzeSecureFrameMeta:faceDetected:
- _objc_msgSend$processFrameDebugData:forSeqType:withDict:
CStrings:
+ "NOTICE: analyzeSecureFaceDetectFrameMeta: Face detected on RGB camera first! Awaiting IR frame...\n"
+ "PearlCoreAnalytics analyzeSecureFaceDetectFrameMeta\n"
+ "PearlCoreAnalytics analyzeSecureFrameMeta: Unexpected secureFaceDetectRequestType: %u\n"
+ "enroll_group_count"
+ "processed_groups"
- "\t"
- "PearlCoreAnalytics analyzeSecureFrameMeta\n"
- "enroll_frames_num"
- "processed_doubles"
```
