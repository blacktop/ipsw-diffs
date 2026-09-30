## libEmbeddedSystemAUs.dylib

> `/System/Library/Frameworks/AudioToolbox.framework/libEmbeddedSystemAUs.dylib`

```diff

-1456.404.0.0.0
-  __TEXT.__text: 0xf0548
-  __TEXT.__auth_stubs: 0x2540
-  __TEXT.__gcc_except_tab: 0x6cac
-  __TEXT.__const: 0x770c
-  __TEXT.__cstring: 0x54eb
-  __TEXT.__oslogstring: 0xb587
+1456.525.0.0.0
+  __TEXT.__text: 0xef348
+  __TEXT.__auth_stubs: 0x2520
+  __TEXT.__const: 0x76bc
   __TEXT.__dlopen_cstrs: 0x2c1
-  __TEXT.__unwind_info: 0x3f60
-  __DATA_CONST.__got: 0x1b8
+  __TEXT.__gcc_except_tab: 0x7214
+  __TEXT.__cstring: 0x54eb
+  __TEXT.__oslogstring: 0xad9d
+  __TEXT.__unwind_info: 0x3e60
+  __DATA_CONST.__got: 0x1c0
   __DATA_CONST.__const: 0xcc8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __AUTH_CONST.__auth_got: 0x12a8
-  __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__const: 0x10408
+  __AUTH_CONST.__auth_got: 0x1298
+  __AUTH_CONST.__auth_ptr: 0x10
+  __AUTH_CONST.__const: 0x103e0
   __AUTH_CONST.__cfstring: 0x3900
   __DATA.__data: 0x8c0
   __DATA.__bss: 0x5a8

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3590
+  Functions: 3491
   Symbols:   4257
-  CStrings:  1656
+  CStrings:  1635
 
Symbols:
+ __ZNSt3__117bad_function_callD1Ev
+ __ZTVNSt3__117bad_function_callE
+ ___muldc3
- __ZNKSt9exception4whatEv
- __ZNSt3__115system_categoryEv
- _logb
- _scalbn
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
