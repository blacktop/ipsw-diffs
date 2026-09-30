## SearchUI

> `/System/Library/PrivateFrameworks/SearchUI.framework/Versions/A/SearchUI`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_mpenum`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH.__data`
- `__DATA_DIRTY.__data`

```diff

-673.0.1.0.0
-  __TEXT.__text: 0xcf958
-  __TEXT.__objc_methlist: 0xf5dc
-  __TEXT.__const: 0x2c84
-  __TEXT.__cstring: 0x3343
-  __TEXT.__oslogstring: 0x25f5
-  __TEXT.__gcc_except_tab: 0x788
+673.0.6.0.0
+  __TEXT.__text: 0xd219c
+  __TEXT.__objc_methlist: 0xf634
+  __TEXT.__const: 0x2f24
+  __TEXT.__cstring: 0x3444
+  __TEXT.__oslogstring: 0x2635
+  __TEXT.__gcc_except_tab: 0x794
   __TEXT.__ustring: 0xa8
   __TEXT.__dlopen_cstrs: 0xb2
-  __TEXT.__swift5_typeref: 0x25ea
-  __TEXT.__constg_swiftt: 0x114c
-  __TEXT.__swift5_reflstr: 0x535
-  __TEXT.__swift5_fieldmd: 0x750
-  __TEXT.__swift5_builtin: 0x64
-  __TEXT.__swift5_assocty: 0x248
-  __TEXT.__swift5_proto: 0x104
-  __TEXT.__swift5_types: 0xc4
+  __TEXT.__swift5_typeref: 0x2c08
+  __TEXT.__constg_swiftt: 0x11bc
+  __TEXT.__swift5_reflstr: 0x56a
+  __TEXT.__swift5_fieldmd: 0x7a0
+  __TEXT.__swift5_builtin: 0x78
+  __TEXT.__swift5_assocty: 0x260
+  __TEXT.__swift5_proto: 0x110
+  __TEXT.__swift5_types: 0xcc
   __TEXT.__swift5_capture: 0x440
   __TEXT.__swift5_protos: 0x20
-  __TEXT.__swift_as_entry: 0xec
-  __TEXT.__swift_as_ret: 0xd4
+  __TEXT.__swift_as_entry: 0xf4
+  __TEXT.__swift_as_ret: 0xdc
   __TEXT.__swift_as_cont: 0x164
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x3a20
-  __TEXT.__eh_frame: 0x19f8
+  __TEXT.__unwind_info: 0x3a80
+  __TEXT.__eh_frame: 0x1a20
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x698
+  __DATA_CONST.__const: 0x6a0
   __DATA_CONST.__objc_classlist: 0x9c8
   __DATA_CONST.__objc_catlist: 0x408
   __DATA_CONST.__objc_protolist: 0x2e0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8580
+  __DATA_CONST.__objc_selrefs: 0x85d8
   __DATA_CONST.__objc_protorefs: 0x78
   __DATA_CONST.__objc_superrefs: 0x5c8
   __DATA_CONST.__objc_arraydata: 0xac0
-  __DATA_CONST.__got: 0x1de8
-  __AUTH_CONST.__const: 0x3b28
+  __DATA_CONST.__got: 0x1e18
+  __AUTH_CONST.__const: 0x3c08
   __AUTH_CONST.__cfstring: 0x3640
-  __AUTH_CONST.__objc_const: 0x1ac68
+  __AUTH_CONST.__objc_const: 0x1ac90
   __AUTH_CONST.__objc_intobj: 0x150
   __AUTH_CONST.__objc_arrayobj: 0x9c0
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH_CONST.__auth_got: 0x1300
-  __AUTH.__objc_data: 0x35e8
+  __AUTH_CONST.__auth_got: 0x13f8
+  __AUTH.__objc_data: 0x3408
   __AUTH.__data: 0x3a0
-  __DATA.__objc_ivar: 0xb94
-  __DATA.__data: 0x2598
-  __DATA.__bss: 0x9c8
-  __DATA.__common: 0xd8
-  __DATA_DIRTY.__objc_data: 0x3828
+  __DATA.__objc_ivar: 0xb98
+  __DATA.__data: 0x2648
+  __DATA.__bss: 0xb38
+  __DATA.__common: 0xe8
+  __DATA_DIRTY.__objc_data: 0x3a08
   __DATA_DIRTY.__data: 0xac0
-  __DATA_DIRTY.__bss: 0x1760
+  __DATA_DIRTY.__bss: 0x1798
   __DATA_DIRTY.__common: 0x58
   - /System/Library/Frameworks/AVFAudio.framework/Versions/A/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5856
-  Symbols:   13385
-  CStrings:  790
+  Functions: 5896
+  Symbols:   13432
+  CStrings:  796
 
Symbols:
+ +[SearchUICardViewController _loadAndEnrichCardSectionsFromCard:cardLoader:withCompletionHandler:]
+ +[SearchUIUtilities appClipIdentifierFromBundleIdentifier:]
+ +[SearchUIUtilities openURLWithWorkspace:]
+ -[SearchUIButtonBackgroundView setUsesThinMaterialBackground:]
+ -[SearchUIButtonBackgroundView usesThinMaterialBackground]
+ -[SearchUICollectionView searchui_observeFirstResponderForWindow:]
+ -[SearchUICollectionView searchui_stopObservingFirstResponder]
+ OBJC_IVAR_$_SearchUIButtonBackgroundView._usesThinMaterialBackground
+ OBJC_IVAR_$_SearchUICollectionView._observedFirstResponderWindow
+ _CGRectIsEmpty
+ _NSURLIsReadableKey
+ _SearchUIFirstResponderObservingContext
+ _SearchUIResultPlatterMaxCornerRadius
+ __42+[SearchUIUtilities openURLWithWorkspace:]_block_invoke
+ __98+[SearchUICardViewController _loadAndEnrichCardSectionsFromCard:cardLoader:withCompletionHandler:]_block_invoke
+ ___42+[SearchUIUtilities openURLWithWorkspace:]_block_invoke
+ ___98+[SearchUICardViewController _loadAndEnrichCardSectionsFromCard:cardLoader:withCompletionHandler:]_block_invoke
+ ___98+[SearchUICardViewController _loadAndEnrichCardSectionsFromCard:cardLoader:withCompletionHandler:]_block_invoke_2
+ ___block_descriptor_48_e8_32s40bs_e28_v24?0"SFCard"8"NSError"16l
+ _associated conformance 8SearchUI11SiriFTEViewV05SwiftB04ViewAA4BodyAdEP_AdE
+ _associated conformance So16NSURLResourceKeyaSHSCSQ
+ _dladdr
+ _objc_msgSend$_loadAndEnrichCardSectionsFromCard:cardLoader:withCompletionHandler:
+ _objc_msgSend$canLoadCard:
+ _objc_msgSend$cardLoader
+ _objc_msgSend$loadCard:completionHandler:
+ _objc_msgSend$openURLWithWorkspace:
+ _objc_msgSend$removeObserver:forKeyPath:context:
+ _objc_msgSend$searchui_observeFirstResponderForWindow:
+ _objc_msgSend$searchui_stopObservingFirstResponder
+ _objc_msgSend$setScrollerInsets:
+ _objc_msgSend$usesThinMaterialBackground
+ _symbolic _____ 7SwiftUI13TextAlignmentO
+ _symbolic _____ 8SearchUI11SiriFTEViewV
+ _symbolic _____ So16NSURLResourceKeya
+ _symbolic _____Sg 7SwiftUI4FontV6DesignO
+ _symbolic ___________yAByAByAByABy_____y_____yAByAByAByABy__________y_____SgGG_____GAFy_____GG_____y_____GG_AByABy__________GAUGATQPGGAUGAUG_____GAFy_____GG_____GAAt 7SwiftUI6SpacerV AA15ModifiedContentV AA6VStackV AA05TupleE0V AA5ImageV AA30_EnvironmentKeyWritingModifierV AA4FontV AA12_FrameLayoutV AK5ScaleO AA016_ForegroundStyleL0V AA017HierarchicalShapeR0V AA4TextV AA08_PaddingO0V AA05_FlexnO0V AA0U9AlignmentO AA010_FixedSizeO0V
+ _symbolic _____yAAyAAyAAyAAy_____y_____yAAyAAyAAyAAy__________y_____SgGG_____GAEy_____GG_____y_____GG_AAyAAy__________GATGASQPGGATGATG_____GAEy_____GG_____G 7SwiftUI15ModifiedContentV AA6VStackV AA05TupleD0V AA5ImageV AA30_EnvironmentKeyWritingModifierV AA4FontV AA12_FrameLayoutV AI5ScaleO AA016_ForegroundStyleK0V AA017HierarchicalShapeQ0V AA4TextV AA08_PaddingN0V AA05_FlexmN0V AA0T9AlignmentO AA010_FixedSizeN0V
+ _symbolic _____yAAyAAyAAy__________y_____SgGG_____GACy_____GG_____y_____GG 7SwiftUI15ModifiedContentV AA5ImageV AA30_EnvironmentKeyWritingModifierV AA4FontV AA12_FrameLayoutV AE5ScaleO AA016_ForegroundStyleI0V AA017HierarchicalShapeO0V
+ _symbolic _____yAAyAAyAAy__________y_____SgGG_____GACy_____GG_____y_____GG_AAyAAy__________GARGAQt 7SwiftUI15ModifiedContentV AA5ImageV AA30_EnvironmentKeyWritingModifierV AA4FontV AA12_FrameLayoutV AE5ScaleO AA016_ForegroundStyleI0V AA017HierarchicalShapeO0V AA4TextV AA08_PaddingL0V
+ _symbolic _____yAAyAAyAAy_____y_____yAAyAAyAAyAAy__________y_____SgGG_____GAEy_____GG_____y_____GG_AAyAAy__________GATGASQPGGATGATG_____GAEy_____GG 7SwiftUI15ModifiedContentV AA6VStackV AA05TupleD0V AA5ImageV AA30_EnvironmentKeyWritingModifierV AA4FontV AA12_FrameLayoutV AI5ScaleO AA016_ForegroundStyleK0V AA017HierarchicalShapeQ0V AA4TextV AA08_PaddingN0V AA05_FlexmN0V AA0T9AlignmentO
+ _symbolic _____yAAyAAy__________y_____SgGG_____GACy_____GG 7SwiftUI15ModifiedContentV AA5ImageV AA30_EnvironmentKeyWritingModifierV AA4FontV AA12_FrameLayoutV AE5ScaleO
+ _symbolic _____yAAyAAy_____y_____yAAyAAyAAyAAy__________y_____SgGG_____GAEy_____GG_____y_____GG_AAyAAy__________GATGASQPGGATGATG_____G 7SwiftUI15ModifiedContentV AA6VStackV AA05TupleD0V AA5ImageV AA30_EnvironmentKeyWritingModifierV AA4FontV AA12_FrameLayoutV AI5ScaleO AA016_ForegroundStyleK0V AA017HierarchicalShapeQ0V AA4TextV AA08_PaddingN0V AA05_FlexmN0V
+ _symbolic _____yAAy__________y_____SgGG_____G 7SwiftUI15ModifiedContentV AA5ImageV AA30_EnvironmentKeyWritingModifierV AA4FontV AA12_FrameLayoutV
+ _symbolic _____yAAy_____y_____yAAyAAyAAyAAy__________y_____SgGG_____GAEy_____GG_____y_____GG_AAyAAy__________GATGASQPGGATGATG 7SwiftUI15ModifiedContentV AA6VStackV AA05TupleD0V AA5ImageV AA30_EnvironmentKeyWritingModifierV AA4FontV AA12_FrameLayoutV AI5ScaleO AA016_ForegroundStyleK0V AA017HierarchicalShapeQ0V AA4TextV AA08_PaddingN0V
+ _symbolic _____y_____G s11_SetStorageC So16NSURLResourceKeya
+ _symbolic _____y_____G s23_ContiguousArrayStorageC So16NSURLResourceKeya
+ _symbolic _____y___________y___________yAEyAEyAEyAEy_____yACyAEyAEyAEyAEy__________y_____SgGG_____GAHy_____GG_____y_____GG_AEyAEy__________GAWGAVQPGGAWGAWG_____GAHy_____GG_____GADQPGG 7SwiftUI13_VariadicViewO4TreeV AA13_HStackLayoutV AA12TupleContentV AA6SpacerV AA08ModifiedI0V AA6VStackV AA5ImageV AA30_EnvironmentKeyWritingModifierV AA4FontV AA06_FrameG0V AQ5ScaleO AA016_ForegroundStyleQ0V AA017HierarchicalShapeV0V AA4TextV AA08_PaddingG0V AA05_FlexsG0V AA0Y9AlignmentO AA010_FixedSizeG0V
+ _symbolic _____y___________y_____yADyADyADy__________y_____SgGG_____GAFy_____GG_____y_____GG_ADyADy__________GAUGATQPGG 7SwiftUI13_VariadicViewO4TreeV AA13_VStackLayoutV AA12TupleContentV AA08ModifiedI0V AA5ImageV AA30_EnvironmentKeyWritingModifierV AA4FontV AA06_FrameG0V AM5ScaleO AA016_ForegroundStyleO0V AA017HierarchicalShapeT0V AA4TextV AA08_PaddingG0V
+ _symbolic _____y_____y___________yADyADyADyADy_____yAByADyADyADyADy__________y_____SgGG_____GAGy_____GG_____y_____GG_ADyADy__________GAVGAUQPGGAVGAVG_____GAGy_____GG_____GACQPGG 7SwiftUI6HStackV AA12TupleContentV AA6SpacerV AA08ModifiedE0V AA6VStackV AA5ImageV AA30_EnvironmentKeyWritingModifierV AA4FontV AA12_FrameLayoutV AM5ScaleO AA016_ForegroundStyleM0V AA017HierarchicalShapeS0V AA4TextV AA08_PaddingP0V AA05_FlexoP0V AA0V9AlignmentO AA010_FixedSizeP0V
+ _symbolic _____y_____y_____yAAyAAyAAyAAy__________y_____SgGG_____GAEy_____GG_____y_____GG_AAyAAy__________GATGASQPGGATG 7SwiftUI15ModifiedContentV AA6VStackV AA05TupleD0V AA5ImageV AA30_EnvironmentKeyWritingModifierV AA4FontV AA12_FrameLayoutV AI5ScaleO AA016_ForegroundStyleK0V AA017HierarchicalShapeQ0V AA4TextV AA08_PaddingN0V
+ _type_layout_string 8SearchUI11SiriFTEViewV
+ _type_layout_string So16NSURLResourceKeya
+ get_witness_table 7SwiftUI6HStackVyAA12TupleContentVyAA6SpacerV_AA08ModifiedE0VyAIyAIyAIyAIyAA6VStackVyAEyAIyAIyAIyAIyAA5ImageVAA30_EnvironmentKeyWritingModifierVyAA4FontVSgGGAA12_FrameLayoutVGAOyAM5ScaleOGGAA016_ForegroundStyleM0VyAA017HierarchicalShapeS0VGG_AIyAIyAA4TextVAA08_PaddingP0VGA9_GA7_QPGGA9_GA9_GAA05_FlexoP0VGAOyAA0V9AlignmentOGGAA010_FixedSizeP0VGAGQPGGAA4ViewHPyHC
- -[SearchUIButtonItemView shouldAvoidBackgroundView]
- GCC_except_table28
- OBJC_IVAR_$_SearchUIButtonItemView._shouldAvoidBackgroundView
- ___87+[SearchUICardViewController _loadAndEnrichCardSectionsFromCard:withCompletionHandler:]_block_invoke
- ___87+[SearchUICardViewController _loadAndEnrichCardSectionsFromCard:withCompletionHandler:]_block_invoke_2
- _objc_msgSend$_loadAndEnrichCardSectionsFromCard:withCompletionHandler:
- _objc_msgSend$shouldAvoidBackgroundView
CStrings:
+ "+[SearchUIUtilities openURL:withCompletion:] called with nil URL; ignoring"
+ "Contradictory frame constraints specified."
+ "Description for first time experience shown to users about Siri AI."
+ "Search for anything or start a conversation with Siri."
+ "SettingToggleSwitch"
+ "Title for Siri AI FTE."
+ "v24@?0@\"SFCard\"8@\"NSError\"16"
- "com.apple.AskSiri"
```
