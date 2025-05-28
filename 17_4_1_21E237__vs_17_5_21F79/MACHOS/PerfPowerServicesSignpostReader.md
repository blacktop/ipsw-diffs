## PerfPowerServicesSignpostReader

> `/System/Library/PrivateFrameworks/PowerlogCore.framework/XPCServices/PerfPowerServicesSignpostReader.xpc/PerfPowerServicesSignpostReader`

```diff

-1851.102.4.0.0
-  __TEXT.__text: 0x93b8
-  __TEXT.__auth_stubs: 0x4f0
-  __TEXT.__objc_stubs: 0x17e0
-  __TEXT.__objc_methlist: 0x3c4
+1851.120.59.0.0
+  __TEXT.__text: 0xa9ec
+  __TEXT.__auth_stubs: 0x500
+  __TEXT.__objc_stubs: 0x1b80
+  __TEXT.__objc_methlist: 0x400
   __TEXT.__const: 0x90
-  __TEXT.__cstring: 0xb64
+  __TEXT.__cstring: 0xc22
   __TEXT.__objc_classname: 0x85
-  __TEXT.__objc_methname: 0x1980
+  __TEXT.__objc_methname: 0x1ba4
   __TEXT.__objc_methtype: 0x258
-  __TEXT.__oslogstring: 0x7cb
-  __TEXT.__gcc_except_tab: 0x29c
-  __TEXT.__unwind_info: 0x1ec
-  __DATA_CONST.__auth_got: 0x288
-  __DATA_CONST.__got: 0x38
-  __DATA_CONST.__const: 0x310
-  __DATA_CONST.__cfstring: 0x1300
+  __TEXT.__oslogstring: 0x9d9
+  __TEXT.__gcc_except_tab: 0x330
+  __TEXT.__unwind_info: 0x208
+  __DATA_CONST.__auth_got: 0x290
+  __DATA_CONST.__got: 0x40
+  __DATA_CONST.__const: 0x3b0
+  __DATA_CONST.__cfstring: 0x1400
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_classrefs: 0x108
+  __DATA_CONST.__objc_classrefs: 0x118
   __DATA_CONST.__objc_superrefs: 0x18
-  __DATA_CONST.__objc_intobj: 0x48
+  __DATA_CONST.__objc_intobj: 0x60
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__objc_arraydata: 0x20
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA.__objc_const: 0xb58
-  __DATA.__objc_selrefs: 0x700
+  __DATA.__objc_selrefs: 0x7e8
   __DATA.__objc_ivar: 0x78
   __DATA.__objc_data: 0x140
   __DATA.__data: 0x120

   - /System/Library/PrivateFrameworks/SampleAnalysis.framework/SampleAnalysis
   - /System/Library/PrivateFrameworks/SignpostCollection.framework/SignpostCollection
   - /System/Library/PrivateFrameworks/SignpostSupport.framework/SignpostSupport
+  - /System/Library/PrivateFrameworks/WorkflowResponsiveness.framework/WorkflowResponsiveness
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsystemstats.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 148
-  Symbols:   154
-  CStrings:  565
+  Functions: 159
+  Symbols:   158
+  CStrings:  615
 
Symbols:
+ _OBJC_CLASS_$_WRWorkflow
+ _OBJC_CLASS_$_WRWorkflowEventTracker
+ _WRErrorDomain
+ _objc_retainBlock
CStrings:
+ "B16@?0@\"SignpostObject\"8"
+ "B8@?0"
+ "CollectionType"
+ "ErrorCode"
+ "IndividuationIdentifier"
+ "OverallEndTime"
+ "OverallStartTime"
+ "Powerlog"
+ "Using allowlist for signpost reading: %@"
+ "WorkflowName"
+ "WorkflowResponsiveness"
+ "[WR] Appending allowlist for workflow '%@': %@"
+ "[WR] Appending allowlist for workflow responsiveness: %@"
+ "[WR] Completing workflow event tracker for workflow '%@'..."
+ "[WR] Event processed for workflow '%@': %@"
+ "[WR] Incomplete Interval processed for workflow '%@': %@"
+ "[WR] Interval processed for workflow '%@': %@"
+ "[WR] Processing signpost object (%@:%@) for workflow '%@': %@"
+ "[WR] Resetting event tracker for workflow '%@' due to device reboot"
+ "[WR] Setting up tracker for workflow '%@'..."
+ "addAllowlist:"
+ "allSignpostTrackers"
+ "allWorkflows"
+ "allowListForAllSignposts"
+ "domain"
+ "emits"
+ "end"
+ "eventEnd"
+ "eventStart"
+ "handleSignpost:"
+ "incompleteIntervalStarts"
+ "individuationIdentifier"
+ "initForReadbackWithWorkflow:eventCompletionCallback:"
+ "intervals"
+ "machContTimeNs"
+ "mutableCopy"
+ "passesSubsystem:category:"
+ "reset"
+ "setBeginEventProcessingBlock:"
+ "setDeviceRebootProcessingBlock:"
+ "signpost"
+ "start"
+ "v16@?0@\"WRWorkflowEventTracker\"8"
+ "workflow"
+ "workflowDataForEventTracker:"
+ "workflowDataForSignpostTracker:"
+ "workflowDataForWREvent:"
+ "workflowDataForWRIncompleteInterval:"
+ "workflowDataForWRInterval:"

```
