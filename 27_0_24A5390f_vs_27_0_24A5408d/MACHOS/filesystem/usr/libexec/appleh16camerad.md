## appleh16camerad

> `/usr/libexec/appleh16camerad`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`

```diff

-6.14.1.0.0
-  __TEXT.__text: 0x844f0
-  __TEXT.__auth_stubs: 0x1fb0
+6.18.0.0.0
+  __TEXT.__text: 0x84844
+  __TEXT.__auth_stubs: 0x1fd0
   __TEXT.__objc_stubs: 0x1400
   __TEXT.__objc_methlist: 0x270
-  __TEXT.__gcc_except_tab: 0x20e8
+  __TEXT.__gcc_except_tab: 0x2104
   __TEXT.__const: 0x2db0
-  __TEXT.__cstring: 0x8afe
-  __TEXT.__oslogstring: 0x5e43
+  __TEXT.__cstring: 0x8b96
+  __TEXT.__oslogstring: 0x5ec3
   __TEXT.__objc_methname: 0x1590
   __TEXT.__objc_classname: 0x88
   __TEXT.__objc_methtype: 0x10e5
-  __TEXT.__unwind_info: 0x1580
-  __DATA_CONST.__const: 0xb6d0
-  __DATA_CONST.__cfstring: 0x3360
+  __TEXT.__unwind_info: 0x1590
+  __DATA_CONST.__const: 0xb710
+  __DATA_CONST.__cfstring: 0x33a0
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_intobj: 0x138
   __DATA_CONST.__objc_arraydata: 0x58
   __DATA_CONST.__objc_arrayobj: 0x60
-  __DATA_CONST.__auth_got: 0xfe8
+  __DATA_CONST.__auth_got: 0xff8
   __DATA_CONST.__got: 0xbc8
   __DATA_CONST.__auth_ptr: 0x60
   __DATA.__objc_const: 0x5c8
   __DATA.__objc_selrefs: 0x618
   __DATA.__objc_ivar: 0x38
   __DATA.__objc_data: 0xf0
-  __DATA.__data: 0x371da0
+  __DATA.__data: 0x380da0
   __DATA.__common: 0x14
-  __DATA.__bss: 0xa9
+  __DATA.__bss: 0xb8
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 1692
-  Symbols:   901
-  CStrings:  2029
+  Functions: 1698
+  Symbols:   903
+  CStrings:  2035
 
Symbols:
+ _CFPreferencesGetAppBooleanValue
+ _xpc_connection_copy_entitlement_value
CStrings:
+ "/usr/local/share/firmware/isp/2226_01XX.dat"
+ "/usr/local/share/firmware/isp/2226_02XX.dat"
+ "6.18"
+ "Audit: XPC peer missing %{public}s (pid %{private}d) — would reject\n"
+ "EnforceClientEntitlement"
+ "Rejecting XPC peer missing %{public}s (pid %{private}d)\n"
+ "com.apple.private.appleh16camerad.client"
- "6.14.1"
```
