## SpeechTranslation

> `/System/Library/PrivateFrameworks/SpeechTranslation.framework/SpeechTranslation`

### Sections with Same Size but Changed Content

- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-385.0.0.0.0
-  __TEXT.__text: 0x32530
-  __TEXT.__objc_methlist: 0x12d4
-  __TEXT.__const: 0xc7c
-  __TEXT.__cstring: 0x107a
-  __TEXT.__oslogstring: 0x2b75
+388.0.0.0.0
+  __TEXT.__text: 0x328b0
+  __TEXT.__objc_methlist: 0x1314
+  __TEXT.__const: 0xc6c
+  __TEXT.__cstring: 0x108a
+  __TEXT.__oslogstring: 0x2ba5
   __TEXT.__gcc_except_tab: 0x258
   __TEXT.__constg_swiftt: 0x458
   __TEXT.__swift5_typeref: 0x675

   __TEXT.__swift_as_entry: 0x48
   __TEXT.__swift_as_ret: 0x60
   __TEXT.__swift_as_cont: 0xc4
-  __TEXT.__unwind_info: 0xcc0
-  __TEXT.__eh_frame: 0xd98
+  __TEXT.__unwind_info: 0xcd0
+  __TEXT.__eh_frame: 0xde8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa98
+  __DATA_CONST.__objc_selrefs: 0xab8
   __DATA_CONST.__objc_protorefs: 0x40
   __DATA_CONST.__objc_superrefs: 0x50
   __DATA_CONST.__got: 0x468
   __AUTH_CONST.__const: 0xd98
   __AUTH_CONST.__cfstring: 0x3e0
-  __AUTH_CONST.__objc_const: 0x2478
+  __AUTH_CONST.__objc_const: 0x2488
   __AUTH_CONST.__auth_got: 0xba8
   __AUTH.__objc_data: 0x640
   __AUTH.__data: 0x6d0
   __DATA.__objc_ivar: 0xcc
-  __DATA.__data: 0xb38
+  __DATA.__data: 0xb28
   __DATA.__bss: 0xc20
   __DATA.__common: 0x98
   __DATA_DIRTY.__objc_data: 0xf0

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1001
-  Symbols:   1347
-  CStrings:  281
+  Functions: 1007
+  Symbols:   1357
+  CStrings:  282
 
Symbols:
+ +[_STSELFLoggingClient sharedClient]
+ -[_STSELFLoggingClient _setUpOrReuseSessionWithConfiguration:]
+ -[_STSELFLoggingClient registerWithConfiguration:]
+ -[_STSpeechTranslatorManager selfLoggingClient]
+ __OBJC_$_CLASS_METHODS__STSELFLoggingClient
+ ___50-[_STSELFLoggingClient registerWithConfiguration:]_block_invoke
+ _objc_msgSend$_setUpOrReuseSessionWithConfiguration:
+ _objc_msgSend$registerWithConfiguration:
+ _objc_msgSend$selfLoggingClient
+ _objc_msgSend$sharedClient
CStrings:
+ "Additional registration doesn't match language of ongoing logging session"
+ "Additional registration for ongoing session ignored."
+ "Register translator for instrumentation observation"
- "Additional client list doesn't match language of ongoing logging session"
- "Additional client list for ongoing session ignored."
```
