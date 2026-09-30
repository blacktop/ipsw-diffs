## IconFoundation

> `/System/Library/PrivateFrameworks/IconFoundation.framework/Versions/A/IconFoundation`

```diff

-  __TEXT.__text: 0x39b90
+  __TEXT.__text: 0x39a64
   __TEXT.__objc_methlist: 0x30d4
-  __TEXT.__cstring: 0x12302
+  __TEXT.__cstring: 0x12382
   __TEXT.__const: 0x9a8
-  __TEXT.__oslogstring: 0xcde
+  __TEXT.__oslogstring: 0xc12
   __TEXT.__constg_swiftt: 0x174
   __TEXT.__swift5_typeref: 0x48
   __TEXT.__swift5_fieldmd: 0xb0
   __TEXT.__swift5_types: 0x2c
   __TEXT.__gcc_except_tab: 0xdc
-  __TEXT.__unwind_info: 0xe38
+  __TEXT.__unwind_info: 0xe30
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1f30
+  __DATA_CONST.__objc_selrefs: 0x1f20
   __DATA_CONST.__objc_superrefs: 0x110
   __DATA_CONST.__objc_arraydata: 0x18
-  __DATA_CONST.__got: 0x3f0
+  __DATA_CONST.__got: 0x3d8
   __AUTH_CONST.__const: 0xb08
-  __AUTH_CONST.__cfstring: 0x1b20
-  __AUTH_CONST.__objc_const: 0x4c78
+  __AUTH_CONST.__cfstring: 0x1b80
+  __AUTH_CONST.__objc_const: 0x4cb8
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__auth_got: 0x7c0
-  __AUTH.__objc_data: 0x618
-  __AUTH.__data: 0x98
-  __DATA.__objc_ivar: 0x338
+  __AUTH.__objc_data: 0x410
+  __DATA.__objc_ivar: 0x33c
   __DATA.__data: 0x2e8
   __DATA.__crash_info: 0x148
   __DATA.__bss: 0x268
   __DATA.__common: 0x290
-  __DATA_DIRTY.__objc_data: 0x938
+  __DATA_DIRTY.__objc_data: 0xb40
+  __DATA_DIRTY.__data: 0x98
   __DATA_DIRTY.__bss: 0x1d8
-  - /System/Library/Frameworks/ApplicationServices.framework/Versions/A/ApplicationServices
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/Versions/A/CoreGraphics
   - /System/Library/Frameworks/CoreImage.framework/Versions/A/CoreImage

   - /System/Library/Frameworks/QuartzCore.framework/Versions/A/QuartzCore
   - /System/Library/PrivateFrameworks/CoreUI.framework/Versions/A/CoreUI
   - /System/Library/PrivateFrameworks/IconRendering.framework/Versions/A/IconRendering
-  - /System/Library/PrivateFrameworks/RenderBox.framework/Versions/A/RenderBox
   - /System/Library/PrivateFrameworks/SFSymbols.framework/Versions/A/SFSymbols
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1546
-  Symbols:   3383
-  CStrings:  3054
+  Functions: 1542
+  Symbols:   3374
+  CStrings:  3056
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __DATA.__data : content changed
Symbols:
+ -[IFPlistParser iconDictionaryExists]
+ -[IFPlistParser isIPadOnly]
+ -[IFPlistParser promoteVariants]
+ -[IFPlistParser setIsIPadOnly:]
+ -[IFPlistParser setPromoteVariants:]
+ -[IFPlistParser(IconContentCapture) dictionaryWithPromotedAlternateIconWithName:variants:]
+ OBJC_IVAR_$_IFPlistParser._isIPadOnly
+ OBJC_IVAR_$_IFPlistParser._promoteVariants
+ _objc_msgSend$dictionaryWithPromotedAlternateIconWithName:variants:
+ _objc_msgSend$iconDictionaryExists
+ _objc_msgSend$isIPadOnly
+ _objc_msgSend$promoteVariants
+ _objc_msgSend$removeObjectsForKeys:
+ _objc_msgSend$setPromoteVariants:
- -[IFConcreteImage finalizedIcon]
- -[IFConcreteImage initWithCGImage:scale:finalizedIcon:]
- -[IFConcreteImage setFinalizedIcon:]
- -[IFImage initWithCGImage:scale:finalizedIcon:]
- -[IFPlistParser(IconContentCapture) subDictionaryForAlternateIconName:variants:]
- IFICCIsPPOCompliant
- OBJC_IVAR_$_IFConcreteImage._finalizedIcon
- _OBJC_CLASS_$_ICRFinalizedIcon
- _OBJC_CLASS_$_ICRIconLayer
- _OBJC_CLASS_$_RBDevice
- _objc_msgSend$finalizedIcon
- _objc_msgSend$initFromSerializedData:device:error:
- _objc_msgSend$initWithCGImage:scale:finalizedIcon:
- _objc_msgSend$initWithFinalizedIcon:
- _objc_msgSend$instancesRespondToSelector:
- _objc_msgSend$serializedDataWithError:
- _objc_msgSend$setFinalizedIcon:
- _objc_msgSend$sharedDefaultDevice
- _objc_msgSend$subDictionaryForAlternateIconName:variants:
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.e9BJyl/Sources/CoreUI/Bom/Common/BOMStack.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.e9BJyl/Sources/CoreUI/Bom/Storage/BOMStorage.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.e9BJyl/Sources/CoreUI/Bom/Storage/BOMStream.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.e9BJyl/Sources/CoreUI/Bom/Storage/BOMTree.c"
+ "B"
+ "Failed to extract Info.plist icon keys for %@"
+ "No catalog asset specified in Info.plist for %@"
+ "No such asset with name %@ in bundle: %@"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.nDfmlM/Sources/CoreUI/Bom/Common/BOMStack.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.nDfmlM/Sources/CoreUI/Bom/Storage/BOMStorage.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.nDfmlM/Sources/CoreUI/Bom/Storage/BOMStream.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.nDfmlM/Sources/CoreUI/Bom/Storage/BOMTree.c"
- "C"
- "Failed to create ICRIconLayer from finalized icon %@"
- "Failed to create finalized icon from serialized data. Error: %@"
- "Failed to serialize finalized icon. Error: %@"
- "No catalog asset specified in Info.plist"

```
