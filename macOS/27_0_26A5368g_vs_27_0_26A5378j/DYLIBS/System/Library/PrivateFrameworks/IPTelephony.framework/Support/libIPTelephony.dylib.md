## libIPTelephony.dylib

> `/System/Library/PrivateFrameworks/IPTelephony.framework/Support/libIPTelephony.dylib`

```diff

-  __TEXT.__text: 0x438fc4
+  __TEXT.__text: 0x43945c
   __TEXT.__init_offsets: 0x188
   __TEXT.__objc_methlist: 0xf9c
   __TEXT.__const: 0x1c070
-  __TEXT.__gcc_except_tab: 0x3b74c
-  __TEXT.__cstring: 0x1297a
-  __TEXT.__oslogstring: 0x451f1
-  __TEXT.__unwind_info: 0x15b68
+  __TEXT.__gcc_except_tab: 0x3b78c
+  __TEXT.__cstring: 0x129d9
+  __TEXT.__oslogstring: 0x454a8
+  __TEXT.__unwind_info: 0x15b50
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2288
+  __DATA_CONST.__const: 0x2278
   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x18
   __DATA_CONST.__objc_selrefs: 0xa38
   __DATA_CONST.__objc_superrefs: 0x70
-  __DATA_CONST.__got: 0x0
+  __DATA_CONST.__got: 0x370
   __AUTH_CONST.__const: 0x2ff88
   __AUTH_CONST.__cfstring: 0x2d60
   __AUTH_CONST.__objc_const: 0x1e28

   __AUTH_CONST.__auth_got: 0xfd0
   __AUTH.__objc_data: 0x3c0
   __DATA.__objc_ivar: 0x164
-  __DATA.__data: 0x438
-  __DATA.__common: 0x138
-  __DATA.__bss: 0x2d0
+  __DATA.__data: 0x3a8
+  __DATA.__common: 0x130
+  __DATA.__bss: 0x1b8
   __DATA_DIRTY.__objc_data: 0xa0
-  __DATA_DIRTY.__data: 0x1b9
-  __DATA_DIRTY.__common: 0x848
-  __DATA_DIRTY.__bss: 0xaa0
+  __DATA_DIRTY.__data: 0x249
+  __DATA_DIRTY.__common: 0x850
+  __DATA_DIRTY.__bss: 0xbb4
   - /System/Library/Frameworks/CFNetwork.framework/Versions/A/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/Versions/A/CoreLocation

   - /usr/lib/libxml2.2.dylib
   Functions: 14669
   Symbols:   29272
-  CStrings:  8046
+  CStrings:  8059
 
Sections:
~ __TEXT.__init_offsets : content changed
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__weak_got : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__weak_auth_got : content changed
~ __AUTH.__objc_data : content changed
~ __DATA_DIRTY.__objc_data : content changed
Symbols:
+ GCC_except_table498
+ GCC_except_table500
+ GCC_except_table502
+ GCC_except_table511
+ GCC_except_table513
+ GCC_except_table525
+ GCC_except_table527
+ GCC_except_table530
+ GCC_except_table537
+ GCC_except_table539
+ GCC_except_table547
+ __ZN22SipRegistrationMetrics11kReasonNoneE
+ __ZNK8ImsPrefs52SkipReRegisterUponRatChangeWhenThereIsNoConnectivityEv
- GCC_except_table499
- GCC_except_table501
- GCC_except_table505
- GCC_except_table512
- GCC_except_table516
- GCC_except_table526
- GCC_except_table529
- GCC_except_table536
- GCC_except_table538
- GCC_except_table546
- __ZN12_GLOBAL__N_110ATM_REG_REE
- __ZN12_GLOBAL__N_119ATM_CALL_End_NormalE
- __ZN3xpceqIPKcEEbRKNS_4dict12object_proxyERKT_
CStrings:
+ "%{private, mask.hash}sSipTcpConnection::processDataFromSocket hasPartial=%{public,bool}d crlfInFlight=%{public,bool}d len=%{public}zu"
+ "%{private, mask.hash}sWill skip reregister due to no connectivity"
+ "%{private, mask.hash}srequesting abc snapshot for CT not recognizing chatbot with subdomain"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.nduWXU/Sources/ipTelephony/Source/Daemon/Core/AWD/cpp/CATM.pb.cc"
+ "CT failed to recognize chatbot"
+ "RCSChatbot"
+ "SkipReRegisterUponRatChangeWhenThereIsNoConnectivity"
+ "[DEBUG]  %{private, mask.hash}sDon't have a complete message yet datalen=%{public}zu bufSize=%{public}zu"
+ "[DEBUG]  %{private, mask.hash}sSuccess SIP %{public}s headerCount=%{public}zu bodyLength=%{public}zu"
+ "[ERROR]  %{private, mask.hash}sDropping SIP %{public}s"
+ "[ERROR]  %{private, mask.hash}sno sipstack %{public}s"
+ "[ERROR]  %{private, mask.hash}sno sipstack: dropping SIP %{public}s"
+ "[ERROR]  Dropping SIP %{public}s"
+ "[ERROR]  Invalid SDP: %{public}s"
+ "[WARN]   %{private, mask.hash}sSuccess but no sip message"
- "%{private, mask.hash}sSipTcpConnection::processDataFromSocket hasPartial=%{bool}d crlfInFlight=%{bool}d"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ZkI5vT/Sources/ipTelephony/Source/Daemon/Core/AWD/cpp/CATM.pb.cc"

```
