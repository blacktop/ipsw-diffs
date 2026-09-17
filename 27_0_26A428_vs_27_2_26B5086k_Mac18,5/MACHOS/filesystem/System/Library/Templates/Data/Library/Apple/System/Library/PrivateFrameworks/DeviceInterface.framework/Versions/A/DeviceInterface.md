## DeviceInterface

> `/System/Library/Templates/Data/Library/Apple/System/Library/PrivateFrameworks/DeviceInterface.framework/Versions/A/DeviceInterface`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__auth_got`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`

```diff

-294.0.0.0.0
-  __TEXT.__text: 0x8b3d4
-  __TEXT.__objc_methlist: 0x6f3c
+297.0.0.0.0
+  __TEXT.__text: 0x8b2cc
+  __TEXT.__objc_methlist: 0x6f2c
   __TEXT.__const: 0x64
-  __TEXT.__cstring: 0x9b1d
+  __TEXT.__cstring: 0x9adf
   __TEXT.__gcc_except_tab: 0x470
   __TEXT.__oslogstring: 0x49
   __TEXT.__unwind_info: 0x2740

   __TEXT.__objc_stubs: 0x7d40
   __TEXT.__auth_stubs: 0x8f0
   __TEXT.__objc_classname: 0xf93
-  __TEXT.__objc_methname: 0xf2ae
-  __TEXT.__objc_methtype: 0x55b0
+  __TEXT.__objc_methname: 0xf244
+  __TEXT.__objc_methtype: 0x55ad
   __DATA_CONST.__const: 0x70
   __DATA_CONST.__objc_classlist: 0x398
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2978
+  __DATA_CONST.__objc_selrefs: 0x2970
   __DATA_CONST.__got: 0x90
   __AUTH_CONST.__const: 0x850
   __AUTH_CONST.__cfstring: 0x8c0
-  __AUTH_CONST.__objc_const: 0xee28
+  __AUTH_CONST.__objc_const: 0xedf8
   __AUTH_CONST.__auth_got: 0x488
   __AUTH.__objc_data: 0x23f0
   __AUTH.__data: 0x5a0
   __DATA.__objc_protorefs: 0x10
   __DATA.__objc_classrefs: 0x430
   __DATA.__objc_superrefs: 0x388
-  __DATA.__objc_ivar: 0xca0
+  __DATA.__objc_ivar: 0xc9c
   __DATA.__data: 0x580
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpcap.A.dylib
-  Functions: 2900
-  Symbols:   5914
-  CStrings:  3654
+  Functions: 2899
+  Symbols:   5912
+  CStrings:  3650
 
Symbols:
+ -[DeviceInterfaceClientXPCServer initWithInterfaceManager:serverQueue:]
+ ___71-[DeviceInterfaceClientXPCServer initWithInterfaceManager:serverQueue:]_block_invoke
+ _objc_msgSend$initWithInterfaceManager:serverQueue:
- -[DeviceInterfaceClientXPCServer asyncTransfersSupported]
- -[DeviceInterfaceClientXPCServer initWithInterfaceManager:serverQueue:asyncTransfersSupported:]
- OBJC_IVAR_$_DeviceInterfaceClientXPCServer._asyncTransfersSupported
- ___95-[DeviceInterfaceClientXPCServer initWithInterfaceManager:serverQueue:asyncTransfersSupported:]_block_invoke
- _objc_msgSend$initWithInterfaceManager:serverQueue:asyncTransfersSupported:
CStrings:
+ "@32@0:8r^{device_interface_manager_t=^v^{device_interface_manager_functions_t}}16@24"
+ "initWithInterfaceManager:serverQueue:"
- "@36@0:8r^{device_interface_manager_t=^v^{device_interface_manager_functions_t}}16@24B32"
- "Send command rejected: async transfers not supported (pid=%d)"
- "TB,R,N,V_asyncTransfersSupported"
- "_asyncTransfersSupported"
- "asyncTransfersSupported"
- "initWithInterfaceManager:serverQueue:asyncTransfersSupported:"
```
