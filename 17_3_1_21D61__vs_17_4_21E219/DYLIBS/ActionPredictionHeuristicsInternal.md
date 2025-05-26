## ActionPredictionHeuristicsInternal

> `/System/Library/PrivateFrameworks/ActionPredictionHeuristicsInternal.framework/ActionPredictionHeuristicsInternal`

```diff

-541.10.1.0.0
-  __TEXT.__text: 0x404a4
+541.14.0.0.0
+  __TEXT.__text: 0x40644
   __TEXT.__auth_stubs: 0x8e0
-  __TEXT.__objc_methlist: 0x26a0
+  __TEXT.__objc_methlist: 0x26d0
   __TEXT.__const: 0x230
-  __TEXT.__cstring: 0x331c
-  __TEXT.__gcc_except_tab: 0xcf0
-  __TEXT.__oslogstring: 0x6efb
+  __TEXT.__cstring: 0x332f
+  __TEXT.__gcc_except_tab: 0xcf4
+  __TEXT.__oslogstring: 0x6f0b
   __TEXT.__dlopen_cstrs: 0x138
-  __TEXT.__unwind_info: 0xdec
-  __TEXT.__objc_classname: 0xcaa
-  __TEXT.__objc_methname: 0x7eee
-  __TEXT.__objc_methtype: 0x11fb
-  __TEXT.__objc_stubs: 0x7240
+  __TEXT.__unwind_info: 0xe04
+  __TEXT.__objc_classname: 0xcab
+  __TEXT.__objc_methname: 0x8002
+  __TEXT.__objc_methtype: 0x1218
+  __TEXT.__objc_stubs: 0x7340
   __DATA_CONST.__got: 0x218
   __DATA_CONST.__const: 0xc08
   __DATA_CONST.__objc_classlist: 0x328
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x8050
-  __DATA_CONST.__objc_selrefs: 0x1ef0
+  __DATA_CONST.__objc_const: 0x8090
+  __DATA_CONST.__objc_selrefs: 0x1f30
+  __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_classrefs: 0x750
+  __DATA_CONST.__objc_superrefs: 0x230
   __DATA_CONST.__objc_arraydata: 0x128
-  __AUTH_CONST.__cfstring: 0x3640
+  __AUTH_CONST.__cfstring: 0x3660
   __AUTH_CONST.__objc_const: 0x2518
   __AUTH_CONST.__const: 0x800
   __AUTH_CONST.__objc_arrayobj: 0x1f8
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__auth_got: 0x480
-  __AUTH.__objc_data: 0x780
-  __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x748
-  __DATA.__objc_superrefs: 0x230
-  __DATA.__objc_ivar: 0x2fc
+  __AUTH.__objc_data: 0x730
+  __DATA.__objc_ivar: 0x304
   __DATA.__data: 0x340
   __DATA.__bss: 0x248
-  __DATA_DIRTY.__objc_data: 0x1810
+  __DATA_DIRTY.__objc_data: 0x1860
   __DATA_DIRTY.__data: 0x40
   __DATA_DIRTY.__bss: 0xf8
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /System/Library/PrivateFrameworks/VoiceShortcutClient.framework/VoiceShortcutClient
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1151
-  Symbols:   5019
-  CStrings:  2444
+  Functions: 1156
+  Symbols:   5041
+  CStrings:  2457
 
Symbols:
+ -[ATXInformationHeuristicRefreshNotitifcationTrigger _createCoalescingTimer]
+ -[ATXInformationHeuristicRefreshNotitifcationTrigger _scheduleTriggerRefresh]
+ -[ATXInformationHeuristicRefreshNotitifcationTrigger _triggerRefresh]
+ -[ATXInformationHeuristicRefreshNotitifcationTrigger initWithNotification:type:coalescingInterval:]
+ GCC_except_table30
+ GCC_except_table34
+ GCC_except_table48
+ GCC_except_table59
+ GCC_except_table78
+ _OBJC_CLASS_$__PASSimpleCoalescingTimer
+ _OBJC_IVAR_$_ATXInformationHeuristicRefreshNotitifcationTrigger._coalescingInterval
+ _OBJC_IVAR_$_ATXInformationHeuristicRefreshNotitifcationTrigger._coalescingTimer
+ ___52-[ATXInformationHeuristicRefreshBiomeTrigger _start]_block_invoke.175
+ ___60-[ATXInformationHeuristicRefreshNotitifcationTrigger _start]_block_invoke.91
+ ___76-[ATXInformationHeuristicRefreshNotitifcationTrigger _createCoalescingTimer]_block_invoke
+ _objc_msgSend$_createCoalescingTimer
+ _objc_msgSend$_scheduleTriggerRefresh
+ _objc_msgSend$_triggerRefresh
+ _objc_msgSend$decodeDoubleForKey:
+ _objc_msgSend$encodeDouble:forKey:
+ _objc_msgSend$initWithNotification:type:coalescingInterval:
+ _objc_msgSend$initWithQueue:operation:
+ _objc_msgSend$runAfterDelaySeconds:coalescingBehavior:
- GCC_except_table43
- GCC_except_table54
- GCC_except_table73
- ___52-[ATXInformationHeuristicRefreshBiomeTrigger _start]_block_invoke.162
- ___60-[ATXInformationHeuristicRefreshNotitifcationTrigger _start]_block_invoke.90
CStrings:
+ "\x12\x11"
+ "@\"_PASSimpleCoalescingTimer\""
+ "ATXInformationHeuristicRefreshNotitifcationTrigger (%p): Received Darwin notification: %{public}@. Triggering heuristics refresh."
+ "ATXInformationHeuristicRefreshNotitifcationTrigger (%p): Received local notification: %{public}@. Triggering heuristics refresh."
+ "T@\"NSString\",?,R,C"
+ "_coalescingInterval"
+ "_coalescingTimer"
+ "_createCoalescingTimer"
+ "_scheduleTriggerRefresh"
+ "_triggerRefresh"
+ "coalescingInterval"
+ "decodeDoubleForKey:"
+ "encodeDouble:forKey:"
+ "initWithNotification:type:coalescingInterval:"
+ "initWithQueue:operation:"
+ "runAfterDelaySeconds:coalescingBehavior:"
- "\x12"
- "ATXInformationHeuristicRefreshNotitifcationTrigger (%p): Received Darwin notification: %@. Triggering heuristics refresh."
- "ATXInformationHeuristicRefreshNotitifcationTrigger (%p): Received local notification: %@. Triggering heuristics refresh."

```
