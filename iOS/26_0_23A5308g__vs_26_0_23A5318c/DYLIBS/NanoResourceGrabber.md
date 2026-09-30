## NanoResourceGrabber

> `/System/Library/PrivateFrameworks/NanoResourceGrabber.framework/NanoResourceGrabber`

```diff

-112.0.0.0.0
-  __TEXT.__text: 0x43e4
-  __TEXT.__auth_stubs: 0x3c0
+113.0.0.0.0
+  __TEXT.__text: 0x43bc
+  __TEXT.__auth_stubs: 0x3f0
   __TEXT.__objc_methlist: 0x36c
   __TEXT.__const: 0x40
-  __TEXT.__oslogstring: 0x773
+  __TEXT.__oslogstring: 0x796
   __TEXT.__cstring: 0x43e
   __TEXT.__gcc_except_tab: 0x100
-  __TEXT.__unwind_info: 0x1b8
+  __TEXT.__unwind_info: 0x1b0
   __TEXT.__objc_classname: 0x5c
-  __TEXT.__objc_methname: 0xd76
+  __TEXT.__objc_methname: 0xcf7
   __TEXT.__objc_methtype: 0x2d2
-  __TEXT.__objc_stubs: 0xa80
-  __DATA_CONST.__got: 0x100
+  __TEXT.__objc_stubs: 0x9c0
+  __DATA_CONST.__got: 0xf0
   __DATA_CONST.__const: 0x298
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3c8
+  __DATA_CONST.__objc_selrefs: 0x3a0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x1f0
+  __AUTH_CONST.__auth_got: 0x208
   __AUTH_CONST.__const: 0xc0
   __AUTH_CONST.__cfstring: 0x360
   __AUTH_CONST.__objc_const: 0x3d0

   - /System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 37EA8A2B-3AC3-3F35-A907-D7ABC3D49631
+  UUID: 0840E64B-9BDF-3231-BE69-82F1C9147D60
   Functions: 109
-  Symbols:   469
-  CStrings:  287
+  Symbols:   464
+  CStrings:  283
 
Symbols:
+ +[NanoResourceGrabber _iconVariant:fromURL:]
+ _CFRelease
+ _LICreateIconForBundleAndDisplayGamut
+ __CFBundleCreateUnique
+ ___54-[NanoResourceGrabber getAppViewListImage:completion:]_block_invoke.77
+ ___54-[NanoResourceGrabber getAppViewListImage:completion:]_block_invoke.77.cold.1
+ _kCFAllocatorDefault
+ _objc_msgSend$_iconVariant:fromURL:
+ _objc_msgSend$imageWithCGImage:scale:orientation:
- +[NanoResourceGrabber _iconVariant:fromBundleID:]
- _OBJC_CLASS_$_ISIcon
- _OBJC_CLASS_$_ISImageDescriptor
- _OBJC_CLASS_$_LSApplicationProxy
- ___54-[NanoResourceGrabber getAppViewListImage:completion:]_block_invoke.80
- ___54-[NanoResourceGrabber getAppViewListImage:completion:]_block_invoke.80.cold.1
- _objc_msgSend$CGImageForDescriptor:
- _objc_msgSend$_iconVariant:fromBundleID:
- _objc_msgSend$_sizeForVariant:
- _objc_msgSend$applicationProxyForIdentifier:
- _objc_msgSend$initWithCGImage:scale:orientation:
- _objc_msgSend$initWithResourceProxy:
- _objc_msgSend$initWithSize:scale:
- _objc_msgSend$prepareImageForDescriptor:
Functions:
~ +[NanoResourceGrabber _iconVariant:fromBundleID:] -> +[NanoResourceGrabber _iconVariant:fromURL:] : 308 -> 268
CStrings:
+ "LICreateIconForBundle returned nil"
+ "_iconVariant:fromURL:"
+ "imageWithCGImage:scale:orientation:"
- "CGImageForDescriptor:"
- "_iconVariant:fromBundleID:"
- "applicationProxyForIdentifier:"
- "initWithCGImage:scale:orientation:"
- "initWithResourceProxy:"
- "initWithSize:scale:"
- "prepareImageForDescriptor:"

```
