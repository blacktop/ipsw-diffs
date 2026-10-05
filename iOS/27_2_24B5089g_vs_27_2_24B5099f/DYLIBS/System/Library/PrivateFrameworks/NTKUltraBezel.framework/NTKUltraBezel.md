## NTKUltraBezel

> `/System/Library/PrivateFrameworks/NTKUltraBezel.framework/NTKUltraBezel`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`
- `__TEXT.__oslogstring`

```diff

-2483.544.0.0.0
-  __TEXT.__text: 0x13c2c
-  __TEXT.__objc_methlist: 0x110c
-  __TEXT.__const: 0x672
+2483.556.1.0.0
+  __TEXT.__text: 0x1497c
+  __TEXT.__objc_methlist: 0x115c
+  __TEXT.__const: 0x6a2
   __TEXT.__cstring: 0xc38
   __TEXT.__oslogstring: 0x272
-  __TEXT.__gcc_except_tab: 0x1a8
+  __TEXT.__gcc_except_tab: 0x278
   __TEXT.__swift5_typeref: 0x8d
   __TEXT.__constg_swiftt: 0x44
   __TEXT.__swift5_reflstr: 0x58

   __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_proto: 0x10
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x640
+  __TEXT.__unwind_info: 0x668
   __TEXT.__eh_frame: 0x128
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x260
+  __DATA_CONST.__const: 0x280
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xdb0
+  __DATA_CONST.__objc_selrefs: 0xe18
   __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__objc_arraydata: 0x38
-  __DATA_CONST.__got: 0x208
+  __DATA_CONST.__got: 0x218
   __AUTH_CONST.__const: 0x2ad
   __AUTH_CONST.__cfstring: 0xb40
-  __AUTH_CONST.__objc_const: 0x1dc0
+  __AUTH_CONST.__objc_const: 0x1e10
   __AUTH_CONST.__objc_floatobj: 0x40
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH_CONST.__objc_intobj: 0x48
+  __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_doubleobj: 0x40
-  __AUTH_CONST.__auth_got: 0x678
+  __AUTH_CONST.__auth_got: 0x680
   __AUTH.__objc_data: 0x3f0
   __AUTH.__data: 0xa0
-  __DATA.__objc_ivar: 0x1c4
+  __DATA.__objc_ivar: 0x1cc
   __DATA.__data: 0x450
   - /System/Library/Frameworks/ClockKit.framework/ClockKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 471
-  Symbols:   915
+  Functions: 483
+  Symbols:   935
   CStrings:  131
 
Symbols:
+ +[CLKFont(NTKFoghornFaceAdditions) _foghornCaseSensitiveFontDescriptor]
+ +[CLKFont(NTKFoghornFaceAdditions) foghornReadinessBezelLabelFontOfSize:]
+ -[NTKFoghornFaceBezelView _readinessBaseLabelAllocatedWidth]
+ -[NTKFoghornFaceBezelView _readinessDeemphasizedBaseColor]
+ -[NTKFoghornFaceBezelView _updateBaseLabelAllocatedWidthForStyle:]
+ -[NTKFoghornFaceBezelView readinessDataState]
+ -[NTKFoghornFaceBezelView readinessLevel]
+ -[NTKFoghornFaceBezelView setReadinessDataState:]
+ -[NTKFoghornFaceBezelView setReadinessLevel:]
+ GCC_except_table26
+ _CGRectGetWidth
+ _NTKFoghornReadinessSnapshotLevel
+ _OBJC_IVAR_$_NTKFoghornFaceBezelView._baseLabelMaxWidthConstraint
+ _OBJC_IVAR_$_NTKFoghornFaceBezelView._readinessDataState
+ _OBJC_IVAR_$_NTKFoghornFaceBezelView._readinessLevel
+ _UIFontFeatureSelectorIdentifierKey
+ _UIFontFeatureTypeIdentifierKey
+ ___71+[CLKFont(NTKFoghornFaceAdditions) _foghornCaseSensitiveFontDescriptor]_block_invoke
+ ___block_descriptor_40_e5_v8?0l
+ ___copy_constructor_8_8_s0_s8_s16_s24_s32_s40_s48_s56_s64_s72_s80_s88
+ ___move_assignment_8_8_s0_s8_s16_s24_s32_s40_s48_s56_s64_s72_s80_s88
+ __foghornCaseSensitiveFontDescriptor.fontDescriptor
+ __foghornCaseSensitiveFontDescriptor.onceToken
+ __readinessColorByScalingAlpha
+ __readinessDeemphasizedColors
- -[NTKFoghornFaceBezelView readinessScore]
- -[NTKFoghornFaceBezelView setReadinessScore:]
- GCC_except_table25
- _NTKFoghornReadinessSnapshotScore
- _OBJC_IVAR_$_NTKFoghornFaceBezelView._readinessScore
CStrings:
+ "Readiness bezel updating with dataState: %ld, level: %@"
- "Readiness bezel updating with dataState: %ld, score: %@"
```
