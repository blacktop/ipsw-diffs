## TextInputCore

> `/System/Library/PrivateFrameworks/TextInputCore.framework/Versions/A/TextInputCore`

```diff

-  __TEXT.__text: 0x1ffc74
+  __TEXT.__text: 0x200fb8
   __TEXT.__init_offsets: 0xc0
-  __TEXT.__objc_methlist: 0xffd0
-  __TEXT.__const: 0x2e20
-  __TEXT.__cstring: 0x12a11
+  __TEXT.__objc_methlist: 0x10018
+  __TEXT.__const: 0x2e30
+  __TEXT.__cstring: 0x12be5
   __TEXT.__dlopen_cstrs: 0x9d
-  __TEXT.__oslogstring: 0x3aae
-  __TEXT.__ustring: 0x502
-  __TEXT.__unwind_info: 0x6008
+  __TEXT.__oslogstring: 0x3aaf
+  __TEXT.__ustring: 0x7bc
+  __TEXT.__unwind_info: 0x6078
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x19e0
+  __DATA_CONST.__const: 0x19f8
   __DATA_CONST.__objc_classlist: 0x818
   __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_protolist: 0x180
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x94a0
+  __DATA_CONST.__objc_selrefs: 0x94e8
   __DATA_CONST.__objc_superrefs: 0x6d8
-  __DATA_CONST.__objc_arraydata: 0xec0
-  __DATA_CONST.__got: 0x1420
-  __AUTH_CONST.__const: 0xbb48
-  __AUTH_CONST.__cfstring: 0xf920
-  __AUTH_CONST.__objc_const: 0x19450
+  __DATA_CONST.__objc_arraydata: 0xed8
+  __DATA_CONST.__got: 0x14c0
+  __AUTH_CONST.__const: 0xbcb0
+  __AUTH_CONST.__cfstring: 0xfec0
+  __AUTH_CONST.__objc_const: 0x194c0
   __AUTH_CONST.__weak_auth_got: 0x30
   __AUTH_CONST.__objc_intobj: 0x5e8
   __AUTH_CONST.__objc_dictobj: 0x118
-  __AUTH_CONST.__objc_arrayobj: 0x2d0
+  __AUTH_CONST.__objc_arrayobj: 0x2e8
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH_CONST.__auth_got: 0x1860
-  __AUTH.__objc_data: 0x2170
+  __AUTH_CONST.__auth_got: 0x1888
+  __AUTH.__objc_data: 0x1fe0
   __AUTH.__data: 0x18
   __AUTH.__thread_vars: 0x30
   __AUTH.__thread_bss: 0x20
-  __DATA.__objc_ivar: 0x11b0
+  __DATA.__objc_ivar: 0x11bc
   __DATA.__data: 0x21c0
-  __DATA.__bss: 0x1780
+  __DATA.__bss: 0x1790
   __DATA.__common: 0x408
-  __DATA_DIRTY.__objc_data: 0x2f80
+  __DATA_DIRTY.__objc_data: 0x3110
   __DATA_DIRTY.__data: 0xb0
-  __DATA_DIRTY.__bss: 0xa40
+  __DATA_DIRTY.__bss: 0xaa8
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/Contacts.framework/Versions/A/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libmecabra.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 10126
-  Symbols:   20874
-  CStrings:  4970
+  Functions: 10165
+  Symbols:   20961
+  CStrings:  5034
 
Sections:
~ __TEXT.__init_offsets : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __AUTH_CONST.__weak_auth_got : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH_CONST.__objc_doubleobj : content changed
~ __AUTH.__data : content changed
~ __AUTH.__thread_vars : content changed
~ __DATA.__data : content changed
Symbols:
+ -[TIKeyboardInputManager(ZephyrEngineSpecializations) _publishDebugChargeForKeyCode:touchLocation:]
+ -[TIKeyboardInputManagerMecabra contextBeforeWithDesiredLength:]
+ -[TIKeyboardInputManagerMecabra onScreenContextForCandidates]
+ -[TIMecabraEnvironment onScreenContext]
+ -[TIMecabraEnvironment setOnScreenContext:]
+ -[TIMecabraEnvironmentContextWrapper setOnScreenStringContext:]
+ -[TIWordSearch setOnScreenContext:]
+ OBJC_IVAR_$_TIKeyboardInputManager._debugChargeBias
+ OBJC_IVAR_$_TIKeyboardInputManager._debugChargeSigma
+ OBJC_IVAR_$_TIMecabraEnvironment._onScreenContext
+ _CGRectIsEmpty
+ _OBJC_CLASS_$_NSDataDetector
+ _ZZL21libmecabraLibraryCorePPcE16frameworkLibrary
+ _ZZL42getMecabraContextSetStringContextSymbolLocvE3ptr
+ __ZL14TIIsPureDigitsP8NSString
+ __ZL17TICollectAllTextsRKNSt3__110shared_ptrI14TIScreenUINodeEEP14NSMutableArrayIP8NSStringE
+ __ZL17TIDeduplicatePairRKNSt3__110shared_ptrI14TIScreenUINodeEES4_
+ __ZL17TIPruneNoisyNodesRKNSt3__110shared_ptrI14TIScreenUINodeEE
+ __ZL20_TIPublishDebugStatePKcPiy
+ __ZL21libmecabraLibraryCorePPc
+ __ZL23TIDeduplicateSubstringsRKNSt3__110shared_ptrI14TIScreenUINodeEE
+ __ZL24TICollectDescendantNodesRKNSt3__110shared_ptrI14TIScreenUINodeEERNS_6vectorIS2_NS_9allocatorIS2_EEEE
+ __ZL24TINormalizeForComparisonP8NSString
+ __ZL27TIDeduplicateCollectionItemRKNSt3__110shared_ptrI14TIScreenUINodeEE
+ __ZL31TINormalizeScreenScrapingStringP8NSString
+ __ZL33TIHasVerticalScrollableDescendantRKNSt3__110shared_ptrI14TIScreenUINodeEE
+ __ZL42getMecabraContextSetStringContextSymbolLocv
+ __ZN2TI8Favonius10BeamSearch20choose_hit_test_nodeERKN3WTF6RefPtrINS0_10SearchNodeEEERKNS3_INS0_8KeyMatchEEES7_S7_PNS0_12HitKeyReasonE
+ __ZNK2TI8Favonius10BeamSearch14hit_key_reasonEv
+ __ZNK2TI8Favonius26FavoniusStrokeBuildManager21debug_last_touch_infoEv
+ __ZNSt3__120__shared_ptr_emplaceI14TIScreenUINodeNS_9allocatorIS1_EEE16__on_zero_sharedEv
+ __ZNSt3__120__shared_ptr_emplaceI14TIScreenUINodeNS_9allocatorIS1_EEE21__on_zero_shared_weakEv
+ __ZNSt3__120__shared_ptr_emplaceI14TIScreenUINodeNS_9allocatorIS1_EEED0Ev
+ __ZNSt3__120__shared_ptr_emplaceI14TIScreenUINodeNS_9allocatorIS1_EEED1Ev
+ __ZNSt3__16vectorINS_10shared_ptrI14TIScreenUINodeEENS_9allocatorIS3_EEE16__destroy_vectorclB9nqn220106Ev
+ __ZNSt3__16vectorINS_10shared_ptrI14TIScreenUINodeEENS_9allocatorIS3_EEE20__throw_length_errorB9nqn220106Ev
+ __ZNSt3__16vectorINS_10shared_ptrI14TIScreenUINodeEENS_9allocatorIS3_EEE24__emplace_back_slow_pathIJRKS3_EEEPS3_DpOT_
+ __ZNSt3__16vectorINS_10shared_ptrI14TIScreenUINodeEENS_9allocatorIS3_EEE5clearB9nqn220106Ev
+ __ZNSt3__16vectorINS_10shared_ptrI14TIScreenUINodeEENS_9allocatorIS3_EEE9push_backB9nqn220106ERKS3_
+ __ZTVNSt3__120__shared_ptr_emplaceI14TIScreenUINodeNS_9allocatorIS1_EEEE
+ __ZZ99-[TIKeyboardInputManager(ZephyrEngineSpecializations) _publishDebugChargeForKeyCode:touchLocation:]E11chargeToken
+ __ZZ99-[TIKeyboardInputManager(ZephyrEngineSpecializations) _publishDebugChargeForKeyCode:touchLocation:]E11decisionSeq
+ __ZZ99-[TIKeyboardInputManager(ZephyrEngineSpecializations) _publishDebugChargeForKeyCode:touchLocation:]E13decisionToken
+ __ZZ99-[TIKeyboardInputManager(ZephyrEngineSpecializations) _publishDebugChargeForKeyCode:touchLocation:]E9chargeSeq
+ __ZZL20TIIsSystemNoiseLabelP8NSStringE12dateDetector
+ __ZZL20TIIsSystemNoiseLabelP8NSStringE12onceTokenDay
+ __ZZL20TIIsSystemNoiseLabelP8NSStringE13exactNoiseSet
+ __ZZL20TIIsSystemNoiseLabelP8NSStringE13onceTokenTime
+ __ZZL20TIIsSystemNoiseLabelP8NSStringE13pureTimeRegex
+ __ZZL20TIIsSystemNoiseLabelP8NSStringE14onceTokenExact
+ __ZZL20TIIsSystemNoiseLabelP8NSStringE15onceTokenPrefix
+ __ZZL20TIIsSystemNoiseLabelP8NSStringE15prefixNoiseList
+ __ZZL20TIIsSystemNoiseLabelP8NSStringE8dayRegex
+ __ZZL20TIIsSystemNoiseLabelP8NSStringE9onceToken
+ __ZZL27TIDeduplicateCollectionItemRKNSt3__110shared_ptrI14TIScreenUINodeEEEN16SubtreeCollector7collectES4_b
+ __ZZL33TIGetShowAllKeysDebugHitAreaValuevE9onceToken
+ ___35-[TIWordSearch setOnScreenContext:]_block_invoke
+ ___99-[TIKeyboardInputManager(ZephyrEngineSpecializations) _publishDebugChargeForKeyCode:touchLocation:]_block_invoke
+ ____ZL20TIIsSystemNoiseLabelP8NSString_block_invoke
+ ____ZL20TIIsSystemNoiseLabelP8NSString_block_invoke_2
+ ____ZL20TIIsSystemNoiseLabelP8NSString_block_invoke_3
+ ____ZL20TIIsSystemNoiseLabelP8NSString_block_invoke_4
+ ____ZL20TIIsSystemNoiseLabelP8NSString_block_invoke_5
+ ____ZL21libmecabraLibraryCorePPc_block_invoke
+ ____ZL33TIGetShowAllKeysDebugHitAreaValuev_block_invoke
+ ____ZL42getMecabraContextSetStringContextSymbolLocv_block_invoke
+ ___block_descriptor_48_a8_32r_e5_v8?0l
+ ___block_descriptor_96_a8_32r40r48r56r64r_e50_v64?0r*8{CGRect={CGPoint=dd}{CGSize=dd}}16Q48^B56l
+ ___copy_helper_block_a8_32r40r48r56r64r
+ ___destroy_helper_block_a8_32r40r48r56r64r
+ _dlerror
+ _dlsym
+ _notify_post
+ _notify_set_state
+ _objc_msgSend$_publishDebugChargeForKeyCode:touchLocation:
+ _objc_msgSend$dataDetectorWithTypes:error:
+ _objc_msgSend$onScreenContextForCandidates
+ _objc_msgSend$range
+ _objc_msgSend$replaceMatchesInString:options:range:withTemplate:
+ _objc_msgSend$replaceOccurrencesOfString:withString:options:range:
+ _objc_msgSend$setOnScreenContext:
+ _objc_msgSend$setOnScreenStringContext:
- __ZN2TI8Favonius10BeamSearch20choose_hit_test_nodeERKN3WTF6RefPtrINS0_10SearchNodeEEERKNS3_INS0_8KeyMatchEEES7_S7_
CStrings:
+ "%s  Setting OnScreenContext to MecabraContext(%p) %{sensitive}@"
+ "(NULL)"
+ "-[TIMecabraEnvironmentContextWrapper setOnScreenStringContext:]"
+ "/usr/lib/libmecabra.dylib"
+ "/usr/local/lib/libmecabra.dylib"
+ "Button"
+ "CollectionItem"
+ "EditableText"
+ "Element("
+ "MecabraContextSetStringContext"
+ "Scrollable"
+ "ShowAllKeysDebugHitArea"
+ "[ \\t\\r\\n,]"
+ "^[\\d\\s,:]+$"
+ "^\\d{1,2}/\\d{1,2}\\s*\\d{1,2}:\\d{2}$|^\\d{1,2}/\\d{1,2}$|^\\d{1,2}:\\d{2}$|^\\d{1,4}/\\d{1,2}/\\d{1,2}$"
+ "accessibilityLabel:\\s*\"((?:[^\"\\\\]|\\\\.)+)\""
+ "com.apple.keyboard.debugCharge"
+ "com.apple.keyboard.debugDecision"
+ "content:\\s*([A-Za-z0-9_]+)"
+ "scrollableAxes: [horizontal,"
+ "scrollableAxes: [horizontal]"
+ "scrollableAxes: [vertical,"
+ "scrollableAxes: [vertical]"
+ "text:\\s*\"((?:[^\"\\\\]|\\\\.)+)\""
+ "オンライン:"
+ "オンライン中"
+ "グループビデオ通話を開始"
+ "グループ音声通話を開始"
+ "スタンプ"
+ "ビデオ通話を開始"
+ "プロフィールを開く"
+ "プロフィール写真"
+ "メッセージの開封証明を表示"
+ "メディア"
+ "令和|平成|昭和|大正|明治|[\\(（][月火水木金土日](?:曜日)?[\\)）]|[\\(（]?(?:星期[一二三四五六日天]|[周週][一二三四五六日天])[\\)）]?|(?:^|[^0-9])[月火水木金土日](?:曜日?|(?=[\\s,，、\\)）]))|昨天|今天|昨日|今日|午前|午[後后]|上午|下午|晚上|早上|凌晨|[\\s,\\.，、]"
+ "关注后可邀请通话"
+ "大頭貼"
+ "头像"
+ "对方头像"
+ "對方頭像"
+ "已讀"
+ "已读"
+ "年"
+ "我的头像"
+ "我的頭像"
+ "投稿"
+ "既読"
+ "日"
+ "最近のメッセージに移動"
+ "月"
+ "貼圖"
+ "音声通話を開始"
+ "頭像"
+ "￼"
+ "\xf0\xf0a"
- "%s  Input mode %@ includes screen contents: %@, with length %@"
- "-[TIKeyboardInputManagerMecabra updateDocumentContext]"
- "Text\\([^)]*text:\\s*\"([^\"]+)\""
- "accessibilityLabel:\\s*\"([^\"]+)\""
- "on_screen_context_for_candidates_predictions"
- "\xf0\xf0!"

```
