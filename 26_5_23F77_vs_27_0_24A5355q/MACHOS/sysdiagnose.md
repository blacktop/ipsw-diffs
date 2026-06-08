## sysdiagnose

> `/usr/bin/sysdiagnose`

```diff

-1527.120.2.0.0
-  __TEXT.__text: 0x47e4
-  __TEXT.__auth_stubs: 0x620
+1587.0.0.0.0
+  __TEXT.__text: 0x3f8c
+  __TEXT.__auth_stubs: 0x5c0
   __TEXT.__objc_stubs: 0x820
   __TEXT.__objc_methlist: 0xac
-  __TEXT.__const: 0x90
-  __TEXT.__gcc_except_tab: 0x74
-  __TEXT.__cstring: 0x23ca
-  __TEXT.__oslogstring: 0x722
+  __TEXT.__const: 0x88
+  __TEXT.__cstring: 0x23bd
+  __TEXT.__oslogstring: 0x66f
   __TEXT.__objc_methname: 0x5d9
-  __TEXT.__objc_classname: 0x14
+  __TEXT.__objc_classname: 0x12
   __TEXT.__objc_methtype: 0x5b
-  __TEXT.__unwind_info: 0x180
-  __DATA_CONST.__auth_got: 0x320
-  __DATA_CONST.__got: 0x140
-  __DATA_CONST.__auth_ptr: 0x8
+  __TEXT.__unwind_info: 0x158
   __DATA_CONST.__const: 0x328
-  __DATA_CONST.__cfstring: 0x6e0
+  __DATA_CONST.__cfstring: 0x700
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_arraydata: 0x28
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_arrayobj: 0x18
+  __DATA_CONST.__auth_got: 0x2e8
+  __DATA_CONST.__got: 0x140
+  __DATA_CONST.__auth_ptr: 0x8
   __DATA.__objc_const: 0xd0
   __DATA.__objc_selrefs: 0x238
   __DATA.__objc_ivar: 0x4

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsysdiagnose.dylib
-  UUID: 9C2AAA5E-426E-32C9-B474-10DADBC128AE
-  Functions: 96
-  Symbols:   150
-  CStrings:  295
+  UUID: 74939F51-2BDE-3CF3-A14C-AE0D497F3CEC
+  Functions: 83
+  Symbols:   143
+  CStrings:  289
 
Symbols:
+ _kCFBooleanTrue
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x24
+ _objc_retain_x8
- _IOIteratorNext
- _IOObjectRelease
- _IORegistryEntryCreateIterator
- _IORegistryEntryFromPath
- _IORegistryEntryGetName
- __Unwind_Resume
- ___objc_personality_v0
- __os_crash_msg
- __os_log_send_and_compose_impl
- _kIOMainPortDefault
- _objc_retain_x22
- _objc_retain_x23
- _objc_retain_x27
- _objc_terminate
- _strcmp
CStrings:
+ "\nAppleInternal options:\n          -c                      macOS: do not run a local sysdiagnose, only gather co-sysdiagnose(s); iOS: force co-sysdiagnose on paired devices.\n          -l                      Do not display legal prompt.\n          -L                      Collect full log archive. This will increase the time sysdiagnose takes to finish.\n          -X                      Run sysdiagnose without time outs.\n"
+ "Got result %d for compute controller check"
+ "IsComputeController"
- "\nAppleInternal options:\n          -c                      OS X: do not run a local sysdiagnose, only gather co-sysdiagnose(s); iOS: force co-sysdiagnose on paired devices.\n          -l                      Do not display legal prompt.\n          -L                      Collect full log archive. This will increase the time sysdiagnose takes to finish.\n          -X                      Run sysdiagnose without time outs.\n"
- "Got result %d for isComputeModuleB check"
- "IODeviceTree"
- "IODeviceTree:/"
- "IOObjectRetain: %{mach.errno}d"
- "IORegistryEntryGetName: %d"
- "assertion failure: \"name\" -> %llu"
- "failed to create IORegistryEntryCreateIterator: %d"
- "failed to find ioreg path: %{public}s"
- "manta-b"

```
