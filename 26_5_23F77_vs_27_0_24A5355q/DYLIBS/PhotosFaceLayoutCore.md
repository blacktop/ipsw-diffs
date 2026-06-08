## PhotosFaceLayoutCore

> `/System/Library/PrivateFrameworks/PhotosFaceLayoutCore.framework/PhotosFaceLayoutCore`

```diff

-95.1.0.0.0
-  __TEXT.__text: 0x62f8
-  __TEXT.__auth_stubs: 0x330
+96.0.0.0.0
+  __TEXT.__text: 0x6190
   __TEXT.__objc_methlist: 0x154
   __TEXT.__const: 0x200
   __TEXT.__oslogstring: 0x187
-  __TEXT.__cstring: 0x134
-  __TEXT.__unwind_info: 0x138
-  __TEXT.__objc_classname: 0x4f
-  __TEXT.__objc_methname: 0x5b2
-  __TEXT.__objc_methtype: 0x1c4
-  __TEXT.__objc_stubs: 0x460
-  __DATA_CONST.__got: 0xa0
+  __TEXT.__cstring: 0x136
+  __TEXT.__unwind_info: 0x130
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x20
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x1a0
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0x1a0
+  __DATA_CONST.__got: 0xa0
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0x80
   __AUTH_CONST.__objc_const: 0x4e8
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH.__objc_data: 0x140
+  __AUTH_CONST.__auth_got: 0x0
+  __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0x38
-  __DATA.__bss: 0x10
+  __DATA_DIRTY.__objc_data: 0xa0
+  __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/PhotosFaceCore.framework/PhotosFaceCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D5A93621-496A-35A6-B66E-AB4AF323C963
+  UUID: 833CD3CF-167F-395A-8B4B-23CD4E1785C0
   Functions: 61
-  Symbols:   279
-  CStrings:  123
+  Symbols:   284
+  CStrings:  23
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x3
- _objc_retainAutoreleasedReturnValue
Functions:
~ -[PFLCCoverageValidator initWithMaskImage:orientation:] : 1060 -> 1032
~ -[PFLCCoverageValidator coverageOfTimeLabel:] : 352 -> 368
~ _combineFaceRects : 284 -> 272
~ _cropTimeAboveFacesWithMask : 828 -> 832
~ _iterativeBidirectionalFacesMaskSolver : 1292 -> 1252
~ -[PFLCCurationPositionScore description] : 188 -> 176
~ _PFLCCurationScoreForAsset : 2084 -> 2056
~ _PFLCCalculateLayout : 2740 -> 2672
~ _layoutNatureMatte : 856 -> 832
~ _layoutNatureNoMatte : 940 -> 908
~ _layoutPeopleMatte : 684 -> 672
~ _layoutPeopleNoMatte : 1700 -> 1664
~ _layoutPetsMatte : 996 -> 980
~ _layoutPetsNoMatte : 1912 -> 1868
~ _pflc_layout_log : 84 -> 68
~ _expandRects : 452 -> 444
~ __rectAsString : 104 -> 100
CStrings:
- ".cxx_destruct"
- "@\"NSDictionary\""
- "@16@0:8"
- "@28@0:8^{CGImage=}16I24"
- "@32@0:8@16Q24"
- "@76@0:8d16d24d32{CGRect={CGPoint=dd}{CGSize=dd}}40B72"
- "@96@0:8d16{CGRect={CGPoint=dd}{CGSize=dd}}24{CGRect={CGPoint=dd}{CGSize=dd}}56Q88"
- "B"
- "B16@0:8"
- "PFLCCoverageValidator"
- "PFLCCurationPositionScore"
- "PFLCCurationScore"
- "PFLCLayout"
- "Q"
- "Q16@0:8"
- "T@\"NSDictionary\",R,N,V_positionScores"
- "TB,N,V_usesMask"
- "TQ,R,N,V_classification"
- "TQ,R,N,V_preferredPosition"
- "Td,N,V_cropScore"
- "Td,N,V_foregroundCoverage"
- "Td,N,V_layoutScore"
- "Td,R,N,V_cropScore"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_visibleRect"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_cropRect"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_timeLabelRect"
- "^I"
- "_classification"
- "_cropRect"
- "_cropScore"
- "_cumulativeData"
- "_foregroundCoverage"
- "_height"
- "_layoutScore"
- "_positionScores"
- "_preferredPosition"
- "_timeLabelRect"
- "_usesMask"
- "_visibleRect"
- "_width"
- "acceptableCropRect"
- "addObject:"
- "arrayWithCapacity:"
- "arrayWithObjects:count:"
- "bytes"
- "centerX"
- "centerY"
- "classification"
- "copy"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "coverageOfTimeLabel:"
- "cropRect"
- "cropScore"
- "d"
- "d16@0:8"
- "d48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
- "dataWithLength:"
- "dealloc"
- "description"
- "detectionType"
- "dictionary"
- "fetchFacesInAsset:options:"
- "foregroundCoverage"
- "init"
- "initWithCropScore:cropRect:timeLabelRect:classification:"
- "initWithCropScore:layoutScore:foregroundCoverage:visibleRect:usesMask:"
- "initWithMaskImage:orientation:"
- "initWithPositionScores:preferredPosition:"
- "layoutScore"
- "localIdentifier"
- "mutableBytes"
- "numberWithUnsignedInteger:"
- "objectAtIndexedSubscript:"
- "pixelHeight"
- "pixelWidth"
- "positionScores"
- "preferredCropRect"
- "preferredPosition"
- "rectValue"
- "setCropScore:"
- "setForegroundCoverage:"
- "setIncludedDetectionTypes:"
- "setLayoutScore:"
- "setObject:forKeyedSubscript:"
- "setUsesMask:"
- "setVisibleRect:"
- "size"
- "stringWithFormat:"
- "timeLabelRect"
- "usesMask"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8d16"
- "v48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
- "valueWithBytes:objCType:"
- "valueWithRect:"
- "visibleRect"
- "{CGRect=\"origin\"{CGPoint=\"x\"d\"y\"d}\"size\"{CGSize=\"width\"d\"height\"d}}"
- "{CGRect={CGPoint=dd}{CGSize=dd}}16@0:8"

```
