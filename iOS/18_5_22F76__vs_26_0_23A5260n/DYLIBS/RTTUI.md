## RTTUI

> `/System/Library/PrivateFrameworks/RTTUI.framework/RTTUI`

```diff

-456.8.10.0.0
-  __TEXT.__text: 0x1912c
-  __TEXT.__auth_stubs: 0x870
-  __TEXT.__objc_methlist: 0x1a88
+485.3.0.0.0
+  __TEXT.__text: 0x19f60
+  __TEXT.__auth_stubs: 0x880
+  __TEXT.__objc_methlist: 0x1ad0
   __TEXT.__const: 0x1d8
-  __TEXT.__gcc_except_tab: 0x668
-  __TEXT.__cstring: 0xaf5
-  __TEXT.__oslogstring: 0x101c
+  __TEXT.__gcc_except_tab: 0x660
+  __TEXT.__cstring: 0xb28
+  __TEXT.__oslogstring: 0x1077
   __TEXT.__dlopen_cstrs: 0x329
   __TEXT.__ustring: 0x14
-  __TEXT.__unwind_info: 0x688
+  __TEXT.__unwind_info: 0x6a0
   __TEXT.__objc_classname: 0x2d4
-  __TEXT.__objc_methname: 0x67fd
-  __TEXT.__objc_methtype: 0x1be7
-  __TEXT.__objc_stubs: 0x5160
+  __TEXT.__objc_methname: 0x6a49
+  __TEXT.__objc_methtype: 0x1c5f
+  __TEXT.__objc_stubs: 0x5360
   __DATA_CONST.__got: 0x418
-  __DATA_CONST.__const: 0x7b0
+  __DATA_CONST.__const: 0x800
   __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1c38
+  __DATA_CONST.__objc_selrefs: 0x1cc8
   __DATA_CONST.__objc_superrefs: 0x68
   __DATA_CONST.__objc_arraydata: 0x80
-  __AUTH_CONST.__auth_got: 0x448
+  __AUTH_CONST.__auth_got: 0x450
   __AUTH_CONST.__const: 0x160
-  __AUTH_CONST.__cfstring: 0xdc0
-  __AUTH_CONST.__objc_const: 0x2160
+  __AUTH_CONST.__cfstring: 0xe00
+  __AUTH_CONST.__objc_const: 0x2170
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_arrayobj: 0x18

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: DF35BA30-F22B-37AA-93BA-C5C695D19821
-  Functions: 476
-  Symbols:   2298
-  CStrings:  1633
+  UUID: 0B8A2ED1-B721-33AE-B9EC-6EADD1721828
+  Functions: 485
+  Symbols:   2335
+  CStrings:  1660
 
Symbols:
+ -[RTTUIConversationViewController _holdButtonItem]
+ -[RTTUIConversationViewController _muteButtonItem]
+ -[RTTUIConversationViewController addTranslatedTranscriptionText:translatedText:isNew:]
+ -[RTTUIConversationViewController deviceDidReceiveTranslation:forUtterance:]
+ GCC_except_table108
+ GCC_except_table122
+ GCC_except_table125
+ GCC_except_table128
+ GCC_except_table34
+ GCC_except_table45
+ GCC_except_table98
+ __UISolariumEnabled
+ ___39-[RTTUIConversationViewController init]_block_invoke.336
+ ___46-[RTTUIConversationViewController toggleMute:]_block_invoke.439
+ ___50-[RTTUIConversationViewController callDidConnect:]_block_invoke.398
+ ___50-[RTTUIConversationViewController callDidConnect:]_block_invoke_2
+ ___50-[RTTUIConversationViewController callDidConnect:]_block_invoke_3
+ ___53-[RTTUIConversationViewController textViewDidChange:]_block_invoke.513
+ ___67-[RTTUIConversationViewController tableView:cellForRowAtIndexPath:]_block_invoke.493
+ ___76-[RTTUIConversationViewController deviceDidReceiveTranslation:forUtterance:]_block_invoke
+ ___82-[RTTUIConversationControllerCoordinator _registerForTranscriptionUpdatesForCall:]_block_invoke.76
+ ___block_descriptor_48_e8_32s40s_e44_v32?0"NSString"8"NSString"16"NSString"24ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e47_v40?0"NSString"8"NSString"16"NSString"24q32ls32l8s40l8
+ ___block_descriptor_72_e8_32s40s48s56s64s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_80_e8_32s40s48s56s64s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
+ ___block_literal_global.323
+ ___block_literal_global.334
+ ___block_literal_global.353
+ ___block_literal_global.36
+ ___block_literal_global.47
+ ___block_literal_global.520
+ _objc_msgSend$_holdButtonItem
+ _objc_msgSend$_muteButtonItem
+ _objc_msgSend$addTranslatedTranscriptionFromOtherContactPath:original:
+ _objc_msgSend$addTranslatedTranscriptionText:translatedText:isNew:
+ _objc_msgSend$callCenter
+ _objc_msgSend$deviceDidReceiveTranslation:forUtterance:
+ _objc_msgSend$hasTranslation
+ _objc_msgSend$initWithImage:style:target:action:
+ _objc_msgSend$lastUtteranceForMe:withText:
+ _objc_msgSend$performCallCenterTask:callCenter:
+ _objc_msgSend$pinnedTrailingGroup
+ _objc_msgSend$registerForUpdatesWithTranslation:forCallUID:
+ _objc_msgSend$setPinnedTrailingGroup:
+ _objc_msgSend$stringByAppendingFormat:
+ _objc_msgSend$translatedText
+ _objc_msgSend$updateTranslatedTranscriptionFromOtherContactPath:original:
+ _objc_msgSend$updateTranslation:
- GCC_except_table100
- GCC_except_table106
- GCC_except_table117
- GCC_except_table120
- GCC_except_table31
- GCC_except_table40
- GCC_except_table90
- ___39-[RTTUIConversationViewController init]_block_invoke.315
- ___46-[RTTUIConversationViewController toggleMute:]_block_invoke.416
- ___53-[RTTUIConversationViewController textViewDidChange:]_block_invoke.490
- ___67-[RTTUIConversationViewController tableView:cellForRowAtIndexPath:]_block_invoke.470
- ___block_descriptor_48_e8_32s40s_e31_v24?0"NSString"8"NSString"16ls32l8s40l8
- ___block_descriptor_48_e8_32s40s_e34_v32?0"NSString"8"NSString"16q24ls32l8s40l8
- ___block_literal_global.18
- ___block_literal_global.29
- ___block_literal_global.320
- ___block_literal_global.331
- ___block_literal_global.350
- ___block_literal_global.505
- _objc_msgSend$registerForUpdates:forCallUID:
CStrings:
+ "\n%@"
+ "@\"UIMenu\"40@0:8@\"UITextView\"16@\"NSArray\"24@\"NSArray\"32"
+ "@36@0:8@16@24B32"
+ "B40@0:8@\"UITextView\"16@\"NSArray\"24@\"NSString\"32"
+ "Got remote translation update callback: %@ %@ %@ for vc %@"
+ "RTTTranslationPrefix"
+ "TTY receive translation |%@|=%@"
+ "_holdButtonItem"
+ "_muteButtonItem"
+ "addTranslatedTranscriptionFromOtherContactPath:original:"
+ "addTranslatedTranscriptionText:translatedText:isNew:"
+ "callCenter"
+ "deviceDidReceiveTranslation:forUtterance:"
+ "hasTranslation"
+ "initWithImage:style:target:action:"
+ "lastUtteranceForMe:withText:"
+ "performCallCenterTask:callCenter:"
+ "pinnedTrailingGroup"
+ "registerForUpdatesWithTranslation:forCallUID:"
+ "setPinnedTrailingGroup:"
+ "stringByAppendingFormat:"
+ "textView:editMenuForTextInRanges:suggestedActions:"
+ "textView:shouldChangeTextInRanges:replacementText:"
+ "translatedText"
+ "updateTranslatedTranscriptionFromOtherContactPath:original:"
+ "updateTranslation:"
+ "v32@?0@\"NSString\"8@\"NSString\"16@\"NSString\"24"
+ "v40@?0@\"NSString\"8@\"NSString\"16@\"NSString\"24q32"
- "registerForUpdates:forCallUID:"
- "v24@?0@\"NSString\"8@\"NSString\"16"
- "v32@?0@\"NSString\"8@\"NSString\"16q24"

```
