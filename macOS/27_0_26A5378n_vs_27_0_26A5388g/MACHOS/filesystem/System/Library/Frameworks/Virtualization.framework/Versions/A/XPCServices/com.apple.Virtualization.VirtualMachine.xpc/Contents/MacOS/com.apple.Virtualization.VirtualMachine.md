## com.apple.Virtualization.VirtualMachine

> `/System/Library/Frameworks/Virtualization.framework/Versions/A/XPCServices/com.apple.Virtualization.VirtualMachine.xpc/Contents/MacOS/com.apple.Virtualization.VirtualMachine`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`
- `__DATA.__data`
- `__DATA.__thread_vars`

```diff

-306.0.1.0.0
-  __TEXT.__text: 0x409e00
+308.0.0.0.0
+  __TEXT.__text: 0x40d2dc
   __TEXT.__auth_stubs: 0x38c0
-  __TEXT.__objc_stubs: 0x1c40
+  __TEXT.__objc_stubs: 0x1c80
   __TEXT.__objc_methlist: 0xc4
-  __TEXT.__const: 0x28cb0
+  __TEXT.__const: 0x28dd0
   __TEXT.__dlopen_cstrs: 0x66
-  __TEXT.__cstring: 0x10cb9
+  __TEXT.__cstring: 0x10cbe
   __TEXT.__objc_classname: 0xc6
-  __TEXT.__objc_methname: 0x1732
+  __TEXT.__objc_methname: 0x17b2
   __TEXT.__objc_methtype: 0xd96
   __TEXT.__constg_swiftt: 0x138
   __TEXT.__swift5_typeref: 0xb4
   __TEXT.__swift5_reflstr: 0x1a7
   __TEXT.__swift5_fieldmd: 0x114
   __TEXT.__swift5_types: 0x10
-  __TEXT.__gcc_except_tab: 0x3b508
-  __TEXT.__oslogstring: 0x465e
-  __TEXT.__unwind_info: 0xfe40
-  __DATA_CONST.__const: 0x20cf8
+  __TEXT.__gcc_except_tab: 0x3b784
+  __TEXT.__oslogstring: 0x4733
+  __TEXT.__unwind_info: 0xfef8
+  __DATA_CONST.__const: 0x20e08
   __DATA_CONST.__cfstring: 0x1140
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arrayobj: 0x48
   __DATA_CONST.__objc_dictobj: 0x78
   __DATA_CONST.__auth_got: 0x1c70
-  __DATA_CONST.__got: 0x618
+  __DATA_CONST.__got: 0x628
   __DATA_CONST.__auth_ptr: 0x118
-  __DATA.__objc_const: 0x678
-  __DATA.__objc_selrefs: 0x738
-  __DATA.__objc_ivar: 0x2c
+  __DATA.__objc_const: 0x698
+  __DATA.__objc_selrefs: 0x748
+  __DATA.__objc_ivar: 0x30
   __DATA.__objc_data: 0x2e8
   __DATA.__data: 0x888
   __DATA.__crash_info: 0x148
   __DATA.__thread_vars: 0x18
   __DATA.__thread_bss: 0x8
-  __DATA.__bss: 0x9b0
+  __DATA.__bss: 0x9c0
   __DATA.__common: 0xa98
   - /System/Library/Frameworks/AccessoryAccess.framework/Versions/A/AccessoryAccess
   - /System/Library/Frameworks/AudioToolbox.framework/Versions/A/AudioToolbox

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/local/lib/libVirtualBiometricServices.dylib
-  Functions: 11533
-  Symbols:   1066
-  CStrings:  3466
+  Functions: 11552
+  Symbols:   1068
+  CStrings:  3477
 
Symbols:
+ _OBJC_CLASS_$_NSFileHandle
+ _OBJC_CLASS_$_VZFileHandleSerialPortAttachment
CStrings:
+ "AMAIR2_EL12"
+ "MAIR2_EL12"
+ "PFAR_EL12"
+ "Received event handler from a connection before MSR support was disabled"
+ "SCTLR2_EL12"
+ "Serial port attachment has no valid file descriptors"
+ "Serial port attachment validation failed"
+ "Serial port socket file descriptor is invalid"
+ "TCR2_EL12"
+ "_guest_supports_msr"
+ "initWithFileDescriptor:closeOnDealloc:"
+ "initWithFileHandleForReading:fileHandleForWriting:"
+ "serial_port_attachment"
- "HCR_EL2.TGE is not supported."
- "Trap to EL2 when HCR_EL2.TGE is supported."
```
