## CryptoTokenKit

> `/System/Library/Frameworks/CryptoTokenKit.framework/CryptoTokenKit`

```diff

-  __TEXT.__text: 0x4977c
+  __TEXT.__text: 0x4a020
   __TEXT.__delay_helper: 0x1f0
-  __TEXT.__objc_methlist: 0x47f4
-  __TEXT.__gcc_except_tab: 0x14d4
+  __TEXT.__objc_methlist: 0x47fc
+  __TEXT.__gcc_except_tab: 0x15ac
   __TEXT.__const: 0x2d0
-  __TEXT.__cstring: 0x3194
-  __TEXT.__oslogstring: 0x3763
+  __TEXT.__cstring: 0x31c4
+  __TEXT.__oslogstring: 0x389d
   __TEXT.__dlopen_cstrs: 0x104
   __TEXT.__swift5_typeref: 0x6a
   __TEXT.__swift5_capture: 0x2c
   __TEXT.__swift_as_entry: 0x4
   __TEXT.__swift_as_ret: 0x4
   __TEXT.__swift_as_cont: 0xc
-  __TEXT.__unwind_info: 0x1878
+  __TEXT.__unwind_info: 0x18a8
   __TEXT.__eh_frame: 0x108
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x18e8
+  __DATA_CONST.__const: 0x1938
   __DATA_CONST.__objc_classlist: 0x318
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x130
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2288
+  __DATA_CONST.__objc_selrefs: 0x22b0
   __DATA_CONST.__objc_protorefs: 0x98
   __DATA_CONST.__objc_superrefs: 0x290
   __DATA_CONST.__objc_arraydata: 0x8
-  __DATA_CONST.__got: 0x5f8
+  __DATA_CONST.__got: 0x620
   __AUTH_CONST.__const: 0xba8
   __AUTH_CONST.__cfstring: 0x3240
   __AUTH_CONST.__objc_const: 0x8b20
   __AUTH_CONST.__objc_intobj: 0x5d0
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_got: 0x750
-  __AUTH.__objc_data: 0x5a0
+  __AUTH.__objc_data: 0x1180
   __DATA.__objc_ivar: 0x58c
-  __DATA.__data: 0xe74
-  __DATA.__bss: 0x218
+  __DATA.__data: 0xe78
+  __DATA.__bss: 0x278
   __DATA.__common: 0x11
-  __DATA_DIRTY.__objc_data: 0x1950
-  __DATA_DIRTY.__bss: 0x280
+  __DATA_DIRTY.__objc_data: 0xd70
+  __DATA_DIRTY.__bss: 0x220
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  Functions: 2066
-  Symbols:   7304
-  CStrings:  1265
+  Functions: 2071
+  Symbols:   7326
+  CStrings:  1272
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__swift5_capture : content changed
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift_as_ret : content changed
~ __TEXT.__swift_as_cont : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
Symbols:
+ -[TKSmartCardSlotEngine clientConnectionTerminated:]
+ GCC_except_table43
+ GCC_except_table49
+ GCC_except_table52
+ GCC_except_table64
+ GCC_except_table74
+ GCC_except_table82
+ GCC_except_table84
+ _OBJC_CLASS_$_NSMutableIndexSet
+ _OUTLINED_FUNCTION_45
+ _OUTLINED_FUNCTION_52
+ _OUTLINED_FUNCTION_56
+ _OUTLINED_FUNCTION_58
+ ___52-[TKSmartCardSlotEngine clientConnectionTerminated:]_block_invoke
+ ___60-[TKSmartCardSlotEngine listener:shouldAcceptNewConnection:]_block_invoke
+ ___60-[TKSmartCardSlotEngine listener:shouldAcceptNewConnection:]_block_invoke_2
+ ___block_descriptor_48_e8_32s40s_e42_v32?0"TKSmartCardSessionRequest"8Q16^B24ls32l8s40l8
+ ___block_descriptor_48_e8_32w40w_e5_v8?0lw32l8w40l8
+ _objc_msgSend$addIndex:
+ _objc_msgSend$clientConnectionTerminated:
+ _objc_msgSend$enumerateObjectsUsingBlock:
+ _objc_msgSend$indexSet
+ _objc_msgSend$removeObjectsAtIndexes:
- GCC_except_table70
- GCC_except_table80
- _OUTLINED_FUNCTION_33
- _OUTLINED_FUNCTION_46
- _OUTLINED_FUNCTION_54
- _OUTLINED_FUNCTION_57
- _OUTLINED_FUNCTION_61
CStrings:
+ "%{public}@: client pid %d gone while holding the session, reclaiming it"
+ "%{public}@: client pid %d gone, dropping %lu queued session request(s)"
+ "%{public}@: clientConnectionTerminated for pid %d"
+ "%{public}@: session busy (held by pid %d), pid %d queued behind it (%lu waiting); notifying holder"
+ "%{public}@: session granted to pid %d (%lu still waiting)"
+ "%{public}@: session requested by pid %d (%lu now queued)"
+ "%{public}@: state reply for client with no pending request, ignoring"
+ "v32@?0@\"TKSmartCardSessionRequest\"8Q16^B24"
- "%{public}@: notifyWithParameters reply for client with no state request — request was torn down or replaced mid-flight (waitForStateFlushedWithReply may stall)"

```
