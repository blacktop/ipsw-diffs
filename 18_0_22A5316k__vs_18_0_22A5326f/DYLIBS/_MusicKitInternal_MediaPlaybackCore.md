## _MusicKitInternal_MediaPlaybackCore

> `/System/Library/PrivateFrameworks/_MusicKitInternal_MediaPlaybackCore.framework/_MusicKitInternal_MediaPlaybackCore`

```diff

-4024.100.70.0.0
-  __TEXT.__text: 0x101f8
-  __TEXT.__auth_stubs: 0xcf0
+4024.100.76.0.0
+  __TEXT.__text: 0x16210
+  __TEXT.__auth_stubs: 0xe60
   __TEXT.__objc_methlist: 0x2c
-  __TEXT.__const: 0x2ae
-  __TEXT.__swift5_typeref: 0x23e
+  __TEXT.__const: 0x3ce
+  __TEXT.__constg_swiftt: 0x108
+  __TEXT.__swift5_typeref: 0x32e
+  __TEXT.__swift5_builtin: 0x3c
+  __TEXT.__swift5_reflstr: 0x119
+  __TEXT.__swift5_assocty: 0x30
+  __TEXT.__swift5_proto: 0x14
+  __TEXT.__swift5_types: 0x1c
+  __TEXT.__swift5_mpenum: 0x8
+  __TEXT.__swift5_fieldmd: 0xd4
+  __TEXT.__swift5_capture: 0x18
+  __TEXT.__oslogstring: 0x314
   __TEXT.__cstring: 0x915
-  __TEXT.__oslogstring: 0x189
-  __TEXT.__swift5_reflstr: 0xa3
-  __TEXT.__swift5_assocty: 0x18
-  __TEXT.__constg_swiftt: 0x5c
-  __TEXT.__swift5_fieldmd: 0x50
-  __TEXT.__swift5_proto: 0x10
-  __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x290
-  __TEXT.__eh_frame: 0x268
+  __TEXT.__unwind_info: 0x488
+  __TEXT.__eh_frame: 0x7c8
   __TEXT.__objc_classname: 0x12
-  __TEXT.__objc_methname: 0x427
+  __TEXT.__objc_methname: 0x449
   __TEXT.__objc_methtype: 0xb
-  __DATA_CONST.__got: 0x430
-  __DATA_CONST.__const: 0xe8
+  __DATA_CONST.__got: 0x490
+  __DATA_CONST.__const: 0x128
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x168
-  __AUTH_CONST.__auth_got: 0x678
-  __AUTH_CONST.__auth_ptr: 0x200
-  __AUTH_CONST.__const: 0xb8
+  __DATA_CONST.__objc_selrefs: 0x180
+  __AUTH_CONST.__auth_got: 0x730
+  __AUTH_CONST.__auth_ptr: 0x270
+  __AUTH_CONST.__const: 0x2b0
   __AUTH_CONST.__objc_const: 0x88
   __AUTH.__objc_data: 0xb0
   __AUTH.__data: 0x28
-  __DATA.__data: 0x210
+  __DATA.__data: 0x208
   __DATA.__bss: 0x228
-  __DATA.__common: 0x18
+  __DATA.__common: 0x30
+  __DATA_DIRTY.__data: 0x90
+  __DATA_DIRTY.__bss: 0x80
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/Intents.framework/Intents
   - /System/Library/Frameworks/MediaPlayer.framework/MediaPlayer
   - /System/Library/Frameworks/MusicKit.framework/MusicKit
   - /System/Library/PrivateFrameworks/MediaPlaybackCore.framework/MediaPlaybackCore

   - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 268
-  Symbols:   215
-  CStrings:  271
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 456
+  Symbols:   332
+  CStrings:  0
 
Symbols:
+ _OBJC_CLASS_$_INPlayMediaIntent
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
+ _objc_release_x9
+ _swift_deallocObject
+ _swift_getForeignTypeMetadata
+ _swift_isClassType
+ _swift_task_alloc
+ _swift_task_dealloc
+ _swift_task_switch
CStrings:
- "\x04\x06E"
- "\x06E"
- "\b\x01\x06E"
- "\b\x06\x06E"
- "\b\v\x06E"
- "\b2oD"
- "\b{\x80D"
- "\b\x92ZD"
- "\b\x95\xf5D"
- "\t\x06E"
- "\x0e\x06E"
- "\x10\x03\x06E"
- "\x10\b\x06E"
- "\x10\r\x06E"
- "\x104oD"
- "\x10}\x80D"
- "\x10\x94ZD"
- "\x10\xfe\x05E"
- "\x18"
- "\x18\x05\x06E"
- "\x18\n\x06E"
- "\x18\n\fE"
- "\x181oD"
- "\x186oD"
- "\x18z\x80D"
- "\x18\x7f\x80D"
- "\x18\x94\xf5D"
- " \x02\x06E"
- " \a\x06E"
- " \f\x06E"
- " 3oD"
- " yjD"
- " |\x80D"
- " \x93ZD"
- " \x96\xf5D"
- "(\x04\x06E"
- "(\t\x06E"
- "(\x0e\x06E"
- "(5oD"
- "(y\x80D"
- "(~\x80D"
- "(\xff\x05E"
- "0\x01\x06E"
- "0\x06\x06E"
- "0\v\x06E"
- "02oD"
- "0{\x80D"
- "0\x92ZD"
- "0\x95\xf5D"
- "5oD"
- "8\x03\x06E"
- "8\b\x06E"
- "8\r\x06E"
- "84oD"
- "8}\x80D"
- "8\x94ZD"
- "8\xfe\x05E"
- "@"
- "@\x05\x06E"
- "@\n\x06E"
- "@6oD"
- "@z\x80D"
- "@\x7f\x80D"
- "@\x94\xf5D"
- "@\xa3\x86D"
- "H\x02\x06E"
- "H\a\x06E"
- "H\f\x06E"
- "H3oD"
- "HxjD\x01\xc0\xe1jPxjD\x01\xc0\xab\xb5\xc0xjD\x01\xc0\xe1j\xc8xjD\x01\xc0\xab\xb5\xe8xjD\x01\xc0\xe1j8yjD\x01\xc0\xe1j@yjD\x01\xc0\xab\xb5\x88yjD\x01\xc0\xe1j(xjD\x01\xc0\xab\xb5xxjD\x01\xc0\xab\xb5\x18yjD\x01\xc0\xab\xb5\xa0\x93\xf5D"
- "HyjD"
- "H|\x80D"
- "H\x93ZD"
- "H\x96\xf5D"
- "H\xfd\x05E"
- "P\x04\x06E"
- "P\t\x06E"
- "P\x0e\x06E"
- "P5oD"
- "Py\x80D"
- "P~\x80D"
- "P\xff\x05E"
- "X\x01\x06E"
- "X\x06\x06E"
- "X\v\x06E"
- "X2oD"
- "XxjD"
- "X{\x80D"
- "X\x92ZD"
- "X\x95\xf5D"
- "`\x03\x06E"
- "`\b\x06E"
- "`\v\fE\x01\xc0\xe1jh\v\fE\x01\xc0\xab\xb5P\f\fE\x01\xc0\xe1jX\f\fE\x01\xc0\xab\xb5\xc0{\x80D\x01\xc0\xe1j\xc8{\x80D\x01\xc0\xab\xb5\xe8{\x80D\x01\xc0\xe1j\xf0{\x80D\x01\xc0\xab\xb5\x10|\x80D\x01\xc0\xe1j\x18|\x80D\x01\xc0\xab\xb58|\x80D\x01\xc0\xe1j@|\x80D\x01\xc0\xab\xb5`|\x80D\x01\xc0\xe1j\x88|\x80D\x01\xc0\xe1j\x90|\x80D\x01\xc0\xab\xb5\xb0|\x80D\x01\xc0\xe1j\xb8|\x80D\x01\xc0\xab\xb5\xd8|\x80D\x01\xc0\xe1j\xe0|\x80D\x01\xc0\xab\xb5"
- "`\f\fE"
- "`\r\x06E"
- "`4oD"
- "`}\x80D"
- "`\x94ZD"
- "`\xfe\x05E"
- "e\x14E\x01\xc0\xab\xb5xe\x14E\x01\xc0\xab\xb5\xc8e\x14E\x01\xc0\xab\xb5\x18f\x14E\x01\xc0\xab\xb5hf\x14E\x01\xc0\xab\xb5\xb8f\x14E\x01\xc0\xab\xb5\xe0f\x14E\x01\xc0\xab\xb5Xg\x14E\x01\xc0\xab\xb5\xa8g\x14E\x01\xc0\xab\xb5\xf8g\x14E\x01\xc0\xab\xb5\x98؉D\x01\xc0\xab\xb5\xc0؉D\x01\xc0\xab\xb5\x10ىD\x01\xc0\xab\xb58ىD\x01\xc0\xab\xb5\xb0ىD\x01\xc0\xab\xb5\xd8ىD\x01\xc0\xab\xb5@ۉD\x01\xc0\xab\xb5\x90ۉD\x01\xc0\xab\xb5\x80܉D\x01\xc0\xab\xb5\xe8݉D\x01\xc0\xab\xb5\b\x8eGG\x01\xa0"
- "h"
- "h\x05\x06E"
- "h\n\x06E"
- "h1oD"
- "h6oD"
- "hz\x80D"
- "h\x7f\x80D"
- "h\x94\xf5D"
- "p\x02\x06E"
- "p\a\x06E"
- "p\v\fE"
- "p\f\x06E"
- "p3oD"
- "pyjD"
- "p|\x80D"
- "p\x93ZD"
- "p\x96\xf5D"
- "p\xfd\x05E"
- "x\x04\x06E"
- "x\t\x06E"
- "x\x0e\x06E"
- "x5oD"
- "xy\x80D"
- "x~\x80D"
- "x\xff\x05E"
- "y\x80D"
- "{\x80D\x01\xc0\xab\xb5P{\x80D\x01\xc0\xab\xb5\xa0{\x80D\x01\xc0\xab\xb5\xc0~\x80D\x01\xc0\xab\xb5`\x7f\x80D\x01\xc0\xab\xb5\x88\x7f\x80D\x01\xc0\xab\xb5 \xfd\x05E"
- "}\x80D\x01\xc0\xe1j\b}\x80D\x01\xc0\xab\xb5(}\x80D\x01\xc0\xe1jP}\x80D\x01\xc0\xe1jX}\x80D\x01\xc0\xab\xb5x}\x80D\x01\xc0\xe1j\x80}\x80D\x01\xc0\xab\xb5\xa0}\x80D\x01\xc0\xe1j\xa8}\x80D\x01\xc0\xab\xb5\xc8}\x80D\x01\xc0\xe1j\xd0}\x80D\x01\xc0\xab\xb5\xf0}\x80D\x01\xc0\xe1j\xf8}\x80D\x01\xc0\xab\xb5\x18~\x80D\x01\xc0\xe1j@~\x80D\x01\xc0\xe1jH~\x80D\x01\xc0\xab\xb5h~\x80D\x01\xc0\xe1j\x90~\x80D\x01\xc0\xe1j\x98~\x80D\x01\xc0\xab\xb5\xe0~\x80D\x01\xc0\xe1j\xe8~\x80D\x01\xc0\xab\xb50\x7f\x80D\x01\xc0\xe1j\xa8\x7f\x80D\x01\xc0\xe1j\xb0\x7f\x80D\x01\xc0\xab\xb5\xd0\x7f\x80D\x01\xc0\xe1j\xd8\x7f\x80D\x01\xc0\xab\xb5\xc0\b\fE\x01\xc0\xab\xb5\x98\t\fE\x01\xc0\xab\xb5\xd0x\x80D\x01\xc0\xab\xb5\xf8x\x80D\x01\xc0\xab\xb5 y\x80D\x01\xc0\xab\xb5Hy\x80D\x01\xc0\xab\xb5\x98y\x80D\x01\xc0\xab\xb5\xc0y\x80D\x01\xc0\xab\xb5\xe8y\x80D\x01\xc0\xab\xb5\x10z\x80D\x01\xc0\xab\xb5`z\x80D\x01\xc0\xab\xb5\x88z\x80D\x01\xc0\xab\xb5\xb0z\x80D\x01\xc0\xab\xb5\xd8z\x80D\x01\xc0\xab\xb5"
- "~\x80D"
- "\x80\x01\x06E"
- "\x80\x06\x06E"
- "\x80\v\x06E"
- "\x802oD"
- "\x80xjD"
- "\x80{\x80D"
- "\x80\x92ZD"
- "\x80\x95\xf5D"
- "\x88\x03\x06E"
- "\x88\b\x06E"
- "\x88\f\fE"
- "\x88\r\x06E"
- "\x884oD"
- "\x88}\x80D"
- "\x88\x94ZD"
- "\x88\xfe\x05E"
- "\x90"
- "\x90\x05\x06E"
- "\x90\n\x06E"
- "\x90\n\fE"
- "\x901oD"
- "\x906oD"
- "\x90z\x80D"
- "\x90\x7f\x80D"
- "\x90\x94\xf5D"
- "\x94ZD\x01\xc0\xe1j\b\x94ZD\x01\xc0\xab\xb5(\x94ZD\x01\xc0\xe1jP\x94ZD\x01\xc0\xe1jx\x94ZD\x01\xc0\xe1j\x80\x94ZD\x01\xc0\xab\xb5\xa0\x94ZD\x01\xc0\xe1j\xa8\x94ZD\x01\xc0\xab\xb5ȔZD\x01\xc0\xe1jДZD\x01\xc0\xab\xb5\xf0\x94ZD\x01\xc0\xe1j\xf8\x94ZD\x01\xc0\xab\xb58\x94\xf5D\x01\xc0\xab\xb5\x88\x94\xf5D\x01\xc0\xab\xb5(\x95\xf5D\x01\xc0\xab\xb5x\x95\xf5D\x01\xc0\xab\xb5ȕ\xf5D\x01\xc0\xab\xb5\x18\x96\xf5D\x01\xc0\xab\xb5h\x96\xf5D\x01\xc0\xab\xb5\xb0\x91ZD\x01\xc0\xab\xb5ؑZD\x01\xc0\xab\xb5"
- "\x95ZD"
- "\x98\x02\x06E"
- "\x98\a\x06E"
- "\x98\f\x06E"
- "\x983oD"
- "\x98yjD"
- "\x98|\x80D"
- "\x98\x93ZD"
- "\x98\x96\xf5D"
- "\x98\xfd\x05E"
- "\xa0\x04\x06E"
- "\xa0\t\x06E"
- "\xa0\t\fE"
- "\xa0\v\fE"
- "\xa0\x0e\x06E"
- "\xa00oD"
- "\xa05oD"
- "\xa0y\x80D"
- "\xa0~\x80D"
- "\xa0\xff\x05E"
- "\xa8\x01\x06E"
- "\xa8\x06\x06E"
- "\xa8\v\x06E"
- "\xa82oD"
- "\xa8xjD"
- "\xa8{\x80D"
- "\xa8\x92ZD"
- "\xa8\x95\xf5D"
- "\xb0\x03\x06E"
- "\xb0\b\x06E"
- "\xb0\r\x06E"
- "\xb04oD"
- "\xb0Z\x14E\x01\xc0\xab\xb5\xd8Z\x14E\x01\xc0\xab\xb5([\x14E\x01\xc0\xab\xb5x[\x14E\x01\xc0\xab\xb5\x18\\\x14E\x01\xc0\xab\xb5h\\\x14E\x01\xc0\xab\xb5\xb8\\\x14E\x01\xc0\xab\xb5\b]\x14E\x01\xc0\xab\xb5X]\x14E\x01\xc0\xab\xb5\xa8]\x14E\x01\xc0\xab\xb5\xf8]\x14E\x01\xc0\xab\xb5\x98^\x14E\x01\xc0\xab\xb5\xc0^\x14E\x01\xc0\xab\xb5\xe8^\x14E\x01\xc0\xab\xb5\x88_\x14E\x01\xc0\xab\xb5(`\x14E\x01\xc0\xab\xb5x`\x14E\x01\xc0\xab\xb5\xc8`\x14E\x01\xc0\xab\xb5\x18a\x14E\x01\xc0\xab\xb5ha\x14E\x01\xc0\xab\xb5\xb8a\x14E\x01\xc0\xab\xb5\bb\x14E\x01\xc0\xab\xb5Xb\x14E\x01\xc0\xab\xb5\xa8b\x14E\x01\xc0\xab\xb5 c\x14E\x01\xc0\xab\xb5\x98c\x14E\x01\xc0\xab\xb5\xc0c\x14E\x01\xc0\xab\xb5\x88d\x14E\x01\xc0\xab\xb5\xd8d\x14E\x01\xc0\xab\xb5"
- "\xb0}\x80D"
- "\xb0\x94ZD"
- "\xb0\xfe\x05E"
- "\xb8"
- "\xb8\x05\x06E"
- "\xb8\n\x06E"
- "\xb81oD"
- "\xb86oD"
- "\xb8z\x80D"
- "\xb8\x7f\x80D"
- "\xb8\x91ZD"
- "\xb8\x93\xf5D\x01\xc0\xe1j\b\x94\xf5D\x01\xc0\xe1jX\x94\xf5D\x01\xc0\xe1j`\x94\xf5D\x01\xc0\xab\xb5\xa8\x94\xf5D\x01\xc0\xe1j\xb0\x94\xf5D\x01\xc0\xab\xb5\xf8\x94\xf5D\x01\xc0\xe1jH\x95\xf5D\x01\xc0\xe1jP\x95\xf5D\x01\xc0\xab\xb5\x98\x95\xf5D\x01\xc0\xe1j\xa0\x95\xf5D\x01\xc0\xab\xb5\xe8\x95\xf5D\x01\xc0\xe1j\xf0\x95\xf5D\x01\xc0\xab\xb58\x96\xf5D\x01\xc0\xe1j@\x96\xf5D\x01\xc0\xab\xb5\x88\x96\xf5D\x01\xc0\xe1j\x90\x96\xf5D\x01\xc0\xab\xb5H\x92ZD\x01\xc0\xe1jP\x92ZD\x01\xc0\xab\xb5p\x92ZD\x01\xc0\xe1jx\x92ZD\x01\xc0\xab\xb5\x98\x92ZD\x01\xc0\xe1j\xa0\x92ZD\x01\xc0\xab\xb5\xc0\x92ZD\x01\xc0\xe1jȒZD\x01\xc0\xab\xb5"
- "\xb8\x94\xf5D"
- "\xc0\x02\x06E"
- "\xc0\a\x06E"
- "\xc0\f\x06E"
- "\xc03oD"
- "\xc0|\x80D"
- "\xc0\x93ZD"
- "\xc0\xfd\x05E"
- "\xc8\x04\x06E"
- "\xc8\b\fE"
- "\xc8\t\x06E"
- "\xc8\f\fE"
- "\xc8\x0e\x06E"
- "\xc80oD"
- "\xc85oD"
- "\xc8y\x80D"
- "\xc8~\x80D"
- "ȓ\xf5D"
- "\xc8\xff\x05E"
- "\xd0\x01\x06E"
- "\xd0\x06\x06E"
- "\xd0\n\fE"
- "\xd0\v\x06E"
- "\xd02oD"
- "\xd0xjD"
- "\xd0{\x80D"
- "ВZD"
- "Е\xf5D"
- "\xd8\x03\x06E"
- "\xd8\b\x06E"
- "\xd8\t\fE"
- "\xd8\r\x06E"
- "\xd84oD"
- "\xd8x\x80D"
- "\xd8}\x80D"
- "ؔZD"
- "\xd8\xfe\x05E"
- "\xe0"
- "\xe0\x05\x06E"
- "\xe0\n\x06E"
- "\xe0\v\fE"
- "\xe01oD"
- "\xe0z\x80D"
- "\xe0\x7f\x80D"
- "\xe0\x91ZD"
- "\xe0\x94\xf5D"
- "\xe8\x02\x06E"
- "\xe8\a\x06E"
- "\xe8\f\x06E"
- "\xe83oD"
- "\xe8|\x80D"
- "\xe8\x93ZD"
- "\xe8\xfd\x05E"
- "\xf0\x04\x06E"
- "\xf0\t\x06E"
- "\xf00oD"
- "\xf05oD"
- "\xf0y\x80D"
- "\xf0~\x80D"
- "\xf0\x93\xf5D"
- "\xf0\xff\x05E"
- "\xf8\x01\x06E"
- "\xf8\x06\x06E"
- "\xf8\v\x06E"
- "\xf82oD"
- "\xf8xjD"
- "\xf8{\x80D"
- "\xf8\x92ZD"
- "\xf8\x95\xf5D"
- "\xfeD\x01\xc0\xab\xb5X_\xfeD\x01\xc0\xe1j`_\xfeD\x01\xc0\xab\xb5\x80_\xfeD\x01\xc0\xe1j\xd0_\xfeD\x01\xc0\xe1jH`\xfeD\x01\xc0\xe1j\x98`\xfeD\x01\xc0\xe1j\xe8`\xfeD\x01\xc0\xe1j8a\xfeD\x01\xc0\xe1j`a\xfeD\x01\xc0\xe1j\xd8a\xfeD\x01\xc0\xe1j(b\xfeD\x01\xc0\xe1jxb\xfeD\x01\xc0\xe1j\xc8b\xfeD\x01\xc0\xe1j\xf0b\xfeD\x01\xc0\xe1jhc\xfeD\x01\xc0\xe1j\b\xa3\x86D\x01\xc0\xe1j0\xa3\x86D\x01\xc0\xe1j8\xa3\x86D\x01\xc0\xab\xb5\xe8^\xfeD\x01\xc0\xab\xb58_\xfeD\x01\xc0\xab\xb5袆D\x01\xc0\xab\xb50xjD"
- "\xff\x05E"

```
