## PrivateMLClient

> `/System/Library/PrivateFrameworks/PrivateMLClient.framework/PrivateMLClient`

```diff

-150.32.0.0.0
-  __TEXT.__text: 0x28cf1c
-  __TEXT.__auth_stubs: 0x2230
-  __TEXT.__const: 0x1c678
-  __TEXT.__swift5_typeref: 0x4558
-  __TEXT.__oslogstring: 0x4ead
-  __TEXT.__constg_swiftt: 0x4314
-  __TEXT.__cstring: 0x6384
+150.34.1.0.0
+  __TEXT.__text: 0x291c04
+  __TEXT.__auth_stubs: 0x2270
+  __TEXT.__const: 0x1c6f8
+  __TEXT.__swift5_typeref: 0x457c
+  __TEXT.__oslogstring: 0x51bd
+  __TEXT.__constg_swiftt: 0x43b4
+  __TEXT.__cstring: 0x6404
   __TEXT.__swift5_builtin: 0x104
-  __TEXT.__swift5_reflstr: 0x4545
-  __TEXT.__swift5_fieldmd: 0x5974
+  __TEXT.__swift5_reflstr: 0x4565
+  __TEXT.__swift5_fieldmd: 0x59b4
   __TEXT.__swift5_assocty: 0x680
-  __TEXT.__swift5_proto: 0x1848
-  __TEXT.__swift5_types: 0x594
+  __TEXT.__swift5_proto: 0x184c
+  __TEXT.__swift5_types: 0x598
   __TEXT.__swift5_mpenum: 0x88
-  __TEXT.__swift5_capture: 0x718
-  __TEXT.__swift_as_entry: 0xf4
+  __TEXT.__swift5_capture: 0x7b8
+  __TEXT.__swift_as_entry: 0xfc
   __TEXT.__swift_as_ret: 0x148
   __TEXT.__swift5_protos: 0x14
-  __TEXT.__unwind_info: 0x9d48
-  __TEXT.__eh_frame: 0xe5b8
-  __TEXT.__objc_classname: 0x670
-  __TEXT.__objc_methname: 0xd4e
+  __TEXT.__unwind_info: 0x9e38
+  __TEXT.__eh_frame: 0xe948
+  __TEXT.__objc_classname: 0x6a0
+  __TEXT.__objc_methname: 0xd9e
   __TEXT.__objc_methtype: 0x1
   __TEXT.__objc_stubs: 0x320
   __DATA_CONST.__got: 0x578
-  __DATA_CONST.__const: 0x28c0
-  __DATA_CONST.__objc_classlist: 0xa0
+  __DATA_CONST.__const: 0x28e0
+  __DATA_CONST.__objc_classlist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xc8
-  __AUTH_CONST.__auth_got: 0x1120
-  __AUTH_CONST.__const: 0x4b90
-  __AUTH_CONST.__objc_const: 0x18e0
-  __AUTH.__objc_data: 0x550
-  __AUTH.__data: 0x9cb8
-  __DATA.__data: 0x77f0
-  __DATA.__bss: 0x2f880
-  __DATA.__common: 0x18
+  __AUTH_CONST.__auth_got: 0x1140
+  __AUTH_CONST.__const: 0x4cd0
+  __AUTH_CONST.__objc_const: 0x19b0
+  __AUTH.__objc_data: 0x5a0
+  __AUTH.__data: 0x9dc8
+  __DATA.__data: 0x7880
+  __DATA.__bss: 0x2f900
+  __DATA.__common: 0x20
   __DATA_DIRTY.__objc_data: 0xf0
   __DATA_DIRTY.__data: 0x1068
   __DATA_DIRTY.__common: 0x8

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: E0ECE97E-589D-3CC4-BEC9-7DD9DEA4798B
-  Functions: 15474
-  Symbols:   2681
-  CStrings:  1457
+  UUID: 34A45432-2E69-3B39-892A-E0A5B6994001
+  Functions: 15557
+  Symbols:   2695
+  CStrings:  1477
 
Symbols:
+ __DATA__TtC15PrivateMLClient13StreamManager
+ __IVARS__TtC15PrivateMLClient13StreamManager
+ __METACLASS_DATA__TtC15PrivateMLClient13StreamManager
+ _objectdestroy.40Tm
+ _swift_weakDestroy
+ _swift_weakInit
+ _swift_weakLoadStrong
+ _symbolic SbIegd_
+ _symbolic ScSy_____G_____yAA_G_____Iegnng_Sg 10Foundation4DataV ScS12ContinuationV 15PrivateMLClient13StreamManagerC
+ _symbolic _____ 15PrivateMLClient13StreamManagerC
+ _symbolic _____Iegd_ s5Int32V
+ _symbolic _____Iegr_ s5Int32V
+ _symbolic ______pSg s5ErrorP
+ _symbolic _____ySiG 15PrivateMLClient11UserDefaultV
- _symbolic ScSy_____GScsyAA______pG_____yAA_G_____yAaC_p_GIegnnnn_Sg 10Foundation4DataV s5ErrorP ScS12ContinuationV ScsAFV
CStrings:
+ "%s: isOpportunistic Request:%{bool}d requestID:%s"
+ "%s:PMLCCM: timeout queue created and added."
+ "%s:PMLCCM: timeout queue exists and added. Count:%ld"
+ "%s:withPrivateMLRequest inferenceID:%s with requestID:%s"
+ "After Opening long-lived connection for session %s isRetry:%{bool}d"
+ "BasicTask defer complete or cancelled."
+ "Force recalculation = %{bool}d"
+ "Force recalculation overriden by userdefaults"
+ "Long-lived connection defer complete Block."
+ "Long-lived connection defer complete due to cancellation Block."
+ "PMLCCM: Timeout connection cancelled. %s"
+ "PMLCCM: release rbAssertion. %s"
+ "PMLCCM: start sleep. %s"
+ "PMLCCM: timed out connection was not used. %s"
+ "PMLCCM: wakeup. %s"
+ "PMLCSM: Don't timeout on client side. %s"
+ "PMLCSM: Timeout connection cancelled. %s"
+ "PMLCSM: release rbAssertion. %s"
+ "PMLCSM: start sleep. %s"
+ "PMLCSM: timed out connection was not used. %s"
+ "PMLCSM: timeout queue created and added. %s"
+ "PMLCSM: timeout task is empty! %s"
+ "PMLCSM: wakeup. %s"
+ "PersistentConnectionState NOT enabled %s"
+ "Started writing input stream to long-lived connection with isPersistentConnectionEnabled on connection %{bool}d with priority %s"
+ "StreamManager:Create StreamManager."
+ "StreamManager:Finish"
+ "StreamManager:Finish with error"
+ "StreamManager:reset"
+ "StreamManager:return data stream."
+ "Subrequest failed Restarting outputstream"
+ "_TtC15PrivateMLClient13StreamManager"
+ "continuation"
+ "gOpportunisticSimulateFailureThrown"
+ "gOpportunisticSimulateFailureThrown ignored"
+ "gOpportunisticSimulateFailureThrown now"
+ "gOpportunisticSimulateFailureThrownModValue"
+ "get hold temp Saved keys:%s with session:%s"
+ "getPersistentConnectionState NOT enabled %s"
+ "isOpportunistic"
+ "outputStreamManager"
+ "privatemlclient.StreamManager"
+ "stream"
- "After Opening long-lived connection for session %s with priority %s isRetry:%{bool}d"
- "Long-lived connection defer complete due to cancellation."
- "Long-lived connection defer complete."
- "PMLCCM: Timeout connection cancelled."
- "PMLCCM: release rbAssertion."
- "PMLCCM: start sleep."
- "PMLCCM: timed out connection was not used."
- "PMLCCM: timeout queue created and added."
- "PMLCCM: timeout queue exists and added. Count:%ld"
- "PMLCCM: wakeup."
- "PMLCSM: Don't timeout on client side."
- "PMLCSM: Timeout connection cancelled."
- "PMLCSM: release rbAssertion."
- "PMLCSM: start sleep."
- "PMLCSM: timed out connection was not used."
- "PMLCSM: timeout queue created and added."
- "PMLCSM: timeout task is empty!"
- "PMLCSM: wakeup."
- "PersistentConnectionState NOT enabled"
- "get hold temp Saved keys:%s"
- "getPersistentConnectionState NOT enabled"
- "outputContinuation"
- "outputStream"

```
