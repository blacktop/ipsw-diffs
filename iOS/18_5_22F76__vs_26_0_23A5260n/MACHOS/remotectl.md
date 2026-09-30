## remotectl

> `/usr/libexec/remotectl`

```diff

-172.100.9.0.0
-  __TEXT.__text: 0x1a214
-  __TEXT.__auth_stubs: 0x1a40
-  __TEXT.__objc_stubs: 0xc0
+196.0.0.0.0
+  __TEXT.__text: 0x19e5c
+  __TEXT.__auth_stubs: 0x1a80
+  __TEXT.__objc_stubs: 0x1c0
   __TEXT.__objc_methlist: 0x104
   __TEXT.__const: 0x7be
   __TEXT.__gcc_except_tab: 0x2b4
-  __TEXT.__cstring: 0x2024
+  __TEXT.__cstring: 0x20b4
   __TEXT.__objc_classname: 0x35
   __TEXT.__oslogstring: 0x12c4
-  __TEXT.__objc_methname: 0x2c8
+  __TEXT.__objc_methname: 0x38c
   __TEXT.__swift5_typeref: 0x238
   __TEXT.__constg_swiftt: 0x2d8
   __TEXT.__swift5_builtin: 0x50

   __TEXT.__swift5_mpenum: 0x34
   __TEXT.__swift5_capture: 0x10
   __TEXT.__objc_methtype: 0xad
-  __TEXT.__unwind_info: 0x518
-  __TEXT.__eh_frame: 0x73c
-  __DATA_CONST.__auth_got: 0xd30
-  __DATA_CONST.__got: 0x260
-  __DATA_CONST.__auth_ptr: 0x218
-  __DATA_CONST.__const: 0x6e0
-  __DATA_CONST.__cfstring: 0x20
+  __TEXT.__unwind_info: 0x510
+  __TEXT.__eh_frame: 0x704
+  __DATA_CONST.__auth_got: 0xd50
+  __DATA_CONST.__got: 0x278
+  __DATA_CONST.__auth_ptr: 0x208
+  __DATA_CONST.__const: 0x758
+  __DATA_CONST.__cfstring: 0xa0
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA.__objc_const: 0x5d8
-  __DATA.__objc_selrefs: 0x140
+  __DATA.__objc_selrefs: 0x180
   __DATA.__objc_data: 0x140
   __DATA.__data: 0x6a0
   __DATA.__bss: 0x810

   - /usr/lib/swift/libswiftSystem.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_errno.dylib
-  - /usr/lib/swift/libswift_math.dylib
-  - /usr/lib/swift/libswift_signal.dylib
-  - /usr/lib/swift/libswift_stdio.dylib
-  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: D8C4BB3E-A79C-37E9-B8BB-86810139A390
-  Functions: 366
-  Symbols:   571
-  CStrings:  442
+  UUID: A9CBF8EE-176D-302D-BD08-C19F04987F0B
+  Functions: 364
+  Symbols:   577
+  CStrings:  463
 
Symbols:
+ _$sSs8UTF8ViewV8distance4from2toSiSS5IndexV_AGtF
+ _$ss11_StringGutsV16_foreignCopyUTF84intoSiSgSrys5UInt8VG_tF
+ _$ss20__StaticArrayStorageCN
+ _OBJC_CLASS_$_NSDictionary
+ _OBJC_CLASS_$_NSMutableDictionary
+ _OBJC_CLASS_$_NSString
+ __swiftImmortalRefCount
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ __xpc_type_dictionary
+ __xpc_type_string
+ _objc_alloc
+ _objc_alloc_init
+ _objc_release_x28
+ _remote_device_copy_local_services
+ _swift_setDeallocating
+ _xpc_dictionary_apply
- _$ss11_StringGutsV8copyUTF84intoSiSgSrys5UInt8VG_tF
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftunistd
- _objc_retain_x25
- _remote_device_copy_local_service_names
- _swift_bridgeObjectRelease_n
- _swift_bridgeObjectRetain_n
CStrings:
+ "%s\n"
+ "B24@?0r*8@\"NSObject<OS_xpc_object>\"16"
+ "InterfaceName"
+ "UniqueDeviceID"
+ "assertion failure: \"local_services != ((void*)0) && xpc_get_type(local_services) == (&_xpc_type_dictionary)\" -> %llu"
+ "copy"
+ "dataWithJSONObject:options:error:"
+ "dictionaryWithObjects:forKeys:count:"
+ "dump-local-ports"
+ "initWithData:encoding:"
+ "interface-name"
+ "local-services"
+ "localizedDescription"
+ "objectForKeyedSubscript:"
+ "setObject:forKeyedSubscript:"
+ "stringWithUTF8String:"
+ "udid"
+ "usage: remotectl dump-local-ports\n"
- "assertion failure: \"local_services != ((void*)0) && xpc_get_type(local_services) == (&_xpc_type_array)\" -> %llu"

```
