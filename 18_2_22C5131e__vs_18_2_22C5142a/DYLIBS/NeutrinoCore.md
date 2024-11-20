## NeutrinoCore

> `/System/Library/PrivateFrameworks/NeutrinoCore.framework/NeutrinoCore`

```diff

-720.10.101.0.0
-  __TEXT.__text: 0x1c745c
-  __TEXT.__auth_stubs: 0x1bb0
-  __TEXT.__objc_methlist: 0x12348
-  __TEXT.__const: 0x1e68
-  __TEXT.__gcc_except_tab: 0x7b0c
-  __TEXT.__cstring: 0x2250b
-  __TEXT.__oslogstring: 0x3114
+722.0.180.0.0
+  __TEXT.__text: 0x1cae1c
+  __TEXT.__auth_stubs: 0x1c10
+  __TEXT.__objc_methlist: 0x12498
+  __TEXT.__const: 0x1e78
+  __TEXT.__gcc_except_tab: 0x7ca4
+  __TEXT.__cstring: 0x22849
+  __TEXT.__oslogstring: 0x33e1
   __TEXT.__dlopen_cstrs: 0x8a
-  __TEXT.__unwind_info: 0x5558
-  __TEXT.__objc_classname: 0x2dc9
-  __TEXT.__objc_methname: 0x1f286
-  __TEXT.__objc_methtype: 0x545f
-  __TEXT.__objc_stubs: 0x17fe0
-  __DATA_CONST.__got: 0x18b0
-  __DATA_CONST.__const: 0x2310
-  __DATA_CONST.__objc_classlist: 0xde8
+  __TEXT.__unwind_info: 0x55e8
+  __TEXT.__objc_classname: 0x2df8
+  __TEXT.__objc_methname: 0x1f513
+  __TEXT.__objc_methtype: 0x5481
+  __TEXT.__objc_stubs: 0x18160
+  __DATA_CONST.__got: 0x18d0
+  __DATA_CONST.__const: 0x2470
+  __DATA_CONST.__objc_classlist: 0xdf8
   __DATA_CONST.__objc_catlist: 0x88
   __DATA_CONST.__objc_protolist: 0x2e8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7760
+  __DATA_CONST.__objc_selrefs: 0x77f0
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x9d8
-  __DATA_CONST.__objc_arraydata: 0x948
-  __AUTH_CONST.__auth_got: 0xdf0
-  __AUTH_CONST.__const: 0x2e08
-  __AUTH_CONST.__cfstring: 0x103c0
-  __AUTH_CONST.__objc_const: 0x26480
-  __AUTH_CONST.__objc_intobj: 0x7e0
+  __DATA_CONST.__objc_superrefs: 0x9e8
+  __DATA_CONST.__objc_arraydata: 0x968
+  __AUTH_CONST.__auth_got: 0xe20
+  __AUTH_CONST.__const: 0x2ee8
+  __AUTH_CONST.__cfstring: 0x10560
+  __AUTH_CONST.__objc_const: 0x26708
+  __AUTH_CONST.__objc_intobj: 0x7f8
   __AUTH_CONST.__objc_dictobj: 0x280
   __AUTH_CONST.__objc_doubleobj: 0xe0
-  __AUTH_CONST.__objc_arrayobj: 0xc0
+  __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH_CONST.__objc_floatobj: 0x30
-  __AUTH.__objc_data: 0xa50
-  __DATA.__objc_ivar: 0x11fc
-  __DATA.__data: 0x23a8
+  __AUTH.__objc_data: 0xaf0
+  __DATA.__objc_ivar: 0x1210
+  __DATA.__data: 0x23b8
   __DATA.__crash_info: 0x40
   __DATA.__bss: 0x278
   __DATA.__common: 0x10

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 7120
-  Symbols:   8984
-  CStrings:  11008
+  Functions: 7159
+  Symbols:   9036
+  CStrings:  11079
 
Symbols:
+ _CGColorSpaceCreateExtended
+ _CGColorSpaceGetHeadroomInfo
+ _CMSampleBufferGetFormatDescription
+ _CMSampleBufferGetSampleAttachmentsArray
+ _CMTimeRangeCopyAsDictionary
+ _CMTimeRangeMakeFromDictionary
+ _NUQuickTimeMetadataKey_SmartStyleRenderingVersion
+ _NUQuicktimeMetadataKey_SmartStyleRenderingBypassed
+ _OBJC_CLASS_$_NUHDROpticalScaleNode
+ _OBJC_CLASS_$_NUVideoCorruptionInfo
+ _OBJC_METACLASS_$_NUHDROpticalScaleNode
+ _OBJC_METACLASS_$_NUVideoCorruptionInfo
+ _PFExists
+ _kCMFormatDescriptionExtension_BitsPerComponent
+ _kCMSampleAttachmentKey_HEVCSyncSampleNALUnitType
- _CGColorSpaceIsHLGBased
CStrings:
+ "\x01\x13\xf43"
+ "\x12\x16"
+ " time: %!@(MISSING)"
+ "+[NUVideoUtilities assetContainsDuplicatePTSSamples:assetTrack:error:]"
+ "+[NUVideoUtilities computeMalformedTimeRangeTrackInAsset:assetTrack:error:]"
+ "+[NUVideoUtilities validateSemanticStyleAsset:error:]"
+ "-[NUColorSpace initWithColorSpaceName:]"
+ "-[NUHDROpticalScaleNode initWithInput:opticalScale:]"
+ "-[NUHDROpticalScaleNode initWithSettings:inputs:]"
+ "-[NUVideoCorruptionInfo initWithType:corruptedRanges:]"
+ "@16@?0@\"NSDictionary\"8"
+ "@32@0:8Q16@24"
+ "B16@?0@\"AVMetadataItem\"8"
+ "B16@?0@\"NSDictionary\"8"
+ "B16@?0@\"NUVideoCorruptionInfo\"8"
+ "Bypassing revert due to corrupted video track"
+ "CIColorMatrix"
+ "Could not determine if asset contains duplicate PTS for the main video track - assuming it's invalid. %!{(MISSING)public}@"
+ "Could not determine malformed ranges for this delta track - assuming it's invalid. %!{(MISSING)public}@"
+ "Could not read next sample buffer"
+ "Detected invalid video asset for semantic styles:\n%!{(MISSING)public}@"
+ "DuplicatePTSInMainVideo"
+ "Failed to obtain delta at time %!{(MISSING)public}@, ignoring. Error: %!{(MISSING)public}@"
+ "Failed to obtain delta, ignoring. Error: %!{(MISSING)public}@"
+ "Failed to obtain metadata sample from pipeline state at time %!{(MISSING)public}@, ignoring"
+ "Failed to validate semantic style video asset: %!{(MISSING)public}@"
+ "HDROpticalScaleNode:scale:"
+ "Issue: %!@(MISSING)"
+ "MalformedDeltaTrack"
+ "MalformedStyleMetadataTrack"
+ "Missing delta frame - ignoring"
+ "Missing delta video track properties, omitting from video composition"
+ "Missing main video track"
+ "Missing video track properties for auxiliary image type "
+ "MissingAuxiliaryTrack (%!@(MISSING))"
+ "MissingStyleMetadataTrack"
+ "NUHDROpticalScaleNode"
+ "NUVideoCorruptionInfo"
+ "T@\"NSArray\",C,N"
+ "T@\"NSArray\",C,N,V_corruptedRanges"
+ "T@\"NSArray\",C,N,V_videoCorruptionInfo"
+ "T@\"NSString\",C,N,V_trackMediaCharateristic"
+ "TQ,V_type"
+ "Unexpected image type %!@(MISSING)"
+ "[%!@(MISSING)x%!@(MISSING)]"
+ "[NUVideoCompositor videoMetadataSamplesFromRequest] skipping metadata sample at %!{(MISSING)public}@. metadataGroup is nil for trackID %!d(MISSING) (%!{(MISSING)public}@),\n DebugInfo: %!{(MISSING)public}@"
+ "_corruptedRanges"
+ "_corruptionInfo"
+ "_trackMediaCharateristic"
+ "_videoCorruptionInfo"
+ "assetContainsDuplicatePTSSamples:assetTrack:error:"
+ "com.apple.quicktime.smartstyle.rendering-version"
+ "computeMalformedTimeRangeTrackInAsset:assetTrack:error:"
+ "corruptedRanges"
+ "extended"
+ "headroom"
+ "initWithColorSpaceName:"
+ "initWithInput:opticalScale:"
+ "initWithType:corruptedRanges:"
+ "inputBVector"
+ "inputGVector"
+ "inputRVector"
+ "isAssetStyled:"
+ "opticalScale"
+ "opticalScale > 0.0"
+ "ranges != nil"
+ "setCorruptedRanges:"
+ "setTrackMediaCharateristic:"
+ "setType:"
+ "setVideoCorruptionInfo:"
+ "trackMediaCharateristic"
+ "tracksWithMediaCharacteristic:forAsset:"
+ "v24@0:8@\"NSArray\"16"
+ "v32@?0@\"NSDictionary\"8Q16^B24"
+ "v56@?0{?=qiIq}8{?=qiIq}32"
+ "validateSemanticStyleAsset:error:"
+ "videoCorruptionInfo"
- "\x01\x13\xf42"
- "Failed to obtain metadata sample from pipeline state"
- "Failed to obtain style image"
- "Missing delta video track properties"
- "[NUVideoCompositor videoMetadataSamplesFromRequest] skipping metadata sample. metadataGroup is nil for trackID %!d(MISSING) (%!{(MISSING)public}@),\n DebugInfo: %!{(MISSING)public}@"
- "imageByToneMappingColorSpaceToWorkingSpace:"
- "kCIContextHLGOpticalScale"

```
