## CMContinuityCaptureCore

> `/System/Library/PrivateFrameworks/CMContinuityCaptureCore.framework/CMContinuityCaptureCore`

```diff

-650.0.0.122.4
-  __TEXT.__text: 0x8bc78
+655.0.0.122.4
+  __TEXT.__text: 0x8bd38
   __TEXT.__auth_stubs: 0x1060
-  __TEXT.__objc_methlist: 0x5d30
-  __TEXT.__const: 0x308
-  __TEXT.__gcc_except_tab: 0x3154
-  __TEXT.__cstring: 0x7b29
-  __TEXT.__oslogstring: 0xa8f9
+  __TEXT.__objc_methlist: 0x5d58
+  __TEXT.__const: 0x310
+  __TEXT.__gcc_except_tab: 0x3190
+  __TEXT.__cstring: 0x7b42
+  __TEXT.__oslogstring: 0xa94b
   __TEXT.__dlopen_cstrs: 0x54
-  __TEXT.__unwind_info: 0x20c8
-  __TEXT.__objc_classname: 0xdf1
-  __TEXT.__objc_methname: 0xd874
-  __TEXT.__objc_methtype: 0x2f0c
-  __TEXT.__objc_stubs: 0x95e0
-  __DATA_CONST.__got: 0x7a8
+  __TEXT.__unwind_info: 0x20d8
+  __TEXT.__objc_classname: 0xdf6
+  __TEXT.__objc_methname: 0xd8b3
+  __TEXT.__objc_methtype: 0x2f1b
+  __TEXT.__objc_stubs: 0x9620
+  __DATA_CONST.__got: 0x7b0
   __DATA_CONST.__const: 0x1bd0
   __DATA_CONST.__objc_classlist: 0x200
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x120
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2e70
+  __DATA_CONST.__objc_selrefs: 0x2e88
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x1f0
   __DATA_CONST.__objc_arraydata: 0x80
   __AUTH_CONST.__auth_got: 0x840
   __AUTH_CONST.__const: 0xa20
-  __AUTH_CONST.__cfstring: 0x4260
-  __AUTH_CONST.__objc_const: 0xa468
+  __AUTH_CONST.__cfstring: 0x4280
+  __AUTH_CONST.__objc_const: 0xa470
   __AUTH_CONST.__objc_intobj: 0x510
   __AUTH_CONST.__objc_doubleobj: 0x80
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH.__objc_data: 0x12c0
-  __DATA.__objc_ivar: 0x890
+  __DATA.__objc_ivar: 0x88c
   __DATA.__data: 0xd98
   __DATA.__bss: 0x168
   __DATA.__common: 0x90

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E7A6C510-1F37-3AF6-B5D9-116E471B0030
-  Functions: 2399
-  Symbols:   8552
-  CStrings:  4792
+  UUID: 20D5A4A2-6128-3381-B813-198782CF606F
+  Functions: 2402
+  Symbols:   8561
+  CStrings:  4799
 
Symbols:
+ -[CMContinuityCaptureDeviceBase lastStreamStartTimeInHostClock]
+ -[CMContinuityCaptureDeviceBase startCollectingFrameLatencyMetrics]
+ -[CMContinuityCaptureDeviceBase stopCollectingFrameLatencyMetrics:]
+ -[CMContinuityCaptureParticipantInfo initWithSocialProfileIdentifier:displayName:]
+ -[CMContinuityCaptureParticipantInfo initWithSocialProfileIdentifier:displayName:].cold.1
+ -[CMContinuityCaptureParticipantInfo initWithSocialProfileIdentifier:displayName:].cold.2
+ GCC_except_table47
+ GCC_except_table55
+ GCC_except_table77
+ GCC_except_table96
+ _OBJC_CLASS_$_NSAssertionHandler
+ _OBJC_IVAR_$_CMContinuityCaptureDeviceBase._lastStreamStartTimeInHostClock
+ _objc_msgSend$currentHandler
+ _objc_msgSend$handleFailureInMethod:object:file:lineNumber:description:
+ _objc_msgSend$initWithSocialProfileIdentifier:displayName:
+ _objc_msgSend$startCollectingFrameLatencyMetrics
+ _objc_msgSend$stopCollectingFrameLatencyMetrics:
- -[CMContinuityCaptureParticipantInfo groupSessionIdentifier]
- -[CMContinuityCaptureParticipantInfo initWithGroupSessionIdentifier:socialProfileIdentifier:displayName:]
- -[CMContinuityCaptureParticipantInfo setGroupSessionIdentifier:]
- GCC_except_table42
- GCC_except_table46
- GCC_except_table54
- GCC_except_table57
- GCC_except_table76
- GCC_except_table78
- _OBJC_IVAR_$_CMContinuityCaptureParticipantInfo._groupSessionIdentifier
- _OBJC_IVAR_$_CMContinuityCaptureVideoDevice._streamStartsTime
- _objc_msgSend$groupSessionIdentifier
- _objc_msgSend$initWithGroupSessionIdentifier:socialProfileIdentifier:displayName:
- _objc_msgSend$setGroupSessionIdentifier:
CStrings:
+ "1\xf01"
+ "<%p> [pong-check] %s The pong assertion is already held so we return immediately."
+ "<CMContinuityCaptureParticipantInfo displayName:%@ socialProfileIdentifier:%@>"
+ "CMContinuityCaptureParticipantInfo.m"
+ "Invalid parameter not satisfying: %@"
+ "T{?=qiIq},R,N"
+ "_lastStreamStartTimeInHostClock"
+ "currentHandler"
+ "handleFailureInMethod:object:file:lineNumber:description:"
+ "initWithSocialProfileIdentifier:displayName:"
+ "lastStreamStartTimeInHostClock"
+ "startCollectingFrameLatencyMetrics"
+ "stopCollectingFrameLatencyMetrics:"
+ "{?=qiIq}16@0:8"
+ "\xf01"
- "1\xf1"
- "<CMContinuityCaptureParticipantInfo displayName:%@ groupSessionIdentifier:%@ socialProfileIdentifier:%@>"
- "T@\"NSString\",C,N,V_groupSessionIdentifier"
- "_groupSessionIdentifier"
- "_streamStartsTime"
- "groupSessionIdentifier"
- "initWithGroupSessionIdentifier:socialProfileIdentifier:displayName:"
- "setGroupSessionIdentifier:"

```
