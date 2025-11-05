## PhotosUIFoundation

> `/System/iOSSupport/System/Library/PrivateFrameworks/PhotosUIFoundation.framework/Versions/A/PhotosUIFoundation`

```diff

-741.0.130.0.0
-  __TEXT.__text: 0x852bc
-  __TEXT.__auth_stubs: 0x2330
-  __TEXT.__objc_methlist: 0x6840
-  __TEXT.__cstring: 0x6649
-  __TEXT.__const: 0x38b0
-  __TEXT.__constg_swiftt: 0x2184
-  __TEXT.__swift5_typeref: 0x19b9
-  __TEXT.__swift5_reflstr: 0x1073
-  __TEXT.__swift5_fieldmd: 0x1128
+751.0.104.0.0
+  __TEXT.__text: 0x87070
+  __TEXT.__auth_stubs: 0x2340
+  __TEXT.__objc_methlist: 0x8204
+  __TEXT.__const: 0x3ab0
+  __TEXT.__dlopen_cstrs: 0x58
+  __TEXT.__cstring: 0x645d
+  __TEXT.__constg_swiftt: 0x22f4
+  __TEXT.__swift5_typeref: 0x1a8f
+  __TEXT.__swift5_reflstr: 0x10f3
+  __TEXT.__swift5_fieldmd: 0x11cc
   __TEXT.__swift5_builtin: 0x12c
   __TEXT.__swift5_assocty: 0x5a0
-  __TEXT.__swift5_proto: 0x208
-  __TEXT.__swift5_types: 0x158
-  __TEXT.__swift5_capture: 0x748
-  __TEXT.__swift5_protos: 0x68
+  __TEXT.__swift5_proto: 0x22c
+  __TEXT.__swift5_types: 0x164
+  __TEXT.__swift5_capture: 0x7c8
+  __TEXT.__swift5_protos: 0x70
   __TEXT.__oslogstring: 0xa38
+  __TEXT.__swift_as_entry: 0x30
+  __TEXT.__swift_as_ret: 0x18
   __TEXT.__gcc_except_tab: 0x728
   __TEXT.__ustring: 0x76
-  __TEXT.__dlopen_cstrs: 0x58
-  __TEXT.__unwind_info: 0x2ef0
-  __TEXT.__eh_frame: 0xc50
-  __TEXT.__objc_classname: 0x105a
-  __TEXT.__objc_methname: 0x1256c
-  __TEXT.__objc_methtype: 0x327d
-  __TEXT.__objc_stubs: 0x8ec0
-  __DATA_CONST.__got: 0x868
-  __DATA_CONST.__const: 0x2210
-  __DATA_CONST.__objc_classlist: 0x3d0
+  __TEXT.__unwind_info: 0x2fb8
+  __TEXT.__eh_frame: 0xce0
+  __TEXT.__objc_classname: 0x1077
+  __TEXT.__objc_methname: 0x12714
+  __TEXT.__objc_methtype: 0x32bc
+  __TEXT.__objc_stubs: 0x8ea0
+  __DATA_CONST.__got: 0x878
+  __DATA_CONST.__const: 0x2290
+  __DATA_CONST.__objc_classlist: 0x3e0
   __DATA_CONST.__objc_catlist: 0x90
   __DATA_CONST.__objc_protolist: 0x1f0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3c48
+  __DATA_CONST.__objc_selrefs: 0x3e08
   __DATA_CONST.__objc_protorefs: 0x70
-  __DATA_CONST.__objc_superrefs: 0x298
+  __DATA_CONST.__objc_superrefs: 0x2a0
   __DATA_CONST.__objc_arraydata: 0x100
-  __AUTH_CONST.__auth_got: 0x11a8
-  __AUTH_CONST.__const: 0x2f90
-  __AUTH_CONST.__cfstring: 0x2ea0
-  __AUTH_CONST.__objc_const: 0x13220
+  __AUTH_CONST.__auth_got: 0x11b0
+  __AUTH_CONST.__const: 0x3268
+  __AUTH_CONST.__cfstring: 0x2ee0
+  __AUTH_CONST.__objc_const: 0x105b0
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__objc_doubleobj: 0x1d0
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH.__objc_data: 0x2808
-  __AUTH.__data: 0x11c8
-  __DATA.__objc_ivar: 0x7b8
-  __DATA.__data: 0x2bf0
-  __DATA.__bss: 0x39c8
+  __AUTH.__objc_data: 0x2858
+  __AUTH.__data: 0x1258
+  __DATA.__objc_ivar: 0x7bc
+  __DATA.__data: 0x2cb8
+  __DATA.__bss: 0x3b58
   __DATA.__common: 0x8
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftIOKit.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: DE609A8A-53B4-313A-BA74-C7E47FA0E621
-  Functions: 5144
-  Symbols:   7314
-  CStrings:  4664
+  UUID: 9D847A31-ACC2-30CC-94C4-AAA56FE36562
+  Functions: 5258
+  Symbols:   7358
+  CStrings:  4679
 
Symbols:
+ +[NSError(PXError) _px_errorWithDomain:code:underlyingError:userInfo:localizedDescription:debugDescription:]
+ +[NSError(PXError) px_errorWithDomain:code:underlyingError:userInfo:debugDescription:]
+ +[PXAccessibilityUtilities isReduceTransparencyEnabled]
+ -[PXAssetsDataSourceManager createReverselySortedDataSourceManager]
+ -[PXAssetsDataSourceManager isReverseSortOrder]
+ -[PXAssetsDataSourceManager setReverseSortOrder:]
+ -[PXBaseDisplayAssetCollection px_isVirtualCollection]
+ -[PXObservable didPublishChanges:]
+ -[PXPhotosEnvironmentReference .cxx_destruct]
+ -[PXPhotosEnvironmentReference initWithWrappedValue:]
+ -[PXPhotosEnvironmentReference init]
+ -[PXPhotosEnvironmentReference wrappedValue]
+ -[PXSectionedDataSourceManager didPublishChanges:]
+ GCC_except_table1009
+ GCC_except_table1063
+ GCC_except_table1084
+ GCC_except_table1093
+ GCC_except_table1095
+ GCC_except_table1110
+ GCC_except_table1247
+ GCC_except_table1265
+ GCC_except_table1324
+ GCC_except_table1452
+ GCC_except_table1484
+ GCC_except_table1694
+ GCC_except_table1708
+ GCC_except_table1712
+ GCC_except_table1719
+ GCC_except_table1726
+ GCC_except_table1741
+ GCC_except_table1748
+ GCC_except_table1762
+ GCC_except_table1858
+ GCC_except_table2014
+ GCC_except_table2080
+ GCC_except_table2142
+ GCC_except_table2158
+ GCC_except_table2236
+ GCC_except_table2246
+ GCC_except_table2379
+ GCC_except_table2464
+ GCC_except_table2596
+ GCC_except_table2609
+ GCC_except_table2612
+ GCC_except_table2631
+ GCC_except_table2636
+ GCC_except_table2644
+ GCC_except_table2648
+ GCC_except_table2652
+ GCC_except_table2678
+ GCC_except_table2704
+ GCC_except_table834
+ GCC_except_table948
+ GCC_except_table958
+ GCC_except_table983
+ OBJC_IVAR_$_PXPhotosEnvironmentReference._wrappedValue
+ _OBJC_CLASS_$_PXPhotosEnvironmentReference
+ _OBJC_CLASS_$_UIAction
+ _OBJC_METACLASS_$_PXPhotosEnvironmentReference
+ _OUTLINED_FUNCTION_34
+ _OUTLINED_FUNCTION_35
+ _OUTLINED_FUNCTION_36
+ _OUTLINED_FUNCTION_37
+ _PROTOCOLS__TtC18PhotosUIFoundation15MenuGroupAction.4
+ _PXActionTypeHelp
+ _PXFontWithTextStyleSymbolicTraitsWeightContentSizeCategory
+ _UIAccessibilityIsReduceTransparencyEnabled
+ __Block_byref_object_copy_.2817
+ __Block_byref_object_copy_.3134
+ __Block_byref_object_copy_.5375
+ __Block_byref_object_copy_.6907
+ __Block_byref_object_copy_.8258
+ __Block_byref_object_copy_.8412
+ __Block_byref_object_dispose_.2818
+ __Block_byref_object_dispose_.3135
+ __Block_byref_object_dispose_.5376
+ __Block_byref_object_dispose_.6908
+ __Block_byref_object_dispose_.8259
+ __Block_byref_object_dispose_.8413
+ __DATA__TtC18PhotosUIFoundationP33_ACBB788456F6235DF61E27048EEF3A1711Environment
+ __IVARS__TtC18PhotosUIFoundationP33_ACBB788456F6235DF61E27048EEF3A1711Environment
+ __METACLASS_DATA__TtC18PhotosUIFoundationP33_ACBB788456F6235DF61E27048EEF3A1711Environment
+ __OBJC_$_CLASS_PROP_LIST_PXAccessibilityUtilities
+ __OBJC_$_INSTANCE_METHODS_PXPhotosEnvironmentReference
+ __OBJC_$_INSTANCE_VARIABLES_PXPhotosEnvironmentReference
+ __OBJC_$_PROP_LIST_PXPhotosEnvironmentReference
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_PXMenuAction
+ __OBJC_CLASS_RO_$_PXPhotosEnvironmentReference
+ __OBJC_METACLASS_RO_$_PXPhotosEnvironmentReference
+ ___swift_async_entry_functlets
+ ___swift_async_ret_functlets
+ __block_literal_global.1639
+ __block_literal_global.2799
+ __block_literal_global.2827
+ __block_literal_global.2997
+ __block_literal_global.3181
+ __block_literal_global.3326
+ __block_literal_global.3729
+ __block_literal_global.3853
+ __block_literal_global.3890
+ __block_literal_global.4200
+ __block_literal_global.4603
+ __block_literal_global.4878
+ __block_literal_global.4983
+ __block_literal_global.4986
+ __block_literal_global.5230
+ __block_literal_global.5423
+ __block_literal_global.5939
+ __block_literal_global.6053
+ __block_literal_global.629
+ __block_literal_global.6419
+ __block_literal_global.684
+ __block_literal_global.7548
+ __block_literal_global.7682
+ __block_literal_global.7787
+ __block_literal_global.8004
+ __block_literal_global.8490
+ __block_literal_global.8524
+ _associated conformance 18PhotosUIFoundation0A27AnyCollectionAdditionalInfoVSHAASQ
+ _dynamic_cast_existential_1_conditional
+ _objc_msgSend$_px_errorWithDomain:code:underlyingError:userInfo:localizedDescription:debugDescription:
+ _objc_msgSend$didPublishChanges:
+ _objc_msgSend$px_isEvent
+ _objc_msgSend$px_isMemory
+ _objc_msgSend$px_isSavedTodayCollection
+ _objc_msgSend$px_isTrip
+ _objc_msgSend$px_isUserCreated
+ _objc_msgSend$setValuesForKeysWithDictionary:
+ _objc_retain_x6
+ _swift_conformsToProtocol2
+ _symbolic $s18PhotosUIFoundation0A22ApproximatelyEquatableP
+ _symbolic $s18PhotosUIFoundation0A24CollectionAdditionalInfoP
+ _symbolic Sb______pYbc 18PhotosUIFoundation0A24CollectionAdditionalInfoP
+ _symbolic So13UIMenuElementCSgyypSgccSg
+ _symbolic _____ 18PhotosUIFoundation0A20WeakSendableTransferV
+ _symbolic _____ 18PhotosUIFoundation0A27AnyCollectionAdditionalInfoV
+ _symbolic _____ 18PhotosUIFoundation11Environment33_ACBB788456F6235DF61E27048EEF3A17LLC
+ _symbolic _____Sg 18PhotosUIFoundation0A27AnyCollectionAdditionalInfoV
+ _symbolic _____Sg_ABt 18PhotosUIFoundation0A27AnyCollectionAdditionalInfoV
+ _symbolic ______p 18PhotosUIFoundation0A11EnvironmentP
+ _symbolic ______p 18PhotosUIFoundation0A24CollectionAdditionalInfoP
+ _symbolic _____yxG 18PhotosUIFoundation15MenuGroupActionC
+ _symbolic yXlSgIeyBy_
+ _symbolic ypSgIegn_
+ _symbolic yypSgc
+ block_copy_helper.8
+ block_descriptor.10
+ block_destroy_helper.9
+ defaultManager.onceToken.3728
- +[NSError(PXError) _px_errorWithDomain:code:underlyingError:localizedDescription:debugDescription:]
- -[PXObservable didPublishChanges]
- -[PXSectionedDataSourceManager didPublishChanges]
- GCC_except_table1008
- GCC_except_table1062
- GCC_except_table1083
- GCC_except_table1092
- GCC_except_table1094
- GCC_except_table1109
- GCC_except_table1246
- GCC_except_table1264
- GCC_except_table1323
- GCC_except_table1451
- GCC_except_table1483
- GCC_except_table1692
- GCC_except_table1706
- GCC_except_table1710
- GCC_except_table1717
- GCC_except_table1724
- GCC_except_table1739
- GCC_except_table1746
- GCC_except_table1760
- GCC_except_table1856
- GCC_except_table2012
- GCC_except_table2078
- GCC_except_table2137
- GCC_except_table2153
- GCC_except_table2230
- GCC_except_table2240
- GCC_except_table2373
- GCC_except_table2458
- GCC_except_table2585
- GCC_except_table2587
- GCC_except_table2601
- GCC_except_table2620
- GCC_except_table2625
- GCC_except_table2633
- GCC_except_table2637
- GCC_except_table2641
- GCC_except_table2667
- GCC_except_table2693
- GCC_except_table833
- GCC_except_table947
- GCC_except_table957
- GCC_except_table982
- _PROTOCOLS__TtC18PhotosUIFoundation15MenuGroupAction.1
- __Block_byref_object_copy_.2818
- __Block_byref_object_copy_.3135
- __Block_byref_object_copy_.5369
- __Block_byref_object_copy_.6895
- __Block_byref_object_copy_.8216
- __Block_byref_object_copy_.8370
- __Block_byref_object_dispose_.2819
- __Block_byref_object_dispose_.3136
- __Block_byref_object_dispose_.5370
- __Block_byref_object_dispose_.6896
- __Block_byref_object_dispose_.8217
- __Block_byref_object_dispose_.8371
- __block_literal_global.1641
- __block_literal_global.2800
- __block_literal_global.2828
- __block_literal_global.2998
- __block_literal_global.3182
- __block_literal_global.3327
- __block_literal_global.3730
- __block_literal_global.3854
- __block_literal_global.3891
- __block_literal_global.4201
- __block_literal_global.4601
- __block_literal_global.4876
- __block_literal_global.4981
- __block_literal_global.4984
- __block_literal_global.5224
- __block_literal_global.5417
- __block_literal_global.5932
- __block_literal_global.6046
- __block_literal_global.632
- __block_literal_global.6412
- __block_literal_global.687
- __block_literal_global.7534
- __block_literal_global.7668
- __block_literal_global.7773
- __block_literal_global.7964
- __block_literal_global.8448
- __block_literal_global.8482
- __swift_FORCE_LOAD_$_swiftFileProvider
- __swift_FORCE_LOAD_$_swiftFileProvider_$_PhotosUIFoundation
- _objc_msgSend$_px_errorWithDomain:code:underlyingError:localizedDescription:debugDescription:
- _objc_msgSend$didPublishChanges
- _objc_msgSend$px_isAllLibraryDuplicatesSmartAlbum
- _objc_msgSend$px_isHiddenSmartAlbum
- _objc_msgSend$px_isImportHistoryCollection
- _objc_msgSend$px_isMediaTypeSmartAlbum
- _objc_msgSend$px_isRecentlyDeletedSmartAlbum
- _objc_msgSend$px_isRecentlyEditedSmartAlbum
- _objc_msgSend$px_isUtilityCollection
- _objc_release_x2
- _symbolic SS3key_yp5valuetSg
- defaultManager.onceToken.3729
CStrings:
+ "-[PXPhotosEnvironmentReference init]"
+ "@\"UIMenuElement\"16@?0@?<v@?@>8"
+ "@64@0:8@16q24@32@40@48@56"
+ "@?<@\"UIMenuElement\"@?@?<v@?@>>16@0:8"
+ "Mismatched value counts after additions and subtractions: array: %p, array.count: %tu, newArray: %p, newArray.count: %tu"
+ "PXActionTypeHelp"
+ "PXPhotosEnvironmentReference"
+ "PXPhotosEnvironmentReference.m"
+ "PhotosUIFoundation/UIMenuElement+PXMenuAction.swift"
+ "T@,R,N,V_wrappedValue"
+ "T@?,?,R,N"
+ "T@?,N,R"
+ "TB,N,GisReverseSortOrder"
+ "_TtC18PhotosUIFoundationP33_ACBB788456F6235DF61E27048EEF3A1711Environment"
+ "__additionalInfo"
+ "_customMenuElementFactory"
+ "_px_errorWithDomain:code:underlyingError:userInfo:localizedDescription:debugDescription:"
+ "_wrappedValue"
+ "createReverselySortedDataSourceManager"
+ "customMenuElementFactory"
+ "didPublishChanges:"
+ "environmentValues"
+ "focalLength"
+ "focalLengthIn35mm"
+ "initWithWrappedValue:"
+ "isReduceTransparencyEnabled"
+ "isReverseSortOrder"
+ "px_errorWithDomain:code:underlyingError:userInfo:debugDescription:"
+ "px_isVirtualCollection"
+ "reverseSortOrder"
+ "sender"
+ "setReverseSortOrder:"
+ "setValuesForKeysWithDictionary:"
+ "waitForPrependAndMainToLoad"
+ "wrappedValue"
- "Can't construct Array with count < 0"
- "Insufficient space allocated to copy string contents"
- "Mismatched value counts after additions and subtractions."
- "Negative value is not representable"
- "PhotosUIFoundation/UIAction+PXMenuAction.swift"
- "Swift/Array.swift"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/Integers.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.initialize with negative count"
- "UnsafeMutablePointer.moveInitialize with negative count"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "UnsafeMutableRawPointer.initializeMemory with negative count"
- "_px_errorWithDomain:code:underlyingError:localizedDescription:debugDescription:"
- "didPublishChanges"
- "invalid Collection: less than 'count' elements in collection"
- "waitForPrependItemListManagerList"

```
