## SystemMigrationUtils

> `/System/Library/PrivateFrameworks/SystemMigrationUtils.framework/Versions/A/SystemMigrationUtils`

```diff

-  __TEXT.__text: 0xc5e8
-  __TEXT.__objc_methlist: 0xa7c
+  __TEXT.__text: 0xc148
+  __TEXT.__objc_methlist: 0x9d4
   __TEXT.__const: 0x88
-  __TEXT.__cstring: 0x1f33
-  __TEXT.__gcc_except_tab: 0x2e8
+  __TEXT.__gcc_except_tab: 0x2e0
+  __TEXT.__cstring: 0x1b27
   __TEXT.__oslogstring: 0xb
-  __TEXT.__unwind_info: 0x340
+  __TEXT.__unwind_info: 0x320
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1b8
-  __DATA_CONST.__objc_classlist: 0x80
+  __DATA_CONST.__const: 0xc0
+  __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x970
-  __DATA_CONST.__objc_superrefs: 0x40
+  __DATA_CONST.__objc_selrefs: 0x920
+  __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_arraydata: 0x18
-  __DATA_CONST.__got: 0x270
-  __AUTH_CONST.__const: 0x2b0
-  __AUTH_CONST.__cfstring: 0x1ca0
-  __AUTH_CONST.__objc_const: 0x11c8
-  __AUTH_CONST.__objc_intobj: 0xf0
+  __DATA_CONST.__got: 0x268
+  __AUTH_CONST.__const: 0x290
+  __AUTH_CONST.__cfstring: 0x1660
+  __AUTH_CONST.__objc_const: 0x1080
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH_CONST.__auth_got: 0x550
-  __AUTH.__objc_data: 0x4d8
-  __DATA.__objc_ivar: 0x7c
+  __AUTH_CONST.__auth_got: 0x540
+  __AUTH.__objc_data: 0x438
+  __DATA.__objc_ivar: 0x78
   __DATA.__data: 0x68
-  __DATA.__bss: 0x40
+  __DATA.__bss: 0x30
   __DATA_DIRTY.__objc_data: 0x28
   __DATA_DIRTY.__bss: 0x8
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libfakelink.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 250
-  Symbols:   954
-  CStrings:  511
+  Functions: 237
+  Symbols:   895
+  CStrings:  409
 
Sections:
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
Symbols:
+ -[SMUDataTemplateCopier _copyDataTemplateFromPath:toPath:error:progress:]
+ -[SMUDataTemplateCopier copyOverlayFromURL:toURL:error:]
+ GCC_except_table25
+ _objc_msgSend$_copyDataTemplateFromPath:toPath:error:progress:
- +[SMAnalyticsFieldConverter valueForCWPHYMode:]
- +[SMAnalyticsManager sharedManager]
- -[SMAnalyticsManager .cxx_destruct]
- -[SMAnalyticsManager init]
- -[SMAnalyticsManager sendEvent:withPayload:]
- -[SMAnalyticsManager traceEventOverallResults1_0:]
- -[SMAnalyticsManager traceMigrationCompleted:]
- -[SMAnalyticsManager traceMigrationTransferStatus:]
- -[SMAnalyticsManager traceODTokenIssuingSuccess:afterRetries:]
- -[SMAnalyticsManager tracePostLoginTaskErrors:]
- -[SMAnalyticsManager tracePostLoginTaskPerformance:]
- -[SMAnalyticsManager traceQuarantinedPath:]
- -[SMAnalyticsManager traceWiFiInfo:]
- OBJC_IVAR_$_SMAnalyticsManager._status
- _AnalyticsSendEvent
- _OBJC_CLASS_$_NSConstantIntegerNumber
- _OBJC_CLASS_$_SMAnalyticsFieldConverter
- _OBJC_CLASS_$_SMAnalyticsManager
- _OBJC_METACLASS_$_SMAnalyticsFieldConverter
- _OBJC_METACLASS_$_SMAnalyticsManager
- _SMAnalyticsCAEventPayloadKeyErrorSignature
- _SMAnalyticsCAEventPayloadKeyMHPostLoginErrorCount
- _SMAnalyticsCAEventPayloadKeyMHPostLoginErrorDescriptions
- _SMAnalyticsCAEventPayloadKeyMHPostLoginErrorIdentity
- _SMAnalyticsCAEventPayloadKeyMHPostLoginPerfTotalDuration
- _SMAnalyticsCAEventPayloadKeyMigrationID
- _SMAnalyticsCAEventPayloadKeyODSTIssuingSuccess
- _SMAnalyticsCAEventPayloadKeyODSTRetries
- _SMAnalyticsCAEventPayloadKeyOriginatingApp
- _SMAnalyticsCAEventPayloadKeyOverallThroughput
- _SMAnalyticsCAEventPayloadKeyPath
- _SMAnalyticsCAEventPayloadKeyPhase
- _SMAnalyticsCAEventPayloadKeyPreferredTransferMode
- _SMAnalyticsCAEventPayloadKeyRequestState_1
- _SMAnalyticsCAEventPayloadKeyResult
- _SMAnalyticsCAEventPayloadKeySizeExpected
- _SMAnalyticsCAEventPayloadKeySizeTransferred
- _SMAnalyticsCAEventPayloadKeySourceType_1
- _SMAnalyticsCAEventPayloadKeyTimeExpected
- _SMAnalyticsCAEventPayloadKeyTimeTaken
- _SMAnalyticsCAEventPayloadKeyWiFiSignalNoise
- _SMAnalyticsCAEventPayloadKeyWiFiSignalStrength
- _SMAnalyticsCAEventPayloadKeyWiFiSpecification
- _SMAnalyticsCAEventPayloadKeyWireThroughput
- _SMAnalyticsCAEventPayloadKeyWireThroughputExpected
- __OBJC_$_CLASS_METHODS_SMAnalyticsFieldConverter
- __OBJC_$_CLASS_METHODS_SMAnalyticsManager
- __OBJC_$_INSTANCE_METHODS_SMAnalyticsManager
- __OBJC_$_INSTANCE_VARIABLES_SMAnalyticsManager
- __OBJC_CLASS_RO_$_SMAnalyticsFieldConverter
- __OBJC_CLASS_RO_$_SMAnalyticsManager
- __OBJC_METACLASS_RO_$_SMAnalyticsFieldConverter
- __OBJC_METACLASS_RO_$_SMAnalyticsManager
- ___35+[SMAnalyticsManager sharedManager]_block_invoke
- _getenv
- _objc_msgSend$numberWithBool:
- _objc_msgSend$numberWithInteger:
- _objc_msgSend$sendEvent:withPayload:
- sharedManager.manager
- sharedManager.onceToken
CStrings:
- "-[SMAnalyticsManager sendEvent:withPayload:]"
- "1"
- "3"
- "4"
- "5"
- "6"
- "7"
- "ErrorCount"
- "ErrorDescriptions"
- "ErrorIdentity"
- "ErrorSignature"
- "MigrationID"
- "OriginatingApp"
- "OverallThroughput"
- "Path"
- "Phase"
- "PreferredTransferMode"
- "Reporting analytics for:\nEvent : %@\n%@"
- "RequestState"
- "Result"
- "Retries"
- "SignalNoise"
- "SignalStrength"
- "SizeExpected"
- "SizeTransferred"
- "SourceType"
- "Success"
- "TimeExpected"
- "TimeTaken"
- "TotalDuration"
- "WLANSpecification"
- "WireThroughput"
- "WireThroughputExpected"
- "__OSINSTALL_ENVIRONMENT"
- "com.apple.SystemMigration.MigrationCompleted"
- "com.apple.SystemMigration.MigrationHelperPostLoginErrors"
- "com.apple.SystemMigration.MigrationHelperPostLoginPerf"
- "com.apple.SystemMigration.OverallResults.1.0"
- "com.apple.SystemMigration.QuarantinedPath"
- "com.apple.SystemMigration.WiFiInfo"
- "com.apple.SystemMigration.macOS.ODTokenIssuing"
- "q"
- "target.transfer.canceled"
- "target.transfer.complete"
- "target.transfer.complete.warning"
- "target.transfer.failed"
- "target.transfer.unknown"
- "windows.transfer.canceled"
- "windows.transfer.complete"
- "windows.transfer.failed"
- "windows.transfer.unknown"
- "windows.transfer.warning"

```
