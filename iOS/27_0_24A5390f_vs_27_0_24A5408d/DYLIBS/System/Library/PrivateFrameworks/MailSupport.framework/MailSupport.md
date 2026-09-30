## MailSupport

> `/System/Library/PrivateFrameworks/MailSupport.framework/MailSupport`

```diff

-3897.100.8.2.5
-  __TEXT.__text: 0x22c78
+3901.100.1.2.7
+  __TEXT.__text: 0x22dd4
   __TEXT.__objc_methlist: 0x19b0
-  __TEXT.__gcc_except_tab: 0x27e4
-  __TEXT.__cstring: 0x4c1b
+  __TEXT.__gcc_except_tab: 0x280c
+  __TEXT.__cstring: 0x4ddb
   __TEXT.__const: 0x472
-  __TEXT.__oslogstring: 0x668
+  __TEXT.__oslogstring: 0x678
   __TEXT.__dlopen_cstrs: 0xd4
   __TEXT.__ustring: 0x18
   __TEXT.__swift5_typeref: 0x3d2

   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1670
+  __DATA_CONST.__objc_selrefs: 0x1678
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x108
   __DATA_CONST.__objc_arraydata: 0x20
   __DATA_CONST.__got: 0x558
   __AUTH_CONST.__const: 0x628
-  __AUTH_CONST.__cfstring: 0x49a0
+  __AUTH_CONST.__cfstring: 0x49c0
   __AUTH_CONST.__objc_const: 0x4488
   __AUTH_CONST.__objc_intobj: 0x168
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_got: 0x6a8
-  __AUTH.__objc_data: 0x120
+  __AUTH.__objc_data: 0x170
   __DATA.__objc_ivar: 0x1bc
   __DATA.__data: 0xbe8
   __DATA.__bss: 0x348
-  __DATA_DIRTY.__objc_data: 0x1218
+  __DATA_DIRTY.__objc_data: 0x11c8
   __DATA_DIRTY.__data: 0x458
   __DATA_DIRTY.__bss: 0x1a0
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 978
-  Symbols:   2572
-  CStrings:  725
+  Symbols:   2573
+  CStrings:  726
 
Symbols:
+ +[MSWritingToolsNodePreservation preserveNodesInWebView:completionHandler:]
+ _OBJC_CLASS_$_MSWritingToolsNodePreservation
+ _OBJC_METACLASS_$_MSWritingToolsNodePreservation
+ __OBJC_$_CLASS_METHODS_MSWritingToolsNodePreservation
+ __OBJC_CLASS_RO_$_MSWritingToolsNodePreservation
+ __OBJC_METACLASS_RO_$_MSWritingToolsNodePreservation
+ ___75+[MSWritingToolsNodePreservation preserveNodesInWebView:completionHandler:]_block_invoke
+ _objc_msgSend$arrayWithCapacity:
- +[MSWritingToolsSignaturePreservation preserveSignatureNodeInWebView:completionHandler:]
- _OBJC_CLASS_$_MSWritingToolsSignaturePreservation
- _OBJC_METACLASS_$_MSWritingToolsSignaturePreservation
- __OBJC_$_CLASS_METHODS_MSWritingToolsSignaturePreservation
- __OBJC_CLASS_RO_$_MSWritingToolsSignaturePreservation
- __OBJC_METACLASS_RO_$_MSWritingToolsSignaturePreservation
- ___88+[MSWritingToolsSignaturePreservation preserveSignatureNodeInWebView:completionHandler:]_block_invoke
Functions:
~ ___88+[MSWritingToolsSignaturePreservation preserveSignatureNodeInWebView:completionHandler:]_block_invoke -> ___75+[MSWritingToolsNodePreservation preserveNodesInWebView:completionHandler:]_block_invoke : 300 -> 648
CStrings:
+ "(function() {var preserved = [];var signatures = document.querySelectorAll('div[id=\"AppleMailSignature\"]');for (var i = 0; i < signatures.length; i++) {  if (!signatures[i].closest('blockquote[type=\"cite\"], blockquote.gmail_quote')) {    preserved.push(signatures[i]);    break;  }}var quotes = document.querySelectorAll('blockquote[type=\"cite\"], blockquote.gmail_quote');for (var j = 0; j < quotes.length; j++) {  var quote = quotes[j];  if (!quote.parentElement || !quote.parentElement.closest('blockquote[type=\"cite\"], blockquote.gmail_quote')) {    preserved.push(quote);  }}return preserved.map(function(node) { return window.webkit.createJSHandle(node); });})()"
+ "WKJSHandle"
+ "[Writing Tools] Failed to create preserved-node JSHandles: %@"
- "(function() {var nodes = document.querySelectorAll('div[id=\"AppleMailSignature\"]');for (var i = 0; i < nodes.length; i++) {  if (!nodes[i].closest('blockquote[type=\"cite\"]'))    return window.webkit.createJSHandle(nodes[i]);}})()"
- "[Writing Tools] Failed to create signature JSHandle: %@"
```
