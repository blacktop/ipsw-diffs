## NetworkStatistics

> `/System/Library/PrivateFrameworks/NetworkStatistics.framework/NetworkStatistics`

```diff

-212.100.5.0.0
-  __TEXT.__text: 0x2c2a8
+212.120.2.0.0
+  __TEXT.__text: 0x2c184
   __TEXT.__auth_stubs: 0xa80
-  __TEXT.__objc_methlist: 0x3f0c
-  __TEXT.__cstring: 0x4157
+  __TEXT.__objc_methlist: 0x3f1c
+  __TEXT.__cstring: 0x4165
   __TEXT.__oslogstring: 0x2151
   __TEXT.__const: 0x11c
   __TEXT.__gcc_except_tab: 0x2ec
-  __TEXT.__unwind_info: 0x9d8
+  __TEXT.__unwind_info: 0xa8c
   __TEXT.__objc_classname: 0x4ef
-  __TEXT.__objc_methname: 0x74d8
+  __TEXT.__objc_methname: 0x755a
   __TEXT.__objc_methtype: 0x7b54
   __TEXT.__objc_stubs: 0x4a20
   __DATA_CONST.__got: 0x48
-  __DATA_CONST.__const: 0x820
+  __DATA_CONST.__const: 0x7e8
   __DATA_CONST.__objc_classlist: 0x188
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x6c18
-  __DATA_CONST.__objc_selrefs: 0x1868
+  __DATA_CONST.__objc_const: 0x6c38
+  __DATA_CONST.__objc_selrefs: 0x1878
   __DATA_CONST.__objc_classrefs: 0x1d8
   __DATA_CONST.__objc_superrefs: 0x120
   __DATA_CONST.__objc_arraydata: 0x238

   - /System/Library/Frameworks/Security.framework/Security
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 00DC0109-25BA-362C-9143-134F584EC660
-  Functions: 1482
-  Symbols:   4781
-  CStrings:  2938
+  UUID: 319C31E7-F117-3DCB-97DD-CC8E17F421FE
+  Functions: 1484
+  Symbols:   4785
+  CStrings:  2940
 
Symbols:
+ -[NWStatsSnapshot delegateAttributionReasonString]
+ -[NWStatsSnapshot delegateAttributionReason]
+ -[NWStatsSnapshot setAttribution:derivation:delegateName:delegateDerivation:extensionName:]
+ -[NWStatsSnapshot setDelegateAttributionReason:]
+ -[NWStatsSource delegateAttributionReason]
+ -[NWStatsSource setAttribution:derivation:delegateName:delegateDerivation:extensionName:]
+ -[NWStatsSource setDelegateAttributionReason:]
+ _OBJC_IVAR_$_NWStatsSnapshot._delegateAttributionReason
+ _OBJC_IVAR_$_NWStatsSource._delegateAttributionReason
+ _attributionReasonString
+ _objc_msgSend$delegateAttributionReason
+ _objc_msgSend$setAttribution:derivation:delegateName:delegateDerivation:extensionName:
+ _objc_msgSend$setDelegateAttributionReason:
- -[NWStatsProtocolSnapshot setAttribution:derivation:delegateName:extensionName:isADaemon:]
- -[NWStatsSnapshot setAttribution:derivation:delegateName:extensionName:isADaemon:]
- -[NWStatsSnapshot setIsADaemon:]
- -[NWStatsSource isADaemon]
- -[NWStatsSource setAttribution:derivation:delegateName:extensionName:isADaemon:]
- -[NWStatsSource setIsADaemon:]
- _OBJC_IVAR_$_NWStatsSnapshot._isADaemon
- _OBJC_IVAR_$_NWStatsSource._isADaemon
- _objc_msgSend$isADaemon
- _objc_msgSend$setAttribution:derivation:delegateName:extensionName:isADaemon:
- _objc_msgSend$setIsADaemon:
CStrings:
+ "Ti,N,V_delegateAttributionReason"
+ "Ti,V_delegateAttributionReason"
+ "_delegateAttributionReason"
+ "delegateAttributionReason"
+ "delegateAttributionReasonString"
+ "reason-nehelp"
+ "reason-static"
+ "setAttribution:derivation:delegateName:delegateDerivation:extensionName:"
+ "setDelegateAttributionReason:"
+ "v48@0:8@16i24@28i36@40"
- "TB,N,V_isADaemon"
- "TB,V_isADaemon"
- "_isADaemon"
- "reason-nehelp "
- "reason-static "
- "setAttribution:derivation:delegateName:extensionName:isADaemon:"
- "setIsADaemon:"
- "v48@0:8@16i24@28@36B44"

```
