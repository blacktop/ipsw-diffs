## TimeSync

> `/System/Library/PrivateFrameworks/TimeSync.framework/TimeSync`

```diff

-1400.57.0.0.0
-  __TEXT.__text: 0x57b3c
+1400.58.0.0.0
+  __TEXT.__text: 0x57e70
   __TEXT.__auth_stubs: 0x920
   __TEXT.__objc_methlist: 0x63a0
   __TEXT.__const: 0x298
-  __TEXT.__oslogstring: 0x3e8a
+  __TEXT.__oslogstring: 0x3ec9
   __TEXT.__cstring: 0x6fb7
   __TEXT.__gcc_except_tab: 0xd24
-  __TEXT.__unwind_info: 0x1790
+  __TEXT.__unwind_info: 0x1798
   __TEXT.__objc_classname: 0x9f6
   __TEXT.__objc_methname: 0xb671
   __TEXT.__objc_methtype: 0x1839
   __TEXT.__objc_stubs: 0x6ec0
   __DATA_CONST.__got: 0x390
-  __DATA_CONST.__const: 0xc88
+  __DATA_CONST.__const: 0xcc8
   __DATA_CONST.__objc_classlist: 0x330
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x60

   __AUTH_CONST.__objc_intobj: 0x30
   __DATA.__objc_ivar: 0x860
   __DATA.__data: 0x488
-  __DATA.__bss: 0xa0
+  __DATA.__bss: 0xb0
   __DATA_DIRTY.__objc_data: 0x1fe0
   __DATA_DIRTY.__bss: 0xf8
   __DATA_DIRTY.__common: 0x4

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 265B5AFD-8117-3024-8384-66848961EF23
-  Functions: 2566
-  Symbols:   7899
-  CStrings:  3860
+  UUID: 27CEFDC7-265E-3559-AC2C-808C049133C3
+  Functions: 2569
+  Symbols:   7909
+  CStrings:  3861
 
Symbols:
+ ___169-[TSXDaemonServiceClient callMethodForDaemonClient:clientMethodSelector:scalarInputs:scalarInputCount:structInput:structInputSize:scalarOutputs:scalarOutputCount:error:]_block_invoke.101
+ ___29-[_TSF_IODConnection dealloc]_block_invoke
+ ___29-[_TSF_IODConnection dealloc]_block_invoke.cold.1
+ ___30-[TSXDaemonServiceClient init]_block_invoke.92
+ ___44-[TSXDaemonServiceClient getMSGClock:error:]_block_invoke.123
+ ___46-[TSXDaemonServiceClient stopMSGExternalSync:]_block_invoke.122
+ ___47-[TSXDaemonServiceClient addMSGClockRef:error:]_block_invoke.126
+ ___47-[TSXDaemonServiceClient isMSGServiceAvailable]_block_invoke.114
+ ___47-[TSXDaemonServiceClient removeMSGClock:error:]_block_invoke.127
+ ___47-[TSXDaemonServiceClient startMSGExternalSync:]_block_invoke.118
+ ___50-[TSXDaemonServiceClient closeDaemonClient:error:]_block_invoke.98
+ ___53-[TSXDaemonServiceClientExported daemonClientRefresh]_block_invoke
+ ___55-[TSXDaemonServiceClient propertiesForRegistryEntryID:]_block_invoke.105
+ ___57-[TSXDaemonServiceClient propertyForRegistryEntryID:key:]_block_invoke.109
+ ___67-[TSXDaemonServiceClientExported msgServiceNotification:arguments:]_block_invoke
+ ___68-[TSXDaemonServiceClient addMSGClock:withNominalSyncDuration:error:]_block_invoke.125
+ ___79-[TSXDaemonServiceClient openDaemonClientWithRegistryEntryID:clientType:error:]_block_invoke.95
+ ___86-[TSXDaemonServiceClient restoreMSGClockSession:withNominalSyncDuration:refCnt:error:]_block_invoke.128
+ ___block_descriptor_178_e5_v8?0l
+ ___block_descriptor_36_e5_v8?0l
+ ___block_literal_global.108
+ ___block_literal_global.121
+ ___block_literal_global.173
+ __dispatchQueue
- -[_TSF_IODConnection initWithService:andType:].cold.1
- ___169-[TSXDaemonServiceClient callMethodForDaemonClient:clientMethodSelector:scalarInputs:scalarInputCount:structInput:structInputSize:scalarOutputs:scalarOutputCount:error:]_block_invoke.97
- ___30-[TSXDaemonServiceClient init]_block_invoke.88
- ___44-[TSXDaemonServiceClient getMSGClock:error:]_block_invoke.119
- ___46-[TSXDaemonServiceClient stopMSGExternalSync:]_block_invoke.118
- ___47-[TSXDaemonServiceClient addMSGClockRef:error:]_block_invoke.122
- ___47-[TSXDaemonServiceClient isMSGServiceAvailable]_block_invoke.110
- ___47-[TSXDaemonServiceClient removeMSGClock:error:]_block_invoke.123
- ___47-[TSXDaemonServiceClient startMSGExternalSync:]_block_invoke.114
- ___50-[TSXDaemonServiceClient closeDaemonClient:error:]_block_invoke.94
- ___55-[TSXDaemonServiceClient propertiesForRegistryEntryID:]_block_invoke.101
- ___57-[TSXDaemonServiceClient propertyForRegistryEntryID:key:]_block_invoke.105
- ___68-[TSXDaemonServiceClient addMSGClock:withNominalSyncDuration:error:]_block_invoke.121
- ___79-[TSXDaemonServiceClient openDaemonClientWithRegistryEntryID:clientType:error:]_block_invoke.91
- ___86-[TSXDaemonServiceClient restoreMSGClockSession:withNominalSyncDuration:refCnt:error:]_block_invoke.124
- ___block_literal_global.100
- ___block_literal_global.109
CStrings:
+ "Failed to deallocate IODConnection to daemon client, error: %@"

```
