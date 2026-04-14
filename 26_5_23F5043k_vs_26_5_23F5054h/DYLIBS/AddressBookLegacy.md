## AddressBookLegacy

> `/System/Library/PrivateFrameworks/AddressBookLegacy.framework/AddressBookLegacy`

```diff

-12851.600.2.0.0
-  __TEXT.__text: 0x75ec8
-  __TEXT.__auth_stubs: 0x2210
+12851.600.11.0.0
+  __TEXT.__text: 0x764c8
+  __TEXT.__auth_stubs: 0x2200
   __TEXT.__objc_methlist: 0x3054
-  __TEXT.__const: 0x341
-  __TEXT.__cstring: 0x26b7a
-  __TEXT.__oslogstring: 0x270f
+  __TEXT.__const: 0x361
+  __TEXT.__cstring: 0x26be8
+  __TEXT.__oslogstring: 0x2a30
   __TEXT.__gcc_except_tab: 0x638
   __TEXT.__dlopen_cstrs: 0xb8
   __TEXT.__ustring: 0x24c
-  __TEXT.__unwind_info: 0x1a30
+  __TEXT.__unwind_info: 0x1a48
   __TEXT.__objc_classname: 0x51d
-  __TEXT.__objc_methname: 0x937c
+  __TEXT.__objc_methname: 0x9397
   __TEXT.__objc_methtype: 0x14e7
-  __TEXT.__objc_stubs: 0x7cc0
+  __TEXT.__objc_stubs: 0x7ce0
   __DATA_CONST.__got: 0x5d8
   __DATA_CONST.__const: 0x27f8
   __DATA_CONST.__objc_classlist: 0x198
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2520
+  __DATA_CONST.__objc_selrefs: 0x2528
   __DATA_CONST.__objc_superrefs: 0x100
   __DATA_CONST.__objc_arraydata: 0x48
-  __AUTH_CONST.__auth_got: 0x1118
-  __AUTH_CONST.__const: 0xe80
-  __AUTH_CONST.__cfstring: 0xdae0
+  __AUTH_CONST.__auth_got: 0x1110
+  __AUTH_CONST.__const: 0xea0
+  __AUTH_CONST.__cfstring: 0xdb00
   __AUTH_CONST.__objc_const: 0x4cb0
   __AUTH_CONST.__objc_doubleobj: 0x60
   __AUTH_CONST.__objc_intobj: 0x120

   __DATA.__objc_ivar: 0x400
   __DATA.__data: 0x2c8
   __DATA.__common: 0x4
-  __DATA.__bss: 0x358
+  __DATA.__bss: 0x368
   __DATA_DIRTY.__objc_data: 0x500
   __DATA_DIRTY.__data: 0x128
   __DATA_DIRTY.__bss: 0x100

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 73C46D2D-F02F-3BC7-AF84-A0FF2CB7801F
-  Functions: 2582
-  Symbols:   7318
-  CStrings:  6111
+  UUID: B6248940-9339-3460-BF98-977E21ACB314
+  Functions: 2588
+  Symbols:   7361
+  CStrings:  6119
 
Symbols:
+ _ABImageUtilsCopySyncImageForPerson.cold.10
+ _ABImageUtilsCopySyncImageForPerson.cold.11
+ _ABImageUtilsCopySyncImageForPerson.cold.12
+ _ABImageUtilsCopySyncImageForPerson.cold.13
+ _ABImageUtilsCopySyncImageForPerson.cold.14
+ _ABImageUtilsCopySyncImageForPerson.cold.15
+ _ABImageUtilsCopySyncImageForPerson.cold.16
+ _ABImageUtilsCopySyncImageForPerson.cold.17
+ _ABImageUtilsCopySyncImageForPerson.cold.18
+ _ABImageUtilsCopySyncImageForPerson.cold.19
+ _ABImageUtilsCopySyncImageForPerson.cold.20
+ _ABImageUtilsCopySyncImageForPerson.cold.21
+ _ABImageUtilsCopySyncImageForPerson.cold.22
+ _ABImageUtilsCopySyncImageForPerson.cold.23
+ _ABImageUtilsCopySyncImageForPerson.cold.8
+ _ABImageUtilsCopySyncImageForPerson.cold.9
+ _ABImageUtilsIsUTTypeInSyncCompatibleFormat
+ _ABImageUtilsTypeOfImageData
+ __ABImageUtilsSyncLog.log
+ __ABImageUtilsSyncLog.onceToken
+ ___ABAddressBookPersonBufferRowHandler_block_invoke.527
+ ____ABImageUtilsSyncLog_block_invoke
+ _objc_msgSend$preferredFilenameExtension
- ___ABAddressBookPersonBufferRowHandler_block_invoke.524
- __copyImageDataReducedUpToSize
- _objc_retain_x26
CStrings:
+ " ), all_person_ids(rowid%@) AS (SELECT pm.rowid%@ FROM preferredmatched pm JOIN ABPerson p ON p.rowid = pm.rowid AND p.PersonLink = -1 UNION ALL SELECT abp.rowid%@ FROM preferredmatched pm JOIN ABPerson p ON p.rowid = pm.rowid AND p.PersonLink != -1 JOIN ABPerson abp ON abp.PersonLink = p.PersonLink ) "
+ " FROM all_person_ids JOIN ABPerson abp ON abp.rowid = all_person_ids.rowid "
+ " FROM preferredmatched JOIN ABPerson abp on (abp.rowid = preferredmatched.rowid) "
+ "%@.SortLanguageIndex, %@.SortSection, %@.Sort "
+ "(unknown)"
+ ", FirstSortLanguageIndex, FirstSortSection, FirstSort"
+ ", LastSortLanguageIndex, LastSortSection, LastSort"
+ ", SortLanguageIndex, SortSection, Sort"
+ ", pm.SortLanguageIndex, pm.SortSection, pm.Sort"
+ "/tmp/%i-savedSyncImage.%@"
+ "Original image is %{public}@ with byteCount=%lu with thumbnail crop rect (%i, %i, %i, %i)"
+ "SELECT rowid%@ FROM ABPerson abp WHERE abp.rowid IN (SELECT rowid FROM matched WHERE matched.personlink = -1 UNION "
+ "SELECT rowid%@ FROM ABPerson where rowid in ( "
+ "WITH preferredmatched(rowid%@) as ( "
+ "[Likeness Update] ABImageUtilsCopySyncImageForPerson: FAILED to produce JPEG sync image (%{public}@). Proceeding without sync image."
+ "[Likeness Update] ABImageUtilsCopySyncImageForPerson: FAILED to produce sync image, byteCount=%lu, maxByteCount=%u. Proceeding without sync image."
+ "[Likeness Update] ABImageUtilsCopySyncImageForPerson: SUCCESS format=%{public}@, byteCount=%lu, maxByteCount=%u"
+ "[Likeness Update] ABImageUtilsCopySyncImageForPerson: original (%{public}@) not usable (byteCount=%lu, isSyncCompatible=%{BOOL}d), trying reduction with preserveAlpha=%{BOOL}d"
+ "[Likeness Update] ABImageUtilsCopySyncImageForPerson: originalFormat=%{public}@, isAlphaSupportedType=%{BOOL}d, hasAlpha=%{BOOL}d, originalByteCount=%lu, maxByteCount=%u, dimensions=%ix%i"
+ "[Likeness Update] ABImageUtilsCopySyncImageForPerson: returning original image as-is, byteCount=%lu, isSyncCompatible=YES"
+ "[Likeness Update] ABImageUtilsCopySyncImageForPerson: returning saved sync image, byteCount=%lu, isSyncCompatible=%{BOOL}d"
+ "[Likeness Update] Exit ABImageUtilsCopySyncImageForPerson: no sync image"
+ "[Likeness Update] Exit ABImageUtilsCopySyncImageForPerson: sync image of type %{public}@, byteCount=%lu with thumbnail crop rect (%i, %i, %i, %i)"
+ "all_person_ids"
+ "image-util-sync"
+ "preferredFilenameExtension"
+ "preferredmatched"
+ "unknown"
- " FROM preferredmatched "
- " JOIN ABPerson abp on (abp.rowid = preferredmatched.rowid) "
- " JOIN ABPerson abp on (abp2.personlink != -1 and abp2.personlink = abp.personlink) OR (abp.rowid = abp2.rowid) "
- " LEFT JOIN ABPerson abp2 on (abp2.rowid = preferredmatched.rowid) "
- ", FirstSortLanguageIndex, FirstSortSection, FirstSort "
- ", LastSortLanguageIndex, LastSortSection, LastSort "
- "/tmp/%i-origImage.jpg"
- "/tmp/%i-savedSyncImage.jpg"
- "ABBufferQuery: unrecognized sorte order: %u"
- "Original image has length = %lu with thumbnail crop rect (%i, %i, %i, %i)"
- "Returning the AB saved sync image."
- "Returning the original image."
- "SELECT rowid %@ FROM ABPerson abp WHERE abp.rowid IN (SELECT rowid FROM matched WHERE matched.personlink = -1 UNION "
- "SELECT rowid %@ FROM ABPerson where rowid in ( "
- "WITH preferredmatched(rowid %@) as ( "
- "[Likeness Update] Exit ABImageUtilsCopySyncImageForPerson: sync image length = %lu with thumbnail crop rect (%i, %i, %i, %i)"
- "[Likeness Update] Scaling failed to reduce to max size, trying again without alpha preservation by allowing JPEG conversion."
- "[Likeness Update] Scaling/compression failed to reduce image of size %lu to max size %u. Proceeding without sync image."
- "preferredmatched.FirstSortLanguageIndex, preferredmatched.FirstSortSection, preferredmatched.FirstSort "
- "preferredmatched.LastSortLanguageIndex, preferredmatched.LastSortSection, preferredmatched.LastSort "
- "public.heic"

```
