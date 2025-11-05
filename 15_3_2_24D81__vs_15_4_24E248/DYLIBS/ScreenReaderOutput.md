## ScreenReaderOutput

> `/System/Library/PrivateFrameworks/ScreenReader.framework/Versions/A/Frameworks/ScreenReaderOutput.framework/Versions/A/ScreenReaderOutput`

```diff

-964.9.2.0.0
-  __TEXT.__text: 0x496d8
+964.12.7.1.0
+  __TEXT.__text: 0x49ba0
   __TEXT.__auth_stubs: 0xd60
-  __TEXT.__objc_methlist: 0x457c
-  __TEXT.__cstring: 0x3ff6
-  __TEXT.__gcc_except_tab: 0x173c
-  __TEXT.__const: 0x2a8
+  __TEXT.__objc_methlist: 0x4f1c
+  __TEXT.__cstring: 0x403a
+  __TEXT.__gcc_except_tab: 0x1744
+  __TEXT.__const: 0x2c8
   __TEXT.__oslogstring: 0x14c4
   __TEXT.__ustring: 0xb2
-  __TEXT.__unwind_info: 0x14c0
+  __TEXT.__unwind_info: 0x14e0
   __TEXT.__objc_classname: 0x86e
-  __TEXT.__objc_methname: 0xaff3
+  __TEXT.__objc_methname: 0xb080
   __TEXT.__objc_methtype: 0x1dfa
-  __TEXT.__objc_stubs: 0x90a0
-  __DATA_CONST.__got: 0x460
+  __TEXT.__objc_stubs: 0x9100
+  __DATA_CONST.__got: 0x458
   __DATA_CONST.__const: 0x180
   __DATA_CONST.__objc_classlist: 0x1b8
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0xc8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2ac0
+  __DATA_CONST.__objc_selrefs: 0x2be0
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x178
   __DATA_CONST.__objc_arraydata: 0x278
   __AUTH_CONST.__auth_got: 0x6c0
   __AUTH_CONST.__const: 0xce8
-  __AUTH_CONST.__cfstring: 0x4620
-  __AUTH_CONST.__objc_const: 0xd340
+  __AUTH_CONST.__cfstring: 0x4680
+  __AUTH_CONST.__objc_const: 0xc1f8
   __AUTH_CONST.__objc_intobj: 0x1008
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH.__objc_data: 0x1130
-  __DATA.__objc_ivar: 0x6a0
-  __DATA.__data: 0xc40
+  __DATA.__objc_ivar: 0x6a4
+  __DATA.__data: 0xc48
   __DATA.__common: 0x10
   __DATA.__bss: 0x318
   - /System/Library/Frameworks/ApplicationServices.framework/Versions/A/ApplicationServices

   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 270C48E1-6CDF-3060-8BBD-8762450E1C4C
-  Functions: 1769
-  Symbols:   4780
-  CStrings:  3533
+  UUID: 108FACB3-49D7-3832-AB19-4E67EF8B8C2B
+  Functions: 1790
+  Symbols:   4814
+  CStrings:  3545
 
Symbols:
+ +[SCROBrailleDisplayInputManager sharedManager].cold.1
+ +[SCROBrailleSubstitutionManager sharedInstance].cold.1
+ +[SCROBrailleTranslationManager inputManager].cold.1
+ +[SCROBrailleTranslationManager sharedManager].cold.1
+ +[SCROBrailleTranslationUtility _dotDescriptionForBrailleString:].cold.1
+ +[SCROClient isClientTrustedWithPortToken:].cold.1
+ +[SCROConnection inUnitTests].cold.1
+ +[SCROMobileBrailleDisplayInputManager sharedManager].cold.1
+ +[SCROScriptClient sharedClient].cold.1
+ +[SCROServer sharedServer].cold.1
+ +[SCROVirtualIOElement systemElement].cold.1
+ -[NSString(SCROBrailleAdditions) _illegalCharacterSet].cold.1
+ -[SCRO2DBrailleReadingContent drawOnCanvas:].cold.1
+ -[SCROBrailleDisplayInputManager _commandForHidUsage:].cold.1
+ -[SCROBrailleDisplayInputManager buttonNameForInputIdentifier:forDisplayWithToken:].cold.1
+ -[SCROBrailleDisplayManager _eventQueue_handleSystemVirtualDisplayKeyPress:]
+ -[SCROBrailleFormatter isTokenSecure]
+ -[SCROBrailleFormatter setIsTokenSecure:]
+ -[SCROBrailleTranslationManager loadTranslatorWithServiceIdentifier:input:].cold.1
+ -[SCROCallback initWithCoder:].cold.1
+ -[SCROMobileBrailleDisplayInputManager _commandForHidUsage:].cold.1
+ -[SCROScriptClient runScriptFile:].cold.1
+ -[SCROScriptClient runShortcutWithIdentifier:].cold.1
+ GCC_except_table295
+ GCC_except_table330
+ GCC_except_table384
+ OBJC_IVAR_$_SCROBrailleFormatter._isTokenSecure
+ SCROUnserializeWrapper.cold.1
+ _OUTLINED_FUNCTION_2
+ _SCROD_BRAILLE_LOG.cold.1
+ _SCROD_LOG.cold.1
+ __36-[SCROBrailleLine newLineDescriptor]_block_invoke_2.cold.1
+ __36-[SCROBrailleLine newLineDescriptor]_block_invoke_2.cold.2
+ _kSCROTokenSecureAttribute
+ _objc_msgSend$isTokenSecure
+ _objc_msgSend$setIsShowingSecureToken:
+ _objc_msgSend$setIsTokenSecure:
- GCC_except_table294
- GCC_except_table329
- GCC_except_table383
CStrings:
+ "Global.findText"
+ "SCRBraille.announcementsOn"
+ "SCROTokenSecureAttribute"
+ "TB,N,V_isTokenSecure"
+ "_eventQueue_handleSystemVirtualDisplayKeyPress:"
+ "_isTokenSecure"
+ "isTokenSecure"
+ "setIsShowingSecureToken:"
+ "setIsTokenSecure:"

```
