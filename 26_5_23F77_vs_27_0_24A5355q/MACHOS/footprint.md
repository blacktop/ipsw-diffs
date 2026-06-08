## footprint

> `/usr/bin/footprint`

```diff

-314.120.5.0.0
-  __TEXT.__text: 0x1c2b0
+356.0.0.0.0
+  __TEXT.__text: 0x1fc30
   __TEXT.__auth_stubs: 0xc40
-  __TEXT.__objc_stubs: 0x2380
-  __TEXT.__objc_methlist: 0x11b4
-  __TEXT.__const: 0x200
-  __TEXT.__cstring: 0x353e
-  __TEXT.__objc_methname: 0x23db
-  __TEXT.__objc_classname: 0x206
-  __TEXT.__objc_methtype: 0x7d2
-  __TEXT.__gcc_except_tab: 0x3d0
+  __TEXT.__objc_stubs: 0x2420
+  __TEXT.__objc_methlist: 0x124c
+  __TEXT.__const: 0x230
+  __TEXT.__cstring: 0x311b
+  __TEXT.__objc_methname: 0x24fe
+  __TEXT.__objc_classname: 0x1db
+  __TEXT.__objc_methtype: 0x7f9
+  __TEXT.__gcc_except_tab: 0x444
   __TEXT.__ustring: 0xd0
   __TEXT.__oslogstring: 0x21
-  __TEXT.__unwind_info: 0x4f8
-  __DATA_CONST.__auth_got: 0x630
-  __DATA_CONST.__got: 0x218
-  __DATA_CONST.__const: 0x17f0
-  __DATA_CONST.__cfstring: 0x22c0
+  __TEXT.__unwind_info: 0x498
+  __DATA_CONST.__const: 0xf10
+  __DATA_CONST.__cfstring: 0x1a00
   __DATA_CONST.__objc_classlist: 0xc0
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x30

   __DATA_CONST.__objc_arraydata: 0x28
   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x2f40
-  __DATA.__objc_selrefs: 0xa08
-  __DATA.__objc_ivar: 0x29c
+  __DATA_CONST.__auth_got: 0x630
+  __DATA_CONST.__got: 0x210
+  __DATA_CONST.__auth_ptr: 0x8
+  __DATA.__objc_const: 0x30b0
+  __DATA.__objc_selrefs: 0xa38
+  __DATA.__objc_ivar: 0x2b8
   __DATA.__objc_data: 0x780
   __DATA.__data: 0x250
   __DATA.__bss: 0x4140

   - /System/Library/PrivateFrameworks/Symbolication.framework/Symbolication
   - /System/Library/PrivateFrameworks/perfdata.framework/perfdata
   - /usr/lib/libSystem.B.dylib
+  - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  UUID: 8E155F8E-26FA-3AA8-9EB9-12828606BFAB
-  Functions: 420
-  Symbols:   3485
-  CStrings:  1467
+  UUID: 1FB9E880-571C-3241-A3F2-81B4896C3702
+  Functions: 435
+  Symbols:   3564
+  CStrings:  1358
 
Symbols:
+ +[FPKernelProcess _nameForWiredInfo:withSymbolicator:zoneNames:zoneCount:]
+ -[FPFootprint _kernelProcess]
+ -[FPFootprint _shouldEnableWireTagSharing]
+ -[FPKernelProcess addMemoryRegion:]
+ -[FPKernelProcess memoryRegions]
+ -[FPKernelProcess removeMemoryRegion:]
+ -[FPKernelProcess setMemoryRegions:]
+ -[FPMemoryMultiRegion copyWithZone:]
+ -[FPMemoryObject _fakeRegion]
+ -[FPMemoryObject _finalizeWithTotal:useRegionDirtySize:skipProcessViewCulling:]
+ -[FPMemoryObject finalizeObjectWithKernelRegion:]
+ -[FPMemoryObject object_id]
+ -[FPMemoryObject wireTag]
+ -[FPMemoryRegion eligibleForProcessView]
+ -[FPMemoryRegion object_id]
+ -[FPMemoryRegion setObject_id:]
+ -[FPMemoryRegion setWireTag:]
+ -[FPMemoryRegion setWiredSize:]
+ -[FPMemoryRegion wireTag]
+ -[FPOutputFormatterText _cstringForFormattedSize:buffer:capacity:]
+ -[FPRangeList distributeKernelRegionBudget:useDirtyCap:]
+ -[FPSharedCache initWithUUID:baseAddress:mappedSize:]
+ .str.217
+ .str.218
+ /Library/Caches/com.apple.xbs/699FBE81-E295-4917-988E-AE7C50022A43/TemporaryDirectory.QqQ1Ua/Binaries/footprint_darwinOS/install/TempContent/Objects/footprint.build/footprint.build/Objects-normal/arm64e/footprint_lto.o/0.arm64e.thinlto.o
+ /Library/Caches/com.apple.xbs/699FBE81-E295-4917-988E-AE7C50022A43/TemporaryDirectory.QqQ1Ua/Binaries/footprint_darwinOS/install/TempContent/Objects/footprint.build/footprint.build/Objects-normal/arm64e/footprint_lto.o/1.arm64e.thinlto.o
+ /Library/Caches/com.apple.xbs/699FBE81-E295-4917-988E-AE7C50022A43/TemporaryDirectory.QqQ1Ua/Binaries/footprint_darwinOS/install/TempContent/Objects/footprint.build/footprint.build/Objects-normal/arm64e/footprint_lto.o/10.arm64e.thinlto.o
+ /Library/Caches/com.apple.xbs/699FBE81-E295-4917-988E-AE7C50022A43/TemporaryDirectory.QqQ1Ua/Binaries/footprint_darwinOS/install/TempContent/Objects/footprint.build/footprint.build/Objects-normal/arm64e/footprint_lto.o/11.arm64e.thinlto.o
+ /Library/Caches/com.apple.xbs/699FBE81-E295-4917-988E-AE7C50022A43/TemporaryDirectory.QqQ1Ua/Binaries/footprint_darwinOS/install/TempContent/Objects/footprint.build/footprint.build/Objects-normal/arm64e/footprint_lto.o/12.arm64e.thinlto.o
+ /Library/Caches/com.apple.xbs/699FBE81-E295-4917-988E-AE7C50022A43/TemporaryDirectory.QqQ1Ua/Binaries/footprint_darwinOS/install/TempContent/Objects/footprint.build/footprint.build/Objects-normal/arm64e/footprint_lto.o/13.arm64e.thinlto.o
+ /Library/Caches/com.apple.xbs/699FBE81-E295-4917-988E-AE7C50022A43/TemporaryDirectory.QqQ1Ua/Binaries/footprint_darwinOS/install/TempContent/Objects/footprint.build/footprint.build/Objects-normal/arm64e/footprint_lto.o/14.arm64e.thinlto.o
+ /Library/Caches/com.apple.xbs/699FBE81-E295-4917-988E-AE7C50022A43/TemporaryDirectory.QqQ1Ua/Binaries/footprint_darwinOS/install/TempContent/Objects/footprint.build/footprint.build/Objects-normal/arm64e/footprint_lto.o/15.arm64e.thinlto.o
+ /Library/Caches/com.apple.xbs/699FBE81-E295-4917-988E-AE7C50022A43/TemporaryDirectory.QqQ1Ua/Binaries/footprint_darwinOS/install/TempContent/Objects/footprint.build/footprint.build/Objects-normal/arm64e/footprint_lto.o/16.arm64e.thinlto.o
+ /Library/Caches/com.apple.xbs/699FBE81-E295-4917-988E-AE7C50022A43/TemporaryDirectory.QqQ1Ua/Binaries/footprint_darwinOS/install/TempContent/Objects/footprint.build/footprint.build/Objects-normal/arm64e/footprint_lto.o/17.arm64e.thinlto.o
+ /Library/Caches/com.apple.xbs/699FBE81-E295-4917-988E-AE7C50022A43/TemporaryDirectory.QqQ1Ua/Binaries/footprint_darwinOS/install/TempContent/Objects/footprint.build/footprint.build/Objects-normal/arm64e/footprint_lto.o/18.arm64e.thinlto.o
+ /Library/Caches/com.apple.xbs/699FBE81-E295-4917-988E-AE7C50022A43/TemporaryDirectory.QqQ1Ua/Binaries/footprint_darwinOS/install/TempContent/Objects/footprint.build/footprint.build/Objects-normal/arm64e/footprint_lto.o/19.arm64e.thinlto.o
+ /Library/Caches/com.apple.xbs/699FBE81-E295-4917-988E-AE7C50022A43/TemporaryDirectory.QqQ1Ua/Binaries/footprint_darwinOS/install/TempContent/Objects/footprint.build/footprint.build/Objects-normal/arm64e/footprint_lto.o/2.arm64e.thinlto.o
+ /Library/Caches/com.apple.xbs/699FBE81-E295-4917-988E-AE7C50022A43/TemporaryDirectory.QqQ1Ua/Binaries/footprint_darwinOS/install/TempContent/Objects/footprint.build/footprint.build/Objects-normal/arm64e/footprint_lto.o/20.arm64e.thinlto.o
+ /Library/Caches/com.apple.xbs/699FBE81-E295-4917-988E-AE7C50022A43/TemporaryDirectory.QqQ1Ua/Binaries/footprint_darwinOS/install/TempContent/Objects/footprint.build/footprint.build/Objects-normal/arm64e/footprint_lto.o/21.arm64e.thinlto.o
+ /Library/Caches/com.apple.xbs/699FBE81-E295-4917-988E-AE7C50022A43/TemporaryDirectory.QqQ1Ua/Binaries/footprint_darwinOS/install/TempContent/Objects/footprint.build/footprint.build/Objects-normal/arm64e/footprint_lto.o/22.arm64e.thinlto.o
+ /Library/Caches/com.apple.xbs/699FBE81-E295-4917-988E-AE7C50022A43/TemporaryDirectory.QqQ1Ua/Binaries/footprint_darwinOS/install/TempContent/Objects/footprint.build/footprint.build/Objects-normal/arm64e/footprint_lto.o/23.arm64e.thinlto.o
+ /Library/Caches/com.apple.xbs/699FBE81-E295-4917-988E-AE7C50022A43/TemporaryDirectory.QqQ1Ua/Binaries/footprint_darwinOS/install/TempContent/Objects/footprint.build/footprint.build/Objects-normal/arm64e/footprint_lto.o/24.arm64e.thinlto.o
+ /Library/Caches/com.apple.xbs/699FBE81-E295-4917-988E-AE7C50022A43/TemporaryDirectory.QqQ1Ua/Binaries/footprint_darwinOS/install/TempContent/Objects/footprint.build/footprint.build/Objects-normal/arm64e/footprint_lto.o/25.arm64e.thinlto.o
+ /Library/Caches/com.apple.xbs/699FBE81-E295-4917-988E-AE7C50022A43/TemporaryDirectory.QqQ1Ua/Binaries/footprint_darwinOS/install/TempContent/Objects/footprint.build/footprint.build/Objects-normal/arm64e/footprint_lto.o/26.arm64e.thinlto.o
+ /Library/Caches/com.apple.xbs/699FBE81-E295-4917-988E-AE7C50022A43/TemporaryDirectory.QqQ1Ua/Binaries/footprint_darwinOS/install/TempContent/Objects/footprint.build/footprint.build/Objects-normal/arm64e/footprint_lto.o/3.arm64e.thinlto.o
+ /Library/Caches/com.apple.xbs/699FBE81-E295-4917-988E-AE7C50022A43/TemporaryDirectory.QqQ1Ua/Binaries/footprint_darwinOS/install/TempContent/Objects/footprint.build/footprint.build/Objects-normal/arm64e/footprint_lto.o/4.arm64e.thinlto.o
+ /Library/Caches/com.apple.xbs/699FBE81-E295-4917-988E-AE7C50022A43/TemporaryDirectory.QqQ1Ua/Binaries/footprint_darwinOS/install/TempContent/Objects/footprint.build/footprint.build/Objects-normal/arm64e/footprint_lto.o/5.arm64e.thinlto.o
+ /Library/Caches/com.apple.xbs/699FBE81-E295-4917-988E-AE7C50022A43/TemporaryDirectory.QqQ1Ua/Binaries/footprint_darwinOS/install/TempContent/Objects/footprint.build/footprint.build/Objects-normal/arm64e/footprint_lto.o/6.arm64e.thinlto.o
+ /Library/Caches/com.apple.xbs/699FBE81-E295-4917-988E-AE7C50022A43/TemporaryDirectory.QqQ1Ua/Binaries/footprint_darwinOS/install/TempContent/Objects/footprint.build/footprint.build/Objects-normal/arm64e/footprint_lto.o/7.arm64e.thinlto.o
+ /Library/Caches/com.apple.xbs/699FBE81-E295-4917-988E-AE7C50022A43/TemporaryDirectory.QqQ1Ua/Binaries/footprint_darwinOS/install/TempContent/Objects/footprint.build/footprint.build/Objects-normal/arm64e/footprint_lto.o/8.arm64e.thinlto.o
+ /Library/Caches/com.apple.xbs/699FBE81-E295-4917-988E-AE7C50022A43/TemporaryDirectory.QqQ1Ua/Sources/footprint_darwinOS/footprint/
+ /Library/Caches/com.apple.xbs/699FBE81-E295-4917-988E-AE7C50022A43/TemporaryDirectory.QqQ1Ua/Sources/footprint_darwinOS/footprint/Import Hacks/
+ /Library/Caches/com.apple.xbs/699FBE81-E295-4917-988E-AE7C50022A43/TemporaryDirectory.QqQ1Ua/Sources/footprint_darwinOS/shared/
+ GCC_except_table30
+ OBJC_IVAR_$_FPFootprint._kernelWireTagToRegion
+ OBJC_IVAR_$_FPFootprint._wireTagUniqueObjects
+ OBJC_IVAR_$_FPFootprintArgs._noReusedAsClean
+ OBJC_IVAR_$_FPMemoryRegion._fake
+ OBJC_IVAR_$_FPMemoryRegion._ledgerTag
+ OBJC_IVAR_$_FPMemoryRegion._reserved
+ OBJC_IVAR_$_FPMemoryRegion._reserved2
+ OBJC_IVAR_$_FPMemoryRegion._wireTag
+ OBJC_IVAR_$_FPMemoryRegion._wiredSize
+ StructFieldDetection.cpp
+ _CFStringGetCStringPtr
+ _OBJC_$_PROP_LIST_FPMemoryObject.140
+ __Block_byref_object_copy_.188
+ __Block_byref_object_dispose_.189
+ __OBJC_$_PROP_LIST_FPKernelProcess
+ ___75-[FPFootprint _generateProcessToProcessGroupsWithSharedCacheProcessGroups:]_block_invoke_2
+ ___block_descriptor_102_e8_32s40s48s56s64r72r_e96_B56?0Q8Q16^{vm_region_submap_info_64=iiIQIIIIIISCCiiISSIQISS}24i32"NSString"36"NSString"44B52ls32l8s40l8s48l8r64l8s56l8r72l8
+ ___block_descriptor_112_e8_32s40s48s56r64r72r80r88r96r_e5_v8?0ls32l8r56l8r64l8r72l8r80l8s40l8r88l8r96l8s48l8
+ ___block_descriptor_40_e8_32s_e12_B24?0Q8^v16ls32l8
+ ___block_descriptor_56_e8_32s40r_e8_v16?0Q8ls32l8r40l8
+ ___block_descriptor_56_e8_32s40s_e12_B24?0Q8^v16ls32l8s40l8
+ ___block_descriptor_73_e8_32s40s48s56s_e12_v24?0^8Q16ls32l8s40l8s48l8s56l8
+ ___block_descriptor_83_e8_32s40s48r_e18_v40?0^i8Q16Q24Q32ls32l8r48l8s40l8
+ ___block_descriptor_88_e8_32s40r48r56r64r_e18_v40?0^i8Q16Q24Q32lr40l8r48l8r56l8r64l8s32l8
+ ___chkstk_darwin
+ __block_literal_global.106
+ __block_literal_global.111
+ __block_literal_global.189
+ __block_literal_global.420
+ _fp_get_vm_object_query_wire_tag
+ _kFPHasVmObjectQueryWireTag
+ _mach_vm_tag_describe
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$initWithBytesNoCopy:length:encoding:freeWhenDone:
+ _objc_msgSend$lengthOfBytesUsingEncoding:
+ _objc_msgSend$maximumLengthOfBytesUsingEncoding:
+ _objc_msgSend$numberWithUnsignedShort:
+ _objc_msgSend$object_id
+ _objc_msgSend$setObject_id:
+ _objc_msgSend$setWireTag:
+ _objc_msgSend$setWiredSize:
+ _objc_msgSend$wireTag
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x5
+ _strnlen
- +[FPKernelProcess _nameForWiredInfo:withKexts:andSymbolicator:zoneNames:zoneCount:]
- -[FPMemoryCategory fullName]
- -[FPOutputFormatterText formattedStringForSize:]
- -[FPSharedCache initWithUUID:baseAddress:mappedSize:slide:]
- .str.244
- .str.245
- /Library/Caches/com.apple.xbs/F94AC8B9-7249-413E-8DE4-6D2569D8B087/TemporaryDirectory.lZt1yM/Binaries/footprint_darwinOS/install/TempContent/Objects/footprint.build/footprint.build/Objects-normal/arm64e/footprint_lto.o/0.arm64e.thinlto.o
- /Library/Caches/com.apple.xbs/F94AC8B9-7249-413E-8DE4-6D2569D8B087/TemporaryDirectory.lZt1yM/Binaries/footprint_darwinOS/install/TempContent/Objects/footprint.build/footprint.build/Objects-normal/arm64e/footprint_lto.o/1.arm64e.thinlto.o
- /Library/Caches/com.apple.xbs/F94AC8B9-7249-413E-8DE4-6D2569D8B087/TemporaryDirectory.lZt1yM/Binaries/footprint_darwinOS/install/TempContent/Objects/footprint.build/footprint.build/Objects-normal/arm64e/footprint_lto.o/10.arm64e.thinlto.o
- /Library/Caches/com.apple.xbs/F94AC8B9-7249-413E-8DE4-6D2569D8B087/TemporaryDirectory.lZt1yM/Binaries/footprint_darwinOS/install/TempContent/Objects/footprint.build/footprint.build/Objects-normal/arm64e/footprint_lto.o/11.arm64e.thinlto.o
- /Library/Caches/com.apple.xbs/F94AC8B9-7249-413E-8DE4-6D2569D8B087/TemporaryDirectory.lZt1yM/Binaries/footprint_darwinOS/install/TempContent/Objects/footprint.build/footprint.build/Objects-normal/arm64e/footprint_lto.o/12.arm64e.thinlto.o
- /Library/Caches/com.apple.xbs/F94AC8B9-7249-413E-8DE4-6D2569D8B087/TemporaryDirectory.lZt1yM/Binaries/footprint_darwinOS/install/TempContent/Objects/footprint.build/footprint.build/Objects-normal/arm64e/footprint_lto.o/13.arm64e.thinlto.o
- /Library/Caches/com.apple.xbs/F94AC8B9-7249-413E-8DE4-6D2569D8B087/TemporaryDirectory.lZt1yM/Binaries/footprint_darwinOS/install/TempContent/Objects/footprint.build/footprint.build/Objects-normal/arm64e/footprint_lto.o/14.arm64e.thinlto.o
- /Library/Caches/com.apple.xbs/F94AC8B9-7249-413E-8DE4-6D2569D8B087/TemporaryDirectory.lZt1yM/Binaries/footprint_darwinOS/install/TempContent/Objects/footprint.build/footprint.build/Objects-normal/arm64e/footprint_lto.o/15.arm64e.thinlto.o
- /Library/Caches/com.apple.xbs/F94AC8B9-7249-413E-8DE4-6D2569D8B087/TemporaryDirectory.lZt1yM/Binaries/footprint_darwinOS/install/TempContent/Objects/footprint.build/footprint.build/Objects-normal/arm64e/footprint_lto.o/16.arm64e.thinlto.o
- /Library/Caches/com.apple.xbs/F94AC8B9-7249-413E-8DE4-6D2569D8B087/TemporaryDirectory.lZt1yM/Binaries/footprint_darwinOS/install/TempContent/Objects/footprint.build/footprint.build/Objects-normal/arm64e/footprint_lto.o/17.arm64e.thinlto.o
- /Library/Caches/com.apple.xbs/F94AC8B9-7249-413E-8DE4-6D2569D8B087/TemporaryDirectory.lZt1yM/Binaries/footprint_darwinOS/install/TempContent/Objects/footprint.build/footprint.build/Objects-normal/arm64e/footprint_lto.o/18.arm64e.thinlto.o
- /Library/Caches/com.apple.xbs/F94AC8B9-7249-413E-8DE4-6D2569D8B087/TemporaryDirectory.lZt1yM/Binaries/footprint_darwinOS/install/TempContent/Objects/footprint.build/footprint.build/Objects-normal/arm64e/footprint_lto.o/19.arm64e.thinlto.o
- /Library/Caches/com.apple.xbs/F94AC8B9-7249-413E-8DE4-6D2569D8B087/TemporaryDirectory.lZt1yM/Binaries/footprint_darwinOS/install/TempContent/Objects/footprint.build/footprint.build/Objects-normal/arm64e/footprint_lto.o/2.arm64e.thinlto.o
- /Library/Caches/com.apple.xbs/F94AC8B9-7249-413E-8DE4-6D2569D8B087/TemporaryDirectory.lZt1yM/Binaries/footprint_darwinOS/install/TempContent/Objects/footprint.build/footprint.build/Objects-normal/arm64e/footprint_lto.o/20.arm64e.thinlto.o
- /Library/Caches/com.apple.xbs/F94AC8B9-7249-413E-8DE4-6D2569D8B087/TemporaryDirectory.lZt1yM/Binaries/footprint_darwinOS/install/TempContent/Objects/footprint.build/footprint.build/Objects-normal/arm64e/footprint_lto.o/21.arm64e.thinlto.o
- /Library/Caches/com.apple.xbs/F94AC8B9-7249-413E-8DE4-6D2569D8B087/TemporaryDirectory.lZt1yM/Binaries/footprint_darwinOS/install/TempContent/Objects/footprint.build/footprint.build/Objects-normal/arm64e/footprint_lto.o/22.arm64e.thinlto.o
- /Library/Caches/com.apple.xbs/F94AC8B9-7249-413E-8DE4-6D2569D8B087/TemporaryDirectory.lZt1yM/Binaries/footprint_darwinOS/install/TempContent/Objects/footprint.build/footprint.build/Objects-normal/arm64e/footprint_lto.o/23.arm64e.thinlto.o
- /Library/Caches/com.apple.xbs/F94AC8B9-7249-413E-8DE4-6D2569D8B087/TemporaryDirectory.lZt1yM/Binaries/footprint_darwinOS/install/TempContent/Objects/footprint.build/footprint.build/Objects-normal/arm64e/footprint_lto.o/24.arm64e.thinlto.o
- /Library/Caches/com.apple.xbs/F94AC8B9-7249-413E-8DE4-6D2569D8B087/TemporaryDirectory.lZt1yM/Binaries/footprint_darwinOS/install/TempContent/Objects/footprint.build/footprint.build/Objects-normal/arm64e/footprint_lto.o/25.arm64e.thinlto.o
- /Library/Caches/com.apple.xbs/F94AC8B9-7249-413E-8DE4-6D2569D8B087/TemporaryDirectory.lZt1yM/Binaries/footprint_darwinOS/install/TempContent/Objects/footprint.build/footprint.build/Objects-normal/arm64e/footprint_lto.o/3.arm64e.thinlto.o
- /Library/Caches/com.apple.xbs/F94AC8B9-7249-413E-8DE4-6D2569D8B087/TemporaryDirectory.lZt1yM/Binaries/footprint_darwinOS/install/TempContent/Objects/footprint.build/footprint.build/Objects-normal/arm64e/footprint_lto.o/4.arm64e.thinlto.o
- /Library/Caches/com.apple.xbs/F94AC8B9-7249-413E-8DE4-6D2569D8B087/TemporaryDirectory.lZt1yM/Binaries/footprint_darwinOS/install/TempContent/Objects/footprint.build/footprint.build/Objects-normal/arm64e/footprint_lto.o/5.arm64e.thinlto.o
- /Library/Caches/com.apple.xbs/F94AC8B9-7249-413E-8DE4-6D2569D8B087/TemporaryDirectory.lZt1yM/Binaries/footprint_darwinOS/install/TempContent/Objects/footprint.build/footprint.build/Objects-normal/arm64e/footprint_lto.o/6.arm64e.thinlto.o
- /Library/Caches/com.apple.xbs/F94AC8B9-7249-413E-8DE4-6D2569D8B087/TemporaryDirectory.lZt1yM/Binaries/footprint_darwinOS/install/TempContent/Objects/footprint.build/footprint.build/Objects-normal/arm64e/footprint_lto.o/7.arm64e.thinlto.o
- /Library/Caches/com.apple.xbs/F94AC8B9-7249-413E-8DE4-6D2569D8B087/TemporaryDirectory.lZt1yM/Binaries/footprint_darwinOS/install/TempContent/Objects/footprint.build/footprint.build/Objects-normal/arm64e/footprint_lto.o/8.arm64e.thinlto.o
- /Library/Caches/com.apple.xbs/F94AC8B9-7249-413E-8DE4-6D2569D8B087/TemporaryDirectory.lZt1yM/Sources/footprint_darwinOS/footprint/
- /Library/Caches/com.apple.xbs/F94AC8B9-7249-413E-8DE4-6D2569D8B087/TemporaryDirectory.lZt1yM/Sources/footprint_darwinOS/footprint/Import Hacks/
- /Library/Caches/com.apple.xbs/F94AC8B9-7249-413E-8DE4-6D2569D8B087/TemporaryDirectory.lZt1yM/Sources/footprint_darwinOS/shared/
- GCC_except_table27
- OBJC_IVAR_$_FPMemoryMultiRegion._auxDataName
- OBJC_IVAR_$_FPMemoryMultiRegion._regionSize
- OBJC_IVAR_$_FPMemoryMultiRegion._totalRegions
- OBJC_IVAR_$_FPMemoryRegion._user_tag
- OBJC_IVAR_$_FPMemoryRegion._wired
- OBJC_IVAR_$_FPSharedCache._slide
- _OBJC_$_PROP_LIST_FPMemoryObject.130
- _OSKextCopyLoadedKextInfo
- _VMURegionTypeDescriptionForTagShareProtAndPager
- __Block_byref_object_copy_.181
- __Block_byref_object_dispose_.182
- ___43-[FPOutputFormatterJSON JSONForCategories:]_block_invoke
- ___44+[FPSharedCache sharedCacheForDyldSnapshot:]_block_invoke
- ___44+[FPSharedCache sharedCacheForDyldSnapshot:]_block_invoke_2
- ___block_descriptor_102_e8_32s40s48s56s64r72r_e93_B56?0Q8Q16^{vm_region_submap_info_64=iiIQIIIIIISCCiiISSIQ}24i32"NSString"36"NSString"44B52ls32l8s40l8s48l8r64l8s56l8r72l8
- ___block_descriptor_120_e8_32s40s48s56s64r72r80r88r96r104r_e5_v8?0ls32l8r64l8r72l8r80l8r88l8s40l8r96l8r104l8s48l8s56l8
- ___block_descriptor_40_e12_B24?0Q8^v16l
- ___block_descriptor_40_e8_32r_e30_v16?0^{dyld_shared_cache_s=}8lr32l8
- ___block_descriptor_40_e8_32r_e9_v16?0r*8lr32l8
- ___block_descriptor_64_e8_32s40s48r_e8_v16?0Q8ls32l8r48l8s40l8
- ___block_descriptor_64_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
- ___block_descriptor_73_e8_32s40r48r_e18_v40?0^i8Q16Q24Q32lr40l8r48l8s32l8
- ___block_descriptor_73_e8_32s40s48s56s64s_e12_v24?0^8Q16ls32l8s40l8s48l8s56l8s64l8
- ___block_descriptor_83_e8_32s40s48r56r_e18_v40?0^i8Q16Q24Q32ls32l8r48l8r56l8s40l8
- ___sampleFootprint_block_invoke_4
- ___sampleFootprint_block_invoke_5
- __block_literal_global.102
- __block_literal_global.107
- __block_literal_global.182
- __block_literal_global.188
- __block_literal_global.427
- _dispatch_async
- _dyld_shared_cache_for_each_file
- _dyld_shared_cache_for_file
- _kCFBundleIdentifierKey
- _kernCounterLabels
- _kernMemoryLabels
- _objc_initWeak
- _objc_msgSend$UTF8String
- _objc_msgSend$dictionaryWithCapacity:
- _objc_msgSend$nonretainedObjectValue
- _objc_msgSend$valueWithNonretainedObject:
- _objc_retainAutoreleasedReturnValue
CStrings:
+ "    --noReusedAsClean        workaround to see true footprint for reusable pages\n                             (won't match phys_footprint, no effect on memgraphs)\n"
+ "    -w, --wide                show wide output with all columns and full paths (implies --swapped --wired)\n    --swapped                 show swapped/compressed column\n    --wired                   show wired column\n    --vmObjectDirty           interpret dirty memory as viewed by VM objects in the kernel\n    --unmapped                search all processes for unmapped memory owned by the target processes\n    --sample <secs>           repeatedly gather footprint at the given sampling interval (best effort,\n                              can be fractional — e.g. 0.5)\n    --sample-duration <secs>  how long to sample in seconds (default: 0 / unlimited)\n    --noCategories            print only total footprint and auxiliary data\n    --sysFootprint            print system memory footprint data (boot_carveout, sys_wired, sys_unwired, sys_footprint)\n"
+ "%llu B"
+ "+[FPMemoryRegion categoryNameForTag:]"
+ "--noReusedAsClean is not compatible with memgraphs (%@) because reused-as-clean behavior only applies to live processes."
+ "B32@0:8@16^{vm_region_submap_info_64=iiIQIIIIIISCCiiISSIQISS}24"
+ "B56@?0Q8Q16^{vm_region_submap_info_64=iiIQIIIIIISCCiiISSIQISS}24i32@\"NSString\"36@\"NSString\"44B52"
+ "RA"
+ "S16@0:8"
+ "Size:%@ Resident:%@ Dirty:%@ IOSurfaceID:%s State:%s %@"
+ "T@\"NSMutableArray\",&,N,V_memoryRegions"
+ "TQ,N,V_object_id"
+ "TQ,N,V_wiredSize"
+ "TS,N"
+ "TS,R,N"
+ "VM region enumeration failed to make forward progress"
+ "_fake"
+ "_kernelWireTagToRegion"
+ "_ledgerTag"
+ "_noReusedAsClean"
+ "_reserved"
+ "_reserved2"
+ "_wireTag"
+ "_wireTagUniqueObjects"
+ "b16"
+ "b2"
+ "b3"
+ "b4"
+ "b46"
+ "desc != NULL"
+ "finalized_wire_tag_unique"
+ "initWithBytesNoCopy:length:encoding:freeWhenDone:"
+ "lengthOfBytesUsingEncoding:"
+ "maximumLengthOfBytesUsingEncoding:"
+ "noReusedAsClean"
+ "numberWithUnsignedShort:"
+ "object_id"
+ "setObject_id:"
+ "setWireTag:"
+ "setWiredSize:"
+ "v20@0:8S16"
+ "wireTag"
+ "wire_tag_%u"
+ "wire_tag_unique_objects"
- "    -w, --wide                show wide output with all columns and full paths (implies --swapped --wired)\n    --swapped                 show swapped/compressed column\n    --wired                   show wired column\n    --vmObjectDirty           interpret dirty memory as viewed by VM objects in the kernel\n    --unmapped                search all processes for unmapped memory owned by the target processes\n    --sample <interval>       repeatedly gather footprint at the given sampling interval in seconds\n                              (can be fractional — e.g. 0.5)\n    --sample-duration <secs>  how long to sample in seconds (default: 0 / unlimited)\n    --noCategories            print only total footprint and auxiliary data\n    --sysFootprint            print system memory footprint data (boot_carveout, sys_wired, sys_unwired, sys_footprint)\n"
- "%lld B"
- "(user wired)"
- "Analyzing and writing output...\n"
- "B32@0:8@16^{vm_region_submap_info_64=iiIQIIIIIISCCiiISSIQ}24"
- "B56@?0Q8Q16^{vm_region_submap_info_64=iiIQIIIIIISCCiiISSIQ}24i32@\"NSString\"36@\"NSString\"44B52"
- "MALLOC metadata"
- "MALLOC_HUGE"
- "MALLOC_LARGE"
- "MALLOC_LARGE_REUSABLE"
- "MALLOC_LARGE_REUSED"
- "MALLOC_NANO"
- "MALLOC_REALLOC"
- "MALLOC_SMALL"
- "MALLOC_TINY"
- "Memory Tag"
- "OSBundleLoadTag"
- "RQ"
- "Size:%s Resident:%s Dirty:%s IOSurfaceID:%s State:%s %s"
- "VM_KERN_COUNT_BOOT_STOLEN"
- "VM_KERN_COUNT_EXCLAVES_CARVEOUT"
- "VM_KERN_COUNT_LOPAGE"
- "VM_KERN_COUNT_MANAGED"
- "VM_KERN_COUNT_MAP_KALLOC"
- "VM_KERN_COUNT_MAP_KALLOC_LARGE_DATA"
- "VM_KERN_COUNT_MAP_KERNEL"
- "VM_KERN_COUNT_MAP_KERNEL_DATA"
- "VM_KERN_COUNT_MAP_ZONE"
- "VM_KERN_COUNT_RESERVED"
- "VM_KERN_COUNT_STOLEN"
- "VM_KERN_COUNT_WIRED"
- "VM_KERN_COUNT_WIRED_BOOT"
- "VM_KERN_COUNT_WIRED_MANAGED"
- "VM_KERN_COUNT_WIRED_STATIC_KERNELCACHE"
- "VM_KERN_MEMORY_ANY"
- "VM_KERN_MEMORY_BSD"
- "VM_KERN_MEMORY_COMPRESSED_DATA"
- "VM_KERN_MEMORY_COMPRESSOR"
- "VM_KERN_MEMORY_CPU"
- "VM_KERN_MEMORY_DIAG"
- "VM_KERN_MEMORY_EXCLAVES"
- "VM_KERN_MEMORY_EXCLAVES_SHARED"
- "VM_KERN_MEMORY_FILE"
- "VM_KERN_MEMORY_FIRST_DYNAMIC"
- "VM_KERN_MEMORY_HV"
- "VM_KERN_MEMORY_IOKIT"
- "VM_KERN_MEMORY_IPC"
- "VM_KERN_MEMORY_KALLOC"
- "VM_KERN_MEMORY_KALLOC_DATA"
- "VM_KERN_MEMORY_KALLOC_SHARED"
- "VM_KERN_MEMORY_KALLOC_TYPE"
- "VM_KERN_MEMORY_KEXT"
- "VM_KERN_MEMORY_LIBKERN"
- "VM_KERN_MEMORY_LOG"
- "VM_KERN_MEMORY_LTABLE"
- "VM_KERN_MEMORY_MBUF"
- "VM_KERN_MEMORY_MLOCK"
- "VM_KERN_MEMORY_MTAG"
- "VM_KERN_MEMORY_NONE"
- "VM_KERN_MEMORY_OSFMK"
- "VM_KERN_MEMORY_OSKEXT"
- "VM_KERN_MEMORY_PHANTOM_CACHE"
- "VM_KERN_MEMORY_PMAP"
- "VM_KERN_MEMORY_PTE"
- "VM_KERN_MEMORY_REASON"
- "VM_KERN_MEMORY_RECOUNT"
- "VM_KERN_MEMORY_RETIRED"
- "VM_KERN_MEMORY_SECURITY"
- "VM_KERN_MEMORY_SKYWALK"
- "VM_KERN_MEMORY_STACK"
- "VM_KERN_MEMORY_TRIAGE"
- "VM_KERN_MEMORY_UBC"
- "VM_KERN_MEMORY_WAITQ"
- "VM_KERN_MEMORY_ZONE"
- "_slide"
- "_user_tag"
- "_wired"
- "com.apple.footprint.sample-analysis"
- "dictionaryWithCapacity:"
- "nonretainedObjectValue"
- "v16@?0^{dyld_shared_cache_s=}8"
- "v16@?0r*8"
- "valueWithNonretainedObject:"

```
