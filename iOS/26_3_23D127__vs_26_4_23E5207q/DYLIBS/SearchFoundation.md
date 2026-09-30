## SearchFoundation

> `/System/Library/PrivateFrameworks/SearchFoundation.framework/SearchFoundation`

```diff

-3505.13.1.0.0
-  __TEXT.__text: 0x38d140
-  __TEXT.__auth_stubs: 0x630
-  __TEXT.__objc_methlist: 0x555c4
+3520.78.1.1.3
+  __TEXT.__text: 0x3d44cc
+  __TEXT.__auth_stubs: 0x5c0
+  __TEXT.__objc_methlist: 0x56744
   __TEXT.__const: 0x80
   __TEXT.__dlopen_cstrs: 0x52
-  __TEXT.__gcc_except_tab: 0x94
-  __TEXT.__cstring: 0x6dbf
+  __TEXT.__gcc_except_tab: 0x98
+  __TEXT.__cstring: 0x6eb0
   __TEXT.__oslogstring: 0x19a
-  __TEXT.__unwind_info: 0x83d0
-  __TEXT.__objc_classname: 0x4765
-  __TEXT.__objc_methname: 0x2f7e9
-  __TEXT.__objc_methtype: 0xfa59
-  __TEXT.__objc_stubs: 0x19720
-  __DATA_CONST.__got: 0x1760
-  __DATA_CONST.__const: 0xad0
-  __DATA_CONST.__objc_classlist: 0x1798
+  __TEXT.__unwind_info: 0x94c8
+  __TEXT.__objc_classname: 0x4855
+  __TEXT.__objc_methname: 0x30169
+  __TEXT.__objc_methtype: 0xfe4f
+  __TEXT.__objc_stubs: 0x19c00
+  __DATA_CONST.__got: 0x17b0
+  __DATA_CONST.__const: 0xaa8
+  __DATA_CONST.__objc_classlist: 0x17e8
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x1650
+  __DATA_CONST.__objc_protolist: 0x16a0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x76c0
+  __DATA_CONST.__objc_selrefs: 0x7850
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x1e88
-  __AUTH_CONST.__auth_got: 0x328
+  __DATA_CONST.__objc_superrefs: 0x1ef8
+  __AUTH_CONST.__auth_got: 0x2f0
   __AUTH_CONST.__const: 0xe0
-  __AUTH_CONST.__cfstring: 0xcfa0
-  __AUTH_CONST.__objc_const: 0xaa0f8
-  __AUTH.__objc_data: 0xc080
-  __DATA.__objc_ivar: 0x4400
-  __DATA.__data: 0x10bd8
+  __AUTH_CONST.__cfstring: 0xd1e0
+  __AUTH_CONST.__objc_const: 0xac490
+  __AUTH.__objc_data: 0xc3a0
+  __DATA.__objc_ivar: 0x44c8
+  __DATA.__data: 0x10f98
   __DATA.__bss: 0xc8
   __DATA_DIRTY.__objc_data: 0x2b70
   __DATA_DIRTY.__bss: 0x20

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 22B2948C-FD08-3636-AD32-163464BBA348
-  Functions: 17338
-  Symbols:   53446
-  CStrings:  13785
+  UUID: 34B6262E-D463-3ABD-AFFC-AC82DF80F141
+  Functions: 17574
+  Symbols:   54123
+  CStrings:  13961
 
Symbols:
+ +[RFAttributionSource supportsSecureCoding]
+ +[RFMarkdownCardSection supportsSecureCoding]
+ +[RFReferenceAttributionCardSection supportsSecureCoding]
+ +[SFPasteCommand supportsSecureCoding]
+ +[SFQuickLookCommand supportsSecureCoding]
+ -[RFAppIconImage fallback]
+ -[RFAppIconImage hasFallback]
+ -[RFAppIconImage setFallback:]
+ -[RFAttribution secondary_title]
+ -[RFAttribution setSecondary_title:]
+ -[RFAttributionSource .cxx_destruct]
+ -[RFAttributionSource attribution]
+ -[RFAttributionSource card_section]
+ -[RFAttributionSource copyWithZone:]
+ -[RFAttributionSource dictionaryRepresentation]
+ -[RFAttributionSource encodeWithCoder:]
+ -[RFAttributionSource hasAttribution]
+ -[RFAttributionSource hasCard_section]
+ -[RFAttributionSource hash]
+ -[RFAttributionSource initWithCoder:]
+ -[RFAttributionSource isEqual:]
+ -[RFAttributionSource jsonData]
+ -[RFAttributionSource setAttribution:]
+ -[RFAttributionSource setCard_section:]
+ -[RFAttributionSource setText_1:]
+ -[RFAttributionSource setThumbnail:]
+ -[RFAttributionSource text_1]
+ -[RFAttributionSource thumbnail]
+ -[RFAttributionSource(ProtobufInitializer) initWithProtobuf:]
+ -[RFLongItemStandardCardSection hasIs_markdown]
+ -[RFLongItemStandardCardSection is_markdown]
+ -[RFLongItemStandardCardSection setIs_markdown:]
+ -[RFMarkdownCardSection .cxx_destruct]
+ -[RFMarkdownCardSection copyWithZone:]
+ -[RFMarkdownCardSection dictionaryRepresentation]
+ -[RFMarkdownCardSection encodeWithCoder:]
+ -[RFMarkdownCardSection hasStreaming_state]
+ -[RFMarkdownCardSection hash]
+ -[RFMarkdownCardSection initWithCoder:]
+ -[RFMarkdownCardSection isEqual:]
+ -[RFMarkdownCardSection jsonData]
+ -[RFMarkdownCardSection markdown_data]
+ -[RFMarkdownCardSection markdown_strings]
+ -[RFMarkdownCardSection setMarkdown_data:]
+ -[RFMarkdownCardSection setMarkdown_strings:]
+ -[RFMarkdownCardSection setStreaming_state:]
+ -[RFMarkdownCardSection streaming_state]
+ -[RFMarkdownCardSection(ProtobufInitializer) initWithProtobuf:]
+ -[RFReferenceAttributionCardSection .cxx_destruct]
+ -[RFReferenceAttributionCardSection add_tint]
+ -[RFReferenceAttributionCardSection attribution_type]
+ -[RFReferenceAttributionCardSection copyWithZone:]
+ -[RFReferenceAttributionCardSection dictionaryRepresentation]
+ -[RFReferenceAttributionCardSection encodeWithCoder:]
+ -[RFReferenceAttributionCardSection expansion_type]
+ -[RFReferenceAttributionCardSection hasAdd_tint]
+ -[RFReferenceAttributionCardSection hasAttribution_type]
+ -[RFReferenceAttributionCardSection hasExpansion_type]
+ -[RFReferenceAttributionCardSection hash]
+ -[RFReferenceAttributionCardSection initWithCoder:]
+ -[RFReferenceAttributionCardSection isEqual:]
+ -[RFReferenceAttributionCardSection jsonData]
+ -[RFReferenceAttributionCardSection setAdd_tint:]
+ -[RFReferenceAttributionCardSection setAttribution_type:]
+ -[RFReferenceAttributionCardSection setExpansion_type:]
+ -[RFReferenceAttributionCardSection setSources:]
+ -[RFReferenceAttributionCardSection setText_1:]
+ -[RFReferenceAttributionCardSection setText_2:]
+ -[RFReferenceAttributionCardSection setThumbnails:]
+ -[RFReferenceAttributionCardSection sources]
+ -[RFReferenceAttributionCardSection text_1]
+ -[RFReferenceAttributionCardSection text_2]
+ -[RFReferenceAttributionCardSection thumbnails]
+ -[RFReferenceAttributionCardSection(ProtobufInitializer) initWithProtobuf:]
+ -[SFCardSectionValue rfMarkdownCardSection]
+ -[SFCardSectionValue rfReferenceAttributionCardSection]
+ -[SFCardSectionValue setRfMarkdownCardSection:]
+ -[SFCardSectionValue setRfReferenceAttributionCardSection:]
+ -[SFPasteCommand .cxx_destruct]
+ -[SFPasteCommand copyWithZone:]
+ -[SFPasteCommand copyableItems]
+ -[SFPasteCommand dictionaryRepresentation]
+ -[SFPasteCommand encodeWithCoder:]
+ -[SFPasteCommand hash]
+ -[SFPasteCommand initWithCoder:]
+ -[SFPasteCommand isEqual:]
+ -[SFPasteCommand jsonData]
+ -[SFPasteCommand setCopyableItems:]
+ -[SFPasteCommand(ProtobufInitializer) initWithProtobuf:]
+ -[SFQuickLookCommand .cxx_destruct]
+ -[SFQuickLookCommand copyWithZone:]
+ -[SFQuickLookCommand dictionaryRepresentation]
+ -[SFQuickLookCommand encodeWithCoder:]
+ -[SFQuickLookCommand hash]
+ -[SFQuickLookCommand initWithCoder:]
+ -[SFQuickLookCommand isEqual:]
+ -[SFQuickLookCommand jsonData]
+ -[SFQuickLookCommand setUrl:]
+ -[SFQuickLookCommand url]
+ -[SFQuickLookCommand(ProtobufInitializer) initWithProtobuf:]
+ -[SFStartLocalSearchFeedback initWithInput:triggerEvent:inputCharCount:inputWordCount:]
+ -[SFStartLocalSearchFeedback inputCharCount]
+ -[SFStartLocalSearchFeedback inputWordCount]
+ -[SFStartLocalSearchFeedback setInputCharCount:]
+ -[SFStartLocalSearchFeedback setInputWordCount:]
+ -[_SFPBCardSectionValue rfMarkdownCardSection]
+ -[_SFPBCardSectionValue rfReferenceAttributionCardSection]
+ -[_SFPBCardSectionValue setRfMarkdownCardSection:]
+ -[_SFPBCardSectionValue setRfReferenceAttributionCardSection:]
+ -[_SFPBCommand pasteCommand]
+ -[_SFPBCommand quickLookCommand]
+ -[_SFPBCommand setPasteCommand:]
+ -[_SFPBCommand setQuickLookCommand:]
+ -[_SFPBPasteCommand .cxx_destruct]
+ -[_SFPBPasteCommand addCopyableItems:]
+ -[_SFPBPasteCommand clearCopyableItems]
+ -[_SFPBPasteCommand copyableItemsAtIndex:]
+ -[_SFPBPasteCommand copyableItemsCount]
+ -[_SFPBPasteCommand copyableItems]
+ -[_SFPBPasteCommand dictionaryRepresentation]
+ -[_SFPBPasteCommand hash]
+ -[_SFPBPasteCommand initWithDictionary:]
+ -[_SFPBPasteCommand initWithJSON:]
+ -[_SFPBPasteCommand isEqual:]
+ -[_SFPBPasteCommand jsonData]
+ -[_SFPBPasteCommand readFrom:]
+ -[_SFPBPasteCommand setCopyableItems:]
+ -[_SFPBPasteCommand writeTo:]
+ -[_SFPBPasteCommand(FacadeInitializer) initWithFacade:]
+ -[_SFPBQuickLookCommand .cxx_destruct]
+ -[_SFPBQuickLookCommand dictionaryRepresentation]
+ -[_SFPBQuickLookCommand hash]
+ -[_SFPBQuickLookCommand initWithDictionary:]
+ -[_SFPBQuickLookCommand initWithJSON:]
+ -[_SFPBQuickLookCommand isEqual:]
+ -[_SFPBQuickLookCommand jsonData]
+ -[_SFPBQuickLookCommand readFrom:]
+ -[_SFPBQuickLookCommand setUrl:]
+ -[_SFPBQuickLookCommand url]
+ -[_SFPBQuickLookCommand writeTo:]
+ -[_SFPBQuickLookCommand(FacadeInitializer) initWithFacade:]
+ -[_SFPBRFAppIconImage fallback]
+ -[_SFPBRFAppIconImage setFallback:]
+ -[_SFPBRFAttribution secondary_title]
+ -[_SFPBRFAttribution setSecondary_title:]
+ -[_SFPBRFAttributionSource .cxx_destruct]
+ -[_SFPBRFAttributionSource attribution]
+ -[_SFPBRFAttributionSource card_section]
+ -[_SFPBRFAttributionSource dictionaryRepresentation]
+ -[_SFPBRFAttributionSource hash]
+ -[_SFPBRFAttributionSource initWithDictionary:]
+ -[_SFPBRFAttributionSource initWithJSON:]
+ -[_SFPBRFAttributionSource isEqual:]
+ -[_SFPBRFAttributionSource jsonData]
+ -[_SFPBRFAttributionSource readFrom:]
+ -[_SFPBRFAttributionSource setAttribution:]
+ -[_SFPBRFAttributionSource setCard_section:]
+ -[_SFPBRFAttributionSource setText_1:]
+ -[_SFPBRFAttributionSource setThumbnail:]
+ -[_SFPBRFAttributionSource text_1]
+ -[_SFPBRFAttributionSource thumbnail]
+ -[_SFPBRFAttributionSource whichSource]
+ -[_SFPBRFAttributionSource writeTo:]
+ -[_SFPBRFAttributionSource(FacadeInitializer) initWithFacade:]
+ -[_SFPBRFLongItemStandardCardSection is_markdown]
+ -[_SFPBRFLongItemStandardCardSection setIs_markdown:]
+ -[_SFPBRFMarkdownCardSection .cxx_destruct]
+ -[_SFPBRFMarkdownCardSection addMarkdown_strings:]
+ -[_SFPBRFMarkdownCardSection clearMarkdown_strings]
+ -[_SFPBRFMarkdownCardSection dictionaryRepresentation]
+ -[_SFPBRFMarkdownCardSection getMarkdown_data:forKey:]
+ -[_SFPBRFMarkdownCardSection hash]
+ -[_SFPBRFMarkdownCardSection initWithDictionary:]
+ -[_SFPBRFMarkdownCardSection initWithJSON:]
+ -[_SFPBRFMarkdownCardSection isEqual:]
+ -[_SFPBRFMarkdownCardSection jsonData]
+ -[_SFPBRFMarkdownCardSection markdown_data]
+ -[_SFPBRFMarkdownCardSection markdown_stringsAtIndex:]
+ -[_SFPBRFMarkdownCardSection markdown_stringsCount]
+ -[_SFPBRFMarkdownCardSection markdown_strings]
+ -[_SFPBRFMarkdownCardSection readFrom:]
+ -[_SFPBRFMarkdownCardSection setMarkdown_data:]
+ -[_SFPBRFMarkdownCardSection setMarkdown_data:forKey:]
+ -[_SFPBRFMarkdownCardSection setMarkdown_strings:]
+ -[_SFPBRFMarkdownCardSection setStreaming_state:]
+ -[_SFPBRFMarkdownCardSection streaming_state]
+ -[_SFPBRFMarkdownCardSection writeTo:]
+ -[_SFPBRFMarkdownCardSection(FacadeInitializer) initWithFacade:]
+ -[_SFPBRFReferenceAttributionCardSection .cxx_destruct]
+ -[_SFPBRFReferenceAttributionCardSection addSources:]
+ -[_SFPBRFReferenceAttributionCardSection addThumbnails:]
+ -[_SFPBRFReferenceAttributionCardSection add_tint]
+ -[_SFPBRFReferenceAttributionCardSection attribution_type]
+ -[_SFPBRFReferenceAttributionCardSection clearSources]
+ -[_SFPBRFReferenceAttributionCardSection clearThumbnails]
+ -[_SFPBRFReferenceAttributionCardSection dictionaryRepresentation]
+ -[_SFPBRFReferenceAttributionCardSection expansion_type]
+ -[_SFPBRFReferenceAttributionCardSection hash]
+ -[_SFPBRFReferenceAttributionCardSection initWithDictionary:]
+ -[_SFPBRFReferenceAttributionCardSection initWithJSON:]
+ -[_SFPBRFReferenceAttributionCardSection isEqual:]
+ -[_SFPBRFReferenceAttributionCardSection jsonData]
+ -[_SFPBRFReferenceAttributionCardSection readFrom:]
+ -[_SFPBRFReferenceAttributionCardSection setAdd_tint:]
+ -[_SFPBRFReferenceAttributionCardSection setAttribution_type:]
+ -[_SFPBRFReferenceAttributionCardSection setExpansion_type:]
+ -[_SFPBRFReferenceAttributionCardSection setSources:]
+ -[_SFPBRFReferenceAttributionCardSection setText_1:]
+ -[_SFPBRFReferenceAttributionCardSection setText_2:]
+ -[_SFPBRFReferenceAttributionCardSection setThumbnails:]
+ -[_SFPBRFReferenceAttributionCardSection sourcesAtIndex:]
+ -[_SFPBRFReferenceAttributionCardSection sourcesCount]
+ -[_SFPBRFReferenceAttributionCardSection sources]
+ -[_SFPBRFReferenceAttributionCardSection text_1]
+ -[_SFPBRFReferenceAttributionCardSection text_2]
+ -[_SFPBRFReferenceAttributionCardSection thumbnailsAtIndex:]
+ -[_SFPBRFReferenceAttributionCardSection thumbnailsCount]
+ -[_SFPBRFReferenceAttributionCardSection thumbnails]
+ -[_SFPBRFReferenceAttributionCardSection writeTo:]
+ -[_SFPBRFReferenceAttributionCardSection(FacadeInitializer) initWithFacade:]
+ GCC_except_table2766
+ GCC_except_table6470
+ GCC_except_table8082
+ _OBJC_CLASS_$_RFAttributionSource
+ _OBJC_CLASS_$_RFMarkdownCardSection
+ _OBJC_CLASS_$_RFReferenceAttributionCardSection
+ _OBJC_CLASS_$_SFPasteCommand
+ _OBJC_CLASS_$_SFQuickLookCommand
+ _OBJC_CLASS_$__SFPBPasteCommand
+ _OBJC_CLASS_$__SFPBQuickLookCommand
+ _OBJC_CLASS_$__SFPBRFAttributionSource
+ _OBJC_CLASS_$__SFPBRFMarkdownCardSection
+ _OBJC_CLASS_$__SFPBRFReferenceAttributionCardSection
+ _OBJC_IVAR_$_RFAppIconImage._fallback
+ _OBJC_IVAR_$_RFAttribution._secondary_title
+ _OBJC_IVAR_$_RFAttributionSource._attribution
+ _OBJC_IVAR_$_RFAttributionSource._card_section
+ _OBJC_IVAR_$_RFAttributionSource._has
+ _OBJC_IVAR_$_RFAttributionSource._text_1
+ _OBJC_IVAR_$_RFAttributionSource._thumbnail
+ _OBJC_IVAR_$_RFLongItemStandardCardSection._is_markdown
+ _OBJC_IVAR_$_RFMarkdownCardSection._has
+ _OBJC_IVAR_$_RFMarkdownCardSection._markdown_data
+ _OBJC_IVAR_$_RFMarkdownCardSection._markdown_strings
+ _OBJC_IVAR_$_RFMarkdownCardSection._streaming_state
+ _OBJC_IVAR_$_RFReferenceAttributionCardSection._add_tint
+ _OBJC_IVAR_$_RFReferenceAttributionCardSection._attribution_type
+ _OBJC_IVAR_$_RFReferenceAttributionCardSection._expansion_type
+ _OBJC_IVAR_$_RFReferenceAttributionCardSection._has
+ _OBJC_IVAR_$_RFReferenceAttributionCardSection._sources
+ _OBJC_IVAR_$_RFReferenceAttributionCardSection._text_1
+ _OBJC_IVAR_$_RFReferenceAttributionCardSection._text_2
+ _OBJC_IVAR_$_RFReferenceAttributionCardSection._thumbnails
+ _OBJC_IVAR_$_SFCardSectionValue._rfMarkdownCardSection
+ _OBJC_IVAR_$_SFCardSectionValue._rfReferenceAttributionCardSection
+ _OBJC_IVAR_$_SFPasteCommand._copyableItems
+ _OBJC_IVAR_$_SFQuickLookCommand._url
+ _OBJC_IVAR_$_SFStartLocalSearchFeedback._inputCharCount
+ _OBJC_IVAR_$_SFStartLocalSearchFeedback._inputWordCount
+ _OBJC_IVAR_$__SFPBCardSectionValue._rfMarkdownCardSection
+ _OBJC_IVAR_$__SFPBCardSectionValue._rfReferenceAttributionCardSection
+ _OBJC_IVAR_$__SFPBCommand._pasteCommand
+ _OBJC_IVAR_$__SFPBCommand._quickLookCommand
+ _OBJC_IVAR_$__SFPBPasteCommand._copyableItems
+ _OBJC_IVAR_$__SFPBQuickLookCommand._url
+ _OBJC_IVAR_$__SFPBRFAppIconImage._fallback
+ _OBJC_IVAR_$__SFPBRFAttribution._secondary_title
+ _OBJC_IVAR_$__SFPBRFAttributionSource._attribution
+ _OBJC_IVAR_$__SFPBRFAttributionSource._card_section
+ _OBJC_IVAR_$__SFPBRFAttributionSource._text_1
+ _OBJC_IVAR_$__SFPBRFAttributionSource._thumbnail
+ _OBJC_IVAR_$__SFPBRFAttributionSource._whichSource
+ _OBJC_IVAR_$__SFPBRFLongItemStandardCardSection._is_markdown
+ _OBJC_IVAR_$__SFPBRFMarkdownCardSection._markdown_data
+ _OBJC_IVAR_$__SFPBRFMarkdownCardSection._markdown_strings
+ _OBJC_IVAR_$__SFPBRFMarkdownCardSection._streaming_state
+ _OBJC_IVAR_$__SFPBRFReferenceAttributionCardSection._add_tint
+ _OBJC_IVAR_$__SFPBRFReferenceAttributionCardSection._attribution_type
+ _OBJC_IVAR_$__SFPBRFReferenceAttributionCardSection._expansion_type
+ _OBJC_IVAR_$__SFPBRFReferenceAttributionCardSection._sources
+ _OBJC_IVAR_$__SFPBRFReferenceAttributionCardSection._text_1
+ _OBJC_IVAR_$__SFPBRFReferenceAttributionCardSection._text_2
+ _OBJC_IVAR_$__SFPBRFReferenceAttributionCardSection._thumbnails
+ _OBJC_METACLASS_$_RFAttributionSource
+ _OBJC_METACLASS_$_RFMarkdownCardSection
+ _OBJC_METACLASS_$_RFReferenceAttributionCardSection
+ _OBJC_METACLASS_$_SFPasteCommand
+ _OBJC_METACLASS_$_SFQuickLookCommand
+ _OBJC_METACLASS_$__SFPBPasteCommand
+ _OBJC_METACLASS_$__SFPBQuickLookCommand
+ _OBJC_METACLASS_$__SFPBRFAttributionSource
+ _OBJC_METACLASS_$__SFPBRFMarkdownCardSection
+ _OBJC_METACLASS_$__SFPBRFReferenceAttributionCardSection
+ _PARLogHandleForCategory.logHandles.0.35187
+ _PARLogHandleForCategory.logHandles.0.71726
+ _PARLogHandleForCategory.logHandles.1.35181
+ _PARLogHandleForCategory.logHandles.1.71723
+ _PARLogHandleForCategory.logHandles.2.35189
+ _PARLogHandleForCategory.logHandles.2.71728
+ _PARLogHandleForCategory.logHandles.3.35190
+ _PARLogHandleForCategory.logHandles.3.71729
+ _PARLogHandleForCategory.logHandles.4.35191
+ _PARLogHandleForCategory.logHandles.4.71731
+ _PARLogHandleForCategory.logHandles.5.35192
+ _PARLogHandleForCategory.logHandles.5.71732
+ _PARLogHandleForCategory.onceToken.35179
+ _PARLogHandleForCategory.onceToken.71722
+ __OBJC_$_CLASS_METHODS_RFAttributionSource
+ __OBJC_$_CLASS_METHODS_RFMarkdownCardSection
+ __OBJC_$_CLASS_METHODS_RFReferenceAttributionCardSection
+ __OBJC_$_CLASS_METHODS_SFPasteCommand
+ __OBJC_$_CLASS_METHODS_SFQuickLookCommand
+ __OBJC_$_CLASS_PROP_LIST_RFAttributionSource
+ __OBJC_$_CLASS_PROP_LIST_RFMarkdownCardSection
+ __OBJC_$_CLASS_PROP_LIST_RFReferenceAttributionCardSection
+ __OBJC_$_CLASS_PROP_LIST_SFPasteCommand
+ __OBJC_$_CLASS_PROP_LIST_SFQuickLookCommand
+ __OBJC_$_CLASS_PROP_LIST__SFPBPasteCommand
+ __OBJC_$_CLASS_PROP_LIST__SFPBQuickLookCommand
+ __OBJC_$_CLASS_PROP_LIST__SFPBRFAttributionSource
+ __OBJC_$_CLASS_PROP_LIST__SFPBRFMarkdownCardSection
+ __OBJC_$_CLASS_PROP_LIST__SFPBRFReferenceAttributionCardSection
+ __OBJC_$_INSTANCE_METHODS_RFAttributionSource(ProtobufInitializer)
+ __OBJC_$_INSTANCE_METHODS_RFMarkdownCardSection(ProtobufInitializer)
+ __OBJC_$_INSTANCE_METHODS_RFReferenceAttributionCardSection(ProtobufInitializer)
+ __OBJC_$_INSTANCE_METHODS_SFPasteCommand(ProtobufInitializer)
+ __OBJC_$_INSTANCE_METHODS_SFQuickLookCommand(ProtobufInitializer)
+ __OBJC_$_INSTANCE_METHODS__SFPBPasteCommand(FacadeInitializer)
+ __OBJC_$_INSTANCE_METHODS__SFPBQuickLookCommand(FacadeInitializer)
+ __OBJC_$_INSTANCE_METHODS__SFPBRFAttributionSource(FacadeInitializer)
+ __OBJC_$_INSTANCE_METHODS__SFPBRFMarkdownCardSection(FacadeInitializer)
+ __OBJC_$_INSTANCE_METHODS__SFPBRFReferenceAttributionCardSection(FacadeInitializer)
+ __OBJC_$_INSTANCE_VARIABLES_RFAttributionSource
+ __OBJC_$_INSTANCE_VARIABLES_RFMarkdownCardSection
+ __OBJC_$_INSTANCE_VARIABLES_RFReferenceAttributionCardSection
+ __OBJC_$_INSTANCE_VARIABLES_SFPasteCommand
+ __OBJC_$_INSTANCE_VARIABLES_SFQuickLookCommand
+ __OBJC_$_INSTANCE_VARIABLES__SFPBPasteCommand
+ __OBJC_$_INSTANCE_VARIABLES__SFPBQuickLookCommand
+ __OBJC_$_INSTANCE_VARIABLES__SFPBRFAttributionSource
+ __OBJC_$_INSTANCE_VARIABLES__SFPBRFMarkdownCardSection
+ __OBJC_$_INSTANCE_VARIABLES__SFPBRFReferenceAttributionCardSection
+ __OBJC_$_PROP_LIST_RFAppIconImage.94
+ __OBJC_$_PROP_LIST_RFAttribution.132
+ __OBJC_$_PROP_LIST_RFAttributionSource
+ __OBJC_$_PROP_LIST_RFAttributionSource.107
+ __OBJC_$_PROP_LIST_RFLongItemStandardCardSection.259
+ __OBJC_$_PROP_LIST_RFMarkdownCardSection
+ __OBJC_$_PROP_LIST_RFMarkdownCardSection.245
+ __OBJC_$_PROP_LIST_RFReferenceAttributionCardSection
+ __OBJC_$_PROP_LIST_RFReferenceAttributionCardSection.267
+ __OBJC_$_PROP_LIST_SFCardSectionValue.1085
+ __OBJC_$_PROP_LIST_SFPasteCommand
+ __OBJC_$_PROP_LIST_SFPasteCommand.105
+ __OBJC_$_PROP_LIST_SFQuickLookCommand
+ __OBJC_$_PROP_LIST_SFQuickLookCommand.105
+ __OBJC_$_PROP_LIST__SFPBCardSectionValue.3386
+ __OBJC_$_PROP_LIST__SFPBClearProactiveCategoryCommand.3417
+ __OBJC_$_PROP_LIST__SFPBClockImage.3447
+ __OBJC_$_PROP_LIST__SFPBCloudChannelsRequestItem.3478
+ __OBJC_$_PROP_LIST__SFPBCollectionCardSection.3515
+ __OBJC_$_PROP_LIST__SFPBCollectionStyle.3573
+ __OBJC_$_PROP_LIST__SFPBCollectionStyleGrid.3595
+ __OBJC_$_PROP_LIST__SFPBCollectionStyleHorizontallyScrolling.3609
+ __OBJC_$_PROP_LIST__SFPBCollectionStyleRow.3639
+ __OBJC_$_PROP_LIST__SFPBColor.3759
+ __OBJC_$_PROP_LIST__SFPBColorBarCardSection.3782
+ __OBJC_$_PROP_LIST__SFPBCombinedCardSection.3789
+ __OBJC_$_PROP_LIST__SFPBCommand.4605
+ __OBJC_$_PROP_LIST__SFPBCommandButtonItem.4620
+ __OBJC_$_PROP_LIST__SFPBCommandReference.4635
+ __OBJC_$_PROP_LIST__SFPBCommandRowCardSection.4658
+ __OBJC_$_PROP_LIST__SFPBCommandValue.4678
+ __OBJC_$_PROP_LIST__SFPBCompactRowCardSection.4693
+ __OBJC_$_PROP_LIST__SFPBContactButtonItem.4727
+ __OBJC_$_PROP_LIST__SFPBContactCopyItem.4742
+ __OBJC_$_PROP_LIST__SFPBContactImage.4777
+ __OBJC_$_PROP_LIST__SFPBCopyCommand.4795
+ __OBJC_$_PROP_LIST__SFPBCopyItem.4867
+ __OBJC_$_PROP_LIST__SFPBCoreSpotlightButtonItem.4894
+ __OBJC_$_PROP_LIST__SFPBCoreSpotlightCopyItem.4925
+ __OBJC_$_PROP_LIST__SFPBCoreSpotlightRankingSignals.5063
+ __OBJC_$_PROP_LIST__SFPBCoreSpotlightShareItem.5078
+ __OBJC_$_PROP_LIST__SFPBCreateCalendarEventCommand.5098
+ __OBJC_$_PROP_LIST__SFPBCreateContactCommand.5113
+ __OBJC_$_PROP_LIST__SFPBCreateReminderCommand.5133
+ __OBJC_$_PROP_LIST__SFPBDate.5147
+ __OBJC_$_PROP_LIST__SFPBDefaultPunchoutAppIconImage.5162
+ __OBJC_$_PROP_LIST__SFPBDescriptionCardSection.5275
+ __OBJC_$_PROP_LIST__SFPBDetailedRowCardSection.5449
+ __OBJC_$_PROP_LIST__SFPBDomainEngagementScore.5487
+ __OBJC_$_PROP_LIST__SFPBDomainSubscriptionRequestItem.5507
+ __OBJC_$_PROP_LIST__SFPBDrillDownMetadata.5614
+ __OBJC_$_PROP_LIST__SFPBDynamicURLImageResource.5668
+ __OBJC_$_PROP_LIST__SFPBEmailCommand.5675
+ __OBJC_$_PROP_LIST__SFPBEmbeddingState.5759
+ __OBJC_$_PROP_LIST__SFPBEngagementSignal.5821
+ __OBJC_$_PROP_LIST__SFPBEntitySearchMetadata.5845
+ __OBJC_$_PROP_LIST__SFPBExecuteMenuItemCommand.5860
+ __OBJC_$_PROP_LIST__SFPBExecuteToolCommand.5883
+ __OBJC_$_PROP_LIST__SFPBExpandInlineCommand.5897
+ __OBJC_$_PROP_LIST__SFPBFillToolAppEntityParameterCommand.5920
+ __OBJC_$_PROP_LIST__SFPBFillToolAppParameterCommand.5935
+ __OBJC_$_PROP_LIST__SFPBFillToolFileParameterCommand.5950
+ __OBJC_$_PROP_LIST__SFPBFillToolParameterCommand.5957
+ __OBJC_$_PROP_LIST__SFPBFillToolPersonParameterCommand.5964
+ __OBJC_$_PROP_LIST__SFPBFindMyCardSection.5971
+ __OBJC_$_PROP_LIST__SFPBFlight.6057
+ __OBJC_$_PROP_LIST__SFPBFlightCardSection.6083
+ __OBJC_$_PROP_LIST__SFPBFlightCheckinCommand.6089
+ __OBJC_$_PROP_LIST__SFPBFlightDateDescriptor.6120
+ __OBJC_$_PROP_LIST__SFPBFlightDetails.6134
+ __OBJC_$_PROP_LIST__SFPBFlightLeg.6340
+ __OBJC_$_PROP_LIST__SFPBFormattedText.6388
+ __OBJC_$_PROP_LIST__SFPBGradientColor.6416
+ __OBJC_$_PROP_LIST__SFPBGraphicalFloat.6430
+ __OBJC_$_PROP_LIST__SFPBGridCardSection.6437
+ __OBJC_$_PROP_LIST__SFPBHashBucketDetail.6467
+ __OBJC_$_PROP_LIST__SFPBHashBucketDetail_HashDetail.6518
+ __OBJC_$_PROP_LIST__SFPBHeroCardSection.6525
+ __OBJC_$_PROP_LIST__SFPBHeroTitleCardSection.6540
+ __OBJC_$_PROP_LIST__SFPBHorizontalButtonCardSection.6559
+ __OBJC_$_PROP_LIST__SFPBHorizontalScrollCardSection.6566
+ __OBJC_$_PROP_LIST__SFPBImage.6870
+ __OBJC_$_PROP_LIST__SFPBImageCopyItem.6877
+ __OBJC_$_PROP_LIST__SFPBImageDerivedColor.6884
+ __OBJC_$_PROP_LIST__SFPBImageOption.6912
+ __OBJC_$_PROP_LIST__SFPBImagesCardSection.6940
+ __OBJC_$_PROP_LIST__SFPBIndexState.7002
+ __OBJC_$_PROP_LIST__SFPBIndexedUserActivityCommand.7017
+ __OBJC_$_PROP_LIST__SFPBInfoCardSection.7047
+ __OBJC_$_PROP_LIST__SFPBInfoTuple.7091
+ __OBJC_$_PROP_LIST__SFPBInvokeSiriCommand.7114
+ __OBJC_$_PROP_LIST__SFPBKeyValueDataCardSection.7145
+ __OBJC_$_PROP_LIST__SFPBKeyValueTuple.7153
+ __OBJC_$_PROP_LIST__SFPBLargeTitleDetailedRowCardSection.7183
+ __OBJC_$_PROP_LIST__SFPBLatLng.7205
+ __OBJC_$_PROP_LIST__SFPBLaunchAppCommand.7220
+ __OBJC_$_PROP_LIST__SFPBLeadingTrailingCardSection.7259
+ __OBJC_$_PROP_LIST__SFPBLinkPresentationCardSection.7289
+ __OBJC_$_PROP_LIST__SFPBListenToCardSection.7320
+ __OBJC_$_PROP_LIST__SFPBLocalImage.7334
+ __OBJC_$_PROP_LIST__SFPBLocationTypeInfo.7349
+ __OBJC_$_PROP_LIST__SFPBMailRankingSignals.7883
+ __OBJC_$_PROP_LIST__SFPBMailResultDetails.7913
+ __OBJC_$_PROP_LIST__SFPBManageReservationCommand.7919
+ __OBJC_$_PROP_LIST__SFPBMapCardSection.7995
+ __OBJC_$_PROP_LIST__SFPBMapPlaceCardSection.8010
+ __OBJC_$_PROP_LIST__SFPBMapRegion.8056
+ __OBJC_$_PROP_LIST__SFPBMapsDetailedRowCardSection.8071
+ __OBJC_$_PROP_LIST__SFPBMediaArtworkImage.8086
+ __OBJC_$_PROP_LIST__SFPBMediaDetail.8101
+ __OBJC_$_PROP_LIST__SFPBMediaInfoCardSection.8215
+ __OBJC_$_PROP_LIST__SFPBMediaItem.8295
+ __OBJC_$_PROP_LIST__SFPBMediaMetadata.8375
+ __OBJC_$_PROP_LIST__SFPBMediaOffer.8414
+ __OBJC_$_PROP_LIST__SFPBMediaPlayerCardSection.8434
+ __OBJC_$_PROP_LIST__SFPBMediaRemoteControlCardSection.8465
+ __OBJC_$_PROP_LIST__SFPBMessageAttachment.8480
+ __OBJC_$_PROP_LIST__SFPBMessageCardSection.8532
+ __OBJC_$_PROP_LIST__SFPBMetaInfoCardSection.8571
+ __OBJC_$_PROP_LIST__SFPBMiniCardSection.8578
+ __OBJC_$_PROP_LIST__SFPBMonogramImage.8601
+ __OBJC_$_PROP_LIST__SFPBMoreResults.8608
+ __OBJC_$_PROP_LIST__SFPBNamedProtobufMessage.8631
+ __OBJC_$_PROP_LIST__SFPBNewsCardSection.8662
+ __OBJC_$_PROP_LIST__SFPBNowPlayingCardSection.8681
+ __OBJC_$_PROP_LIST__SFPBOpenAppClipCommand.8696
+ __OBJC_$_PROP_LIST__SFPBOpenCalculationCommand.8727
+ __OBJC_$_PROP_LIST__SFPBOpenCoreSpotlightItemCommand.8742
+ __OBJC_$_PROP_LIST__SFPBOpenFileProviderItemCommand.8757
+ __OBJC_$_PROP_LIST__SFPBOpenMediaCommand.8772
+ __OBJC_$_PROP_LIST__SFPBOpenPunchoutCommand.8779
+ __OBJC_$_PROP_LIST__SFPBOpenWebClipCommand.8786
+ __OBJC_$_PROP_LIST__SFPBPasteCommand
+ __OBJC_$_PROP_LIST__SFPBPasteCommand.8793
+ __OBJC_$_PROP_LIST__SFPBPatternModel.8832
+ __OBJC_$_PROP_LIST__SFPBPegasusDisplayFields.8863
+ __OBJC_$_PROP_LIST__SFPBPerformContactActionCommand.8893
+ __OBJC_$_PROP_LIST__SFPBPerformContactQueryCommand.8900
+ __OBJC_$_PROP_LIST__SFPBPerformEntityQueryCommand.8971
+ __OBJC_$_PROP_LIST__SFPBPerformIntentCommand.8994
+ __OBJC_$_PROP_LIST__SFPBPerformPersonEntityQueryCommand.9001
+ __OBJC_$_PROP_LIST__SFPBPerson.9056
+ __OBJC_$_PROP_LIST__SFPBPersonHeaderCardSection.9063
+ __OBJC_$_PROP_LIST__SFPBPhotosAggregatedInfo.9093
+ __OBJC_$_PROP_LIST__SFPBPhotosAlbumImage.9108
+ __OBJC_$_PROP_LIST__SFPBPhotosAttributes.9162
+ __OBJC_$_PROP_LIST__SFPBPhotosLibraryImage.9198
+ __OBJC_$_PROP_LIST__SFPBPhotosMemoryImage.9213
+ __OBJC_$_PROP_LIST__SFPBPhotosRankingInfo.9291
+ __OBJC_$_PROP_LIST__SFPBPin.9306
+ __OBJC_$_PROP_LIST__SFPBPlayAudioButtonItem.9339
+ __OBJC_$_PROP_LIST__SFPBPlayMediaCommand.9362
+ __OBJC_$_PROP_LIST__SFPBPlayVideoCommand.9369
+ __OBJC_$_PROP_LIST__SFPBPlayWatchListItemButtonItem.9389
+ __OBJC_$_PROP_LIST__SFPBPointSize.9412
+ __OBJC_$_PROP_LIST__SFPBProduct.9443
+ __OBJC_$_PROP_LIST__SFPBProductAvailability.9465
+ __OBJC_$_PROP_LIST__SFPBProductCardSection.9480
+ __OBJC_$_PROP_LIST__SFPBProductInventory.9536
+ __OBJC_$_PROP_LIST__SFPBProductInventoryResult.9559
+ __OBJC_$_PROP_LIST__SFPBPunchout.9624
+ __OBJC_$_PROP_LIST__SFPBQueryUnderstandingParse.9782
+ __OBJC_$_PROP_LIST__SFPBQuickLookCommand
+ __OBJC_$_PROP_LIST__SFPBQuickLookCommand.9789
+ __OBJC_$_PROP_LIST__SFPBQuickLookThumbnailImage.9797
+ __OBJC_$_PROP_LIST__SFPBRFAppIconImage.9825
+ __OBJC_$_PROP_LIST__SFPBRFAspectRatio.9833
+ __OBJC_$_PROP_LIST__SFPBRFAttribution.9890
+ __OBJC_$_PROP_LIST__SFPBRFAttributionSource
+ __OBJC_$_PROP_LIST__SFPBRFAttributionSource.9931
+ __OBJC_$_PROP_LIST__SFPBRFAvatarImage.9950
+ __OBJC_$_PROP_LIST__SFPBRFBadgedImage.9964
+ __OBJC_$_PROP_LIST__SFPBRFBinaryButtonCardSection.9987
+ __OBJC_$_PROP_LIST__SFPBRFButtonCardSection.9995
+ __OBJC_$_PROP_LIST__SFPBRFColor.10029
+ __OBJC_$_PROP_LIST__SFPBRFDefaultBrowserAppIconImage.10035
+ __OBJC_$_PROP_LIST__SFPBRFDisambiguationTitleCardSection.10043
+ __OBJC_$_PROP_LIST__SFPBRFEngageable.10072
+ __OBJC_$_PROP_LIST__SFPBRFExpandableStandardCardSection.10107
+ __OBJC_$_PROP_LIST__SFPBRFExpandingComponentContent.10130
+ __OBJC_$_PROP_LIST__SFPBRFFactItemButtonCardSection.10215
+ __OBJC_$_PROP_LIST__SFPBRFFactItemDetailedNumberCardSection.10234
+ __OBJC_$_PROP_LIST__SFPBRFFactItemHeroButtonCardSection.10241
+ __OBJC_$_PROP_LIST__SFPBRFFactItemHeroNumberCardSection.10274
+ __OBJC_$_PROP_LIST__SFPBRFFactItemImageRightCardSection.10281
+ __OBJC_$_PROP_LIST__SFPBRFFactItemShortHeroNumberCardSection.10288
+ __OBJC_$_PROP_LIST__SFPBRFFactItemShortNumberCardSection.10295
+ __OBJC_$_PROP_LIST__SFPBRFFactItemStandardCardSection.10311
+ __OBJC_$_PROP_LIST__SFPBRFFont.10339
+ __OBJC_$_PROP_LIST__SFPBRFFont_RFSystemFont.11542
+ __OBJC_$_PROP_LIST__SFPBRFFormattedText.10491
+ __OBJC_$_PROP_LIST__SFPBRFHighlightedSubstring.10506
+ __OBJC_$_PROP_LIST__SFPBRFImageElement.10526
+ __OBJC_$_PROP_LIST__SFPBRFImageSource.10625
+ __OBJC_$_PROP_LIST__SFPBRFLongItemStandardCardSection.10664
+ __OBJC_$_PROP_LIST__SFPBRFMapAnnotation.10694
+ __OBJC_$_PROP_LIST__SFPBRFMapCardSection.10761
+ __OBJC_$_PROP_LIST__SFPBRFMapMarker.10794
+ __OBJC_$_PROP_LIST__SFPBRFMapMarkerIdentifier.10825
+ __OBJC_$_PROP_LIST__SFPBRFMapMarkerImage.10840
+ __OBJC_$_PROP_LIST__SFPBRFMapMarkerText.10848
+ __OBJC_$_PROP_LIST__SFPBRFMapPoint.10870
+ __OBJC_$_PROP_LIST__SFPBRFMarkdownCardSection
+ __OBJC_$_PROP_LIST__SFPBRFMarkdownCardSection.10908
+ __OBJC_$_PROP_LIST__SFPBRFMonogramImage.10923
+ __OBJC_$_PROP_LIST__SFPBRFMultiButtonCardSection.10938
+ __OBJC_$_PROP_LIST__SFPBRFOptionalBool.10945
+ __OBJC_$_PROP_LIST__SFPBRFOptionalFloat.10952
+ __OBJC_$_PROP_LIST__SFPBRFPreview.10959
+ __OBJC_$_PROP_LIST__SFPBRFPreviewList.10981
+ __OBJC_$_PROP_LIST__SFPBRFPrimaryHeaderMarqueeCardSection.10996
+ __OBJC_$_PROP_LIST__SFPBRFPrimaryHeaderRichCardSection.11003
+ __OBJC_$_PROP_LIST__SFPBRFPrimaryHeaderStackedImageCardSection.11011
+ __OBJC_$_PROP_LIST__SFPBRFPrimaryHeaderStandardCardSection.11018
+ __OBJC_$_PROP_LIST__SFPBRFRGBValue.11048
+ __OBJC_$_PROP_LIST__SFPBRFReferenceAttributionCardSection
+ __OBJC_$_PROP_LIST__SFPBRFReferenceAttributionCardSection.11092
+ __OBJC_$_PROP_LIST__SFPBRFReferenceCenteredCardSection.11099
+ __OBJC_$_PROP_LIST__SFPBRFReferenceFootnoteCardSection.11106
+ __OBJC_$_PROP_LIST__SFPBRFReferenceItemButtonCardSection.11113
+ __OBJC_$_PROP_LIST__SFPBRFReferenceItemLogoCardSection.11120
+ __OBJC_$_PROP_LIST__SFPBRFReferenceRichCardSection.11127
+ __OBJC_$_PROP_LIST__SFPBRFReferenceStandardCardSection.11134
+ __OBJC_$_PROP_LIST__SFPBRFSecondaryHeaderEmphasizedCardSection.11141
+ __OBJC_$_PROP_LIST__SFPBRFSecondaryHeaderStandardCardSection.11148
+ __OBJC_$_PROP_LIST__SFPBRFShowMoreOnTap.11171
+ __OBJC_$_PROP_LIST__SFPBRFSimpleItemPlayerCardSection.11186
+ __OBJC_$_PROP_LIST__SFPBRFSimpleItemReverseRichCardSection.11193
+ __OBJC_$_PROP_LIST__SFPBRFSimpleItemRichCardSection.11224
+ __OBJC_$_PROP_LIST__SFPBRFSimpleItemRichSearchResultCardSection.11231
+ __OBJC_$_PROP_LIST__SFPBRFSimpleItemStandardCardSection.11238
+ __OBJC_$_PROP_LIST__SFPBRFSimpleItemVisualElementCardSection.11262
+ __OBJC_$_PROP_LIST__SFPBRFSummaryItemAlignedTextCardSection.11278
+ __OBJC_$_PROP_LIST__SFPBRFSummaryItemAttribution.11302
+ __OBJC_$_PROP_LIST__SFPBRFSummaryItemButtonCardSection.11309
+ __OBJC_$_PROP_LIST__SFPBRFSummaryItemDetailedTextCardSection.11316
+ __OBJC_$_PROP_LIST__SFPBRFSummaryItemExpandableCardSection.11348
+ __OBJC_$_PROP_LIST__SFPBRFSummaryItemExpandableContent.11363
+ __OBJC_$_PROP_LIST__SFPBRFSummaryItemImageRightCardSection.11383
+ __OBJC_$_PROP_LIST__SFPBRFSummaryItemPairCardSection.11390
+ __OBJC_$_PROP_LIST__SFPBRFSummaryItemPairNumberCardSection.11429
+ __OBJC_$_PROP_LIST__SFPBRFSummaryItemPlayerCardSection.11436
+ __OBJC_$_PROP_LIST__SFPBRFSummaryItemShortNumberCardSection.11443
+ __OBJC_$_PROP_LIST__SFPBRFSummaryItemStandardCardSection.11458
+ __OBJC_$_PROP_LIST__SFPBRFSummaryItemSwitchV2CardSection.11473
+ __OBJC_$_PROP_LIST__SFPBRFSummaryItemTextCardSection.11480
+ __OBJC_$_PROP_LIST__SFPBRFSymbolImage.11535
+ __OBJC_$_PROP_LIST__SFPBRFTableCell.11569
+ __OBJC_$_PROP_LIST__SFPBRFTableColumnDefinition.11599
+ __OBJC_$_PROP_LIST__SFPBRFTableContentColumnDefinition.11645
+ __OBJC_$_PROP_LIST__SFPBRFTableHeaderCardSection.11710
+ __OBJC_$_PROP_LIST__SFPBRFTableRowCardSection.11725
+ __OBJC_$_PROP_LIST__SFPBRFTableSpacerColumnDefinition.11731
+ __OBJC_$_PROP_LIST__SFPBRFTextElement.11775
+ __OBJC_$_PROP_LIST__SFPBRFTextEncapsulation.11781
+ __OBJC_$_PROP_LIST__SFPBRFTextProperty.11811
+ __OBJC_$_PROP_LIST__SFPBRFUrlImage.11875
+ __OBJC_$_PROP_LIST__SFPBRFVisualElement.11894
+ __OBJC_$_PROP_LIST__SFPBRFVisualProperty.11916
+ __OBJC_$_PROP_LIST__SFPBRFVisualPropertyWithAction.11931
+ __OBJC_$_PROP_LIST__SFPBReferentialCommand.11938
+ __OBJC_$_PROP_LIST__SFPBRejectPeopleInPhotoCommand.11958
+ __OBJC_$_PROP_LIST__SFPBReminder.11973
+ __OBJC_$_PROP_LIST__SFPBRequestAppClipInstallCommand.11980
+ __OBJC_$_PROP_LIST__SFPBRequestProductPageCommand.12011
+ __OBJC_$_PROP_LIST__SFPBRequestUserReportCommand.12018
+ __OBJC_$_PROP_LIST__SFPBResponseWrapperCardSection.12072
+ __OBJC_$_PROP_LIST__SFPBResultEntity.12100
+ __OBJC_$_PROP_LIST__SFPBRichText.12140
+ __OBJC_$_PROP_LIST__SFPBRichTitleCardSection.12288
+ __OBJC_$_PROP_LIST__SFPBRowCardSection.12383
+ __OBJC_$_PROP_LIST__SFPBRunVoiceShortcutCommand.12398
+ __OBJC_$_PROP_LIST__SFPBSafariAttributes.12412
+ __OBJC_$_PROP_LIST__SFPBSafariTableOfContentsCardSection.12458
+ __OBJC_$_PROP_LIST__SFPBSafariTableOfContentsItem.12474
+ __OBJC_$_PROP_LIST__SFPBScene.12496
+ __OBJC_$_PROP_LIST__SFPBScoreboardCardSection.12540
+ __OBJC_$_PROP_LIST__SFPBSearchInAppCommand.12555
+ __OBJC_$_PROP_LIST__SFPBSearchSuggestion.12633
+ __OBJC_$_PROP_LIST__SFPBSearchWebCommand.12640
+ __OBJC_$_PROP_LIST__SFPBSectionHeaderCardSection.12648
+ __OBJC_$_PROP_LIST__SFPBSelectableGridCardSection.12678
+ __OBJC_$_PROP_LIST__SFPBShareCommand.12711
+ __OBJC_$_PROP_LIST__SFPBShareItem.12744
+ __OBJC_$_PROP_LIST__SFPBShortcutsImage.12759
+ __OBJC_$_PROP_LIST__SFPBShowAppStoreSheetCommand.12774
+ __OBJC_$_PROP_LIST__SFPBShowContactCardCommand.12789
+ __OBJC_$_PROP_LIST__SFPBShowPhotosOneUpViewCommand.12840
+ __OBJC_$_PROP_LIST__SFPBShowPurchaseRequestSheetCommand.12855
+ __OBJC_$_PROP_LIST__SFPBShowSFCardCommand.12870
+ __OBJC_$_PROP_LIST__SFPBShowScreenTimeRequestSheetCommand.12877
+ __OBJC_$_PROP_LIST__SFPBShowWrapperResponseViewCommand.12884
+ __OBJC_$_PROP_LIST__SFPBSocialMediaPostCardSection.12948
+ __OBJC_$_PROP_LIST__SFPBSplitCardSection.13015
+ __OBJC_$_PROP_LIST__SFPBSportsDetail.13030
+ __OBJC_$_PROP_LIST__SFPBSportsFollowButtonItem.13058
+ __OBJC_$_PROP_LIST__SFPBSportsItem.13065
+ __OBJC_$_PROP_LIST__SFPBSportsSubscriptionRequestItem.13096
+ __OBJC_$_PROP_LIST__SFPBSportsTeam.13128
+ __OBJC_$_PROP_LIST__SFPBSpotlightEmbeddingState.13158
+ __OBJC_$_PROP_LIST__SFPBStockChartCardSection.13181
+ __OBJC_$_PROP_LIST__SFPBStoreButtonItem.13204
+ __OBJC_$_PROP_LIST__SFPBStringDictionary.13223
+ __OBJC_$_PROP_LIST__SFPBStrokeAnimationCardSection.13274
+ __OBJC_$_PROP_LIST__SFPBStructuredLocation.13297
+ __OBJC_$_PROP_LIST__SFPBSubscribeForUpdatesCommand.13330
+ __OBJC_$_PROP_LIST__SFPBSuggestionCardSection.13369
+ __OBJC_$_PROP_LIST__SFPBSymbolImage.13411
+ __OBJC_$_PROP_LIST__SFPBTableAlignmentSchema.13435
+ __OBJC_$_PROP_LIST__SFPBTableColumnAlignment.13465
+ __OBJC_$_PROP_LIST__SFPBTableHeaderRowCardSection.13533
+ __OBJC_$_PROP_LIST__SFPBTableRowCardSection.13553
+ __OBJC_$_PROP_LIST__SFPBText.13570
+ __OBJC_$_PROP_LIST__SFPBTextColumn.13592
+ __OBJC_$_PROP_LIST__SFPBTextColumnSection.13627
+ __OBJC_$_PROP_LIST__SFPBTextColumnsCardSection.13638
+ __OBJC_$_PROP_LIST__SFPBTextCopyItem.13653
+ __OBJC_$_PROP_LIST__SFPBTimeZone.13660
+ __OBJC_$_PROP_LIST__SFPBTitleCardSection.13667
+ __OBJC_$_PROP_LIST__SFPBTitleSubtitleTuple.13674
+ __OBJC_$_PROP_LIST__SFPBToggleAudioCommand.13697
+ __OBJC_$_PROP_LIST__SFPBToggleButtonConfiguration.13721
+ __OBJC_$_PROP_LIST__SFPBToggleWatchListStatusCommand.13736
+ __OBJC_$_PROP_LIST__SFPBTopic.13779
+ __OBJC_$_PROP_LIST__SFPBTrack.13811
+ __OBJC_$_PROP_LIST__SFPBTrackListCardSection.13833
+ __OBJC_$_PROP_LIST__SFPBURL.13840
+ __OBJC_$_PROP_LIST__SFPBURLCopyItem.13847
+ __OBJC_$_PROP_LIST__SFPBURLImage.13862
+ __OBJC_$_PROP_LIST__SFPBURLShareItem.13869
+ __OBJC_$_PROP_LIST__SFPBUpdateSearchQueryCommand.13884
+ __OBJC_$_PROP_LIST__SFPBUpdateSportsFollowingStatusCommand.13899
+ __OBJC_$_PROP_LIST__SFPBUserActivityData.13930
+ __OBJC_$_PROP_LIST__SFPBUserActivityInfo.13953
+ __OBJC_$_PROP_LIST__SFPBUserReportRequest.14028
+ __OBJC_$_PROP_LIST__SFPBVerticalLayoutCardSection.14059
+ __OBJC_$_PROP_LIST__SFPBViewEmailCommand.14065
+ __OBJC_$_PROP_LIST__SFPBWatchListButtonItem.14072
+ __OBJC_$_PROP_LIST__SFPBWatchListCardSection.14079
+ __OBJC_$_PROP_LIST__SFPBWatchListItem.14158
+ __OBJC_$_PROP_LIST__SFPBWatchNowCardSection.14172
+ __OBJC_$_PROP_LIST__SFPBWeatherColor.14219
+ __OBJC_$_PROP_LIST__SFPBWeatherDetails.14226
+ __OBJC_$_PROP_LIST__SFPBWebCardSection.14241
+ __OBJC_$_PROP_LIST__SFPBWorldMapCardSection.14264
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_RFAttributionSource
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_RFMarkdownCardSection
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_RFReferenceAttributionCardSection
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SFPasteCommand
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SFQuickLookCommand
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__SFPBPasteCommand
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__SFPBQuickLookCommand
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__SFPBRFAttributionSource
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__SFPBRFMarkdownCardSection
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__SFPBRFReferenceAttributionCardSection
+ __OBJC_$_PROTOCOL_METHOD_TYPES_RFAttributionSource
+ __OBJC_$_PROTOCOL_METHOD_TYPES_RFMarkdownCardSection
+ __OBJC_$_PROTOCOL_METHOD_TYPES_RFReferenceAttributionCardSection
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SFPasteCommand
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SFQuickLookCommand
+ __OBJC_$_PROTOCOL_METHOD_TYPES__SFPBPasteCommand
+ __OBJC_$_PROTOCOL_METHOD_TYPES__SFPBQuickLookCommand
+ __OBJC_$_PROTOCOL_METHOD_TYPES__SFPBRFAttributionSource
+ __OBJC_$_PROTOCOL_METHOD_TYPES__SFPBRFMarkdownCardSection
+ __OBJC_$_PROTOCOL_METHOD_TYPES__SFPBRFReferenceAttributionCardSection
+ __OBJC_$_PROTOCOL_REFS_RFAttributionSource
+ __OBJC_$_PROTOCOL_REFS_RFMarkdownCardSection
+ __OBJC_$_PROTOCOL_REFS_RFReferenceAttributionCardSection
+ __OBJC_$_PROTOCOL_REFS_SFPasteCommand
+ __OBJC_$_PROTOCOL_REFS_SFQuickLookCommand
+ __OBJC_$_PROTOCOL_REFS__SFPBPasteCommand
+ __OBJC_$_PROTOCOL_REFS__SFPBQuickLookCommand
+ __OBJC_$_PROTOCOL_REFS__SFPBRFAttributionSource
+ __OBJC_$_PROTOCOL_REFS__SFPBRFMarkdownCardSection
+ __OBJC_$_PROTOCOL_REFS__SFPBRFReferenceAttributionCardSection
+ __OBJC_CLASS_PROTOCOLS_$_RFAttributionSource
+ __OBJC_CLASS_PROTOCOLS_$_RFMarkdownCardSection
+ __OBJC_CLASS_PROTOCOLS_$_RFReferenceAttributionCardSection
+ __OBJC_CLASS_PROTOCOLS_$_SFPasteCommand
+ __OBJC_CLASS_PROTOCOLS_$_SFQuickLookCommand
+ __OBJC_CLASS_PROTOCOLS_$__SFPBPasteCommand
+ __OBJC_CLASS_PROTOCOLS_$__SFPBQuickLookCommand
+ __OBJC_CLASS_PROTOCOLS_$__SFPBRFAttributionSource
+ __OBJC_CLASS_PROTOCOLS_$__SFPBRFMarkdownCardSection
+ __OBJC_CLASS_PROTOCOLS_$__SFPBRFReferenceAttributionCardSection
+ __OBJC_CLASS_RO_$_RFAttributionSource
+ __OBJC_CLASS_RO_$_RFMarkdownCardSection
+ __OBJC_CLASS_RO_$_RFReferenceAttributionCardSection
+ __OBJC_CLASS_RO_$_SFPasteCommand
+ __OBJC_CLASS_RO_$_SFQuickLookCommand
+ __OBJC_CLASS_RO_$__SFPBPasteCommand
+ __OBJC_CLASS_RO_$__SFPBQuickLookCommand
+ __OBJC_CLASS_RO_$__SFPBRFAttributionSource
+ __OBJC_CLASS_RO_$__SFPBRFMarkdownCardSection
+ __OBJC_CLASS_RO_$__SFPBRFReferenceAttributionCardSection
+ __OBJC_LABEL_PROTOCOL_$_RFAttributionSource
+ __OBJC_LABEL_PROTOCOL_$_RFMarkdownCardSection
+ __OBJC_LABEL_PROTOCOL_$_RFReferenceAttributionCardSection
+ __OBJC_LABEL_PROTOCOL_$_SFPasteCommand
+ __OBJC_LABEL_PROTOCOL_$_SFQuickLookCommand
+ __OBJC_LABEL_PROTOCOL_$__SFPBPasteCommand
+ __OBJC_LABEL_PROTOCOL_$__SFPBQuickLookCommand
+ __OBJC_LABEL_PROTOCOL_$__SFPBRFAttributionSource
+ __OBJC_LABEL_PROTOCOL_$__SFPBRFMarkdownCardSection
+ __OBJC_LABEL_PROTOCOL_$__SFPBRFReferenceAttributionCardSection
+ __OBJC_METACLASS_RO_$_RFAttributionSource
+ __OBJC_METACLASS_RO_$_RFMarkdownCardSection
+ __OBJC_METACLASS_RO_$_RFReferenceAttributionCardSection
+ __OBJC_METACLASS_RO_$_SFPasteCommand
+ __OBJC_METACLASS_RO_$_SFQuickLookCommand
+ __OBJC_METACLASS_RO_$__SFPBPasteCommand
+ __OBJC_METACLASS_RO_$__SFPBQuickLookCommand
+ __OBJC_METACLASS_RO_$__SFPBRFAttributionSource
+ __OBJC_METACLASS_RO_$__SFPBRFMarkdownCardSection
+ __OBJC_METACLASS_RO_$__SFPBRFReferenceAttributionCardSection
+ __OBJC_PROTOCOL_$_RFAttributionSource
+ __OBJC_PROTOCOL_$_RFMarkdownCardSection
+ __OBJC_PROTOCOL_$_RFReferenceAttributionCardSection
+ __OBJC_PROTOCOL_$_SFPasteCommand
+ __OBJC_PROTOCOL_$_SFQuickLookCommand
+ __OBJC_PROTOCOL_$__SFPBPasteCommand
+ __OBJC_PROTOCOL_$__SFPBQuickLookCommand
+ __OBJC_PROTOCOL_$__SFPBRFAttributionSource
+ __OBJC_PROTOCOL_$__SFPBRFMarkdownCardSection
+ __OBJC_PROTOCOL_$__SFPBRFReferenceAttributionCardSection
+ __SFPBPasteCommandReadFrom
+ __SFPBQuickLookCommandReadFrom
+ __SFPBRFAttributionSourceReadFrom
+ __SFPBRFMarkdownCardSectionReadFrom
+ __SFPBRFReferenceAttributionCardSectionReadFrom
+ ___PARLogHandleForCategory_block_invoke.35185
+ ___PARLogHandleForCategory_block_invoke.71725
+ ___block_literal_global.35180
+ ___block_literal_global.35961
+ ___block_literal_global.37690
+ ___block_literal_global.71738
+ ___getDispatchQueue_block_invoke.71742
+ _getDispatchQueue.71736
+ _getDispatchQueue.onceToken.71737
+ _getDispatchQueue.queue.71739
+ _objc_autorelease
+ _objc_msgSend$addMarkdown_strings:
+ _objc_msgSend$addThumbnails:
+ _objc_msgSend$attribution_type
+ _objc_msgSend$card_section
+ _objc_msgSend$expansion_type
+ _objc_msgSend$fallback
+ _objc_msgSend$hasAttribution
+ _objc_msgSend$hasAttribution_type
+ _objc_msgSend$hasCard_section
+ _objc_msgSend$hasExpansion_type
+ _objc_msgSend$hasFallback
+ _objc_msgSend$hasIs_markdown
+ _objc_msgSend$hasStreaming_state
+ _objc_msgSend$is_markdown
+ _objc_msgSend$markdown_data
+ _objc_msgSend$markdown_strings
+ _objc_msgSend$pasteCommand
+ _objc_msgSend$quickLookCommand
+ _objc_msgSend$rfMarkdownCardSection
+ _objc_msgSend$rfReferenceAttributionCardSection
+ _objc_msgSend$secondary_title
+ _objc_msgSend$setAttribution_type:
+ _objc_msgSend$setCard_section:
+ _objc_msgSend$setExpansion_type:
+ _objc_msgSend$setFallback:
+ _objc_msgSend$setInputCharCount:
+ _objc_msgSend$setInputWordCount:
+ _objc_msgSend$setIs_markdown:
+ _objc_msgSend$setMarkdown_data:
+ _objc_msgSend$setMarkdown_data:forKey:
+ _objc_msgSend$setMarkdown_strings:
+ _objc_msgSend$setPasteCommand:
+ _objc_msgSend$setQuickLookCommand:
+ _objc_msgSend$setRfMarkdownCardSection:
+ _objc_msgSend$setRfReferenceAttributionCardSection:
+ _objc_msgSend$setSecondary_title:
+ _objc_msgSend$setStreaming_state:
+ _objc_msgSend$setThumbnails:
+ _objc_msgSend$streaming_state
+ _objc_msgSend$thumbnails
- GCC_except_table2767
- GCC_except_table6416
- GCC_except_table7974
- _PARLogHandleForCategory.logHandles.0.34901
- _PARLogHandleForCategory.logHandles.0.70635
- _PARLogHandleForCategory.logHandles.1.34895
- _PARLogHandleForCategory.logHandles.1.70632
- _PARLogHandleForCategory.logHandles.2.34903
- _PARLogHandleForCategory.logHandles.2.70637
- _PARLogHandleForCategory.logHandles.3.34904
- _PARLogHandleForCategory.logHandles.3.70638
- _PARLogHandleForCategory.logHandles.4.34905
- _PARLogHandleForCategory.logHandles.4.70640
- _PARLogHandleForCategory.logHandles.5.34906
- _PARLogHandleForCategory.logHandles.5.70641
- _PARLogHandleForCategory.onceToken.34893
- _PARLogHandleForCategory.onceToken.70631
- __OBJC_$_PROP_LIST_RFAppIconImage.88
- __OBJC_$_PROP_LIST_RFAttribution.127
- __OBJC_$_PROP_LIST_RFLongItemStandardCardSection.253
- __OBJC_$_PROP_LIST_SFCardSectionValue.1067
- __OBJC_$_PROP_LIST__SFPBCardSectionValue.3360
- __OBJC_$_PROP_LIST__SFPBClearProactiveCategoryCommand.3391
- __OBJC_$_PROP_LIST__SFPBClockImage.3421
- __OBJC_$_PROP_LIST__SFPBCloudChannelsRequestItem.3452
- __OBJC_$_PROP_LIST__SFPBCollectionCardSection.3489
- __OBJC_$_PROP_LIST__SFPBCollectionStyle.3547
- __OBJC_$_PROP_LIST__SFPBCollectionStyleGrid.3569
- __OBJC_$_PROP_LIST__SFPBCollectionStyleHorizontallyScrolling.3583
- __OBJC_$_PROP_LIST__SFPBCollectionStyleRow.3613
- __OBJC_$_PROP_LIST__SFPBColor.3733
- __OBJC_$_PROP_LIST__SFPBColorBarCardSection.3756
- __OBJC_$_PROP_LIST__SFPBCombinedCardSection.3763
- __OBJC_$_PROP_LIST__SFPBCommand.4553
- __OBJC_$_PROP_LIST__SFPBCommandButtonItem.4568
- __OBJC_$_PROP_LIST__SFPBCommandReference.4583
- __OBJC_$_PROP_LIST__SFPBCommandRowCardSection.4606
- __OBJC_$_PROP_LIST__SFPBCommandValue.4626
- __OBJC_$_PROP_LIST__SFPBCompactRowCardSection.4641
- __OBJC_$_PROP_LIST__SFPBContactButtonItem.4675
- __OBJC_$_PROP_LIST__SFPBContactCopyItem.4690
- __OBJC_$_PROP_LIST__SFPBContactImage.4725
- __OBJC_$_PROP_LIST__SFPBCopyCommand.4743
- __OBJC_$_PROP_LIST__SFPBCopyItem.4815
- __OBJC_$_PROP_LIST__SFPBCoreSpotlightButtonItem.4842
- __OBJC_$_PROP_LIST__SFPBCoreSpotlightCopyItem.4873
- __OBJC_$_PROP_LIST__SFPBCoreSpotlightRankingSignals.5011
- __OBJC_$_PROP_LIST__SFPBCoreSpotlightShareItem.5026
- __OBJC_$_PROP_LIST__SFPBCreateCalendarEventCommand.5046
- __OBJC_$_PROP_LIST__SFPBCreateContactCommand.5061
- __OBJC_$_PROP_LIST__SFPBCreateReminderCommand.5081
- __OBJC_$_PROP_LIST__SFPBDate.5095
- __OBJC_$_PROP_LIST__SFPBDefaultPunchoutAppIconImage.5110
- __OBJC_$_PROP_LIST__SFPBDescriptionCardSection.5223
- __OBJC_$_PROP_LIST__SFPBDetailedRowCardSection.5397
- __OBJC_$_PROP_LIST__SFPBDomainEngagementScore.5435
- __OBJC_$_PROP_LIST__SFPBDomainSubscriptionRequestItem.5455
- __OBJC_$_PROP_LIST__SFPBDrillDownMetadata.5562
- __OBJC_$_PROP_LIST__SFPBDynamicURLImageResource.5616
- __OBJC_$_PROP_LIST__SFPBEmailCommand.5623
- __OBJC_$_PROP_LIST__SFPBEmbeddingState.5707
- __OBJC_$_PROP_LIST__SFPBEngagementSignal.5769
- __OBJC_$_PROP_LIST__SFPBEntitySearchMetadata.5793
- __OBJC_$_PROP_LIST__SFPBExecuteMenuItemCommand.5808
- __OBJC_$_PROP_LIST__SFPBExecuteToolCommand.5831
- __OBJC_$_PROP_LIST__SFPBExpandInlineCommand.5845
- __OBJC_$_PROP_LIST__SFPBFillToolAppEntityParameterCommand.5868
- __OBJC_$_PROP_LIST__SFPBFillToolAppParameterCommand.5883
- __OBJC_$_PROP_LIST__SFPBFillToolFileParameterCommand.5898
- __OBJC_$_PROP_LIST__SFPBFillToolParameterCommand.5905
- __OBJC_$_PROP_LIST__SFPBFillToolPersonParameterCommand.5912
- __OBJC_$_PROP_LIST__SFPBFindMyCardSection.5919
- __OBJC_$_PROP_LIST__SFPBFlight.6005
- __OBJC_$_PROP_LIST__SFPBFlightCardSection.6031
- __OBJC_$_PROP_LIST__SFPBFlightCheckinCommand.6037
- __OBJC_$_PROP_LIST__SFPBFlightDateDescriptor.6068
- __OBJC_$_PROP_LIST__SFPBFlightDetails.6082
- __OBJC_$_PROP_LIST__SFPBFlightLeg.6288
- __OBJC_$_PROP_LIST__SFPBFormattedText.6336
- __OBJC_$_PROP_LIST__SFPBGradientColor.6364
- __OBJC_$_PROP_LIST__SFPBGraphicalFloat.6378
- __OBJC_$_PROP_LIST__SFPBGridCardSection.6385
- __OBJC_$_PROP_LIST__SFPBHashBucketDetail.6415
- __OBJC_$_PROP_LIST__SFPBHashBucketDetail_HashDetail.6466
- __OBJC_$_PROP_LIST__SFPBHeroCardSection.6473
- __OBJC_$_PROP_LIST__SFPBHeroTitleCardSection.6488
- __OBJC_$_PROP_LIST__SFPBHorizontalButtonCardSection.6507
- __OBJC_$_PROP_LIST__SFPBHorizontalScrollCardSection.6514
- __OBJC_$_PROP_LIST__SFPBImage.6818
- __OBJC_$_PROP_LIST__SFPBImageCopyItem.6825
- __OBJC_$_PROP_LIST__SFPBImageDerivedColor.6832
- __OBJC_$_PROP_LIST__SFPBImageOption.6860
- __OBJC_$_PROP_LIST__SFPBImagesCardSection.6888
- __OBJC_$_PROP_LIST__SFPBIndexState.6950
- __OBJC_$_PROP_LIST__SFPBIndexedUserActivityCommand.6965
- __OBJC_$_PROP_LIST__SFPBInfoCardSection.6995
- __OBJC_$_PROP_LIST__SFPBInfoTuple.7039
- __OBJC_$_PROP_LIST__SFPBInvokeSiriCommand.7062
- __OBJC_$_PROP_LIST__SFPBKeyValueDataCardSection.7093
- __OBJC_$_PROP_LIST__SFPBKeyValueTuple.7101
- __OBJC_$_PROP_LIST__SFPBLargeTitleDetailedRowCardSection.7131
- __OBJC_$_PROP_LIST__SFPBLatLng.7153
- __OBJC_$_PROP_LIST__SFPBLaunchAppCommand.7168
- __OBJC_$_PROP_LIST__SFPBLeadingTrailingCardSection.7207
- __OBJC_$_PROP_LIST__SFPBLinkPresentationCardSection.7237
- __OBJC_$_PROP_LIST__SFPBListenToCardSection.7268
- __OBJC_$_PROP_LIST__SFPBLocalImage.7282
- __OBJC_$_PROP_LIST__SFPBLocationTypeInfo.7297
- __OBJC_$_PROP_LIST__SFPBMailRankingSignals.7831
- __OBJC_$_PROP_LIST__SFPBMailResultDetails.7861
- __OBJC_$_PROP_LIST__SFPBManageReservationCommand.7867
- __OBJC_$_PROP_LIST__SFPBMapCardSection.7943
- __OBJC_$_PROP_LIST__SFPBMapPlaceCardSection.7958
- __OBJC_$_PROP_LIST__SFPBMapRegion.8004
- __OBJC_$_PROP_LIST__SFPBMapsDetailedRowCardSection.8019
- __OBJC_$_PROP_LIST__SFPBMediaArtworkImage.8034
- __OBJC_$_PROP_LIST__SFPBMediaDetail.8049
- __OBJC_$_PROP_LIST__SFPBMediaInfoCardSection.8163
- __OBJC_$_PROP_LIST__SFPBMediaItem.8243
- __OBJC_$_PROP_LIST__SFPBMediaMetadata.8323
- __OBJC_$_PROP_LIST__SFPBMediaOffer.8362
- __OBJC_$_PROP_LIST__SFPBMediaPlayerCardSection.8382
- __OBJC_$_PROP_LIST__SFPBMediaRemoteControlCardSection.8413
- __OBJC_$_PROP_LIST__SFPBMessageAttachment.8428
- __OBJC_$_PROP_LIST__SFPBMessageCardSection.8480
- __OBJC_$_PROP_LIST__SFPBMetaInfoCardSection.8519
- __OBJC_$_PROP_LIST__SFPBMiniCardSection.8526
- __OBJC_$_PROP_LIST__SFPBMonogramImage.8549
- __OBJC_$_PROP_LIST__SFPBMoreResults.8556
- __OBJC_$_PROP_LIST__SFPBNamedProtobufMessage.8579
- __OBJC_$_PROP_LIST__SFPBNewsCardSection.8610
- __OBJC_$_PROP_LIST__SFPBNowPlayingCardSection.8629
- __OBJC_$_PROP_LIST__SFPBOpenAppClipCommand.8644
- __OBJC_$_PROP_LIST__SFPBOpenCalculationCommand.8675
- __OBJC_$_PROP_LIST__SFPBOpenCoreSpotlightItemCommand.8690
- __OBJC_$_PROP_LIST__SFPBOpenFileProviderItemCommand.8705
- __OBJC_$_PROP_LIST__SFPBOpenMediaCommand.8720
- __OBJC_$_PROP_LIST__SFPBOpenPunchoutCommand.8727
- __OBJC_$_PROP_LIST__SFPBOpenWebClipCommand.8734
- __OBJC_$_PROP_LIST__SFPBPatternModel.8773
- __OBJC_$_PROP_LIST__SFPBPegasusDisplayFields.8804
- __OBJC_$_PROP_LIST__SFPBPerformContactActionCommand.8834
- __OBJC_$_PROP_LIST__SFPBPerformContactQueryCommand.8841
- __OBJC_$_PROP_LIST__SFPBPerformEntityQueryCommand.8912
- __OBJC_$_PROP_LIST__SFPBPerformIntentCommand.8935
- __OBJC_$_PROP_LIST__SFPBPerformPersonEntityQueryCommand.8942
- __OBJC_$_PROP_LIST__SFPBPerson.8997
- __OBJC_$_PROP_LIST__SFPBPersonHeaderCardSection.9004
- __OBJC_$_PROP_LIST__SFPBPhotosAggregatedInfo.9034
- __OBJC_$_PROP_LIST__SFPBPhotosAlbumImage.9049
- __OBJC_$_PROP_LIST__SFPBPhotosAttributes.9103
- __OBJC_$_PROP_LIST__SFPBPhotosLibraryImage.9139
- __OBJC_$_PROP_LIST__SFPBPhotosMemoryImage.9154
- __OBJC_$_PROP_LIST__SFPBPhotosRankingInfo.9232
- __OBJC_$_PROP_LIST__SFPBPin.9247
- __OBJC_$_PROP_LIST__SFPBPlayAudioButtonItem.9280
- __OBJC_$_PROP_LIST__SFPBPlayMediaCommand.9303
- __OBJC_$_PROP_LIST__SFPBPlayVideoCommand.9310
- __OBJC_$_PROP_LIST__SFPBPlayWatchListItemButtonItem.9330
- __OBJC_$_PROP_LIST__SFPBPointSize.9353
- __OBJC_$_PROP_LIST__SFPBProduct.9384
- __OBJC_$_PROP_LIST__SFPBProductAvailability.9406
- __OBJC_$_PROP_LIST__SFPBProductCardSection.9421
- __OBJC_$_PROP_LIST__SFPBProductInventory.9477
- __OBJC_$_PROP_LIST__SFPBProductInventoryResult.9500
- __OBJC_$_PROP_LIST__SFPBPunchout.9565
- __OBJC_$_PROP_LIST__SFPBQueryUnderstandingParse.9723
- __OBJC_$_PROP_LIST__SFPBQuickLookThumbnailImage.9731
- __OBJC_$_PROP_LIST__SFPBRFAppIconImage.9751
- __OBJC_$_PROP_LIST__SFPBRFAspectRatio.9759
- __OBJC_$_PROP_LIST__SFPBRFAttribution.9811
- __OBJC_$_PROP_LIST__SFPBRFAvatarImage.9830
- __OBJC_$_PROP_LIST__SFPBRFBadgedImage.9844
- __OBJC_$_PROP_LIST__SFPBRFBinaryButtonCardSection.9867
- __OBJC_$_PROP_LIST__SFPBRFButtonCardSection.9875
- __OBJC_$_PROP_LIST__SFPBRFColor.9909
- __OBJC_$_PROP_LIST__SFPBRFDefaultBrowserAppIconImage.9915
- __OBJC_$_PROP_LIST__SFPBRFDisambiguationTitleCardSection.9931
- __OBJC_$_PROP_LIST__SFPBRFEngageable.9960
- __OBJC_$_PROP_LIST__SFPBRFExpandableStandardCardSection.9995
- __OBJC_$_PROP_LIST__SFPBRFExpandingComponentContent.10018
- __OBJC_$_PROP_LIST__SFPBRFFactItemButtonCardSection.10103
- __OBJC_$_PROP_LIST__SFPBRFFactItemDetailedNumberCardSection.10122
- __OBJC_$_PROP_LIST__SFPBRFFactItemHeroButtonCardSection.10129
- __OBJC_$_PROP_LIST__SFPBRFFactItemHeroNumberCardSection.10162
- __OBJC_$_PROP_LIST__SFPBRFFactItemImageRightCardSection.10169
- __OBJC_$_PROP_LIST__SFPBRFFactItemShortHeroNumberCardSection.10176
- __OBJC_$_PROP_LIST__SFPBRFFactItemShortNumberCardSection.10183
- __OBJC_$_PROP_LIST__SFPBRFFactItemStandardCardSection.10199
- __OBJC_$_PROP_LIST__SFPBRFFont.10227
- __OBJC_$_PROP_LIST__SFPBRFFont_RFSystemFont.11354
- __OBJC_$_PROP_LIST__SFPBRFFormattedText.10381
- __OBJC_$_PROP_LIST__SFPBRFHighlightedSubstring.10396
- __OBJC_$_PROP_LIST__SFPBRFImageElement.10416
- __OBJC_$_PROP_LIST__SFPBRFImageSource.10515
- __OBJC_$_PROP_LIST__SFPBRFLongItemStandardCardSection.10546
- __OBJC_$_PROP_LIST__SFPBRFMapAnnotation.10576
- __OBJC_$_PROP_LIST__SFPBRFMapCardSection.10643
- __OBJC_$_PROP_LIST__SFPBRFMapMarker.10676
- __OBJC_$_PROP_LIST__SFPBRFMapMarkerIdentifier.10707
- __OBJC_$_PROP_LIST__SFPBRFMapMarkerImage.10722
- __OBJC_$_PROP_LIST__SFPBRFMapMarkerText.10730
- __OBJC_$_PROP_LIST__SFPBRFMapPoint.10752
- __OBJC_$_PROP_LIST__SFPBRFMonogramImage.10767
- __OBJC_$_PROP_LIST__SFPBRFMultiButtonCardSection.10782
- __OBJC_$_PROP_LIST__SFPBRFOptionalBool.10789
- __OBJC_$_PROP_LIST__SFPBRFOptionalFloat.10796
- __OBJC_$_PROP_LIST__SFPBRFPreview.10803
- __OBJC_$_PROP_LIST__SFPBRFPreviewList.10825
- __OBJC_$_PROP_LIST__SFPBRFPrimaryHeaderMarqueeCardSection.10840
- __OBJC_$_PROP_LIST__SFPBRFPrimaryHeaderRichCardSection.10847
- __OBJC_$_PROP_LIST__SFPBRFPrimaryHeaderStackedImageCardSection.10855
- __OBJC_$_PROP_LIST__SFPBRFPrimaryHeaderStandardCardSection.10862
- __OBJC_$_PROP_LIST__SFPBRFRGBValue.10892
- __OBJC_$_PROP_LIST__SFPBRFReferenceCenteredCardSection.10904
- __OBJC_$_PROP_LIST__SFPBRFReferenceFootnoteCardSection.10911
- __OBJC_$_PROP_LIST__SFPBRFReferenceItemButtonCardSection.10918
- __OBJC_$_PROP_LIST__SFPBRFReferenceItemLogoCardSection.10925
- __OBJC_$_PROP_LIST__SFPBRFReferenceRichCardSection.10932
- __OBJC_$_PROP_LIST__SFPBRFReferenceStandardCardSection.10939
- __OBJC_$_PROP_LIST__SFPBRFSecondaryHeaderEmphasizedCardSection.10946
- __OBJC_$_PROP_LIST__SFPBRFSecondaryHeaderStandardCardSection.10953
- __OBJC_$_PROP_LIST__SFPBRFShowMoreOnTap.10976
- __OBJC_$_PROP_LIST__SFPBRFSimpleItemPlayerCardSection.10991
- __OBJC_$_PROP_LIST__SFPBRFSimpleItemReverseRichCardSection.10998
- __OBJC_$_PROP_LIST__SFPBRFSimpleItemRichCardSection.11029
- __OBJC_$_PROP_LIST__SFPBRFSimpleItemRichSearchResultCardSection.11036
- __OBJC_$_PROP_LIST__SFPBRFSimpleItemStandardCardSection.11043
- __OBJC_$_PROP_LIST__SFPBRFSimpleItemVisualElementCardSection.11067
- __OBJC_$_PROP_LIST__SFPBRFSummaryItemAlignedTextCardSection.11083
- __OBJC_$_PROP_LIST__SFPBRFSummaryItemAttribution.11107
- __OBJC_$_PROP_LIST__SFPBRFSummaryItemButtonCardSection.11114
- __OBJC_$_PROP_LIST__SFPBRFSummaryItemDetailedTextCardSection.11121
- __OBJC_$_PROP_LIST__SFPBRFSummaryItemExpandableCardSection.11160
- __OBJC_$_PROP_LIST__SFPBRFSummaryItemExpandableContent.11175
- __OBJC_$_PROP_LIST__SFPBRFSummaryItemImageRightCardSection.11195
- __OBJC_$_PROP_LIST__SFPBRFSummaryItemPairCardSection.11202
- __OBJC_$_PROP_LIST__SFPBRFSummaryItemPairNumberCardSection.11241
- __OBJC_$_PROP_LIST__SFPBRFSummaryItemPlayerCardSection.11248
- __OBJC_$_PROP_LIST__SFPBRFSummaryItemShortNumberCardSection.11255
- __OBJC_$_PROP_LIST__SFPBRFSummaryItemStandardCardSection.11270
- __OBJC_$_PROP_LIST__SFPBRFSummaryItemSwitchV2CardSection.11285
- __OBJC_$_PROP_LIST__SFPBRFSummaryItemTextCardSection.11292
- __OBJC_$_PROP_LIST__SFPBRFSymbolImage.11347
- __OBJC_$_PROP_LIST__SFPBRFTableCell.11381
- __OBJC_$_PROP_LIST__SFPBRFTableColumnDefinition.11411
- __OBJC_$_PROP_LIST__SFPBRFTableContentColumnDefinition.11457
- __OBJC_$_PROP_LIST__SFPBRFTableHeaderCardSection.11522
- __OBJC_$_PROP_LIST__SFPBRFTableRowCardSection.11537
- __OBJC_$_PROP_LIST__SFPBRFTableSpacerColumnDefinition.11543
- __OBJC_$_PROP_LIST__SFPBRFTextElement.11587
- __OBJC_$_PROP_LIST__SFPBRFTextEncapsulation.11593
- __OBJC_$_PROP_LIST__SFPBRFTextProperty.11623
- __OBJC_$_PROP_LIST__SFPBRFUrlImage.11687
- __OBJC_$_PROP_LIST__SFPBRFVisualElement.11706
- __OBJC_$_PROP_LIST__SFPBRFVisualProperty.11728
- __OBJC_$_PROP_LIST__SFPBRFVisualPropertyWithAction.11743
- __OBJC_$_PROP_LIST__SFPBReferentialCommand.11750
- __OBJC_$_PROP_LIST__SFPBRejectPeopleInPhotoCommand.11770
- __OBJC_$_PROP_LIST__SFPBReminder.11785
- __OBJC_$_PROP_LIST__SFPBRequestAppClipInstallCommand.11792
- __OBJC_$_PROP_LIST__SFPBRequestProductPageCommand.11823
- __OBJC_$_PROP_LIST__SFPBRequestUserReportCommand.11830
- __OBJC_$_PROP_LIST__SFPBResponseWrapperCardSection.11884
- __OBJC_$_PROP_LIST__SFPBResultEntity.11912
- __OBJC_$_PROP_LIST__SFPBRichText.11952
- __OBJC_$_PROP_LIST__SFPBRichTitleCardSection.12100
- __OBJC_$_PROP_LIST__SFPBRowCardSection.12195
- __OBJC_$_PROP_LIST__SFPBRunVoiceShortcutCommand.12210
- __OBJC_$_PROP_LIST__SFPBSafariAttributes.12224
- __OBJC_$_PROP_LIST__SFPBSafariTableOfContentsCardSection.12270
- __OBJC_$_PROP_LIST__SFPBSafariTableOfContentsItem.12286
- __OBJC_$_PROP_LIST__SFPBScene.12308
- __OBJC_$_PROP_LIST__SFPBScoreboardCardSection.12352
- __OBJC_$_PROP_LIST__SFPBSearchInAppCommand.12367
- __OBJC_$_PROP_LIST__SFPBSearchSuggestion.12445
- __OBJC_$_PROP_LIST__SFPBSearchWebCommand.12452
- __OBJC_$_PROP_LIST__SFPBSectionHeaderCardSection.12460
- __OBJC_$_PROP_LIST__SFPBSelectableGridCardSection.12490
- __OBJC_$_PROP_LIST__SFPBShareCommand.12523
- __OBJC_$_PROP_LIST__SFPBShareItem.12556
- __OBJC_$_PROP_LIST__SFPBShortcutsImage.12571
- __OBJC_$_PROP_LIST__SFPBShowAppStoreSheetCommand.12586
- __OBJC_$_PROP_LIST__SFPBShowContactCardCommand.12601
- __OBJC_$_PROP_LIST__SFPBShowPhotosOneUpViewCommand.12652
- __OBJC_$_PROP_LIST__SFPBShowPurchaseRequestSheetCommand.12667
- __OBJC_$_PROP_LIST__SFPBShowSFCardCommand.12682
- __OBJC_$_PROP_LIST__SFPBShowScreenTimeRequestSheetCommand.12689
- __OBJC_$_PROP_LIST__SFPBShowWrapperResponseViewCommand.12696
- __OBJC_$_PROP_LIST__SFPBSocialMediaPostCardSection.12760
- __OBJC_$_PROP_LIST__SFPBSplitCardSection.12827
- __OBJC_$_PROP_LIST__SFPBSportsDetail.12842
- __OBJC_$_PROP_LIST__SFPBSportsFollowButtonItem.12870
- __OBJC_$_PROP_LIST__SFPBSportsItem.12877
- __OBJC_$_PROP_LIST__SFPBSportsSubscriptionRequestItem.12908
- __OBJC_$_PROP_LIST__SFPBSportsTeam.12940
- __OBJC_$_PROP_LIST__SFPBSpotlightEmbeddingState.12970
- __OBJC_$_PROP_LIST__SFPBStockChartCardSection.12993
- __OBJC_$_PROP_LIST__SFPBStoreButtonItem.13016
- __OBJC_$_PROP_LIST__SFPBStringDictionary.13035
- __OBJC_$_PROP_LIST__SFPBStrokeAnimationCardSection.13086
- __OBJC_$_PROP_LIST__SFPBStructuredLocation.13109
- __OBJC_$_PROP_LIST__SFPBSubscribeForUpdatesCommand.13142
- __OBJC_$_PROP_LIST__SFPBSuggestionCardSection.13181
- __OBJC_$_PROP_LIST__SFPBSymbolImage.13223
- __OBJC_$_PROP_LIST__SFPBTableAlignmentSchema.13247
- __OBJC_$_PROP_LIST__SFPBTableColumnAlignment.13277
- __OBJC_$_PROP_LIST__SFPBTableHeaderRowCardSection.13345
- __OBJC_$_PROP_LIST__SFPBTableRowCardSection.13365
- __OBJC_$_PROP_LIST__SFPBText.13382
- __OBJC_$_PROP_LIST__SFPBTextColumn.13404
- __OBJC_$_PROP_LIST__SFPBTextColumnSection.13439
- __OBJC_$_PROP_LIST__SFPBTextColumnsCardSection.13450
- __OBJC_$_PROP_LIST__SFPBTextCopyItem.13465
- __OBJC_$_PROP_LIST__SFPBTimeZone.13472
- __OBJC_$_PROP_LIST__SFPBTitleCardSection.13479
- __OBJC_$_PROP_LIST__SFPBTitleSubtitleTuple.13486
- __OBJC_$_PROP_LIST__SFPBToggleAudioCommand.13509
- __OBJC_$_PROP_LIST__SFPBToggleButtonConfiguration.13533
- __OBJC_$_PROP_LIST__SFPBToggleWatchListStatusCommand.13548
- __OBJC_$_PROP_LIST__SFPBTopic.13591
- __OBJC_$_PROP_LIST__SFPBTrack.13623
- __OBJC_$_PROP_LIST__SFPBTrackListCardSection.13645
- __OBJC_$_PROP_LIST__SFPBURL.13652
- __OBJC_$_PROP_LIST__SFPBURLCopyItem.13659
- __OBJC_$_PROP_LIST__SFPBURLImage.13674
- __OBJC_$_PROP_LIST__SFPBURLShareItem.13681
- __OBJC_$_PROP_LIST__SFPBUpdateSearchQueryCommand.13696
- __OBJC_$_PROP_LIST__SFPBUpdateSportsFollowingStatusCommand.13711
- __OBJC_$_PROP_LIST__SFPBUserActivityData.13742
- __OBJC_$_PROP_LIST__SFPBUserActivityInfo.13765
- __OBJC_$_PROP_LIST__SFPBUserReportRequest.13840
- __OBJC_$_PROP_LIST__SFPBVerticalLayoutCardSection.13871
- __OBJC_$_PROP_LIST__SFPBViewEmailCommand.13877
- __OBJC_$_PROP_LIST__SFPBWatchListButtonItem.13884
- __OBJC_$_PROP_LIST__SFPBWatchListCardSection.13891
- __OBJC_$_PROP_LIST__SFPBWatchListItem.13970
- __OBJC_$_PROP_LIST__SFPBWatchNowCardSection.13984
- __OBJC_$_PROP_LIST__SFPBWeatherColor.14031
- __OBJC_$_PROP_LIST__SFPBWeatherDetails.14038
- __OBJC_$_PROP_LIST__SFPBWebCardSection.14053
- __OBJC_$_PROP_LIST__SFPBWorldMapCardSection.14076
- ___55-[SFCardSection(ProtobufInitializer) initWithProtobuf:]_block_invoke
- ___60-[SFSearchSuggestion(ProtobufInitializer) initWithProtobuf:]_block_invoke
- ___PARLogHandleForCategory_block_invoke.34899
- ___PARLogHandleForCategory_block_invoke.70634
- ___block_descriptor_40_e8_32s_e15_v32?0816^B24ls32l8
- ___block_literal_global.34894
- ___block_literal_global.35675
- ___block_literal_global.37404
- ___block_literal_global.70647
- ___getDispatchQueue_block_invoke.70651
- _getDispatchQueue.70645
- _getDispatchQueue.onceToken.70646
- _getDispatchQueue.queue.70648
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$enumerateKeysAndObjectsUsingBlock:
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x7
- _objc_retain_x8
CStrings:
+ "247"
+ "248"
+ "?\f"
+ "@\"RFAttribution\""
+ "@\"RFAttribution\"16@0:8"
+ "@\"RFMarkdownCardSection\""
+ "@\"RFMarkdownCardSection\"16@0:8"
+ "@\"RFReferenceAttributionCardSection\""
+ "@\"RFReferenceAttributionCardSection\"16@0:8"
+ "@\"_SFPBPasteCommand\""
+ "@\"_SFPBPasteCommand\"16@0:8"
+ "@\"_SFPBQuickLookCommand\""
+ "@\"_SFPBQuickLookCommand\"16@0:8"
+ "@\"_SFPBRFAttribution\""
+ "@\"_SFPBRFAttribution\"16@0:8"
+ "@\"_SFPBRFAttributionSource\"24@0:8Q16"
+ "@\"_SFPBRFMarkdownCardSection\""
+ "@\"_SFPBRFMarkdownCardSection\"16@0:8"
+ "@\"_SFPBRFReferenceAttributionCardSection\""
+ "@\"_SFPBRFReferenceAttributionCardSection\"16@0:8"
+ "RFAttributionSource"
+ "RFMarkdownCardSection"
+ "RFReferenceAttributionCardSection"
+ "SFPasteCommand"
+ "SFQuickLookCommand"
+ "T@\"NSArray\",C,N,V_markdown_strings"
+ "T@\"NSArray\",C,N,V_thumbnails"
+ "T@\"NSDictionary\",C,N,V_markdown_data"
+ "T@\"NSMutableDictionary\",C,N,V_markdown_data"
+ "T@\"NSString\",C,N,V_text_1"
+ "T@\"NSString\",C,N,V_text_2"
+ "T@\"RFAttribution\",&,N"
+ "T@\"RFAttribution\",&,N,V_attribution"
+ "T@\"RFMarkdownCardSection\",&,N"
+ "T@\"RFMarkdownCardSection\",&,N,V_rfMarkdownCardSection"
+ "T@\"RFReferenceAttributionCardSection\",&,N"
+ "T@\"RFReferenceAttributionCardSection\",&,N,V_rfReferenceAttributionCardSection"
+ "T@\"RFTextProperty\",&,N,V_secondary_title"
+ "T@\"SFCardSection\",&,N,V_card_section"
+ "T@\"SFCopyItem\",&,N,V_copyableItems"
+ "T@\"_SFPBCardSection\",&,N,V_card_section"
+ "T@\"_SFPBPasteCommand\",&,N"
+ "T@\"_SFPBPasteCommand\",&,N,V_pasteCommand"
+ "T@\"_SFPBQuickLookCommand\",&,N"
+ "T@\"_SFPBQuickLookCommand\",&,N,V_quickLookCommand"
+ "T@\"_SFPBRFAttribution\",&,N"
+ "T@\"_SFPBRFAttribution\",&,N,V_attribution"
+ "T@\"_SFPBRFMarkdownCardSection\",&,N"
+ "T@\"_SFPBRFMarkdownCardSection\",&,N,V_rfMarkdownCardSection"
+ "T@\"_SFPBRFReferenceAttributionCardSection\",&,N"
+ "T@\"_SFPBRFReferenceAttributionCardSection\",&,N,V_rfReferenceAttributionCardSection"
+ "T@\"_SFPBRFTextProperty\",&,N,V_secondary_title"
+ "TB,N,V_is_markdown"
+ "TQ,N,V_inputCharCount"
+ "TQ,N,V_inputWordCount"
+ "TQ,R,N,V_whichSource"
+ "Ti,N,V_attribution_type"
+ "Ti,N,V_expansion_type"
+ "Ti,N,V_fallback"
+ "Ti,N,V_streaming_state"
+ "_SFPBPasteCommand"
+ "_SFPBQuickLookCommand"
+ "_SFPBRFAttributionSource"
+ "_SFPBRFMarkdownCardSection"
+ "_SFPBRFReferenceAttributionCardSection"
+ "_attribution_type"
+ "_card_section"
+ "_expansion_type"
+ "_fallback"
+ "_inputCharCount"
+ "_inputWordCount"
+ "_is_markdown"
+ "_markdown_data"
+ "_markdown_strings"
+ "_pasteCommand"
+ "_quickLookCommand"
+ "_rfMarkdownCardSection"
+ "_rfReferenceAttributionCardSection"
+ "_secondary_title"
+ "_streaming_state"
+ "_thumbnails"
+ "_whichSource"
+ "addMarkdown_strings:"
+ "addThumbnails:"
+ "attributionType"
+ "attribution_type"
+ "clearMarkdown_strings"
+ "clearThumbnails"
+ "expansionType"
+ "expansion_type"
+ "fallback"
+ "getMarkdown_data:forKey:"
+ "hasAttribution"
+ "hasAttribution_type"
+ "hasCard_section"
+ "hasExpansion_type"
+ "hasFallback"
+ "hasIs_markdown"
+ "hasStreaming_state"
+ "initWithInput:triggerEvent:inputCharCount:inputWordCount:"
+ "inputCharCount"
+ "inputWordCount"
+ "isMarkdown"
+ "is_markdown"
+ "markdownData"
+ "markdownStrings"
+ "markdown_data"
+ "markdown_strings"
+ "markdown_stringsAtIndex:"
+ "markdown_stringsCount"
+ "pasteCommand"
+ "quickLookCommand"
+ "rfMarkdownCardSection"
+ "rfReferenceAttributionCardSection"
+ "secondary_title"
+ "setAttribution_type:"
+ "setCard_section:"
+ "setExpansion_type:"
+ "setFallback:"
+ "setInputCharCount:"
+ "setInputWordCount:"
+ "setIs_markdown:"
+ "setMarkdown_data:"
+ "setMarkdown_data:forKey:"
+ "setMarkdown_strings:"
+ "setPasteCommand:"
+ "setQuickLookCommand:"
+ "setRfMarkdownCardSection:"
+ "setRfReferenceAttributionCardSection:"
+ "setSecondary_title:"
+ "setStreaming_state:"
+ "setThumbnails:"
+ "streamingState"
+ "streaming_state"
+ "thumbnails"
+ "thumbnailsAtIndex:"
+ "thumbnailsCount"
+ "v24@0:8@\"RFAttribution\"16"
+ "v24@0:8@\"RFMarkdownCardSection\"16"
+ "v24@0:8@\"RFReferenceAttributionCardSection\"16"
+ "v24@0:8@\"_SFPBPasteCommand\"16"
+ "v24@0:8@\"_SFPBQuickLookCommand\"16"
+ "v24@0:8@\"_SFPBRFAttributionSource\"16"
+ "v24@0:8@\"_SFPBRFMarkdownCardSection\"16"
+ "v24@0:8@\"_SFPBRFReferenceAttributionCardSection\"16"
+ "v32@0:8@\"NSData\"16@\"NSString\"24"
+ "whichSource"
+ "{?=\"attribution\"b1\"card_section\"b1}"
+ "{?=\"attribution_type\"b1\"expansion_type\"b1\"add_tint\"b1}"
+ "{?=\"image_style\"b1\"fallback\"b1}"
+ "{?=\"is_quote\"b1\"has_background_platter\"b1\"is_fresh\"b1\"is_markdown\"b1}"
+ "{?=\"streaming_state\"b1}"
- "T@\"SFCopyItem\",N"
- "T@\"SFCopyItem\",N,V_copyableItems"
- "enumerateKeysAndObjectsUsingBlock:"
- "v32@?0@8@16^B24"
- "{?=\"is_quote\"b1\"has_background_platter\"b1\"is_fresh\"b1}"

```
