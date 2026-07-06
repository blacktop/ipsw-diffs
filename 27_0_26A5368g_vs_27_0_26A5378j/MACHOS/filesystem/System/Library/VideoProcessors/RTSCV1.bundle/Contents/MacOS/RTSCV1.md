## RTSCV1

> `/System/Library/VideoProcessors/RTSCV1.bundle/Contents/MacOS/RTSCV1`

```diff

-  __TEXT.__text: 0x16028
+  __TEXT.__text: 0x16074
   __TEXT.__auth_stubs: 0x580
   __TEXT.__objc_stubs: 0x16e0
   __TEXT.__objc_methlist: 0xf34

   __DATA_CONST.__objc_superrefs: 0x78
   __DATA_CONST.__objc_intobj: 0x18
   __DATA_CONST.__auth_got: 0x2d0
-  __DATA_CONST.__got: 0x198
+  __DATA_CONST.__got: 0x1a0
   __DATA_CONST.__auth_ptr: 0x8
   __DATA.__objc_const: 0x2948
   __DATA.__objc_selrefs: 0x878
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__oslogstring : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_selrefs : content changed
~ __DATA.__data : content changed
Functions:
~ -[RTSCProcessorV1 _updateOutputFOV] : 2036 -> 2112
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: %d motion-related log messages filtered out (max of 1/s displayed from FigMotionProcessingUtilities)"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Could not find Hall sample for the given timestamp on hallPositionIndex %d"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Could not find a motion sample within %fms of the current frame. Frame timestamp is %f, sample timestamps in the ring buffer are from %f to %f, latestTimeDifference %f"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Could not find the closest motion sample index in the ring buffer for the frame timestamp (%f)."
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Extracting only the first %d ISP Hall samples"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Extracting only the first %d ISP motion samples"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Quaternion pointer is null!"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Unsupported Hall data version %d"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Warning! The before and after Hall sample timestamp difference is close to 0.0f!"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Warning! The before and after motion sample timestamp difference is close to 0.0f!"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: interpolateQuaternionsByAngle: delta quaternion w %f is larger than 1"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/RTSC/Bundle/Computation/RTSCAutocovarianceDynamicsAnalyzer4DOF.m %s: Failed to initialize"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/RTSC/Bundle/Computation/RTSCKalmanFilter4DOF.m %s: Filter is nil"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/RTSC/Bundle/Computation/RTSCStabilizationUtilities.m %s: Reference camera is not valid"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/RTSC/Bundle/Computation/RTSCStabilizationUtilities.m %s: maxTimescale is less than minTimescale. Forcing maxTimescale = minTimescale"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/RTSC/Bundle/Computation/RTSCStabilizationUtilities.m %s: minTimescale and transitionTime must be greater than zero"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: %d motion-related log messages filtered out (max of 1/s displayed from FigMotionProcessingUtilities)"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Could not find Hall sample for the given timestamp on hallPositionIndex %d"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Could not find a motion sample within %fms of the current frame. Frame timestamp is %f, sample timestamps in the ring buffer are from %f to %f, latestTimeDifference %f"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Could not find the closest motion sample index in the ring buffer for the frame timestamp (%f)."
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Extracting only the first %d ISP Hall samples"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Extracting only the first %d ISP motion samples"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Quaternion pointer is null!"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Unsupported Hall data version %d"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Warning! The before and after Hall sample timestamp difference is close to 0.0f!"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Warning! The before and after motion sample timestamp difference is close to 0.0f!"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: interpolateQuaternionsByAngle: delta quaternion w %f is larger than 1"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/VideoProcessors/RTSC/Bundle/Computation/RTSCAutocovarianceDynamicsAnalyzer4DOF.m %s: Failed to initialize"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/VideoProcessors/RTSC/Bundle/Computation/RTSCKalmanFilter4DOF.m %s: Filter is nil"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/VideoProcessors/RTSC/Bundle/Computation/RTSCStabilizationUtilities.m %s: Reference camera is not valid"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/VideoProcessors/RTSC/Bundle/Computation/RTSCStabilizationUtilities.m %s: maxTimescale is less than minTimescale. Forcing maxTimescale = minTimescale"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/VideoProcessors/RTSC/Bundle/Computation/RTSCStabilizationUtilities.m %s: minTimescale and transitionTime must be greater than zero"

```
