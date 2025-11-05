## SafetyKit

> `/System/Library/Frameworks/SafetyKit.framework/Versions/A/SafetyKit`

```diff

-121.0.1.0.0
-  __TEXT.__text: 0xead8
+125.0.14.0.0
+  __TEXT.__text: 0xeb38
   __TEXT.__auth_stubs: 0x4c0
-  __TEXT.__objc_methlist: 0xa28
+  __TEXT.__objc_methlist: 0xd84
   __TEXT.__const: 0x90
-  __TEXT.__cstring: 0x147f
+  __TEXT.__cstring: 0x16c4
   __TEXT.__oslogstring: 0x18fa
-  __TEXT.__gcc_except_tab: 0x2cc
-  __TEXT.__unwind_info: 0x420
-  __TEXT.__objc_classname: 0x2c8
-  __TEXT.__objc_methname: 0x272c
-  __TEXT.__objc_methtype: 0xa61
+  __TEXT.__gcc_except_tab: 0x2d4
+  __TEXT.__unwind_info: 0x438
+  __TEXT.__objc_classname: 0x2da
+  __TEXT.__objc_methname: 0x2749
+  __TEXT.__objc_methtype: 0xa6f
   __TEXT.__objc_stubs: 0x1fe0
   __DATA_CONST.__got: 0x210
-  __DATA_CONST.__const: 0xe8
-  __DATA_CONST.__objc_classlist: 0x88
+  __DATA_CONST.__const: 0x180
+  __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8d8
+  __DATA_CONST.__objc_selrefs: 0xa18
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x60
   __AUTH_CONST.__auth_got: 0x270
   __AUTH_CONST.__const: 0x5b0
-  __AUTH_CONST.__cfstring: 0x720
-  __AUTH_CONST.__objc_const: 0x2b60
-  __AUTH.__objc_data: 0x550
+  __AUTH_CONST.__cfstring: 0x900
+  __AUTH_CONST.__objc_const: 0x2638
+  __AUTH.__objc_data: 0x5a0
   __DATA.__objc_ivar: 0xbc
   __DATA.__data: 0x608
   __DATA.__bss: 0x60

   - /System/Library/PrivateFrameworks/TCC.framework/Versions/A/TCC
   - /System/Library/PrivateFrameworks/TelephonyUtilities.framework/Versions/A/TelephonyUtilities
   - /usr/lib/libSystem.B.dylib
+  - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1A5531CD-11B0-37E7-B042-1ED1DDFD2607
-  Functions: 384
-  Symbols:   1145
-  CStrings:  874
+  UUID: E6A1533C-599F-3F48-AE79-B4EFDCDA747A
+  Functions: 391
+  Symbols:   1172
+  CStrings:  907
 
Symbols:
+ +[SABundleManager locationBundle].cold.1
+ +[SACrashDetectionManager isAvailable].cold.1
+ -[CSKappaConnection sendFeedbackConsent:andUUID:]
+ -[SACrashDetectionManager authorizationStatus].cold.1
+ -[SACrashDetectionManager requestAuthorizationWithCompletionHandler:].cold.5
+ -[SACrashDetectionManager setDelegate:].cold.3
+ _CSKappaConnectionBringupFeedbackAssistantMessage
+ _CSKappaConnectionCommandKey
+ _CSKappaConnectionFeedbackAssistantConsentKey
+ _CSKappaConnectionFeedbackAssistantConsentResponse
+ _CSKappaConnectionFeedbackAssistantUUIDKey
+ _CSKappaConnectionReturn
+ _CSKappaConnectionSendCommandName
+ _CSKappaConnectionServiceName
+ _CSKappaConnectionTestMessageName
+ _CSKappaConnectionTestPowerAssertionName
+ _CSKappaConnectionTestSOSName
+ _CSKappaConnectionTestSignalName
+ _CSKappaConnectionTestTTRName
+ _CSKappaConnectionTestTriggerName
+ _CSKappaConnectionValueKey
+ _OBJC_CLASS_$_CSKappaConnection
+ _OBJC_METACLASS_$_CSKappaConnection
+ __OBJC_$_INSTANCE_METHODS_CSKappaConnection
+ __OBJC_CLASS_RO_$_CSKappaConnection
+ __OBJC_METACLASS_RO_$_CSKappaConnection
+ sa_default_log.cold.1
- _OUTLINED_FUNCTION_8
CStrings:
+ "CSKappaCommandKey"
+ "CSKappaConnection"
+ "CSKappaConnectionBringupFeedbackAssistantMessage"
+ "CSKappaFeedbackAssistantConsentKey"
+ "CSKappaFeedbackAssistantUUIDKey"
+ "CSKappaReturnKey"
+ "CSKappaValueKey"
+ "com.apple.anomalydetectiond.kappa"
+ "com.apple.anomalydetectiond.kappa.command"
+ "com.apple.anomalydetectiond.kappa.feedbackConsentResponse"
+ "com.apple.anomalydetectiond.kappa.message.test"
+ "com.apple.anomalydetectiond.kappa.powerassertion.test"
+ "com.apple.anomalydetectiond.kappa.signal.test"
+ "com.apple.anomalydetectiond.kappa.sos.test"
+ "com.apple.anomalydetectiond.kappa.trigger.test"
+ "com.apple.anomalydetectiond.kappa.ttr.test"
+ "sendFeedbackConsent:andUUID:"
+ "v28@0:8B16@20"

```
