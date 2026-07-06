## libCoreRepairState.dylib

> `/usr/lib/libCoreRepairState.dylib`

```diff

-  __TEXT.__text: 0x14ff4
-  __TEXT.__objc_methlist: 0xc80
-  __TEXT.__const: 0x173
-  __TEXT.__cstring: 0xb3f
-  __TEXT.__oslogstring: 0x179b
+  __TEXT.__text: 0x1787c
+  __TEXT.__objc_methlist: 0xe70
+  __TEXT.__const: 0x18b
+  __TEXT.__cstring: 0xbc7
+  __TEXT.__oslogstring: 0x1ce5
   __TEXT.__gcc_except_tab: 0x44
-  __TEXT.__unwind_info: 0x398
+  __TEXT.__unwind_info: 0x418
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x48
-  __DATA_CONST.__objc_classlist: 0x68
+  __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb90
+  __DATA_CONST.__objc_selrefs: 0xc90
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x40
+  __DATA_CONST.__objc_superrefs: 0x50
   __DATA_CONST.__objc_arraydata: 0x1d0
-  __DATA_CONST.__got: 0x1d0
-  __AUTH_CONST.__const: 0xf0
-  __AUTH_CONST.__cfstring: 0x1740
-  __AUTH_CONST.__objc_const: 0xdb0
+  __DATA_CONST.__got: 0x1f0
+  __AUTH_CONST.__const: 0x120
+  __AUTH_CONST.__cfstring: 0x1800
+  __AUTH_CONST.__objc_const: 0x10d8
   __AUTH_CONST.__objc_arrayobj: 0x228
-  __AUTH_CONST.__objc_intobj: 0x48
+  __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x410
-  __DATA.__objc_ivar: 0x7c
+  __AUTH.__objc_data: 0x500
+  __DATA.__objc_ivar: 0x9c
   __DATA.__data: 0x60
   __DATA.__bss: 0xc0
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libamsupport.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 418
-  Symbols:   204
-  CStrings:  579
+  Functions: 482
+  Symbols:   218
+  CStrings:  635
 
Sections:
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __DATA.__data : content changed
Symbols:
+ _CFBooleanGetTypeID
+ _CFBooleanGetValue
+ _CFGetTypeID
+ _IOConnectCallScalarMethod
+ _IOConnectCallStructMethod
+ _OBJC_CLASS_$_CRInputDeviceController
+ _OBJC_CLASS_$_CRInputDeviceManager
+ _OBJC_CLASS_$_CRSmcController
+ _OBJC_CLASS_$_NSThread
+ _OBJC_METACLASS_$_CRInputDeviceController
+ _OBJC_METACLASS_$_CRInputDeviceManager
+ _OBJC_METACLASS_$_CRSmcController
+ _dispatch_async
+ _dispatch_get_global_queue
CStrings:
+ "\""
+ "%@ smc force lid state returns with %d"
+ "%ld is force enabled: %d"
+ "%s force enabled keyboard returned %d"
+ "%s force enabled trackpad returned %d"
+ "%s force lid state returned %d"
+ "-[CRInputDeviceController dealloc]"
+ "AppleSMC"
+ "Closing SMC returns: %d"
+ "FIFO"
+ "Failed to %s force enable"
+ "Failed to %s force lid state"
+ "Failed to covert from valueBuffer to byteData"
+ "Failed to get HID report %ld, status:%03x"
+ "Failed to modify SMC override"
+ "Failed to modify keyboard override"
+ "Failed to modify trackpad override"
+ "Failed to open HID device"
+ "Failed to open HID for %ld. Retry: %d"
+ "Failed to open SMC port"
+ "Failed to open SMC, error: %d, retrying..."
+ "Failed to read SMC key %@, error: %d"
+ "Failed to set lid state"
+ "Failed to set report; status: %03x"
+ "Failed to write data to key %@, error: 0x%x"
+ "Has Unsealed Display"
+ "Has Unsealed LAS2"
+ "LAS!"
+ "MSLD"
+ "No LAS2"
+ "No info found for key '%s' (0x%X, 0x%X)\n"
+ "No need to enable input device"
+ "Process is not entitled"
+ "Read failed for key '%s' (0x%X, 0x%X)\n"
+ "SMC key(%@) reading failed, error: 0x%x"
+ "Successfully %s force enable"
+ "Try to open HID device %ld"
+ "Unexpected NULL value returned from SecTaskCreateFromSelf"
+ "Unknown input device type %ld"
+ "Write failed for key '%s' (0x%X, 0x%X)\n"
+ "Write succeed for key '%s', value returned = 0x%X"
+ "buffer overflow on string/key conversion"
+ "com.apple.private.corerepair.control-input-device"
+ "destination for key read does not match expected size (Key: '%s', Expected Size: %u, Supplied Size: %lu)\n"
+ "disable"
+ "enable"
+ "hidDevice chosen: %@"
+ "hidDevices found: %@"
+ "reset"
+ "set"

```
