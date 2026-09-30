## UIKitCore

> `/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`

```diff

-9126.5.1.1.101
-  __TEXT.__text: 0x1b526e8
+9126.5.3.0.0
+  __TEXT.__text: 0x1b53444
   __TEXT.__auth_stubs: 0xdb60
   __TEXT.__delay_helper: 0x1bc
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x1947d0
-  __TEXT.__const: 0x40db8
+  __TEXT.__objc_methlist: 0x194818
+  __TEXT.__const: 0x40da8
   __TEXT.__dlopen_cstrs: 0x4a2f
   __TEXT.__swift5_typeref: 0x13dda
   __TEXT.__swift5_capture: 0xdae0
-  __TEXT.__cstring: 0xf156c
+  __TEXT.__cstring: 0xf15b9
   __TEXT.__swift5_reflstr: 0x135e7
   __TEXT.__swift5_assocty: 0x40b0
   __TEXT.__swift5_fieldmd: 0x136e4

   __TEXT.__swift5_protos: 0x200
   __TEXT.__swift5_proto: 0x1ec8
   __TEXT.__swift5_types: 0x1760
-  __TEXT.__oslogstring: 0x4c40d
+  __TEXT.__oslogstring: 0x4c45b
   __TEXT.__swift_as_entry: 0x18c
   __TEXT.__swift_as_ret: 0x130
   __TEXT.__swift5_mpenum: 0x21c
   __TEXT.__swift5_types2: 0x4
   __TEXT.__gcc_except_tab: 0x25e6c
   __TEXT.__ustring: 0x2786
-  __TEXT.__unwind_info: 0x71968
+  __TEXT.__unwind_info: 0x71980
   __TEXT.__eh_frame: 0x7000
   __TEXT.__objc_classname: 0x3c8c0
-  __TEXT.__objc_methname: 0x3212ea
+  __TEXT.__objc_methname: 0x32141a
   __TEXT.__objc_methtype: 0x790b8
-  __TEXT.__objc_stubs: 0x1e3ce0
+  __TEXT.__objc_stubs: 0x1e3da0
   __DATA_CONST.__got: 0x7950
   __DATA_CONST.__const: 0x3c628
   __DATA_CONST.__objc_classlist: 0xae10
   __DATA_CONST.__objc_catlist: 0x328
   __DATA_CONST.__objc_protolist: 0x31b8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x929e8
+  __DATA_CONST.__objc_selrefs: 0x92a50
   __DATA_CONST.__objc_protorefs: 0xc30
   __DATA_CONST.__objc_superrefs: 0x73f0
-  __DATA_CONST.__objc_arraydata: 0x4638
+  __DATA_CONST.__objc_arraydata: 0x4648
   __AUTH_CONST.__auth_got: 0x6dc8
-  __AUTH_CONST.__const: 0x5cfb8
-  __AUTH_CONST.__cfstring: 0xb05e0
-  __AUTH_CONST.__objc_const: 0x267a88
+  __AUTH_CONST.__const: 0x5cff8
+  __AUTH_CONST.__cfstring: 0xb0620
+  __AUTH_CONST.__objc_const: 0x267a98
   __AUTH_CONST.__objc_arrayobj: 0x2f28
   __AUTH_CONST.__objc_doubleobj: 0x1000
   __AUTH_CONST.__objc_intobj: 0x4fc8

   __DATA_DIRTY.__objc_data: 0x2bae8
   __DATA_DIRTY.__uikit_ip: 0x11e8
   __DATA_DIRTY.__data: 0x7488
-  __DATA_DIRTY.__bss: 0x13438
+  __DATA_DIRTY.__bss: 0x13458
   __DATA_DIRTY.__common: 0x4a0
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/Accessibility.framework/Accessibility

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: FECB8690-456C-3818-9F12-83A7AC9C5AD3
-  Functions: 173480
-  Symbols:   437788
-  CStrings:  181172
+  UUID: CE4034D5-7EE1-3C19-B122-15CE3982B20E
+  Functions: 173489
+  Symbols:   437814
+  CStrings:  181192
 
Symbols:
+ +[UIKeyboardImpl systemShellMinimumKeyboardPadding]
+ +[_UISignalAnalytics asyncSignalQueue]
+ +[_UISignalAnalytics sendSignal:toChannel:withNullableUniqueStringID:withCreationTimestamp:withPayload:]
+ -[UIKBRTIPartner _canHandleResponderCommand:sender:target:]
+ -[UIKBRTIPartner _tryKeyCommand:]
+ -[UIKBRTIPartner _tryKeyCommandWithSelector:]
+ GCC_except_table1005
+ GCC_except_table265
+ ___38+[_UISignalAnalytics asyncSignalQueue]_block_invoke
+ ___45-[UIKBRTIPartner _tryKeyCommandWithSelector:]_block_invoke
+ ___53-[UIKBRTIPartner _queryWKDocumentRequest:completion:]_block_invoke.917
+ ___61+[_UISignalAnalytics asyncSendMissingKeyboardSignal:payload:]_block_invoke
+ ___block_literal_global.1257
+ ___block_literal_global.1273
+ ___block_literal_global.2579
+ ___block_literal_global.394
+ ___block_literal_global.498
+ ___block_literal_global.569
+ _objc_msgSend$_canHandleResponderCommand:sender:target:
+ _objc_msgSend$_tryKeyCommand:
+ _objc_msgSend$_tryKeyCommandWithSelector:
+ _objc_msgSend$asyncSignalQueue
+ _objc_msgSend$sendSignal:toChannel:withNullableUniqueStringID:withCreationTimestamp:withPayload:
+ _objc_msgSend$systemShellMinimumKeyboardPadding
- GCC_except_table1004
- GCC_except_table1012
- GCC_except_table256
- GCC_except_table266
- GCC_except_table331
- ___53-[UIKBRTIPartner _queryWKDocumentRequest:completion:]_block_invoke.861
- ___block_literal_global.1197
- ___block_literal_global.1200
- ___block_literal_global.1213
- ___block_literal_global.2576
- ___block_literal_global.478
- ___block_literal_global.483
- ___block_literal_global.568
- ___block_literal_global.868
CStrings:
+ "Inuktitut-Nattilik"
+ "Inuktitut-Nunavik"
+ "Inuktitut-Nunavut"
+ "Key command '%@' has unexpected argument count: %lu"
+ "SPI 32 missing at runtime"
+ "_canHandleResponderCommand:sender:target:"
+ "_tryKeyCommand:"
+ "_tryKeyCommandWithSelector:"
+ "asyncSignalQueue"
+ "com.apple.UIKit.signalAnalytics"
+ "insertParagraphSeparator:"
+ "moveToBeginningOfLine:"
+ "moveToEndOfLine:"
+ "pageDown:"
+ "pageUp:"
+ "scrollPageDown:"
+ "scrollPageUp:"
+ "sendSignal:toChannel:withNullableUniqueStringID:withCreationTimestamp:withPayload:"
+ "systemShellMinimumKeyboardPadding"
- "Inuktitut"

```
