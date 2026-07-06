## libIPTelephony.dylib

> `/System/Library/PrivateFrameworks/IPTelephony.framework/Support/libIPTelephony.dylib`

```diff

-  __TEXT.__text: 0x4aabd0
+  __TEXT.__text: 0x4aafb0
   __TEXT.__init_offsets: 0x1a4
   __TEXT.__objc_methlist: 0x674
-  __TEXT.__const: 0x1f83c
-  __TEXT.__gcc_except_tab: 0x41e34
-  __TEXT.__cstring: 0x140b5
-  __TEXT.__oslogstring: 0x4caba
+  __TEXT.__const: 0x1f84c
+  __TEXT.__gcc_except_tab: 0x41e80
+  __TEXT.__cstring: 0x1410f
+  __TEXT.__oslogstring: 0x4cd41
   __TEXT.__unwind_info: 0x18168
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x3da8
+  __DATA_CONST.__const: 0x3d98
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8

   __AUTH_CONST.__auth_got: 0x16a0
   __AUTH.__objc_data: 0xf0
   __DATA.__objc_ivar: 0x48
-  __DATA.__data: 0x378
-  __DATA.__bss: 0x144
-  __DATA.__common: 0x108
+  __DATA.__data: 0x268
+  __DATA.__common: 0xa8
+  __DATA.__bss: 0x14
   __DATA_DIRTY.__objc_data: 0xf0
-  __DATA_DIRTY.__data: 0x1c0
-  __DATA_DIRTY.__common: 0x888
-  __DATA_DIRTY.__bss: 0xc78
+  __DATA_DIRTY.__data: 0x2d0
+  __DATA_DIRTY.__bss: 0xda8
+  __DATA_DIRTY.__common: 0x8e0
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation

   - /usr/lib/libxml2.2.dylib
   Functions: 16405
   Symbols:   49547
-  CStrings:  9004
+  CStrings:  9017
 
Sections:
~ __TEXT.__init_offsets : content changed
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__weak_got : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__weak_auth_got : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH.__objc_data : content changed
~ __DATA_DIRTY.__objc_data : content changed
Symbols:
+ GCC_except_table501
+ GCC_except_table503
+ GCC_except_table505
+ GCC_except_table511
+ GCC_except_table513
+ GCC_except_table515
+ GCC_except_table519
+ GCC_except_table522
+ GCC_except_table524
+ GCC_except_table531
+ GCC_except_table535
+ GCC_except_table537
+ GCC_except_table539
+ GCC_except_table543
+ GCC_except_table547
+ GCC_except_table553
+ GCC_except_table555
+ GCC_except_table565
+ GCC_except_table569
+ __ZN22SipRegistrationMetrics11kReasonNoneE
+ __ZNK8ImsPrefs52SkipReRegisterUponRatChangeWhenThereIsNoConnectivityEv
- GCC_except_table502
- GCC_except_table504
- GCC_except_table508
- GCC_except_table512
- GCC_except_table514
- GCC_except_table517
- GCC_except_table521
- GCC_except_table523
- GCC_except_table526
- GCC_except_table532
- GCC_except_table536
- GCC_except_table538
- GCC_except_table542
- GCC_except_table545
- GCC_except_table552
- GCC_except_table554
- GCC_except_table564
- GCC_except_table568
- __ZN12_GLOBAL__N_110ATM_REG_REE
- __ZN12_GLOBAL__N_119ATM_CALL_End_NormalE
- __ZN3xpceqIPKcEEbRKNS_4dict12object_proxyERKT_
CStrings:
+ "#D %{private, mask.hash}sDon't have a complete message yet datalen=%{public}zu bufSize=%{public}zu"
+ "#D %{private, mask.hash}sSuccess SIP %{public}s headerCount=%{public}zu bodyLength=%{public}zu"
+ "#E %{private, mask.hash}sDropping SIP %{public}s"
+ "#E %{private, mask.hash}sno sipstack %{public}s"
+ "#E %{private, mask.hash}sno sipstack: dropping SIP %{public}s"
+ "#E Dropping SIP %{public}s"
+ "#E Invalid SDP: %{public}s"
+ "#W %{private, mask.hash}sSuccess but no sip message"
+ "%{private, mask.hash}sSipTcpConnection::processDataFromSocket hasPartial=%{public,bool}d crlfInFlight=%{public,bool}d len=%{public}zu"
+ "%{private, mask.hash}sWill skip reregister due to no connectivity"
+ "%{private, mask.hash}srequesting abc snapshot for CT not recognizing chatbot with subdomain"
+ "CT failed to recognize chatbot"
+ "RCSChatbot"
+ "SkipReRegisterUponRatChangeWhenThereIsNoConnectivity"
- "%{private, mask.hash}sSipTcpConnection::processDataFromSocket hasPartial=%{bool}d crlfInFlight=%{bool}d"

```
