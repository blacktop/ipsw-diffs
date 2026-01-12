## PosterBoardServices

> `/System/Library/PrivateFrameworks/PosterBoardServices.framework/PosterBoardServices`

```diff

-304.3.3.0.0
-  __TEXT.__text: 0x4be20
-  __TEXT.__auth_stubs: 0xaf0
+304.3.4.1.0
+  __TEXT.__text: 0x4c664
+  __TEXT.__auth_stubs: 0xae0
   __TEXT.__objc_methlist: 0x3c94
   __TEXT.__const: 0x140
-  __TEXT.__cstring: 0x4944
-  __TEXT.__gcc_except_tab: 0x90c
-  __TEXT.__oslogstring: 0x2867
-  __TEXT.__dlopen_cstrs: 0x244
-  __TEXT.__unwind_info: 0x1080
+  __TEXT.__cstring: 0x4a2e
+  __TEXT.__gcc_except_tab: 0x958
+  __TEXT.__oslogstring: 0x2759
+  __TEXT.__dlopen_cstrs: 0x2a6
+  __TEXT.__unwind_info: 0x10c0
   __TEXT.__objc_classname: 0x89a
-  __TEXT.__objc_methname: 0xa945
+  __TEXT.__objc_methname: 0xa970
   __TEXT.__objc_methtype: 0x1c38
-  __TEXT.__objc_stubs: 0x6200
-  __DATA_CONST.__got: 0x488
-  __DATA_CONST.__const: 0x1218
+  __TEXT.__objc_stubs: 0x6220
+  __DATA_CONST.__got: 0x480
+  __DATA_CONST.__const: 0x1230
   __DATA_CONST.__objc_classlist: 0x220
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1f68
+  __DATA_CONST.__objc_selrefs: 0x1f70
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x1f8
-  __AUTH_CONST.__auth_got: 0x588
+  __AUTH_CONST.__auth_got: 0x580
   __AUTH_CONST.__const: 0x4c0
   __AUTH_CONST.__cfstring: 0x37a0
   __AUTH_CONST.__objc_const: 0xc2e8

   __AUTH.__objc_data: 0xb40
   __DATA.__objc_ivar: 0x430
   __DATA.__data: 0x5c0
-  __DATA.__bss: 0x98
+  __DATA.__bss: 0xb0
   __DATA_DIRTY.__objc_data: 0xa00
-  __DATA_DIRTY.__bss: 0x88
+  __DATA_DIRTY.__bss: 0x90
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
   - /System/Library/PrivateFrameworks/PosterFoundation.framework/PosterFoundation
   - /System/Library/PrivateFrameworks/PosterFuturesKit.framework/PosterFuturesKit
-  - /System/Library/PrivateFrameworks/PosterUIFoundation.framework/PosterUIFoundation
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8382078E-5578-356A-9643-D299C28F8EA7
-  Functions: 1734
-  Symbols:   6150
-  CStrings:  2963
+  UUID: 484F8322-217A-3E53-B48D-24C467372A2E
+  Functions: 1744
+  Symbols:   6177
+  CStrings:  2968
 
Symbols:
+ GCC_except_table11
+ GCC_except_table25
+ GCC_except_table26
+ _OBJC_CLASS_$_PFPosterExtensionProvider
+ ___getPUIIOSurfaceFromCGImageSymbolLoc_block_invoke
+ ___getPUIImageEncoderErrorDomainSymbolLoc_block_invoke
+ ___getPUIImageOnDiskFormatClass_block_invoke
+ ___getPUIImageOnDiskFormatClass_block_invoke.cold.1
+ _getPUIIOSurfaceFromCGImageSymbolLoc.ptr
+ _getPUIImageEncoderErrorDomain
+ _getPUIImageEncoderErrorDomain.cold.1
+ _getPUIImageEncoderErrorDomainSymbolLoc.ptr
+ _getPUIImageOnDiskFormatClass.softClass
+ _objc_msgSend$newBundleIdentifierForOldBundleIdentifier:
+ _soft_PUIIOSurfaceFromCGImage
+ _soft_PUIIOSurfaceFromCGImage.cold.1
- +[PRSPosterConfiguration decodeFromPersistableRepresentation:expectedContainerIdentifier:error:].cold.3
- _OBJC_CLASS_$_PUIImageOnDiskFormat
- _PUIIOSurfaceFromCGImage
- _PUIImageEncoderErrorDomain
CStrings:
+ "Class getPUIImageOnDiskFormatClass(void)_block_invoke"
+ "IOSurface *soft_PUIIOSurfaceFromCGImage(CGImageRef, BOOL)"
+ "NSErrorDomain getPUIImageEncoderErrorDomain(void)"
+ "PUIIOSurfaceFromCGImage"
+ "PUIImageEncoderErrorDomain"
+ "PUIImageOnDiskFormat"
+ "[decodeFromPersistableRepresentation] Migrating extension bundle ID from %{public}@ to %{public}@"
+ "[decodeFromPersistableRepresentation] migratedContainerURL is not a valid file system location: %@"
+ "newBundleIdentifierForOldBundleIdentifier:"
- "[decodeFromPersistableRepresentation] container UUID was wrong length; checking if this configuration's file system URL is reachable..."
- "[decodeFromPersistableRepresentation] fixedContainerURL is not a valid file system location: %@"
- "[decodeFromPersistableRepresentation] unable to find container uuid; checking if this is a valid file system location..."
- "[decodeFromPersistableRepresentation] unable to find container uuid; this is not a valid file system location: %@"

```
