## SearchFoundation

> `/System/Library/PrivateFrameworks/SearchFoundation.framework/SearchFoundation`

```diff

-3303.5.1.0.0
-  __TEXT.__text: 0x2c71fc
+3304.72.1.0.0
+  __TEXT.__text: 0x3039fc
   __TEXT.__auth_stubs: 0x5a0
-  __TEXT.__objc_methlist: 0x2a858
+  __TEXT.__objc_methlist: 0x2da00
   __TEXT.__const: 0x68
   __TEXT.__gcc_except_tab: 0x38
-  __TEXT.__cstring: 0x52c8
+  __TEXT.__cstring: 0x578f
   __TEXT.__oslogstring: 0x17c
   __TEXT.__dlopen_cstrs: 0x52
-  __TEXT.__unwind_info: 0x6da0
-  __TEXT.__objc_classname: 0x3a0b
-  __TEXT.__objc_methname: 0x239a3
-  __TEXT.__objc_methtype: 0xc0c1
-  __TEXT.__objc_stubs: 0x13980
+  __TEXT.__unwind_info: 0x75e0
+  __TEXT.__objc_classname: 0x3f79
+  __TEXT.__objc_methname: 0x25e43
+  __TEXT.__objc_methtype: 0xd458
+  __TEXT.__objc_stubs: 0x14900
   __DATA_CONST.__got: 0x40
-  __DATA_CONST.__const: 0x978
-  __DATA_CONST.__objc_classlist: 0x1398
+  __DATA_CONST.__const: 0xa28
+  __DATA_CONST.__objc_classlist: 0x1508
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x1250
+  __DATA_CONST.__objc_protolist: 0x13c0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xa8a80
-  __DATA_CONST.__objc_selrefs: 0x5cf0
-  __AUTH_CONST.__objc_const: 0x10d20
+  __DATA_CONST.__objc_const: 0xb5eb0
+  __DATA_CONST.__objc_selrefs: 0x6110
+  __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_classrefs: 0x14c8
+  __DATA_CONST.__objc_superrefs: 0x1b60
+  __AUTH_CONST.__objc_const: 0x12088
+  __AUTH_CONST.__cfstring: 0xae40
   __AUTH_CONST.__const: 0xc0
-  __AUTH_CONST.__cfstring: 0xa580
   __AUTH_CONST.__auth_got: 0x2e0
-  __AUTH.__objc_data: 0x9880
-  __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x1360
-  __DATA.__objc_superrefs: 0x1950
-  __DATA.__objc_ivar: 0x361c
-  __DATA.__data: 0xdbf0
+  __AUTH.__objc_data: 0xa6e0
+  __DATA.__objc_ivar: 0x3a10
+  __DATA.__data: 0xed30
   __DATA.__bss: 0xa0
   __DATA_DIRTY.__objc_data: 0x2b70
   __DATA_DIRTY.__bss: 0x20

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: DB92C90C-1B90-362A-BA80-5FD8F27AE4DB
-  Functions: 14179
-  Symbols:   43265
-  CStrings:  11005
+  UUID: B4E5E93F-13DB-35EE-B6ED-C4932702E48D
+  Functions: 15215
+  Symbols:   46382
+  CStrings:  11617
 
Symbols:
+ +[RFBinaryButtonCardSection supportsSecureCoding]
+ +[RFButtonCardSection supportsSecureCoding]
+ +[RFFont supportsSecureCoding]
+ +[RFPrimaryHeaderStackedImageCardSection supportsSecureCoding]
+ +[RFReferenceCenteredCardSection supportsSecureCoding]
+ +[RFReferenceItemButtonCardSection supportsSecureCoding]
+ +[RFReferenceItemLogoCardSection supportsSecureCoding]
+ +[RFSecondaryHeaderEmphasizedCardSection supportsSecureCoding]
+ +[RFSecondaryHeaderStandardCardSection supportsSecureCoding]
+ +[RFSimpleItemReverseRichCardSection supportsSecureCoding]
+ +[RFSimpleItemRichSearchResultCardSection supportsSecureCoding]
+ +[RFSimpleItemVisualElementCardSection supportsSecureCoding]
+ +[RFSummaryItemButtonCardSection supportsSecureCoding]
+ +[RFSummaryItemImageRightCardSection supportsSecureCoding]
+ +[RFSummaryItemPlayerCardSection supportsSecureCoding]
+ +[RFSystemFont supportsSecureCoding]
+ +[SFHashBucketDetail supportsSecureCoding]
+ +[SFHashDetail supportsSecureCoding]
+ +[SFPlayAudioButtonItem supportsSecureCoding]
+ +[SFPlayWatchListItemButtonItem supportsSecureCoding]
+ +[SFRequestProductPageCommand supportsSecureCoding]
+ +[SFShortcutsImage supportsSecureCoding]
+ +[SFStoreButtonItem supportsSecureCoding]
+ -[RFBinaryButtonCardSection .cxx_destruct]
+ -[RFBinaryButtonCardSection copyWithZone:]
+ -[RFBinaryButtonCardSection dictionaryRepresentation]
+ -[RFBinaryButtonCardSection encodeWithCoder:]
+ -[RFBinaryButtonCardSection hash]
+ -[RFBinaryButtonCardSection initWithCoder:]
+ -[RFBinaryButtonCardSection isEqual:]
+ -[RFBinaryButtonCardSection jsonData]
+ -[RFBinaryButtonCardSection primary_button]
+ -[RFBinaryButtonCardSection secondary_button]
+ -[RFBinaryButtonCardSection setPrimary_button:]
+ -[RFBinaryButtonCardSection setSecondary_button:]
+ -[RFBinaryButtonCardSection(ProtobufInitializer) initWithProtobuf:]
+ -[RFButtonCardSection .cxx_destruct]
+ -[RFButtonCardSection button]
+ -[RFButtonCardSection copyWithZone:]
+ -[RFButtonCardSection dictionaryRepresentation]
+ -[RFButtonCardSection encodeWithCoder:]
+ -[RFButtonCardSection hash]
+ -[RFButtonCardSection initWithCoder:]
+ -[RFButtonCardSection isEqual:]
+ -[RFButtonCardSection jsonData]
+ -[RFButtonCardSection setButton:]
+ -[RFButtonCardSection(ProtobufInitializer) initWithProtobuf:]
+ -[RFFactItemButtonCardSection buttonItemsAreBottom]
+ -[RFFactItemButtonCardSection hasButtonItemsAreBottom]
+ -[RFFactItemButtonCardSection setButtonItemsAreBottom:]
+ -[RFFactItemButtonCardSection setThumbnail2:]
+ -[RFFactItemButtonCardSection thumbnail2]
+ -[RFFactItemStandardCardSection setThumbnail2:]
+ -[RFFactItemStandardCardSection thumbnail2]
+ -[RFFont .cxx_destruct]
+ -[RFFont copyWithZone:]
+ -[RFFont dictionaryRepresentation]
+ -[RFFont encodeWithCoder:]
+ -[RFFont hasName]
+ -[RFFont hasSystem]
+ -[RFFont hash]
+ -[RFFont initWithCoder:]
+ -[RFFont isEqual:]
+ -[RFFont jsonData]
+ -[RFFont name]
+ -[RFFont setName:]
+ -[RFFont setSystem:]
+ -[RFFont system]
+ -[RFFont(ProtobufInitializer) initWithProtobuf:]
+ -[RFFormattedText font]
+ -[RFFormattedText setFont:]
+ -[RFPrimaryHeaderMarqueeCardSection addTint]
+ -[RFPrimaryHeaderMarqueeCardSection hasAddTint]
+ -[RFPrimaryHeaderMarqueeCardSection setAddTint:]
+ -[RFPrimaryHeaderRichCardSection addTint]
+ -[RFPrimaryHeaderRichCardSection hasAddTint]
+ -[RFPrimaryHeaderRichCardSection setAddTint:]
+ -[RFPrimaryHeaderStackedImageCardSection .cxx_destruct]
+ -[RFPrimaryHeaderStackedImageCardSection copyWithZone:]
+ -[RFPrimaryHeaderStackedImageCardSection dictionaryRepresentation]
+ -[RFPrimaryHeaderStackedImageCardSection encodeWithCoder:]
+ -[RFPrimaryHeaderStackedImageCardSection hash]
+ -[RFPrimaryHeaderStackedImageCardSection images]
+ -[RFPrimaryHeaderStackedImageCardSection initWithCoder:]
+ -[RFPrimaryHeaderStackedImageCardSection isEqual:]
+ -[RFPrimaryHeaderStackedImageCardSection jsonData]
+ -[RFPrimaryHeaderStackedImageCardSection setImages:]
+ -[RFPrimaryHeaderStackedImageCardSection setText_1:]
+ -[RFPrimaryHeaderStackedImageCardSection setText_2:]
+ -[RFPrimaryHeaderStackedImageCardSection text_1]
+ -[RFPrimaryHeaderStackedImageCardSection text_2]
+ -[RFPrimaryHeaderStackedImageCardSection(ProtobufInitializer) initWithProtobuf:]
+ -[RFPrimaryHeaderStandardCardSection addTint]
+ -[RFPrimaryHeaderStandardCardSection hasAddTint]
+ -[RFPrimaryHeaderStandardCardSection setAddTint:]
+ -[RFReferenceCenteredCardSection .cxx_destruct]
+ -[RFReferenceCenteredCardSection add_tint]
+ -[RFReferenceCenteredCardSection copyWithZone:]
+ -[RFReferenceCenteredCardSection dictionaryRepresentation]
+ -[RFReferenceCenteredCardSection encodeWithCoder:]
+ -[RFReferenceCenteredCardSection hasAdd_tint]
+ -[RFReferenceCenteredCardSection hash]
+ -[RFReferenceCenteredCardSection initWithCoder:]
+ -[RFReferenceCenteredCardSection isEqual:]
+ -[RFReferenceCenteredCardSection jsonData]
+ -[RFReferenceCenteredCardSection setAdd_tint:]
+ -[RFReferenceCenteredCardSection setText_1:]
+ -[RFReferenceCenteredCardSection setText_2:]
+ -[RFReferenceCenteredCardSection setText_3:]
+ -[RFReferenceCenteredCardSection setText_4:]
+ -[RFReferenceCenteredCardSection text_1]
+ -[RFReferenceCenteredCardSection text_2]
+ -[RFReferenceCenteredCardSection text_3]
+ -[RFReferenceCenteredCardSection text_4]
+ -[RFReferenceCenteredCardSection(ProtobufInitializer) initWithProtobuf:]
+ -[RFReferenceFootnoteCardSection addTint]
+ -[RFReferenceFootnoteCardSection hasAddTint]
+ -[RFReferenceFootnoteCardSection setAddTint:]
+ -[RFReferenceItemButtonCardSection .cxx_destruct]
+ -[RFReferenceItemButtonCardSection button_1]
+ -[RFReferenceItemButtonCardSection copyWithZone:]
+ -[RFReferenceItemButtonCardSection dictionaryRepresentation]
+ -[RFReferenceItemButtonCardSection encodeWithCoder:]
+ -[RFReferenceItemButtonCardSection hash]
+ -[RFReferenceItemButtonCardSection initWithCoder:]
+ -[RFReferenceItemButtonCardSection isEqual:]
+ -[RFReferenceItemButtonCardSection jsonData]
+ -[RFReferenceItemButtonCardSection setButton_1:]
+ -[RFReferenceItemButtonCardSection(ProtobufInitializer) initWithProtobuf:]
+ -[RFReferenceItemLogoCardSection .cxx_destruct]
+ -[RFReferenceItemLogoCardSection copyWithZone:]
+ -[RFReferenceItemLogoCardSection dictionaryRepresentation]
+ -[RFReferenceItemLogoCardSection encodeWithCoder:]
+ -[RFReferenceItemLogoCardSection hash]
+ -[RFReferenceItemLogoCardSection initWithCoder:]
+ -[RFReferenceItemLogoCardSection isEqual:]
+ -[RFReferenceItemLogoCardSection jsonData]
+ -[RFReferenceItemLogoCardSection setThumbnail:]
+ -[RFReferenceItemLogoCardSection thumbnail]
+ -[RFReferenceItemLogoCardSection(ProtobufInitializer) initWithProtobuf:]
+ -[RFReferenceRichCardSection addTint]
+ -[RFReferenceRichCardSection hasAddTint]
+ -[RFReferenceRichCardSection setAddTint:]
+ -[RFReferenceStandardCardSection addTint]
+ -[RFReferenceStandardCardSection hasAddTint]
+ -[RFReferenceStandardCardSection setAddTint:]
+ -[RFSecondaryHeaderEmphasizedCardSection .cxx_destruct]
+ -[RFSecondaryHeaderEmphasizedCardSection copyWithZone:]
+ -[RFSecondaryHeaderEmphasizedCardSection dictionaryRepresentation]
+ -[RFSecondaryHeaderEmphasizedCardSection encodeWithCoder:]
+ -[RFSecondaryHeaderEmphasizedCardSection hash]
+ -[RFSecondaryHeaderEmphasizedCardSection initWithCoder:]
+ -[RFSecondaryHeaderEmphasizedCardSection isEqual:]
+ -[RFSecondaryHeaderEmphasizedCardSection jsonData]
+ -[RFSecondaryHeaderEmphasizedCardSection setText_1:]
+ -[RFSecondaryHeaderEmphasizedCardSection text_1]
+ -[RFSecondaryHeaderEmphasizedCardSection(ProtobufInitializer) initWithProtobuf:]
+ -[RFSecondaryHeaderStandardCardSection .cxx_destruct]
+ -[RFSecondaryHeaderStandardCardSection copyWithZone:]
+ -[RFSecondaryHeaderStandardCardSection dictionaryRepresentation]
+ -[RFSecondaryHeaderStandardCardSection encodeWithCoder:]
+ -[RFSecondaryHeaderStandardCardSection hash]
+ -[RFSecondaryHeaderStandardCardSection initWithCoder:]
+ -[RFSecondaryHeaderStandardCardSection isEqual:]
+ -[RFSecondaryHeaderStandardCardSection jsonData]
+ -[RFSecondaryHeaderStandardCardSection setText_1:]
+ -[RFSecondaryHeaderStandardCardSection text_1]
+ -[RFSecondaryHeaderStandardCardSection(ProtobufInitializer) initWithProtobuf:]
+ -[RFSimpleItemReverseRichCardSection .cxx_destruct]
+ -[RFSimpleItemReverseRichCardSection copyWithZone:]
+ -[RFSimpleItemReverseRichCardSection dictionaryRepresentation]
+ -[RFSimpleItemReverseRichCardSection encodeWithCoder:]
+ -[RFSimpleItemReverseRichCardSection hash]
+ -[RFSimpleItemReverseRichCardSection initWithCoder:]
+ -[RFSimpleItemReverseRichCardSection isEqual:]
+ -[RFSimpleItemReverseRichCardSection jsonData]
+ -[RFSimpleItemReverseRichCardSection setText_1:]
+ -[RFSimpleItemReverseRichCardSection setText_2:]
+ -[RFSimpleItemReverseRichCardSection setText_3:]
+ -[RFSimpleItemReverseRichCardSection setText_4:]
+ -[RFSimpleItemReverseRichCardSection setThumbnail:]
+ -[RFSimpleItemReverseRichCardSection text_1]
+ -[RFSimpleItemReverseRichCardSection text_2]
+ -[RFSimpleItemReverseRichCardSection text_3]
+ -[RFSimpleItemReverseRichCardSection text_4]
+ -[RFSimpleItemReverseRichCardSection thumbnail]
+ -[RFSimpleItemReverseRichCardSection(ProtobufInitializer) initWithProtobuf:]
+ -[RFSimpleItemRichSearchResultCardSection .cxx_destruct]
+ -[RFSimpleItemRichSearchResultCardSection copyWithZone:]
+ -[RFSimpleItemRichSearchResultCardSection dictionaryRepresentation]
+ -[RFSimpleItemRichSearchResultCardSection encodeWithCoder:]
+ -[RFSimpleItemRichSearchResultCardSection hash]
+ -[RFSimpleItemRichSearchResultCardSection initWithCoder:]
+ -[RFSimpleItemRichSearchResultCardSection isEqual:]
+ -[RFSimpleItemRichSearchResultCardSection jsonData]
+ -[RFSimpleItemRichSearchResultCardSection setText_1:]
+ -[RFSimpleItemRichSearchResultCardSection setText_2:]
+ -[RFSimpleItemRichSearchResultCardSection setText_3:]
+ -[RFSimpleItemRichSearchResultCardSection setText_4:]
+ -[RFSimpleItemRichSearchResultCardSection setText_5:]
+ -[RFSimpleItemRichSearchResultCardSection setText_6:]
+ -[RFSimpleItemRichSearchResultCardSection setText_7:]
+ -[RFSimpleItemRichSearchResultCardSection setText_8:]
+ -[RFSimpleItemRichSearchResultCardSection setThumbnail:]
+ -[RFSimpleItemRichSearchResultCardSection text_1]
+ -[RFSimpleItemRichSearchResultCardSection text_2]
+ -[RFSimpleItemRichSearchResultCardSection text_3]
+ -[RFSimpleItemRichSearchResultCardSection text_4]
+ -[RFSimpleItemRichSearchResultCardSection text_5]
+ -[RFSimpleItemRichSearchResultCardSection text_6]
+ -[RFSimpleItemRichSearchResultCardSection text_7]
+ -[RFSimpleItemRichSearchResultCardSection text_8]
+ -[RFSimpleItemRichSearchResultCardSection thumbnail]
+ -[RFSimpleItemRichSearchResultCardSection(ProtobufInitializer) initWithProtobuf:]
+ -[RFSimpleItemVisualElementCardSection .cxx_destruct]
+ -[RFSimpleItemVisualElementCardSection copyWithZone:]
+ -[RFSimpleItemVisualElementCardSection dictionaryRepresentation]
+ -[RFSimpleItemVisualElementCardSection encodeWithCoder:]
+ -[RFSimpleItemVisualElementCardSection footnote]
+ -[RFSimpleItemVisualElementCardSection hasHorizontal_alignment]
+ -[RFSimpleItemVisualElementCardSection hash]
+ -[RFSimpleItemVisualElementCardSection horizontal_alignment]
+ -[RFSimpleItemVisualElementCardSection image]
+ -[RFSimpleItemVisualElementCardSection initWithCoder:]
+ -[RFSimpleItemVisualElementCardSection isEqual:]
+ -[RFSimpleItemVisualElementCardSection jsonData]
+ -[RFSimpleItemVisualElementCardSection setFootnote:]
+ -[RFSimpleItemVisualElementCardSection setHorizontal_alignment:]
+ -[RFSimpleItemVisualElementCardSection setImage:]
+ -[RFSimpleItemVisualElementCardSection setText_1:]
+ -[RFSimpleItemVisualElementCardSection setText_2:]
+ -[RFSimpleItemVisualElementCardSection text_1]
+ -[RFSimpleItemVisualElementCardSection text_2]
+ -[RFSimpleItemVisualElementCardSection(ProtobufInitializer) initWithProtobuf:]
+ -[RFSummaryItemButtonCardSection .cxx_destruct]
+ -[RFSummaryItemButtonCardSection buttonItemsAreTrailing]
+ -[RFSummaryItemButtonCardSection button_1]
+ -[RFSummaryItemButtonCardSection button_2]
+ -[RFSummaryItemButtonCardSection button_3]
+ -[RFSummaryItemButtonCardSection copyWithZone:]
+ -[RFSummaryItemButtonCardSection dictionaryRepresentation]
+ -[RFSummaryItemButtonCardSection encodeWithCoder:]
+ -[RFSummaryItemButtonCardSection hasButtonItemsAreTrailing]
+ -[RFSummaryItemButtonCardSection hash]
+ -[RFSummaryItemButtonCardSection initWithCoder:]
+ -[RFSummaryItemButtonCardSection isEqual:]
+ -[RFSummaryItemButtonCardSection jsonData]
+ -[RFSummaryItemButtonCardSection setButtonItemsAreTrailing:]
+ -[RFSummaryItemButtonCardSection setButton_1:]
+ -[RFSummaryItemButtonCardSection setButton_2:]
+ -[RFSummaryItemButtonCardSection setButton_3:]
+ -[RFSummaryItemButtonCardSection setText_1:]
+ -[RFSummaryItemButtonCardSection setText_2:]
+ -[RFSummaryItemButtonCardSection setText_3:]
+ -[RFSummaryItemButtonCardSection setText_4:]
+ -[RFSummaryItemButtonCardSection setThumbnail:]
+ -[RFSummaryItemButtonCardSection text_1]
+ -[RFSummaryItemButtonCardSection text_2]
+ -[RFSummaryItemButtonCardSection text_3]
+ -[RFSummaryItemButtonCardSection text_4]
+ -[RFSummaryItemButtonCardSection thumbnail]
+ -[RFSummaryItemButtonCardSection(ProtobufInitializer) initWithProtobuf:]
+ -[RFSummaryItemImageRightCardSection .cxx_destruct]
+ -[RFSummaryItemImageRightCardSection copyWithZone:]
+ -[RFSummaryItemImageRightCardSection dictionaryRepresentation]
+ -[RFSummaryItemImageRightCardSection encodeWithCoder:]
+ -[RFSummaryItemImageRightCardSection hash]
+ -[RFSummaryItemImageRightCardSection initWithCoder:]
+ -[RFSummaryItemImageRightCardSection isEqual:]
+ -[RFSummaryItemImageRightCardSection jsonData]
+ -[RFSummaryItemImageRightCardSection setText_1:]
+ -[RFSummaryItemImageRightCardSection setText_2:]
+ -[RFSummaryItemImageRightCardSection setText_3:]
+ -[RFSummaryItemImageRightCardSection setText_4:]
+ -[RFSummaryItemImageRightCardSection setThumbnail_1:]
+ -[RFSummaryItemImageRightCardSection setThumbnail_2:]
+ -[RFSummaryItemImageRightCardSection text_1]
+ -[RFSummaryItemImageRightCardSection text_2]
+ -[RFSummaryItemImageRightCardSection text_3]
+ -[RFSummaryItemImageRightCardSection text_4]
+ -[RFSummaryItemImageRightCardSection thumbnail_1]
+ -[RFSummaryItemImageRightCardSection thumbnail_2]
+ -[RFSummaryItemImageRightCardSection(ProtobufInitializer) initWithProtobuf:]
+ -[RFSummaryItemPlayerCardSection .cxx_destruct]
+ -[RFSummaryItemPlayerCardSection copyWithZone:]
+ -[RFSummaryItemPlayerCardSection dictionaryRepresentation]
+ -[RFSummaryItemPlayerCardSection encodeWithCoder:]
+ -[RFSummaryItemPlayerCardSection hash]
+ -[RFSummaryItemPlayerCardSection initWithCoder:]
+ -[RFSummaryItemPlayerCardSection isEqual:]
+ -[RFSummaryItemPlayerCardSection jsonData]
+ -[RFSummaryItemPlayerCardSection player]
+ -[RFSummaryItemPlayerCardSection setPlayer:]
+ -[RFSummaryItemPlayerCardSection setText_1:]
+ -[RFSummaryItemPlayerCardSection setText_2:]
+ -[RFSummaryItemPlayerCardSection setText_3:]
+ -[RFSummaryItemPlayerCardSection setText_4:]
+ -[RFSummaryItemPlayerCardSection setThumbnail:]
+ -[RFSummaryItemPlayerCardSection text_1]
+ -[RFSummaryItemPlayerCardSection text_2]
+ -[RFSummaryItemPlayerCardSection text_3]
+ -[RFSummaryItemPlayerCardSection text_4]
+ -[RFSummaryItemPlayerCardSection thumbnail]
+ -[RFSummaryItemPlayerCardSection(ProtobufInitializer) initWithProtobuf:]
+ -[RFSystemFont .cxx_destruct]
+ -[RFSystemFont copyWithZone:]
+ -[RFSystemFont dictionaryRepresentation]
+ -[RFSystemFont encodeWithCoder:]
+ -[RFSystemFont hasWeight]
+ -[RFSystemFont hash]
+ -[RFSystemFont initWithCoder:]
+ -[RFSystemFont isEqual:]
+ -[RFSystemFont jsonData]
+ -[RFSystemFont setSize:]
+ -[RFSystemFont setWeight:]
+ -[RFSystemFont size]
+ -[RFSystemFont weight]
+ -[RFSystemFont(ProtobufInitializer) initWithProtobuf:]
+ -[RFTableCell applySmallCaps]
+ -[RFTableCell hasApplySmallCaps]
+ -[RFTableCell setApplySmallCaps:]
+ -[RFTableRowCardSection hasVertical_alignment]
+ -[RFTableRowCardSection setVertical_alignment:]
+ -[RFTableRowCardSection vertical_alignment]
+ -[RFUrlImage background_color]
+ -[RFUrlImage setBackground_color:]
+ -[SFCardSectionValue rfBinaryButtonCardSection]
+ -[SFCardSectionValue rfButtonCardSection]
+ -[SFCardSectionValue rfPrimaryHeaderStackedImageCardSection]
+ -[SFCardSectionValue rfReferenceCenteredCardSection]
+ -[SFCardSectionValue rfReferenceItemButtonCardSection]
+ -[SFCardSectionValue rfReferenceItemLogoCardSection]
+ -[SFCardSectionValue rfSecondaryHeaderEmphasizedCardSection]
+ -[SFCardSectionValue rfSecondaryHeaderStandardCardSection]
+ -[SFCardSectionValue rfSimpleItemReverseRichCardSection]
+ -[SFCardSectionValue rfSimpleItemRichSearchResultCardSection]
+ -[SFCardSectionValue rfSimpleItemVisualElementCardSection]
+ -[SFCardSectionValue rfSummaryItemButtonCardSection]
+ -[SFCardSectionValue rfSummaryItemImageRightCardSection]
+ -[SFCardSectionValue rfSummaryItemPlayerCardSection]
+ -[SFCardSectionValue setRfBinaryButtonCardSection:]
+ -[SFCardSectionValue setRfButtonCardSection:]
+ -[SFCardSectionValue setRfPrimaryHeaderStackedImageCardSection:]
+ -[SFCardSectionValue setRfReferenceCenteredCardSection:]
+ -[SFCardSectionValue setRfReferenceItemButtonCardSection:]
+ -[SFCardSectionValue setRfReferenceItemLogoCardSection:]
+ -[SFCardSectionValue setRfSecondaryHeaderEmphasizedCardSection:]
+ -[SFCardSectionValue setRfSecondaryHeaderStandardCardSection:]
+ -[SFCardSectionValue setRfSimpleItemReverseRichCardSection:]
+ -[SFCardSectionValue setRfSimpleItemRichSearchResultCardSection:]
+ -[SFCardSectionValue setRfSimpleItemVisualElementCardSection:]
+ -[SFCardSectionValue setRfSummaryItemButtonCardSection:]
+ -[SFCardSectionValue setRfSummaryItemImageRightCardSection:]
+ -[SFCardSectionValue setRfSummaryItemPlayerCardSection:]
+ -[SFCollectionStyleGrid gridStyle]
+ -[SFCollectionStyleGrid hasGridStyle]
+ -[SFCollectionStyleGrid setGridStyle:]
+ -[SFCollectionStyleRow hasIsInsetGrouped]
+ -[SFCollectionStyleRow isInsetGrouped]
+ -[SFCollectionStyleRow setIsInsetGrouped:]
+ -[SFContactButtonItem actionTypesToShow]
+ -[SFContactButtonItem setActionTypesToShow:]
+ -[SFDomainEngagementScore iFunScore]
+ -[SFDomainEngagementScore setIFunScore:]
+ -[SFDomainEngagementScore(Handwritten) initWithDomain:scoreConfidence:score:]
+ -[SFEngagementSignal(Handwritten) initWithVersion:serverScore:severScoreConfidence:localScore:localScoreConfidence:domainScores:]
+ -[SFHashBucketDetail .cxx_destruct]
+ -[SFHashBucketDetail copyWithZone:]
+ -[SFHashBucketDetail dictionaryRepresentation]
+ -[SFHashBucketDetail encodeWithCoder:]
+ -[SFHashBucketDetail hash]
+ -[SFHashBucketDetail hash_details]
+ -[SFHashBucketDetail hash_prefix]
+ -[SFHashBucketDetail initWithCoder:]
+ -[SFHashBucketDetail isEqual:]
+ -[SFHashBucketDetail jsonData]
+ -[SFHashBucketDetail setHash_details:]
+ -[SFHashBucketDetail setHash_prefix:]
+ -[SFHashBucketDetail(ProtobufInitializer) initWithProtobuf:]
+ -[SFHashDetail .cxx_destruct]
+ -[SFHashDetail copyWithZone:]
+ -[SFHashDetail dictionaryRepresentation]
+ -[SFHashDetail encodeWithCoder:]
+ -[SFHashDetail full_hash]
+ -[SFHashDetail hasHas_ee]
+ -[SFHashDetail hasHas_summary]
+ -[SFHashDetail has_ee]
+ -[SFHashDetail has_summary]
+ -[SFHashDetail hash]
+ -[SFHashDetail initWithCoder:]
+ -[SFHashDetail isEqual:]
+ -[SFHashDetail jsonData]
+ -[SFHashDetail setFull_hash:]
+ -[SFHashDetail setHas_ee:]
+ -[SFHashDetail setHas_summary:]
+ -[SFHashDetail(ProtobufInitializer) initWithProtobuf:]
+ -[SFMediaMetadata mediaIdentifier]
+ -[SFMediaMetadata setMediaIdentifier:]
+ -[SFPlayAudioButtonItem .cxx_destruct]
+ -[SFPlayAudioButtonItem copyWithZone:]
+ -[SFPlayAudioButtonItem dictionaryRepresentation]
+ -[SFPlayAudioButtonItem encodeWithCoder:]
+ -[SFPlayAudioButtonItem hash]
+ -[SFPlayAudioButtonItem initWithCoder:]
+ -[SFPlayAudioButtonItem isEqual:]
+ -[SFPlayAudioButtonItem jsonData]
+ -[SFPlayAudioButtonItem mediaMetadata]
+ -[SFPlayAudioButtonItem setMediaMetadata:]
+ -[SFPlayAudioButtonItem setToggleButtonConfiguration:]
+ -[SFPlayAudioButtonItem toggleButtonConfiguration]
+ -[SFPlayAudioButtonItem(ProtobufInitializer) initWithProtobuf:]
+ -[SFPlayMediaCommand hasShouldPause]
+ -[SFPlayMediaCommand setShouldPause:]
+ -[SFPlayMediaCommand shouldPause]
+ -[SFPlayWatchListItemButtonItem .cxx_destruct]
+ -[SFPlayWatchListItemButtonItem copyWithZone:]
+ -[SFPlayWatchListItemButtonItem dictionaryRepresentation]
+ -[SFPlayWatchListItemButtonItem encodeWithCoder:]
+ -[SFPlayWatchListItemButtonItem hash]
+ -[SFPlayWatchListItemButtonItem image]
+ -[SFPlayWatchListItemButtonItem initWithCoder:]
+ -[SFPlayWatchListItemButtonItem isEqual:]
+ -[SFPlayWatchListItemButtonItem jsonData]
+ -[SFPlayWatchListItemButtonItem setImage:]
+ -[SFPlayWatchListItemButtonItem setTitle:]
+ -[SFPlayWatchListItemButtonItem setWatchListItem:]
+ -[SFPlayWatchListItemButtonItem title]
+ -[SFPlayWatchListItemButtonItem watchListItem]
+ -[SFPlayWatchListItemButtonItem(ProtobufInitializer) initWithProtobuf:]
+ -[SFRequestProductPageCommand .cxx_destruct]
+ -[SFRequestProductPageCommand copyWithZone:]
+ -[SFRequestProductPageCommand dictionaryRepresentation]
+ -[SFRequestProductPageCommand distributorBundleIdentifier]
+ -[SFRequestProductPageCommand encodeWithCoder:]
+ -[SFRequestProductPageCommand hasItemIdentifier]
+ -[SFRequestProductPageCommand hasVersionIdentifier]
+ -[SFRequestProductPageCommand hash]
+ -[SFRequestProductPageCommand initWithCoder:]
+ -[SFRequestProductPageCommand isEqual:]
+ -[SFRequestProductPageCommand itemIdentifier]
+ -[SFRequestProductPageCommand jsonData]
+ -[SFRequestProductPageCommand setDistributorBundleIdentifier:]
+ -[SFRequestProductPageCommand setItemIdentifier:]
+ -[SFRequestProductPageCommand setVersionIdentifier:]
+ -[SFRequestProductPageCommand versionIdentifier]
+ -[SFRequestProductPageCommand(ProtobufInitializer) initWithProtobuf:]
+ -[SFSearchInAppCommand hasSearchInAppType]
+ -[SFSearchInAppCommand searchInAppType]
+ -[SFSearchInAppCommand setSearchInAppType:]
+ -[SFSearchResult indexOfResultInSectionWhenRanked]
+ -[SFSearchResult indexOfSectionWhenRanked]
+ -[SFSearchResult setIndexOfResultInSectionWhenRanked:]
+ -[SFSearchResult setIndexOfSectionWhenRanked:]
+ -[SFShortcutsImage .cxx_destruct]
+ -[SFShortcutsImage copyWithZone:]
+ -[SFShortcutsImage dictionaryRepresentation]
+ -[SFShortcutsImage encodeWithCoder:]
+ -[SFShortcutsImage hash]
+ -[SFShortcutsImage initWithCoder:]
+ -[SFShortcutsImage isEqual:]
+ -[SFShortcutsImage jsonData]
+ -[SFShortcutsImage lnPropertyIdentifier]
+ -[SFShortcutsImage setLnPropertyIdentifier:]
+ -[SFStoreButtonItem .cxx_destruct]
+ -[SFStoreButtonItem copyWithZone:]
+ -[SFStoreButtonItem dictionaryRepresentation]
+ -[SFStoreButtonItem encodeWithCoder:]
+ -[SFStoreButtonItem hasShouldOpenAppAfterInstallCompletes]
+ -[SFStoreButtonItem hash]
+ -[SFStoreButtonItem identifier]
+ -[SFStoreButtonItem initWithCoder:]
+ -[SFStoreButtonItem isEqual:]
+ -[SFStoreButtonItem jsonData]
+ -[SFStoreButtonItem setIdentifier:]
+ -[SFStoreButtonItem setShouldOpenAppAfterInstallCompletes:]
+ -[SFStoreButtonItem shouldOpenAppAfterInstallCompletes]
+ -[SFStoreButtonItem(ProtobufInitializer) initWithProtobuf:]
+ -[SFSymbolImage fillStyle]
+ -[SFSymbolImage hasFillStyle]
+ -[SFSymbolImage setFillStyle:]
+ -[SFToggleWatchListStatusCommand hasShouldAddToWatchList]
+ -[SFToggleWatchListStatusCommand setShouldAddToWatchList:]
+ -[SFToggleWatchListStatusCommand shouldAddToWatchList]
+ -[SFWatchListButtonItem setToggleButtonConfiguration:]
+ -[SFWatchListButtonItem toggleButtonConfiguration]
+ -[_SFPBButtonItem playAudioButtonItem]
+ -[_SFPBButtonItem playWatchListItemButtonItem]
+ -[_SFPBButtonItem setPlayAudioButtonItem:]
+ -[_SFPBButtonItem setPlayWatchListItemButtonItem:]
+ -[_SFPBButtonItem setStoreButtonItem:]
+ -[_SFPBButtonItem storeButtonItem]
+ -[_SFPBCardSectionValue rfBinaryButtonCardSection]
+ -[_SFPBCardSectionValue rfButtonCardSection]
+ -[_SFPBCardSectionValue rfPrimaryHeaderStackedImageCardSection]
+ -[_SFPBCardSectionValue rfReferenceCenteredCardSection]
+ -[_SFPBCardSectionValue rfReferenceItemButtonCardSection]
+ -[_SFPBCardSectionValue rfReferenceItemLogoCardSection]
+ -[_SFPBCardSectionValue rfSecondaryHeaderEmphasizedCardSection]
+ -[_SFPBCardSectionValue rfSecondaryHeaderStandardCardSection]
+ -[_SFPBCardSectionValue rfSimpleItemReverseRichCardSection]
+ -[_SFPBCardSectionValue rfSimpleItemRichSearchResultCardSection]
+ -[_SFPBCardSectionValue rfSimpleItemVisualElementCardSection]
+ -[_SFPBCardSectionValue rfSummaryItemButtonCardSection]
+ -[_SFPBCardSectionValue rfSummaryItemImageRightCardSection]
+ -[_SFPBCardSectionValue rfSummaryItemPlayerCardSection]
+ -[_SFPBCardSectionValue setRfBinaryButtonCardSection:]
+ -[_SFPBCardSectionValue setRfButtonCardSection:]
+ -[_SFPBCardSectionValue setRfPrimaryHeaderStackedImageCardSection:]
+ -[_SFPBCardSectionValue setRfReferenceCenteredCardSection:]
+ -[_SFPBCardSectionValue setRfReferenceItemButtonCardSection:]
+ -[_SFPBCardSectionValue setRfReferenceItemLogoCardSection:]
+ -[_SFPBCardSectionValue setRfSecondaryHeaderEmphasizedCardSection:]
+ -[_SFPBCardSectionValue setRfSecondaryHeaderStandardCardSection:]
+ -[_SFPBCardSectionValue setRfSimpleItemReverseRichCardSection:]
+ -[_SFPBCardSectionValue setRfSimpleItemRichSearchResultCardSection:]
+ -[_SFPBCardSectionValue setRfSimpleItemVisualElementCardSection:]
+ -[_SFPBCardSectionValue setRfSummaryItemButtonCardSection:]
+ -[_SFPBCardSectionValue setRfSummaryItemImageRightCardSection:]
+ -[_SFPBCardSectionValue setRfSummaryItemPlayerCardSection:]
+ -[_SFPBCollectionStyleGrid gridStyle]
+ -[_SFPBCollectionStyleGrid setGridStyle:]
+ -[_SFPBCollectionStyleRow isInsetGrouped]
+ -[_SFPBCollectionStyleRow setIsInsetGrouped:]
+ -[_SFPBCommand requestProductPageCommand]
+ -[_SFPBCommand setRequestProductPageCommand:]
+ -[_SFPBContactButtonItem actionTypesToShowAtIndex:]
+ -[_SFPBContactButtonItem actionTypesToShowCount]
+ -[_SFPBContactButtonItem actionTypesToShows]
+ -[_SFPBContactButtonItem addActionTypesToShow:]
+ -[_SFPBContactButtonItem clearActionTypesToShow]
+ -[_SFPBContactButtonItem setActionTypesToShow:]
+ -[_SFPBContactButtonItem setActionTypesToShows:]
+ -[_SFPBDomainEngagementScore iFunScore]
+ -[_SFPBDomainEngagementScore setIFunScore:]
+ -[_SFPBHashBucketDetail .cxx_destruct]
+ -[_SFPBHashBucketDetail addHash_details:]
+ -[_SFPBHashBucketDetail clearHash_details]
+ -[_SFPBHashBucketDetail dictionaryRepresentation]
+ -[_SFPBHashBucketDetail hash]
+ -[_SFPBHashBucketDetail hash_detailsAtIndex:]
+ -[_SFPBHashBucketDetail hash_detailsCount]
+ -[_SFPBHashBucketDetail hash_details]
+ -[_SFPBHashBucketDetail hash_prefix]
+ -[_SFPBHashBucketDetail initWithDictionary:]
+ -[_SFPBHashBucketDetail initWithJSON:]
+ -[_SFPBHashBucketDetail isEqual:]
+ -[_SFPBHashBucketDetail jsonData]
+ -[_SFPBHashBucketDetail readFrom:]
+ -[_SFPBHashBucketDetail setHash_details:]
+ -[_SFPBHashBucketDetail setHash_prefix:]
+ -[_SFPBHashBucketDetail writeTo:]
+ -[_SFPBHashBucketDetail(FacadeInitializer) initWithFacade:]
+ -[_SFPBHashBucketDetail_HashDetail .cxx_destruct]
+ -[_SFPBHashBucketDetail_HashDetail dictionaryRepresentation]
+ -[_SFPBHashBucketDetail_HashDetail full_hash]
+ -[_SFPBHashBucketDetail_HashDetail has_ee]
+ -[_SFPBHashBucketDetail_HashDetail has_summary]
+ -[_SFPBHashBucketDetail_HashDetail hash]
+ -[_SFPBHashBucketDetail_HashDetail initWithDictionary:]
+ -[_SFPBHashBucketDetail_HashDetail initWithJSON:]
+ -[_SFPBHashBucketDetail_HashDetail isEqual:]
+ -[_SFPBHashBucketDetail_HashDetail jsonData]
+ -[_SFPBHashBucketDetail_HashDetail readFrom:]
+ -[_SFPBHashBucketDetail_HashDetail setFull_hash:]
+ -[_SFPBHashBucketDetail_HashDetail setHas_ee:]
+ -[_SFPBHashBucketDetail_HashDetail setHas_summary:]
+ -[_SFPBHashBucketDetail_HashDetail writeTo:]
+ -[_SFPBHashBucketDetail_HashDetail(FacadeInitializer) initWithFacade:]
+ -[_SFPBImage setShortcutsImage:]
+ -[_SFPBImage shortcutsImage]
+ -[_SFPBMediaMetadata mediaIdentifier]
+ -[_SFPBMediaMetadata setMediaIdentifier:]
+ -[_SFPBPlayAudioButtonItem .cxx_destruct]
+ -[_SFPBPlayAudioButtonItem dictionaryRepresentation]
+ -[_SFPBPlayAudioButtonItem hash]
+ -[_SFPBPlayAudioButtonItem initWithDictionary:]
+ -[_SFPBPlayAudioButtonItem initWithJSON:]
+ -[_SFPBPlayAudioButtonItem isEqual:]
+ -[_SFPBPlayAudioButtonItem jsonData]
+ -[_SFPBPlayAudioButtonItem mediaMetadata]
+ -[_SFPBPlayAudioButtonItem readFrom:]
+ -[_SFPBPlayAudioButtonItem setMediaMetadata:]
+ -[_SFPBPlayAudioButtonItem setToggleButtonConfiguration:]
+ -[_SFPBPlayAudioButtonItem setUniqueId:]
+ -[_SFPBPlayAudioButtonItem toggleButtonConfiguration]
+ -[_SFPBPlayAudioButtonItem uniqueId]
+ -[_SFPBPlayAudioButtonItem writeTo:]
+ -[_SFPBPlayAudioButtonItem(FacadeInitializer) initWithFacade:]
+ -[_SFPBPlayMediaCommand setShouldPause:]
+ -[_SFPBPlayMediaCommand shouldPause]
+ -[_SFPBPlayWatchListItemButtonItem .cxx_destruct]
+ -[_SFPBPlayWatchListItemButtonItem dictionaryRepresentation]
+ -[_SFPBPlayWatchListItemButtonItem hash]
+ -[_SFPBPlayWatchListItemButtonItem image]
+ -[_SFPBPlayWatchListItemButtonItem initWithDictionary:]
+ -[_SFPBPlayWatchListItemButtonItem initWithJSON:]
+ -[_SFPBPlayWatchListItemButtonItem isEqual:]
+ -[_SFPBPlayWatchListItemButtonItem jsonData]
+ -[_SFPBPlayWatchListItemButtonItem readFrom:]
+ -[_SFPBPlayWatchListItemButtonItem setImage:]
+ -[_SFPBPlayWatchListItemButtonItem setTitle:]
+ -[_SFPBPlayWatchListItemButtonItem setUniqueId:]
+ -[_SFPBPlayWatchListItemButtonItem setWatchListItem:]
+ -[_SFPBPlayWatchListItemButtonItem title]
+ -[_SFPBPlayWatchListItemButtonItem uniqueId]
+ -[_SFPBPlayWatchListItemButtonItem watchListItem]
+ -[_SFPBPlayWatchListItemButtonItem writeTo:]
+ -[_SFPBPlayWatchListItemButtonItem(FacadeInitializer) initWithFacade:]
+ -[_SFPBRFBinaryButtonCardSection .cxx_destruct]
+ -[_SFPBRFBinaryButtonCardSection dictionaryRepresentation]
+ -[_SFPBRFBinaryButtonCardSection hash]
+ -[_SFPBRFBinaryButtonCardSection initWithDictionary:]
+ -[_SFPBRFBinaryButtonCardSection initWithJSON:]
+ -[_SFPBRFBinaryButtonCardSection isEqual:]
+ -[_SFPBRFBinaryButtonCardSection jsonData]
+ -[_SFPBRFBinaryButtonCardSection primary_button]
+ -[_SFPBRFBinaryButtonCardSection readFrom:]
+ -[_SFPBRFBinaryButtonCardSection secondary_button]
+ -[_SFPBRFBinaryButtonCardSection setPrimary_button:]
+ -[_SFPBRFBinaryButtonCardSection setSecondary_button:]
+ -[_SFPBRFBinaryButtonCardSection writeTo:]
+ -[_SFPBRFBinaryButtonCardSection(FacadeInitializer) initWithFacade:]
+ -[_SFPBRFButtonCardSection .cxx_destruct]
+ -[_SFPBRFButtonCardSection button]
+ -[_SFPBRFButtonCardSection dictionaryRepresentation]
+ -[_SFPBRFButtonCardSection hash]
+ -[_SFPBRFButtonCardSection initWithDictionary:]
+ -[_SFPBRFButtonCardSection initWithJSON:]
+ -[_SFPBRFButtonCardSection isEqual:]
+ -[_SFPBRFButtonCardSection jsonData]
+ -[_SFPBRFButtonCardSection readFrom:]
+ -[_SFPBRFButtonCardSection setButton:]
+ -[_SFPBRFButtonCardSection writeTo:]
+ -[_SFPBRFButtonCardSection(FacadeInitializer) initWithFacade:]
+ -[_SFPBRFFactItemButtonCardSection buttonItemsAreBottom]
+ -[_SFPBRFFactItemButtonCardSection setButtonItemsAreBottom:]
+ -[_SFPBRFFactItemButtonCardSection setThumbnail2:]
+ -[_SFPBRFFactItemButtonCardSection thumbnail2]
+ -[_SFPBRFFactItemStandardCardSection setThumbnail2:]
+ -[_SFPBRFFactItemStandardCardSection thumbnail2]
+ -[_SFPBRFFont .cxx_destruct]
+ -[_SFPBRFFont dictionaryRepresentation]
+ -[_SFPBRFFont hash]
+ -[_SFPBRFFont initWithDictionary:]
+ -[_SFPBRFFont initWithJSON:]
+ -[_SFPBRFFont isEqual:]
+ -[_SFPBRFFont jsonData]
+ -[_SFPBRFFont name]
+ -[_SFPBRFFont readFrom:]
+ -[_SFPBRFFont setName:]
+ -[_SFPBRFFont setSystem:]
+ -[_SFPBRFFont system]
+ -[_SFPBRFFont whichValue]
+ -[_SFPBRFFont writeTo:]
+ -[_SFPBRFFont(FacadeInitializer) initWithFacade:]
+ -[_SFPBRFFont_RFSystemFont dictionaryRepresentation]
+ -[_SFPBRFFont_RFSystemFont hash]
+ -[_SFPBRFFont_RFSystemFont initWithDictionary:]
+ -[_SFPBRFFont_RFSystemFont initWithJSON:]
+ -[_SFPBRFFont_RFSystemFont isEqual:]
+ -[_SFPBRFFont_RFSystemFont jsonData]
+ -[_SFPBRFFont_RFSystemFont readFrom:]
+ -[_SFPBRFFont_RFSystemFont setSize:]
+ -[_SFPBRFFont_RFSystemFont setWeight:]
+ -[_SFPBRFFont_RFSystemFont size]
+ -[_SFPBRFFont_RFSystemFont weight]
+ -[_SFPBRFFont_RFSystemFont writeTo:]
+ -[_SFPBRFFont_RFSystemFont(FacadeInitializer) initWithFacade:]
+ -[_SFPBRFFormattedText font]
+ -[_SFPBRFFormattedText setFont:]
+ -[_SFPBRFPrimaryHeaderMarqueeCardSection addTint]
+ -[_SFPBRFPrimaryHeaderMarqueeCardSection setAddTint:]
+ -[_SFPBRFPrimaryHeaderRichCardSection addTint]
+ -[_SFPBRFPrimaryHeaderRichCardSection setAddTint:]
+ -[_SFPBRFPrimaryHeaderStackedImageCardSection .cxx_destruct]
+ -[_SFPBRFPrimaryHeaderStackedImageCardSection addImages:]
+ -[_SFPBRFPrimaryHeaderStackedImageCardSection clearImages]
+ -[_SFPBRFPrimaryHeaderStackedImageCardSection dictionaryRepresentation]
+ -[_SFPBRFPrimaryHeaderStackedImageCardSection hash]
+ -[_SFPBRFPrimaryHeaderStackedImageCardSection imagesAtIndex:]
+ -[_SFPBRFPrimaryHeaderStackedImageCardSection imagesCount]
+ -[_SFPBRFPrimaryHeaderStackedImageCardSection images]
+ -[_SFPBRFPrimaryHeaderStackedImageCardSection initWithDictionary:]
+ -[_SFPBRFPrimaryHeaderStackedImageCardSection initWithJSON:]
+ -[_SFPBRFPrimaryHeaderStackedImageCardSection isEqual:]
+ -[_SFPBRFPrimaryHeaderStackedImageCardSection jsonData]
+ -[_SFPBRFPrimaryHeaderStackedImageCardSection readFrom:]
+ -[_SFPBRFPrimaryHeaderStackedImageCardSection setImages:]
+ -[_SFPBRFPrimaryHeaderStackedImageCardSection setText_1:]
+ -[_SFPBRFPrimaryHeaderStackedImageCardSection setText_2:]
+ -[_SFPBRFPrimaryHeaderStackedImageCardSection text_1]
+ -[_SFPBRFPrimaryHeaderStackedImageCardSection text_2]
+ -[_SFPBRFPrimaryHeaderStackedImageCardSection writeTo:]
+ -[_SFPBRFPrimaryHeaderStackedImageCardSection(FacadeInitializer) initWithFacade:]
+ -[_SFPBRFPrimaryHeaderStandardCardSection addTint]
+ -[_SFPBRFPrimaryHeaderStandardCardSection setAddTint:]
+ -[_SFPBRFReferenceCenteredCardSection .cxx_destruct]
+ -[_SFPBRFReferenceCenteredCardSection add_tint]
+ -[_SFPBRFReferenceCenteredCardSection dictionaryRepresentation]
+ -[_SFPBRFReferenceCenteredCardSection hash]
+ -[_SFPBRFReferenceCenteredCardSection initWithDictionary:]
+ -[_SFPBRFReferenceCenteredCardSection initWithJSON:]
+ -[_SFPBRFReferenceCenteredCardSection isEqual:]
+ -[_SFPBRFReferenceCenteredCardSection jsonData]
+ -[_SFPBRFReferenceCenteredCardSection readFrom:]
+ -[_SFPBRFReferenceCenteredCardSection setAdd_tint:]
+ -[_SFPBRFReferenceCenteredCardSection setText_1:]
+ -[_SFPBRFReferenceCenteredCardSection setText_2:]
+ -[_SFPBRFReferenceCenteredCardSection setText_3:]
+ -[_SFPBRFReferenceCenteredCardSection setText_4:]
+ -[_SFPBRFReferenceCenteredCardSection text_1]
+ -[_SFPBRFReferenceCenteredCardSection text_2]
+ -[_SFPBRFReferenceCenteredCardSection text_3]
+ -[_SFPBRFReferenceCenteredCardSection text_4]
+ -[_SFPBRFReferenceCenteredCardSection writeTo:]
+ -[_SFPBRFReferenceCenteredCardSection(FacadeInitializer) initWithFacade:]
+ -[_SFPBRFReferenceFootnoteCardSection addTint]
+ -[_SFPBRFReferenceFootnoteCardSection setAddTint:]
+ -[_SFPBRFReferenceItemButtonCardSection .cxx_destruct]
+ -[_SFPBRFReferenceItemButtonCardSection button_1]
+ -[_SFPBRFReferenceItemButtonCardSection dictionaryRepresentation]
+ -[_SFPBRFReferenceItemButtonCardSection hash]
+ -[_SFPBRFReferenceItemButtonCardSection initWithDictionary:]
+ -[_SFPBRFReferenceItemButtonCardSection initWithJSON:]
+ -[_SFPBRFReferenceItemButtonCardSection isEqual:]
+ -[_SFPBRFReferenceItemButtonCardSection jsonData]
+ -[_SFPBRFReferenceItemButtonCardSection readFrom:]
+ -[_SFPBRFReferenceItemButtonCardSection setButton_1:]
+ -[_SFPBRFReferenceItemButtonCardSection writeTo:]
+ -[_SFPBRFReferenceItemButtonCardSection(FacadeInitializer) initWithFacade:]
+ -[_SFPBRFReferenceItemLogoCardSection .cxx_destruct]
+ -[_SFPBRFReferenceItemLogoCardSection dictionaryRepresentation]
+ -[_SFPBRFReferenceItemLogoCardSection hash]
+ -[_SFPBRFReferenceItemLogoCardSection initWithDictionary:]
+ -[_SFPBRFReferenceItemLogoCardSection initWithJSON:]
+ -[_SFPBRFReferenceItemLogoCardSection isEqual:]
+ -[_SFPBRFReferenceItemLogoCardSection jsonData]
+ -[_SFPBRFReferenceItemLogoCardSection readFrom:]
+ -[_SFPBRFReferenceItemLogoCardSection setThumbnail:]
+ -[_SFPBRFReferenceItemLogoCardSection thumbnail]
+ -[_SFPBRFReferenceItemLogoCardSection writeTo:]
+ -[_SFPBRFReferenceItemLogoCardSection(FacadeInitializer) initWithFacade:]
+ -[_SFPBRFReferenceRichCardSection addTint]
+ -[_SFPBRFReferenceRichCardSection setAddTint:]
+ -[_SFPBRFReferenceStandardCardSection addTint]
+ -[_SFPBRFReferenceStandardCardSection setAddTint:]
+ -[_SFPBRFSecondaryHeaderEmphasizedCardSection .cxx_destruct]
+ -[_SFPBRFSecondaryHeaderEmphasizedCardSection dictionaryRepresentation]
+ -[_SFPBRFSecondaryHeaderEmphasizedCardSection hash]
+ -[_SFPBRFSecondaryHeaderEmphasizedCardSection initWithDictionary:]
+ -[_SFPBRFSecondaryHeaderEmphasizedCardSection initWithJSON:]
+ -[_SFPBRFSecondaryHeaderEmphasizedCardSection isEqual:]
+ -[_SFPBRFSecondaryHeaderEmphasizedCardSection jsonData]
+ -[_SFPBRFSecondaryHeaderEmphasizedCardSection readFrom:]
+ -[_SFPBRFSecondaryHeaderEmphasizedCardSection setText_1:]
+ -[_SFPBRFSecondaryHeaderEmphasizedCardSection text_1]
+ -[_SFPBRFSecondaryHeaderEmphasizedCardSection writeTo:]
+ -[_SFPBRFSecondaryHeaderEmphasizedCardSection(FacadeInitializer) initWithFacade:]
+ -[_SFPBRFSecondaryHeaderStandardCardSection .cxx_destruct]
+ -[_SFPBRFSecondaryHeaderStandardCardSection dictionaryRepresentation]
+ -[_SFPBRFSecondaryHeaderStandardCardSection hash]
+ -[_SFPBRFSecondaryHeaderStandardCardSection initWithDictionary:]
+ -[_SFPBRFSecondaryHeaderStandardCardSection initWithJSON:]
+ -[_SFPBRFSecondaryHeaderStandardCardSection isEqual:]
+ -[_SFPBRFSecondaryHeaderStandardCardSection jsonData]
+ -[_SFPBRFSecondaryHeaderStandardCardSection readFrom:]
+ -[_SFPBRFSecondaryHeaderStandardCardSection setText_1:]
+ -[_SFPBRFSecondaryHeaderStandardCardSection text_1]
+ -[_SFPBRFSecondaryHeaderStandardCardSection writeTo:]
+ -[_SFPBRFSecondaryHeaderStandardCardSection(FacadeInitializer) initWithFacade:]
+ -[_SFPBRFSimpleItemReverseRichCardSection .cxx_destruct]
+ -[_SFPBRFSimpleItemReverseRichCardSection addText_3:]
+ -[_SFPBRFSimpleItemReverseRichCardSection clearText_3]
+ -[_SFPBRFSimpleItemReverseRichCardSection dictionaryRepresentation]
+ -[_SFPBRFSimpleItemReverseRichCardSection hash]
+ -[_SFPBRFSimpleItemReverseRichCardSection initWithDictionary:]
+ -[_SFPBRFSimpleItemReverseRichCardSection initWithJSON:]
+ -[_SFPBRFSimpleItemReverseRichCardSection isEqual:]
+ -[_SFPBRFSimpleItemReverseRichCardSection jsonData]
+ -[_SFPBRFSimpleItemReverseRichCardSection readFrom:]
+ -[_SFPBRFSimpleItemReverseRichCardSection setText_1:]
+ -[_SFPBRFSimpleItemReverseRichCardSection setText_2:]
+ -[_SFPBRFSimpleItemReverseRichCardSection setText_3:]
+ -[_SFPBRFSimpleItemReverseRichCardSection setText_3s:]
+ -[_SFPBRFSimpleItemReverseRichCardSection setText_4:]
+ -[_SFPBRFSimpleItemReverseRichCardSection setThumbnail:]
+ -[_SFPBRFSimpleItemReverseRichCardSection text_1]
+ -[_SFPBRFSimpleItemReverseRichCardSection text_2]
+ -[_SFPBRFSimpleItemReverseRichCardSection text_3AtIndex:]
+ -[_SFPBRFSimpleItemReverseRichCardSection text_3Count]
+ -[_SFPBRFSimpleItemReverseRichCardSection text_3s]
+ -[_SFPBRFSimpleItemReverseRichCardSection text_4]
+ -[_SFPBRFSimpleItemReverseRichCardSection thumbnail]
+ -[_SFPBRFSimpleItemReverseRichCardSection writeTo:]
+ -[_SFPBRFSimpleItemReverseRichCardSection(FacadeInitializer) initWithFacade:]
+ -[_SFPBRFSimpleItemRichSearchResultCardSection .cxx_destruct]
+ -[_SFPBRFSimpleItemRichSearchResultCardSection addText_3:]
+ -[_SFPBRFSimpleItemRichSearchResultCardSection addText_5:]
+ -[_SFPBRFSimpleItemRichSearchResultCardSection clearText_3]
+ -[_SFPBRFSimpleItemRichSearchResultCardSection clearText_5]
+ -[_SFPBRFSimpleItemRichSearchResultCardSection dictionaryRepresentation]
+ -[_SFPBRFSimpleItemRichSearchResultCardSection hash]
+ -[_SFPBRFSimpleItemRichSearchResultCardSection initWithDictionary:]
+ -[_SFPBRFSimpleItemRichSearchResultCardSection initWithJSON:]
+ -[_SFPBRFSimpleItemRichSearchResultCardSection isEqual:]
+ -[_SFPBRFSimpleItemRichSearchResultCardSection jsonData]
+ -[_SFPBRFSimpleItemRichSearchResultCardSection readFrom:]
+ -[_SFPBRFSimpleItemRichSearchResultCardSection setText_1:]
+ -[_SFPBRFSimpleItemRichSearchResultCardSection setText_2:]
+ -[_SFPBRFSimpleItemRichSearchResultCardSection setText_3:]
+ -[_SFPBRFSimpleItemRichSearchResultCardSection setText_3s:]
+ -[_SFPBRFSimpleItemRichSearchResultCardSection setText_4:]
+ -[_SFPBRFSimpleItemRichSearchResultCardSection setText_5:]
+ -[_SFPBRFSimpleItemRichSearchResultCardSection setText_5s:]
+ -[_SFPBRFSimpleItemRichSearchResultCardSection setText_6:]
+ -[_SFPBRFSimpleItemRichSearchResultCardSection setText_7:]
+ -[_SFPBRFSimpleItemRichSearchResultCardSection setText_8:]
+ -[_SFPBRFSimpleItemRichSearchResultCardSection setThumbnail:]
+ -[_SFPBRFSimpleItemRichSearchResultCardSection text_1]
+ -[_SFPBRFSimpleItemRichSearchResultCardSection text_2]
+ -[_SFPBRFSimpleItemRichSearchResultCardSection text_3AtIndex:]
+ -[_SFPBRFSimpleItemRichSearchResultCardSection text_3Count]
+ -[_SFPBRFSimpleItemRichSearchResultCardSection text_3s]
+ -[_SFPBRFSimpleItemRichSearchResultCardSection text_4]
+ -[_SFPBRFSimpleItemRichSearchResultCardSection text_5AtIndex:]
+ -[_SFPBRFSimpleItemRichSearchResultCardSection text_5Count]
+ -[_SFPBRFSimpleItemRichSearchResultCardSection text_5s]
+ -[_SFPBRFSimpleItemRichSearchResultCardSection text_6]
+ -[_SFPBRFSimpleItemRichSearchResultCardSection text_7]
+ -[_SFPBRFSimpleItemRichSearchResultCardSection text_8]
+ -[_SFPBRFSimpleItemRichSearchResultCardSection thumbnail]
+ -[_SFPBRFSimpleItemRichSearchResultCardSection writeTo:]
+ -[_SFPBRFSimpleItemRichSearchResultCardSection(FacadeInitializer) initWithFacade:]
+ -[_SFPBRFSimpleItemVisualElementCardSection .cxx_destruct]
+ -[_SFPBRFSimpleItemVisualElementCardSection dictionaryRepresentation]
+ -[_SFPBRFSimpleItemVisualElementCardSection footnote]
+ -[_SFPBRFSimpleItemVisualElementCardSection hash]
+ -[_SFPBRFSimpleItemVisualElementCardSection horizontal_alignment]
+ -[_SFPBRFSimpleItemVisualElementCardSection image]
+ -[_SFPBRFSimpleItemVisualElementCardSection initWithDictionary:]
+ -[_SFPBRFSimpleItemVisualElementCardSection initWithJSON:]
+ -[_SFPBRFSimpleItemVisualElementCardSection isEqual:]
+ -[_SFPBRFSimpleItemVisualElementCardSection jsonData]
+ -[_SFPBRFSimpleItemVisualElementCardSection readFrom:]
+ -[_SFPBRFSimpleItemVisualElementCardSection setFootnote:]
+ -[_SFPBRFSimpleItemVisualElementCardSection setHorizontal_alignment:]
+ -[_SFPBRFSimpleItemVisualElementCardSection setImage:]
+ -[_SFPBRFSimpleItemVisualElementCardSection setText_1:]
+ -[_SFPBRFSimpleItemVisualElementCardSection setText_2:]
+ -[_SFPBRFSimpleItemVisualElementCardSection text_1]
+ -[_SFPBRFSimpleItemVisualElementCardSection text_2]
+ -[_SFPBRFSimpleItemVisualElementCardSection writeTo:]
+ -[_SFPBRFSimpleItemVisualElementCardSection(FacadeInitializer) initWithFacade:]
+ -[_SFPBRFSummaryItemButtonCardSection .cxx_destruct]
+ -[_SFPBRFSummaryItemButtonCardSection addText_2:]
+ -[_SFPBRFSummaryItemButtonCardSection addText_3:]
+ -[_SFPBRFSummaryItemButtonCardSection buttonItemsAreTrailing]
+ -[_SFPBRFSummaryItemButtonCardSection button_1]
+ -[_SFPBRFSummaryItemButtonCardSection button_2]
+ -[_SFPBRFSummaryItemButtonCardSection button_3]
+ -[_SFPBRFSummaryItemButtonCardSection clearText_2]
+ -[_SFPBRFSummaryItemButtonCardSection clearText_3]
+ -[_SFPBRFSummaryItemButtonCardSection dictionaryRepresentation]
+ -[_SFPBRFSummaryItemButtonCardSection hash]
+ -[_SFPBRFSummaryItemButtonCardSection initWithDictionary:]
+ -[_SFPBRFSummaryItemButtonCardSection initWithJSON:]
+ -[_SFPBRFSummaryItemButtonCardSection isEqual:]
+ -[_SFPBRFSummaryItemButtonCardSection jsonData]
+ -[_SFPBRFSummaryItemButtonCardSection readFrom:]
+ -[_SFPBRFSummaryItemButtonCardSection setButtonItemsAreTrailing:]
+ -[_SFPBRFSummaryItemButtonCardSection setButton_1:]
+ -[_SFPBRFSummaryItemButtonCardSection setButton_2:]
+ -[_SFPBRFSummaryItemButtonCardSection setButton_3:]
+ -[_SFPBRFSummaryItemButtonCardSection setText_1:]
+ -[_SFPBRFSummaryItemButtonCardSection setText_2:]
+ -[_SFPBRFSummaryItemButtonCardSection setText_2s:]
+ -[_SFPBRFSummaryItemButtonCardSection setText_3:]
+ -[_SFPBRFSummaryItemButtonCardSection setText_3s:]
+ -[_SFPBRFSummaryItemButtonCardSection setText_4:]
+ -[_SFPBRFSummaryItemButtonCardSection setThumbnail:]
+ -[_SFPBRFSummaryItemButtonCardSection text_1]
+ -[_SFPBRFSummaryItemButtonCardSection text_2AtIndex:]
+ -[_SFPBRFSummaryItemButtonCardSection text_2Count]
+ -[_SFPBRFSummaryItemButtonCardSection text_2s]
+ -[_SFPBRFSummaryItemButtonCardSection text_3AtIndex:]
+ -[_SFPBRFSummaryItemButtonCardSection text_3Count]
+ -[_SFPBRFSummaryItemButtonCardSection text_3s]
+ -[_SFPBRFSummaryItemButtonCardSection text_4]
+ -[_SFPBRFSummaryItemButtonCardSection thumbnail]
+ -[_SFPBRFSummaryItemButtonCardSection writeTo:]
+ -[_SFPBRFSummaryItemButtonCardSection(FacadeInitializer) initWithFacade:]
+ -[_SFPBRFSummaryItemImageRightCardSection .cxx_destruct]
+ -[_SFPBRFSummaryItemImageRightCardSection addText_2:]
+ -[_SFPBRFSummaryItemImageRightCardSection addText_3:]
+ -[_SFPBRFSummaryItemImageRightCardSection clearText_2]
+ -[_SFPBRFSummaryItemImageRightCardSection clearText_3]
+ -[_SFPBRFSummaryItemImageRightCardSection dictionaryRepresentation]
+ -[_SFPBRFSummaryItemImageRightCardSection hash]
+ -[_SFPBRFSummaryItemImageRightCardSection initWithDictionary:]
+ -[_SFPBRFSummaryItemImageRightCardSection initWithJSON:]
+ -[_SFPBRFSummaryItemImageRightCardSection isEqual:]
+ -[_SFPBRFSummaryItemImageRightCardSection jsonData]
+ -[_SFPBRFSummaryItemImageRightCardSection readFrom:]
+ -[_SFPBRFSummaryItemImageRightCardSection setText_1:]
+ -[_SFPBRFSummaryItemImageRightCardSection setText_2:]
+ -[_SFPBRFSummaryItemImageRightCardSection setText_2s:]
+ -[_SFPBRFSummaryItemImageRightCardSection setText_3:]
+ -[_SFPBRFSummaryItemImageRightCardSection setText_3s:]
+ -[_SFPBRFSummaryItemImageRightCardSection setText_4:]
+ -[_SFPBRFSummaryItemImageRightCardSection setThumbnail_1:]
+ -[_SFPBRFSummaryItemImageRightCardSection setThumbnail_2:]
+ -[_SFPBRFSummaryItemImageRightCardSection text_1]
+ -[_SFPBRFSummaryItemImageRightCardSection text_2AtIndex:]
+ -[_SFPBRFSummaryItemImageRightCardSection text_2Count]
+ -[_SFPBRFSummaryItemImageRightCardSection text_2s]
+ -[_SFPBRFSummaryItemImageRightCardSection text_3AtIndex:]
+ -[_SFPBRFSummaryItemImageRightCardSection text_3Count]
+ -[_SFPBRFSummaryItemImageRightCardSection text_3s]
+ -[_SFPBRFSummaryItemImageRightCardSection text_4]
+ -[_SFPBRFSummaryItemImageRightCardSection thumbnail_1]
+ -[_SFPBRFSummaryItemImageRightCardSection thumbnail_2]
+ -[_SFPBRFSummaryItemImageRightCardSection writeTo:]
+ -[_SFPBRFSummaryItemImageRightCardSection(FacadeInitializer) initWithFacade:]
+ -[_SFPBRFSummaryItemPlayerCardSection .cxx_destruct]
+ -[_SFPBRFSummaryItemPlayerCardSection dictionaryRepresentation]
+ -[_SFPBRFSummaryItemPlayerCardSection hash]
+ -[_SFPBRFSummaryItemPlayerCardSection initWithDictionary:]
+ -[_SFPBRFSummaryItemPlayerCardSection initWithJSON:]
+ -[_SFPBRFSummaryItemPlayerCardSection isEqual:]
+ -[_SFPBRFSummaryItemPlayerCardSection jsonData]
+ -[_SFPBRFSummaryItemPlayerCardSection player]
+ -[_SFPBRFSummaryItemPlayerCardSection readFrom:]
+ -[_SFPBRFSummaryItemPlayerCardSection setPlayer:]
+ -[_SFPBRFSummaryItemPlayerCardSection setText_1:]
+ -[_SFPBRFSummaryItemPlayerCardSection setText_2:]
+ -[_SFPBRFSummaryItemPlayerCardSection setText_3:]
+ -[_SFPBRFSummaryItemPlayerCardSection setText_4:]
+ -[_SFPBRFSummaryItemPlayerCardSection setThumbnail:]
+ -[_SFPBRFSummaryItemPlayerCardSection text_1]
+ -[_SFPBRFSummaryItemPlayerCardSection text_2]
+ -[_SFPBRFSummaryItemPlayerCardSection text_3]
+ -[_SFPBRFSummaryItemPlayerCardSection text_4]
+ -[_SFPBRFSummaryItemPlayerCardSection thumbnail]
+ -[_SFPBRFSummaryItemPlayerCardSection writeTo:]
+ -[_SFPBRFSummaryItemPlayerCardSection(FacadeInitializer) initWithFacade:]
+ -[_SFPBRFTableCell applySmallCaps]
+ -[_SFPBRFTableCell setApplySmallCaps:]
+ -[_SFPBRFTableRowCardSection setVertical_alignment:]
+ -[_SFPBRFTableRowCardSection vertical_alignment]
+ -[_SFPBRFUrlImage background_color]
+ -[_SFPBRFUrlImage setBackground_color:]
+ -[_SFPBRequestProductPageCommand .cxx_destruct]
+ -[_SFPBRequestProductPageCommand dictionaryRepresentation]
+ -[_SFPBRequestProductPageCommand distributorBundleIdentifier]
+ -[_SFPBRequestProductPageCommand hash]
+ -[_SFPBRequestProductPageCommand initWithDictionary:]
+ -[_SFPBRequestProductPageCommand initWithJSON:]
+ -[_SFPBRequestProductPageCommand isEqual:]
+ -[_SFPBRequestProductPageCommand itemIdentifier]
+ -[_SFPBRequestProductPageCommand jsonData]
+ -[_SFPBRequestProductPageCommand readFrom:]
+ -[_SFPBRequestProductPageCommand setDistributorBundleIdentifier:]
+ -[_SFPBRequestProductPageCommand setItemIdentifier:]
+ -[_SFPBRequestProductPageCommand setVersionIdentifier:]
+ -[_SFPBRequestProductPageCommand versionIdentifier]
+ -[_SFPBRequestProductPageCommand writeTo:]
+ -[_SFPBRequestProductPageCommand(FacadeInitializer) initWithFacade:]
+ -[_SFPBSearchInAppCommand searchInAppType]
+ -[_SFPBSearchInAppCommand setSearchInAppType:]
+ -[_SFPBShortcutsImage .cxx_destruct]
+ -[_SFPBShortcutsImage dictionaryRepresentation]
+ -[_SFPBShortcutsImage hash]
+ -[_SFPBShortcutsImage initWithDictionary:]
+ -[_SFPBShortcutsImage initWithJSON:]
+ -[_SFPBShortcutsImage isEqual:]
+ -[_SFPBShortcutsImage jsonData]
+ -[_SFPBShortcutsImage lnPropertyIdentifier]
+ -[_SFPBShortcutsImage readFrom:]
+ -[_SFPBShortcutsImage setLnPropertyIdentifier:]
+ -[_SFPBShortcutsImage writeTo:]
+ -[_SFPBStoreButtonItem .cxx_destruct]
+ -[_SFPBStoreButtonItem dictionaryRepresentation]
+ -[_SFPBStoreButtonItem hash]
+ -[_SFPBStoreButtonItem identifier]
+ -[_SFPBStoreButtonItem initWithDictionary:]
+ -[_SFPBStoreButtonItem initWithJSON:]
+ -[_SFPBStoreButtonItem isEqual:]
+ -[_SFPBStoreButtonItem jsonData]
+ -[_SFPBStoreButtonItem readFrom:]
+ -[_SFPBStoreButtonItem setIdentifier:]
+ -[_SFPBStoreButtonItem setShouldOpenAppAfterInstallCompletes:]
+ -[_SFPBStoreButtonItem setUniqueId:]
+ -[_SFPBStoreButtonItem shouldOpenAppAfterInstallCompletes]
+ -[_SFPBStoreButtonItem uniqueId]
+ -[_SFPBStoreButtonItem writeTo:]
+ -[_SFPBStoreButtonItem(FacadeInitializer) initWithFacade:]
+ -[_SFPBSymbolImage fillStyle]
+ -[_SFPBSymbolImage setFillStyle:]
+ -[_SFPBToggleWatchListStatusCommand setShouldAddToWatchList:]
+ -[_SFPBToggleWatchListStatusCommand shouldAddToWatchList]
+ -[_SFPBWatchListButtonItem setToggleButtonConfiguration:]
+ -[_SFPBWatchListButtonItem toggleButtonConfiguration]
+ GCC_except_table6127
+ GCC_except_table6922
+ _OBJC_CLASS_$_RFBinaryButtonCardSection
+ _OBJC_CLASS_$_RFButtonCardSection
+ _OBJC_CLASS_$_RFFont
+ _OBJC_CLASS_$_RFPrimaryHeaderStackedImageCardSection
+ _OBJC_CLASS_$_RFReferenceCenteredCardSection
+ _OBJC_CLASS_$_RFReferenceItemButtonCardSection
+ _OBJC_CLASS_$_RFReferenceItemLogoCardSection
+ _OBJC_CLASS_$_RFSecondaryHeaderEmphasizedCardSection
+ _OBJC_CLASS_$_RFSecondaryHeaderStandardCardSection
+ _OBJC_CLASS_$_RFSimpleItemReverseRichCardSection
+ _OBJC_CLASS_$_RFSimpleItemRichSearchResultCardSection
+ _OBJC_CLASS_$_RFSimpleItemVisualElementCardSection
+ _OBJC_CLASS_$_RFSummaryItemButtonCardSection
+ _OBJC_CLASS_$_RFSummaryItemImageRightCardSection
+ _OBJC_CLASS_$_RFSummaryItemPlayerCardSection
+ _OBJC_CLASS_$_RFSystemFont
+ _OBJC_CLASS_$_SFHashBucketDetail
+ _OBJC_CLASS_$_SFHashDetail
+ _OBJC_CLASS_$_SFPlayAudioButtonItem
+ _OBJC_CLASS_$_SFPlayWatchListItemButtonItem
+ _OBJC_CLASS_$_SFRequestProductPageCommand
+ _OBJC_CLASS_$_SFShortcutsImage
+ _OBJC_CLASS_$_SFStoreButtonItem
+ _OBJC_CLASS_$__SFPBHashBucketDetail
+ _OBJC_CLASS_$__SFPBHashBucketDetail_HashDetail
+ _OBJC_CLASS_$__SFPBPlayAudioButtonItem
+ _OBJC_CLASS_$__SFPBPlayWatchListItemButtonItem
+ _OBJC_CLASS_$__SFPBRFBinaryButtonCardSection
+ _OBJC_CLASS_$__SFPBRFButtonCardSection
+ _OBJC_CLASS_$__SFPBRFFont
+ _OBJC_CLASS_$__SFPBRFFont_RFSystemFont
+ _OBJC_CLASS_$__SFPBRFPrimaryHeaderStackedImageCardSection
+ _OBJC_CLASS_$__SFPBRFReferenceCenteredCardSection
+ _OBJC_CLASS_$__SFPBRFReferenceItemButtonCardSection
+ _OBJC_CLASS_$__SFPBRFReferenceItemLogoCardSection
+ _OBJC_CLASS_$__SFPBRFSecondaryHeaderEmphasizedCardSection
+ _OBJC_CLASS_$__SFPBRFSecondaryHeaderStandardCardSection
+ _OBJC_CLASS_$__SFPBRFSimpleItemReverseRichCardSection
+ _OBJC_CLASS_$__SFPBRFSimpleItemRichSearchResultCardSection
+ _OBJC_CLASS_$__SFPBRFSimpleItemVisualElementCardSection
+ _OBJC_CLASS_$__SFPBRFSummaryItemButtonCardSection
+ _OBJC_CLASS_$__SFPBRFSummaryItemImageRightCardSection
+ _OBJC_CLASS_$__SFPBRFSummaryItemPlayerCardSection
+ _OBJC_CLASS_$__SFPBRequestProductPageCommand
+ _OBJC_CLASS_$__SFPBShortcutsImage
+ _OBJC_CLASS_$__SFPBStoreButtonItem
+ _OBJC_IVAR_$_RFBinaryButtonCardSection._primary_button
+ _OBJC_IVAR_$_RFBinaryButtonCardSection._secondary_button
+ _OBJC_IVAR_$_RFButtonCardSection._button
+ _OBJC_IVAR_$_RFFactItemButtonCardSection._buttonItemsAreBottom
+ _OBJC_IVAR_$_RFFactItemButtonCardSection._has
+ _OBJC_IVAR_$_RFFactItemButtonCardSection._thumbnail2
+ _OBJC_IVAR_$_RFFactItemStandardCardSection._thumbnail2
+ _OBJC_IVAR_$_RFFont._has
+ _OBJC_IVAR_$_RFFont._name
+ _OBJC_IVAR_$_RFFont._system
+ _OBJC_IVAR_$_RFFormattedText._font
+ _OBJC_IVAR_$_RFPrimaryHeaderMarqueeCardSection._addTint
+ _OBJC_IVAR_$_RFPrimaryHeaderMarqueeCardSection._has
+ _OBJC_IVAR_$_RFPrimaryHeaderRichCardSection._addTint
+ _OBJC_IVAR_$_RFPrimaryHeaderRichCardSection._has
+ _OBJC_IVAR_$_RFPrimaryHeaderStackedImageCardSection._images
+ _OBJC_IVAR_$_RFPrimaryHeaderStackedImageCardSection._text_1
+ _OBJC_IVAR_$_RFPrimaryHeaderStackedImageCardSection._text_2
+ _OBJC_IVAR_$_RFPrimaryHeaderStandardCardSection._addTint
+ _OBJC_IVAR_$_RFPrimaryHeaderStandardCardSection._has
+ _OBJC_IVAR_$_RFReferenceCenteredCardSection._add_tint
+ _OBJC_IVAR_$_RFReferenceCenteredCardSection._has
+ _OBJC_IVAR_$_RFReferenceCenteredCardSection._text_1
+ _OBJC_IVAR_$_RFReferenceCenteredCardSection._text_2
+ _OBJC_IVAR_$_RFReferenceCenteredCardSection._text_3
+ _OBJC_IVAR_$_RFReferenceCenteredCardSection._text_4
+ _OBJC_IVAR_$_RFReferenceFootnoteCardSection._addTint
+ _OBJC_IVAR_$_RFReferenceFootnoteCardSection._has
+ _OBJC_IVAR_$_RFReferenceItemButtonCardSection._button_1
+ _OBJC_IVAR_$_RFReferenceItemLogoCardSection._thumbnail
+ _OBJC_IVAR_$_RFReferenceRichCardSection._addTint
+ _OBJC_IVAR_$_RFReferenceRichCardSection._has
+ _OBJC_IVAR_$_RFReferenceStandardCardSection._addTint
+ _OBJC_IVAR_$_RFReferenceStandardCardSection._has
+ _OBJC_IVAR_$_RFSecondaryHeaderEmphasizedCardSection._text_1
+ _OBJC_IVAR_$_RFSecondaryHeaderStandardCardSection._text_1
+ _OBJC_IVAR_$_RFSimpleItemReverseRichCardSection._text_1
+ _OBJC_IVAR_$_RFSimpleItemReverseRichCardSection._text_2
+ _OBJC_IVAR_$_RFSimpleItemReverseRichCardSection._text_3
+ _OBJC_IVAR_$_RFSimpleItemReverseRichCardSection._text_4
+ _OBJC_IVAR_$_RFSimpleItemReverseRichCardSection._thumbnail
+ _OBJC_IVAR_$_RFSimpleItemRichSearchResultCardSection._text_1
+ _OBJC_IVAR_$_RFSimpleItemRichSearchResultCardSection._text_2
+ _OBJC_IVAR_$_RFSimpleItemRichSearchResultCardSection._text_3
+ _OBJC_IVAR_$_RFSimpleItemRichSearchResultCardSection._text_4
+ _OBJC_IVAR_$_RFSimpleItemRichSearchResultCardSection._text_5
+ _OBJC_IVAR_$_RFSimpleItemRichSearchResultCardSection._text_6
+ _OBJC_IVAR_$_RFSimpleItemRichSearchResultCardSection._text_7
+ _OBJC_IVAR_$_RFSimpleItemRichSearchResultCardSection._text_8
+ _OBJC_IVAR_$_RFSimpleItemRichSearchResultCardSection._thumbnail
+ _OBJC_IVAR_$_RFSimpleItemVisualElementCardSection._footnote
+ _OBJC_IVAR_$_RFSimpleItemVisualElementCardSection._has
+ _OBJC_IVAR_$_RFSimpleItemVisualElementCardSection._horizontal_alignment
+ _OBJC_IVAR_$_RFSimpleItemVisualElementCardSection._image
+ _OBJC_IVAR_$_RFSimpleItemVisualElementCardSection._text_1
+ _OBJC_IVAR_$_RFSimpleItemVisualElementCardSection._text_2
+ _OBJC_IVAR_$_RFSummaryItemButtonCardSection._buttonItemsAreTrailing
+ _OBJC_IVAR_$_RFSummaryItemButtonCardSection._button_1
+ _OBJC_IVAR_$_RFSummaryItemButtonCardSection._button_2
+ _OBJC_IVAR_$_RFSummaryItemButtonCardSection._button_3
+ _OBJC_IVAR_$_RFSummaryItemButtonCardSection._has
+ _OBJC_IVAR_$_RFSummaryItemButtonCardSection._text_1
+ _OBJC_IVAR_$_RFSummaryItemButtonCardSection._text_2
+ _OBJC_IVAR_$_RFSummaryItemButtonCardSection._text_3
+ _OBJC_IVAR_$_RFSummaryItemButtonCardSection._text_4
+ _OBJC_IVAR_$_RFSummaryItemButtonCardSection._thumbnail
+ _OBJC_IVAR_$_RFSummaryItemImageRightCardSection._text_1
+ _OBJC_IVAR_$_RFSummaryItemImageRightCardSection._text_2
+ _OBJC_IVAR_$_RFSummaryItemImageRightCardSection._text_3
+ _OBJC_IVAR_$_RFSummaryItemImageRightCardSection._text_4
+ _OBJC_IVAR_$_RFSummaryItemImageRightCardSection._thumbnail_1
+ _OBJC_IVAR_$_RFSummaryItemImageRightCardSection._thumbnail_2
+ _OBJC_IVAR_$_RFSummaryItemPlayerCardSection._player
+ _OBJC_IVAR_$_RFSummaryItemPlayerCardSection._text_1
+ _OBJC_IVAR_$_RFSummaryItemPlayerCardSection._text_2
+ _OBJC_IVAR_$_RFSummaryItemPlayerCardSection._text_3
+ _OBJC_IVAR_$_RFSummaryItemPlayerCardSection._text_4
+ _OBJC_IVAR_$_RFSummaryItemPlayerCardSection._thumbnail
+ _OBJC_IVAR_$_RFSystemFont._has
+ _OBJC_IVAR_$_RFSystemFont._size
+ _OBJC_IVAR_$_RFSystemFont._weight
+ _OBJC_IVAR_$_RFTableCell._applySmallCaps
+ _OBJC_IVAR_$_RFTableRowCardSection._has
+ _OBJC_IVAR_$_RFTableRowCardSection._vertical_alignment
+ _OBJC_IVAR_$_RFUrlImage._background_color
+ _OBJC_IVAR_$_SFCardSectionValue._rfBinaryButtonCardSection
+ _OBJC_IVAR_$_SFCardSectionValue._rfButtonCardSection
+ _OBJC_IVAR_$_SFCardSectionValue._rfPrimaryHeaderStackedImageCardSection
+ _OBJC_IVAR_$_SFCardSectionValue._rfReferenceCenteredCardSection
+ _OBJC_IVAR_$_SFCardSectionValue._rfReferenceItemButtonCardSection
+ _OBJC_IVAR_$_SFCardSectionValue._rfReferenceItemLogoCardSection
+ _OBJC_IVAR_$_SFCardSectionValue._rfSecondaryHeaderEmphasizedCardSection
+ _OBJC_IVAR_$_SFCardSectionValue._rfSecondaryHeaderStandardCardSection
+ _OBJC_IVAR_$_SFCardSectionValue._rfSimpleItemReverseRichCardSection
+ _OBJC_IVAR_$_SFCardSectionValue._rfSimpleItemRichSearchResultCardSection
+ _OBJC_IVAR_$_SFCardSectionValue._rfSimpleItemVisualElementCardSection
+ _OBJC_IVAR_$_SFCardSectionValue._rfSummaryItemButtonCardSection
+ _OBJC_IVAR_$_SFCardSectionValue._rfSummaryItemImageRightCardSection
+ _OBJC_IVAR_$_SFCardSectionValue._rfSummaryItemPlayerCardSection
+ _OBJC_IVAR_$_SFCollectionStyleGrid._gridStyle
+ _OBJC_IVAR_$_SFCollectionStyleRow._isInsetGrouped
+ _OBJC_IVAR_$_SFContactButtonItem._actionTypesToShow
+ _OBJC_IVAR_$_SFDomainEngagementScore._iFunScore
+ _OBJC_IVAR_$_SFHashBucketDetail._hash_details
+ _OBJC_IVAR_$_SFHashBucketDetail._hash_prefix
+ _OBJC_IVAR_$_SFHashDetail._full_hash
+ _OBJC_IVAR_$_SFHashDetail._has
+ _OBJC_IVAR_$_SFHashDetail._has_ee
+ _OBJC_IVAR_$_SFHashDetail._has_summary
+ _OBJC_IVAR_$_SFMediaMetadata._mediaIdentifier
+ _OBJC_IVAR_$_SFPlayAudioButtonItem._mediaMetadata
+ _OBJC_IVAR_$_SFPlayAudioButtonItem._toggleButtonConfiguration
+ _OBJC_IVAR_$_SFPlayMediaCommand._shouldPause
+ _OBJC_IVAR_$_SFPlayWatchListItemButtonItem._image
+ _OBJC_IVAR_$_SFPlayWatchListItemButtonItem._title
+ _OBJC_IVAR_$_SFPlayWatchListItemButtonItem._watchListItem
+ _OBJC_IVAR_$_SFRequestProductPageCommand._distributorBundleIdentifier
+ _OBJC_IVAR_$_SFRequestProductPageCommand._has
+ _OBJC_IVAR_$_SFRequestProductPageCommand._itemIdentifier
+ _OBJC_IVAR_$_SFRequestProductPageCommand._versionIdentifier
+ _OBJC_IVAR_$_SFSearchInAppCommand._has
+ _OBJC_IVAR_$_SFSearchInAppCommand._searchInAppType
+ _OBJC_IVAR_$_SFSearchResult._indexOfResultInSectionWhenRanked
+ _OBJC_IVAR_$_SFSearchResult._indexOfSectionWhenRanked
+ _OBJC_IVAR_$_SFShortcutsImage._lnPropertyIdentifier
+ _OBJC_IVAR_$_SFStoreButtonItem._has
+ _OBJC_IVAR_$_SFStoreButtonItem._identifier
+ _OBJC_IVAR_$_SFStoreButtonItem._shouldOpenAppAfterInstallCompletes
+ _OBJC_IVAR_$_SFSymbolImage._fillStyle
+ _OBJC_IVAR_$_SFToggleWatchListStatusCommand._has
+ _OBJC_IVAR_$_SFToggleWatchListStatusCommand._shouldAddToWatchList
+ _OBJC_IVAR_$_SFWatchListButtonItem._toggleButtonConfiguration
+ _OBJC_IVAR_$__SFPBButtonItem._playAudioButtonItem
+ _OBJC_IVAR_$__SFPBButtonItem._playWatchListItemButtonItem
+ _OBJC_IVAR_$__SFPBButtonItem._storeButtonItem
+ _OBJC_IVAR_$__SFPBCardSectionValue._rfBinaryButtonCardSection
+ _OBJC_IVAR_$__SFPBCardSectionValue._rfButtonCardSection
+ _OBJC_IVAR_$__SFPBCardSectionValue._rfPrimaryHeaderStackedImageCardSection
+ _OBJC_IVAR_$__SFPBCardSectionValue._rfReferenceCenteredCardSection
+ _OBJC_IVAR_$__SFPBCardSectionValue._rfReferenceItemButtonCardSection
+ _OBJC_IVAR_$__SFPBCardSectionValue._rfReferenceItemLogoCardSection
+ _OBJC_IVAR_$__SFPBCardSectionValue._rfSecondaryHeaderEmphasizedCardSection
+ _OBJC_IVAR_$__SFPBCardSectionValue._rfSecondaryHeaderStandardCardSection
+ _OBJC_IVAR_$__SFPBCardSectionValue._rfSimpleItemReverseRichCardSection
+ _OBJC_IVAR_$__SFPBCardSectionValue._rfSimpleItemRichSearchResultCardSection
+ _OBJC_IVAR_$__SFPBCardSectionValue._rfSimpleItemVisualElementCardSection
+ _OBJC_IVAR_$__SFPBCardSectionValue._rfSummaryItemButtonCardSection
+ _OBJC_IVAR_$__SFPBCardSectionValue._rfSummaryItemImageRightCardSection
+ _OBJC_IVAR_$__SFPBCardSectionValue._rfSummaryItemPlayerCardSection
+ _OBJC_IVAR_$__SFPBCollectionStyleGrid._gridStyle
+ _OBJC_IVAR_$__SFPBCollectionStyleRow._isInsetGrouped
+ _OBJC_IVAR_$__SFPBCommand._requestProductPageCommand
+ _OBJC_IVAR_$__SFPBContactButtonItem._actionTypesToShows
+ _OBJC_IVAR_$__SFPBDomainEngagementScore._iFunScore
+ _OBJC_IVAR_$__SFPBHashBucketDetail._hash_details
+ _OBJC_IVAR_$__SFPBHashBucketDetail._hash_prefix
+ _OBJC_IVAR_$__SFPBHashBucketDetail_HashDetail._full_hash
+ _OBJC_IVAR_$__SFPBHashBucketDetail_HashDetail._has_ee
+ _OBJC_IVAR_$__SFPBHashBucketDetail_HashDetail._has_summary
+ _OBJC_IVAR_$__SFPBImage._shortcutsImage
+ _OBJC_IVAR_$__SFPBMediaMetadata._mediaIdentifier
+ _OBJC_IVAR_$__SFPBPlayAudioButtonItem._mediaMetadata
+ _OBJC_IVAR_$__SFPBPlayAudioButtonItem._toggleButtonConfiguration
+ _OBJC_IVAR_$__SFPBPlayAudioButtonItem._uniqueId
+ _OBJC_IVAR_$__SFPBPlayMediaCommand._shouldPause
+ _OBJC_IVAR_$__SFPBPlayWatchListItemButtonItem._image
+ _OBJC_IVAR_$__SFPBPlayWatchListItemButtonItem._title
+ _OBJC_IVAR_$__SFPBPlayWatchListItemButtonItem._uniqueId
+ _OBJC_IVAR_$__SFPBPlayWatchListItemButtonItem._watchListItem
+ _OBJC_IVAR_$__SFPBRFBinaryButtonCardSection._primary_button
+ _OBJC_IVAR_$__SFPBRFBinaryButtonCardSection._secondary_button
+ _OBJC_IVAR_$__SFPBRFButtonCardSection._button
+ _OBJC_IVAR_$__SFPBRFFactItemButtonCardSection._buttonItemsAreBottom
+ _OBJC_IVAR_$__SFPBRFFactItemButtonCardSection._thumbnail2
+ _OBJC_IVAR_$__SFPBRFFactItemStandardCardSection._thumbnail2
+ _OBJC_IVAR_$__SFPBRFFont._name
+ _OBJC_IVAR_$__SFPBRFFont._system
+ _OBJC_IVAR_$__SFPBRFFont._whichValue
+ _OBJC_IVAR_$__SFPBRFFont_RFSystemFont._size
+ _OBJC_IVAR_$__SFPBRFFont_RFSystemFont._weight
+ _OBJC_IVAR_$__SFPBRFFormattedText._font
+ _OBJC_IVAR_$__SFPBRFPrimaryHeaderMarqueeCardSection._addTint
+ _OBJC_IVAR_$__SFPBRFPrimaryHeaderRichCardSection._addTint
+ _OBJC_IVAR_$__SFPBRFPrimaryHeaderStackedImageCardSection._images
+ _OBJC_IVAR_$__SFPBRFPrimaryHeaderStackedImageCardSection._text_1
+ _OBJC_IVAR_$__SFPBRFPrimaryHeaderStackedImageCardSection._text_2
+ _OBJC_IVAR_$__SFPBRFPrimaryHeaderStandardCardSection._addTint
+ _OBJC_IVAR_$__SFPBRFReferenceCenteredCardSection._add_tint
+ _OBJC_IVAR_$__SFPBRFReferenceCenteredCardSection._text_1
+ _OBJC_IVAR_$__SFPBRFReferenceCenteredCardSection._text_2
+ _OBJC_IVAR_$__SFPBRFReferenceCenteredCardSection._text_3
+ _OBJC_IVAR_$__SFPBRFReferenceCenteredCardSection._text_4
+ _OBJC_IVAR_$__SFPBRFReferenceFootnoteCardSection._addTint
+ _OBJC_IVAR_$__SFPBRFReferenceItemButtonCardSection._button_1
+ _OBJC_IVAR_$__SFPBRFReferenceItemLogoCardSection._thumbnail
+ _OBJC_IVAR_$__SFPBRFReferenceRichCardSection._addTint
+ _OBJC_IVAR_$__SFPBRFReferenceStandardCardSection._addTint
+ _OBJC_IVAR_$__SFPBRFSecondaryHeaderEmphasizedCardSection._text_1
+ _OBJC_IVAR_$__SFPBRFSecondaryHeaderStandardCardSection._text_1
+ _OBJC_IVAR_$__SFPBRFSimpleItemReverseRichCardSection._text_1
+ _OBJC_IVAR_$__SFPBRFSimpleItemReverseRichCardSection._text_2
+ _OBJC_IVAR_$__SFPBRFSimpleItemReverseRichCardSection._text_3s
+ _OBJC_IVAR_$__SFPBRFSimpleItemReverseRichCardSection._text_4
+ _OBJC_IVAR_$__SFPBRFSimpleItemReverseRichCardSection._thumbnail
+ _OBJC_IVAR_$__SFPBRFSimpleItemRichSearchResultCardSection._text_1
+ _OBJC_IVAR_$__SFPBRFSimpleItemRichSearchResultCardSection._text_2
+ _OBJC_IVAR_$__SFPBRFSimpleItemRichSearchResultCardSection._text_3s
+ _OBJC_IVAR_$__SFPBRFSimpleItemRichSearchResultCardSection._text_4
+ _OBJC_IVAR_$__SFPBRFSimpleItemRichSearchResultCardSection._text_5s
+ _OBJC_IVAR_$__SFPBRFSimpleItemRichSearchResultCardSection._text_6
+ _OBJC_IVAR_$__SFPBRFSimpleItemRichSearchResultCardSection._text_7
+ _OBJC_IVAR_$__SFPBRFSimpleItemRichSearchResultCardSection._text_8
+ _OBJC_IVAR_$__SFPBRFSimpleItemRichSearchResultCardSection._thumbnail
+ _OBJC_IVAR_$__SFPBRFSimpleItemVisualElementCardSection._footnote
+ _OBJC_IVAR_$__SFPBRFSimpleItemVisualElementCardSection._horizontal_alignment
+ _OBJC_IVAR_$__SFPBRFSimpleItemVisualElementCardSection._image
+ _OBJC_IVAR_$__SFPBRFSimpleItemVisualElementCardSection._text_1
+ _OBJC_IVAR_$__SFPBRFSimpleItemVisualElementCardSection._text_2
+ _OBJC_IVAR_$__SFPBRFSummaryItemButtonCardSection._buttonItemsAreTrailing
+ _OBJC_IVAR_$__SFPBRFSummaryItemButtonCardSection._button_1
+ _OBJC_IVAR_$__SFPBRFSummaryItemButtonCardSection._button_2
+ _OBJC_IVAR_$__SFPBRFSummaryItemButtonCardSection._button_3
+ _OBJC_IVAR_$__SFPBRFSummaryItemButtonCardSection._text_1
+ _OBJC_IVAR_$__SFPBRFSummaryItemButtonCardSection._text_2s
+ _OBJC_IVAR_$__SFPBRFSummaryItemButtonCardSection._text_3s
+ _OBJC_IVAR_$__SFPBRFSummaryItemButtonCardSection._text_4
+ _OBJC_IVAR_$__SFPBRFSummaryItemButtonCardSection._thumbnail
+ _OBJC_IVAR_$__SFPBRFSummaryItemImageRightCardSection._text_1
+ _OBJC_IVAR_$__SFPBRFSummaryItemImageRightCardSection._text_2s
+ _OBJC_IVAR_$__SFPBRFSummaryItemImageRightCardSection._text_3s
+ _OBJC_IVAR_$__SFPBRFSummaryItemImageRightCardSection._text_4
+ _OBJC_IVAR_$__SFPBRFSummaryItemImageRightCardSection._thumbnail_1
+ _OBJC_IVAR_$__SFPBRFSummaryItemImageRightCardSection._thumbnail_2
+ _OBJC_IVAR_$__SFPBRFSummaryItemPlayerCardSection._player
+ _OBJC_IVAR_$__SFPBRFSummaryItemPlayerCardSection._text_1
+ _OBJC_IVAR_$__SFPBRFSummaryItemPlayerCardSection._text_2
+ _OBJC_IVAR_$__SFPBRFSummaryItemPlayerCardSection._text_3
+ _OBJC_IVAR_$__SFPBRFSummaryItemPlayerCardSection._text_4
+ _OBJC_IVAR_$__SFPBRFSummaryItemPlayerCardSection._thumbnail
+ _OBJC_IVAR_$__SFPBRFTableCell._applySmallCaps
+ _OBJC_IVAR_$__SFPBRFTableRowCardSection._vertical_alignment
+ _OBJC_IVAR_$__SFPBRFUrlImage._background_color
+ _OBJC_IVAR_$__SFPBRequestProductPageCommand._distributorBundleIdentifier
+ _OBJC_IVAR_$__SFPBRequestProductPageCommand._itemIdentifier
+ _OBJC_IVAR_$__SFPBRequestProductPageCommand._versionIdentifier
+ _OBJC_IVAR_$__SFPBSearchInAppCommand._searchInAppType
+ _OBJC_IVAR_$__SFPBShortcutsImage._lnPropertyIdentifier
+ _OBJC_IVAR_$__SFPBStoreButtonItem._identifier
+ _OBJC_IVAR_$__SFPBStoreButtonItem._shouldOpenAppAfterInstallCompletes
+ _OBJC_IVAR_$__SFPBStoreButtonItem._uniqueId
+ _OBJC_IVAR_$__SFPBSymbolImage._fillStyle
+ _OBJC_IVAR_$__SFPBToggleWatchListStatusCommand._shouldAddToWatchList
+ _OBJC_IVAR_$__SFPBWatchListButtonItem._toggleButtonConfiguration
+ _OBJC_METACLASS_$_RFBinaryButtonCardSection
+ _OBJC_METACLASS_$_RFButtonCardSection
+ _OBJC_METACLASS_$_RFFont
+ _OBJC_METACLASS_$_RFPrimaryHeaderStackedImageCardSection
+ _OBJC_METACLASS_$_RFReferenceCenteredCardSection
+ _OBJC_METACLASS_$_RFReferenceItemButtonCardSection
+ _OBJC_METACLASS_$_RFReferenceItemLogoCardSection
+ _OBJC_METACLASS_$_RFSecondaryHeaderEmphasizedCardSection
+ _OBJC_METACLASS_$_RFSecondaryHeaderStandardCardSection
+ _OBJC_METACLASS_$_RFSimpleItemReverseRichCardSection
+ _OBJC_METACLASS_$_RFSimpleItemRichSearchResultCardSection
+ _OBJC_METACLASS_$_RFSimpleItemVisualElementCardSection
+ _OBJC_METACLASS_$_RFSummaryItemButtonCardSection
+ _OBJC_METACLASS_$_RFSummaryItemImageRightCardSection
+ _OBJC_METACLASS_$_RFSummaryItemPlayerCardSection
+ _OBJC_METACLASS_$_RFSystemFont
+ _OBJC_METACLASS_$_SFHashBucketDetail
+ _OBJC_METACLASS_$_SFHashDetail
+ _OBJC_METACLASS_$_SFPlayAudioButtonItem
+ _OBJC_METACLASS_$_SFPlayWatchListItemButtonItem
+ _OBJC_METACLASS_$_SFRequestProductPageCommand
+ _OBJC_METACLASS_$_SFShortcutsImage
+ _OBJC_METACLASS_$_SFStoreButtonItem
+ _OBJC_METACLASS_$__SFPBHashBucketDetail
+ _OBJC_METACLASS_$__SFPBHashBucketDetail_HashDetail
+ _OBJC_METACLASS_$__SFPBPlayAudioButtonItem
+ _OBJC_METACLASS_$__SFPBPlayWatchListItemButtonItem
+ _OBJC_METACLASS_$__SFPBRFBinaryButtonCardSection
+ _OBJC_METACLASS_$__SFPBRFButtonCardSection
+ _OBJC_METACLASS_$__SFPBRFFont
+ _OBJC_METACLASS_$__SFPBRFFont_RFSystemFont
+ _OBJC_METACLASS_$__SFPBRFPrimaryHeaderStackedImageCardSection
+ _OBJC_METACLASS_$__SFPBRFReferenceCenteredCardSection
+ _OBJC_METACLASS_$__SFPBRFReferenceItemButtonCardSection
+ _OBJC_METACLASS_$__SFPBRFReferenceItemLogoCardSection
+ _OBJC_METACLASS_$__SFPBRFSecondaryHeaderEmphasizedCardSection
+ _OBJC_METACLASS_$__SFPBRFSecondaryHeaderStandardCardSection
+ _OBJC_METACLASS_$__SFPBRFSimpleItemReverseRichCardSection
+ _OBJC_METACLASS_$__SFPBRFSimpleItemRichSearchResultCardSection
+ _OBJC_METACLASS_$__SFPBRFSimpleItemVisualElementCardSection
+ _OBJC_METACLASS_$__SFPBRFSummaryItemButtonCardSection
+ _OBJC_METACLASS_$__SFPBRFSummaryItemImageRightCardSection
+ _OBJC_METACLASS_$__SFPBRFSummaryItemPlayerCardSection
+ _OBJC_METACLASS_$__SFPBRequestProductPageCommand
+ _OBJC_METACLASS_$__SFPBShortcutsImage
+ _OBJC_METACLASS_$__SFPBStoreButtonItem
+ _PARLogHandleForCategory.logHandles.0.56502
+ _PARLogHandleForCategory.logHandles.0.60064
+ _PARLogHandleForCategory.logHandles.1.56496
+ _PARLogHandleForCategory.logHandles.1.60061
+ _PARLogHandleForCategory.logHandles.2.56504
+ _PARLogHandleForCategory.logHandles.2.60066
+ _PARLogHandleForCategory.logHandles.3.56505
+ _PARLogHandleForCategory.logHandles.3.60067
+ _PARLogHandleForCategory.logHandles.4.56506
+ _PARLogHandleForCategory.logHandles.4.60069
+ _PARLogHandleForCategory.logHandles.5.56507
+ _PARLogHandleForCategory.logHandles.5.60070
+ _PARLogHandleForCategory.onceToken.56494
+ _PARLogHandleForCategory.onceToken.60060
+ __OBJC_$_CLASS_METHODS_RFBinaryButtonCardSection(ProtobufInitializer)
+ __OBJC_$_CLASS_METHODS_RFButtonCardSection(ProtobufInitializer)
+ __OBJC_$_CLASS_METHODS_RFFont(ProtobufInitializer)
+ __OBJC_$_CLASS_METHODS_RFPrimaryHeaderStackedImageCardSection(ProtobufInitializer)
+ __OBJC_$_CLASS_METHODS_RFReferenceCenteredCardSection(ProtobufInitializer)
+ __OBJC_$_CLASS_METHODS_RFReferenceItemButtonCardSection(ProtobufInitializer)
+ __OBJC_$_CLASS_METHODS_RFReferenceItemLogoCardSection(ProtobufInitializer)
+ __OBJC_$_CLASS_METHODS_RFSecondaryHeaderEmphasizedCardSection(ProtobufInitializer)
+ __OBJC_$_CLASS_METHODS_RFSecondaryHeaderStandardCardSection(ProtobufInitializer)
+ __OBJC_$_CLASS_METHODS_RFSimpleItemReverseRichCardSection(ProtobufInitializer)
+ __OBJC_$_CLASS_METHODS_RFSimpleItemRichSearchResultCardSection(ProtobufInitializer)
+ __OBJC_$_CLASS_METHODS_RFSimpleItemVisualElementCardSection(ProtobufInitializer)
+ __OBJC_$_CLASS_METHODS_RFSummaryItemButtonCardSection(ProtobufInitializer)
+ __OBJC_$_CLASS_METHODS_RFSummaryItemImageRightCardSection(ProtobufInitializer)
+ __OBJC_$_CLASS_METHODS_RFSummaryItemPlayerCardSection(ProtobufInitializer)
+ __OBJC_$_CLASS_METHODS_RFSystemFont(ProtobufInitializer)
+ __OBJC_$_CLASS_METHODS_SFDomainEngagementScore(ProtobufInitializer|Handwritten)
+ __OBJC_$_CLASS_METHODS_SFEngagementSignal(ProtobufInitializer|Handwritten)
+ __OBJC_$_CLASS_METHODS_SFHashBucketDetail(ProtobufInitializer)
+ __OBJC_$_CLASS_METHODS_SFHashDetail(ProtobufInitializer)
+ __OBJC_$_CLASS_METHODS_SFPlayAudioButtonItem(ProtobufInitializer)
+ __OBJC_$_CLASS_METHODS_SFPlayWatchListItemButtonItem(ProtobufInitializer)
+ __OBJC_$_CLASS_METHODS_SFRequestProductPageCommand(ProtobufInitializer)
+ __OBJC_$_CLASS_METHODS_SFShortcutsImage
+ __OBJC_$_CLASS_METHODS_SFStoreButtonItem(ProtobufInitializer)
+ __OBJC_$_CLASS_PROP_LIST_RFBinaryButtonCardSection
+ __OBJC_$_CLASS_PROP_LIST_RFButtonCardSection
+ __OBJC_$_CLASS_PROP_LIST_RFFont
+ __OBJC_$_CLASS_PROP_LIST_RFPrimaryHeaderStackedImageCardSection
+ __OBJC_$_CLASS_PROP_LIST_RFReferenceCenteredCardSection
+ __OBJC_$_CLASS_PROP_LIST_RFReferenceItemButtonCardSection
+ __OBJC_$_CLASS_PROP_LIST_RFReferenceItemLogoCardSection
+ __OBJC_$_CLASS_PROP_LIST_RFSecondaryHeaderEmphasizedCardSection
+ __OBJC_$_CLASS_PROP_LIST_RFSecondaryHeaderStandardCardSection
+ __OBJC_$_CLASS_PROP_LIST_RFSimpleItemReverseRichCardSection
+ __OBJC_$_CLASS_PROP_LIST_RFSimpleItemRichSearchResultCardSection
+ __OBJC_$_CLASS_PROP_LIST_RFSimpleItemVisualElementCardSection
+ __OBJC_$_CLASS_PROP_LIST_RFSummaryItemButtonCardSection
+ __OBJC_$_CLASS_PROP_LIST_RFSummaryItemImageRightCardSection
+ __OBJC_$_CLASS_PROP_LIST_RFSummaryItemPlayerCardSection
+ __OBJC_$_CLASS_PROP_LIST_RFSystemFont
+ __OBJC_$_CLASS_PROP_LIST_SFHashBucketDetail
+ __OBJC_$_CLASS_PROP_LIST_SFHashDetail
+ __OBJC_$_CLASS_PROP_LIST_SFPlayAudioButtonItem
+ __OBJC_$_CLASS_PROP_LIST_SFPlayWatchListItemButtonItem
+ __OBJC_$_CLASS_PROP_LIST_SFRequestProductPageCommand
+ __OBJC_$_CLASS_PROP_LIST_SFShortcutsImage
+ __OBJC_$_CLASS_PROP_LIST_SFStoreButtonItem
+ __OBJC_$_CLASS_PROP_LIST__SFPBHashBucketDetail
+ __OBJC_$_CLASS_PROP_LIST__SFPBHashBucketDetail_HashDetail
+ __OBJC_$_CLASS_PROP_LIST__SFPBPlayAudioButtonItem
+ __OBJC_$_CLASS_PROP_LIST__SFPBPlayWatchListItemButtonItem
+ __OBJC_$_CLASS_PROP_LIST__SFPBRFBinaryButtonCardSection
+ __OBJC_$_CLASS_PROP_LIST__SFPBRFButtonCardSection
+ __OBJC_$_CLASS_PROP_LIST__SFPBRFFont
+ __OBJC_$_CLASS_PROP_LIST__SFPBRFFont_RFSystemFont
+ __OBJC_$_CLASS_PROP_LIST__SFPBRFPrimaryHeaderStackedImageCardSection
+ __OBJC_$_CLASS_PROP_LIST__SFPBRFReferenceCenteredCardSection
+ __OBJC_$_CLASS_PROP_LIST__SFPBRFReferenceItemButtonCardSection
+ __OBJC_$_CLASS_PROP_LIST__SFPBRFReferenceItemLogoCardSection
+ __OBJC_$_CLASS_PROP_LIST__SFPBRFSecondaryHeaderEmphasizedCardSection
+ __OBJC_$_CLASS_PROP_LIST__SFPBRFSecondaryHeaderStandardCardSection
+ __OBJC_$_CLASS_PROP_LIST__SFPBRFSimpleItemReverseRichCardSection
+ __OBJC_$_CLASS_PROP_LIST__SFPBRFSimpleItemRichSearchResultCardSection
+ __OBJC_$_CLASS_PROP_LIST__SFPBRFSimpleItemVisualElementCardSection
+ __OBJC_$_CLASS_PROP_LIST__SFPBRFSummaryItemButtonCardSection
+ __OBJC_$_CLASS_PROP_LIST__SFPBRFSummaryItemImageRightCardSection
+ __OBJC_$_CLASS_PROP_LIST__SFPBRFSummaryItemPlayerCardSection
+ __OBJC_$_CLASS_PROP_LIST__SFPBRequestProductPageCommand
+ __OBJC_$_CLASS_PROP_LIST__SFPBShortcutsImage
+ __OBJC_$_CLASS_PROP_LIST__SFPBStoreButtonItem
+ __OBJC_$_INSTANCE_METHODS_RFBinaryButtonCardSection(ProtobufInitializer)
+ __OBJC_$_INSTANCE_METHODS_RFButtonCardSection(ProtobufInitializer)
+ __OBJC_$_INSTANCE_METHODS_RFFont(ProtobufInitializer)
+ __OBJC_$_INSTANCE_METHODS_RFPrimaryHeaderStackedImageCardSection(ProtobufInitializer)
+ __OBJC_$_INSTANCE_METHODS_RFReferenceCenteredCardSection(ProtobufInitializer)
+ __OBJC_$_INSTANCE_METHODS_RFReferenceItemButtonCardSection(ProtobufInitializer)
+ __OBJC_$_INSTANCE_METHODS_RFReferenceItemLogoCardSection(ProtobufInitializer)
+ __OBJC_$_INSTANCE_METHODS_RFSecondaryHeaderEmphasizedCardSection(ProtobufInitializer)
+ __OBJC_$_INSTANCE_METHODS_RFSecondaryHeaderStandardCardSection(ProtobufInitializer)
+ __OBJC_$_INSTANCE_METHODS_RFSimpleItemReverseRichCardSection(ProtobufInitializer)
+ __OBJC_$_INSTANCE_METHODS_RFSimpleItemRichSearchResultCardSection(ProtobufInitializer)
+ __OBJC_$_INSTANCE_METHODS_RFSimpleItemVisualElementCardSection(ProtobufInitializer)
+ __OBJC_$_INSTANCE_METHODS_RFSummaryItemButtonCardSection(ProtobufInitializer)
+ __OBJC_$_INSTANCE_METHODS_RFSummaryItemImageRightCardSection(ProtobufInitializer)
+ __OBJC_$_INSTANCE_METHODS_RFSummaryItemPlayerCardSection(ProtobufInitializer)
+ __OBJC_$_INSTANCE_METHODS_RFSystemFont(ProtobufInitializer)
+ __OBJC_$_INSTANCE_METHODS_SFDomainEngagementScore(ProtobufInitializer|Handwritten)
+ __OBJC_$_INSTANCE_METHODS_SFEngagementSignal(ProtobufInitializer|Handwritten)
+ __OBJC_$_INSTANCE_METHODS_SFHashBucketDetail(ProtobufInitializer)
+ __OBJC_$_INSTANCE_METHODS_SFHashDetail(ProtobufInitializer)
+ __OBJC_$_INSTANCE_METHODS_SFPlayAudioButtonItem(ProtobufInitializer)
+ __OBJC_$_INSTANCE_METHODS_SFPlayWatchListItemButtonItem(ProtobufInitializer)
+ __OBJC_$_INSTANCE_METHODS_SFRequestProductPageCommand(ProtobufInitializer)
+ __OBJC_$_INSTANCE_METHODS_SFShortcutsImage
+ __OBJC_$_INSTANCE_METHODS_SFStoreButtonItem(ProtobufInitializer)
+ __OBJC_$_INSTANCE_METHODS__SFPBHashBucketDetail(FacadeInitializer)
+ __OBJC_$_INSTANCE_METHODS__SFPBHashBucketDetail_HashDetail(FacadeInitializer)
+ __OBJC_$_INSTANCE_METHODS__SFPBPlayAudioButtonItem(FacadeInitializer)
+ __OBJC_$_INSTANCE_METHODS__SFPBPlayWatchListItemButtonItem(FacadeInitializer)
+ __OBJC_$_INSTANCE_METHODS__SFPBRFBinaryButtonCardSection(FacadeInitializer)
+ __OBJC_$_INSTANCE_METHODS__SFPBRFButtonCardSection(FacadeInitializer)
+ __OBJC_$_INSTANCE_METHODS__SFPBRFFont(FacadeInitializer)
+ __OBJC_$_INSTANCE_METHODS__SFPBRFFont_RFSystemFont(FacadeInitializer)
+ __OBJC_$_INSTANCE_METHODS__SFPBRFPrimaryHeaderStackedImageCardSection(FacadeInitializer)
+ __OBJC_$_INSTANCE_METHODS__SFPBRFReferenceCenteredCardSection(FacadeInitializer)
+ __OBJC_$_INSTANCE_METHODS__SFPBRFReferenceItemButtonCardSection(FacadeInitializer)
+ __OBJC_$_INSTANCE_METHODS__SFPBRFReferenceItemLogoCardSection(FacadeInitializer)
+ __OBJC_$_INSTANCE_METHODS__SFPBRFSecondaryHeaderEmphasizedCardSection(FacadeInitializer)
+ __OBJC_$_INSTANCE_METHODS__SFPBRFSecondaryHeaderStandardCardSection(FacadeInitializer)
+ __OBJC_$_INSTANCE_METHODS__SFPBRFSimpleItemReverseRichCardSection(FacadeInitializer)
+ __OBJC_$_INSTANCE_METHODS__SFPBRFSimpleItemRichSearchResultCardSection(FacadeInitializer)
+ __OBJC_$_INSTANCE_METHODS__SFPBRFSimpleItemVisualElementCardSection(FacadeInitializer)
+ __OBJC_$_INSTANCE_METHODS__SFPBRFSummaryItemButtonCardSection(FacadeInitializer)
+ __OBJC_$_INSTANCE_METHODS__SFPBRFSummaryItemImageRightCardSection(FacadeInitializer)
+ __OBJC_$_INSTANCE_METHODS__SFPBRFSummaryItemPlayerCardSection(FacadeInitializer)
+ __OBJC_$_INSTANCE_METHODS__SFPBRequestProductPageCommand(FacadeInitializer)
+ __OBJC_$_INSTANCE_METHODS__SFPBShortcutsImage
+ __OBJC_$_INSTANCE_METHODS__SFPBStoreButtonItem(FacadeInitializer)
+ __OBJC_$_INSTANCE_VARIABLES_RFBinaryButtonCardSection
+ __OBJC_$_INSTANCE_VARIABLES_RFButtonCardSection
+ __OBJC_$_INSTANCE_VARIABLES_RFFont
+ __OBJC_$_INSTANCE_VARIABLES_RFPrimaryHeaderStackedImageCardSection
+ __OBJC_$_INSTANCE_VARIABLES_RFReferenceCenteredCardSection
+ __OBJC_$_INSTANCE_VARIABLES_RFReferenceItemButtonCardSection
+ __OBJC_$_INSTANCE_VARIABLES_RFReferenceItemLogoCardSection
+ __OBJC_$_INSTANCE_VARIABLES_RFSecondaryHeaderEmphasizedCardSection
+ __OBJC_$_INSTANCE_VARIABLES_RFSecondaryHeaderStandardCardSection
+ __OBJC_$_INSTANCE_VARIABLES_RFSimpleItemReverseRichCardSection
+ __OBJC_$_INSTANCE_VARIABLES_RFSimpleItemRichSearchResultCardSection
+ __OBJC_$_INSTANCE_VARIABLES_RFSimpleItemVisualElementCardSection
+ __OBJC_$_INSTANCE_VARIABLES_RFSummaryItemButtonCardSection
+ __OBJC_$_INSTANCE_VARIABLES_RFSummaryItemImageRightCardSection
+ __OBJC_$_INSTANCE_VARIABLES_RFSummaryItemPlayerCardSection
+ __OBJC_$_INSTANCE_VARIABLES_RFSystemFont
+ __OBJC_$_INSTANCE_VARIABLES_SFHashBucketDetail
+ __OBJC_$_INSTANCE_VARIABLES_SFHashDetail
+ __OBJC_$_INSTANCE_VARIABLES_SFPlayAudioButtonItem
+ __OBJC_$_INSTANCE_VARIABLES_SFPlayWatchListItemButtonItem
+ __OBJC_$_INSTANCE_VARIABLES_SFRequestProductPageCommand
+ __OBJC_$_INSTANCE_VARIABLES_SFShortcutsImage
+ __OBJC_$_INSTANCE_VARIABLES_SFStoreButtonItem
+ __OBJC_$_INSTANCE_VARIABLES__SFPBHashBucketDetail
+ __OBJC_$_INSTANCE_VARIABLES__SFPBHashBucketDetail_HashDetail
+ __OBJC_$_INSTANCE_VARIABLES__SFPBPlayAudioButtonItem
+ __OBJC_$_INSTANCE_VARIABLES__SFPBPlayWatchListItemButtonItem
+ __OBJC_$_INSTANCE_VARIABLES__SFPBRFBinaryButtonCardSection
+ __OBJC_$_INSTANCE_VARIABLES__SFPBRFButtonCardSection
+ __OBJC_$_INSTANCE_VARIABLES__SFPBRFFont
+ __OBJC_$_INSTANCE_VARIABLES__SFPBRFFont_RFSystemFont
+ __OBJC_$_INSTANCE_VARIABLES__SFPBRFPrimaryHeaderStackedImageCardSection
+ __OBJC_$_INSTANCE_VARIABLES__SFPBRFReferenceCenteredCardSection
+ __OBJC_$_INSTANCE_VARIABLES__SFPBRFReferenceItemButtonCardSection
+ __OBJC_$_INSTANCE_VARIABLES__SFPBRFReferenceItemLogoCardSection
+ __OBJC_$_INSTANCE_VARIABLES__SFPBRFSecondaryHeaderEmphasizedCardSection
+ __OBJC_$_INSTANCE_VARIABLES__SFPBRFSecondaryHeaderStandardCardSection
+ __OBJC_$_INSTANCE_VARIABLES__SFPBRFSimpleItemReverseRichCardSection
+ __OBJC_$_INSTANCE_VARIABLES__SFPBRFSimpleItemRichSearchResultCardSection
+ __OBJC_$_INSTANCE_VARIABLES__SFPBRFSimpleItemVisualElementCardSection
+ __OBJC_$_INSTANCE_VARIABLES__SFPBRFSummaryItemButtonCardSection
+ __OBJC_$_INSTANCE_VARIABLES__SFPBRFSummaryItemImageRightCardSection
+ __OBJC_$_INSTANCE_VARIABLES__SFPBRFSummaryItemPlayerCardSection
+ __OBJC_$_INSTANCE_VARIABLES__SFPBRequestProductPageCommand
+ __OBJC_$_INSTANCE_VARIABLES__SFPBShortcutsImage
+ __OBJC_$_INSTANCE_VARIABLES__SFPBStoreButtonItem
+ __OBJC_$_PROP_LIST_RFAppIconImage.88
+ __OBJC_$_PROP_LIST_RFAspectRatio.82
+ __OBJC_$_PROP_LIST_RFAttribution.127
+ __OBJC_$_PROP_LIST_RFAvatarImage.89
+ __OBJC_$_PROP_LIST_RFBadgedImage.82
+ __OBJC_$_PROP_LIST_RFBinaryButtonCardSection
+ __OBJC_$_PROP_LIST_RFBinaryButtonCardSection.198
+ __OBJC_$_PROP_LIST_RFButtonCardSection
+ __OBJC_$_PROP_LIST_RFButtonCardSection.193
+ __OBJC_$_PROP_LIST_RFColor.99
+ __OBJC_$_PROP_LIST_RFDefaultBrowserAppIconImage.77
+ __OBJC_$_PROP_LIST_RFExpandableStandardCardSection.202
+ __OBJC_$_PROP_LIST_RFExpandingComponentContent.90
+ __OBJC_$_PROP_LIST_RFFactItemButtonCardSection.256
+ __OBJC_$_PROP_LIST_RFFactItemDetailedNumberCardSection.217
+ __OBJC_$_PROP_LIST_RFFactItemHeroButtonCardSection.207
+ __OBJC_$_PROP_LIST_RFFactItemHeroNumberCardSection.219
+ __OBJC_$_PROP_LIST_RFFactItemImageRightCardSection.207
+ __OBJC_$_PROP_LIST_RFFactItemShortHeroNumberCardSection.228
+ __OBJC_$_PROP_LIST_RFFactItemShortNumberCardSection.228
+ __OBJC_$_PROP_LIST_RFFactItemStandardCardSection.228
+ __OBJC_$_PROP_LIST_RFFont
+ __OBJC_$_PROP_LIST_RFFont.90
+ __OBJC_$_PROP_LIST_RFFormattedText.154
+ __OBJC_$_PROP_LIST_RFHighlightedSubstring.76
+ __OBJC_$_PROP_LIST_RFImageElement.77
+ __OBJC_$_PROP_LIST_RFImageSource.149
+ __OBJC_$_PROP_LIST_RFLongItemStandardCardSection.208
+ __OBJC_$_PROP_LIST_RFMonogramImage.88
+ __OBJC_$_PROP_LIST_RFOptionalBool.76
+ __OBJC_$_PROP_LIST_RFOptionalFloat.77
+ __OBJC_$_PROP_LIST_RFPrimaryHeaderMarqueeCardSection.216
+ __OBJC_$_PROP_LIST_RFPrimaryHeaderRichCardSection.226
+ __OBJC_$_PROP_LIST_RFPrimaryHeaderStackedImageCardSection
+ __OBJC_$_PROP_LIST_RFPrimaryHeaderStackedImageCardSection.204
+ __OBJC_$_PROP_LIST_RFPrimaryHeaderStandardCardSection.212
+ __OBJC_$_PROP_LIST_RFRGBValue.87
+ __OBJC_$_PROP_LIST_RFReferenceCenteredCardSection
+ __OBJC_$_PROP_LIST_RFReferenceCenteredCardSection.217
+ __OBJC_$_PROP_LIST_RFReferenceFootnoteCardSection.217
+ __OBJC_$_PROP_LIST_RFReferenceItemButtonCardSection
+ __OBJC_$_PROP_LIST_RFReferenceItemButtonCardSection.193
+ __OBJC_$_PROP_LIST_RFReferenceItemLogoCardSection
+ __OBJC_$_PROP_LIST_RFReferenceItemLogoCardSection.193
+ __OBJC_$_PROP_LIST_RFReferenceRichCardSection.216
+ __OBJC_$_PROP_LIST_RFReferenceStandardCardSection.202
+ __OBJC_$_PROP_LIST_RFSecondaryHeaderEmphasizedCardSection
+ __OBJC_$_PROP_LIST_RFSecondaryHeaderEmphasizedCardSection.193
+ __OBJC_$_PROP_LIST_RFSecondaryHeaderStandardCardSection
+ __OBJC_$_PROP_LIST_RFSecondaryHeaderStandardCardSection.193
+ __OBJC_$_PROP_LIST_RFShowMoreOnTap.76
+ __OBJC_$_PROP_LIST_RFSimpleItemPlayerCardSection.218
+ __OBJC_$_PROP_LIST_RFSimpleItemReverseRichCardSection
+ __OBJC_$_PROP_LIST_RFSimpleItemReverseRichCardSection.218
+ __OBJC_$_PROP_LIST_RFSimpleItemRichCardSection.238
+ __OBJC_$_PROP_LIST_RFSimpleItemRichSearchResultCardSection
+ __OBJC_$_PROP_LIST_RFSimpleItemRichSearchResultCardSection.238
+ __OBJC_$_PROP_LIST_RFSimpleItemStandardCardSection.219
+ __OBJC_$_PROP_LIST_RFSimpleItemVisualElementCardSection
+ __OBJC_$_PROP_LIST_RFSimpleItemVisualElementCardSection.221
+ __OBJC_$_PROP_LIST_RFSummaryItemAlignedTextCardSection.228
+ __OBJC_$_PROP_LIST_RFSummaryItemButtonCardSection
+ __OBJC_$_PROP_LIST_RFSummaryItemButtonCardSection.246
+ __OBJC_$_PROP_LIST_RFSummaryItemDetailedTextCardSection.227
+ __OBJC_$_PROP_LIST_RFSummaryItemImageRightCardSection
+ __OBJC_$_PROP_LIST_RFSummaryItemImageRightCardSection.223
+ __OBJC_$_PROP_LIST_RFSummaryItemPairCardSection.217
+ __OBJC_$_PROP_LIST_RFSummaryItemPairNumberCardSection.238
+ __OBJC_$_PROP_LIST_RFSummaryItemPlayerCardSection
+ __OBJC_$_PROP_LIST_RFSummaryItemPlayerCardSection.226
+ __OBJC_$_PROP_LIST_RFSummaryItemShortNumberCardSection.233
+ __OBJC_$_PROP_LIST_RFSummaryItemStandardCardSection.227
+ __OBJC_$_PROP_LIST_RFSummaryItemSwitchV2CardSection.226
+ __OBJC_$_PROP_LIST_RFSummaryItemTextCardSection.214
+ __OBJC_$_PROP_LIST_RFSymbolImage.122
+ __OBJC_$_PROP_LIST_RFSystemFont
+ __OBJC_$_PROP_LIST_RFSystemFont.89
+ __OBJC_$_PROP_LIST_RFTableCell.118
+ __OBJC_$_PROP_LIST_RFTableColumnDefinition.90
+ __OBJC_$_PROP_LIST_RFTableContentColumnDefinition.99
+ __OBJC_$_PROP_LIST_RFTableHeaderCardSection.200
+ __OBJC_$_PROP_LIST_RFTableRowCardSection.199
+ __OBJC_$_PROP_LIST_RFTableSpacerColumnDefinition.65
+ __OBJC_$_PROP_LIST_RFTextElement.95
+ __OBJC_$_PROP_LIST_RFTextEncapsulation.77
+ __OBJC_$_PROP_LIST_RFTextProperty.88
+ __OBJC_$_PROP_LIST_RFUrlImage.133
+ __OBJC_$_PROP_LIST_RFVisualElement.80
+ __OBJC_$_PROP_LIST_RFVisualProperty.88
+ __OBJC_$_PROP_LIST_SFAbstractCommand.89
+ __OBJC_$_PROP_LIST_SFActionItem.270
+ __OBJC_$_PROP_LIST_SFActivityIndicatorCardSection.192
+ __OBJC_$_PROP_LIST_SFAddToPhotosLibraryCommand.105
+ __OBJC_$_PROP_LIST_SFAirport.134
+ __OBJC_$_PROP_LIST_SFApiResults.95
+ __OBJC_$_PROP_LIST_SFAppAutoShortcutsButtonItem.84
+ __OBJC_$_PROP_LIST_SFAppAutoShortcutsItem.76
+ __OBJC_$_PROP_LIST_SFAppColor.105
+ __OBJC_$_PROP_LIST_SFAppIconCardSection.197
+ __OBJC_$_PROP_LIST_SFAppIconImage.145
+ __OBJC_$_PROP_LIST_SFAppLink.106
+ __OBJC_$_PROP_LIST_SFAppLinkCardSection.200
+ __OBJC_$_PROP_LIST_SFArchiveViewCardSection.195
+ __OBJC_$_PROP_LIST_SFAttributionFooterCardSection.215
+ __OBJC_$_PROP_LIST_SFAudioPlaybackCardSection.235
+ __OBJC_$_PROP_LIST_SFBeginMapsRoutingCommand.138
+ __OBJC_$_PROP_LIST_SFButton.93
+ __OBJC_$_PROP_LIST_SFButtonCardSection.205
+ __OBJC_$_PROP_LIST_SFButtonItem.76
+ __OBJC_$_PROP_LIST_SFButtonListCardSection.203
+ __OBJC_$_PROP_LIST_SFCATModel.89
+ __OBJC_$_PROP_LIST_SFCalendarColor.105
+ __OBJC_$_PROP_LIST_SFCalendarEvent.115
+ __OBJC_$_PROP_LIST_SFCalendarImage.139
+ __OBJC_$_PROP_LIST_SFCallCommand.102
+ __OBJC_$_PROP_LIST_SFCard.310
+ __OBJC_$_PROP_LIST_SFCardMetadata.87
+ __OBJC_$_PROP_LIST_SFCardSearchMetadata.98
+ __OBJC_$_PROP_LIST_SFCardSectionValue.1013
+ __OBJC_$_PROP_LIST_SFClearProactiveCategoryCommand.123
+ __OBJC_$_PROP_LIST_SFClockImage.149
+ __OBJC_$_PROP_LIST_SFCloudChannelsRequestItem.86
+ __OBJC_$_PROP_LIST_SFCollectionCardSection.225
+ __OBJC_$_PROP_LIST_SFCollectionStyle.76
+ __OBJC_$_PROP_LIST_SFCollectionStyleGrid.91
+ __OBJC_$_PROP_LIST_SFCollectionStyleHorizontallyScrolling.81
+ __OBJC_$_PROP_LIST_SFCollectionStyleRow.89
+ __OBJC_$_PROP_LIST_SFColor.117
+ __OBJC_$_PROP_LIST_SFColorBarCardSection.209
+ __OBJC_$_PROP_LIST_SFCombinedCardSection.193
+ __OBJC_$_PROP_LIST_SFCommand.103
+ __OBJC_$_PROP_LIST_SFCommandButtonItem.121
+ __OBJC_$_PROP_LIST_SFCommandReference.76
+ __OBJC_$_PROP_LIST_SFCommandRowCardSection.220
+ __OBJC_$_PROP_LIST_SFCommandValue.77
+ __OBJC_$_PROP_LIST_SFCompactRowCardSection.219
+ __OBJC_$_PROP_LIST_SFContactButtonItem.101
+ __OBJC_$_PROP_LIST_SFContactCopyItem.88
+ __OBJC_$_PROP_LIST_SFContactImage.154
+ __OBJC_$_PROP_LIST_SFCopyCommand.105
+ __OBJC_$_PROP_LIST_SFCopyItem.65
+ __OBJC_$_PROP_LIST_SFCoreSpotlightButtonItem.97
+ __OBJC_$_PROP_LIST_SFCoreSpotlightCopyItem.97
+ __OBJC_$_PROP_LIST_SFCoreSpotlightRankingSignals.130
+ __OBJC_$_PROP_LIST_SFCoreSpotlightShareItem.88
+ __OBJC_$_PROP_LIST_SFCreateCalendarEventCommand.105
+ __OBJC_$_PROP_LIST_SFCreateContactCommand.116
+ __OBJC_$_PROP_LIST_SFCreateReminderCommand.105
+ __OBJC_$_PROP_LIST_SFDescriptionCardSection.290
+ __OBJC_$_PROP_LIST_SFDetailedRowCardSection.320
+ __OBJC_$_PROP_LIST_SFDomainEngagementScore.99
+ __OBJC_$_PROP_LIST_SFDomainSubscriptionRequestItem.65
+ __OBJC_$_PROP_LIST_SFDrillDownMetadata.148
+ __OBJC_$_PROP_LIST_SFDynamicURLImageResource.112
+ __OBJC_$_PROP_LIST_SFEmailCommand.102
+ __OBJC_$_PROP_LIST_SFEngagementSignal.106
+ __OBJC_$_PROP_LIST_SFEntitySearchMetadata.91
+ __OBJC_$_PROP_LIST_SFExpandInlineCommand.104
+ __OBJC_$_PROP_LIST_SFFindMyCardSection.193
+ __OBJC_$_PROP_LIST_SFFlight.120
+ __OBJC_$_PROP_LIST_SFFlightCardSection.207
+ __OBJC_$_PROP_LIST_SFFlightLeg.176
+ __OBJC_$_PROP_LIST_SFFlightTopic.93
+ __OBJC_$_PROP_LIST_SFFormattedText.122
+ __OBJC_$_PROP_LIST_SFGradientColor.115
+ __OBJC_$_PROP_LIST_SFGridCardSection.193
+ __OBJC_$_PROP_LIST_SFHashBucketDetail
+ __OBJC_$_PROP_LIST_SFHashBucketDetail.85
+ __OBJC_$_PROP_LIST_SFHashDetail
+ __OBJC_$_PROP_LIST_SFHashDetail.93
+ __OBJC_$_PROP_LIST_SFHeroCardSection.225
+ __OBJC_$_PROP_LIST_SFHeroTitleCardSection.218
+ __OBJC_$_PROP_LIST_SFHorizontalButtonCardSection.193
+ __OBJC_$_PROP_LIST_SFHorizontalScrollCardSection.204
+ __OBJC_$_PROP_LIST_SFImage.167
+ __OBJC_$_PROP_LIST_SFImageCopyItem.79
+ __OBJC_$_PROP_LIST_SFImageDerivedColor.106
+ __OBJC_$_PROP_LIST_SFImageOption.89
+ __OBJC_$_PROP_LIST_SFImagesCardSection.202
+ __OBJC_$_PROP_LIST_SFIndexState.97
+ __OBJC_$_PROP_LIST_SFIndexedUserActivityCommand.107
+ __OBJC_$_PROP_LIST_SFInfoCardSection.204
+ __OBJC_$_PROP_LIST_SFInfoTuple.101
+ __OBJC_$_PROP_LIST_SFInvokeSiriCommand.102
+ __OBJC_$_PROP_LIST_SFKeyValueDataCardSection.202
+ __OBJC_$_PROP_LIST_SFKeyValueTuple.81
+ __OBJC_$_PROP_LIST_SFLargeTitleDetailedRowCardSection.211
+ __OBJC_$_PROP_LIST_SFLatLng.83
+ __OBJC_$_PROP_LIST_SFLaunchAppCommand.102
+ __OBJC_$_PROP_LIST_SFLeadingTrailingCardSection.210
+ __OBJC_$_PROP_LIST_SFLinkPresentationCardSection.210
+ __OBJC_$_PROP_LIST_SFListenToCardSection.205
+ __OBJC_$_PROP_LIST_SFLocalImage.136
+ __OBJC_$_PROP_LIST_SFLocalTopic.87
+ __OBJC_$_PROP_LIST_SFLocationTypeInfo.76
+ __OBJC_$_PROP_LIST_SFMailRankingSignals.146
+ __OBJC_$_PROP_LIST_SFMailResultDetails.94
+ __OBJC_$_PROP_LIST_SFManageReservationCommand.104
+ __OBJC_$_PROP_LIST_SFMapCardSection.249
+ __OBJC_$_PROP_LIST_SFMapPlaceCardSection.209
+ __OBJC_$_PROP_LIST_SFMapRegion.101
+ __OBJC_$_PROP_LIST_SFMapsDetailedRowCardSection.206
+ __OBJC_$_PROP_LIST_SFMediaArtworkImage.155
+ __OBJC_$_PROP_LIST_SFMediaDetail.85
+ __OBJC_$_PROP_LIST_SFMediaInfoCardSection.261
+ __OBJC_$_PROP_LIST_SFMediaItem.142
+ __OBJC_$_PROP_LIST_SFMediaMetadata.122
+ __OBJC_$_PROP_LIST_SFMediaOffer.225
+ __OBJC_$_PROP_LIST_SFMediaPlayerCardSection.203
+ __OBJC_$_PROP_LIST_SFMediaRemoteControlCardSection.206
+ __OBJC_$_PROP_LIST_SFMessageAttachment.106
+ __OBJC_$_PROP_LIST_SFMessageCardSection.225
+ __OBJC_$_PROP_LIST_SFMetaInfoCardSection.219
+ __OBJC_$_PROP_LIST_SFMiniCardSection.210
+ __OBJC_$_PROP_LIST_SFMonogramImage.145
+ __OBJC_$_PROP_LIST_SFMoreResults.76
+ __OBJC_$_PROP_LIST_SFNamedProtobufMessage.84
+ __OBJC_$_PROP_LIST_SFNewsCardSection.229
+ __OBJC_$_PROP_LIST_SFNowPlayingCardSection.200
+ __OBJC_$_PROP_LIST_SFOpenAppClipCommand.102
+ __OBJC_$_PROP_LIST_SFOpenCalculationCommand.107
+ __OBJC_$_PROP_LIST_SFOpenCoreSpotlightItemCommand.112
+ __OBJC_$_PROP_LIST_SFOpenFileProviderItemCommand.118
+ __OBJC_$_PROP_LIST_SFOpenMediaCommand.111
+ __OBJC_$_PROP_LIST_SFOpenPunchoutCommand.105
+ __OBJC_$_PROP_LIST_SFOpenWebClipCommand.102
+ __OBJC_$_PROP_LIST_SFPatternModel.94
+ __OBJC_$_PROP_LIST_SFPerformContactActionCommand.120
+ __OBJC_$_PROP_LIST_SFPerformContactQueryCommand.102
+ __OBJC_$_PROP_LIST_SFPerformEntityQueryCommand.156
+ __OBJC_$_PROP_LIST_SFPerformIntentCommand.124
+ __OBJC_$_PROP_LIST_SFPerformPersonEntityQueryCommand.105
+ __OBJC_$_PROP_LIST_SFPerson.105
+ __OBJC_$_PROP_LIST_SFPersonHeaderCardSection.193
+ __OBJC_$_PROP_LIST_SFPhotosLibraryImage.159
+ __OBJC_$_PROP_LIST_SFPin.124
+ __OBJC_$_PROP_LIST_SFPlayAudioButtonItem
+ __OBJC_$_PROP_LIST_SFPlayAudioButtonItem.93
+ __OBJC_$_PROP_LIST_SFPlayMediaCommand.126
+ __OBJC_$_PROP_LIST_SFPlayVideoCommand.105
+ __OBJC_$_PROP_LIST_SFPlayWatchListItemButtonItem
+ __OBJC_$_PROP_LIST_SFPlayWatchListItemButtonItem.101
+ __OBJC_$_PROP_LIST_SFProduct.106
+ __OBJC_$_PROP_LIST_SFProductAvailability.77
+ __OBJC_$_PROP_LIST_SFProductCardSection.195
+ __OBJC_$_PROP_LIST_SFProductInventory.128
+ __OBJC_$_PROP_LIST_SFProductInventoryResult.85
+ __OBJC_$_PROP_LIST_SFQueryTopic.95
+ __OBJC_$_PROP_LIST_SFQueryUnderstandingParse.170
+ __OBJC_$_PROP_LIST_SFQuickLookThumbnailImage.150
+ __OBJC_$_PROP_LIST_SFReferentialCommand.76
+ __OBJC_$_PROP_LIST_SFRejectPeopleInPhotoCommand.114
+ __OBJC_$_PROP_LIST_SFReminder.90
+ __OBJC_$_PROP_LIST_SFRequestAppClipInstallCommand.111
+ __OBJC_$_PROP_LIST_SFRequestProductPageCommand
+ __OBJC_$_PROP_LIST_SFRequestProductPageCommand.119
+ __OBJC_$_PROP_LIST_SFRequestUserReportCommand.105
+ __OBJC_$_PROP_LIST_SFResponseWrapperCardSection.216
+ __OBJC_$_PROP_LIST_SFResultEntity.90
+ __OBJC_$_PROP_LIST_SFRichText.113
+ __OBJC_$_PROP_LIST_SFRichTitleCardSection.359
+ __OBJC_$_PROP_LIST_SFRowCardSection.276
+ __OBJC_$_PROP_LIST_SFRunVoiceShortcutCommand.107
+ __OBJC_$_PROP_LIST_SFScene.86
+ __OBJC_$_PROP_LIST_SFScoreboardCardSection.219
+ __OBJC_$_PROP_LIST_SFSearchInAppCommand.119
+ __OBJC_$_PROP_LIST_SFSearchSuggestion.165
+ __OBJC_$_PROP_LIST_SFSearchWebCommand.102
+ __OBJC_$_PROP_LIST_SFSectionHeaderCardSection.196
+ __OBJC_$_PROP_LIST_SFSelectableGridCardSection.202
+ __OBJC_$_PROP_LIST_SFShareCommand.105
+ __OBJC_$_PROP_LIST_SFShareItem.65
+ __OBJC_$_PROP_LIST_SFShortcutsImage
+ __OBJC_$_PROP_LIST_SFShortcutsImage.136
+ __OBJC_$_PROP_LIST_SFShowAppStoreSheetCommand.107
+ __OBJC_$_PROP_LIST_SFShowContactCardCommand.113
+ __OBJC_$_PROP_LIST_SFShowPhotosOneUpViewCommand.137
+ __OBJC_$_PROP_LIST_SFShowPurchaseRequestSheetCommand.102
+ __OBJC_$_PROP_LIST_SFShowSFCardCommand.105
+ __OBJC_$_PROP_LIST_SFShowScreenTimeRequestSheetCommand.102
+ __OBJC_$_PROP_LIST_SFShowWrapperResponseViewCommand.105
+ __OBJC_$_PROP_LIST_SFSocialMediaPostCardSection.253
+ __OBJC_$_PROP_LIST_SFSplitCardSection.225
+ __OBJC_$_PROP_LIST_SFSportsFollowButtonItem.93
+ __OBJC_$_PROP_LIST_SFSportsItem.88
+ __OBJC_$_PROP_LIST_SFSportsSubscriptionRequestItem.88
+ __OBJC_$_PROP_LIST_SFSportsTeam.120
+ __OBJC_$_PROP_LIST_SFSportsTopic.88
+ __OBJC_$_PROP_LIST_SFStockChartCardSection.204
+ __OBJC_$_PROP_LIST_SFStoreButtonItem
+ __OBJC_$_PROP_LIST_SFStoreButtonItem.94
+ __OBJC_$_PROP_LIST_SFStrokeAnimationCardSection.208
+ __OBJC_$_PROP_LIST_SFStructuredLocation.97
+ __OBJC_$_PROP_LIST_SFSubscribeForUpdatesCommand.114
+ __OBJC_$_PROP_LIST_SFSuggestionCardSection.245
+ __OBJC_$_PROP_LIST_SFSymbolImage.170
+ __OBJC_$_PROP_LIST_SFTableAlignmentSchema.85
+ __OBJC_$_PROP_LIST_SFTableColumnAlignment.92
+ __OBJC_$_PROP_LIST_SFTableHeaderRowCardSection.212
+ __OBJC_$_PROP_LIST_SFTableRowCardSection.245
+ __OBJC_$_PROP_LIST_SFText.87
+ __OBJC_$_PROP_LIST_SFTextColumn.77
+ __OBJC_$_PROP_LIST_SFTextColumnSection.97
+ __OBJC_$_PROP_LIST_SFTextColumnsCardSection.209
+ __OBJC_$_PROP_LIST_SFTextCopyItem.78
+ __OBJC_$_PROP_LIST_SFTitleCardSection.206
+ __OBJC_$_PROP_LIST_SFTitleSubtitleTuple.81
+ __OBJC_$_PROP_LIST_SFToggleAudioCommand.124
+ __OBJC_$_PROP_LIST_SFToggleButtonConfiguration.95
+ __OBJC_$_PROP_LIST_SFToggleWatchListStatusCommand.116
+ __OBJC_$_PROP_LIST_SFTopic.71
+ __OBJC_$_PROP_LIST_SFTrack.115
+ __OBJC_$_PROP_LIST_SFTrackListCardSection.200
+ __OBJC_$_PROP_LIST_SFURLImage.144
+ __OBJC_$_PROP_LIST_SFURLShareItem.79
+ __OBJC_$_PROP_LIST_SFUpdateSearchQueryCommand.114
+ __OBJC_$_PROP_LIST_SFUpdateSportsFollowingStatusCommand.116
+ __OBJC_$_PROP_LIST_SFUserActivityData.85
+ __OBJC_$_PROP_LIST_SFUserActivityInfo.102
+ __OBJC_$_PROP_LIST_SFUserReportRequest.131
+ __OBJC_$_PROP_LIST_SFVerticalLayoutCardSection.230
+ __OBJC_$_PROP_LIST_SFViewEmailCommand.104
+ __OBJC_$_PROP_LIST_SFWatchListButtonItem.93
+ __OBJC_$_PROP_LIST_SFWatchListCardSection.196
+ __OBJC_$_PROP_LIST_SFWatchListItem.142
+ __OBJC_$_PROP_LIST_SFWatchNowCardSection.201
+ __OBJC_$_PROP_LIST_SFWeatherColor.123
+ __OBJC_$_PROP_LIST_SFWeatherTopic.93
+ __OBJC_$_PROP_LIST_SFWebCardSection.192
+ __OBJC_$_PROP_LIST_SFWorldMapCardSection.201
+ __OBJC_$_PROP_LIST__SFPBAbstractCommand.93
+ __OBJC_$_PROP_LIST__SFPBActionItem.388
+ __OBJC_$_PROP_LIST__SFPBActivityIndicatorCardSection.477
+ __OBJC_$_PROP_LIST__SFPBAddToPhotosLibraryCommand.492
+ __OBJC_$_PROP_LIST__SFPBAirport.584
+ __OBJC_$_PROP_LIST__SFPBApiResults.622
+ __OBJC_$_PROP_LIST__SFPBAppAutoShortcutsButtonItem.653
+ __OBJC_$_PROP_LIST__SFPBAppAutoShortcutsItem.668
+ __OBJC_$_PROP_LIST__SFPBAppColor.675
+ __OBJC_$_PROP_LIST__SFPBAppIconCardSection.690
+ __OBJC_$_PROP_LIST__SFPBAppIconImage.705
+ __OBJC_$_PROP_LIST__SFPBAppLink.728
+ __OBJC_$_PROP_LIST__SFPBAppLinkCardSection.758
+ __OBJC_$_PROP_LIST__SFPBArchiveViewCardSection.773
+ __OBJC_$_PROP_LIST__SFPBAttributionFooterCardSection.817
+ __OBJC_$_PROP_LIST__SFPBAudioPlaybackCardSection.870
+ __OBJC_$_PROP_LIST__SFPBBeginMapsRoutingCommand.877
+ __OBJC_$_PROP_LIST__SFPBButton.900
+ __OBJC_$_PROP_LIST__SFPBButtonCardSection.907
+ __OBJC_$_PROP_LIST__SFPBButtonItem.1036
+ __OBJC_$_PROP_LIST__SFPBButtonListCardSection.1074
+ __OBJC_$_PROP_LIST__SFPBCATModel.1097
+ __OBJC_$_PROP_LIST__SFPBCalendarColor.1112
+ __OBJC_$_PROP_LIST__SFPBCalendarEvent.1162
+ __OBJC_$_PROP_LIST__SFPBCalendarImage.1177
+ __OBJC_$_PROP_LIST__SFPBCallCommand.1184
+ __OBJC_$_PROP_LIST__SFPBCard.1367
+ __OBJC_$_PROP_LIST__SFPBCardMetadata.1390
+ __OBJC_$_PROP_LIST__SFPBCardSearchMetadata.1421
+ __OBJC_$_PROP_LIST__SFPBCardSection.1594
+ __OBJC_$_PROP_LIST__SFPBCardSectionValue.2966
+ __OBJC_$_PROP_LIST__SFPBClearProactiveCategoryCommand.2997
+ __OBJC_$_PROP_LIST__SFPBClockImage.3027
+ __OBJC_$_PROP_LIST__SFPBCloudChannelsRequestItem.3058
+ __OBJC_$_PROP_LIST__SFPBCollectionCardSection.3095
+ __OBJC_$_PROP_LIST__SFPBCollectionStyle.3153
+ __OBJC_$_PROP_LIST__SFPBCollectionStyleGrid.3175
+ __OBJC_$_PROP_LIST__SFPBCollectionStyleHorizontallyScrolling.3189
+ __OBJC_$_PROP_LIST__SFPBCollectionStyleRow.3211
+ __OBJC_$_PROP_LIST__SFPBColor.3331
+ __OBJC_$_PROP_LIST__SFPBColorBarCardSection.3354
+ __OBJC_$_PROP_LIST__SFPBCombinedCardSection.3361
+ __OBJC_$_PROP_LIST__SFPBCommand.4047
+ __OBJC_$_PROP_LIST__SFPBCommandButtonItem.4062
+ __OBJC_$_PROP_LIST__SFPBCommandReference.4077
+ __OBJC_$_PROP_LIST__SFPBCommandRowCardSection.4100
+ __OBJC_$_PROP_LIST__SFPBCommandValue.4120
+ __OBJC_$_PROP_LIST__SFPBCompactRowCardSection.4135
+ __OBJC_$_PROP_LIST__SFPBContactButtonItem.4169
+ __OBJC_$_PROP_LIST__SFPBContactCopyItem.4184
+ __OBJC_$_PROP_LIST__SFPBContactImage.4219
+ __OBJC_$_PROP_LIST__SFPBCopyCommand.4239
+ __OBJC_$_PROP_LIST__SFPBCopyItem.4298
+ __OBJC_$_PROP_LIST__SFPBCoreSpotlightButtonItem.4325
+ __OBJC_$_PROP_LIST__SFPBCoreSpotlightCopyItem.4356
+ __OBJC_$_PROP_LIST__SFPBCoreSpotlightRankingSignals.4438
+ __OBJC_$_PROP_LIST__SFPBCoreSpotlightShareItem.4453
+ __OBJC_$_PROP_LIST__SFPBCreateCalendarEventCommand.4473
+ __OBJC_$_PROP_LIST__SFPBCreateContactCommand.4488
+ __OBJC_$_PROP_LIST__SFPBCreateReminderCommand.4508
+ __OBJC_$_PROP_LIST__SFPBDate.4526
+ __OBJC_$_PROP_LIST__SFPBDescriptionCardSection.4639
+ __OBJC_$_PROP_LIST__SFPBDetailedRowCardSection.4813
+ __OBJC_$_PROP_LIST__SFPBDomainEngagementScore.4851
+ __OBJC_$_PROP_LIST__SFPBDomainSubscriptionRequestItem.4871
+ __OBJC_$_PROP_LIST__SFPBDrillDownMetadata.4978
+ __OBJC_$_PROP_LIST__SFPBDynamicURLImageResource.5032
+ __OBJC_$_PROP_LIST__SFPBEmailCommand.5039
+ __OBJC_$_PROP_LIST__SFPBEngagementSignal.5101
+ __OBJC_$_PROP_LIST__SFPBEntitySearchMetadata.5125
+ __OBJC_$_PROP_LIST__SFPBExpandInlineCommand.5139
+ __OBJC_$_PROP_LIST__SFPBFindMyCardSection.5146
+ __OBJC_$_PROP_LIST__SFPBFlight.5232
+ __OBJC_$_PROP_LIST__SFPBFlightCardSection.5258
+ __OBJC_$_PROP_LIST__SFPBFlightDetails.5272
+ __OBJC_$_PROP_LIST__SFPBFlightLeg.5412
+ __OBJC_$_PROP_LIST__SFPBFormattedText.5460
+ __OBJC_$_PROP_LIST__SFPBGradientColor.5488
+ __OBJC_$_PROP_LIST__SFPBGraphicalFloat.5502
+ __OBJC_$_PROP_LIST__SFPBGridCardSection.5509
+ __OBJC_$_PROP_LIST__SFPBHashBucketDetail
+ __OBJC_$_PROP_LIST__SFPBHashBucketDetail.5539
+ __OBJC_$_PROP_LIST__SFPBHashBucketDetail_HashDetail
+ __OBJC_$_PROP_LIST__SFPBHashBucketDetail_HashDetail.5570
+ __OBJC_$_PROP_LIST__SFPBHeroCardSection.5577
+ __OBJC_$_PROP_LIST__SFPBHeroTitleCardSection.5592
+ __OBJC_$_PROP_LIST__SFPBHorizontalButtonCardSection.5611
+ __OBJC_$_PROP_LIST__SFPBHorizontalScrollCardSection.5618
+ __OBJC_$_PROP_LIST__SFPBImage.5883
+ __OBJC_$_PROP_LIST__SFPBImageCopyItem.5890
+ __OBJC_$_PROP_LIST__SFPBImageDerivedColor.5897
+ __OBJC_$_PROP_LIST__SFPBImageOption.5925
+ __OBJC_$_PROP_LIST__SFPBImagesCardSection.5953
+ __OBJC_$_PROP_LIST__SFPBIndexState.5999
+ __OBJC_$_PROP_LIST__SFPBIndexedUserActivityCommand.6014
+ __OBJC_$_PROP_LIST__SFPBInfoCardSection.6044
+ __OBJC_$_PROP_LIST__SFPBInfoTuple.6088
+ __OBJC_$_PROP_LIST__SFPBInvokeSiriCommand.6103
+ __OBJC_$_PROP_LIST__SFPBKeyValueDataCardSection.6134
+ __OBJC_$_PROP_LIST__SFPBKeyValueTuple.6142
+ __OBJC_$_PROP_LIST__SFPBLargeTitleDetailedRowCardSection.6172
+ __OBJC_$_PROP_LIST__SFPBLatLng.6194
+ __OBJC_$_PROP_LIST__SFPBLaunchAppCommand.6201
+ __OBJC_$_PROP_LIST__SFPBLeadingTrailingCardSection.6240
+ __OBJC_$_PROP_LIST__SFPBLinkPresentationCardSection.6277
+ __OBJC_$_PROP_LIST__SFPBListenToCardSection.6308
+ __OBJC_$_PROP_LIST__SFPBLocalImage.6322
+ __OBJC_$_PROP_LIST__SFPBLocationTypeInfo.6337
+ __OBJC_$_PROP_LIST__SFPBMailRankingSignals.6439
+ __OBJC_$_PROP_LIST__SFPBMailResultDetails.6469
+ __OBJC_$_PROP_LIST__SFPBManageReservationCommand.6475
+ __OBJC_$_PROP_LIST__SFPBMapCardSection.6551
+ __OBJC_$_PROP_LIST__SFPBMapPlaceCardSection.6566
+ __OBJC_$_PROP_LIST__SFPBMapRegion.6612
+ __OBJC_$_PROP_LIST__SFPBMapsDetailedRowCardSection.6627
+ __OBJC_$_PROP_LIST__SFPBMediaArtworkImage.6642
+ __OBJC_$_PROP_LIST__SFPBMediaDetail.6657
+ __OBJC_$_PROP_LIST__SFPBMediaInfoCardSection.6771
+ __OBJC_$_PROP_LIST__SFPBMediaItem.6851
+ __OBJC_$_PROP_LIST__SFPBMediaMetadata.6931
+ __OBJC_$_PROP_LIST__SFPBMediaOffer.6970
+ __OBJC_$_PROP_LIST__SFPBMediaPlayerCardSection.6990
+ __OBJC_$_PROP_LIST__SFPBMediaRemoteControlCardSection.7021
+ __OBJC_$_PROP_LIST__SFPBMessageAttachment.7037
+ __OBJC_$_PROP_LIST__SFPBMessageCardSection.7089
+ __OBJC_$_PROP_LIST__SFPBMetaInfoCardSection.7128
+ __OBJC_$_PROP_LIST__SFPBMiniCardSection.7135
+ __OBJC_$_PROP_LIST__SFPBMonogramImage.7158
+ __OBJC_$_PROP_LIST__SFPBMoreResults.7165
+ __OBJC_$_PROP_LIST__SFPBNamedProtobufMessage.7188
+ __OBJC_$_PROP_LIST__SFPBNewsCardSection.7219
+ __OBJC_$_PROP_LIST__SFPBNowPlayingCardSection.7238
+ __OBJC_$_PROP_LIST__SFPBOpenAppClipCommand.7253
+ __OBJC_$_PROP_LIST__SFPBOpenCalculationCommand.7276
+ __OBJC_$_PROP_LIST__SFPBOpenCoreSpotlightItemCommand.7291
+ __OBJC_$_PROP_LIST__SFPBOpenFileProviderItemCommand.7314
+ __OBJC_$_PROP_LIST__SFPBOpenMediaCommand.7329
+ __OBJC_$_PROP_LIST__SFPBOpenPunchoutCommand.7336
+ __OBJC_$_PROP_LIST__SFPBOpenWebClipCommand.7343
+ __OBJC_$_PROP_LIST__SFPBPatternModel.7382
+ __OBJC_$_PROP_LIST__SFPBPerformContactActionCommand.7412
+ __OBJC_$_PROP_LIST__SFPBPerformContactQueryCommand.7419
+ __OBJC_$_PROP_LIST__SFPBPerformEntityQueryCommand.7458
+ __OBJC_$_PROP_LIST__SFPBPerformIntentCommand.7473
+ __OBJC_$_PROP_LIST__SFPBPerformPersonEntityQueryCommand.7480
+ __OBJC_$_PROP_LIST__SFPBPerson.7535
+ __OBJC_$_PROP_LIST__SFPBPersonHeaderCardSection.7542
+ __OBJC_$_PROP_LIST__SFPBPhotosLibraryImage.7578
+ __OBJC_$_PROP_LIST__SFPBPin.7593
+ __OBJC_$_PROP_LIST__SFPBPlayAudioButtonItem
+ __OBJC_$_PROP_LIST__SFPBPlayAudioButtonItem.7613
+ __OBJC_$_PROP_LIST__SFPBPlayMediaCommand.7636
+ __OBJC_$_PROP_LIST__SFPBPlayVideoCommand.7643
+ __OBJC_$_PROP_LIST__SFPBPlayWatchListItemButtonItem
+ __OBJC_$_PROP_LIST__SFPBPlayWatchListItemButtonItem.7663
+ __OBJC_$_PROP_LIST__SFPBPointSize.7686
+ __OBJC_$_PROP_LIST__SFPBProduct.7717
+ __OBJC_$_PROP_LIST__SFPBProductAvailability.7739
+ __OBJC_$_PROP_LIST__SFPBProductCardSection.7754
+ __OBJC_$_PROP_LIST__SFPBProductInventory.7810
+ __OBJC_$_PROP_LIST__SFPBProductInventoryResult.7833
+ __OBJC_$_PROP_LIST__SFPBPunchout.7890
+ __OBJC_$_PROP_LIST__SFPBQueryUnderstandingParse.8024
+ __OBJC_$_PROP_LIST__SFPBQuickLookThumbnailImage.8039
+ __OBJC_$_PROP_LIST__SFPBRFAppIconImage.8059
+ __OBJC_$_PROP_LIST__SFPBRFAspectRatio.8067
+ __OBJC_$_PROP_LIST__SFPBRFAttribution.8119
+ __OBJC_$_PROP_LIST__SFPBRFAvatarImage.8138
+ __OBJC_$_PROP_LIST__SFPBRFBadgedImage.8152
+ __OBJC_$_PROP_LIST__SFPBRFBinaryButtonCardSection
+ __OBJC_$_PROP_LIST__SFPBRFBinaryButtonCardSection.8175
+ __OBJC_$_PROP_LIST__SFPBRFButtonCardSection
+ __OBJC_$_PROP_LIST__SFPBRFButtonCardSection.8183
+ __OBJC_$_PROP_LIST__SFPBRFColor.8217
+ __OBJC_$_PROP_LIST__SFPBRFDefaultBrowserAppIconImage.8223
+ __OBJC_$_PROP_LIST__SFPBRFExpandableStandardCardSection.8258
+ __OBJC_$_PROP_LIST__SFPBRFExpandingComponentContent.8281
+ __OBJC_$_PROP_LIST__SFPBRFFactItemButtonCardSection.8375
+ __OBJC_$_PROP_LIST__SFPBRFFactItemDetailedNumberCardSection.8390
+ __OBJC_$_PROP_LIST__SFPBRFFactItemHeroButtonCardSection.8397
+ __OBJC_$_PROP_LIST__SFPBRFFactItemHeroNumberCardSection.8434
+ __OBJC_$_PROP_LIST__SFPBRFFactItemImageRightCardSection.8441
+ __OBJC_$_PROP_LIST__SFPBRFFactItemShortHeroNumberCardSection.8448
+ __OBJC_$_PROP_LIST__SFPBRFFactItemShortNumberCardSection.8455
+ __OBJC_$_PROP_LIST__SFPBRFFactItemStandardCardSection.8471
+ __OBJC_$_PROP_LIST__SFPBRFFont
+ __OBJC_$_PROP_LIST__SFPBRFFont.8491
+ __OBJC_$_PROP_LIST__SFPBRFFont_RFSystemFont
+ __OBJC_$_PROP_LIST__SFPBRFFont_RFSystemFont.9205
+ __OBJC_$_PROP_LIST__SFPBRFFormattedText.8608
+ __OBJC_$_PROP_LIST__SFPBRFHighlightedSubstring.8623
+ __OBJC_$_PROP_LIST__SFPBRFImageElement.8643
+ __OBJC_$_PROP_LIST__SFPBRFImageSource.8742
+ __OBJC_$_PROP_LIST__SFPBRFLongItemStandardCardSection.8765
+ __OBJC_$_PROP_LIST__SFPBRFMonogramImage.8780
+ __OBJC_$_PROP_LIST__SFPBRFOptionalBool.8787
+ __OBJC_$_PROP_LIST__SFPBRFOptionalFloat.8794
+ __OBJC_$_PROP_LIST__SFPBRFPrimaryHeaderMarqueeCardSection.8809
+ __OBJC_$_PROP_LIST__SFPBRFPrimaryHeaderRichCardSection.8816
+ __OBJC_$_PROP_LIST__SFPBRFPrimaryHeaderStackedImageCardSection
+ __OBJC_$_PROP_LIST__SFPBRFPrimaryHeaderStackedImageCardSection.8824
+ __OBJC_$_PROP_LIST__SFPBRFPrimaryHeaderStandardCardSection.8831
+ __OBJC_$_PROP_LIST__SFPBRFRGBValue.8861
+ __OBJC_$_PROP_LIST__SFPBRFReferenceCenteredCardSection
+ __OBJC_$_PROP_LIST__SFPBRFReferenceCenteredCardSection.8873
+ __OBJC_$_PROP_LIST__SFPBRFReferenceFootnoteCardSection.8880
+ __OBJC_$_PROP_LIST__SFPBRFReferenceItemButtonCardSection
+ __OBJC_$_PROP_LIST__SFPBRFReferenceItemButtonCardSection.8887
+ __OBJC_$_PROP_LIST__SFPBRFReferenceItemLogoCardSection
+ __OBJC_$_PROP_LIST__SFPBRFReferenceItemLogoCardSection.8894
+ __OBJC_$_PROP_LIST__SFPBRFReferenceRichCardSection.8901
+ __OBJC_$_PROP_LIST__SFPBRFReferenceStandardCardSection.8908
+ __OBJC_$_PROP_LIST__SFPBRFSecondaryHeaderEmphasizedCardSection
+ __OBJC_$_PROP_LIST__SFPBRFSecondaryHeaderEmphasizedCardSection.8915
+ __OBJC_$_PROP_LIST__SFPBRFSecondaryHeaderStandardCardSection
+ __OBJC_$_PROP_LIST__SFPBRFSecondaryHeaderStandardCardSection.8922
+ __OBJC_$_PROP_LIST__SFPBRFShowMoreOnTap.8937
+ __OBJC_$_PROP_LIST__SFPBRFSimpleItemPlayerCardSection.8952
+ __OBJC_$_PROP_LIST__SFPBRFSimpleItemReverseRichCardSection
+ __OBJC_$_PROP_LIST__SFPBRFSimpleItemReverseRichCardSection.8959
+ __OBJC_$_PROP_LIST__SFPBRFSimpleItemRichCardSection.8990
+ __OBJC_$_PROP_LIST__SFPBRFSimpleItemRichSearchResultCardSection
+ __OBJC_$_PROP_LIST__SFPBRFSimpleItemRichSearchResultCardSection.8997
+ __OBJC_$_PROP_LIST__SFPBRFSimpleItemStandardCardSection.9004
+ __OBJC_$_PROP_LIST__SFPBRFSimpleItemVisualElementCardSection
+ __OBJC_$_PROP_LIST__SFPBRFSimpleItemVisualElementCardSection.9020
+ __OBJC_$_PROP_LIST__SFPBRFSummaryItemAlignedTextCardSection.9036
+ __OBJC_$_PROP_LIST__SFPBRFSummaryItemButtonCardSection
+ __OBJC_$_PROP_LIST__SFPBRFSummaryItemButtonCardSection.9043
+ __OBJC_$_PROP_LIST__SFPBRFSummaryItemDetailedTextCardSection.9050
+ __OBJC_$_PROP_LIST__SFPBRFSummaryItemImageRightCardSection
+ __OBJC_$_PROP_LIST__SFPBRFSummaryItemImageRightCardSection.9070
+ __OBJC_$_PROP_LIST__SFPBRFSummaryItemPairCardSection.9077
+ __OBJC_$_PROP_LIST__SFPBRFSummaryItemPairNumberCardSection.9100
+ __OBJC_$_PROP_LIST__SFPBRFSummaryItemPlayerCardSection
+ __OBJC_$_PROP_LIST__SFPBRFSummaryItemPlayerCardSection.9107
+ __OBJC_$_PROP_LIST__SFPBRFSummaryItemShortNumberCardSection.9114
+ __OBJC_$_PROP_LIST__SFPBRFSummaryItemStandardCardSection.9129
+ __OBJC_$_PROP_LIST__SFPBRFSummaryItemSwitchV2CardSection.9144
+ __OBJC_$_PROP_LIST__SFPBRFSummaryItemTextCardSection.9151
+ __OBJC_$_PROP_LIST__SFPBRFSymbolImage.9190
+ __OBJC_$_PROP_LIST__SFPBRFTableCell.9241
+ __OBJC_$_PROP_LIST__SFPBRFTableColumnDefinition.9271
+ __OBJC_$_PROP_LIST__SFPBRFTableContentColumnDefinition.9301
+ __OBJC_$_PROP_LIST__SFPBRFTableHeaderCardSection.9350
+ __OBJC_$_PROP_LIST__SFPBRFTableRowCardSection.9365
+ __OBJC_$_PROP_LIST__SFPBRFTableSpacerColumnDefinition.9371
+ __OBJC_$_PROP_LIST__SFPBRFTextElement.9415
+ __OBJC_$_PROP_LIST__SFPBRFTextEncapsulation.9429
+ __OBJC_$_PROP_LIST__SFPBRFTextProperty.9459
+ __OBJC_$_PROP_LIST__SFPBRFUrlImage.9515
+ __OBJC_$_PROP_LIST__SFPBRFVisualElement.9534
+ __OBJC_$_PROP_LIST__SFPBRFVisualProperty.9556
+ __OBJC_$_PROP_LIST__SFPBReferentialCommand.9563
+ __OBJC_$_PROP_LIST__SFPBRejectPeopleInPhotoCommand.9583
+ __OBJC_$_PROP_LIST__SFPBReminder.9598
+ __OBJC_$_PROP_LIST__SFPBRequestAppClipInstallCommand.9605
+ __OBJC_$_PROP_LIST__SFPBRequestProductPageCommand
+ __OBJC_$_PROP_LIST__SFPBRequestProductPageCommand.9636
+ __OBJC_$_PROP_LIST__SFPBRequestUserReportCommand.9643
+ __OBJC_$_PROP_LIST__SFPBResponseWrapperCardSection.9697
+ __OBJC_$_PROP_LIST__SFPBResultEntity.9725
+ __OBJC_$_PROP_LIST__SFPBRichText.9765
+ __OBJC_$_PROP_LIST__SFPBRichTitleCardSection.9913
+ __OBJC_$_PROP_LIST__SFPBRowCardSection.10008
+ __OBJC_$_PROP_LIST__SFPBRunVoiceShortcutCommand.10023
+ __OBJC_$_PROP_LIST__SFPBScene.10045
+ __OBJC_$_PROP_LIST__SFPBScoreboardCardSection.10089
+ __OBJC_$_PROP_LIST__SFPBSearchInAppCommand.10104
+ __OBJC_$_PROP_LIST__SFPBSearchSuggestion.10186
+ __OBJC_$_PROP_LIST__SFPBSearchWebCommand.10193
+ __OBJC_$_PROP_LIST__SFPBSectionHeaderCardSection.10201
+ __OBJC_$_PROP_LIST__SFPBSelectableGridCardSection.10231
+ __OBJC_$_PROP_LIST__SFPBShareCommand.10251
+ __OBJC_$_PROP_LIST__SFPBShareItem.10284
+ __OBJC_$_PROP_LIST__SFPBShortcutsImage
+ __OBJC_$_PROP_LIST__SFPBShortcutsImage.10299
+ __OBJC_$_PROP_LIST__SFPBShowAppStoreSheetCommand.10314
+ __OBJC_$_PROP_LIST__SFPBShowContactCardCommand.10329
+ __OBJC_$_PROP_LIST__SFPBShowPhotosOneUpViewCommand.10380
+ __OBJC_$_PROP_LIST__SFPBShowPurchaseRequestSheetCommand.10395
+ __OBJC_$_PROP_LIST__SFPBShowSFCardCommand.10410
+ __OBJC_$_PROP_LIST__SFPBShowScreenTimeRequestSheetCommand.10417
+ __OBJC_$_PROP_LIST__SFPBShowWrapperResponseViewCommand.10424
+ __OBJC_$_PROP_LIST__SFPBSocialMediaPostCardSection.10488
+ __OBJC_$_PROP_LIST__SFPBSplitCardSection.10555
+ __OBJC_$_PROP_LIST__SFPBSportsDetail.10570
+ __OBJC_$_PROP_LIST__SFPBSportsFollowButtonItem.10590
+ __OBJC_$_PROP_LIST__SFPBSportsItem.10597
+ __OBJC_$_PROP_LIST__SFPBSportsSubscriptionRequestItem.10628
+ __OBJC_$_PROP_LIST__SFPBSportsTeam.10660
+ __OBJC_$_PROP_LIST__SFPBStockChartCardSection.10683
+ __OBJC_$_PROP_LIST__SFPBStoreButtonItem
+ __OBJC_$_PROP_LIST__SFPBStoreButtonItem.10698
+ __OBJC_$_PROP_LIST__SFPBStringDictionary.10717
+ __OBJC_$_PROP_LIST__SFPBStrokeAnimationCardSection.10768
+ __OBJC_$_PROP_LIST__SFPBStructuredLocation.10791
+ __OBJC_$_PROP_LIST__SFPBSubscribeForUpdatesCommand.10824
+ __OBJC_$_PROP_LIST__SFPBSuggestionCardSection.10863
+ __OBJC_$_PROP_LIST__SFPBSymbolImage.10905
+ __OBJC_$_PROP_LIST__SFPBTableAlignmentSchema.10929
+ __OBJC_$_PROP_LIST__SFPBTableColumnAlignment.10959
+ __OBJC_$_PROP_LIST__SFPBTableHeaderRowCardSection.11027
+ __OBJC_$_PROP_LIST__SFPBTableRowCardSection.11047
+ __OBJC_$_PROP_LIST__SFPBText.11064
+ __OBJC_$_PROP_LIST__SFPBTextColumn.11086
+ __OBJC_$_PROP_LIST__SFPBTextColumnSection.11121
+ __OBJC_$_PROP_LIST__SFPBTextColumnsCardSection.11132
+ __OBJC_$_PROP_LIST__SFPBTextCopyItem.11147
+ __OBJC_$_PROP_LIST__SFPBTimeZone.11154
+ __OBJC_$_PROP_LIST__SFPBTitleCardSection.11161
+ __OBJC_$_PROP_LIST__SFPBTitleSubtitleTuple.11168
+ __OBJC_$_PROP_LIST__SFPBToggleAudioCommand.11191
+ __OBJC_$_PROP_LIST__SFPBToggleButtonConfiguration.11215
+ __OBJC_$_PROP_LIST__SFPBToggleWatchListStatusCommand.11230
+ __OBJC_$_PROP_LIST__SFPBTopic.11273
+ __OBJC_$_PROP_LIST__SFPBTrack.11305
+ __OBJC_$_PROP_LIST__SFPBTrackListCardSection.11327
+ __OBJC_$_PROP_LIST__SFPBURL.11334
+ __OBJC_$_PROP_LIST__SFPBURLImage.11349
+ __OBJC_$_PROP_LIST__SFPBURLShareItem.11356
+ __OBJC_$_PROP_LIST__SFPBUpdateSearchQueryCommand.11371
+ __OBJC_$_PROP_LIST__SFPBUpdateSportsFollowingStatusCommand.11386
+ __OBJC_$_PROP_LIST__SFPBUserActivityData.11417
+ __OBJC_$_PROP_LIST__SFPBUserActivityInfo.11440
+ __OBJC_$_PROP_LIST__SFPBUserReportRequest.11515
+ __OBJC_$_PROP_LIST__SFPBVerticalLayoutCardSection.11546
+ __OBJC_$_PROP_LIST__SFPBViewEmailCommand.11552
+ __OBJC_$_PROP_LIST__SFPBWatchListButtonItem.11559
+ __OBJC_$_PROP_LIST__SFPBWatchListCardSection.11566
+ __OBJC_$_PROP_LIST__SFPBWatchListItem.11645
+ __OBJC_$_PROP_LIST__SFPBWatchNowCardSection.11659
+ __OBJC_$_PROP_LIST__SFPBWeatherColor.11674
+ __OBJC_$_PROP_LIST__SFPBWeatherDetails.11681
+ __OBJC_$_PROP_LIST__SFPBWebCardSection.11696
+ __OBJC_$_PROP_LIST__SFPBWorldMapCardSection.11719
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_RFBinaryButtonCardSection
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_RFButtonCardSection
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_RFFont
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_RFPrimaryHeaderStackedImageCardSection
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_RFReferenceCenteredCardSection
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_RFReferenceItemButtonCardSection
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_RFReferenceItemLogoCardSection
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_RFSecondaryHeaderEmphasizedCardSection
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_RFSecondaryHeaderStandardCardSection
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_RFSimpleItemReverseRichCardSection
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_RFSimpleItemRichSearchResultCardSection
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_RFSimpleItemVisualElementCardSection
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_RFSummaryItemButtonCardSection
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_RFSummaryItemImageRightCardSection
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_RFSummaryItemPlayerCardSection
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_RFSystemFont
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SFHashBucketDetail
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SFHashDetail
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SFPlayAudioButtonItem
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SFPlayWatchListItemButtonItem
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SFRequestProductPageCommand
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SFShortcutsImage
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SFStoreButtonItem
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__SFPBHashBucketDetail
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__SFPBHashBucketDetail_HashDetail
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__SFPBPlayAudioButtonItem
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__SFPBPlayWatchListItemButtonItem
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__SFPBRFBinaryButtonCardSection
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__SFPBRFButtonCardSection
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__SFPBRFFont
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__SFPBRFFont_RFSystemFont
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__SFPBRFPrimaryHeaderStackedImageCardSection
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__SFPBRFReferenceCenteredCardSection
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__SFPBRFReferenceItemButtonCardSection
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__SFPBRFReferenceItemLogoCardSection
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__SFPBRFSecondaryHeaderEmphasizedCardSection
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__SFPBRFSecondaryHeaderStandardCardSection
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__SFPBRFSimpleItemReverseRichCardSection
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__SFPBRFSimpleItemRichSearchResultCardSection
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__SFPBRFSimpleItemVisualElementCardSection
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__SFPBRFSummaryItemButtonCardSection
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__SFPBRFSummaryItemImageRightCardSection
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__SFPBRFSummaryItemPlayerCardSection
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__SFPBRequestProductPageCommand
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__SFPBShortcutsImage
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__SFPBStoreButtonItem
+ __OBJC_$_PROTOCOL_METHOD_TYPES_RFBinaryButtonCardSection
+ __OBJC_$_PROTOCOL_METHOD_TYPES_RFButtonCardSection
+ __OBJC_$_PROTOCOL_METHOD_TYPES_RFFont
+ __OBJC_$_PROTOCOL_METHOD_TYPES_RFPrimaryHeaderStackedImageCardSection
+ __OBJC_$_PROTOCOL_METHOD_TYPES_RFReferenceCenteredCardSection
+ __OBJC_$_PROTOCOL_METHOD_TYPES_RFReferenceItemButtonCardSection
+ __OBJC_$_PROTOCOL_METHOD_TYPES_RFReferenceItemLogoCardSection
+ __OBJC_$_PROTOCOL_METHOD_TYPES_RFSecondaryHeaderEmphasizedCardSection
+ __OBJC_$_PROTOCOL_METHOD_TYPES_RFSecondaryHeaderStandardCardSection
+ __OBJC_$_PROTOCOL_METHOD_TYPES_RFSimpleItemReverseRichCardSection
+ __OBJC_$_PROTOCOL_METHOD_TYPES_RFSimpleItemRichSearchResultCardSection
+ __OBJC_$_PROTOCOL_METHOD_TYPES_RFSimpleItemVisualElementCardSection
+ __OBJC_$_PROTOCOL_METHOD_TYPES_RFSummaryItemButtonCardSection
+ __OBJC_$_PROTOCOL_METHOD_TYPES_RFSummaryItemImageRightCardSection
+ __OBJC_$_PROTOCOL_METHOD_TYPES_RFSummaryItemPlayerCardSection
+ __OBJC_$_PROTOCOL_METHOD_TYPES_RFSystemFont
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SFHashBucketDetail
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SFHashDetail
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SFPlayAudioButtonItem
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SFPlayWatchListItemButtonItem
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SFRequestProductPageCommand
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SFShortcutsImage
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SFStoreButtonItem
+ __OBJC_$_PROTOCOL_METHOD_TYPES__SFPBHashBucketDetail
+ __OBJC_$_PROTOCOL_METHOD_TYPES__SFPBHashBucketDetail_HashDetail
+ __OBJC_$_PROTOCOL_METHOD_TYPES__SFPBPlayAudioButtonItem
+ __OBJC_$_PROTOCOL_METHOD_TYPES__SFPBPlayWatchListItemButtonItem
+ __OBJC_$_PROTOCOL_METHOD_TYPES__SFPBRFBinaryButtonCardSection
+ __OBJC_$_PROTOCOL_METHOD_TYPES__SFPBRFButtonCardSection
+ __OBJC_$_PROTOCOL_METHOD_TYPES__SFPBRFFont
+ __OBJC_$_PROTOCOL_METHOD_TYPES__SFPBRFFont_RFSystemFont
+ __OBJC_$_PROTOCOL_METHOD_TYPES__SFPBRFPrimaryHeaderStackedImageCardSection
+ __OBJC_$_PROTOCOL_METHOD_TYPES__SFPBRFReferenceCenteredCardSection
+ __OBJC_$_PROTOCOL_METHOD_TYPES__SFPBRFReferenceItemButtonCardSection
+ __OBJC_$_PROTOCOL_METHOD_TYPES__SFPBRFReferenceItemLogoCardSection
+ __OBJC_$_PROTOCOL_METHOD_TYPES__SFPBRFSecondaryHeaderEmphasizedCardSection
+ __OBJC_$_PROTOCOL_METHOD_TYPES__SFPBRFSecondaryHeaderStandardCardSection
+ __OBJC_$_PROTOCOL_METHOD_TYPES__SFPBRFSimpleItemReverseRichCardSection
+ __OBJC_$_PROTOCOL_METHOD_TYPES__SFPBRFSimpleItemRichSearchResultCardSection
+ __OBJC_$_PROTOCOL_METHOD_TYPES__SFPBRFSimpleItemVisualElementCardSection
+ __OBJC_$_PROTOCOL_METHOD_TYPES__SFPBRFSummaryItemButtonCardSection
+ __OBJC_$_PROTOCOL_METHOD_TYPES__SFPBRFSummaryItemImageRightCardSection
+ __OBJC_$_PROTOCOL_METHOD_TYPES__SFPBRFSummaryItemPlayerCardSection
+ __OBJC_$_PROTOCOL_METHOD_TYPES__SFPBRequestProductPageCommand
+ __OBJC_$_PROTOCOL_METHOD_TYPES__SFPBShortcutsImage
+ __OBJC_$_PROTOCOL_METHOD_TYPES__SFPBStoreButtonItem
+ __OBJC_$_PROTOCOL_REFS_RFBinaryButtonCardSection
+ __OBJC_$_PROTOCOL_REFS_RFButtonCardSection
+ __OBJC_$_PROTOCOL_REFS_RFFont
+ __OBJC_$_PROTOCOL_REFS_RFPrimaryHeaderStackedImageCardSection
+ __OBJC_$_PROTOCOL_REFS_RFReferenceCenteredCardSection
+ __OBJC_$_PROTOCOL_REFS_RFReferenceItemButtonCardSection
+ __OBJC_$_PROTOCOL_REFS_RFReferenceItemLogoCardSection
+ __OBJC_$_PROTOCOL_REFS_RFSecondaryHeaderEmphasizedCardSection
+ __OBJC_$_PROTOCOL_REFS_RFSecondaryHeaderStandardCardSection
+ __OBJC_$_PROTOCOL_REFS_RFSimpleItemReverseRichCardSection
+ __OBJC_$_PROTOCOL_REFS_RFSimpleItemRichSearchResultCardSection
+ __OBJC_$_PROTOCOL_REFS_RFSimpleItemVisualElementCardSection
+ __OBJC_$_PROTOCOL_REFS_RFSummaryItemButtonCardSection
+ __OBJC_$_PROTOCOL_REFS_RFSummaryItemImageRightCardSection
+ __OBJC_$_PROTOCOL_REFS_RFSummaryItemPlayerCardSection
+ __OBJC_$_PROTOCOL_REFS_RFSystemFont
+ __OBJC_$_PROTOCOL_REFS_SFHashBucketDetail
+ __OBJC_$_PROTOCOL_REFS_SFHashDetail
+ __OBJC_$_PROTOCOL_REFS_SFPlayAudioButtonItem
+ __OBJC_$_PROTOCOL_REFS_SFPlayWatchListItemButtonItem
+ __OBJC_$_PROTOCOL_REFS_SFRequestProductPageCommand
+ __OBJC_$_PROTOCOL_REFS_SFShortcutsImage
+ __OBJC_$_PROTOCOL_REFS_SFStoreButtonItem
+ __OBJC_$_PROTOCOL_REFS__SFPBHashBucketDetail
+ __OBJC_$_PROTOCOL_REFS__SFPBHashBucketDetail_HashDetail
+ __OBJC_$_PROTOCOL_REFS__SFPBPlayAudioButtonItem
+ __OBJC_$_PROTOCOL_REFS__SFPBPlayWatchListItemButtonItem
+ __OBJC_$_PROTOCOL_REFS__SFPBRFBinaryButtonCardSection
+ __OBJC_$_PROTOCOL_REFS__SFPBRFButtonCardSection
+ __OBJC_$_PROTOCOL_REFS__SFPBRFFont
+ __OBJC_$_PROTOCOL_REFS__SFPBRFFont_RFSystemFont
+ __OBJC_$_PROTOCOL_REFS__SFPBRFPrimaryHeaderStackedImageCardSection
+ __OBJC_$_PROTOCOL_REFS__SFPBRFReferenceCenteredCardSection
+ __OBJC_$_PROTOCOL_REFS__SFPBRFReferenceItemButtonCardSection
+ __OBJC_$_PROTOCOL_REFS__SFPBRFReferenceItemLogoCardSection
+ __OBJC_$_PROTOCOL_REFS__SFPBRFSecondaryHeaderEmphasizedCardSection
+ __OBJC_$_PROTOCOL_REFS__SFPBRFSecondaryHeaderStandardCardSection
+ __OBJC_$_PROTOCOL_REFS__SFPBRFSimpleItemReverseRichCardSection
+ __OBJC_$_PROTOCOL_REFS__SFPBRFSimpleItemRichSearchResultCardSection
+ __OBJC_$_PROTOCOL_REFS__SFPBRFSimpleItemVisualElementCardSection
+ __OBJC_$_PROTOCOL_REFS__SFPBRFSummaryItemButtonCardSection
+ __OBJC_$_PROTOCOL_REFS__SFPBRFSummaryItemImageRightCardSection
+ __OBJC_$_PROTOCOL_REFS__SFPBRFSummaryItemPlayerCardSection
+ __OBJC_$_PROTOCOL_REFS__SFPBRequestProductPageCommand
+ __OBJC_$_PROTOCOL_REFS__SFPBShortcutsImage
+ __OBJC_$_PROTOCOL_REFS__SFPBStoreButtonItem
+ __OBJC_CLASS_PROTOCOLS_$_RFBinaryButtonCardSection
+ __OBJC_CLASS_PROTOCOLS_$_RFButtonCardSection
+ __OBJC_CLASS_PROTOCOLS_$_RFFont
+ __OBJC_CLASS_PROTOCOLS_$_RFPrimaryHeaderStackedImageCardSection
+ __OBJC_CLASS_PROTOCOLS_$_RFReferenceCenteredCardSection
+ __OBJC_CLASS_PROTOCOLS_$_RFReferenceItemButtonCardSection
+ __OBJC_CLASS_PROTOCOLS_$_RFReferenceItemLogoCardSection
+ __OBJC_CLASS_PROTOCOLS_$_RFSecondaryHeaderEmphasizedCardSection
+ __OBJC_CLASS_PROTOCOLS_$_RFSecondaryHeaderStandardCardSection
+ __OBJC_CLASS_PROTOCOLS_$_RFSimpleItemReverseRichCardSection
+ __OBJC_CLASS_PROTOCOLS_$_RFSimpleItemRichSearchResultCardSection
+ __OBJC_CLASS_PROTOCOLS_$_RFSimpleItemVisualElementCardSection
+ __OBJC_CLASS_PROTOCOLS_$_RFSummaryItemButtonCardSection
+ __OBJC_CLASS_PROTOCOLS_$_RFSummaryItemImageRightCardSection
+ __OBJC_CLASS_PROTOCOLS_$_RFSummaryItemPlayerCardSection
+ __OBJC_CLASS_PROTOCOLS_$_RFSystemFont
+ __OBJC_CLASS_PROTOCOLS_$_SFHashBucketDetail
+ __OBJC_CLASS_PROTOCOLS_$_SFHashDetail
+ __OBJC_CLASS_PROTOCOLS_$_SFPlayAudioButtonItem
+ __OBJC_CLASS_PROTOCOLS_$_SFPlayWatchListItemButtonItem
+ __OBJC_CLASS_PROTOCOLS_$_SFRequestProductPageCommand
+ __OBJC_CLASS_PROTOCOLS_$_SFShortcutsImage
+ __OBJC_CLASS_PROTOCOLS_$_SFStoreButtonItem
+ __OBJC_CLASS_PROTOCOLS_$__SFPBHashBucketDetail
+ __OBJC_CLASS_PROTOCOLS_$__SFPBHashBucketDetail_HashDetail
+ __OBJC_CLASS_PROTOCOLS_$__SFPBPlayAudioButtonItem
+ __OBJC_CLASS_PROTOCOLS_$__SFPBPlayWatchListItemButtonItem
+ __OBJC_CLASS_PROTOCOLS_$__SFPBRFBinaryButtonCardSection
+ __OBJC_CLASS_PROTOCOLS_$__SFPBRFButtonCardSection
+ __OBJC_CLASS_PROTOCOLS_$__SFPBRFFont
+ __OBJC_CLASS_PROTOCOLS_$__SFPBRFFont_RFSystemFont
+ __OBJC_CLASS_PROTOCOLS_$__SFPBRFPrimaryHeaderStackedImageCardSection
+ __OBJC_CLASS_PROTOCOLS_$__SFPBRFReferenceCenteredCardSection
+ __OBJC_CLASS_PROTOCOLS_$__SFPBRFReferenceItemButtonCardSection
+ __OBJC_CLASS_PROTOCOLS_$__SFPBRFReferenceItemLogoCardSection
+ __OBJC_CLASS_PROTOCOLS_$__SFPBRFSecondaryHeaderEmphasizedCardSection
+ __OBJC_CLASS_PROTOCOLS_$__SFPBRFSecondaryHeaderStandardCardSection
+ __OBJC_CLASS_PROTOCOLS_$__SFPBRFSimpleItemReverseRichCardSection
+ __OBJC_CLASS_PROTOCOLS_$__SFPBRFSimpleItemRichSearchResultCardSection
+ __OBJC_CLASS_PROTOCOLS_$__SFPBRFSimpleItemVisualElementCardSection
+ __OBJC_CLASS_PROTOCOLS_$__SFPBRFSummaryItemButtonCardSection
+ __OBJC_CLASS_PROTOCOLS_$__SFPBRFSummaryItemImageRightCardSection
+ __OBJC_CLASS_PROTOCOLS_$__SFPBRFSummaryItemPlayerCardSection
+ __OBJC_CLASS_PROTOCOLS_$__SFPBRequestProductPageCommand
+ __OBJC_CLASS_PROTOCOLS_$__SFPBShortcutsImage
+ __OBJC_CLASS_PROTOCOLS_$__SFPBStoreButtonItem
+ __OBJC_CLASS_RO_$_RFBinaryButtonCardSection
+ __OBJC_CLASS_RO_$_RFButtonCardSection
+ __OBJC_CLASS_RO_$_RFFont
+ __OBJC_CLASS_RO_$_RFPrimaryHeaderStackedImageCardSection
+ __OBJC_CLASS_RO_$_RFReferenceCenteredCardSection
+ __OBJC_CLASS_RO_$_RFReferenceItemButtonCardSection
+ __OBJC_CLASS_RO_$_RFReferenceItemLogoCardSection
+ __OBJC_CLASS_RO_$_RFSecondaryHeaderEmphasizedCardSection
+ __OBJC_CLASS_RO_$_RFSecondaryHeaderStandardCardSection
+ __OBJC_CLASS_RO_$_RFSimpleItemReverseRichCardSection
+ __OBJC_CLASS_RO_$_RFSimpleItemRichSearchResultCardSection
+ __OBJC_CLASS_RO_$_RFSimpleItemVisualElementCardSection
+ __OBJC_CLASS_RO_$_RFSummaryItemButtonCardSection
+ __OBJC_CLASS_RO_$_RFSummaryItemImageRightCardSection
+ __OBJC_CLASS_RO_$_RFSummaryItemPlayerCardSection
+ __OBJC_CLASS_RO_$_RFSystemFont
+ __OBJC_CLASS_RO_$_SFHashBucketDetail
+ __OBJC_CLASS_RO_$_SFHashDetail
+ __OBJC_CLASS_RO_$_SFPlayAudioButtonItem
+ __OBJC_CLASS_RO_$_SFPlayWatchListItemButtonItem
+ __OBJC_CLASS_RO_$_SFRequestProductPageCommand
+ __OBJC_CLASS_RO_$_SFShortcutsImage
+ __OBJC_CLASS_RO_$_SFStoreButtonItem
+ __OBJC_CLASS_RO_$__SFPBHashBucketDetail
+ __OBJC_CLASS_RO_$__SFPBHashBucketDetail_HashDetail
+ __OBJC_CLASS_RO_$__SFPBPlayAudioButtonItem
+ __OBJC_CLASS_RO_$__SFPBPlayWatchListItemButtonItem
+ __OBJC_CLASS_RO_$__SFPBRFBinaryButtonCardSection
+ __OBJC_CLASS_RO_$__SFPBRFButtonCardSection
+ __OBJC_CLASS_RO_$__SFPBRFFont
+ __OBJC_CLASS_RO_$__SFPBRFFont_RFSystemFont
+ __OBJC_CLASS_RO_$__SFPBRFPrimaryHeaderStackedImageCardSection
+ __OBJC_CLASS_RO_$__SFPBRFReferenceCenteredCardSection
+ __OBJC_CLASS_RO_$__SFPBRFReferenceItemButtonCardSection
+ __OBJC_CLASS_RO_$__SFPBRFReferenceItemLogoCardSection
+ __OBJC_CLASS_RO_$__SFPBRFSecondaryHeaderEmphasizedCardSection
+ __OBJC_CLASS_RO_$__SFPBRFSecondaryHeaderStandardCardSection
+ __OBJC_CLASS_RO_$__SFPBRFSimpleItemReverseRichCardSection
+ __OBJC_CLASS_RO_$__SFPBRFSimpleItemRichSearchResultCardSection
+ __OBJC_CLASS_RO_$__SFPBRFSimpleItemVisualElementCardSection
+ __OBJC_CLASS_RO_$__SFPBRFSummaryItemButtonCardSection
+ __OBJC_CLASS_RO_$__SFPBRFSummaryItemImageRightCardSection
+ __OBJC_CLASS_RO_$__SFPBRFSummaryItemPlayerCardSection
+ __OBJC_CLASS_RO_$__SFPBRequestProductPageCommand
+ __OBJC_CLASS_RO_$__SFPBShortcutsImage
+ __OBJC_CLASS_RO_$__SFPBStoreButtonItem
+ __OBJC_LABEL_PROTOCOL_$_RFBinaryButtonCardSection
+ __OBJC_LABEL_PROTOCOL_$_RFButtonCardSection
+ __OBJC_LABEL_PROTOCOL_$_RFFont
+ __OBJC_LABEL_PROTOCOL_$_RFPrimaryHeaderStackedImageCardSection
+ __OBJC_LABEL_PROTOCOL_$_RFReferenceCenteredCardSection
+ __OBJC_LABEL_PROTOCOL_$_RFReferenceItemButtonCardSection
+ __OBJC_LABEL_PROTOCOL_$_RFReferenceItemLogoCardSection
+ __OBJC_LABEL_PROTOCOL_$_RFSecondaryHeaderEmphasizedCardSection
+ __OBJC_LABEL_PROTOCOL_$_RFSecondaryHeaderStandardCardSection
+ __OBJC_LABEL_PROTOCOL_$_RFSimpleItemReverseRichCardSection
+ __OBJC_LABEL_PROTOCOL_$_RFSimpleItemRichSearchResultCardSection
+ __OBJC_LABEL_PROTOCOL_$_RFSimpleItemVisualElementCardSection
+ __OBJC_LABEL_PROTOCOL_$_RFSummaryItemButtonCardSection
+ __OBJC_LABEL_PROTOCOL_$_RFSummaryItemImageRightCardSection
+ __OBJC_LABEL_PROTOCOL_$_RFSummaryItemPlayerCardSection
+ __OBJC_LABEL_PROTOCOL_$_RFSystemFont
+ __OBJC_LABEL_PROTOCOL_$_SFHashBucketDetail
+ __OBJC_LABEL_PROTOCOL_$_SFHashDetail
+ __OBJC_LABEL_PROTOCOL_$_SFPlayAudioButtonItem
+ __OBJC_LABEL_PROTOCOL_$_SFPlayWatchListItemButtonItem
+ __OBJC_LABEL_PROTOCOL_$_SFRequestProductPageCommand
+ __OBJC_LABEL_PROTOCOL_$_SFShortcutsImage
+ __OBJC_LABEL_PROTOCOL_$_SFStoreButtonItem
+ __OBJC_LABEL_PROTOCOL_$__SFPBHashBucketDetail
+ __OBJC_LABEL_PROTOCOL_$__SFPBHashBucketDetail_HashDetail
+ __OBJC_LABEL_PROTOCOL_$__SFPBPlayAudioButtonItem
+ __OBJC_LABEL_PROTOCOL_$__SFPBPlayWatchListItemButtonItem
+ __OBJC_LABEL_PROTOCOL_$__SFPBRFBinaryButtonCardSection
+ __OBJC_LABEL_PROTOCOL_$__SFPBRFButtonCardSection
+ __OBJC_LABEL_PROTOCOL_$__SFPBRFFont
+ __OBJC_LABEL_PROTOCOL_$__SFPBRFFont_RFSystemFont
+ __OBJC_LABEL_PROTOCOL_$__SFPBRFPrimaryHeaderStackedImageCardSection
+ __OBJC_LABEL_PROTOCOL_$__SFPBRFReferenceCenteredCardSection
+ __OBJC_LABEL_PROTOCOL_$__SFPBRFReferenceItemButtonCardSection
+ __OBJC_LABEL_PROTOCOL_$__SFPBRFReferenceItemLogoCardSection
+ __OBJC_LABEL_PROTOCOL_$__SFPBRFSecondaryHeaderEmphasizedCardSection
+ __OBJC_LABEL_PROTOCOL_$__SFPBRFSecondaryHeaderStandardCardSection
+ __OBJC_LABEL_PROTOCOL_$__SFPBRFSimpleItemReverseRichCardSection
+ __OBJC_LABEL_PROTOCOL_$__SFPBRFSimpleItemRichSearchResultCardSection
+ __OBJC_LABEL_PROTOCOL_$__SFPBRFSimpleItemVisualElementCardSection
+ __OBJC_LABEL_PROTOCOL_$__SFPBRFSummaryItemButtonCardSection
+ __OBJC_LABEL_PROTOCOL_$__SFPBRFSummaryItemImageRightCardSection
+ __OBJC_LABEL_PROTOCOL_$__SFPBRFSummaryItemPlayerCardSection
+ __OBJC_LABEL_PROTOCOL_$__SFPBRequestProductPageCommand
+ __OBJC_LABEL_PROTOCOL_$__SFPBShortcutsImage
+ __OBJC_LABEL_PROTOCOL_$__SFPBStoreButtonItem
+ __OBJC_METACLASS_RO_$_RFBinaryButtonCardSection
+ __OBJC_METACLASS_RO_$_RFButtonCardSection
+ __OBJC_METACLASS_RO_$_RFFont
+ __OBJC_METACLASS_RO_$_RFPrimaryHeaderStackedImageCardSection
+ __OBJC_METACLASS_RO_$_RFReferenceCenteredCardSection
+ __OBJC_METACLASS_RO_$_RFReferenceItemButtonCardSection
+ __OBJC_METACLASS_RO_$_RFReferenceItemLogoCardSection
+ __OBJC_METACLASS_RO_$_RFSecondaryHeaderEmphasizedCardSection
+ __OBJC_METACLASS_RO_$_RFSecondaryHeaderStandardCardSection
+ __OBJC_METACLASS_RO_$_RFSimpleItemReverseRichCardSection
+ __OBJC_METACLASS_RO_$_RFSimpleItemRichSearchResultCardSection
+ __OBJC_METACLASS_RO_$_RFSimpleItemVisualElementCardSection
+ __OBJC_METACLASS_RO_$_RFSummaryItemButtonCardSection
+ __OBJC_METACLASS_RO_$_RFSummaryItemImageRightCardSection
+ __OBJC_METACLASS_RO_$_RFSummaryItemPlayerCardSection
+ __OBJC_METACLASS_RO_$_RFSystemFont
+ __OBJC_METACLASS_RO_$_SFHashBucketDetail
+ __OBJC_METACLASS_RO_$_SFHashDetail
+ __OBJC_METACLASS_RO_$_SFPlayAudioButtonItem
+ __OBJC_METACLASS_RO_$_SFPlayWatchListItemButtonItem
+ __OBJC_METACLASS_RO_$_SFRequestProductPageCommand
+ __OBJC_METACLASS_RO_$_SFShortcutsImage
+ __OBJC_METACLASS_RO_$_SFStoreButtonItem
+ __OBJC_METACLASS_RO_$__SFPBHashBucketDetail
+ __OBJC_METACLASS_RO_$__SFPBHashBucketDetail_HashDetail
+ __OBJC_METACLASS_RO_$__SFPBPlayAudioButtonItem
+ __OBJC_METACLASS_RO_$__SFPBPlayWatchListItemButtonItem
+ __OBJC_METACLASS_RO_$__SFPBRFBinaryButtonCardSection
+ __OBJC_METACLASS_RO_$__SFPBRFButtonCardSection
+ __OBJC_METACLASS_RO_$__SFPBRFFont
+ __OBJC_METACLASS_RO_$__SFPBRFFont_RFSystemFont
+ __OBJC_METACLASS_RO_$__SFPBRFPrimaryHeaderStackedImageCardSection
+ __OBJC_METACLASS_RO_$__SFPBRFReferenceCenteredCardSection
+ __OBJC_METACLASS_RO_$__SFPBRFReferenceItemButtonCardSection
+ __OBJC_METACLASS_RO_$__SFPBRFReferenceItemLogoCardSection
+ __OBJC_METACLASS_RO_$__SFPBRFSecondaryHeaderEmphasizedCardSection
+ __OBJC_METACLASS_RO_$__SFPBRFSecondaryHeaderStandardCardSection
+ __OBJC_METACLASS_RO_$__SFPBRFSimpleItemReverseRichCardSection
+ __OBJC_METACLASS_RO_$__SFPBRFSimpleItemRichSearchResultCardSection
+ __OBJC_METACLASS_RO_$__SFPBRFSimpleItemVisualElementCardSection
+ __OBJC_METACLASS_RO_$__SFPBRFSummaryItemButtonCardSection
+ __OBJC_METACLASS_RO_$__SFPBRFSummaryItemImageRightCardSection
+ __OBJC_METACLASS_RO_$__SFPBRFSummaryItemPlayerCardSection
+ __OBJC_METACLASS_RO_$__SFPBRequestProductPageCommand
+ __OBJC_METACLASS_RO_$__SFPBShortcutsImage
+ __OBJC_METACLASS_RO_$__SFPBStoreButtonItem
+ __OBJC_PROTOCOL_$_RFBinaryButtonCardSection
+ __OBJC_PROTOCOL_$_RFButtonCardSection
+ __OBJC_PROTOCOL_$_RFFont
+ __OBJC_PROTOCOL_$_RFPrimaryHeaderStackedImageCardSection
+ __OBJC_PROTOCOL_$_RFReferenceCenteredCardSection
+ __OBJC_PROTOCOL_$_RFReferenceItemButtonCardSection
+ __OBJC_PROTOCOL_$_RFReferenceItemLogoCardSection
+ __OBJC_PROTOCOL_$_RFSecondaryHeaderEmphasizedCardSection
+ __OBJC_PROTOCOL_$_RFSecondaryHeaderStandardCardSection
+ __OBJC_PROTOCOL_$_RFSimpleItemReverseRichCardSection
+ __OBJC_PROTOCOL_$_RFSimpleItemRichSearchResultCardSection
+ __OBJC_PROTOCOL_$_RFSimpleItemVisualElementCardSection
+ __OBJC_PROTOCOL_$_RFSummaryItemButtonCardSection
+ __OBJC_PROTOCOL_$_RFSummaryItemImageRightCardSection
+ __OBJC_PROTOCOL_$_RFSummaryItemPlayerCardSection
+ __OBJC_PROTOCOL_$_RFSystemFont
+ __OBJC_PROTOCOL_$_SFHashBucketDetail
+ __OBJC_PROTOCOL_$_SFHashDetail
+ __OBJC_PROTOCOL_$_SFPlayAudioButtonItem
+ __OBJC_PROTOCOL_$_SFPlayWatchListItemButtonItem
+ __OBJC_PROTOCOL_$_SFRequestProductPageCommand
+ __OBJC_PROTOCOL_$_SFShortcutsImage
+ __OBJC_PROTOCOL_$_SFStoreButtonItem
+ __OBJC_PROTOCOL_$__SFPBHashBucketDetail
+ __OBJC_PROTOCOL_$__SFPBHashBucketDetail_HashDetail
+ __OBJC_PROTOCOL_$__SFPBPlayAudioButtonItem
+ __OBJC_PROTOCOL_$__SFPBPlayWatchListItemButtonItem
+ __OBJC_PROTOCOL_$__SFPBRFBinaryButtonCardSection
+ __OBJC_PROTOCOL_$__SFPBRFButtonCardSection
+ __OBJC_PROTOCOL_$__SFPBRFFont
+ __OBJC_PROTOCOL_$__SFPBRFFont_RFSystemFont
+ __OBJC_PROTOCOL_$__SFPBRFPrimaryHeaderStackedImageCardSection
+ __OBJC_PROTOCOL_$__SFPBRFReferenceCenteredCardSection
+ __OBJC_PROTOCOL_$__SFPBRFReferenceItemButtonCardSection
+ __OBJC_PROTOCOL_$__SFPBRFReferenceItemLogoCardSection
+ __OBJC_PROTOCOL_$__SFPBRFSecondaryHeaderEmphasizedCardSection
+ __OBJC_PROTOCOL_$__SFPBRFSecondaryHeaderStandardCardSection
+ __OBJC_PROTOCOL_$__SFPBRFSimpleItemReverseRichCardSection
+ __OBJC_PROTOCOL_$__SFPBRFSimpleItemRichSearchResultCardSection
+ __OBJC_PROTOCOL_$__SFPBRFSimpleItemVisualElementCardSection
+ __OBJC_PROTOCOL_$__SFPBRFSummaryItemButtonCardSection
+ __OBJC_PROTOCOL_$__SFPBRFSummaryItemImageRightCardSection
+ __OBJC_PROTOCOL_$__SFPBRFSummaryItemPlayerCardSection
+ __OBJC_PROTOCOL_$__SFPBRequestProductPageCommand
+ __OBJC_PROTOCOL_$__SFPBShortcutsImage
+ __OBJC_PROTOCOL_$__SFPBStoreButtonItem
+ __SFPBHashBucketDetailReadFrom
+ __SFPBHashBucketDetail_HashDetailReadFrom
+ __SFPBPlayAudioButtonItemReadFrom
+ __SFPBPlayWatchListItemButtonItemReadFrom
+ __SFPBRFBinaryButtonCardSectionReadFrom
+ __SFPBRFButtonCardSectionReadFrom
+ __SFPBRFFontReadFrom
+ __SFPBRFFont_RFSystemFontReadFrom
+ __SFPBRFPrimaryHeaderStackedImageCardSectionReadFrom
+ __SFPBRFReferenceCenteredCardSectionReadFrom
+ __SFPBRFReferenceItemButtonCardSectionReadFrom
+ __SFPBRFReferenceItemLogoCardSectionReadFrom
+ __SFPBRFSecondaryHeaderEmphasizedCardSectionReadFrom
+ __SFPBRFSecondaryHeaderStandardCardSectionReadFrom
+ __SFPBRFSimpleItemReverseRichCardSectionReadFrom
+ __SFPBRFSimpleItemRichSearchResultCardSectionReadFrom
+ __SFPBRFSimpleItemVisualElementCardSectionReadFrom
+ __SFPBRFSummaryItemButtonCardSectionReadFrom
+ __SFPBRFSummaryItemImageRightCardSectionReadFrom
+ __SFPBRFSummaryItemPlayerCardSectionReadFrom
+ __SFPBRequestProductPageCommandReadFrom
+ __SFPBShortcutsImageReadFrom
+ __SFPBStoreButtonItemReadFrom
+ ___PARLogHandleForCategory_block_invoke.56500
+ ___PARLogHandleForCategory_block_invoke.60063
+ ___block_literal_global.106
+ ___block_literal_global.114
+ ___block_literal_global.56495
+ ___block_literal_global.56875
+ ___block_literal_global.60076
+ ___getDispatchQueue_block_invoke.60080
+ _getDispatchQueue.60074
+ _getDispatchQueue.onceToken.60075
+ _getDispatchQueue.queue.60077
+ _objc_msgSend$actionTypesToShow
+ _objc_msgSend$actionTypesToShows
+ _objc_msgSend$addActionTypesToShow:
+ _objc_msgSend$addHash_details:
+ _objc_msgSend$addTint
+ _objc_msgSend$add_tint
+ _objc_msgSend$applySmallCaps
+ _objc_msgSend$buttonItemsAreBottom
+ _objc_msgSend$distributorBundleIdentifier
+ _objc_msgSend$fillStyle
+ _objc_msgSend$font
+ _objc_msgSend$full_hash
+ _objc_msgSend$gridStyle
+ _objc_msgSend$hasAddTint
+ _objc_msgSend$hasAdd_tint
+ _objc_msgSend$hasApplySmallCaps
+ _objc_msgSend$hasButtonItemsAreBottom
+ _objc_msgSend$hasFillStyle
+ _objc_msgSend$hasGridStyle
+ _objc_msgSend$hasHas_ee
+ _objc_msgSend$hasHas_summary
+ _objc_msgSend$hasIsInsetGrouped
+ _objc_msgSend$hasItemIdentifier
+ _objc_msgSend$hasSearchInAppType
+ _objc_msgSend$hasShouldAddToWatchList
+ _objc_msgSend$hasShouldOpenAppAfterInstallCompletes
+ _objc_msgSend$hasShouldPause
+ _objc_msgSend$hasSystem
+ _objc_msgSend$hasVersionIdentifier
+ _objc_msgSend$hasVertical_alignment
+ _objc_msgSend$hasWeight
+ _objc_msgSend$has_ee
+ _objc_msgSend$has_summary
+ _objc_msgSend$hash_details
+ _objc_msgSend$hash_prefix
+ _objc_msgSend$iFunScore
+ _objc_msgSend$indexOfResultInSectionWhenRanked
+ _objc_msgSend$indexOfSectionWhenRanked
+ _objc_msgSend$isInsetGrouped
+ _objc_msgSend$itemIdentifier
+ _objc_msgSend$lnPropertyIdentifier
+ _objc_msgSend$mediaIdentifier
+ _objc_msgSend$playAudioButtonItem
+ _objc_msgSend$playWatchListItemButtonItem
+ _objc_msgSend$primary_button
+ _objc_msgSend$requestProductPageCommand
+ _objc_msgSend$rfBinaryButtonCardSection
+ _objc_msgSend$rfButtonCardSection
+ _objc_msgSend$rfPrimaryHeaderStackedImageCardSection
+ _objc_msgSend$rfReferenceCenteredCardSection
+ _objc_msgSend$rfReferenceItemButtonCardSection
+ _objc_msgSend$rfReferenceItemLogoCardSection
+ _objc_msgSend$rfSecondaryHeaderEmphasizedCardSection
+ _objc_msgSend$rfSecondaryHeaderStandardCardSection
+ _objc_msgSend$rfSimpleItemReverseRichCardSection
+ _objc_msgSend$rfSimpleItemRichSearchResultCardSection
+ _objc_msgSend$rfSimpleItemVisualElementCardSection
+ _objc_msgSend$rfSummaryItemButtonCardSection
+ _objc_msgSend$rfSummaryItemImageRightCardSection
+ _objc_msgSend$rfSummaryItemPlayerCardSection
+ _objc_msgSend$searchInAppType
+ _objc_msgSend$secondary_button
+ _objc_msgSend$setActionTypesToShow:
+ _objc_msgSend$setActionTypesToShows:
+ _objc_msgSend$setAddTint:
+ _objc_msgSend$setAdd_tint:
+ _objc_msgSend$setApplySmallCaps:
+ _objc_msgSend$setButtonItemsAreBottom:
+ _objc_msgSend$setDistributorBundleIdentifier:
+ _objc_msgSend$setFillStyle:
+ _objc_msgSend$setFont:
+ _objc_msgSend$setFull_hash:
+ _objc_msgSend$setGridStyle:
+ _objc_msgSend$setHas_ee:
+ _objc_msgSend$setHas_summary:
+ _objc_msgSend$setHash_details:
+ _objc_msgSend$setHash_prefix:
+ _objc_msgSend$setIFunScore:
+ _objc_msgSend$setIndexOfResultInSectionWhenRanked:
+ _objc_msgSend$setIndexOfSectionWhenRanked:
+ _objc_msgSend$setIsInsetGrouped:
+ _objc_msgSend$setItemIdentifier:
+ _objc_msgSend$setLnPropertyIdentifier:
+ _objc_msgSend$setMediaIdentifier:
+ _objc_msgSend$setPlayAudioButtonItem:
+ _objc_msgSend$setPlayWatchListItemButtonItem:
+ _objc_msgSend$setPrimary_button:
+ _objc_msgSend$setRequestProductPageCommand:
+ _objc_msgSend$setRfBinaryButtonCardSection:
+ _objc_msgSend$setRfButtonCardSection:
+ _objc_msgSend$setRfPrimaryHeaderStackedImageCardSection:
+ _objc_msgSend$setRfReferenceCenteredCardSection:
+ _objc_msgSend$setRfReferenceItemButtonCardSection:
+ _objc_msgSend$setRfReferenceItemLogoCardSection:
+ _objc_msgSend$setRfSecondaryHeaderEmphasizedCardSection:
+ _objc_msgSend$setRfSecondaryHeaderStandardCardSection:
+ _objc_msgSend$setRfSimpleItemReverseRichCardSection:
+ _objc_msgSend$setRfSimpleItemRichSearchResultCardSection:
+ _objc_msgSend$setRfSimpleItemVisualElementCardSection:
+ _objc_msgSend$setRfSummaryItemButtonCardSection:
+ _objc_msgSend$setRfSummaryItemImageRightCardSection:
+ _objc_msgSend$setRfSummaryItemPlayerCardSection:
+ _objc_msgSend$setSearchInAppType:
+ _objc_msgSend$setSecondary_button:
+ _objc_msgSend$setShortcutsImage:
+ _objc_msgSend$setShouldAddToWatchList:
+ _objc_msgSend$setShouldOpenAppAfterInstallCompletes:
+ _objc_msgSend$setShouldPause:
+ _objc_msgSend$setStoreButtonItem:
+ _objc_msgSend$setSystem:
+ _objc_msgSend$setThumbnail2:
+ _objc_msgSend$setVersionIdentifier:
+ _objc_msgSend$setVertical_alignment:
+ _objc_msgSend$setWeight:
+ _objc_msgSend$shortcutsImage
+ _objc_msgSend$shouldAddToWatchList
+ _objc_msgSend$shouldOpenAppAfterInstallCompletes
+ _objc_msgSend$shouldPause
+ _objc_msgSend$storeButtonItem
+ _objc_msgSend$system
+ _objc_msgSend$thumbnail2
+ _objc_msgSend$versionIdentifier
+ _objc_msgSend$vertical_alignment
+ _objc_msgSend$weight
- GCC_except_table5674
- GCC_except_table6419
- _PARLogHandleForCategory.logHandles.0.51573
- _PARLogHandleForCategory.logHandles.0.54678
- _PARLogHandleForCategory.logHandles.1.51567
- _PARLogHandleForCategory.logHandles.1.54675
- _PARLogHandleForCategory.logHandles.2.51575
- _PARLogHandleForCategory.logHandles.2.54680
- _PARLogHandleForCategory.logHandles.3.51576
- _PARLogHandleForCategory.logHandles.3.54681
- _PARLogHandleForCategory.logHandles.4.51577
- _PARLogHandleForCategory.logHandles.4.54683
- _PARLogHandleForCategory.logHandles.5.51578
- _PARLogHandleForCategory.logHandles.5.54684
- _PARLogHandleForCategory.onceToken.51565
- _PARLogHandleForCategory.onceToken.54674
- __OBJC_$_CLASS_METHODS_SFDomainEngagementScore(ProtobufInitializer)
- __OBJC_$_CLASS_METHODS_SFEngagementSignal(ProtobufInitializer)
- __OBJC_$_INSTANCE_METHODS_SFDomainEngagementScore(ProtobufInitializer)
- __OBJC_$_INSTANCE_METHODS_SFEngagementSignal(ProtobufInitializer)
- __OBJC_$_PROP_LIST_RFAppIconImage.87
- __OBJC_$_PROP_LIST_RFAspectRatio.81
- __OBJC_$_PROP_LIST_RFAttribution.126
- __OBJC_$_PROP_LIST_RFAvatarImage.88
- __OBJC_$_PROP_LIST_RFBadgedImage.81
- __OBJC_$_PROP_LIST_RFColor.98
- __OBJC_$_PROP_LIST_RFDefaultBrowserAppIconImage.76
- __OBJC_$_PROP_LIST_RFExpandableStandardCardSection.201
- __OBJC_$_PROP_LIST_RFExpandingComponentContent.89
- __OBJC_$_PROP_LIST_RFFactItemButtonCardSection.241
- __OBJC_$_PROP_LIST_RFFactItemDetailedNumberCardSection.216
- __OBJC_$_PROP_LIST_RFFactItemHeroButtonCardSection.206
- __OBJC_$_PROP_LIST_RFFactItemHeroNumberCardSection.218
- __OBJC_$_PROP_LIST_RFFactItemImageRightCardSection.206
- __OBJC_$_PROP_LIST_RFFactItemShortHeroNumberCardSection.227
- __OBJC_$_PROP_LIST_RFFactItemShortNumberCardSection.227
- __OBJC_$_PROP_LIST_RFFactItemStandardCardSection.222
- __OBJC_$_PROP_LIST_RFFormattedText.144
- __OBJC_$_PROP_LIST_RFHighlightedSubstring.75
- __OBJC_$_PROP_LIST_RFImageElement.76
- __OBJC_$_PROP_LIST_RFImageSource.148
- __OBJC_$_PROP_LIST_RFLongItemStandardCardSection.207
- __OBJC_$_PROP_LIST_RFMonogramImage.87
- __OBJC_$_PROP_LIST_RFOptionalBool.75
- __OBJC_$_PROP_LIST_RFOptionalFloat.76
- __OBJC_$_PROP_LIST_RFPrimaryHeaderMarqueeCardSection.206
- __OBJC_$_PROP_LIST_RFPrimaryHeaderRichCardSection.216
- __OBJC_$_PROP_LIST_RFPrimaryHeaderStandardCardSection.202
- __OBJC_$_PROP_LIST_RFRGBValue.86
- __OBJC_$_PROP_LIST_RFReferenceFootnoteCardSection.207
- __OBJC_$_PROP_LIST_RFReferenceRichCardSection.206
- __OBJC_$_PROP_LIST_RFReferenceStandardCardSection.192
- __OBJC_$_PROP_LIST_RFShowMoreOnTap.75
- __OBJC_$_PROP_LIST_RFSimpleItemPlayerCardSection.217
- __OBJC_$_PROP_LIST_RFSimpleItemRichCardSection.237
- __OBJC_$_PROP_LIST_RFSimpleItemStandardCardSection.218
- __OBJC_$_PROP_LIST_RFSummaryItemAlignedTextCardSection.227
- __OBJC_$_PROP_LIST_RFSummaryItemDetailedTextCardSection.226
- __OBJC_$_PROP_LIST_RFSummaryItemPairCardSection.216
- __OBJC_$_PROP_LIST_RFSummaryItemPairNumberCardSection.237
- __OBJC_$_PROP_LIST_RFSummaryItemShortNumberCardSection.232
- __OBJC_$_PROP_LIST_RFSummaryItemStandardCardSection.226
- __OBJC_$_PROP_LIST_RFSummaryItemSwitchV2CardSection.225
- __OBJC_$_PROP_LIST_RFSummaryItemTextCardSection.213
- __OBJC_$_PROP_LIST_RFSymbolImage.121
- __OBJC_$_PROP_LIST_RFTableCell.108
- __OBJC_$_PROP_LIST_RFTableColumnDefinition.89
- __OBJC_$_PROP_LIST_RFTableContentColumnDefinition.98
- __OBJC_$_PROP_LIST_RFTableHeaderCardSection.199
- __OBJC_$_PROP_LIST_RFTableRowCardSection.189
- __OBJC_$_PROP_LIST_RFTableSpacerColumnDefinition.64
- __OBJC_$_PROP_LIST_RFTextElement.94
- __OBJC_$_PROP_LIST_RFTextEncapsulation.76
- __OBJC_$_PROP_LIST_RFTextProperty.87
- __OBJC_$_PROP_LIST_RFUrlImage.123
- __OBJC_$_PROP_LIST_RFVisualElement.79
- __OBJC_$_PROP_LIST_RFVisualProperty.87
- __OBJC_$_PROP_LIST_SFAbstractCommand.88
- __OBJC_$_PROP_LIST_SFActionItem.269
- __OBJC_$_PROP_LIST_SFActivityIndicatorCardSection.191
- __OBJC_$_PROP_LIST_SFAddToPhotosLibraryCommand.104
- __OBJC_$_PROP_LIST_SFAirport.133
- __OBJC_$_PROP_LIST_SFApiResults.94
- __OBJC_$_PROP_LIST_SFAppAutoShortcutsButtonItem.83
- __OBJC_$_PROP_LIST_SFAppAutoShortcutsItem.75
- __OBJC_$_PROP_LIST_SFAppColor.104
- __OBJC_$_PROP_LIST_SFAppIconCardSection.196
- __OBJC_$_PROP_LIST_SFAppIconImage.144
- __OBJC_$_PROP_LIST_SFAppLink.105
- __OBJC_$_PROP_LIST_SFAppLinkCardSection.199
- __OBJC_$_PROP_LIST_SFArchiveViewCardSection.194
- __OBJC_$_PROP_LIST_SFAttributionFooterCardSection.214
- __OBJC_$_PROP_LIST_SFAudioPlaybackCardSection.234
- __OBJC_$_PROP_LIST_SFBeginMapsRoutingCommand.137
- __OBJC_$_PROP_LIST_SFButton.92
- __OBJC_$_PROP_LIST_SFButtonCardSection.204
- __OBJC_$_PROP_LIST_SFButtonItem.75
- __OBJC_$_PROP_LIST_SFButtonListCardSection.202
- __OBJC_$_PROP_LIST_SFCATModel.88
- __OBJC_$_PROP_LIST_SFCalendarColor.104
- __OBJC_$_PROP_LIST_SFCalendarEvent.114
- __OBJC_$_PROP_LIST_SFCalendarImage.138
- __OBJC_$_PROP_LIST_SFCallCommand.101
- __OBJC_$_PROP_LIST_SFCard.309
- __OBJC_$_PROP_LIST_SFCardMetadata.86
- __OBJC_$_PROP_LIST_SFCardSearchMetadata.97
- __OBJC_$_PROP_LIST_SFCardSectionValue.886
- __OBJC_$_PROP_LIST_SFClearProactiveCategoryCommand.122
- __OBJC_$_PROP_LIST_SFClockImage.148
- __OBJC_$_PROP_LIST_SFCloudChannelsRequestItem.85
- __OBJC_$_PROP_LIST_SFCollectionCardSection.224
- __OBJC_$_PROP_LIST_SFCollectionStyle.75
- __OBJC_$_PROP_LIST_SFCollectionStyleGrid.80
- __OBJC_$_PROP_LIST_SFCollectionStyleHorizontallyScrolling.80
- __OBJC_$_PROP_LIST_SFCollectionStyleRow.82
- __OBJC_$_PROP_LIST_SFColor.116
- __OBJC_$_PROP_LIST_SFColorBarCardSection.208
- __OBJC_$_PROP_LIST_SFCombinedCardSection.192
- __OBJC_$_PROP_LIST_SFCommand.102
- __OBJC_$_PROP_LIST_SFCommandButtonItem.120
- __OBJC_$_PROP_LIST_SFCommandReference.75
- __OBJC_$_PROP_LIST_SFCommandRowCardSection.219
- __OBJC_$_PROP_LIST_SFCommandValue.76
- __OBJC_$_PROP_LIST_SFCompactRowCardSection.218
- __OBJC_$_PROP_LIST_SFContactButtonItem.91
- __OBJC_$_PROP_LIST_SFContactCopyItem.87
- __OBJC_$_PROP_LIST_SFContactImage.153
- __OBJC_$_PROP_LIST_SFCopyCommand.104
- __OBJC_$_PROP_LIST_SFCopyItem.64
- __OBJC_$_PROP_LIST_SFCoreSpotlightButtonItem.96
- __OBJC_$_PROP_LIST_SFCoreSpotlightCopyItem.96
- __OBJC_$_PROP_LIST_SFCoreSpotlightRankingSignals.129
- __OBJC_$_PROP_LIST_SFCoreSpotlightShareItem.87
- __OBJC_$_PROP_LIST_SFCreateCalendarEventCommand.104
- __OBJC_$_PROP_LIST_SFCreateContactCommand.115
- __OBJC_$_PROP_LIST_SFCreateReminderCommand.104
- __OBJC_$_PROP_LIST_SFDescriptionCardSection.289
- __OBJC_$_PROP_LIST_SFDetailedRowCardSection.319
- __OBJC_$_PROP_LIST_SFDomainEngagementScore.93
- __OBJC_$_PROP_LIST_SFDomainSubscriptionRequestItem.64
- __OBJC_$_PROP_LIST_SFDrillDownMetadata.147
- __OBJC_$_PROP_LIST_SFDynamicURLImageResource.111
- __OBJC_$_PROP_LIST_SFEmailCommand.101
- __OBJC_$_PROP_LIST_SFEngagementSignal.105
- __OBJC_$_PROP_LIST_SFEntitySearchMetadata.90
- __OBJC_$_PROP_LIST_SFExpandInlineCommand.103
- __OBJC_$_PROP_LIST_SFFindMyCardSection.192
- __OBJC_$_PROP_LIST_SFFlight.119
- __OBJC_$_PROP_LIST_SFFlightCardSection.206
- __OBJC_$_PROP_LIST_SFFlightLeg.175
- __OBJC_$_PROP_LIST_SFFlightTopic.92
- __OBJC_$_PROP_LIST_SFFormattedText.121
- __OBJC_$_PROP_LIST_SFGradientColor.114
- __OBJC_$_PROP_LIST_SFGridCardSection.192
- __OBJC_$_PROP_LIST_SFHeroCardSection.224
- __OBJC_$_PROP_LIST_SFHeroTitleCardSection.217
- __OBJC_$_PROP_LIST_SFHorizontalButtonCardSection.192
- __OBJC_$_PROP_LIST_SFHorizontalScrollCardSection.203
- __OBJC_$_PROP_LIST_SFImage.166
- __OBJC_$_PROP_LIST_SFImageCopyItem.78
- __OBJC_$_PROP_LIST_SFImageDerivedColor.105
- __OBJC_$_PROP_LIST_SFImageOption.88
- __OBJC_$_PROP_LIST_SFImagesCardSection.201
- __OBJC_$_PROP_LIST_SFIndexState.96
- __OBJC_$_PROP_LIST_SFIndexedUserActivityCommand.106
- __OBJC_$_PROP_LIST_SFInfoCardSection.203
- __OBJC_$_PROP_LIST_SFInfoTuple.100
- __OBJC_$_PROP_LIST_SFInvokeSiriCommand.101
- __OBJC_$_PROP_LIST_SFKeyValueDataCardSection.201
- __OBJC_$_PROP_LIST_SFKeyValueTuple.80
- __OBJC_$_PROP_LIST_SFLargeTitleDetailedRowCardSection.210
- __OBJC_$_PROP_LIST_SFLatLng.82
- __OBJC_$_PROP_LIST_SFLaunchAppCommand.101
- __OBJC_$_PROP_LIST_SFLeadingTrailingCardSection.209
- __OBJC_$_PROP_LIST_SFLinkPresentationCardSection.209
- __OBJC_$_PROP_LIST_SFListenToCardSection.204
- __OBJC_$_PROP_LIST_SFLocalImage.135
- __OBJC_$_PROP_LIST_SFLocalTopic.86
- __OBJC_$_PROP_LIST_SFLocationTypeInfo.75
- __OBJC_$_PROP_LIST_SFMailRankingSignals.145
- __OBJC_$_PROP_LIST_SFMailResultDetails.93
- __OBJC_$_PROP_LIST_SFManageReservationCommand.103
- __OBJC_$_PROP_LIST_SFMapCardSection.248
- __OBJC_$_PROP_LIST_SFMapPlaceCardSection.208
- __OBJC_$_PROP_LIST_SFMapRegion.100
- __OBJC_$_PROP_LIST_SFMapsDetailedRowCardSection.205
- __OBJC_$_PROP_LIST_SFMediaArtworkImage.154
- __OBJC_$_PROP_LIST_SFMediaDetail.84
- __OBJC_$_PROP_LIST_SFMediaInfoCardSection.260
- __OBJC_$_PROP_LIST_SFMediaItem.141
- __OBJC_$_PROP_LIST_SFMediaMetadata.116
- __OBJC_$_PROP_LIST_SFMediaOffer.224
- __OBJC_$_PROP_LIST_SFMediaPlayerCardSection.202
- __OBJC_$_PROP_LIST_SFMediaRemoteControlCardSection.205
- __OBJC_$_PROP_LIST_SFMessageAttachment.105
- __OBJC_$_PROP_LIST_SFMessageCardSection.224
- __OBJC_$_PROP_LIST_SFMetaInfoCardSection.218
- __OBJC_$_PROP_LIST_SFMiniCardSection.209
- __OBJC_$_PROP_LIST_SFMonogramImage.144
- __OBJC_$_PROP_LIST_SFMoreResults.75
- __OBJC_$_PROP_LIST_SFNamedProtobufMessage.83
- __OBJC_$_PROP_LIST_SFNewsCardSection.228
- __OBJC_$_PROP_LIST_SFNowPlayingCardSection.199
- __OBJC_$_PROP_LIST_SFOpenAppClipCommand.101
- __OBJC_$_PROP_LIST_SFOpenCalculationCommand.106
- __OBJC_$_PROP_LIST_SFOpenCoreSpotlightItemCommand.111
- __OBJC_$_PROP_LIST_SFOpenFileProviderItemCommand.117
- __OBJC_$_PROP_LIST_SFOpenMediaCommand.110
- __OBJC_$_PROP_LIST_SFOpenPunchoutCommand.104
- __OBJC_$_PROP_LIST_SFOpenWebClipCommand.101
- __OBJC_$_PROP_LIST_SFPatternModel.93
- __OBJC_$_PROP_LIST_SFPerformContactActionCommand.119
- __OBJC_$_PROP_LIST_SFPerformContactQueryCommand.101
- __OBJC_$_PROP_LIST_SFPerformEntityQueryCommand.155
- __OBJC_$_PROP_LIST_SFPerformIntentCommand.123
- __OBJC_$_PROP_LIST_SFPerformPersonEntityQueryCommand.104
- __OBJC_$_PROP_LIST_SFPerson.104
- __OBJC_$_PROP_LIST_SFPersonHeaderCardSection.192
- __OBJC_$_PROP_LIST_SFPhotosLibraryImage.158
- __OBJC_$_PROP_LIST_SFPin.123
- __OBJC_$_PROP_LIST_SFPlayMediaCommand.116
- __OBJC_$_PROP_LIST_SFPlayVideoCommand.104
- __OBJC_$_PROP_LIST_SFProduct.105
- __OBJC_$_PROP_LIST_SFProductAvailability.76
- __OBJC_$_PROP_LIST_SFProductCardSection.194
- __OBJC_$_PROP_LIST_SFProductInventory.127
- __OBJC_$_PROP_LIST_SFProductInventoryResult.84
- __OBJC_$_PROP_LIST_SFQueryTopic.94
- __OBJC_$_PROP_LIST_SFQueryUnderstandingParse.169
- __OBJC_$_PROP_LIST_SFQuickLookThumbnailImage.149
- __OBJC_$_PROP_LIST_SFReferentialCommand.75
- __OBJC_$_PROP_LIST_SFRejectPeopleInPhotoCommand.113
- __OBJC_$_PROP_LIST_SFReminder.89
- __OBJC_$_PROP_LIST_SFRequestAppClipInstallCommand.110
- __OBJC_$_PROP_LIST_SFRequestUserReportCommand.104
- __OBJC_$_PROP_LIST_SFResponseWrapperCardSection.215
- __OBJC_$_PROP_LIST_SFResultEntity.89
- __OBJC_$_PROP_LIST_SFRichText.112
- __OBJC_$_PROP_LIST_SFRichTitleCardSection.358
- __OBJC_$_PROP_LIST_SFRowCardSection.275
- __OBJC_$_PROP_LIST_SFRunVoiceShortcutCommand.106
- __OBJC_$_PROP_LIST_SFScene.85
- __OBJC_$_PROP_LIST_SFScoreboardCardSection.218
- __OBJC_$_PROP_LIST_SFSearchInAppCommand.106
- __OBJC_$_PROP_LIST_SFSearchSuggestion.164
- __OBJC_$_PROP_LIST_SFSearchWebCommand.101
- __OBJC_$_PROP_LIST_SFSectionHeaderCardSection.195
- __OBJC_$_PROP_LIST_SFSelectableGridCardSection.201
- __OBJC_$_PROP_LIST_SFShareCommand.104
- __OBJC_$_PROP_LIST_SFShareItem.64
- __OBJC_$_PROP_LIST_SFShowAppStoreSheetCommand.106
- __OBJC_$_PROP_LIST_SFShowContactCardCommand.112
- __OBJC_$_PROP_LIST_SFShowPhotosOneUpViewCommand.136
- __OBJC_$_PROP_LIST_SFShowPurchaseRequestSheetCommand.101
- __OBJC_$_PROP_LIST_SFShowSFCardCommand.104
- __OBJC_$_PROP_LIST_SFShowScreenTimeRequestSheetCommand.101
- __OBJC_$_PROP_LIST_SFShowWrapperResponseViewCommand.104
- __OBJC_$_PROP_LIST_SFSocialMediaPostCardSection.252
- __OBJC_$_PROP_LIST_SFSplitCardSection.224
- __OBJC_$_PROP_LIST_SFSportsFollowButtonItem.92
- __OBJC_$_PROP_LIST_SFSportsItem.87
- __OBJC_$_PROP_LIST_SFSportsSubscriptionRequestItem.87
- __OBJC_$_PROP_LIST_SFSportsTeam.119
- __OBJC_$_PROP_LIST_SFSportsTopic.87
- __OBJC_$_PROP_LIST_SFStockChartCardSection.203
- __OBJC_$_PROP_LIST_SFStrokeAnimationCardSection.207
- __OBJC_$_PROP_LIST_SFStructuredLocation.96
- __OBJC_$_PROP_LIST_SFSubscribeForUpdatesCommand.113
- __OBJC_$_PROP_LIST_SFSuggestionCardSection.244
- __OBJC_$_PROP_LIST_SFSymbolImage.163
- __OBJC_$_PROP_LIST_SFTableAlignmentSchema.84
- __OBJC_$_PROP_LIST_SFTableColumnAlignment.91
- __OBJC_$_PROP_LIST_SFTableHeaderRowCardSection.211
- __OBJC_$_PROP_LIST_SFTableRowCardSection.244
- __OBJC_$_PROP_LIST_SFText.86
- __OBJC_$_PROP_LIST_SFTextColumn.76
- __OBJC_$_PROP_LIST_SFTextColumnSection.96
- __OBJC_$_PROP_LIST_SFTextColumnsCardSection.208
- __OBJC_$_PROP_LIST_SFTextCopyItem.77
- __OBJC_$_PROP_LIST_SFTitleCardSection.205
- __OBJC_$_PROP_LIST_SFTitleSubtitleTuple.80
- __OBJC_$_PROP_LIST_SFToggleAudioCommand.123
- __OBJC_$_PROP_LIST_SFToggleButtonConfiguration.94
- __OBJC_$_PROP_LIST_SFToggleWatchListStatusCommand.104
- __OBJC_$_PROP_LIST_SFTopic.70
- __OBJC_$_PROP_LIST_SFTrack.114
- __OBJC_$_PROP_LIST_SFTrackListCardSection.199
- __OBJC_$_PROP_LIST_SFURLImage.143
- __OBJC_$_PROP_LIST_SFURLShareItem.78
- __OBJC_$_PROP_LIST_SFUpdateSearchQueryCommand.113
- __OBJC_$_PROP_LIST_SFUpdateSportsFollowingStatusCommand.115
- __OBJC_$_PROP_LIST_SFUserActivityData.84
- __OBJC_$_PROP_LIST_SFUserActivityInfo.101
- __OBJC_$_PROP_LIST_SFUserReportRequest.130
- __OBJC_$_PROP_LIST_SFVerticalLayoutCardSection.229
- __OBJC_$_PROP_LIST_SFViewEmailCommand.103
- __OBJC_$_PROP_LIST_SFWatchListButtonItem.83
- __OBJC_$_PROP_LIST_SFWatchListCardSection.195
- __OBJC_$_PROP_LIST_SFWatchListItem.141
- __OBJC_$_PROP_LIST_SFWatchNowCardSection.200
- __OBJC_$_PROP_LIST_SFWeatherColor.122
- __OBJC_$_PROP_LIST_SFWeatherTopic.92
- __OBJC_$_PROP_LIST_SFWebCardSection.191
- __OBJC_$_PROP_LIST_SFWorldMapCardSection.200
- __OBJC_$_PROP_LIST__SFPBAbstractCommand.92
- __OBJC_$_PROP_LIST__SFPBActionItem.387
- __OBJC_$_PROP_LIST__SFPBActivityIndicatorCardSection.476
- __OBJC_$_PROP_LIST__SFPBAddToPhotosLibraryCommand.491
- __OBJC_$_PROP_LIST__SFPBAirport.583
- __OBJC_$_PROP_LIST__SFPBApiResults.621
- __OBJC_$_PROP_LIST__SFPBAppAutoShortcutsButtonItem.652
- __OBJC_$_PROP_LIST__SFPBAppAutoShortcutsItem.667
- __OBJC_$_PROP_LIST__SFPBAppColor.674
- __OBJC_$_PROP_LIST__SFPBAppIconCardSection.689
- __OBJC_$_PROP_LIST__SFPBAppIconImage.704
- __OBJC_$_PROP_LIST__SFPBAppLink.727
- __OBJC_$_PROP_LIST__SFPBAppLinkCardSection.757
- __OBJC_$_PROP_LIST__SFPBArchiveViewCardSection.772
- __OBJC_$_PROP_LIST__SFPBAttributionFooterCardSection.816
- __OBJC_$_PROP_LIST__SFPBAudioPlaybackCardSection.869
- __OBJC_$_PROP_LIST__SFPBBeginMapsRoutingCommand.876
- __OBJC_$_PROP_LIST__SFPBButton.899
- __OBJC_$_PROP_LIST__SFPBButtonCardSection.906
- __OBJC_$_PROP_LIST__SFPBButtonItem.996
- __OBJC_$_PROP_LIST__SFPBButtonListCardSection.1034
- __OBJC_$_PROP_LIST__SFPBCATModel.1057
- __OBJC_$_PROP_LIST__SFPBCalendarColor.1072
- __OBJC_$_PROP_LIST__SFPBCalendarEvent.1122
- __OBJC_$_PROP_LIST__SFPBCalendarImage.1137
- __OBJC_$_PROP_LIST__SFPBCallCommand.1144
- __OBJC_$_PROP_LIST__SFPBCard.1327
- __OBJC_$_PROP_LIST__SFPBCardMetadata.1350
- __OBJC_$_PROP_LIST__SFPBCardSearchMetadata.1381
- __OBJC_$_PROP_LIST__SFPBCardSection.1554
- __OBJC_$_PROP_LIST__SFPBCardSectionValue.2744
- __OBJC_$_PROP_LIST__SFPBClearProactiveCategoryCommand.2775
- __OBJC_$_PROP_LIST__SFPBClockImage.2805
- __OBJC_$_PROP_LIST__SFPBCloudChannelsRequestItem.2836
- __OBJC_$_PROP_LIST__SFPBCollectionCardSection.2873
- __OBJC_$_PROP_LIST__SFPBCollectionStyle.2931
- __OBJC_$_PROP_LIST__SFPBCollectionStyleGrid.2945
- __OBJC_$_PROP_LIST__SFPBCollectionStyleHorizontallyScrolling.2959
- __OBJC_$_PROP_LIST__SFPBCollectionStyleRow.2973
- __OBJC_$_PROP_LIST__SFPBColor.3093
- __OBJC_$_PROP_LIST__SFPBColorBarCardSection.3116
- __OBJC_$_PROP_LIST__SFPBCombinedCardSection.3123
- __OBJC_$_PROP_LIST__SFPBCommand.3796
- __OBJC_$_PROP_LIST__SFPBCommandButtonItem.3811
- __OBJC_$_PROP_LIST__SFPBCommandReference.3826
- __OBJC_$_PROP_LIST__SFPBCommandRowCardSection.3849
- __OBJC_$_PROP_LIST__SFPBCommandValue.3869
- __OBJC_$_PROP_LIST__SFPBCompactRowCardSection.3884
- __OBJC_$_PROP_LIST__SFPBContactButtonItem.3904
- __OBJC_$_PROP_LIST__SFPBContactCopyItem.3919
- __OBJC_$_PROP_LIST__SFPBContactImage.3954
- __OBJC_$_PROP_LIST__SFPBCopyCommand.3974
- __OBJC_$_PROP_LIST__SFPBCopyItem.4033
- __OBJC_$_PROP_LIST__SFPBCoreSpotlightButtonItem.4060
- __OBJC_$_PROP_LIST__SFPBCoreSpotlightCopyItem.4091
- __OBJC_$_PROP_LIST__SFPBCoreSpotlightRankingSignals.4173
- __OBJC_$_PROP_LIST__SFPBCoreSpotlightShareItem.4188
- __OBJC_$_PROP_LIST__SFPBCreateCalendarEventCommand.4208
- __OBJC_$_PROP_LIST__SFPBCreateContactCommand.4223
- __OBJC_$_PROP_LIST__SFPBCreateReminderCommand.4243
- __OBJC_$_PROP_LIST__SFPBDate.4261
- __OBJC_$_PROP_LIST__SFPBDescriptionCardSection.4374
- __OBJC_$_PROP_LIST__SFPBDetailedRowCardSection.4548
- __OBJC_$_PROP_LIST__SFPBDomainEngagementScore.4578
- __OBJC_$_PROP_LIST__SFPBDomainSubscriptionRequestItem.4598
- __OBJC_$_PROP_LIST__SFPBDrillDownMetadata.4705
- __OBJC_$_PROP_LIST__SFPBDynamicURLImageResource.4759
- __OBJC_$_PROP_LIST__SFPBEmailCommand.4766
- __OBJC_$_PROP_LIST__SFPBEngagementSignal.4828
- __OBJC_$_PROP_LIST__SFPBEntitySearchMetadata.4852
- __OBJC_$_PROP_LIST__SFPBExpandInlineCommand.4866
- __OBJC_$_PROP_LIST__SFPBFindMyCardSection.4873
- __OBJC_$_PROP_LIST__SFPBFlight.4959
- __OBJC_$_PROP_LIST__SFPBFlightCardSection.4985
- __OBJC_$_PROP_LIST__SFPBFlightDetails.4999
- __OBJC_$_PROP_LIST__SFPBFlightLeg.5139
- __OBJC_$_PROP_LIST__SFPBFormattedText.5187
- __OBJC_$_PROP_LIST__SFPBGradientColor.5215
- __OBJC_$_PROP_LIST__SFPBGraphicalFloat.5229
- __OBJC_$_PROP_LIST__SFPBGridCardSection.5236
- __OBJC_$_PROP_LIST__SFPBHeroCardSection.5243
- __OBJC_$_PROP_LIST__SFPBHeroTitleCardSection.5258
- __OBJC_$_PROP_LIST__SFPBHorizontalButtonCardSection.5277
- __OBJC_$_PROP_LIST__SFPBHorizontalScrollCardSection.5284
- __OBJC_$_PROP_LIST__SFPBImage.5536
- __OBJC_$_PROP_LIST__SFPBImageCopyItem.5543
- __OBJC_$_PROP_LIST__SFPBImageDerivedColor.5550
- __OBJC_$_PROP_LIST__SFPBImageOption.5578
- __OBJC_$_PROP_LIST__SFPBImagesCardSection.5606
- __OBJC_$_PROP_LIST__SFPBIndexState.5652
- __OBJC_$_PROP_LIST__SFPBIndexedUserActivityCommand.5667
- __OBJC_$_PROP_LIST__SFPBInfoCardSection.5697
- __OBJC_$_PROP_LIST__SFPBInfoTuple.5741
- __OBJC_$_PROP_LIST__SFPBInvokeSiriCommand.5756
- __OBJC_$_PROP_LIST__SFPBKeyValueDataCardSection.5787
- __OBJC_$_PROP_LIST__SFPBKeyValueTuple.5795
- __OBJC_$_PROP_LIST__SFPBLargeTitleDetailedRowCardSection.5825
- __OBJC_$_PROP_LIST__SFPBLatLng.5847
- __OBJC_$_PROP_LIST__SFPBLaunchAppCommand.5854
- __OBJC_$_PROP_LIST__SFPBLeadingTrailingCardSection.5893
- __OBJC_$_PROP_LIST__SFPBLinkPresentationCardSection.5930
- __OBJC_$_PROP_LIST__SFPBListenToCardSection.5961
- __OBJC_$_PROP_LIST__SFPBLocalImage.5975
- __OBJC_$_PROP_LIST__SFPBLocationTypeInfo.5990
- __OBJC_$_PROP_LIST__SFPBMailRankingSignals.6092
- __OBJC_$_PROP_LIST__SFPBMailResultDetails.6122
- __OBJC_$_PROP_LIST__SFPBManageReservationCommand.6128
- __OBJC_$_PROP_LIST__SFPBMapCardSection.6204
- __OBJC_$_PROP_LIST__SFPBMapPlaceCardSection.6219
- __OBJC_$_PROP_LIST__SFPBMapRegion.6265
- __OBJC_$_PROP_LIST__SFPBMapsDetailedRowCardSection.6280
- __OBJC_$_PROP_LIST__SFPBMediaArtworkImage.6295
- __OBJC_$_PROP_LIST__SFPBMediaDetail.6310
- __OBJC_$_PROP_LIST__SFPBMediaInfoCardSection.6424
- __OBJC_$_PROP_LIST__SFPBMediaItem.6504
- __OBJC_$_PROP_LIST__SFPBMediaMetadata.6576
- __OBJC_$_PROP_LIST__SFPBMediaOffer.6615
- __OBJC_$_PROP_LIST__SFPBMediaPlayerCardSection.6635
- __OBJC_$_PROP_LIST__SFPBMediaRemoteControlCardSection.6666
- __OBJC_$_PROP_LIST__SFPBMessageAttachment.6682
- __OBJC_$_PROP_LIST__SFPBMessageCardSection.6734
- __OBJC_$_PROP_LIST__SFPBMetaInfoCardSection.6773
- __OBJC_$_PROP_LIST__SFPBMiniCardSection.6780
- __OBJC_$_PROP_LIST__SFPBMonogramImage.6803
- __OBJC_$_PROP_LIST__SFPBMoreResults.6810
- __OBJC_$_PROP_LIST__SFPBNamedProtobufMessage.6833
- __OBJC_$_PROP_LIST__SFPBNewsCardSection.6864
- __OBJC_$_PROP_LIST__SFPBNowPlayingCardSection.6883
- __OBJC_$_PROP_LIST__SFPBOpenAppClipCommand.6898
- __OBJC_$_PROP_LIST__SFPBOpenCalculationCommand.6921
- __OBJC_$_PROP_LIST__SFPBOpenCoreSpotlightItemCommand.6936
- __OBJC_$_PROP_LIST__SFPBOpenFileProviderItemCommand.6959
- __OBJC_$_PROP_LIST__SFPBOpenMediaCommand.6974
- __OBJC_$_PROP_LIST__SFPBOpenPunchoutCommand.6981
- __OBJC_$_PROP_LIST__SFPBOpenWebClipCommand.6988
- __OBJC_$_PROP_LIST__SFPBPatternModel.7027
- __OBJC_$_PROP_LIST__SFPBPerformContactActionCommand.7057
- __OBJC_$_PROP_LIST__SFPBPerformContactQueryCommand.7064
- __OBJC_$_PROP_LIST__SFPBPerformEntityQueryCommand.7103
- __OBJC_$_PROP_LIST__SFPBPerformIntentCommand.7118
- __OBJC_$_PROP_LIST__SFPBPerformPersonEntityQueryCommand.7125
- __OBJC_$_PROP_LIST__SFPBPerson.7180
- __OBJC_$_PROP_LIST__SFPBPersonHeaderCardSection.7187
- __OBJC_$_PROP_LIST__SFPBPhotosLibraryImage.7223
- __OBJC_$_PROP_LIST__SFPBPin.7238
- __OBJC_$_PROP_LIST__SFPBPlayMediaCommand.7253
- __OBJC_$_PROP_LIST__SFPBPlayVideoCommand.7260
- __OBJC_$_PROP_LIST__SFPBPointSize.7283
- __OBJC_$_PROP_LIST__SFPBProduct.7314
- __OBJC_$_PROP_LIST__SFPBProductAvailability.7336
- __OBJC_$_PROP_LIST__SFPBProductCardSection.7351
- __OBJC_$_PROP_LIST__SFPBProductInventory.7407
- __OBJC_$_PROP_LIST__SFPBProductInventoryResult.7430
- __OBJC_$_PROP_LIST__SFPBPunchout.7487
- __OBJC_$_PROP_LIST__SFPBQueryUnderstandingParse.7621
- __OBJC_$_PROP_LIST__SFPBQuickLookThumbnailImage.7636
- __OBJC_$_PROP_LIST__SFPBRFAppIconImage.7656
- __OBJC_$_PROP_LIST__SFPBRFAspectRatio.7664
- __OBJC_$_PROP_LIST__SFPBRFAttribution.7716
- __OBJC_$_PROP_LIST__SFPBRFAvatarImage.7735
- __OBJC_$_PROP_LIST__SFPBRFBadgedImage.7749
- __OBJC_$_PROP_LIST__SFPBRFColor.7783
- __OBJC_$_PROP_LIST__SFPBRFDefaultBrowserAppIconImage.7789
- __OBJC_$_PROP_LIST__SFPBRFExpandableStandardCardSection.7824
- __OBJC_$_PROP_LIST__SFPBRFExpandingComponentContent.7847
- __OBJC_$_PROP_LIST__SFPBRFFactItemButtonCardSection.7925
- __OBJC_$_PROP_LIST__SFPBRFFactItemDetailedNumberCardSection.7940
- __OBJC_$_PROP_LIST__SFPBRFFactItemHeroButtonCardSection.7948
- __OBJC_$_PROP_LIST__SFPBRFFactItemHeroNumberCardSection.7985
- __OBJC_$_PROP_LIST__SFPBRFFactItemImageRightCardSection.7992
- __OBJC_$_PROP_LIST__SFPBRFFactItemShortHeroNumberCardSection.7999
- __OBJC_$_PROP_LIST__SFPBRFFactItemShortNumberCardSection.8006
- __OBJC_$_PROP_LIST__SFPBRFFactItemStandardCardSection.8022
- __OBJC_$_PROP_LIST__SFPBRFFormattedText.8126
- __OBJC_$_PROP_LIST__SFPBRFHighlightedSubstring.8141
- __OBJC_$_PROP_LIST__SFPBRFImageElement.8161
- __OBJC_$_PROP_LIST__SFPBRFImageSource.8260
- __OBJC_$_PROP_LIST__SFPBRFLongItemStandardCardSection.8283
- __OBJC_$_PROP_LIST__SFPBRFMonogramImage.8298
- __OBJC_$_PROP_LIST__SFPBRFOptionalBool.8305
- __OBJC_$_PROP_LIST__SFPBRFOptionalFloat.8312
- __OBJC_$_PROP_LIST__SFPBRFPrimaryHeaderMarqueeCardSection.8319
- __OBJC_$_PROP_LIST__SFPBRFPrimaryHeaderRichCardSection.8326
- __OBJC_$_PROP_LIST__SFPBRFPrimaryHeaderStandardCardSection.8333
- __OBJC_$_PROP_LIST__SFPBRFRGBValue.8363
- __OBJC_$_PROP_LIST__SFPBRFReferenceFootnoteCardSection.8370
- __OBJC_$_PROP_LIST__SFPBRFReferenceRichCardSection.8377
- __OBJC_$_PROP_LIST__SFPBRFReferenceStandardCardSection.8384
- __OBJC_$_PROP_LIST__SFPBRFShowMoreOnTap.8399
- __OBJC_$_PROP_LIST__SFPBRFSimpleItemPlayerCardSection.8414
- __OBJC_$_PROP_LIST__SFPBRFSimpleItemRichCardSection.8445
- __OBJC_$_PROP_LIST__SFPBRFSimpleItemStandardCardSection.8452
- __OBJC_$_PROP_LIST__SFPBRFSummaryItemAlignedTextCardSection.8468
- __OBJC_$_PROP_LIST__SFPBRFSummaryItemDetailedTextCardSection.8475
- __OBJC_$_PROP_LIST__SFPBRFSummaryItemPairCardSection.8498
- __OBJC_$_PROP_LIST__SFPBRFSummaryItemPairNumberCardSection.8521
- __OBJC_$_PROP_LIST__SFPBRFSummaryItemShortNumberCardSection.8528
- __OBJC_$_PROP_LIST__SFPBRFSummaryItemStandardCardSection.8543
- __OBJC_$_PROP_LIST__SFPBRFSummaryItemSwitchV2CardSection.8558
- __OBJC_$_PROP_LIST__SFPBRFSummaryItemTextCardSection.8565
- __OBJC_$_PROP_LIST__SFPBRFSymbolImage.8604
- __OBJC_$_PROP_LIST__SFPBRFTableCell.8640
- __OBJC_$_PROP_LIST__SFPBRFTableColumnDefinition.8670
- __OBJC_$_PROP_LIST__SFPBRFTableContentColumnDefinition.8700
- __OBJC_$_PROP_LIST__SFPBRFTableHeaderCardSection.8749
- __OBJC_$_PROP_LIST__SFPBRFTableRowCardSection.8756
- __OBJC_$_PROP_LIST__SFPBRFTableSpacerColumnDefinition.8762
- __OBJC_$_PROP_LIST__SFPBRFTextElement.8806
- __OBJC_$_PROP_LIST__SFPBRFTextEncapsulation.8820
- __OBJC_$_PROP_LIST__SFPBRFTextProperty.8850
- __OBJC_$_PROP_LIST__SFPBRFUrlImage.8906
- __OBJC_$_PROP_LIST__SFPBRFVisualElement.8925
- __OBJC_$_PROP_LIST__SFPBRFVisualProperty.8947
- __OBJC_$_PROP_LIST__SFPBReferentialCommand.8954
- __OBJC_$_PROP_LIST__SFPBRejectPeopleInPhotoCommand.8974
- __OBJC_$_PROP_LIST__SFPBReminder.8989
- __OBJC_$_PROP_LIST__SFPBRequestAppClipInstallCommand.8996
- __OBJC_$_PROP_LIST__SFPBRequestUserReportCommand.9003
- __OBJC_$_PROP_LIST__SFPBResponseWrapperCardSection.9057
- __OBJC_$_PROP_LIST__SFPBResultEntity.9085
- __OBJC_$_PROP_LIST__SFPBRichText.9125
- __OBJC_$_PROP_LIST__SFPBRichTitleCardSection.9273
- __OBJC_$_PROP_LIST__SFPBRowCardSection.9368
- __OBJC_$_PROP_LIST__SFPBRunVoiceShortcutCommand.9383
- __OBJC_$_PROP_LIST__SFPBScene.9405
- __OBJC_$_PROP_LIST__SFPBScoreboardCardSection.9449
- __OBJC_$_PROP_LIST__SFPBSearchInAppCommand.9456
- __OBJC_$_PROP_LIST__SFPBSearchSuggestion.9538
- __OBJC_$_PROP_LIST__SFPBSearchWebCommand.9545
- __OBJC_$_PROP_LIST__SFPBSectionHeaderCardSection.9553
- __OBJC_$_PROP_LIST__SFPBSelectableGridCardSection.9583
- __OBJC_$_PROP_LIST__SFPBShareCommand.9603
- __OBJC_$_PROP_LIST__SFPBShareItem.9636
- __OBJC_$_PROP_LIST__SFPBShowAppStoreSheetCommand.9651
- __OBJC_$_PROP_LIST__SFPBShowContactCardCommand.9666
- __OBJC_$_PROP_LIST__SFPBShowPhotosOneUpViewCommand.9717
- __OBJC_$_PROP_LIST__SFPBShowPurchaseRequestSheetCommand.9732
- __OBJC_$_PROP_LIST__SFPBShowSFCardCommand.9747
- __OBJC_$_PROP_LIST__SFPBShowScreenTimeRequestSheetCommand.9754
- __OBJC_$_PROP_LIST__SFPBShowWrapperResponseViewCommand.9761
- __OBJC_$_PROP_LIST__SFPBSocialMediaPostCardSection.9825
- __OBJC_$_PROP_LIST__SFPBSplitCardSection.9892
- __OBJC_$_PROP_LIST__SFPBSportsDetail.9907
- __OBJC_$_PROP_LIST__SFPBSportsFollowButtonItem.9940
- __OBJC_$_PROP_LIST__SFPBSportsItem.9947
- __OBJC_$_PROP_LIST__SFPBSportsSubscriptionRequestItem.9978
- __OBJC_$_PROP_LIST__SFPBSportsTeam.10010
- __OBJC_$_PROP_LIST__SFPBStockChartCardSection.10033
- __OBJC_$_PROP_LIST__SFPBStringDictionary.10052
- __OBJC_$_PROP_LIST__SFPBStrokeAnimationCardSection.10103
- __OBJC_$_PROP_LIST__SFPBStructuredLocation.10126
- __OBJC_$_PROP_LIST__SFPBSubscribeForUpdatesCommand.10159
- __OBJC_$_PROP_LIST__SFPBSuggestionCardSection.10198
- __OBJC_$_PROP_LIST__SFPBSymbolImage.10232
- __OBJC_$_PROP_LIST__SFPBTableAlignmentSchema.10256
- __OBJC_$_PROP_LIST__SFPBTableColumnAlignment.10286
- __OBJC_$_PROP_LIST__SFPBTableHeaderRowCardSection.10354
- __OBJC_$_PROP_LIST__SFPBTableRowCardSection.10374
- __OBJC_$_PROP_LIST__SFPBText.10391
- __OBJC_$_PROP_LIST__SFPBTextColumn.10413
- __OBJC_$_PROP_LIST__SFPBTextColumnSection.10448
- __OBJC_$_PROP_LIST__SFPBTextColumnsCardSection.10459
- __OBJC_$_PROP_LIST__SFPBTextCopyItem.10474
- __OBJC_$_PROP_LIST__SFPBTimeZone.10481
- __OBJC_$_PROP_LIST__SFPBTitleCardSection.10488
- __OBJC_$_PROP_LIST__SFPBTitleSubtitleTuple.10495
- __OBJC_$_PROP_LIST__SFPBToggleAudioCommand.10518
- __OBJC_$_PROP_LIST__SFPBToggleButtonConfiguration.10542
- __OBJC_$_PROP_LIST__SFPBToggleWatchListStatusCommand.10562
- __OBJC_$_PROP_LIST__SFPBTopic.10605
- __OBJC_$_PROP_LIST__SFPBTrack.10637
- __OBJC_$_PROP_LIST__SFPBTrackListCardSection.10659
- __OBJC_$_PROP_LIST__SFPBURL.10666
- __OBJC_$_PROP_LIST__SFPBURLImage.10681
- __OBJC_$_PROP_LIST__SFPBURLShareItem.10688
- __OBJC_$_PROP_LIST__SFPBUpdateSearchQueryCommand.10703
- __OBJC_$_PROP_LIST__SFPBUpdateSportsFollowingStatusCommand.10718
- __OBJC_$_PROP_LIST__SFPBUserActivityData.10749
- __OBJC_$_PROP_LIST__SFPBUserActivityInfo.10772
- __OBJC_$_PROP_LIST__SFPBUserReportRequest.10847
- __OBJC_$_PROP_LIST__SFPBVerticalLayoutCardSection.10878
- __OBJC_$_PROP_LIST__SFPBViewEmailCommand.10884
- __OBJC_$_PROP_LIST__SFPBWatchListButtonItem.10891
- __OBJC_$_PROP_LIST__SFPBWatchListCardSection.10898
- __OBJC_$_PROP_LIST__SFPBWatchListItem.10977
- __OBJC_$_PROP_LIST__SFPBWatchNowCardSection.10991
- __OBJC_$_PROP_LIST__SFPBWeatherColor.11006
- __OBJC_$_PROP_LIST__SFPBWeatherDetails.11013
- __OBJC_$_PROP_LIST__SFPBWebCardSection.11028
- __OBJC_$_PROP_LIST__SFPBWorldMapCardSection.11051
- ___PARLogHandleForCategory_block_invoke.51571
- ___PARLogHandleForCategory_block_invoke.54677
- ___block_literal_global.105
- ___block_literal_global.113
- ___block_literal_global.51566
- ___block_literal_global.51932
- ___block_literal_global.54687
- ___getDispatchQueue_block_invoke.54691
- _getDispatchQueue.54685
- _getDispatchQueue.onceToken.54686
- _getDispatchQueue.queue.54688
CStrings:
+ "\x0f\x0f\x0f\b"
+ "\x0f\x0f\x0f\x0f\x0f\x0f\x0f"
+ "/\x06"
+ "228"
+ "229"
+ "230"
+ "231"
+ "232"
+ "233"
+ "234"
+ "235"
+ "236"
+ "237"
+ "238"
+ "239"
+ "240"
+ "241"
+ "62"
+ "@\"RFBinaryButtonCardSection\""
+ "@\"RFBinaryButtonCardSection\"16@0:8"
+ "@\"RFButtonCardSection\""
+ "@\"RFButtonCardSection\"16@0:8"
+ "@\"RFFont\""
+ "@\"RFFont\"16@0:8"
+ "@\"RFPrimaryHeaderStackedImageCardSection\""
+ "@\"RFPrimaryHeaderStackedImageCardSection\"16@0:8"
+ "@\"RFReferenceCenteredCardSection\""
+ "@\"RFReferenceCenteredCardSection\"16@0:8"
+ "@\"RFReferenceItemButtonCardSection\""
+ "@\"RFReferenceItemButtonCardSection\"16@0:8"
+ "@\"RFReferenceItemLogoCardSection\""
+ "@\"RFReferenceItemLogoCardSection\"16@0:8"
+ "@\"RFSecondaryHeaderEmphasizedCardSection\""
+ "@\"RFSecondaryHeaderEmphasizedCardSection\"16@0:8"
+ "@\"RFSecondaryHeaderStandardCardSection\""
+ "@\"RFSecondaryHeaderStandardCardSection\"16@0:8"
+ "@\"RFSimpleItemReverseRichCardSection\""
+ "@\"RFSimpleItemReverseRichCardSection\"16@0:8"
+ "@\"RFSimpleItemRichSearchResultCardSection\""
+ "@\"RFSimpleItemRichSearchResultCardSection\"16@0:8"
+ "@\"RFSimpleItemVisualElementCardSection\""
+ "@\"RFSimpleItemVisualElementCardSection\"16@0:8"
+ "@\"RFSummaryItemButtonCardSection\""
+ "@\"RFSummaryItemButtonCardSection\"16@0:8"
+ "@\"RFSummaryItemImageRightCardSection\""
+ "@\"RFSummaryItemImageRightCardSection\"16@0:8"
+ "@\"RFSummaryItemPlayerCardSection\""
+ "@\"RFSummaryItemPlayerCardSection\"16@0:8"
+ "@\"RFSystemFont\""
+ "@\"RFSystemFont\"16@0:8"
+ "@\"_SFPBHashBucketDetail_HashDetail\"24@0:8Q16"
+ "@\"_SFPBPlayAudioButtonItem\""
+ "@\"_SFPBPlayAudioButtonItem\"16@0:8"
+ "@\"_SFPBPlayWatchListItemButtonItem\""
+ "@\"_SFPBPlayWatchListItemButtonItem\"16@0:8"
+ "@\"_SFPBRFBinaryButtonCardSection\""
+ "@\"_SFPBRFBinaryButtonCardSection\"16@0:8"
+ "@\"_SFPBRFButtonCardSection\""
+ "@\"_SFPBRFButtonCardSection\"16@0:8"
+ "@\"_SFPBRFFont\""
+ "@\"_SFPBRFFont\"16@0:8"
+ "@\"_SFPBRFFont_RFSystemFont\""
+ "@\"_SFPBRFFont_RFSystemFont\"16@0:8"
+ "@\"_SFPBRFPrimaryHeaderStackedImageCardSection\""
+ "@\"_SFPBRFPrimaryHeaderStackedImageCardSection\"16@0:8"
+ "@\"_SFPBRFReferenceCenteredCardSection\""
+ "@\"_SFPBRFReferenceCenteredCardSection\"16@0:8"
+ "@\"_SFPBRFReferenceItemButtonCardSection\""
+ "@\"_SFPBRFReferenceItemButtonCardSection\"16@0:8"
+ "@\"_SFPBRFReferenceItemLogoCardSection\""
+ "@\"_SFPBRFReferenceItemLogoCardSection\"16@0:8"
+ "@\"_SFPBRFSecondaryHeaderEmphasizedCardSection\""
+ "@\"_SFPBRFSecondaryHeaderEmphasizedCardSection\"16@0:8"
+ "@\"_SFPBRFSecondaryHeaderStandardCardSection\""
+ "@\"_SFPBRFSecondaryHeaderStandardCardSection\"16@0:8"
+ "@\"_SFPBRFSimpleItemReverseRichCardSection\""
+ "@\"_SFPBRFSimpleItemReverseRichCardSection\"16@0:8"
+ "@\"_SFPBRFSimpleItemRichSearchResultCardSection\""
+ "@\"_SFPBRFSimpleItemRichSearchResultCardSection\"16@0:8"
+ "@\"_SFPBRFSimpleItemVisualElementCardSection\""
+ "@\"_SFPBRFSimpleItemVisualElementCardSection\"16@0:8"
+ "@\"_SFPBRFSummaryItemButtonCardSection\""
+ "@\"_SFPBRFSummaryItemButtonCardSection\"16@0:8"
+ "@\"_SFPBRFSummaryItemImageRightCardSection\""
+ "@\"_SFPBRFSummaryItemImageRightCardSection\"16@0:8"
+ "@\"_SFPBRFSummaryItemPlayerCardSection\""
+ "@\"_SFPBRFSummaryItemPlayerCardSection\"16@0:8"
+ "@\"_SFPBRFVisualProperty\"24@0:8Q16"
+ "@\"_SFPBRequestProductPageCommand\""
+ "@\"_SFPBRequestProductPageCommand\"16@0:8"
+ "@\"_SFPBShortcutsImage\""
+ "@\"_SFPBShortcutsImage\"16@0:8"
+ "@\"_SFPBStoreButtonItem\""
+ "@\"_SFPBStoreButtonItem\"16@0:8"
+ "@64@0:8@16@24@32@40@48@56"
+ "RFBinaryButtonCardSection"
+ "RFButtonCardSection"
+ "RFFont"
+ "RFPrimaryHeaderStackedImageCardSection"
+ "RFReferenceCenteredCardSection"
+ "RFReferenceItemButtonCardSection"
+ "RFReferenceItemLogoCardSection"
+ "RFSecondaryHeaderEmphasizedCardSection"
+ "RFSecondaryHeaderStandardCardSection"
+ "RFSimpleItemReverseRichCardSection"
+ "RFSimpleItemRichSearchResultCardSection"
+ "RFSimpleItemVisualElementCardSection"
+ "RFSummaryItemButtonCardSection"
+ "RFSummaryItemImageRightCardSection"
+ "RFSummaryItemPlayerCardSection"
+ "RFSystemFont"
+ "SFHashBucketDetail"
+ "SFHashDetail"
+ "SFPlayAudioButtonItem"
+ "SFPlayWatchListItemButtonItem"
+ "SFRequestProductPageCommand"
+ "SFShortcutsImage"
+ "SFStoreButtonItem"
+ "T@\"NSArray\",C,N,V_actionTypesToShow"
+ "T@\"NSArray\",C,N,V_actionTypesToShows"
+ "T@\"NSArray\",C,N,V_hash_details"
+ "T@\"NSNumber\",&,N,V_indexOfResultInSectionWhenRanked"
+ "T@\"NSNumber\",&,N,V_indexOfSectionWhenRanked"
+ "T@\"NSNumber\",C,N,V_iFunScore"
+ "T@\"NSNumber\",C,N,V_size"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",C,N,V_distributorBundleIdentifier"
+ "T@\"NSString\",C,N,V_full_hash"
+ "T@\"NSString\",C,N,V_hash_prefix"
+ "T@\"NSString\",C,N,V_lnPropertyIdentifier"
+ "T@\"NSString\",C,N,V_mediaIdentifier"
+ "T@\"RFBinaryButtonCardSection\",&,N"
+ "T@\"RFBinaryButtonCardSection\",&,N,V_rfBinaryButtonCardSection"
+ "T@\"RFButtonCardSection\",&,N"
+ "T@\"RFButtonCardSection\",&,N,V_rfButtonCardSection"
+ "T@\"RFFont\",&,N"
+ "T@\"RFFont\",&,N,V_font"
+ "T@\"RFPrimaryHeaderStackedImageCardSection\",&,N"
+ "T@\"RFPrimaryHeaderStackedImageCardSection\",&,N,V_rfPrimaryHeaderStackedImageCardSection"
+ "T@\"RFReferenceCenteredCardSection\",&,N"
+ "T@\"RFReferenceCenteredCardSection\",&,N,V_rfReferenceCenteredCardSection"
+ "T@\"RFReferenceItemButtonCardSection\",&,N"
+ "T@\"RFReferenceItemButtonCardSection\",&,N,V_rfReferenceItemButtonCardSection"
+ "T@\"RFReferenceItemLogoCardSection\",&,N"
+ "T@\"RFReferenceItemLogoCardSection\",&,N,V_rfReferenceItemLogoCardSection"
+ "T@\"RFSecondaryHeaderEmphasizedCardSection\",&,N"
+ "T@\"RFSecondaryHeaderEmphasizedCardSection\",&,N,V_rfSecondaryHeaderEmphasizedCardSection"
+ "T@\"RFSecondaryHeaderStandardCardSection\",&,N"
+ "T@\"RFSecondaryHeaderStandardCardSection\",&,N,V_rfSecondaryHeaderStandardCardSection"
+ "T@\"RFSimpleItemReverseRichCardSection\",&,N"
+ "T@\"RFSimpleItemReverseRichCardSection\",&,N,V_rfSimpleItemReverseRichCardSection"
+ "T@\"RFSimpleItemRichSearchResultCardSection\",&,N"
+ "T@\"RFSimpleItemRichSearchResultCardSection\",&,N,V_rfSimpleItemRichSearchResultCardSection"
+ "T@\"RFSimpleItemVisualElementCardSection\",&,N"
+ "T@\"RFSimpleItemVisualElementCardSection\",&,N,V_rfSimpleItemVisualElementCardSection"
+ "T@\"RFSummaryItemButtonCardSection\",&,N"
+ "T@\"RFSummaryItemButtonCardSection\",&,N,V_rfSummaryItemButtonCardSection"
+ "T@\"RFSummaryItemImageRightCardSection\",&,N"
+ "T@\"RFSummaryItemImageRightCardSection\",&,N,V_rfSummaryItemImageRightCardSection"
+ "T@\"RFSummaryItemPlayerCardSection\",&,N"
+ "T@\"RFSummaryItemPlayerCardSection\",&,N,V_rfSummaryItemPlayerCardSection"
+ "T@\"RFSystemFont\",&,N"
+ "T@\"RFSystemFont\",&,N,V_system"
+ "T@\"RFTextProperty\",&,N,V_footnote"
+ "T@\"RFVisualProperty\",&,N,V_thumbnail2"
+ "T@\"SFButtonItem\",&,N,V_primary_button"
+ "T@\"SFButtonItem\",&,N,V_secondary_button"
+ "T@\"_SFPBButtonItem\",&,N,V_primary_button"
+ "T@\"_SFPBButtonItem\",&,N,V_secondary_button"
+ "T@\"_SFPBPlayAudioButtonItem\",&,N"
+ "T@\"_SFPBPlayAudioButtonItem\",&,N,V_playAudioButtonItem"
+ "T@\"_SFPBPlayWatchListItemButtonItem\",&,N"
+ "T@\"_SFPBPlayWatchListItemButtonItem\",&,N,V_playWatchListItemButtonItem"
+ "T@\"_SFPBRFBinaryButtonCardSection\",&,N"
+ "T@\"_SFPBRFBinaryButtonCardSection\",&,N,V_rfBinaryButtonCardSection"
+ "T@\"_SFPBRFButtonCardSection\",&,N"
+ "T@\"_SFPBRFButtonCardSection\",&,N,V_rfButtonCardSection"
+ "T@\"_SFPBRFFont\",&,N"
+ "T@\"_SFPBRFFont\",&,N,V_font"
+ "T@\"_SFPBRFFont_RFSystemFont\",&,N"
+ "T@\"_SFPBRFFont_RFSystemFont\",&,N,V_system"
+ "T@\"_SFPBRFPrimaryHeaderStackedImageCardSection\",&,N"
+ "T@\"_SFPBRFPrimaryHeaderStackedImageCardSection\",&,N,V_rfPrimaryHeaderStackedImageCardSection"
+ "T@\"_SFPBRFReferenceCenteredCardSection\",&,N"
+ "T@\"_SFPBRFReferenceCenteredCardSection\",&,N,V_rfReferenceCenteredCardSection"
+ "T@\"_SFPBRFReferenceItemButtonCardSection\",&,N"
+ "T@\"_SFPBRFReferenceItemButtonCardSection\",&,N,V_rfReferenceItemButtonCardSection"
+ "T@\"_SFPBRFReferenceItemLogoCardSection\",&,N"
+ "T@\"_SFPBRFReferenceItemLogoCardSection\",&,N,V_rfReferenceItemLogoCardSection"
+ "T@\"_SFPBRFSecondaryHeaderEmphasizedCardSection\",&,N"
+ "T@\"_SFPBRFSecondaryHeaderEmphasizedCardSection\",&,N,V_rfSecondaryHeaderEmphasizedCardSection"
+ "T@\"_SFPBRFSecondaryHeaderStandardCardSection\",&,N"
+ "T@\"_SFPBRFSecondaryHeaderStandardCardSection\",&,N,V_rfSecondaryHeaderStandardCardSection"
+ "T@\"_SFPBRFSimpleItemReverseRichCardSection\",&,N"
+ "T@\"_SFPBRFSimpleItemReverseRichCardSection\",&,N,V_rfSimpleItemReverseRichCardSection"
+ "T@\"_SFPBRFSimpleItemRichSearchResultCardSection\",&,N"
+ "T@\"_SFPBRFSimpleItemRichSearchResultCardSection\",&,N,V_rfSimpleItemRichSearchResultCardSection"
+ "T@\"_SFPBRFSimpleItemVisualElementCardSection\",&,N"
+ "T@\"_SFPBRFSimpleItemVisualElementCardSection\",&,N,V_rfSimpleItemVisualElementCardSection"
+ "T@\"_SFPBRFSummaryItemButtonCardSection\",&,N"
+ "T@\"_SFPBRFSummaryItemButtonCardSection\",&,N,V_rfSummaryItemButtonCardSection"
+ "T@\"_SFPBRFSummaryItemImageRightCardSection\",&,N"
+ "T@\"_SFPBRFSummaryItemImageRightCardSection\",&,N,V_rfSummaryItemImageRightCardSection"
+ "T@\"_SFPBRFSummaryItemPlayerCardSection\",&,N"
+ "T@\"_SFPBRFSummaryItemPlayerCardSection\",&,N,V_rfSummaryItemPlayerCardSection"
+ "T@\"_SFPBRFTextProperty\",&,N,V_footnote"
+ "T@\"_SFPBRFVisualProperty\",&,N,V_thumbnail2"
+ "T@\"_SFPBRequestProductPageCommand\",&,N"
+ "T@\"_SFPBRequestProductPageCommand\",&,N,V_requestProductPageCommand"
+ "T@\"_SFPBShortcutsImage\",&,N"
+ "T@\"_SFPBShortcutsImage\",&,N,V_shortcutsImage"
+ "T@\"_SFPBStoreButtonItem\",&,N"
+ "T@\"_SFPBStoreButtonItem\",&,N,V_storeButtonItem"
+ "TB,N,V_addTint"
+ "TB,N,V_add_tint"
+ "TB,N,V_applySmallCaps"
+ "TB,N,V_buttonItemsAreBottom"
+ "TB,N,V_has_ee"
+ "TB,N,V_has_summary"
+ "TB,N,V_isInsetGrouped"
+ "TB,N,V_shouldAddToWatchList"
+ "TB,N,V_shouldOpenAppAfterInstallCompletes"
+ "TB,N,V_shouldPause"
+ "TQ,N,V_itemIdentifier"
+ "TQ,N,V_versionIdentifier"
+ "Tf,N,V_iFunScore"
+ "Tf,N,V_size"
+ "Ti,N,V_fillStyle"
+ "Ti,N,V_gridStyle"
+ "Ti,N,V_searchInAppType"
+ "Ti,N,V_vertical_alignment"
+ "Ti,N,V_weight"
+ "_SFPBHashBucketDetail"
+ "_SFPBHashBucketDetail_HashDetail"
+ "_SFPBPlayAudioButtonItem"
+ "_SFPBPlayWatchListItemButtonItem"
+ "_SFPBRFBinaryButtonCardSection"
+ "_SFPBRFButtonCardSection"
+ "_SFPBRFFont"
+ "_SFPBRFFont_RFSystemFont"
+ "_SFPBRFPrimaryHeaderStackedImageCardSection"
+ "_SFPBRFReferenceCenteredCardSection"
+ "_SFPBRFReferenceItemButtonCardSection"
+ "_SFPBRFReferenceItemLogoCardSection"
+ "_SFPBRFSecondaryHeaderEmphasizedCardSection"
+ "_SFPBRFSecondaryHeaderStandardCardSection"
+ "_SFPBRFSimpleItemReverseRichCardSection"
+ "_SFPBRFSimpleItemRichSearchResultCardSection"
+ "_SFPBRFSimpleItemVisualElementCardSection"
+ "_SFPBRFSummaryItemButtonCardSection"
+ "_SFPBRFSummaryItemImageRightCardSection"
+ "_SFPBRFSummaryItemPlayerCardSection"
+ "_SFPBRequestProductPageCommand"
+ "_SFPBShortcutsImage"
+ "_SFPBStoreButtonItem"
+ "_actionTypesToShow"
+ "_actionTypesToShows"
+ "_addTint"
+ "_add_tint"
+ "_applySmallCaps"
+ "_buttonItemsAreBottom"
+ "_distributorBundleIdentifier"
+ "_fillStyle"
+ "_font"
+ "_full_hash"
+ "_gridStyle"
+ "_has_ee"
+ "_has_summary"
+ "_hash_details"
+ "_hash_prefix"
+ "_iFunScore"
+ "_indexOfResultInSectionWhenRanked"
+ "_indexOfSectionWhenRanked"
+ "_isInsetGrouped"
+ "_itemIdentifier"
+ "_lnPropertyIdentifier"
+ "_mediaIdentifier"
+ "_playAudioButtonItem"
+ "_playWatchListItemButtonItem"
+ "_primary_button"
+ "_requestProductPageCommand"
+ "_rfBinaryButtonCardSection"
+ "_rfButtonCardSection"
+ "_rfPrimaryHeaderStackedImageCardSection"
+ "_rfReferenceCenteredCardSection"
+ "_rfReferenceItemButtonCardSection"
+ "_rfReferenceItemLogoCardSection"
+ "_rfSecondaryHeaderEmphasizedCardSection"
+ "_rfSecondaryHeaderStandardCardSection"
+ "_rfSimpleItemReverseRichCardSection"
+ "_rfSimpleItemRichSearchResultCardSection"
+ "_rfSimpleItemVisualElementCardSection"
+ "_rfSummaryItemButtonCardSection"
+ "_rfSummaryItemImageRightCardSection"
+ "_rfSummaryItemPlayerCardSection"
+ "_searchInAppType"
+ "_secondary_button"
+ "_shortcutsImage"
+ "_shouldAddToWatchList"
+ "_shouldOpenAppAfterInstallCompletes"
+ "_shouldPause"
+ "_storeButtonItem"
+ "_system"
+ "_thumbnail2"
+ "_versionIdentifier"
+ "_vertical_alignment"
+ "_weight"
+ "actionTypesToShow"
+ "actionTypesToShowAtIndex:"
+ "actionTypesToShowCount"
+ "actionTypesToShows"
+ "addActionTypesToShow:"
+ "addHash_details:"
+ "addTint"
+ "add_tint"
+ "applySmallCaps"
+ "buttonItemsAreBottom"
+ "clearActionTypesToShow"
+ "clearHash_details"
+ "com.apple.conversion"
+ "com.apple.health"
+ "com.apple.parsec.dictionary"
+ "com.apple.shortcuts"
+ "com.apple.systempreferences"
+ "com.apple.tips"
+ "distributorBundleIdentifier"
+ "fillStyle"
+ "font"
+ "fullHash"
+ "full_hash"
+ "gridStyle"
+ "hasAddTint"
+ "hasAdd_tint"
+ "hasApplySmallCaps"
+ "hasButtonItemsAreBottom"
+ "hasEe"
+ "hasFillStyle"
+ "hasGridStyle"
+ "hasHas_ee"
+ "hasHas_summary"
+ "hasIsInsetGrouped"
+ "hasItemIdentifier"
+ "hasSearchInAppType"
+ "hasShouldAddToWatchList"
+ "hasShouldOpenAppAfterInstallCompletes"
+ "hasShouldPause"
+ "hasSummary"
+ "hasSystem"
+ "hasVersionIdentifier"
+ "hasVertical_alignment"
+ "hasWeight"
+ "has_ee"
+ "has_summary"
+ "hashDetails"
+ "hashPrefix"
+ "hash_details"
+ "hash_detailsAtIndex:"
+ "hash_detailsCount"
+ "hash_prefix"
+ "i24@0:8Q16"
+ "iFunScore"
+ "indexOfResultInSectionWhenRanked"
+ "indexOfSectionWhenRanked"
+ "initWithDomain:scoreConfidence:score:"
+ "initWithVersion:serverScore:severScoreConfidence:localScore:localScoreConfidence:domainScores:"
+ "isInsetGrouped"
+ "itemIdentifier"
+ "lnPropertyIdentifier"
+ "mediaIdentifier"
+ "o\x0f\n\x11\x11/\x02\x15\x14\x17"
+ "playAudioButtonItem"
+ "playWatchListItemButtonItem"
+ "primaryButton"
+ "primary_button"
+ "requestProductPageCommand"
+ "rfBinaryButtonCardSection"
+ "rfButtonCardSection"
+ "rfPrimaryHeaderStackedImageCardSection"
+ "rfReferenceCenteredCardSection"
+ "rfReferenceItemButtonCardSection"
+ "rfReferenceItemLogoCardSection"
+ "rfSecondaryHeaderEmphasizedCardSection"
+ "rfSecondaryHeaderStandardCardSection"
+ "rfSimpleItemReverseRichCardSection"
+ "rfSimpleItemRichSearchResultCardSection"
+ "rfSimpleItemVisualElementCardSection"
+ "rfSummaryItemButtonCardSection"
+ "rfSummaryItemImageRightCardSection"
+ "rfSummaryItemPlayerCardSection"
+ "searchInAppType"
+ "secondaryButton"
+ "secondary_button"
+ "setActionTypesToShow:"
+ "setActionTypesToShows:"
+ "setAddTint:"
+ "setAdd_tint:"
+ "setApplySmallCaps:"
+ "setButtonItemsAreBottom:"
+ "setDistributorBundleIdentifier:"
+ "setFillStyle:"
+ "setFont:"
+ "setFull_hash:"
+ "setGridStyle:"
+ "setHas_ee:"
+ "setHas_summary:"
+ "setHash_details:"
+ "setHash_prefix:"
+ "setIFunScore:"
+ "setIndexOfResultInSectionWhenRanked:"
+ "setIndexOfSectionWhenRanked:"
+ "setIsInsetGrouped:"
+ "setItemIdentifier:"
+ "setLnPropertyIdentifier:"
+ "setMediaIdentifier:"
+ "setPlayAudioButtonItem:"
+ "setPlayWatchListItemButtonItem:"
+ "setPrimary_button:"
+ "setRequestProductPageCommand:"
+ "setRfBinaryButtonCardSection:"
+ "setRfButtonCardSection:"
+ "setRfPrimaryHeaderStackedImageCardSection:"
+ "setRfReferenceCenteredCardSection:"
+ "setRfReferenceItemButtonCardSection:"
+ "setRfReferenceItemLogoCardSection:"
+ "setRfSecondaryHeaderEmphasizedCardSection:"
+ "setRfSecondaryHeaderStandardCardSection:"
+ "setRfSimpleItemReverseRichCardSection:"
+ "setRfSimpleItemRichSearchResultCardSection:"
+ "setRfSimpleItemVisualElementCardSection:"
+ "setRfSummaryItemButtonCardSection:"
+ "setRfSummaryItemImageRightCardSection:"
+ "setRfSummaryItemPlayerCardSection:"
+ "setSearchInAppType:"
+ "setSecondary_button:"
+ "setShortcutsImage:"
+ "setShouldAddToWatchList:"
+ "setShouldOpenAppAfterInstallCompletes:"
+ "setShouldPause:"
+ "setStoreButtonItem:"
+ "setSystem:"
+ "setThumbnail2:"
+ "setVersionIdentifier:"
+ "setVertical_alignment:"
+ "setWeight:"
+ "shortcutsImage"
+ "shouldAddToWatchList"
+ "shouldOpenAppAfterInstallCompletes"
+ "shouldPause"
+ "storeButtonItem"
+ "system"
+ "v24@0:8@\"RFBinaryButtonCardSection\"16"
+ "v24@0:8@\"RFButtonCardSection\"16"
+ "v24@0:8@\"RFFont\"16"
+ "v24@0:8@\"RFPrimaryHeaderStackedImageCardSection\"16"
+ "v24@0:8@\"RFReferenceCenteredCardSection\"16"
+ "v24@0:8@\"RFReferenceItemButtonCardSection\"16"
+ "v24@0:8@\"RFReferenceItemLogoCardSection\"16"
+ "v24@0:8@\"RFSecondaryHeaderEmphasizedCardSection\"16"
+ "v24@0:8@\"RFSecondaryHeaderStandardCardSection\"16"
+ "v24@0:8@\"RFSimpleItemReverseRichCardSection\"16"
+ "v24@0:8@\"RFSimpleItemRichSearchResultCardSection\"16"
+ "v24@0:8@\"RFSimpleItemVisualElementCardSection\"16"
+ "v24@0:8@\"RFSummaryItemButtonCardSection\"16"
+ "v24@0:8@\"RFSummaryItemImageRightCardSection\"16"
+ "v24@0:8@\"RFSummaryItemPlayerCardSection\"16"
+ "v24@0:8@\"RFSystemFont\"16"
+ "v24@0:8@\"_SFPBHashBucketDetail_HashDetail\"16"
+ "v24@0:8@\"_SFPBPlayAudioButtonItem\"16"
+ "v24@0:8@\"_SFPBPlayWatchListItemButtonItem\"16"
+ "v24@0:8@\"_SFPBRFBinaryButtonCardSection\"16"
+ "v24@0:8@\"_SFPBRFButtonCardSection\"16"
+ "v24@0:8@\"_SFPBRFFont\"16"
+ "v24@0:8@\"_SFPBRFFont_RFSystemFont\"16"
+ "v24@0:8@\"_SFPBRFPrimaryHeaderStackedImageCardSection\"16"
+ "v24@0:8@\"_SFPBRFReferenceCenteredCardSection\"16"
+ "v24@0:8@\"_SFPBRFReferenceItemButtonCardSection\"16"
+ "v24@0:8@\"_SFPBRFReferenceItemLogoCardSection\"16"
+ "v24@0:8@\"_SFPBRFSecondaryHeaderEmphasizedCardSection\"16"
+ "v24@0:8@\"_SFPBRFSecondaryHeaderStandardCardSection\"16"
+ "v24@0:8@\"_SFPBRFSimpleItemReverseRichCardSection\"16"
+ "v24@0:8@\"_SFPBRFSimpleItemRichSearchResultCardSection\"16"
+ "v24@0:8@\"_SFPBRFSimpleItemVisualElementCardSection\"16"
+ "v24@0:8@\"_SFPBRFSummaryItemButtonCardSection\"16"
+ "v24@0:8@\"_SFPBRFSummaryItemImageRightCardSection\"16"
+ "v24@0:8@\"_SFPBRFSummaryItemPlayerCardSection\"16"
+ "v24@0:8@\"_SFPBRequestProductPageCommand\"16"
+ "v24@0:8@\"_SFPBShortcutsImage\"16"
+ "v24@0:8@\"_SFPBStoreButtonItem\"16"
+ "versionIdentifier"
+ "verticalAlignment"
+ "vertical_alignment"
+ "weight"
+ "{?=\"addTint\"b1}"
+ "{?=\"add_tint\"b1}"
+ "{?=\"buttonItemsAreBottom\"b1}"
+ "{?=\"buttonItemsAreTrailing\"b1}"
+ "{?=\"drawPlattersIfNecessary\"b1\"isInsetGrouped\"b1}"
+ "{?=\"has_summary\"b1\"has_ee\"b1}"
+ "{?=\"itemIdentifier\"b1\"versionIdentifier\"b1}"
+ "{?=\"name\"b1\"system\"b1}"
+ "{?=\"numberOfColumns\"b1\"gridStyle\"b1}"
+ "{?=\"playbackLocation\"b1\"shouldPause\"b1}"
+ "{?=\"punchThroughBackground\"b1\"backgroundColor\"b1\"primaryColor\"b1\"secondaryColor\"b1\"fillStyle\"b1}"
+ "{?=\"searchInAppType\"b1}"
+ "{?=\"shouldAddToWatchList\"b1}"
+ "{?=\"shouldOpenAppAfterInstallCompletes\"b1}"
+ "{?=\"text\"b1\"visual\"b1\"horizontal_alignment\"b1\"applySmallCaps\"b1}"
+ "{?=\"vertical_alignment\"b1}"
+ "{?=\"weight\"b1}"
- "\n"
- "\x0f\x0f\x0f\a"
- "\x0f\x0f\x0f\x0f\x0f\x0f\x01"
- "o\x0f\n\x11\x11/\x02\x15\x14\x15"
- "{?=\"drawPlattersIfNecessary\"b1}"
- "{?=\"numberOfColumns\"b1}"
- "{?=\"playbackLocation\"b1}"
- "{?=\"punchThroughBackground\"b1\"backgroundColor\"b1\"primaryColor\"b1\"secondaryColor\"b1}"
- "{?=\"text\"b1\"visual\"b1\"horizontal_alignment\"b1}"

```
