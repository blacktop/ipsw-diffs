## AXMediaUtilities

> `/System/Library/PrivateFrameworks/AXMediaUtilities.framework/AXMediaUtilities`

```diff

-  __TEXT.__text: 0xd4428
+  __TEXT.__text: 0xd43d8
   __TEXT.__objc_methlist: 0xb51c
   __TEXT.__const: 0x166c
   __TEXT.__dlopen_cstrs: 0xc72
   __TEXT.__swift5_typeref: 0x2f0
-  __TEXT.__cstring: 0xa686
+  __TEXT.__cstring: 0xa679
   __TEXT.__swift5_reflstr: 0x25d
   __TEXT.__swift5_assocty: 0xc0
   __TEXT.__constg_swiftt: 0x3f8

   __DATA_CONST.__objc_protolist: 0xd0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6220
+  __DATA_CONST.__objc_selrefs: 0x6228
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x418
   __DATA_CONST.__objc_arraydata: 0x6b8
   __DATA_CONST.__got: 0xe30
   __AUTH_CONST.__const: 0x1d28
-  __AUTH_CONST.__cfstring: 0xcc40
+  __AUTH_CONST.__cfstring: 0xcc20
   __AUTH_CONST.__objc_const: 0x14378
   __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__objc_intobj: 0xab0
   __AUTH_CONST.__objc_doubleobj: 0x290
   __AUTH_CONST.__objc_arrayobj: 0x240
   __AUTH_CONST.__objc_dictobj: 0x78
-  __AUTH_CONST.__auth_got: 0xef8
+  __AUTH_CONST.__auth_got: 0xf00
   __AUTH.__objc_data: 0x3db0
   __AUTH.__data: 0x78
   __DATA.__objc_ivar: 0xec0

   - /System/Library/Frameworks/NaturalLanguage.framework/NaturalLanguage
   - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
   - /System/Library/Frameworks/Security.framework/Security
+  - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
   - /System/Library/Frameworks/VideoToolbox.framework/VideoToolbox
   - /System/Library/Frameworks/Vision.framework/Vision

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 4743
-  Symbols:   15805
-  CStrings:  4125
+  Symbols:   15807
+  CStrings:  4123
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__const : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__swift5_assocty : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_fieldmd : content changed
~ __TEXT.__swift5_builtin : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __TEXT.__unwind_info : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__weak_got : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__got : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__weak_auth_got : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_doubleobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH.__objc_data : content changed
~ __AUTH.__data : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
Symbols:
+ _SCDynamicStoreCopyComputerName
+ _objc_msgSend$setMuteHapticsWhileRecordingAudio:
Functions:
~ +[ImageTools create420YCbCr8BufferFromPlanar8Buffer:withWidth:andWithHeight:andWithBytesPerRow:toLumaBuffer:withBytesPerRowLuma:andToChromaBuffer:withBytesPerRowChroma:] : 980 -> 976
~ +[ImageTools create420YCbCr8BufferFromRGB8Buffer:withWidth:andWithHeight:andWithBytesPerRow:andAlphaFirst:toLumaBuffer:withBytesPerRowLuma:andToChromaBuffer:withBytesPerRowChroma:] : 900 -> 896
~ +[ImageTools createRGB8BufferFrom420Y8PlanarBuffer:withBytesPerRowY:andFrom420Cb8Buffer:withBytesPerRowCb:andFrom420Cr8Buffer:withBytesPerRowCr:andWithWidth:andWithHeight:andAlphaFirst:toRGB8Buffer:withBytesPerRowDst:] : 708 -> 668
~ +[ImageTools createRGB8BufferFrom420Y8BiPlanarBuffer:withBytesPerRowLuma:andFrom420CbCr8Buffer:withBytesPerRowChroma:andWithWidth:andWithHeight:andAlphaFirst:toRGB8Buffer:withBytesPerRowDst:] : 688 -> 652
~ -[AXMHapticComponent transitionToState:completion:] : 988 -> 1000
~ -[AXMDeviceInfo computerName] : 116 -> 140
~ sub_1caeef834 -> sub_1ceede874 : 768 -> 740
~ sub_1caef0938 -> sub_1ceedf95c : 416 -> 412
CStrings:
- "ComputerName"

```
