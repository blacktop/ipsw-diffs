## TextInputCore

> `/System/Library/PrivateFrameworks/TextInputCore.framework/TextInputCore`

```diff

-3511.100.0.0.0
-  __TEXT.__text: 0x21ba7c
+3515.0.0.0.0
+  __TEXT.__text: 0x21bb60
   __TEXT.__auth_stubs: 0x35d0
   __TEXT.__init_offsets: 0xbc
   __TEXT.__objc_methlist: 0x10620

   __TEXT.__cstring: 0x199a4
   __TEXT.__oslogstring: 0x4073
   __TEXT.__ustring: 0x3ca
-  __TEXT.__unwind_info: 0x6418
+  __TEXT.__unwind_info: 0x6410
   __TEXT.__objc_classname: 0x221f
-  __TEXT.__objc_methname: 0x30654
+  __TEXT.__objc_methname: 0x3067a
   __TEXT.__objc_methtype: 0x66df
-  __TEXT.__objc_stubs: 0x219c0
+  __TEXT.__objc_stubs: 0x21a00
   __DATA_CONST.__got: 0x1740
   __DATA_CONST.__const: 0x4e00
   __DATA_CONST.__objc_classlist: 0x830
   __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_protolist: 0x190
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9d00
+  __DATA_CONST.__objc_selrefs: 0x9d10
   __DATA_CONST.__objc_superrefs: 0x708
   __DATA_CONST.__objc_arraydata: 0xcb0
   __AUTH_CONST.__auth_got: 0x1af0

   - /usr/lib/libmecabra.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: C65E8107-89B0-3BA1-B716-E057E28A5EC8
+  UUID: F193DC61-C036-3B4D-BC68-16E2756D1CAC
   Functions: 10286
-  Symbols:   30956
-  CStrings:  14170
+  Symbols:   30958
+  CStrings:  14172
 
Symbols:
+ _objc_msgSend$delimitingPrefix
+ _objc_msgSend$setDelimitingPrefix:
Functions:
~ -[TIKeyboardInputManagerPolymorph setInputManagerForKeyboardState:withInputEvent:] : 584 -> 596
~ -[TIKeyboardInputManager_mul shouldPassAlternativeInputAsPrediction:isRecognized:] : 560 -> 672
~ -[TIKeyboardInputManager_mul handleKeyboardInput:] : 1752 -> 1796
~ -[TIKeyboardInputManager addInput:withContext:] : 1724 -> 1748
~ -[TIKeyboardInputManager shouldOmitEmojiCandidates] : 100 -> 108
~ __ZN2TI8Favonius26FavoniusStrokeBuildManager17delete_from_inputEv : 240 -> 252
~ __ZN2TI8Favonius26FavoniusStrokeBuildManager19InputTouchAlignment17delete_from_inputEv : 92 -> 108
CStrings:
+ "delimitingPrefix"
+ "setDelimitingPrefix:"

```
