## ScreenReaderOutput

> `/System/Library/PrivateFrameworks/ScreenReaderOutput.framework/ScreenReaderOutput`

```diff

-424.2.0.0.0
-  __TEXT.__text: 0x70724
-  __TEXT.__auth_stubs: 0x1930
-  __TEXT.__objc_methlist: 0x6dec
+424.4.0.0.0
+  __TEXT.__text: 0x7159c
+  __TEXT.__auth_stubs: 0x1970
+  __TEXT.__objc_methlist: 0x6e64
   __TEXT.__gcc_except_tab: 0x1898
   __TEXT.__const: 0x908
-  __TEXT.__cstring: 0x59a8
-  __TEXT.__oslogstring: 0x1f5b
-  __TEXT.__ustring: 0x96
+  __TEXT.__cstring: 0x59e8
+  __TEXT.__oslogstring: 0x1fdb
+  __TEXT.__ustring: 0x9e
   __TEXT.__swift5_typeref: 0x39a
   __TEXT.__constg_swiftt: 0x414
   __TEXT.__swift5_builtin: 0x3c

   __TEXT.__swift_as_entry: 0x40
   __TEXT.__swift_as_ret: 0x48
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x1e98
+  __TEXT.__unwind_info: 0x1eb0
   __TEXT.__eh_frame: 0x678
   __TEXT.__objc_classname: 0xab8
-  __TEXT.__objc_methname: 0xf968
+  __TEXT.__objc_methname: 0xf97a
   __TEXT.__objc_methtype: 0x2293
-  __TEXT.__objc_stubs: 0xd600
-  __DATA_CONST.__got: 0x578
+  __TEXT.__objc_stubs: 0xd660
+  __DATA_CONST.__got: 0x580
   __DATA_CONST.__const: 0xc78
   __DATA_CONST.__objc_classlist: 0x2a8
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0xe8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3e70
+  __DATA_CONST.__objc_selrefs: 0x3e98
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x1f0
   __DATA_CONST.__objc_arraydata: 0x380
-  __AUTH_CONST.__auth_got: 0xca8
+  __AUTH_CONST.__auth_got: 0xcc8
   __AUTH_CONST.__const: 0x18f0
-  __AUTH_CONST.__cfstring: 0x5140
-  __AUTH_CONST.__objc_const: 0xf010
-  __AUTH_CONST.__objc_intobj: 0x9c0
+  __AUTH_CONST.__cfstring: 0x51c0
+  __AUTH_CONST.__objc_const: 0xf040
+  __AUTH_CONST.__objc_intobj: 0x9d8
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0xc20
   __AUTH.__data: 0x5b8
-  __DATA.__objc_ivar: 0x844
+  __DATA.__objc_ivar: 0x848
   __DATA.__data: 0x1030
   __DATA.__common: 0x28
   __DATA.__bss: 0x7c8

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 08C5794C-FFFC-39D4-BFF2-F050B417BFE2
-  Functions: 2841
-  Symbols:   9143
-  CStrings:  4748
+  UUID: 294081C1-D760-350E-ACC1-E14FBCCCD527
+  Functions: 2851
+  Symbols:   9172
+  CStrings:  4761
 
Symbols:
+ +[SCROBrailleUIUtilities brailleForBackButton]
+ +[SCROBrailleUIUtilities brailleForBackButton].cold.1
+ -[SCROBrailleDisplayManager _eventQueue_migratePasteBoardContentToSystem]
+ -[SCROBrailleUIBrailleAreaView setShowsBackButton:]
+ -[SCROBrailleUIBrailleAreaView showsBackButton]
+ -[SCROBrailleUIBrailleNotesApp _labelForFolder:]
+ -[SCROBrailleUIDynamicBrailleView _backButtonHandleEvent:]
+ -[SCROBrailleUIDynamicBrailleView _contentHandleEvent:]
+ -[SCROBrailleUIDynamicBrailleView setShowingBackButton:]
+ -[SCROBrailleUIDynamicBrailleView setShowsBackButton:]
+ -[SCROBrailleUIDynamicBrailleView setValueCache:]
+ -[SCROBrailleUIDynamicBrailleView showingBackButton]
+ -[SCROBrailleUIDynamicBrailleView showsBackButton]
+ -[SCROBrailleUIDynamicBrailleView valueCache]
+ -[SCROBrailleUIFinderApp _isFileSizeAcceptableForURL:]
+ -[SCROBrailleUIMainApp _replaceCalculatorListItemContentWith:]
+ -[SCROBrailleUISettingsManager showsBackButton]
+ -[SCROVirtualBrailleDriver enqueueForceTranslate]
+ GCC_except_table100
+ GCC_except_table107
+ GCC_except_table108
+ GCC_except_table110
+ GCC_except_table130
+ GCC_except_table140
+ GCC_except_table143
+ GCC_except_table144
+ GCC_except_table147
+ GCC_except_table164
+ GCC_except_table166
+ GCC_except_table176
+ GCC_except_table177
+ GCC_except_table197
+ GCC_except_table198
+ GCC_except_table249
+ GCC_except_table303
+ GCC_except_table305
+ GCC_except_table340
+ GCC_except_table406
+ GCC_except_table68
+ GCC_except_table69
+ GCC_except_table73
+ GCC_except_table76
+ GCC_except_table77
+ GCC_except_table78
+ GCC_except_table93
+ GCC_except_table98
+ _NSFileSize
+ _OBJC_IVAR_$_SCROBrailleUIBrailleAreaView._showsBackButton
+ _OBJC_IVAR_$_SCROBrailleUIDynamicBrailleView._showingBackButton
+ _OBJC_IVAR_$_SCROBrailleUIDynamicBrailleView._showsBackButton
+ _OBJC_IVAR_$_SCROBrailleUIDynamicBrailleView._valueCache
+ _VOTLogBraille
+ ___46+[SCROBrailleUIUtilities brailleForBackButton]_block_invoke
+ ___block_literal_global.108
+ ___block_literal_global.112
+ ___block_literal_global.146
+ ___block_literal_global.150
+ ___block_literal_global.270
+ ___block_literal_global.273
+ ___block_literal_global.279
+ ___block_literal_global.336
+ ___block_literal_global.362
+ ___block_literal_global.365
+ ___block_literal_global.368
+ ___block_literal_global.371
+ ___block_literal_global.374
+ __os_signpost_emit_with_name_impl
+ _brailleForBackButton._brailleforBackButton
+ _brailleForBackButton.onceToken
+ _objc_msgSend$_eventQueue_migratePasteBoardContentToSystem
+ _objc_msgSend$_isFileSizeAcceptableForURL:
+ _objc_msgSend$_labelForFolder:
+ _objc_msgSend$_replaceCalculatorListItemContentWith:
+ _objc_msgSend$attributesOfItemAtPath:error:
+ _objc_msgSend$brailleForBackButton
+ _objc_msgSend$enqueueForceTranslate
+ _objc_msgSend$numberWithUnsignedLongLong:
+ _objc_msgSend$showsBackButton
+ _objc_msgSend$textValue
+ _objc_msgSend$unsignedLongLongValue
+ _objc_msgSend$voiceOverTouchBrailleUIShowsBackButton
+ _os_signpost_enabled
+ _os_signpost_id_generate
- -[SCROBrailleDisplayInput prepareToMemorizeNextKey]
- -[SCROBrailleDisplayInput requestPrepareToMemorizeNextKey]
- -[SCROBrailleDisplayInput setPrepareToMemorizeNextKey:]
- -[SCROBrailleDisplayInput setRequestPrepareToMemorizeNextKey:]
- -[SCROBrailleDisplayInput setWillMemorizeNow:]
- -[SCROBrailleDisplayInput willMemorizeNow]
- -[SCROBrailleUIBrailleAreaView _brailleForBackButton]
- -[SCROBrailleUIBrailleAreaView _brailleForBackButton].cold.1
- GCC_except_table104
- GCC_except_table106
- GCC_except_table113
- GCC_except_table114
- GCC_except_table116
- GCC_except_table136
- GCC_except_table146
- GCC_except_table153
- GCC_except_table155
- GCC_except_table156
- GCC_except_table170
- GCC_except_table172
- GCC_except_table182
- GCC_except_table183
- GCC_except_table203
- GCC_except_table204
- GCC_except_table255
- GCC_except_table302
- GCC_except_table304
- GCC_except_table339
- GCC_except_table405
- GCC_except_table71
- GCC_except_table79
- GCC_except_table81
- GCC_except_table82
- GCC_except_table83
- GCC_except_table84
- GCC_except_table99
- _OBJC_IVAR_$_SCROBrailleDisplayInput._prepareToMemorizeNextKey
- _OBJC_IVAR_$_SCROBrailleDisplayInput._requestPrepareToMemorizeNextKey
- _OBJC_IVAR_$_SCROBrailleDisplayInput._willMemorizeNow
- ___53-[SCROBrailleUIBrailleAreaView _brailleForBackButton]_block_invoke
- ___block_literal_global.105
- ___block_literal_global.109
- ___block_literal_global.143
- ___block_literal_global.147
- ___block_literal_global.267
- ___block_literal_global.269
- ___block_literal_global.275
- ___block_literal_global.335
- ___block_literal_global.358
- ___block_literal_global.361
- ___block_literal_global.364
- ___block_literal_global.367
- ___block_literal_global.370
- __brailleForBackButton._brailleforBackButton
- __brailleForBackButton.onceToken
- _objc_msgSend$_brailleForBackButton
- _objc_msgSend$brailleDisplay:willMemorizeKey:
- _objc_msgSend$nextWillMemorizeNotificationTime
- _objc_msgSend$prepareToMemorizeNextKey
- _objc_msgSend$requestPrepareToMemorizeNextKey
- _objc_msgSend$setPrepareToMemorizeNextKey:
- _objc_msgSend$setRequestPrepareToMemorizeNextKey:
- _objc_msgSend$setWillMemorizeNow:
- _objc_msgSend$willMemorizeNow
CStrings:
+ "BRF File bigger than 5MB"
+ "Detect Displays"
+ "Error getting file attributes: %@"
+ "Set Main Cells"
+ "Signpost id %@ generated for Driver %@"
+ "TB,N,V_showsBackButton"
+ "_eventQueue_migratePasteBoardContentToSystem"
+ "_isFileSizeAcceptableForURL:"
+ "_labelForFolder:"
+ "_replaceCalculatorListItemContentWith:"
+ "_showsBackButton"
+ "attributesOfItemAtPath:error:"
+ "brailleForBackButton"
+ "context.menu.copy"
+ "enqueueForceTranslate"
+ "finder.file.too.big"
+ "live.captions.context.menu.copy"
+ "numberWithUnsignedLongLong:"
+ "setShowsBackButton:"
+ "showsBackButton"
+ "unsignedLongLongValue"
+ "voiceOverTouchBrailleUIShowsBackButton"
- "TB,N,V_prepareToMemorizeNextKey"
- "TB,N,V_requestPrepareToMemorizeNextKey"
- "TB,N,V_willMemorizeNow"
- "_brailleForBackButton"
- "_prepareToMemorizeNextKey"
- "_requestPrepareToMemorizeNextKey"
- "_willMemorizeNow"
- "prepareToMemorizeNextKey"
- "requestPrepareToMemorizeNextKey"
- "setPrepareToMemorizeNextKey:"
- "setRequestPrepareToMemorizeNextKey:"
- "setWillMemorizeNow:"
- "willMemorizeNow"

```
