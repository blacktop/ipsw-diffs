## libIPTelephony.dylib

> `/System/Library/PrivateFrameworks/IPTelephony.framework/Support/libIPTelephony.dylib`

```diff

-2658.1.0.0.0
-  __TEXT.__text: 0x50e208
+2658.2.0.0.0
+  __TEXT.__text: 0x50e528
   __TEXT.__auth_stubs: 0x2d80
-  __TEXT.__init_offsets: 0x158
+  __TEXT.__init_offsets: 0x15c
   __TEXT.__objc_methlist: 0x748
   __TEXT.__const: 0x2016b
-  __TEXT.__gcc_except_tab: 0x4ecec
-  __TEXT.__cstring: 0x37b7c
-  __TEXT.__oslogstring: 0xfbc6
-  __TEXT.__unwind_info: 0x18eb8
+  __TEXT.__gcc_except_tab: 0x4ecfc
+  __TEXT.__cstring: 0x37be1
+  __TEXT.__oslogstring: 0xfc59
+  __TEXT.__unwind_info: 0x18ec8
   __TEXT.__objc_classname: 0x12f
   __TEXT.__objc_methname: 0x1de8
   __TEXT.__objc_methtype: 0x1118

   __DATA.__objc_ivar: 0x64
   __DATA.__data: 0x398
   __DATA.__bss: 0x20
-  __DATA.__common: 0xe4
+  __DATA.__common: 0xfc
   __DATA_DIRTY.__objc_data: 0xf0
   __DATA_DIRTY.__data: 0x1d0
   __DATA_DIRTY.__common: 0xc30

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprotobuf-lite.dylib
   - /usr/lib/libxml2.2.dylib
-  Functions: 17054
-  Symbols:   25848
-  CStrings:  9686
+  Functions: 17056
+  Symbols:   25852
+  CStrings:  9688
 
Symbols:
+ __GLOBAL__sub_I_SipRegistrationMetrics.cpp
+ __ZN22SipRegistrationMetrics11kReasonNoneE
+ __ZN22SipRegistrationMetrics39kReasonIPSecCompletionEnforcementFailedE
+ __ZN9ImsResultlsIA68_cEERS_RKT_
Functions:
~ __ZN3ims9analytics23RegistrationResultEvent25createRegistrationSuccessENSt3__110shared_ptrI8SipStackEERK33SipRegistrationActiveNotification : 2344 -> 2444
~ __ZN3ims9analytics23RegistrationResultEvent23createRegistrationErrorENSt3__110shared_ptrI8SipStackEERK32SipRegistrationErrorNotification : 2908 -> 2836
~ __ZN21SipRegistrationClient14handleResponseENSt3__110shared_ptrIK11SipResponseEENS1_I20SipClientTransactionEE : 4920 -> 5488
+ __ZN9ImsResultlsIA68_cEERS_RKT_
+ __GLOBAL__sub_I_SipRegistrationMetrics.cpp
~ __ZN9SipDialog19cancelInviteRequestENSt3__110shared_ptrI20SipClientTransactionEEPK26BambiCallTerminationReason : 1196 -> 1112
CStrings:
+ "#W %{private, mask.hash}sI need IPSec, but Reg 200 OK arrived over default transport: ignored. Will retry Registration."
+ "%{private, mask.hash}sreceived Reg 200 OK. EnableIPSec: %{bool}d, Enforce IPSec: %{bool}d, DefaultTransportGroup: %p, RecvTransportGroup: %p, isEmergency: %{bool}d"
+ "IPSec completion enforcement: 200 OK on insecure transport rejected"
+ "IPSecCompletionEnforcementFailed"
- "#W %{private, mask.hash}sI need IPSec, but Reg 200 OK arrived over default transport: ignored."
- "%{private, mask.hash}sreceived Reg 200 OK"
```
