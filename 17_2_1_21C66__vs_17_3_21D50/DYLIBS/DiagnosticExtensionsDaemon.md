## DiagnosticExtensionsDaemon

> `/System/Library/PrivateFrameworks/DiagnosticExtensionsDaemon.framework/DiagnosticExtensionsDaemon`

```diff

-170.2.3.0.0
-  __TEXT.__text: 0x6d75c
-  __TEXT.__auth_stubs: 0x960
-  __TEXT.__objc_methlist: 0x5d54
+170.2.3.2.0
+  __TEXT.__text: 0x6dccc
+  __TEXT.__auth_stubs: 0x980
+  __TEXT.__objc_methlist: 0x5dbc
   __TEXT.__const: 0xd0
-  __TEXT.__cstring: 0x4f69
-  __TEXT.__gcc_except_tab: 0x143c
+  __TEXT.__cstring: 0x4fdc
+  __TEXT.__gcc_except_tab: 0x1438
   __TEXT.__oslogstring: 0x8345
   __TEXT.__ustring: 0xc
-  __TEXT.__unwind_info: 0x1918
-  __TEXT.__objc_classname: 0x871
-  __TEXT.__objc_methname: 0xe8ed
-  __TEXT.__objc_methtype: 0x22e7
-  __TEXT.__objc_stubs: 0xb9a0
-  __DATA_CONST.__got: 0x1b0
+  __TEXT.__unwind_info: 0x1924
+  __TEXT.__objc_classname: 0x873
+  __TEXT.__objc_methname: 0xeacf
+  __TEXT.__objc_methtype: 0x230a
+  __TEXT.__objc_stubs: 0xbb20
+  __DATA_CONST.__got: 0x1c0
   __DATA_CONST.__const: 0x1bc8
   __DATA_CONST.__objc_classlist: 0x258
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x11718
-  __DATA_CONST.__objc_selrefs: 0x36e8
+  __DATA_CONST.__objc_const: 0x11778
+  __DATA_CONST.__objc_selrefs: 0x3758
   __DATA_CONST.__objc_arraydata: 0x48
-  __AUTH_CONST.__cfstring: 0x4aa0
+  __AUTH_CONST.__cfstring: 0x4b20
   __AUTH_CONST.__objc_const: 0x2020
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__const: 0xbc0
   __AUTH_CONST.__objc_intobj: 0x330
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH_CONST.__auth_got: 0x4c0
+  __AUTH_CONST.__auth_got: 0x4d0
   __AUTH.__objc_data: 0xeb0
   __DATA.__objc_protorefs: 0x28
-  __DATA.__objc_classrefs: 0x500
+  __DATA.__objc_classrefs: 0x508
   __DATA.__objc_superrefs: 0x1a0
-  __DATA.__objc_ivar: 0x59c
+  __DATA.__objc_ivar: 0x5a4
   __DATA.__data: 0xa40
   __DATA.__bss: 0x178
   __DATA_DIRTY.__objc_data: 0x8c0

   - /System/Library/Frameworks/MultipeerConnectivity.framework/MultipeerConnectivity
   - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
   - /System/Library/Frameworks/Security.framework/Security
+  - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
   - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
   - /System/Library/PrivateFrameworks/AirPlaySupport.framework/AirPlaySupport
+  - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreFollowUp.framework/CoreFollowUp
   - /System/Library/PrivateFrameworks/DiagnosticExtensions.framework/DiagnosticExtensions

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2C430DEF-DE73-30B4-821F-DAF8A9C51BA3
-  Functions: 2719
-  Symbols:   9282
-  CStrings:  5018
+  UUID: 1C9B1100-B7CC-3C11-8D6A-AF2CD6A665A7
+  Functions: 2728
+  Symbols:   9319
+  CStrings:  5046
 
Symbols:
+ -[DEDCloudKitClient previousRecordsQueue]
+ -[DEDCloudKitClient restoreQueue]
+ -[DEDCloudKitClient setPreviousRecordsQueue:]
+ -[DEDCloudKitFinisher _performCloudKitOperations]
+ -[DEDCloudKitFinisher _reachabilityChanged:]
+ -[DEDCloudKitFinisher attachmentGroupModel]
+ -[DEDCloudKitFinisher scheduleOperationsOnAvailability]
+ -[DEDCloudKitFinisher setAttachmentGroupModel:]
+ -[DEDCloudKitFinisher unscheduleOperationsOnAvailability]
+ _CPNetworkObserverReachable
+ _CPNetworkObserverReachableFlags
+ _OBJC_CLASS_$_CPNetworkObserver
+ _OBJC_IVAR_$_DEDCloudKitClient._previousRecordsQueue
+ _OBJC_IVAR_$_DEDCloudKitFinisher._attachmentGroupModel
+ ___49-[DEDCloudKitFinisher _performCloudKitOperations]_block_invoke
+ ___49-[DEDCloudKitFinisher _performCloudKitOperations]_block_invoke_2
+ _objc_msgSend$_performCloudKitOperations
+ _objc_msgSend$addObserver:selector:forHostname:
+ _objc_msgSend$attachmentGroupModel
+ _objc_msgSend$previousRecordsQueue
+ _objc_msgSend$removeObserver:
+ _objc_msgSend$restoreQueue
+ _objc_msgSend$scheduleOperationsOnAvailability
+ _objc_msgSend$setAllowsExpensiveNetworkAccess:
+ _objc_msgSend$setAttachmentGroupModel:
+ _objc_msgSend$setPreviousRecordsQueue:
+ _objc_msgSend$sharedNetworkObserver
+ _objc_msgSend$unscheduleOperationsOnAvailability
+ _objc_msgSend$userInfo
+ _xpc_activity_copy_criteria
+ _xpc_equal
- GCC_except_table25
- ___55-[DEDCloudKitFinisher finishSession:withConfiguration:]_block_invoke.99
- ___55-[DEDCloudKitFinisher finishSession:withConfiguration:]_block_invoke_2
- _objc_msgSend$bugSessionConfig
CStrings:
+ "\x06"
+ "%f"
+ "1\x17"
+ "@\"DEDCloudKitAttachmentGroupModel\""
+ "T@\"DEDCloudKitAttachmentGroupModel\",&,V_attachmentGroupModel"
+ "T@\"NSArray\",&,N,V_previousRecordsQueue"
+ "_attachmentGroupModel"
+ "_performCloudKitOperations"
+ "_previousRecordsQueue"
+ "_reachabilityChanged:"
+ "addObserver:selector:forHostname:"
+ "apple.com"
+ "attachmentGroupModel"
+ "com.apple.diagnosticextensionsd.commit-file-%@-%@"
+ "com.apple.diagnosticextensionsd.commit-record-%@-%@"
+ "previousRecordsQueue"
+ "removeObserver:"
+ "restoreQueue"
+ "scheduleOperationsOnAvailability"
+ "setAllowsExpensiveNetworkAccess:"
+ "setAttachmentGroupModel:"
+ "setPreviousRecordsQueue:"
+ "sharedNetworkObserver"
+ "unscheduleOperationsOnAvailability"
+ "userInfo"
- "1\x16"

```
