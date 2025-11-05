## PersonaUI

> `/System/iOSSupport/System/Library/PrivateFrameworks/PersonaUI.framework/Versions/A/PersonaUI`

```diff

-1359.0.0.0.0
-  __TEXT.__text: 0x7f10
+1359.500.41.0.0
+  __TEXT.__text: 0x7ed0
   __TEXT.__auth_stubs: 0x750
-  __TEXT.__objc_methlist: 0x988
+  __TEXT.__objc_methlist: 0xb4c
   __TEXT.__const: 0x348
   __TEXT.__cstring: 0x76a
   __TEXT.__oslogstring: 0x1ff
   __TEXT.__gcc_except_tab: 0x18
-  __TEXT.__unwind_info: 0x2b8
+  __TEXT.__unwind_info: 0x2c8
   __TEXT.__objc_classname: 0xe4
-  __TEXT.__objc_methname: 0x1df6
-  __TEXT.__objc_methtype: 0x5dd
+  __TEXT.__objc_methname: 0x1e17
+  __TEXT.__objc_methtype: 0x60b
   __TEXT.__objc_stubs: 0x1c80
   __DATA_CONST.__got: 0x1a0
   __DATA_CONST.__const: 0x2c0

   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8e8
+  __DATA_CONST.__objc_selrefs: 0x9b8
   __DATA_CONST.__objc_superrefs: 0x38
   __AUTH_CONST.__auth_got: 0x3b8
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x7a0
-  __AUTH_CONST.__objc_const: 0x1450
+  __AUTH_CONST.__objc_const: 0x1120
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0xb4

   - /System/iOSSupport/System/Library/Frameworks/UIKit.framework/Versions/A/UIKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 024E631F-86B9-34F8-B7B6-19250A731D00
-  Functions: 220
-  Symbols:   796
-  CStrings:  624
+  UUID: 29572CE4-5DB4-345D-A015-BF0E68ED60AD
+  Functions: 222
+  Symbols:   798
+  CStrings:  626
 
Symbols:
+ +[NSBundle(PersonaUI) pr_personaUIBundle].cold.1
+ +[PRMonogram _fontSpecs].cold.1
+ _objc_retain_x26
- _objc_retain_x25
Functions:
~ -[PRImageView setImage:] : 128 -> 124
~ -[PRMonogram setText:] : 188 -> 180
~ +[PRMonogram _fontSpecs] : 84 -> 68
~ -[PRMonogram(DataRepresentation) appendToRecipe:text:fontIndex:] : 212 -> 196
~ -[PRMonogram(DataRepresentation) dataRepresentationWithVersion:] : 460 -> 456
~ -[PRMonogram(DataRepresentation) _takeValuesFromDataRepresentation:] : 916 -> 896
~ +[PRLikenessCache _ensureExistenceOfDirectory:] : 304 -> 308
~ ___55-[PRLikenessCache imageForLikeness:context:completion:]_block_invoke_2 : 208 -> 204
~ -[PRLikenessCache _renderImageForLikeness:context:completion:] : 532 -> 536
~ +[PRLikenessCache _removeImageAtURL:] : 296 -> 300
~ -[PRMonogramColor setColorName:] : 200 -> 192
~ +[NSBundle(PersonaUI) pr_personaUIBundle] : 84 -> 68
~ -[PRLikenessView setCircular:] : 136 -> 128
~ -[PRLikenessView _setDisplayedView:] : 188 -> 180
~ -[PRMonogramView setMonogram:] : 276 -> 272
CStrings:
+ "textField:insertInputSuggestion:"
+ "v32@0:8@\"UITextField\"16@\"UIInputSuggestion\"24"

```
