## amsaccountsd

> `/System/Library/PrivateFrameworks/AppleMediaServices.framework/amsaccountsd`

```diff

-9.0.72.0.0
-  __TEXT.__text: 0x20af54
-  __TEXT.__auth_stubs: 0x3cb0
-  __TEXT.__objc_stubs: 0x97c0
-  __TEXT.__objc_methlist: 0x53ac
-  __TEXT.__const: 0x1b984
-  __TEXT.__objc_classname: 0xe6d
-  __TEXT.__objc_methname: 0xe8d4
-  __TEXT.__oslogstring: 0xd421
-  __TEXT.__objc_methtype: 0x41d8
-  __TEXT.__cstring: 0xaf47
+9.0.76.0.0
+  __TEXT.__text: 0x20c928
+  __TEXT.__auth_stubs: 0x3cf0
+  __TEXT.__objc_stubs: 0x97e0
+  __TEXT.__objc_methlist: 0x5424
+  __TEXT.__const: 0x1b9b4
+  __TEXT.__objc_classname: 0xe85
+  __TEXT.__objc_methname: 0xe8f3
+  __TEXT.__oslogstring: 0xd481
+  __TEXT.__objc_methtype: 0x4211
+  __TEXT.__cstring: 0xaf87
   __TEXT.__gcc_except_tab: 0xe30
   __TEXT.__dlopen_cstrs: 0x34d
-  __TEXT.__swift5_typeref: 0x6c08
-  __TEXT.__constg_swiftt: 0x5340
+  __TEXT.__swift5_typeref: 0x6cb8
+  __TEXT.__constg_swiftt: 0x5350
   __TEXT.__swift5_reflstr: 0x455d
-  __TEXT.__swift5_fieldmd: 0x6330
-  __TEXT.__swift5_capture: 0xa38
+  __TEXT.__swift5_fieldmd: 0x6340
+  __TEXT.__swift5_capture: 0xa48
   __TEXT.__swift5_builtin: 0x118
   __TEXT.__swift5_mpenum: 0x78
   __TEXT.__swift5_assocty: 0x8f8
-  __TEXT.__swift5_proto: 0x16ec
+  __TEXT.__swift5_proto: 0x16e8
   __TEXT.__swift5_types: 0x684
   __TEXT.__swift_as_entry: 0x200
   __TEXT.__swift_as_ret: 0x2a8
-  __TEXT.__swift5_protos: 0xac
+  __TEXT.__swift5_protos: 0xb0
   __TEXT.__swift5_types2: 0x8
-  __TEXT.__unwind_info: 0x85c8
+  __TEXT.__unwind_info: 0x85d8
   __TEXT.__eh_frame: 0xf59c
-  __DATA_CONST.__auth_got: 0x1e68
+  __DATA_CONST.__auth_got: 0x1e88
   __DATA_CONST.__got: 0x1210
   __DATA_CONST.__auth_ptr: 0xce0
-  __DATA_CONST.__const: 0x12208
+  __DATA_CONST.__const: 0x12228
   __DATA_CONST.__cfstring: 0x3fc0
   __DATA_CONST.__objc_classlist: 0x340
   __DATA_CONST.__objc_catlist: 0x90
-  __DATA_CONST.__objc_protolist: 0x268
+  __DATA_CONST.__objc_protolist: 0x288
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x68
+  __DATA_CONST.__objc_protorefs: 0x78
   __DATA_CONST.__objc_superrefs: 0x190
   __DATA_CONST.__objc_intobj: 0x90
   __DATA_CONST.__linkguard: 0x2c
-  __DATA.__objc_const: 0xad80
-  __DATA.__objc_selrefs: 0x37c8
-  __DATA.__objc_ivar: 0x338
-  __DATA.__objc_data: 0x2298
-  __DATA.__data: 0xa280
-  __DATA.__bss: 0x2d3f0
+  __DATA.__objc_const: 0xadf8
+  __DATA.__objc_selrefs: 0x37d8
+  __DATA.__objc_ivar: 0x33c
+  __DATA.__objc_data: 0x2330
+  __DATA.__data: 0xa350
+  __DATA.__bss: 0x2d400
   __DATA.__common: 0x190
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 1EEAB1C3-BB02-3D41-929B-E277221EB975
-  Functions: 13100
-  Symbols:   1860
-  CStrings:  5363
+  UUID: BC2FCBB0-AF1A-3F27-8F9E-1A2D23886184
+  Functions: 13089
+  Symbols:   1863
+  CStrings:  5375
 
Symbols:
+ _$sSa10FoundationE19_bridgeToObjectiveCSo7NSArrayCyF
+ _$sSo17OS_dispatch_queueC8DispatchE5async5group3qos5flags7executeySo0a1_b1_F0CSg_AC0D3QoSVAC0D13WorkItemFlagsVyyXBtF
+ _signal
+ _xpc_transaction_exit_clean
- _$s8Dispatch0A12TimeIntervalOMn
CStrings:
+ "%{public}@: Shutting down, new transactions will be discarded"
+ "%{public}@: [%{public}@] Not taking a transaction or doing work because we are shutting down (transactionID: %{public}@)"
+ "@\"NSXPCListener\""
+ "@24@0:8@\"NSCoder\"16"
+ "AMSLiveTransactionStore"
+ "NSCoding"
+ "NSSecureCoding"
+ "Not taking a transaction because we are shutting down (transaction "
+ "Shutting down, new transactions will be discarded"
+ "T@\"NSXPCListener\",&,N,V_listener"
+ "TB,R"
+ "_listener"
+ "encodeWithCoder:"
+ "isShuttingDown"
+ "setListener:"
+ "supportsSecureCoding"
+ "v24@0:8@\"NSCoder\"16"
- "%{public}@: Flush all keep alive transaction. remaining transactions = %{public}@"
- "_TtC12amsaccountsd20LiveTransactionStore"
- "flushAllKeepAliveTransactions"
- "holdTime"
- "resetReleaseKeepAliveTransactionTimeDelayValue"
- "v32@?0@\"NSString\"8@\"NSObject<OS_os_transaction>\"16^B24"

```
