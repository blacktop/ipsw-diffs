## PhotosFaceLayoutCore

> `/System/Library/PrivateFrameworks/PhotosFaceLayoutCore.framework/PhotosFaceLayoutCore`

```diff

 95.0.0.0.0
-  __TEXT.__text: 0x6334
-  __TEXT.__auth_stubs: 0x380
+  __TEXT.__text: 0x62f8
+  __TEXT.__auth_stubs: 0x330
   __TEXT.__objc_methlist: 0x154
-  __TEXT.__const: 0x220
+  __TEXT.__const: 0x200
   __TEXT.__oslogstring: 0x187
   __TEXT.__cstring: 0x134
-  __TEXT.__unwind_info: 0x130
+  __TEXT.__unwind_info: 0x138
   __TEXT.__objc_classname: 0x4f
   __TEXT.__objc_methname: 0x5b2
   __TEXT.__objc_methtype: 0x1c4

   __DATA_CONST.__objc_selrefs: 0x1a0
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0x1c8
+  __AUTH_CONST.__auth_got: 0x1a0
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0x80
   __AUTH_CONST.__objc_const: 0x4e8

   - /System/Library/PrivateFrameworks/PhotosFaceCore.framework/PhotosFaceCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 77032A93-9873-3508-BBC9-687A059512B6
+  UUID: 2BACDDB5-2EDE-3952-8473-DE7E746FDFEA
   Functions: 61
-  Symbols:   284
+  Symbols:   279
   CStrings:  123
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
- _objc_claimAutoreleasedReturnValue
- _objc_retain
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x3
Functions:
~ -[PFLCCoverageValidator initWithMaskImage:orientation:] : 1216 -> 1060
~ _combineFaceRects : 272 -> 284
~ _cropTimeBelowFacesNoMask : 500 -> 504
~ _cropTimeAboveFacesWithMask : 824 -> 828
~ _iterativeBidirectionalFacesMaskSolver : 1524 -> 1292
~ -[PFLCCurationPositionScore description] : 176 -> 188
~ _PFLCCurationScoreForAsset : 2052 -> 2084
~ _PFLCCalculateLayout : 2672 -> 2740
~ _layoutNatureMatte : 832 -> 856
~ _layoutNatureNoMatte : 908 -> 940
~ _layoutPeopleMatte : 672 -> 684
~ _layoutPeopleNoMatte : 1664 -> 1700
~ _layoutPetsMatte : 980 -> 996
~ _layoutPetsNoMatte : 1868 -> 1912
~ _pflc_layout_log : 68 -> 84
~ _expandRects : 440 -> 452
~ __rectAsString : 100 -> 104

```
