## SearchFoundation

> `/System/Library/PrivateFrameworks/SearchFoundation.framework/SearchFoundation`

```diff

-3300.117.1.0.0
-  __TEXT.__text: 0x267788
+3301.13.1.0.0
+  __TEXT.__text: 0x2704f8
   __TEXT.__auth_stubs: 0x5a0
-  __TEXT.__objc_methlist: 0x270c8
+  __TEXT.__objc_methlist: 0x27910
   __TEXT.__const: 0x68
   __TEXT.__gcc_except_tab: 0x38
-  __TEXT.__cstring: 0x4735
+  __TEXT.__cstring: 0x4f79
   __TEXT.__oslogstring: 0x17c
   __TEXT.__dlopen_cstrs: 0x52
-  __TEXT.__unwind_info: 0x6650
-  __TEXT.__objc_classname: 0x33e2
-  __TEXT.__objc_methname: 0x210dd
-  __TEXT.__objc_methtype: 0xac0a
-  __TEXT.__objc_stubs: 0x12a00
+  __TEXT.__unwind_info: 0x67b0
+  __TEXT.__objc_classname: 0x348d
+  __TEXT.__objc_methname: 0x21865
+  __TEXT.__objc_methtype: 0xadaa
+  __TEXT.__objc_stubs: 0x12e20
   __DATA_CONST.__got: 0x40
-  __DATA_CONST.__const: 0x6e8
-  __DATA_CONST.__objc_classlist: 0x11e8
+  __DATA_CONST.__const: 0x978
+  __DATA_CONST.__objc_classlist: 0x1228
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x10a0
+  __DATA_CONST.__objc_protolist: 0x10e0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x99800
-  __DATA_CONST.__objc_selrefs: 0x5880
-  __AUTH_CONST.__objc_const: 0xf658
-  __AUTH_CONST.__cfstring: 0x92c0
+  __DATA_CONST.__objc_const: 0x9c450
+  __DATA_CONST.__objc_selrefs: 0x59e0
+  __AUTH_CONST.__objc_const: 0xf970
+  __AUTH_CONST.__cfstring: 0x9ee0
   __AUTH_CONST.__const: 0xc0
   __AUTH_CONST.__auth_got: 0x2e0
-  __AUTH.__objc_data: 0x87a0
+  __AUTH.__objc_data: 0x8a20
   __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x11b8
-  __DATA.__objc_superrefs: 0x1728
-  __DATA.__objc_ivar: 0x320c
-  __DATA.__data: 0xc7f0
-  __DATA.__bss: 0x60
+  __DATA.__objc_classrefs: 0x11f0
+  __DATA.__objc_superrefs: 0x1768
+  __DATA.__objc_ivar: 0x32a0
+  __DATA.__data: 0xcab0
+  __DATA.__bss: 0xa0
   __DATA_DIRTY.__objc_data: 0x2b70
   __DATA_DIRTY.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 13028
-  Symbols:   39793
-  CStrings:  8995
+  Functions: 13202
+  Symbols:   40325
+  CStrings:  9198
 
Symbols:
+ +[RFAttribution supportsSecureCoding]
+ +[RFHighlightedSubstring supportsSecureCoding]
+ +[SFCommandReference supportsSecureCoding]
+ -[RFAttribution .cxx_destruct]
+ -[RFAttribution commandReference]
+ -[RFAttribution copyWithZone:]
+ -[RFAttribution dictionaryRepresentation]
+ -[RFAttribution encodeWithCoder:]
+ -[RFAttribution hash]
+ -[RFAttribution image]
+ -[RFAttribution index]
+ -[RFAttribution initWithCoder:]
+ -[RFAttribution isEqual:]
+ -[RFAttribution jsonData]
+ -[RFAttribution locale]
+ -[RFAttribution setCommandReference:]
+ -[RFAttribution setImage:]
+ -[RFAttribution setIndex:]
+ -[RFAttribution setLocale:]
+ -[RFAttribution setSubtitle:]
+ -[RFAttribution setTitle:]
+ -[RFAttribution subtitle]
+ -[RFAttribution title]
+ -[RFAttribution(ProtobufInitializer) initWithProtobuf:]
+ -[RFFormattedText attributions]
+ -[RFFormattedText highlighted_substrings]
+ -[RFFormattedText setAttributions:]
+ -[RFFormattedText setHighlighted_substrings:]
+ -[RFHighlightedSubstring .cxx_destruct]
+ -[RFHighlightedSubstring copyWithZone:]
+ -[RFHighlightedSubstring dictionaryRepresentation]
+ -[RFHighlightedSubstring encodeWithCoder:]
+ -[RFHighlightedSubstring hash]
+ -[RFHighlightedSubstring initWithCoder:]
+ -[RFHighlightedSubstring isEqual:]
+ -[RFHighlightedSubstring jsonData]
+ -[RFHighlightedSubstring setSubstring:]
+ -[RFHighlightedSubstring substring]
+ -[RFHighlightedSubstring(ProtobufInitializer) initWithProtobuf:]
+ -[SFCardSection forceEnable3DTouch]
+ -[SFCardSection referencedCommands]
+ -[SFCardSection setForceEnable3DTouch:]
+ -[SFCardSection setReferencedCommands:]
+ -[SFCommand commandReference]
+ -[SFCommand setCommandReference:]
+ -[SFCommandReference .cxx_destruct]
+ -[SFCommandReference copyWithZone:]
+ -[SFCommandReference dictionaryRepresentation]
+ -[SFCommandReference encodeWithCoder:]
+ -[SFCommandReference hash]
+ -[SFCommandReference initWithCoder:]
+ -[SFCommandReference isEqual:]
+ -[SFCommandReference jsonData]
+ -[SFCommandReference referenceIdentifier]
+ -[SFCommandReference setReferenceIdentifier:]
+ -[SFCommandReference(ProtobufInitializer) initWithProtobuf:]
+ -[SFDrillDownMetadata params]
+ -[SFDrillDownMetadata setParams:]
+ -[_SFPBCardSection addReferencedCommands:]
+ -[_SFPBCardSection clearReferencedCommands]
+ -[_SFPBCardSection forceEnable3DTouch]
+ -[_SFPBCardSection referencedCommandsAtIndex:]
+ -[_SFPBCardSection referencedCommandsCount]
+ -[_SFPBCardSection referencedCommands]
+ -[_SFPBCardSection setForceEnable3DTouch:]
+ -[_SFPBCardSection setReferencedCommands:]
+ -[_SFPBCommand commandReference]
+ -[_SFPBCommand setCommandReference:]
+ -[_SFPBCommandReference .cxx_destruct]
+ -[_SFPBCommandReference dictionaryRepresentation]
+ -[_SFPBCommandReference hash]
+ -[_SFPBCommandReference initWithDictionary:]
+ -[_SFPBCommandReference initWithJSON:]
+ -[_SFPBCommandReference isEqual:]
+ -[_SFPBCommandReference jsonData]
+ -[_SFPBCommandReference readFrom:]
+ -[_SFPBCommandReference referenceIdentifier]
+ -[_SFPBCommandReference setReferenceIdentifier:]
+ -[_SFPBCommandReference writeTo:]
+ -[_SFPBCommandReference(FacadeInitializer) initWithFacade:]
+ -[_SFPBDomainEngagementScore dictionaryRepresentation]
+ -[_SFPBDomainEngagementScore domain]
+ -[_SFPBDomainEngagementScore hash]
+ -[_SFPBDomainEngagementScore initWithDictionary:]
+ -[_SFPBDomainEngagementScore initWithJSON:]
+ -[_SFPBDomainEngagementScore isEqual:]
+ -[_SFPBDomainEngagementScore jsonData]
+ -[_SFPBDomainEngagementScore readFrom:]
+ -[_SFPBDomainEngagementScore scoreConfidence]
+ -[_SFPBDomainEngagementScore score]
+ -[_SFPBDomainEngagementScore setDomain:]
+ -[_SFPBDomainEngagementScore setScore:]
+ -[_SFPBDomainEngagementScore setScoreConfidence:]
+ -[_SFPBDomainEngagementScore writeTo:]
+ -[_SFPBDrillDownMetadata params]
+ -[_SFPBDrillDownMetadata setParams:]
+ -[_SFPBEngagementSignal .cxx_destruct]
+ -[_SFPBEngagementSignal addDomainEngagementScores:]
+ -[_SFPBEngagementSignal clearDomainEngagementScores]
+ -[_SFPBEngagementSignal dictionaryRepresentation]
+ -[_SFPBEngagementSignal domainEngagementScoresAtIndex:]
+ -[_SFPBEngagementSignal domainEngagementScoresCount]
+ -[_SFPBEngagementSignal domainEngagementScores]
+ -[_SFPBEngagementSignal hash]
+ -[_SFPBEngagementSignal initWithDictionary:]
+ -[_SFPBEngagementSignal initWithJSON:]
+ -[_SFPBEngagementSignal isEqual:]
+ -[_SFPBEngagementSignal jsonData]
+ -[_SFPBEngagementSignal localScoreConfidence]
+ -[_SFPBEngagementSignal localScore]
+ -[_SFPBEngagementSignal readFrom:]
+ -[_SFPBEngagementSignal serverScoreConfidence]
+ -[_SFPBEngagementSignal serverScore]
+ -[_SFPBEngagementSignal setDomainEngagementScores:]
+ -[_SFPBEngagementSignal setLocalScore:]
+ -[_SFPBEngagementSignal setLocalScoreConfidence:]
+ -[_SFPBEngagementSignal setServerScore:]
+ -[_SFPBEngagementSignal setServerScoreConfidence:]
+ -[_SFPBEngagementSignal setVersion:]
+ -[_SFPBEngagementSignal version]
+ -[_SFPBEngagementSignal writeTo:]
+ -[_SFPBRFAttribution .cxx_destruct]
+ -[_SFPBRFAttribution commandReference]
+ -[_SFPBRFAttribution dictionaryRepresentation]
+ -[_SFPBRFAttribution hash]
+ -[_SFPBRFAttribution image]
+ -[_SFPBRFAttribution index]
+ -[_SFPBRFAttribution initWithDictionary:]
+ -[_SFPBRFAttribution initWithJSON:]
+ -[_SFPBRFAttribution isEqual:]
+ -[_SFPBRFAttribution jsonData]
+ -[_SFPBRFAttribution locale]
+ -[_SFPBRFAttribution readFrom:]
+ -[_SFPBRFAttribution setCommandReference:]
+ -[_SFPBRFAttribution setImage:]
+ -[_SFPBRFAttribution setIndex:]
+ -[_SFPBRFAttribution setLocale:]
+ -[_SFPBRFAttribution setSubtitle:]
+ -[_SFPBRFAttribution setTitle:]
+ -[_SFPBRFAttribution subtitle]
+ -[_SFPBRFAttribution title]
+ -[_SFPBRFAttribution writeTo:]
+ -[_SFPBRFAttribution(FacadeInitializer) initWithFacade:]
+ -[_SFPBRFFormattedText addAttributions:]
+ -[_SFPBRFFormattedText addHighlighted_substrings:]
+ -[_SFPBRFFormattedText attributionsAtIndex:]
+ -[_SFPBRFFormattedText attributionsCount]
+ -[_SFPBRFFormattedText attributions]
+ -[_SFPBRFFormattedText clearAttributions]
+ -[_SFPBRFFormattedText clearHighlighted_substrings]
+ -[_SFPBRFFormattedText highlighted_substringsAtIndex:]
+ -[_SFPBRFFormattedText highlighted_substringsCount]
+ -[_SFPBRFFormattedText highlighted_substrings]
+ -[_SFPBRFFormattedText setAttributions:]
+ -[_SFPBRFFormattedText setHighlighted_substrings:]
+ -[_SFPBRFHighlightedSubstring .cxx_destruct]
+ -[_SFPBRFHighlightedSubstring dictionaryRepresentation]
+ -[_SFPBRFHighlightedSubstring hash]
+ -[_SFPBRFHighlightedSubstring initWithDictionary:]
+ -[_SFPBRFHighlightedSubstring initWithJSON:]
+ -[_SFPBRFHighlightedSubstring isEqual:]
+ -[_SFPBRFHighlightedSubstring jsonData]
+ -[_SFPBRFHighlightedSubstring readFrom:]
+ -[_SFPBRFHighlightedSubstring setSubstring:]
+ -[_SFPBRFHighlightedSubstring substring]
+ -[_SFPBRFHighlightedSubstring writeTo:]
+ -[_SFPBRFHighlightedSubstring(FacadeInitializer) initWithFacade:]
+ GCC_except_table10424
+ GCC_except_table11081
+ _OBJC_CLASS_$_RFAttribution
+ _OBJC_CLASS_$_RFHighlightedSubstring
+ _OBJC_CLASS_$_SFCommandReference
+ _OBJC_CLASS_$__SFPBCommandReference
+ _OBJC_CLASS_$__SFPBDomainEngagementScore
+ _OBJC_CLASS_$__SFPBEngagementSignal
+ _OBJC_CLASS_$__SFPBRFAttribution
+ _OBJC_CLASS_$__SFPBRFHighlightedSubstring
+ _OBJC_IVAR_$_RFAttribution._commandReference
+ _OBJC_IVAR_$_RFAttribution._image
+ _OBJC_IVAR_$_RFAttribution._index
+ _OBJC_IVAR_$_RFAttribution._locale
+ _OBJC_IVAR_$_RFAttribution._subtitle
+ _OBJC_IVAR_$_RFAttribution._title
+ _OBJC_IVAR_$_RFFormattedText._attributions
+ _OBJC_IVAR_$_RFFormattedText._highlighted_substrings
+ _OBJC_IVAR_$_RFHighlightedSubstring._substring
+ _OBJC_IVAR_$_SFCardSection._forceEnable3DTouch
+ _OBJC_IVAR_$_SFCardSection._referencedCommands
+ _OBJC_IVAR_$_SFCommand._commandReference
+ _OBJC_IVAR_$_SFCommandReference._referenceIdentifier
+ _OBJC_IVAR_$_SFDrillDownMetadata._params
+ _OBJC_IVAR_$__SFPBCardSection._forceEnable3DTouch
+ _OBJC_IVAR_$__SFPBCardSection._referencedCommands
+ _OBJC_IVAR_$__SFPBCommand._commandReference
+ _OBJC_IVAR_$__SFPBCommandReference._referenceIdentifier
+ _OBJC_IVAR_$__SFPBDomainEngagementScore._domain
+ _OBJC_IVAR_$__SFPBDomainEngagementScore._score
+ _OBJC_IVAR_$__SFPBDomainEngagementScore._scoreConfidence
+ _OBJC_IVAR_$__SFPBDrillDownMetadata._params
+ _OBJC_IVAR_$__SFPBEngagementSignal._domainEngagementScores
+ _OBJC_IVAR_$__SFPBEngagementSignal._localScore
+ _OBJC_IVAR_$__SFPBEngagementSignal._localScoreConfidence
+ _OBJC_IVAR_$__SFPBEngagementSignal._serverScore
+ _OBJC_IVAR_$__SFPBEngagementSignal._serverScoreConfidence
+ _OBJC_IVAR_$__SFPBEngagementSignal._version
+ _OBJC_IVAR_$__SFPBRFAttribution._commandReference
+ _OBJC_IVAR_$__SFPBRFAttribution._image
+ _OBJC_IVAR_$__SFPBRFAttribution._index
+ _OBJC_IVAR_$__SFPBRFAttribution._locale
+ _OBJC_IVAR_$__SFPBRFAttribution._subtitle
+ _OBJC_IVAR_$__SFPBRFAttribution._title
+ _OBJC_IVAR_$__SFPBRFFormattedText._attributions
+ _OBJC_IVAR_$__SFPBRFFormattedText._highlighted_substrings
+ _OBJC_IVAR_$__SFPBRFHighlightedSubstring._substring
+ _OBJC_METACLASS_$_RFAttribution
+ _OBJC_METACLASS_$_RFHighlightedSubstring
+ _OBJC_METACLASS_$_SFCommandReference
+ _OBJC_METACLASS_$__SFPBCommandReference
+ _OBJC_METACLASS_$__SFPBDomainEngagementScore
+ _OBJC_METACLASS_$__SFPBEngagementSignal
+ _OBJC_METACLASS_$__SFPBRFAttribution
+ _OBJC_METACLASS_$__SFPBRFHighlightedSubstring
+ _PARLogHandleForCategory.logHandles.0.29159
+ _PARLogHandleForCategory.logHandles.0.35431
+ _PARLogHandleForCategory.logHandles.1.29155
+ _PARLogHandleForCategory.logHandles.1.35424
+ _PARLogHandleForCategory.logHandles.2.29161
+ _PARLogHandleForCategory.logHandles.2.35434
+ _PARLogHandleForCategory.logHandles.3.29163
+ _PARLogHandleForCategory.logHandles.3.35435
+ _PARLogHandleForCategory.logHandles.4.29165
+ _PARLogHandleForCategory.logHandles.4.35436
+ _PARLogHandleForCategory.logHandles.5.29166
+ _PARLogHandleForCategory.logHandles.5.35438
+ _PARLogHandleForCategory.onceToken.29154
+ _PARLogHandleForCategory.onceToken.35422
+ __OBJC_$_CLASS_METHODS_RFAttribution(ProtobufInitializer)
+ __OBJC_$_CLASS_METHODS_RFHighlightedSubstring(ProtobufInitializer)
+ __OBJC_$_CLASS_METHODS_SFCommandReference(ProtobufInitializer)
+ __OBJC_$_CLASS_PROP_LIST_RFAttribution
+ __OBJC_$_CLASS_PROP_LIST_RFHighlightedSubstring
+ __OBJC_$_CLASS_PROP_LIST_SFCommandReference
+ __OBJC_$_CLASS_PROP_LIST__SFPBCommandReference
+ __OBJC_$_CLASS_PROP_LIST__SFPBDomainEngagementScore
+ __OBJC_$_CLASS_PROP_LIST__SFPBEngagementSignal
+ __OBJC_$_CLASS_PROP_LIST__SFPBRFAttribution
+ __OBJC_$_CLASS_PROP_LIST__SFPBRFHighlightedSubstring
+ __OBJC_$_INSTANCE_METHODS_RFAttribution(ProtobufInitializer)
+ __OBJC_$_INSTANCE_METHODS_RFHighlightedSubstring(ProtobufInitializer)
+ __OBJC_$_INSTANCE_METHODS_SFCommandReference(ProtobufInitializer)
+ __OBJC_$_INSTANCE_METHODS__SFPBCommandReference(FacadeInitializer)
+ __OBJC_$_INSTANCE_METHODS__SFPBDomainEngagementScore
+ __OBJC_$_INSTANCE_METHODS__SFPBEngagementSignal
+ __OBJC_$_INSTANCE_METHODS__SFPBRFAttribution(FacadeInitializer)
+ __OBJC_$_INSTANCE_METHODS__SFPBRFHighlightedSubstring(FacadeInitializer)
+ __OBJC_$_INSTANCE_VARIABLES_RFAttribution
+ __OBJC_$_INSTANCE_VARIABLES_RFHighlightedSubstring
+ __OBJC_$_INSTANCE_VARIABLES_SFCommandReference
+ __OBJC_$_INSTANCE_VARIABLES__SFPBCommandReference
+ __OBJC_$_INSTANCE_VARIABLES__SFPBDomainEngagementScore
+ __OBJC_$_INSTANCE_VARIABLES__SFPBEngagementSignal
+ __OBJC_$_INSTANCE_VARIABLES__SFPBRFAttribution
+ __OBJC_$_INSTANCE_VARIABLES__SFPBRFHighlightedSubstring
+ __OBJC_$_PROP_LIST_RFAttribution
+ __OBJC_$_PROP_LIST_RFAttribution.116
+ __OBJC_$_PROP_LIST_RFExpandableStandardCardSection.201
+ __OBJC_$_PROP_LIST_RFFactItemButtonCardSection.241
+ __OBJC_$_PROP_LIST_RFFactItemShortNumberCardSection.227
+ __OBJC_$_PROP_LIST_RFFactItemStandardCardSection.222
+ __OBJC_$_PROP_LIST_RFFormattedText.144
+ __OBJC_$_PROP_LIST_RFHighlightedSubstring
+ __OBJC_$_PROP_LIST_RFHighlightedSubstring.75
+ __OBJC_$_PROP_LIST_RFLongItemStandardCardSection.207
+ __OBJC_$_PROP_LIST_RFPrimaryHeaderRichCardSection.216
+ __OBJC_$_PROP_LIST_RFPrimaryHeaderStandardCardSection.202
+ __OBJC_$_PROP_LIST_RFReferenceFootnoteCardSection.207
+ __OBJC_$_PROP_LIST_RFReferenceRichCardSection.206
+ __OBJC_$_PROP_LIST_RFReferenceStandardCardSection.192
+ __OBJC_$_PROP_LIST_RFSimpleItemRichCardSection.237
+ __OBJC_$_PROP_LIST_RFSimpleItemStandardCardSection.218
+ __OBJC_$_PROP_LIST_RFSummaryItemAlignedTextCardSection.227
+ __OBJC_$_PROP_LIST_RFSummaryItemShortNumberCardSection.232
+ __OBJC_$_PROP_LIST_RFSummaryItemStandardCardSection.226
+ __OBJC_$_PROP_LIST_RFSummaryItemTextCardSection.213
+ __OBJC_$_PROP_LIST_SFActivityIndicatorCardSection.191
+ __OBJC_$_PROP_LIST_SFAddToPhotosLibraryCommand.104
+ __OBJC_$_PROP_LIST_SFAppIconCardSection.196
+ __OBJC_$_PROP_LIST_SFAppLinkCardSection.199
+ __OBJC_$_PROP_LIST_SFArchiveViewCardSection.194
+ __OBJC_$_PROP_LIST_SFAttributionFooterCardSection.214
+ __OBJC_$_PROP_LIST_SFAudioPlaybackCardSection.234
+ __OBJC_$_PROP_LIST_SFBeginMapsRoutingCommand.137
+ __OBJC_$_PROP_LIST_SFButtonCardSection.204
+ __OBJC_$_PROP_LIST_SFButtonListCardSection.202
+ __OBJC_$_PROP_LIST_SFCallCommand.101
+ __OBJC_$_PROP_LIST_SFClearProactiveCategoryCommand.122
+ __OBJC_$_PROP_LIST_SFCollectionCardSection.224
+ __OBJC_$_PROP_LIST_SFColorBarCardSection.208
+ __OBJC_$_PROP_LIST_SFCombinedCardSection.192
+ __OBJC_$_PROP_LIST_SFCommand.102
+ __OBJC_$_PROP_LIST_SFCommandReference
+ __OBJC_$_PROP_LIST_SFCommandReference.75
+ __OBJC_$_PROP_LIST_SFCommandRowCardSection.219
+ __OBJC_$_PROP_LIST_SFCompactRowCardSection.218
+ __OBJC_$_PROP_LIST_SFCopyCommand.104
+ __OBJC_$_PROP_LIST_SFCreateCalendarEventCommand.104
+ __OBJC_$_PROP_LIST_SFCreateContactCommand.115
+ __OBJC_$_PROP_LIST_SFCreateReminderCommand.104
+ __OBJC_$_PROP_LIST_SFDescriptionCardSection.289
+ __OBJC_$_PROP_LIST_SFDetailedRowCardSection.319
+ __OBJC_$_PROP_LIST_SFDrillDownMetadata.147
+ __OBJC_$_PROP_LIST_SFEmailCommand.101
+ __OBJC_$_PROP_LIST_SFExpandInlineCommand.103
+ __OBJC_$_PROP_LIST_SFFindMyCardSection.192
+ __OBJC_$_PROP_LIST_SFFlightCardSection.206
+ __OBJC_$_PROP_LIST_SFGridCardSection.192
+ __OBJC_$_PROP_LIST_SFHeroCardSection.224
+ __OBJC_$_PROP_LIST_SFHeroTitleCardSection.217
+ __OBJC_$_PROP_LIST_SFHorizontalButtonCardSection.192
+ __OBJC_$_PROP_LIST_SFHorizontalScrollCardSection.203
+ __OBJC_$_PROP_LIST_SFImagesCardSection.201
+ __OBJC_$_PROP_LIST_SFIndexedUserActivityCommand.106
+ __OBJC_$_PROP_LIST_SFInfoCardSection.203
+ __OBJC_$_PROP_LIST_SFInvokeSiriCommand.101
+ __OBJC_$_PROP_LIST_SFKeyValueDataCardSection.201
+ __OBJC_$_PROP_LIST_SFLargeTitleDetailedRowCardSection.210
+ __OBJC_$_PROP_LIST_SFLaunchAppCommand.101
+ __OBJC_$_PROP_LIST_SFLeadingTrailingCardSection.209
+ __OBJC_$_PROP_LIST_SFLinkPresentationCardSection.209
+ __OBJC_$_PROP_LIST_SFListenToCardSection.204
+ __OBJC_$_PROP_LIST_SFManageReservationCommand.103
+ __OBJC_$_PROP_LIST_SFMapCardSection.248
+ __OBJC_$_PROP_LIST_SFMapPlaceCardSection.208
+ __OBJC_$_PROP_LIST_SFMapsDetailedRowCardSection.205
+ __OBJC_$_PROP_LIST_SFMediaInfoCardSection.260
+ __OBJC_$_PROP_LIST_SFMediaPlayerCardSection.202
+ __OBJC_$_PROP_LIST_SFMediaRemoteControlCardSection.205
+ __OBJC_$_PROP_LIST_SFMessageCardSection.224
+ __OBJC_$_PROP_LIST_SFMetaInfoCardSection.218
+ __OBJC_$_PROP_LIST_SFMiniCardSection.209
+ __OBJC_$_PROP_LIST_SFNewsCardSection.228
+ __OBJC_$_PROP_LIST_SFNowPlayingCardSection.199
+ __OBJC_$_PROP_LIST_SFOpenAppClipCommand.101
+ __OBJC_$_PROP_LIST_SFOpenCalculationCommand.106
+ __OBJC_$_PROP_LIST_SFOpenCoreSpotlightItemCommand.111
+ __OBJC_$_PROP_LIST_SFOpenFileProviderItemCommand.117
+ __OBJC_$_PROP_LIST_SFOpenMediaCommand.110
+ __OBJC_$_PROP_LIST_SFOpenPunchoutCommand.104
+ __OBJC_$_PROP_LIST_SFOpenWebClipCommand.101
+ __OBJC_$_PROP_LIST_SFPerformContactActionCommand.119
+ __OBJC_$_PROP_LIST_SFPerformContactQueryCommand.101
+ __OBJC_$_PROP_LIST_SFPerformEntityQueryCommand.155
+ __OBJC_$_PROP_LIST_SFPerformIntentCommand.123
+ __OBJC_$_PROP_LIST_SFPerformPersonEntityQueryCommand.104
+ __OBJC_$_PROP_LIST_SFPersonHeaderCardSection.192
+ __OBJC_$_PROP_LIST_SFPlayMediaCommand.116
+ __OBJC_$_PROP_LIST_SFPlayVideoCommand.104
+ __OBJC_$_PROP_LIST_SFProductCardSection.194
+ __OBJC_$_PROP_LIST_SFRejectPeopleInPhotoCommand.113
+ __OBJC_$_PROP_LIST_SFRequestAppClipInstallCommand.110
+ __OBJC_$_PROP_LIST_SFRequestUserReportCommand.104
+ __OBJC_$_PROP_LIST_SFResponseWrapperCardSection.215
+ __OBJC_$_PROP_LIST_SFRichTitleCardSection.358
+ __OBJC_$_PROP_LIST_SFRowCardSection.275
+ __OBJC_$_PROP_LIST_SFRunVoiceShortcutCommand.106
+ __OBJC_$_PROP_LIST_SFScoreboardCardSection.218
+ __OBJC_$_PROP_LIST_SFSearchInAppCommand.106
+ __OBJC_$_PROP_LIST_SFSearchWebCommand.101
+ __OBJC_$_PROP_LIST_SFSectionHeaderCardSection.195
+ __OBJC_$_PROP_LIST_SFSelectableGridCardSection.201
+ __OBJC_$_PROP_LIST_SFShareCommand.104
+ __OBJC_$_PROP_LIST_SFShowAppStoreSheetCommand.106
+ __OBJC_$_PROP_LIST_SFShowContactCardCommand.112
+ __OBJC_$_PROP_LIST_SFShowPhotosOneUpViewCommand.136
+ __OBJC_$_PROP_LIST_SFShowPurchaseRequestSheetCommand.101
+ __OBJC_$_PROP_LIST_SFShowSFCardCommand.104
+ __OBJC_$_PROP_LIST_SFShowScreenTimeRequestSheetCommand.101
+ __OBJC_$_PROP_LIST_SFShowWrapperResponseViewCommand.104
+ __OBJC_$_PROP_LIST_SFSocialMediaPostCardSection.252
+ __OBJC_$_PROP_LIST_SFSplitCardSection.224
+ __OBJC_$_PROP_LIST_SFStockChartCardSection.203
+ __OBJC_$_PROP_LIST_SFStrokeAnimationCardSection.207
+ __OBJC_$_PROP_LIST_SFSubscribeForUpdatesCommand.113
+ __OBJC_$_PROP_LIST_SFSuggestionCardSection.244
+ __OBJC_$_PROP_LIST_SFTableHeaderRowCardSection.211
+ __OBJC_$_PROP_LIST_SFTableRowCardSection.244
+ __OBJC_$_PROP_LIST_SFTextColumnsCardSection.208
+ __OBJC_$_PROP_LIST_SFTitleCardSection.205
+ __OBJC_$_PROP_LIST_SFToggleAudioCommand.123
+ __OBJC_$_PROP_LIST_SFToggleWatchListStatusCommand.104
+ __OBJC_$_PROP_LIST_SFTrackListCardSection.199
+ __OBJC_$_PROP_LIST_SFUpdateSearchQueryCommand.113
+ __OBJC_$_PROP_LIST_SFVerticalLayoutCardSection.229
+ __OBJC_$_PROP_LIST_SFViewEmailCommand.103
+ __OBJC_$_PROP_LIST_SFWatchListCardSection.195
+ __OBJC_$_PROP_LIST_SFWatchNowCardSection.200
+ __OBJC_$_PROP_LIST_SFWebCardSection.191
+ __OBJC_$_PROP_LIST_SFWorldMapCardSection.200
+ __OBJC_$_PROP_LIST__SFPBCardSection.1541
+ __OBJC_$_PROP_LIST__SFPBCardSectionValue.2562
+ __OBJC_$_PROP_LIST__SFPBClearProactiveCategoryCommand.2593
+ __OBJC_$_PROP_LIST__SFPBClockImage.2623
+ __OBJC_$_PROP_LIST__SFPBCloudChannelsRequestItem.2654
+ __OBJC_$_PROP_LIST__SFPBCollectionCardSection.2691
+ __OBJC_$_PROP_LIST__SFPBCollectionStyle.2749
+ __OBJC_$_PROP_LIST__SFPBCollectionStyleGrid.2763
+ __OBJC_$_PROP_LIST__SFPBCollectionStyleHorizontallyScrolling.2777
+ __OBJC_$_PROP_LIST__SFPBCollectionStyleRow.2791
+ __OBJC_$_PROP_LIST__SFPBColor.2911
+ __OBJC_$_PROP_LIST__SFPBColorBarCardSection.2934
+ __OBJC_$_PROP_LIST__SFPBCombinedCardSection.2941
+ __OBJC_$_PROP_LIST__SFPBCommand.3601
+ __OBJC_$_PROP_LIST__SFPBCommandButtonItem.3616
+ __OBJC_$_PROP_LIST__SFPBCommandReference
+ __OBJC_$_PROP_LIST__SFPBCommandReference.3631
+ __OBJC_$_PROP_LIST__SFPBCommandRowCardSection.3654
+ __OBJC_$_PROP_LIST__SFPBCommandValue.3674
+ __OBJC_$_PROP_LIST__SFPBCompactRowCardSection.3689
+ __OBJC_$_PROP_LIST__SFPBContactButtonItem.3709
+ __OBJC_$_PROP_LIST__SFPBContactCopyItem.3724
+ __OBJC_$_PROP_LIST__SFPBContactImage.3759
+ __OBJC_$_PROP_LIST__SFPBCopyCommand.3779
+ __OBJC_$_PROP_LIST__SFPBCopyItem.3838
+ __OBJC_$_PROP_LIST__SFPBCoreSpotlightButtonItem.3865
+ __OBJC_$_PROP_LIST__SFPBCoreSpotlightCopyItem.3896
+ __OBJC_$_PROP_LIST__SFPBCoreSpotlightRankingSignals.3978
+ __OBJC_$_PROP_LIST__SFPBCoreSpotlightShareItem.3993
+ __OBJC_$_PROP_LIST__SFPBCreateCalendarEventCommand.4013
+ __OBJC_$_PROP_LIST__SFPBCreateContactCommand.4028
+ __OBJC_$_PROP_LIST__SFPBCreateReminderCommand.4048
+ __OBJC_$_PROP_LIST__SFPBDate.4066
+ __OBJC_$_PROP_LIST__SFPBDescriptionCardSection.4179
+ __OBJC_$_PROP_LIST__SFPBDetailedRowCardSection.4353
+ __OBJC_$_PROP_LIST__SFPBDomainEngagementScore
+ __OBJC_$_PROP_LIST__SFPBDomainEngagementScore.4383
+ __OBJC_$_PROP_LIST__SFPBDomainSubscriptionRequestItem.4403
+ __OBJC_$_PROP_LIST__SFPBDrillDownMetadata.4510
+ __OBJC_$_PROP_LIST__SFPBDynamicURLImageResource.4564
+ __OBJC_$_PROP_LIST__SFPBEmailCommand.4571
+ __OBJC_$_PROP_LIST__SFPBEngagementSignal
+ __OBJC_$_PROP_LIST__SFPBEngagementSignal.4633
+ __OBJC_$_PROP_LIST__SFPBEntitySearchMetadata.4657
+ __OBJC_$_PROP_LIST__SFPBExpandInlineCommand.4671
+ __OBJC_$_PROP_LIST__SFPBFindMyCardSection.4678
+ __OBJC_$_PROP_LIST__SFPBFlight.4764
+ __OBJC_$_PROP_LIST__SFPBFlightCardSection.4790
+ __OBJC_$_PROP_LIST__SFPBFlightDetails.4804
+ __OBJC_$_PROP_LIST__SFPBFlightLeg.4944
+ __OBJC_$_PROP_LIST__SFPBFormattedText.4992
+ __OBJC_$_PROP_LIST__SFPBGradientColor.5020
+ __OBJC_$_PROP_LIST__SFPBGraphicalFloat.5034
+ __OBJC_$_PROP_LIST__SFPBGridCardSection.5041
+ __OBJC_$_PROP_LIST__SFPBHeroCardSection.5048
+ __OBJC_$_PROP_LIST__SFPBHeroTitleCardSection.5063
+ __OBJC_$_PROP_LIST__SFPBHorizontalButtonCardSection.5082
+ __OBJC_$_PROP_LIST__SFPBHorizontalScrollCardSection.5089
+ __OBJC_$_PROP_LIST__SFPBImage.5341
+ __OBJC_$_PROP_LIST__SFPBImageCopyItem.5348
+ __OBJC_$_PROP_LIST__SFPBImageDerivedColor.5355
+ __OBJC_$_PROP_LIST__SFPBImageOption.5383
+ __OBJC_$_PROP_LIST__SFPBImagesCardSection.5411
+ __OBJC_$_PROP_LIST__SFPBIndexState.5457
+ __OBJC_$_PROP_LIST__SFPBIndexedUserActivityCommand.5472
+ __OBJC_$_PROP_LIST__SFPBInfoCardSection.5502
+ __OBJC_$_PROP_LIST__SFPBInfoTuple.5546
+ __OBJC_$_PROP_LIST__SFPBInvokeSiriCommand.5561
+ __OBJC_$_PROP_LIST__SFPBKeyValueDataCardSection.5592
+ __OBJC_$_PROP_LIST__SFPBKeyValueTuple.5600
+ __OBJC_$_PROP_LIST__SFPBLargeTitleDetailedRowCardSection.5630
+ __OBJC_$_PROP_LIST__SFPBLatLng.5652
+ __OBJC_$_PROP_LIST__SFPBLaunchAppCommand.5659
+ __OBJC_$_PROP_LIST__SFPBLeadingTrailingCardSection.5698
+ __OBJC_$_PROP_LIST__SFPBLinkPresentationCardSection.5735
+ __OBJC_$_PROP_LIST__SFPBListenToCardSection.5766
+ __OBJC_$_PROP_LIST__SFPBLocalImage.5780
+ __OBJC_$_PROP_LIST__SFPBLocationTypeInfo.5795
+ __OBJC_$_PROP_LIST__SFPBMailRankingSignals.5897
+ __OBJC_$_PROP_LIST__SFPBMailResultDetails.5927
+ __OBJC_$_PROP_LIST__SFPBManageReservationCommand.5933
+ __OBJC_$_PROP_LIST__SFPBMapCardSection.6009
+ __OBJC_$_PROP_LIST__SFPBMapPlaceCardSection.6024
+ __OBJC_$_PROP_LIST__SFPBMapRegion.6070
+ __OBJC_$_PROP_LIST__SFPBMapsDetailedRowCardSection.6085
+ __OBJC_$_PROP_LIST__SFPBMediaArtworkImage.6100
+ __OBJC_$_PROP_LIST__SFPBMediaDetail.6115
+ __OBJC_$_PROP_LIST__SFPBMediaInfoCardSection.6229
+ __OBJC_$_PROP_LIST__SFPBMediaItem.6309
+ __OBJC_$_PROP_LIST__SFPBMediaMetadata.6381
+ __OBJC_$_PROP_LIST__SFPBMediaOffer.6420
+ __OBJC_$_PROP_LIST__SFPBMediaPlayerCardSection.6440
+ __OBJC_$_PROP_LIST__SFPBMediaRemoteControlCardSection.6471
+ __OBJC_$_PROP_LIST__SFPBMessageAttachment.6487
+ __OBJC_$_PROP_LIST__SFPBMessageCardSection.6539
+ __OBJC_$_PROP_LIST__SFPBMetaInfoCardSection.6578
+ __OBJC_$_PROP_LIST__SFPBMiniCardSection.6585
+ __OBJC_$_PROP_LIST__SFPBMonogramImage.6608
+ __OBJC_$_PROP_LIST__SFPBMoreResults.6615
+ __OBJC_$_PROP_LIST__SFPBNamedProtobufMessage.6638
+ __OBJC_$_PROP_LIST__SFPBNewsCardSection.6669
+ __OBJC_$_PROP_LIST__SFPBNowPlayingCardSection.6688
+ __OBJC_$_PROP_LIST__SFPBOpenAppClipCommand.6703
+ __OBJC_$_PROP_LIST__SFPBOpenCalculationCommand.6726
+ __OBJC_$_PROP_LIST__SFPBOpenCoreSpotlightItemCommand.6741
+ __OBJC_$_PROP_LIST__SFPBOpenFileProviderItemCommand.6764
+ __OBJC_$_PROP_LIST__SFPBOpenMediaCommand.6779
+ __OBJC_$_PROP_LIST__SFPBOpenPunchoutCommand.6786
+ __OBJC_$_PROP_LIST__SFPBOpenWebClipCommand.6793
+ __OBJC_$_PROP_LIST__SFPBPatternModel.6832
+ __OBJC_$_PROP_LIST__SFPBPerformContactActionCommand.6862
+ __OBJC_$_PROP_LIST__SFPBPerformContactQueryCommand.6869
+ __OBJC_$_PROP_LIST__SFPBPerformEntityQueryCommand.6908
+ __OBJC_$_PROP_LIST__SFPBPerformIntentCommand.6923
+ __OBJC_$_PROP_LIST__SFPBPerformPersonEntityQueryCommand.6930
+ __OBJC_$_PROP_LIST__SFPBPerson.6985
+ __OBJC_$_PROP_LIST__SFPBPersonHeaderCardSection.6992
+ __OBJC_$_PROP_LIST__SFPBPhotosLibraryImage.7028
+ __OBJC_$_PROP_LIST__SFPBPin.7043
+ __OBJC_$_PROP_LIST__SFPBPlayMediaCommand.7058
+ __OBJC_$_PROP_LIST__SFPBPlayVideoCommand.7065
+ __OBJC_$_PROP_LIST__SFPBPointSize.7088
+ __OBJC_$_PROP_LIST__SFPBProduct.7119
+ __OBJC_$_PROP_LIST__SFPBProductAvailability.7141
+ __OBJC_$_PROP_LIST__SFPBProductCardSection.7156
+ __OBJC_$_PROP_LIST__SFPBProductInventory.7212
+ __OBJC_$_PROP_LIST__SFPBProductInventoryResult.7235
+ __OBJC_$_PROP_LIST__SFPBPunchout.7292
+ __OBJC_$_PROP_LIST__SFPBQueryUnderstandingParse.7426
+ __OBJC_$_PROP_LIST__SFPBQuickLookThumbnailImage.7441
+ __OBJC_$_PROP_LIST__SFPBRFAppIconImage.7461
+ __OBJC_$_PROP_LIST__SFPBRFAspectRatio.7469
+ __OBJC_$_PROP_LIST__SFPBRFAttribution
+ __OBJC_$_PROP_LIST__SFPBRFAttribution.7505
+ __OBJC_$_PROP_LIST__SFPBRFAvatarImage.7524
+ __OBJC_$_PROP_LIST__SFPBRFBadgedImage.7538
+ __OBJC_$_PROP_LIST__SFPBRFColor.7572
+ __OBJC_$_PROP_LIST__SFPBRFDefaultBrowserAppIconImage.7578
+ __OBJC_$_PROP_LIST__SFPBRFExpandableStandardCardSection.7613
+ __OBJC_$_PROP_LIST__SFPBRFExpandingComponentContent.7636
+ __OBJC_$_PROP_LIST__SFPBRFFactItemButtonCardSection.7714
+ __OBJC_$_PROP_LIST__SFPBRFFactItemShortNumberCardSection.7759
+ __OBJC_$_PROP_LIST__SFPBRFFactItemStandardCardSection.7775
+ __OBJC_$_PROP_LIST__SFPBRFFormattedText.7879
+ __OBJC_$_PROP_LIST__SFPBRFHighlightedSubstring
+ __OBJC_$_PROP_LIST__SFPBRFHighlightedSubstring.7894
+ __OBJC_$_PROP_LIST__SFPBRFImageElement.7914
+ __OBJC_$_PROP_LIST__SFPBRFImageSource.8005
+ __OBJC_$_PROP_LIST__SFPBRFLongItemStandardCardSection.8028
+ __OBJC_$_PROP_LIST__SFPBRFMonogramImage.8043
+ __OBJC_$_PROP_LIST__SFPBRFOptionalBool.8050
+ __OBJC_$_PROP_LIST__SFPBRFOptionalFloat.8057
+ __OBJC_$_PROP_LIST__SFPBRFPrimaryHeaderRichCardSection.8064
+ __OBJC_$_PROP_LIST__SFPBRFPrimaryHeaderStandardCardSection.8071
+ __OBJC_$_PROP_LIST__SFPBRFRGBValue.8101
+ __OBJC_$_PROP_LIST__SFPBRFReferenceFootnoteCardSection.8108
+ __OBJC_$_PROP_LIST__SFPBRFReferenceRichCardSection.8115
+ __OBJC_$_PROP_LIST__SFPBRFReferenceStandardCardSection.8122
+ __OBJC_$_PROP_LIST__SFPBRFSimpleItemRichCardSection.8153
+ __OBJC_$_PROP_LIST__SFPBRFSimpleItemStandardCardSection.8160
+ __OBJC_$_PROP_LIST__SFPBRFSummaryItemAlignedTextCardSection.8176
+ __OBJC_$_PROP_LIST__SFPBRFSummaryItemShortNumberCardSection.8183
+ __OBJC_$_PROP_LIST__SFPBRFSummaryItemStandardCardSection.8198
+ __OBJC_$_PROP_LIST__SFPBRFSummaryItemTextCardSection.8205
+ __OBJC_$_PROP_LIST__SFPBRFSymbolImage.8244
+ __OBJC_$_PROP_LIST__SFPBRFTextElement.8275
+ __OBJC_$_PROP_LIST__SFPBRFTextEncapsulation.8289
+ __OBJC_$_PROP_LIST__SFPBRFTextProperty.8319
+ __OBJC_$_PROP_LIST__SFPBRFUrlImage.8375
+ __OBJC_$_PROP_LIST__SFPBRFVisualElement.8394
+ __OBJC_$_PROP_LIST__SFPBRFVisualProperty.8416
+ __OBJC_$_PROP_LIST__SFPBReferentialCommand.8423
+ __OBJC_$_PROP_LIST__SFPBRejectPeopleInPhotoCommand.8443
+ __OBJC_$_PROP_LIST__SFPBReminder.8458
+ __OBJC_$_PROP_LIST__SFPBRequestAppClipInstallCommand.8465
+ __OBJC_$_PROP_LIST__SFPBRequestUserReportCommand.8472
+ __OBJC_$_PROP_LIST__SFPBResponseWrapperCardSection.8526
+ __OBJC_$_PROP_LIST__SFPBResultEntity.8554
+ __OBJC_$_PROP_LIST__SFPBRichText.8594
+ __OBJC_$_PROP_LIST__SFPBRichTitleCardSection.8742
+ __OBJC_$_PROP_LIST__SFPBRowCardSection.8837
+ __OBJC_$_PROP_LIST__SFPBRunVoiceShortcutCommand.8852
+ __OBJC_$_PROP_LIST__SFPBScene.8874
+ __OBJC_$_PROP_LIST__SFPBScoreboardCardSection.8918
+ __OBJC_$_PROP_LIST__SFPBSearchInAppCommand.8925
+ __OBJC_$_PROP_LIST__SFPBSearchSuggestion.9007
+ __OBJC_$_PROP_LIST__SFPBSearchWebCommand.9014
+ __OBJC_$_PROP_LIST__SFPBSectionHeaderCardSection.9022
+ __OBJC_$_PROP_LIST__SFPBSelectableGridCardSection.9052
+ __OBJC_$_PROP_LIST__SFPBShareCommand.9072
+ __OBJC_$_PROP_LIST__SFPBShareItem.9105
+ __OBJC_$_PROP_LIST__SFPBShowAppStoreSheetCommand.9120
+ __OBJC_$_PROP_LIST__SFPBShowContactCardCommand.9135
+ __OBJC_$_PROP_LIST__SFPBShowPhotosOneUpViewCommand.9186
+ __OBJC_$_PROP_LIST__SFPBShowPurchaseRequestSheetCommand.9201
+ __OBJC_$_PROP_LIST__SFPBShowSFCardCommand.9216
+ __OBJC_$_PROP_LIST__SFPBShowScreenTimeRequestSheetCommand.9223
+ __OBJC_$_PROP_LIST__SFPBShowWrapperResponseViewCommand.9230
+ __OBJC_$_PROP_LIST__SFPBSocialMediaPostCardSection.9294
+ __OBJC_$_PROP_LIST__SFPBSplitCardSection.9361
+ __OBJC_$_PROP_LIST__SFPBSportsDetail.9376
+ __OBJC_$_PROP_LIST__SFPBSportsSubscriptionRequestItem.9407
+ __OBJC_$_PROP_LIST__SFPBSportsTeam.9440
+ __OBJC_$_PROP_LIST__SFPBStockChartCardSection.9463
+ __OBJC_$_PROP_LIST__SFPBStringDictionary.9482
+ __OBJC_$_PROP_LIST__SFPBStrokeAnimationCardSection.9533
+ __OBJC_$_PROP_LIST__SFPBStructuredLocation.9556
+ __OBJC_$_PROP_LIST__SFPBSubscribeForUpdatesCommand.9589
+ __OBJC_$_PROP_LIST__SFPBSuggestionCardSection.9628
+ __OBJC_$_PROP_LIST__SFPBSymbolImage.9662
+ __OBJC_$_PROP_LIST__SFPBTableAlignmentSchema.9686
+ __OBJC_$_PROP_LIST__SFPBTableColumnAlignment.9716
+ __OBJC_$_PROP_LIST__SFPBTableHeaderRowCardSection.9784
+ __OBJC_$_PROP_LIST__SFPBTableRowCardSection.9804
+ __OBJC_$_PROP_LIST__SFPBText.9821
+ __OBJC_$_PROP_LIST__SFPBTextColumn.9843
+ __OBJC_$_PROP_LIST__SFPBTextColumnSection.9878
+ __OBJC_$_PROP_LIST__SFPBTextColumnsCardSection.9901
+ __OBJC_$_PROP_LIST__SFPBTextCopyItem.9916
+ __OBJC_$_PROP_LIST__SFPBTimeZone.9923
+ __OBJC_$_PROP_LIST__SFPBTitleCardSection.9930
+ __OBJC_$_PROP_LIST__SFPBTitleSubtitleTuple.9937
+ __OBJC_$_PROP_LIST__SFPBToggleAudioCommand.9960
+ __OBJC_$_PROP_LIST__SFPBToggleWatchListStatusCommand.9980
+ __OBJC_$_PROP_LIST__SFPBTopic.10023
+ __OBJC_$_PROP_LIST__SFPBTrack.10055
+ __OBJC_$_PROP_LIST__SFPBTrackListCardSection.10077
+ __OBJC_$_PROP_LIST__SFPBURL.10084
+ __OBJC_$_PROP_LIST__SFPBURLImage.10099
+ __OBJC_$_PROP_LIST__SFPBURLShareItem.10106
+ __OBJC_$_PROP_LIST__SFPBUpdateSearchQueryCommand.10121
+ __OBJC_$_PROP_LIST__SFPBUserActivityData.10152
+ __OBJC_$_PROP_LIST__SFPBUserActivityInfo.10175
+ __OBJC_$_PROP_LIST__SFPBUserReportRequest.10250
+ __OBJC_$_PROP_LIST__SFPBVerticalLayoutCardSection.10281
+ __OBJC_$_PROP_LIST__SFPBViewEmailCommand.10287
+ __OBJC_$_PROP_LIST__SFPBWatchListButtonItem.10294
+ __OBJC_$_PROP_LIST__SFPBWatchListCardSection.10301
+ __OBJC_$_PROP_LIST__SFPBWatchListItem.10380
+ __OBJC_$_PROP_LIST__SFPBWatchNowCardSection.10394
+ __OBJC_$_PROP_LIST__SFPBWeatherColor.10409
+ __OBJC_$_PROP_LIST__SFPBWeatherDetails.10416
+ __OBJC_$_PROP_LIST__SFPBWebCardSection.10431
+ __OBJC_$_PROP_LIST__SFPBWorldMapCardSection.10454
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_RFAttribution
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_RFHighlightedSubstring
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SFCommandReference
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__SFPBCommandReference
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__SFPBDomainEngagementScore
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__SFPBEngagementSignal
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__SFPBRFAttribution
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__SFPBRFHighlightedSubstring
+ __OBJC_$_PROTOCOL_METHOD_TYPES_RFAttribution
+ __OBJC_$_PROTOCOL_METHOD_TYPES_RFHighlightedSubstring
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SFCommandReference
+ __OBJC_$_PROTOCOL_METHOD_TYPES__SFPBCommandReference
+ __OBJC_$_PROTOCOL_METHOD_TYPES__SFPBDomainEngagementScore
+ __OBJC_$_PROTOCOL_METHOD_TYPES__SFPBEngagementSignal
+ __OBJC_$_PROTOCOL_METHOD_TYPES__SFPBRFAttribution
+ __OBJC_$_PROTOCOL_METHOD_TYPES__SFPBRFHighlightedSubstring
+ __OBJC_$_PROTOCOL_REFS_RFAttribution
+ __OBJC_$_PROTOCOL_REFS_RFHighlightedSubstring
+ __OBJC_$_PROTOCOL_REFS_SFCommandReference
+ __OBJC_$_PROTOCOL_REFS__SFPBCommandReference
+ __OBJC_$_PROTOCOL_REFS__SFPBDomainEngagementScore
+ __OBJC_$_PROTOCOL_REFS__SFPBEngagementSignal
+ __OBJC_$_PROTOCOL_REFS__SFPBRFAttribution
+ __OBJC_$_PROTOCOL_REFS__SFPBRFHighlightedSubstring
+ __OBJC_CLASS_PROTOCOLS_$_RFAttribution
+ __OBJC_CLASS_PROTOCOLS_$_RFHighlightedSubstring
+ __OBJC_CLASS_PROTOCOLS_$_SFCommandReference
+ __OBJC_CLASS_PROTOCOLS_$__SFPBCommandReference
+ __OBJC_CLASS_PROTOCOLS_$__SFPBDomainEngagementScore
+ __OBJC_CLASS_PROTOCOLS_$__SFPBEngagementSignal
+ __OBJC_CLASS_PROTOCOLS_$__SFPBRFAttribution
+ __OBJC_CLASS_PROTOCOLS_$__SFPBRFHighlightedSubstring
+ __OBJC_CLASS_RO_$_RFAttribution
+ __OBJC_CLASS_RO_$_RFHighlightedSubstring
+ __OBJC_CLASS_RO_$_SFCommandReference
+ __OBJC_CLASS_RO_$__SFPBCommandReference
+ __OBJC_CLASS_RO_$__SFPBDomainEngagementScore
+ __OBJC_CLASS_RO_$__SFPBEngagementSignal
+ __OBJC_CLASS_RO_$__SFPBRFAttribution
+ __OBJC_CLASS_RO_$__SFPBRFHighlightedSubstring
+ __OBJC_LABEL_PROTOCOL_$_RFAttribution
+ __OBJC_LABEL_PROTOCOL_$_RFHighlightedSubstring
+ __OBJC_LABEL_PROTOCOL_$_SFCommandReference
+ __OBJC_LABEL_PROTOCOL_$__SFPBCommandReference
+ __OBJC_LABEL_PROTOCOL_$__SFPBDomainEngagementScore
+ __OBJC_LABEL_PROTOCOL_$__SFPBEngagementSignal
+ __OBJC_LABEL_PROTOCOL_$__SFPBRFAttribution
+ __OBJC_LABEL_PROTOCOL_$__SFPBRFHighlightedSubstring
+ __OBJC_METACLASS_RO_$_RFAttribution
+ __OBJC_METACLASS_RO_$_RFHighlightedSubstring
+ __OBJC_METACLASS_RO_$_SFCommandReference
+ __OBJC_METACLASS_RO_$__SFPBCommandReference
+ __OBJC_METACLASS_RO_$__SFPBDomainEngagementScore
+ __OBJC_METACLASS_RO_$__SFPBEngagementSignal
+ __OBJC_METACLASS_RO_$__SFPBRFAttribution
+ __OBJC_METACLASS_RO_$__SFPBRFHighlightedSubstring
+ __OBJC_PROTOCOL_$_RFAttribution
+ __OBJC_PROTOCOL_$_RFHighlightedSubstring
+ __OBJC_PROTOCOL_$_SFCommandReference
+ __OBJC_PROTOCOL_$__SFPBCommandReference
+ __OBJC_PROTOCOL_$__SFPBDomainEngagementScore
+ __OBJC_PROTOCOL_$__SFPBEngagementSignal
+ __OBJC_PROTOCOL_$__SFPBRFAttribution
+ __OBJC_PROTOCOL_$__SFPBRFHighlightedSubstring
+ __SFPBCommandReferenceReadFrom
+ __SFPBDomainEngagementScoreReadFrom
+ __SFPBEngagementSignalReadFrom
+ __SFPBRFAttributionReadFrom
+ __SFPBRFHighlightedSubstringReadFrom
+ ___PARLogHandleForCategory_block_invoke.29157
+ ___PARLogHandleForCategory_block_invoke.35428
+ ___block_literal_global.23814
+ ___block_literal_global.29169
+ ___block_literal_global.35423
+ ___getDispatchQueue_block_invoke.29173
+ _getDispatchQueue.29167
+ _getDispatchQueue.onceToken.29168
+ _getDispatchQueue.queue.29170
+ _objc_msgSend$addAttributions:
+ _objc_msgSend$addDomainEngagementScores:
+ _objc_msgSend$addHighlighted_substrings:
+ _objc_msgSend$addReferencedCommands:
+ _objc_msgSend$attributions
+ _objc_msgSend$commandReference
+ _objc_msgSend$domain
+ _objc_msgSend$domainEngagementScores
+ _objc_msgSend$forceEnable3DTouch
+ _objc_msgSend$highlighted_substrings
+ _objc_msgSend$index
+ _objc_msgSend$localScore
+ _objc_msgSend$localScoreConfidence
+ _objc_msgSend$locale
+ _objc_msgSend$referencedCommands
+ _objc_msgSend$scoreConfidence
+ _objc_msgSend$serverScoreConfidence
+ _objc_msgSend$setAttributions:
+ _objc_msgSend$setCommandReference:
+ _objc_msgSend$setDomain:
+ _objc_msgSend$setForceEnable3DTouch:
+ _objc_msgSend$setHighlighted_substrings:
+ _objc_msgSend$setIndex:
+ _objc_msgSend$setLocalScore:
+ _objc_msgSend$setLocalScoreConfidence:
+ _objc_msgSend$setLocale:
+ _objc_msgSend$setReferencedCommands:
+ _objc_msgSend$setScoreConfidence:
+ _objc_msgSend$setServerScoreConfidence:
+ _objc_msgSend$setSubstring:
+ _objc_msgSend$setVersion:
+ _objc_msgSend$substring
+ _objc_msgSend$version
- GCC_except_table10267
- GCC_except_table10924
- _PARLogHandleForCategory.logHandles.0.28472
- _PARLogHandleForCategory.logHandles.0.34639
- _PARLogHandleForCategory.logHandles.1.28468
- _PARLogHandleForCategory.logHandles.1.34632
- _PARLogHandleForCategory.logHandles.2.28474
- _PARLogHandleForCategory.logHandles.2.34642
- _PARLogHandleForCategory.logHandles.3.28476
- _PARLogHandleForCategory.logHandles.3.34643
- _PARLogHandleForCategory.logHandles.4.28478
- _PARLogHandleForCategory.logHandles.4.34644
- _PARLogHandleForCategory.logHandles.5.28479
- _PARLogHandleForCategory.logHandles.5.34646
- _PARLogHandleForCategory.onceToken.28467
- _PARLogHandleForCategory.onceToken.34630
- __OBJC_$_PROP_LIST_RFExpandableStandardCardSection.195
- __OBJC_$_PROP_LIST_RFFactItemButtonCardSection.235
- __OBJC_$_PROP_LIST_RFFactItemShortNumberCardSection.221
- __OBJC_$_PROP_LIST_RFFactItemStandardCardSection.216
- __OBJC_$_PROP_LIST_RFFormattedText.130
- __OBJC_$_PROP_LIST_RFLongItemStandardCardSection.201
- __OBJC_$_PROP_LIST_RFPrimaryHeaderRichCardSection.210
- __OBJC_$_PROP_LIST_RFPrimaryHeaderStandardCardSection.196
- __OBJC_$_PROP_LIST_RFReferenceFootnoteCardSection.201
- __OBJC_$_PROP_LIST_RFReferenceRichCardSection.200
- __OBJC_$_PROP_LIST_RFReferenceStandardCardSection.186
- __OBJC_$_PROP_LIST_RFSimpleItemRichCardSection.231
- __OBJC_$_PROP_LIST_RFSimpleItemStandardCardSection.212
- __OBJC_$_PROP_LIST_RFSummaryItemAlignedTextCardSection.221
- __OBJC_$_PROP_LIST_RFSummaryItemShortNumberCardSection.226
- __OBJC_$_PROP_LIST_RFSummaryItemStandardCardSection.220
- __OBJC_$_PROP_LIST_RFSummaryItemTextCardSection.207
- __OBJC_$_PROP_LIST_SFActivityIndicatorCardSection.185
- __OBJC_$_PROP_LIST_SFAddToPhotosLibraryCommand.98
- __OBJC_$_PROP_LIST_SFAppIconCardSection.190
- __OBJC_$_PROP_LIST_SFAppLinkCardSection.193
- __OBJC_$_PROP_LIST_SFArchiveViewCardSection.188
- __OBJC_$_PROP_LIST_SFAttributionFooterCardSection.208
- __OBJC_$_PROP_LIST_SFAudioPlaybackCardSection.228
- __OBJC_$_PROP_LIST_SFBeginMapsRoutingCommand.131
- __OBJC_$_PROP_LIST_SFButtonCardSection.198
- __OBJC_$_PROP_LIST_SFButtonListCardSection.196
- __OBJC_$_PROP_LIST_SFCallCommand.95
- __OBJC_$_PROP_LIST_SFClearProactiveCategoryCommand.116
- __OBJC_$_PROP_LIST_SFCollectionCardSection.218
- __OBJC_$_PROP_LIST_SFColorBarCardSection.202
- __OBJC_$_PROP_LIST_SFCombinedCardSection.186
- __OBJC_$_PROP_LIST_SFCommand.93
- __OBJC_$_PROP_LIST_SFCommandRowCardSection.213
- __OBJC_$_PROP_LIST_SFCompactRowCardSection.212
- __OBJC_$_PROP_LIST_SFCopyCommand.98
- __OBJC_$_PROP_LIST_SFCreateCalendarEventCommand.98
- __OBJC_$_PROP_LIST_SFCreateContactCommand.109
- __OBJC_$_PROP_LIST_SFCreateReminderCommand.98
- __OBJC_$_PROP_LIST_SFDescriptionCardSection.283
- __OBJC_$_PROP_LIST_SFDetailedRowCardSection.313
- __OBJC_$_PROP_LIST_SFDrillDownMetadata.142
- __OBJC_$_PROP_LIST_SFEmailCommand.95
- __OBJC_$_PROP_LIST_SFExpandInlineCommand.97
- __OBJC_$_PROP_LIST_SFFindMyCardSection.186
- __OBJC_$_PROP_LIST_SFFlightCardSection.200
- __OBJC_$_PROP_LIST_SFGridCardSection.186
- __OBJC_$_PROP_LIST_SFHeroCardSection.218
- __OBJC_$_PROP_LIST_SFHeroTitleCardSection.211
- __OBJC_$_PROP_LIST_SFHorizontalButtonCardSection.186
- __OBJC_$_PROP_LIST_SFHorizontalScrollCardSection.197
- __OBJC_$_PROP_LIST_SFImagesCardSection.195
- __OBJC_$_PROP_LIST_SFIndexedUserActivityCommand.100
- __OBJC_$_PROP_LIST_SFInfoCardSection.197
- __OBJC_$_PROP_LIST_SFInvokeSiriCommand.95
- __OBJC_$_PROP_LIST_SFKeyValueDataCardSection.195
- __OBJC_$_PROP_LIST_SFLargeTitleDetailedRowCardSection.204
- __OBJC_$_PROP_LIST_SFLaunchAppCommand.95
- __OBJC_$_PROP_LIST_SFLeadingTrailingCardSection.203
- __OBJC_$_PROP_LIST_SFLinkPresentationCardSection.203
- __OBJC_$_PROP_LIST_SFListenToCardSection.198
- __OBJC_$_PROP_LIST_SFManageReservationCommand.97
- __OBJC_$_PROP_LIST_SFMapCardSection.242
- __OBJC_$_PROP_LIST_SFMapPlaceCardSection.202
- __OBJC_$_PROP_LIST_SFMapsDetailedRowCardSection.199
- __OBJC_$_PROP_LIST_SFMediaInfoCardSection.254
- __OBJC_$_PROP_LIST_SFMediaPlayerCardSection.196
- __OBJC_$_PROP_LIST_SFMediaRemoteControlCardSection.199
- __OBJC_$_PROP_LIST_SFMessageCardSection.218
- __OBJC_$_PROP_LIST_SFMetaInfoCardSection.212
- __OBJC_$_PROP_LIST_SFMiniCardSection.203
- __OBJC_$_PROP_LIST_SFNewsCardSection.222
- __OBJC_$_PROP_LIST_SFNowPlayingCardSection.193
- __OBJC_$_PROP_LIST_SFOpenAppClipCommand.95
- __OBJC_$_PROP_LIST_SFOpenCalculationCommand.100
- __OBJC_$_PROP_LIST_SFOpenCoreSpotlightItemCommand.105
- __OBJC_$_PROP_LIST_SFOpenFileProviderItemCommand.111
- __OBJC_$_PROP_LIST_SFOpenMediaCommand.104
- __OBJC_$_PROP_LIST_SFOpenPunchoutCommand.98
- __OBJC_$_PROP_LIST_SFOpenWebClipCommand.95
- __OBJC_$_PROP_LIST_SFPerformContactActionCommand.113
- __OBJC_$_PROP_LIST_SFPerformContactQueryCommand.95
- __OBJC_$_PROP_LIST_SFPerformEntityQueryCommand.149
- __OBJC_$_PROP_LIST_SFPerformIntentCommand.117
- __OBJC_$_PROP_LIST_SFPerformPersonEntityQueryCommand.98
- __OBJC_$_PROP_LIST_SFPersonHeaderCardSection.186
- __OBJC_$_PROP_LIST_SFPlayMediaCommand.110
- __OBJC_$_PROP_LIST_SFPlayVideoCommand.98
- __OBJC_$_PROP_LIST_SFProductCardSection.188
- __OBJC_$_PROP_LIST_SFRejectPeopleInPhotoCommand.107
- __OBJC_$_PROP_LIST_SFRequestAppClipInstallCommand.104
- __OBJC_$_PROP_LIST_SFRequestUserReportCommand.98
- __OBJC_$_PROP_LIST_SFResponseWrapperCardSection.209
- __OBJC_$_PROP_LIST_SFRichTitleCardSection.352
- __OBJC_$_PROP_LIST_SFRowCardSection.269
- __OBJC_$_PROP_LIST_SFRunVoiceShortcutCommand.100
- __OBJC_$_PROP_LIST_SFScoreboardCardSection.212
- __OBJC_$_PROP_LIST_SFSearchInAppCommand.100
- __OBJC_$_PROP_LIST_SFSearchWebCommand.95
- __OBJC_$_PROP_LIST_SFSectionHeaderCardSection.189
- __OBJC_$_PROP_LIST_SFSelectableGridCardSection.195
- __OBJC_$_PROP_LIST_SFShareCommand.98
- __OBJC_$_PROP_LIST_SFShowAppStoreSheetCommand.100
- __OBJC_$_PROP_LIST_SFShowContactCardCommand.106
- __OBJC_$_PROP_LIST_SFShowPhotosOneUpViewCommand.130
- __OBJC_$_PROP_LIST_SFShowPurchaseRequestSheetCommand.95
- __OBJC_$_PROP_LIST_SFShowSFCardCommand.98
- __OBJC_$_PROP_LIST_SFShowScreenTimeRequestSheetCommand.95
- __OBJC_$_PROP_LIST_SFShowWrapperResponseViewCommand.98
- __OBJC_$_PROP_LIST_SFSocialMediaPostCardSection.246
- __OBJC_$_PROP_LIST_SFSplitCardSection.218
- __OBJC_$_PROP_LIST_SFStockChartCardSection.197
- __OBJC_$_PROP_LIST_SFStrokeAnimationCardSection.201
- __OBJC_$_PROP_LIST_SFSubscribeForUpdatesCommand.107
- __OBJC_$_PROP_LIST_SFSuggestionCardSection.238
- __OBJC_$_PROP_LIST_SFTableHeaderRowCardSection.205
- __OBJC_$_PROP_LIST_SFTableRowCardSection.238
- __OBJC_$_PROP_LIST_SFTextColumnsCardSection.202
- __OBJC_$_PROP_LIST_SFTitleCardSection.199
- __OBJC_$_PROP_LIST_SFToggleAudioCommand.117
- __OBJC_$_PROP_LIST_SFToggleWatchListStatusCommand.98
- __OBJC_$_PROP_LIST_SFTrackListCardSection.193
- __OBJC_$_PROP_LIST_SFUpdateSearchQueryCommand.107
- __OBJC_$_PROP_LIST_SFVerticalLayoutCardSection.223
- __OBJC_$_PROP_LIST_SFViewEmailCommand.97
- __OBJC_$_PROP_LIST_SFWatchListCardSection.189
- __OBJC_$_PROP_LIST_SFWatchNowCardSection.194
- __OBJC_$_PROP_LIST_SFWebCardSection.185
- __OBJC_$_PROP_LIST_SFWorldMapCardSection.194
- __OBJC_$_PROP_LIST__SFPBCardSection.1520
- __OBJC_$_PROP_LIST__SFPBCardSectionValue.2541
- __OBJC_$_PROP_LIST__SFPBClearProactiveCategoryCommand.2572
- __OBJC_$_PROP_LIST__SFPBClockImage.2602
- __OBJC_$_PROP_LIST__SFPBCloudChannelsRequestItem.2633
- __OBJC_$_PROP_LIST__SFPBCollectionCardSection.2670
- __OBJC_$_PROP_LIST__SFPBCollectionStyle.2728
- __OBJC_$_PROP_LIST__SFPBCollectionStyleGrid.2742
- __OBJC_$_PROP_LIST__SFPBCollectionStyleHorizontallyScrolling.2756
- __OBJC_$_PROP_LIST__SFPBCollectionStyleRow.2770
- __OBJC_$_PROP_LIST__SFPBColor.2890
- __OBJC_$_PROP_LIST__SFPBColorBarCardSection.2913
- __OBJC_$_PROP_LIST__SFPBCombinedCardSection.2920
- __OBJC_$_PROP_LIST__SFPBCommand.3567
- __OBJC_$_PROP_LIST__SFPBCommandButtonItem.3582
- __OBJC_$_PROP_LIST__SFPBCommandRowCardSection.3605
- __OBJC_$_PROP_LIST__SFPBCommandValue.3625
- __OBJC_$_PROP_LIST__SFPBCompactRowCardSection.3640
- __OBJC_$_PROP_LIST__SFPBContactButtonItem.3660
- __OBJC_$_PROP_LIST__SFPBContactCopyItem.3675
- __OBJC_$_PROP_LIST__SFPBContactImage.3710
- __OBJC_$_PROP_LIST__SFPBCopyCommand.3730
- __OBJC_$_PROP_LIST__SFPBCopyItem.3789
- __OBJC_$_PROP_LIST__SFPBCoreSpotlightButtonItem.3816
- __OBJC_$_PROP_LIST__SFPBCoreSpotlightCopyItem.3847
- __OBJC_$_PROP_LIST__SFPBCoreSpotlightRankingSignals.3929
- __OBJC_$_PROP_LIST__SFPBCoreSpotlightShareItem.3944
- __OBJC_$_PROP_LIST__SFPBCreateCalendarEventCommand.3964
- __OBJC_$_PROP_LIST__SFPBCreateContactCommand.3979
- __OBJC_$_PROP_LIST__SFPBCreateReminderCommand.3999
- __OBJC_$_PROP_LIST__SFPBDate.4017
- __OBJC_$_PROP_LIST__SFPBDescriptionCardSection.4130
- __OBJC_$_PROP_LIST__SFPBDetailedRowCardSection.4304
- __OBJC_$_PROP_LIST__SFPBDomainSubscriptionRequestItem.4324
- __OBJC_$_PROP_LIST__SFPBDrillDownMetadata.4430
- __OBJC_$_PROP_LIST__SFPBDynamicURLImageResource.4484
- __OBJC_$_PROP_LIST__SFPBEmailCommand.4491
- __OBJC_$_PROP_LIST__SFPBEntitySearchMetadata.4515
- __OBJC_$_PROP_LIST__SFPBExpandInlineCommand.4529
- __OBJC_$_PROP_LIST__SFPBFindMyCardSection.4536
- __OBJC_$_PROP_LIST__SFPBFlight.4622
- __OBJC_$_PROP_LIST__SFPBFlightCardSection.4648
- __OBJC_$_PROP_LIST__SFPBFlightDetails.4662
- __OBJC_$_PROP_LIST__SFPBFlightLeg.4802
- __OBJC_$_PROP_LIST__SFPBFormattedText.4850
- __OBJC_$_PROP_LIST__SFPBGradientColor.4878
- __OBJC_$_PROP_LIST__SFPBGraphicalFloat.4892
- __OBJC_$_PROP_LIST__SFPBGridCardSection.4899
- __OBJC_$_PROP_LIST__SFPBHeroCardSection.4906
- __OBJC_$_PROP_LIST__SFPBHeroTitleCardSection.4921
- __OBJC_$_PROP_LIST__SFPBHorizontalButtonCardSection.4940
- __OBJC_$_PROP_LIST__SFPBHorizontalScrollCardSection.4947
- __OBJC_$_PROP_LIST__SFPBImage.5199
- __OBJC_$_PROP_LIST__SFPBImageCopyItem.5206
- __OBJC_$_PROP_LIST__SFPBImageDerivedColor.5213
- __OBJC_$_PROP_LIST__SFPBImageOption.5241
- __OBJC_$_PROP_LIST__SFPBImagesCardSection.5269
- __OBJC_$_PROP_LIST__SFPBIndexState.5315
- __OBJC_$_PROP_LIST__SFPBIndexedUserActivityCommand.5330
- __OBJC_$_PROP_LIST__SFPBInfoCardSection.5360
- __OBJC_$_PROP_LIST__SFPBInfoTuple.5404
- __OBJC_$_PROP_LIST__SFPBInvokeSiriCommand.5419
- __OBJC_$_PROP_LIST__SFPBKeyValueDataCardSection.5450
- __OBJC_$_PROP_LIST__SFPBKeyValueTuple.5458
- __OBJC_$_PROP_LIST__SFPBLargeTitleDetailedRowCardSection.5488
- __OBJC_$_PROP_LIST__SFPBLatLng.5510
- __OBJC_$_PROP_LIST__SFPBLaunchAppCommand.5517
- __OBJC_$_PROP_LIST__SFPBLeadingTrailingCardSection.5556
- __OBJC_$_PROP_LIST__SFPBLinkPresentationCardSection.5593
- __OBJC_$_PROP_LIST__SFPBListenToCardSection.5624
- __OBJC_$_PROP_LIST__SFPBLocalImage.5638
- __OBJC_$_PROP_LIST__SFPBLocationTypeInfo.5653
- __OBJC_$_PROP_LIST__SFPBMailRankingSignals.5755
- __OBJC_$_PROP_LIST__SFPBMailResultDetails.5785
- __OBJC_$_PROP_LIST__SFPBManageReservationCommand.5791
- __OBJC_$_PROP_LIST__SFPBMapCardSection.5867
- __OBJC_$_PROP_LIST__SFPBMapPlaceCardSection.5882
- __OBJC_$_PROP_LIST__SFPBMapRegion.5928
- __OBJC_$_PROP_LIST__SFPBMapsDetailedRowCardSection.5943
- __OBJC_$_PROP_LIST__SFPBMediaArtworkImage.5958
- __OBJC_$_PROP_LIST__SFPBMediaDetail.5973
- __OBJC_$_PROP_LIST__SFPBMediaInfoCardSection.6087
- __OBJC_$_PROP_LIST__SFPBMediaItem.6167
- __OBJC_$_PROP_LIST__SFPBMediaMetadata.6239
- __OBJC_$_PROP_LIST__SFPBMediaOffer.6278
- __OBJC_$_PROP_LIST__SFPBMediaPlayerCardSection.6298
- __OBJC_$_PROP_LIST__SFPBMediaRemoteControlCardSection.6329
- __OBJC_$_PROP_LIST__SFPBMessageAttachment.6345
- __OBJC_$_PROP_LIST__SFPBMessageCardSection.6397
- __OBJC_$_PROP_LIST__SFPBMetaInfoCardSection.6436
- __OBJC_$_PROP_LIST__SFPBMiniCardSection.6443
- __OBJC_$_PROP_LIST__SFPBMonogramImage.6466
- __OBJC_$_PROP_LIST__SFPBMoreResults.6473
- __OBJC_$_PROP_LIST__SFPBNamedProtobufMessage.6496
- __OBJC_$_PROP_LIST__SFPBNewsCardSection.6527
- __OBJC_$_PROP_LIST__SFPBNowPlayingCardSection.6546
- __OBJC_$_PROP_LIST__SFPBOpenAppClipCommand.6561
- __OBJC_$_PROP_LIST__SFPBOpenCalculationCommand.6584
- __OBJC_$_PROP_LIST__SFPBOpenCoreSpotlightItemCommand.6599
- __OBJC_$_PROP_LIST__SFPBOpenFileProviderItemCommand.6622
- __OBJC_$_PROP_LIST__SFPBOpenMediaCommand.6637
- __OBJC_$_PROP_LIST__SFPBOpenPunchoutCommand.6644
- __OBJC_$_PROP_LIST__SFPBOpenWebClipCommand.6651
- __OBJC_$_PROP_LIST__SFPBPatternModel.6690
- __OBJC_$_PROP_LIST__SFPBPerformContactActionCommand.6720
- __OBJC_$_PROP_LIST__SFPBPerformContactQueryCommand.6727
- __OBJC_$_PROP_LIST__SFPBPerformEntityQueryCommand.6766
- __OBJC_$_PROP_LIST__SFPBPerformIntentCommand.6781
- __OBJC_$_PROP_LIST__SFPBPerformPersonEntityQueryCommand.6788
- __OBJC_$_PROP_LIST__SFPBPerson.6843
- __OBJC_$_PROP_LIST__SFPBPersonHeaderCardSection.6850
- __OBJC_$_PROP_LIST__SFPBPhotosLibraryImage.6886
- __OBJC_$_PROP_LIST__SFPBPin.6901
- __OBJC_$_PROP_LIST__SFPBPlayMediaCommand.6916
- __OBJC_$_PROP_LIST__SFPBPlayVideoCommand.6923
- __OBJC_$_PROP_LIST__SFPBPointSize.6946
- __OBJC_$_PROP_LIST__SFPBProduct.6977
- __OBJC_$_PROP_LIST__SFPBProductAvailability.6999
- __OBJC_$_PROP_LIST__SFPBProductCardSection.7014
- __OBJC_$_PROP_LIST__SFPBProductInventory.7070
- __OBJC_$_PROP_LIST__SFPBProductInventoryResult.7093
- __OBJC_$_PROP_LIST__SFPBPunchout.7150
- __OBJC_$_PROP_LIST__SFPBQueryUnderstandingParse.7284
- __OBJC_$_PROP_LIST__SFPBQuickLookThumbnailImage.7299
- __OBJC_$_PROP_LIST__SFPBRFAppIconImage.7319
- __OBJC_$_PROP_LIST__SFPBRFAspectRatio.7327
- __OBJC_$_PROP_LIST__SFPBRFAvatarImage.7346
- __OBJC_$_PROP_LIST__SFPBRFBadgedImage.7360
- __OBJC_$_PROP_LIST__SFPBRFColor.7394
- __OBJC_$_PROP_LIST__SFPBRFDefaultBrowserAppIconImage.7400
- __OBJC_$_PROP_LIST__SFPBRFExpandableStandardCardSection.7435
- __OBJC_$_PROP_LIST__SFPBRFExpandingComponentContent.7458
- __OBJC_$_PROP_LIST__SFPBRFFactItemButtonCardSection.7546
- __OBJC_$_PROP_LIST__SFPBRFFactItemShortNumberCardSection.7591
- __OBJC_$_PROP_LIST__SFPBRFFactItemStandardCardSection.7607
- __OBJC_$_PROP_LIST__SFPBRFFormattedText.7681
- __OBJC_$_PROP_LIST__SFPBRFImageElement.7701
- __OBJC_$_PROP_LIST__SFPBRFImageSource.7792
- __OBJC_$_PROP_LIST__SFPBRFLongItemStandardCardSection.7815
- __OBJC_$_PROP_LIST__SFPBRFMonogramImage.7830
- __OBJC_$_PROP_LIST__SFPBRFOptionalBool.7837
- __OBJC_$_PROP_LIST__SFPBRFOptionalFloat.7844
- __OBJC_$_PROP_LIST__SFPBRFPrimaryHeaderRichCardSection.7851
- __OBJC_$_PROP_LIST__SFPBRFPrimaryHeaderStandardCardSection.7858
- __OBJC_$_PROP_LIST__SFPBRFRGBValue.7888
- __OBJC_$_PROP_LIST__SFPBRFReferenceFootnoteCardSection.7895
- __OBJC_$_PROP_LIST__SFPBRFReferenceRichCardSection.7902
- __OBJC_$_PROP_LIST__SFPBRFReferenceStandardCardSection.7909
- __OBJC_$_PROP_LIST__SFPBRFSimpleItemRichCardSection.7940
- __OBJC_$_PROP_LIST__SFPBRFSimpleItemStandardCardSection.7947
- __OBJC_$_PROP_LIST__SFPBRFSummaryItemAlignedTextCardSection.7963
- __OBJC_$_PROP_LIST__SFPBRFSummaryItemShortNumberCardSection.7970
- __OBJC_$_PROP_LIST__SFPBRFSummaryItemStandardCardSection.7985
- __OBJC_$_PROP_LIST__SFPBRFSummaryItemTextCardSection.7992
- __OBJC_$_PROP_LIST__SFPBRFSymbolImage.8031
- __OBJC_$_PROP_LIST__SFPBRFTextElement.8062
- __OBJC_$_PROP_LIST__SFPBRFTextEncapsulation.8076
- __OBJC_$_PROP_LIST__SFPBRFTextProperty.8106
- __OBJC_$_PROP_LIST__SFPBRFUrlImage.8162
- __OBJC_$_PROP_LIST__SFPBRFVisualElement.8181
- __OBJC_$_PROP_LIST__SFPBRFVisualProperty.8203
- __OBJC_$_PROP_LIST__SFPBReferentialCommand.8218
- __OBJC_$_PROP_LIST__SFPBRejectPeopleInPhotoCommand.8238
- __OBJC_$_PROP_LIST__SFPBReminder.8253
- __OBJC_$_PROP_LIST__SFPBRequestAppClipInstallCommand.8260
- __OBJC_$_PROP_LIST__SFPBRequestUserReportCommand.8267
- __OBJC_$_PROP_LIST__SFPBResponseWrapperCardSection.8321
- __OBJC_$_PROP_LIST__SFPBResultEntity.8349
- __OBJC_$_PROP_LIST__SFPBRichText.8389
- __OBJC_$_PROP_LIST__SFPBRichTitleCardSection.8537
- __OBJC_$_PROP_LIST__SFPBRowCardSection.8632
- __OBJC_$_PROP_LIST__SFPBRunVoiceShortcutCommand.8647
- __OBJC_$_PROP_LIST__SFPBScene.8669
- __OBJC_$_PROP_LIST__SFPBScoreboardCardSection.8713
- __OBJC_$_PROP_LIST__SFPBSearchInAppCommand.8720
- __OBJC_$_PROP_LIST__SFPBSearchSuggestion.8809
- __OBJC_$_PROP_LIST__SFPBSearchWebCommand.8816
- __OBJC_$_PROP_LIST__SFPBSectionHeaderCardSection.8824
- __OBJC_$_PROP_LIST__SFPBSelectableGridCardSection.8854
- __OBJC_$_PROP_LIST__SFPBShareCommand.8874
- __OBJC_$_PROP_LIST__SFPBShareItem.8907
- __OBJC_$_PROP_LIST__SFPBShowAppStoreSheetCommand.8922
- __OBJC_$_PROP_LIST__SFPBShowContactCardCommand.8937
- __OBJC_$_PROP_LIST__SFPBShowPhotosOneUpViewCommand.8988
- __OBJC_$_PROP_LIST__SFPBShowPurchaseRequestSheetCommand.9003
- __OBJC_$_PROP_LIST__SFPBShowSFCardCommand.9018
- __OBJC_$_PROP_LIST__SFPBShowScreenTimeRequestSheetCommand.9025
- __OBJC_$_PROP_LIST__SFPBShowWrapperResponseViewCommand.9032
- __OBJC_$_PROP_LIST__SFPBSocialMediaPostCardSection.9096
- __OBJC_$_PROP_LIST__SFPBSplitCardSection.9163
- __OBJC_$_PROP_LIST__SFPBSportsDetail.9178
- __OBJC_$_PROP_LIST__SFPBSportsSubscriptionRequestItem.9209
- __OBJC_$_PROP_LIST__SFPBSportsTeam.9242
- __OBJC_$_PROP_LIST__SFPBStockChartCardSection.9265
- __OBJC_$_PROP_LIST__SFPBStringDictionary.9284
- __OBJC_$_PROP_LIST__SFPBStrokeAnimationCardSection.9335
- __OBJC_$_PROP_LIST__SFPBStructuredLocation.9358
- __OBJC_$_PROP_LIST__SFPBSubscribeForUpdatesCommand.9391
- __OBJC_$_PROP_LIST__SFPBSuggestionCardSection.9430
- __OBJC_$_PROP_LIST__SFPBSymbolImage.9464
- __OBJC_$_PROP_LIST__SFPBTableAlignmentSchema.9488
- __OBJC_$_PROP_LIST__SFPBTableColumnAlignment.9518
- __OBJC_$_PROP_LIST__SFPBTableHeaderRowCardSection.9586
- __OBJC_$_PROP_LIST__SFPBTableRowCardSection.9606
- __OBJC_$_PROP_LIST__SFPBText.9623
- __OBJC_$_PROP_LIST__SFPBTextColumn.9645
- __OBJC_$_PROP_LIST__SFPBTextColumnSection.9680
- __OBJC_$_PROP_LIST__SFPBTextColumnsCardSection.9703
- __OBJC_$_PROP_LIST__SFPBTextCopyItem.9718
- __OBJC_$_PROP_LIST__SFPBTimeZone.9725
- __OBJC_$_PROP_LIST__SFPBTitleCardSection.9732
- __OBJC_$_PROP_LIST__SFPBTitleSubtitleTuple.9739
- __OBJC_$_PROP_LIST__SFPBToggleAudioCommand.9762
- __OBJC_$_PROP_LIST__SFPBToggleWatchListStatusCommand.9782
- __OBJC_$_PROP_LIST__SFPBTopic.9825
- __OBJC_$_PROP_LIST__SFPBTrack.9857
- __OBJC_$_PROP_LIST__SFPBTrackListCardSection.9879
- __OBJC_$_PROP_LIST__SFPBURL.9886
- __OBJC_$_PROP_LIST__SFPBURLImage.9901
- __OBJC_$_PROP_LIST__SFPBURLShareItem.9908
- __OBJC_$_PROP_LIST__SFPBUpdateSearchQueryCommand.9923
- __OBJC_$_PROP_LIST__SFPBUserActivityData.9954
- __OBJC_$_PROP_LIST__SFPBUserActivityInfo.9977
- __OBJC_$_PROP_LIST__SFPBUserReportRequest.10052
- __OBJC_$_PROP_LIST__SFPBVerticalLayoutCardSection.10083
- __OBJC_$_PROP_LIST__SFPBViewEmailCommand.10089
- __OBJC_$_PROP_LIST__SFPBWatchListButtonItem.10096
- __OBJC_$_PROP_LIST__SFPBWatchListCardSection.10103
- __OBJC_$_PROP_LIST__SFPBWatchListItem.10182
- __OBJC_$_PROP_LIST__SFPBWatchNowCardSection.10196
- __OBJC_$_PROP_LIST__SFPBWeatherColor.10211
- __OBJC_$_PROP_LIST__SFPBWeatherDetails.10218
- __OBJC_$_PROP_LIST__SFPBWebCardSection.10233
- __OBJC_$_PROP_LIST__SFPBWorldMapCardSection.10256
- ___PARLogHandleForCategory_block_invoke.28470
- ___PARLogHandleForCategory_block_invoke.34636
- ___block_literal_global.23189
- ___block_literal_global.28482
- ___block_literal_global.34631
- ___getDispatchQueue_block_invoke.28486
- _getDispatchQueue.28480
- _getDispatchQueue.onceToken.28481
- _getDispatchQueue.queue.28483
CStrings:
+ "\x0f\x0f\x0f\x06"
+ "@\"SFCommandReference\""
+ "@\"SFCommandReference\"16@0:8"
+ "@\"_SFPBCommand\"24@0:8Q16"
+ "@\"_SFPBCommandReference\""
+ "@\"_SFPBCommandReference\"16@0:8"
+ "@\"_SFPBDomainEngagementScore\"24@0:8Q16"
+ "@\"_SFPBRFAttribution\"24@0:8Q16"
+ "@\"_SFPBRFHighlightedSubstring\"24@0:8Q16"
+ "RFAttribution"
+ "RFHighlightedSubstring"
+ "SFCommandReference"
+ "T@\"NSArray\",C,N,V_attributions"
+ "T@\"NSArray\",C,N,V_domainEngagementScores"
+ "T@\"NSArray\",C,N,V_highlighted_substrings"
+ "T@\"NSArray\",C,N,V_referencedCommands"
+ "T@\"NSNumber\",C,N,V_index"
+ "T@\"NSString\",C,N,V_locale"
+ "T@\"NSString\",C,N,V_params"
+ "T@\"NSString\",C,N,V_substring"
+ "T@\"RFTextProperty\",&,N,V_subtitle"
+ "T@\"RFTextProperty\",&,N,V_title"
+ "T@\"RFVisualProperty\",&,N,V_image"
+ "T@\"SFCommandReference\",&,N"
+ "T@\"SFCommandReference\",&,N,V_commandReference"
+ "T@\"_SFPBCommandReference\",&,N"
+ "T@\"_SFPBCommandReference\",&,N,V_commandReference"
+ "T@\"_SFPBRFTextProperty\",&,N,V_subtitle"
+ "T@\"_SFPBRFTextProperty\",&,N,V_title"
+ "T@\"_SFPBRFVisualProperty\",&,N,V_image"
+ "TB,N,V_forceEnable3DTouch"
+ "Tf,N,V_localScore"
+ "Tf,N,V_score"
+ "Tf,N,V_serverScore"
+ "Ti,N,V_domain"
+ "Ti,N,V_index"
+ "Ti,N,V_localScoreConfidence"
+ "Ti,N,V_scoreConfidence"
+ "Ti,N,V_serverScoreConfidence"
+ "Ti,N,V_version"
+ "_SFPBCommandReference"
+ "_SFPBDomainEngagementScore"
+ "_SFPBEngagementSignal"
+ "_SFPBRFAttribution"
+ "_SFPBRFHighlightedSubstring"
+ "_attributions"
+ "_commandReference"
+ "_domainEngagementScores"
+ "_forceEnable3DTouch"
+ "_highlighted_substrings"
+ "_index"
+ "_localScore"
+ "_localScoreConfidence"
+ "_locale"
+ "_referencedCommands"
+ "_scoreConfidence"
+ "_serverScoreConfidence"
+ "_substring"
+ "_version"
+ "addAttributions:"
+ "addDomainEngagementScores:"
+ "addHighlighted_substrings:"
+ "addReferencedCommands:"
+ "attributions"
+ "attributionsAtIndex:"
+ "attributionsCount"
+ "clearAttributions"
+ "clearDomainEngagementScores"
+ "clearHighlighted_substrings"
+ "clearReferencedCommands"
+ "com.apple.application"
+ "com.apple.applications"
+ "com.apple.bookmarks"
+ "com.apple.calculator"
+ "com.apple.calendar"
+ "com.apple.clouddocs.mobiledocumentsfileprovider"
+ "com.apple.coresuggestions"
+ "com.apple.developer"
+ "com.apple.dictionary"
+ "com.apple.directories"
+ "com.apple.documents"
+ "com.apple.ibooks"
+ "com.apple.keynote"
+ "com.apple.mail"
+ "com.apple.maps"
+ "com.apple.mobileaddressbook"
+ "com.apple.mobilecal"
+ "com.apple.mobilemail"
+ "com.apple.mobilenotes"
+ "com.apple.mobilesafari"
+ "com.apple.mobilesms"
+ "com.apple.mobiletimer"
+ "com.apple.music"
+ "com.apple.news"
+ "com.apple.numbers"
+ "com.apple.other"
+ "com.apple.other:search_app_store"
+ "com.apple.other:search_maps"
+ "com.apple.other:search_web"
+ "com.apple.other:taptoradar"
+ "com.apple.parsec.flights"
+ "com.apple.parsec.itunes.artist"
+ "com.apple.parsec.itunes.iossoftware"
+ "com.apple.parsec.kg"
+ "com.apple.parsec.maps"
+ "com.apple.parsec.movies"
+ "com.apple.parsec.news"
+ "com.apple.parsec.sports"
+ "com.apple.parsec.stocks"
+ "com.apple.parsec.tv.tvshow"
+ "com.apple.parsec.weather"
+ "com.apple.parsec.web_answer"
+ "com.apple.parsec.web_images"
+ "com.apple.parsec.web_index"
+ "com.apple.pdfs"
+ "com.apple.photos"
+ "com.apple.podcasts"
+ "com.apple.preferences"
+ "com.apple.reminders"
+ "com.apple.searchd.suggestions"
+ "com.apple.settings"
+ "com.apple.spotlight.related_search"
+ "com.apple.spotlight.suggestionlist.contact"
+ "com.apple.spotlight.suggestionlist.local"
+ "com.apple.spotlight.suggestionlist.parsec"
+ "com.apple.spotlight.suggestionlist.usertypedstring"
+ "com.apple.stocks"
+ "com.apple.taptoradar"
+ "com.apple.unknown"
+ "com.apple.voicememos"
+ "com.apple.weather"
+ "com.atebits.tweetie2"
+ "com.getdropbox.dropbox"
+ "com.giphy.giphyformessenger"
+ "com.google.chrome.ios"
+ "com.google.ios.youtube"
+ "com.google.maps"
+ "com.google.photos"
+ "com.groupon.grouponapp"
+ "com.linkedin.linkedin"
+ "com.microsoft.office.outlook"
+ "com.mlb.atbatuniversal"
+ "com.pandora"
+ "com.riffsy.riffsykeyboard"
+ "com.stubhub.stubhub"
+ "com.yahoo.aerogram"
+ "com.yelp.yelpiphone"
+ "com.zillow.zillowmap"
+ "commandReference"
+ "domainEngagementScores"
+ "domainEngagementScoresAtIndex:"
+ "domainEngagementScoresCount"
+ "forceEnable3DTouch"
+ "highlightedSubstrings"
+ "highlighted_substrings"
+ "highlighted_substringsAtIndex:"
+ "highlighted_substringsCount"
+ "index"
+ "localScore"
+ "localScoreConfidence"
+ "locale"
+ "net.whatsapp.whatsapp"
+ "pinterest"
+ "referencedCommands"
+ "referencedCommandsAtIndex:"
+ "referencedCommandsCount"
+ "scoreConfidence"
+ "serverScoreConfidence"
+ "setAttributions:"
+ "setCommandReference:"
+ "setDomainEngagementScores:"
+ "setForceEnable3DTouch:"
+ "setHighlighted_substrings:"
+ "setIndex:"
+ "setLocalScore:"
+ "setLocalScoreConfidence:"
+ "setLocale:"
+ "setReferencedCommands:"
+ "setScoreConfidence:"
+ "setServerScoreConfidence:"
+ "setSubstring:"
+ "setVersion:"
+ "substring"
+ "tv.twitch"
+ "v24@0:8@\"SFCommandReference\"16"
+ "v24@0:8@\"_SFPBCommandReference\"16"
+ "v24@0:8@\"_SFPBDomainEngagementScore\"16"
+ "v24@0:8@\"_SFPBRFAttribution\"16"
+ "v24@0:8@\"_SFPBRFHighlightedSubstring\"16"
+ "version"
- "\x0f\x0f\x0f\x05"
- "/\x03"

```
