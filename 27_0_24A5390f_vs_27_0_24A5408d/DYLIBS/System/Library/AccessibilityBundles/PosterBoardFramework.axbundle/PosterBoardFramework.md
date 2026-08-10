## PosterBoardFramework

> `/System/Library/AccessibilityBundles/PosterBoardFramework.axbundle/PosterBoardFramework`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__constg_swiftt`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__DATA_DIRTY.__objc_data`

```diff

-3045.0.0.0.0
-  __TEXT.__text: 0x5d30
+3048.0.0.0.0
+  __TEXT.__text: 0x5f34
   __TEXT.__objc_methlist: 0x860
-  __TEXT.__const: 0x40
+  __TEXT.__const: 0x50
   __TEXT.__constg_swiftt: 0x2c
   __TEXT.__swift5_typeref: 0x6
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_types: 0x4
   __TEXT.__gcc_except_tab: 0x9c
   __TEXT.__cstring: 0x15d2
-  __TEXT.__unwind_info: 0x290
+  __TEXT.__oslogstring: 0x1ea
+  __TEXT.__unwind_info: 0x298
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0x138
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x410
-  __DATA_CONST.__objc_superrefs: 0x78
+  __DATA_CONST.__objc_superrefs: 0x80
   __DATA_CONST.__got: 0xf0
   __AUTH_CONST.__const: 0xa0
   __AUTH_CONST.__cfstring: 0x16a0

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 179
-  Symbols:   644
-  CStrings:  206
+  Symbols:   650
+  CStrings:  209
 
Symbols:
+ _AXAIWhiteGloveLoggingEnabled
+ _AXLogCommon
+ _NSStringFromClass
+ __os_log_error_impl
+ __os_log_impl
+ _os_log_type_enabled
Functions:
~ -[PBFPosterGalleryPreviewCellAccessibility accessibilityLabel] : 388 -> 620
~ -[PosterGalleryAffordanceCollectionViewCellAccessibility accessibilityLabel] : 12 -> 296
CStrings:
+ "rdar://168563356 PBFPosterGalleryPreviewCell accessibilityLabel default-fallback previewIdentifier=%{public}@ label=%{public}@ (no posterTitle, no accessibilityValue)"
+ "rdar://168563356 PBFPosterGalleryPreviewCell accessibilityLabel enter previewIdentifier=%{public}@ posterTitle=%{public}@ mappedLabel=%{public}@ superValue=%{public}@"
+ "rdar://168563356 PosterGalleryAffordanceCollectionViewCell accessibilityLabel class=%{public}@ identifier=%{public}@ label=%{public}@ superLabel=%{public}@"
```
