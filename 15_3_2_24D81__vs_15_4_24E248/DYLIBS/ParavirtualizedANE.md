## ParavirtualizedANE

> `/System/Library/PrivateFrameworks/ParavirtualizedANE.framework/Versions/A/ParavirtualizedANE`

```diff

-370.31.1.0.0
-  __TEXT.__text: 0x13e98
-  __TEXT.__auth_stubs: 0x410
-  __TEXT.__objc_methlist: 0x52c
-  __TEXT.__const: 0x1b0
-  __TEXT.__cstring: 0xbb2
-  __TEXT.__oslogstring: 0x3636
-  __TEXT.__gcc_except_tab: 0x2508
-  __TEXT.__unwind_info: 0x518
+370.56.0.0.0
+  __TEXT.__text: 0x14e34
+  __TEXT.__auth_stubs: 0x430
+  __TEXT.__objc_methlist: 0x53c
+  __TEXT.__const: 0x190
+  __TEXT.__cstring: 0xc25
+  __TEXT.__oslogstring: 0x35c7
+  __TEXT.__gcc_except_tab: 0x26d0
+  __TEXT.__unwind_info: 0x538
   __TEXT.__objc_classname: 0x2f
-  __TEXT.__objc_methname: 0x1669
-  __TEXT.__objc_methtype: 0x79c
-  __TEXT.__objc_stubs: 0x1760
-  __DATA_CONST.__got: 0x140
+  __TEXT.__objc_methname: 0x1702
+  __TEXT.__objc_methtype: 0x7ab
+  __TEXT.__objc_stubs: 0x1800
+  __DATA_CONST.__got: 0x148
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x678
+  __DATA_CONST.__objc_selrefs: 0x6a0
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x218
+  __AUTH_CONST.__auth_got: 0x228
   __AUTH_CONST.__const: 0xb0
-  __AUTH_CONST.__cfstring: 0xbc0
+  __AUTH_CONST.__cfstring: 0xc80
   __AUTH_CONST.__objc_const: 0x320
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0xa0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E58738BF-D418-300B-BA67-303431DE68DC
-  Functions: 320
-  Symbols:   752
-  CStrings:  697
+  UUID: DCE85382-8BC2-37AD-A3B9-76B84E0B27E5
+  Functions: 328
+  Symbols:   769
+  CStrings:  720
 
Symbols:
+ +[_ANEVirtualPlatformClient getPrecompiledModelPath:error:]
+ -[_ANEVirtualPlatformClient loadModelDictionary:].cold.3
+ -[_ANEVirtualPlatformClient validateNetworkCreate:].cold.19
+ -[_ANEVirtualPlatformClient validateNetworkCreate:].cold.20
+ -[_ANEVirtualPlatformClient validateNetworkCreate:].cold.21
+ -[_ANEVirtualPlatformClient validateNetworkCreate:].cold.22
+ GCC_except_table105
+ GCC_except_table110
+ GCC_except_table114
+ GCC_except_table120
+ GCC_except_table88
+ GCC_except_table90
+ _CFDictionaryCreateMutable
+ _OBJC_CLASS_$__ANEErrors
+ _OUTLINED_FUNCTION_28
+ _OUTLINED_FUNCTION_29
+ __ZNSt3__115allocate_sharedB8ne190102I17_IOSurfaceWrapperNS_9allocatorIS1_EEJRjRU8__strongPU19objcproto9OS_os_log8NSObjectELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
+ __ZNSt3__115allocate_sharedB8ne190102I17_IOSurfaceWrapperNS_9allocatorIS1_EEJRjU8__strongPU19objcproto9OS_os_log8NSObjectELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
+ __ZNSt3__119__shared_weak_count16__release_sharedB8ne190102Ev
+ __ZNSt3__120__shared_ptr_emplaceI17_IOSurfaceWrapperNS_9allocatorIS1_EEEC2B8ne190102IJRjRU8__strongPU19objcproto9OS_os_log8NSObjectES3_Li0EEES3_DpOT_
+ __ZNSt3__120__shared_ptr_emplaceI17_IOSurfaceWrapperNS_9allocatorIS1_EEEC2B8ne190102IJRjU8__strongPU19objcproto9OS_os_log8NSObjectES3_Li0EEES3_DpOT_
+ _kCFTypeDictionaryKeyCallBacks
+ _kCFTypeDictionaryValueCallBacks
+ _objc_autorelease
+ _objc_msgSend$dataNotFoundForMethod:
+ _objc_msgSend$decodeObjectOfClass:forKey:
+ _objc_msgSend$fileNotFoundErrorForMethod:
+ _objc_msgSend$getPrecompiledModelPath:error:
+ _objc_msgSend$numberWithLongLong:
+ _objc_msgSend$programInferenceOtherErrorForMethod:
+ _objc_msgSend$stringByAppendingPathComponent:
+ _objc_msgSend$unsignedLongLongValue
- GCC_except_table102
- GCC_except_table109
- GCC_except_table111
- GCC_except_table117
- GCC_except_table89
- _OBJC_CLASS_$_NSArray
- _OBJC_CLASS_$_NSSet
- __ZNSt3__115allocate_sharedB8ne180100I17_IOSurfaceWrapperNS_9allocatorIS1_EEJRjRU8__strongPU19objcproto9OS_os_log8NSObjectEvEENS_10shared_ptrIT_EERKT0_DpOT1_
- __ZNSt3__115allocate_sharedB8ne180100I17_IOSurfaceWrapperNS_9allocatorIS1_EEJRjU8__strongPU19objcproto9OS_os_log8NSObjectEvEENS_10shared_ptrIT_EERKT0_DpOT1_
- __ZNSt3__119__shared_weak_count16__release_sharedB8ne180100Ev
- __ZNSt3__120__shared_ptr_emplaceI17_IOSurfaceWrapperNS_9allocatorIS1_EEEC2B8ne180100IJRjRU8__strongPU19objcproto9OS_os_log8NSObjectES3_Li0EEES3_DpOT_
- __ZNSt3__120__shared_ptr_emplaceI17_IOSurfaceWrapperNS_9allocatorIS1_EEEC2B8ne180100IJRjU8__strongPU19objcproto9OS_os_log8NSObjectES3_Li0EEES3_DpOT_
- _objc_msgSend$arrayWithObjects:count:
- _objc_msgSend$decodeObjectOfClasses:forKey:
- _objc_msgSend$setWithArray:
CStrings:
+ "%@ ERROR: Failed to get milTextData!"
+ "%@ ERROR: Failed to get milTextDataIOSurface!"
+ "%@ ERROR: milTextDataIOSID is 0!"
+ "%@ ERROR: milTextDataLength is 0!"
+ "%@: ERROR : loadModel FAILED : Precompiled option set but could not get path to precompiled model"
+ "%@: FAILED to generate aneRequest"
+ "%@: FAILED to get model from local cache"
+ "%@: FAILED to get programHandle"
+ "%@: No optionsIOSID found"
+ "%@: optionsLength is 0 for optionsIOSID=%u"
+ "%s: unarchive error %@ \n"
+ "@32@0:8@16^@24"
+ "Failed to generate aneRequest"
+ "Model not found"
+ "ProgramHandle not found"
+ "dataNotFoundForMethod:"
+ "decodeObjectOfClass:forKey:"
+ "fileNotFoundErrorForMethod:"
+ "getPrecompiledModelPath:error:"
+ "ioSIDMilTextData"
+ "milTextDataLength"
+ "model.mil"
+ "numberWithLongLong:"
+ "programInferenceOtherErrorForMethod:"
+ "stringByAppendingPathComponent:"
+ "unsignedLongLongValue"
- "%@: ANEVirtualClient unarchive error %@ \n"
- "%@: ANEVirtualPlatformClient evaluateWithModelDictionary FAILED : Could not pull ANEModel from local cache : programHandle=0"
- "%@: ANEVirtualPlatformClient evaluateWithModelDictionary FAILED : kVirtANEIOSIDOptions not found!"
- "%@: ANEVirtualPlatformClient evaluateWithModelDictionary FAILED : kVirtANEOptionsLength not found!"
- "%@: ANEVirtualPlatformClient evaluateWithModelDictionary FAILED : programHandle cannot be 0"
- "%@: ANEVirtualPlatformClient evaluateWithModelDictionary NON-FATAL : could not update performance stats"
- "arrayWithObjects:count:"
- "decodeObjectOfClasses:forKey:"
- "setWithArray:"

```
