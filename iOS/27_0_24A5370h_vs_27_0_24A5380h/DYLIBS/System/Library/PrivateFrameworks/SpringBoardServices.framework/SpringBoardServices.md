## SpringBoardServices

> `/System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices`

```diff

-  __TEXT.__text: 0x7a5ec
-  __TEXT.__objc_methlist: 0x8a68
-  __TEXT.__cstring: 0xdc48
+  __TEXT.__text: 0x7b5fc
+  __TEXT.__objc_methlist: 0x8b58
+  __TEXT.__cstring: 0xde60
   __TEXT.__const: 0x768
-  __TEXT.__oslogstring: 0x4787
-  __TEXT.__gcc_except_tab: 0xc94
+  __TEXT.__oslogstring: 0x490e
+  __TEXT.__gcc_except_tab: 0xcbc
   __TEXT.__dlopen_cstrs: 0x170
   __TEXT.__ustring: 0x58
-  __TEXT.__unwind_info: 0x29c0
+  __TEXT.__unwind_info: 0x29f8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x3928
-  __DATA_CONST.__objc_classlist: 0x6c8
+  __DATA_CONST.__const: 0x3908
+  __DATA_CONST.__objc_classlist: 0x6d0
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x2c0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3448
+  __DATA_CONST.__objc_selrefs: 0x3490
   __DATA_CONST.__objc_protorefs: 0x1b8
-  __DATA_CONST.__objc_superrefs: 0x480
+  __DATA_CONST.__objc_superrefs: 0x488
   __DATA_CONST.__objc_arraydata: 0x18
-  __DATA_CONST.__got: 0x8b8
+  __DATA_CONST.__got: 0x8c0
   __AUTH_CONST.__const: 0x2908
-  __AUTH_CONST.__cfstring: 0xace0
-  __AUTH_CONST.__objc_const: 0x25b70
+  __AUTH_CONST.__cfstring: 0xaea0
+  __AUTH_CONST.__objc_const: 0x260a8
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_got: 0x830
-  __AUTH.__objc_data: 0x33e0
-  __DATA.__objc_ivar: 0x864
+  __AUTH.__objc_data: 0x3ac0
+  __DATA.__objc_ivar: 0x874
   __DATA.__data: 0x2210
   __DATA.__bss: 0x900
-  __DATA_DIRTY.__objc_data: 0xff0
+  __DATA_DIRTY.__objc_data: 0x960
   __DATA_DIRTY.__data: 0x40
   __DATA_DIRTY.__bss: 0x268
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 4274
-  Symbols:   14550
-  CStrings:  3485
+  Functions: 4302
+  Symbols:   14633
+  CStrings:  3521
 
Sections:
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __DATA.__data : content changed
Symbols:
+ +[SBSAppResizingServiceStatus supportsBSXPCSecureCoding]
+ -[SBSAppResizingService _resetForBrokenConnection]
+ -[SBSAppResizingService addObserver:]
+ -[SBSAppResizingService removeObserver:]
+ -[SBSAppResizingService serverDidUpdateStatus:]
+ -[SBSAppResizingService status]
+ -[SBSAppResizingServiceStatus .cxx_destruct]
+ -[SBSAppResizingServiceStatus description]
+ -[SBSAppResizingServiceStatus encodeWithBSXPCCoder:]
+ -[SBSAppResizingServiceStatus hash]
+ -[SBSAppResizingServiceStatus initWithBSXPCCoder:]
+ -[SBSAppResizingServiceStatus initWithUnavailabilityReasons:resizableApplication:]
+ -[SBSAppResizingServiceStatus isEqual:]
+ -[SBSAppResizingServiceStatus isResizingPossible]
+ -[SBSAppResizingServiceStatus resizableApplication]
+ -[SBSAppResizingServiceStatus unavailabilityReasons]
+ -[SBSLockScreenService simulateCaptureLaunchFromSource:bundleIdentifier:completion:]
+ -[SBSLockScreenServiceConnection simulateCaptureLaunchFromSource:bundleIdentifier:completion:]
+ _OBJC_CLASS_$_SBSAppResizingServiceStatus
+ _OBJC_IVAR_$_SBSAppResizingService._lock_observers
+ _OBJC_IVAR_$_SBSAppResizingService._lock_status
+ _OBJC_IVAR_$_SBSAppResizingServiceStatus._resizableApplication
+ _OBJC_IVAR_$_SBSAppResizingServiceStatus._unavailabilityReasons
+ _OBJC_METACLASS_$_SBSAppResizingServiceStatus
+ _OUTLINED_FUNCTION_9
+ _SBSAppResizingUnavailabilityReasonsDescription
+ _SBSCaptureLaunchSimulationErrorDomain
+ __OBJC_$_CLASS_METHODS_SBSAppResizingServiceStatus
+ __OBJC_$_INSTANCE_METHODS_SBSAppResizingServiceStatus
+ __OBJC_$_INSTANCE_VARIABLES_SBSAppResizingServiceStatus
+ __OBJC_$_PROP_LIST_SBSAppResizingServiceStatus
+ __OBJC_CLASS_PROTOCOLS_$_SBSAppResizingServiceStatus
+ __OBJC_CLASS_RO_$_SBSAppResizingServiceStatus
+ __OBJC_METACLASS_RO_$_SBSAppResizingServiceStatus
+ ___94-[SBSLockScreenServiceConnection simulateCaptureLaunchFromSource:bundleIdentifier:completion:]_block_invoke
+ _objc_msgSend$_resetForBrokenConnection
+ _objc_msgSend$initWithUnavailabilityReasons:resizableApplication:
+ _objc_msgSend$isResizingPossible
+ _objc_msgSend$resizableApplication
+ _objc_msgSend$resizingService:didUpdateStatus:
+ _objc_msgSend$simulateCaptureLaunchFromSource:bundleIdentifier:completion:
+ _objc_msgSend$unavailabilityReasons
- ___block_descriptor_48_e8_32s40w_e29_v16?0"BSServiceConnection"8lw40l8s32l8
CStrings:
+ "<%@: %p; resizingPossible: %d; unavailabilityReasons: %@; resizableApplication: %@>"
+ "DeviceUnsupported"
+ "Initializing"
+ "Landscape"
+ "LegacyApplication"
+ "NSString * _Nullable SBSAppResizingUnavailabilityReasonNameForReason(SBSAppResizingUnavailabilityReasons)"
+ "NoApplication"
+ "Other"
+ "SBSAppResizingService: %{public}@"
+ "SBSAppResizingService: committed resolvedSize: %{public}@"
+ "SBSAppResizingService: interrupted"
+ "SBSAppResizingService: minSize: %{public}@; maxSize: %{public}@"
+ "SBSAppResizingService: server ended resizing"
+ "SBSAppResizingServiceStatus.m"
+ "SBSCaptureLaunchSimulationErrorDomain"
+ "SBSLockScreenService: error from request to simulate capture launch : %@"
+ "SBSLockScreenService: failed request to simulate capture launch (no remoteTarget)"
+ "UnderLock"
+ "called simulateCaptureLaunchFromSource:bundleIdentifier:completion: after invalidation"
+ "kResizableApplicationKey"
+ "kUnavailabilityReasonsKey"
+ "unhandled SBSAppResizingUnavailabilityReasons: %ld"

```
