## com.apple.SpeechRecognitionCore.brokerd

> `/System/Library/PrivateFrameworks/SpeechRecognitionCore.framework/Versions/A/XPCServices/com.apple.SpeechRecognitionCore.brokerd.xpc/Contents/MacOS/com.apple.SpeechRecognitionCore.brokerd`

```diff

-  __TEXT.__text: 0x12ae8
-  __TEXT.__auth_stubs: 0xdc0
+  __TEXT.__text: 0x12b14
+  __TEXT.__auth_stubs: 0xda0
   __TEXT.__objc_stubs: 0x14c0
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0x5b4
   __TEXT.__const: 0x162
-  __TEXT.__cstring: 0xd33
-  __TEXT.__oslogstring: 0x1613
-  __TEXT.__gcc_except_tab: 0x8ec
+  __TEXT.__cstring: 0xcb3
+  __TEXT.__oslogstring: 0x16a3
+  __TEXT.__gcc_except_tab: 0x8e8
   __TEXT.__objc_classname: 0xa0
   __TEXT.__objc_methname: 0x14a3
   __TEXT.__objc_methtype: 0x29c

   __TEXT.__constg_swiftt: 0x38
   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x540
+  __TEXT.__unwind_info: 0x538
   __DATA_CONST.__const: 0x9a8
-  __DATA_CONST.__cfstring: 0x10c0
+  __DATA_CONST.__cfstring: 0x1060
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10

   __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA_CONST.__auth_got: 0x6f8
-  __DATA_CONST.__got: 0x238
+  __DATA_CONST.__auth_got: 0x6e8
+  __DATA_CONST.__got: 0x240
   __DATA_CONST.__auth_ptr: 0x30
   __DATA.__objc_const: 0x4a0
   __DATA.__objc_selrefs: 0x5d8

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 308
-  Symbols:   317
-  CStrings:  700
+  Functions: 310
+  Symbols:   315
+  CStrings:  696
 
Sections:
~ __TEXT.__init_offsets : content changed
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__const : content changed
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
+ __os_log_debug_impl
+ __os_log_error_impl
- _CFDataGetBytePtr
- _CFDataGetLength
- _CFStringCreateExternalRepresentation
- _CFStringCreateWithFormatAndArguments
CStrings:
+ "FeedbackText ID = (%{public}@) Text = %{sensitive}@"
+ "Received invalid recognizer ID in UpdateRecognizer %{public}lld"
- "%.*s"
- "FeedbackText ID = (%@) Text = %@"
- "Received invalid recognizer ID in UpdateRecognizer %lld"

```
