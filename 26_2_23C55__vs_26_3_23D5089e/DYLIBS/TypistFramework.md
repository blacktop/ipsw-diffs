## TypistFramework

> `/System/Library/PrivateFrameworks/TypistFramework.framework/TypistFramework`

```diff

-474.0.0.0.0
-  __TEXT.__text: 0x41274
+476.0.0.0.0
+  __TEXT.__text: 0x41570
   __TEXT.__auth_stubs: 0xd60
   __TEXT.__objc_methlist: 0x3774
   __TEXT.__const: 0x3c2
-  __TEXT.__gcc_except_tab: 0xb94
-  __TEXT.__cstring: 0x57b2
+  __TEXT.__gcc_except_tab: 0xbe4
+  __TEXT.__cstring: 0x58a2
   __TEXT.__ustring: 0x1366
   __TEXT.__dlopen_cstrs: 0x6d
   __TEXT.__oslogstring: 0xc

   __TEXT.__swift5_fieldmd: 0x94
   __TEXT.__swift5_proto: 0x4
   __TEXT.__swift5_types: 0x10
-  __TEXT.__unwind_info: 0xdf8
+  __TEXT.__unwind_info: 0xe10
   __TEXT.__eh_frame: 0x48
   __TEXT.__objc_classname: 0x554
   __TEXT.__objc_methname: 0x8534

   __DATA_CONST.__objc_arraydata: 0x3c28
   __AUTH_CONST.__auth_got: 0x6c0
   __AUTH_CONST.__const: 0x608
-  __AUTH_CONST.__cfstring: 0x11440
+  __AUTH_CONST.__cfstring: 0x114c0
   __AUTH_CONST.__objc_const: 0x49b0
   __AUTH_CONST.__objc_doubleobj: 0x80
   __AUTH_CONST.__objc_intobj: 0xbb8

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  UUID: 482FDDF1-B7FE-3B1F-B4D7-D1756931DA6A
+  UUID: B5EF75A8-84BA-3338-AEAE-E43556A4C970
   Functions: 1294
-  Symbols:   4610
-  CStrings:  5279
+  Symbols:   4612
+  CStrings:  5287
 
Symbols:
+ GCC_except_table13
+ GCC_except_table19
+ ___block_descriptor_72_e8_32s40s48r56r_e34_v16?0"<RCPEventStreamComposer>"8ls32l8s40l8r48l8r56l8
+ ___block_descriptor_80_e8_32s40s48s56s64r72r_e34_v16?0"<RCPEventStreamComposer>"8ls32l8s40l8r64l8s48l8s56l8r72l8
+ ___block_literal_global.349
+ ___block_literal_global.511
+ ___block_literal_global.525
- ___block_descriptor_56_e8_32s40s_e34_v16?0"<RCPEventStreamComposer>"8ls32l8s40l8
- ___block_descriptor_64_e8_32s40s48s56s_e34_v16?0"<RCPEventStreamComposer>"8ls32l8s40l8s48l8s56l8
- ___block_literal_global.334
- ___block_literal_global.496
- ___block_literal_global.510
Functions:
~ -[TypistHWKeyboard _usagePairsForText:] : 368 -> 668
~ ___39-[TypistHWKeyboard _usagePairsForText:]_block_invoke -> ___Block_byref_object_copy_ : 1380 -> 16
~ -[TypistHWKeyboard generateEventStream:] -> ___Block_byref_object_dispose_ : 144 -> 8
~ -[TypistHWKeyboard _generateKeystrokeStream:appendTypeInterval:] -> ___39-[TypistHWKeyboard _usagePairsForText:]_block_invoke : 1528 -> 1480
~ -[TypistHWKeyboard pressKeycodes:] -> -[TypistHWKeyboard generateEventStream:] : 636 -> 144
~ ___Block_byref_object_copy_ -> -[TypistHWKeyboard _generateKeystrokeStream:appendTypeInterval:] : 16 -> 1528
~ ___Block_byref_object_dispose_ -> -[TypistHWKeyboard pressKeycodes:] : 8 -> 660
~ -[TypistHWKeyboard pressAndHoldKeys:forDuration:withValidation:after:] : 452 -> 676
~ ___70-[TypistHWKeyboard pressAndHoldKeys:forDuration:withValidation:after:]_block_invoke : 844 -> 952
~ -[TypistKeyboard attachHardwareKeyboardWithCountryCode:] : 148 -> 156
CStrings:
+ "(%@)"
+ "(%@) "
+ "[TypistHWKeyboard - _usagePairsForText]: Generating events for text [%@] -- [%@]"
+ "[TypistHWKeyboard - pressAndHoldKeys]: Generating events for text [%@] -- [%@]"
+ "[TypistHWKeyboard - pressKeycodes]: Key press sequence for keycodes: [%@] -- [%@]"
- "sender %@ "

```
