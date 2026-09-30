## MediaAnalysisServices

> `/System/Library/PrivateFrameworks/MediaAnalysisServices.framework/Versions/A/MediaAnalysisServices`

```diff

-435.79.5.4.0
-  __TEXT.__text: 0x3f400
-  __TEXT.__objc_methlist: 0x4f74
-  __TEXT.__const: 0x100
-  __TEXT.__cstring: 0x3adf
-  __TEXT.__gcc_except_tab: 0x44c8
-  __TEXT.__oslogstring: 0x2309
+460.7.1.0.0
+  __TEXT.__text: 0x406e0
+  __TEXT.__objc_methlist: 0x4fc4
+  __TEXT.__const: 0x108
+  __TEXT.__cstring: 0x3e38
+  __TEXT.__gcc_except_tab: 0x44d8
+  __TEXT.__oslogstring: 0x2326
   __TEXT.__dlopen_cstrs: 0x417
-  __TEXT.__unwind_info: 0x2098
+  __TEXT.__unwind_info: 0x2120
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0x430
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1958
+  __DATA_CONST.__objc_selrefs: 0x1990
   __DATA_CONST.__objc_protorefs: 0x40
   __DATA_CONST.__objc_superrefs: 0x3f0
   __DATA_CONST.__got: 0x518
   __AUTH_CONST.__const: 0xc68
-  __AUTH_CONST.__cfstring: 0x4ce0
-  __AUTH_CONST.__objc_const: 0xa228
+  __AUTH_CONST.__cfstring: 0x4de0
+  __AUTH_CONST.__objc_const: 0xa2e8
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x1180
-  __DATA.__objc_ivar: 0x5a4
+  __DATA.__objc_ivar: 0x5b4
   __DATA.__data: 0x420
   __DATA_DIRTY.__objc_data: 0x1860
   __DATA_DIRTY.__bss: 0x80

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1726
-  Symbols:   3893
-  CStrings:  864
+  Functions: 1771
+  Symbols:   3904
+  CStrings:  877
 
Symbols:
+ -[MADTextTokenizationRequest computeOffsets]
+ -[MADTextTokenizationRequest setComputeOffsets:]
+ -[MADTextTokenizationResult initWithTokenIDs:tokenOffsets:error:]
+ -[MADTextTokenizationResult tokenOffsets]
+ -[MADVideoSafetyClassificationRequest goreFrameCountThreshold]
+ -[MADVideoSafetyClassificationRequest setGoreFrameCountThreshold:]
+ -[MADVideoSafetyClassificationRequest setViolentFrameCountThreshold:]
+ -[MADVideoSafetyClassificationRequest violentFrameCountThreshold]
+ OBJC_IVAR_$_MADTextTokenizationRequest._computeOffsets
+ OBJC_IVAR_$_MADTextTokenizationResult._tokenOffsets
+ OBJC_IVAR_$_MADVideoSafetyClassificationRequest._goreFrameCountThreshold
+ OBJC_IVAR_$_MADVideoSafetyClassificationRequest._violentFrameCountThreshold
- -[MADTextTokenizationResult initWithTokenIDs:error:]
CStrings:
+ ", goreFrameCountThreshold: %@"
+ ", tokenOffsets: %@"
+ ", violentFrameCountThreshold: %@"
+ "./Utilities/CGUtilities.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/MediaAnalysis/MediaAnalysisServices/ComputeService/MADCoreMLResult.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/MediaAnalysis/MediaAnalysisServices/MADVideoSession/MADVideoSession.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/MediaAnalysis/MediaAnalysisServices/MADVideoSession/Utilities/MADPixelBufferProcesser.mm"
+ "ComputeOffsets"
+ "GoreFrameCountThreshold"
+ "TokenOffsets"
+ "ViolentFrameCountThreshold"
+ "[LOG_ERROR] %s[%d]: code %d\n"
+ "computeOffsets: %d, "
```
