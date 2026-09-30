## libEmbeddedSystemAUs.dylib

> `/System/Library/Frameworks/AudioToolbox.framework/libEmbeddedSystemAUs.dylib`

```diff

   __TEXT.__gcc_except_tab: 0x6cac
   __TEXT.__const: 0x770c
   __TEXT.__cstring: 0x54eb
-  __TEXT.__oslogstring: 0xad9d
+  __TEXT.__oslogstring: 0xb587
   __TEXT.__dlopen_cstrs: 0x2c1
   __TEXT.__unwind_info: 0x3f60
   __DATA_CONST.__got: 0x1b8

   - /usr/lib/libobjc.A.dylib
   Functions: 3590
   Symbols:   4257
-  CStrings:  1635
+  CStrings:  1656
 
CStrings:
+ "%25s:%-5d ASSERTION FAILURE [(!\"Exception caught when accessing the vector container\") != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(!IsValid()) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(IsAnchorSampleTimeValid()) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(STIsGE(inSampleTime, 0.) && STIsLE(inSampleTime, kUnspecifiedSampleTime)) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(STIsGE(startSampleTime, 0.) && !STIsUnspecified(startSampleTime)) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(STIsGT(inSliceEndSampleTime, sliceStartSampleTime)) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(STIsLE(curRenderTime, sliceStartTime) && STIsLE(sliceEndTime, endRenderTime)) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(STIsLE(sliceStartTime, sliceEndTime)) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(inFrameOffset < 0 && mParameterCurve.size() > 1) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(inSegment->eventType == kParameterEvent_Ramped && mRawSegment.eventType == kParameterEvent_Ramped) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(inStartFrame <= inEndFrame) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(mBufferCapacity == 0 || nBytes <= mBufferCapacity) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(mBufferMemory == __null) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(mParameterCurve.GetNumberOfControlPoints() != 1) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(numberOfFrames > 0) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(outValue <= 1 && outValue >= 0) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(outputFrames == nFrames) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(renderUntil <= SInt32(inNumberFrames)) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(srcABL.mNumberBuffers == destABL.mNumberBuffers) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(srcBuf->mNumberChannels == destBuf->mNumberChannels) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(tempABL->mNumberBuffers >= inbl->mNumberBuffers) != 0 is false]: "
+ "%25s:%-5d ASSERTION FAILURE [(tempABL->mNumberBuffers >= outbl->mNumberBuffers) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE: "

```
