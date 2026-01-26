## ScreenReaderOutput

> `/System/Library/PrivateFrameworks/ScreenReaderOutput.framework/ScreenReaderOutput`

```diff

-424.4.8.0.0
-  __TEXT.__text: 0x74f34
+424.4.11.0.0
+  __TEXT.__text: 0x753e8
   __TEXT.__auth_stubs: 0x1b60
-  __TEXT.__objc_methlist: 0x6ef0
-  __TEXT.__gcc_except_tab: 0x1890
+  __TEXT.__objc_methlist: 0x6f20
+  __TEXT.__gcc_except_tab: 0x1898
   __TEXT.__const: 0xc98
   __TEXT.__cstring: 0x5b88
-  __TEXT.__oslogstring: 0x20ab
+  __TEXT.__oslogstring: 0x225b
   __TEXT.__ustring: 0x9e
   __TEXT.__swift5_typeref: 0x51e
   __TEXT.__constg_swiftt: 0x488

   __TEXT.__swift_as_entry: 0x40
   __TEXT.__swift_as_ret: 0x48
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x1f98
+  __TEXT.__unwind_info: 0x1fb0
   __TEXT.__eh_frame: 0x6e8
   __TEXT.__objc_classname: 0xab8
-  __TEXT.__objc_methname: 0xfa2d
+  __TEXT.__objc_methname: 0xfa99
   __TEXT.__objc_methtype: 0x2293
-  __TEXT.__objc_stubs: 0xd680
+  __TEXT.__objc_stubs: 0xd6c0
   __DATA_CONST.__got: 0x608
   __DATA_CONST.__const: 0xc88
   __DATA_CONST.__objc_classlist: 0x2b0
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3ee8
+  __DATA_CONST.__objc_selrefs: 0x3ef8
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x1f0
   __DATA_CONST.__objc_arraydata: 0x380
   __AUTH_CONST.__auth_got: 0xdc0
-  __AUTH_CONST.__const: 0x1ab8
+  __AUTH_CONST.__const: 0x1af8
   __AUTH_CONST.__cfstring: 0x51c0
-  __AUTH_CONST.__objc_const: 0xf228
+  __AUTH_CONST.__objc_const: 0xf288
   __AUTH_CONST.__objc_intobj: 0x9d8
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0xd10
   __AUTH.__data: 0x5e0
-  __DATA.__objc_ivar: 0x848
+  __DATA.__objc_ivar: 0x850
   __DATA.__data: 0x10e0
   __DATA.__common: 0x30
   __DATA.__bss: 0x9b8

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 6CE85C44-C9AA-3566-BF1B-57ACFEA37C2F
-  Functions: 2949
-  Symbols:   9250
-  CStrings:  4789
+  UUID: 94F2B691-506C-315F-9F61-8DD344DACC7C
+  Functions: 2956
+  Symbols:   9270
+  CStrings:  4799
 
Symbols:
+ -[SCROBrailleDisplay setShouldForceLinearOutput:]
+ -[SCROBrailleDisplay shouldForceLinearOutput]
+ -[SCROBrailleLine setShouldForceLinearOutput:]
+ -[SCROBrailleLine shouldForceLinearOutput]
+ GCC_except_table109
+ GCC_except_table111
+ GCC_except_table131
+ GCC_except_table141
+ GCC_except_table145
+ GCC_except_table148
+ GCC_except_table151
+ GCC_except_table165
+ GCC_except_table167
+ GCC_except_table178
+ GCC_except_table199
+ GCC_except_table251
+ GCC_except_table306
+ GCC_except_table308
+ GCC_except_table343
+ GCC_except_table409
+ _OBJC_IVAR_$_SCROBrailleDisplay._shouldForceLinearOutput
+ _OBJC_IVAR_$_SCROBrailleLine._shouldForceLinearOutput
+ ___52-[SCROBrailleDisplayManager handleBrailleUIRequest:]_block_invoke_3
+ ___52-[SCROBrailleDisplayManager handleBrailleUIRequest:]_block_invoke_4
+ ___56-[SCROBrailleDisplayManager _eventQueue_startBrailleUI:]_block_invoke.187
+ ___56-[SCROBrailleDisplayManager _eventQueue_startBrailleUI:]_block_invoke_2
+ ___block_literal_global.193
+ ___block_literal_global.225
+ ___block_literal_global.345
+ _objc_msgSend$setShouldForceLinearOutput:
+ _objc_msgSend$shouldForceLinearOutput
- GCC_except_table107
- GCC_except_table110
- GCC_except_table130
- GCC_except_table140
- GCC_except_table143
- GCC_except_table147
- GCC_except_table149
- GCC_except_table164
- GCC_except_table166
- GCC_except_table176
- GCC_except_table197
- GCC_except_table249
- GCC_except_table303
- GCC_except_table305
- GCC_except_table340
- GCC_except_table406
- ___56-[SCROBrailleDisplayManager _eventQueue_startBrailleUI:]_block_invoke.189
- ___block_literal_global.336
CStrings:
+ "Error: Cannot access focusedItem - focusedIndex %ld is out of bounds for items array of size %lu"
+ "Error: Cannot navigate to first item - items array is empty"
+ "Error: Cannot navigate to last item - items array is empty"
+ "Error: Cannot navigate to next item - items array is empty"
+ "Error: Cannot navigate to previous item - items array is empty"
+ "Error: Cannot replace item - focusedIndex %ld is out of bounds for items array of size %lu"
+ "TB,N,V_shouldForceLinearOutput"
+ "_shouldForceLinearOutput"
+ "setShouldForceLinearOutput:"
+ "shouldForceLinearOutput"

```
