## SystemStatusServer

> `/System/Library/PrivateFrameworks/SystemStatusServer.framework/SystemStatusServer`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_protolist`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-282.0.0.0.0
-  __TEXT.__text: 0x1fac4
-  __TEXT.__objc_methlist: 0x1d90
-  __TEXT.__const: 0xd0
+284.1.0.0.0
+  __TEXT.__text: 0x20774
+  __TEXT.__objc_methlist: 0x1e98
+  __TEXT.__const: 0xd8
   __TEXT.__dlopen_cstrs: 0x52
-  __TEXT.__cstring: 0x1c7a
-  __TEXT.__gcc_except_tab: 0x328
-  __TEXT.__oslogstring: 0xaee
-  __TEXT.__unwind_info: 0x870
+  __TEXT.__cstring: 0x1d3b
+  __TEXT.__gcc_except_tab: 0x33c
+  __TEXT.__oslogstring: 0xe55
+  __TEXT.__unwind_info: 0x8a0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xdd8
-  __DATA_CONST.__objc_classlist: 0x128
+  __DATA_CONST.__const: 0xe28
+  __DATA_CONST.__objc_classlist: 0x130
   __DATA_CONST.__objc_protolist: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1358
-  __DATA_CONST.__objc_superrefs: 0x108
-  __DATA_CONST.__got: 0x410
-  __AUTH_CONST.__const: 0x2a0
-  __AUTH_CONST.__cfstring: 0x1760
-  __AUTH_CONST.__objc_const: 0x4260
+  __DATA_CONST.__objc_selrefs: 0x1418
+  __DATA_CONST.__objc_superrefs: 0x110
+  __DATA_CONST.__got: 0x438
+  __AUTH_CONST.__const: 0x2c0
+  __AUTH_CONST.__cfstring: 0x17e0
+  __AUTH_CONST.__objc_const: 0x44f8
   __AUTH_CONST.__auth_got: 0x0
-  __DATA.__objc_ivar: 0x2a4
+  __AUTH.__objc_data: 0x50
+  __DATA.__objc_ivar: 0x2c8
   __DATA.__data: 0xba0
   __DATA_DIRTY.__objc_ivar: 0x8
   __DATA_DIRTY.__objc_data: 0xb90
-  __DATA_DIRTY.__bss: 0x60
+  __DATA_DIRTY.__bss: 0x70
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/CoreTelephony.framework/CoreTelephony

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 740
-  Symbols:   2165
-  CStrings:  286
+  Functions: 766
+  Symbols:   2230
+  CStrings:  303
 
Symbols:
+ +[STStatusDomainPublisherXPCClientHandle _serverCompletionForXPCReplyBlock:]
+ -[STStatusDomainXPCClientWakeUpAssertion .cxx_destruct]
+ -[STStatusDomainXPCClientWakeUpAssertion _acquireNewHandleMessageAssertion]
+ -[STStatusDomainXPCClientWakeUpAssertion _invalidateHandleMessageAssertion]
+ -[STStatusDomainXPCClientWakeUpAssertion acquire]
+ -[STStatusDomainXPCClientWakeUpAssertion assertionAcquisitionCount]
+ -[STStatusDomainXPCClientWakeUpAssertion clientIsRunningBoardManaged]
+ -[STStatusDomainXPCClientWakeUpAssertion clientPID]
+ -[STStatusDomainXPCClientWakeUpAssertion dealloc]
+ -[STStatusDomainXPCClientWakeUpAssertion handleMessageAssertionAcquisitionTimestamp]
+ -[STStatusDomainXPCClientWakeUpAssertion handleMessageAssertion]
+ -[STStatusDomainXPCClientWakeUpAssertion initWithClientAuditToken:queue:]
+ -[STStatusDomainXPCClientWakeUpAssertion invalidateHandleMessageAssertionTimer]
+ -[STStatusDomainXPCClientWakeUpAssertion invalidate]
+ -[STStatusDomainXPCClientWakeUpAssertion isInvalidated]
+ -[STStatusDomainXPCClientWakeUpAssertion queue]
+ -[STStatusDomainXPCClientWakeUpAssertion relinquish]
+ -[STStatusDomainXPCClientWakeUpAssertion setAssertionAcquisitionCount:]
+ -[STStatusDomainXPCClientWakeUpAssertion setHandleMessageAssertion:]
+ -[STStatusDomainXPCClientWakeUpAssertion setHandleMessageAssertionAcquisitionTimestamp:]
+ -[STStatusDomainXPCClientWakeUpAssertion setInvalidateHandleMessageAssertionTimer:]
+ -[STStatusDomainXPCClientWakeUpAssertion setInvalidated:]
+ GCC_except_table5
+ _BSFloatLessThanFloat
+ _OBJC_CLASS_$_NSXPCConnection
+ _OBJC_CLASS_$_RBSAssertion
+ _OBJC_CLASS_$_RBSDomainAttribute
+ _OBJC_CLASS_$_RBSTarget
+ _OBJC_CLASS_$_STStatusDomainXPCClientWakeUpAssertion
+ _OBJC_IVAR_$_STStatusDomainXPCClientHandle._clientWakeUpAssertion
+ _OBJC_IVAR_$_STStatusDomainXPCClientWakeUpAssertion._assertionAcquisitionCount
+ _OBJC_IVAR_$_STStatusDomainXPCClientWakeUpAssertion._clientIsRunningBoardManaged
+ _OBJC_IVAR_$_STStatusDomainXPCClientWakeUpAssertion._clientPID
+ _OBJC_IVAR_$_STStatusDomainXPCClientWakeUpAssertion._handleMessageAssertion
+ _OBJC_IVAR_$_STStatusDomainXPCClientWakeUpAssertion._handleMessageAssertionAcquisitionTimestamp
+ _OBJC_IVAR_$_STStatusDomainXPCClientWakeUpAssertion._invalidateHandleMessageAssertionTimer
+ _OBJC_IVAR_$_STStatusDomainXPCClientWakeUpAssertion._invalidated
+ _OBJC_IVAR_$_STStatusDomainXPCClientWakeUpAssertion._queue
+ _OBJC_METACLASS_$_STStatusDomainXPCClientWakeUpAssertion
+ _STSystemStatusLogClientWakeUp
+ __OBJC_$_INSTANCE_METHODS_STStatusDomainXPCClientWakeUpAssertion
+ __OBJC_$_INSTANCE_VARIABLES_STStatusDomainXPCClientWakeUpAssertion
+ __OBJC_$_PROP_LIST_STStatusDomainXPCClientWakeUpAssertion
+ __OBJC_CLASS_PROTOCOLS_$_STStatusDomainXPCClientWakeUpAssertion
+ __OBJC_CLASS_RO_$_STStatusDomainXPCClientWakeUpAssertion
+ __OBJC_METACLASS_RO_$_STStatusDomainXPCClientWakeUpAssertion
+ ___52-[STStatusDomainXPCClientWakeUpAssertion relinquish]_block_invoke
+ ___76+[STStatusDomainPublisherXPCClientHandle _serverCompletionForXPCReplyBlock:]_block_invoke
+ ___STSystemStatusLogClientWakeUp_block_invoke
+ ___block_descriptor_40_e8_32bs_e37_v16?0"NSObject<OS_dispatch_queue>"8ls32l8
+ ___block_descriptor_40_e8_32w_e31_v16?0"BSContinuousMachTimer"8lw32l8
+ ___block_descriptor_74_e8_32s40s48s56bs_e5_v8?0ls32l8s56l8s40l8s48l8
+ _objc_msgSend$_acquireNewHandleMessageAssertion
+ _objc_msgSend$_handoffCurrentReplyToQueue:block:
+ _objc_msgSend$_invalidateHandleMessageAssertion
+ _objc_msgSend$acquire
+ _objc_msgSend$acquireWithError:
+ _objc_msgSend$attributeWithDomain:name:
+ _objc_msgSend$clientPID
+ _objc_msgSend$initWithClientAuditToken:queue:
+ _objc_msgSend$initWithExplanation:target:attributes:
+ _objc_msgSend$isApplication
+ _objc_msgSend$relinquish
+ _objc_msgSend$setInvalidateHandleMessageAssertionTimer:
+ _objc_msgSend$targetWithPid:
+ _objc_opt_self
+ _objc_retainBlock
- ___block_descriptor_74_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s48l8s56l8
- _dispatch_block_create
CStrings:
+ "ClientWakeUp"
+ "Observer-HandleMessage"
+ "STStatusDomainXPCClientWakeUpAssertion:%d"
+ "SYSTEMSTATUSSERVER CLIENT ERROR: attempted to acquire wake up assertion that was invalidated"
+ "SYSTEMSTATUSSERVER CLIENT ERROR: attempted to relinquish wake up assertion that was invalidated"
+ "SYSTEMSTATUSSERVER CLIENT ERROR: invalidated wake up assertion that was already invalidated"
+ "SYSTEMSTATUSSERVER CLIENT ERROR: wake up assertion deallocated without being invalidated"
+ "SystemStatus sending update to observer client: %d"
+ "cancelling scheduled invalidation of Observer-HandleMessage assertion for client: %d"
+ "com.apple.systemstatusd"
+ "creating new Observer-HandleMessage assertion for client: %d"
+ "failed to acquire Observer-HandleMessage assertion for client: %d"
+ "invalidating Observer-HandleMessage assertion immediately for client: %d"
+ "performing scheduled invalidation of Observer-HandleMessage assertion for client: %d"
+ "reusing Observer-HandleMessage assertion for client: %d"
+ "scheduling invalidation of Observer-HandleMessage assertion for client: %d"
+ "v16@?0@\"NSObject<OS_dispatch_queue>\"8"
```
