## peakpowermanagerd

> `/usr/libexec/peakpowermanagerd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1191.0.27.0.0
-  __TEXT.__text: 0x10cc0
-  __TEXT.__auth_stubs: 0x5e0
-  __TEXT.__objc_stubs: 0x2280
+1191.0.37.0.0
+  __TEXT.__text: 0x10e80
+  __TEXT.__auth_stubs: 0x600
+  __TEXT.__objc_stubs: 0x22c0
   __TEXT.__objc_methlist: 0x10f4
-  __TEXT.__objc_methname: 0x2b40
-  __TEXT.__cstring: 0x8cd
+  __TEXT.__objc_methname: 0x2b5f
+  __TEXT.__cstring: 0x93e
   __TEXT.__objc_classname: 0x50
   __TEXT.__objc_methtype: 0x332
-  __TEXT.__gcc_except_tab: 0x90
+  __TEXT.__gcc_except_tab: 0xc4
   __TEXT.__const: 0x58
-  __TEXT.__oslogstring: 0xabf
+  __TEXT.__oslogstring: 0xb38
   __TEXT.__unwind_info: 0x2d0
-  __DATA_CONST.__const: 0xf0
+  __DATA_CONST.__const: 0x110
   __DATA_CONST.__cfstring: 0xac0
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x20
-  __DATA_CONST.__auth_got: 0x300
-  __DATA_CONST.__got: 0xa0
+  __DATA_CONST.__auth_got: 0x310
+  __DATA_CONST.__got: 0xb0
   __DATA.__objc_const: 0x13f0
-  __DATA.__objc_selrefs: 0xc20
+  __DATA.__objc_selrefs: 0xc30
   __DATA.__objc_ivar: 0x114
   __DATA.__objc_data: 0x140
   __DATA.__data: 0x60
-  __DATA.__bss: 0x29
+  __DATA.__bss: 0x31
   __DATA.__common: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/Versions/A/ProtocolBuffer
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 451
-  Symbols:   125
-  CStrings:  679
+  Functions: 454
+  Symbols:   129
+  CStrings:  686
 
Symbols:
+ _OBJC_CLASS_$_NSValue
+ _bootstrap_check_in
+ _bootstrap_port
+ _exit
+ _objc_opt_new
+ _os_transaction_create
- _IODataQueueAllocateNotificationPort
- _mach_port_mod_refs
CStrings:
+ "%s: draining telemetry queue backlog on launch\n"
+ "%s: failed to request telemetry donation on launch\n"
+ "Telemetry entry has missing or invalid category; skipping entry\n"
+ "com.apple.peakpowermanagerd.telemetry-drain"
+ "com.apple.peakpowermanagerd.telemetry-notification"
+ "main_block_invoke"
+ "peakpowermanagerd could not check in notification MachService (%s) status %d\n"
+ "peakpowermanagerd: CPMS telemetry bridge torn down; exiting for clean relaunch\n"
+ "pointerValue"
+ "valueWithPointer:"
- "peakpowermanagerd could not allocate mach notification port\n"
- "peakpowermanagerd failed to destroy mach port status code : %d\n"
- "peakpowermanagerd failed to send mach port deallocated notification to kext\n"
```
