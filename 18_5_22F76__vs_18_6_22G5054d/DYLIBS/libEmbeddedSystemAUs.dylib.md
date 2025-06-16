## libEmbeddedSystemAUs.dylib

> `/System/Library/Frameworks/AudioToolbox.framework/libEmbeddedSystemAUs.dylib`

```diff

-1456.607.0.0.0
+1456.701.0.0.0
   __TEXT.__text: 0xefa94
   __TEXT.__auth_stubs: 0x2520
   __TEXT.__const: 0x76ac
   __TEXT.__dlopen_cstrs: 0x2c1
   __TEXT.__gcc_except_tab: 0x74dc
   __TEXT.__cstring: 0x54d8
-  __TEXT.__oslogstring: 0xb587
+  __TEXT.__oslogstring: 0xad9d
   __TEXT.__unwind_info: 0x3ed0
   __DATA_CONST.__got: 0x1c0
   __DATA_CONST.__const: 0xcc8

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B8C3F72B-0E73-374C-A3C7-D0ABA4AE0917
+  UUID: 78CE2C6D-9D72-3074-8B4F-36DEAA0FF7FD
   Functions: 3496
   Symbols:   9213
-  CStrings:  2110
+  CStrings:  2089
 
CStrings:
+ "%25s:%-5d ASSERTION FAILURE: "
- "%25s:%-5d ASSERTION FAILURE [(!\"Exception caught when accessing the vector container\") != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(!IsValid()) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(IsAnchorSampleTimeValid()) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(STIsGE(inSampleTime, 0.) && STIsLE(inSampleTime, kUnspecifiedSampleTime)) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(STIsGE(startSampleTime, 0.) && !STIsUnspecified(startSampleTime)) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(STIsGT(inSliceEndSampleTime, sliceStartSampleTime)) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(STIsLE(curRenderTime, sliceStartTime) && STIsLE(sliceEndTime, endRenderTime)) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(STIsLE(sliceStartTime, sliceEndTime)) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(inFrameOffset < 0 && mParameterCurve.size() > 1) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(inSegment->eventType == kParameterEvent_Ramped && mRawSegment.eventType == kParameterEvent_Ramped) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(inStartFrame <= inEndFrame) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(mBufferCapacity == 0 || nBytes <= mBufferCapacity) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(mBufferMemory == __null) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(mParameterCurve.GetNumberOfControlPoints() != 1) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(numberOfFrames > 0) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(outValue <= 1 && outValue >= 0) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(outputFrames == nFrames) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(renderUntil <= SInt32(inNumberFrames)) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(srcABL.mNumberBuffers == destABL.mNumberBuffers) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(srcBuf->mNumberChannels == destBuf->mNumberChannels) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(tempABL->mNumberBuffers >= inbl->mNumberBuffers) != 0 is false]: "
- "%25s:%-5d ASSERTION FAILURE [(tempABL->mNumberBuffers >= outbl->mNumberBuffers) != 0 is false]: "

```
