## AppPredictionClient

> `/System/Library/PrivateFrameworks/AppPredictionClient.framework/AppPredictionClient`

```diff

-619.12.0.0.0
-  __TEXT.__text: 0x190108
+619.14.0.0.0
+  __TEXT.__text: 0x1903fc
   __TEXT.__auth_stubs: 0xf00
-  __TEXT.__objc_methlist: 0x18cf4
+  __TEXT.__objc_methlist: 0x18d3c
   __TEXT.__const: 0x6f8
-  __TEXT.__cstring: 0x1bba8
+  __TEXT.__cstring: 0x1bbe9
   __TEXT.__oslogstring: 0x17a08
   __TEXT.__gcc_except_tab: 0x232c
   __TEXT.__dlopen_cstrs: 0x42d
   __TEXT.__ustring: 0x18a
-  __TEXT.__unwind_info: 0x6720
+  __TEXT.__unwind_info: 0x6728
   __TEXT.__objc_classname: 0x3bce
-  __TEXT.__objc_methname: 0x346a4
-  __TEXT.__objc_methtype: 0x6782
-  __TEXT.__objc_stubs: 0x1cda0
+  __TEXT.__objc_methname: 0x3481a
+  __TEXT.__objc_methtype: 0x67b0
+  __TEXT.__objc_stubs: 0x1cdc0
   __DATA_CONST.__got: 0x1718
-  __DATA_CONST.__const: 0x6380
+  __DATA_CONST.__const: 0x63b8
   __DATA_CONST.__objc_classlist: 0xe40
   __DATA_CONST.__objc_catlist: 0x90
   __DATA_CONST.__objc_protolist: 0x268
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9fb8
+  __DATA_CONST.__objc_selrefs: 0x9fd0
   __DATA_CONST.__objc_protorefs: 0xb0
   __DATA_CONST.__objc_superrefs: 0xc48
   __DATA_CONST.__objc_arraydata: 0xaf8
   __AUTH_CONST.__auth_got: 0x790
   __AUTH_CONST.__const: 0x2a80
-  __AUTH_CONST.__cfstring: 0x15280
-  __AUTH_CONST.__objc_const: 0x45e68
+  __AUTH_CONST.__cfstring: 0x152e0
+  __AUTH_CONST.__objc_const: 0x45ed8
   __AUTH_CONST.__objc_intobj: 0xa20
   __AUTH_CONST.__objc_arrayobj: 0x6d8
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0x168
   __AUTH.__objc_data: 0x4330
-  __DATA.__objc_ivar: 0x1c6c
+  __DATA.__objc_ivar: 0x1c74
   __DATA.__data: 0x1cf0
   __DATA.__bss: 0x390
   __DATA_DIRTY.__objc_data: 0x4b50

   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 06A4D6F0-718A-3D2D-B675-8547FF0FE517
-  Functions: 10717
-  Symbols:   35247
-  CStrings:  16077
+  UUID: B76C573C-58CE-36FF-AA84-859B070C86D9
+  Functions: 10723
+  Symbols:   35262
+  CStrings:  16089
 
Symbols:
+ -[ATXFaceGalleryItem containerBundleIdentifier]
+ -[ATXFaceGalleryItem initWithIdentifier:descriptorIdentifier:extensionBundleIdentifier:containerBundleIdentifier:localizedDisplayName:modeSemanticType:titleFontName:titleColor:subtitleComplication:layoutType:complications:landscapeComplications:]
+ -[ATXFaceGalleryItem setContainerBundleIdentifier:]
+ -[ATXPBFaceGalleryItem containerBundleIdentifier]
+ -[ATXPBFaceGalleryItem hasContainerBundleIdentifier]
+ -[ATXPBFaceGalleryItem setContainerBundleIdentifier:]
+ OBJC_IVAR_$_ATXPBFaceGalleryItem._containerBundleIdentifier
+ _OBJC_IVAR_$_ATXFaceGalleryItem._containerBundleIdentifier
+ ___48+[ATXContactModeEntity vipContactEmailAddresses]_block_invoke.386
+ ___48+[ATXContactModeEntity vipContactEmailAddresses]_block_invoke.386.cold.1
+ ___block_literal_global.105
+ ___block_literal_global.88
+ _objc_msgSend$initWithIdentifier:descriptorIdentifier:extensionBundleIdentifier:containerBundleIdentifier:localizedDisplayName:modeSemanticType:titleFontName:titleColor:subtitleComplication:layoutType:complications:landscapeComplications:
+ _objc_msgSend$setContainerBundleIdentifier:
- ___48+[ATXContactModeEntity vipContactEmailAddresses]_block_invoke.377
- ___48+[ATXContactModeEntity vipContactEmailAddresses]_block_invoke.377.cold.1
- ___block_literal_global.102
- ___block_literal_global.85
- _objc_msgSend$initWithIdentifier:descriptorIdentifier:extensionBundleIdentifier:localizedDisplayName:modeSemanticType:titleFontName:titleColor:subtitleComplication:layoutType:complications:landscapeComplications:
CStrings:
+ "@112@0:8@16@24@32@40@48@56@64@72@80q88@96@104"
+ "ExpandablePreview"
+ "HWVersion"
+ "Hello"
+ "T@\"NSString\",&,N,V_containerBundleIdentifier"
+ "T@\"NSString\",C,N,V_containerBundleIdentifier"
+ "hasContainerBundleIdentifier"
+ "identifier: %@, descriptorIdentifier: %@, extensionBundleIdentifier: %@, containerBundleIdentifier: %@, displayNameLocalizationKey: %@, localizedDisplayName: %@, titleFontName: %@, titleColor: %@, subtitleComplication: %@, layoutType: %d, complications: %@, landscapeComplications: %@, modeSemanticType: %@, score: %@, blankTemplate: %@, shouldShowAsShuffleStack: %@, source: %@"
+ "initWithIdentifier:descriptorIdentifier:extensionBundleIdentifier:containerBundleIdentifier:localizedDisplayName:modeSemanticType:titleFontName:titleColor:subtitleComplication:layoutType:complications:landscapeComplications:"
+ "setContainerBundleIdentifier:"
- "identifier: %@, descriptorIdentifier: %@, extensionBundleIdentifier: %@, displayNameLocalizationKey: %@, localizedDisplayName: %@, titleFontName: %@, titleColor: %@, subtitleComplication: %@, layoutType: %d, complications: %@, landscapeComplications: %@, modeSemanticType: %@, score: %@, blankTemplate: %@, shouldShowAsShuffleStack: %@, source: %@"

```
