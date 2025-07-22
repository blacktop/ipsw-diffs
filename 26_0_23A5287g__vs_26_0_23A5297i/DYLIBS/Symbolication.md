## Symbolication

> `/System/Library/PrivateFrameworks/Symbolication.framework/Symbolication`

```diff

-64572.129.1.0.0
-  __TEXT.__text: 0xacffc
-  __TEXT.__auth_stubs: 0x21a0
-  __TEXT.__objc_methlist: 0x6508
-  __TEXT.__const: 0x1c0
-  __TEXT.__cstring: 0xfca3
-  __TEXT.__gcc_except_tab: 0x4f18
-  __TEXT.__oslogstring: 0x1642
+64572.134.1.0.0
+  __TEXT.__text: 0xb0834
+  __TEXT.__auth_stubs: 0x2410
+  __TEXT.__objc_methlist: 0x65c0
+  __TEXT.__const: 0x2b6
+  __TEXT.__cstring: 0xff88
+  __TEXT.__gcc_except_tab: 0x4ebc
+  __TEXT.__oslogstring: 0x17ac
   __TEXT.__ustring: 0x24
-  __TEXT.__unwind_info: 0x2870
+  __TEXT.__swift5_typeref: 0x402
+  __TEXT.__swift5_capture: 0x120
+  __TEXT.__constg_swiftt: 0xc8
+  __TEXT.__swift5_builtin: 0x50
+  __TEXT.__swift5_reflstr: 0x311
+  __TEXT.__swift5_fieldmd: 0x2a8
+  __TEXT.__swift5_types: 0x14
+  __TEXT.__unwind_info: 0x2940
   __TEXT.__objc_classname: 0x83a
-  __TEXT.__objc_methname: 0xf364
-  __TEXT.__objc_methtype: 0x5e0c
-  __TEXT.__objc_stubs: 0x9920
-  __DATA_CONST.__got: 0x428
-  __DATA_CONST.__const: 0x3660
-  __DATA_CONST.__objc_classlist: 0x2c0
+  __TEXT.__objc_methname: 0xf42d
+  __TEXT.__objc_methtype: 0x5e7c
+  __TEXT.__objc_stubs: 0x9a00
+  __DATA_CONST.__got: 0x458
+  __DATA_CONST.__const: 0x35f8
+  __DATA_CONST.__objc_classlist: 0x2d0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3518
+  __DATA_CONST.__objc_selrefs: 0x3560
   __DATA_CONST.__objc_superrefs: 0x200
   __DATA_CONST.__objc_arraydata: 0x870
-  __AUTH_CONST.__auth_got: 0x10e8
-  __AUTH_CONST.__const: 0xb88
-  __AUTH_CONST.__cfstring: 0xd7c0
-  __AUTH_CONST.__objc_const: 0xbb60
+  __AUTH_CONST.__auth_got: 0x1220
+  __AUTH_CONST.__const: 0x11d8
+  __AUTH_CONST.__cfstring: 0xd860
+  __AUTH_CONST.__objc_const: 0xbcd8
   __AUTH_CONST.__objc_arrayobj: 0xf0
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH.__objc_data: 0x3c0
+  __AUTH.__objc_data: 0x4a0
+  __AUTH.__data: 0x50
   __AUTH.__thread_vars: 0x30
   __AUTH.__thread_bss: 0x8
-  __DATA.__objc_ivar: 0xc68
-  __DATA.__data: 0xce8
-  __DATA.__bss: 0x530
+  __DATA.__objc_ivar: 0xc6c
+  __DATA.__data: 0xd58
+  __DATA.__bss: 0x548
   __DATA.__common: 0xf9
   __DATA_DIRTY.__objc_data: 0x17c0
   __DATA_DIRTY.__crash_info: 0x148

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 247499E2-6D40-323F-9ECF-9E298C776590
-  Functions: 3011
-  Symbols:   10367
-  CStrings:  7696
+  - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswiftos.dylib
+  UUID: 2F6D5596-0601-3FED-9FB3-80F939E23DD4
+  Functions: 3119
+  Symbols:   10531
+  CStrings:  7742
 
Symbols:
+ +[VMUVMRegion columnHeadersWithOptions:maximumLength:memorySizeDivisor:hasFractionalPageSizes:].cold.1
+ -[VMUVMRegion descriptionWithOptions:maximumLength:memorySizeDivisor:hasFractionalPageSizes:].cold.2
+ -[VMUVMRegion getVMRegionAttributeStatusData:]
+ -[VMUVMRegion isDyldPrivateMemory]
+ -[VMUVMRegion isJIT]
+ -[VMUVMRegion isTPRO]
+ -[VMUVMRegion setVMRegionAttributeStatusData:]
+ GCC_except_table110
+ GCC_except_table124
+ GCC_except_table132
+ GCC_except_table141
+ GCC_except_table144
+ GCC_except_table150
+ GCC_except_table153
+ OBJC_IVAR_$_VMUVMRegion.is_jit
+ OBJC_IVAR_$_VMUVMRegion.is_tpro
+ _OBJC_CLASS_$_VMUAttributeGraphRegionIdentifier
+ _OBJC_CLASS_$_VMUAttributeGraphTypeIdentifier
+ _OBJC_IVAR_$_VMUObjectIdentifier._attributeGraphTypeIdentifier
+ _OBJC_METACLASS_$_VMUAttributeGraphRegionIdentifier
+ _OBJC_METACLASS_$_VMUAttributeGraphTypeIdentifier
+ _VMUEnumerateMallocBlocksInZone
+ __Block_copy
+ __Block_release
+ __DATA_VMUAttributeGraphRegionIdentifier
+ __DATA_VMUAttributeGraphTypeIdentifier
+ __INSTANCE_METHODS_VMUAttributeGraphRegionIdentifier
+ __INSTANCE_METHODS_VMUAttributeGraphTypeIdentifier
+ __IVARS_VMUAttributeGraphRegionIdentifier
+ __IVARS_VMUAttributeGraphTypeIdentifier
+ __METACLASS_DATA_VMUAttributeGraphRegionIdentifier
+ __METACLASS_DATA_VMUAttributeGraphTypeIdentifier
+ __PROPERTIES_VMUAttributeGraphRegionIdentifier
+ ___block_literal_global.339
+ ___block_literal_global.343
+ ___block_literal_global.363
+ ___block_literal_global.388
+ ___block_literal_global.398
+ ___block_literal_global.443
+ ___block_literal_global.810
+ ___copy_assignment_8_8_pa0_65378_0_pa0_34562_8_pa0_19484_16_pa0_61410_24_pa0_57512_32_pa0_14389_40_pa0_43219_48_pa0_63934_56_pa0_3758_64_pa0_6027_72_pa0_18472_80_pa0_3398_88_pa0_16233_96_pa0_55737_104_pa0_53179_112_pa0_8858_120_t128w4
+ ___maxAttributesWidth_block_invoke
+ ___swift_instantiateConcreteTypeFromMangledName
+ ___swift_memcpy16_8
+ ___swift_memcpy200_8
+ ___swift_memcpy32_8
+ ___swift_memcpy8_8
+ ___swift_noop_void_return
+ ___swift_reflection_version
+ __swiftEmptyArrayStorage
+ __swiftEmptyDictionarySingleton
+ __swiftEmptySetSingleton
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftCoreFoundation_$_Symbolication
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftDispatch_$_Symbolication
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftFoundation_$_Symbolication
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftObjectiveC_$_Symbolication
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swiftXPC_$_Symbolication
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_Builtin_float_$_Symbolication
+ __swift_FORCE_LOAD_$_swiftos
+ __swift_FORCE_LOAD_$_swiftos_$_Symbolication
+ __swift_stdlib_reportUnimplementedInitializer
+ _block_copy_helper
+ _block_copy_helper.11
+ _block_copy_helper.14
+ _block_copy_helper.20
+ _block_copy_helper.23
+ _block_descriptor
+ _block_descriptor.13
+ _block_descriptor.16
+ _block_descriptor.22
+ _block_descriptor.25
+ _block_destroy_helper
+ _block_destroy_helper.12
+ _block_destroy_helper.15
+ _block_destroy_helper.21
+ _block_destroy_helper.24
+ _kVMUVMRegionCurrentClassVersion_block_invoke.allPossibleAttributesWidth
+ _maxAttributesWidth.maxAttributesWidthVar
+ _maxAttributesWidth.onceToken
+ _objc_allocWithZone
+ _objc_msgSend$attributeGraphVMRegionBaseAddress
+ _objc_msgSend$classInfoForAttributeGraphValueWithMetadata:
+ _objc_msgSend$getVMRegionAttributeStatusData:
+ _objc_msgSend$initWithTask:identifyOldRegions:
+ _objc_msgSend$isDyldPrivateMemory
+ _objc_msgSend$metadataPointerForAllocation:
+ _objc_msgSend$regionIsOldAttributeGraphVMRegionMapping:
+ _objc_msgSend$setVMRegionAttributeStatusData:
+ _swift_allocObject
+ _swift_beginAccess
+ _swift_bridgeObjectRelease
+ _swift_bridgeObjectRetain
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_initWithCopy
+ _swift_cvw_initializeBufferWithCopyOfBuffer
+ _swift_deallocObject
+ _swift_deallocPartialClassInstance
+ _swift_endAccess
+ _swift_getForeignTypeMetadata
+ _swift_getObjCClassFromMetadata
+ _swift_getObjCClassMetadata
+ _swift_getTypeByMangledNameInContext2
+ _swift_isUniquelyReferenced_nonNull_native
+ _swift_release
+ _swift_retain
+ _swift_slowAlloc
+ _swift_slowDealloc
+ _swift_unknownObjectUnownedDestroy
+ _swift_unknownObjectUnownedInit
+ _swift_unknownObjectUnownedLoadStrong
+ _symbolic SDy_____AAG s6UInt64V
+ _symbolic SDy_____AAGz_Xx s6UInt64V
+ _symbolic SPy_____GSg s4Int8V
+ _symbolic SS
+ _symbolic Sb
+ _symbolic Sbz_Xx
+ _symbolic Shy_____G s6UInt64V
+ _symbolic Shy_____Gz_Xx s6UInt64V
+ _symbolic Si
+ _symbolic SiSpy_____GSg_SVSgtXCSg So14_malloc_zone_tV
+ _symbolic SiSpy_____GSg_SitXCSg So14_malloc_zone_tV
+ _symbolic So12VMUClassInfoC
+ _symbolic So31VMUAttributeGraphTypeIdentifierC
+ _symbolic So7VMUTaskC
+ _symbolic Spy_____GSVIetCyd_ So14_malloc_zone_tV
+ _symbolic Spy_____GSg So22malloc_introspection_tV
+ _symbolic Su
+ _symbolic SvSg
+ _symbolic SvSgSpy_____GSg_AASi_____tXCSg So14_malloc_zone_tV s6UInt64V
+ _symbolic SvSgSpy_____GSg_AASitXCSg So14_malloc_zone_tV
+ _symbolic SvSgSpy_____GSg_S2i_____AEtXCSg So14_malloc_zone_tV s6UInt64V
+ _symbolic SvSgSpy_____GSg_S2i_____tXCSg So14_malloc_zone_tV s6UInt64V
+ _symbolic SvSgSpy_____GSg_S2itXCSg So14_malloc_zone_tV
+ _symbolic SvSgSpy_____GSg_Si_____tXCSg So14_malloc_zone_tV s6UInt64V
+ _symbolic SvSgSpy_____GSg_SitXCSg So14_malloc_zone_tV
+ _symbolic _____ 2os6LoggerV
+ _symbolic _____ So10vm_range_ta
+ _symbolic _____ So14_malloc_zone_tV
+ _symbolic _____ So19malloc_statistics_tV
+ _symbolic _____ So22malloc_introspection_tV
+ _symbolic _____ So31VMUAttributeGraphTypeIdentifierC13SymbolicationE15CachedClassInfo33_2BBC42CB446F339ECD05FF6CA4EE6EEALLO
+ _symbolic _____ s5Int32V
+ _symbolic _____ s6UInt32V
+ _symbolic _____ s6UInt64V
+ _symbolic _____Spy_____GSgAAIgyyy_ s6UInt32V So10vm_range_ta
+ _symbolic _____Spy_____GSgXCSg s5Int32V So14_malloc_zone_tV
+ _symbolic _____Spy_____GSg_SiSpySvSgGSgAAtXCSg s6UInt32V So14_malloc_zone_tV
+ _symbolic _____Spy_____GSg_SvSgtXCSg s5Int32V So14_malloc_zone_tV
+ _symbolic ___________SvSgABSuAaB_S2uSpyACGSgtXCSgyAB_AcBSpy_____GSgABtXCSgtXCSg s5Int32V s6UInt32V So10vm_range_ta
+ _symbolic _____y_____ABG s18_DictionaryStorageC s6UInt64V
+ _symbolic _____y_____G s11_SetStorageC s6UInt64V
+ _symbolic _____y__________G s18_DictionaryStorageC s6UInt64V So31VMUAttributeGraphTypeIdentifierC13SymbolicationE15CachedClassInfo33_2BBC42CB446F339ECD05FF6CA4EE6EEALLO
+ _symbolic _____z_Xx s5Int32V
+ _symbolic ySpy_____GSgXCSg So14_malloc_zone_tV
+ _symbolic ySpy_____GSg_SpySvSgGSg_____tXCSg So14_malloc_zone_tV s6UInt32V
+ _symbolic ySpy_____GSg_Spy_____GSgtXCSg So14_malloc_zone_tV So0A13_statistics_tV
+ _symbolic ySpy_____GSg_SvSgSitXCSg So14_malloc_zone_tV
+ _symbolic ySpy_____GSg_SvSgtXCSg So14_malloc_zone_tV
+ _symbolic ySpy_____GSg______tXCSg So14_malloc_zone_tV s5Int32V
+ _symbolic ySpy_____GSg_ySvSg_ADtcSgtXCSg So14_malloc_zone_tV
+ _symbolic y______AASu_____AA_S2uSpySvSgGSgtXCSg_____SgtXCSg s6UInt32V s5Int32V s13OpaquePointerV
+ _symbolic y______Su_____AA_S2uSpySvSgGSgtXCSgSpy_____GSgtXCSg s6UInt32V s5Int32V So19malloc_statistics_tV
+ _type_layout_string So10vm_range_ta
+ _type_layout_string So14_malloc_zone_tV
+ _type_layout_string So19malloc_statistics_tV
+ _type_layout_string So31VMUAttributeGraphTypeIdentifierC13SymbolicationE15CachedClassInfo33_2BBC42CB446F339ECD05FF6CA4EE6EEALLO
+ _vmuEnumerateMallocBlocksInZoneRecorderAdapter
- -[VMUObjectIdentifier locateSwiftValuesInAttributeGraph]
- GCC_except_table136
- GCC_except_table145
- GCC_except_table148
- GCC_except_table154
- GCC_except_table79
- _OBJC_IVAR_$_VMUObjectIdentifier._attributeGraphSwiftMetadataToClassInfo
- _OBJC_IVAR_$_VMUObjectIdentifier._swiftValueInAttributeGraphAddressesToTypeMetadata
- ___56-[VMUObjectIdentifier locateSwiftValuesInAttributeGraph]_block_invoke
- ___56-[VMUObjectIdentifier locateSwiftValuesInAttributeGraph]_block_invoke_2
- ___block_descriptor_48_e8_32s40s_e82_i32?0Q8^{malloc_introspection_t=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?I}16"NSString"24ls32l8s40l8
- ___block_descriptor_48_e8_32s_e82_i32?0Q8^{malloc_introspection_t=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?I}16"NSString"24ls32l8
- ___block_descriptor_80_e8_32s40s48s56r_e9_v16?0^?8lr56l8s32l8s40l8s48l8
- ___block_descriptor_88_e8_32s40s48s56r_e9_v16?0^?8ls32l8r56l8s40l8s48l8
- ___block_literal_global.119
- ___block_literal_global.346
- ___block_literal_global.350
- ___block_literal_global.370
- ___block_literal_global.394
- ___block_literal_global.404
- ___block_literal_global.449
- ___block_literal_global.818
- ___markOthers_block_invoke
- ___markOthers_block_invoke_2
- __pointerRecorderBlockContextAdapter
- _attributeGraphVMRegionsStartRecorder
- _objc_msgSend$locateSwiftValuesInAttributeGraph
- _zoneEnumeratorBlockAdapter
- _zoneEnumeratorRangeRecorder
CStrings:
+ "  ATTRIBUTES"
+ " %@ %@  "
+ " %@PURGE=%c"
+ " ATTRIBUTES "
+ "%-*s %*s-%-*s [%@] %s/%s %s%-*s%s  %s"
+ "%-*s %@-%@ [%@] %s/%s SM=%s%@%@  %@"
+ "@\"VMUAttributeGraphTypeIdentifier\""
+ "@48@0:8^{_VMUVMRegionData=QQIiiIIIIIiICCCIIb1b1b1b1b1b1b1b25QQQQQQQ}16q24@32^@40"
+ "JIT"
+ "Symbolication_Internal.VMUAttributeGraphRegionIdentifier"
+ "Symbolication_Internal.VMUAttributeGraphTypeIdentifier"
+ "TPRO"
+ "TQ,N,R,VattributeGraphVMRegionBaseAddress"
+ "VMUAttributeGraphRegionIdentifier"
+ "VMUAttributeGraphRegionIdentifier.init() - failed to enumerate AttributeGraph malloc zone with the error %d"
+ "VMUAttributeGraphRegionIdentifier.init() failed - symbol _AGGraphVMRegionBaseAddress exists but is smaller than expected"
+ "VMUAttributeGraphRegionIdentifier.init() failed to read _AGGraphVMRegionBaseAddress with the error %d"
+ "VMUAttributeGraphTypeIdentifier"
+ "[Region Attributes Data] Count: %u\n\n"
+ "_attributeGraphTypeIdentifier"
+ "attributeGraphSwiftMetadataToClassInfo"
+ "attributeGraphVMRegionBaseAddress"
+ "b25"
+ "classInfoForAttributeGraphValueWithMetadata:"
+ "getVMRegionAttributeStatusData:"
+ "i48@0:8^Q16^Q24^I32^{vm_region_submap_info_64_with_extra_flag=iiIQIIIIIISCCiiISSIQ}40"
+ "init()"
+ "initWithTask:identifyOldRegions:"
+ "isDyldPrivateMemory"
+ "isJIT"
+ "isTPRO"
+ "is_jit"
+ "is_tpro"
+ "metadataPointerForAllocation:"
+ "oldAttributeGraphVMRegionBaseAddresses"
+ "regionAttributesData"
+ "regionIsOldAttributeGraphVMRegionMapping:"
+ "setVMRegionAttributeStatusData:"
+ "swiftValueInAttributeGraphAddressesToTypeMetadata"
+ "v24@0:8^{_VMUVMRegionAttributeStatusData=b1b1b14}16"
+ "v32@0:8^{_VMUVMRegionData=QQIiiIIIIIiICCCIIb1b1b1b1b1b1b1b25QQQQQQQ}16@24"
- " PURGE=%c"
- "%-*s %*s-%-*s [%@] %s/%s %s%s  %s"
- "%-*s %@-%@ [%@] %s/%s SM=%s%@  %@"
- "@48@0:8^{_VMUVMRegionData=QQIiiIIIIIiICCCIIb1b1b1b1b1b27QQQQQQQ}16q24@32^@40"
- "_attributeGraphSwiftMetadataToClassInfo"
- "_swiftValueInAttributeGraphAddressesToTypeMetadata"
- "b27"
- "i48@0:8^Q16^Q24^I32^{vm_region_submap_info_64=iiIQIIIIIISCCiiISIQ}40"
- "locateSwiftValuesInAttributeGraph"
- "v32@0:8^{_VMUVMRegionData=QQIiiIIIIIiICCCIIb1b1b1b1b1b27QQQQQQQ}16@24"

```
