## WiFiPolicy

> `/System/Library/PrivateFrameworks/WiFiPolicy.framework/Versions/A/WiFiPolicy`

```diff

-925.30.0.0.0
-  __TEXT.__text: 0xc392c
+925.31.0.0.0
+  __TEXT.__text: 0xc3c3c
   __TEXT.__auth_stubs: 0x12d0
-  __TEXT.__objc_methlist: 0x110a8
+  __TEXT.__objc_methlist: 0x110d0
   __TEXT.__const: 0x628
-  __TEXT.__cstring: 0x1b514
+  __TEXT.__cstring: 0x1b4f7
   __TEXT.__oslogstring: 0x3559
   __TEXT.__gcc_except_tab: 0x17a0
-  __TEXT.__unwind_info: 0x20d0
-  __TEXT.__objc_classname: 0x1378
-  __TEXT.__objc_methname: 0x3155f
+  __TEXT.__unwind_info: 0x20d8
+  __TEXT.__objc_classname: 0x1379
+  __TEXT.__objc_methname: 0x315e5
   __TEXT.__objc_methtype: 0x39f7
-  __TEXT.__objc_stubs: 0x179e0
+  __TEXT.__objc_stubs: 0x17a20
   __DATA_CONST.__got: 0x9e0
   __DATA_CONST.__const: 0xb98
   __DATA_CONST.__objc_classlist: 0x510
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x100
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x95d8
+  __DATA_CONST.__objc_selrefs: 0x95f0
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x430
   __DATA_CONST.__objc_arraydata: 0xa58

   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__const: 0x1ba0
   __AUTH_CONST.__cfstring: 0x18460
-  __AUTH_CONST.__objc_const: 0x20a88
+  __AUTH_CONST.__objc_const: 0x20ac0
   __AUTH_CONST.__objc_intobj: 0x1740
   __AUTH_CONST.__objc_arrayobj: 0x390
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH.__objc_data: 0x3200
-  __DATA.__objc_ivar: 0x208c
+  __DATA.__objc_ivar: 0x2090
   __DATA.__data: 0x1bc0
   __DATA.__bss: 0x263
   __DATA.__common: 0x20

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 6017
-  Symbols:   13524
-  CStrings:  13061
+  Functions: 6020
+  Symbols:   13531
+  CStrings:  13066
 
Symbols:
+ -[WiFiSoftError submitABCReportWithReason:event:]
+ -[WiFiUsageLinkSession joinFailSoftError]
+ -[WiFiUsageLinkSession setJoinFailSoftError:]
+ GCC_except_table48
+ OBJC_IVAR_$_WiFiUsageLinkSession._joinFailSoftError
+ __49-[WiFiSoftError submitABCReportWithReason:event:]_block_invoke.94
+ __49-[WiFiSoftError submitABCReportWithReason:event:]_block_invoke.cold.1
+ __49-[WiFiSoftError submitABCReportWithReason:event:]_block_invoke.cold.2
+ __OBJC_$_PROP_LIST_WiFiUsageLinkSession
+ ___49-[WiFiSoftError submitABCReportWithReason:event:]_block_invoke
+ _objc_msgSend$consecutiveJoinFailureCount
+ _objc_msgSend$submitABCReportWithReason:event:
- __43-[WiFiSoftError submitABCReportWithReason:]_block_invoke.94
- __43-[WiFiSoftError submitABCReportWithReason:]_block_invoke.cold.1
- __43-[WiFiSoftError submitABCReportWithReason:]_block_invoke.cold.2
- ___43-[WiFiSoftError submitABCReportWithReason:]_block_invoke
CStrings:
+ "\x12\x12B!\x11!"
+ "-[WiFiSoftError submitABCReportWithReason:event:]_block_invoke"
+ "/AppleInternal/Library/BuildRoots/fa4539c7-059d-11f0-b0c1-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/WiFiPolicy/frameworks/Sources/TrafficEngineering/WFTrafficEngManager.m"
+ "T@\"WiFiSoftError\",&,N,V_joinFailSoftError"
+ "_joinFailSoftError"
+ "joinFailSoftError"
+ "setJoinFailSoftError:"
+ "submitABCReportWithReason:event:"
+ "\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0!\x93\x114\x11\x8f\x0f\x03\xf0\xf0\xf0\x91s\xf0\xf0\xf0\x91\xa2t\xb2S'\x11\x11\x91\xf0\xa1\x11\xf0\xb4"
- "\x12\x12B!\x11"
- "%s Rejected due to [WiFiUsagePrivacyFilter isInternalInstall]\n"
- "-[WiFiSoftError submitABCReportWithReason:]_block_invoke"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/WiFiPolicy/frameworks/Sources/TrafficEngineering/WFTrafficEngManager.m"
- "\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0!\x93\x11$\x11\x8f\x0f\x03\xf0\xf0\xf0\x91s\xf0\xf0\xf0\x91\xb2t\xb2S'\x11\x11\x91\xf0\xa1\x11\xf0\xb4"

```
