## com.apple.Virtualization.VirtualMachine

> `/System/Library/Frameworks/Virtualization.framework/Versions/Current/XPCServices/com.apple.Virtualization.VirtualMachine.xpc/Contents/MacOS/com.apple.Virtualization.VirtualMachine`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`
- `__DATA.__thread_vars`

```diff

-308.0.0.0.0
-  __TEXT.__text: 0x40d2dc
-  __TEXT.__auth_stubs: 0x38c0
+308.1.7.0.0
+  __TEXT.__text: 0x40dbdc
+  __TEXT.__auth_stubs: 0x38d0
   __TEXT.__objc_stubs: 0x1c80
   __TEXT.__objc_methlist: 0xc4
-  __TEXT.__const: 0x28dd0
+  __TEXT.__const: 0x28e70
   __TEXT.__dlopen_cstrs: 0x66
-  __TEXT.__cstring: 0x10cbe
+  __TEXT.__cstring: 0x10d00
   __TEXT.__objc_classname: 0xc6
   __TEXT.__objc_methname: 0x17b2
   __TEXT.__objc_methtype: 0xd96

   __TEXT.__swift5_reflstr: 0x1a7
   __TEXT.__swift5_fieldmd: 0x114
   __TEXT.__swift5_types: 0x10
-  __TEXT.__gcc_except_tab: 0x3b784
-  __TEXT.__oslogstring: 0x4733
-  __TEXT.__unwind_info: 0xfef8
-  __DATA_CONST.__const: 0x20e08
+  __TEXT.__gcc_except_tab: 0x3b798
+  __TEXT.__oslogstring: 0x4717
+  __TEXT.__unwind_info: 0xff18
+  __DATA_CONST.__const: 0x20e98
   __DATA_CONST.__cfstring: 0x1140
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x18
-  __DATA_CONST.__objc_intobj: 0x78
+  __DATA_CONST.__objc_intobj: 0x60
   __DATA_CONST.__objc_arraydata: 0xb0
   __DATA_CONST.__objc_arrayobj: 0x48
   __DATA_CONST.__objc_dictobj: 0x78
-  __DATA_CONST.__auth_got: 0x1c70
+  __DATA_CONST.__objc_doubleobj: 0x10
+  __DATA_CONST.__auth_got: 0x1c78
   __DATA_CONST.__got: 0x628
   __DATA_CONST.__auth_ptr: 0x118
   __DATA.__objc_const: 0x698

   __DATA.__crash_info: 0x148
   __DATA.__thread_vars: 0x18
   __DATA.__thread_bss: 0x8
-  __DATA.__bss: 0x9c0
+  __DATA.__bss: 0x9d0
   __DATA.__common: 0xa98
   - /System/Library/Frameworks/AccessoryAccess.framework/Versions/A/AccessoryAccess
   - /System/Library/Frameworks/AudioToolbox.framework/Versions/A/AudioToolbox

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/local/lib/libVirtualBiometricServices.dylib
-  Functions: 11552
-  Symbols:   1068
-  CStrings:  3477
+  Functions: 11561
+  Symbols:   1070
+  CStrings:  3479
 
Symbols:
+ _OBJC_CLASS_$_NSConstantDoubleNumber
+ _audit_token_to_pid
CStrings:
+ "IDT should NOT be set for TRBs on IN endpoints."
+ "Received event on stale/torn-down connection"
+ "relay_audit_token"
- "Received event handler from a connection before MSR support was disabled"
```
