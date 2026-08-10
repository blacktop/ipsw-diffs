## ActivityProgressKit

> `/System/Library/PrivateFrameworks/ActivityProgressKit.framework/ActivityProgressKit`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__AUTH_CONST.__const`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-390.0.0.0.0
-  __TEXT.__text: 0x25fc
-  __TEXT.__objc_methlist: 0x1b8
+391.0.0.0.0
+  __TEXT.__text: 0x26d4
+  __TEXT.__objc_methlist: 0x1d0
   __TEXT.__const: 0x4da
-  __TEXT.__cstring: 0x125
+  __TEXT.__cstring: 0x165
   __TEXT.__swift5_typeref: 0x132
   __TEXT.__swift5_capture: 0x10
   __TEXT.__constg_swiftt: 0x144

   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x198
+  __DATA_CONST.__objc_selrefs: 0x1a8
   __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x1e8
-  __AUTH_CONST.__cfstring: 0x160
-  __AUTH_CONST.__objc_const: 0x498
+  __AUTH_CONST.__cfstring: 0x1a0
+  __AUTH_CONST.__objc_const: 0x4c8
   __AUTH_CONST.__auth_got: 0x270
-  __DATA.__objc_ivar: 0x14
+  __DATA.__objc_ivar: 0x18
   __DATA.__data: 0x110
   __DATA.__bss: 0x860
   __DATA_DIRTY.__objc_data: 0xf0

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 131
-  Symbols:   248
-  CStrings:  15
+  Functions: 133
+  Symbols:   252
+  CStrings:  17
 
Symbols:
+ -[APKActivityProgress initWithCompletedUnitCount:totalUnitCount:cancelled:shouldHideProgressUI:preserveSubtitleOnFailure:]
+ -[APKActivityProgress preserveSubtitleOnFailure]
+ -[APKActivityProgress setPreserveSubtitleOnFailure:]
+ _OBJC_IVAR_$_APKActivityProgress._preserveSubtitleOnFailure
+ _objc_msgSend$initWithCompletedUnitCount:totalUnitCount:cancelled:shouldHideProgressUI:preserveSubtitleOnFailure:
+ _objc_msgSend$preserveSubtitleOnFailure
- -[APKActivityProgress initWithCompletedUnitCount:totalUnitCount:cancelled:shouldHideProgressUI:]
- _objc_msgSend$initWithCompletedUnitCount:totalUnitCount:cancelled:shouldHideProgressUI:
CStrings:
+ "PreserveSubtitleOnFailure"
+ "preserveSubtitleOnFailure"
```
