## transparencyd

> `/usr/libexec/transparencyd`

```diff

-1033.62.3.0.0
-  __TEXT.__text: 0x1b1de0
+1033.80.17.0.1
+  __TEXT.__text: 0x1b2f64
   __TEXT.__auth_stubs: 0x23d0
-  __TEXT.__objc_stubs: 0x19060
-  __TEXT.__objc_methlist: 0x11020
-  __TEXT.__cstring: 0x10856
-  __TEXT.__objc_classname: 0x29ee
-  __TEXT.__objc_methname: 0x1e7ba
-  __TEXT.__objc_methtype: 0x6731
+  __TEXT.__objc_stubs: 0x19260
+  __TEXT.__objc_methlist: 0x11128
+  __TEXT.__cstring: 0x1088d
+  __TEXT.__objc_classname: 0x2a05
+  __TEXT.__objc_methname: 0x1e9c6
+  __TEXT.__objc_methtype: 0x6772
   __TEXT.__const: 0x29f8
-  __TEXT.__gcc_except_tab: 0x348c
-  __TEXT.__oslogstring: 0xdb06
+  __TEXT.__gcc_except_tab: 0x34fc
+  __TEXT.__oslogstring: 0xdc85
   __TEXT.__dlopen_cstrs: 0x56
   __TEXT.__swift5_typeref: 0xbd6
   __TEXT.__swift5_capture: 0x718

   __TEXT.__swift5_proto: 0x140
   __TEXT.__swift5_types: 0xb8
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__unwind_info: 0x69d0
+  __TEXT.__unwind_info: 0x6a14
   __TEXT.__eh_frame: 0x104c
   __DATA_CONST.__auth_got: 0x11f8
-  __DATA_CONST.__got: 0x778
+  __DATA_CONST.__got: 0x780
   __DATA_CONST.__auth_ptr: 0x70
-  __DATA_CONST.__const: 0x12100
-  __DATA_CONST.__cfstring: 0xcf40
-  __DATA_CONST.__objc_classlist: 0xb38
+  __DATA_CONST.__const: 0x12290
+  __DATA_CONST.__cfstring: 0xcf80
+  __DATA_CONST.__objc_classlist: 0xb48
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x2c8
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0x188
   __DATA_CONST.__objc_dictobj: 0x140
   __DATA_CONST.__objc_arrayobj: 0x1b0
-  __DATA.__objc_const: 0x29b70
-  __DATA.__objc_selrefs: 0x7430
+  __DATA.__objc_const: 0x29df0
+  __DATA.__objc_selrefs: 0x74b0
   __DATA.__objc_protorefs: 0x58
-  __DATA.__objc_classrefs: 0xd48
-  __DATA.__objc_superrefs: 0x6a0
-  __DATA.__objc_ivar: 0xf24
-  __DATA.__objc_data: 0x79b8
+  __DATA.__objc_classrefs: 0xd58
+  __DATA.__objc_superrefs: 0x6b0
+  __DATA.__objc_ivar: 0xf3c
+  __DATA.__objc_data: 0x7a58
   __DATA.__data: 0x5980
   __DATA.__thread_vars: 0x48
   __DATA.__thread_bss: 0xc

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 9970
-  Symbols:   1054
-  CStrings:  10127
+  Functions: 10002
+  Symbols:   1055
+  CStrings:  10170
 
Symbols:
+ _kTransparencyTriggerOperationBAACertFetcher
CStrings:
+ "%{public}@: %@"
+ "@\"KTBAAKey\""
+ "@28@0:8@16i24"
+ "@40@0:8^{__SecKey=}16@24@32"
+ "Error fetching BAA cert from triggerBAACertFetcher: %@"
+ "Error fetching BAA cert, starting exponential backoff to request a new cert. %{public}@"
+ "KTBAAKey"
+ "KTIDSAccountHolder"
+ "KTIDSActualOperations-idsController"
+ "Known state state %lu for view: %@"
+ "Q24@0:8@\"NSString\"16"
+ "T@\"KTBAAKey\",&,V_baaKey"
+ "T@\"NSArray\",&,V_idsAccounts"
+ "T@\"NSObject<OS_dispatch_queue>\",&,V_idsControllerQueue"
+ "T@\"NSString\",&,V_idsDSID"
+ "T^{__SecKey=},V_referenceKey"
+ "Ti,V_accountType"
+ "_accountType"
+ "_baaKey"
+ "_idsAccounts"
+ "_idsControllerQueue"
+ "_idsDSID"
+ "_referenceKey"
+ "accountController:accountDisabled: %@"
+ "baaKey"
+ "ckksGetKnownBadState:"
+ "deleting download record %{public}@"
+ "deleting downloadId %{public}@"
+ "failed to find downloadId %{public}@: %@"
+ "failing STH downloadId %{public}@"
+ "idsAccounts"
+ "idsControllerQueue"
+ "idsDSID"
+ "initWithIDSAccount:"
+ "initWithIDSDSID:type:"
+ "initWithKey:certificates:failure:"
+ "missing"
+ "onQueueProcessStatus: pending status for appleID"
+ "publickey-missing"
+ "referenceKey"
+ "rpcKnownBadState:reply:"
+ "setAccountType:"
+ "setBaaKey:"
+ "setIdsAccounts:"
+ "setIdsControllerQueue:"
+ "setIdsDSID:"
+ "setReferenceKey:"
+ "triggerBAACertFetcher"
+ "v16@?0@\"KTBAAKey\"8"
+ "v16@?0Q8"
+ "v28@0:8B16@?<v@?@\"KTBAAKey\">20"
+ "validBAAKey"
- "\t"
- "\x11\x12"
- "T^{__SecKey=},V_bik"
- "_bik"
- "accountController:accountDisableda: %@"
- "bik"
- "setBik:"
- "v28@0:8B16@?<v@?@@\"NSArray\"@\"NSError\">20"
- "v32@?0@8@\"NSArray\"16@\"NSError\"24"

```
