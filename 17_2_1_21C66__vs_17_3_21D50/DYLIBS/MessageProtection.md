## MessageProtection

> `/System/Library/PrivateFrameworks/MessageProtection.framework/MessageProtection`

```diff

-327.60.2.0.0
-  __TEXT.__text: 0x3a5f8
+327.82.2.0.0
+  __TEXT.__text: 0x3a9dc
   __TEXT.__auth_stubs: 0x16f0
-  __TEXT.__objc_methlist: 0x1bfc
-  __TEXT.__cstring: 0x2731
-  __TEXT.__oslogstring: 0x168e
+  __TEXT.__objc_methlist: 0x1c24
+  __TEXT.__cstring: 0x26f1
+  __TEXT.__oslogstring: 0x170f
   __TEXT.__const: 0xf66
   __TEXT.__gcc_except_tab: 0x224
   __TEXT.__ustring: 0x21c

   __TEXT.__swift5_fieldmd: 0x414
   __TEXT.__swift5_capture: 0x40
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x1df0
+  __TEXT.__unwind_info: 0x1e0c
   __TEXT.__eh_frame: 0xef8
   __TEXT.__objc_classname: 0x510
-  __TEXT.__objc_methname: 0x3226
+  __TEXT.__objc_methname: 0x3278
   __TEXT.__objc_methtype: 0xaea
-  __TEXT.__objc_stubs: 0x2800
+  __TEXT.__objc_stubs: 0x2840
   __DATA_CONST.__got: 0x2e0
   __DATA_CONST.__const: 0x2d0
   __DATA_CONST.__objc_classlist: 0x1d8

   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x3d48
-  __DATA_CONST.__objc_selrefs: 0xc80
+  __DATA_CONST.__objc_selrefs: 0xc98
   __AUTH_CONST.__objc_const: 0x48
-  __AUTH_CONST.__cfstring: 0x17c0
+  __AUTH_CONST.__cfstring: 0x17a0
   __AUTH_CONST.__auth_ptr: 0x78
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__const: 0x418

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 1345
-  Symbols:   4456
-  CStrings:  1143
+  Functions: 1351
+  Symbols:   4470
+  CStrings:  1147
 
Symbols:
+ -[NGMFullDeviceIdentity testing_duplicatePrekeyRegistration]
+ -[NGMReplayManager duplicateTagForPrekey:]
+ -[NGMReplayManager duplicateTagForPrekey:].cold.1
+ -[NGMReplayManager pruneDuplicates:tag:moc:]
+ -[NGMReplayManager registeredPrekeyForNGMPrekey:objectContext:].cold.2
+ _OUTLINED_FUNCTION_5
+ _objc_msgSend$duplicateTagForPrekey:
+ _objc_msgSend$pruneDuplicates:tag:moc:
CStrings:
+ "Failed to create a duplicate for the prekey. {error = %@}"
+ "We have duplicate entries on registered prekey. {tag = %@, error = %@}"
+ "duplicateTagForPrekey:"
+ "pruneDuplicates:tag:moc:"
+ "testing_duplicatePrekeyRegistration"
- "We have duplicate entries on registered prekey: %@."

```
