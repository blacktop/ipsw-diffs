## QueryParser

> `/System/Library/PrivateFrameworks/QueryParser.framework/QueryParser`

```diff

-2312.1.0.4.0
-  __TEXT.__text: 0x8b0a0
-  __TEXT.__auth_stubs: 0x19a0
+2314.2.0.0.0
+  __TEXT.__text: 0x8bcb8
+  __TEXT.__auth_stubs: 0x1930
   __TEXT.__objc_methlist: 0x4ac
-  __TEXT.__const: 0xfba
-  __TEXT.__gcc_except_tab: 0xa018
-  __TEXT.__oslogstring: 0x1a86
-  __TEXT.__cstring: 0x692f
+  __TEXT.__const: 0xfaa
+  __TEXT.__gcc_except_tab: 0xa0ec
+  __TEXT.__oslogstring: 0x1ead
+  __TEXT.__cstring: 0x6988
   __TEXT.__ustring: 0xec
   __TEXT.__dlopen_cstrs: 0x41
-  __TEXT.__unwind_info: 0x2d70
+  __TEXT.__unwind_info: 0x2d48
   __TEXT.__objc_classname: 0xb3
-  __TEXT.__objc_methname: 0x1c3e
+  __TEXT.__objc_methname: 0x1ca8
   __TEXT.__objc_methtype: 0x337
-  __TEXT.__objc_stubs: 0x2340
-  __DATA_CONST.__got: 0x3d8
-  __DATA_CONST.__const: 0x20b8
+  __TEXT.__objc_stubs: 0x23c0
+  __DATA_CONST.__got: 0x3d0
+  __DATA_CONST.__const: 0x20a0
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x968
+  __DATA_CONST.__objc_selrefs: 0x988
   __DATA_CONST.__objc_superrefs: 0x30
   __DATA_CONST.__objc_arraydata: 0x8d0
-  __AUTH_CONST.__auth_got: 0xce8
-  __AUTH_CONST.__auth_ptr: 0x70
+  __AUTH_CONST.__auth_got: 0xcb0
+  __AUTH_CONST.__auth_ptr: 0x78
   __AUTH_CONST.__const: 0x19f0
-  __AUTH_CONST.__cfstring: 0xaa40
+  __AUTH_CONST.__cfstring: 0xaac0
   __AUTH_CONST.__objc_const: 0xd80
   __AUTH_CONST.__objc_intobj: 0x840
   __AUTH_CONST.__objc_dictobj: 0xa0

   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x84
   __DATA.__data: 0x750
-  __DATA.__bss: 0x180
+  __DATA.__bss: 0x170
   __DATA_DIRTY.__objc_data: 0x230
   __DATA_DIRTY.__data: 0x70
-  __DATA_DIRTY.__bss: 0x1b8
+  __DATA_DIRTY.__bss: 0x1d8
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1883
-  Symbols:   2789
-  CStrings:  2162
+  Functions: 1882
+  Symbols:   2775
+  CStrings:  2190
 
Symbols:
+ _CFAttributedStringReplaceAttributedString
+ _CFCharacterSetCreateMutableCopy
+ _CFCharacterSetUnion
+ _OBJC_CLASS_$_NSAttributedString
+ _OBJC_CLASS_$_NSUserDefaults
+ _SILexiconCacheEnumerateOVSAnnotationsInString
+ __ZNSt3__15mutex4lockEv
+ __ZNSt3__15mutex6unlockEv
+ __ZNSt3__15mutexD1Ev
+ _kCFLocaleExemplarCharacterSet
- _CFStringGetCStringPtr
- __ZNKSt3__16locale9use_facetERNS0_2idE
- __ZNKSt3__18ios_base6getlocEv
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2ERKS5_mmRKS4_
- __ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEE6sentryC1ERS3_
- __ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEE6sentryD1Ev
- __ZNSt3__114basic_iostreamIcNS_11char_traitsIcEEED2Ev
- __ZNSt3__115basic_streambufIcNS_11char_traitsIcEEEC2Ev
- __ZNSt3__115basic_streambufIcNS_11char_traitsIcEEED2Ev
- __ZNSt3__15ctypeIcE2idE
- __ZNSt3__16localeD1Ev
- __ZNSt3__18ios_base33__set_badbit_and_consider_rethrowEv
- __ZNSt3__18ios_base4initEPv
- __ZNSt3__18ios_base5clearEj
- __ZNSt3__19basic_iosIcNS_11char_traitsIcEEED2Ev
- __ZTTNSt3__118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE
- __ZTVNSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEEE
- __ZTVNSt3__118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE
CStrings:
+ "."
+ "EMOJI"
+ "EnablePersonalizedEmbedding"
+ "QPDataDetector"
+ "QueryParserDataDetectors: Creating lexicon scanner"
+ "QueryParserDataDetectors: releasing data detectors"
+ "QueryParserDataDetectors: setting dynamic sources on lexicon scanner"
+ "[QPNLU] Stripping trailing '.' from input string"
+ "[QPNLU] starting m_parser parse with u2:%!d(MISSING) and llm:%!d(MISSING) embeddings:%!d(MISSING)"
+ "[QPParser] empty embedding string"
+ "[QPParser] not generating embedding due to failed canUseEmbeddings check"
+ "[QPParser] not generating embedding due to failed language check"
+ "[QPParser] not generating embedding due to failed string check"
+ "[QPParser] not generating embedding due to no embedder available"
+ "[QPParser] not generating embedding for %!@(MISSING) due to unicode chars in embedding query string"
+ "[QPParser] not generating embedding for empty string"
+ "[QPU2Parser] can't remove ARG_LOCATION because of low confidence"
+ "[QPU2Parser] can't remove ARG_PERSON because of low confidence"
+ "[QPU2Parser] can't remove holiday span from query"
+ "[QPU2Parser] embedding string - (%!@(MISSING))"
+ "[QPU2Parser] personalized embedding: %!d(MISSING)"
+ "appendAttributedString:"
+ "boolForKey:"
+ "generateEmbeddingForTextInputs:extendedContextLength:queryID:timeout:error:"
+ "initWithString:attributes:"
+ "kMDItemPhotosPeoplePersonIdentifiers"
+ "loaded lexicon cache in %!f(MISSING)ms"
+ "not loading lexicon cache because safety annotations aren't loaded"
+ "queryForAttributes: query complete in %!f(MISSING)ms"
+ "standardUserDefaults"
+ "unable to load lexicon cache in %!f(MISSING)ms"
+ "update: loaded lexicon cache in %!f(MISSING)ms"
+ "update: unable to load lexicon cache in %!f(MISSING)ms"
+ "updated parser in %!f(MISSING)ms"
+ "v48@?0r*8Q16{?=*Q{?=IC}}24"
- "QueryParserDataDetectors: loading dynamic sources"
- "[QPNLU] starting m_parser parse with u2:%!d(MISSING) and llm:%!d(MISSING)"
- "[QPParser] can't remove holiday span from query"
- "generateEmbeddingForTextInputs:queryID:timeout:error:"
- "queryForAttributes: query complete"
- "unable to load lexicon cache"
- "v40@?0r*8Q16{?=*{?=IC}}24"

```
