## SiriCrossDeviceArbitration

> `/System/Library/PrivateFrameworks/SiriCrossDeviceArbitration.framework/Versions/A/SiriCrossDeviceArbitration`

```diff

-  __TEXT.__text: 0x31040
-  __TEXT.__objc_methlist: 0x30d4
+  __TEXT.__text: 0x312ec
+  __TEXT.__objc_methlist: 0x30fc
   __TEXT.__const: 0x1b0
   __TEXT.__dlopen_cstrs: 0xc2
   __TEXT.__gcc_except_tab: 0x370
-  __TEXT.__oslogstring: 0x5428
-  __TEXT.__cstring: 0x5d8c
+  __TEXT.__oslogstring: 0x54a6
+  __TEXT.__cstring: 0x5da9
   __TEXT.__unwind_info: 0xd38
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_classlist: 0x148
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1df0
+  __DATA_CONST.__objc_selrefs: 0x1e08
   __DATA_CONST.__objc_superrefs: 0x128
   __DATA_CONST.__objc_arraydata: 0x60
   __DATA_CONST.__got: 0x2e8
   __AUTH_CONST.__const: 0xe60
-  __AUTH_CONST.__cfstring: 0x2e80
-  __AUTH_CONST.__objc_const: 0x5318
+  __AUTH_CONST.__cfstring: 0x2ea0
+  __AUTH_CONST.__objc_const: 0x5338
   __AUTH_CONST.__objc_intobj: 0x108
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__auth_got: 0x350
-  __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0x4f8
+  __AUTH.__objc_data: 0x640
+  __DATA.__objc_ivar: 0x4fc
   __DATA.__data: 0x5d0
   __DATA.__bss: 0x120
-  __DATA_DIRTY.__objc_data: 0xc80
+  __DATA_DIRTY.__objc_data: 0x690
   __DATA_DIRTY.__bss: 0x78
   __DATA_DIRTY.__common: 0x10
   - /System/Library/Frameworks/CoreBluetooth.framework/Versions/A/CoreBluetooth

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1265
-  Symbols:   3090
-  CStrings:  1413
+  Functions: 1269
+  Symbols:   3098
+  CStrings:  1417
 
Sections:
~ __TEXT.__gcc_except_tab : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__got : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __DATA.__data : content changed
Symbols:
+ -[SCDAAssistantPreferences myriadForceInstrumentationEnabled]
+ -[SCDAPreferences forceInstrumentationEnabled]
+ -[SCDARecord isAnOutgoing]
+ GCC_except_table1022
+ GCC_except_table1042
+ GCC_except_table1063
+ GCC_except_table1131
+ GCC_except_table1162
+ GCC_except_table1175
+ GCC_except_table251
+ GCC_except_table261
+ GCC_except_table529
+ GCC_except_table758
+ GCC_except_table804
+ GCC_except_table875
+ GCC_except_table890
+ GCC_except_table940
+ GCC_except_table944
+ GCC_except_table951
+ GCC_except_table978
+ OBJC_IVAR_$_SCDACoordinator._forceInstrumentationEnabled
+ ___61-[SCDAAssistantPreferences myriadForceInstrumentationEnabled]_block_invoke
+ _objc_msgSend$forceInstrumentationEnabled
+ _objc_msgSend$isAnOutgoing
+ _objc_msgSend$myriadForceInstrumentationEnabled
- GCC_except_table1019
- GCC_except_table1039
- GCC_except_table1060
- GCC_except_table1128
- GCC_except_table1156
- GCC_except_table1172
- GCC_except_table250
- GCC_except_table260
- GCC_except_table526
- GCC_except_table755
- GCC_except_table801
- GCC_except_table872
- GCC_except_table887
- GCC_except_table937
- GCC_except_table941
- GCC_except_table948
- GCC_except_table975
CStrings:
+ "%s #scda Not attempting / applying watch threshold boost because rebalance is enabled. rawAudioGoodnessScore: %u"
+ "%s BTLE trumping from in ear voice trigger"
+ "%s Skipping continuation loop: trigger was outgoing/self"
+ "%s Unexpectedly lowering goodness score %du for in ear trigger"
+ "Myriad Force Instrumentation"
- "%s #scda Not attempting / applying watch threshold boost because rebalance is enabled."
- "%s BTLE in-ear trigger entering election with default goodness"

```
