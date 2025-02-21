## GamepadHIDServiceFilter

> `/System/Library/HIDPlugins/ServiceFilters/GamepadHIDServiceFilter.plugin/GamepadHIDServiceFilter`

```diff

-12.3.1.0.0
-  __TEXT.__text: 0x2154
-  __TEXT.__auth_stubs: 0x300
-  __TEXT.__objc_stubs: 0x460
+12.4.10.0.0
+  __TEXT.__text: 0x2388
+  __TEXT.__auth_stubs: 0x330
+  __TEXT.__objc_stubs: 0x580
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x1d8
-  __TEXT.__const: 0x30
+  __TEXT.__objc_methlist: 0x5ac
+  __TEXT.__const: 0x40
   __TEXT.__gcc_except_tab: 0x3c
-  __TEXT.__cstring: 0x1f6
-  __TEXT.__oslogstring: 0x27d
-  __TEXT.__objc_methname: 0xbd1
-  __TEXT.__objc_classname: 0x243
-  __TEXT.__objc_methtype: 0x841
+  __TEXT.__cstring: 0x209
+  __TEXT.__oslogstring: 0x291
+  __TEXT.__objc_methname: 0xcca
+  __TEXT.__objc_classname: 0x27f
+  __TEXT.__objc_methtype: 0x8b5
   __TEXT.__unwind_info: 0x110
-  __DATA_CONST.__auth_got: 0x190
-  __DATA_CONST.__got: 0x88
-  __DATA_CONST.__const: 0x218
-  __DATA_CONST.__cfstring: 0x240
+  __DATA_CONST.__auth_got: 0x1a8
+  __DATA_CONST.__got: 0x90
+  __DATA_CONST.__const: 0x1f8
+  __DATA_CONST.__cfstring: 0x260
   __DATA_CONST.__objc_classlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x88
+  __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x70
+  __DATA_CONST.__objc_protorefs: 0x80
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA.__objc_const: 0xda8
-  __DATA.__objc_selrefs: 0x240
-  __DATA.__objc_ivar: 0x3c
+  __DATA.__objc_const: 0x7c0
+  __DATA.__objc_selrefs: 0x3b0
+  __DATA.__objc_ivar: 0x44
   __DATA.__objc_data: 0x50
-  __DATA.__data: 0x660
-  __DATA.__bss: 0xb9
+  __DATA.__data: 0x720
+  __DATA.__bss: 0xa9
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/GameControllerFoundation.framework/GameControllerFoundation
   - /System/Library/PrivateFrameworks/HID.framework/HID
-  - /System/Library/PrivateFrameworks/MobileBluetooth.framework/MobileBluetooth
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 83
-  Symbols:   75
-  CStrings:  276
+  Functions: 95
+  Symbols:   81
+  CStrings:  294
 
Symbols:
+ _IOHIDEventSetEventFlags
+ _IORegistryEntrySearchCFProperty
+ _OBJC_CLASS_$_HIDEvent
+ _hexStringFromByteArray
+ _isPartnerSupportEnabled
+ _objc_opt_class
+ _objc_opt_isKindOfClass
- _objc_retain_x3
CStrings:
+ "\x02\x12\x11\x12\x11"
+ "Authenticated"
+ "GCIdleServiceClientInterface"
+ "GCIdleServiceServerInterface"
+ "IOService"
+ "_authenticated"
+ "_serviceID"
+ "appendEvent:"
+ "boolValue"
+ "connectToIdleServiceWithClient:reply:"
+ "dispatchEvent:"
+ "doubleValueForField:"
+ "initWithService: %@, registryID = %llu, authenticated = %@"
+ "initWithType:timestamp:senderID:"
+ "requestIdleDiconnect:"
+ "serviceID"
+ "setDoubleValue:forField:"
+ "setIntegerValue:forField:"
+ "timestamp"
+ "v24@0:8@\"NSString\"16"
+ "v32@0:8@\"<GCIdleServiceClientInterface>\"16@?<v@?@\"<GCIdleServiceServerInterface>\"@\"NSError\">24"
+ "\xc3"
- "\x02\x12\x14"
- "initWithService: %@, registryID = %llu"
- "\xa3"

```
