## fm

> `/usr/bin/fm`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_types`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_entry`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__bss`

```diff

-2.0.59.0.0
-  __TEXT.__text: 0xc2d50
-  __TEXT.__auth_stubs: 0x2ff0
+2.0.62.1.402
+  __TEXT.__text: 0xcd718
+  __TEXT.__auth_stubs: 0x3120
   __TEXT.__objc_stubs: 0x260
   __TEXT.__objc_methlist: 0x104
-  __TEXT.__const: 0x4254
-  __TEXT.__constg_swiftt: 0xdb4
-  __TEXT.__swift5_typeref: 0x1293
+  __TEXT.__const: 0x4364
+  __TEXT.__constg_swiftt: 0xe04
+  __TEXT.__swift5_typeref: 0x13bb
   __TEXT.__swift5_builtin: 0xb4
-  __TEXT.__swift5_reflstr: 0xf27
-  __TEXT.__swift5_fieldmd: 0x135c
+  __TEXT.__swift5_reflstr: 0x10a7
+  __TEXT.__swift5_fieldmd: 0x1478
   __TEXT.__swift5_assocty: 0x90
-  __TEXT.__swift5_proto: 0x2d8
+  __TEXT.__swift5_proto: 0x2e4
   __TEXT.__swift5_types: 0x180
-  __TEXT.__cstring: 0x5c5a
+  __TEXT.__cstring: 0x6522
   __TEXT.__swift_as_entry: 0xdc
   __TEXT.__swift_as_ret: 0x19c
   __TEXT.__swift_as_cont: 0x2b0
   __TEXT.__objc_classname: 0x141
-  __TEXT.__objc_methname: 0x77d
+  __TEXT.__objc_methname: 0x81d
   __TEXT.__objc_methtype: 0xb4
-  __TEXT.__swift5_mpenum: 0x3c
-  __TEXT.__swift5_capture: 0x7f4
-  __TEXT.__swift5_protos: 0x8
+  __TEXT.__swift5_mpenum: 0x38
+  __TEXT.__swift5_capture: 0x824
+  __TEXT.__swift5_protos: 0x10
   __TEXT.__oslogstring: 0x48
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x1a30
-  __TEXT.__eh_frame: 0x3f48
-  __DATA_CONST.__const: 0x3158
+  __TEXT.__unwind_info: 0x1ac0
+  __TEXT.__eh_frame: 0x3fb0
+  __DATA_CONST.__const: 0x3368
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__auth_got: 0x1800
-  __DATA_CONST.__got: 0x788
-  __DATA_CONST.__auth_ptr: 0x7f8
-  __DATA.__objc_const: 0xbf0
+  __DATA_CONST.__auth_got: 0x1898
+  __DATA_CONST.__got: 0x7c0
+  __DATA_CONST.__auth_ptr: 0x828
+  __DATA.__objc_const: 0xcd0
   __DATA.__objc_selrefs: 0x138
   __DATA.__objc_data: 0xa0
-  __DATA.__data: 0x20a0
+  __DATA.__data: 0x2170
   __DATA.__bss: 0x5500
-  __DATA.__common: 0x298
+  __DATA.__common: 0x2e8
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/FoundationModels.framework/Versions/A/FoundationModels
   - /System/Library/Frameworks/ImageIO.framework/Versions/A/ImageIO
   - /System/Library/Frameworks/Network.framework/Versions/A/Network
   - /System/Library/Frameworks/Security.framework/Versions/A/Security
+  - /System/Library/Frameworks/_Vision_FoundationModels.framework/Versions/A/_Vision_FoundationModels
   - /System/Library/PrivateFrameworks/ArgumentParserInternal.framework/Versions/A/ArgumentParserInternal
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/swift/libswiftAVFoundation.dylib
+  - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
+  - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIOKit.dylib
+  - /usr/lib/swift/libswiftMLCompute.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftSynchronization.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1853
-  Symbols:   1179
-  CStrings:  536
+  Functions: 1913
+  Symbols:   1212
+  CStrings:  579
 
