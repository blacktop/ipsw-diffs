## libsystemstats.dylib

> `/usr/lib/libsystemstats.dylib`

```diff

-507.0.0.0.0
-  __TEXT.__text: 0x7920
-  __TEXT.__auth_stubs: 0x900
-  __TEXT.__const: 0xf8
-  __TEXT.__cstring: 0x68d
+510.0.0.0.0
+  __TEXT.__text: 0x78e0
+  __TEXT.__auth_stubs: 0x8b0
+  __TEXT.__const: 0x100
+  __TEXT.__cstring: 0x6ad
   __TEXT.__gcc_except_tab: 0x274
-  __TEXT.__oslogstring: 0xace
-  __TEXT.__unwind_info: 0x240
+  __TEXT.__oslogstring: 0xb9f
+  __TEXT.__unwind_info: 0x250
   __TEXT.__objc_methname: 0x185
   __TEXT.__objc_stubs: 0x240
   __DATA_CONST.__got: 0x60
   __DATA_CONST.__const: 0x378
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x98
-  __AUTH_CONST.__auth_got: 0x490
+  __AUTH_CONST.__auth_got: 0x468
   __AUTH_CONST.__const: 0xa0
   __AUTH_CONST.__cfstring: 0x160
   __DATA.__bss: 0x18

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 4F6816A8-FA8E-3998-8BE7-B01C7A5EE39C
-  Functions: 169
-  Symbols:   208
-  CStrings:  168
+  UUID: BC041C59-CF0A-3206-9F69-3295C1A6741D
+  Functions: 179
+  Symbols:   204
+  CStrings:  173
 
Symbols:
+ _objc_autoreleaseReturnValue
+ _objc_retainAutoreleasedReturnValue
+ _systemstats_get_microstackshots_buffer_size
- _objc_claimAutoreleasedReturnValue
- _objc_retain
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x27
- _objc_retain_x4
- _objc_retain_x6
CStrings:
+ "Microstackshot PMI cycle interval overridden to disabled"
+ "Unable to get kern.microstackshot.buffer_size: %{errno}d"
+ "kern.microstackshot.buffer_size"
+ "telemetry_buffer_size has invalid value %u"
+ "telemetry_buffer_size too large (%u), capping at %d"

```
