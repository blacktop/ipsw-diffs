## vCard

> `/System/Library/PrivateFrameworks/vCard.framework/vCard`

```diff

-3624.2.0.0.0
-  __TEXT.__text: 0x236d4
+3630.0.0.0.0
+  __TEXT.__text: 0x23878
   __TEXT.__auth_stubs: 0x830
-  __TEXT.__objc_methlist: 0x32d4
+  __TEXT.__objc_methlist: 0x3314
   __TEXT.__const: 0x184
-  __TEXT.__cstring: 0x1c25
+  __TEXT.__cstring: 0x1c65
   __TEXT.__oslogstring: 0x51e
   __TEXT.__ustring: 0x8
   __TEXT.__gcc_except_tab: 0xdc

   __TEXT.__swift5_reflstr: 0x1e
   __TEXT.__unwind_info: 0xa68
   __TEXT.__objc_classname: 0x8b9
-  __TEXT.__objc_methname: 0x714d
+  __TEXT.__objc_methname: 0x7219
   __TEXT.__objc_methtype: 0xe12
-  __TEXT.__objc_stubs: 0x6220
+  __TEXT.__objc_stubs: 0x6260
   __DATA_CONST.__got: 0xf0
-  __DATA_CONST.__const: 0xd50
+  __DATA_CONST.__const: 0xd58
   __DATA_CONST.__objc_classlist: 0x298
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x5408
-  __DATA_CONST.__objc_selrefs: 0x1e28
+  __DATA_CONST.__objc_const: 0x5478
+  __DATA_CONST.__objc_selrefs: 0x1e48
   __DATA_CONST.__objc_arraydata: 0x98
   __AUTH_CONST.__objc_const: 0x0
-  __AUTH_CONST.__cfstring: 0x3420
+  __AUTH_CONST.__cfstring: 0x3460
   __AUTH_CONST.__objc_arrayobj: 0xc0
+  __AUTH_CONST.__const: 0x110
   __AUTH_CONST.__objc_doubleobj: 0x50
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__const: 0x10
   __AUTH_CONST.__auth_got: 0x428
   __AUTH.__objc_data: 0x0
   __DATA.__objc_protorefs: 0x10
   __DATA.__objc_classrefs: 0x340
   __DATA.__objc_superrefs: 0xf8
-  __DATA.__objc_ivar: 0x340
+  __DATA.__objc_ivar: 0x344
   __DATA.__objc_data: 0x38
   __DATA.__data: 0x580
   __DATA.__bss: 0x198
-  __DATA_DIRTY.__const: 0x5c0
+  __DATA_DIRTY.__const: 0x4c0
   __DATA_DIRTY.__objc_const: 0x1ee0
   __DATA_DIRTY.__objc_data: 0x1bf8
   __DATA_DIRTY.__data: 0x130

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 1171
-  Symbols:   4484
-  CStrings:  2100
+  Functions: 1176
+  Symbols:   4498
+  CStrings:  2108
 
Symbols:
+ -[CNVCard30CardBuilder addSensitiveContentConfiguration]
+ -[CNVCardFilteredPerson sensitiveContentConfiguration]
+ -[CNVCardParser parse_VND_63_SENSITIVE_CONTENT_CONFIG]
+ -[CNVCardPerson sensitiveContentConfiguration]
+ -[CNVCardPerson setSensitiveContentConfiguration:]
+ _CNVCardKeySensitiveContentConfiguration
+ _OBJC_IVAR_$_CNVCardPerson._activityAlerts
+ _OBJC_IVAR_$_CNVCardPerson._addressingGrammars
+ _OBJC_IVAR_$_CNVCardPerson._alternateBirthdayComponents
+ _OBJC_IVAR_$_CNVCardPerson._birthdayComponents
+ _OBJC_IVAR_$_CNVCardPerson._calendarURIs
+ _OBJC_IVAR_$_CNVCardPerson._cardDAVUID
+ _OBJC_IVAR_$_CNVCardPerson._department
+ _OBJC_IVAR_$_CNVCardPerson._downtimeWhitelistAuthorization
+ _OBJC_IVAR_$_CNVCardPerson._emailAddresses
+ _OBJC_IVAR_$_CNVCardPerson._firstName
+ _OBJC_IVAR_$_CNVCardPerson._imageBackgroundColorsData
+ _OBJC_IVAR_$_CNVCardPerson._imageCropRects
+ _OBJC_IVAR_$_CNVCardPerson._imageData
+ _OBJC_IVAR_$_CNVCardPerson._imageHash
+ _OBJC_IVAR_$_CNVCardPerson._imageReferences
+ _OBJC_IVAR_$_CNVCardPerson._imageType
+ _OBJC_IVAR_$_CNVCardPerson._instantMessagingAddresses
+ _OBJC_IVAR_$_CNVCardPerson._isCompany
+ _OBJC_IVAR_$_CNVCardPerson._isMe
+ _OBJC_IVAR_$_CNVCardPerson._jobTitle
+ _OBJC_IVAR_$_CNVCardPerson._largeImageCropRects
+ _OBJC_IVAR_$_CNVCardPerson._largeImageData
+ _OBJC_IVAR_$_CNVCardPerson._lastName
+ _OBJC_IVAR_$_CNVCardPerson._maidenName
+ _OBJC_IVAR_$_CNVCardPerson._memojiMetadata
+ _OBJC_IVAR_$_CNVCardPerson._middleName
+ _OBJC_IVAR_$_CNVCardPerson._nameOrder
+ _OBJC_IVAR_$_CNVCardPerson._namesOfParentGroups
+ _OBJC_IVAR_$_CNVCardPerson._nickname
+ _OBJC_IVAR_$_CNVCardPerson._note
+ _OBJC_IVAR_$_CNVCardPerson._organization
+ _OBJC_IVAR_$_CNVCardPerson._otherDateComponents
+ _OBJC_IVAR_$_CNVCardPerson._phoneNumbers
+ _OBJC_IVAR_$_CNVCardPerson._phonemeData
+ _OBJC_IVAR_$_CNVCardPerson._phoneticFirstName
+ _OBJC_IVAR_$_CNVCardPerson._phoneticLastName
+ _OBJC_IVAR_$_CNVCardPerson._phoneticMiddleName
+ _OBJC_IVAR_$_CNVCardPerson._phoneticOrganization
+ _OBJC_IVAR_$_CNVCardPerson._postalAddresses
+ _OBJC_IVAR_$_CNVCardPerson._preferredApplePersonaIdentifier
+ _OBJC_IVAR_$_CNVCardPerson._preferredLikenessSource
+ _OBJC_IVAR_$_CNVCardPerson._pronunciationFirstName
+ _OBJC_IVAR_$_CNVCardPerson._pronunciationLastName
+ _OBJC_IVAR_$_CNVCardPerson._relatedNames
+ _OBJC_IVAR_$_CNVCardPerson._sensitiveContentConfiguration
+ _OBJC_IVAR_$_CNVCardPerson._sharedPhotoDisplayPreference
+ _OBJC_IVAR_$_CNVCardPerson._socialProfiles
+ _OBJC_IVAR_$_CNVCardPerson._suffix
+ _OBJC_IVAR_$_CNVCardPerson._title
+ _OBJC_IVAR_$_CNVCardPerson._uid
+ _OBJC_IVAR_$_CNVCardPerson._unknownProperties
+ _OBJC_IVAR_$_CNVCardPerson._urls
+ _OBJC_IVAR_$_CNVCardPerson._wallpaper
+ _OBJC_IVAR_$_CNVCardPerson._watchWallpaperImageData
+ __OBJC_$_PROP_LIST_CNVCardPerson.342
+ ___block_literal_global.190
+ ___block_literal_global.222
+ ___block_literal_global.383
+ ___block_literal_global.392
+ ___block_literal_global.443
+ ___block_literal_global.446
+ ___block_literal_global.449
+ ___block_literal_global.452
+ __unnamed_array_storage.457
+ __unnamed_array_storage.509
+ _objc_msgSend$addSensitiveContentConfiguration
+ _objc_msgSend$sensitiveContentConfiguration
- OBJC_IVAR_$_CNVCardPerson._activityAlerts
- OBJC_IVAR_$_CNVCardPerson._addressingGrammars
- OBJC_IVAR_$_CNVCardPerson._alternateBirthdayComponents
- OBJC_IVAR_$_CNVCardPerson._birthdayComponents
- OBJC_IVAR_$_CNVCardPerson._calendarURIs
- OBJC_IVAR_$_CNVCardPerson._cardDAVUID
- OBJC_IVAR_$_CNVCardPerson._department
- OBJC_IVAR_$_CNVCardPerson._downtimeWhitelistAuthorization
- OBJC_IVAR_$_CNVCardPerson._emailAddresses
- OBJC_IVAR_$_CNVCardPerson._firstName
- OBJC_IVAR_$_CNVCardPerson._imageBackgroundColorsData
- OBJC_IVAR_$_CNVCardPerson._imageCropRects
- OBJC_IVAR_$_CNVCardPerson._imageData
- OBJC_IVAR_$_CNVCardPerson._imageHash
- OBJC_IVAR_$_CNVCardPerson._imageReferences
- OBJC_IVAR_$_CNVCardPerson._imageType
- OBJC_IVAR_$_CNVCardPerson._instantMessagingAddresses
- OBJC_IVAR_$_CNVCardPerson._isCompany
- OBJC_IVAR_$_CNVCardPerson._isMe
- OBJC_IVAR_$_CNVCardPerson._jobTitle
- OBJC_IVAR_$_CNVCardPerson._largeImageCropRects
- OBJC_IVAR_$_CNVCardPerson._largeImageData
- OBJC_IVAR_$_CNVCardPerson._lastName
- OBJC_IVAR_$_CNVCardPerson._maidenName
- OBJC_IVAR_$_CNVCardPerson._memojiMetadata
- OBJC_IVAR_$_CNVCardPerson._middleName
- OBJC_IVAR_$_CNVCardPerson._nameOrder
- OBJC_IVAR_$_CNVCardPerson._namesOfParentGroups
- OBJC_IVAR_$_CNVCardPerson._nickname
- OBJC_IVAR_$_CNVCardPerson._note
- OBJC_IVAR_$_CNVCardPerson._organization
- OBJC_IVAR_$_CNVCardPerson._otherDateComponents
- OBJC_IVAR_$_CNVCardPerson._phoneNumbers
- OBJC_IVAR_$_CNVCardPerson._phonemeData
- OBJC_IVAR_$_CNVCardPerson._phoneticFirstName
- OBJC_IVAR_$_CNVCardPerson._phoneticLastName
- OBJC_IVAR_$_CNVCardPerson._phoneticMiddleName
- OBJC_IVAR_$_CNVCardPerson._phoneticOrganization
- OBJC_IVAR_$_CNVCardPerson._postalAddresses
- OBJC_IVAR_$_CNVCardPerson._preferredApplePersonaIdentifier
- OBJC_IVAR_$_CNVCardPerson._preferredLikenessSource
- OBJC_IVAR_$_CNVCardPerson._pronunciationFirstName
- OBJC_IVAR_$_CNVCardPerson._pronunciationLastName
- OBJC_IVAR_$_CNVCardPerson._relatedNames
- OBJC_IVAR_$_CNVCardPerson._sharedPhotoDisplayPreference
- OBJC_IVAR_$_CNVCardPerson._socialProfiles
- OBJC_IVAR_$_CNVCardPerson._suffix
- OBJC_IVAR_$_CNVCardPerson._title
- OBJC_IVAR_$_CNVCardPerson._uid
- OBJC_IVAR_$_CNVCardPerson._unknownProperties
- OBJC_IVAR_$_CNVCardPerson._urls
- OBJC_IVAR_$_CNVCardPerson._wallpaper
- OBJC_IVAR_$_CNVCardPerson._watchWallpaperImageData
- __OBJC_$_PROP_LIST_CNVCardPerson.337
- ___block_literal_global.187
- ___block_literal_global.219
- ___block_literal_global.378
- ___block_literal_global.387
- ___block_literal_global.438
- ___block_literal_global.441
- ___block_literal_global.444
- ___block_literal_global.447
- __unnamed_array_storage.452
- __unnamed_array_storage.504
CStrings:
+ "\x0f\x02\x1f\x0e\x13"
+ "T@\"NSData\",&,V_sensitiveContentConfiguration"
+ "VND-63-SENSITIVE-CONTENT-CONFIG"
+ "_sensitiveContentConfiguration"
+ "addSensitiveContentConfiguration"
+ "parse_VND_63_SENSITIVE_CONTENT_CONFIG"
+ "sensitiveContentConfiguration"
+ "setSensitiveContentConfiguration:"
- "\x0f\x02\x1f\r\x13"

```
