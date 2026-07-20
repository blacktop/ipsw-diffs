## cameraispdarwinsimd

> `/usr/libexec/cameraispdarwinsimd`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__auth_ptr`
- `__DATA.__data`

```diff

-20.54.2.0.0
-  __TEXT.__text: 0x14ae4
-  __TEXT.__auth_stubs: 0xd00
+20.57.4.0.0
+  __TEXT.__text: 0x14d48
+  __TEXT.__auth_stubs: 0xd40
   __TEXT.__init_offsets: 0x4
-  __TEXT.__cstring: 0x1961
-  __TEXT.__const: 0x150
+  __TEXT.__cstring: 0x19ea
+  __TEXT.__const: 0x160
   __TEXT.__gcc_except_tab: 0x1dc
-  __TEXT.__oslogstring: 0x222b
-  __TEXT.__unwind_info: 0x338
-  __DATA_CONST.__const: 0x7d30
-  __DATA_CONST.__cfstring: 0x580
+  __TEXT.__oslogstring: 0x22ab
+  __TEXT.__unwind_info: 0x350
+  __DATA_CONST.__const: 0x7d80
+  __DATA_CONST.__cfstring: 0x5c0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0x688
-  __DATA_CONST.__got: 0xc0
+  __DATA_CONST.__auth_got: 0x6a8
+  __DATA_CONST.__got: 0xc8
   __DATA_CONST.__auth_ptr: 0x10
   __DATA.__data: 0x3aebe8
-  __DATA.__bss: 0xa4
+  __DATA.__bss: 0xb8
   __DATA.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreVideo.framework/Versions/A/CoreVideo

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 291
-  Symbols:   239
-  CStrings:  392
+  Functions: 296
+  Symbols:   244
+  CStrings:  399
 
Symbols:
+ _CFPreferencesGetAppBooleanValue
+ __xpc_type_bool
+ _dispatch_once
+ _xpc_bool_get_value
+ _xpc_connection_copy_entitlement_value
CStrings:
+ "/usr/local/share/firmware/isp/dcs_isp_fw.bin"
+ "20.57.4"
+ "<UNKNOWN>"
+ "Audit: XPC peer missing %{public}s (pid %{private}d) — would reject\n"
+ "EnforceClientEntitlement"
+ "Rejecting XPC peer missing %{public}s (pid %{private}d)\n"
+ "com.apple.cameraispd"
+ "com.apple.private.cameraispd.client"
- "20.54.2"
```
