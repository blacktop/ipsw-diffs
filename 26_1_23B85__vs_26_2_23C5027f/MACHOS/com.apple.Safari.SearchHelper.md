## com.apple.Safari.SearchHelper

> `/System/Library/PrivateFrameworks/SafariShared.framework/XPCServices/com.apple.Safari.SearchHelper.xpc/com.apple.Safari.SearchHelper`

```diff

-7622.2.11.10.8
-  __TEXT.__text: 0x2f4c
-  __TEXT.__auth_stubs: 0x450
-  __TEXT.__objc_stubs: 0xc80
-  __TEXT.__objc_methlist: 0x488
-  __TEXT.__cstring: 0x1e5
-  __TEXT.__const: 0x38
-  __TEXT.__objc_methname: 0x12b0
-  __TEXT.__oslogstring: 0x19f
+7623.1.12.10.4
+  __TEXT.__text: 0x3378
+  __TEXT.__auth_stubs: 0x440
+  __TEXT.__objc_stubs: 0xe20
+  __TEXT.__objc_methlist: 0x4b8
+  __TEXT.__cstring: 0x1cb
+  __TEXT.__const: 0x40
+  __TEXT.__objc_methname: 0x149c
+  __TEXT.__oslogstring: 0x1d9
   __TEXT.__objc_classname: 0xde
   __TEXT.__objc_methtype: 0x5ff
-  __TEXT.__gcc_except_tab: 0x260
-  __TEXT.__unwind_info: 0x170
-  __DATA_CONST.__auth_got: 0x238
-  __DATA_CONST.__got: 0x118
-  __DATA_CONST.__const: 0x260
-  __DATA_CONST.__cfstring: 0x280
+  __TEXT.__gcc_except_tab: 0x308
+  __TEXT.__unwind_info: 0x190
+  __DATA_CONST.__auth_got: 0x230
+  __DATA_CONST.__got: 0x130
+  __DATA_CONST.__const: 0x220
+  __DATA_CONST.__cfstring: 0x2e0
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0x8
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA.__objc_const: 0x800
-  __DATA.__objc_selrefs: 0x4d8
+  __DATA.__objc_selrefs: 0x540
   __DATA.__objc_ivar: 0x44
   __DATA.__objc_data: 0x140
   __DATA.__data: 0x1e0
-  __DATA.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/JavaScriptCore.framework/JavaScriptCore

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: FA2865E9-FB8F-36F9-B764-FABE6F17F5B5
-  Functions: 70
-  Symbols:   115
-  CStrings:  300
+  UUID: 8493F98E-724C-39BC-B283-91EB188C3E1E
+  Functions: 69
+  Symbols:   117
+  CStrings:  317
 
Symbols:
+ _OBJC_CLASS_$_NSAttributedString
+ _OBJC_CLASS_$_WBSRichSearchSuggestion
+ _OBJC_CLASS_$_WBSRichSearchSuggestionsResult
+ _WBSOSLogOpenSearch
+ _WBSOSLogSafariSuggestions
+ _objc_release_x26
+ _objc_retain_x27
- _dispatch_once
- _objc_enumerationMutation
- _objc_release_x1
- _objc_retain_x24
- _os_log_create
CStrings:
+ "Rich search suggestion has invalid dictionary content: %@"
+ "_autocompleteToFirstSuggestionFromResponse:"
+ "_parseSuggestionsFromJSONResponse:postFixSuggestions:richSearchSuggestionsResult:"
+ "_prefixNavigationalIntentFromResponse:"
+ "_richSearchSuggestionForDictionary:searchString:"
+ "_startParsingWithURLSession:"
+ "a"
+ "addRichSearchSuggestion:forSearchString:"
+ "arrayWithObjects:count:"
+ "firstObject"
+ "google:topqueryintent"
+ "initWithMarkdownString:options:baseURL:error:"
+ "initWithSuggestions:"
+ "initWithTitle:subtitle:entityIDURLParameter:"
+ "q"
+ "removeObjectAtIndex:"
+ "safari_boolForKey:"
+ "safari_validateContentWithRequiredKeys:optionalKeys:keyToExpectedValueType:outExceptionString:"
+ "setAutocompleteToFirstSuggestion:"
+ "setPostFixSuggestions:"
+ "setPrefixNavigationalIntent:"
+ "setRichSearchSuggestionsResult:"
+ "string"
- "OpenSearch"
- "SafariSuggestions"
- "_startParsing"
- "_timingData"
- "com.apple.SafariShared"
- "countByEnumeratingWithState:objects:count:"
- "countOfBytesReceived"
- "initWithSuggestions:postFixSuggestions:prefixNavigationalIntent:sizeInBytes:statusCode:timingData:"
- "statusCode"

```
