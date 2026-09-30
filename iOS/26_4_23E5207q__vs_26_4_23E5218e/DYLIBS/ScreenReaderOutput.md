## ScreenReaderOutput

> `/System/Library/PrivateFrameworks/ScreenReaderOutput.framework/ScreenReaderOutput`

```diff

-424.10.0.0.0
-  __TEXT.__text: 0x79a40
+424.12.0.0.0
+  __TEXT.__text: 0x7a614
   __TEXT.__auth_stubs: 0x1b00
-  __TEXT.__objc_methlist: 0x6f20
+  __TEXT.__objc_methlist: 0x6fe8
   __TEXT.__gcc_except_tab: 0x183c
   __TEXT.__const: 0xcb8
-  __TEXT.__cstring: 0x538d
+  __TEXT.__cstring: 0x539d
   __TEXT.__oslogstring: 0x225b
   __TEXT.__ustring: 0x9e
   __TEXT.__swift5_typeref: 0x530

   __TEXT.__swift_as_entry: 0x40
   __TEXT.__swift_as_ret: 0x48
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x21f8
+  __TEXT.__unwind_info: 0x2228
   __TEXT.__eh_frame: 0x670
-  __TEXT.__objc_classname: 0xd9f
-  __TEXT.__objc_methname: 0xfe9b
-  __TEXT.__objc_methtype: 0x233e
-  __TEXT.__objc_stubs: 0xd920
+  __TEXT.__objc_classname: 0xdbf
+  __TEXT.__objc_methname: 0x1001b
+  __TEXT.__objc_methtype: 0x239e
+  __TEXT.__objc_stubs: 0xda20
   __DATA_CONST.__got: 0x5f0
   __DATA_CONST.__const: 0xc88
   __DATA_CONST.__objc_classlist: 0x2b0
   __DATA_CONST.__objc_catlist: 0x20
-  __DATA_CONST.__objc_protolist: 0xf0
+  __DATA_CONST.__objc_protolist: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3ef8
+  __DATA_CONST.__objc_selrefs: 0x3f40
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x1f0
   __DATA_CONST.__objc_arraydata: 0x380
   __AUTH_CONST.__auth_got: 0xd90
   __AUTH_CONST.__const: 0x1978
-  __AUTH_CONST.__cfstring: 0x51c0
-  __AUTH_CONST.__objc_const: 0xf288
+  __AUTH_CONST.__cfstring: 0x5200
+  __AUTH_CONST.__objc_const: 0xf3e0
   __AUTH_CONST.__objc_intobj: 0x9d8
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0xd10
   __AUTH.__data: 0x5e0
   __DATA.__objc_ivar: 0x850
-  __DATA.__data: 0x10e0
+  __DATA.__data: 0x1140
   __DATA.__common: 0x30
   __DATA.__bss: 0xab8
   __DATA_DIRTY.__objc_data: 0xe10

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 91AF0DE0-3E6C-37D9-9B23-53854D889E67
-  Functions: 2960
-  Symbols:   9308
-  CStrings:  4779
+  UUID: DF204D8F-18E6-3BE5-831F-D8DF4B163027
+  Functions: 2971
+  Symbols:   9346
+  CStrings:  4797
 
Symbols:
+ -[SCRO2DBraillePlane content]
+ -[SCRO2DBraillePlane createContentWithBrailleData:width:height:canvas:previousFirstDisplayedLine:]
+ -[SCRO2DBrailleReadingContent elementIndexForDisplayLineNumber:]
+ -[SCRO2DBrailleReadingContent elementIndexForLineNumber:]
+ -[SCRO2DBrailleReadingContent firstDisplayedLine]
+ -[SCRO2DBrailleReadingContent initWithBrailleData:width:height:wordWrap:previousFirstDisplayedLine:]
+ -[SCROBrailleDisplayManager didDeleteScriptChar]
+ -[SCROBrailleLine didDeleteScriptChar]
+ -[SCROBrailleUIDynamicBrailleView _finalizeTranscriptionOnMainThread]
+ -[SCROBrailleUIDynamicBrailleView _handleTranscribedTextOnMainThread:]
+ GCC_except_table175
+ GCC_except_table307
+ GCC_except_table309
+ GCC_except_table344
+ GCC_except_table412
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_SCRO2DBrailleContentProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SCROBrailleEventDispatcherDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SCROBrailleEventDispatcherDelegate
+ __OBJC_$_PROTOCOL_REFS_SCROBrailleEventDispatcherDelegate
+ __OBJC_LABEL_PROTOCOL_$_SCROBrailleEventDispatcherDelegate
+ __OBJC_PROTOCOL_$_SCROBrailleEventDispatcherDelegate
+ ___48-[SCROBrailleDisplayManager didDeleteScriptChar]_block_invoke
+ ___61-[SCROBrailleDisplayManager _eventQueue_setBrailleFormatter:]_block_invoke
+ ___block_literal_global.372
+ ___block_literal_global.384
+ _objc_msgSend$_finalizeTranscriptionOnMainThread
+ _objc_msgSend$content
+ _objc_msgSend$createContentWithBrailleData:width:height:canvas:previousFirstDisplayedLine:
+ _objc_msgSend$didDeleteScriptChar
+ _objc_msgSend$elementIndexForDisplayLineNumber:
+ _objc_msgSend$elementIndexForLineNumber:
+ _objc_msgSend$firstDisplayedLine
+ _objc_msgSend$initWithBrailleData:width:height:wordWrap:previousFirstDisplayedLine:
+ _objc_msgSend$setAttributedString:
- -[SCRO2DBraillePlane createContentWithBrailleData:width:height:canvas:]
- GCC_except_table174
- GCC_except_table306
- GCC_except_table308
- GCC_except_table343
- GCC_except_table409
- ___block_literal_global.345
- ___block_literal_global.42
- _objc_msgSend$createContentWithBrailleData:width:height:canvas:
CStrings:
+ "@\"<SCROBrailleEventDispatcherDelegate>\""
+ "@52@0:8@16q24q32B40q44"
+ "@56@0:8@16q24q32@40q48"
+ "SCROBrailleEventDispatcherDelegate"
+ "T@\"<SCRO2DBrailleContentProtocol>\",R,N,V_content"
+ "Tq,R,N,V_firstDisplayedLine"
+ "_finalizeTranscriptionOnMainThread"
+ "_handleTranscribedTextOnMainThread:"
+ "aqui OBrailleDisplay.handleCommandRouterKeyEvent: selectionBegin %@ selectionEnd %@"
+ "createContentWithBrailleData:width:height:canvas:previousFirstDisplayedLine:"
+ "didDeleteScriptChar"
+ "elementIndexForDisplayLineNumber:"
+ "elementIndexForLineNumber:"
+ "firstDisplayedLine"
+ "initWithBrailleData:width:height:wordWrap:previousFirstDisplayedLine:"
+ "isFinal"
+ "setAttributedString:"
+ "v24@0:8@\"SCROBrailleEvent\"16"
- "@48@0:8@16q24q32@40"
- "aqui OBrailleDisplay.handleCommandRouterKeyEvent: selectionBegin %d selectionEnd %d"
- "createContentWithBrailleData:width:height:canvas:"

```
