## CompanionCamera

> `/System/Library/PrivateFrameworks/CompanionCamera.framework/CompanionCamera`

```diff

 2024.200.4.0.0
-  __TEXT.__text: 0x8934
-  __TEXT.__objc_methlist: 0xb3c
+  __TEXT.__text: 0x945c
+  __TEXT.__objc_methlist: 0xbbc
   __TEXT.__const: 0x110
-  __TEXT.__gcc_except_tab: 0x78
-  __TEXT.__oslogstring: 0x5c1
-  __TEXT.__cstring: 0xd07
-  __TEXT.__unwind_info: 0x418
+  __TEXT.__gcc_except_tab: 0x118
+  __TEXT.__oslogstring: 0x60b
+  __TEXT.__cstring: 0xf7a
+  __TEXT.__unwind_info: 0x488
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x3f0
-  __DATA_CONST.__objc_classlist: 0x28
+  __DATA_CONST.__const: 0x468
+  __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x810
+  __DATA_CONST.__objc_selrefs: 0x878
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x18
-  __DATA_CONST.__got: 0xa8
+  __DATA_CONST.__objc_superrefs: 0x20
+  __DATA_CONST.__got: 0xc8
   __AUTH_CONST.__const: 0x460
-  __AUTH_CONST.__cfstring: 0x720
-  __AUTH_CONST.__objc_const: 0xa90
-  __AUTH_CONST.__objc_intobj: 0x48
+  __AUTH_CONST.__cfstring: 0x9a0
+  __AUTH_CONST.__objc_const: 0xba8
+  __AUTH_CONST.__objc_intobj: 0xf0
   __AUTH_CONST.__auth_got: 0x0
-  __DATA.__objc_ivar: 0x78
+  __DATA.__objc_ivar: 0x88
   __DATA.__data: 0x1e0
-  __DATA_DIRTY.__objc_data: 0x190
-  __DATA_DIRTY.__bss: 0x40
+  __DATA_DIRTY.__objc_data: 0x1e0
+  __DATA_DIRTY.__bss: 0x50
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /System/Library/PrivateFrameworks/DockKitCore.framework/DockKitCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 253
-  Symbols:   448
-  CStrings:  139
+  Functions: 269
+  Symbols:   486
+  CStrings:  163
 
Symbols:
+ +[ViewfinderReliability sharedInstance]
+ -[ViewfinderReliability .cxx_destruct]
+ -[ViewfinderReliability _checkForRepeatedEvent:]
+ -[ViewfinderReliability _checkForUnexpectedEvent:]
+ -[ViewfinderReliability _print]
+ -[ViewfinderReliability _registerSources]
+ -[ViewfinderReliability _reset]
+ -[ViewfinderReliability init]
+ -[ViewfinderReliability logEvent:]
+ GCC_except_table3
+ GCC_except_table5
+ GCC_except_table8
+ GCC_except_table9
+ _CFPreferencesGetAppBooleanValue
+ _NSStringFromViewfinderReliabiliyEvent
+ _OBJC_CLASS_$_NSCountedSet
+ _OBJC_CLASS_$_NSMutableString
+ _OBJC_CLASS_$_ViewfinderReliability
+ _OBJC_IVAR_$_ViewfinderReliability._events
+ _OBJC_IVAR_$_ViewfinderReliability._log
+ _OBJC_IVAR_$_ViewfinderReliability._printSource
+ _OBJC_IVAR_$_ViewfinderReliability._resetSource
+ _OBJC_METACLASS_$_ViewfinderReliability
+ __OBJC_$_CLASS_METHODS_ViewfinderReliability
+ __OBJC_$_INSTANCE_METHODS_ViewfinderReliability
+ __OBJC_$_INSTANCE_VARIABLES_ViewfinderReliability
+ __OBJC_CLASS_RO_$_ViewfinderReliability
+ __OBJC_METACLASS_RO_$_ViewfinderReliability
+ ___39+[ViewfinderReliability sharedInstance]_block_invoke
+ ___41-[ViewfinderReliability _registerSources]_block_invoke
+ ___41-[ViewfinderReliability _registerSources]_block_invoke_2
+ __dispatch_source_type_signal
+ __os_log_fault_impl
+ _objc_enumerationMutation
+ _objc_sync_enter
+ _objc_sync_exit
+ _os_variant_has_internal_diagnostics
+ _signal
CStrings:
+ "%@: %lu\n"
+ "CameraAppLaunch"
+ "CameraAppLaunchFailed"
+ "CameraAppLaunchhSucceeded"
+ "CameraPreviewIDSSocketCreationFailed"
+ "CloseCameraMessageReceived"
+ "Count of events:\n%@"
+ "DaemonXPCConnectionInterruption"
+ "DaemonXPCConnectionInvalidation"
+ "DaemonXPCConnectionReceived"
+ "FigCameraViewfinderCreation"
+ "FigCameraViewfinderSessionDidBegin"
+ "FigCameraViewfinderSessionDidEnd"
+ "FigCameraViewfinderSessionOpenPreviewStream"
+ "FigCameraViewfinderSessionPreviewStreamDidClose"
+ "FigCameraViewfinderSessionPreviewStreamDidOpen"
+ "FigCameraViewfinderStarted"
+ "OpenCameraMessageReceived"
+ "Repeated event: %@"
+ "Reset events."
+ "Unexpected event: %@"
+ "ViewfinderReliability"
+ "ViewfinderReliability_CheckRepeatedEvents"
+ "ViewfinderReliability_CheckUnexpectedEvents"
```
