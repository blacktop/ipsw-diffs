## com.apple.SpeechRecognitionCore.brokerd

> `/System/Library/PrivateFrameworks/SpeechRecognitionCore.framework/XPCServices/com.apple.SpeechRecognitionCore.brokerd.xpc/com.apple.SpeechRecognitionCore.brokerd`

```diff

-  __TEXT.__text: 0x10be4
-  __TEXT.__auth_stubs: 0xd80
+  __TEXT.__text: 0x10b58
+  __TEXT.__auth_stubs: 0xd50
   __TEXT.__objc_stubs: 0x14e0
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0x5b4
-  __TEXT.__const: 0x162
-  __TEXT.__cstring: 0xbe3
-  __TEXT.__oslogstring: 0x1513
-  __TEXT.__gcc_except_tab: 0x7a0
+  __TEXT.__const: 0x152
+  __TEXT.__cstring: 0xbb3
+  __TEXT.__oslogstring: 0x1553
+  __TEXT.__gcc_except_tab: 0x78c
   __TEXT.__objc_classname: 0xa0
   __TEXT.__objc_methname: 0x14bc
   __TEXT.__objc_methtype: 0x29c

   __TEXT.__constg_swiftt: 0x38
   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x4d0
+  __TEXT.__unwind_info: 0x4c0
   __DATA_CONST.__const: 0x910
-  __DATA_CONST.__cfstring: 0xf60
+  __DATA_CONST.__cfstring: 0xf40
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10

   __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA_CONST.__auth_got: 0x6d8
-  __DATA_CONST.__got: 0x218
+  __DATA_CONST.__auth_got: 0x6c0
+  __DATA_CONST.__got: 0x220
   __DATA_CONST.__auth_ptr: 0x30
   __DATA.__objc_const: 0x4a0
   __DATA.__objc_selrefs: 0x5e0

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 264
-  Symbols:   306
-  CStrings:  665
+  Symbols:   303
+  CStrings:  663
 
Sections:
~ __TEXT.__init_offsets : content changed
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__constg_swiftt : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_dictobj : content changed
~ __DATA_CONST.__auth_ptr : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_selrefs : content changed
~ __DATA.__objc_data : content changed
~ __DATA.__data : content changed
Symbols:
+ __os_log_error_impl
- _CFDataGetBytePtr
- _CFDataGetLength
- _CFStringCreateExternalRepresentation
- _CFStringCreateWithFormatAndArguments
CStrings:
+ "Received invalid recognizer ID in UpdateRecognizer %{public}lld"
- "%.*s"
- "Received invalid recognizer ID in UpdateRecognizer %lld"

```
