## SearchFoundation

> `/System/Library/PrivateFrameworks/SearchFoundation.framework/SearchFoundation`

```diff

-3605.27.1.11.1
-  __TEXT.__text: 0x3bae24
-  __TEXT.__objc_methlist: 0x57a34
-  __TEXT.__const: 0x88
+3610.11.1.0.0
+  __TEXT.__text: 0x3c5a3c
+  __TEXT.__objc_methlist: 0x586ac
+  __TEXT.__const: 0x80
   __TEXT.__dlopen_cstrs: 0x52
   __TEXT.__gcc_except_tab: 0x94
-  __TEXT.__cstring: 0xbd60
+  __TEXT.__cstring: 0xbdd4
   __TEXT.__oslogstring: 0x19a
-  __TEXT.__unwind_info: 0xa338
+  __TEXT.__unwind_info: 0xa410
   __TEXT.__eh_frame: 0x50
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0xaa8
-  __DATA_CONST.__objc_classlist: 0x1838
+  __DATA_CONST.__objc_classlist: 0x1858
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x16f0
+  __DATA_CONST.__objc_protolist: 0x1710
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x79f0
+  __DATA_CONST.__objc_selrefs: 0x7a68
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x1f48
-  __DATA_CONST.__got: 0x17e8
+  __DATA_CONST.__objc_superrefs: 0x1f70
+  __DATA_CONST.__got: 0x1808
   __AUTH_CONST.__const: 0xe0
-  __AUTH_CONST.__cfstring: 0x13000
-  __AUTH_CONST.__objc_const: 0xb02e0
+  __AUTH_CONST.__cfstring: 0x130e0
+  __AUTH_CONST.__objc_const: 0xb1b60
   __AUTH_CONST.__objc_intobj: 0xd08
   __AUTH_CONST.__auth_got: 0x328
-  __AUTH.__objc_data: 0x8700
-  __DATA.__objc_ivar: 0x45c0
-  __DATA.__data: 0x11358
+  __AUTH.__objc_data: 0x8840
+  __DATA.__objc_ivar: 0x4690
+  __DATA.__data: 0x114d8
   __DATA_DIRTY.__objc_data: 0x6b30
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 17813
-  Symbols:   33374
-  CStrings:  2491
+  Functions: 17964
+  Symbols:   33634
+  CStrings:  2498
 
Symbols:
+ +[RFDataImage supportsSecureCoding]
+ +[RFSummaryItemPairWithButtonCardSection supportsSecureCoding]
+ -[RFAppIconImage backup_image]
+ -[RFAppIconImage setBackup_image:]
+ -[RFDataImage .cxx_destruct]
+ -[RFDataImage aspect_ratio]
+ -[RFDataImage background_color]
+ -[RFDataImage copyWithZone:]
+ -[RFDataImage corner_rounding_mode]
+ -[RFDataImage dark_mode_data]
+ -[RFDataImage data]
+ -[RFDataImage dictionaryRepresentation]
+ -[RFDataImage encodeWithCoder:]
+ -[RFDataImage hasCorner_rounding_mode]
+ -[RFDataImage hasImage_style]
+ -[RFDataImage hasPunches_through_background]
+ -[RFDataImage hasSizing_mode]
+ -[RFDataImage hasVibrancy]
+ -[RFDataImage hash]
+ -[RFDataImage image_style]
+ -[RFDataImage initWithCoder:]
+ -[RFDataImage isEqual:]
+ -[RFDataImage jsonData]
+ -[RFDataImage punches_through_background]
+ -[RFDataImage setAspect_ratio:]
+ -[RFDataImage setBackground_color:]
+ -[RFDataImage setCorner_rounding_mode:]
+ -[RFDataImage setDark_mode_data:]
+ -[RFDataImage setData:]
+ -[RFDataImage setImage_style:]
+ -[RFDataImage setPunches_through_background:]
+ -[RFDataImage setSizing_mode:]
+ -[RFDataImage setVibrancy:]
+ -[RFDataImage sizing_mode]
+ -[RFDataImage vibrancy]
+ -[RFDataImage(ProtobufInitializer) initWithProtobuf:]
+ -[RFImageSource data_image]
+ -[RFImageSource hasData_image]
+ -[RFImageSource setData_image:]
+ -[RFSummaryItemPairWithButtonCardSection .cxx_destruct]
+ -[RFSummaryItemPairWithButtonCardSection button_1]
+ -[RFSummaryItemPairWithButtonCardSection copyWithZone:]
+ -[RFSummaryItemPairWithButtonCardSection dictionaryRepresentation]
+ -[RFSummaryItemPairWithButtonCardSection encodeWithCoder:]
+ -[RFSummaryItemPairWithButtonCardSection hash]
+ -[RFSummaryItemPairWithButtonCardSection initWithCoder:]
+ -[RFSummaryItemPairWithButtonCardSection isEqual:]
+ -[RFSummaryItemPairWithButtonCardSection jsonData]
+ -[RFSummaryItemPairWithButtonCardSection setButton_1:]
+ -[RFSummaryItemPairWithButtonCardSection setText_1:]
+ -[RFSummaryItemPairWithButtonCardSection setText_2:]
+ -[RFSummaryItemPairWithButtonCardSection setText_3:]
+ -[RFSummaryItemPairWithButtonCardSection setText_4:]
+ -[RFSummaryItemPairWithButtonCardSection setText_5:]
+ -[RFSummaryItemPairWithButtonCardSection setText_6:]
+ -[RFSummaryItemPairWithButtonCardSection setText_7:]
+ -[RFSummaryItemPairWithButtonCardSection setText_8:]
+ -[RFSummaryItemPairWithButtonCardSection setThumbnail_1:]
+ -[RFSummaryItemPairWithButtonCardSection setThumbnail_2:]
+ -[RFSummaryItemPairWithButtonCardSection text_1]
+ -[RFSummaryItemPairWithButtonCardSection text_2]
+ -[RFSummaryItemPairWithButtonCardSection text_3]
+ -[RFSummaryItemPairWithButtonCardSection text_4]
+ -[RFSummaryItemPairWithButtonCardSection text_5]
+ -[RFSummaryItemPairWithButtonCardSection text_6]
+ -[RFSummaryItemPairWithButtonCardSection text_7]
+ -[RFSummaryItemPairWithButtonCardSection text_8]
+ -[RFSummaryItemPairWithButtonCardSection thumbnail_1]
+ -[RFSummaryItemPairWithButtonCardSection thumbnail_2]
+ -[RFSummaryItemPairWithButtonCardSection(ProtobufInitializer) initWithProtobuf:]
+ -[SFCardSectionValue rfSummaryItemPairWithButtonCardSection]
+ -[SFCardSectionValue setRfSummaryItemPairWithButtonCardSection:]
+ -[SFSportsItem hasIsEventLive]
+ -[SFSportsItem isEventLive]
+ -[SFSportsItem setIsEventLive:]
+ -[SFToggleButtonConfiguration hasIconOnly]
+ -[SFToggleButtonConfiguration iconOnly]
+ -[SFToggleButtonConfiguration setIconOnly:]
+ -[_SFPBCardSectionValue rfSummaryItemPairWithButtonCardSection]
+ -[_SFPBCardSectionValue setRfSummaryItemPairWithButtonCardSection:]
+ -[_SFPBRFAppIconImage backup_image]
+ -[_SFPBRFAppIconImage setBackup_image:]
+ -[_SFPBRFDataImage .cxx_destruct]
+ -[_SFPBRFDataImage aspect_ratio]
+ -[_SFPBRFDataImage background_color]
+ -[_SFPBRFDataImage corner_rounding_mode]
+ -[_SFPBRFDataImage dark_mode_data]
+ -[_SFPBRFDataImage data]
+ -[_SFPBRFDataImage dictionaryRepresentation]
+ -[_SFPBRFDataImage hash]
+ -[_SFPBRFDataImage image_style]
+ -[_SFPBRFDataImage initWithDictionary:]
+ -[_SFPBRFDataImage initWithJSON:]
+ -[_SFPBRFDataImage isEqual:]
+ -[_SFPBRFDataImage jsonData]
+ -[_SFPBRFDataImage punches_through_background]
+ -[_SFPBRFDataImage readFrom:]
+ -[_SFPBRFDataImage setAspect_ratio:]
+ -[_SFPBRFDataImage setBackground_color:]
+ -[_SFPBRFDataImage setCorner_rounding_mode:]
+ -[_SFPBRFDataImage setDark_mode_data:]
+ -[_SFPBRFDataImage setData:]
+ -[_SFPBRFDataImage setImage_style:]
+ -[_SFPBRFDataImage setPunches_through_background:]
+ -[_SFPBRFDataImage setSizing_mode:]
+ -[_SFPBRFDataImage setVibrancy:]
+ -[_SFPBRFDataImage sizing_mode]
+ -[_SFPBRFDataImage vibrancy]
+ -[_SFPBRFDataImage writeTo:]
+ -[_SFPBRFDataImage(FacadeInitializer) initWithFacade:]
+ -[_SFPBRFImageSource data_image]
+ -[_SFPBRFImageSource setData_image:]
+ -[_SFPBRFSummaryItemPairWithButtonCardSection .cxx_destruct]
+ -[_SFPBRFSummaryItemPairWithButtonCardSection button_1]
+ -[_SFPBRFSummaryItemPairWithButtonCardSection dictionaryRepresentation]
+ -[_SFPBRFSummaryItemPairWithButtonCardSection hash]
+ -[_SFPBRFSummaryItemPairWithButtonCardSection initWithDictionary:]
+ -[_SFPBRFSummaryItemPairWithButtonCardSection initWithJSON:]
+ -[_SFPBRFSummaryItemPairWithButtonCardSection isEqual:]
+ -[_SFPBRFSummaryItemPairWithButtonCardSection jsonData]
+ -[_SFPBRFSummaryItemPairWithButtonCardSection readFrom:]
+ -[_SFPBRFSummaryItemPairWithButtonCardSection setButton_1:]
+ -[_SFPBRFSummaryItemPairWithButtonCardSection setText_1:]
+ -[_SFPBRFSummaryItemPairWithButtonCardSection setText_2:]
+ -[_SFPBRFSummaryItemPairWithButtonCardSection setText_3:]
+ -[_SFPBRFSummaryItemPairWithButtonCardSection setText_4:]
+ -[_SFPBRFSummaryItemPairWithButtonCardSection setText_5:]
+ -[_SFPBRFSummaryItemPairWithButtonCardSection setText_6:]
+ -[_SFPBRFSummaryItemPairWithButtonCardSection setText_7:]
+ -[_SFPBRFSummaryItemPairWithButtonCardSection setText_8:]
+ -[_SFPBRFSummaryItemPairWithButtonCardSection setThumbnail_1:]
+ -[_SFPBRFSummaryItemPairWithButtonCardSection setThumbnail_2:]
+ -[_SFPBRFSummaryItemPairWithButtonCardSection text_1]
+ -[_SFPBRFSummaryItemPairWithButtonCardSection text_2]
+ -[_SFPBRFSummaryItemPairWithButtonCardSection text_3]
+ -[_SFPBRFSummaryItemPairWithButtonCardSection text_4]
+ -[_SFPBRFSummaryItemPairWithButtonCardSection text_5]
+ -[_SFPBRFSummaryItemPairWithButtonCardSection text_6]
+ -[_SFPBRFSummaryItemPairWithButtonCardSection text_7]
+ -[_SFPBRFSummaryItemPairWithButtonCardSection text_8]
+ -[_SFPBRFSummaryItemPairWithButtonCardSection thumbnail_1]
+ -[_SFPBRFSummaryItemPairWithButtonCardSection thumbnail_2]
+ -[_SFPBRFSummaryItemPairWithButtonCardSection writeTo:]
+ -[_SFPBRFSummaryItemPairWithButtonCardSection(FacadeInitializer) initWithFacade:]
+ -[_SFPBSportsItem isEventLive]
+ -[_SFPBSportsItem setIsEventLive:]
+ -[_SFPBToggleButtonConfiguration iconOnly]
+ -[_SFPBToggleButtonConfiguration setIconOnly:]
+ GCC_except_table2850
+ GCC_except_table6574
+ GCC_except_table8234
+ _OBJC_CLASS_$_RFDataImage
+ _OBJC_CLASS_$_RFSummaryItemPairWithButtonCardSection
+ _OBJC_CLASS_$__SFPBRFDataImage
+ _OBJC_CLASS_$__SFPBRFSummaryItemPairWithButtonCardSection
+ _OBJC_IVAR_$_RFAppIconImage._backup_image
+ _OBJC_IVAR_$_RFDataImage._aspect_ratio
+ _OBJC_IVAR_$_RFDataImage._background_color
+ _OBJC_IVAR_$_RFDataImage._corner_rounding_mode
+ _OBJC_IVAR_$_RFDataImage._dark_mode_data
+ _OBJC_IVAR_$_RFDataImage._data
+ _OBJC_IVAR_$_RFDataImage._has
+ _OBJC_IVAR_$_RFDataImage._image_style
+ _OBJC_IVAR_$_RFDataImage._punches_through_background
+ _OBJC_IVAR_$_RFDataImage._sizing_mode
+ _OBJC_IVAR_$_RFDataImage._vibrancy
+ _OBJC_IVAR_$_RFImageSource._data_image
+ _OBJC_IVAR_$_RFSummaryItemPairWithButtonCardSection._button_1
+ _OBJC_IVAR_$_RFSummaryItemPairWithButtonCardSection._text_1
+ _OBJC_IVAR_$_RFSummaryItemPairWithButtonCardSection._text_2
+ _OBJC_IVAR_$_RFSummaryItemPairWithButtonCardSection._text_3
+ _OBJC_IVAR_$_RFSummaryItemPairWithButtonCardSection._text_4
+ _OBJC_IVAR_$_RFSummaryItemPairWithButtonCardSection._text_5
+ _OBJC_IVAR_$_RFSummaryItemPairWithButtonCardSection._text_6
+ _OBJC_IVAR_$_RFSummaryItemPairWithButtonCardSection._text_7
+ _OBJC_IVAR_$_RFSummaryItemPairWithButtonCardSection._text_8
+ _OBJC_IVAR_$_RFSummaryItemPairWithButtonCardSection._thumbnail_1
+ _OBJC_IVAR_$_RFSummaryItemPairWithButtonCardSection._thumbnail_2
+ _OBJC_IVAR_$_SFCardSectionValue._rfSummaryItemPairWithButtonCardSection
+ _OBJC_IVAR_$_SFSportsItem._isEventLive
+ _OBJC_IVAR_$_SFToggleButtonConfiguration._has
+ _OBJC_IVAR_$_SFToggleButtonConfiguration._iconOnly
+ _OBJC_IVAR_$__SFPBCardSectionValue._rfSummaryItemPairWithButtonCardSection
+ _OBJC_IVAR_$__SFPBRFAppIconImage._backup_image
+ _OBJC_IVAR_$__SFPBRFDataImage._aspect_ratio
+ _OBJC_IVAR_$__SFPBRFDataImage._background_color
+ _OBJC_IVAR_$__SFPBRFDataImage._corner_rounding_mode
+ _OBJC_IVAR_$__SFPBRFDataImage._dark_mode_data
+ _OBJC_IVAR_$__SFPBRFDataImage._data
+ _OBJC_IVAR_$__SFPBRFDataImage._image_style
+ _OBJC_IVAR_$__SFPBRFDataImage._punches_through_background
+ _OBJC_IVAR_$__SFPBRFDataImage._sizing_mode
+ _OBJC_IVAR_$__SFPBRFDataImage._vibrancy
+ _OBJC_IVAR_$__SFPBRFImageSource._data_image
+ _OBJC_IVAR_$__SFPBRFSummaryItemPairWithButtonCardSection._button_1
+ _OBJC_IVAR_$__SFPBRFSummaryItemPairWithButtonCardSection._text_1
+ _OBJC_IVAR_$__SFPBRFSummaryItemPairWithButtonCardSection._text_2
+ _OBJC_IVAR_$__SFPBRFSummaryItemPairWithButtonCardSection._text_3
+ _OBJC_IVAR_$__SFPBRFSummaryItemPairWithButtonCardSection._text_4
+ _OBJC_IVAR_$__SFPBRFSummaryItemPairWithButtonCardSection._text_5
+ _OBJC_IVAR_$__SFPBRFSummaryItemPairWithButtonCardSection._text_6
+ _OBJC_IVAR_$__SFPBRFSummaryItemPairWithButtonCardSection._text_7
+ _OBJC_IVAR_$__SFPBRFSummaryItemPairWithButtonCardSection._text_8
+ _OBJC_IVAR_$__SFPBRFSummaryItemPairWithButtonCardSection._thumbnail_1
+ _OBJC_IVAR_$__SFPBRFSummaryItemPairWithButtonCardSection._thumbnail_2
+ _OBJC_IVAR_$__SFPBSportsItem._isEventLive
+ _OBJC_IVAR_$__SFPBToggleButtonConfiguration._iconOnly
+ _OBJC_METACLASS_$_RFDataImage
+ _OBJC_METACLASS_$_RFSummaryItemPairWithButtonCardSection
+ _OBJC_METACLASS_$__SFPBRFDataImage
+ _OBJC_METACLASS_$__SFPBRFSummaryItemPairWithButtonCardSection
+ __OBJC_$_CLASS_METHODS_RFDataImage
+ __OBJC_$_CLASS_METHODS_RFSummaryItemPairWithButtonCardSection
+ __OBJC_$_CLASS_PROP_LIST_RFDataImage
+ __OBJC_$_CLASS_PROP_LIST_RFSummaryItemPairWithButtonCardSection
+ __OBJC_$_CLASS_PROP_LIST__SFPBRFDataImage
+ __OBJC_$_CLASS_PROP_LIST__SFPBRFSummaryItemPairWithButtonCardSection
+ __OBJC_$_INSTANCE_METHODS_RFDataImage(ProtobufInitializer)
+ __OBJC_$_INSTANCE_METHODS_RFSummaryItemPairWithButtonCardSection(ProtobufInitializer)
+ __OBJC_$_INSTANCE_METHODS__SFPBRFDataImage(FacadeInitializer)
+ __OBJC_$_INSTANCE_METHODS__SFPBRFSummaryItemPairWithButtonCardSection(FacadeInitializer)
+ __OBJC_$_INSTANCE_VARIABLES_RFDataImage
+ __OBJC_$_INSTANCE_VARIABLES_RFSummaryItemPairWithButtonCardSection
+ __OBJC_$_INSTANCE_VARIABLES__SFPBRFDataImage
+ __OBJC_$_INSTANCE_VARIABLES__SFPBRFSummaryItemPairWithButtonCardSection
+ __OBJC_$_PROP_LIST_RFDataImage
+ __OBJC_$_PROP_LIST_RFSummaryItemPairWithButtonCardSection
+ __OBJC_$_PROP_LIST__SFPBRFDataImage
+ __OBJC_$_PROP_LIST__SFPBRFSummaryItemPairWithButtonCardSection
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_RFDataImage
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_RFSummaryItemPairWithButtonCardSection
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__SFPBRFDataImage
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__SFPBRFSummaryItemPairWithButtonCardSection
+ __OBJC_$_PROTOCOL_METHOD_TYPES_RFDataImage
+ __OBJC_$_PROTOCOL_METHOD_TYPES_RFSummaryItemPairWithButtonCardSection
+ __OBJC_$_PROTOCOL_METHOD_TYPES__SFPBRFDataImage
+ __OBJC_$_PROTOCOL_METHOD_TYPES__SFPBRFSummaryItemPairWithButtonCardSection
+ __OBJC_$_PROTOCOL_REFS_RFDataImage
+ __OBJC_$_PROTOCOL_REFS_RFSummaryItemPairWithButtonCardSection
+ __OBJC_$_PROTOCOL_REFS__SFPBRFDataImage
+ __OBJC_$_PROTOCOL_REFS__SFPBRFSummaryItemPairWithButtonCardSection
+ __OBJC_CLASS_PROTOCOLS_$_RFDataImage
+ __OBJC_CLASS_PROTOCOLS_$_RFSummaryItemPairWithButtonCardSection
+ __OBJC_CLASS_PROTOCOLS_$__SFPBRFDataImage
+ __OBJC_CLASS_PROTOCOLS_$__SFPBRFSummaryItemPairWithButtonCardSection
+ __OBJC_CLASS_RO_$_RFDataImage
+ __OBJC_CLASS_RO_$_RFSummaryItemPairWithButtonCardSection
+ __OBJC_CLASS_RO_$__SFPBRFDataImage
+ __OBJC_CLASS_RO_$__SFPBRFSummaryItemPairWithButtonCardSection
+ __OBJC_LABEL_PROTOCOL_$_RFDataImage
+ __OBJC_LABEL_PROTOCOL_$_RFSummaryItemPairWithButtonCardSection
+ __OBJC_LABEL_PROTOCOL_$__SFPBRFDataImage
+ __OBJC_LABEL_PROTOCOL_$__SFPBRFSummaryItemPairWithButtonCardSection
+ __OBJC_METACLASS_RO_$_RFDataImage
+ __OBJC_METACLASS_RO_$_RFSummaryItemPairWithButtonCardSection
+ __OBJC_METACLASS_RO_$__SFPBRFDataImage
+ __OBJC_METACLASS_RO_$__SFPBRFSummaryItemPairWithButtonCardSection
+ __OBJC_PROTOCOL_$_RFDataImage
+ __OBJC_PROTOCOL_$_RFSummaryItemPairWithButtonCardSection
+ __OBJC_PROTOCOL_$__SFPBRFDataImage
+ __OBJC_PROTOCOL_$__SFPBRFSummaryItemPairWithButtonCardSection
+ __SFPBRFDataImageReadFrom
+ __SFPBRFSummaryItemPairWithButtonCardSectionReadFrom
- GCC_except_table2844
- GCC_except_table6562
- GCC_except_table8186
CStrings:
+ "ButtonItemStylePlain"
+ "backupImage"
+ "darkModeData"
+ "dataImage"
+ "iconOnly"
+ "isEventLive"
+ "rfSummaryItemPairWithButtonCardSection"
```
