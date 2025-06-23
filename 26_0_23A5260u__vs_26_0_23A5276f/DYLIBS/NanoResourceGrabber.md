## NanoResourceGrabber

> `/System/Library/PrivateFrameworks/NanoResourceGrabber.framework/NanoResourceGrabber`

```diff

-110.0.0.0.0
-  __TEXT.__text: 0x3cb4
-  __TEXT.__auth_stubs: 0x3c0
-  __TEXT.__objc_methlist: 0x35c
+111.0.0.0.0
+  __TEXT.__text: 0x3d08
+  __TEXT.__auth_stubs: 0x390
+  __TEXT.__objc_methlist: 0x36c
   __TEXT.__const: 0x40
-  __TEXT.__oslogstring: 0x6d5
+  __TEXT.__oslogstring: 0x6b2
   __TEXT.__cstring: 0x41a
   __TEXT.__gcc_except_tab: 0x68
-  __TEXT.__unwind_info: 0x188
+  __TEXT.__unwind_info: 0x190
   __TEXT.__objc_classname: 0x5c
-  __TEXT.__objc_methname: 0xc6e
-  __TEXT.__objc_methtype: 0x2bd
-  __TEXT.__objc_stubs: 0x960
-  __DATA_CONST.__got: 0xd8
+  __TEXT.__objc_methname: 0xcfe
+  __TEXT.__objc_methtype: 0x2d2
+  __TEXT.__objc_stubs: 0xa20
+  __DATA_CONST.__got: 0xe8
   __DATA_CONST.__const: 0x248
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x380
+  __DATA_CONST.__objc_selrefs: 0x3b0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x1f0
+  __AUTH_CONST.__auth_got: 0x1d8
   __AUTH_CONST.__const: 0xc0
   __AUTH_CONST.__cfstring: 0x340
   __AUTH_CONST.__objc_const: 0x3d0

   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/AppConduit.framework/AppConduit
   - /System/Library/PrivateFrameworks/DiagnosticLogCollection.framework/DiagnosticLogCollection
+  - /System/Library/PrivateFrameworks/IconServices.framework/IconServices
   - /System/Library/PrivateFrameworks/MobileIcons.framework/MobileIcons
   - /System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 81F173DD-C5A6-311F-A59E-C74148665005
-  Functions: 99
-  Symbols:   434
-  CStrings:  270
+  UUID: 7AA74272-EFF6-39DF-AF82-1F25C794E5C6
+  Functions: 100
+  Symbols:   441
+  CStrings:  276
 
Symbols:
+ +[NanoResourceGrabber _iconVariant:fromBundleID:]
+ +[NanoResourceGrabber _sizeForVariant:]
+ _OBJC_CLASS_$_ISIcon
+ _OBJC_CLASS_$_ISImageDescriptor
+ _OBJC_CLASS_$_LSApplicationProxy
+ ___54-[NanoResourceGrabber getAppViewListImage:completion:]_block_invoke.80
+ ___54-[NanoResourceGrabber getAppViewListImage:completion:]_block_invoke.80.cold.1
+ _objc_msgSend$CGImageForDescriptor:
+ _objc_msgSend$_iconVariant:fromBundleID:
+ _objc_msgSend$_sizeForVariant:
+ _objc_msgSend$applicationProxyForIdentifier:
+ _objc_msgSend$initWithCGImage:scale:orientation:
+ _objc_msgSend$initWithResourceProxy:
+ _objc_msgSend$initWithSize:scale:
+ _objc_msgSend$prepareImageForDescriptor:
- +[NanoResourceGrabber _iconVariant:fromURL:]
- _CFRelease
- _LICreateIconForBundleAndDisplayGamut
- __CFBundleCreateUnique
- ___54-[NanoResourceGrabber getAppViewListImage:completion:]_block_invoke.77
- ___54-[NanoResourceGrabber getAppViewListImage:completion:]_block_invoke.77.cold.1
- _kCFAllocatorDefault
- _objc_msgSend$_iconVariant:fromURL:
- _objc_msgSend$imageWithCGImage:scale:orientation:
CStrings:
+ "CGImageForDescriptor:"
+ "_iconVariant:fromBundleID:"
+ "_sizeForVariant:"
+ "applicationProxyForIdentifier:"
+ "initWithCGImage:scale:orientation:"
+ "initWithResourceProxy:"
+ "initWithSize:scale:"
+ "prepareImageForDescriptor:"
+ "{CGSize=dd}20@0:8i16"
- "LICreateIconForBundle returned nil"
- "_iconVariant:fromURL:"
- "imageWithCGImage:scale:orientation:"

```
