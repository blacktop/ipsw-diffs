## Portrait

> `/System/iOSSupport/System/Library/PrivateFrameworks/Portrait.framework/Versions/A/Portrait`

```diff

-560.21.2.0.0
-  __TEXT.__text: 0x99fec
+560.40.3.0.0
+  __TEXT.__text: 0x9ad58
   __TEXT.__delay_helper: 0x264
-  __TEXT.__objc_methlist: 0xa174
-  __TEXT.__const: 0x20b10
-  __TEXT.__cstring: 0x5567
-  __TEXT.__oslogstring: 0x613d
+  __TEXT.__objc_methlist: 0xa20c
+  __TEXT.__const: 0x20b20
+  __TEXT.__cstring: 0x556d
+  __TEXT.__oslogstring: 0x6440
   __TEXT.__gcc_except_tab: 0x1b50
   __TEXT.__ustring: 0x30
-  __TEXT.__unwind_info: 0x3038
+  __TEXT.__unwind_info: 0x3060
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x55e0
+  __DATA_CONST.__objc_selrefs: 0x5638
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_classrefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x518

   __DATA_CONST.__got: 0x8d8
   __AUTH_CONST.__const: 0x460
   __AUTH_CONST.__cfstring: 0x5520
-  __AUTH_CONST.__objc_const: 0x1ebf8
+  __AUTH_CONST.__objc_const: 0x1ec70
   __AUTH_CONST.__objc_intobj: 0xb70
   __AUTH_CONST.__objc_arrayobj: 0x1b0
   __AUTH_CONST.__objc_doubleobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x140
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x8c0
-  __DATA.__objc_ivar: 0x194c
+  __DATA.__objc_ivar: 0x1954
   __DATA.__data: 0x7a8
   __DATA_DIRTY.__objc_data: 0x2f30
   __DATA_DIRTY.__data: 0x4

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 4148
-  Symbols:   9289
-  CStrings:  1576
+  Functions: 4161
+  Symbols:   9306
+  CStrings:  1586
 
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
+ OBJC_IVAR_$_PTCinematographyPostcaptureRefinement._didReportInputStall
+ OBJC_IVAR_$_PTCinematographyPostcaptureRefinement._firstInputTimeWithoutOutput
+ OBJC_IVAR_$_PTCinematographyPostcaptureRefinement._lastProcessedInputFrameIndex
+ _objc_msgSend$_advanceToInputFrameNearestTime:
+ _objc_msgSend$_checkForInputStallAtTime:
+ _objc_msgSend$_inputFrameSpacing
+ _objc_msgSend$_lastProcessedInputFrame
+ _objc_msgSend$expectedInputTime
+ _objc_msgSend$processNextDisparityBuffer:atTime:
- -[PTCinematographyPostcaptureRefinement _priorInputFrame]
- OBJC_IVAR_$_PTDisparityFilterDEMA_LKT._erodeMonocularDisparity
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
