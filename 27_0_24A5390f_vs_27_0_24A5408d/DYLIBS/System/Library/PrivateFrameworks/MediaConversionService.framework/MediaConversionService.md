## MediaConversionService

> `/System/Library/PrivateFrameworks/MediaConversionService.framework/MediaConversionService`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH_CONST.__objc_dictobj`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-910.33.102.0.0
-  __TEXT.__text: 0x1b4d4
-  __TEXT.__objc_methlist: 0x1c2c
+912.0.111.0.0
+  __TEXT.__text: 0x1b520
+  __TEXT.__objc_methlist: 0x1c3c
   __TEXT.__const: 0xc0
   __TEXT.__gcc_except_tab: 0x58c
   __TEXT.__cstring: 0x4c8c

   __DATA_CONST.__objc_classlist: 0xb8
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x14a8
+  __DATA_CONST.__objc_selrefs: 0x14b0
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x58
   __DATA_CONST.__objc_arraydata: 0x4c8
-  __DATA_CONST.__got: 0x390
+  __DATA_CONST.__got: 0x398
   __AUTH_CONST.__const: 0x140
   __AUTH_CONST.__cfstring: 0x2da0
   __AUTH_CONST.__objc_const: 0x2a78

   - /System/Library/PrivateFrameworks/PhotosFormats.framework/PhotosFormats
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 639
-  Symbols:   1894
+  Functions: 640
+  Symbols:   1897
   CStrings:  553
 
Symbols:
+ -[PHMediaFormatConversionImplementation_MediaConversionService _conversionErrorForStatus:underlyingError:]
+ GCC_except_table506
+ GCC_except_table508
+ GCC_except_table594
+ GCC_except_table596
+ GCC_except_table599
+ GCC_except_table601
+ GCC_except_table614
+ ___NSDictionary0__struct
+ ___block_descriptor_64_e8_32s40s48bs56w_e37_v32?0q8"NSDictionary"16"NSError"24ls32l8w56l8s40l8s48l8
+ _objc_msgSend$_conversionErrorForStatus:underlyingError:
- GCC_except_table505
- GCC_except_table507
- GCC_except_table593
- GCC_except_table595
- GCC_except_table598
- GCC_except_table600
- GCC_except_table613
- ___block_descriptor_56_e8_32s40bs48w_e37_v32?0q8"NSDictionary"16"NSError"24ls32l8w48l8s40l8
Functions:
~ -[PHMediaFormatConversionRequest _calculateRequiresFormatConversion] : 1108 -> 1128
~ ___136-[PHMediaFormatConversionImplementation_MediaConversionService submitNonSinglePassVideoConversionRequest:destination:completionHandler:]_block_invoke : 400 -> 268
~ -[PHMediaFormatConversionImplementation_MediaConversionService submitSinglePassVideoConversionRequest:destination:completionHandler:] : 720 -> 732
~ ___133-[PHMediaFormatConversionImplementation_MediaConversionService submitSinglePassVideoConversionRequest:destination:completionHandler:]_block_invoke : 396 -> 264
~ ___112-[PHMediaFormatConversionImplementation_MediaConversionService performImageConversionRequest:completionHandler:]_block_invoke : 228 -> 260
+ -[PHMediaFormatConversionImplementation_MediaConversionService _conversionErrorForStatus:underlyingError:]
```
