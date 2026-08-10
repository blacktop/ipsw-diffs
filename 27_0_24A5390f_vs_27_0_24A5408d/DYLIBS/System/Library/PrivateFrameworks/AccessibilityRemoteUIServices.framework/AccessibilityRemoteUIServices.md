## AccessibilityRemoteUIServices

> `/System/Library/PrivateFrameworks/AccessibilityRemoteUIServices.framework/AccessibilityRemoteUIServices`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__DATA.__data`

```diff

-3237.1.0.0.0
-  __TEXT.__text: 0x4ff8
-  __TEXT.__objc_methlist: 0xb14
+3240.3.0.0.0
+  __TEXT.__text: 0x5148
+  __TEXT.__objc_methlist: 0xb64
   __TEXT.__const: 0x68
-  __TEXT.__gcc_except_tab: 0x54
-  __TEXT.__cstring: 0x4ef
-  __TEXT.__unwind_info: 0x1f8
+  __TEXT.__gcc_except_tab: 0x60
+  __TEXT.__cstring: 0x52b
+  __TEXT.__unwind_info: 0x200
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x198
+  __DATA_CONST.__const: 0x1a0
   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa00
+  __DATA_CONST.__objc_selrefs: 0xa40
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_arraydata: 0x18
-  __DATA_CONST.__got: 0x2f0
+  __DATA_CONST.__got: 0x2f8
   __AUTH_CONST.__const: 0x60
-  __AUTH_CONST.__cfstring: 0x6a0
-  __AUTH_CONST.__objc_const: 0xff8
+  __AUTH_CONST.__cfstring: 0x6c0
+  __AUTH_CONST.__objc_const: 0x1028
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x320
-  __DATA.__objc_ivar: 0x44
+  __DATA.__objc_ivar: 0x48
   __DATA.__data: 0x480
   __DATA.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 144
-  Symbols:   676
-  CStrings:  59
+  Functions: 148
+  Symbols:   692
+  CStrings:  60
 
Symbols:
+ +[AXRemoteViewServiceAdaptor stopHandlingHIDEventsForRemoteViewController:]
+ -[AXRConnectedDeviceViewController _stopHandlingHIDEvents]
+ -[AXRConnectedDeviceViewController _tearDownHIDEventHandling]
+ -[_AXRemoteNearbyDevicesViewController stopHandlingHIDEvents]
+ GCC_except_table37
+ GCC_except_table69
+ _AXRemoteViewServiceShouldStopHandlingHIDEventsNotification
+ _OBJC_CLASS_$_NSNotificationCenter
+ _OBJC_IVAR_$_AXRConnectedDeviceViewController._hasTornDownHIDEventHandling
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_AXRemoteViewServiceInterface
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AXRemoteViewServiceInterface
+ _objc_msgSend$_tearDownHIDEventHandling
+ _objc_msgSend$addObserver:selector:name:object:
+ _objc_msgSend$defaultCenter
+ _objc_msgSend$removeObserver:name:object:
+ _objc_msgSend$serviceViewControllerProxy
+ _objc_msgSend$stopHandlingHIDEvents
+ _objc_opt_respondsToSelector
- GCC_except_table35
- GCC_except_table67
CStrings:
+ "AXRemoteViewServiceShouldStopHandlingHIDEventsNotification"
```
