## usbaudiod

> `/System/Library/Audio/Plug-Ins/usbaudio.bundle/usbaudiod`

```diff

-802.17.0.0.0
-  __TEXT.__text: 0x112818
+802.30.0.0.0
+  __TEXT.__text: 0x11374c
   __TEXT.__auth_stubs: 0x19e0
   __TEXT.__objc_stubs: 0x220
   __TEXT.__init_offsets: 0x8
-  __TEXT.__objc_methlist: 0x7fc
-  __TEXT.__const: 0xbae2
-  __TEXT.__cstring: 0x7f42
-  __TEXT.__swift5_typeref: 0x2d36
+  __TEXT.__objc_methlist: 0x804
+  __TEXT.__const: 0xbaf2
+  __TEXT.__cstring: 0x7fb2
+  __TEXT.__swift5_typeref: 0x2d2e
   __TEXT.__swift5_entry: 0x8
   __TEXT.__gcc_except_tab: 0x300
   __TEXT.__objc_classname: 0x81
   __TEXT.__objc_methname: 0x1886
   __TEXT.__objc_methtype: 0x7fd
-  __TEXT.__oslogstring: 0x1e3
-  __TEXT.__constg_swiftt: 0x5108
+  __TEXT.__oslogstring: 0x210
+  __TEXT.__constg_swiftt: 0x5144
   __TEXT.__swift5_reflstr: 0x51b6
   __TEXT.__swift5_fieldmd: 0x6664
   __TEXT.__swift5_builtin: 0xdac

   __TEXT.__swift5_mpenum: 0x4c
   __TEXT.__swift_as_entry: 0x4
   __TEXT.__swift_as_ret: 0x8
-  __TEXT.__unwind_info: 0x36a0
+  __TEXT.__unwind_info: 0x36e0
   __TEXT.__eh_frame: 0x5d20
   __DATA_CONST.__auth_got: 0xd00
   __DATA_CONST.__got: 0x3e0
-  __DATA_CONST.__auth_ptr: 0xaf0
-  __DATA_CONST.__const: 0xdf18
+  __DATA_CONST.__auth_ptr: 0xaf8
+  __DATA_CONST.__const: 0xded8
   __DATA_CONST.__cfstring: 0xe0
   __DATA_CONST.__objc_classlist: 0x230
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x20
-  __DATA.__objc_const: 0x4e40
+  __DATA.__objc_const: 0x4e20
   __DATA.__objc_selrefs: 0x840
   __DATA.__objc_ivar: 0x68
-  __DATA.__objc_data: 0x2550
-  __DATA.__data: 0x5690
-  __DATA.__common: 0x200
+  __DATA.__objc_data: 0x2548
+  __DATA.__data: 0x56c0
+  __DATA.__common: 0x1f8
   __DATA.__bss: 0x115e0
   - /System/Library/Frameworks/CoreAudio.framework/CoreAudio
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
   - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 0E9F3049-B755-318D-8B03-3FAA73687EF4
-  Functions: 4978
-  Symbols:   670
-  CStrings:  1283
+  UUID: 3FBC0D08-1B02-3CC7-9A71-87D6FBF03541
+  Functions: 4988
+  Symbols:   666
+  CStrings:  1284
 
Symbols:
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
CStrings:
+ " ADC3 device with an invalid Cluster. generating a default Cluster"
+ " because it is not the first audio function"
+ " in USBDevice.init"
+ " retrieving string "
+ "Ignoring usbInterface with number "
+ "current microframe timestamp calcError %lld = ns %lld, uf1 x%llx, uf2 x%llx, ts %lld c %lld\n"
+ "timestampStream"
- ") already enumerated"
- "Device with interface "
- "Unknown Multi-Function USB Audio Device"
- "current microframe timestamp calcError ns %lld\n"
- "timeStampStream"
- "usbHostObjectEntryID"

```
