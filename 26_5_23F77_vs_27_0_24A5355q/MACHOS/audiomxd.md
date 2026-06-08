## audiomxd

> `/usr/libexec/audiomxd`

```diff

-1556.604.2.0.0
-  __TEXT.__text: 0x3ee8
-  __TEXT.__auth_stubs: 0x8a0
+1619.4.0.0.0
+  __TEXT.__text: 0x43bc
+  __TEXT.__auth_stubs: 0x890
   __TEXT.__objc_stubs: 0xc0
-  __TEXT.__const: 0xa4
+  __TEXT.__const: 0xa0
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__gcc_except_tab: 0x370
-  __TEXT.__cstring: 0x4bf
-  __TEXT.__oslogstring: 0x325
-  __TEXT.__objc_classname: 0x1
+  __TEXT.__gcc_except_tab: 0x374
+  __TEXT.__cstring: 0x4c0
+  __TEXT.__oslogstring: 0x326
   __TEXT.__objc_methname: 0x7f
-  __TEXT.__unwind_info: 0x170
-  __DATA_CONST.__auth_got: 0x460
-  __DATA_CONST.__got: 0xd8
-  __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x360
+  __TEXT.__unwind_info: 0x1e0
+  __DATA_CONST.__const: 0x3e8
   __DATA_CONST.__cfstring: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__auth_got: 0x458
+  __DATA_CONST.__got: 0xc8
+  __DATA_CONST.__auth_ptr: 0x8
   __DATA.__objc_selrefs: 0x30
   __DATA.__bss: 0x38
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox

   - /System/Library/PrivateFrameworks/Tightbeam.framework/Tightbeam
   - /System/Library/PrivateFrameworks/WatchdogClient.framework/WatchdogClient
   - /System/Library/PrivateFrameworks/caulk.framework/caulk
-  - /usr/lib/libAudioToolboxUtility.dylib
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6609D035-CC4C-35D0-BDAC-19DA38FC75A0
-  Functions: 57
-  Symbols:   176
+  UUID: 8D5A0387-14FF-3BDA-B818-0C29D46ACEBE
+  Functions: 77
+  Symbols:   171
   CStrings:  94
 
Symbols:
+ _CFArrayGetValueAtIndex
+ __ZN5caulk4mach7details17release_os_objectEPv
+ __ZN5caulk8platform12process_nameEi
+ __xpc_type_error
+ _tb_endpoint_destruct
+ _xpc_connection_set_context
+ _xpc_connection_set_event_handler
- __ZN10XPC_ObjectD2Ev
- __ZN11XPC_Service17ConnectionHandlerEP17_xpc_connection_s
- __ZN14XPC_Connection10InitializeEv
- __ZN14XPC_Connection14ProcessMessageEPv
- __ZN14XPC_Connection8FinalizeEPS_
- __ZN14XPC_ConnectionD2Ev
- __ZN14XPC_DictionaryD1Ev
- __ZN17PlatformUtilities11processNameEi
- __ZNK9CACFArray9GetCFTypeEjRPKv
- __ZTV14XPC_Connection
- __ZTV14XPC_Dictionary
- _os_release
CStrings:
+ "%25s:%-5d [audiomxd conclave][%s] conclave launch succeeded"
- "%25s:%-5d [audiomxd conclave][%s] conclave launch suceeded"

```
