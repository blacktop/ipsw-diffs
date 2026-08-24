## login

> `/System/Library/PrivateFrameworks/login.framework/Versions/A/login`

```diff

-272.0.0.0.0
-  __TEXT.__text: 0x17f88
-  __TEXT.__objc_methlist: 0x12bc
+273.0.0.0.0
+  __TEXT.__text: 0x18744
+  __TEXT.__objc_methlist: 0x1334
   __TEXT.__const: 0x60
-  __TEXT.__gcc_except_tab: 0xd64
-  __TEXT.__cstring: 0x3aea
+  __TEXT.__gcc_except_tab: 0xd9c
+  __TEXT.__cstring: 0x3c95
   __TEXT.__dlopen_cstrs: 0xf5
-  __TEXT.__unwind_info: 0xa10
+  __TEXT.__unwind_info: 0xa48
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb18
+  __DATA_CONST.__objc_selrefs: 0xb68
   __DATA_CONST.__objc_protorefs: 0x58
   __DATA_CONST.__objc_superrefs: 0x90
+  __DATA_CONST.__objc_arraydata: 0x8
   __DATA_CONST.__got: 0x238
-  __AUTH_CONST.__const: 0x8c8
-  __AUTH_CONST.__cfstring: 0x2740
-  __AUTH_CONST.__objc_const: 0x4648
+  __AUTH_CONST.__const: 0x908
+  __AUTH_CONST.__cfstring: 0x2760
+  __AUTH_CONST.__objc_const: 0x46f8
+  __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x690
-  __DATA.__objc_ivar: 0xb0
+  __DATA.__objc_ivar: 0xc0
   __DATA.__data: 0x5b0
-  __DATA.__bss: 0x128
+  __DATA.__bss: 0x160
   __DATA.__common: 0x20
   __DATA_DIRTY.__objc_data: 0xf0
   __DATA_DIRTY.__bss: 0x40

   - /System/Library/PrivateFrameworks/login.framework/Versions/A/Frameworks/loginsupport.framework/Versions/A/loginsupport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 572
-  Symbols:   1504
-  CStrings:  513
+  Functions: 594
+  Symbols:   1540
+  CStrings:  519
 
Symbols:
+ +[LFVolume availabilityGenerationForTesting]
+ +[LFVolume setShouldCacheClassificationFailuresForTesting:]
+ -[LFVolume _computeDataVolumes]
+ -[LFVolume _pruneAvailabilityCacheIfStale]
+ -[LFVolume apfsDiskRefChecked]
+ -[LFVolume dataVolumesCache]
+ -[LFVolume dataVolumesChecked]
+ -[LFVolume setApfsDiskRefChecked:]
+ -[LFVolume setDataVolumesCache:]
+ -[LFVolume setDataVolumesChecked:]
+ GCC_except_table75
+ OBJC_IVAR_$_LFVolume._apfsDiskRefChecked
+ OBJC_IVAR_$_LFVolume._availabilityCacheGeneration
+ OBJC_IVAR_$_LFVolume._dataVolumesCache
+ OBJC_IVAR_$_LFVolume._dataVolumesChecked
+ _LFBootedToFVUnlock
+ _LFVolumeShouldCacheClassificationFailures
+ _LFVolumeShouldCacheClassificationFailures.cacheFailures
+ _LFVolumeShouldCacheClassificationFailures.onceToken
+ _LFVolumeStartAvailabilityInvalidation.onceToken
+ _OBJC_CLASS_$_NSConstantArray
+ _OUTLINED_FUNCTION_2
+ __LFVolumeDiskAppeared
+ __LFVolumeDiskDescriptionChanged
+ __LFVolumeShouldCacheClassificationFailures
+ ___LFVolumeShouldCacheClassificationFailures_block_invoke
+ ___LFVolumeStartAvailabilityInvalidation_block_invoke
+ ____LFVolumeShouldCacheClassificationFailures_block_invoke
+ ____LFVolumeStartAvailabilityInvalidation_block_invoke
+ ___getDARegisterDiskAppearedCallbackSymbolLoc_block_invoke
+ ___getDARegisterDiskDescriptionChangedCallbackSymbolLoc_block_invoke
+ _gLFVolumeAvailabilityGeneration
+ _gLFVolumeCacheOverrideForTesting
+ _objc_msgSend$_computeDataVolumes
+ _objc_msgSend$_pruneAvailabilityCacheIfStale
+ getDARegisterDiskAppearedCallbackSymbolLoc.ptr
+ getDARegisterDiskDescriptionChangedCallbackSymbolLoc.ptr
- GCC_except_table26
CStrings:
+ "DARegisterDiskAppearedCallback"
+ "DARegisterDiskDescriptionChangedCallback"
+ "DAVolumePath"
+ "com.apple.loginframework.volumeInvalidation"
+ "void *DARegisterDiskAppearedCallbackFunction(DASessionRef, CFDictionaryRef _Nullable, DADiskAppearedCallback, void * _Nullable)"
+ "void *DARegisterDiskDescriptionChangedCallbackFunction(DASessionRef, CFDictionaryRef _Nullable, CFArrayRef _Nullable, DADiskDescriptionChangedCallback, void * _Nullable)"
```
