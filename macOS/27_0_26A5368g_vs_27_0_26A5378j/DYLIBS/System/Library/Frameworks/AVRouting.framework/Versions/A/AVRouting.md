## AVRouting

> `/System/Library/Frameworks/AVRouting.framework/Versions/A/AVRouting`

```diff

-  __TEXT.__text: 0x5bda4
+  __TEXT.__text: 0x5bf30
   __TEXT.__objc_methlist: 0x6278
   __TEXT.__const: 0x110
-  __TEXT.__cstring: 0xdfc9
-  __TEXT.__oslogstring: 0xb348
+  __TEXT.__cstring: 0xe01c
+  __TEXT.__oslogstring: 0xb3aa
   __TEXT.__gcc_except_tab: 0x5b8
-  __TEXT.__unwind_info: 0x1660
+  __TEXT.__unwind_info: 0x1668
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0x370
   __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1dc8
+  __DATA_CONST.__objc_selrefs: 0x1dd0
   __DATA_CONST.__objc_superrefs: 0x2c8
-  __DATA_CONST.__got: 0xfa8
+  __DATA_CONST.__got: 0xfd8
   __AUTH_CONST.__const: 0xe50
-  __AUTH_CONST.__cfstring: 0x4320
+  __AUTH_CONST.__cfstring: 0x4340
   __AUTH_CONST.__objc_const: 0xb6a8
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x1090
+  __AUTH.__objc_data: 0x1220
   __DATA.__objc_ivar: 0x538
   __DATA.__data: 0xb70
   __DATA.__bss: 0x88
   __DATA.__common: 0x90
-  __DATA_DIRTY.__objc_data: 0x11d0
+  __DATA_DIRTY.__objc_data: 0x1040
   __DATA_DIRTY.__common: 0x160
   __DATA_DIRTY.__bss: 0xc8
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/Versions/A/CoreGraphics
   - /System/Library/Frameworks/CoreMedia.framework/Versions/A/CoreMedia
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
-  - /System/Library/Frameworks/MediaToolbox.framework/Versions/A/MediaToolbox
   - /System/Library/Frameworks/Security.framework/Versions/A/Security
   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/Versions/A/UniformTypeIdentifiers
   - /System/Library/PrivateFrameworks/CoreUtils.framework/Versions/A/CoreUtils

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 2490
-  Symbols:   5885
-  CStrings:  2094
+  Symbols:   5889
+  CStrings:  2098
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __DATA.__data : content changed
Symbols:
+ _OBJC_CLASS_$_NSKeyedUnarchiver
+ _OBJC_CLASS_$_UTTypeCodingBox
+ _objc_msgSend$type
+ _objc_msgSend$unarchivedObjectOfClass:fromData:error:
Functions:
~ -[AVFigRouteDescriptorOutputDeviceImpl protocolTypeIdentifier] : 80 -> 476
CStrings:
+ "-[AVFigRouteDescriptorOutputDeviceImpl protocolTypeIdentifier]"
+ "<<<< AVOutputDevice (FigRouteDescriptor) >>>> %s: Failed to unarchive UTTypeCodingBox: %{public}@"
+ "ProtocolTypeArchive"

```
