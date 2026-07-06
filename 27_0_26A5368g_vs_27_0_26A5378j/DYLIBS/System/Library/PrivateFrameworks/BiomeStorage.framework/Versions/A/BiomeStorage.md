## BiomeStorage

> `/System/Library/PrivateFrameworks/BiomeStorage.framework/Versions/A/BiomeStorage`

```diff

-  __TEXT.__text: 0x2b8d8
+  __TEXT.__text: 0x2b8f0
   __TEXT.__objc_methlist: 0x2094
   __TEXT.__const: 0x1e8
-  __TEXT.__cstring: 0x174c
+  __TEXT.__cstring: 0x178b
   __TEXT.__oslogstring: 0x43f2
   __TEXT.__gcc_except_tab: 0x90c
   __TEXT.__dlopen_cstrs: 0xac

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x1350
   __DATA_CONST.__objc_protorefs: 0x10
+  __DATA_CONST.__objc_classrefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xc0
   __DATA_CONST.__got: 0x238
   __AUTH_CONST.__const: 0x660
-  __AUTH_CONST.__cfstring: 0x1540
+  __AUTH_CONST.__cfstring: 0x1560
   __AUTH_CONST.__objc_const: 0x4cf8
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x1e0

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
   Functions: 1031
-  Symbols:   2409
-  CStrings:  610
+  Symbols:   2410
+  CStrings:  612
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__const : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__got : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH.__objc_data : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
Symbols:
+ _OBJC_CLASS_$_NSMutableData
Functions:
~ -[BMStreamDatastore enumerateEventsFrom:to:options:usingBlock:] : 284 -> 320
~ -[BMFrameStore(V2) isValidFrameV2:currentFrame:expectedState:copyOfData:frameState:frameSize:validations:enumerationOptions:errorCode:] : 1960 -> 2128
~ -[BMFrameStore(V2) enumerateWithOptionsV2:fromOffset:usingBlock:] : 5520 -> 5340
CStrings:
+ "isValidFrameV2: Frame size:%d smaller than BMFrameHeaderV2:%zu"

```
