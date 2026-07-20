## TextComposerRuntime

> `/System/Library/PrivateFrameworks/TextComposerRuntime.framework/Versions/A/TextComposerRuntime`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_protos`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__AUTH.__objc_data`
- `__DATA_DIRTY.__objc_data`

```diff

-211.18.0.0.0
-  __TEXT.__text: 0x742cc
-  __TEXT.__objc_methlist: 0x4f8
-  __TEXT.__const: 0x3b64
-  __TEXT.__cstring: 0x12397
-  __TEXT.__oslogstring: 0x26b3
-  __TEXT.__constg_swiftt: 0xaa4
-  __TEXT.__swift5_typeref: 0x1839
+211.20.0.0.0
+  __TEXT.__text: 0x771fc
+  __TEXT.__objc_methlist: 0x4d8
+  __TEXT.__const: 0x3c84
+  __TEXT.__cstring: 0x12447
+  __TEXT.__oslogstring: 0x2873
+  __TEXT.__constg_swiftt: 0xad8
+  __TEXT.__swift5_typeref: 0x17d5
   __TEXT.__swift5_builtin: 0x64
-  __TEXT.__swift5_reflstr: 0xb62
-  __TEXT.__swift5_fieldmd: 0xf0c
+  __TEXT.__swift5_reflstr: 0xc02
+  __TEXT.__swift5_fieldmd: 0xfc4
   __TEXT.__swift5_assocty: 0x2b0
   __TEXT.__swift5_proto: 0x25c
-  __TEXT.__swift5_types: 0xf4
-  __TEXT.__swift_as_entry: 0x184
-  __TEXT.__swift_as_ret: 0x19c
-  __TEXT.__swift_as_cont: 0x43c
+  __TEXT.__swift5_types: 0xf8
+  __TEXT.__swift_as_entry: 0x180
+  __TEXT.__swift_as_ret: 0x1a4
+  __TEXT.__swift_as_cont: 0x45c
   __TEXT.__swift5_protos: 0x10
-  __TEXT.__swift5_capture: 0xdf4
-  __TEXT.__unwind_info: 0x1ec0
-  __TEXT.__eh_frame: 0x5370
+  __TEXT.__swift5_capture: 0xdb0
+  __TEXT.__unwind_info: 0x1f40
+  __TEXT.__eh_frame: 0x5528
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3a0
+  __DATA_CONST.__objc_selrefs: 0x390
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x3c20
-  __AUTH_CONST.__objc_const: 0xa90
-  __AUTH_CONST.__auth_got: 0x16a0
+  __AUTH_CONST.__const: 0x3bd0
+  __AUTH_CONST.__objc_const: 0xa88
+  __AUTH_CONST.__auth_got: 0x1740
   __AUTH.__objc_data: 0x130
-  __AUTH.__data: 0x5f0
-  __DATA.__data: 0xab8
+  __AUTH.__data: 0x6d0
+  __DATA.__data: 0xaf8
   __DATA.__bss: 0x3f80
-  __DATA.__common: 0x48
+  __DATA.__common: 0x60
   __DATA_DIRTY.__objc_data: 0x170
-  __DATA_DIRTY.__data: 0xa18
+  __DATA_DIRTY.__data: 0xa38
   __DATA_DIRTY.__bss: 0xa00
   __DATA_DIRTY.__common: 0x58
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /System/Library/PrivateFrameworks/Archetype.framework/Versions/A/Archetype
   - /System/Library/PrivateFrameworks/CoreEmoji.framework/Versions/A/CoreEmoji
   - /System/Library/PrivateFrameworks/FeatureFlags.framework/Versions/A/FeatureFlags
+  - /System/Library/PrivateFrameworks/GenerativeFunctionsFoundation.framework/Versions/A/GenerativeFunctionsFoundation
   - /System/Library/PrivateFrameworks/GenerativeFunctionsInstrumentation.framework/Versions/A/GenerativeFunctionsInstrumentation
   - /System/Library/PrivateFrameworks/GenerativeModels.framework/Versions/A/GenerativeModels
   - /System/Library/PrivateFrameworks/GenerativeModelsFoundation.framework/Versions/A/GenerativeModelsFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2952
-  Symbols:   168
-  CStrings:  294
+  Functions: 3001
+  Symbols:   170
+  CStrings:  305
 
Symbols:
+ _TCTextCompositionAssistantOptionKeyContentWarning
+ _TCTextCompositionAssistantOptionKeySuppressValidation
CStrings:
+ "FeatureBasedModelConfig(\n    modelCatalogAssetBundleID: "
+ "[RewriteSafety] Input scrub threw unexpected error: %@"
+ "[RewriteSafety] Input text was rewritten by safety filter"
+ "[RewriteSafety] Input triggered safety warning: %@"
+ "[RewriteSafety] Output scrub threw unexpected error: %@"
+ "[RewriteSafety] Output triggered safety warning: %@"
+ "[RewriteSafety] Output was rewritten by safety filter"
+ "[RewriteSafety] Safety disabled, skipping all scrubs"
+ "address_forms"
+ "expressive_marker"
+ "formality"
+ "script_balance"
+ "speech_level"
+ "{\n  \"writing_style_patterns\": {\n    \"description\": \"Default writing style patterns to keep email drafts sounding human, clear, and natural (not overly formal or robotic).\",\n    \"vocabulary\": {\n      \"usage\": \"advanced\",\n      \"description\": \"Uses a broader range of words familiar to high-school-educated adults. Includes moderate abstraction, mild figurative language, and commonly used terms, but still widely accessible. Examples: The company is getting bigger quickly. The team fixed the problem fast.\"\n    },\n    \"formatting\": {\n      \"usage\": \"lacking_formatting\",\n      \"description\": \"Keeps formatting minimal and straightforward, typically using plain paragraphs rather than heavy structure. Even without much formatting, aims for readability by keeping paragraphs from becoming overly long. Only use Paragraphs → for narrative or descriptive text; Bulleted/Numbered lists → for items, steps, or options; Tables → only when side-by-side comparison adds value (e.g., pros/cons, data, schedules)\"\n    },\n    \"padding\": {\n      \"usage\": \"balanced_padding\",\n      \"description\": \"Uses a balanced amount of polite softening (brief courtesy phrases, light qualifiers) to sound considerate without adding filler. Stays direct while still sounding warm and human. Examples: In order to → To; Due to the fact that → Because; I would like to say that → just say it\"\n    },\n    \"sentence_structure\": {\n      \"usage\": \"balanced\",\n      \"description\": \"Uses a measured mix of sentence lengths and standard, clear connections (e.g., and, but, because). It balances the need for clarity with the ability to convey multiple concepts across smoothly transitioning sentences.\"\n    },\n    \"grammar\": {\n      \"description\": \"Default punctuation scenarios to keep emails readable and natural. Only uses the predefined scenarios listed for each punctuation type.\",\n      \"patterns\": {\n        \"capitalization\": [\n          \"Salutations & Signatures\"\n        ],\n        \"question_marks\": [\n          \"Requests\",\n          \"Confirmations\"\n        ],\n        \"exclamation_marks\": [\n          \"Gratitude\",\n          \"Enthusiasm\"\n        ],\n        \"commas\": [\n          \"Structure Use\"\n        ],\n        \"periods\": [\n          \"Sentence Endings\"\n        ],\n        \"semicolons\": [\n        \n        ],\n        \"colons\": [\n          \"Lists\",\n          \"Headings\"\n        ],\n        \"parentheses\": [\n          \"Additional Info\"\n        ],\n        \"script_balance\": [\n        \n        ],\n        \"expressive_marker\": [\n        \n        ]\n      }\n    }\n  },\n  \"mail_component_patterns\": {\n    \"description\": \"Default email components that keep drafts feeling natural and appropriately personable for most recipients.\",\n    \"address_forms\": {\n      \"usage\": [],\n      \"description\": \"\"\n    },\n    \"salutations\": {\n      \"usage\": [\n        \"Hi {name},\",\n        \"Hi there,\",\n        \"Coach {name},\",\n        \"Dr. {name}\",\n        \"Good morning, {name}\",\n        \"Good afternoon, {name}\",\n        \"Professor {name}\",\n        \"Mr. {name}\",\n        \"Ms. {name}\",\n        \"Mrs. {name}\",\n        \"Hey {name}\",\n        \"{name},\"\n      ],\n      \"description\": \"Use a simple greeting. Add the recipient’s name when available in {name} to sound more natural.\"\n    },\n    \"openings\": {\n      \"usage\": [\n        \"I wanted to let you know that\",\n        \"I’m reaching out to share that\",\n        \"Just wanted to let you know\",\n        \"I wanted to make you aware that\",\n        \"Thought I’d reach out to let you know\",\n        \"I wanted to touch base to share\",\n        \"I thought I’d let you know\",\n        \"I’m checking in to share\"\n      ],\n      \"description\": \"Optional brief opener. Keep it short and relevant; skip it when the email is very tactical or time-sensitive.\"\n    },\n    \"closings\": {\n      \"usage\": [\n        \"Thanks for your time.\",\n        \"I appreciate your help.\",\n        \"Thanks in advance for your assistance.\",\n        \"Looking forward to hearing from you.\",\n        \"Please let me know if you have any questions.\",\n        \"Let me know if you have any questions.\",\n        \"Happy to answer any questions you have.\",\n        \"Reach out if you need anything.\",\n        \"Feel free to ask if anything’s unclear.\",\n        \"I’m happy to help with anything you need.\",\n        \"Thanks so much!\",\n        \"Really appreciate your help.\",\n        \"Can’t wait to hear your thoughts.\",\n        \"Excited to hear what you think.\",\n        \"Hope to hear from you soon.\"\n      ],\n      \"description\": \"Close with a short, friendly line that matches the tone of the request (more neutral for formal threads; warmer for familiar contacts).\"\n    },\n    \"sign_offs\": {\n      \"usage\": [\n        \"Thanks,\",\n        \"Thank you,\",\n        \"Many thanks,\",\n        \"Best,\",\n        \"All the best,\",\n        \"Take care,\",\n        \"Thanks again,\",\n        \"Talk soon,\",\n        \"See you soon,\",\n        \"Thanks so much,\",\n        \"See you\",\n        \"Until next time,\",\n        \"Chat soon,\"\n      ],\n      \"description\": \"Use a simple sign-off that sounds natural and not overly formal. Prefer consistency within a thread.\"\n    },\n    \"signatures\": {\n      \"usage\": [],\n      \"description\": \"\"\n    }\n  },\n  \"relationship_with_recipient\": {\n    \"category\": \"other\",\n    \"description\": \"Assume you’ve emailed this audience at least once before. Both you and the recipient are comfortable sharing private or everyday information over email in a friendly, respectful way, but not publicly or on social media.\",\n    \"tone_effect\": \"Clear, straightforward, polite. Use conversational phrasing without being overly friendly, expressive, enthusiastic, approachable, familiar, inappropriate.\",\n    \"structure_effect\": \"Standard (simple email flow). Use a clear greeting, a short purpose statement, then the key details/request, and a brief close. Keep paragraphs short, avoid unnecessary headings, and only add bullets/lists when clarity requires it.\",\n    \"content_effect\": \"General (context-first, action-clear). Include only the details needed for the recipient to understand and act. Avoid assumptions about prior knowledge; avoid adding speculative details.\"\n  }\n}"
- "WritingAssistantModelConfig(\n    modelCatalogAssetBundleID: "
- "nicknames"
- "{\n  \"writing_style_patterns\": {\n    \"description\": \"Default writing style patterns to keep email drafts sounding human, clear, and natural (not overly formal or robotic).\",\n    \"vocabulary\": {\n      \"usage\": \"advanced\",\n      \"description\": \"Uses a broader range of words familiar to high-school-educated adults. Includes moderate abstraction, mild figurative language, and commonly used terms, but still widely accessible. Examples: The company is getting bigger quickly. The team fixed the problem fast.\"\n    },\n    \"formatting\": {\n      \"usage\": \"lacking_formatting\",\n      \"description\": \"Keeps formatting minimal and straightforward, typically using plain paragraphs rather than heavy structure. Even without much formatting, aims for readability by keeping paragraphs from becoming overly long. Only use Paragraphs → for narrative or descriptive text; Bulleted/Numbered lists → for items, steps, or options; Tables → only when side-by-side comparison adds value (e.g., pros/cons, data, schedules)\"\n    },\n    \"padding\": {\n      \"usage\": \"balanced_padding\",\n      \"description\": \"Uses a balanced amount of polite softening (brief courtesy phrases, light qualifiers) to sound considerate without adding filler. Stays direct while still sounding warm and human. Examples: In order to → To; Due to the fact that → Because; I would like to say that → just say it\"\n    },\n    \"sentence_structure\": {\n      \"usage\": \"balanced\",\n      \"description\": \"Uses a measured mix of sentence lengths and standard, clear connections (e.g., and, but, because). It balances the need for clarity with the ability to convey multiple concepts across smoothly transitioning sentences.\"\n    },\n    \"grammar\": {\n      \"description\": \"Default punctuation scenarios to keep emails readable and natural. Only uses the predefined scenarios listed for each punctuation type.\",\n      \"patterns\": {\n        \"capitalization\": [\n          \"Salutations & Signatures\"\n        ],\n        \"question_marks\": [\n          \"Requests\",\n          \"Confirmations\"\n        ],\n        \"exclamation_marks\": [\n          \"Gratitude\",\n          \"Enthusiasm\"\n        ],\n        \"commas\": [\n          \"Structure Use\"\n        ],\n        \"periods\": [\n          \"Sentence Endings\"\n        ],\n        \"semicolons\": [\n          \n        ],\n        \"colons\": [\n          \"Lists\",\n          \"Headings\"\n        ],\n        \"parentheses\": [\n          \"Additional Info\"\n        ]\n      }\n    }\n  },\n  \"mail_component_patterns\": {\n    \"description\": \"Default email components that keep drafts feeling natural and appropriately personable for most recipients.\",\n    \"nicknames\": {\n      \"usage\": [],\n      \"description\": \"\"\n    },\n    \"salutations\": {\n      \"usage\": [\n        \"Hi {name},\",\n        \"Hi there,\",\n        \"Coach {name},\",\n        \"Dr. {name}\",\n        \"Good morning, {name}\",\n        \"Good afternoon, {name}\",\n        \"Professor {name}\",\n        \"Mr. {name}\",\n        \"Ms. {name}\",\n        \"Mrs. {name}\",\n        \"Hey {name}\",\n        \"{name},\"\n      ],\n      \"description\": \"Use a simple greeting. Add the recipient’s name when available in {name} to sound more natural.\"\n    },\n    \"openings\": {\n      \"usage\": [\n        \"I wanted to let you know that\",\n        \"I’m reaching out to share that\",\n        \"Just wanted to let you know\",\n        \"I wanted to make you aware that\",\n        \"Thought I’d reach out to let you know\",\n        \"I wanted to touch base to share\",\n        \"I thought I’d let you know\",\n        \"I’m checking in to share\"\n      ],\n      \"description\": \"Optional brief opener. Keep it short and relevant; skip it when the email is very tactical or time-sensitive.\"\n    },\n    \"closings\": {\n      \"usage\": [\n        \"Thanks for your time.\",\n        \"I appreciate your help.\",\n        \"Thanks in advance for your assistance.\",\n        \"Looking forward to hearing from you.\",\n        \"Please let me know if you have any questions.\",\n        \"Let me know if you have any questions.\",\n        \"Happy to answer any questions you have.\",\n        \"Reach out if you need anything.\",\n        \"Feel free to ask if anything’s unclear.\",\n        \"I’m happy to help with anything you need.\",\n        \"Thanks so much!\",\n        \"Really appreciate your help.\",\n        \"Can’t wait to hear your thoughts.\",\n        \"Excited to hear what you think.\",\n        \"Hope to hear from you soon.\"\n      ],\n      \"description\": \"Close with a short, friendly line that matches the tone of the request (more neutral for formal threads; warmer for familiar contacts).\"\n    },\n    \"sign_offs\": {\n      \"usage\": [\n        \"Thanks,\",\n        \"Thank you,\",\n        \"Many thanks,\",\n        \"Best,\",\n        \"All the best,\",\n        \"Take care,\",\n        \"Thanks again,\",\n        \"Talk soon,\",\n        \"See you soon,\",\n        \"Thanks so much,\",\n        \"See you\",\n        \"Until next time,\",\n        \"Chat soon,\"\n      ],\n      \"description\": \"Use a simple sign-off that sounds natural and not overly formal. Prefer consistency within a thread.\"\n    },\n    \"signatures\": {\n      \"usage\": [],\n      \"description\": \"\"\n    }\n  },\n  \"relationship_with_recipient\": {\n    \"category\": \"other\",\n    \"description\": \"Assume you’ve emailed this audience at least once before. Both you and the recipient are comfortable sharing private or everyday information over email in a friendly, respectful way, but not publicly or on social media.\",\n    \"tone_effect\": \"Clear, straightforward, polite. Use conversational phrasing without being overly friendly, expressive, enthusiastic, approachable, familiar, inappropriate.\",\n    \"structure_effect\": \"Standard (simple email flow). Use a clear greeting, a short purpose statement, then the key details/request, and a brief close. Keep paragraphs short, avoid unnecessary headings, and only add bullets/lists when clarity requires it.\",\n    \"content_effect\": \"General (context-first, action-clear). Include only the details needed for the recipient to understand and act. Avoid assumptions about prior knowledge; avoid adding speculative details.\"\n  }\n}"
```
