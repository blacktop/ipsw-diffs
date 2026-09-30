## com.apple.Virtualization.VirtualMachine

> `/System/Library/Frameworks/Virtualization.framework/Versions/A/XPCServices/com.apple.Virtualization.VirtualMachine.xpc/Contents/MacOS/com.apple.Virtualization.VirtualMachine`

```diff

-210.4.4.0.0
-  __TEXT.__text: 0x314398
-  __TEXT.__auth_stubs: 0x29b0
+210.5.6.0.0
+  __TEXT.__text: 0x308c98
+  __TEXT.__auth_stubs: 0x29e0
   __TEXT.__objc_stubs: 0x1b80
-  __TEXT.__objc_methlist: 0x64
-  __TEXT.__const: 0x20b3c
-  __TEXT.__cstring: 0xcc9d
-  __TEXT.__gcc_except_tab: 0x26628
+  __TEXT.__objc_methlist: 0x240
+  __TEXT.__const: 0x21aa0
+  __TEXT.__cstring: 0xcd99
+  __TEXT.__dlopen_cstrs: 0x66
+  __TEXT.__gcc_except_tab: 0x2654c
   __TEXT.__objc_classname: 0xb2
   __TEXT.__objc_methname: 0x15a4
   __TEXT.__objc_methtype: 0x2ab
-  __TEXT.__oslogstring: 0x343d
-  __TEXT.__dlopen_cstrs: 0x66
-  __TEXT.__unwind_info: 0xbc40
-  __TEXT.__eh_frame: 0x1c0
-  __DATA_CONST.__auth_got: 0x14e8
-  __DATA_CONST.__got: 0x4c0
-  __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x19ba8
-  __DATA_CONST.__cfstring: 0x7a0
+  __TEXT.__oslogstring: 0x3503
+  __TEXT.__unwind_info: 0xc190
+  __TEXT.__eh_frame: 0x188
+  __DATA_CONST.__auth_got: 0x1500
+  __DATA_CONST.__got: 0x4d0
+  __DATA_CONST.__auth_ptr: 0x18
+  __DATA_CONST.__const: 0x1a4b0
+  __DATA_CONST.__cfstring: 0x840
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x10
-  __DATA.__objc_const: 0x760
-  __DATA.__objc_selrefs: 0x710
+  __DATA_CONST.__objc_intobj: 0x30
+  __DATA_CONST.__objc_arraydata: 0x50
+  __DATA_CONST.__objc_arrayobj: 0x48
+  __DATA_CONST.__objc_dictobj: 0x50
+  __DATA.__objc_const: 0x3f0
+  __DATA.__objc_selrefs: 0x7a8
   __DATA.__objc_ivar: 0x8
   __DATA.__objc_data: 0xf0
-  __DATA.__data: 0x1150
+  __DATA.__data: 0x10d0
   __DATA.__crash_info: 0x40
   __DATA.__thread_vars: 0x18
   __DATA.__thread_bss: 0x8
-  __DATA.__common: 0x30
   __DATA.__bss: 0x7f8
+  __DATA.__common: 0x40
   - /System/Library/Frameworks/AudioToolbox.framework/Versions/A/AudioToolbox
   - /System/Library/Frameworks/CoreAudio.framework/Versions/A/CoreAudio
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
   - /usr/local/lib/libVirtualBiometricServices.dylib
-  UUID: 592706D7-9D1E-3BB5-A131-A626C7875375
-  Functions: 9285
-  Symbols:   867
-  CStrings:  2896
+  UUID: 3B4ABECD-D035-3ADA-9E8B-6F3882ED8737
+  Functions: 9427
+  Symbols:   882
+  CStrings:  2920
 
Symbols:
+ _OBJC_CLASS_$_NSConstantArray
+ _OBJC_CLASS_$_NSConstantDictionary
+ _OBJC_CLASS_$_NSConstantIntegerNumber
+ _VTParavirtualizationHostSessionCompleteInvalidate
+ __CFXPCCreateXPCObjectFromCFObject
+ __ZNSt3__117bad_function_callD1Ev
+ __ZTINSt3__117bad_function_callE
+ __ZTVNSt3__117bad_function_callE
+ ___kCFBooleanTrue
+ __os_feature_enabled_impl
+ _vmnet_enable_virtio_header_key
+ _xpc_add_bundle_with_lwcr
+ _xpc_dictionary_create_empty
+ _xpc_dictionary_get_data
+ _xpc_dictionary_set_data
+ _xpc_release
- __ZN13diskimage_uio21diskimage_open_paramsaSEOS0_
CStrings:
+ "$query"
+ "ADIForwardSecureTunnelMessage returned %d"
+ "Failed to create LWCR constraints."
+ "Failed to disable queue #%u, err=%d"
+ "Failed to enable queue #%u, err=%d"
+ "Failed to get queue base, err=%d"
+ "Failed to reset vhost device status, err=%d"
+ "Failed to set queue #%u to size %u, err=%d"
+ "Fatal queue misuse error: %s"
+ "VirtualizationCore"
+ "chosen"
+ "com.apple.private.virtualization.plugin"
+ "delta_x"
+ "duplex"
+ "entitlements"
+ "i"
+ "implicitly_adds_video_toolbox_device"
+ "session"
+ "topology"
+ "vmnetEnableVirtIOHeader"
+ "xpc_add_bundle_with_lwcr failed."
- "Failed to set queue #%u %s, err=%d"
- "Unhandled error value: %d"

```
