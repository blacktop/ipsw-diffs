## PosterUIFoundation

> `/System/Library/PrivateFrameworks/PosterUIFoundation.framework/PosterUIFoundation`

```diff

-304.2.6.100.0
-  __TEXT.__text: 0x925e8
-  __TEXT.__auth_stubs: 0x1c90
-  __TEXT.__objc_methlist: 0xa95c
-  __TEXT.__const: 0xc04
-  __TEXT.__oslogstring: 0x3711
+304.3.3.0.0
+  __TEXT.__text: 0x92a9c
+  __TEXT.__auth_stubs: 0x1ca0
+  __TEXT.__objc_methlist: 0xa98c
+  __TEXT.__const: 0xc24
+  __TEXT.__oslogstring: 0x3721
   __TEXT.__cstring: 0x6122
   __TEXT.__gcc_except_tab: 0x165c
   __TEXT.__dlopen_cstrs: 0x1a8

   __TEXT.__swift5_proto: 0x24
   __TEXT.__swift5_types: 0x24
   __TEXT.__swift5_capture: 0x10
-  __TEXT.__unwind_info: 0x2760
+  __TEXT.__unwind_info: 0x2768
   __TEXT.__objc_classname: 0x1853
-  __TEXT.__objc_methname: 0x193ff
-  __TEXT.__objc_methtype: 0x3e97
-  __TEXT.__objc_stubs: 0x116e0
-  __DATA_CONST.__got: 0xe70
+  __TEXT.__objc_methname: 0x1945a
+  __TEXT.__objc_methtype: 0x3eb3
+  __TEXT.__objc_stubs: 0x11700
+  __DATA_CONST.__got: 0xe90
   __DATA_CONST.__const: 0x2640
   __DATA_CONST.__objc_classlist: 0x4f8
   __DATA_CONST.__objc_catlist: 0xc0
   __DATA_CONST.__objc_protolist: 0x1c0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5848
+  __DATA_CONST.__objc_selrefs: 0x5868
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x410
   __DATA_CONST.__objc_arraydata: 0x1b0
-  __AUTH_CONST.__auth_got: 0xe58
+  __AUTH_CONST.__auth_got: 0xe60
   __AUTH_CONST.__const: 0xf80
   __AUTH_CONST.__cfstring: 0x7140
-  __AUTH_CONST.__objc_const: 0x1eb98
+  __AUTH_CONST.__objc_const: 0x1eba8
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_intobj: 0x318
   __AUTH_CONST.__objc_doubleobj: 0x2b0
   __AUTH_CONST.__objc_arrayobj: 0xa8
+  __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH.__objc_data: 0x2410
   __AUTH.__data: 0x110
   __DATA.__objc_ivar: 0xbd8

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 02003079-3292-3207-8702-0F4E97C741AC
-  Functions: 3956
-  Symbols:   14205
-  CStrings:  7021
+  UUID: D56D2E56-B7BD-39B7-BD37-F2209A50EB5A
+  Functions: 3962
+  Symbols:   14222
+  CStrings:  7026
 
Symbols:
+ +[PUIImageOnDiskFormat jpg]
+ +[PUIPosterSnapshotBundlePredicate predicateMatchingSnapshotDefinition:]
+ -[PUIImageEncoder readImageOrientation]
+ -[PUIImageEncoder saveImage:orientation:error:]
+ -[PUIImageEncoder saveImage:orientation:error:].cold.1
+ _CGImagePropertyOrientationForUIImageOrientation
+ _CGImageSourceCopyPropertiesAtIndex
+ _OBJC_CLASS_$_NSConstantFloatNumber
+ _UIImageOrientationForCGImagePropertyOrientation
+ _UTTypeJPEG
+ _kCGImageDestinationLossyCompressionQuality
+ _kCGImagePropertyJPEGDictionary
+ _kCGImagePropertyOrientation
+ _objc_msgSend$readImageOrientation
+ _objc_msgSend$saveImage:orientation:error:
- -[PUIImageEncoder saveImage:error:].cold.1
- _objc_msgSend$saveImage:error:
CStrings:
+ "-[PUIImageEncoder saveImage:orientation:error:]"
+ "@40@0:8^{CGImage=}16q24^@32"
+ "jpg"
+ "predicateMatchingSnapshotDefinition:"
+ "readImageOrientation"
+ "saveImage:orientation:error:"
- "-[PUIImageEncoder saveImage:error:]"

```
