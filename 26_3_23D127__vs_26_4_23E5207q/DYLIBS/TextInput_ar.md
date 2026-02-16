## TextInput_ar

> `/System/Library/TextInput/TextInput_ar.bundle/TextInput_ar`

```diff

-3532.3.2.3.0
-  __TEXT.__text: 0xe14
-  __TEXT.__auth_stubs: 0x1e0
+3532.4.3.0.0
+  __TEXT.__text: 0xec8
+  __TEXT.__auth_stubs: 0x1b0
   __TEXT.__init_offsets: 0x8
   __TEXT.__objc_methlist: 0xc0
   __TEXT.__const: 0x8

   __DATA_CONST.__objc_selrefs: 0x140
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__objc_arraydata: 0x3d0
-  __AUTH_CONST.__auth_got: 0xf8
+  __AUTH_CONST.__auth_got: 0xe0
   __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__cfstring: 0x8c0
   __AUTH_CONST.__objc_const: 0x120

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A96FFC6D-B2A9-35CF-8825-7CF3E35B801C
+  UUID: 6CCF7175-20C3-3C5A-B549-228C072E48AC
   Functions: 22
-  Symbols:   148
+  Symbols:   145
   CStrings:  157
 
Symbols:
+ _objc_release_x25
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x20
- _objc_claimAutoreleasedReturnValue
- _objc_release_x26
- _objc_release_x28
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x2
- _objc_retain_x28
Functions:
~ -[TIKeyboardInputManager_ar isUsingMultilingual] : 204 -> 216
~ +[TIKeyboardInputManager_ar generateKeyLayoutMapReverse] : 280 -> 284
~ +[TIKeyboardInputManager_ar generateKeyLayoutMapReverseV2] : 280 -> 284
~ +[TIKeyboardInputManagerTransliteration_ar arabicPrefixes] : 68 -> 84
~ +[TIKeyboardInputManagerTransliteration_ar rtlMarkExcludedClientIdentifiers] : 68 -> 84
~ -[TIKeyboardInputManagerTransliteration_ar shouldExcludeRtlMarkHandling] : 116 -> 128
~ -[TIKeyboardInputManagerTransliteration_ar addInput:withContext:] : 172 -> 168
~ -[TIKeyboardInputManagerTransliteration_ar addRtlMark:] : 240 -> 272
~ -[TIKeyboardInputManagerTransliteration_ar removeRtlMark:] : 656 -> 720
~ -[TIKeyboardInputManagerTransliteration_ar handleSpaceDeletionWithContext:] : 864 -> 888

```
