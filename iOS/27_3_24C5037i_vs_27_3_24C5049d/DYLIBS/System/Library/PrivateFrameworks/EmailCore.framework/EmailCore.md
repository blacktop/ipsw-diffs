## EmailCore

> `/System/Library/PrivateFrameworks/EmailCore.framework/EmailCore`

```diff

-3901.300.26.0.0
-  __TEXT.__text: 0x60214
-  __TEXT.__objc_methlist: 0x5108
-  __TEXT.__gcc_except_tab: 0x7344
-  __TEXT.__const: 0x1560
-  __TEXT.__cstring: 0x83fe
+3901.300.60.0.0
+  __TEXT.__text: 0x63128
+  __TEXT.__objc_methlist: 0x5178
+  __TEXT.__gcc_except_tab: 0x74a4
+  __TEXT.__const: 0x15d0
+  __TEXT.__cstring: 0x846e
   __TEXT.__oslogstring: 0xcc5
   __TEXT.__ustring: 0x90
   __TEXT.__constg_swiftt: 0x148
-  __TEXT.__swift5_typeref: 0x1ac
-  __TEXT.__swift5_reflstr: 0x5a3
-  __TEXT.__swift5_fieldmd: 0x430
-  __TEXT.__swift5_proto: 0x24
+  __TEXT.__swift5_typeref: 0x1d0
   __TEXT.__swift5_types: 0x20
+  __TEXT.__swift5_reflstr: 0x683
+  __TEXT.__swift5_fieldmd: 0x49c
+  __TEXT.__swift5_proto: 0x24
   __TEXT.__swift5_assocty: 0x18
-  __TEXT.__unwind_info: 0x2f10
-  __TEXT.__eh_frame: 0x1c0
+  __TEXT.__unwind_info: 0x2fc0
+  __TEXT.__eh_frame: 0x1f8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2258
+  __DATA_CONST.__const: 0x2260
   __DATA_CONST.__objc_classlist: 0x358
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x120
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2a78
+  __DATA_CONST.__objc_selrefs: 0x2ac8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x278
   __DATA_CONST.__objc_arraydata: 0x80
-  __DATA_CONST.__got: 0x778
-  __AUTH_CONST.__const: 0x24f9
-  __AUTH_CONST.__cfstring: 0x5480
-  __AUTH_CONST.__objc_const: 0xa990
+  __DATA_CONST.__got: 0x788
+  __AUTH_CONST.__const: 0x25a0
+  __AUTH_CONST.__cfstring: 0x5580
+  __AUTH_CONST.__objc_const: 0xaab0
   __AUTH_CONST.__objc_arrayobj: 0xf0
   __AUTH_CONST.__objc_intobj: 0x198
-  __AUTH_CONST.__auth_got: 0xc98
+  __AUTH_CONST.__auth_got: 0xcb8
   __AUTH.__objc_data: 0x128
   __AUTH.__data: 0xc20
   __DATA.__objc_ivar: 0x4bc
-  __DATA.__data: 0xec8
+  __DATA.__data: 0xee8
   __DATA.__common: 0x24
   __DATA_DIRTY.__objc_data: 0x2058
-  __DATA_DIRTY.__data: 0x378
+  __DATA_DIRTY.__data: 0x3c0
   __DATA_DIRTY.__bss: 0x1b8
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2135
-  Symbols:   4239
-  CStrings:  1544
+  Functions: 2162
+  Symbols:   4254
+  CStrings:  1552
 
Symbols:
+ +[ECMessageBodyParsingUtils _blockquoteDepthAtLocation:inHTML:]
+ +[ECMessageBodyParsingUtils _html:hasTag:atLocation:]
+ +[ECMessageBodyParsingUtils _locationOfOpenTag:enclosingLocation:inHTML:]
+ +[ECMessageBodyParsingUtils _rangeOfDivStartingAtLocation:inHTML:]
+ +[ECMessageBodyParsingUtils _rangeOfManagedSignatureInHTML:fromLocation:aboveQuotedContentOnly:]
+ +[ECMessageBodyParsingUtils rangeOfManagedSignatureAboveQuotedContentInHTMLBody:]
+ +[ECMessageBodyParsingUtils readableBodyFromHTMLBody:options:maxLength:]
+ +[ECMessageBodyParsingUtils strippedManagedSignatureFromHTMLBody:]
+ +[ECSecureMIMETrustEvaluation configureTrust:withOptions:]
+ _ECHTMLIDSignatureAttribute
+ _kSecMatchLimitAll
+ _kSecReturnAttributes
+ _swift_release_x19
+ _symbolic SaySDySSypGG
+ _symbolic Say_____GSg s6UInt16V
+ _symbolic _____ySSG s23_ContiguousArrayStorageC
- -[ECAuthenticationScheme connectionClassForAccountClass:]
CStrings:
+ "<!--"
+ "</blockquote"
+ "</div"
+ "<blockquote"
+ "<br><br><br/><br/>"
+ "<div"
+ "<div data-siri-quote-preamble"
+ "id=\"AppleMailSignature\""
```
