## SearchFoundation

> `/System/Library/PrivateFrameworks/SearchFoundation.framework/Versions/A/SearchFoundation`

```diff

-3404.77.2.14.1
-  __TEXT.__text: 0x3b0428
+3405.10.1.0.0
+  __TEXT.__text: 0x3c5fec
   __TEXT.__auth_stubs: 0x430
-  __TEXT.__objc_methlist: 0x52284
-  __TEXT.__const: 0x90
+  __TEXT.__objc_methlist: 0x53e9c
+  __TEXT.__const: 0x88
   __TEXT.__dlopen_cstrs: 0x52
   __TEXT.__gcc_except_tab: 0x38
-  __TEXT.__cstring: 0x68bb
+  __TEXT.__cstring: 0x6a67
   __TEXT.__oslogstring: 0x19a
-  __TEXT.__unwind_info: 0x7e18
-  __TEXT.__objc_classname: 0x441c
-  __TEXT.__objc_methname: 0x2d2c8
-  __TEXT.__objc_methtype: 0xf04f
-  __TEXT.__objc_stubs: 0x18500
-  __DATA_CONST.__got: 0x1680
+  __TEXT.__unwind_info: 0x8218
+  __TEXT.__objc_classname: 0x46a1
+  __TEXT.__objc_methname: 0x2e05c
+  __TEXT.__objc_methtype: 0xf694
+  __TEXT.__objc_stubs: 0x18ac0
+  __DATA_CONST.__got: 0x1730
   __DATA_CONST.__const: 0x8f0
-  __DATA_CONST.__objc_classlist: 0x16a8
+  __DATA_CONST.__objc_classlist: 0x1758
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x1560
+  __DATA_CONST.__objc_protolist: 0x1610
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x71b0
+  __DATA_CONST.__objc_selrefs: 0x7350
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x1d50
+  __DATA_CONST.__objc_superrefs: 0x1e48
   __AUTH_CONST.__auth_got: 0x228
   __AUTH_CONST.__const: 0x320
-  __AUTH_CONST.__cfstring: 0xc6a0
-  __AUTH_CONST.__objc_const: 0xa3050
-  __AUTH.__objc_data: 0x9740
-  __DATA.__objc_ivar: 0x4180
-  __DATA.__data: 0x10098
+  __AUTH_CONST.__cfstring: 0xc9a0
+  __AUTH_CONST.__objc_const: 0xa6ab8
+  __AUTH.__objc_data: 0x9e20
+  __DATA.__objc_ivar: 0x4284
+  __DATA.__data: 0x108d8
   __DATA.__bss: 0xe8
   __DATA_DIRTY.__objc_data: 0x4b50
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 16693
-  Symbols:   35053
-  CStrings:  11654
+  Functions: 17064
+  Symbols:   35876
+  CStrings:  11856
 
Symbols:
+ +[RFSummaryItemAttribution supportsSecureCoding]
+ +[RFSummaryItemExpandableCardSection supportsSecureCoding]
+ +[RFSummaryItemExpandableContent supportsSecureCoding]
+ +[SFFillToolAppEntityParameterCommand supportsSecureCoding]
+ +[SFFillToolAppParameterCommand supportsSecureCoding]
+ +[SFFillToolFileParameterCommand supportsSecureCoding]
+ +[SFFillToolParameterCommand supportsSecureCoding]
+ +[SFFillToolPersonParameterCommand supportsSecureCoding]
+ +[SFPhotosAlbumImage supportsSecureCoding]
+ +[SFPhotosMemoryImage supportsSecureCoding]
+ +[SFURLCopyItem supportsSecureCoding]
+ -[RFSummaryItemAttribution .cxx_destruct]
+ -[RFSummaryItemAttribution copyWithZone:]
+ -[RFSummaryItemAttribution dictionaryRepresentation]
+ -[RFSummaryItemAttribution encodeWithCoder:]
+ -[RFSummaryItemAttribution hash]
+ -[RFSummaryItemAttribution initWithCoder:]
+ -[RFSummaryItemAttribution isEqual:]
+ -[RFSummaryItemAttribution jsonData]
+ -[RFSummaryItemAttribution setText:]
+ -[RFSummaryItemAttribution setText_compact:]
+ -[RFSummaryItemAttribution setText_minimal:]
+ -[RFSummaryItemAttribution text]
+ -[RFSummaryItemAttribution text_compact]
+ -[RFSummaryItemAttribution text_minimal]
+ -[RFSummaryItemAttribution(ProtobufInitializer) initWithProtobuf:]
+ -[RFSummaryItemExpandableCardSection .cxx_destruct]
+ -[RFSummaryItemExpandableCardSection attribution]
+ -[RFSummaryItemExpandableCardSection attribution_ignores_expansion]
+ -[RFSummaryItemExpandableCardSection copyWithZone:]
+ -[RFSummaryItemExpandableCardSection dictionaryRepresentation]
+ -[RFSummaryItemExpandableCardSection encodeWithCoder:]
+ -[RFSummaryItemExpandableCardSection expanding_component_content]
+ -[RFSummaryItemExpandableCardSection hasAttribution_ignores_expansion]
+ -[RFSummaryItemExpandableCardSection hash]
+ -[RFSummaryItemExpandableCardSection initWithCoder:]
+ -[RFSummaryItemExpandableCardSection isEqual:]
+ -[RFSummaryItemExpandableCardSection jsonData]
+ -[RFSummaryItemExpandableCardSection setAttribution:]
+ -[RFSummaryItemExpandableCardSection setAttribution_ignores_expansion:]
+ -[RFSummaryItemExpandableCardSection setExpanding_component_content:]
+ -[RFSummaryItemExpandableCardSection setText_1:]
+ -[RFSummaryItemExpandableCardSection setText_2:]
+ -[RFSummaryItemExpandableCardSection text_1]
+ -[RFSummaryItemExpandableCardSection text_2]
+ -[RFSummaryItemExpandableCardSection(ProtobufInitializer) initWithProtobuf:]
+ -[RFSummaryItemExpandableContent .cxx_destruct]
+ -[RFSummaryItemExpandableContent copyWithZone:]
+ -[RFSummaryItemExpandableContent dictionaryRepresentation]
+ -[RFSummaryItemExpandableContent encodeWithCoder:]
+ -[RFSummaryItemExpandableContent hasSimple_item_rich_card_section]
+ -[RFSummaryItemExpandableContent hash]
+ -[RFSummaryItemExpandableContent initWithCoder:]
+ -[RFSummaryItemExpandableContent isEqual:]
+ -[RFSummaryItemExpandableContent jsonData]
+ -[RFSummaryItemExpandableContent setSimple_item_rich_card_section:]
+ -[RFSummaryItemExpandableContent simple_item_rich_card_section]
+ -[RFSummaryItemExpandableContent(ProtobufInitializer) initWithProtobuf:]
+ -[SFCardSectionValue rfSummaryItemExpandableCardSection]
+ -[SFCardSectionValue setRfSummaryItemExpandableCardSection:]
+ -[SFCopyCommand copyableItems]
+ -[SFCopyCommand setCopyableItems:]
+ -[SFFillToolAppEntityParameterCommand .cxx_destruct]
+ -[SFFillToolAppEntityParameterCommand copyWithZone:]
+ -[SFFillToolAppEntityParameterCommand dictionaryRepresentation]
+ -[SFFillToolAppEntityParameterCommand encodeWithCoder:]
+ -[SFFillToolAppEntityParameterCommand encodedTypedValue]
+ -[SFFillToolAppEntityParameterCommand entity]
+ -[SFFillToolAppEntityParameterCommand hash]
+ -[SFFillToolAppEntityParameterCommand initWithCoder:]
+ -[SFFillToolAppEntityParameterCommand isEqual:]
+ -[SFFillToolAppEntityParameterCommand jsonData]
+ -[SFFillToolAppEntityParameterCommand setEncodedTypedValue:]
+ -[SFFillToolAppEntityParameterCommand setEntity:]
+ -[SFFillToolAppEntityParameterCommand(ProtobufInitializer) initWithProtobuf:]
+ -[SFFillToolAppParameterCommand .cxx_destruct]
+ -[SFFillToolAppParameterCommand applicationPath]
+ -[SFFillToolAppParameterCommand bundleIdentifier]
+ -[SFFillToolAppParameterCommand copyWithZone:]
+ -[SFFillToolAppParameterCommand dictionaryRepresentation]
+ -[SFFillToolAppParameterCommand encodeWithCoder:]
+ -[SFFillToolAppParameterCommand encodedTypedValue]
+ -[SFFillToolAppParameterCommand hash]
+ -[SFFillToolAppParameterCommand initWithCoder:]
+ -[SFFillToolAppParameterCommand isEqual:]
+ -[SFFillToolAppParameterCommand jsonData]
+ -[SFFillToolAppParameterCommand setApplicationPath:]
+ -[SFFillToolAppParameterCommand setBundleIdentifier:]
+ -[SFFillToolAppParameterCommand setEncodedTypedValue:]
+ -[SFFillToolAppParameterCommand(ProtobufInitializer) initWithProtobuf:]
+ -[SFFillToolFileParameterCommand .cxx_destruct]
+ -[SFFillToolFileParameterCommand copyWithZone:]
+ -[SFFillToolFileParameterCommand dictionaryRepresentation]
+ -[SFFillToolFileParameterCommand encodeWithCoder:]
+ -[SFFillToolFileParameterCommand encodedTypedValue]
+ -[SFFillToolFileParameterCommand filePath]
+ -[SFFillToolFileParameterCommand hash]
+ -[SFFillToolFileParameterCommand initWithCoder:]
+ -[SFFillToolFileParameterCommand isEqual:]
+ -[SFFillToolFileParameterCommand jsonData]
+ -[SFFillToolFileParameterCommand setEncodedTypedValue:]
+ -[SFFillToolFileParameterCommand setFilePath:]
+ -[SFFillToolFileParameterCommand(ProtobufInitializer) initWithProtobuf:]
+ -[SFFillToolParameterCommand .cxx_destruct]
+ -[SFFillToolParameterCommand copyWithZone:]
+ -[SFFillToolParameterCommand dictionaryRepresentation]
+ -[SFFillToolParameterCommand encodeWithCoder:]
+ -[SFFillToolParameterCommand encodedTypedValue]
+ -[SFFillToolParameterCommand hash]
+ -[SFFillToolParameterCommand initWithCoder:]
+ -[SFFillToolParameterCommand isEqual:]
+ -[SFFillToolParameterCommand jsonData]
+ -[SFFillToolParameterCommand setEncodedTypedValue:]
+ -[SFFillToolParameterCommand(ProtobufInitializer) initWithProtobuf:]
+ -[SFFillToolPersonParameterCommand .cxx_destruct]
+ -[SFFillToolPersonParameterCommand copyWithZone:]
+ -[SFFillToolPersonParameterCommand dictionaryRepresentation]
+ -[SFFillToolPersonParameterCommand encodeWithCoder:]
+ -[SFFillToolPersonParameterCommand encodedTypedValue]
+ -[SFFillToolPersonParameterCommand hash]
+ -[SFFillToolPersonParameterCommand initWithCoder:]
+ -[SFFillToolPersonParameterCommand isEqual:]
+ -[SFFillToolPersonParameterCommand jsonData]
+ -[SFFillToolPersonParameterCommand person]
+ -[SFFillToolPersonParameterCommand setEncodedTypedValue:]
+ -[SFFillToolPersonParameterCommand setPerson:]
+ -[SFFillToolPersonParameterCommand(ProtobufInitializer) initWithProtobuf:]
+ -[SFPhotosAlbumImage .cxx_destruct]
+ -[SFPhotosAlbumImage albumIdentifier]
+ -[SFPhotosAlbumImage applicationBundleIdentifier]
+ -[SFPhotosAlbumImage copyWithZone:]
+ -[SFPhotosAlbumImage dictionaryRepresentation]
+ -[SFPhotosAlbumImage encodeWithCoder:]
+ -[SFPhotosAlbumImage hash]
+ -[SFPhotosAlbumImage initWithCoder:]
+ -[SFPhotosAlbumImage isEqual:]
+ -[SFPhotosAlbumImage jsonData]
+ -[SFPhotosAlbumImage setAlbumIdentifier:]
+ -[SFPhotosAlbumImage setApplicationBundleIdentifier:]
+ -[SFPhotosAlbumImage(ProtobufInitializer) initWithProtobuf:]
+ -[SFPhotosMemoryImage .cxx_destruct]
+ -[SFPhotosMemoryImage applicationBundleIdentifier]
+ -[SFPhotosMemoryImage copyWithZone:]
+ -[SFPhotosMemoryImage dictionaryRepresentation]
+ -[SFPhotosMemoryImage encodeWithCoder:]
+ -[SFPhotosMemoryImage hash]
+ -[SFPhotosMemoryImage initWithCoder:]
+ -[SFPhotosMemoryImage isEqual:]
+ -[SFPhotosMemoryImage jsonData]
+ -[SFPhotosMemoryImage memoryIdentifier]
+ -[SFPhotosMemoryImage setApplicationBundleIdentifier:]
+ -[SFPhotosMemoryImage setMemoryIdentifier:]
+ -[SFPhotosMemoryImage(ProtobufInitializer) initWithProtobuf:]
+ -[SFShareCommand setShareItems:]
+ -[SFShareCommand shareItems]
+ -[SFURLCopyItem .cxx_destruct]
+ -[SFURLCopyItem copyWithZone:]
+ -[SFURLCopyItem dictionaryRepresentation]
+ -[SFURLCopyItem encodeWithCoder:]
+ -[SFURLCopyItem hash]
+ -[SFURLCopyItem initWithCoder:]
+ -[SFURLCopyItem isEqual:]
+ -[SFURLCopyItem jsonData]
+ -[SFURLCopyItem setUrl:]
+ -[SFURLCopyItem url]
+ -[SFURLCopyItem(ProtobufInitializer) initWithProtobuf:]
+ -[_SFPBCardSectionValue rfSummaryItemExpandableCardSection]
+ -[_SFPBCardSectionValue setRfSummaryItemExpandableCardSection:]
+ -[_SFPBCommand fillToolAppEntityParameterCommand]
+ -[_SFPBCommand fillToolAppParameterCommand]
+ -[_SFPBCommand fillToolFileParameterCommand]
+ -[_SFPBCommand fillToolParameterCommand]
+ -[_SFPBCommand fillToolPersonParameterCommand]
+ -[_SFPBCommand setFillToolAppEntityParameterCommand:]
+ -[_SFPBCommand setFillToolAppParameterCommand:]
+ -[_SFPBCommand setFillToolFileParameterCommand:]
+ -[_SFPBCommand setFillToolParameterCommand:]
+ -[_SFPBCommand setFillToolPersonParameterCommand:]
+ -[_SFPBCopyCommand addCopyableItems:]
+ -[_SFPBCopyCommand clearCopyableItems]
+ -[_SFPBCopyCommand copyableItemsAtIndex:]
+ -[_SFPBCopyCommand copyableItemsCount]
+ -[_SFPBCopyCommand copyableItems]
+ -[_SFPBCopyCommand setCopyableItems:]
+ -[_SFPBCopyItem setUrlCopyItem:]
+ -[_SFPBCopyItem urlCopyItem]
+ -[_SFPBFillToolAppEntityParameterCommand .cxx_destruct]
+ -[_SFPBFillToolAppEntityParameterCommand dictionaryRepresentation]
+ -[_SFPBFillToolAppEntityParameterCommand encodedTypedValue]
+ -[_SFPBFillToolAppEntityParameterCommand entity]
+ -[_SFPBFillToolAppEntityParameterCommand hash]
+ -[_SFPBFillToolAppEntityParameterCommand initWithDictionary:]
+ -[_SFPBFillToolAppEntityParameterCommand initWithJSON:]
+ -[_SFPBFillToolAppEntityParameterCommand isEqual:]
+ -[_SFPBFillToolAppEntityParameterCommand jsonData]
+ -[_SFPBFillToolAppEntityParameterCommand readFrom:]
+ -[_SFPBFillToolAppEntityParameterCommand setEncodedTypedValue:]
+ -[_SFPBFillToolAppEntityParameterCommand setEntity:]
+ -[_SFPBFillToolAppEntityParameterCommand writeTo:]
+ -[_SFPBFillToolAppEntityParameterCommand(FacadeInitializer) initWithFacade:]
+ -[_SFPBFillToolAppParameterCommand .cxx_destruct]
+ -[_SFPBFillToolAppParameterCommand applicationPath]
+ -[_SFPBFillToolAppParameterCommand bundleIdentifier]
+ -[_SFPBFillToolAppParameterCommand dictionaryRepresentation]
+ -[_SFPBFillToolAppParameterCommand encodedTypedValue]
+ -[_SFPBFillToolAppParameterCommand hash]
+ -[_SFPBFillToolAppParameterCommand initWithDictionary:]
+ -[_SFPBFillToolAppParameterCommand initWithJSON:]
+ -[_SFPBFillToolAppParameterCommand isEqual:]
+ -[_SFPBFillToolAppParameterCommand jsonData]
+ -[_SFPBFillToolAppParameterCommand readFrom:]
+ -[_SFPBFillToolAppParameterCommand setApplicationPath:]
+ -[_SFPBFillToolAppParameterCommand setBundleIdentifier:]
+ -[_SFPBFillToolAppParameterCommand setEncodedTypedValue:]
+ -[_SFPBFillToolAppParameterCommand writeTo:]
+ -[_SFPBFillToolAppParameterCommand(FacadeInitializer) initWithFacade:]
+ -[_SFPBFillToolFileParameterCommand .cxx_destruct]
+ -[_SFPBFillToolFileParameterCommand dictionaryRepresentation]
+ -[_SFPBFillToolFileParameterCommand encodedTypedValue]
+ -[_SFPBFillToolFileParameterCommand filePath]
+ -[_SFPBFillToolFileParameterCommand hash]
+ -[_SFPBFillToolFileParameterCommand initWithDictionary:]
+ -[_SFPBFillToolFileParameterCommand initWithJSON:]
+ -[_SFPBFillToolFileParameterCommand isEqual:]
+ -[_SFPBFillToolFileParameterCommand jsonData]
+ -[_SFPBFillToolFileParameterCommand readFrom:]
+ -[_SFPBFillToolFileParameterCommand setEncodedTypedValue:]
+ -[_SFPBFillToolFileParameterCommand setFilePath:]
+ -[_SFPBFillToolFileParameterCommand writeTo:]
+ -[_SFPBFillToolFileParameterCommand(FacadeInitializer) initWithFacade:]
+ -[_SFPBFillToolParameterCommand .cxx_destruct]
+ -[_SFPBFillToolParameterCommand dictionaryRepresentation]
+ -[_SFPBFillToolParameterCommand encodedTypedValue]
+ -[_SFPBFillToolParameterCommand hash]
+ -[_SFPBFillToolParameterCommand initWithDictionary:]
+ -[_SFPBFillToolParameterCommand initWithJSON:]
+ -[_SFPBFillToolParameterCommand isEqual:]
+ -[_SFPBFillToolParameterCommand jsonData]
+ -[_SFPBFillToolParameterCommand readFrom:]
+ -[_SFPBFillToolParameterCommand setEncodedTypedValue:]
+ -[_SFPBFillToolParameterCommand writeTo:]
+ -[_SFPBFillToolParameterCommand(FacadeInitializer) initWithFacade:]
+ -[_SFPBFillToolPersonParameterCommand .cxx_destruct]
+ -[_SFPBFillToolPersonParameterCommand dictionaryRepresentation]
+ -[_SFPBFillToolPersonParameterCommand encodedTypedValue]
+ -[_SFPBFillToolPersonParameterCommand hash]
+ -[_SFPBFillToolPersonParameterCommand initWithDictionary:]
+ -[_SFPBFillToolPersonParameterCommand initWithJSON:]
+ -[_SFPBFillToolPersonParameterCommand isEqual:]
+ -[_SFPBFillToolPersonParameterCommand jsonData]
+ -[_SFPBFillToolPersonParameterCommand person]
+ -[_SFPBFillToolPersonParameterCommand readFrom:]
+ -[_SFPBFillToolPersonParameterCommand setEncodedTypedValue:]
+ -[_SFPBFillToolPersonParameterCommand setPerson:]
+ -[_SFPBFillToolPersonParameterCommand writeTo:]
+ -[_SFPBFillToolPersonParameterCommand(FacadeInitializer) initWithFacade:]
+ -[_SFPBImage photosAlbumImage]
+ -[_SFPBImage photosMemoryImage]
+ -[_SFPBImage setPhotosAlbumImage:]
+ -[_SFPBImage setPhotosMemoryImage:]
+ -[_SFPBPhotosAlbumImage .cxx_destruct]
+ -[_SFPBPhotosAlbumImage albumIdentifier]
+ -[_SFPBPhotosAlbumImage applicationBundleIdentifier]
+ -[_SFPBPhotosAlbumImage dictionaryRepresentation]
+ -[_SFPBPhotosAlbumImage hash]
+ -[_SFPBPhotosAlbumImage initWithDictionary:]
+ -[_SFPBPhotosAlbumImage initWithJSON:]
+ -[_SFPBPhotosAlbumImage isEqual:]
+ -[_SFPBPhotosAlbumImage jsonData]
+ -[_SFPBPhotosAlbumImage readFrom:]
+ -[_SFPBPhotosAlbumImage setAlbumIdentifier:]
+ -[_SFPBPhotosAlbumImage setApplicationBundleIdentifier:]
+ -[_SFPBPhotosAlbumImage writeTo:]
+ -[_SFPBPhotosAlbumImage(FacadeInitializer) initWithFacade:]
+ -[_SFPBPhotosMemoryImage .cxx_destruct]
+ -[_SFPBPhotosMemoryImage applicationBundleIdentifier]
+ -[_SFPBPhotosMemoryImage dictionaryRepresentation]
+ -[_SFPBPhotosMemoryImage hash]
+ -[_SFPBPhotosMemoryImage initWithDictionary:]
+ -[_SFPBPhotosMemoryImage initWithJSON:]
+ -[_SFPBPhotosMemoryImage isEqual:]
+ -[_SFPBPhotosMemoryImage jsonData]
+ -[_SFPBPhotosMemoryImage memoryIdentifier]
+ -[_SFPBPhotosMemoryImage readFrom:]
+ -[_SFPBPhotosMemoryImage setApplicationBundleIdentifier:]
+ -[_SFPBPhotosMemoryImage setMemoryIdentifier:]
+ -[_SFPBPhotosMemoryImage writeTo:]
+ -[_SFPBPhotosMemoryImage(FacadeInitializer) initWithFacade:]
+ -[_SFPBRFSummaryItemAttribution .cxx_destruct]
+ -[_SFPBRFSummaryItemAttribution dictionaryRepresentation]
+ -[_SFPBRFSummaryItemAttribution hash]
+ -[_SFPBRFSummaryItemAttribution initWithDictionary:]
+ -[_SFPBRFSummaryItemAttribution initWithJSON:]
+ -[_SFPBRFSummaryItemAttribution isEqual:]
+ -[_SFPBRFSummaryItemAttribution jsonData]
+ -[_SFPBRFSummaryItemAttribution readFrom:]
+ -[_SFPBRFSummaryItemAttribution setText:]
+ -[_SFPBRFSummaryItemAttribution setText_compact:]
+ -[_SFPBRFSummaryItemAttribution setText_minimal:]
+ -[_SFPBRFSummaryItemAttribution text]
+ -[_SFPBRFSummaryItemAttribution text_compact]
+ -[_SFPBRFSummaryItemAttribution text_minimal]
+ -[_SFPBRFSummaryItemAttribution writeTo:]
+ -[_SFPBRFSummaryItemAttribution(FacadeInitializer) initWithFacade:]
+ -[_SFPBRFSummaryItemExpandableCardSection .cxx_destruct]
+ -[_SFPBRFSummaryItemExpandableCardSection addExpanding_component_content:]
+ -[_SFPBRFSummaryItemExpandableCardSection attribution]
+ -[_SFPBRFSummaryItemExpandableCardSection attribution_ignores_expansion]
+ -[_SFPBRFSummaryItemExpandableCardSection clearExpanding_component_content]
+ -[_SFPBRFSummaryItemExpandableCardSection dictionaryRepresentation]
+ -[_SFPBRFSummaryItemExpandableCardSection expanding_component_contentAtIndex:]
+ -[_SFPBRFSummaryItemExpandableCardSection expanding_component_contentCount]
+ -[_SFPBRFSummaryItemExpandableCardSection expanding_component_contents]
+ -[_SFPBRFSummaryItemExpandableCardSection hash]
+ -[_SFPBRFSummaryItemExpandableCardSection initWithDictionary:]
+ -[_SFPBRFSummaryItemExpandableCardSection initWithJSON:]
+ -[_SFPBRFSummaryItemExpandableCardSection isEqual:]
+ -[_SFPBRFSummaryItemExpandableCardSection jsonData]
+ -[_SFPBRFSummaryItemExpandableCardSection readFrom:]
+ -[_SFPBRFSummaryItemExpandableCardSection setAttribution:]
+ -[_SFPBRFSummaryItemExpandableCardSection setAttribution_ignores_expansion:]
+ -[_SFPBRFSummaryItemExpandableCardSection setExpanding_component_content:]
+ -[_SFPBRFSummaryItemExpandableCardSection setExpanding_component_contents:]
+ -[_SFPBRFSummaryItemExpandableCardSection setText_1:]
+ -[_SFPBRFSummaryItemExpandableCardSection setText_2:]
+ -[_SFPBRFSummaryItemExpandableCardSection text_1]
+ -[_SFPBRFSummaryItemExpandableCardSection text_2]
+ -[_SFPBRFSummaryItemExpandableCardSection writeTo:]
+ -[_SFPBRFSummaryItemExpandableCardSection(FacadeInitializer) initWithFacade:]
+ -[_SFPBRFSummaryItemExpandableContent .cxx_destruct]
+ -[_SFPBRFSummaryItemExpandableContent dictionaryRepresentation]
+ -[_SFPBRFSummaryItemExpandableContent hash]
+ -[_SFPBRFSummaryItemExpandableContent initWithDictionary:]
+ -[_SFPBRFSummaryItemExpandableContent initWithJSON:]
+ -[_SFPBRFSummaryItemExpandableContent isEqual:]
+ -[_SFPBRFSummaryItemExpandableContent jsonData]
+ -[_SFPBRFSummaryItemExpandableContent readFrom:]
+ -[_SFPBRFSummaryItemExpandableContent setSimple_item_rich_card_section:]
+ -[_SFPBRFSummaryItemExpandableContent simple_item_rich_card_section]
+ -[_SFPBRFSummaryItemExpandableContent whichValue]
+ -[_SFPBRFSummaryItemExpandableContent writeTo:]
+ -[_SFPBRFSummaryItemExpandableContent(FacadeInitializer) initWithFacade:]
+ -[_SFPBShareCommand addShareItems:]
+ -[_SFPBShareCommand clearShareItems]
+ -[_SFPBShareCommand setShareItems:]
+ -[_SFPBShareCommand shareItemsAtIndex:]
+ -[_SFPBShareCommand shareItemsCount]
+ -[_SFPBShareCommand shareItems]
+ -[_SFPBURLCopyItem .cxx_destruct]
+ -[_SFPBURLCopyItem dictionaryRepresentation]
+ -[_SFPBURLCopyItem hash]
+ -[_SFPBURLCopyItem initWithDictionary:]
+ -[_SFPBURLCopyItem initWithJSON:]
+ -[_SFPBURLCopyItem isEqual:]
+ -[_SFPBURLCopyItem jsonData]
+ -[_SFPBURLCopyItem readFrom:]
+ -[_SFPBURLCopyItem setUrl:]
+ -[_SFPBURLCopyItem url]
+ -[_SFPBURLCopyItem writeTo:]
+ -[_SFPBURLCopyItem(FacadeInitializer) initWithFacade:]
+ GCC_except_table2753
+ GCC_except_table7825
+ OBJC_IVAR_$_RFSummaryItemAttribution._text
+ OBJC_IVAR_$_RFSummaryItemAttribution._text_compact
+ OBJC_IVAR_$_RFSummaryItemAttribution._text_minimal
+ OBJC_IVAR_$_RFSummaryItemExpandableCardSection._attribution
+ OBJC_IVAR_$_RFSummaryItemExpandableCardSection._attribution_ignores_expansion
+ OBJC_IVAR_$_RFSummaryItemExpandableCardSection._expanding_component_content
+ OBJC_IVAR_$_RFSummaryItemExpandableCardSection._has
+ OBJC_IVAR_$_RFSummaryItemExpandableCardSection._text_1
+ OBJC_IVAR_$_RFSummaryItemExpandableCardSection._text_2
+ OBJC_IVAR_$_RFSummaryItemExpandableContent._has
+ OBJC_IVAR_$_RFSummaryItemExpandableContent._simple_item_rich_card_section
+ OBJC_IVAR_$_SFCardSectionValue._rfSummaryItemExpandableCardSection
+ OBJC_IVAR_$_SFCopyCommand._copyableItems
+ OBJC_IVAR_$_SFFillToolAppEntityParameterCommand._encodedTypedValue
+ OBJC_IVAR_$_SFFillToolAppEntityParameterCommand._entity
+ OBJC_IVAR_$_SFFillToolAppParameterCommand._applicationPath
+ OBJC_IVAR_$_SFFillToolAppParameterCommand._bundleIdentifier
+ OBJC_IVAR_$_SFFillToolAppParameterCommand._encodedTypedValue
+ OBJC_IVAR_$_SFFillToolFileParameterCommand._encodedTypedValue
+ OBJC_IVAR_$_SFFillToolFileParameterCommand._filePath
+ OBJC_IVAR_$_SFFillToolParameterCommand._encodedTypedValue
+ OBJC_IVAR_$_SFFillToolPersonParameterCommand._encodedTypedValue
+ OBJC_IVAR_$_SFFillToolPersonParameterCommand._person
+ OBJC_IVAR_$_SFPhotosAlbumImage._albumIdentifier
+ OBJC_IVAR_$_SFPhotosAlbumImage._applicationBundleIdentifier
+ OBJC_IVAR_$_SFPhotosMemoryImage._applicationBundleIdentifier
+ OBJC_IVAR_$_SFPhotosMemoryImage._memoryIdentifier
+ OBJC_IVAR_$_SFShareCommand._shareItems
+ OBJC_IVAR_$_SFURLCopyItem._url
+ OBJC_IVAR_$__SFPBCardSectionValue._rfSummaryItemExpandableCardSection
+ OBJC_IVAR_$__SFPBCommand._fillToolAppEntityParameterCommand
+ OBJC_IVAR_$__SFPBCommand._fillToolAppParameterCommand
+ OBJC_IVAR_$__SFPBCommand._fillToolFileParameterCommand
+ OBJC_IVAR_$__SFPBCommand._fillToolParameterCommand
+ OBJC_IVAR_$__SFPBCommand._fillToolPersonParameterCommand
+ OBJC_IVAR_$__SFPBCopyCommand._copyableItems
+ OBJC_IVAR_$__SFPBCopyItem._urlCopyItem
+ OBJC_IVAR_$__SFPBFillToolAppEntityParameterCommand._encodedTypedValue
+ OBJC_IVAR_$__SFPBFillToolAppEntityParameterCommand._entity
+ OBJC_IVAR_$__SFPBFillToolAppParameterCommand._applicationPath
+ OBJC_IVAR_$__SFPBFillToolAppParameterCommand._bundleIdentifier
+ OBJC_IVAR_$__SFPBFillToolAppParameterCommand._encodedTypedValue
+ OBJC_IVAR_$__SFPBFillToolFileParameterCommand._encodedTypedValue
+ OBJC_IVAR_$__SFPBFillToolFileParameterCommand._filePath
+ OBJC_IVAR_$__SFPBFillToolParameterCommand._encodedTypedValue
+ OBJC_IVAR_$__SFPBFillToolPersonParameterCommand._encodedTypedValue
+ OBJC_IVAR_$__SFPBFillToolPersonParameterCommand._person
+ OBJC_IVAR_$__SFPBImage._photosAlbumImage
+ OBJC_IVAR_$__SFPBImage._photosMemoryImage
+ OBJC_IVAR_$__SFPBPhotosAlbumImage._albumIdentifier
+ OBJC_IVAR_$__SFPBPhotosAlbumImage._applicationBundleIdentifier
+ OBJC_IVAR_$__SFPBPhotosMemoryImage._applicationBundleIdentifier
+ OBJC_IVAR_$__SFPBPhotosMemoryImage._memoryIdentifier
+ OBJC_IVAR_$__SFPBRFSummaryItemAttribution._text
+ OBJC_IVAR_$__SFPBRFSummaryItemAttribution._text_compact
+ OBJC_IVAR_$__SFPBRFSummaryItemAttribution._text_minimal
+ OBJC_IVAR_$__SFPBRFSummaryItemExpandableCardSection._attribution
+ OBJC_IVAR_$__SFPBRFSummaryItemExpandableCardSection._attribution_ignores_expansion
+ OBJC_IVAR_$__SFPBRFSummaryItemExpandableCardSection._expanding_component_contents
+ OBJC_IVAR_$__SFPBRFSummaryItemExpandableCardSection._text_1
+ OBJC_IVAR_$__SFPBRFSummaryItemExpandableCardSection._text_2
+ OBJC_IVAR_$__SFPBRFSummaryItemExpandableContent._simple_item_rich_card_section
+ OBJC_IVAR_$__SFPBRFSummaryItemExpandableContent._whichValue
+ OBJC_IVAR_$__SFPBShareCommand._shareItems
+ OBJC_IVAR_$__SFPBURLCopyItem._url
+ PARLogHandleForCategory.logHandles.0.33653
+ PARLogHandleForCategory.logHandles.0.68868
+ PARLogHandleForCategory.logHandles.1.33647
+ PARLogHandleForCategory.logHandles.1.68864
+ PARLogHandleForCategory.logHandles.2.33655
+ PARLogHandleForCategory.logHandles.2.68869
+ PARLogHandleForCategory.logHandles.3.33656
+ PARLogHandleForCategory.logHandles.3.68871
+ PARLogHandleForCategory.logHandles.4.33657
+ PARLogHandleForCategory.logHandles.4.68872
+ PARLogHandleForCategory.logHandles.5.33658
+ PARLogHandleForCategory.logHandles.5.68873
+ PARLogHandleForCategory.onceToken.33645
+ PARLogHandleForCategory.onceToken.68863
+ _OBJC_$_PROP_LIST_RFSummaryItemAttribution.87
+ _OBJC_$_PROP_LIST_RFSummaryItemExpandableCardSection.252
+ _OBJC_$_PROP_LIST_RFSummaryItemExpandableContent.80
+ _OBJC_$_PROP_LIST_SFCardSectionValue.1067
+ _OBJC_$_PROP_LIST_SFCopyCommand.114
+ _OBJC_$_PROP_LIST_SFFillToolAppEntityParameterCommand.111
+ _OBJC_$_PROP_LIST_SFFillToolAppParameterCommand.113
+ _OBJC_$_PROP_LIST_SFFillToolFileParameterCommand.108
+ _OBJC_$_PROP_LIST_SFFillToolParameterCommand.102
+ _OBJC_$_PROP_LIST_SFFillToolPersonParameterCommand.111
+ _OBJC_$_PROP_LIST_SFPhotosAlbumImage.141
+ _OBJC_$_PROP_LIST_SFPhotosMemoryImage.141
+ _OBJC_$_PROP_LIST_SFShareCommand.114
+ _OBJC_$_PROP_LIST_SFURLCopyItem.79
+ _OBJC_$_PROP_LIST__SFPBCardSectionValue.3345
+ _OBJC_$_PROP_LIST__SFPBClearProactiveCategoryCommand.3376
+ _OBJC_$_PROP_LIST__SFPBClockImage.3406
+ _OBJC_$_PROP_LIST__SFPBCloudChannelsRequestItem.3437
+ _OBJC_$_PROP_LIST__SFPBCollectionCardSection.3474
+ _OBJC_$_PROP_LIST__SFPBCollectionStyle.3532
+ _OBJC_$_PROP_LIST__SFPBCollectionStyleGrid.3554
+ _OBJC_$_PROP_LIST__SFPBCollectionStyleHorizontallyScrolling.3568
+ _OBJC_$_PROP_LIST__SFPBCollectionStyleRow.3598
+ _OBJC_$_PROP_LIST__SFPBColor.3718
+ _OBJC_$_PROP_LIST__SFPBColorBarCardSection.3741
+ _OBJC_$_PROP_LIST__SFPBCombinedCardSection.3748
+ _OBJC_$_PROP_LIST__SFPBCommand.4538
+ _OBJC_$_PROP_LIST__SFPBCommandButtonItem.4553
+ _OBJC_$_PROP_LIST__SFPBCommandReference.4568
+ _OBJC_$_PROP_LIST__SFPBCommandRowCardSection.4591
+ _OBJC_$_PROP_LIST__SFPBCommandValue.4611
+ _OBJC_$_PROP_LIST__SFPBCompactRowCardSection.4626
+ _OBJC_$_PROP_LIST__SFPBContactButtonItem.4660
+ _OBJC_$_PROP_LIST__SFPBContactCopyItem.4675
+ _OBJC_$_PROP_LIST__SFPBContactImage.4710
+ _OBJC_$_PROP_LIST__SFPBCopyCommand.4743
+ _OBJC_$_PROP_LIST__SFPBCopyItem.4815
+ _OBJC_$_PROP_LIST__SFPBCoreSpotlightButtonItem.4842
+ _OBJC_$_PROP_LIST__SFPBCoreSpotlightCopyItem.4873
+ _OBJC_$_PROP_LIST__SFPBCoreSpotlightRankingSignals.5011
+ _OBJC_$_PROP_LIST__SFPBCoreSpotlightShareItem.5026
+ _OBJC_$_PROP_LIST__SFPBCreateCalendarEventCommand.5046
+ _OBJC_$_PROP_LIST__SFPBCreateContactCommand.5061
+ _OBJC_$_PROP_LIST__SFPBCreateReminderCommand.5081
+ _OBJC_$_PROP_LIST__SFPBDate.5095
+ _OBJC_$_PROP_LIST__SFPBDefaultPunchoutAppIconImage.5110
+ _OBJC_$_PROP_LIST__SFPBDescriptionCardSection.5223
+ _OBJC_$_PROP_LIST__SFPBDetailedRowCardSection.5397
+ _OBJC_$_PROP_LIST__SFPBDomainEngagementScore.5435
+ _OBJC_$_PROP_LIST__SFPBDomainSubscriptionRequestItem.5455
+ _OBJC_$_PROP_LIST__SFPBDrillDownMetadata.5562
+ _OBJC_$_PROP_LIST__SFPBDynamicURLImageResource.5616
+ _OBJC_$_PROP_LIST__SFPBEmailCommand.5623
+ _OBJC_$_PROP_LIST__SFPBEngagementSignal.5685
+ _OBJC_$_PROP_LIST__SFPBEntitySearchMetadata.5709
+ _OBJC_$_PROP_LIST__SFPBExecuteMenuItemCommand.5724
+ _OBJC_$_PROP_LIST__SFPBExecuteToolCommand.5747
+ _OBJC_$_PROP_LIST__SFPBExpandInlineCommand.5761
+ _OBJC_$_PROP_LIST__SFPBFillToolAppEntityParameterCommand.5784
+ _OBJC_$_PROP_LIST__SFPBFillToolAppParameterCommand.5799
+ _OBJC_$_PROP_LIST__SFPBFillToolFileParameterCommand.5814
+ _OBJC_$_PROP_LIST__SFPBFillToolParameterCommand.5821
+ _OBJC_$_PROP_LIST__SFPBFillToolPersonParameterCommand.5828
+ _OBJC_$_PROP_LIST__SFPBFindMyCardSection.5835
+ _OBJC_$_PROP_LIST__SFPBFlight.5921
+ _OBJC_$_PROP_LIST__SFPBFlightCardSection.5947
+ _OBJC_$_PROP_LIST__SFPBFlightCheckinCommand.5953
+ _OBJC_$_PROP_LIST__SFPBFlightDetails.5967
+ _OBJC_$_PROP_LIST__SFPBFlightLeg.6107
+ _OBJC_$_PROP_LIST__SFPBFormattedText.6155
+ _OBJC_$_PROP_LIST__SFPBGradientColor.6183
+ _OBJC_$_PROP_LIST__SFPBGraphicalFloat.6197
+ _OBJC_$_PROP_LIST__SFPBGridCardSection.6204
+ _OBJC_$_PROP_LIST__SFPBHashBucketDetail.6234
+ _OBJC_$_PROP_LIST__SFPBHashBucketDetail_HashDetail.6285
+ _OBJC_$_PROP_LIST__SFPBHeroCardSection.6292
+ _OBJC_$_PROP_LIST__SFPBHeroTitleCardSection.6307
+ _OBJC_$_PROP_LIST__SFPBHorizontalButtonCardSection.6326
+ _OBJC_$_PROP_LIST__SFPBHorizontalScrollCardSection.6333
+ _OBJC_$_PROP_LIST__SFPBImage.6637
+ _OBJC_$_PROP_LIST__SFPBImageCopyItem.6644
+ _OBJC_$_PROP_LIST__SFPBImageDerivedColor.6651
+ _OBJC_$_PROP_LIST__SFPBImageOption.6679
+ _OBJC_$_PROP_LIST__SFPBImagesCardSection.6707
+ _OBJC_$_PROP_LIST__SFPBIndexState.6753
+ _OBJC_$_PROP_LIST__SFPBIndexedUserActivityCommand.6768
+ _OBJC_$_PROP_LIST__SFPBInfoCardSection.6798
+ _OBJC_$_PROP_LIST__SFPBInfoTuple.6842
+ _OBJC_$_PROP_LIST__SFPBInvokeSiriCommand.6857
+ _OBJC_$_PROP_LIST__SFPBKeyValueDataCardSection.6888
+ _OBJC_$_PROP_LIST__SFPBKeyValueTuple.6896
+ _OBJC_$_PROP_LIST__SFPBLargeTitleDetailedRowCardSection.6926
+ _OBJC_$_PROP_LIST__SFPBLatLng.6948
+ _OBJC_$_PROP_LIST__SFPBLaunchAppCommand.6955
+ _OBJC_$_PROP_LIST__SFPBLeadingTrailingCardSection.6994
+ _OBJC_$_PROP_LIST__SFPBLinkPresentationCardSection.7024
+ _OBJC_$_PROP_LIST__SFPBListenToCardSection.7055
+ _OBJC_$_PROP_LIST__SFPBLocalImage.7069
+ _OBJC_$_PROP_LIST__SFPBLocationTypeInfo.7084
+ _OBJC_$_PROP_LIST__SFPBMailRankingSignals.7618
+ _OBJC_$_PROP_LIST__SFPBMailResultDetails.7648
+ _OBJC_$_PROP_LIST__SFPBManageReservationCommand.7654
+ _OBJC_$_PROP_LIST__SFPBMapCardSection.7730
+ _OBJC_$_PROP_LIST__SFPBMapPlaceCardSection.7745
+ _OBJC_$_PROP_LIST__SFPBMapRegion.7791
+ _OBJC_$_PROP_LIST__SFPBMapsDetailedRowCardSection.7806
+ _OBJC_$_PROP_LIST__SFPBMediaArtworkImage.7821
+ _OBJC_$_PROP_LIST__SFPBMediaDetail.7836
+ _OBJC_$_PROP_LIST__SFPBMediaInfoCardSection.7950
+ _OBJC_$_PROP_LIST__SFPBMediaItem.8030
+ _OBJC_$_PROP_LIST__SFPBMediaMetadata.8110
+ _OBJC_$_PROP_LIST__SFPBMediaOffer.8149
+ _OBJC_$_PROP_LIST__SFPBMediaPlayerCardSection.8169
+ _OBJC_$_PROP_LIST__SFPBMediaRemoteControlCardSection.8200
+ _OBJC_$_PROP_LIST__SFPBMessageAttachment.8215
+ _OBJC_$_PROP_LIST__SFPBMessageCardSection.8267
+ _OBJC_$_PROP_LIST__SFPBMetaInfoCardSection.8306
+ _OBJC_$_PROP_LIST__SFPBMiniCardSection.8313
+ _OBJC_$_PROP_LIST__SFPBMonogramImage.8336
+ _OBJC_$_PROP_LIST__SFPBMoreResults.8343
+ _OBJC_$_PROP_LIST__SFPBNamedProtobufMessage.8366
+ _OBJC_$_PROP_LIST__SFPBNewsCardSection.8397
+ _OBJC_$_PROP_LIST__SFPBNowPlayingCardSection.8416
+ _OBJC_$_PROP_LIST__SFPBOpenAppClipCommand.8431
+ _OBJC_$_PROP_LIST__SFPBOpenCalculationCommand.8462
+ _OBJC_$_PROP_LIST__SFPBOpenCoreSpotlightItemCommand.8477
+ _OBJC_$_PROP_LIST__SFPBOpenFileProviderItemCommand.8492
+ _OBJC_$_PROP_LIST__SFPBOpenMediaCommand.8507
+ _OBJC_$_PROP_LIST__SFPBOpenPunchoutCommand.8514
+ _OBJC_$_PROP_LIST__SFPBOpenWebClipCommand.8521
+ _OBJC_$_PROP_LIST__SFPBPatternModel.8560
+ _OBJC_$_PROP_LIST__SFPBPerformContactActionCommand.8590
+ _OBJC_$_PROP_LIST__SFPBPerformContactQueryCommand.8597
+ _OBJC_$_PROP_LIST__SFPBPerformEntityQueryCommand.8668
+ _OBJC_$_PROP_LIST__SFPBPerformIntentCommand.8691
+ _OBJC_$_PROP_LIST__SFPBPerformPersonEntityQueryCommand.8698
+ _OBJC_$_PROP_LIST__SFPBPerson.8753
+ _OBJC_$_PROP_LIST__SFPBPersonHeaderCardSection.8760
+ _OBJC_$_PROP_LIST__SFPBPhotosAggregatedInfo.8790
+ _OBJC_$_PROP_LIST__SFPBPhotosAlbumImage.8805
+ _OBJC_$_PROP_LIST__SFPBPhotosAttributes.8859
+ _OBJC_$_PROP_LIST__SFPBPhotosLibraryImage.8895
+ _OBJC_$_PROP_LIST__SFPBPhotosMemoryImage.8910
+ _OBJC_$_PROP_LIST__SFPBPhotosRankingInfo.8940
+ _OBJC_$_PROP_LIST__SFPBPin.8955
+ _OBJC_$_PROP_LIST__SFPBPlayAudioButtonItem.8988
+ _OBJC_$_PROP_LIST__SFPBPlayMediaCommand.9011
+ _OBJC_$_PROP_LIST__SFPBPlayVideoCommand.9018
+ _OBJC_$_PROP_LIST__SFPBPlayWatchListItemButtonItem.9038
+ _OBJC_$_PROP_LIST__SFPBPointSize.9061
+ _OBJC_$_PROP_LIST__SFPBProduct.9092
+ _OBJC_$_PROP_LIST__SFPBProductAvailability.9114
+ _OBJC_$_PROP_LIST__SFPBProductCardSection.9129
+ _OBJC_$_PROP_LIST__SFPBProductInventory.9185
+ _OBJC_$_PROP_LIST__SFPBProductInventoryResult.9208
+ _OBJC_$_PROP_LIST__SFPBPunchout.9273
+ _OBJC_$_PROP_LIST__SFPBQueryUnderstandingParse.9431
+ _OBJC_$_PROP_LIST__SFPBQuickLookThumbnailImage.9439
+ _OBJC_$_PROP_LIST__SFPBRFAppIconImage.9459
+ _OBJC_$_PROP_LIST__SFPBRFAspectRatio.9467
+ _OBJC_$_PROP_LIST__SFPBRFAttribution.9519
+ _OBJC_$_PROP_LIST__SFPBRFAvatarImage.9538
+ _OBJC_$_PROP_LIST__SFPBRFBadgedImage.9552
+ _OBJC_$_PROP_LIST__SFPBRFBinaryButtonCardSection.9575
+ _OBJC_$_PROP_LIST__SFPBRFButtonCardSection.9583
+ _OBJC_$_PROP_LIST__SFPBRFColor.9617
+ _OBJC_$_PROP_LIST__SFPBRFDefaultBrowserAppIconImage.9623
+ _OBJC_$_PROP_LIST__SFPBRFDisambiguationTitleCardSection.9639
+ _OBJC_$_PROP_LIST__SFPBRFEngageable.9668
+ _OBJC_$_PROP_LIST__SFPBRFExpandableStandardCardSection.9703
+ _OBJC_$_PROP_LIST__SFPBRFExpandingComponentContent.9726
+ _OBJC_$_PROP_LIST__SFPBRFFactItemButtonCardSection.9811
+ _OBJC_$_PROP_LIST__SFPBRFFactItemDetailedNumberCardSection.9830
+ _OBJC_$_PROP_LIST__SFPBRFFactItemHeroButtonCardSection.9837
+ _OBJC_$_PROP_LIST__SFPBRFFactItemHeroNumberCardSection.9870
+ _OBJC_$_PROP_LIST__SFPBRFFactItemImageRightCardSection.9877
+ _OBJC_$_PROP_LIST__SFPBRFFactItemShortHeroNumberCardSection.9884
+ _OBJC_$_PROP_LIST__SFPBRFFactItemShortNumberCardSection.9891
+ _OBJC_$_PROP_LIST__SFPBRFFactItemStandardCardSection.9907
+ _OBJC_$_PROP_LIST__SFPBRFFont.9935
+ _OBJC_$_PROP_LIST__SFPBRFFont_RFSystemFont.11038
+ _OBJC_$_PROP_LIST__SFPBRFFormattedText.10089
+ _OBJC_$_PROP_LIST__SFPBRFHighlightedSubstring.10104
+ _OBJC_$_PROP_LIST__SFPBRFImageElement.10124
+ _OBJC_$_PROP_LIST__SFPBRFImageSource.10223
+ _OBJC_$_PROP_LIST__SFPBRFLongItemStandardCardSection.10246
+ _OBJC_$_PROP_LIST__SFPBRFMapAnnotation.10276
+ _OBJC_$_PROP_LIST__SFPBRFMapCardSection.10343
+ _OBJC_$_PROP_LIST__SFPBRFMapMarker.10376
+ _OBJC_$_PROP_LIST__SFPBRFMapMarkerIdentifier.10407
+ _OBJC_$_PROP_LIST__SFPBRFMapMarkerImage.10422
+ _OBJC_$_PROP_LIST__SFPBRFMapMarkerText.10430
+ _OBJC_$_PROP_LIST__SFPBRFMapPoint.10452
+ _OBJC_$_PROP_LIST__SFPBRFMonogramImage.10467
+ _OBJC_$_PROP_LIST__SFPBRFMultiButtonCardSection.10482
+ _OBJC_$_PROP_LIST__SFPBRFOptionalBool.10489
+ _OBJC_$_PROP_LIST__SFPBRFOptionalFloat.10496
+ _OBJC_$_PROP_LIST__SFPBRFPreview.10503
+ _OBJC_$_PROP_LIST__SFPBRFPreviewList.10525
+ _OBJC_$_PROP_LIST__SFPBRFPrimaryHeaderMarqueeCardSection.10540
+ _OBJC_$_PROP_LIST__SFPBRFPrimaryHeaderRichCardSection.10547
+ _OBJC_$_PROP_LIST__SFPBRFPrimaryHeaderStackedImageCardSection.10555
+ _OBJC_$_PROP_LIST__SFPBRFPrimaryHeaderStandardCardSection.10562
+ _OBJC_$_PROP_LIST__SFPBRFRGBValue.10592
+ _OBJC_$_PROP_LIST__SFPBRFReferenceCenteredCardSection.10604
+ _OBJC_$_PROP_LIST__SFPBRFReferenceFootnoteCardSection.10611
+ _OBJC_$_PROP_LIST__SFPBRFReferenceItemButtonCardSection.10618
+ _OBJC_$_PROP_LIST__SFPBRFReferenceItemLogoCardSection.10625
+ _OBJC_$_PROP_LIST__SFPBRFReferenceRichCardSection.10632
+ _OBJC_$_PROP_LIST__SFPBRFReferenceStandardCardSection.10639
+ _OBJC_$_PROP_LIST__SFPBRFSecondaryHeaderEmphasizedCardSection.10646
+ _OBJC_$_PROP_LIST__SFPBRFSecondaryHeaderStandardCardSection.10653
+ _OBJC_$_PROP_LIST__SFPBRFShowMoreOnTap.10668
+ _OBJC_$_PROP_LIST__SFPBRFSimpleItemPlayerCardSection.10683
+ _OBJC_$_PROP_LIST__SFPBRFSimpleItemReverseRichCardSection.10690
+ _OBJC_$_PROP_LIST__SFPBRFSimpleItemRichCardSection.10721
+ _OBJC_$_PROP_LIST__SFPBRFSimpleItemRichSearchResultCardSection.10728
+ _OBJC_$_PROP_LIST__SFPBRFSimpleItemStandardCardSection.10735
+ _OBJC_$_PROP_LIST__SFPBRFSimpleItemVisualElementCardSection.10759
+ _OBJC_$_PROP_LIST__SFPBRFSummaryItemAlignedTextCardSection.10775
+ _OBJC_$_PROP_LIST__SFPBRFSummaryItemAttribution.10799
+ _OBJC_$_PROP_LIST__SFPBRFSummaryItemButtonCardSection.10806
+ _OBJC_$_PROP_LIST__SFPBRFSummaryItemDetailedTextCardSection.10813
+ _OBJC_$_PROP_LIST__SFPBRFSummaryItemExpandableCardSection.10844
+ _OBJC_$_PROP_LIST__SFPBRFSummaryItemExpandableContent.10859
+ _OBJC_$_PROP_LIST__SFPBRFSummaryItemImageRightCardSection.10879
+ _OBJC_$_PROP_LIST__SFPBRFSummaryItemPairCardSection.10886
+ _OBJC_$_PROP_LIST__SFPBRFSummaryItemPairNumberCardSection.10925
+ _OBJC_$_PROP_LIST__SFPBRFSummaryItemPlayerCardSection.10932
+ _OBJC_$_PROP_LIST__SFPBRFSummaryItemShortNumberCardSection.10939
+ _OBJC_$_PROP_LIST__SFPBRFSummaryItemStandardCardSection.10954
+ _OBJC_$_PROP_LIST__SFPBRFSummaryItemSwitchV2CardSection.10969
+ _OBJC_$_PROP_LIST__SFPBRFSummaryItemTextCardSection.10976
+ _OBJC_$_PROP_LIST__SFPBRFSymbolImage.11031
+ _OBJC_$_PROP_LIST__SFPBRFTableCell.11065
+ _OBJC_$_PROP_LIST__SFPBRFTableColumnDefinition.11095
+ _OBJC_$_PROP_LIST__SFPBRFTableContentColumnDefinition.11141
+ _OBJC_$_PROP_LIST__SFPBRFTableHeaderCardSection.11206
+ _OBJC_$_PROP_LIST__SFPBRFTableRowCardSection.11221
+ _OBJC_$_PROP_LIST__SFPBRFTableSpacerColumnDefinition.11227
+ _OBJC_$_PROP_LIST__SFPBRFTextElement.11271
+ _OBJC_$_PROP_LIST__SFPBRFTextEncapsulation.11277
+ _OBJC_$_PROP_LIST__SFPBRFTextProperty.11307
+ _OBJC_$_PROP_LIST__SFPBRFUrlImage.11371
+ _OBJC_$_PROP_LIST__SFPBRFVisualElement.11390
+ _OBJC_$_PROP_LIST__SFPBRFVisualProperty.11412
+ _OBJC_$_PROP_LIST__SFPBRFVisualPropertyWithAction.11427
+ _OBJC_$_PROP_LIST__SFPBReferentialCommand.11434
+ _OBJC_$_PROP_LIST__SFPBRejectPeopleInPhotoCommand.11454
+ _OBJC_$_PROP_LIST__SFPBReminder.11469
+ _OBJC_$_PROP_LIST__SFPBRequestAppClipInstallCommand.11476
+ _OBJC_$_PROP_LIST__SFPBRequestProductPageCommand.11507
+ _OBJC_$_PROP_LIST__SFPBRequestUserReportCommand.11514
+ _OBJC_$_PROP_LIST__SFPBResponseWrapperCardSection.11568
+ _OBJC_$_PROP_LIST__SFPBResultEntity.11596
+ _OBJC_$_PROP_LIST__SFPBRichText.11636
+ _OBJC_$_PROP_LIST__SFPBRichTitleCardSection.11784
+ _OBJC_$_PROP_LIST__SFPBRowCardSection.11879
+ _OBJC_$_PROP_LIST__SFPBRunVoiceShortcutCommand.11894
+ _OBJC_$_PROP_LIST__SFPBSafariAttributes.11908
+ _OBJC_$_PROP_LIST__SFPBSafariTableOfContentsCardSection.11954
+ _OBJC_$_PROP_LIST__SFPBSafariTableOfContentsItem.11970
+ _OBJC_$_PROP_LIST__SFPBScene.11992
+ _OBJC_$_PROP_LIST__SFPBScoreboardCardSection.12036
+ _OBJC_$_PROP_LIST__SFPBSearchInAppCommand.12051
+ _OBJC_$_PROP_LIST__SFPBSearchSuggestion.12129
+ _OBJC_$_PROP_LIST__SFPBSearchWebCommand.12136
+ _OBJC_$_PROP_LIST__SFPBSectionHeaderCardSection.12144
+ _OBJC_$_PROP_LIST__SFPBSelectableGridCardSection.12174
+ _OBJC_$_PROP_LIST__SFPBShareCommand.12207
+ _OBJC_$_PROP_LIST__SFPBShareItem.12240
+ _OBJC_$_PROP_LIST__SFPBShortcutsImage.12255
+ _OBJC_$_PROP_LIST__SFPBShowAppStoreSheetCommand.12270
+ _OBJC_$_PROP_LIST__SFPBShowContactCardCommand.12285
+ _OBJC_$_PROP_LIST__SFPBShowPhotosOneUpViewCommand.12336
+ _OBJC_$_PROP_LIST__SFPBShowPurchaseRequestSheetCommand.12351
+ _OBJC_$_PROP_LIST__SFPBShowSFCardCommand.12366
+ _OBJC_$_PROP_LIST__SFPBShowScreenTimeRequestSheetCommand.12373
+ _OBJC_$_PROP_LIST__SFPBShowWrapperResponseViewCommand.12380
+ _OBJC_$_PROP_LIST__SFPBSocialMediaPostCardSection.12444
+ _OBJC_$_PROP_LIST__SFPBSplitCardSection.12511
+ _OBJC_$_PROP_LIST__SFPBSportsDetail.12526
+ _OBJC_$_PROP_LIST__SFPBSportsFollowButtonItem.12554
+ _OBJC_$_PROP_LIST__SFPBSportsItem.12561
+ _OBJC_$_PROP_LIST__SFPBSportsSubscriptionRequestItem.12592
+ _OBJC_$_PROP_LIST__SFPBSportsTeam.12624
+ _OBJC_$_PROP_LIST__SFPBStockChartCardSection.12647
+ _OBJC_$_PROP_LIST__SFPBStoreButtonItem.12670
+ _OBJC_$_PROP_LIST__SFPBStringDictionary.12689
+ _OBJC_$_PROP_LIST__SFPBStrokeAnimationCardSection.12740
+ _OBJC_$_PROP_LIST__SFPBStructuredLocation.12763
+ _OBJC_$_PROP_LIST__SFPBSubscribeForUpdatesCommand.12796
+ _OBJC_$_PROP_LIST__SFPBSuggestionCardSection.12835
+ _OBJC_$_PROP_LIST__SFPBSymbolImage.12877
+ _OBJC_$_PROP_LIST__SFPBTableAlignmentSchema.12901
+ _OBJC_$_PROP_LIST__SFPBTableColumnAlignment.12931
+ _OBJC_$_PROP_LIST__SFPBTableHeaderRowCardSection.12999
+ _OBJC_$_PROP_LIST__SFPBTableRowCardSection.13019
+ _OBJC_$_PROP_LIST__SFPBText.13036
+ _OBJC_$_PROP_LIST__SFPBTextColumn.13058
+ _OBJC_$_PROP_LIST__SFPBTextColumnSection.13093
+ _OBJC_$_PROP_LIST__SFPBTextColumnsCardSection.13104
+ _OBJC_$_PROP_LIST__SFPBTextCopyItem.13119
+ _OBJC_$_PROP_LIST__SFPBTimeZone.13126
+ _OBJC_$_PROP_LIST__SFPBTitleCardSection.13133
+ _OBJC_$_PROP_LIST__SFPBTitleSubtitleTuple.13140
+ _OBJC_$_PROP_LIST__SFPBToggleAudioCommand.13163
+ _OBJC_$_PROP_LIST__SFPBToggleButtonConfiguration.13187
+ _OBJC_$_PROP_LIST__SFPBToggleWatchListStatusCommand.13202
+ _OBJC_$_PROP_LIST__SFPBTopic.13245
+ _OBJC_$_PROP_LIST__SFPBTrack.13277
+ _OBJC_$_PROP_LIST__SFPBTrackListCardSection.13299
+ _OBJC_$_PROP_LIST__SFPBURL.13306
+ _OBJC_$_PROP_LIST__SFPBURLCopyItem.13313
+ _OBJC_$_PROP_LIST__SFPBURLImage.13328
+ _OBJC_$_PROP_LIST__SFPBURLShareItem.13335
+ _OBJC_$_PROP_LIST__SFPBUpdateSearchQueryCommand.13350
+ _OBJC_$_PROP_LIST__SFPBUpdateSportsFollowingStatusCommand.13365
+ _OBJC_$_PROP_LIST__SFPBUserActivityData.13396
+ _OBJC_$_PROP_LIST__SFPBUserActivityInfo.13419
+ _OBJC_$_PROP_LIST__SFPBUserReportRequest.13494
+ _OBJC_$_PROP_LIST__SFPBVerticalLayoutCardSection.13525
+ _OBJC_$_PROP_LIST__SFPBViewEmailCommand.13531
+ _OBJC_$_PROP_LIST__SFPBWatchListButtonItem.13538
+ _OBJC_$_PROP_LIST__SFPBWatchListCardSection.13545
+ _OBJC_$_PROP_LIST__SFPBWatchListItem.13624
+ _OBJC_$_PROP_LIST__SFPBWatchNowCardSection.13638
+ _OBJC_$_PROP_LIST__SFPBWeatherColor.13685
+ _OBJC_$_PROP_LIST__SFPBWeatherDetails.13692
+ _OBJC_$_PROP_LIST__SFPBWebCardSection.13707
+ _OBJC_$_PROP_LIST__SFPBWorldMapCardSection.13730
+ _OBJC_CLASS_$_RFSummaryItemAttribution
+ _OBJC_CLASS_$_RFSummaryItemExpandableCardSection
+ _OBJC_CLASS_$_RFSummaryItemExpandableContent
+ _OBJC_CLASS_$_SFFillToolAppEntityParameterCommand
+ _OBJC_CLASS_$_SFFillToolAppParameterCommand
+ _OBJC_CLASS_$_SFFillToolFileParameterCommand
+ _OBJC_CLASS_$_SFFillToolParameterCommand
+ _OBJC_CLASS_$_SFFillToolPersonParameterCommand
+ _OBJC_CLASS_$_SFPhotosAlbumImage
+ _OBJC_CLASS_$_SFPhotosMemoryImage
+ _OBJC_CLASS_$_SFURLCopyItem
+ _OBJC_CLASS_$__SFPBFillToolAppEntityParameterCommand
+ _OBJC_CLASS_$__SFPBFillToolAppParameterCommand
+ _OBJC_CLASS_$__SFPBFillToolFileParameterCommand
+ _OBJC_CLASS_$__SFPBFillToolParameterCommand
+ _OBJC_CLASS_$__SFPBFillToolPersonParameterCommand
+ _OBJC_CLASS_$__SFPBPhotosAlbumImage
+ _OBJC_CLASS_$__SFPBPhotosMemoryImage
+ _OBJC_CLASS_$__SFPBRFSummaryItemAttribution
+ _OBJC_CLASS_$__SFPBRFSummaryItemExpandableCardSection
+ _OBJC_CLASS_$__SFPBRFSummaryItemExpandableContent
+ _OBJC_CLASS_$__SFPBURLCopyItem
+ _OBJC_METACLASS_$_RFSummaryItemAttribution
+ _OBJC_METACLASS_$_RFSummaryItemExpandableCardSection
+ _OBJC_METACLASS_$_RFSummaryItemExpandableContent
+ _OBJC_METACLASS_$_SFFillToolAppEntityParameterCommand
+ _OBJC_METACLASS_$_SFFillToolAppParameterCommand
+ _OBJC_METACLASS_$_SFFillToolFileParameterCommand
+ _OBJC_METACLASS_$_SFFillToolParameterCommand
+ _OBJC_METACLASS_$_SFFillToolPersonParameterCommand
+ _OBJC_METACLASS_$_SFPhotosAlbumImage
+ _OBJC_METACLASS_$_SFPhotosMemoryImage
+ _OBJC_METACLASS_$_SFURLCopyItem
+ _OBJC_METACLASS_$__SFPBFillToolAppEntityParameterCommand
+ _OBJC_METACLASS_$__SFPBFillToolAppParameterCommand
+ _OBJC_METACLASS_$__SFPBFillToolFileParameterCommand
+ _OBJC_METACLASS_$__SFPBFillToolParameterCommand
+ _OBJC_METACLASS_$__SFPBFillToolPersonParameterCommand
+ _OBJC_METACLASS_$__SFPBPhotosAlbumImage
+ _OBJC_METACLASS_$__SFPBPhotosMemoryImage
+ _OBJC_METACLASS_$__SFPBRFSummaryItemAttribution
+ _OBJC_METACLASS_$__SFPBRFSummaryItemExpandableCardSection
+ _OBJC_METACLASS_$__SFPBRFSummaryItemExpandableContent
+ _OBJC_METACLASS_$__SFPBURLCopyItem
+ __OBJC_$_CLASS_METHODS_RFSummaryItemAttribution
+ __OBJC_$_CLASS_METHODS_RFSummaryItemExpandableCardSection
+ __OBJC_$_CLASS_METHODS_RFSummaryItemExpandableContent
+ __OBJC_$_CLASS_METHODS_SFFillToolAppEntityParameterCommand
+ __OBJC_$_CLASS_METHODS_SFFillToolAppParameterCommand
+ __OBJC_$_CLASS_METHODS_SFFillToolFileParameterCommand
+ __OBJC_$_CLASS_METHODS_SFFillToolParameterCommand
+ __OBJC_$_CLASS_METHODS_SFFillToolPersonParameterCommand
+ __OBJC_$_CLASS_METHODS_SFPhotosAlbumImage
+ __OBJC_$_CLASS_METHODS_SFPhotosMemoryImage
+ __OBJC_$_CLASS_METHODS_SFURLCopyItem
+ __OBJC_$_CLASS_PROP_LIST_RFSummaryItemAttribution
+ __OBJC_$_CLASS_PROP_LIST_RFSummaryItemExpandableCardSection
+ __OBJC_$_CLASS_PROP_LIST_RFSummaryItemExpandableContent
+ __OBJC_$_CLASS_PROP_LIST_SFFillToolAppEntityParameterCommand
+ __OBJC_$_CLASS_PROP_LIST_SFFillToolAppParameterCommand
+ __OBJC_$_CLASS_PROP_LIST_SFFillToolFileParameterCommand
+ __OBJC_$_CLASS_PROP_LIST_SFFillToolParameterCommand
+ __OBJC_$_CLASS_PROP_LIST_SFFillToolPersonParameterCommand
+ __OBJC_$_CLASS_PROP_LIST_SFPhotosAlbumImage
+ __OBJC_$_CLASS_PROP_LIST_SFPhotosMemoryImage
+ __OBJC_$_CLASS_PROP_LIST_SFURLCopyItem
+ __OBJC_$_CLASS_PROP_LIST__SFPBFillToolAppEntityParameterCommand
+ __OBJC_$_CLASS_PROP_LIST__SFPBFillToolAppParameterCommand
+ __OBJC_$_CLASS_PROP_LIST__SFPBFillToolFileParameterCommand
+ __OBJC_$_CLASS_PROP_LIST__SFPBFillToolParameterCommand
+ __OBJC_$_CLASS_PROP_LIST__SFPBFillToolPersonParameterCommand
+ __OBJC_$_CLASS_PROP_LIST__SFPBPhotosAlbumImage
+ __OBJC_$_CLASS_PROP_LIST__SFPBPhotosMemoryImage
+ __OBJC_$_CLASS_PROP_LIST__SFPBRFSummaryItemAttribution
+ __OBJC_$_CLASS_PROP_LIST__SFPBRFSummaryItemExpandableCardSection
+ __OBJC_$_CLASS_PROP_LIST__SFPBRFSummaryItemExpandableContent
+ __OBJC_$_CLASS_PROP_LIST__SFPBURLCopyItem
+ __OBJC_$_INSTANCE_METHODS_RFSummaryItemAttribution(ProtobufInitializer)
+ __OBJC_$_INSTANCE_METHODS_RFSummaryItemExpandableCardSection(ProtobufInitializer)
+ __OBJC_$_INSTANCE_METHODS_RFSummaryItemExpandableContent(ProtobufInitializer)
+ __OBJC_$_INSTANCE_METHODS_SFFillToolAppEntityParameterCommand(ProtobufInitializer)
+ __OBJC_$_INSTANCE_METHODS_SFFillToolAppParameterCommand(ProtobufInitializer)
+ __OBJC_$_INSTANCE_METHODS_SFFillToolFileParameterCommand(ProtobufInitializer)
+ __OBJC_$_INSTANCE_METHODS_SFFillToolParameterCommand(ProtobufInitializer)
+ __OBJC_$_INSTANCE_METHODS_SFFillToolPersonParameterCommand(ProtobufInitializer)
+ __OBJC_$_INSTANCE_METHODS_SFPhotosAlbumImage(ProtobufInitializer)
+ __OBJC_$_INSTANCE_METHODS_SFPhotosMemoryImage(ProtobufInitializer)
+ __OBJC_$_INSTANCE_METHODS_SFURLCopyItem(ProtobufInitializer)
+ __OBJC_$_INSTANCE_METHODS__SFPBFillToolAppEntityParameterCommand(FacadeInitializer)
+ __OBJC_$_INSTANCE_METHODS__SFPBFillToolAppParameterCommand(FacadeInitializer)
+ __OBJC_$_INSTANCE_METHODS__SFPBFillToolFileParameterCommand(FacadeInitializer)
+ __OBJC_$_INSTANCE_METHODS__SFPBFillToolParameterCommand(FacadeInitializer)
+ __OBJC_$_INSTANCE_METHODS__SFPBFillToolPersonParameterCommand(FacadeInitializer)
+ __OBJC_$_INSTANCE_METHODS__SFPBPhotosAlbumImage(FacadeInitializer)
+ __OBJC_$_INSTANCE_METHODS__SFPBPhotosMemoryImage(FacadeInitializer)
+ __OBJC_$_INSTANCE_METHODS__SFPBRFSummaryItemAttribution(FacadeInitializer)
+ __OBJC_$_INSTANCE_METHODS__SFPBRFSummaryItemExpandableCardSection(FacadeInitializer)
+ __OBJC_$_INSTANCE_METHODS__SFPBRFSummaryItemExpandableContent(FacadeInitializer)
+ __OBJC_$_INSTANCE_METHODS__SFPBURLCopyItem(FacadeInitializer)
+ __OBJC_$_INSTANCE_VARIABLES_RFSummaryItemAttribution
+ __OBJC_$_INSTANCE_VARIABLES_RFSummaryItemExpandableCardSection
+ __OBJC_$_INSTANCE_VARIABLES_RFSummaryItemExpandableContent
+ __OBJC_$_INSTANCE_VARIABLES_SFFillToolAppEntityParameterCommand
+ __OBJC_$_INSTANCE_VARIABLES_SFFillToolAppParameterCommand
+ __OBJC_$_INSTANCE_VARIABLES_SFFillToolFileParameterCommand
+ __OBJC_$_INSTANCE_VARIABLES_SFFillToolParameterCommand
+ __OBJC_$_INSTANCE_VARIABLES_SFFillToolPersonParameterCommand
+ __OBJC_$_INSTANCE_VARIABLES_SFPhotosAlbumImage
+ __OBJC_$_INSTANCE_VARIABLES_SFPhotosMemoryImage
+ __OBJC_$_INSTANCE_VARIABLES_SFURLCopyItem
+ __OBJC_$_INSTANCE_VARIABLES__SFPBFillToolAppEntityParameterCommand
+ __OBJC_$_INSTANCE_VARIABLES__SFPBFillToolAppParameterCommand
+ __OBJC_$_INSTANCE_VARIABLES__SFPBFillToolFileParameterCommand
+ __OBJC_$_INSTANCE_VARIABLES__SFPBFillToolParameterCommand
+ __OBJC_$_INSTANCE_VARIABLES__SFPBFillToolPersonParameterCommand
+ __OBJC_$_INSTANCE_VARIABLES__SFPBPhotosAlbumImage
+ __OBJC_$_INSTANCE_VARIABLES__SFPBPhotosMemoryImage
+ __OBJC_$_INSTANCE_VARIABLES__SFPBRFSummaryItemAttribution
+ __OBJC_$_INSTANCE_VARIABLES__SFPBRFSummaryItemExpandableCardSection
+ __OBJC_$_INSTANCE_VARIABLES__SFPBRFSummaryItemExpandableContent
+ __OBJC_$_INSTANCE_VARIABLES__SFPBURLCopyItem
+ __OBJC_$_PROP_LIST_RFSummaryItemAttribution
+ __OBJC_$_PROP_LIST_RFSummaryItemExpandableCardSection
+ __OBJC_$_PROP_LIST_RFSummaryItemExpandableContent
+ __OBJC_$_PROP_LIST_SFFillToolAppEntityParameterCommand
+ __OBJC_$_PROP_LIST_SFFillToolAppParameterCommand
+ __OBJC_$_PROP_LIST_SFFillToolFileParameterCommand
+ __OBJC_$_PROP_LIST_SFFillToolParameterCommand
+ __OBJC_$_PROP_LIST_SFFillToolPersonParameterCommand
+ __OBJC_$_PROP_LIST_SFPhotosAlbumImage
+ __OBJC_$_PROP_LIST_SFPhotosMemoryImage
+ __OBJC_$_PROP_LIST_SFURLCopyItem
+ __OBJC_$_PROP_LIST__SFPBFillToolAppEntityParameterCommand
+ __OBJC_$_PROP_LIST__SFPBFillToolAppParameterCommand
+ __OBJC_$_PROP_LIST__SFPBFillToolFileParameterCommand
+ __OBJC_$_PROP_LIST__SFPBFillToolParameterCommand
+ __OBJC_$_PROP_LIST__SFPBFillToolPersonParameterCommand
+ __OBJC_$_PROP_LIST__SFPBPhotosAlbumImage
+ __OBJC_$_PROP_LIST__SFPBPhotosMemoryImage
+ __OBJC_$_PROP_LIST__SFPBRFSummaryItemAttribution
+ __OBJC_$_PROP_LIST__SFPBRFSummaryItemExpandableCardSection
+ __OBJC_$_PROP_LIST__SFPBRFSummaryItemExpandableContent
+ __OBJC_$_PROP_LIST__SFPBURLCopyItem
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_RFSummaryItemAttribution
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_RFSummaryItemExpandableCardSection
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_RFSummaryItemExpandableContent
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SFFillToolAppEntityParameterCommand
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SFFillToolAppParameterCommand
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SFFillToolFileParameterCommand
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SFFillToolParameterCommand
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SFFillToolPersonParameterCommand
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SFPhotosAlbumImage
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SFPhotosMemoryImage
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SFURLCopyItem
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__SFPBFillToolAppEntityParameterCommand
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__SFPBFillToolAppParameterCommand
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__SFPBFillToolFileParameterCommand
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__SFPBFillToolParameterCommand
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__SFPBFillToolPersonParameterCommand
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__SFPBPhotosAlbumImage
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__SFPBPhotosMemoryImage
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__SFPBRFSummaryItemAttribution
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__SFPBRFSummaryItemExpandableCardSection
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__SFPBRFSummaryItemExpandableContent
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__SFPBURLCopyItem
+ __OBJC_$_PROTOCOL_METHOD_TYPES_RFSummaryItemAttribution
+ __OBJC_$_PROTOCOL_METHOD_TYPES_RFSummaryItemExpandableCardSection
+ __OBJC_$_PROTOCOL_METHOD_TYPES_RFSummaryItemExpandableContent
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SFFillToolAppEntityParameterCommand
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SFFillToolAppParameterCommand
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SFFillToolFileParameterCommand
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SFFillToolParameterCommand
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SFFillToolPersonParameterCommand
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SFPhotosAlbumImage
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SFPhotosMemoryImage
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SFURLCopyItem
+ __OBJC_$_PROTOCOL_METHOD_TYPES__SFPBFillToolAppEntityParameterCommand
+ __OBJC_$_PROTOCOL_METHOD_TYPES__SFPBFillToolAppParameterCommand
+ __OBJC_$_PROTOCOL_METHOD_TYPES__SFPBFillToolFileParameterCommand
+ __OBJC_$_PROTOCOL_METHOD_TYPES__SFPBFillToolParameterCommand
+ __OBJC_$_PROTOCOL_METHOD_TYPES__SFPBFillToolPersonParameterCommand
+ __OBJC_$_PROTOCOL_METHOD_TYPES__SFPBPhotosAlbumImage
+ __OBJC_$_PROTOCOL_METHOD_TYPES__SFPBPhotosMemoryImage
+ __OBJC_$_PROTOCOL_METHOD_TYPES__SFPBRFSummaryItemAttribution
+ __OBJC_$_PROTOCOL_METHOD_TYPES__SFPBRFSummaryItemExpandableCardSection
+ __OBJC_$_PROTOCOL_METHOD_TYPES__SFPBRFSummaryItemExpandableContent
+ __OBJC_$_PROTOCOL_METHOD_TYPES__SFPBURLCopyItem
+ __OBJC_$_PROTOCOL_REFS_RFSummaryItemAttribution
+ __OBJC_$_PROTOCOL_REFS_RFSummaryItemExpandableCardSection
+ __OBJC_$_PROTOCOL_REFS_RFSummaryItemExpandableContent
+ __OBJC_$_PROTOCOL_REFS_SFFillToolAppEntityParameterCommand
+ __OBJC_$_PROTOCOL_REFS_SFFillToolAppParameterCommand
+ __OBJC_$_PROTOCOL_REFS_SFFillToolFileParameterCommand
+ __OBJC_$_PROTOCOL_REFS_SFFillToolParameterCommand
+ __OBJC_$_PROTOCOL_REFS_SFFillToolPersonParameterCommand
+ __OBJC_$_PROTOCOL_REFS_SFPhotosAlbumImage
+ __OBJC_$_PROTOCOL_REFS_SFPhotosMemoryImage
+ __OBJC_$_PROTOCOL_REFS_SFURLCopyItem
+ __OBJC_$_PROTOCOL_REFS__SFPBFillToolAppEntityParameterCommand
+ __OBJC_$_PROTOCOL_REFS__SFPBFillToolAppParameterCommand
+ __OBJC_$_PROTOCOL_REFS__SFPBFillToolFileParameterCommand
+ __OBJC_$_PROTOCOL_REFS__SFPBFillToolParameterCommand
+ __OBJC_$_PROTOCOL_REFS__SFPBFillToolPersonParameterCommand
+ __OBJC_$_PROTOCOL_REFS__SFPBPhotosAlbumImage
+ __OBJC_$_PROTOCOL_REFS__SFPBPhotosMemoryImage
+ __OBJC_$_PROTOCOL_REFS__SFPBRFSummaryItemAttribution
+ __OBJC_$_PROTOCOL_REFS__SFPBRFSummaryItemExpandableCardSection
+ __OBJC_$_PROTOCOL_REFS__SFPBRFSummaryItemExpandableContent
+ __OBJC_$_PROTOCOL_REFS__SFPBURLCopyItem
+ __OBJC_CLASS_PROTOCOLS_$_RFSummaryItemAttribution
+ __OBJC_CLASS_PROTOCOLS_$_RFSummaryItemExpandableCardSection
+ __OBJC_CLASS_PROTOCOLS_$_RFSummaryItemExpandableContent
+ __OBJC_CLASS_PROTOCOLS_$_SFFillToolAppEntityParameterCommand
+ __OBJC_CLASS_PROTOCOLS_$_SFFillToolAppParameterCommand
+ __OBJC_CLASS_PROTOCOLS_$_SFFillToolFileParameterCommand
+ __OBJC_CLASS_PROTOCOLS_$_SFFillToolParameterCommand
+ __OBJC_CLASS_PROTOCOLS_$_SFFillToolPersonParameterCommand
+ __OBJC_CLASS_PROTOCOLS_$_SFPhotosAlbumImage
+ __OBJC_CLASS_PROTOCOLS_$_SFPhotosMemoryImage
+ __OBJC_CLASS_PROTOCOLS_$_SFURLCopyItem
+ __OBJC_CLASS_PROTOCOLS_$__SFPBFillToolAppEntityParameterCommand
+ __OBJC_CLASS_PROTOCOLS_$__SFPBFillToolAppParameterCommand
+ __OBJC_CLASS_PROTOCOLS_$__SFPBFillToolFileParameterCommand
+ __OBJC_CLASS_PROTOCOLS_$__SFPBFillToolParameterCommand
+ __OBJC_CLASS_PROTOCOLS_$__SFPBFillToolPersonParameterCommand
+ __OBJC_CLASS_PROTOCOLS_$__SFPBPhotosAlbumImage
+ __OBJC_CLASS_PROTOCOLS_$__SFPBPhotosMemoryImage
+ __OBJC_CLASS_PROTOCOLS_$__SFPBRFSummaryItemAttribution
+ __OBJC_CLASS_PROTOCOLS_$__SFPBRFSummaryItemExpandableCardSection
+ __OBJC_CLASS_PROTOCOLS_$__SFPBRFSummaryItemExpandableContent
+ __OBJC_CLASS_PROTOCOLS_$__SFPBURLCopyItem
+ __OBJC_CLASS_RO_$_RFSummaryItemAttribution
+ __OBJC_CLASS_RO_$_RFSummaryItemExpandableCardSection
+ __OBJC_CLASS_RO_$_RFSummaryItemExpandableContent
+ __OBJC_CLASS_RO_$_SFFillToolAppEntityParameterCommand
+ __OBJC_CLASS_RO_$_SFFillToolAppParameterCommand
+ __OBJC_CLASS_RO_$_SFFillToolFileParameterCommand
+ __OBJC_CLASS_RO_$_SFFillToolParameterCommand
+ __OBJC_CLASS_RO_$_SFFillToolPersonParameterCommand
+ __OBJC_CLASS_RO_$_SFPhotosAlbumImage
+ __OBJC_CLASS_RO_$_SFPhotosMemoryImage
+ __OBJC_CLASS_RO_$_SFURLCopyItem
+ __OBJC_CLASS_RO_$__SFPBFillToolAppEntityParameterCommand
+ __OBJC_CLASS_RO_$__SFPBFillToolAppParameterCommand
+ __OBJC_CLASS_RO_$__SFPBFillToolFileParameterCommand
+ __OBJC_CLASS_RO_$__SFPBFillToolParameterCommand
+ __OBJC_CLASS_RO_$__SFPBFillToolPersonParameterCommand
+ __OBJC_CLASS_RO_$__SFPBPhotosAlbumImage
+ __OBJC_CLASS_RO_$__SFPBPhotosMemoryImage
+ __OBJC_CLASS_RO_$__SFPBRFSummaryItemAttribution
+ __OBJC_CLASS_RO_$__SFPBRFSummaryItemExpandableCardSection
+ __OBJC_CLASS_RO_$__SFPBRFSummaryItemExpandableContent
+ __OBJC_CLASS_RO_$__SFPBURLCopyItem
+ __OBJC_LABEL_PROTOCOL_$_RFSummaryItemAttribution
+ __OBJC_LABEL_PROTOCOL_$_RFSummaryItemExpandableCardSection
+ __OBJC_LABEL_PROTOCOL_$_RFSummaryItemExpandableContent
+ __OBJC_LABEL_PROTOCOL_$_SFFillToolAppEntityParameterCommand
+ __OBJC_LABEL_PROTOCOL_$_SFFillToolAppParameterCommand
+ __OBJC_LABEL_PROTOCOL_$_SFFillToolFileParameterCommand
+ __OBJC_LABEL_PROTOCOL_$_SFFillToolParameterCommand
+ __OBJC_LABEL_PROTOCOL_$_SFFillToolPersonParameterCommand
+ __OBJC_LABEL_PROTOCOL_$_SFPhotosAlbumImage
+ __OBJC_LABEL_PROTOCOL_$_SFPhotosMemoryImage
+ __OBJC_LABEL_PROTOCOL_$_SFURLCopyItem
+ __OBJC_LABEL_PROTOCOL_$__SFPBFillToolAppEntityParameterCommand
+ __OBJC_LABEL_PROTOCOL_$__SFPBFillToolAppParameterCommand
+ __OBJC_LABEL_PROTOCOL_$__SFPBFillToolFileParameterCommand
+ __OBJC_LABEL_PROTOCOL_$__SFPBFillToolParameterCommand
+ __OBJC_LABEL_PROTOCOL_$__SFPBFillToolPersonParameterCommand
+ __OBJC_LABEL_PROTOCOL_$__SFPBPhotosAlbumImage
+ __OBJC_LABEL_PROTOCOL_$__SFPBPhotosMemoryImage
+ __OBJC_LABEL_PROTOCOL_$__SFPBRFSummaryItemAttribution
+ __OBJC_LABEL_PROTOCOL_$__SFPBRFSummaryItemExpandableCardSection
+ __OBJC_LABEL_PROTOCOL_$__SFPBRFSummaryItemExpandableContent
+ __OBJC_LABEL_PROTOCOL_$__SFPBURLCopyItem
+ __OBJC_METACLASS_RO_$_RFSummaryItemAttribution
+ __OBJC_METACLASS_RO_$_RFSummaryItemExpandableCardSection
+ __OBJC_METACLASS_RO_$_RFSummaryItemExpandableContent
+ __OBJC_METACLASS_RO_$_SFFillToolAppEntityParameterCommand
+ __OBJC_METACLASS_RO_$_SFFillToolAppParameterCommand
+ __OBJC_METACLASS_RO_$_SFFillToolFileParameterCommand
+ __OBJC_METACLASS_RO_$_SFFillToolParameterCommand
+ __OBJC_METACLASS_RO_$_SFFillToolPersonParameterCommand
+ __OBJC_METACLASS_RO_$_SFPhotosAlbumImage
+ __OBJC_METACLASS_RO_$_SFPhotosMemoryImage
+ __OBJC_METACLASS_RO_$_SFURLCopyItem
+ __OBJC_METACLASS_RO_$__SFPBFillToolAppEntityParameterCommand
+ __OBJC_METACLASS_RO_$__SFPBFillToolAppParameterCommand
+ __OBJC_METACLASS_RO_$__SFPBFillToolFileParameterCommand
+ __OBJC_METACLASS_RO_$__SFPBFillToolParameterCommand
+ __OBJC_METACLASS_RO_$__SFPBFillToolPersonParameterCommand
+ __OBJC_METACLASS_RO_$__SFPBPhotosAlbumImage
+ __OBJC_METACLASS_RO_$__SFPBPhotosMemoryImage
+ __OBJC_METACLASS_RO_$__SFPBRFSummaryItemAttribution
+ __OBJC_METACLASS_RO_$__SFPBRFSummaryItemExpandableCardSection
+ __OBJC_METACLASS_RO_$__SFPBRFSummaryItemExpandableContent
+ __OBJC_METACLASS_RO_$__SFPBURLCopyItem
+ __OBJC_PROTOCOL_$_RFSummaryItemAttribution
+ __OBJC_PROTOCOL_$_RFSummaryItemExpandableCardSection
+ __OBJC_PROTOCOL_$_RFSummaryItemExpandableContent
+ __OBJC_PROTOCOL_$_SFFillToolAppEntityParameterCommand
+ __OBJC_PROTOCOL_$_SFFillToolAppParameterCommand
+ __OBJC_PROTOCOL_$_SFFillToolFileParameterCommand
+ __OBJC_PROTOCOL_$_SFFillToolParameterCommand
+ __OBJC_PROTOCOL_$_SFFillToolPersonParameterCommand
+ __OBJC_PROTOCOL_$_SFPhotosAlbumImage
+ __OBJC_PROTOCOL_$_SFPhotosMemoryImage
+ __OBJC_PROTOCOL_$_SFURLCopyItem
+ __OBJC_PROTOCOL_$__SFPBFillToolAppEntityParameterCommand
+ __OBJC_PROTOCOL_$__SFPBFillToolAppParameterCommand
+ __OBJC_PROTOCOL_$__SFPBFillToolFileParameterCommand
+ __OBJC_PROTOCOL_$__SFPBFillToolParameterCommand
+ __OBJC_PROTOCOL_$__SFPBFillToolPersonParameterCommand
+ __OBJC_PROTOCOL_$__SFPBPhotosAlbumImage
+ __OBJC_PROTOCOL_$__SFPBPhotosMemoryImage
+ __OBJC_PROTOCOL_$__SFPBRFSummaryItemAttribution
+ __OBJC_PROTOCOL_$__SFPBRFSummaryItemExpandableCardSection
+ __OBJC_PROTOCOL_$__SFPBRFSummaryItemExpandableContent
+ __OBJC_PROTOCOL_$__SFPBURLCopyItem
+ __PARLogHandleForCategory_block_invoke.33651
+ __PARLogHandleForCategory_block_invoke.68866
+ __SFPBFillToolAppEntityParameterCommandReadFrom
+ __SFPBFillToolAppParameterCommandReadFrom
+ __SFPBFillToolFileParameterCommandReadFrom
+ __SFPBFillToolParameterCommandReadFrom
+ __SFPBFillToolPersonParameterCommandReadFrom
+ __SFPBPhotosAlbumImageReadFrom
+ __SFPBPhotosMemoryImageReadFrom
+ __SFPBRFSummaryItemAttributionReadFrom
+ __SFPBRFSummaryItemExpandableCardSectionReadFrom
+ __SFPBRFSummaryItemExpandableContentReadFrom
+ __SFPBURLCopyItemReadFrom
+ __block_literal_global.33646
+ __block_literal_global.34418
+ __block_literal_global.36124
+ __block_literal_global.68879
+ __getDispatchQueue_block_invoke.68883
+ _objc_msgSend$addCopyableItems:
+ _objc_msgSend$addShareItems:
+ _objc_msgSend$albumIdentifier
+ _objc_msgSend$applicationPath
+ _objc_msgSend$attribution
+ _objc_msgSend$attribution_ignores_expansion
+ _objc_msgSend$copyableItems
+ _objc_msgSend$encodedTypedValue
+ _objc_msgSend$entity
+ _objc_msgSend$fillToolAppEntityParameterCommand
+ _objc_msgSend$fillToolAppParameterCommand
+ _objc_msgSend$fillToolFileParameterCommand
+ _objc_msgSend$fillToolParameterCommand
+ _objc_msgSend$fillToolPersonParameterCommand
+ _objc_msgSend$hasAttribution_ignores_expansion
+ _objc_msgSend$hasSimple_item_rich_card_section
+ _objc_msgSend$memoryIdentifier
+ _objc_msgSend$photosAlbumImage
+ _objc_msgSend$photosMemoryImage
+ _objc_msgSend$rfSummaryItemExpandableCardSection
+ _objc_msgSend$setAlbumIdentifier:
+ _objc_msgSend$setApplicationPath:
+ _objc_msgSend$setAttribution:
+ _objc_msgSend$setAttribution_ignores_expansion:
+ _objc_msgSend$setCopyableItems:
+ _objc_msgSend$setEncodedTypedValue:
+ _objc_msgSend$setEntity:
+ _objc_msgSend$setFillToolAppEntityParameterCommand:
+ _objc_msgSend$setFillToolAppParameterCommand:
+ _objc_msgSend$setFillToolFileParameterCommand:
+ _objc_msgSend$setFillToolParameterCommand:
+ _objc_msgSend$setFillToolPersonParameterCommand:
+ _objc_msgSend$setMemoryIdentifier:
+ _objc_msgSend$setPhotosAlbumImage:
+ _objc_msgSend$setPhotosMemoryImage:
+ _objc_msgSend$setRfSummaryItemExpandableCardSection:
+ _objc_msgSend$setShareItems:
+ _objc_msgSend$setSimple_item_rich_card_section:
+ _objc_msgSend$setText_compact:
+ _objc_msgSend$setText_minimal:
+ _objc_msgSend$setUrlCopyItem:
+ _objc_msgSend$shareItems
+ _objc_msgSend$simple_item_rich_card_section
+ _objc_msgSend$text_compact
+ _objc_msgSend$text_minimal
+ _objc_msgSend$urlCopyItem
+ getDispatchQueue.68877
+ getDispatchQueue.onceToken.68878
+ getDispatchQueue.queue.68880
- GCC_except_table2719
- GCC_except_table7648
- PARLogHandleForCategory.logHandles.0.33252
- PARLogHandleForCategory.logHandles.0.67030
- PARLogHandleForCategory.logHandles.1.33246
- PARLogHandleForCategory.logHandles.1.67026
- PARLogHandleForCategory.logHandles.2.33254
- PARLogHandleForCategory.logHandles.2.67031
- PARLogHandleForCategory.logHandles.3.33255
- PARLogHandleForCategory.logHandles.3.67033
- PARLogHandleForCategory.logHandles.4.33256
- PARLogHandleForCategory.logHandles.4.67034
- PARLogHandleForCategory.logHandles.5.33257
- PARLogHandleForCategory.logHandles.5.67035
- PARLogHandleForCategory.onceToken.33244
- PARLogHandleForCategory.onceToken.67025
- _OBJC_$_PROP_LIST_SFCardSectionValue.1058
- _OBJC_$_PROP_LIST_SFCopyCommand.105
- _OBJC_$_PROP_LIST_SFShareCommand.105
- _OBJC_$_PROP_LIST__SFPBCardSectionValue.3332
- _OBJC_$_PROP_LIST__SFPBClearProactiveCategoryCommand.3363
- _OBJC_$_PROP_LIST__SFPBClockImage.3393
- _OBJC_$_PROP_LIST__SFPBCloudChannelsRequestItem.3424
- _OBJC_$_PROP_LIST__SFPBCollectionCardSection.3461
- _OBJC_$_PROP_LIST__SFPBCollectionStyle.3519
- _OBJC_$_PROP_LIST__SFPBCollectionStyleGrid.3541
- _OBJC_$_PROP_LIST__SFPBCollectionStyleHorizontallyScrolling.3555
- _OBJC_$_PROP_LIST__SFPBCollectionStyleRow.3585
- _OBJC_$_PROP_LIST__SFPBColor.3705
- _OBJC_$_PROP_LIST__SFPBColorBarCardSection.3728
- _OBJC_$_PROP_LIST__SFPBCombinedCardSection.3735
- _OBJC_$_PROP_LIST__SFPBCommand.4460
- _OBJC_$_PROP_LIST__SFPBCommandButtonItem.4475
- _OBJC_$_PROP_LIST__SFPBCommandReference.4490
- _OBJC_$_PROP_LIST__SFPBCommandRowCardSection.4513
- _OBJC_$_PROP_LIST__SFPBCommandValue.4533
- _OBJC_$_PROP_LIST__SFPBCompactRowCardSection.4548
- _OBJC_$_PROP_LIST__SFPBContactButtonItem.4582
- _OBJC_$_PROP_LIST__SFPBContactCopyItem.4597
- _OBJC_$_PROP_LIST__SFPBContactImage.4632
- _OBJC_$_PROP_LIST__SFPBCopyCommand.4652
- _OBJC_$_PROP_LIST__SFPBCopyItem.4711
- _OBJC_$_PROP_LIST__SFPBCoreSpotlightButtonItem.4738
- _OBJC_$_PROP_LIST__SFPBCoreSpotlightCopyItem.4769
- _OBJC_$_PROP_LIST__SFPBCoreSpotlightRankingSignals.4907
- _OBJC_$_PROP_LIST__SFPBCoreSpotlightShareItem.4922
- _OBJC_$_PROP_LIST__SFPBCreateCalendarEventCommand.4942
- _OBJC_$_PROP_LIST__SFPBCreateContactCommand.4957
- _OBJC_$_PROP_LIST__SFPBCreateReminderCommand.4977
- _OBJC_$_PROP_LIST__SFPBDate.4991
- _OBJC_$_PROP_LIST__SFPBDefaultPunchoutAppIconImage.5006
- _OBJC_$_PROP_LIST__SFPBDescriptionCardSection.5119
- _OBJC_$_PROP_LIST__SFPBDetailedRowCardSection.5293
- _OBJC_$_PROP_LIST__SFPBDomainEngagementScore.5331
- _OBJC_$_PROP_LIST__SFPBDomainSubscriptionRequestItem.5351
- _OBJC_$_PROP_LIST__SFPBDrillDownMetadata.5458
- _OBJC_$_PROP_LIST__SFPBDynamicURLImageResource.5512
- _OBJC_$_PROP_LIST__SFPBEmailCommand.5519
- _OBJC_$_PROP_LIST__SFPBEngagementSignal.5581
- _OBJC_$_PROP_LIST__SFPBEntitySearchMetadata.5605
- _OBJC_$_PROP_LIST__SFPBExecuteMenuItemCommand.5620
- _OBJC_$_PROP_LIST__SFPBExecuteToolCommand.5643
- _OBJC_$_PROP_LIST__SFPBExpandInlineCommand.5657
- _OBJC_$_PROP_LIST__SFPBFindMyCardSection.5664
- _OBJC_$_PROP_LIST__SFPBFlight.5750
- _OBJC_$_PROP_LIST__SFPBFlightCardSection.5776
- _OBJC_$_PROP_LIST__SFPBFlightCheckinCommand.5782
- _OBJC_$_PROP_LIST__SFPBFlightDetails.5796
- _OBJC_$_PROP_LIST__SFPBFlightLeg.5936
- _OBJC_$_PROP_LIST__SFPBFormattedText.5984
- _OBJC_$_PROP_LIST__SFPBGradientColor.6012
- _OBJC_$_PROP_LIST__SFPBGraphicalFloat.6026
- _OBJC_$_PROP_LIST__SFPBGridCardSection.6033
- _OBJC_$_PROP_LIST__SFPBHashBucketDetail.6063
- _OBJC_$_PROP_LIST__SFPBHashBucketDetail_HashDetail.6114
- _OBJC_$_PROP_LIST__SFPBHeroCardSection.6121
- _OBJC_$_PROP_LIST__SFPBHeroTitleCardSection.6136
- _OBJC_$_PROP_LIST__SFPBHorizontalButtonCardSection.6155
- _OBJC_$_PROP_LIST__SFPBHorizontalScrollCardSection.6162
- _OBJC_$_PROP_LIST__SFPBImage.6440
- _OBJC_$_PROP_LIST__SFPBImageCopyItem.6447
- _OBJC_$_PROP_LIST__SFPBImageDerivedColor.6454
- _OBJC_$_PROP_LIST__SFPBImageOption.6482
- _OBJC_$_PROP_LIST__SFPBImagesCardSection.6510
- _OBJC_$_PROP_LIST__SFPBIndexState.6556
- _OBJC_$_PROP_LIST__SFPBIndexedUserActivityCommand.6571
- _OBJC_$_PROP_LIST__SFPBInfoCardSection.6601
- _OBJC_$_PROP_LIST__SFPBInfoTuple.6645
- _OBJC_$_PROP_LIST__SFPBInvokeSiriCommand.6660
- _OBJC_$_PROP_LIST__SFPBKeyValueDataCardSection.6691
- _OBJC_$_PROP_LIST__SFPBKeyValueTuple.6699
- _OBJC_$_PROP_LIST__SFPBLargeTitleDetailedRowCardSection.6729
- _OBJC_$_PROP_LIST__SFPBLatLng.6751
- _OBJC_$_PROP_LIST__SFPBLaunchAppCommand.6758
- _OBJC_$_PROP_LIST__SFPBLeadingTrailingCardSection.6797
- _OBJC_$_PROP_LIST__SFPBLinkPresentationCardSection.6827
- _OBJC_$_PROP_LIST__SFPBListenToCardSection.6858
- _OBJC_$_PROP_LIST__SFPBLocalImage.6872
- _OBJC_$_PROP_LIST__SFPBLocationTypeInfo.6887
- _OBJC_$_PROP_LIST__SFPBMailRankingSignals.7421
- _OBJC_$_PROP_LIST__SFPBMailResultDetails.7451
- _OBJC_$_PROP_LIST__SFPBManageReservationCommand.7457
- _OBJC_$_PROP_LIST__SFPBMapCardSection.7533
- _OBJC_$_PROP_LIST__SFPBMapPlaceCardSection.7548
- _OBJC_$_PROP_LIST__SFPBMapRegion.7594
- _OBJC_$_PROP_LIST__SFPBMapsDetailedRowCardSection.7609
- _OBJC_$_PROP_LIST__SFPBMediaArtworkImage.7624
- _OBJC_$_PROP_LIST__SFPBMediaDetail.7639
- _OBJC_$_PROP_LIST__SFPBMediaInfoCardSection.7753
- _OBJC_$_PROP_LIST__SFPBMediaItem.7833
- _OBJC_$_PROP_LIST__SFPBMediaMetadata.7913
- _OBJC_$_PROP_LIST__SFPBMediaOffer.7952
- _OBJC_$_PROP_LIST__SFPBMediaPlayerCardSection.7972
- _OBJC_$_PROP_LIST__SFPBMediaRemoteControlCardSection.8003
- _OBJC_$_PROP_LIST__SFPBMessageAttachment.8018
- _OBJC_$_PROP_LIST__SFPBMessageCardSection.8070
- _OBJC_$_PROP_LIST__SFPBMetaInfoCardSection.8109
- _OBJC_$_PROP_LIST__SFPBMiniCardSection.8116
- _OBJC_$_PROP_LIST__SFPBMonogramImage.8139
- _OBJC_$_PROP_LIST__SFPBMoreResults.8146
- _OBJC_$_PROP_LIST__SFPBNamedProtobufMessage.8169
- _OBJC_$_PROP_LIST__SFPBNewsCardSection.8200
- _OBJC_$_PROP_LIST__SFPBNowPlayingCardSection.8219
- _OBJC_$_PROP_LIST__SFPBOpenAppClipCommand.8234
- _OBJC_$_PROP_LIST__SFPBOpenCalculationCommand.8265
- _OBJC_$_PROP_LIST__SFPBOpenCoreSpotlightItemCommand.8280
- _OBJC_$_PROP_LIST__SFPBOpenFileProviderItemCommand.8295
- _OBJC_$_PROP_LIST__SFPBOpenMediaCommand.8310
- _OBJC_$_PROP_LIST__SFPBOpenPunchoutCommand.8317
- _OBJC_$_PROP_LIST__SFPBOpenWebClipCommand.8324
- _OBJC_$_PROP_LIST__SFPBPatternModel.8363
- _OBJC_$_PROP_LIST__SFPBPerformContactActionCommand.8393
- _OBJC_$_PROP_LIST__SFPBPerformContactQueryCommand.8400
- _OBJC_$_PROP_LIST__SFPBPerformEntityQueryCommand.8471
- _OBJC_$_PROP_LIST__SFPBPerformIntentCommand.8494
- _OBJC_$_PROP_LIST__SFPBPerformPersonEntityQueryCommand.8501
- _OBJC_$_PROP_LIST__SFPBPerson.8556
- _OBJC_$_PROP_LIST__SFPBPersonHeaderCardSection.8563
- _OBJC_$_PROP_LIST__SFPBPhotosAggregatedInfo.8593
- _OBJC_$_PROP_LIST__SFPBPhotosAttributes.8647
- _OBJC_$_PROP_LIST__SFPBPhotosLibraryImage.8683
- _OBJC_$_PROP_LIST__SFPBPhotosRankingInfo.8713
- _OBJC_$_PROP_LIST__SFPBPin.8728
- _OBJC_$_PROP_LIST__SFPBPlayAudioButtonItem.8761
- _OBJC_$_PROP_LIST__SFPBPlayMediaCommand.8784
- _OBJC_$_PROP_LIST__SFPBPlayVideoCommand.8791
- _OBJC_$_PROP_LIST__SFPBPlayWatchListItemButtonItem.8811
- _OBJC_$_PROP_LIST__SFPBPointSize.8834
- _OBJC_$_PROP_LIST__SFPBProduct.8865
- _OBJC_$_PROP_LIST__SFPBProductAvailability.8887
- _OBJC_$_PROP_LIST__SFPBProductCardSection.8902
- _OBJC_$_PROP_LIST__SFPBProductInventory.8958
- _OBJC_$_PROP_LIST__SFPBProductInventoryResult.8981
- _OBJC_$_PROP_LIST__SFPBPunchout.9046
- _OBJC_$_PROP_LIST__SFPBQueryUnderstandingParse.9204
- _OBJC_$_PROP_LIST__SFPBQuickLookThumbnailImage.9219
- _OBJC_$_PROP_LIST__SFPBRFAppIconImage.9239
- _OBJC_$_PROP_LIST__SFPBRFAspectRatio.9247
- _OBJC_$_PROP_LIST__SFPBRFAttribution.9299
- _OBJC_$_PROP_LIST__SFPBRFAvatarImage.9318
- _OBJC_$_PROP_LIST__SFPBRFBadgedImage.9332
- _OBJC_$_PROP_LIST__SFPBRFBinaryButtonCardSection.9355
- _OBJC_$_PROP_LIST__SFPBRFButtonCardSection.9363
- _OBJC_$_PROP_LIST__SFPBRFColor.9397
- _OBJC_$_PROP_LIST__SFPBRFDefaultBrowserAppIconImage.9403
- _OBJC_$_PROP_LIST__SFPBRFDisambiguationTitleCardSection.9419
- _OBJC_$_PROP_LIST__SFPBRFEngageable.9448
- _OBJC_$_PROP_LIST__SFPBRFExpandableStandardCardSection.9483
- _OBJC_$_PROP_LIST__SFPBRFExpandingComponentContent.9506
- _OBJC_$_PROP_LIST__SFPBRFFactItemButtonCardSection.9591
- _OBJC_$_PROP_LIST__SFPBRFFactItemDetailedNumberCardSection.9610
- _OBJC_$_PROP_LIST__SFPBRFFactItemHeroButtonCardSection.9617
- _OBJC_$_PROP_LIST__SFPBRFFactItemHeroNumberCardSection.9650
- _OBJC_$_PROP_LIST__SFPBRFFactItemImageRightCardSection.9657
- _OBJC_$_PROP_LIST__SFPBRFFactItemShortHeroNumberCardSection.9664
- _OBJC_$_PROP_LIST__SFPBRFFactItemShortNumberCardSection.9671
- _OBJC_$_PROP_LIST__SFPBRFFactItemStandardCardSection.9687
- _OBJC_$_PROP_LIST__SFPBRFFont.9715
- _OBJC_$_PROP_LIST__SFPBRFFont_RFSystemFont.10748
- _OBJC_$_PROP_LIST__SFPBRFFormattedText.9869
- _OBJC_$_PROP_LIST__SFPBRFHighlightedSubstring.9884
- _OBJC_$_PROP_LIST__SFPBRFImageElement.9904
- _OBJC_$_PROP_LIST__SFPBRFImageSource.10003
- _OBJC_$_PROP_LIST__SFPBRFLongItemStandardCardSection.10026
- _OBJC_$_PROP_LIST__SFPBRFMapAnnotation.10056
- _OBJC_$_PROP_LIST__SFPBRFMapCardSection.10123
- _OBJC_$_PROP_LIST__SFPBRFMapMarker.10156
- _OBJC_$_PROP_LIST__SFPBRFMapMarkerIdentifier.10187
- _OBJC_$_PROP_LIST__SFPBRFMapMarkerImage.10202
- _OBJC_$_PROP_LIST__SFPBRFMapMarkerText.10210
- _OBJC_$_PROP_LIST__SFPBRFMapPoint.10232
- _OBJC_$_PROP_LIST__SFPBRFMonogramImage.10247
- _OBJC_$_PROP_LIST__SFPBRFMultiButtonCardSection.10262
- _OBJC_$_PROP_LIST__SFPBRFOptionalBool.10269
- _OBJC_$_PROP_LIST__SFPBRFOptionalFloat.10276
- _OBJC_$_PROP_LIST__SFPBRFPreview.10283
- _OBJC_$_PROP_LIST__SFPBRFPreviewList.10305
- _OBJC_$_PROP_LIST__SFPBRFPrimaryHeaderMarqueeCardSection.10320
- _OBJC_$_PROP_LIST__SFPBRFPrimaryHeaderRichCardSection.10327
- _OBJC_$_PROP_LIST__SFPBRFPrimaryHeaderStackedImageCardSection.10335
- _OBJC_$_PROP_LIST__SFPBRFPrimaryHeaderStandardCardSection.10342
- _OBJC_$_PROP_LIST__SFPBRFRGBValue.10372
- _OBJC_$_PROP_LIST__SFPBRFReferenceCenteredCardSection.10384
- _OBJC_$_PROP_LIST__SFPBRFReferenceFootnoteCardSection.10391
- _OBJC_$_PROP_LIST__SFPBRFReferenceItemButtonCardSection.10398
- _OBJC_$_PROP_LIST__SFPBRFReferenceItemLogoCardSection.10405
- _OBJC_$_PROP_LIST__SFPBRFReferenceRichCardSection.10412
- _OBJC_$_PROP_LIST__SFPBRFReferenceStandardCardSection.10419
- _OBJC_$_PROP_LIST__SFPBRFSecondaryHeaderEmphasizedCardSection.10426
- _OBJC_$_PROP_LIST__SFPBRFSecondaryHeaderStandardCardSection.10433
- _OBJC_$_PROP_LIST__SFPBRFShowMoreOnTap.10448
- _OBJC_$_PROP_LIST__SFPBRFSimpleItemPlayerCardSection.10463
- _OBJC_$_PROP_LIST__SFPBRFSimpleItemReverseRichCardSection.10470
- _OBJC_$_PROP_LIST__SFPBRFSimpleItemRichCardSection.10501
- _OBJC_$_PROP_LIST__SFPBRFSimpleItemRichSearchResultCardSection.10508
- _OBJC_$_PROP_LIST__SFPBRFSimpleItemStandardCardSection.10515
- _OBJC_$_PROP_LIST__SFPBRFSimpleItemVisualElementCardSection.10539
- _OBJC_$_PROP_LIST__SFPBRFSummaryItemAlignedTextCardSection.10555
- _OBJC_$_PROP_LIST__SFPBRFSummaryItemButtonCardSection.10562
- _OBJC_$_PROP_LIST__SFPBRFSummaryItemDetailedTextCardSection.10569
- _OBJC_$_PROP_LIST__SFPBRFSummaryItemImageRightCardSection.10589
- _OBJC_$_PROP_LIST__SFPBRFSummaryItemPairCardSection.10596
- _OBJC_$_PROP_LIST__SFPBRFSummaryItemPairNumberCardSection.10635
- _OBJC_$_PROP_LIST__SFPBRFSummaryItemPlayerCardSection.10642
- _OBJC_$_PROP_LIST__SFPBRFSummaryItemShortNumberCardSection.10649
- _OBJC_$_PROP_LIST__SFPBRFSummaryItemStandardCardSection.10664
- _OBJC_$_PROP_LIST__SFPBRFSummaryItemSwitchV2CardSection.10679
- _OBJC_$_PROP_LIST__SFPBRFSummaryItemTextCardSection.10686
- _OBJC_$_PROP_LIST__SFPBRFSymbolImage.10741
- _OBJC_$_PROP_LIST__SFPBRFTableCell.10776
- _OBJC_$_PROP_LIST__SFPBRFTableColumnDefinition.10806
- _OBJC_$_PROP_LIST__SFPBRFTableContentColumnDefinition.10852
- _OBJC_$_PROP_LIST__SFPBRFTableHeaderCardSection.10917
- _OBJC_$_PROP_LIST__SFPBRFTableRowCardSection.10932
- _OBJC_$_PROP_LIST__SFPBRFTableSpacerColumnDefinition.10938
- _OBJC_$_PROP_LIST__SFPBRFTextElement.10982
- _OBJC_$_PROP_LIST__SFPBRFTextEncapsulation.10988
- _OBJC_$_PROP_LIST__SFPBRFTextProperty.11018
- _OBJC_$_PROP_LIST__SFPBRFUrlImage.11082
- _OBJC_$_PROP_LIST__SFPBRFVisualElement.11101
- _OBJC_$_PROP_LIST__SFPBRFVisualProperty.11123
- _OBJC_$_PROP_LIST__SFPBRFVisualPropertyWithAction.11138
- _OBJC_$_PROP_LIST__SFPBReferentialCommand.11145
- _OBJC_$_PROP_LIST__SFPBRejectPeopleInPhotoCommand.11165
- _OBJC_$_PROP_LIST__SFPBReminder.11180
- _OBJC_$_PROP_LIST__SFPBRequestAppClipInstallCommand.11187
- _OBJC_$_PROP_LIST__SFPBRequestProductPageCommand.11218
- _OBJC_$_PROP_LIST__SFPBRequestUserReportCommand.11225
- _OBJC_$_PROP_LIST__SFPBResponseWrapperCardSection.11279
- _OBJC_$_PROP_LIST__SFPBResultEntity.11307
- _OBJC_$_PROP_LIST__SFPBRichText.11347
- _OBJC_$_PROP_LIST__SFPBRichTitleCardSection.11495
- _OBJC_$_PROP_LIST__SFPBRowCardSection.11590
- _OBJC_$_PROP_LIST__SFPBRunVoiceShortcutCommand.11605
- _OBJC_$_PROP_LIST__SFPBSafariAttributes.11619
- _OBJC_$_PROP_LIST__SFPBSafariTableOfContentsCardSection.11665
- _OBJC_$_PROP_LIST__SFPBSafariTableOfContentsItem.11681
- _OBJC_$_PROP_LIST__SFPBScene.11703
- _OBJC_$_PROP_LIST__SFPBScoreboardCardSection.11747
- _OBJC_$_PROP_LIST__SFPBSearchInAppCommand.11762
- _OBJC_$_PROP_LIST__SFPBSearchSuggestion.11840
- _OBJC_$_PROP_LIST__SFPBSearchWebCommand.11847
- _OBJC_$_PROP_LIST__SFPBSectionHeaderCardSection.11855
- _OBJC_$_PROP_LIST__SFPBSelectableGridCardSection.11885
- _OBJC_$_PROP_LIST__SFPBShareCommand.11905
- _OBJC_$_PROP_LIST__SFPBShareItem.11938
- _OBJC_$_PROP_LIST__SFPBShortcutsImage.11953
- _OBJC_$_PROP_LIST__SFPBShowAppStoreSheetCommand.11968
- _OBJC_$_PROP_LIST__SFPBShowContactCardCommand.11983
- _OBJC_$_PROP_LIST__SFPBShowPhotosOneUpViewCommand.12034
- _OBJC_$_PROP_LIST__SFPBShowPurchaseRequestSheetCommand.12049
- _OBJC_$_PROP_LIST__SFPBShowSFCardCommand.12064
- _OBJC_$_PROP_LIST__SFPBShowScreenTimeRequestSheetCommand.12071
- _OBJC_$_PROP_LIST__SFPBShowWrapperResponseViewCommand.12078
- _OBJC_$_PROP_LIST__SFPBSocialMediaPostCardSection.12142
- _OBJC_$_PROP_LIST__SFPBSplitCardSection.12209
- _OBJC_$_PROP_LIST__SFPBSportsDetail.12224
- _OBJC_$_PROP_LIST__SFPBSportsFollowButtonItem.12252
- _OBJC_$_PROP_LIST__SFPBSportsItem.12259
- _OBJC_$_PROP_LIST__SFPBSportsSubscriptionRequestItem.12290
- _OBJC_$_PROP_LIST__SFPBSportsTeam.12322
- _OBJC_$_PROP_LIST__SFPBStockChartCardSection.12345
- _OBJC_$_PROP_LIST__SFPBStoreButtonItem.12368
- _OBJC_$_PROP_LIST__SFPBStringDictionary.12387
- _OBJC_$_PROP_LIST__SFPBStrokeAnimationCardSection.12438
- _OBJC_$_PROP_LIST__SFPBStructuredLocation.12461
- _OBJC_$_PROP_LIST__SFPBSubscribeForUpdatesCommand.12494
- _OBJC_$_PROP_LIST__SFPBSuggestionCardSection.12533
- _OBJC_$_PROP_LIST__SFPBSymbolImage.12575
- _OBJC_$_PROP_LIST__SFPBTableAlignmentSchema.12599
- _OBJC_$_PROP_LIST__SFPBTableColumnAlignment.12629
- _OBJC_$_PROP_LIST__SFPBTableHeaderRowCardSection.12697
- _OBJC_$_PROP_LIST__SFPBTableRowCardSection.12717
- _OBJC_$_PROP_LIST__SFPBText.12734
- _OBJC_$_PROP_LIST__SFPBTextColumn.12756
- _OBJC_$_PROP_LIST__SFPBTextColumnSection.12791
- _OBJC_$_PROP_LIST__SFPBTextColumnsCardSection.12802
- _OBJC_$_PROP_LIST__SFPBTextCopyItem.12817
- _OBJC_$_PROP_LIST__SFPBTimeZone.12824
- _OBJC_$_PROP_LIST__SFPBTitleCardSection.12831
- _OBJC_$_PROP_LIST__SFPBTitleSubtitleTuple.12838
- _OBJC_$_PROP_LIST__SFPBToggleAudioCommand.12861
- _OBJC_$_PROP_LIST__SFPBToggleButtonConfiguration.12885
- _OBJC_$_PROP_LIST__SFPBToggleWatchListStatusCommand.12900
- _OBJC_$_PROP_LIST__SFPBTopic.12943
- _OBJC_$_PROP_LIST__SFPBTrack.12975
- _OBJC_$_PROP_LIST__SFPBTrackListCardSection.12997
- _OBJC_$_PROP_LIST__SFPBURL.13004
- _OBJC_$_PROP_LIST__SFPBURLImage.13019
- _OBJC_$_PROP_LIST__SFPBURLShareItem.13026
- _OBJC_$_PROP_LIST__SFPBUpdateSearchQueryCommand.13041
- _OBJC_$_PROP_LIST__SFPBUpdateSportsFollowingStatusCommand.13056
- _OBJC_$_PROP_LIST__SFPBUserActivityData.13087
- _OBJC_$_PROP_LIST__SFPBUserActivityInfo.13110
- _OBJC_$_PROP_LIST__SFPBUserReportRequest.13185
- _OBJC_$_PROP_LIST__SFPBVerticalLayoutCardSection.13216
- _OBJC_$_PROP_LIST__SFPBViewEmailCommand.13222
- _OBJC_$_PROP_LIST__SFPBWatchListButtonItem.13229
- _OBJC_$_PROP_LIST__SFPBWatchListCardSection.13236
- _OBJC_$_PROP_LIST__SFPBWatchListItem.13315
- _OBJC_$_PROP_LIST__SFPBWatchNowCardSection.13329
- _OBJC_$_PROP_LIST__SFPBWeatherColor.13376
- _OBJC_$_PROP_LIST__SFPBWeatherDetails.13383
- _OBJC_$_PROP_LIST__SFPBWebCardSection.13398
- _OBJC_$_PROP_LIST__SFPBWorldMapCardSection.13421
- __PARLogHandleForCategory_block_invoke.33250
- __PARLogHandleForCategory_block_invoke.67028
- __block_literal_global.33245
- __block_literal_global.34017
- __block_literal_global.35723
- __block_literal_global.67041
- __getDispatchQueue_block_invoke.67045
- getDispatchQueue.67039
- getDispatchQueue.onceToken.67040
- getDispatchQueue.queue.67042
CStrings:
+ "\x0f\x0f\x0f\x0f\x01"
+ "\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x06"
+ "/\t"
+ "246"
+ "65"
+ "66"
+ "@\"RFSummaryItemAttribution\""
+ "@\"RFSummaryItemAttribution\"16@0:8"
+ "@\"RFSummaryItemExpandableCardSection\""
+ "@\"RFSummaryItemExpandableCardSection\"16@0:8"
+ "@\"_SFPBCopyItem\"24@0:8Q16"
+ "@\"_SFPBFillToolAppEntityParameterCommand\""
+ "@\"_SFPBFillToolAppEntityParameterCommand\"16@0:8"
+ "@\"_SFPBFillToolAppParameterCommand\""
+ "@\"_SFPBFillToolAppParameterCommand\"16@0:8"
+ "@\"_SFPBFillToolFileParameterCommand\""
+ "@\"_SFPBFillToolFileParameterCommand\"16@0:8"
+ "@\"_SFPBFillToolParameterCommand\""
+ "@\"_SFPBFillToolParameterCommand\"16@0:8"
+ "@\"_SFPBFillToolPersonParameterCommand\""
+ "@\"_SFPBFillToolPersonParameterCommand\"16@0:8"
+ "@\"_SFPBPhotosAlbumImage\""
+ "@\"_SFPBPhotosAlbumImage\"16@0:8"
+ "@\"_SFPBPhotosMemoryImage\""
+ "@\"_SFPBPhotosMemoryImage\"16@0:8"
+ "@\"_SFPBRFSummaryItemAttribution\""
+ "@\"_SFPBRFSummaryItemAttribution\"16@0:8"
+ "@\"_SFPBRFSummaryItemExpandableCardSection\""
+ "@\"_SFPBRFSummaryItemExpandableCardSection\"16@0:8"
+ "@\"_SFPBRFSummaryItemExpandableContent\"24@0:8Q16"
+ "@\"_SFPBShareItem\"24@0:8Q16"
+ "@\"_SFPBURLCopyItem\""
+ "@\"_SFPBURLCopyItem\"16@0:8"
+ "RFSummaryItemAttribution"
+ "RFSummaryItemExpandableCardSection"
+ "RFSummaryItemExpandableContent"
+ "SFFillToolAppEntityParameterCommand"
+ "SFFillToolAppParameterCommand"
+ "SFFillToolFileParameterCommand"
+ "SFFillToolParameterCommand"
+ "SFFillToolPersonParameterCommand"
+ "SFPhotosAlbumImage"
+ "SFPhotosMemoryImage"
+ "SFURLCopyItem"
+ "T@\"NSArray\",C,N,V_copyableItems"
+ "T@\"NSArray\",C,N,V_shareItems"
+ "T@\"NSData\",C,N,V_encodedTypedValue"
+ "T@\"NSString\",C,N,V_albumIdentifier"
+ "T@\"NSString\",C,N,V_applicationPath"
+ "T@\"NSString\",C,N,V_filePath"
+ "T@\"NSString\",C,N,V_memoryIdentifier"
+ "T@\"RFSimpleItemRichCardSection\",&,N,V_simple_item_rich_card_section"
+ "T@\"RFSummaryItemAttribution\",&,N"
+ "T@\"RFSummaryItemAttribution\",&,N,V_attribution"
+ "T@\"RFSummaryItemExpandableCardSection\",&,N"
+ "T@\"RFSummaryItemExpandableCardSection\",&,N,V_rfSummaryItemExpandableCardSection"
+ "T@\"RFTextProperty\",&,N,V_text_compact"
+ "T@\"RFTextProperty\",&,N,V_text_minimal"
+ "T@\"SFAppEntityAnnotation\",&,N,V_entity"
+ "T@\"_SFPBAppEntityAnnotation\",&,N,V_entity"
+ "T@\"_SFPBFillToolAppEntityParameterCommand\",&,N"
+ "T@\"_SFPBFillToolAppEntityParameterCommand\",&,N,V_fillToolAppEntityParameterCommand"
+ "T@\"_SFPBFillToolAppParameterCommand\",&,N"
+ "T@\"_SFPBFillToolAppParameterCommand\",&,N,V_fillToolAppParameterCommand"
+ "T@\"_SFPBFillToolFileParameterCommand\",&,N"
+ "T@\"_SFPBFillToolFileParameterCommand\",&,N,V_fillToolFileParameterCommand"
+ "T@\"_SFPBFillToolParameterCommand\",&,N"
+ "T@\"_SFPBFillToolParameterCommand\",&,N,V_fillToolParameterCommand"
+ "T@\"_SFPBFillToolPersonParameterCommand\",&,N"
+ "T@\"_SFPBFillToolPersonParameterCommand\",&,N,V_fillToolPersonParameterCommand"
+ "T@\"_SFPBPhotosAlbumImage\",&,N"
+ "T@\"_SFPBPhotosAlbumImage\",&,N,V_photosAlbumImage"
+ "T@\"_SFPBPhotosMemoryImage\",&,N"
+ "T@\"_SFPBPhotosMemoryImage\",&,N,V_photosMemoryImage"
+ "T@\"_SFPBRFSimpleItemRichCardSection\",&,N,V_simple_item_rich_card_section"
+ "T@\"_SFPBRFSummaryItemAttribution\",&,N"
+ "T@\"_SFPBRFSummaryItemAttribution\",&,N,V_attribution"
+ "T@\"_SFPBRFSummaryItemExpandableCardSection\",&,N"
+ "T@\"_SFPBRFSummaryItemExpandableCardSection\",&,N,V_rfSummaryItemExpandableCardSection"
+ "T@\"_SFPBRFTextProperty\",&,N,V_text_compact"
+ "T@\"_SFPBRFTextProperty\",&,N,V_text_minimal"
+ "T@\"_SFPBURLCopyItem\",&,N"
+ "T@\"_SFPBURLCopyItem\",&,N,V_urlCopyItem"
+ "TB,N,V_attribution_ignores_expansion"
+ "_SFPBFillToolAppEntityParameterCommand"
+ "_SFPBFillToolAppParameterCommand"
+ "_SFPBFillToolFileParameterCommand"
+ "_SFPBFillToolParameterCommand"
+ "_SFPBFillToolPersonParameterCommand"
+ "_SFPBPhotosAlbumImage"
+ "_SFPBPhotosMemoryImage"
+ "_SFPBRFSummaryItemAttribution"
+ "_SFPBRFSummaryItemExpandableCardSection"
+ "_SFPBRFSummaryItemExpandableContent"
+ "_SFPBURLCopyItem"
+ "_albumIdentifier"
+ "_applicationPath"
+ "_attribution"
+ "_attribution_ignores_expansion"
+ "_copyableItems"
+ "_encodedTypedValue"
+ "_entity"
+ "_fillToolAppEntityParameterCommand"
+ "_fillToolAppParameterCommand"
+ "_fillToolFileParameterCommand"
+ "_fillToolParameterCommand"
+ "_fillToolPersonParameterCommand"
+ "_memoryIdentifier"
+ "_photosAlbumImage"
+ "_photosMemoryImage"
+ "_rfSummaryItemExpandableCardSection"
+ "_shareItems"
+ "_simple_item_rich_card_section"
+ "_text_compact"
+ "_text_minimal"
+ "_urlCopyItem"
+ "addCopyableItems:"
+ "addShareItems:"
+ "albumIdentifier"
+ "applicationPath"
+ "attribution"
+ "attributionIgnoresExpansion"
+ "attribution_ignores_expansion"
+ "clearCopyableItems"
+ "clearShareItems"
+ "copyableItems"
+ "copyableItemsAtIndex:"
+ "copyableItemsCount"
+ "encodedTypedValue"
+ "entity"
+ "fillToolAppEntityParameterCommand"
+ "fillToolAppParameterCommand"
+ "fillToolFileParameterCommand"
+ "fillToolParameterCommand"
+ "fillToolPersonParameterCommand"
+ "hasAttribution_ignores_expansion"
+ "hasSimple_item_rich_card_section"
+ "memoryIdentifier"
+ "photosAlbumImage"
+ "photosMemoryImage"
+ "rfSummaryItemExpandableCardSection"
+ "setAlbumIdentifier:"
+ "setApplicationPath:"
+ "setAttribution:"
+ "setAttribution_ignores_expansion:"
+ "setCopyableItems:"
+ "setEncodedTypedValue:"
+ "setEntity:"
+ "setFillToolAppEntityParameterCommand:"
+ "setFillToolAppParameterCommand:"
+ "setFillToolFileParameterCommand:"
+ "setFillToolParameterCommand:"
+ "setFillToolPersonParameterCommand:"
+ "setMemoryIdentifier:"
+ "setPhotosAlbumImage:"
+ "setPhotosMemoryImage:"
+ "setRfSummaryItemExpandableCardSection:"
+ "setShareItems:"
+ "setSimple_item_rich_card_section:"
+ "setText_compact:"
+ "setText_minimal:"
+ "setUrlCopyItem:"
+ "shareItems"
+ "shareItemsAtIndex:"
+ "shareItemsCount"
+ "simpleItemRichCardSection"
+ "simple_item_rich_card_section"
+ "textCompact"
+ "textMinimal"
+ "text_compact"
+ "text_minimal"
+ "urlCopyItem"
+ "v24@0:8@\"RFSummaryItemAttribution\"16"
+ "v24@0:8@\"RFSummaryItemExpandableCardSection\"16"
+ "v24@0:8@\"_SFPBFillToolAppEntityParameterCommand\"16"
+ "v24@0:8@\"_SFPBFillToolAppParameterCommand\"16"
+ "v24@0:8@\"_SFPBFillToolFileParameterCommand\"16"
+ "v24@0:8@\"_SFPBFillToolParameterCommand\"16"
+ "v24@0:8@\"_SFPBFillToolPersonParameterCommand\"16"
+ "v24@0:8@\"_SFPBPhotosAlbumImage\"16"
+ "v24@0:8@\"_SFPBPhotosMemoryImage\"16"
+ "v24@0:8@\"_SFPBRFSummaryItemAttribution\"16"
+ "v24@0:8@\"_SFPBRFSummaryItemExpandableCardSection\"16"
+ "v24@0:8@\"_SFPBRFSummaryItemExpandableContent\"16"
+ "v24@0:8@\"_SFPBURLCopyItem\"16"
+ "{?=\"attribution_ignores_expansion\"b1}"
+ "{?=\"simple_item_rich_card_section\"b1}"
- "\x0f\x0f\x0f\v"
- "\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x05"

```
