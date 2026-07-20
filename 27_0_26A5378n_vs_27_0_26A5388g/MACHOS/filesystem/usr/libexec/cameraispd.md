## cameraispd

> `/usr/libexec/cameraispd`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-20.54.2.0.0
-  __TEXT.__text: 0x898e8
-  __TEXT.__auth_stubs: 0x18a0
+20.57.4.0.0
+  __TEXT.__text: 0x8a12c
+  __TEXT.__auth_stubs: 0x18d0
   __TEXT.__objc_stubs: 0x980
   __TEXT.__init_offsets: 0x1c
   __TEXT.__objc_methlist: 0x334
-  __TEXT.__cstring: 0x6280
-  __TEXT.__const: 0x1fca0
+  __TEXT.__cstring: 0x630a
+  __TEXT.__const: 0x1fd90
   __TEXT.__gcc_except_tab: 0xed0
-  __TEXT.__oslogstring: 0x46f7
+  __TEXT.__oslogstring: 0x4874
   __TEXT.__objc_methname: 0x9dd
   __TEXT.__objc_classname: 0xa0
   __TEXT.__objc_methtype: 0x5f9
-  __TEXT.__unwind_info: 0xe98
-  __DATA_CONST.__const: 0x8ac0
-  __DATA_CONST.__cfstring: 0x2620
+  __TEXT.__unwind_info: 0xeb0
+  __DATA_CONST.__const: 0x8b10
+  __DATA_CONST.__cfstring: 0x2660
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0x8
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA_CONST.__auth_got: 0xc60
-  __DATA_CONST.__got: 0x13c0
+  __DATA_CONST.__auth_got: 0xc78
+  __DATA_CONST.__got: 0x13d0
   __DATA_CONST.__auth_ptr: 0x40
   __DATA.__objc_const: 0x5c8
   __DATA.__objc_selrefs: 0x390
   __DATA.__objc_ivar: 0x14
   __DATA.__objc_data: 0xf0
   __DATA.__data: 0x3af330
-  __DATA.__bss: 0x500
+  __DATA.__bss: 0x510
   __DATA.__common: 0x18
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate
   - /System/Library/Frameworks/AudioToolbox.framework/Versions/A/AudioToolbox

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 1370
-  Symbols:   1047
-  CStrings:  1504
+  Functions: 1377
+  Symbols:   1052
+  CStrings:  1516
 
Symbols:
+ _CFPreferencesGetAppBooleanValue
+ __xpc_type_bool
+ _kFigCaptureStreamMetadata_IAD
+ _xpc_bool_get_value
+ _xpc_connection_copy_entitlement_value
CStrings:
+ "%s - ABDNet: Failed to create empty buffers to clear map in daemon\n"
+ "%s - ABDNet: Sending %lu buffers to daemon\n"
+ "%s - Failed to create daemon buffer array\n"
+ "%s - Failed to mirror buffers to daemon: 0x%08X\n"
+ "%s - Mirroring %ld buffers to daemon (pooID=%d)\n"
+ "/usr/local/share/firmware/isp/dcs_isp_fw.bin"
+ "20.57.4"
+ "<UNKNOWN>"
+ "Audit: XPC peer missing %{public}s (pid %{private}d) — would reject\n"
+ "EnforceClientEntitlement"
+ "FinalizeMappedBuffers"
+ "Rejecting XPC peer missing %{public}s (pid %{private}d)\n"
+ "com.apple.private.cameraispd.client"
- "20.54.2"
```
