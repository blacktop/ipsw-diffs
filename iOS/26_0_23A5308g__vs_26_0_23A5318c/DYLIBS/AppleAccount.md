## AppleAccount

> `/System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount`

```diff

-1033.0.0.0.0
-  __TEXT.__text: 0xe8eb8
+1034.0.0.0.0
+  __TEXT.__text: 0xe9010
   __TEXT.__auth_stubs: 0x1180
-  __TEXT.__objc_methlist: 0xad1c
-  __TEXT.__cstring: 0xeecc
+  __TEXT.__objc_methlist: 0xad34
+  __TEXT.__cstring: 0xeeac
   __TEXT.__const: 0x2380
   __TEXT.__gcc_except_tab: 0x249c
   __TEXT.__oslogstring: 0xfc1d

   __TEXT.__swift5_capture: 0x90
   __TEXT.__swift_as_entry: 0x14
   __TEXT.__swift_as_ret: 0x14
-  __TEXT.__unwind_info: 0x2ee8
+  __TEXT.__unwind_info: 0x2ef0
   __TEXT.__eh_frame: 0x3e8
   __TEXT.__objc_classname: 0x1fac
-  __TEXT.__objc_methname: 0x1570a
+  __TEXT.__objc_methname: 0x1577f
   __TEXT.__objc_methtype: 0x2fe6
-  __TEXT.__objc_stubs: 0xc080
+  __TEXT.__objc_stubs: 0xc0c0
   __DATA_CONST.__got: 0xd80
   __DATA_CONST.__const: 0x3a98
   __DATA_CONST.__objc_classlist: 0x7f0
   __DATA_CONST.__objc_catlist: 0x98
   __DATA_CONST.__objc_protolist: 0x1e8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4d98
+  __DATA_CONST.__objc_selrefs: 0x4da8
   __DATA_CONST.__objc_protorefs: 0x78
   __DATA_CONST.__objc_superrefs: 0x570
   __DATA_CONST.__objc_arraydata: 0xe0
   __AUTH_CONST.__auth_got: 0x8d0
   __AUTH_CONST.__const: 0x7110
-  __AUTH_CONST.__cfstring: 0xcd40
+  __AUTH_CONST.__cfstring: 0xcd20
   __AUTH_CONST.__objc_const: 0x23760
   __AUTH_CONST.__objc_intobj: 0x120
   __AUTH_CONST.__objc_dictobj: 0x28

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 63637991-DA99-33AC-82E9-46300A550F7B
-  Functions: 4881
-  Symbols:   16149
+  UUID: 974A3ED0-B04A-3A0E-B1F3-971C2C1626B0
+  Functions: 4883
+  Symbols:   16155
   CStrings:  8895
 
Symbols:
+ -[AAFollowUpController(Convenience) _constructAnalyticsInforFromAccount:forIdentifier:]
+ -[AAFollowUpController(Convenience) sendPostCFUTelemetryEventWithAccount:forIdentifier:success:error:]
+ -[AAFollowUpController(Convenience) sendPostCFUTelemetryEventWithAccount:forIdentifier:success:error:].cold.1
+ ___101-[AAFollowUpController(Convenience) dismissFollowUpsStartingWithIdentifierPrefix:account:completion:]_block_invoke.382
+ ___101-[AAFollowUpController(Convenience) dismissFollowUpsStartingWithIdentifierPrefix:account:completion:]_block_invoke.382.cold.1
+ ___75-[AAFollowUpController(Convenience) pendingFollowUpsForAccount:completion:]_block_invoke.383
+ ___80-[AAFollowUpController(Convenience) _dismissFollowUpWithIdentifiers:completion:]_block_invoke.387
+ ___80-[AAFollowUpController(Convenience) _dismissFollowUpWithIdentifiers:completion:]_block_invoke.387.cold.1
+ ___87-[AAFollowUpController(Convenience) dismissFollowUpsForAccount:identifiers:completion:]_block_invoke.381
+ ___89-[AAFollowUpController(Convenience) dismissFollowUpWithIdentifier:forAccount:completion:]_block_invoke.379
+ ___89-[AAFollowUpController(Convenience) dismissFollowUpWithIdentifier:forAccount:completion:]_block_invoke.379.cold.1
+ ___89-[AAFollowUpController(Convenience) dismissFollowUpWithIdentifier:forAccount:completion:]_block_invoke.379.cold.2
+ ___91-[AAFollowUpController(Convenience) pendingFollowUpItemUserInfosWithIdentifier:completion:]_block_invoke.391
+ ____AAFollowUpControllerHandleSetupAssistantExited_block_invoke.443
+ ___block_literal_global.394
+ ___block_literal_global.445
+ _objc_msgSend$_constructAnalyticsInforFromAccount:forIdentifier:
+ _objc_msgSend$sendPostCFUTelemetryEventWithAccount:forIdentifier:success:error:
- GCC_except_table61
- ___101-[AAFollowUpController(Convenience) dismissFollowUpsStartingWithIdentifierPrefix:account:completion:]_block_invoke.385
- ___101-[AAFollowUpController(Convenience) dismissFollowUpsStartingWithIdentifierPrefix:account:completion:]_block_invoke.385.cold.1
- ___75-[AAFollowUpController(Convenience) pendingFollowUpsForAccount:completion:]_block_invoke.386
- ___80-[AAFollowUpController(Convenience) _dismissFollowUpWithIdentifiers:completion:]_block_invoke.390
- ___80-[AAFollowUpController(Convenience) _dismissFollowUpWithIdentifiers:completion:]_block_invoke.390.cold.1
- ___87-[AAFollowUpController(Convenience) dismissFollowUpsForAccount:identifiers:completion:]_block_invoke.384
- ___89-[AAFollowUpController(Convenience) dismissFollowUpWithIdentifier:forAccount:completion:]_block_invoke.382
- ___89-[AAFollowUpController(Convenience) dismissFollowUpWithIdentifier:forAccount:completion:]_block_invoke.382.cold.1
- ___89-[AAFollowUpController(Convenience) dismissFollowUpWithIdentifier:forAccount:completion:]_block_invoke.382.cold.2
- ___91-[AAFollowUpController(Convenience) pendingFollowUpItemUserInfosWithIdentifier:completion:]_block_invoke.395
- ___95-[AAFollowUpController(Convenience) postFollowUpWithIdentifier:forAccount:userInfo:completion:]_block_invoke.cold.1
- ____AAFollowUpControllerHandleSetupAssistantExited_block_invoke.437
- ___block_literal_global.398
- ___block_literal_global.439
CStrings:
+ "_constructAnalyticsInforFromAccount:forIdentifier:"
+ "sendPostCFUTelemetryEventWithAccount:forIdentifier:success:error:"
- "INHERITANCE_INVITED_MESSAGES_BUBBLE_BODY"

```
