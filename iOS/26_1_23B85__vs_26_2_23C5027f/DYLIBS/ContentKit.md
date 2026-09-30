## ContentKit

> `/System/Library/PrivateFrameworks/ContentKit.framework/ContentKit`

```diff

-4042.0.4.0.0
-  __TEXT.__text: 0x183070
+4044.0.3.0.0
+  __TEXT.__text: 0x183458
   __TEXT.__auth_stubs: 0x3230
-  __TEXT.__objc_methlist: 0xc35c
-  __TEXT.__const: 0x5afc
+  __TEXT.__objc_methlist: 0xc364
+  __TEXT.__const: 0x5b0c
   __TEXT.__dlopen_cstrs: 0x19af
-  __TEXT.__cstring: 0x18222
-  __TEXT.__swift5_typeref: 0x17ee
+  __TEXT.__cstring: 0x18289
+  __TEXT.__swift5_typeref: 0x17f4
   __TEXT.__swift5_capture: 0x214
-  __TEXT.__constg_swiftt: 0xfc8
+  __TEXT.__constg_swiftt: 0xfe4
   __TEXT.__swift5_reflstr: 0x9a7
-  __TEXT.__swift5_fieldmd: 0xe40
+  __TEXT.__swift5_fieldmd: 0xe50
   __TEXT.__swift5_builtin: 0x64
   __TEXT.__swift5_assocty: 0x1f8
-  __TEXT.__oslogstring: 0x41bb
+  __TEXT.__oslogstring: 0x41fc
   __TEXT.__swift5_protos: 0x10
   __TEXT.__swift5_proto: 0x34c
-  __TEXT.__swift5_types: 0x128
+  __TEXT.__swift5_types: 0x12c
   __TEXT.__swift_as_entry: 0x21c
   __TEXT.__swift_as_ret: 0x320
   __TEXT.__swift5_mpenum: 0x20

   __TEXT.__unwind_info: 0x6930
   __TEXT.__eh_frame: 0x6550
   __TEXT.__objc_classname: 0x1872
-  __TEXT.__objc_methname: 0x1aca1
+  __TEXT.__objc_methname: 0x1acd7
   __TEXT.__objc_methtype: 0x2ba6
-  __TEXT.__objc_stubs: 0x15480
+  __TEXT.__objc_stubs: 0x154a0
   __DATA_CONST.__got: 0x1278
-  __DATA_CONST.__const: 0x5f90
+  __DATA_CONST.__const: 0x5fb8
   __DATA_CONST.__objc_classlist: 0x6f8
   __DATA_CONST.__objc_catlist: 0x120
   __DATA_CONST.__objc_protolist: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6620
+  __DATA_CONST.__objc_selrefs: 0x6628
   __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_superrefs: 0x498
   __DATA_CONST.__objc_arraydata: 0x1490
   __AUTH_CONST.__auth_got: 0x1928
-  __AUTH_CONST.__const: 0x5418
-  __AUTH_CONST.__cfstring: 0x11ce0
+  __AUTH_CONST.__const: 0x5490
+  __AUTH_CONST.__cfstring: 0x11d00
   __AUTH_CONST.__objc_const: 0x15018
   __AUTH_CONST.__objc_intobj: 0x1ef0
   __AUTH_CONST.__objc_arrayobj: 0xf0

   - /usr/lib/libz.1.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCallKit.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
+  - /usr/lib/swift/libswiftCoreAudio_Private.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib

   - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
+  - /usr/lib/swift/libswiftMLCompute.dylib
+  - /usr/lib/swift/libswiftMapKit.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftNaturalLanguage.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
+  - /usr/lib/swift/libswiftVideoToolbox.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 9B92100C-3AD7-333F-AB52-9EE481B08C5D
-  Functions: 8908
-  Symbols:   21488
-  CStrings:  11728
+  UUID: 118F24B8-0413-33D5-9AE5-1EF60830AE5C
+  Functions: 8915
+  Symbols:   21506
+  CStrings:  11733
 
Symbols:
+ +[LNSystemEntityValueType(WFContentItem) classFromClassName:]
+ -[WFContentCollection(RichTextGeneration) getRichTextRepresentationWithPermissionRequestor:completion:]
+ GCC_except_table5428
+ _AVFoundationLibrary.22070
+ _AVFoundationLibraryCore.frameworkLibrary.22088
+ _ContactsLibrary.23380
+ _ContactsLibraryCore.frameworkLibrary.23400
+ _CoreLocationLibrary.25039
+ _CoreLocationLibraryCore.frameworkLibrary.25042
+ _FileProviderLibraryCore.frameworkLibrary.23468
+ _MapKitLibrary.25012
+ _MapKitLibraryCore.frameworkLibrary.25020
+ _MediaPlayerLibrary.26908
+ _MediaPlayerLibraryCore.frameworkLibrary.22099
+ _MediaPlayerLibraryCore.frameworkLibrary.26321
+ _MediaPlayerLibraryCore.frameworkLibrary.26919
+ _PhotosLibraryCore.frameworkLibrary.22128
+ _UIFoundationLibrary.25587
+ _UIFoundationLibraryCore.frameworkLibrary.25602
+ _UIKitLibrary.sLib.22039
+ _UIKitLibrary.sOnce.22032
+ _WFEnforceClass.23132
+ ___103-[WFContentCollection(RichTextGeneration) getRichTextRepresentationWithPermissionRequestor:completion:]_block_invoke
+ ___103-[WFContentCollection(RichTextGeneration) getRichTextRepresentationWithPermissionRequestor:completion:]_block_invoke.176
+ ___103-[WFContentCollection(RichTextGeneration) getRichTextRepresentationWithPermissionRequestor:completion:]_block_invoke_2
+ ___103-[WFContentCollection(RichTextGeneration) getRichTextRepresentationWithPermissionRequestor:completion:]_block_invoke_3
+ ___103-[WFContentCollection(RichTextGeneration) getRichTextRepresentationWithPermissionRequestor:completion:]_block_invoke_4
+ ___AVFoundationLibraryCore_block_invoke.22089
+ ___Block_byref_object_copy_.22807
+ ___Block_byref_object_copy_.25622
+ ___Block_byref_object_copy_.26998
+ ___Block_byref_object_copy_.27938
+ ___Block_byref_object_dispose_.22808
+ ___Block_byref_object_dispose_.25623
+ ___Block_byref_object_dispose_.26999
+ ___Block_byref_object_dispose_.27939
+ ___ContactsLibraryCore_block_invoke.23401
+ ___CoreLocationLibraryCore_block_invoke.25043
+ ___FileProviderLibraryCore_block_invoke.23469
+ ___MapKitLibraryCore_block_invoke.25021
+ ___MediaPlayerLibraryCore_block_invoke.22100
+ ___MediaPlayerLibraryCore_block_invoke.26322
+ ___MediaPlayerLibraryCore_block_invoke.26920
+ ___PhotosLibraryCore_block_invoke.22129
+ ___UIFoundationLibraryCore_block_invoke.25603
+ ___UIKitLibrary_block_invoke.22037
+ ___block_descriptor_48_e8_32s40s_e49_v40?0"WFContentItem"8Q16?<v?"NSError">24^B32ls32l8s40l8
+ ___block_literal_global.16.25817
+ ___block_literal_global.177.25126
+ ___block_literal_global.186.25128
+ ___block_literal_global.22033
+ ___block_literal_global.22142
+ ___block_literal_global.22981
+ ___block_literal_global.23248
+ ___block_literal_global.23405
+ ___block_literal_global.23655
+ ___block_literal_global.23906
+ ___block_literal_global.25124
+ ___block_literal_global.25813
+ ___block_literal_global.26877
+ ___block_literal_global.26941
+ ___block_literal_global.27108
+ ___block_literal_global.27192
+ ___block_literal_global.27272
+ ___block_literal_global.27802
+ ___block_literal_global.3.23658
+ ___block_literal_global.392.22903
+ ___block_literal_global.56.23250
+ ___block_literal_global.63.22060
+ ___block_literal_global.69.22062
+ ___block_literal_global.75.22064
+ ___block_literal_global.77.23684
+ ___getAVMetadataCommonKeyTitleSymbolLoc_block_invoke.22069
+ ___getAVURLAssetClass_block_invoke.22078
+ ___getCLGeocoderClass_block_invoke.25038
+ ___getCLLocationClass_block_invoke.25061
+ ___getCLPlacemarkClass_block_invoke.25054
+ ___getCNContactEmailAddressesKeySymbolLoc_block_invoke.23386
+ ___getCNContactPhoneNumbersKeySymbolLoc_block_invoke.23379
+ ___getCNContactUrlAddressesKeySymbolLoc_block_invoke.23390
+ ___getMKLocalSearchClass_block_invoke.25010
+ ___getMKLocalSearchRequestClass_block_invoke.25008
+ ___getMKMapItemClass_block_invoke.25071
+ ___getMKPlacemarkClass_block_invoke.25034
+ ___getMPMediaItemClass_block_invoke.26907
+ ___getMPMediaItemPropertyMediaTypeSymbolLoc_block_invoke.26930
+ ___getMPMediaItemPropertyTitleSymbolLoc_block_invoke.22097
+ ___getMPMediaQueryClass_block_invoke.26937
+ ___getNSDocumentTypeDocumentAttributeSymbolLoc_block_invoke.25586
+ ___getNSHTMLTextDocumentTypeSymbolLoc_block_invoke.25593
+ __swift_FORCE_LOAD_$_swiftCallKit
+ __swift_FORCE_LOAD_$_swiftCallKit_$_ContentKit
+ __swift_FORCE_LOAD_$_swiftCoreAudio_Private
+ __swift_FORCE_LOAD_$_swiftCoreAudio_Private_$_ContentKit
+ __swift_FORCE_LOAD_$_swiftMLCompute
+ __swift_FORCE_LOAD_$_swiftMLCompute_$_ContentKit
+ __swift_FORCE_LOAD_$_swiftMapKit
+ __swift_FORCE_LOAD_$_swiftMapKit_$_ContentKit
+ __swift_FORCE_LOAD_$_swiftVideoToolbox
+ __swift_FORCE_LOAD_$_swiftVideoToolbox_$_ContentKit
+ _audit_stringAVFoundation.22091
+ _audit_stringContacts.23404
+ _audit_stringCoreLocation.25046
+ _audit_stringFileProvider.23484
+ _audit_stringMapKit.25026
+ _audit_stringMediaPlayer.22103
+ _audit_stringMediaPlayer.26337
+ _audit_stringMediaPlayer.26926
+ _audit_stringPhotos.22133
+ _audit_stringUIFoundation.25606
+ _getAVMetadataCommonKeyTitleSymbolLoc.ptr.22068
+ _getAVURLAssetClass.softClass.22077
+ _getCLGeocoderClass.softClass.25037
+ _getCLLocationClass.24985
+ _getCLLocationClass.softClass.25060
+ _getCLPlacemarkClass.softClass.25053
+ _getCNContactEmailAddressesKeySymbolLoc.ptr.23385
+ _getCNContactPhoneNumbersKeySymbolLoc.ptr.23378
+ _getCNContactUrlAddressesKeySymbolLoc.ptr.23389
+ _getMKLocalSearchClass.softClass.25009
+ _getMKLocalSearchRequestClass.softClass.25007
+ _getMKMapItemClass.25065
+ _getMKMapItemClass.softClass.25070
+ _getMKPlacemarkClass.25032
+ _getMKPlacemarkClass.softClass.25033
+ _getMPMediaItemClass.softClass.26906
+ _getMPMediaItemPropertyMediaTypeSymbolLoc.ptr.26929
+ _getMPMediaItemPropertyTitleSymbolLoc.ptr.22096
+ _getMPMediaQueryClass.softClass.26936
+ _getNSDocumentTypeDocumentAttributeSymbolLoc.ptr.25585
+ _getNSHTMLTextDocumentTypeSymbolLoc.ptr.25592
+ _objc_msgSend$classFromClassName:
+ _rcsid.24887
+ _rcsid.24934
+ _sharedProvider.onceToken.22141
+ _symbolic _____ 10ContentKit21WFGeneratedOutputTypeO9ConstantsV
- -[WFContentCollection(RichTextGeneration) getRichTextRepresentation:]
- GCC_except_table5427
- _AVFoundationLibrary.22068
- _AVFoundationLibraryCore.frameworkLibrary.22086
- _ContactsLibrary.23378
- _ContactsLibraryCore.frameworkLibrary.23398
- _CoreLocationLibrary.25036
- _CoreLocationLibraryCore.frameworkLibrary.25039
- _FileProviderLibraryCore.frameworkLibrary.23466
- _MapKitLibrary.25009
- _MapKitLibraryCore.frameworkLibrary.25017
- _MediaPlayerLibrary.26905
- _MediaPlayerLibraryCore.frameworkLibrary.22097
- _MediaPlayerLibraryCore.frameworkLibrary.26318
- _MediaPlayerLibraryCore.frameworkLibrary.26916
- _PhotosLibraryCore.frameworkLibrary.22126
- _UIFoundationLibrary.25584
- _UIFoundationLibraryCore.frameworkLibrary.25599
- _UIKitLibrary.sLib.22037
- _UIKitLibrary.sOnce.22030
- _WFEnforceClass.23130
- ___69-[WFContentCollection(RichTextGeneration) getRichTextRepresentation:]_block_invoke
- ___69-[WFContentCollection(RichTextGeneration) getRichTextRepresentation:]_block_invoke.174
- ___69-[WFContentCollection(RichTextGeneration) getRichTextRepresentation:]_block_invoke_2
- ___69-[WFContentCollection(RichTextGeneration) getRichTextRepresentation:]_block_invoke_3
- ___69-[WFContentCollection(RichTextGeneration) getRichTextRepresentation:]_block_invoke_4
- ___AVFoundationLibraryCore_block_invoke.22087
- ___Block_byref_object_copy_.22805
- ___Block_byref_object_copy_.25619
- ___Block_byref_object_copy_.26995
- ___Block_byref_object_copy_.27927
- ___Block_byref_object_dispose_.22806
- ___Block_byref_object_dispose_.25620
- ___Block_byref_object_dispose_.26996
- ___Block_byref_object_dispose_.27928
- ___ContactsLibraryCore_block_invoke.23399
- ___CoreLocationLibraryCore_block_invoke.25040
- ___FileProviderLibraryCore_block_invoke.23467
- ___MapKitLibraryCore_block_invoke.25018
- ___MediaPlayerLibraryCore_block_invoke.22098
- ___MediaPlayerLibraryCore_block_invoke.26319
- ___MediaPlayerLibraryCore_block_invoke.26917
- ___PhotosLibraryCore_block_invoke.22127
- ___UIFoundationLibraryCore_block_invoke.25600
- ___UIKitLibrary_block_invoke.22035
- ___block_descriptor_40_e8_32s_e49_v40?0"WFContentItem"8Q16?<v?"NSError">24^B32ls32l8
- ___block_literal_global.16.25814
- ___block_literal_global.177.25123
- ___block_literal_global.186.25125
- ___block_literal_global.22031
- ___block_literal_global.22140
- ___block_literal_global.22979
- ___block_literal_global.23246
- ___block_literal_global.23403
- ___block_literal_global.23653
- ___block_literal_global.23904
- ___block_literal_global.25121
- ___block_literal_global.25810
- ___block_literal_global.26874
- ___block_literal_global.26938
- ___block_literal_global.27105
- ___block_literal_global.27189
- ___block_literal_global.27269
- ___block_literal_global.27793
- ___block_literal_global.3.23656
- ___block_literal_global.392.22901
- ___block_literal_global.56.23248
- ___block_literal_global.63.22058
- ___block_literal_global.69.22060
- ___block_literal_global.75.22062
- ___block_literal_global.77.23682
- ___getAVMetadataCommonKeyTitleSymbolLoc_block_invoke.22067
- ___getAVURLAssetClass_block_invoke.22076
- ___getCLGeocoderClass_block_invoke.25035
- ___getCLLocationClass_block_invoke.25058
- ___getCLPlacemarkClass_block_invoke.25051
- ___getCNContactEmailAddressesKeySymbolLoc_block_invoke.23384
- ___getCNContactPhoneNumbersKeySymbolLoc_block_invoke.23377
- ___getCNContactUrlAddressesKeySymbolLoc_block_invoke.23388
- ___getMKLocalSearchClass_block_invoke.25007
- ___getMKLocalSearchRequestClass_block_invoke.25005
- ___getMKMapItemClass_block_invoke.25068
- ___getMKPlacemarkClass_block_invoke.25031
- ___getMPMediaItemClass_block_invoke.26904
- ___getMPMediaItemPropertyMediaTypeSymbolLoc_block_invoke.26927
- ___getMPMediaItemPropertyTitleSymbolLoc_block_invoke.22095
- ___getMPMediaQueryClass_block_invoke.26934
- ___getNSDocumentTypeDocumentAttributeSymbolLoc_block_invoke.25583
- ___getNSHTMLTextDocumentTypeSymbolLoc_block_invoke.25590
- _audit_stringAVFoundation.22089
- _audit_stringContacts.23402
- _audit_stringCoreLocation.25043
- _audit_stringFileProvider.23482
- _audit_stringMapKit.25023
- _audit_stringMediaPlayer.22101
- _audit_stringMediaPlayer.26334
- _audit_stringMediaPlayer.26923
- _audit_stringPhotos.22131
- _audit_stringUIFoundation.25603
- _getAVMetadataCommonKeyTitleSymbolLoc.ptr.22066
- _getAVURLAssetClass.softClass.22075
- _getCLGeocoderClass.softClass.25034
- _getCLLocationClass.24982
- _getCLLocationClass.softClass.25057
- _getCLPlacemarkClass.softClass.25050
- _getCNContactEmailAddressesKeySymbolLoc.ptr.23383
- _getCNContactPhoneNumbersKeySymbolLoc.ptr.23376
- _getCNContactUrlAddressesKeySymbolLoc.ptr.23387
- _getMKLocalSearchClass.softClass.25006
- _getMKLocalSearchRequestClass.softClass.25004
- _getMKMapItemClass.25062
- _getMKMapItemClass.softClass.25067
- _getMKPlacemarkClass.25029
- _getMKPlacemarkClass.softClass.25030
- _getMPMediaItemClass.softClass.26903
- _getMPMediaItemPropertyMediaTypeSymbolLoc.ptr.26926
- _getMPMediaItemPropertyTitleSymbolLoc.ptr.22094
- _getMPMediaQueryClass.softClass.26933
- _getNSDocumentTypeDocumentAttributeSymbolLoc.ptr.25582
- _getNSHTMLTextDocumentTypeSymbolLoc.ptr.25589
- _rcsid.24884
- _rcsid.24931
- _sharedProvider.onceToken.22139
CStrings:
+ "%s LNSystemEntityValueType is getting a malformed class name: %@"
+ "+[LNSystemEntityValueType(WFContentItem) classFromClassName:]"
+ "-[WFContentCollection(RichTextGeneration) getRichTextRepresentationWithPermissionRequestor:completion:]_block_invoke_4"
+ "Entity"
+ "classFromClassName:"
+ "getRichTextRepresentationWithPermissionRequestor:completion:"
- "-[WFContentCollection(RichTextGeneration) getRichTextRepresentation:]_block_invoke_4"
- "getRichTextRepresentation:"

```
