## WritingToolsUIService

> `/Applications/WritingToolsUIService.app/WritingToolsUIService`

```diff

-44.502.0.0.0
-  __TEXT.__text: 0x182440
-  __TEXT.__auth_stubs: 0x4e40
+44.504.1.0.0
+  __TEXT.__text: 0x183c90
+  __TEXT.__auth_stubs: 0x4e50
   __TEXT.__objc_methlist: 0x1104
   __TEXT.__const: 0xe7f4
-  __TEXT.__cstring: 0x7fd5
+  __TEXT.__cstring: 0x8025
   __TEXT.__swift5_typeref: 0x27d9e
   __TEXT.__objc_methname: 0x3e4b
   __TEXT.__constg_swiftt: 0x591c

   __TEXT.__swift5_mpenum: 0x18
   __TEXT.__swift5_entry: 0x8
   __TEXT.__unwind_info: 0x49e0
-  __TEXT.__eh_frame: 0x6510
-  __DATA_CONST.__auth_got: 0x2720
+  __TEXT.__eh_frame: 0x6518
+  __DATA_CONST.__auth_got: 0x2728
   __DATA_CONST.__got: 0x1300
-  __DATA_CONST.__auth_ptr: 0x2318
-  __DATA_CONST.__const: 0x8408
+  __DATA_CONST.__auth_ptr: 0x25a0
+  __DATA_CONST.__const: 0x8430
   __DATA_CONST.__objc_classlist: 0x138
   __DATA_CONST.__objc_protolist: 0x140
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 6806
-  Symbols:   2388
-  CStrings:  1621
+  Functions: 6809
+  Symbols:   2389
+  CStrings:  1620
 
Symbols:
+ _$s27GenerativeAssistantSettings0abC8ProviderC11LLMProviderO20localizedDisplayNameSSyF
CStrings:
+ "\n\nWhen generating an image, just show the image. DO NOT comment on the image or how you generated it, leaving the \"body\" field of the JSON output as an empty string if the description of the image is the only content you would put in that field. You should however include a \"refinements\" field with a list of potential refinements for the image. If the user requests text and an image, make sure you ACTUALLY generate the image.\n\n*Phase 1*: Understand input.\n\n1. Carefully read the user's prompt and decide if there is enough information to produce a personalized response.\n    - Take into account any attachments that the user may have provided.\n    - If you identify the missing information necessary to complete the document, passing them in the `"
- "\n\nWhen generating an image, just show the image. DO NOT comment on the image or how you generated it, leaving the \"body\" field of the JSON output blank if the description of the image is the only content you would put in that field. If the user requests text and an image, make sure you ACTUALLY generate the image.\n\n*Phase 1*: Understand input.\n\n1. Carefully read the user's prompt and decide if there is enough information to produce a personalized response.\n    - Take into account any attachments that the user may have provided.\n    - If you identify the missing information necessary to complete the document, passing them in the `"
- "ChatGPT Suggestions"

```
