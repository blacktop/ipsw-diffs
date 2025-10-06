## QuickLookThumbnailGeneration

> `/System/Library/PrivateFrameworks/QuickLookThumbnailGeneration.framework/QuickLookThumbnailGeneration`

```diff

-186.4.1.0.0
-  __TEXT.__text: 0x530
-  __TEXT.__auth_stubs: 0x110
+186.5.3.0.0
+  __TEXT.__text: 0x634
+  __TEXT.__auth_stubs: 0x170
   __TEXT.__objc_methlist: 0x38
   __TEXT.__const: 0x68
   __TEXT.__cstring: 0x17
+  __TEXT.__oslogstring: 0x26
   __TEXT.__dlopen_cstrs: 0x41
   __TEXT.__unwind_info: 0x68
   __TEXT.__objc_classname: 0x3b
-  __TEXT.__objc_methname: 0x1da
-  __TEXT.__objc_methtype: 0x3d
+  __TEXT.__objc_methname: 0x1e0
+  __TEXT.__objc_methtype: 0x41
   __TEXT.__objc_stubs: 0x140
-  __DATA_CONST.__got: 0x58
+  __DATA_CONST.__got: 0x60
   __DATA_CONST.__const: 0x38
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0xd8
   __DATA_CONST.__objc_selrefs: 0x60
+  __DATA_CONST.__objc_classrefs: 0x20
   __AUTH_CONST.__cfstring: 0x20
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_const: 0x48
-  __AUTH_CONST.__auth_got: 0x90
+  __AUTH_CONST.__auth_got: 0xc0
   __AUTH.__objc_data: 0xa0
-  __DATA.__objc_classrefs: 0x20
   __DATA.__bss: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/UIFoundation.framework/UIFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E19A5FDD-4E2F-3230-BDAB-CFE10D0607F4
-  Functions: 5
-  Symbols:   73
-  CStrings:  24
+  UUID: 80BAF88B-1D0F-3837-A19C-7EE4CD24B2D7
+  Functions: 6
+  Symbols:   82
+  CStrings:  25
 
Symbols:
+ +[QLTextThumbnailRenderer mutableAttributedStringForThumbnailWithURL:documentAttributes:error:]
+ +[QLTextThumbnailRenderer mutableAttributedStringForThumbnailWithURL:documentAttributes:error:].cold.1
+ _QLTInitLogging
+ __os_log_error_impl
+ _objc_release_x25
+ _objc_release_x26
+ _objc_retainAutorelease
+ _os_log_type_enabled
+ _qltLogHandles
- +[QLTextThumbnailRenderer mutableAttributedStringForThumbnailWithURL:documentAttributes:]
CStrings:
+ "@40@0:8@16^@24^@32"
+ "Could not get content type for %@: %@"
+ "mutableAttributedStringForThumbnailWithURL:documentAttributes:error:"
- "@32@0:8@16^@24"
- "mutableAttributedStringForThumbnailWithURL:documentAttributes:"

```
