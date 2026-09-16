## MediaAnalysisServices

> `/System/Library/PrivateFrameworks/MediaAnalysisServices.framework/MediaAnalysisServices`

```diff

-435.79.1.5.0
-  __TEXT.__text: 0x3b8f8
-  __TEXT.__objc_methlist: 0x4fa4
-  __TEXT.__const: 0xf8
-  __TEXT.__cstring: 0x38be
-  __TEXT.__gcc_except_tab: 0x4448
-  __TEXT.__oslogstring: 0x2309
+460.7.1.0.0
+  __TEXT.__text: 0x3cbb4
+  __TEXT.__objc_methlist: 0x5024
+  __TEXT.__const: 0x100
+  __TEXT.__cstring: 0x3ba5
+  __TEXT.__gcc_except_tab: 0x4458
+  __TEXT.__oslogstring: 0x2326
   __TEXT.__dlopen_cstrs: 0x417
-  __TEXT.__unwind_info: 0x2040
+  __TEXT.__unwind_info: 0x20c8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0x430
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1978
+  __DATA_CONST.__objc_selrefs: 0x19d0
   __DATA_CONST.__objc_protorefs: 0x40
   __DATA_CONST.__objc_superrefs: 0x3f0
   __DATA_CONST.__got: 0x518
   __AUTH_CONST.__const: 0x338
-  __AUTH_CONST.__cfstring: 0x4ce0
-  __AUTH_CONST.__objc_const: 0xa248
+  __AUTH_CONST.__cfstring: 0x4de0
+  __AUTH_CONST.__objc_const: 0xa328
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x11d0
-  __DATA.__objc_ivar: 0x5a4
+  __DATA.__objc_ivar: 0x5b4
   __DATA.__data: 0x420
   __DATA_DIRTY.__objc_data: 0x1810
   __DATA_DIRTY.__bss: 0x80

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1698
-  Symbols:   3789
-  CStrings:  858
+  Functions: 1743
+  Symbols:   3800
+  CStrings:  871
 
Symbols:
+ -[MADTextTokenizationRequest computeOffsets]
+ -[MADTextTokenizationRequest setComputeOffsets:]
+ -[MADTextTokenizationResult initWithTokenIDs:tokenOffsets:error:]
+ -[MADTextTokenizationResult tokenOffsets]
+ -[MADVideoSafetyClassificationRequest goreFrameCountThreshold]
+ -[MADVideoSafetyClassificationRequest setGoreFrameCountThreshold:]
+ -[MADVideoSafetyClassificationRequest setViolentFrameCountThreshold:]
+ -[MADVideoSafetyClassificationRequest violentFrameCountThreshold]
+ _OBJC_IVAR_$_MADTextTokenizationRequest._computeOffsets
+ _OBJC_IVAR_$_MADTextTokenizationResult._tokenOffsets
+ _OBJC_IVAR_$_MADVideoSafetyClassificationRequest._goreFrameCountThreshold
+ _OBJC_IVAR_$_MADVideoSafetyClassificationRequest._violentFrameCountThreshold
- -[MADTextTokenizationResult initWithTokenIDs:error:]
CStrings:
+ ", goreFrameCountThreshold: %@"
+ ", tokenOffsets: %@"
+ ", violentFrameCountThreshold: %@"
+ "./Utilities/CGUtilities.h"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/MediaAnalysis/MediaAnalysisServices/ComputeService/MADCoreMLResult.mm"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/MediaAnalysis/MediaAnalysisServices/MADVideoSession/MADVideoSession.mm"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/MediaAnalysis/MediaAnalysisServices/MADVideoSession/Utilities/MADPixelBufferProcesser.mm"
+ "ComputeOffsets"
+ "GoreFrameCountThreshold"
+ "TokenOffsets"
+ "ViolentFrameCountThreshold"
+ "[LOG_ERROR] %s[%d]: code %d\n"
+ "computeOffsets: %d, "
```
