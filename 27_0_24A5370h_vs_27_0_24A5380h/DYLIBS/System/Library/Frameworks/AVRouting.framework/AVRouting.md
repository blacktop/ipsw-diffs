## AVRouting

> `/System/Library/Frameworks/AVRouting.framework/AVRouting`

```diff

-  __TEXT.__text: 0x63d50
+  __TEXT.__text: 0x63edc
   __TEXT.__objc_methlist: 0x6728
   __TEXT.__const: 0x10c
   __TEXT.__gcc_except_tab: 0x6c4
-  __TEXT.__cstring: 0xecfe
-  __TEXT.__oslogstring: 0xc927
+  __TEXT.__cstring: 0xed51
+  __TEXT.__oslogstring: 0xc989
   __TEXT.__dlopen_cstrs: 0x56
-  __TEXT.__unwind_info: 0x1898
+  __TEXT.__unwind_info: 0x18a0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0x3b8
   __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2000
+  __DATA_CONST.__objc_selrefs: 0x2008
   __DATA_CONST.__objc_superrefs: 0x2f8
-  __DATA_CONST.__got: 0x10d8
+  __DATA_CONST.__got: 0x1108
   __AUTH_CONST.__const: 0x410
-  __AUTH_CONST.__cfstring: 0x4640
+  __AUTH_CONST.__cfstring: 0x4660
   __AUTH_CONST.__objc_const: 0xc100
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x1720
+  __AUTH.__objc_data: 0x1810
   __DATA.__objc_ivar: 0x5a0
   __DATA.__data: 0xb70
   __DATA.__bss: 0xd8
   __DATA.__common: 0x100
-  __DATA_DIRTY.__objc_data: 0xe10
+  __DATA_DIRTY.__objc_data: 0xd20
   __DATA_DIRTY.__common: 0x110
   __DATA_DIRTY.__bss: 0xb0
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 2572
-  Symbols:   9036
-  CStrings:  2267
+  Symbols:   9040
+  CStrings:  2271
 
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
