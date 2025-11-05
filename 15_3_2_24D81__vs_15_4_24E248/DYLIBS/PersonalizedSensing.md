## PersonalizedSensing

> `/System/Library/PrivateFrameworks/PersonalizedSensing.framework/Versions/A/PersonalizedSensing`

```diff

-205.0.1.0.0
-  __TEXT.__text: 0xa13c
+206.0.7.0.0
+  __TEXT.__text: 0xa328
   __TEXT.__auth_stubs: 0x330
-  __TEXT.__objc_methlist: 0xf9c
+  __TEXT.__objc_methlist: 0x101c
   __TEXT.__const: 0xd0
-  __TEXT.__cstring: 0xc04
+  __TEXT.__cstring: 0xc28
   __TEXT.__oslogstring: 0x51a
   __TEXT.__gcc_except_tab: 0x1ac
-  __TEXT.__unwind_info: 0x3f0
+  __TEXT.__unwind_info: 0x400
   __TEXT.__objc_classname: 0x220
-  __TEXT.__objc_methname: 0x21b4
+  __TEXT.__objc_methname: 0x2218
   __TEXT.__objc_methtype: 0x25e
-  __TEXT.__objc_stubs: 0x1d40
+  __TEXT.__objc_stubs: 0x1dc0
   __DATA_CONST.__got: 0x160
   __DATA_CONST.__const: 0x120
   __DATA_CONST.__objc_classlist: 0xa0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x978
+  __DATA_CONST.__objc_selrefs: 0x998
   __DATA_CONST.__objc_superrefs: 0x88
   __DATA_CONST.__objc_arraydata: 0x10
   __AUTH_CONST.__auth_got: 0x1b0
   __AUTH_CONST.__const: 0x260
-  __AUTH_CONST.__cfstring: 0xf80
-  __AUTH_CONST.__objc_const: 0x1c68
+  __AUTH_CONST.__cfstring: 0xfc0
+  __AUTH_CONST.__objc_const: 0x1c50
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x640
-  __DATA.__objc_ivar: 0x104
+  __DATA.__objc_ivar: 0x10c
   __DATA.__data: 0x1b0
   __DATA.__bss: 0x60
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libperfcheck.dylib
-  UUID: 1D31C16D-B575-352A-B9BE-57797BACC020
-  Functions: 361
-  Symbols:   1007
-  CStrings:  801
+  UUID: A13A11E6-AEBA-3B34-9778-D6F2807052D8
+  Functions: 371
+  Symbols:   1023
+  CStrings:  813
 
Symbols:
+ +[MOPerformanceMeasurement isEnabled].cold.1
+ +[NSDate(MOExtensions) dateFormatter].cold.1
+ +[NSDate(MOExtensions) dayNameFormatterInEnglish].cold.1
+ +[NSDate(MOExtensions) monthDayFormatter].cold.1
+ +[NSDate(MOExtensions) relativeBundleDateFormatter].cold.1
+ -[MOContextMusicMetaData artist]
+ -[MOContextMusicMetaData setArtist:]
+ -[MOContextMusicMetaData setTitle:]
+ -[MOContextMusicMetaData title]
+ -[MOPersonalizedSensingServiceManager _fetchPersonalizedSyncContextWithOptions:withReply:].cold.1
+ OBJC_IVAR_$_MOContextMusicMetaData._artist
+ OBJC_IVAR_$_MOContextMusicMetaData._title
+ _objc_msgSend$artist
+ _objc_msgSend$setArtist:
+ _objc_msgSend$setTitle:
+ _objc_msgSend$title
CStrings:
+ "T@\"NSString\",&,N,V_artist"
+ "T@\"NSString\",&,N,V_title"
+ "_artist"
+ "_title"
+ "artist"
+ "music string, %@, artist, %@, title, %@"
+ "setArtist:"
+ "setTitle:"
+ "title"
- "music string, %@"

```
