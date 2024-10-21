## libmobileassetd.dylib

> `/usr/lib/libmobileassetd.dylib`

```diff

-1309.42.4.0.0
-  __TEXT.__text: 0x261afc
+1309.42.5.0.0
+  __TEXT.__text: 0x261abc
   __TEXT.__auth_stubs: 0x2370
-  __TEXT.__objc_stubs: 0x1fa00
-  __TEXT.__objc_methlist: 0xef90
+  __TEXT.__objc_stubs: 0x1fa20
+  __TEXT.__objc_methlist: 0xefa0
   __TEXT.__const: 0x494e
-  __TEXT.__objc_methname: 0x372cd
-  __TEXT.__cstring: 0x4c92c
+  __TEXT.__objc_methname: 0x37303
+  __TEXT.__cstring: 0x4c76c
   __TEXT.__objc_classname: 0xd7b
   __TEXT.__objc_methtype: 0x3562
-  __TEXT.__oslogstring: 0x3114b
+  __TEXT.__oslogstring: 0x310d5
   __TEXT.__gcc_except_tab: 0x2544
   __TEXT.__dlopen_cstrs: 0x5a
   __TEXT.__swift5_typeref: 0x10c4

   __DATA_CONST.__got: 0x6c8
   __DATA_CONST.__auth_ptr: 0x9c8
   __DATA_CONST.__const: 0x66b8
-  __DATA_CONST.__cfstring: 0x316e0
+  __DATA_CONST.__cfstring: 0x315a0
   __DATA_CONST.__objc_classlist: 0x3e0
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8b28
+  __DATA_CONST.__objc_selrefs: 0x8b30
   __DATA_CONST.__objc_intobj: 0x3f0
-  __DATA_CONST.__objc_arraydata: 0x988
+  __DATA_CONST.__objc_arraydata: 0x940
   __DATA_CONST.__objc_arrayobj: 0x1b0
   __DATA_CONST.__objc_dictobj: 0xf0
   __DATA.__objc_const: 0x14528

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 8277
-  Symbols:   14852
-  CStrings:  15770
+  Functions: 8278
+  Symbols:   14855
+  CStrings:  15760
 
Symbols:
+ +[MADAutoAssetSecure isPersonalizationOrGraftingRequired:forSetDescriptor:]
+ +[MADAutoAssetSecure isPersonalizationOrGraftingRequired:forSetDescriptor:].cold.1
+ __152-[MADAutoAssetSecure _personalizeGraftSetDownloaded:forSetDescriptor:allowingNetwork:requiringPersonalization:requiringGrafting:shouldGraft:completion:]_block_invoke.1101
+ __152-[MADAutoAssetSecure _personalizeGraftSetDownloaded:forSetDescriptor:allowingNetwork:requiringPersonalization:requiringGrafting:shouldGraft:completion:]_block_invoke.1101.cold.1
+ __152-[MADAutoAssetSecure _personalizeGraftSetDownloaded:forSetDescriptor:allowingNetwork:requiringPersonalization:requiringGrafting:shouldGraft:completion:]_block_invoke.1111
+ __45+[MADAutoAssetScheduler resumeFromPersisted:]_block_invoke.1010
+ __45+[MADAutoAssetScheduler resumeFromPersisted:]_block_invoke.1057
+ __54-[MADAutoAssetScheduler _registerForAndStartActivity:]_block_invoke.1106
+ __54-[MADAutoAssetScheduler _registerForAndStartActivity:]_block_invoke.1106.cold.1
+ __54-[MADAutoAssetScheduler _registerForAndStartActivity:]_block_invoke.1113
+ __60+[MADAutoAssetSecure mapToExclave:forDescriptor:completion:]_block_invoke.1089
+ __60+[MADAutoAssetSecure mapToExclave:forDescriptor:completion:]_block_invoke.1090
+ __60+[MADAutoAssetSecure mapToExclave:forDescriptor:completion:]_block_invoke.1091
+ __block_literal_global.1007
+ __block_literal_global.1009
+ __block_literal_global.1158
+ _objc_msgSend$isPersonalizationOrGraftingRequired:forSetDescriptor:
- GCC_except_table63
- __152-[MADAutoAssetSecure _personalizeGraftSetDownloaded:forSetDescriptor:allowingNetwork:requiringPersonalization:requiringGrafting:shouldGraft:completion:]_block_invoke.1107
- __152-[MADAutoAssetSecure _personalizeGraftSetDownloaded:forSetDescriptor:allowingNetwork:requiringPersonalization:requiringGrafting:shouldGraft:completion:]_block_invoke.1107.cold.1
- __152-[MADAutoAssetSecure _personalizeGraftSetDownloaded:forSetDescriptor:allowingNetwork:requiringPersonalization:requiringGrafting:shouldGraft:completion:]_block_invoke.1117
- __45+[MADAutoAssetScheduler resumeFromPersisted:]_block_invoke.1034
- __45+[MADAutoAssetScheduler resumeFromPersisted:]_block_invoke.1081
- __54-[MADAutoAssetScheduler _registerForAndStartActivity:]_block_invoke.1130
- __54-[MADAutoAssetScheduler _registerForAndStartActivity:]_block_invoke.1130.cold.1
- __54-[MADAutoAssetScheduler _registerForAndStartActivity:]_block_invoke.1137
- __60+[MADAutoAssetSecure mapToExclave:forDescriptor:completion:]_block_invoke.1095
- __60+[MADAutoAssetSecure mapToExclave:forDescriptor:completion:]_block_invoke.1096
- __60+[MADAutoAssetSecure mapToExclave:forDescriptor:completion:]_block_invoke.1097
- __block_literal_global.1031
- __block_literal_global.1033
CStrings:
+ "\n[AUTO-SECURE][AUTO-GRAFT-REMOVE-ALL] {%!{(MISSING)public}@} endAccess ERROR | error:%!{(MISSING)public}@ | ungraftDescriptor:%!{(MISSING)public}@ | success:%!{(MISSING)public}@"
+ "2.2.20"
+ "CrystalB"
+ "Starting built-in MobileAsset brain built Oct 15 2024 22:29:25"
+ "Starting downloaded MobileAsset brain (version: %!@(MISSING)) built Oct 15 2024 22:29:25"
+ "isPersonalizationOrGraftingRequired:forSetDescriptor:"
- "\n[AUTO-SECURE][AUTO-GRAFT-REMOVE-ALL] {%!{(MISSING)public}@} unable to endAccess | error:%!{(MISSING)public}@ | nextUngraftDescriptor:%!{(MISSING)public}@"
- "\n[AUTO-SECURE][AUTO-GRAFT-REMOVE-ALL] {%!{(MISSING)public}@} unable to initialize SecureMobileAssetBundle | nextUngraftDescriptor:%!{(MISSING)public}@"
- "2.2.19"
- "CrystalBSeed"
- "Starting built-in MobileAsset brain built Oct  8 2024 23:13:29"
- "Starting downloaded MobileAsset brain (version: %!@(MISSING)) built Oct  8 2024 23:13:29"
- "com.apple.MobileAsset.UAF.FM.CodeLM"
- "com.apple.MobileAsset.UAF.FM.GenerativeModels"
- "com.apple.MobileAsset.UAF.Handwriting.Synthesis"
- "com.apple.MobileAsset.UAF.IF.Planner"
- "com.apple.MobileAsset.UAF.Photos.MagicCleanup"
- "com.apple.MobileAsset.UAF.Search.ODLA"
- "com.apple.MobileAsset.UAF.Speech.AutomaticSpeechRecognition"
- "com.apple.MobileAsset.UAF.VoiceAssistant"
- "no secureAssetBundle | nextUngraftDescriptor:%!@(MISSING)"
- "unable to end access | nextUngraftDescriptor:%!@(MISSING)"

```
