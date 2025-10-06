## SpringBoard

> `/System/Library/DataClassMigrators/SpringBoard.migrator/SpringBoard`

```diff

-4416.11.7.0.0
-  __TEXT.__text: 0xbc88
+4416.25.105.0.0
+  __TEXT.__text: 0xbe34
   __TEXT.__auth_stubs: 0x5e0
-  __TEXT.__objc_stubs: 0x1820
+  __TEXT.__objc_stubs: 0x1860
   __TEXT.__objc_methlist: 0x4fc
-  __TEXT.__cstring: 0x12eb
-  __TEXT.__objc_methname: 0x1910
+  __TEXT.__cstring: 0x1351
+  __TEXT.__objc_methname: 0x192a
   __TEXT.__oslogstring: 0xe97
   __TEXT.__objc_classname: 0x125
   __TEXT.__objc_methtype: 0x329
   __TEXT.__const: 0x30
   __TEXT.__gcc_except_tab: 0xd0
-  __TEXT.__unwind_info: 0x220
+  __TEXT.__unwind_info: 0x228
   __DATA_CONST.__auth_got: 0x300
   __DATA_CONST.__got: 0xe8
-  __DATA_CONST.__const: 0xfd8
+  __DATA_CONST.__const: 0x1058
   __DATA_CONST.__cfstring: 0xc40
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_catlist: 0x8

   __DATA_CONST.__objc_arraydata: 0x80
   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA.__objc_const: 0xc20
-  __DATA.__objc_selrefs: 0x6d0
-  __DATA.__objc_classrefs: 0x170
+  __DATA.__objc_selrefs: 0x6e0
+  __DATA.__objc_classrefs: 0x178
   __DATA.__objc_superrefs: 0x38
   __DATA.__objc_ivar: 0x5c
   __DATA.__objc_data: 0x280
   __DATA.__data: 0x128
-  __DATA.__bss: 0x6f0
+  __DATA.__bss: 0x710
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
   - /System/Library/PrivateFrameworks/GraphicsServices.framework/GraphicsServices
   - /System/Library/PrivateFrameworks/IconServices.framework/IconServices
+  - /System/Library/PrivateFrameworks/PaperBoardUI.framework/PaperBoardUI
   - /System/Library/PrivateFrameworks/PosterBoardServices.framework/PosterBoardServices
   - /System/Library/PrivateFrameworks/SplashBoard.framework/SplashBoard
   - /System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: AF7AC227-54B2-3B59-9E96-D543031FC046
-  Functions: 359
-  Symbols:   326
-  CStrings:  702
+  UUID: 021C212C-0019-3610-99D5-1A83375C80B5
+  Functions: 364
+  Symbols:   329
+  CStrings:  707
 
Symbols:
+ _OBJC_CLASS_$_PBUIWallpaperConfigurationManager
+ _SBLogSystemActionCoaching
+ _SBLogSystemApertureOrientation
CStrings:
+ "SystemActionCoaching"
+ "SystemApertureOrientation"
+ "cleanup"
+ "dataStores"
+ "pointScale"
+ "v32@?0@\"<SBDataMigratorCleanuppableDataStore>\"8Q16^B24"
- "scale"

```
