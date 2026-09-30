## libIPTelephony.dylib

> `/System/Library/PrivateFrameworks/IPTelephony.framework/Support/libIPTelephony.dylib`

```diff

-2764.0.0.0.0
-  __TEXT.__text: 0x4ab92c
-  __TEXT.__init_offsets: 0x1a4
+2765.0.0.0.0
+  __TEXT.__text: 0x4abc04
+  __TEXT.__init_offsets: 0x1a8
   __TEXT.__objc_methlist: 0x74c
   __TEXT.__const: 0x1f9fc
-  __TEXT.__gcc_except_tab: 0x41ec8
-  __TEXT.__cstring: 0x140b7
-  __TEXT.__oslogstring: 0x4cd37
+  __TEXT.__gcc_except_tab: 0x41f00
+  __TEXT.__cstring: 0x14117
+  __TEXT.__oslogstring: 0x4cdca
   __TEXT.__unwind_info: 0x181e0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __AUTH.__objc_data: 0x140
   __DATA.__objc_ivar: 0x4c
   __DATA.__data: 0x2c8
-  __DATA.__common: 0xa8
+  __DATA.__common: 0xc0
   __DATA.__bss: 0x14
   __DATA_DIRTY.__objc_data: 0xf0
   __DATA_DIRTY.__data: 0x2d0

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprotobuf-lite.dylib
   - /usr/lib/libxml2.2.dylib
-  Functions: 16438
-  Symbols:   25127
-  CStrings:  8702
+  Functions: 16439
+  Symbols:   25130
+  CStrings:  8704
 
Symbols:
+ __GLOBAL__sub_I_SipRegistrationMetrics.cpp
+ __ZN22SipRegistrationMetrics39kReasonIPSecCompletionEnforcementFailedE
+ __ZN9ImsResultlsIA68_cEERS_RKT_
Functions:
~ __ZN13LazuliSession19handleInviteFailureEjRKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEERK6SipUrijN3xpc5arrayE : 7860 -> 7972
~ __ZN21SipRegistrationClient14handleResponseENSt3__110shared_ptrIK11SipResponseEENS1_I20SipClientTransactionEE : 4912 -> 5428
+ __GLOBAL__sub_I_SipRegistrationMetrics.cpp
~ __ZN9SipDialog19cancelInviteRequestENSt3__110shared_ptrI20SipClientTransactionEEPK24ImsCallTerminationReason : 1232 -> 1204
CStrings:
+ "#W %{private, mask.hash}sI need IPSec, but Reg 200 OK arrived over default transport: ignored. Will retry Registration."
+ "%{private, mask.hash}sreceived Reg 200 OK. EnableIPSec: %{bool}d, Enforce IPSec: %{bool}d, DefaultTransportGroup: %p, RecvTransportGroup: %p, isEmergency: %{bool}d"
+ "IPSec completion enforcement: 200 OK on insecure transport rejected"
+ "IPSecCompletionEnforcementFailed"
- "#W %{private, mask.hash}sI need IPSec, but Reg 200 OK arrived over default transport: ignored."
- "%{private, mask.hash}sreceived Reg 200 OK"
```
