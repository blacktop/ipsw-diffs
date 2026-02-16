## TextInput_chr

> `/System/Library/TextInput/TextInput_chr.bundle/TextInput_chr`

```diff

-3532.3.2.3.0
-  __TEXT.__text: 0xbf8
-  __TEXT.__auth_stubs: 0x170
+3532.4.3.0.0
+  __TEXT.__text: 0xc3c
+  __TEXT.__auth_stubs: 0x160
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0x68
   __TEXT.__const: 0xa8

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xd0
   __DATA_CONST.__objc_arraydata: 0x30
-  __AUTH_CONST.__auth_got: 0xc0
+  __AUTH_CONST.__auth_got: 0xb8
   __AUTH_CONST.__cfstring: 0xe0
   __AUTH_CONST.__objc_const: 0x90
   __AUTH_CONST.__objc_arrayobj: 0x18

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3C3E018E-B60F-3784-82E2-C8975111DCA5
+  UUID: 24EBF21F-A497-3517-921D-DD98C02C9AC8
   Functions: 10
-  Symbols:   82
+  Symbols:   81
   CStrings:  39
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x2
Functions:
~ -[TIKeyboardInputManager_chr initImplementation] : 172 -> 180
~ +[TIKeyboardInputManager_chr stringByComposingInput:] : 764 -> 772
~ -[TIKeyboardInputManager_chr internalStringToExternal:] : 108 -> 116
~ -[TIKeyboardInputManager_chr externalStringToInternal:] : 956 -> 960
~ -[TIKeyboardInputManager_chr contextualDisplayKeys] : 576 -> 616

```
