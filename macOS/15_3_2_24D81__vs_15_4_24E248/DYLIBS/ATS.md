## ATS

> `/System/Library/Frameworks/ApplicationServices.framework/Versions/A/Frameworks/ATS.framework/Versions/A/ATS`

```diff

 580.3.0.1.0
-  __TEXT.__text: 0x6d158
+  __TEXT.__text: 0x6c474
   __TEXT.__auth_stubs: 0x17e0
-  __TEXT.__const: 0x4647
+  __TEXT.__const: 0x46d7
   __TEXT.__cstring: 0x772a
   __TEXT.__ustring: 0xe34
-  __TEXT.__gcc_except_tab: 0xa90
+  __TEXT.__gcc_except_tab: 0xa7c
   __TEXT.__oslogstring: 0x3
   __TEXT.__dlopen_cstrs: 0x2e1
-  __TEXT.__unwind_info: 0x9a8
+  __TEXT.__unwind_info: 0x9c0
   __TEXT.__objc_classname: 0x1
   __TEXT.__objc_methname: 0x3b2
   __TEXT.__objc_stubs: 0x560
-  __DATA_CONST.__got: 0x1d8
+  __DATA_CONST.__got: 0x1d0
   __DATA_CONST.__const: 0x1420
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x158

   __AUTH_CONST.__objc_intobj: 0x18
   __DATA.__data: 0x8f0
   __DATA.__crash_info: 0x40
-  __DATA.__bss: 0xad8
+  __DATA.__bss: 0xae0
   __DATA.__common: 0xda0
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/Versions/A/CoreGraphics

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 76DD6D90-7A86-34AB-8531-568C0158BB47
-  Functions: 1687
-  Symbols:   2715
+  UUID: A68D71A8-592C-3DE6-99FD-764024F360CC
+  Functions: 1801
+  Symbols:   2868
   CStrings:  1777
 
Symbols:
+ ATSAutoActivateFont.cold.1
+ ATSFontValidateDynamic.cold.1
+ ATSLightFontActivateFromFileReference.cold.1
+ ATSLightFontActivateFromMemory.cold.1
+ ATSLightFontDeactivate.cold.1
+ ATSLightFontFamilies.cold.2
+ ATSLightFontFamilyFindFromName.cold.1
+ ATSLightFontFamilyFindFromQuickDrawName.cold.1
+ ATSLightFontFamilyGetGeneration.cold.1
+ ATSLightFontFamilyGetName.cold.1
+ ATSLightFontFamilyGetQuickDrawName.cold.1
+ ATSLightFontFamilyIteratorCreate.cold.1
+ ATSLightFontFamilyIteratorCreate.cold.2
+ ATSLightFontFamilyIteratorNext.cold.1
+ ATSLightFontFamilyIteratorNext.cold.2
+ ATSLightFontFamilyIteratorReset.cold.1
+ ATSLightFontFamilyIteratorReset.cold.2
+ ATSLightFontFindFromContainer.cold.1
+ ATSLightFontFindFromName.cold.1
+ ATSLightFontFindFromPostScriptName.cold.1
+ ATSLightFontGetContainer.cold.1
+ ATSLightFontGetContainerFromFileReference.cold.1
+ ATSLightFontGetFileReference.cold.1
+ ATSLightFontGetGeneration.cold.1
+ ATSLightFontGetName.cold.1
+ ATSLightFontIsEnabled.cold.1
+ ATSLightFontIteratorCreate.cold.1
+ ATSLightFontIteratorCreate.cold.2
+ ATSLightFontIteratorNext.cold.1
+ ATSLightFontIteratorNext.cold.2
+ ATSLightFontIteratorNext.cold.3
+ ATSLightFontIteratorReset.cold.1
+ ATSLightFontIteratorReset.cold.2
+ ATSLightFontNotificationSubscribe.cold.1
+ ATSLightFontNotificationUnsubscribe.cold.1
+ ATSLightFontNotify.cold.1
+ ATSLightFontSetEnabled.cold.1
+ ATSLightGetGeneration.cold.1
+ ApplyMorph.cold.1
+ AssureMappedResourceFork.cold.1
+ CTFontCopyPostScriptName.cold.1
+ CTFontCreateWithFontToken.cold.1
+ CalculateNextFontFamilyIndex.cold.1
+ CreateValidationReport.cold.3
+ CreateValidationReport.cold.4
+ FOFindTableInCache.cold.1
+ FOGetAliasNameDictonaryForIndex.cold.1
+ FOGetCoveredUnicodeChars.cold.1
+ FOLazyInitialize.cold.1
+ GCC_except_table14
+ GCC_except_table20
+ GCC_except_table24
+ GCC_except_table35
+ GCC_except_table37
+ GCC_except_table42
+ GCC_except_table48
+ GCC_except_table53
+ GCC_except_table57
+ GCC_except_table59
+ GCC_except_table63
+ GCC_except_table88
+ GCC_except_table9
+ HighLevelAPITests.cold.1
+ HighLevelAPITestsCT.cold.1
+ HighLevelTest.cold.1
+ HighLevelTest.cold.2
+ PrintFamilyClient.cold.1
+ SendFontManagementMessageWithMessageStatus.cold.1
+ _AllocateDeltaXArray
+ _MergedGlobals.5
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ _RegisterContainerWithDirectoryPath
+ _ZL20AssureMappedDataForkt.cold.1
+ _ZL22FindDoubleNameCallbackiPK8__CFDataPvP23ATSAutoActivateHookInfo.cold.1
+ _ZL23Convert1BitTo8BitPixelsmPKcmPcm.cold.1
+ _ZL23Convert1BitTo8BitPixelsmPKcmPcm.cold.2
+ _ZL23Convert1BitTo8BitPixelsmPKcmPcm.cold.3
+ _ZL28FOGetFamilyInstanceResourcesjtstssPP13FamRecPrivatePmPP7FontRecS2_Ps.cold.1
+ _ZL29GetFontFamilyFromNameCallbackiPK8__CFDataPvP23ATSAutoActivateHookInfo.cold.1
+ _ZL29UpdateStandardFontDirectoriesv.cold.1
+ __MergedGlobals
+ __ZL10defaultBox
+ __ZL13UnionFixedBoxP14FixedRectanglePKS_
+ __ZL16BoxFondATMStrikeP6FamRecmP14FixedRectanglePi
+ __ZL16XUpdateATMStrikeP7FontRecP4Rects
+ __ZL17InverseMapString8PKtmS0_Pj
+ __ZL18InverseMapString10PKtmS0_Pj
+ __ZL20InverseMapString4_32PKtmS0_Pj
+ __ZL20InverseMapString6_32PKtmS0_Pj
+ __ZL9symbolBox
+ __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorIN3OTL8CoverageEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorIPKvEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__19remove_ifB8nn190102IPl14IsDeletedGlyphEET_S3_S3_T0_
+ __ZSt28__throw_bad_array_new_lengthB8nn190102v
- GCC_except_table11
- GCC_except_table16
- GCC_except_table22
- GCC_except_table30
- GCC_except_table36
- GCC_except_table39
- GCC_except_table4
- GCC_except_table45
- GCC_except_table49
- GCC_except_table54
- GCC_except_table58
- GCC_except_table62
- GCC_except_table87
- _ClusterEnumerator
- _ZZ32_eATSFontIsStandardFontDirectoryE11lastRequest.0
- _ZZ32_eATSFontIsStandardFontDirectoryE11lastRequest.1
- __ZGVZ24CTFontCopyPostScriptNameE4func
- __ZGVZ25CTFontCreateWithFontTokenE4func
- __ZGVZL22Expand1BitTo8BitPixelsmPKcPcE14k1BitTo8BitLUT
- __ZL10gKnownDirs
- __ZL10gReplyPort
- __ZL11gClienetPID
- __ZL14gKnownDirItems
- __ZL14gLameFONDCache
- __ZL14gTrackOFACalls
- __ZL15gXTypeFunctions
- __ZL16gTrackOFAHandled
- __ZL17gNotificationLock
- __ZL18gLameFONDCacheLock
- __ZL18gServerIsValidator
- __ZL18gTrackOFACacheHits
- __ZL19atsNotificationList
- __ZL19gTrackOFACacheCalls
- __ZL20gATSServerNameSuffix
- __ZL22gGlyphNamesMappingLock
- __ZL22gTrackOFAIndividualReg
- __ZL23gFontRefToGlyphNamsDict
- __ZL23gGenerationMemoryObject
- __ZL23gTrackOFACacheCacheHits
- __ZL24atsNotificationListCount
- __ZL26gPreprocessedPostTableLock
- __ZL27gTrackOFACacheIndividualReg
- __ZL35gFontRefToPreprocessedPostTableDict
- __ZNSt3__119__allocate_at_leastB8nn180100INS_9allocatorIN3OTL8CoverageEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8nn180100INS_9allocatorIPKvEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__19remove_ifB8nn180100IPl14IsDeletedGlyphEET_S3_S3_T0_
- __ZSt28__throw_bad_array_new_lengthB8nn180100v
- __ZZ17OFAGlyphCacheFindE4gpid
- __ZZ21ValidateDynamicCommonE24triedSoftLinkingCoreText
- __ZZ21ValidateDynamicCommonE30__CTFontManagerIsSupportedFont
- __ZZ24CTFontCopyPostScriptNameE4func
- __ZZ25CTFontCreateWithFontTokenE4func
- __ZZ35_eATSFontGetStandardFontDirectoriesE8doneOnce
- __ZZL17GetCoreTextHandlevE4once
- __ZZL17GetCoreTextHandlevE6handle
- __ZZL20ReconnectToATSServerihhE13gReconnecting
- __ZZL20ReconnectToATSServerihhE20gThread_Reconnecting
- __ZZL22Expand1BitTo8BitPixelsmPKcPcE14k1BitTo8BitLUT
- __ZZL27UnregisterDataFontWithXTypejjE34ctFontManagerUnregisterFontForData
- ___CTFontCopyCharacterSet
- ___CTFontCopyTraits
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ATS/FontObjects/Sources/ATSFontAutoActivate.cc"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ATS/Validation/coresources/validatehighlevel.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ATS/FontObjects/Sources/ATSFontAutoActivate.cc"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ATS/Validation/coresources/validatehighlevel.c"

```
