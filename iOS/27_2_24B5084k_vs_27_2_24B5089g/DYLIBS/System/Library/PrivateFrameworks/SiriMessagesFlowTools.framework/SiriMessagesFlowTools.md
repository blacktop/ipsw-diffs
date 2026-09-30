## SiriMessagesFlowTools

> `/System/Library/PrivateFrameworks/SiriMessagesFlowTools.framework/SiriMessagesFlowTools`

```diff

-3605.15.1.0.0
-  __TEXT.__text: 0x114718
+3605.17.1.1.1
+  __TEXT.__text: 0x1155f8
   __TEXT.__objc_methlist: 0x16c
-  __TEXT.__const: 0xaf54
+  __TEXT.__const: 0xaf64
   __TEXT.__swift5_typeref: 0x374e
   __TEXT.__swift5_reflstr: 0x2048
   __TEXT.__swift5_assocty: 0xd20

   __TEXT.__swift5_types: 0x274
   __TEXT.__swift_as_entry: 0x378
   __TEXT.__swift_as_ret: 0x46c
-  __TEXT.__cstring: 0x2034
+  __TEXT.__cstring: 0x20b4
   __TEXT.__swift_as_cont: 0x720
-  __TEXT.__oslogstring: 0x8351
-  __TEXT.__swift5_capture: 0x6f8
+  __TEXT.__oslogstring: 0x83a1
+  __TEXT.__swift5_capture: 0x708
   __TEXT.__swift5_protos: 0x54
   __TEXT.__swift5_mpenum: 0x4c
-  __TEXT.__unwind_info: 0x4628
-  __TEXT.__eh_frame: 0x9610
+  __TEXT.__unwind_info: 0x4640
+  __TEXT.__eh_frame: 0x9658
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x6f0
   __DATA_CONST.__objc_protorefs: 0x28
-  __DATA_CONST.__got: 0x1038
-  __AUTH_CONST.__const: 0x4928
+  __DATA_CONST.__got: 0x1028
+  __AUTH_CONST.__const: 0x4950
   __AUTH_CONST.__objc_const: 0x16b0
   __AUTH_CONST.__auth_got: 0x21c0
   __AUTH.__objc_data: 0x98
   __AUTH.__data: 0x1240
-  __DATA.__data: 0x1b08
+  __DATA.__data: 0x1af8
   __DATA.__common: 0x1d0
   __DATA_DIRTY.__objc_data: 0xb8
-  __DATA_DIRTY.__data: 0x19c0
-  __DATA_DIRTY.__bss: 0x2a00
+  __DATA_DIRTY.__data: 0x19d0
+  __DATA_DIRTY.__bss: 0x2e00
   __DATA_DIRTY.__common: 0xc0
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AppIntents.framework/AppIntents

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5719
+  Functions: 5728
   Symbols:   2222
-  CStrings:  639
+  CStrings:  640
 
Symbols:
+ _objc_msgSend$setActive:withOptions:error:
- _objc_msgSend$setActive:error:
CStrings:
+ "#UnsendLastMessageSentWithSiriTool %s: received a result other than .confirmed from callback.showActionConfirmation. Flow tool should never reach this point."
+ "invokeAppIntent(entities:hydratedTypedValue:toolDefinition:bundleIdentifier:typeName:callback:skipConfirmation:)"
- "#UnsendLastMessageSentWithSiriTool user cancelled unsend confirmation"
```
