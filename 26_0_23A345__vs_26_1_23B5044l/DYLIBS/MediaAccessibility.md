## MediaAccessibility

> `/System/Library/Frameworks/MediaAccessibility.framework/MediaAccessibility`

```diff

-214.0.0.0.0
+216.0.0.0.0
   __TEXT.__text: 0xe320
   __TEXT.__auth_stubs: 0xd90
   __TEXT.__objc_methlist: 0x464

   __TEXT.__objc_methtype: 0x2ff
   __TEXT.__objc_stubs: 0x820
   __DATA_CONST.__got: 0x190
-  __DATA_CONST.__const: 0x4f8
+  __DATA_CONST.__const: 0x540
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  UUID: A2286CE0-9F3C-3FCE-8D23-10E76FFB45A3
+  UUID: 4F6C45B4-0A63-3C6F-A182-C993CB32860E
   Functions: 497
-  Symbols:   1228
+  Symbols:   1236
   CStrings:  482
 
Symbols:
+ _MACreatePrefCategoryKey
+ _kMADisplayFilterPrefBlueColorCorrectionIntensityKey
+ _kMADisplayFilterPrefCategoryEnabledKey
+ _kMADisplayFilterPrefGrayscaleCorrectionIntensityKey
+ _kMADisplayFilterPrefGreenColorCorrectionIntensityKey
+ _kMADisplayFilterPrefRedColorCorrectionIntensityKey
+ _kMADisplayFilterPrefReduceWhitePointIntensityKey
+ _kMADisplayFilterPrefSingleColorHueKey
+ _kMADisplayFilterPrefSingleColorIntensityKey
+ _kMADisplayFilterPrefTypeKey
- __createPrefCategoryKey
Functions:
~ _MADisplayFilterPrefPossibleTypesForCategory -> _MACreatePrefCategoryKey : 36 -> 96
~ _MADisplayFilterPrefSuspendNotifications -> _MADisplayFilterPrefPossibleTypesForCategory : 12 -> 36
~ _MADisplayFilterPrefGetType -> _MADisplayFilterPrefSuspendNotifications : 232 -> 12
~ __copyPrefFilterType -> _MADisplayFilterPrefGetType : 68 -> 232
~ _MADisplayFilterPrefSetType -> __copyPrefFilterType : 156 -> 68
~ __createPrefCategoryKey -> _MADisplayFilterPrefSetType : 96 -> 156

```
