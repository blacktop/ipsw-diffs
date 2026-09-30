## bookassetd

> `/System/Library/PrivateFrameworks/BookLibraryCore.framework/Support/bookassetd`

```diff

-2229.0.0.0.0
-  __TEXT.__text: 0x14ebec
-  __TEXT.__auth_stubs: 0xd90
-  __TEXT.__objc_stubs: 0xd6a0
-  __TEXT.__objc_methlist: 0x60cc
+2230.0.0.0.0
+  __TEXT.__text: 0x148494
+  __TEXT.__auth_stubs: 0xda0
+  __TEXT.__objc_stubs: 0xd020
+  __TEXT.__objc_methlist: 0x555c
   __TEXT.__const: 0x15990
-  __TEXT.__objc_classname: 0xe24
-  __TEXT.__cstring: 0x40af
-  __TEXT.__objc_methname: 0x121c6
+  __TEXT.__objc_classname: 0xdd4
+  __TEXT.__cstring: 0x3774
+  __TEXT.__objc_methname: 0x11561
   __TEXT.__oslogstring: 0xc14e
-  __TEXT.__objc_methtype: 0x31bc
+  __TEXT.__objc_methtype: 0x317d
   __TEXT.__gcc_except_tab: 0x1bcc
   __TEXT.__dlopen_cstrs: 0x66
-  __TEXT.__unwind_info: 0x1d40
+  __TEXT.__unwind_info: 0x1b70
   __TEXT.__eh_frame: 0x1620
-  __DATA_CONST.__auth_got: 0x6e0
-  __DATA_CONST.__got: 0x7e0
+  __DATA_CONST.__auth_got: 0x6e8
+  __DATA_CONST.__got: 0x8a8
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0xae80
-  __DATA_CONST.__cfstring: 0x5220
-  __DATA_CONST.__objc_classlist: 0x348
+  __DATA_CONST.__const: 0xa7c0
+  __DATA_CONST.__cfstring: 0x3740
+  __DATA_CONST.__objc_classlist: 0x328
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x140
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x288
+  __DATA_CONST.__objc_superrefs: 0x268
   __DATA_CONST.__objc_intobj: 0xc30
   __DATA_CONST.__objc_arraydata: 0x60
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_doubleobj: 0x20
-  __DATA.__objc_const: 0xd208
-  __DATA.__objc_selrefs: 0x4100
-  __DATA.__objc_ivar: 0x78c
-  __DATA.__objc_data: 0x20d0
+  __DATA.__objc_const: 0xcad0
+  __DATA.__objc_selrefs: 0x3cb8
+  __DATA.__objc_ivar: 0x770
+  __DATA.__objc_data: 0x1f90
   __DATA.__data: 0x1258
   __DATA.__bss: 0x160
   __DATA.__common: 0xa2c

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2630
-  Symbols:   556
-  CStrings:  4997
+  Functions: 2387
+  Symbols:   583
+  CStrings:  4611
 
Symbols:
+ _BLDownloadMetadataKeyAdditionalInfo
+ _BLDownloadMetadataKeyHas4K
+ _BLDownloadMetadataKeyHasDolbyVision
+ _BLDownloadMetadataKeyHasHDR
+ _BLDownloadMetadataKeyHashChunkHashes
+ _BLDownloadMetadataKeyHashChunkSize
+ _BLDownloadMetadataKeyHashChunks
+ _BLDownloadMetadataKeyIsHLS
+ _BLDownloadMetadataKeyIsZipStreamable
+ _BLDownloadMetadataKeyMD5
+ _BLDownloadMetadataKeyRequestPersistentID
+ _BLGetItemIdentifierFromValue
+ _BLGetNSNumberFromValue
+ _BLGetUnsignedLongLongFromValue
+ _BLSSDownloadAssetPropertyIsDRMFree
+ _BLSSDownloadAssetPropertyStoreFlavor
+ _BLSSDownloadAssetPropertyVideoDimensions
+ _BLSSDownloadMetadataKeyIsPurchaseRedownload
+ _BLSSDownloadPropertyIsRestore
+ _BLSSDownloadPropertyKind
+ _BLSSDownloadPropertyStoreAccountAppleID
+ _BLSSDownloadPropertyStoreAccountIdentifier
+ _BLSSDownloadPropertyStoreCollectionIdentifier
+ _BLSSDownloadPropertyStoreFrontIdentifier
+ _BLSSDownloadPropertyStoreItemIdentifier
+ _BLSSDownloadPropertyStoreSoftwareVersionIdentifier
+ _BLSSDownloadPropertyTitle
+ _OBJC_CLASS_$_BLDownloadMetadata
+ _OBJC_CLASS_$_BLItemContentRating
+ _OBJC_METACLASS_$_BLDownloadMetadata
+ _kMBBackgroundRestoreCellularAccessChangedNotification
- _GSMainScreenScaleFactor
- _OBJC_CLASS_$_NSDateFormatter
- _OBJC_CLASS_$_NSTimeZone
- _strtoull
CStrings:
+ "presentingWindow"
- "%!@(MISSING): [%!@(MISSING) %!l(MISSING)dx%!l(MISSING)d] %!@(MISSING)"
- ".%!@(MISSING)"
- "2"
- "4"
- "7"
- "@2x"
- "@32@0:8{CGSize=dd}16"
- "@40@0:8{CGSize=dd}16d32"
- "BLDownloadMetadata"
- "BLItemArtworkImage"
- "BLItemContentRating"
- "BLItemImageCollection"
- "HDR"
- "MD5HashStrings"
- "R"
- "T"
- "T@\"NSArray\",&"
- "T@\"NSArray\",R,N,V_itemImages"
- "T@\"NSData\",&"
- "T@\"NSDate\",&"
- "T@\"NSDictionary\",&"
- "T@\"NSDictionary\",R"
- "T@\"NSNumber\",&"
- "T@\"NSNumber\",C"
- "T@\"NSString\",&"
- "T@\"NSString\",C,N,V_imageKind"
- "T@\"NSURL\",&"
- "T@\"NSURL\",&,N"
- "T@\"NSURL\",C"
- "T@,C"
- "TB,GisAutomaticDownload"
- "TB,GisDeviceBasedVPP"
- "TB,GisRedownloadDownload"
- "TB,R,GhasHDR"
- "TQ"
- "T{CGSize=dd},R,N"
- "U"
- "UIRequiredDeviceCapabilities"
- "URLString"
- "V"
- "Z"
- "_assetDictionary"
- "_dateValueForValue:"
- "_dictionary"
- "_imageKind"
- "_imagesForSize:scale:"
- "_itemImages"
- "_keyStyle"
- "_newDateFormatter"
- "_newImageCollectionWithURLString:"
- "_newImagesForDictionary:"
- "_releaseDateValue"
- "_setValue:forKey:"
- "_setValue:forTopLevelKey:"
- "_setValueCopy:forMetadataKey:"
- "_setValueCopy:forProperty:"
- "_stringValueForValue:"
- "_thumbnailArtworkImage"
- "_urlValueForValue:"
- "_valueForFirstAvailableTopLevelKey:"
- "action-params"
- "apple"
- "appleID"
- "ar-movies"
- "artist-id"
- "artist-name"
- "artistId"
- "artwork-urls"
- "assets"
- "au-oflc"
- "au-tv"
- "auto-download"
- "automaticDownload"
- "bbfc"
- "be-movies"
- "bestImageForSize:"
- "betaExternalVersionIdentifier"
- "bg-movies"
- "bn-movies"
- "bo-movies"
- "box-height"
- "box-width"
- "br-movies"
- "bundle-id"
- "buy-params-256"
- "buyParams"
- "by-movies"
- "ca-chvrs"
- "ca-tv"
- "cancel-download-url"
- "caseInsensitiveCompare:"
- "ch-movies"
- "chunks"
- "cl-movies"
- "classForCoder"
- "cn-movies"
- "co-movies"
- "collection-id"
- "collection-name"
- "com.apple.MobileBackup.backgroundCellularAccessChanged"
- "compilation"
- "composer-id"
- "composerId"
- "contentRatingDictionary"
- "cr-movies"
- "cy-movies"
- "cz-movies"
- "dateFromString:"
- "de-fsk"
- "de-tv"
- "deviceBasedVPP"
- "disc-count"
- "disc-number"
- "discCount"
- "discNumber"
- "dk-movies"
- "do-movies"
- "download-permalink"
- "download-queue-item.default"
- "downloadPermalink"
- "ec-movies"
- "ee-movies"
- "episode-guid"
- "episode-number"
- "episode-sort-id"
- "epr"
- "es-movies"
- "esrb"
- "f"
- "fi-movies"
- "floatValue"
- "fr-cnc"
- "fr-tv"
- "fsk"
- "g"
- "games"
- "ge-movies"
- "genre-id"
- "genre-name"
- "genreId"
- "genreName"
- "gf-movies"
- "gr-movies"
- "gt-movies"
- "gy-movies"
- "h"
- "has-4k"
- "has-dolby-vision"
- "has-hdr"
- "hasHDR"
- "hasSuffix:"
- "hashes"
- "height"
- "high-definition"
- "hk-movies"
- "hls-playlist-url"
- "hn-movies"
- "hu-movies"
- "icon-url"
- "id-movies"
- "ie-ifco"
- "image-type"
- "imageKind"
- "imageScale"
- "imageSize"
- "imagesForKind:"
- "imagesForSize:"
- "indexOfObject:"
- "initWithArtworkDictionary:"
- "initWithCapacity:"
- "initWithImageCollection:"
- "initWithItemImages:"
- "initWithUUIDString:"
- "is-apple-music-show"
- "is-auto-download"
- "is-hls"
- "is-movies"
- "is-redownload"
- "isDeviceBased"
- "isDeviceBasedVPP"
- "isRedownloadDownload"
- "isSharedResource"
- "isStreamable"
- "it-movies"
- "itemImages"
- "itunes-games"
- "jm-movies"
- "jp-eirin"
- "jp-tv"
- "keyStyle"
- "kg-movies"
- "kh-movies"
- "kr-movies"
- "kz-movies"
- "la-movies"
- "label"
- "launch-extras-url"
- "lk-movies"
- "long-description"
- "lrpluspub"
- "lrpub"
- "lt-movies"
- "lu-movies"
- "lv-movies"
- "md-movies"
- "md5"
- "mk-movies"
- "mo-movies"
- "movement"
- "movement-count"
- "movement-number"
- "mpaa"
- "mt-movies"
- "mx-movies"
- "my-movies"
- "network-name"
- "ni-movies"
- "nl-movies"
- "no-movies"
- "numberWithFloat:"
- "nz-oflc"
- "pa-movies"
- "pageProgressionDirection"
- "pe-movies"
- "ph-movies"
- "pl-movies"
- "playlistArtistName"
- "pluspub"
- "podcast-feed-url"
- "podcast-type"
- "preOrderIdentifier"
- "preferredAssetFlavor"
- "preorder-id"
- "primaryAssetDictionary"
- "pt-movies"
- "pub"
- "py-movies"
- "rating"
- "ratingSystemFromString:"
- "redownload-params"
- "redownloadDownload"
- "release-date"
- "releaseDateString"
- "rental-id"
- "requestPersistentID"
- "requiredDeviceCapabilities"
- "riaa"
- "ro-movies"
- "ru-movies"
- "sagaId"
- "scale"
- "se-movies"
- "season-number"
- "setAppleID:"
- "setArtistIdentifier:"
- "setBetaExternalVersionIdentifier:"
- "setCloudIdentifier:"
- "setCollectionIdentifier:"
- "setCollectionIndexInCollectionGroup:"
- "setCollectionName:"
- "setCompilation:"
- "setComposerIdentifier:"
- "setComposerName:"
- "setContentRating:"
- "setCopyright:"
- "setDateFormat:"
- "setDeviceBasedVPP:"
- "setDictionary:"
- "setEpisodeIdentifier:"
- "setEpisodeSortIdentifier:"
- "setEpubRightsData:"
- "setExplicitContent:"
- "setFullSizeImageURL:"
- "setGenreIdentifier:"
- "setHighDefinition:"
- "setHlsPlaylistURL:"
- "setImageKind:"
- "setImageKindWithTypeName:variantName:"
- "setIndexInCollection:"
- "setItemIdentifier:"
- "setKeyStyle:"
- "setLaunchExtrasUrl:"
- "setLenient:"
- "setLongDescription:"
- "setLongSeasonDescription:"
- "setMD5HashStrings:numberOfBytesToHash:"
- "setMusicShow:"
- "setNetworkName:"
- "setNumberOfCollectionsInCollectionGroup:"
- "setNumberOfItemsInCollection:"
- "setPageProgressionDirection:"
- "setPodcastEpisodeGUID:"
- "setPodcastFeedURL:"
- "setPodcastType:"
- "setPreOrderIdentifier:"
- "setPrimaryAssetURL:"
- "setRank:"
- "setRatingDescription:"
- "setRatingLabel:"
- "setRatingSystem:"
- "setRedownloadActionParameters:"
- "setRedownloadDownload:"
- "setReleaseDate:"
- "setReleaseDateString:"
- "setReleaseYear:"
- "setRental:"
- "setRentalID:"
- "setRequestPersistentID:"
- "setRequiredDeviceCapabilities:"
- "setSeasonNumber:"
- "setSeriesName:"
- "setSharedResource:"
- "setShortDescription:"
- "setShouldDownloadAutomatically:"
- "setSortArtistName:"
- "setSortCollectionName:"
- "setThumbnailNewsstandBindingEdge:"
- "setThumbnailNewsstandBindingType:"
- "setTimeZone:"
- "setURL:"
- "setValue:forKey:"
- "setVariantIdentifier:"
- "setVideoDetailsDictionary:"
- "setViewStoreItemURL:"
- "sg-movies"
- "sgGuid"
- "shouldDownloadAutomatically"
- "show-composer"
- "show-name"
- "si-movies"
- "sk-movies"
- "softwareIcon57x57URL"
- "softwareVersionBundleId"
- "sortArtistName"
- "sortCollectionName"
- "sortTitle"
- "sortedArrayUsingFunction:context:"
- "sr-movies"
- "stringByAppendingFormat:"
- "stringFromDate:"
- "substringToIndex:"
- "sv-movies"
- "system"
- "th-movies"
- "thumbnail-newsstand-binding-edge"
- "thumbnail-newsstand-binding-type"
- "thumbnail-url"
- "thumbnailImageCollection"
- "timeZoneForSecondsFromGMT:"
- "tj-movies"
- "tr-movies"
- "track-count"
- "track-number"
- "trackCount"
- "trackNumber"
- "tw-movies"
- "ua-movies"
- "uk-tv"
- "unmodified-title"
- "us-cable"
- "us-tv"
- "uy-movies"
- "uz-movies"
- "variantId"
- "variantIdentifier"
- "ve-movies"
- "videoDetails"
- "vn-movies"
- "width"
- "work"
- "year"
- "yyyy-MM-dd'T'HH:mm:ss'Z'"
- "{CGSize=dd}16@0:8"

```
