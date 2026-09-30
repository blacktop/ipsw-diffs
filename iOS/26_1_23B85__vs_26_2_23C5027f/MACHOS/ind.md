## ind

> `/System/Library/PrivateFrameworks/iCloudNotification.framework/ind`

```diff

-301.23.1.7.0
-  __TEXT.__text: 0x375c4
-  __TEXT.__auth_stubs: 0x1350
-  __TEXT.__objc_stubs: 0x4240
-  __TEXT.__objc_methlist: 0x1b54
-  __TEXT.__cstring: 0x217f
-  __TEXT.__objc_methname: 0x4cae
-  __TEXT.__oslogstring: 0x4b12
-  __TEXT.__objc_classname: 0x4df
-  __TEXT.__objc_methtype: 0x10c2
-  __TEXT.__const: 0xc50
+301.23.1.8.0
+  __TEXT.__text: 0x385c4
+  __TEXT.__auth_stubs: 0x1360
+  __TEXT.__objc_stubs: 0x43a0
+  __TEXT.__objc_methlist: 0x1c1c
+  __TEXT.__cstring: 0x237f
+  __TEXT.__objc_methname: 0x4e9d
+  __TEXT.__oslogstring: 0x4c62
+  __TEXT.__objc_classname: 0x50a
+  __TEXT.__objc_methtype: 0x10f2
+  __TEXT.__const: 0xc60
   __TEXT.__gcc_except_tab: 0x4e4
   __TEXT.__dlopen_cstrs: 0x56
   __TEXT.__swift5_typeref: 0x50c
   __TEXT.__swift5_fieldmd: 0x254
   __TEXT.__constg_swiftt: 0x494
-  __TEXT.__swift5_reflstr: 0x16a
+  __TEXT.__swift5_reflstr: 0x164
   __TEXT.__swift5_capture: 0x228
   __TEXT.__swift5_protos: 0x8
   __TEXT.__swift5_proto: 0x78

   __TEXT.__swift_as_ret: 0x68
   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_builtin: 0x28
-  __TEXT.__unwind_info: 0xf68
+  __TEXT.__unwind_info: 0xf90
   __TEXT.__eh_frame: 0xef0
-  __DATA_CONST.__auth_got: 0x9b8
+  __DATA_CONST.__auth_got: 0x9c0
   __DATA_CONST.__got: 0x5b0
   __DATA_CONST.__auth_ptr: 0x1b0
   __DATA_CONST.__const: 0x17e0
-  __DATA_CONST.__cfstring: 0x1fe0
-  __DATA_CONST.__objc_classlist: 0x188
+  __DATA_CONST.__cfstring: 0x2200
+  __DATA_CONST.__objc_classlist: 0x198
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_superrefs: 0x128
   __DATA_CONST.__linkguard: 0xe
   __DATA_CONST.__objc_intobj: 0x78
-  __DATA.__objc_const: 0x4618
-  __DATA.__objc_selrefs: 0x14c0
-  __DATA.__objc_ivar: 0x194
-  __DATA.__objc_data: 0x1378
+  __DATA.__objc_const: 0x4838
+  __DATA.__objc_selrefs: 0x1530
+  __DATA.__objc_ivar: 0x1a8
+  __DATA.__objc_data: 0x1418
   __DATA.__data: 0x630
   __DATA.__bss: 0xef0
   __DATA.__common: 0x60

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 9051CB01-0D26-3D0B-AA3C-25AEAF109326
-  Functions: 1258
-  Symbols:   578
-  CStrings:  2012
+  UUID: B646F6FB-E46F-304D-A40F-A4BE09E7BB8D
+  Functions: 1292
+  Symbols:   581
+  CStrings:  2077
 
Symbols:
+ _NSStringFromSelector
+ _OBJC_CLASS_$_NSProxy
+ _OBJC_METACLASS_$_NSProxy
CStrings:
+ "%s.activity"
+ "-[INDaemon _performHeartbeatRegistration]_block_invoke_2"
+ "@\"INTransactionManager\""
+ "@\"NSSet\""
+ "@32@0:8@16@?24"
+ "INTransactionManager"
+ "INTransactionManager: Completed work for transaction '%@'"
+ "INTransactionManager: Invalid parameters - transactionName=%@ block=%p"
+ "INTransactionManager: Releasing transaction '%@'"
+ "INTransactionManager: Starting transaction '%@'"
+ "INTransactionManager: Starting transaction '%@' with return value"
+ "INXPCTransactionProxy"
+ "T@\"INTransactionManager\",&,N,V_transactionManager"
+ "T@\"INTransactionManager\",R,N,V_transactionManager"
+ "T@\"NSSet\",R,N,V_skipTransactionMethods"
+ "T@,R,N,V_target"
+ "UTF8String"
+ "XPC notifyd matching event stream handler called."
+ "_skipTransactionMethods"
+ "_transactionManager"
+ "com.apple.ind.configureXPCEventStreamHandler.notifyd"
+ "com.apple.ind.configureXPCEventStreamHandler.vfs"
+ "com.apple.ind.didReceiveIncomingMessage"
+ "com.apple.ind.didReceivePublicToken"
+ "com.apple.ind.handleDeviceDidSetupNotification"
+ "com.apple.ind.performHeartbeatRegistration"
+ "com.apple.ind.registrationDigestCacheDidBecomeAvailable"
+ "com.apple.ind.start"
+ "connectionDidInvalidate"
+ "connectionWasInvalidated"
+ "defaultSkipMethods"
+ "executeWithTransaction:block:"
+ "executeWithTransactionReturning:block:"
+ "forwardInvocation:"
+ "initWithTarget:"
+ "initWithTarget:skipMethods:transactionManager:"
+ "invokeWithTarget:"
+ "selector"
+ "setTransactionManager:"
+ "setWithObjects:"
+ "skipTransactionMethods"
+ "target"
+ "transactionManager"
- "-[INDaemon _performHeartbeatRegistration]"

```
