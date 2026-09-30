## CompanionCamera

> `/System/Library/PrivateFrameworks/CompanionCamera.framework/CompanionCamera`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__AUTH_CONST.__const`
- `__AUTH.__objc_data`
- `__DATA.__data`

```diff

 2023.500.2.0.0
-  __TEXT.__text: 0x8ba0
-  __TEXT.__auth_stubs: 0x340
-  __TEXT.__objc_methlist: 0xa54
+  __TEXT.__text: 0x97e4
+  __TEXT.__auth_stubs: 0x3b0
+  __TEXT.__objc_methlist: 0xad4
   __TEXT.__const: 0xf0
-  __TEXT.__gcc_except_tab: 0x94
-  __TEXT.__oslogstring: 0x53b
-  __TEXT.__cstring: 0xb32
-  __TEXT.__unwind_info: 0x230
-  __TEXT.__objc_classname: 0x10a
-  __TEXT.__objc_methname: 0x18e8
-  __TEXT.__objc_methtype: 0x4b3
-  __TEXT.__objc_stubs: 0x15c0
-  __DATA_CONST.__got: 0xb0
-  __DATA_CONST.__const: 0x3f0
-  __DATA_CONST.__objc_classlist: 0x28
+  __TEXT.__gcc_except_tab: 0x14c
+  __TEXT.__oslogstring: 0x585
+  __TEXT.__cstring: 0xda3
+  __TEXT.__unwind_info: 0x288
+  __TEXT.__objc_classname: 0x122
+  __TEXT.__objc_methname: 0x19da
+  __TEXT.__objc_methtype: 0x4da
+  __TEXT.__objc_stubs: 0x1760
+  __DATA_CONST.__got: 0xd0
+  __DATA_CONST.__const: 0x468
+  __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x770
+  __DATA_CONST.__objc_selrefs: 0x7d8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__auth_got: 0x1b0
+  __DATA_CONST.__objc_superrefs: 0x20
+  __AUTH_CONST.__auth_got: 0x1e8
   __AUTH_CONST.__const: 0x3a0
-  __AUTH_CONST.__cfstring: 0x740
-  __AUTH_CONST.__objc_const: 0xa60
-  __AUTH_CONST.__objc_intobj: 0x48
+  __AUTH_CONST.__cfstring: 0x9c0
+  __AUTH_CONST.__objc_const: 0xb78
+  __AUTH_CONST.__objc_intobj: 0xf0
   __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0x78
+  __DATA.__objc_ivar: 0x88
   __DATA.__data: 0x1e0
   __DATA.__bss: 0x20
-  __DATA_DIRTY.__objc_data: 0xf0
-  __DATA_DIRTY.__bss: 0x30
+  __DATA_DIRTY.__objc_data: 0x140
+  __DATA_DIRTY.__bss: 0x40
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /System/Library/PrivateFrameworks/DockKitCore.framework/DockKitCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 245
-  Symbols:   602
-  CStrings:  482
+  Functions: 263
+  Symbols:   653
+  CStrings:  525
 
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
+ _objc_msgSend$_checkForRepeatedEvent:
+ _objc_msgSend$_checkForUnexpectedEvent:
+ _objc_msgSend$_print
+ _objc_msgSend$_registerSources
+ _objc_msgSend$_reset
+ _objc_msgSend$addObject:
+ _objc_msgSend$appendString:
+ _objc_msgSend$countByEnumeratingWithState:objects:count:
+ _objc_msgSend$countForObject:
+ _objc_msgSend$logEvent:
+ _objc_msgSend$removeAllObjects
+ _objc_msgSend$set
+ _objc_msgSend$string
+ _objc_sync_enter
+ _objc_sync_exit
+ _os_variant_has_internal_diagnostics
+ _signal
CStrings:
+ "%@: %lu\n"
+ "@\"NSCountedSet\""
+ "@\"NSObject<OS_os_log>\""
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
+ "_checkForRepeatedEvent:"
+ "_checkForUnexpectedEvent:"
+ "_events"
+ "_log"
+ "_print"
+ "_printSource"
+ "_registerSources"
+ "_reset"
+ "_resetSource"
+ "addObject:"
+ "appendString:"
+ "countByEnumeratingWithState:objects:count:"
+ "countForObject:"
+ "logEvent:"
+ "removeAllObjects"
+ "set"
+ "string"
```
