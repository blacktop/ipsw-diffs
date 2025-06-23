## ScreenshotServices

> `/System/Library/PrivateFrameworks/ScreenshotServices.framework/ScreenshotServices`

```diff

-400.1.100.0.0
-  __TEXT.__text: 0x1ba4c
+404.0.0.0.0
+  __TEXT.__text: 0x1bcdc
   __TEXT.__auth_stubs: 0x910
-  __TEXT.__objc_methlist: 0x23e4
+  __TEXT.__objc_methlist: 0x23ec
   __TEXT.__const: 0x158
-  __TEXT.__cstring: 0x1b54
+  __TEXT.__cstring: 0x1b78
   __TEXT.__oslogstring: 0xf7f
   __TEXT.__gcc_except_tab: 0x39c
   __TEXT.__dlopen_cstrs: 0x4ae
-  __TEXT.__unwind_info: 0xa60
+  __TEXT.__unwind_info: 0xa70
   __TEXT.__objc_classname: 0x81e
-  __TEXT.__objc_methname: 0x60ad
+  __TEXT.__objc_methname: 0x613c
   __TEXT.__objc_methtype: 0xf4f
-  __TEXT.__objc_stubs: 0x5600
-  __DATA_CONST.__got: 0x678
-  __DATA_CONST.__const: 0xa58
+  __TEXT.__objc_stubs: 0x56e0
+  __DATA_CONST.__got: 0x6a8
+  __DATA_CONST.__const: 0xa78
   __DATA_CONST.__objc_classlist: 0x1e0
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1a40
+  __DATA_CONST.__objc_selrefs: 0x1a80
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0xe8
   __DATA_CONST.__objc_arraydata: 0x38
   __AUTH_CONST.__auth_got: 0x498
-  __AUTH_CONST.__const: 0x6c0
-  __AUTH_CONST.__cfstring: 0x19e0
-  __AUTH_CONST.__objc_const: 0x48c0
+  __AUTH_CONST.__const: 0x6e0
+  __AUTH_CONST.__cfstring: 0x1a40
+  __AUTH_CONST.__objc_const: 0x48d0
   __AUTH_CONST.__objc_doubleobj: 0x40
   __AUTH_CONST.__objc_intobj: 0x108
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x730
   __DATA.__objc_ivar: 0x238
   __DATA.__data: 0x6e0
-  __DATA.__bss: 0x120
+  __DATA.__bss: 0x130
   __DATA_DIRTY.__objc_data: 0xb90
   __DATA_DIRTY.__bss: 0xb8
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9E00B085-08B9-3EC9-83A7-082DD359F3F3
-  Functions: 901
-  Symbols:   3666
-  CStrings:  1879
+  UUID: C94BA907-D418-3F0A-B749-0AEAEBE8EB7F
+  Functions: 904
+  Symbols:   3688
+  CStrings:  1894
 
Symbols:
+ +[UIImage(SSImageSurface) ss_imageProperties].cold.1
+ -[SSScreenCapturerPresentationOptions effectivePresentationMode]
+ _NSCalendarIdentifierGregorian
+ _OBJC_CLASS_$_NSCalendar
+ _OBJC_CLASS_$_NSDateFormatter
+ _OBJC_CLASS_$_NSLocale
+ ___45+[UIImage(SSImageSurface) ss_imageProperties]_block_invoke
+ _kCGImagePropertyExifDateTimeOriginal
+ _kCGImagePropertyTIFFDateTime
+ _objc_msgSend$addEntriesFromDictionary:
+ _objc_msgSend$dictionary
+ _objc_msgSend$effectivePresentationMode
+ _objc_msgSend$initWithCalendarIdentifier:
+ _objc_msgSend$localeWithLocaleIdentifier:
+ _objc_msgSend$setCalendar:
+ _objc_msgSend$setDateFormat:
+ _objc_msgSend$setLocale:
+ _objc_msgSend$stringFromDate:
+ _ss_imageProperties.exifDateTimeFormatter
+ _ss_imageProperties.onceToken
- _objc_msgSend$_initWithIOSurface:scale:orientation:
- _objc_msgSend$hasRemoteViewController
Functions:
~ -[SSScreenCapturerPresentationOptions description] : 220 -> 200
+ -[SSScreenCapturerPresentationOptions effectivePresentationMode]
~ +[UIImage(SSImageSurface) ss_imageProperties] : 420 -> 736
+ ___45+[UIImage(SSImageSurface) ss_imageProperties]_block_invoke
~ -[SSScreenCapturer _takeScreenshotWithOptionsCollection:serviceOptions:presentationOptions:appleInternalOptions:] : 2044 -> 1984
~ -[SSOtherScreenSnapshotter takeScreenshot] : 512 -> 536
~ ___42-[SSOtherScreenSnapshotter takeScreenshot]_block_invoke : 8 -> 140
+ +[UIImage(SSImageSurface) ss_imageProperties].cold.1
CStrings:
+ "Automatic"
+ "TQ,R,N"
+ "addEntriesFromDictionary:"
+ "dictionary"
+ "effectivePresentationMode"
+ "en_US"
+ "initWithCalendarIdentifier:"
+ "localeWithLocaleIdentifier:"
+ "setCalendar:"
+ "setDateFormat:"
+ "setLocale:"
+ "stringFromDate:"
+ "yyyy:MM:dd HH:mm:ss"
- "_initWithIOSurface:scale:orientation:"

```
