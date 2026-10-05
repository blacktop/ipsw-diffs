## libIPTelephony.dylib

> `/System/Library/PrivateFrameworks/IPTelephony.framework/Support/libIPTelephony.dylib`

```diff

-2772.1.0.0.0
-  __TEXT.__text: 0x49dd64
+2774.0.0.0.0
+  __TEXT.__text: 0x49df0c
   __TEXT.__init_offsets: 0x1a8
   __TEXT.__objc_methlist: 0x74c
   __TEXT.__const: 0x1f9ec
-  __TEXT.__gcc_except_tab: 0x41f0c
+  __TEXT.__gcc_except_tab: 0x41f10
   __TEXT.__cstring: 0x14117
-  __TEXT.__oslogstring: 0x4cbd8
+  __TEXT.__oslogstring: 0x4ccb8
   __TEXT.__unwind_info: 0x19910
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   - /usr/lib/libxml2.2.dylib
   Functions: 16440
   Symbols:   24908
-  CStrings:  8703
+  CStrings:  8706
 
Functions:
~ __ZN9SDPParser24parseTTYFormatParametersER18SDPMediaFormatInfotNSt3__112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEE : 772 -> 888
~ __ZN12SipUserAgent20initializeAuthClientEb : 1436 -> 1432
~ __ZN21SipRegistrationClient14handleResponseENSt3__110shared_ptrIK11SipResponseEENS1_I20SipClientTransactionEE : 5428 -> 5572
~ __ZN18IPTelephonyManager18_initializeFromSIMERKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEERKN3ims11StackConfigE : 3660 -> 3852
~ __ZN18IPTelephonyManager17initializeFromSIMERKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEES8_RKN3ims11StackConfigENS0_10shared_ptrI8ImsPrefsEES8_ : 2228 -> 2204
CStrings:
+ "#E %{private, mask.hash}sSip stack not found %{public}s"
+ "#W %{private, mask.hash}sI need IPSec, but Reg 200 OK arrived over default transport, and I am roaming: accepted."
+ "#W %{private, mask.hash}sI need IPSec, but Reg 200 OK arrived over default transport: ignored! Will retry Registration."
+ "#W TTY with unexpected format parameters parsed: '%s'"
- "#W %{private, mask.hash}sI need IPSec, but Reg 200 OK arrived over default transport: ignored. Will retry Registration."
```
