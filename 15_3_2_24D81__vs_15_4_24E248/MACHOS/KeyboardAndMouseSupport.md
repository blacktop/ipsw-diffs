## KeyboardAndMouseSupport

> `/System/Library/Frameworks/GameController.framework/Versions/A/Resources/KeyboardAndMouseSupport.bundle/Contents/MacOS/KeyboardAndMouseSupport`

```diff

-12.3.1.0.0
-  __TEXT.__text: 0x450c
-  __TEXT.__auth_stubs: 0x310
-  __TEXT.__objc_stubs: 0x800
-  __TEXT.__objc_methlist: 0x17c
+12.4.12.0.0
+  __TEXT.__text: 0x4040
+  __TEXT.__auth_stubs: 0x2e0
+  __TEXT.__objc_stubs: 0x880
+  __TEXT.__objc_methlist: 0x34c
   __TEXT.__const: 0x18
-  __TEXT.__objc_methname: 0x8bd
-  __TEXT.__objc_classname: 0xeb
-  __TEXT.__objc_methtype: 0x27f
-  __TEXT.__cstring: 0x36
-  __TEXT.__gcc_except_tab: 0x194
-  __TEXT.__oslogstring: 0x398
-  __TEXT.__unwind_info: 0x168
-  __DATA_CONST.__auth_got: 0x198
-  __DATA_CONST.__got: 0x3a8
-  __DATA_CONST.__const: 0x100
-  __DATA_CONST.__cfstring: 0x20
+  __TEXT.__objc_methname: 0xaa8
+  __TEXT.__objc_classname: 0x108
+  __TEXT.__objc_methtype: 0x356
+  __TEXT.__cstring: 0x63
+  __TEXT.__gcc_except_tab: 0x134
+  __TEXT.__oslogstring: 0x1d1
+  __TEXT.__unwind_info: 0x188
+  __DATA_CONST.__auth_got: 0x180
+  __DATA_CONST.__got: 0x408
+  __DATA_CONST.__const: 0xd0
+  __DATA_CONST.__cfstring: 0xa0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x30
+  __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_classrefs: 0x98
+  __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
-  __DATA.__objc_const: 0x918
-  __DATA.__objc_selrefs: 0x258
-  __DATA.__objc_ivar: 0x34
+  __DATA_CONST.__objc_intobj: 0x48
+  __DATA.__objc_const: 0xa88
+  __DATA.__objc_selrefs: 0x350
+  __DATA.__objc_ivar: 0x44
   __DATA.__objc_data: 0xa0
-  __DATA.__data: 0x240
+  __DATA.__data: 0x2a0
   __DATA.__bss: 0x10
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/Carbon.framework/Versions/A/Carbon

   - /System/Library/PrivateFrameworks/GameControllerFoundation.framework/Versions/A/GameControllerFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C14A3384-2826-343B-B16D-F36E5E285159
-  Functions: 81
-  Symbols:   412
-  CStrings:  190
+  UUID: 2E5B50F7-13A8-316E-8208-D60C85CF4630
+  Functions: 79
+  Symbols:   422
+  CStrings:  216
 
Symbols:
+ -[GCKeyboardAndMouseManagerImpl _onqueue_HIDServiceAdded:]
+ -[GCKeyboardAndMouseManagerImpl _onqueue_HIDServiceAdded:].cold.1
+ -[GCKeyboardAndMouseManagerImpl _onqueue_HIDServiceAdded:].cold.2
+ -[GCKeyboardAndMouseManagerImpl _onqueue_HIDServiceAdded:].cold.3
+ -[GCKeyboardAndMouseManagerImpl _onqueue_HIDServiceRemoved:]
+ -[GCKeyboardAndMouseManagerImpl _onqueue_HIDServiceRemoved:].cold.1
+ -[GCKeyboardAndMouseManagerImpl _onqueue_HIDServiceRemoved:].cold.2
+ -[GCKeyboardAndMouseManagerImpl _onqueue_removeMouse:].cold.1
+ -[GCKeyboardAndMouseManagerImpl activateWithSession:environment:]
+ -[GCKeyboardAndMouseManagerImpl awakeWithSession:environment:]
+ -[GCKeyboardAndMouseManagerImpl initWithDeviceSessionConfiguration:queue:environment:]
+ -[GCKeyboardAndMouseManagerImpl invalidateWithSession:environment:]
+ -[GCKeyboardAndMouseManagerImpl keyboards]
+ -[GCKeyboardAndMouseManagerImpl matchingHIDServiceAttributes]
+ -[GCKeyboardAndMouseManagerImpl servicesDidChange:withAddedServices:removedServices:]
+ GCC_except_table11
+ GCC_except_table13
+ GCC_except_table2
+ GCC_except_table21
+ GCC_except_table3
+ GCC_except_table31
+ OBJC_IVAR_$_GCKeyboardAndMouseManagerImpl._clientQueue
+ OBJC_IVAR_$_GCKeyboardAndMouseManagerImpl._hidEventSource
+ OBJC_IVAR_$_GCKeyboardAndMouseManagerImpl._hidServiceProviding
+ OBJC_IVAR_$_GCKeyboardAndMouseManagerImpl._monitorKeyboards
+ OBJC_IVAR_$_GCKeyboardAndMouseManagerImpl._monitorMice
+ OBJC_IVAR_$_GCKeyboardAndMouseManagerImpl._sessionQueue
+ _GCLookupService
+ _OBJC_CLASS_$_NSConstantIntegerNumber
+ _OBJC_CLASS_$_NSDictionary
+ _OBJC_CLASS_$_NSMutableSet
+ _OBJC_CLASS_$__GCCurrentApplicationForegroundMonitor
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ __OBJC_$_CATEGORY_INSTANCE_METHODS__GCKeyboardEventImpl_$_CGEvent
+ __OBJC_$_PROP_LIST_GCHIDSystemServiceProviding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_GCHIDSystemServiceProviding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_GCHIDSystemServiceProviding
+ __OBJC_$_PROTOCOL_REFS_GCHIDSystemServiceProviding
+ __OBJC_CLASS_PROTOCOLS_$_GCKeyboardAndMouseManagerImpl
+ __OBJC_LABEL_PROTOCOL_$_GCHIDSystemServiceProviding
+ __OBJC_PROTOCOL_$_GCHIDSystemServiceProviding
+ __OBJC_PROTOCOL_REFERENCE_$_GCHIDSystemServiceProviding
+ ___65-[GCKeyboardAndMouseManagerImpl activateWithSession:environment:]_block_invoke
+ ___85-[GCKeyboardAndMouseManagerImpl servicesDidChange:withAddedServices:removedServices:]_block_invoke
+ ___NSArray0__struct
+ ___block_descriptor_56_e8_32s40s48s_e5_v8?0l
+ ___copy_helper_block_e8_32s40s48s
+ ___destroy_helper_block_e8_32s40s48s
+ _dispatch_sync
+ _gc_log_keyboard_and_mouse.cold.1
+ _objc_msgSend$arrayWithObjects:count:
+ _objc_msgSend$clientQueue
+ _objc_msgSend$dictionaryWithObjects:forKeys:count:
+ _objc_msgSend$didChangeValueForKey:withSetMutation:usingObjects:
+ _objc_msgSend$hidEventSource
+ _objc_msgSend$hidEventSystemQueue
+ _objc_msgSend$registerServicesChangedObserver:notifyExisting:
+ _objc_msgSend$services
+ _objc_msgSend$setWithObject:
+ _objc_msgSend$stringPropertyForKey:
+ _objc_msgSend$unregisterServicesChangedObserver:notifyExisting:
+ _objc_msgSend$willChangeValueForKey:withSetMutation:usingObjects:
- -[GCKeyboardAndMouseManagerImpl _onqueue_publishKeyboard:]
- -[GCKeyboardAndMouseManagerImpl _onqueue_publishMouse:]
- -[GCKeyboardAndMouseManagerImpl _onqueue_unpublishKeyboard:]
- -[GCKeyboardAndMouseManagerImpl _onqueue_unpublishMouse:]
- -[GCKeyboardAndMouseManagerImpl addDeviceWithServiceRef:]
- -[GCKeyboardAndMouseManagerImpl addDeviceWithServiceRef:].cold.1
- -[GCKeyboardAndMouseManagerImpl addDeviceWithServiceRef:].cold.2
- -[GCKeyboardAndMouseManagerImpl coalescedKeyboard]
- -[GCKeyboardAndMouseManagerImpl currentMouse]
- -[GCKeyboardAndMouseManagerImpl handleHIDEvent:]
- -[GCKeyboardAndMouseManagerImpl initWithQueue:]
- -[GCKeyboardAndMouseManagerImpl removeDeviceWithServiceRef:]
- -[GCKeyboardAndMouseManagerImpl setCurrentMouse:]
- -[GCKeyboardAndMouseManagerImpl setCurrentMouse:].cold.1
- -[GCKeyboardAndMouseManagerImpl setCurrentMouse:].cold.2
- -[GCKeyboardAndMouseManagerImpl updateCurrentMouseAfterDisconnecting:]
- GCC_except_table0
- GCC_except_table14
- GCC_except_table18
- GCC_except_table24
- GCC_except_table28
- GCC_except_table32
- OBJC_IVAR_$_GCKeyboardAndMouseManagerImpl._currentMouse
- OBJC_IVAR_$_GCKeyboardAndMouseManagerImpl._devicesQueue
- _GCKeyboardDidConnectNotification
- _GCKeyboardDidDisconnectNotification
- _GCMouseDidBecomeCurrentNotification
- _GCMouseDidConnectNotification
- _GCMouseDidDisconnectNotification
- _GCMouseDidStopBeingCurrentNotification
- _IOHIDServiceClientCopyProperty
- _OBJC_CLASS_$_GCHIDServiceInfo
- _OBJC_CLASS_$_NSNotificationCenter
- _OBJC_CLASS_$__GCControllerManager
- __OBJC_$_INSTANCE_METHODS__GCKeyboardEventImpl(CGEvent)
- ___47-[GCKeyboardAndMouseManagerImpl initWithQueue:]_block_invoke
- ___55-[GCKeyboardAndMouseManagerImpl _onqueue_publishMouse:]_block_invoke
- ___57-[GCKeyboardAndMouseManagerImpl _onqueue_unpublishMouse:]_block_invoke
- ___57-[GCKeyboardAndMouseManagerImpl addDeviceWithServiceRef:]_block_invoke
- ___57-[GCKeyboardAndMouseManagerImpl addDeviceWithServiceRef:]_block_invoke_2
- ___58-[GCKeyboardAndMouseManagerImpl _onqueue_publishKeyboard:]_block_invoke
- ___60-[GCKeyboardAndMouseManagerImpl _onqueue_unpublishKeyboard:]_block_invoke
- ___60-[GCKeyboardAndMouseManagerImpl removeDeviceWithServiceRef:]_block_invoke
- ___60-[GCKeyboardAndMouseManagerImpl removeDeviceWithServiceRef:]_block_invoke_2
- ___block_descriptor_40_e8_32s_e5_v8?0l
- ___block_descriptor_48_e8_32s40s_e5_v8?0l
- ___copy_helper_block_e8_32s
- ___copy_helper_block_e8_32s40s
- ___destroy_helper_block_e8_32s
- __dispatch_main_q
- _currentProcessIsGameControllerDaemon
- _dispatch_async
- _dispatch_barrier_async
- _dispatch_get_current_queue
- _objc_msgSend$currentMouse
- _objc_msgSend$defaultCenter
- _objc_msgSend$initWithService:
- _objc_msgSend$initWithService:queue:
- _objc_msgSend$lastEventTimestamp
- _objc_msgSend$mice
- _objc_msgSend$postNotificationName:object:userInfo:
- _objc_msgSend$setCurrentMouse:
CStrings:
+ "@\"<GCHIDSystemServiceInfo>\"24@0:8Q16"
+ "@\"<GCHIDSystemServiceProviding>\""
+ "@\"NSObject<OS_dispatch_queue>\"16@0:8"
+ "@\"NSSet\"16@0:8"
+ "@\"_GCHIDEventSubject\""
+ "@24@0:8Q16"
+ "@28@0:8@?16B24"
+ "@28@0:8@?<v@?@\"NSSet\"@\"NSArray\"@\"NSArray\">16B24"
+ "@40@0:8@16@24@32"
+ "B"
+ "DeviceUsage"
+ "DeviceUsagePage"
+ "GCHIDSystemServiceProviding"
+ "T@\"NSObject<OS_dispatch_queue>\",R"
+ "T@\"NSSet\",R"
+ "_clientQueue"
+ "_hidEventSource"
+ "_hidServiceProviding"
+ "_monitorKeyboards"
+ "_monitorMice"
+ "_sessionQueue"
+ "activateWithSession:environment:"
+ "arrayWithObjects:count:"
+ "awakeWithSession:environment:"
+ "clientQueue"
+ "dictionaryWithObjects:forKeys:count:"
+ "didChangeValueForKey:withSetMutation:usingObjects:"
+ "hidEventSource"
+ "hidEventSystemQueue"
+ "i"
+ "initWithDeviceSessionConfiguration:queue:environment:"
+ "invalidateWithSession:environment:"
+ "keyboards"
+ "matchingHIDServiceAttributes"
+ "queue"
+ "registerServicesChangedHandler:notifyExisting:"
+ "registerServicesChangedObserver:notifyExisting:"
+ "serviceForRegistryID:"
+ "services"
+ "servicesDidChange:withAddedServices:removedServices:"
+ "setWithObject:"
+ "stringPropertyForKey:"
+ "unregisterServicesChangedObserver:notifyExisting:"
+ "v28@0:8@\"<GCHIDSystemServiceMatchObserver>\"16B24"
+ "v28@0:8@16B24"
+ "v32@0:8@16@24"
+ "v40@0:8@16@24@32"
+ "willChangeValueForKey:withSetMutation:usingObjects:"
- "#WARNING Ignoring added HID Service because it returned an invalid registryID:\n%@"
- "#WARNING Ignoring removed HID Service because it returned an invalid registryID:\n%@"
- "@\"GCMouse\""
- "@24@0:8@16"
- "B24@0:8^{__IOHIDEvent=}16"
- "B24@0:8^{__IOHIDServiceClient=}16"
- "Posting GCKeyboardDidConnectNotification for keyboard."
- "Posting GCKeyboardDidDisconnectNotification for keyboard."
- "Posting GCMouseDidBecomeCurrent for %@"
- "Posting GCMouseDidConnectNotification for %@."
- "Posting GCMouseDidDisconnectNotification for %@."
- "Posting GCMouseDidStopBeingCurrent for %@"
- "T@\"GCKeyboard\",R,V_coalescedKeyboard"
- "T@\"GCMouse\",R"
- "_currentMouse"
- "_devicesQueue"
- "addDeviceWithServiceRef:"
- "currentMouse"
- "defaultCenter"
- "handleHIDEvent:"
- "initWithQueue:"
- "initWithService:"
- "initWithService:queue:"
- "lastEventTimestamp"
- "postNotificationName:object:userInfo:"
- "removeDeviceWithServiceRef:"
- "setCurrentMouse:"
- "v24@0:8^{__IOHIDServiceClient=}16"

```
