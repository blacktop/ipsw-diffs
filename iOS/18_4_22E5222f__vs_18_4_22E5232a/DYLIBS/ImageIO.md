## ImageIO

> `/System/Library/Frameworks/ImageIO.framework/ImageIO`

```diff

-2661.4.7.0.0
-  __TEXT.__text: 0x465030
-  __TEXT.__auth_stubs: 0x4110
+2661.4.9.1.1
+  __TEXT.__text: 0x465344
+  __TEXT.__auth_stubs: 0x4120
   __TEXT.__objc_methlist: 0xb58
-  __TEXT.__const: 0xb89f8
-  __TEXT.__gcc_except_tab: 0x1fa20
-  __TEXT.__cstring: 0x7bd8b
+  __TEXT.__const: 0xb8a08
+  __TEXT.__gcc_except_tab: 0x1fa84
+  __TEXT.__cstring: 0x7c0b2
   __TEXT.__oslogstring: 0x17
   __TEXT.__ustring: 0x20
-  __TEXT.__unwind_info: 0xd740
+  __TEXT.__unwind_info: 0xd758
   __TEXT.__eh_frame: 0x510
   __TEXT.__objc_classname: 0xce
   __TEXT.__objc_methname: 0x2a12

   __DATA_CONST.__objc_selrefs: 0xa48
   __DATA_CONST.__objc_superrefs: 0x30
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__auth_got: 0x20a0
+  __AUTH_CONST.__auth_got: 0x20a8
   __AUTH_CONST.__auth_ptr: 0xa0
   __AUTH_CONST.__const: 0x3cde0
   __AUTH_CONST.__cfstring: 0xda80

   __AUTH.__data: 0x1d0
   __DATA.__objc_ivar: 0x84
   __DATA.__data: 0x2cf0
-  __DATA.__bss: 0x12800
+  __DATA.__bss: 0x12820
   __DATA.__common: 0x7ec4
   __DATA_DIRTY.__data: 0x170
   __DATA_DIRTY.__crash_info: 0x40
   __DATA_DIRTY.__common: 0xd33
-  __DATA_DIRTY.__bss: 0x2610
+  __DATA_DIRTY.__bss: 0x2600
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/ColorSync.framework/ColorSync
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libexpat.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 13880
-  Symbols:   16810
-  CStrings:  12721
+  Functions: 13887
+  Symbols:   16818
+  CStrings:  12732
 
Symbols:
+ _mach_port_mod_refs
CStrings:
+ "    AppleJPEGReadPlugin - offset: %ld   size: %d\n"
+ "    AppleJPEGReadPlugin::initialize   jpegOffset: %d   jpegLength: %d\n"
+ "    HEIFReadPlugin(JPEG) - offset: %ld   size: %d\n"
+ "    calling appleJPEGDecodeOpen: NOT seeking to jpegOffset: %d\n"
+ "    calling appleJPEGDecodeOpen: seeking to jpegOffset: %d\n"
+ "(NULL)"
+ "(zero size)"
+ "*** ERROR: CGImageCreateFlexRangeMetadata failed to create gainmapdata (err=%d)\n"
+ "*** ERROR: CGImagePluginInitThumbJPEGAtOffsetWithOptions is called with offset: %ld   size: %ld\n"
+ "*** ERROR: applejpeg_decode_open_file returned: %d '%s'    (jpegOffset: %d   jpegSize: %d) fileSize: %ld\n"
+ "*** ERROR: mach_make_memory_entry_64: %s\n"
+ "*** ERROR: ❌ '%s' OWNERLESS SERVER ALLOCATION: %s, %llu bytes\n"
+ "*** ERROR: ❌ '%s' mach_memory_entry_ownership error: [%d] %s  owner:%d  '%s' %ld bytes\n"
+ "iio_xpc_msg_name"
+ "offset:%ld  size:%ld"
+ "|"
+ "|  |"
+ "☀️  HEIFReadPlugin::HEIFReadPlugin   [%p]\n"
+ "☀️  HEIFReadPlugin::~HEIFReadPlugin  ••• [%p]\n"
+ "☀️  no apply / no tone mapping / no compute stats [%p]\n"
+ "❌ ERROR: IIO_CreateIdentityToken should not be called from the ImageIOXPCService\n"
+ "❌ ERROR: failed to create token. 'task_create_identity_token' returned %ld"
+ "❌ ERROR: kCGImageBlockFormatBGRx8 is called for %d-bpp (%d-bpc) image (rdar://143602439)\n"
- "%02X "
- "%c"
- "(zero-length)"
- "*** ERROR: OWNERLESS SERVER ALLOCATION: %s, %llu bytes"
- "*** ERROR: applejpeg_decode_open_file returned: %d '%s'\n"
- "*** ERROR: kCGImageBlockFormatBGRx8 is called for %d-bpp (%d-bpc) image\n"
- "*** ERROR: mach_make_memory_entry_64: %s"
- "*** ERROR: mach_memory_entry_ownership: %s"
- "*** ERROR: task_create_identity_token: %s"
- "[%p]-(%ld) %s"
- "saveDataToXPCObject_block_invoke"
- "|x                                              |  |                |"

```
