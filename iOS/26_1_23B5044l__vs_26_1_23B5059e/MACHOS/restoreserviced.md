## restoreserviced

> `/usr/libexec/restoreserviced`

```diff

-38.0.0.0.0
-  __TEXT.__text: 0x13c90
-  __TEXT.__auth_stubs: 0xea0
-  __TEXT.__objc_stubs: 0x17c0
+41.0.0.0.0
+  __TEXT.__text: 0x13950
+  __TEXT.__auth_stubs: 0xe20
+  __TEXT.__objc_stubs: 0x1760
   __TEXT.__objc_methlist: 0xcac
   __TEXT.__const: 0xb7c
-  __TEXT.__cstring: 0x760f
+  __TEXT.__cstring: 0x74f7
   __TEXT.__oslogstring: 0x34d
   __TEXT.__gcc_except_tab: 0x218
-  __TEXT.__objc_methname: 0x17dc
+  __TEXT.__objc_methname: 0x17c1
   __TEXT.__objc_classname: 0x10f
   __TEXT.__objc_methtype: 0x789
-  __TEXT.__unwind_info: 0x570
-  __DATA_CONST.__auth_got: 0x760
-  __DATA_CONST.__got: 0x188
+  __TEXT.__unwind_info: 0x568
+  __DATA_CONST.__auth_got: 0x720
+  __DATA_CONST.__got: 0x180
   __DATA_CONST.__const: 0xc78
-  __DATA_CONST.__cfstring: 0x3720
+  __DATA_CONST.__cfstring: 0x3760
   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_classrefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x68
   __DATA_CONST.__objc_intobj: 0x30
   __DATA.__objc_const: 0x1340
-  __DATA.__objc_selrefs: 0x740
+  __DATA.__objc_selrefs: 0x730
   __DATA.__objc_ivar: 0xe0
   __DATA.__objc_data: 0x460
   __DATA.__data: 0x618

   - /usr/lib/libauthinstall.dylib
   - /usr/lib/libimage4.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2B45BF5F-78A4-3B90-B19D-E3C1EE740391
-  Functions: 502
-  Symbols:   294
-  CStrings:  1829
+  UUID: 6ABACE8F-3D30-3F20-8DB8-116EAC42E40A
+  Functions: 501
+  Symbols:   285
+  CStrings:  1826
 
Symbols:
+ _IOServiceGetMatchingServices
- _CFRunLoopAddSource
- _CFRunLoopGetCurrent
- _CFRunLoopRemoveSource
- _CFRunLoopRunInMode
- _IONotificationPortCreate
- _IONotificationPortDestroy
- _IONotificationPortGetRunLoopSource
- _IORegistryEntryCreateIterator
- _IOServiceAddMatchingNotification
- _kCFRunLoopDefaultMode
CStrings:
+ "%s(%@) entered\n"
+ "%s(%@) found %lu nodes\n"
+ "Banyan"
+ "BanyanUARP"
+ "caseInsensitiveCompare:"
- "Failed to create DT node for IODeviceTree\n"
- "Failed to create iterator for DeviceTree.\n"
- "Found %lu nodes in the device tree. Waiting some (small) amount of time for them to register as an IOSerivce\n"
- "Found only %d when we should have found %d\n"
- "IODeviceTree:/arm-io"
- "IOServiceAddMatchingNotification() failed with return %d"
- "IOServiceFirstMatch"
- "longLongValue"
- "numberWithLongLong:"
- "unsignedIntValue"

```
