## VoiceOverServices

> `/System/iOSSupport/System/Library/PrivateFrameworks/VoiceOverServices.framework/Versions/A/VoiceOverServices`

```diff

-3237.0.0.0.0
-  __TEXT.__text: 0x27fe8
-  __TEXT.__objc_methlist: 0x28d4
+3240.0.1.2.0
+  __TEXT.__text: 0x288dc
+  __TEXT.__objc_methlist: 0x292c
   __TEXT.__dlopen_cstrs: 0x41
   __TEXT.__const: 0x40
   __TEXT.__gcc_except_tab: 0xc4
-  __TEXT.__cstring: 0x61e3
+  __TEXT.__cstring: 0x637a
   __TEXT.__oslogstring: 0x39e
   __TEXT.__unwind_info: 0x560
   __TEXT.__objc_stubs: 0x0

   __DATA_CONST.__objc_classlist: 0xc0
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1870
+  __DATA_CONST.__objc_selrefs: 0x18c0
   __DATA_CONST.__objc_superrefs: 0x90
+  __DATA_CONST.__objc_arraydata: 0x20
   __DATA_CONST.__got: 0x180
-  __AUTH_CONST.__const: 0x3100
-  __AUTH_CONST.__cfstring: 0x7460
-  __AUTH_CONST.__objc_const: 0x3b28
+  __AUTH_CONST.__const: 0x31c0
+  __AUTH_CONST.__cfstring: 0x76a0
+  __AUTH_CONST.__objc_const: 0x3b88
+  __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0xfc
-  __DATA.__data: 0xdc8
-  __DATA.__bss: 0x5b0
+  __DATA.__data: 0xde8
+  __DATA.__bss: 0x618
   __DATA_DIRTY.__objc_data: 0x780
   __DATA_DIRTY.__bss: 0x12a0
   - /System/Library/Frameworks/CoreBluetooth.framework/Versions/A/CoreBluetooth

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1237
-  Symbols:   3501
-  CStrings:  973
+  Functions: 1251
+  Symbols:   3544
+  CStrings:  991
 
Symbols:
+ +[VOSCommand Braille2DZoomIn]
+ +[VOSCommand Braille2DZoomOut]
+ +[VOSCommand BrailleShowImage]
+ +[VOSCommand IntelligentScreenDescription]
+ +[VOSCommand ShowRecognitionOptions]
+ +[VOSOutputEvent ImageRecognition]
+ -[VOSCommandManager _migrateRetiredImageExplorerCommandDefaults:resolver:]
+ Braille2DZoomIn._Command
+ Braille2DZoomIn.onceToken
+ Braille2DZoomOut._Command
+ Braille2DZoomOut.onceToken
+ BrailleShowImage._Command
+ BrailleShowImage.onceToken
+ GCC_except_table1136
+ ImageRecognition._Event
+ ImageRecognition.onceToken
+ IntelligentScreenDescription._Command
+ IntelligentScreenDescription.onceToken
+ ShowRecognitionOptions._Command
+ ShowRecognitionOptions.onceToken
+ VOSAccessibilitySharedSupportBundle._sharedSupportBundle
+ _AXAskShouldHideOptions
+ _OBJC_CLASS_$_NSConstantArray
+ _VOSAccessibilitySharedSupportBundle
+ ___29+[VOSCommand Braille2DZoomIn]_block_invoke
+ ___30+[VOSCommand Braille2DZoomOut]_block_invoke
+ ___30+[VOSCommand BrailleShowImage]_block_invoke
+ ___34+[VOSOutputEvent ImageRecognition]_block_invoke
+ ___36+[VOSCommand ShowRecognitionOptions]_block_invoke
+ ___42+[VOSCommand IntelligentScreenDescription]_block_invoke
+ _kVOTEventCommandBraille2DZoomIn
+ _kVOTEventCommandBraille2DZoomOut
+ _kVOTEventCommandIntelligentScreenDescription
+ _kVOTEventCommandShowRecognitionOptions
+ _objc_msgSend$Braille2DZoomIn
+ _objc_msgSend$Braille2DZoomOut
+ _objc_msgSend$BrailleShowImage
+ _objc_msgSend$ImageRecognition
+ _objc_msgSend$IntelligentScreenDescription
+ _objc_msgSend$ShowRecognitionOptions
+ _objc_msgSend$_migrateRetiredImageExplorerCommandDefaults:resolver:
+ _objc_msgSend$imageExplorerSeedKeyboardShortcutsDidMigrate
+ _objc_msgSend$objectAtIndexedSubscript:
+ _objc_msgSend$setImageExplorerSeedKeyboardShortcutsDidMigrate:
- GCC_except_table1122
CStrings:
+ "/System/Library/PrivateFrameworks/AccessibilitySharedSupport.framework"
+ "B"
+ "Braille2DZoomIn"
+ "Braille2DZoomOut"
+ "BrailleShowImage"
+ "Copy Focus Debug Info to Clipboard"
+ "E"
+ "ImageRecognition"
+ "IntelligentScreenDescription"
+ "LoopScanningMagnifier_ML"
+ "P"
+ "R"
+ "ShowRecognitionOptions"
+ "VOTEventCommandBraille2DZoomIn"
+ "VOTEventCommandBraille2DZoomOut"
+ "VOTEventCommandIntelligentScreenDescription"
+ "VOTEventCommandShowRecognitionOptions"
+ "wav"
```
