## PersonaKit

> `/System/Library/PrivateFrameworks/PersonaKit.framework/Versions/A/PersonaKit`

```diff

-1359.0.0.0.0
-  __TEXT.__text: 0x9614
+1359.500.41.0.0
+  __TEXT.__text: 0x9610
   __TEXT.__auth_stubs: 0x310
-  __TEXT.__objc_methlist: 0x640
+  __TEXT.__objc_methlist: 0x8a8
   __TEXT.__const: 0x69
   __TEXT.__gcc_except_tab: 0x78
   __TEXT.__cstring: 0x131c

   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5b0
+  __DATA_CONST.__objc_selrefs: 0x640
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
   __AUTH_CONST.__auth_got: 0x198
   __AUTH_CONST.__const: 0x430
   __AUTH_CONST.__cfstring: 0x6c0
-  __AUTH_CONST.__objc_const: 0x12f8
+  __AUTH_CONST.__objc_const: 0xe68
   __DATA.__objc_ivar: 0x70
   __DATA.__data: 0x180
   __DATA.__bss: 0x10

   - /System/Library/Frameworks/ImageIO.framework/Versions/A/ImageIO
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F3090B4F-E0D8-3B4C-83A8-ECB398EFEDE1
-  Functions: 215
-  Symbols:   571
+  UUID: 4F450311-D2BA-3255-B72C-2B9EF7CAC4AE
+  Functions: 218
+  Symbols:   574
   CStrings:  615
 
Symbols:
+ +[PRLikeness _dateFormatter].cold.1
+ +[PRPersonaServiceInterface XPCInterface].cold.1
+ _PRGetLogSystem.cold.1
Functions:
~ __PRGetLogSystem : 84 -> 68
~ -[PRPersonaStore _personaServiceConnection] : 500 -> 492
~ +[PRPersonaServiceInterface XPCInterface] : 84 -> 68
~ +[NSString(PersonaKit) pr_hexStringWithData:] : 208 -> 204
~ +[PRLikeness likenessWithPropagatedData:] : 472 -> 468
~ +[PRLikeness _dateFormatter] : 84 -> 68

```
