## UnblockClient

> `/System/Library/PrivateFrameworks/UnblockClient.framework/UnblockClient`

```diff

-13.0.0.0.0
-  __TEXT.__text: 0x6000
-  __TEXT.__auth_stubs: 0x4e0
-  __TEXT.__objc_methlist: 0x538
+14.0.0.0.0
+  __TEXT.__text: 0x6828
+  __TEXT.__auth_stubs: 0x470
+  __TEXT.__objc_methlist: 0x558
   __TEXT.__const: 0x78
-  __TEXT.__gcc_except_tab: 0x150
-  __TEXT.__cstring: 0xb68
+  __TEXT.__gcc_except_tab: 0x10c
+  __TEXT.__cstring: 0xf28
   __TEXT.__oslogstring: 0x615
-  __TEXT.__unwind_info: 0x170
-  __TEXT.__objc_classname: 0x9c
-  __TEXT.__objc_methname: 0xf81
+  __TEXT.__unwind_info: 0x168
+  __TEXT.__objc_classname: 0x9f
+  __TEXT.__objc_methname: 0xfc9
   __TEXT.__objc_methtype: 0x1d5
-  __TEXT.__objc_stubs: 0xc00
+  __TEXT.__objc_stubs: 0xc40
   __DATA_CONST.__got: 0xd8
-  __DATA_CONST.__const: 0x1b0
+  __DATA_CONST.__const: 0x1e0
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3e8
+  __DATA_CONST.__objc_selrefs: 0x400
   __DATA_CONST.__objc_superrefs: 0x30
-  __AUTH_CONST.__auth_got: 0x280
+  __AUTH_CONST.__auth_got: 0x248
   __AUTH_CONST.__const: 0xc0
-  __AUTH_CONST.__cfstring: 0xf00
-  __AUTH_CONST.__objc_const: 0xb40
+  __AUTH_CONST.__cfstring: 0x1100
+  __AUTH_CONST.__objc_const: 0xb78
   __AUTH_CONST.__objc_intobj: 0x30
-  __DATA.__objc_ivar: 0x88
+  __DATA.__objc_ivar: 0x8c
   __DATA.__data: 0xc0
   __DATA_DIRTY.__objc_data: 0x1e0
   __DATA_DIRTY.__bss: 0x10

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E3A126F5-192F-3611-B3AD-C13FC51F09C2
-  Functions: 140
-  Symbols:   600
-  CStrings:  508
+  UUID: F1466257-6DB2-37CF-84BA-DC30B7BBED45
+  Functions: 146
+  Symbols:   609
+  CStrings:  544
 
Symbols:
+ -[UBStuckServiceRecoveryResult suppressTelemetry]
+ -[UBUnblockClient clientName]
+ -[UBUnblockClient setClientName:]
+ -[UBUnblockClient(XPCHandling) openConnectionToUnblockService].cold.3
+ GCC_except_table54
+ _OBJC_IVAR_$_UBUnblockClient._clientName
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ __OBJC_$_PROP_LIST_UBUnblockClient
+ ___58-[UBStuckServiceRecoveryResult _recoveryHadEffectiveness:]_block_invoke.369
+ ___58-[UBStuckServiceRecoveryResult _recoveryHadEffectiveness:]_block_invoke_2.380
+ ___61-[UBUnblockClient recover:stackshotData:replyQueue:callback:]_block_invoke.664
+ ___61-[UBUnblockClient recover:stackshotData:replyQueue:callback:]_block_invoke.665
+ ___block_literal_global.382
+ ___block_literal_global.393
+ ___block_literal_global.401
+ ___block_literal_global.623
+ __os_log_debug_impl
+ _objc_msgSend$UTF8String
+ _objc_msgSend$setThreadID:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x26
- GCC_except_table53
- ___58-[UBStuckServiceRecoveryResult _recoveryHadEffectiveness:]_block_invoke.327
- ___58-[UBStuckServiceRecoveryResult _recoveryHadEffectiveness:]_block_invoke_2.338
- ___61-[UBUnblockClient recover:stackshotData:replyQueue:callback:]_block_invoke.615
- ___61-[UBUnblockClient recover:stackshotData:replyQueue:callback:]_block_invoke.616
- ___block_literal_global.340
- ___block_literal_global.351
- ___block_literal_global.359
- ___block_literal_global.574
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x24
- _objc_retain_x28
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x8
- _objc_unsafeClaimAutoreleasedReturnValue
CStrings:
+ "%@ (%d)"
+ "(no thread)"
+ "Deadlock cycle:                             %@ -> %@\n"
+ "Issue type:                                 %@\n"
+ "Monitored service:                          "
+ "Monitoring process:                         %@\n"
+ "Number of other issues:                     %ld\n"
+ "Processes blocked by other issues:          %@\n"
+ "Processes blocked by this issue:            %@\n"
+ "Recovery confidence:                        %@\n"
+ "Service dependency chain:                   %@\n"
+ "T@\"NSString\",&,V_clientName"
+ "Threads stuck:                              %lu threads stuck"
+ "Time since issue began:                     %@s"
+ "UTF8String"
+ "Unblock recovery status:                    %@\n"
+ "Unblock selected process (not terminated):  %@ [%d]\n"
+ "Unblock terminated process:                 %@ [%d]\n"
+ "process dependency"
+ "process suspended"
+ "recovery attempted"
+ "recovery not attempted (error)"
+ "recovery not attempted (low confidence)"
+ "recovery not attempted (no issues found)"
+ "recovery not attempted (process has higher jetsam priority)"
+ "recovery not attempted (process is another service)"
+ "recovery not attempted (process is being debugged)"
+ "recovery not attempted (process is not terminable)"
+ "recovery not attempted (process is suspended)"
+ "recovery not attempted (process is third party)"
+ "recovery not attempted (process is unblock server)"
+ "recovery not attempted (process stuck internally)"
+ "recovery not attempted (termination failed)"
+ "recovery not attempted (unknown(%ld))"
+ "recovery not attempted (unknown)"
+ "setClientName:"
+ "suppressTelemetry"
+ "thread dependency"
+ "time correlation"
- "Deadlock:            %@ -> %@\n"
- "Dependency chain:    %@\n"
- "Issue type:          %@\n"
- "Monitored service:   "
- "Monitoring process:  %@\n"
- "Number of other issues: %ld\n"
- "Processes blocked by this issue: %@\n"
- "Recovery confidence: %@\n"
- "Recovery status:     %@\n"
- "Threads stuck:         %lu threads stuck"
- "Time since issue began: %@s"
- "Unblock selected process (not terminated): %@ [%d]\n"
- "Unblock terminated process: %@ [%d]\n"
- "definitive"
- "error"
- "indirect correlation"
- "process stuck internally"
- "recovered"
- "unrecovered"

```
