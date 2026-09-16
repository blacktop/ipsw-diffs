## Portrait

> `/System/Library/PrivateFrameworks/Portrait.framework/Portrait`

```diff

-560.22.2.0.0
-  __TEXT.__text: 0x96888
+560.40.3.0.0
+  __TEXT.__text: 0x97624
   __TEXT.__delay_helper: 0x264
-  __TEXT.__objc_methlist: 0xa0c4
-  __TEXT.__const: 0x20b00
-  __TEXT.__cstring: 0x52dd
-  __TEXT.__oslogstring: 0x5e30
+  __TEXT.__objc_methlist: 0xa15c
+  __TEXT.__const: 0x20b10
+  __TEXT.__cstring: 0x52e3
+  __TEXT.__oslogstring: 0x6133
   __TEXT.__gcc_except_tab: 0x1af4
   __TEXT.__ustring: 0x30
-  __TEXT.__unwind_info: 0x2f90
+  __TEXT.__unwind_info: 0x2fb0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5548
+  __DATA_CONST.__objc_selrefs: 0x55a0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_classrefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x510

   __DATA_CONST.__got: 0x8b8
   __AUTH_CONST.__const: 0x460
   __AUTH_CONST.__cfstring: 0x50a0
-  __AUTH_CONST.__objc_const: 0x1e5a8
+  __AUTH_CONST.__objc_const: 0x1e620
   __AUTH_CONST.__objc_intobj: 0xaf8
   __AUTH_CONST.__objc_arrayobj: 0x180
   __AUTH_CONST.__objc_doubleobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x910
-  __DATA.__objc_ivar: 0x1918
+  __DATA.__objc_ivar: 0x1920
   __DATA.__data: 0x7b0
   __DATA_DIRTY.__objc_data: 0x2e90
   __DATA_DIRTY.__bss: 0x8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 4109
-  Symbols:   9145
-  CStrings:  1518
+  Functions: 4122
+  Symbols:   9162
+  CStrings:  1528
 
Symbols:
+ -[PTCinematographyPostcaptureRefinement _advanceToInputFrameNearestTime:]
+ -[PTCinematographyPostcaptureRefinement _checkForInputStallAtTime:]
+ -[PTCinematographyPostcaptureRefinement _inputFrameSpacing]
+ -[PTCinematographyPostcaptureRefinement _lastProcessedInputFrame]
+ -[PTCinematographyPostcaptureRefinement didReportInputStall]
+ -[PTCinematographyPostcaptureRefinement firstInputTimeWithoutOutput]
+ -[PTCinematographyPostcaptureRefinement lastProcessedInputFrameIndex]
+ -[PTCinematographyPostcaptureRefinement processNextDisparityBuffer:atTime:]
+ -[PTCinematographyPostcaptureRefinement setDidReportInputStall:]
+ -[PTCinematographyPostcaptureRefinement setFirstInputTimeWithoutOutput:]
+ -[PTCinematographyPostcaptureRefinement setLastProcessedInputFrameIndex:]
+ -[PTPixelBufferCache removePixelBufferForTime:withinTolerance:]
+ _OBJC_IVAR_$_PTCinematographyPostcaptureRefinement._didReportInputStall
+ _OBJC_IVAR_$_PTCinematographyPostcaptureRefinement._firstInputTimeWithoutOutput
+ _OBJC_IVAR_$_PTCinematographyPostcaptureRefinement._lastProcessedInputFrameIndex
+ _objc_msgSend$_advanceToInputFrameNearestTime:
+ _objc_msgSend$_checkForInputStallAtTime:
+ _objc_msgSend$_inputFrameSpacing
+ _objc_msgSend$_lastProcessedInputFrame
+ _objc_msgSend$expectedInputTime
+ _objc_msgSend$processNextDisparityBuffer:atTime:
- -[PTCinematographyPostcaptureRefinement _priorInputFrame]
- _OBJC_IVAR_$_PTDisparityFilterDEMA_LKT._erodeMonocularDisparity
- _OUTLINED_FUNCTION_11
- _objc_msgSend$_priorInputFrame
CStrings:
+ "Base decision filtering: %lu decisions in, %lu out"
+ "Cinematography: fast (per-frame metadata sampler, no decisions)"
+ "Cinematography: refined (generation %lu, %lu frames, %lu decisions)"
+ "Cinematography: snapshot (generation %lu, %lu frames, %lu decisions)"
+ "Input time %@ is not within half a frame of any script frame (nearest is %@); ignoring disparity buffer"
+ "Input time %@ precedes expected input time %@; ignoring disparity buffer"
+ "No frame near input time %@ to apply disparity buffer to"
+ "No output frame after inputs spanning %.2fs from %@; inputs may be too sparse (about 24 per second of source are needed)"
+ "No timestamp within tolerance %f seconds of the requested timestamp found in cache"
+ "Skipping %lu input frame(s) to reach input time %@"
+ "Tolerance passed to removePixelBufferForTime:withinTolerance: must be numeric, finite and non-negative"
+ "lastProcessedInputFrameIndex"
- "PTDisparityFilterDEMA_LKT enabling disparity erosion with strength: %.2f"
- "PortTypeFrontSuperWide"
```
