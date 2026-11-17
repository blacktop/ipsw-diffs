## MailUI

> `/System/Library/PrivateFrameworks/MailUI.framework/MailUI`

```diff

-3901.300.26.0.0
-  __TEXT.__text: 0x37667c
+3901.300.60.0.0
+  __TEXT.__text: 0x37dd64
   __TEXT.__objc_methlist: 0xa14c
-  __TEXT.__cstring: 0x100f9
-  __TEXT.__const: 0x11744
+  __TEXT.__cstring: 0x104d9
+  __TEXT.__const: 0x118c4
   __TEXT.__gcc_except_tab: 0xe98
-  __TEXT.__oslogstring: 0x7ad0
+  __TEXT.__oslogstring: 0x7b50
   __TEXT.__dlopen_cstrs: 0xba
   __TEXT.__ustring: 0x2e2
-  __TEXT.__swift5_typeref: 0x19666
-  __TEXT.__swift5_capture: 0x5f64
-  __TEXT.__constg_swiftt: 0x49f4
+  __TEXT.__swift5_typeref: 0x196e6
+  __TEXT.__swift5_capture: 0x6004
+  __TEXT.__constg_swiftt: 0x4a44
   __TEXT.__swift5_builtin: 0x564
-  __TEXT.__swift5_reflstr: 0x3e33
-  __TEXT.__swift5_fieldmd: 0x3800
+  __TEXT.__swift5_reflstr: 0x3e73
+  __TEXT.__swift5_fieldmd: 0x384c
   __TEXT.__swift5_assocty: 0x1210
-  __TEXT.__swift5_proto: 0x6a0
-  __TEXT.__swift5_types: 0x584
-  __TEXT.__swift_as_entry: 0x194
-  __TEXT.__swift_as_ret: 0x168
-  __TEXT.__swift_as_cont: 0x290
+  __TEXT.__swift5_proto: 0x6a4
+  __TEXT.__swift5_types: 0x588
+  __TEXT.__swift_as_entry: 0x1a8
+  __TEXT.__swift_as_ret: 0x180
+  __TEXT.__swift_as_cont: 0x2c8
   __TEXT.__swift5_protos: 0x2c
   __TEXT.__swift5_mpenum: 0x30
-  __TEXT.__unwind_info: 0xf290
-  __TEXT.__eh_frame: 0x363c
+  __TEXT.__unwind_info: 0xf430
+  __TEXT.__eh_frame: 0x37ac
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0xe0
   __DATA_CONST.__objc_protolist: 0x378
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x67e0
+  __DATA_CONST.__objc_selrefs: 0x67f8
   __DATA_CONST.__objc_protorefs: 0x140
   __DATA_CONST.__objc_superrefs: 0x290
   __DATA_CONST.__objc_arraydata: 0x58
-  __DATA_CONST.__got: 0x20e0
-  __AUTH_CONST.__const: 0x13e08
+  __DATA_CONST.__got: 0x2100
+  __AUTH_CONST.__const: 0x13fa0
   __AUTH_CONST.__cfstring: 0x4b80
   __AUTH_CONST.__objc_const: 0x14908
   __AUTH_CONST.__objc_intobj: 0x288
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH_CONST.__auth_got: 0x32d0
+  __AUTH_CONST.__auth_got: 0x3368
   __AUTH.__objc_data: 0x1e70
-  __AUTH.__data: 0x1680
+  __AUTH.__data: 0x1730
   __DATA.__objc_ivar: 0x9b4
-  __DATA.__data: 0x7670
+  __DATA.__data: 0x76e0
   __DATA.__objc_stublist: 0x8
   __DATA.__common: 0x3f0
   __DATA_DIRTY.__objc_data: 0x3058
-  __DATA_DIRTY.__data: 0x3608
+  __DATA_DIRTY.__data: 0x3618
   __DATA_DIRTY.__bss: 0x59f0
   __DATA_DIRTY.__common: 0x40
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 16083
-  Symbols:   8877
-  CStrings:  2182
+  Functions: 16181
+  Symbols:   8886
+  CStrings:  2194
 
Symbols:
+ -[MessageListPositionHelper actuallyVisibleItemIDs]
+ ___51-[MessageListPositionHelper actuallyVisibleItemIDs]_block_invoke
+ ___block_descriptor_72_e8_32s_e21_16?0"NSIndexPath"8ls32l8
+ _symbolic SDySSSo16CSSearchableItemCG
+ _symbolic SJ
+ _symbolic SS_So16CSSearchableItemCt
+ _symbolic SaySsG
+ _symbolic Say_____G 6MailUI14CSQueryBuilderC
+ _symbolic So11NSPredicateCSg
+ _symbolic _____ 6MailUI16TypedComposeBodyO
+ _symbolic ______AAt 6MailUI16TypedComposeBodyO
+ _symbolic _____y_____GSg 12HybridSearch15ComposableQueryV AA11MailContentV
- -[MessageListPositionHelper actuallyVisibleIndexPaths]
- ___54-[MessageListPositionHelper actuallyVisibleIndexPaths]_block_invoke
- ___block_descriptor_72_e8_32s_e21_B16?0"NSIndexPath"8ls32l8
CStrings:
+ " && "
+ " = "
+ " AND "
+ " CONTAINS "
+ " OR "
+ "#SiriMail bodyHTML: callAsyncJavaScript failed (%s)"
+ "#SiriMail managedSignatureText: callAsyncJavaScript failed (%s)"
+ "'*"
+ "*'cd"
+ "Dialog to show and say when an email update was skipped because the new body was only the signature."
+ "Draft_Body_Only_Signature_Dialog"
+ "Sorry, I didnʼt change the email because the new text was only your signature."
+ "\\"
+ "\\s*(?:\\A|(?<=\\n))"
+ "\\s*\\z"
+ "\\s+"
+ "const body = document.body;\n// The `Apple-mail-*` class strings and bare `attachment` tag are how MessageUI renders\n// inline photos/PDFs/files; we hardcode them because the ObjC constants aren't in scope here.\nconst preservedSelector = 'blockquote[type=\"cite\"], div#AppleMailSignature, attachment, ' +\n    '.Apple-mail-imageattach, .Apple-mail-pdf, .Apple-mail-fileattach';\n// Use querySelector + walk up so we find the body-level ancestor of a preserved\n// node even when MessageUI wraps it in a div (e.g., a blockquote nested inside\n// a `<div>` wrapper in a user-pasted reply). Iterating `body.children` and\n// matching directly would miss those.\nlet firstPreserved = body.querySelector(preservedSelector);\nif (firstPreserved === null) {\n    body.innerHTML = newHTML;\n    return;\n}\n// A reopened maild draft wraps the user text and the signature in one div, so clear what precedes the signature\n// inside each wrapper too. Other preserved nodes (a quote's attribution, inline attachments) keep their wrapper.\nconst clearsInsideWrappers = firstPreserved.matches('div#AppleMailSignature');\nwhile (firstPreserved.parentNode !== body) {\n    while (clearsInsideWrappers && firstPreserved.previousSibling) {\n        firstPreserved.parentNode.removeChild(firstPreserved.previousSibling);\n    }\n    firstPreserved = firstPreserved.parentNode;\n}\nwhile (body.firstChild && body.firstChild !== firstPreserved) {\n    body.removeChild(body.firstChild);\n}\nif (newHTML.length > 0) {\n    // Insert the parsed nodes directly via a <template> so we don't introduce an\n    // extra wrapper <div> — keeping the same DOM shape as the no-preserved-node\n    // path above (which assigns to `body.innerHTML` without a wrapper).\n    const template = document.createElement('template');\n    template.innerHTML = newHTML;\n    body.insertBefore(template.content, firstPreserved);\n}"
+ "const signature = Array.from(document.querySelectorAll('div#AppleMailSignature'))\n    .find(node => !node.closest('blockquote[type=\"cite\"]'));\nreturn signature ? (signature.innerText || signature.textContent || '') : '';"
+ "return document.body.innerHTML;"
- "&&"
- "="
- "AND"
- "CONTAINS"
- "OR"
- "const body = document.body;\n// The `Apple-mail-*` class strings and bare `attachment` tag are how MessageUI renders\n// inline photos/PDFs/files; we hardcode them because the ObjC constants aren't in scope here.\nconst preservedSelector = 'blockquote[type=\"cite\"], div#AppleMailSignature, attachment, ' +\n    '.Apple-mail-imageattach, .Apple-mail-pdf, .Apple-mail-fileattach';\n// Use querySelector + walk up so we find the body-level ancestor of a preserved\n// node even when MessageUI wraps it in a div (e.g., a blockquote nested inside\n// a `<div>` wrapper in a user-pasted reply). Iterating `body.children` and\n// matching directly would miss those.\nlet firstPreserved = body.querySelector(preservedSelector);\nwhile (firstPreserved && firstPreserved.parentNode !== body) {\n    firstPreserved = firstPreserved.parentNode;\n}\nif (firstPreserved === null) {\n    body.innerHTML = newHTML;\n    return;\n}\nwhile (body.firstChild && body.firstChild !== firstPreserved) {\n    body.removeChild(body.firstChild);\n}\nif (newHTML.length > 0) {\n    // Insert the parsed nodes directly via a <template> so we don't introduce an\n    // extra wrapper <div> — keeping the same DOM shape as the no-preserved-node\n    // path above (which assigns to `body.innerHTML` without a wrapper).\n    const template = document.createElement('template');\n    template.innerHTML = newHTML;\n    body.insertBefore(template.content, firstPreserved);\n}"
- "||"
```
