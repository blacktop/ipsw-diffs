## AddressBookLegacy

> `/System/Library/PrivateFrameworks/AddressBookLegacy.framework/AddressBookLegacy`

```diff

-12695.0.0.0.0
-  __TEXT.__text: 0x6ddfc
+12699.0.0.0.0
+  __TEXT.__text: 0x6e25c
   __TEXT.__auth_stubs: 0x2190
-  __TEXT.__objc_methlist: 0x2c78
+  __TEXT.__objc_methlist: 0x2cc8
   __TEXT.__const: 0x268
-  __TEXT.__cstring: 0x23109
+  __TEXT.__cstring: 0x24017
   __TEXT.__oslogstring: 0x1a74
-  __TEXT.__gcc_except_tab: 0x560
+  __TEXT.__gcc_except_tab: 0x570
   __TEXT.__dlopen_cstrs: 0xb8
   __TEXT.__ustring: 0x1b8
-  __TEXT.__unwind_info: 0x1774
+  __TEXT.__unwind_info: 0x1788
   __TEXT.__objc_classname: 0x4bc
-  __TEXT.__objc_methname: 0x8c7d
-  __TEXT.__objc_methtype: 0x13e0
-  __TEXT.__objc_stubs: 0x77a0
+  __TEXT.__objc_methname: 0x8d4f
+  __TEXT.__objc_methtype: 0x1418
+  __TEXT.__objc_stubs: 0x7860
   __DATA_CONST.__got: 0x1e8
-  __DATA_CONST.__const: 0x2568
+  __DATA_CONST.__const: 0x25b8
   __DATA_CONST.__objc_classlist: 0x178
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x36d8
-  __DATA_CONST.__objc_selrefs: 0x2310
+  __DATA_CONST.__objc_const: 0x36f8
+  __DATA_CONST.__objc_selrefs: 0x2340
   __DATA_CONST.__objc_arraydata: 0x48
-  __AUTH_CONST.__cfstring: 0xcda0
+  __AUTH_CONST.__cfstring: 0xcee0
   __AUTH_CONST.__const: 0xdd0
   __AUTH_CONST.__objc_const: 0x1338
   __AUTH_CONST.__objc_doubleobj: 0x60

   __AUTH.__objc_data: 0xa00
   __DATA.__objc_classrefs: 0x3a0
   __DATA.__objc_superrefs: 0xf8
-  __DATA.__objc_ivar: 0x3c8
+  __DATA.__objc_ivar: 0x3cc
   __DATA.__data: 0x3a8
-  __DATA.__common: 0x0
+  __DATA.__common: 0x10
   __DATA.__bss: 0x258
   __DATA_DIRTY.__objc_data: 0x4b0
   __DATA_DIRTY.__data: 0x130

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 90493ABA-E2DB-3E8D-B34D-0061FCF4FE2F
-  Functions: 2308
-  Symbols:   6611
-  CStrings:  5720
+  UUID: 72F79353-B594-3E88-93CB-A6BD6A166C50
+  Functions: 2315
+  Symbols:   6636
+  CStrings:  5750
 
Symbols:
+ +[ABVCardCardDAVExporter copyVCardRepresentationOfRecord:withPhoto:extraPhotoParameters:includeWallpaper:]
+ +[ABVCardCardDAVRecord includeWallpaperURIInVCards]
+ +[ABVCardRecord includeWallpaperURIInVCards]
+ -[ABVCardCardDAVParser importToGroup:]
+ -[ABVCardCardDAVParser importToPerson:]
+ -[ABVCardCardDAVParser initWithData:importOptions:]
+ -[ABVCardCardDAVParser initWithData:watchdogTimer:importOptions:]
+ -[ABVCardCardDAVValueSetter initWithGroup:options:]
+ -[ABVCardCardDAVValueSetter initWithPerson:options:]
+ -[ABVCardParser parseWallpaper:]
+ -[ABVCardRecord _copyVCardRepresentationAsStringIncludeExternalProperties:withPhoto:extraPhotoParameters:includePrivateData:includeWallpaper:]
+ GCC_except_table100
+ GCC_except_table101
+ GCC_except_table81
+ GCC_except_table88
+ GCC_except_table89
+ GCC_except_table98
+ _OBJC_IVAR_$_ABVCardCardDAVParser._importOptions
+ _OBJC_IVAR_$_ABVCardCardDAVValueSetter._wallpaperSupported
+ ___block_literal_global.166
+ ___block_literal_global.414
+ ___block_literal_global.71
+ ___block_literal_global.768
+ _kABCPersonSensitiveContentConfigurationProperty
+ _kABCPersonWallpaperURIProperty
+ _kABPersonSensitiveContentConfigurationProperty
+ _kABPersonWallpaperURIProperty
+ _objc_msgSend$_copyVCardRepresentationAsStringIncludeExternalProperties:withPhoto:extraPhotoParameters:includePrivateData:includeWallpaper:
+ _objc_msgSend$copyVCardRepresentationOfRecord:withPhoto:extraPhotoParameters:includeWallpaper:
+ _objc_msgSend$importToGroup:
+ _objc_msgSend$importToPerson:
+ _objc_msgSend$includeWallpaperURIInVCards
+ _objc_msgSend$initWithData:watchdogTimer:importOptions:
+ _objc_msgSend$initWithGroup:options:
+ _objc_msgSend$initWithPerson:options:
+ _objc_msgSend$parseWallpaper:
- -[ABVCardCardDAVValueSetter initWithGroup:removeExistingProperties:]
- -[ABVCardCardDAVValueSetter initWithPerson:removeExistingProperties:]
- -[ABVCardParser parseWallpaper]
- -[ABVCardRecord _copyVCardRepresentationAsStringIncludeExternalProperties:withPhoto:extraPhotoParameters:includePrivateData:]
- GCC_except_table78
- GCC_except_table85
- GCC_except_table86
- GCC_except_table95
- GCC_except_table96
- GCC_except_table97
- _OBJC_IVAR_$_ABVCardCardDAVParser._removeExistingProperties
- ___block_literal_global.160
- ___block_literal_global.411
- ___block_literal_global.68
- ___block_literal_global.752
- _objc_msgSend$_copyVCardRepresentationAsStringIncludeExternalProperties:withPhoto:extraPhotoParameters:includePrivateData:
- _objc_msgSend$initWithGroup:removeExistingProperties:
- _objc_msgSend$initWithPerson:removeExistingProperties:
CStrings:
+ "-[ABVCardCardDAVParser importToGroup:]"
+ "-[ABVCardCardDAVParser importToPerson:]"
+ "-[ABVCardRecord _copyVCardRepresentationAsStringIncludeExternalProperties:withPhoto:extraPhotoParameters:includePrivateData:includeWallpaper:]"
+ "@32@0:8^v16Q24"
+ "@40@0:8@16@24Q32"
+ "@44@0:8B16@20@28B36B40"
+ "@44@0:8^v16@24@32B40"
+ "@72@0:8^v16@24^{__CFSet=}32B40I44q48@56q64"
+ "CREATE TABLE ABPerson (ROWID INTEGER PRIMARY KEY AUTOINCREMENT, First TEXT, Last TEXT, Middle TEXT, FirstPhonetic TEXT, MiddlePhonetic TEXT, LastPhonetic TEXT, Organization TEXT, Department TEXT, Note TEXT, Kind INTEGER, Birthday TEXT, JobTitle TEXT, Nickname TEXT, Prefix TEXT, Suffix TEXT, FirstSort TEXT, LastSort TEXT, CreationDate INTEGER, ModificationDate INTEGER, CompositeNameFallback TEXT, ExternalIdentifier TEXT, ExternalModificationTag TEXT, ExternalUUID TEXT, StoreID INTEGER, DisplayName TEXT, ExternalRepresentation BLOB, FirstSortSection TEXT, LastSortSection TEXT, FirstSortLanguageIndex INTEGER DEFAULT 2147483647, LastSortLanguageIndex INTEGER DEFAULT 2147483647, PersonLink INTEGER DEFAULT -1, ImageURI TEXT, IsPreferredName INTEGER DEFAULT 1, guid TEXT NOT NULL DEFAULT (ab_generate_guid()), PhonemeData TEXT, AlternateBirthday TEXT, MapsData TEXT, FirstPronunciation TEXT, MiddlePronunciation TEXT, LastPronunciation TEXT, OrganizationPhonetic TEXT, OrganizationPronunciation TEXT, PreviousFamilyName TEXT, PreferredLikenessSource TEXT, PreferredPersonaIdentifier TEXT, PreferredChannel TEXT, DowntimeWhitelist TEXT, ImageType TEXT, ImageHash BLOB, MemojiMetadata BLOB, Wallpaper BLOB, DisplayFlags INTEGER, WatchWallpaperImageData BLOB, WallpaperMetadata BLOB, ImageBackgroundColorsData BLOB, SensitiveContentConfiguration BLOB, WallpaperURI TEXT, UNIQUE(guid));"
+ "INSERT INTO ABPerson (ROWID, First, Last, Middle, FirstPhonetic, MiddlePhonetic, LastPhonetic, Organization, Department, Note, Kind, Birthday, JobTitle, Nickname, Prefix, Suffix, FirstSort, LastSort, CreationDate, ModificationDate, CompositeNameFallback, StoreID, ExternalIdentifier, ExternalModificationTag, ExternalUUID, ExternalRepresentation, FirstSortSection, LastSortSection, FirstSortLanguageIndex, LastSortLanguageIndex, PersonLink, ImageURI, guid, PhonemeData, AlternateBirthday, MapsData, FirstPronunciation, MiddlePronunciation, LastPronunciation, OrganizationPhonetic, OrganizationPronunciation, PreviousFamilyName, PreferredLikenessSource, PreferredPersonaIdentifier, PreferredChannel, DowntimeWhitelist, ImageType, ImageHash, MemojiMetadata, Wallpaper, DisplayFlags, WatchWallpaperImageData, WallpaperMetadata, ImageBackgroundColorsData, SensitiveContentConfiguration) SELECT ROWID, First, Last, Middle, FirstPhonetic, MiddlePhonetic, LastPhonetic, Organization, Department, Note, Kind, ab_normalize_date(Birthday), JobTitle, Nickname, Prefix, Suffix, FirstSort, LastSort, CreationDate, ModificationDate, CompositeNameFallback, StoreID, ExternalIdentifier, ExternalModificationTag, ExternalUUID, ExternalRepresentation, FirstSortSection, LastSortSection, FirstSortLanguageIndex, LastSortLanguageIndex, PersonLink, ImageURI, ab_repair_guid(guid), PhonemeData, AlternateBirthday, MapsData , FirstPronunciation, MiddlePronunciation, LastPronunciation, OrganizationPhonetic, OrganizationPronunciation, PreviousFamilyName, PreferredLikenessSource, PreferredPersonaIdentifier, PreferredChannel, DowntimeWhitelist, ImageType, ImageHash, MemojiMetadata, Wallpaper, DisplayFlags, WatchWallpaperImageData, WallpaperMetadata, ImageBackgroundColorsData, SensitiveContentConfiguration FROM ABPerson_old;"
+ "INSERT INTO ABPerson (ROWID, First, Last, Middle, FirstPhonetic, MiddlePhonetic, LastPhonetic, Organization, Department, Note, Kind, Birthday, JobTitle, Nickname, Prefix, Suffix, FirstSort, LastSort, CreationDate, ModificationDate, CompositeNameFallback, StoreID, ExternalIdentifier, ExternalModificationTag, ExternalUUID, ExternalRepresentation, FirstSortSection, LastSortSection, FirstSortLanguageIndex, LastSortLanguageIndex, PersonLink, ImageURI, guid, PhonemeData, AlternateBirthday, MapsData, FirstPronunciation, MiddlePronunciation, LastPronunciation, OrganizationPhonetic, OrganizationPronunciation, PreviousFamilyName, PreferredLikenessSource, PreferredPersonaIdentifier, PreferredChannel, DowntimeWhitelist, ImageType, ImageHash, MemojiMetadata, Wallpaper, DisplayFlags, WatchWallpaperImageData, WallpaperMetadata, ImageBackgroundColorsData, SensitiveContentConfiguration, WallpaperURI) SELECT ROWID, First, Last, Middle, FirstPhonetic, MiddlePhonetic, LastPhonetic, Organization, Department, Note, Kind, ab_normalize_date(Birthday), JobTitle, Nickname, Prefix, Suffix, FirstSort, LastSort, CreationDate, ModificationDate, CompositeNameFallback, StoreID, ExternalIdentifier, ExternalModificationTag, ExternalUUID, ExternalRepresentation, FirstSortSection, LastSortSection, FirstSortLanguageIndex, LastSortLanguageIndex, PersonLink, ImageURI, ab_repair_guid(guid), PhonemeData, AlternateBirthday, MapsData , FirstPronunciation, MiddlePronunciation, LastPronunciation, OrganizationPhonetic, OrganizationPronunciation, PreviousFamilyName, PreferredLikenessSource, PreferredPersonaIdentifier, PreferredChannel, DowntimeWhitelist, ImageType, ImageHash, MemojiMetadata, Wallpaper, DisplayFlags, WatchWallpaperImageData, WallpaperMetadata, ImageBackgroundColorsData, SensitiveContentConfiguration, WallpaperURI FROM ABPerson_old;"
+ "SensitiveContentConfiguration"
+ "Tq,N,V_countOfContactsInBuffer"
+ "Tq,N,V_maxContactsPerBatch"
+ "VND-63-SENSITIVE-CONTENT-CONFIG"
+ "VND-63-SENSITIVE-CONTENT-CONFIG:"
+ "VND-63-WALLPAPER"
+ "VND-63-WALLPAPER;ENCODING=b:"
+ "VND-63-WALLPAPER;VALUE=uri:"
+ "WallpaperURI"
+ "X-WALLPAPER"
+ "_copyVCardRepresentationAsStringIncludeExternalProperties:withPhoto:extraPhotoParameters:includePrivateData:includeWallpaper:"
+ "_importOptions"
+ "_wallpaperSupported"
+ "copyVCardRepresentationOfRecord:withPhoto:extraPhotoParameters:includeWallpaper:"
+ "importToGroup:"
+ "importToPerson:"
+ "includeWallpaperURIInVCards"
+ "initWithData:importOptions:"
+ "initWithData:watchdogTimer:importOptions:"
+ "initWithGroup:options:"
+ "initWithPerson:options:"
+ "parseWallpaper:"
- "-[ABVCardCardDAVParser importToGroup:removeExistingProperties:]"
- "-[ABVCardCardDAVParser importToPerson:removeExistingProperties:]"
- "-[ABVCardRecord _copyVCardRepresentationAsStringIncludeExternalProperties:withPhoto:extraPhotoParameters:includePrivateData:]"
- "@40@0:8B16@20@28B36"
- "@72@0:8^v16@24^{__CFSet=}32B40I44Q48@56q64"
- "CREATE TABLE ABPerson (ROWID INTEGER PRIMARY KEY AUTOINCREMENT, First TEXT, Last TEXT, Middle TEXT, FirstPhonetic TEXT, MiddlePhonetic TEXT, LastPhonetic TEXT, Organization TEXT, Department TEXT, Note TEXT, Kind INTEGER, Birthday TEXT, JobTitle TEXT, Nickname TEXT, Prefix TEXT, Suffix TEXT, FirstSort TEXT, LastSort TEXT, CreationDate INTEGER, ModificationDate INTEGER, CompositeNameFallback TEXT, ExternalIdentifier TEXT, ExternalModificationTag TEXT, ExternalUUID TEXT, StoreID INTEGER, DisplayName TEXT, ExternalRepresentation BLOB, FirstSortSection TEXT, LastSortSection TEXT, FirstSortLanguageIndex INTEGER DEFAULT 2147483647, LastSortLanguageIndex INTEGER DEFAULT 2147483647, PersonLink INTEGER DEFAULT -1, ImageURI TEXT, IsPreferredName INTEGER DEFAULT 1, guid TEXT NOT NULL DEFAULT (ab_generate_guid()), PhonemeData TEXT, AlternateBirthday TEXT, MapsData TEXT, FirstPronunciation TEXT, MiddlePronunciation TEXT, LastPronunciation TEXT, OrganizationPhonetic TEXT, OrganizationPronunciation TEXT, PreviousFamilyName TEXT, PreferredLikenessSource TEXT, PreferredPersonaIdentifier TEXT, PreferredChannel TEXT, DowntimeWhitelist TEXT, ImageType TEXT, ImageHash BLOB, MemojiMetadata BLOB, Wallpaper BLOB, DisplayFlags INTEGER, WatchWallpaperImageData BLOB, WallpaperMetadata BLOB, ImageBackgroundColorsData BLOB, UNIQUE(guid));"
- "TQ,N,V_countOfContactsInBuffer"
- "TQ,N,V_maxContactsPerBatch"
- "_copyVCardRepresentationAsStringIncludeExternalProperties:withPhoto:extraPhotoParameters:includePrivateData:"
- "_removeExistingProperties"
- "initWithGroup:removeExistingProperties:"
- "initWithPerson:removeExistingProperties:"
- "parseWallpaper"

```
