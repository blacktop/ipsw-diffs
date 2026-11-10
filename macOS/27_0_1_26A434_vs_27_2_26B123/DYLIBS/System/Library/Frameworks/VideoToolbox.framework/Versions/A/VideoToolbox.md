## VideoToolbox

> `/System/Library/Frameworks/VideoToolbox.framework/Versions/A/VideoToolbox`

```diff

-3350.77.5.6.0
-  __TEXT.__text: 0x555ae0
-  __TEXT.__objc_methlist: 0x159c
-  __TEXT.__cstring: 0xd6bd
+3385.14.5.2.0
+  __TEXT.__text: 0x556334
+  __TEXT.__objc_methlist: 0x15cc
+  __TEXT.__cstring: 0xd6ed
   __TEXT.__const: 0xdd8c
   __TEXT.__oslogstring: 0x5b62
-  __TEXT.__gcc_except_tab: 0x1f0
+  __TEXT.__gcc_except_tab: 0x204
   __TEXT.__dlopen_cstrs: 0x9b
   __TEXT.__constg_swiftt: 0x4d8
   __TEXT.__swift5_typeref: 0x4d7

   __TEXT.__swift_as_entry: 0x8
   __TEXT.__swift_as_ret: 0x8
   __TEXT.__swift_as_cont: 0x1c
-  __TEXT.__unwind_info: 0x6088
+  __TEXT.__unwind_info: 0x6090
   __TEXT.__eh_frame: 0x8020
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x33f0
+  __DATA_CONST.__const: 0x3458
   __DATA_CONST.__objc_classlist: 0xd0
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xcb8
+  __DATA_CONST.__objc_selrefs: 0xcd0
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0xb8
   __DATA_CONST.__objc_arraydata: 0x38
-  __DATA_CONST.__got: 0xe38
+  __DATA_CONST.__got: 0xe60
   __AUTH_CONST.__const: 0x44048
-  __AUTH_CONST.__cfstring: 0xc0c0
-  __AUTH_CONST.__objc_const: 0x3db0
+  __AUTH_CONST.__cfstring: 0xc140
+  __AUTH_CONST.__objc_const: 0x3ed0
   __AUTH_CONST.__objc_doubleobj: 0x30
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_intobj: 0x48
-  __AUTH_CONST.__auth_got: 0x1eb0
+  __AUTH_CONST.__auth_got: 0x1ed0
   __AUTH_CONST.__auth_ptr: 0x300
   __AUTH.__objc_data: 0x730
   __AUTH.__data: 0x1d8
-  __DATA.__objc_ivar: 0x244
-  __DATA.__data: 0x9b0
+  __DATA.__objc_ivar: 0x25c
+  __DATA.__data: 0x9d0
   __DATA.__bss: 0x2040
   __DATA.__common: 0xe8
   __DATA_DIRTY.__objc_data: 0x50
   __DATA_DIRTY.__data: 0x4e4
   __DATA_DIRTY.__crash_info: 0x148
-  __DATA_DIRTY.__bss: 0x64a
+  __DATA_DIRTY.__bss: 0x652
   __DATA_DIRTY.__common: 0x128
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate
   - /System/Library/Frameworks/ColorSync.framework/Versions/A/ColorSync

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 9497
-  Symbols:   11655
-  CStrings:  2221
+  Functions: 9502
+  Symbols:   11678
+  CStrings:  2225
 
Symbols:
+ -[VTLowLatencyFrameInterpolationImplementation modelID]
+ -[VTLowLatencySuperResolutionScalerImplementation modelID]
+ -[VTTemporalNoiseFilterImplementation _validateParameters:]
+ GCC_except_table35
+ OBJC_IVAR_$_VTFrameProcessor._firstProcessCallTimeMs
+ OBJC_IVAR_$_VTFrameProcessor._lastErrorCode
+ OBJC_IVAR_$_VTFrameProcessor._lastProcessCallTimeMs
+ OBJC_IVAR_$_VTFrameProcessor._processCallCount
+ OBJC_IVAR_$_VTFrameProcessor._sourceFrameRateTotalMeasuredDurationSeconds
+ OBJC_IVAR_$_VTFrameProcessor._sourceFrameRateTotalMeasuredFrames
+ _CFBundleGetIdentifier
+ _CFBundleGetMainBundle
+ __OBJC_$_PROP_LIST_VTFrameProcessorImplementationPrivate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_VTFrameProcessorImplementationPrivate
+ ___block_descriptor_48_e8_32o40r_e53_v24?0"VTTemporalNoiseFilterParameters"8"NSError"16l
+ _kFigReportingEventKey_VTFP_ClientBundleID
+ _kFigReportingEventKey_VTFP_ModelID
+ _kFigReportingEventKey_VTFP_ProcessCallRate
+ _kFigReportingEventKey_VTFP_SourceFrameRate
+ _kVTCompressionPropertyKey_MachThreadPriorityForThreadEmittingFrames
+ _objc_autorelease
+ _objc_msgSend$_validateParameters:
+ _objc_msgSend$currentModel
+ _objc_msgSend$firstObject
+ _objc_msgSend$modelID
+ _objc_msgSend$nextFrame
+ _objc_opt_respondsToSelector
- -[VTTemporalNoiseFilterImplementation _validateParameters:error:]
- ___block_descriptor_48_e8_32o_e53_v24?0"VTTemporalNoiseFilterParameters"8"NSError"16l
- _objc_msgSend$_validateParameters:error:
- vtCopyCodecList
CStrings:
+ "ClientBundleID"
+ "ModelID"
+ "ProcessCallRate"
+ "SourceFrameRate"
```
