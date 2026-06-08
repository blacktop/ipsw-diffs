## companioncamerad

> `/System/Library/PrivateFrameworks/CompanionCamera.framework/Support/companioncamerad`

```diff

-2023.500.2.0.0
-  __TEXT.__text: 0x24e70
-  __TEXT.__auth_stubs: 0x750
-  __TEXT.__objc_stubs: 0x2240
-  __TEXT.__objc_methlist: 0x30c4
-  __TEXT.__const: 0x110
-  __TEXT.__gcc_except_tab: 0x1a8
-  __TEXT.__cstring: 0x171a
-  __TEXT.__oslogstring: 0x807
-  __TEXT.__objc_methname: 0x3907
-  __TEXT.__objc_classname: 0x4e1
-  __TEXT.__objc_methtype: 0x12a1
+2024.100.12.0.0
+  __TEXT.__text: 0x240b8
+  __TEXT.__auth_stubs: 0x740
+  __TEXT.__objc_stubs: 0x20c0
+  __TEXT.__objc_methlist: 0x30a4
+  __TEXT.__const: 0x120
+  __TEXT.__gcc_except_tab: 0xc4
+  __TEXT.__cstring: 0x14e8
+  __TEXT.__oslogstring: 0x7bd
+  __TEXT.__objc_methname: 0x3860
+  __TEXT.__objc_classname: 0x4c1
+  __TEXT.__objc_methtype: 0x1301
   __TEXT.__dlopen_cstrs: 0x4f
-  __TEXT.__unwind_info: 0x9a0
-  __DATA_CONST.__auth_got: 0x3b8
-  __DATA_CONST.__got: 0x150
-  __DATA_CONST.__const: 0xc90
-  __DATA_CONST.__cfstring: 0x1240
-  __DATA_CONST.__objc_classlist: 0x178
-  __DATA_CONST.__objc_protolist: 0x38
+  __TEXT.__unwind_info: 0x8f0
+  __DATA_CONST.__const: 0xc78
+  __DATA_CONST.__cfstring: 0x1020
+  __DATA_CONST.__objc_classlist: 0x170
+  __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x158
-  __DATA_CONST.__objc_intobj: 0xc0
-  __DATA.__objc_const: 0x4ea0
-  __DATA.__objc_selrefs: 0x1030
-  __DATA.__objc_ivar: 0x2b4
-  __DATA.__objc_data: 0xeb0
-  __DATA.__data: 0x2a0
-  __DATA.__bss: 0x70
+  __DATA_CONST.__objc_superrefs: 0x150
+  __DATA_CONST.__objc_intobj: 0x18
+  __DATA_CONST.__auth_got: 0x3b0
+  __DATA_CONST.__got: 0x130
+  __DATA.__objc_const: 0x4df8
+  __DATA.__objc_selrefs: 0xfd0
+  __DATA.__objc_ivar: 0x2a4
+  __DATA.__objc_data: 0xe60
+  __DATA.__data: 0x300
+  __DATA.__bss: 0x60
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 35D85955-ED60-3FA5-BD38-AD16DDCCA16C
-  Functions: 1063
-  Symbols:   173
-  CStrings:  1321
+  UUID: A1BDF6FB-2D02-367C-8539-0AA2813036A9
+  Functions: 1041
+  Symbols:   168
+  CStrings:  1266
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x3
+ _objc_retain_x4
- _CFPreferencesGetAppBooleanValue
- _OBJC_CLASS_$_NSCountedSet
- _OBJC_CLASS_$_NSMutableString
- __dispatch_main_q
- __dispatch_source_type_signal
- _objc_retainAutoreleasedReturnValue
- _objc_sync_enter
- _objc_sync_exit
- _signal
CStrings:
+ "@\"<NMSMessageCenterDelegate>\"16@0:8"
+ "NMSMessageCenterProtocol"
+ "NotSupported"
+ "T@\"<NMSMessageCenterDelegate>\",W,N"
+ "VisualIntelligence"
+ "v24@0:8@\"<NMSMessageCenterDelegate>\"16"
+ "v24@0:8@\"NMSOutgoingRequest\"16"
+ "v28@0:8@\"<NMSMessageCenterProtocol>\"16B24"
+ "v32@0:8@\"<NMSMessageCenterProtocol>\"16@\"NMSIncomingRequest\"24"
+ "v32@0:8@\"<NMSMessageCenterProtocol>\"16@\"NMSOutgoingRequest\"24"
+ "v32@0:8@\"<NMSMessageCenterProtocol>\"16@\"NMSUnpairedResponse\"24"
- "%@: %lu\n"
- "@\"NSCountedSet\""
- "@\"NSObject<OS_os_log>\""
- "CameraAppLaunch"
- "CameraAppLaunchFailed"
- "CameraAppLaunchhSucceeded"
- "CameraPreviewIDSSocketCreationFailed"
- "CloseCameraMessageReceived"
- "Count of events:\n%@"
- "DaemonXPCConnectionInterruption"
- "DaemonXPCConnectionInvalidation"
- "DaemonXPCConnectionReceived"
- "FigCameraViewfinderCreation"
- "FigCameraViewfinderSessionDidBegin"
- "FigCameraViewfinderSessionDidEnd"
- "FigCameraViewfinderSessionOpenPreviewStream"
- "FigCameraViewfinderSessionPreviewStreamDidClose"
- "FigCameraViewfinderSessionPreviewStreamDidOpen"
- "FigCameraViewfinderStarted"
- "OpenCameraMessageReceived"
- "Repeated event: %@"
- "Reset events."
- "Unexpected event: %@"
- "ViewfinderReliability"
- "ViewfinderReliability_CheckRepeatedEvents"
- "ViewfinderReliability_CheckUnexpectedEvents"
- "_checkForRepeatedEvent:"
- "_checkForUnexpectedEvent:"
- "_events"
- "_log"
- "_print"
- "_printSource"
- "_registerSources"
- "_reset"
- "_resetSource"
- "appendString:"
- "containsObject:"
- "countForObject:"
- "logEvent:"
- "set"
- "sharedInstance"
- "string"
- "v24@0:8q16"
- "v28@0:8@\"NMSMessageCenter\"16B24"
- "v32@0:8@\"NMSMessageCenter\"16@\"NMSIncomingRequest\"24"
- "v32@0:8@\"NMSMessageCenter\"16@\"NMSOutgoingRequest\"24"
- "v32@0:8@\"NMSMessageCenter\"16@\"NMSUnpairedResponse\"24"

```
