## TypistFramework

> `/System/Library/PrivateFrameworks/TypistFramework.framework/TypistFramework`

```diff

-476.0.0.0.0
-  __TEXT.__text: 0x41570
+477.0.0.0.0
+  __TEXT.__text: 0x413c8
   __TEXT.__auth_stubs: 0xd60
   __TEXT.__objc_methlist: 0x3774
   __TEXT.__const: 0x3c2
-  __TEXT.__gcc_except_tab: 0xbe4
-  __TEXT.__cstring: 0x58a2
+  __TEXT.__gcc_except_tab: 0xbcc
+  __TEXT.__cstring: 0x5892
   __TEXT.__ustring: 0x1366
   __TEXT.__dlopen_cstrs: 0x6d
   __TEXT.__oslogstring: 0xc

   __TEXT.__unwind_info: 0xe10
   __TEXT.__eh_frame: 0x48
   __TEXT.__objc_classname: 0x554
-  __TEXT.__objc_methname: 0x8534
+  __TEXT.__objc_methname: 0x854b
   __TEXT.__objc_methtype: 0x114f
-  __TEXT.__objc_stubs: 0x7ac0
+  __TEXT.__objc_stubs: 0x7ae0
   __DATA_CONST.__got: 0x530
   __DATA_CONST.__const: 0x8d8
   __DATA_CONST.__objc_classlist: 0x188
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x23d0
+  __DATA_CONST.__objc_selrefs: 0x23d8
   __DATA_CONST.__objc_superrefs: 0x120
   __DATA_CONST.__objc_arraydata: 0x3c28
   __AUTH_CONST.__auth_got: 0x6c0

   __AUTH.__data: 0x28
   __DATA.__objc_ivar: 0x2a8
   __DATA.__data: 0x1e8
-  __DATA.__bss: 0x300
+  __DATA.__bss: 0x2f0
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x168
   __DATA_DIRTY.__bss: 0x48

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  UUID: B5EF75A8-84BA-3338-AEAE-E43556A4C970
-  Functions: 1294
-  Symbols:   4612
-  CStrings:  5287
+  UUID: 08F2AB14-F270-33E5-984E-E4138B46AE0F
+  Functions: 1293
+  Symbols:   4610
+  CStrings:  5288
 
Symbols:
+ ___block_descriptor_64_e8_32s40s48r_e34_v16?0"<RCPEventStreamComposer>"8ls32l8s40l8r48l8
+ ___block_descriptor_72_e8_32s40s48s56s64r_e34_v16?0"<RCPEventStreamComposer>"8ls32l8s40l8s48l8s56l8r64l8
+ ___block_literal_global.346
+ ___block_literal_global.508
+ ___block_literal_global.522
+ __activeConnectionPtr.activeConnection
+ _objc_msgSend$getVisibleKeyboardName
- ___48+[TypistKeyboardDataInputUIClient tryConnection]_block_invoke
- ___block_descriptor_72_e8_32s40s48r56r_e34_v16?0"<RCPEventStreamComposer>"8ls32l8s40l8r48l8r56l8
- ___block_descriptor_80_e8_32s40s48s56s64r72r_e34_v16?0"<RCPEventStreamComposer>"8ls32l8s40l8r64l8s48l8s56l8r72l8
- ___block_literal_global.349
- ___block_literal_global.511
- ___block_literal_global.525
- __activeConnectionPtr.activeConnectionPtr
- _tryConnection.onceToken
Functions:
~ -[TypistHWKeyboard _usagePairsForText:] : 668 -> 532
~ ___39-[TypistHWKeyboard _usagePairsForText:]_block_invoke : 1480 -> 1444
~ -[TypistHWKeyboard pressAndHoldKeys:forDuration:withValidation:after:] : 676 -> 552
~ ___70-[TypistHWKeyboard pressAndHoldKeys:forDuration:withValidation:after:]_block_invoke : 952 -> 904
~ +[TypistKeyboardDataInputUIClient connectToRemoteKeyboard:targetApplication:] : 148 -> 152
~ +[TypistKeyboardDataInputUIClient tryConnection] : 136 -> 152
- ___48+[TypistKeyboardDataInputUIClient tryConnection]_block_invoke
~ +[TypistKeyboardDataInputUIClient getAllCandidates] : 108 -> 112
~ +[TypistKeyboardDataInputUIClient getVisibleCandidateList:] : 176 -> 188
CStrings:
+ "[TypistHWKeyboard - _usagePairsForText]: Generating events -- [%@]"
+ "[TypistHWKeyboard - pressAndHoldKeys]: Generating events -- [%@]"
+ "getVisibleKeyboardName"
- "[TypistHWKeyboard - _usagePairsForText]: Generating events for text [%@] -- [%@]"
- "[TypistHWKeyboard - pressAndHoldKeys]: Generating events for text [%@] -- [%@]"

```
