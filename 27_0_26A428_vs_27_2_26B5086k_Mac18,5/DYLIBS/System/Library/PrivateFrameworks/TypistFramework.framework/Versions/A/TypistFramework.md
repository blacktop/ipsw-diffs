## TypistFramework

> `/System/Library/PrivateFrameworks/TypistFramework.framework/Versions/A/TypistFramework`

### Sections with Same Size but Changed Content

- `__TEXT.__ustring`

```diff

-493.0.0.0.0
-  __TEXT.__text: 0x11830
-  __TEXT.__objc_methlist: 0x1404
-  __TEXT.__const: 0x1c2
-  __TEXT.__gcc_except_tab: 0x1fc
-  __TEXT.__cstring: 0x2a72
+498.0.0.0.0
+  __TEXT.__text: 0x11c6c
+  __TEXT.__objc_methlist: 0x1454
+  __TEXT.__const: 0x212
   __TEXT.__ustring: 0xa18
+  __TEXT.__cstring: 0x2a72
+  __TEXT.__gcc_except_tab: 0x1fc
   __TEXT.__oslogstring: 0xc
   __TEXT.__swift5_typeref: 0xaa
   __TEXT.__constg_swiftt: 0xb0

   __TEXT.__swift5_fieldmd: 0x94
   __TEXT.__swift5_proto: 0x4
   __TEXT.__swift5_types: 0x10
-  __TEXT.__unwind_info: 0x560
+  __TEXT.__unwind_info: 0x568
   __TEXT.__eh_frame: 0x48
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xe98
+  __DATA_CONST.__objc_selrefs: 0xec8
   __DATA_CONST.__objc_classrefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x50
   __DATA_CONST.__objc_arraydata: 0x1fa0

   __AUTH_CONST.__const: 0x788
   __AUTH_CONST.__cfstring: 0x9b80
   __AUTH_CONST.__objc_const: 0x2250
-  __AUTH_CONST.__objc_doubleobj: 0x50
   __AUTH_CONST.__objc_intobj: 0x1308
-  __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x48
-  __AUTH_CONST.__auth_got: 0x410
+  __AUTH_CONST.__objc_dictobj: 0x78
+  __AUTH_CONST.__objc_doubleobj: 0x50
+  __AUTH_CONST.__auth_got: 0x428
   __AUTH.__objc_data: 0x548
   __AUTH.__data: 0x28
   __DATA.__objc_ivar: 0x138

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 505
-  Symbols:   1253
+  Functions: 512
+  Symbols:   1266
   CStrings:  1270
 
Symbols:
+ +[TypistKeyboardUtilities(MathUtilities) _clampedThumbLengthCM:]
+ +[TypistKeyboardUtilities(MathUtilities) generatePerimeterPointWithCenter:bounds:offset:]
+ +[TypistKeyboardUtilities(MathUtilities) generateThumbReachPointForKeyCenter:reference:errorScale:millimetresPerPoint:]
+ +[TypistKeyboardUtilities(MathUtilities) thumbBaseSigmaMMForLengthCM:]
+ +[TypistKeyboardUtilities(MathUtilities) thumbReachRadiusMMForLengthCM:]
+ +[TypistKeyboardUtilities(MathUtilities) thumbReachReferenceForLengthCM:anchor:isRightThumb:]
+ +[TypistKeyboardUtilities(MathUtilities) validateTouchPoint:withinBounds:]
+ -[TypistHWKeyboard senderProperties]
+ -[TypistHWKeyboard setSenderProperties:]
+ OBJC_IVAR_$_TypistHWKeyboard._senderProperties
+ __OBJC_$_CATEGORY_CLASS_METHODS_NSString_$_ArabicFormConverter
+ __OBJC_$_CATEGORY_NSCharacterSet_$_Arabic
+ __OBJC_$_CATEGORY_NSString_$_ArabicFormConverter
+ __OBJC_$_CLASS_METHODS_NSCharacterSet(Arabic|Cursive|Hangul|Latex)
+ __OBJC_$_CLASS_METHODS_TypistKeyboardUtilities(KeyboardSettings|MathUtilities|RecapUtilities)
+ __OBJC_$_INSTANCE_METHODS_NSString(ArabicFormConverter|TYTextDirectionAnnotations|Grapheme)
+ _atan2
+ _hypot
+ _objc_msgSend$_clampedThumbLengthCM:
+ _objc_msgSend$generateGaussianPointWithMean:andSigma:
+ _objc_msgSend$senderProperties
+ _objc_msgSend$thumbBaseSigmaMMForLengthCM:
+ _objc_msgSend$thumbReachRadiusMMForLengthCM:
+ _sin
- -[TypistHWKeyboard propertyDictionary]
- -[TypistHWKeyboard setPropertyDictionary:]
- OBJC_IVAR_$_TypistHWKeyboard._propertyDictionary
- __OBJC_$_CATEGORY_NSCharacterSet_$_Cursive
- __OBJC_$_CATEGORY_NSString_$_TYTextDirectionAnnotations
- __OBJC_$_CLASS_METHODS_NSCharacterSet(Cursive|Arabic|Latex|Hangul)
- __OBJC_$_CLASS_METHODS_NSString(TYTextDirectionAnnotations|Grapheme|ArabicFormConverter)
- __OBJC_$_CLASS_METHODS_TypistKeyboardUtilities(MathUtilities|RecapUtilities|KeyboardSettings)
- __OBJC_$_INSTANCE_METHODS_NSString(TYTextDirectionAnnotations|Grapheme|ArabicFormConverter)
- _objc_msgSend$propertyDictionary
- _objc_msgSend$setPropertyDictionary:
```
