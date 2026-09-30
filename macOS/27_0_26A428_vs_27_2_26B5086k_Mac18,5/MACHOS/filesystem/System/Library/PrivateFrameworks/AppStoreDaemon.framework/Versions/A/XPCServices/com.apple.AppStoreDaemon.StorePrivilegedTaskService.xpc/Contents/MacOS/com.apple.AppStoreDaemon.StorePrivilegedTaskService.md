## com.apple.AppStoreDaemon.StorePrivilegedTaskService

> `/System/Library/PrivateFrameworks/AppStoreDaemon.framework/Versions/A/XPCServices/com.apple.AppStoreDaemon.StorePrivilegedTaskService.xpc/Contents/MacOS/com.apple.AppStoreDaemon.StorePrivilegedTaskService`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-13.0.52.1.2
-  __TEXT.__text: 0x3804
-  __TEXT.__auth_stubs: 0x2e0
-  __TEXT.__objc_stubs: 0x7a0
-  __TEXT.__objc_methlist: 0x22c
-  __TEXT.__const: 0x48
-  __TEXT.__cstring: 0x350
-  __TEXT.__oslogstring: 0x59e
-  __TEXT.__gcc_except_tab: 0x34
-  __TEXT.__objc_methname: 0x95b
+13.1.12.0.0
+  __TEXT.__text: 0x42c8
+  __TEXT.__auth_stubs: 0x380
+  __TEXT.__objc_stubs: 0x8c0
+  __TEXT.__objc_methlist: 0x248
+  __TEXT.__const: 0x58
+  __TEXT.__cstring: 0x360
+  __TEXT.__oslogstring: 0x682
+  __TEXT.__gcc_except_tab: 0x4c
+  __TEXT.__objc_methname: 0xa51
   __TEXT.__objc_classname: 0x57
-  __TEXT.__objc_methtype: 0x2cb
-  __TEXT.__unwind_info: 0x120
-  __DATA_CONST.__const: 0x1b0
+  __TEXT.__objc_methtype: 0x31a
+  __TEXT.__unwind_info: 0x160
+  __DATA_CONST.__const: 0x240
   __DATA_CONST.__cfstring: 0x200
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x18

   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_intobj: 0x48
-  __DATA_CONST.__auth_got: 0x180
-  __DATA_CONST.__got: 0x100
-  __DATA.__objc_const: 0x2a8
-  __DATA.__objc_selrefs: 0x2e8
+  __DATA_CONST.__auth_got: 0x1d0
+  __DATA_CONST.__got: 0x128
+  __DATA.__objc_const: 0x2b0
+  __DATA.__objc_selrefs: 0x338
   __DATA.__objc_ivar: 0x8
   __DATA.__objc_data: 0x50
   __DATA.__data: 0x120
   __DATA.__common: 0x160
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
+  - /System/Library/Frameworks/CoreGraphics.framework/Versions/A/CoreGraphics
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
+  - /System/Library/PrivateFrameworks/IconServices.framework/Versions/A/IconServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 43
-  Symbols:   92
-  CStrings:  228
+  Functions: 54
+  Symbols:   107
+  CStrings:  243
 
Symbols:
+ _CGContextDrawImage
+ _CGContextGetCTM
+ _CGDataProviderCreateWithCFData
+ _CGDataProviderRelease
+ _CGImageCreateWithJPEGDataProvider
+ _CGImageCreateWithPNGDataProvider
+ _CGImageGetHeight
+ _CGImageGetWidth
+ _CGImageRelease
+ _OBJC_CLASS_$_IFImage
+ _OBJC_CLASS_$_ISIcon
+ _OBJC_CLASS_$_ISImageDescriptor
+ _OBJC_CLASS_$_NSArray
+ _OBJC_CLASS_$_NSGraphicsContext
+ __Block_object_dispose
CStrings:
+ "CGContext"
+ "CGImageForDescriptor:"
+ "Could not decode unprocessed artwork as JPEG or PNG, falling back to raw data"
+ "IconServices returned no image for descriptor at size %.0f"
+ "Placeholder creation with artwork processing requested with name %{public}@ for %{public}@"
+ "arrayWithObjects:count:"
+ "createPlaceholderFromUnprocessedArtwork:name:metadata:withReplyHandler:"
+ "currentContext"
+ "initWithCGImage:scale:"
+ "initWithImages:"
+ "initWithSize:scale:"
+ "prepareImagesForImageDescriptors:"
+ "setShape:"
+ "v16@?0@\"NSURL\"8"
+ "v48@0:8@\"NSData\"16@\"NSString\"24@\"NSDictionary\"32@?<v@?@\"NSError\"@\"NSString\">40"
```
