## BiometricKitUI

> `/System/Library/PrivateFrameworks/BiometricKitUI.framework/BiometricKitUI`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`

```diff

-685.1.2.0.0
-  __TEXT.__text: 0x6ee28
-  __TEXT.__objc_methlist: 0x7300
+685.1.4.0.0
+  __TEXT.__text: 0x6ef70
+  __TEXT.__objc_methlist: 0x7368
   __TEXT.__const: 0xd44
   __TEXT.__gcc_except_tab: 0xde4
   __TEXT.__cstring: 0x3036
-  __TEXT.__oslogstring: 0x6a83
+  __TEXT.__oslogstring: 0x6b13
   __TEXT.__dlopen_cstrs: 0x292
   __TEXT.__swift5_typeref: 0x2c2
   __TEXT.__swift5_capture: 0x114

   __TEXT.__swift5_proto: 0x20
   __TEXT.__swift5_types: 0x34
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x2150
+  __TEXT.__unwind_info: 0x2158
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1238
+  __DATA_CONST.__const: 0x1260
   __DATA_CONST.__objc_classlist: 0x248
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x160
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4928
+  __DATA_CONST.__objc_selrefs: 0x4950
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x198
   __DATA_CONST.__objc_arraydata: 0x188
   __DATA_CONST.__got: 0x880
   __AUTH_CONST.__const: 0xc50
   __AUTH_CONST.__cfstring: 0x3440
-  __AUTH_CONST.__objc_const: 0x10720
+  __AUTH_CONST.__objc_const: 0x10790
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__objc_floatobj: 0x80

   __AUTH_CONST.__auth_got: 0x970
   __AUTH.__objc_data: 0x1448
   __AUTH.__data: 0x180
-  __DATA.__objc_ivar: 0xa00
+  __DATA.__objc_ivar: 0xa08
   __DATA.__data: 0x11c0
   __DATA.__common: 0x1f8
   __DATA_DIRTY.__objc_data: 0x550

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2878
-  Symbols:   4586
-  CStrings:  1083
+  Functions: 2887
+  Symbols:   4600
+  CStrings:  1085
 
Symbols:
+ +[BKUIPearlEnrollController preloadCollectingFramesForAgeVerification:completion:]
+ +[BKUIPearlEnrollViewController preloadCollectingFramesForAgeVerification:completion:]
+ -[BKUIPearlEnrollController collectsFramesForAgeVerification]
+ -[BKUIPearlEnrollController setCollectsFramesForAgeVerification:]
+ -[BKUIPearlEnrollView initWithFrame:videoCaptureSession:inSheet:positioningGuideView:squareNeedsPositionLayout:collectsFramesForAgeVerification:]
+ -[BKUIPearlEnrollViewController collectsFramesForAgeVerification]
+ -[BKUIPearlEnrollViewController setCollectsFramesForAgeVerification:]
+ -[BKUIPearlVideoCaptureSession collectsFramesForAgeVerification]
+ -[BKUIPearlVideoCaptureSession initCollectingFramesForAgeVerification:]
+ GCC_except_table41
+ GCC_except_table50
+ GCC_except_table62
+ GCC_except_table63
+ GCC_except_table73
+ GCC_except_table97
+ _OBJC_IVAR_$_BKUIPearlEnrollViewController._collectsFramesForAgeVerification
+ _OBJC_IVAR_$_BKUIPearlVideoCaptureSession._collectsFramesForAgeVerification
+ ___145-[BKUIPearlEnrollView initWithFrame:videoCaptureSession:inSheet:positioningGuideView:squareNeedsPositionLayout:collectsFramesForAgeVerification:]_block_invoke
+ ___61-[BKUIPearlJindoEnrollViewController nextStateButtonPressed:]_block_invoke_2
+ ___86+[BKUIPearlEnrollViewController preloadCollectingFramesForAgeVerification:completion:]_block_invoke
+ ___block_descriptor_57_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
- GCC_except_table40
- GCC_except_table49
- GCC_except_table60
- GCC_except_table72
- GCC_except_table96
- ___112-[BKUIPearlEnrollView initWithFrame:videoCaptureSession:inSheet:positioningGuideView:squareNeedsPositionLayout:]_block_invoke
- ___55+[BKUIPearlEnrollViewController preloadWithCompletion:]_block_invoke
CStrings:
+ "CaptureSession: Collecting frames for age verification; setting up selfie session"
+ "CaptureSession: Not collecting frames for age verification; skipping selfie session"
+ "Will collect frames for age verification: %@"
+ "\x91"
- "Pearl: skipping Jindo banner post as enrollment is no longer active"
- "\x81"
```
