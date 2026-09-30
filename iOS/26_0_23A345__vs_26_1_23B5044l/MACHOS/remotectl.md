## remotectl

> `/usr/libexec/remotectl`

```diff

-202.0.1.0.0
-  __TEXT.__text: 0x19e5c
-  __TEXT.__auth_stubs: 0x1a80
-  __TEXT.__objc_stubs: 0x1c0
+202.40.9.0.0
+  __TEXT.__text: 0x1a0a4
+  __TEXT.__auth_stubs: 0x1aa0
+  __TEXT.__objc_stubs: 0x220
   __TEXT.__objc_methlist: 0x104
   __TEXT.__const: 0x7be
-  __TEXT.__gcc_except_tab: 0x2b4
-  __TEXT.__cstring: 0x20b4
+  __TEXT.__gcc_except_tab: 0x2e4
+  __TEXT.__cstring: 0x2144
   __TEXT.__objc_classname: 0x35
   __TEXT.__oslogstring: 0x12c4
-  __TEXT.__objc_methname: 0x38c
+  __TEXT.__objc_methname: 0x3c3
   __TEXT.__swift5_typeref: 0x238
   __TEXT.__constg_swiftt: 0x2d8
   __TEXT.__swift5_builtin: 0x50

   __TEXT.__swift5_mpenum: 0x34
   __TEXT.__swift5_capture: 0x10
   __TEXT.__objc_methtype: 0xad
-  __TEXT.__unwind_info: 0x510
+  __TEXT.__unwind_info: 0x4f8
   __TEXT.__eh_frame: 0x704
-  __DATA_CONST.__auth_got: 0xd50
-  __DATA_CONST.__got: 0x278
+  __DATA_CONST.__auth_got: 0xd60
+  __DATA_CONST.__got: 0x280
   __DATA_CONST.__auth_ptr: 0x208
   __DATA_CONST.__const: 0x738
-  __DATA_CONST.__cfstring: 0xa0
+  __DATA_CONST.__cfstring: 0x140
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA.__objc_const: 0x5d8
-  __DATA.__objc_selrefs: 0x180
+  __DATA.__objc_selrefs: 0x198
   __DATA.__objc_data: 0x140
   __DATA.__data: 0x6a0
   __DATA.__bss: 0x810

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 2A0DAC55-5C59-3A8C-84E5-9492550AE068
-  Functions: 364
-  Symbols:   573
-  CStrings:  463
+  UUID: 4B4C0A54-15CE-3D4D-A253-B385CF10283B
+  Functions: 359
+  Symbols:   576
+  CStrings:  483
 
Symbols:
+ _OBJC_CLASS_$_NSMutableArray
+ _fputc
+ _remote_device_copy_device_matching
+ _xpc_dictionary_create_empty
+ _xpc_dictionary_set_string
- _remote_device_copy_device_with_name
- _remote_device_copy_device_with_uuid
CStrings:
+ "\nDevice Types:\n"
+ " and "
+ ", "
+ "AvailableService"
+ "DeviceName"
+ "DeviceType"
+ "DeviceUUID"
+ "Invalid device type\n"
+ "Unable to find device with %@"
+ "addObject:"
+ "componentsJoinedByString:"
+ "name '%s'"
+ "service '%s'"
+ "stringWithFormat:"
+ "t:"
+ "type '%s'"
+ "usage: remotectl get-property [-t type] (name|uuid|trait) [service] property\n"
+ "usage: remotectl show [-t type] (name|uuid|trait)\n"
- "Unable to find device \"%s\".\n"
- "usage: remotectl get-property (type|name|uuid|trait) [service] property\n"
- "usage: remotectl show (type|name|uuid|trait)\n"

```
