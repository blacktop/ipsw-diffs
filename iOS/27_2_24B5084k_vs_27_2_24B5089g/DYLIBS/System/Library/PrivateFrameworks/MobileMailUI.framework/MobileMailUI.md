## MobileMailUI

> `/System/Library/PrivateFrameworks/MobileMailUI.framework/MobileMailUI`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`

```diff

-3901.200.34.0.0
-  __TEXT.__text: 0x4cc34
-  __TEXT.__objc_methlist: 0x5304
-  __TEXT.__gcc_except_tab: 0x98c0
-  __TEXT.__const: 0x8514
+3901.200.41.0.0
+  __TEXT.__text: 0x4ccac
+  __TEXT.__objc_methlist: 0x531c
+  __TEXT.__gcc_except_tab: 0x9890
+  __TEXT.__const: 0x8504
   __TEXT.__cstring: 0x342c
   __TEXT.__ustring: 0x318
-  __TEXT.__oslogstring: 0x2367
+  __TEXT.__oslogstring: 0x24b7
   __TEXT.__dlopen_cstrs: 0x97
   __TEXT.__swift5_typeref: 0x2a2
   __TEXT.__swift5_capture: 0x128

   __TEXT.__swift_as_entry: 0x14
   __TEXT.__swift_as_ret: 0x18
   __TEXT.__swift_as_cont: 0x28
-  __TEXT.__unwind_info: 0x2d18
+  __TEXT.__unwind_info: 0x2d20
   __TEXT.__eh_frame: 0x1b0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x160
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4258
+  __DATA_CONST.__objc_selrefs: 0x4270
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x150
   __DATA_CONST.__objc_arraydata: 0xe8
-  __DATA_CONST.__got: 0xb48
+  __DATA_CONST.__got: 0xb60
   __AUTH_CONST.__const: 0x730
   __AUTH_CONST.__cfstring: 0x3140
-  __AUTH_CONST.__objc_const: 0x7fd8
+  __AUTH_CONST.__objc_const: 0x7ff8
   __AUTH_CONST.__objc_intobj: 0xf0
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_doubleobj: 0x20

   __AUTH_CONST.__auth_got: 0x898
   __AUTH.__objc_data: 0xa60
   __AUTH.__data: 0xe8
-  __DATA.__objc_ivar: 0x4dc
+  __DATA.__objc_ivar: 0x4e0
   __DATA.__data: 0x1158
   __DATA.__common: 0x78
   __DATA_DIRTY.__objc_data: 0xb38

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1764
-  Symbols:   5138
-  CStrings:  678
+  Functions: 1766
+  Symbols:   5150
+  CStrings:  679
 
Symbols:
+ -[MFMessageContentView _committedDocumentMatchesContentURL:]
+ -[MFMessageContentView _discardFirstPaintGateState]
+ -[MFMessageContentView _handleNavigationFailure:]
+ -[MFMessageContentView webView:didFailProvisionalNavigation:withError:]
+ -[MFWebViewLoadingController cancelPendingContent]
+ GCC_except_table158
+ GCC_except_table160
+ GCC_except_table165
+ GCC_except_table167
+ GCC_except_table178
+ GCC_except_table188
+ GCC_except_table201
+ GCC_except_table204
+ GCC_except_table214
+ GCC_except_table217
+ GCC_except_table227
+ GCC_except_table229
+ GCC_except_table236
+ GCC_except_table238
+ GCC_except_table243
+ GCC_except_table253
+ GCC_except_table255
+ GCC_except_table266
+ GCC_except_table268
+ GCC_except_table269
+ GCC_except_table274
+ GCC_except_table281
+ GCC_except_table283
+ GCC_except_table286
+ GCC_except_table288
+ GCC_except_table360
+ GCC_except_table361
+ GCC_except_table369
+ GCC_except_table371
+ GCC_except_table372
+ GCC_except_table374
+ _EMErrorDomain
+ _NSURLErrorDomain
+ _OBJC_IVAR_$_MFMessageContentView._committedDocumentURL
+ _WKErrorDomain
+ _objc_msgSend$_committedDocumentMatchesContentURL:
+ _objc_msgSend$_committedURL
+ _objc_msgSend$_discardFirstPaintGateState
+ _objc_msgSend$_handleNavigationFailure:
+ _objc_msgSend$cancelPendingContent
+ _objc_msgSend$ef_hasScheme:
+ _objc_msgSend$ef_match
+ _objc_msgSend$errorWithDomain:code:userInfo:
- -[MFWebViewLoadingController clearContent]
- -[VIPManager allVIPEmailAddressesCriterion]
- -[VIPManager criterionForEmailAddresses:]
- GCC_except_table151
- GCC_except_table156
- GCC_except_table162
- GCC_except_table168
- GCC_except_table169
- GCC_except_table171
- GCC_except_table182
- GCC_except_table196
- GCC_except_table209
- GCC_except_table220
- GCC_except_table221
- GCC_except_table233
- GCC_except_table234
- GCC_except_table239
- GCC_except_table240
- GCC_except_table242
- GCC_except_table247
- GCC_except_table261
- GCC_except_table263
- GCC_except_table270
- GCC_except_table272
- GCC_except_table273
- GCC_except_table282
- GCC_except_table356
- GCC_except_table357
- GCC_except_table364
- GCC_except_table365
- GCC_except_table366
- GCC_except_table367
- _objc_msgSend$clearContent
- _objc_msgSend$initWithType:qualifier:expression:
- _objc_msgSend$mf_copyIDNADecodedEmailAddress
- _objc_msgSend$orCompoundCriterionWithCriteria:
CStrings:
+ "<%{public}@: %p>: Canceling pending content: %@"
+ "<%{public}@: %p>: Message Content View did fail navigation, substituting error content: %{public}@"
+ "<%{public}@: %p>: honoring first paint for error markup, skipping the content URL match. committed=%{public}@"
+ "<%{public}@: %p>: superseded navigation, not treating as a failure: %{public}@"
+ "<%{public}@: %p>: webView first paint precedes the commit of the expected document, disregarding this event. committed=%{public}@ expected=%{public}@ loading indicator visible: %@"
+ "\xf0\xf0R"
- "<%{public}@: %p>: Clearing webview content: %@"
- "<%{public}@: %p>: Message Content View did fail navigation: %{public}@"
- "MFWebViewLoadingController.clearContent"
- "WebView=%{public}p"
- "\xf0\xf0B"
```
