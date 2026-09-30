## EasyConfig

> `/System/Library/PrivateFrameworks/EasyConfig.framework/Versions/A/EasyConfig`

```diff

-760.36.2.0.0
-  __TEXT.__text: 0x50d8
+770.26.0.0.0
+  __TEXT.__text: 0x50e0
   __TEXT.__auth_stubs: 0x660
-  __TEXT.__objc_methlist: 0x320
+  __TEXT.__objc_methlist: 0x334
   __TEXT.__const: 0x10
-  __TEXT.__cstring: 0x1027
-  __TEXT.__unwind_info: 0x168
+  __TEXT.__cstring: 0x1028
+  __TEXT.__unwind_info: 0x170
   __TEXT.__objc_classname: 0x27
   __TEXT.__objc_methname: 0xa32
-  __TEXT.__objc_methtype: 0x5c9
+  __TEXT.__objc_methtype: 0x5cb
   __TEXT.__objc_stubs: 0x5c0
   __DATA_CONST.__got: 0x88
   __DATA_CONST.__const: 0xd0

   __AUTH_CONST.__auth_got: 0x338
   __AUTH_CONST.__const: 0x150
   __AUTH_CONST.__cfstring: 0x4a0
-  __AUTH_CONST.__objc_const: 0x890
+  __AUTH_CONST.__objc_const: 0x870
   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0xe0
   __DATA.__data: 0xd0

   - /System/Library/PrivateFrameworks/CoreUtils.framework/Versions/A/CoreUtils
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B9716067-9B7A-3CB8-A7F6-A781D2814F27
+  UUID: EEB40954-434A-319A-AE5B-1B3C7F347B1E
   Functions: 99
   Symbols:   370
   CStrings:  369
Symbols:
+ ___block_descriptor_40_e8_32s_e197_v16?0^{HTTPMessagePrivate={__CFRuntimeBase=QAQ}^{HTTPMessagePrivate}{?=[8192c]Q*Q*Qi*Q{?=*Q*Q*Q*Q*Q*Q*Q***Q*Q}*Qi*QCQCi}CiC*QQQ[1000C]*^{?}*Q[2{iovec=^vQ}]^{iovec}iQiii^v^v^v^v^v^v^?^??iCq*iQI*}8l
- ___block_descriptor_40_e8_32s_e196_v16?0^{HTTPMessagePrivate={__CFRuntimeBase=QAQ}^{HTTPMessagePrivate}{?=[8192c]Q*Q*Qi*Q{?=*Q*Q*Q*Q*Q*Q*Q***Q*Q}*Qi*QCQCi}CiC*QQQ[1000C]*^{?}*Q[2{iovec=^vQ}]^{iovec}iQiii^v^v^v^v^v^v^?^??iCq*iQI}8l
Functions:
~ -[EasyConfigDevice _timeoutTimerStart:block:] : 248 -> 244
~ -[EasyConfigDevice _startBonjourWithTimeout:handler:] : 800 -> 772
~ -[EasyConfigDevice _logEnded] : 280 -> 276
~ -[EasyConfigDevice _postConfigCheckStart:] : 604 -> 596
~ -[EasyConfigDevice _findDevicePostConfigEvent:info:] : 772 -> 776
~ -[EasyConfigDevice _pairVerifyNext:] : 824 -> 808
~ -[EasyConfigDevice _pairVerifyStart] : 564 -> 572
~ -[EasyConfigDevice _pairSetupNext:] : 696 -> 684
~ -[EasyConfigDevice _pairSetupStart] : 512 -> 524
~ -[EasyConfigDevice _findDevicePreConfigEvent:info:] : 316 -> 320
~ -[EasyConfigDevice _trySetupCode:] : 184 -> 180
~ ___36-[EasyConfigDevice resumePostConfig]_block_invoke : 248 -> 252
~ -[EasyConfigDevice _stop:] : 952 -> 964
~ -[EasyConfigDevice _start] : 964 -> 1000
~ +[EasyConfigDevice supportedScanRecord:] : 228 -> 220
~ _EasyConfigCreateDictionaryFromTLV : 876 -> 888
CStrings:
+ "i24@0:8^{HTTPMessagePrivate={__CFRuntimeBase=QAQ}^{HTTPMessagePrivate}{?=[8192c]Q*Q*Qi*Q{?=*Q*Q*Q*Q*Q*Q*Q***Q*Q}*Qi*QCQCi}CiC*QQQ[1000C]*^{?}*Q[2{iovec=^vQ}]^{iovec}iQiii^v^v^v^v^v^v^?^?@?iCq*iQI*}16"
+ "v16@?0^{HTTPMessagePrivate={__CFRuntimeBase=QAQ}^{HTTPMessagePrivate}{?=[8192c]Q*Q*Qi*Q{?=*Q*Q*Q*Q*Q*Q*Q***Q*Q}*Qi*QCQCi}CiC*QQQ[1000C]*^{?}*Q[2{iovec=^vQ}]^{iovec}iQiii^v^v^v^v^v^v^?^?@?iCq*iQI*}8"
+ "v24@0:8^{HTTPMessagePrivate={__CFRuntimeBase=QAQ}^{HTTPMessagePrivate}{?=[8192c]Q*Q*Qi*Q{?=*Q*Q*Q*Q*Q*Q*Q***Q*Q}*Qi*QCQCi}CiC*QQQ[1000C]*^{?}*Q[2{iovec=^vQ}]^{iovec}iQiii^v^v^v^v^v^v^?^?@?iCq*iQI*}16"
- "i24@0:8^{HTTPMessagePrivate={__CFRuntimeBase=QAQ}^{HTTPMessagePrivate}{?=[8192c]Q*Q*Qi*Q{?=*Q*Q*Q*Q*Q*Q*Q***Q*Q}*Qi*QCQCi}CiC*QQQ[1000C]*^{?}*Q[2{iovec=^vQ}]^{iovec}iQiii^v^v^v^v^v^v^?^?@?iCq*iQI}16"
- "v16@?0^{HTTPMessagePrivate={__CFRuntimeBase=QAQ}^{HTTPMessagePrivate}{?=[8192c]Q*Q*Qi*Q{?=*Q*Q*Q*Q*Q*Q*Q***Q*Q}*Qi*QCQCi}CiC*QQQ[1000C]*^{?}*Q[2{iovec=^vQ}]^{iovec}iQiii^v^v^v^v^v^v^?^?@?iCq*iQI}8"
- "v24@0:8^{HTTPMessagePrivate={__CFRuntimeBase=QAQ}^{HTTPMessagePrivate}{?=[8192c]Q*Q*Qi*Q{?=*Q*Q*Q*Q*Q*Q*Q***Q*Q}*Qi*QCQCi}CiC*QQQ[1000C]*^{?}*Q[2{iovec=^vQ}]^{iovec}iQiii^v^v^v^v^v^v^?^?@?iCq*iQI}16"

```
