## AVKit

> `/System/iOSSupport/System/Library/Frameworks/AVKit.framework/Versions/A/AVKit`

```diff

-  __TEXT.__text: 0x15f0d4
-  __TEXT.__objc_methlist: 0x19230
+  __TEXT.__text: 0x1626ec
+  __TEXT.__objc_methlist: 0x197d8
   __TEXT.__dlopen_cstrs: 0x58
-  __TEXT.__const: 0x20b0
-  __TEXT.__constg_swiftt: 0x938
-  __TEXT.__swift5_typeref: 0x31a8
-  __TEXT.__swift5_builtin: 0x78
-  __TEXT.__swift5_reflstr: 0x565
-  __TEXT.__swift5_fieldmd: 0x54c
-  __TEXT.__swift5_assocty: 0x108
-  __TEXT.__swift5_proto: 0x70
-  __TEXT.__swift5_types: 0x6c
-  __TEXT.__cstring: 0xc2d4
-  __TEXT.__swift5_capture: 0x480
-  __TEXT.__swift_as_entry: 0x3c
-  __TEXT.__swift_as_cont: 0x54
+  __TEXT.__const: 0x24b0
+  __TEXT.__constg_swiftt: 0xd28
+  __TEXT.__swift5_typeref: 0x33c8
+  __TEXT.__swift5_builtin: 0x8c
+  __TEXT.__swift5_reflstr: 0x5c5
+  __TEXT.__swift5_fieldmd: 0x644
+  __TEXT.__swift5_assocty: 0x138
+  __TEXT.__swift5_proto: 0x98
+  __TEXT.__swift5_types: 0x78
+  __TEXT.__cstring: 0xc35e
+  __TEXT.__swift5_capture: 0x448
+  __TEXT.__swift_as_entry: 0x38
+  __TEXT.__swift_as_cont: 0x50
   __TEXT.__swift_as_ret: 0x10
-  __TEXT.__swift5_protos: 0x20
-  __TEXT.__gcc_except_tab: 0x3670
-  __TEXT.__oslogstring: 0x4e3c
+  __TEXT.__swift5_protos: 0x40
+  __TEXT.__gcc_except_tab: 0x363c
+  __TEXT.__oslogstring: 0x4d7c
   __TEXT.__ustring: 0x3c
-  __TEXT.__unwind_info: 0x5c50
-  __TEXT.__eh_frame: 0xc80
+  __TEXT.__unwind_info: 0x5de0
+  __TEXT.__eh_frame: 0xc28
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x25f0
-  __DATA_CONST.__objc_classlist: 0x860
+  __DATA_CONST.__objc_classlist: 0x8a0
   __DATA_CONST.__objc_catlist: 0xd0
   __DATA_CONST.__objc_protolist: 0x460
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa7e0
+  __DATA_CONST.__objc_selrefs: 0xa890
   __DATA_CONST.__objc_protorefs: 0x78
-  __DATA_CONST.__objc_superrefs: 0x680
+  __DATA_CONST.__objc_superrefs: 0x6c0
   __DATA_CONST.__objc_arraydata: 0x168
-  __DATA_CONST.__got: 0xf18
-  __AUTH_CONST.__const: 0x3090
-  __AUTH_CONST.__cfstring: 0x59a0
-  __AUTH_CONST.__objc_const: 0x2de90
+  __DATA_CONST.__got: 0x1020
+  __AUTH_CONST.__const: 0x3130
+  __AUTH_CONST.__cfstring: 0x5aa0
+  __AUTH_CONST.__objc_const: 0x2ea28
   __AUTH_CONST.__objc_intobj: 0x4f8
   __AUTH_CONST.__objc_arrayobj: 0x168
   __AUTH_CONST.__objc_doubleobj: 0x210
-  __AUTH_CONST.__auth_got: 0xf30
-  __AUTH.__objc_data: 0x48f8
-  __AUTH.__data: 0x410
-  __DATA.__objc_ivar: 0x28a4
-  __DATA.__data: 0x3a00
-  __DATA.__bss: 0x11c8
+  __AUTH_CONST.__auth_got: 0xf28
+  __AUTH.__objc_data: 0x4d20
+  __AUTH.__data: 0x3e8
+  __DATA.__objc_ivar: 0x290c
+  __DATA.__data: 0x3a48
+  __DATA.__bss: 0x16c8
   __DATA.__common: 0xe8
-  __DATA_DIRTY.__objc_data: 0x12d0
-  __DATA_DIRTY.__data: 0x50
+  __DATA_DIRTY.__objc_data: 0x1128
+  __DATA_DIRTY.__data: 0x80
   __DATA_DIRTY.__bss: 0x18
   - /System/Library/Frameworks/AVFAudio.framework/Versions/A/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 9481
-  Symbols:   20411
-  CStrings:  2390
+  Functions: 9698
+  Symbols:   20661
+  CStrings:  2404
 
Sections:
~ __TEXT.__swift_as_ret : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_doubleobj : content changed
Symbols:
+ +[AVPlaybackUserInterfaceContentArtwork artworkWithURL:contentType:size:]
+ +[AVPlaybackUserInterfaceContentArtwork supportsSecureCoding]
+ +[AVPlaybackUserInterfaceContentMetadata supportsSecureCoding]
+ +[AVPlaybackUserInterfaceContentMetadataTemplate supportsSecureCoding]
+ +[AVPlaybackUserInterfaceContentURLArtwork supportsSecureCoding]
+ +[AVPlaybackUserInterfaceContentVideoProperties supportsSecureCoding]
+ +[AVPlaybackUserInterfaceMediaSelectionOption supportsSecureCoding]
+ +[AVPlaybackUserInterfacePlaybackPosition supportsSecureCoding]
+ +[AVPlaybackUserInterfaceTimelineSegment supportsSecureCoding]
+ -[AVMobileGlassControlsView _topInsetForLayoutFrame]
+ -[AVMobileGlassControlsView layoutUsingBarInsets]
+ -[AVPlaybackUserInterfaceContentArtwork copyWithZone:]
+ -[AVPlaybackUserInterfaceContentArtwork encodeWithCoder:]
+ -[AVPlaybackUserInterfaceContentArtwork hash]
+ -[AVPlaybackUserInterfaceContentArtwork initWithCoder:]
+ -[AVPlaybackUserInterfaceContentArtwork initWithSize:]
+ -[AVPlaybackUserInterfaceContentArtwork isEqual:]
+ -[AVPlaybackUserInterfaceContentArtwork isEqualToContentArtwork:]
+ -[AVPlaybackUserInterfaceContentArtwork size]
+ -[AVPlaybackUserInterfaceContentMetadata .cxx_destruct]
+ -[AVPlaybackUserInterfaceContentMetadata artworkRepresentations]
+ -[AVPlaybackUserInterfaceContentMetadata copyWithZone:]
+ -[AVPlaybackUserInterfaceContentMetadata encodeWithCoder:]
+ -[AVPlaybackUserInterfaceContentMetadata hash]
+ -[AVPlaybackUserInterfaceContentMetadata initWithCoder:]
+ -[AVPlaybackUserInterfaceContentMetadata initWithTemplate:]
+ -[AVPlaybackUserInterfaceContentMetadata initWithVideoProperties:title:subtitle:artworkRepresentations:]
+ -[AVPlaybackUserInterfaceContentMetadata isEqual:]
+ -[AVPlaybackUserInterfaceContentMetadata isEqualToMetadata:]
+ -[AVPlaybackUserInterfaceContentMetadata subtitle]
+ -[AVPlaybackUserInterfaceContentMetadata title]
+ -[AVPlaybackUserInterfaceContentMetadata videoProperties]
+ -[AVPlaybackUserInterfaceContentMetadataTemplate .cxx_destruct]
+ -[AVPlaybackUserInterfaceContentMetadataTemplate artworkRepresentations]
+ -[AVPlaybackUserInterfaceContentMetadataTemplate copyWithZone:]
+ -[AVPlaybackUserInterfaceContentMetadataTemplate encodeWithCoder:]
+ -[AVPlaybackUserInterfaceContentMetadataTemplate hash]
+ -[AVPlaybackUserInterfaceContentMetadataTemplate initWithCoder:]
+ -[AVPlaybackUserInterfaceContentMetadataTemplate init]
+ -[AVPlaybackUserInterfaceContentMetadataTemplate isEqual:]
+ -[AVPlaybackUserInterfaceContentMetadataTemplate isEqualToMetadataTemplate:]
+ -[AVPlaybackUserInterfaceContentMetadataTemplate setArtworkRepresentations:]
+ -[AVPlaybackUserInterfaceContentMetadataTemplate setSubtitle:]
+ -[AVPlaybackUserInterfaceContentMetadataTemplate setTitle:]
+ -[AVPlaybackUserInterfaceContentMetadataTemplate setVideoProperties:]
+ -[AVPlaybackUserInterfaceContentMetadataTemplate subtitle]
+ -[AVPlaybackUserInterfaceContentMetadataTemplate title]
+ -[AVPlaybackUserInterfaceContentMetadataTemplate videoProperties]
+ -[AVPlaybackUserInterfaceContentURLArtwork .cxx_destruct]
+ -[AVPlaybackUserInterfaceContentURLArtwork contentType]
+ -[AVPlaybackUserInterfaceContentURLArtwork copyWithZone:]
+ -[AVPlaybackUserInterfaceContentURLArtwork encodeWithCoder:]
+ -[AVPlaybackUserInterfaceContentURLArtwork hash]
+ -[AVPlaybackUserInterfaceContentURLArtwork initWithCoder:]
+ -[AVPlaybackUserInterfaceContentURLArtwork initWithURL:contentType:size:]
+ -[AVPlaybackUserInterfaceContentURLArtwork isEqual:]
+ -[AVPlaybackUserInterfaceContentURLArtwork isEqualToContentURLArtwork:]
+ -[AVPlaybackUserInterfaceContentURLArtwork url]
+ -[AVPlaybackUserInterfaceContentVideoProperties copyWithZone:]
+ -[AVPlaybackUserInterfaceContentVideoProperties encodeWithCoder:]
+ -[AVPlaybackUserInterfaceContentVideoProperties hash]
+ -[AVPlaybackUserInterfaceContentVideoProperties initWithCoder:]
+ -[AVPlaybackUserInterfaceContentVideoProperties initWithPresentationSize:]
+ -[AVPlaybackUserInterfaceContentVideoProperties isEqual:]
+ -[AVPlaybackUserInterfaceContentVideoProperties isEqualToVideoProperties:]
+ -[AVPlaybackUserInterfaceContentVideoProperties presentationSize]
+ -[AVPlaybackUserInterfaceMediaSelectionOption .cxx_destruct]
+ -[AVPlaybackUserInterfaceMediaSelectionOption copyWithZone:]
+ -[AVPlaybackUserInterfaceMediaSelectionOption displayNameWithSymbolPlaceholder]
+ -[AVPlaybackUserInterfaceMediaSelectionOption displayName]
+ -[AVPlaybackUserInterfaceMediaSelectionOption encodeWithCoder:]
+ -[AVPlaybackUserInterfaceMediaSelectionOption extendedLanguageTag]
+ -[AVPlaybackUserInterfaceMediaSelectionOption hash]
+ -[AVPlaybackUserInterfaceMediaSelectionOption identifier]
+ -[AVPlaybackUserInterfaceMediaSelectionOption initWithCoder:]
+ -[AVPlaybackUserInterfaceMediaSelectionOption initWithDisplayName:identifier:extendedLanguageTag:mediaCharacteristics:]
+ -[AVPlaybackUserInterfaceMediaSelectionOption initWithDisplayName:identifier:extendedLanguageTag:mediaCharacteristics:mediaOptionSource:]
+ -[AVPlaybackUserInterfaceMediaSelectionOption initWithMediaOptionSource:extendedLanguageTag:]
+ -[AVPlaybackUserInterfaceMediaSelectionOption isAppleMachineGenerated]
+ -[AVPlaybackUserInterfaceMediaSelectionOption isAvailable]
+ -[AVPlaybackUserInterfaceMediaSelectionOption isEqual:]
+ -[AVPlaybackUserInterfaceMediaSelectionOption isEqualToTrackOption:]
+ -[AVPlaybackUserInterfaceMediaSelectionOption mediaCharacteristics]
+ -[AVPlaybackUserInterfaceMediaSelectionOption mediaOptionSource]
+ -[AVPlaybackUserInterfacePlaybackPosition copyWithZone:]
+ -[AVPlaybackUserInterfacePlaybackPosition encodeWithCoder:]
+ -[AVPlaybackUserInterfacePlaybackPosition hash]
+ -[AVPlaybackUserInterfacePlaybackPosition hostTime]
+ -[AVPlaybackUserInterfacePlaybackPosition initWithCoder:]
+ -[AVPlaybackUserInterfacePlaybackPosition initWithPosition:hostTime:rate:]
+ -[AVPlaybackUserInterfacePlaybackPosition isEqual:]
+ -[AVPlaybackUserInterfacePlaybackPosition isEqualToPlaybackPosition:]
+ -[AVPlaybackUserInterfacePlaybackPosition position]
+ -[AVPlaybackUserInterfacePlaybackPosition rate]
+ -[AVPlaybackUserInterfaceTimelineSegment .cxx_destruct]
+ -[AVPlaybackUserInterfaceTimelineSegment copyWithZone:]
+ -[AVPlaybackUserInterfaceTimelineSegment encodeWithCoder:]
+ -[AVPlaybackUserInterfaceTimelineSegment hash]
+ -[AVPlaybackUserInterfaceTimelineSegment identifier]
+ -[AVPlaybackUserInterfaceTimelineSegment initWithCoder:]
+ -[AVPlaybackUserInterfaceTimelineSegment initWithTimeRange:segmentType:marked:requiresLinearPlayback:identifier:]
+ -[AVPlaybackUserInterfaceTimelineSegment isEqual:]
+ -[AVPlaybackUserInterfaceTimelineSegment isEqualToTimelineSegment:]
+ -[AVPlaybackUserInterfaceTimelineSegment isMarked]
+ -[AVPlaybackUserInterfaceTimelineSegment requiresLinearPlayback]
+ -[AVPlaybackUserInterfaceTimelineSegment segmentType]
+ -[AVPlaybackUserInterfaceTimelineSegment timeRange]
+ -[AVPlayerViewControllerContentView stopObservations]
+ GCC_except_table1003
+ GCC_except_table1098
+ GCC_except_table1199
+ GCC_except_table1305
+ GCC_except_table1312
+ GCC_except_table1331
+ GCC_except_table1344
+ GCC_except_table1348
+ GCC_except_table1349
+ GCC_except_table1379
+ GCC_except_table1380
+ GCC_except_table1390
+ GCC_except_table1392
+ GCC_except_table1400
+ GCC_except_table1404
+ GCC_except_table1406
+ GCC_except_table1418
+ GCC_except_table1420
+ GCC_except_table1423
+ GCC_except_table1425
+ GCC_except_table1462
+ GCC_except_table1469
+ GCC_except_table1471
+ GCC_except_table1476
+ GCC_except_table1526
+ GCC_except_table1532
+ GCC_except_table1537
+ GCC_except_table1540
+ GCC_except_table1541
+ GCC_except_table1542
+ GCC_except_table1556
+ GCC_except_table1854
+ GCC_except_table1857
+ GCC_except_table1893
+ GCC_except_table1943
+ GCC_except_table2022
+ GCC_except_table2023
+ GCC_except_table2031
+ GCC_except_table2074
+ GCC_except_table2079
+ GCC_except_table2094
+ GCC_except_table2162
+ GCC_except_table2284
+ GCC_except_table2475
+ GCC_except_table2482
+ GCC_except_table2485
+ GCC_except_table2516
+ GCC_except_table2517
+ GCC_except_table2613
+ GCC_except_table2636
+ GCC_except_table2866
+ GCC_except_table3010
+ GCC_except_table3186
+ GCC_except_table3208
+ GCC_except_table3385
+ GCC_except_table3388
+ GCC_except_table3393
+ GCC_except_table3395
+ GCC_except_table3399
+ GCC_except_table3422
+ GCC_except_table3428
+ GCC_except_table3432
+ GCC_except_table3433
+ GCC_except_table3434
+ GCC_except_table3439
+ GCC_except_table3447
+ GCC_except_table3462
+ GCC_except_table3475
+ GCC_except_table3511
+ GCC_except_table3520
+ GCC_except_table3525
+ GCC_except_table3559
+ GCC_except_table3571
+ GCC_except_table3599
+ GCC_except_table3605
+ GCC_except_table3619
+ GCC_except_table3682
+ GCC_except_table3707
+ GCC_except_table3716
+ GCC_except_table3750
+ GCC_except_table3751
+ GCC_except_table3777
+ GCC_except_table3834
+ GCC_except_table3910
+ GCC_except_table3911
+ GCC_except_table3996
+ GCC_except_table4057
+ GCC_except_table4090
+ GCC_except_table4165
+ GCC_except_table4185
+ GCC_except_table4376
+ GCC_except_table4489
+ GCC_except_table4650
+ GCC_except_table5051
+ GCC_except_table5057
+ GCC_except_table5061
+ GCC_except_table5065
+ GCC_except_table5077
+ GCC_except_table5098
+ GCC_except_table5107
+ GCC_except_table5109
+ GCC_except_table5167
+ GCC_except_table5219
+ GCC_except_table5497
+ GCC_except_table5498
+ GCC_except_table5499
+ GCC_except_table5509
+ GCC_except_table5670
+ GCC_except_table5701
+ GCC_except_table5704
+ GCC_except_table5710
+ GCC_except_table5715
+ GCC_except_table5755
+ GCC_except_table5838
+ GCC_except_table6027
+ GCC_except_table6036
+ GCC_except_table6052
+ GCC_except_table6070
+ GCC_except_table6072
+ GCC_except_table6083
+ GCC_except_table6127
+ GCC_except_table6176
+ GCC_except_table6192
+ GCC_except_table6330
+ GCC_except_table6350
+ GCC_except_table6416
+ GCC_except_table6526
+ GCC_except_table6533
+ GCC_except_table6644
+ GCC_except_table6665
+ GCC_except_table6667
+ GCC_except_table670
+ GCC_except_table6775
+ GCC_except_table6804
+ GCC_except_table6805
+ GCC_except_table6839
+ GCC_except_table6841
+ GCC_except_table6961
+ GCC_except_table706
+ GCC_except_table7065
+ GCC_except_table708
+ GCC_except_table7144
+ GCC_except_table7148
+ GCC_except_table7160
+ GCC_except_table722
+ GCC_except_table7264
+ GCC_except_table7267
+ GCC_except_table7270
+ GCC_except_table7272
+ GCC_except_table7405
+ GCC_except_table7474
+ GCC_except_table7504
+ GCC_except_table7505
+ GCC_except_table7506
+ GCC_except_table7507
+ GCC_except_table7511
+ GCC_except_table7528
+ GCC_except_table7552
+ GCC_except_table7627
+ GCC_except_table7759
+ GCC_except_table7761
+ GCC_except_table7775
+ GCC_except_table782
+ GCC_except_table8008
+ GCC_except_table8014
+ GCC_except_table8153
+ GCC_except_table8175
+ GCC_except_table8300
+ GCC_except_table8307
+ GCC_except_table8321
+ GCC_except_table849
+ GCC_except_table8505
+ GCC_except_table8521
+ GCC_except_table8522
+ GCC_except_table8526
+ GCC_except_table8534
+ GCC_except_table8570
+ GCC_except_table8592
+ GCC_except_table8646
+ GCC_except_table979
+ OBJC_IVAR_$_AVMobileGlassVolumeControlsView._hasAppliedInitialSliderValue
+ OBJC_IVAR_$_AVPlaybackUserInterfaceContentArtwork._size
+ OBJC_IVAR_$_AVPlaybackUserInterfaceContentMetadata._artworkRepresentations
+ OBJC_IVAR_$_AVPlaybackUserInterfaceContentMetadata._subtitle
+ OBJC_IVAR_$_AVPlaybackUserInterfaceContentMetadata._title
+ OBJC_IVAR_$_AVPlaybackUserInterfaceContentMetadata._videoProperties
+ OBJC_IVAR_$_AVPlaybackUserInterfaceContentMetadataTemplate._artworkRepresentations
+ OBJC_IVAR_$_AVPlaybackUserInterfaceContentMetadataTemplate._subtitle
+ OBJC_IVAR_$_AVPlaybackUserInterfaceContentMetadataTemplate._title
+ OBJC_IVAR_$_AVPlaybackUserInterfaceContentMetadataTemplate._videoProperties
+ OBJC_IVAR_$_AVPlaybackUserInterfaceContentURLArtwork._contentType
+ OBJC_IVAR_$_AVPlaybackUserInterfaceContentURLArtwork._url
+ OBJC_IVAR_$_AVPlaybackUserInterfaceContentVideoProperties._presentationSize
+ OBJC_IVAR_$_AVPlaybackUserInterfaceMediaSelectionOption._displayName
+ OBJC_IVAR_$_AVPlaybackUserInterfaceMediaSelectionOption._extendedLanguageTag
+ OBJC_IVAR_$_AVPlaybackUserInterfaceMediaSelectionOption._identifier
+ OBJC_IVAR_$_AVPlaybackUserInterfaceMediaSelectionOption._mediaCharacteristics
+ OBJC_IVAR_$_AVPlaybackUserInterfaceMediaSelectionOption._mediaOptionSource
+ OBJC_IVAR_$_AVPlaybackUserInterfacePlaybackPosition._hostTime
+ OBJC_IVAR_$_AVPlaybackUserInterfacePlaybackPosition._position
+ OBJC_IVAR_$_AVPlaybackUserInterfacePlaybackPosition._rate
+ OBJC_IVAR_$_AVPlaybackUserInterfaceTimelineSegment._identifier
+ OBJC_IVAR_$_AVPlaybackUserInterfaceTimelineSegment._marked
+ OBJC_IVAR_$_AVPlaybackUserInterfaceTimelineSegment._requiresLinearPlayback
+ OBJC_IVAR_$_AVPlaybackUserInterfaceTimelineSegment._segmentType
+ OBJC_IVAR_$_AVPlaybackUserInterfaceTimelineSegment._timeRange
+ _OBJC_CLASS_$_AVPlaybackUserInterfaceContentArtwork
+ _OBJC_CLASS_$_AVPlaybackUserInterfaceContentMetadata
+ _OBJC_CLASS_$_AVPlaybackUserInterfaceContentMetadataTemplate
+ _OBJC_CLASS_$_AVPlaybackUserInterfaceContentURLArtwork
+ _OBJC_CLASS_$_AVPlaybackUserInterfaceContentVideoProperties
+ _OBJC_CLASS_$_AVPlaybackUserInterfaceMediaSelectionOption
+ _OBJC_CLASS_$_AVPlaybackUserInterfacePlaybackPosition
+ _OBJC_CLASS_$_AVPlaybackUserInterfaceTimelineSegment
+ _OBJC_CLASS_$_UISceneAccessory
+ _OBJC_METACLASS_$_AVPlaybackUserInterfaceContentArtwork
+ _OBJC_METACLASS_$_AVPlaybackUserInterfaceContentMetadata
+ _OBJC_METACLASS_$_AVPlaybackUserInterfaceContentMetadataTemplate
+ _OBJC_METACLASS_$_AVPlaybackUserInterfaceContentURLArtwork
+ _OBJC_METACLASS_$_AVPlaybackUserInterfaceContentVideoProperties
+ _OBJC_METACLASS_$_AVPlaybackUserInterfaceMediaSelectionOption
+ _OBJC_METACLASS_$_AVPlaybackUserInterfacePlaybackPosition
+ _OBJC_METACLASS_$_AVPlaybackUserInterfaceTimelineSegment
+ __OBJC_$_CLASS_METHODS_AVPlaybackUserInterfaceContentArtwork
+ __OBJC_$_CLASS_METHODS_AVPlaybackUserInterfaceContentMetadata
+ __OBJC_$_CLASS_METHODS_AVPlaybackUserInterfaceContentMetadataTemplate
+ __OBJC_$_CLASS_METHODS_AVPlaybackUserInterfaceContentURLArtwork
+ __OBJC_$_CLASS_METHODS_AVPlaybackUserInterfaceContentVideoProperties
+ __OBJC_$_CLASS_METHODS_AVPlaybackUserInterfaceMediaSelectionOption
+ __OBJC_$_CLASS_METHODS_AVPlaybackUserInterfacePlaybackPosition
+ __OBJC_$_CLASS_METHODS_AVPlaybackUserInterfaceTimelineSegment
+ __OBJC_$_CLASS_PROP_LIST_AVPlaybackUserInterfaceContentArtwork
+ __OBJC_$_CLASS_PROP_LIST_AVPlaybackUserInterfaceContentMetadata
+ __OBJC_$_CLASS_PROP_LIST_AVPlaybackUserInterfaceContentMetadataTemplate
+ __OBJC_$_CLASS_PROP_LIST_AVPlaybackUserInterfaceContentVideoProperties
+ __OBJC_$_CLASS_PROP_LIST_AVPlaybackUserInterfaceMediaSelectionOption
+ __OBJC_$_CLASS_PROP_LIST_AVPlaybackUserInterfacePlaybackPosition
+ __OBJC_$_CLASS_PROP_LIST_AVPlaybackUserInterfaceTimelineSegment
+ __OBJC_$_INSTANCE_METHODS_AVPlaybackUserInterfaceContentArtwork
+ __OBJC_$_INSTANCE_METHODS_AVPlaybackUserInterfaceContentMetadata
+ __OBJC_$_INSTANCE_METHODS_AVPlaybackUserInterfaceContentMetadataTemplate
+ __OBJC_$_INSTANCE_METHODS_AVPlaybackUserInterfaceContentURLArtwork
+ __OBJC_$_INSTANCE_METHODS_AVPlaybackUserInterfaceContentVideoProperties
+ __OBJC_$_INSTANCE_METHODS_AVPlaybackUserInterfaceMediaSelectionOption
+ __OBJC_$_INSTANCE_METHODS_AVPlaybackUserInterfacePlaybackPosition
+ __OBJC_$_INSTANCE_METHODS_AVPlaybackUserInterfaceTimelineSegment
+ __OBJC_$_INSTANCE_VARIABLES_AVPlaybackUserInterfaceContentArtwork
+ __OBJC_$_INSTANCE_VARIABLES_AVPlaybackUserInterfaceContentMetadata
+ __OBJC_$_INSTANCE_VARIABLES_AVPlaybackUserInterfaceContentMetadataTemplate
+ __OBJC_$_INSTANCE_VARIABLES_AVPlaybackUserInterfaceContentURLArtwork
+ __OBJC_$_INSTANCE_VARIABLES_AVPlaybackUserInterfaceContentVideoProperties
+ __OBJC_$_INSTANCE_VARIABLES_AVPlaybackUserInterfaceMediaSelectionOption
+ __OBJC_$_INSTANCE_VARIABLES_AVPlaybackUserInterfacePlaybackPosition
+ __OBJC_$_INSTANCE_VARIABLES_AVPlaybackUserInterfaceTimelineSegment
+ __OBJC_$_PROP_LIST_AVPlaybackUserInterfaceContentArtwork
+ __OBJC_$_PROP_LIST_AVPlaybackUserInterfaceContentMetadata
+ __OBJC_$_PROP_LIST_AVPlaybackUserInterfaceContentMetadataTemplate
+ __OBJC_$_PROP_LIST_AVPlaybackUserInterfaceContentURLArtwork
+ __OBJC_$_PROP_LIST_AVPlaybackUserInterfaceContentVideoProperties
+ __OBJC_$_PROP_LIST_AVPlaybackUserInterfaceMediaSelectionOption
+ __OBJC_$_PROP_LIST_AVPlaybackUserInterfacePlaybackPosition
+ __OBJC_$_PROP_LIST_AVPlaybackUserInterfaceTimelineSegment
+ __OBJC_CLASS_PROTOCOLS_$_AVPlaybackUserInterfaceContentArtwork
+ __OBJC_CLASS_PROTOCOLS_$_AVPlaybackUserInterfaceContentMetadata
+ __OBJC_CLASS_PROTOCOLS_$_AVPlaybackUserInterfaceContentMetadataTemplate
+ __OBJC_CLASS_PROTOCOLS_$_AVPlaybackUserInterfaceContentVideoProperties
+ __OBJC_CLASS_PROTOCOLS_$_AVPlaybackUserInterfaceMediaSelectionOption
+ __OBJC_CLASS_PROTOCOLS_$_AVPlaybackUserInterfacePlaybackPosition
+ __OBJC_CLASS_PROTOCOLS_$_AVPlaybackUserInterfaceTimelineSegment
+ __OBJC_CLASS_RO_$_AVPlaybackUserInterfaceContentArtwork
+ __OBJC_CLASS_RO_$_AVPlaybackUserInterfaceContentMetadata
+ __OBJC_CLASS_RO_$_AVPlaybackUserInterfaceContentMetadataTemplate
+ __OBJC_CLASS_RO_$_AVPlaybackUserInterfaceContentURLArtwork
+ __OBJC_CLASS_RO_$_AVPlaybackUserInterfaceContentVideoProperties
+ __OBJC_CLASS_RO_$_AVPlaybackUserInterfaceMediaSelectionOption
+ __OBJC_CLASS_RO_$_AVPlaybackUserInterfacePlaybackPosition
+ __OBJC_CLASS_RO_$_AVPlaybackUserInterfaceTimelineSegment
+ __OBJC_METACLASS_RO_$_AVPlaybackUserInterfaceContentArtwork
+ __OBJC_METACLASS_RO_$_AVPlaybackUserInterfaceContentMetadata
+ __OBJC_METACLASS_RO_$_AVPlaybackUserInterfaceContentMetadataTemplate
+ __OBJC_METACLASS_RO_$_AVPlaybackUserInterfaceContentURLArtwork
+ __OBJC_METACLASS_RO_$_AVPlaybackUserInterfaceContentVideoProperties
+ __OBJC_METACLASS_RO_$_AVPlaybackUserInterfaceMediaSelectionOption
+ __OBJC_METACLASS_RO_$_AVPlaybackUserInterfacePlaybackPosition
+ __OBJC_METACLASS_RO_$_AVPlaybackUserInterfaceTimelineSegment
+ ___block_descriptor_33_e39_B16?0"AVMobileGlassAuxiliaryControl"8l
+ ___swift_memcpy64_8
+ __swift_closure_destructor.107Tm
+ __swift_closure_destructor.53Tm
+ _associated conformance 5AVKit38AVPlaybackUserInterfaceContentMetadataV15VideoPropertiesVSHAASQ
+ _associated conformance 5AVKit38AVPlaybackUserInterfaceContentMetadataVSHAASQ
+ _associated conformance So21AVMediaCharacteristicaSHSCSQ
+ _associated conformance So21AVMediaCharacteristicas20_SwiftNewtypeWrapperSCSY
+ _associated conformance So21AVMediaCharacteristicas20_SwiftNewtypeWrapperSCs35_HasCustomAnyHashableRepresentation
+ _objc_msgSend$artworkRepresentations
+ _objc_msgSend$decodeFloatForKey:
+ _objc_msgSend$encodeFloat:forKey:
+ _objc_msgSend$externalNonInteractiveSceneAccessoryWithConfiguration:
+ _objc_msgSend$hostTime
+ _objc_msgSend$initWithDisplayName:identifier:extendedLanguageTag:mediaCharacteristics:
+ _objc_msgSend$initWithDisplayName:identifier:extendedLanguageTag:mediaCharacteristics:mediaOptionSource:
+ _objc_msgSend$initWithPosition:hostTime:rate:
+ _objc_msgSend$initWithPresentationSize:
+ _objc_msgSend$initWithTimeRange:segmentType:marked:requiresLinearPlayback:identifier:
+ _objc_msgSend$initWithVideoProperties:title:subtitle:artworkRepresentations:
+ _objc_msgSend$isEqualToContentArtwork:
+ _objc_msgSend$isEqualToContentURLArtwork:
+ _objc_msgSend$isEqualToPlaybackPosition:
+ _objc_msgSend$isEqualToTrackOption:
+ _objc_msgSend$isEqualToVideoProperties:
+ _objc_msgSend$layoutUsingBarInsets
+ _objc_msgSend$mediaCharacteristics
+ _objc_msgSend$registerSceneAccessory:
+ _objc_msgSend$segmentType
+ _objc_msgSend$setArtworkRepresentations:
+ _objc_msgSend$setVideoProperties:
+ _objc_msgSend$stopObservations
+ _objc_msgSend$videoProperties
+ _symbolic $s5AVKit35AVPlaybackUserInterfaceControllableP
+ _symbolic $s5AVKit37AVPlaybackUserInterfaceVideoProvidingP
+ _symbolic $s5AVKit39AVPlaybackUserInterfaceTimeControllableP
+ _symbolic $s5AVKit40AVPlaybackUserInterfaceMetadataProvidingP
+ _symbolic $s5AVKit41AVPlaybackUserInterfaceVolumeControllableP
+ _symbolic $s5AVKit43AVPlaybackUserInterfacePlaybackControllableP
+ _symbolic $s5AVKit44AVPlaybackUserInterfaceThumbnailControllableP
+ _symbolic $s5AVKit49AVPlaybackUserInterfaceMediaSelectionControllableP
+ _symbolic SaySo37AVPlaybackUserInterfaceContentArtworkCG
+ _symbolic _____ 5AVKit38AVPlaybackUserInterfaceContentMetadataV
+ _symbolic _____ 5AVKit38AVPlaybackUserInterfaceContentMetadataV15VideoPropertiesV
+ _symbolic _____ So21AVMediaCharacteristica
+ _symbolic _____Sg 5AVKit38AVPlaybackUserInterfaceContentMetadataV15VideoPropertiesV
+ _type_layout_string 5AVKit38AVPlaybackUserInterfaceContentMetadataV
+ _type_layout_string 5AVKit38AVPlaybackUserInterfaceContentMetadataV15VideoPropertiesV
- GCC_except_table1094
- GCC_except_table1121
- GCC_except_table1134
- GCC_except_table1200
- GCC_except_table1207
- GCC_except_table1215
- GCC_except_table1243
- GCC_except_table1244
- GCC_except_table1274
- GCC_except_table1275
- GCC_except_table1285
- GCC_except_table1287
- GCC_except_table1295
- GCC_except_table1299
- GCC_except_table1301
- GCC_except_table1313
- GCC_except_table1315
- GCC_except_table1318
- GCC_except_table1357
- GCC_except_table1364
- GCC_except_table1366
- GCC_except_table1371
- GCC_except_table1421
- GCC_except_table1427
- GCC_except_table1432
- GCC_except_table1435
- GCC_except_table1436
- GCC_except_table1437
- GCC_except_table1451
- GCC_except_table1749
- GCC_except_table1752
- GCC_except_table1788
- GCC_except_table1838
- GCC_except_table1917
- GCC_except_table1918
- GCC_except_table1926
- GCC_except_table1969
- GCC_except_table1974
- GCC_except_table1989
- GCC_except_table2057
- GCC_except_table2179
- GCC_except_table2370
- GCC_except_table2377
- GCC_except_table2380
- GCC_except_table2411
- GCC_except_table2412
- GCC_except_table2508
- GCC_except_table2531
- GCC_except_table2761
- GCC_except_table2905
- GCC_except_table3081
- GCC_except_table3103
- GCC_except_table3280
- GCC_except_table3283
- GCC_except_table3288
- GCC_except_table3290
- GCC_except_table3294
- GCC_except_table3317
- GCC_except_table3323
- GCC_except_table3327
- GCC_except_table3328
- GCC_except_table3329
- GCC_except_table3334
- GCC_except_table3342
- GCC_except_table3357
- GCC_except_table3370
- GCC_except_table3406
- GCC_except_table3415
- GCC_except_table3420
- GCC_except_table3454
- GCC_except_table3466
- GCC_except_table3494
- GCC_except_table3500
- GCC_except_table3514
- GCC_except_table3577
- GCC_except_table3602
- GCC_except_table3611
- GCC_except_table3645
- GCC_except_table3646
- GCC_except_table3672
- GCC_except_table3729
- GCC_except_table3805
- GCC_except_table3806
- GCC_except_table3891
- GCC_except_table3952
- GCC_except_table3985
- GCC_except_table4060
- GCC_except_table4080
- GCC_except_table4271
- GCC_except_table4384
- GCC_except_table4545
- GCC_except_table4946
- GCC_except_table4952
- GCC_except_table4956
- GCC_except_table4960
- GCC_except_table4972
- GCC_except_table4993
- GCC_except_table5002
- GCC_except_table5004
- GCC_except_table5062
- GCC_except_table5114
- GCC_except_table5392
- GCC_except_table5393
- GCC_except_table5394
- GCC_except_table5404
- GCC_except_table5565
- GCC_except_table5596
- GCC_except_table5599
- GCC_except_table5605
- GCC_except_table5610
- GCC_except_table565
- GCC_except_table5650
- GCC_except_table5733
- GCC_except_table5922
- GCC_except_table5931
- GCC_except_table5947
- GCC_except_table5965
- GCC_except_table5967
- GCC_except_table5978
- GCC_except_table601
- GCC_except_table6022
- GCC_except_table603
- GCC_except_table6071
- GCC_except_table6087
- GCC_except_table617
- GCC_except_table6225
- GCC_except_table6245
- GCC_except_table6311
- GCC_except_table6421
- GCC_except_table6428
- GCC_except_table6539
- GCC_except_table6560
- GCC_except_table6562
- GCC_except_table6670
- GCC_except_table6699
- GCC_except_table6700
- GCC_except_table6734
- GCC_except_table6736
- GCC_except_table677
- GCC_except_table6856
- GCC_except_table6960
- GCC_except_table7039
- GCC_except_table7043
- GCC_except_table7055
- GCC_except_table7159
- GCC_except_table7162
- GCC_except_table7165
- GCC_except_table7167
- GCC_except_table7300
- GCC_except_table7369
- GCC_except_table7399
- GCC_except_table7400
- GCC_except_table7401
- GCC_except_table7402
- GCC_except_table7406
- GCC_except_table7421
- GCC_except_table744
- GCC_except_table7445
- GCC_except_table7519
- GCC_except_table7651
- GCC_except_table7653
- GCC_except_table7667
- GCC_except_table7900
- GCC_except_table7906
- GCC_except_table8045
- GCC_except_table8067
- GCC_except_table8192
- GCC_except_table8199
- GCC_except_table8213
- GCC_except_table8397
- GCC_except_table8413
- GCC_except_table8414
- GCC_except_table8418
- GCC_except_table8426
- GCC_except_table8462
- GCC_except_table8484
- GCC_except_table8538
- GCC_except_table874
- GCC_except_table898
- GCC_except_table993
- _OBJC_CLASS_$__UISceneCompanion
- ___block_descriptor_32_e39_B16?0"AVMobileGlassAuxiliaryControl"8l
- __os_log_fault_impl
- __swift_closure_destructor.57Tm
- _keypath_get_selector_hasSeekableLiveStreamingContent
- _objc_msgSend$_registerSceneCompanion:
- _objc_msgSend$externalNonInteractiveCompanionWithConfiguration:
CStrings:
+ "artworkRepresentations"
+ "hostTime.timescale"
+ "hostTime.value"
+ "mediaCharacteristics"
+ "position.timescale"
+ "position.value"
+ "segmentType"
+ "videoProperties"
- "Transport controls frame is smaller than desired during content tab presenting animation. Aux controls will compress and produce a wrong frame that UIKit animates from when controls reappear."
- "\xc1"

```
