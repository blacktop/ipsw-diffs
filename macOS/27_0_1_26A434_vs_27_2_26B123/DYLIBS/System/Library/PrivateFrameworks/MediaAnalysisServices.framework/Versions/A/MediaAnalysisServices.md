## MediaAnalysisServices

> `/System/Library/PrivateFrameworks/MediaAnalysisServices.framework/Versions/A/MediaAnalysisServices`

```diff

-435.79.5.4.0
-  __TEXT.__text: 0x403f8
-  __TEXT.__objc_methlist: 0x4f74
+460.14.5.2.0
+  __TEXT.__text: 0x40bc0
+  __TEXT.__objc_methlist: 0x4fd4
   __TEXT.__const: 0x100
-  __TEXT.__cstring: 0x3adf
-  __TEXT.__gcc_except_tab: 0x44c8
+  __TEXT.__cstring: 0x3bbf
+  __TEXT.__gcc_except_tab: 0x455c
   __TEXT.__oslogstring: 0x2309
   __TEXT.__dlopen_cstrs: 0x417
-  __TEXT.__unwind_info: 0x1c70
+  __TEXT.__unwind_info: 0x1c80
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0x430
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1958
+  __DATA_CONST.__objc_selrefs: 0x19b0
   __DATA_CONST.__objc_protorefs: 0x40
   __DATA_CONST.__objc_superrefs: 0x3f0
-  __DATA_CONST.__got: 0x518
+  __DATA_CONST.__got: 0x520
   __AUTH_CONST.__const: 0xc68
-  __AUTH_CONST.__cfstring: 0x4ce0
-  __AUTH_CONST.__objc_const: 0xa228
+  __AUTH_CONST.__cfstring: 0x4e00
+  __AUTH_CONST.__objc_const: 0xa2e8
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x1180
-  __DATA.__objc_ivar: 0x5a4
-  __DATA.__data: 0x420
+  __DATA.__objc_ivar: 0x5b4
   __DATA.__bss: 0x90
-  __DATA_DIRTY.__objc_data: 0x1860
+  __DATA_DIRTY.__objc_data: 0x29e0
+  __DATA_DIRTY.__data: 0x420
   __DATA_DIRTY.__bss: 0x80
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1726
-  Symbols:   3893
-  CStrings:  864
+  Functions: 1734
+  Symbols:   3909
+  CStrings:  873
 
Symbols:
+ -[MADService fileTypeForURL:]
+ -[MADTextTokenizationRequest computeOffsets]
+ -[MADTextTokenizationRequest setComputeOffsets:]
+ -[MADTextTokenizationResult initWithTokenIDs:tokenOffsets:error:]
+ -[MADTextTokenizationResult tokenOffsets]
+ -[MADVideoSafetyClassificationRequest goreFrameCountThreshold]
+ -[MADVideoSafetyClassificationRequest setGoreFrameCountThreshold:]
+ -[MADVideoSafetyClassificationRequest setViolentFrameCountThreshold:]
+ -[MADVideoSafetyClassificationRequest violentFrameCountThreshold]
+ GCC_except_table100
+ GCC_except_table110
+ GCC_except_table131
+ GCC_except_table133
+ GCC_except_table142
+ GCC_except_table148
+ GCC_except_table156
+ GCC_except_table159
+ GCC_except_table171
+ GCC_except_table174
+ GCC_except_table177
+ GCC_except_table179
+ GCC_except_table181
+ GCC_except_table183
+ GCC_except_table185
+ GCC_except_table188
+ GCC_except_table195
+ GCC_except_table206
+ GCC_except_table211
+ GCC_except_table214
+ GCC_except_table88
+ OBJC_IVAR_$_MADTextTokenizationRequest._computeOffsets
+ OBJC_IVAR_$_MADTextTokenizationResult._tokenOffsets
+ OBJC_IVAR_$_MADVideoSafetyClassificationRequest._goreFrameCountThreshold
+ OBJC_IVAR_$_MADVideoSafetyClassificationRequest._violentFrameCountThreshold
+ _OBJC_CLASS_$_NSFileHandle
+ _objc_msgSend$fileHandleForReadingFromURL:error:
+ _objc_msgSend$fileTypeForURL:
+ _objc_msgSend$pathExtension
+ _objc_msgSend$requestImageProcessing:forFileHandle:fileType:identifier:requestID:andReply:
+ _objc_msgSend$requestVideoProcessing:fileHandle:fileType:fileURL:sandboxToken:identifier:requestID:reply:
+ _objc_msgSend$requiresBlastdoor
+ _objc_msgSend$typeWithFilenameExtension:
- -[MADTextTokenizationResult initWithTokenIDs:error:]
- GCC_except_table112
- GCC_except_table132
- GCC_except_table134
- GCC_except_table143
- GCC_except_table149
- GCC_except_table158
- GCC_except_table168
- GCC_except_table173
- GCC_except_table176
- GCC_except_table178
- GCC_except_table180
- GCC_except_table182
- GCC_except_table184
- GCC_except_table186
- GCC_except_table189
- GCC_except_table196
- GCC_except_table209
- GCC_except_table212
- GCC_except_table85
- GCC_except_table87
- GCC_except_table89
- GCC_except_table91
- GCC_except_table97
- _objc_msgSend$requestImageProcessing:forAssetURL:withSandboxToken:identifier:requestID:andReply:
- _objc_msgSend$requestVideoProcessing:assetURL:sandboxToken:identifier:requestID:reply:
CStrings:
+ ", goreFrameCountThreshold: %@"
+ ", tokenOffsets: %@"
+ ", violentFrameCountThreshold: %@"
+ "ComputeOffsets"
+ "Could not determine a media type for %@"
+ "GoreFrameCountThreshold"
+ "TokenOffsets"
+ "ViolentFrameCountThreshold"
+ "computeOffsets: %d, "
```