Symbols:
+ _$s16FoundationModels10AttachmentV5labelyACyxGSSF
+ _$s16FoundationModels10AttachmentVA2A05ImageC7ContentVRszlE8imageURL11orientationACyAEG0A00G0V_So26CGImagePropertyOrientationVSgtcfC
+ _$s16FoundationModels10AttachmentVMn
+ _$s16FoundationModels10AttachmentVyxGAA19PromptRepresentableAAMc
+ _$s16FoundationModels20LanguageModelSessionC13ToolCallErrorV010underlyingH0s0H0_pvg
+ _$s16FoundationModels20LanguageModelSessionC13ToolCallErrorV4toolAA0F0_pvg
+ _$s16FoundationModels20LanguageModelSessionC13ToolCallErrorVMa
+ _$s16FoundationModels20LanguageModelSessionC7prewarm12promptPrefixyAA6PromptVSg_tF
+ _$s16FoundationModels22ImageAttachmentContentVMn
+ _$s16FoundationModels4ToolMp
+ _$s16FoundationModels4ToolP11descriptionSSvgTj
+ _$s16FoundationModels4ToolP4nameSSvgTj
+ _$s22ArgumentParserInternal0A4HelpVs32ExpressibleByStringInterpolationAAMc
+ _$s24_Vision_FoundationModels17BarcodeReaderToolV0bC00F0AAMc
+ _$s24_Vision_FoundationModels17BarcodeReaderToolV4name11descriptionACSSSg_AFtcfC
+ _$s24_Vision_FoundationModels17BarcodeReaderToolVMa
+ _$s24_Vision_FoundationModels17BarcodeReaderToolVMn
+ _$s24_Vision_FoundationModels7OCRToolV0bC04ToolAAMc
+ _$s24_Vision_FoundationModels7OCRToolV4name11descriptionACSSSg_AFtcfC
+ _$s24_Vision_FoundationModels7OCRToolVMa
+ _$s24_Vision_FoundationModels7OCRToolVMn
+ _$ss11_StringGutsV20fastUTF8ScalarLength10startingAtS2i_tF
+ _$ss15ContinuousClockV7InstantV1loiySbAD_ADtFZ
+ _$ss15ContinuousClockV7InstantV8advanced2byADs8DurationV_tF
+ _$ss15ContinuousClockV7InstantVSLsMc
+ _$ss32ExpressibleByStringInterpolationPss07DefaultcD0V0cD0RtzrlE06stringD0xAD_tcfC
+ _$ss8DurationV1loiySbAB_ABtFZ
+ __swift_FORCE_LOAD_$_swiftAVFoundation
+ __swift_FORCE_LOAD_$_swiftAccelerate
+ __swift_FORCE_LOAD_$_swiftCompression
+ __swift_FORCE_LOAD_$_swiftCoreMIDI
+ __swift_FORCE_LOAD_$_swiftMLCompute
+ __swift_FORCE_LOAD_$_swiftQuartzCore
+ _swift_getTupleTypeMetadata2
- _$s16FoundationModels12InstructionsVAA0C13RepresentableAAWP
CStrings:
+ " --image value(s). Provide at most one --label per --image."
+ " --label value(s) for "
+ " DENIED by ancestor policy"
+ " FAIL: no audit token AND no path req=\""
+ " FAIL: token-present-but-secCode-failed (likely pidversion race) req=\""
+ " denied by policy"
+ " fm> [Cancelled.]\n"
+ " identifiably signed"
+ " is not an identifiable signer"
+ " label "
+ " not identifiably signed"
+ " via=audit-token req=\""
+ "'\nfm count-tokens -i 'You are a helpful assistant' '"
+ "' is not enabled."
+ "' | fm count-tokens"
+ "--label has no effect without an image-using tool. Enable --tool barcode or --tool ocr (or drop the --label flag)."
+ "--save-transcript <f>"
+ ". /tools add <name> · /tools remove <name>"
+ ". Enable with /tools add <name>."
+ "/resume requires a session name. Use /sessions to list saved sessions."
+ "/tools [add|remove <name>]"
+ "/tools add requires a tool name (e.g. /tools add barcode)"
+ "/tools remove requires a tool name (e.g. /tools remove ocr)"
+ "A short, descriptive title for this conversation — 2 to 4 lowercase words joined by hyphens, e.g. swift-concurrency, recipe-suggestions, code-review"
+ "Built-in tool to enable ("
+ "Built-in tool to enable (repeatable). Known: "
+ "Cannot specify both --resume and --instructions. The transcript already contains its instructions."
+ "Continue a saved conversation from its transcript"
+ "Continue an earlier conversation: load a saved transcript so the model picks up with its previous turns as context"
+ "Count the number of tokens the request would consume using the on-device system model's tokenizer. Supports positional prompts, --text and --image segments, --instructions, and --resume.\n\nWhen stdout is a terminal the output is prefixed with 'Token count: '; when piped or redirected (or when --quiet is passed) only the integer is printed. When no prompt is given on the command line, the prompt is read from standard input if stdin is piped."
+ "Failed to resume: "
+ "Format responses using Markdown: use headings (#, ##, ###), bold (**text**), inline code (`text`), fenced code blocks, and bullet lists (- item). Do NOT wrap the entire response in a code fence."
+ "Label for the corresponding --image (paired by order)"
+ "Label for the corresponding --image (repeatable, paired by order). Requires --tool. Defaults to 'image_<index>'."
+ "List, add, or remove built-in tools ("
+ "No built-in tools are available in this build."
+ "No built-in tools are available in this build. Drop the --tool flag."
+ "No tools enabled. Known: "
+ "Press Ctrl+C again to exit."
+ "Private Cloud Compute is not available in this context. Please use the Terminal app."
+ "Save the transcript to a file after responding. An absolute path is used as-is; a bare filename is saved in the current directory."
+ "Save transcript to a file after responding"
+ "The --schema option is not supported with the count-tokens command"
+ "The --verbose option is not supported with the count-tokens command. Use --quiet for bare-integer output in scripts."
+ "Tools are available for this conversation. When the user's request matches one of\nthe available tools, you MUST invoke the tool — do not answer from memory, do not\nask the user to run it themselves, and do not describe what the tool would do.\nCall the tool, then base your reply on its result.\n\nAvailable tools:\n"
+ "Transcript saved to: "
+ "Use /tools to list active tools."
+ "Warning: Failed to save transcript '"
+ "Y@c(pvFvndA$geu%gd[="
+ "Y@c(pvFvndA$p?['neO="
+ "echo 'What is Swift?' | fm count-tokens"
+ "fdBwnTF'VTS%pT&y"
+ "fdBwnTF'VTS%pT&yVTqyozc'ndZJ"
+ "fm count-tokens '"
+ "fm count-tokens 'Hello world'"
+ "fm count-tokens 'What is Swift?'"
+ "fm count-tokens --image photo.jpg --text 'Describe this image'"
+ "fm count-tokens --resume session.json 'Follow up'"
+ "fm count-tokens -i 'Answer concisely'"
+ "fm count-tokens -i 'You are a helpful assistant' 'What is Swift?'"
+ "idleExitHintExpiry"
+ "interruptRequested"
+ "lastCancelAt"
+ "nd_yo{_}gzyypvNvf?F\"YzS%pT&yYy_ypz>}ozS!VvOuoz^tfdBwnTF'VTS%pT&y"
+ "nextImageLabelID"
+ "no Terminal.app ancestor in process chain"
+ "pass2 FAILED: boundary pid="
+ "pass2 OK boundary pid="
+ "pass3 FAILED: no com.apple.Terminal ancestor in chain"
+ "pass3 OK com.apple.Terminal ancestor present"
+ "pendingImageLabels"
+ "saveTranscriptPath"
+ "statusNotice"
+ "tools"
+ "walkToSessionBoundary FAILED: deniedAncestor pid="
- " FAIL: no audit token AND no path"
- " FAIL: token-present-but-secCode-failed (likely pidversion race)"
- " via=audit-token result="
- "'\nfm token-count -i 'You are a helpful assistant' '"
- "' | fm token-count"
- "--load-transcript <f>"
- "--save-transcript <n>"
- "/[a-z][a-z0-9]*(-[a-z][a-z0-9]*){1,2}/"
- "/load requires a session name. Use /history to list sessions."
- "2-3 hyphen-separated lowercase words suitable for a filename, e.g. swift-concurrency, recipe-suggestions, code-review"
- "Cannot specify both --load-transcript and --instructions. The transcript already contains its instructions."
- "Count the number of tokens the request would consume using the on-device system model's tokenizer. Supports positional prompts, --text and --image segments, --instructions, and --load-transcript.\n\nWhen stdout is a terminal the output is prefixed with 'Token count: '; when piped or redirected (or when --quiet is passed) only the integer is printed. When no prompt is given on the command line, the prompt is read from standard input if stdin is piped."
- "Failed to load: "
- "Format responses using Markdown: use headings (#, ##, ###),\nbold (**text**), inline code (`text`), fenced code blocks,\nand bullet lists (- item). Do NOT wrap the entire response in a code fence."
- "Loaded session '"
- "PCC inference is not available in this context."
- "Path to a saved transcript"
- "Path to a saved transcript for conversational context"
- "Save the session transcript to ~/.fm/sessions/<name> after responding"
- "Save transcript after responding"
- "The --schema option is not supported with the token-count command"
- "The --verbose option is not supported with the token-count command. Use --quiet for bare-integer output in scripts."
- "Warning: Failed to save session '"
- "appleSigned pid="
- "echo 'What is Swift?' | fm token-count"
- "fm token-count '"
- "fm token-count 'Hello world'"
- "fm token-count 'What is Swift?'"
- "fm token-count --image photo.jpg --text 'Describe this image'"
- "fm token-count --load-transcript session.json 'Follow up'"
- "fm token-count -i 'Answer concisely'"
- "fm token-count -i 'You are a helpful assistant' 'What is Swift?'"
```
