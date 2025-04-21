## libsystemstats.dylib

> `/usr/lib/libsystemstats.dylib`

```diff

-498.100.2.0.0
-  __TEXT.__text: 0x70a0
-  __TEXT.__auth_stubs: 0x8e0
-  __TEXT.__const: 0xf0
-  __TEXT.__cstring: 0x627
+498.120.2.0.0
+  __TEXT.__text: 0x7920
+  __TEXT.__auth_stubs: 0x900
+  __TEXT.__const: 0xf8
+  __TEXT.__cstring: 0x68d
   __TEXT.__gcc_except_tab: 0x274
-  __TEXT.__oslogstring: 0x900
+  __TEXT.__oslogstring: 0xace
   __TEXT.__unwind_info: 0x238
   __TEXT.__objc_methname: 0x185
   __TEXT.__objc_stubs: 0x240
-  __DATA_CONST.__got: 0x50
+  __DATA_CONST.__got: 0x60
   __DATA_CONST.__const: 0x378
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x98
-  __AUTH_CONST.__auth_got: 0x480
+  __AUTH_CONST.__auth_got: 0x490
   __AUTH_CONST.__const: 0xa0
-  __AUTH_CONST.__cfstring: 0x100
+  __AUTH_CONST.__cfstring: 0x160
   __DATA.__bss: 0x18
   __DATA_DIRTY.__data: 0x540
   __DATA_DIRTY.__bss: 0x30

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 156
-  Symbols:   201
-  CStrings:  144
+  Functions: 169
+  Symbols:   208
+  CStrings:  157
 
Symbols:
+ _CFNumberCreate
+ _CFPreferencesSetValue
+ _CFPreferencesSynchronize
+ _kCFAllocatorDefault
+ _kCFPreferencesAnyHost
+ _systemstats_get_microstackshot_cycle_interval_default
+ _systemstats_get_microstackshot_cycle_interval_override
+ _systemstats_set_microstackshot_cycle_interval_override
- _objc_retain_x3
CStrings:
+ "Invalid microstackshot cycle override: %llu < min %llu"
+ "Invalid microstackshot cycle override: %llu > max %llu"
+ "Invalid number for microstackshot cycle interval override: %lld"
+ "Invalid number for preferences setting %{public}@: %{public}@"
+ "Invalid value for preferences setting %{public}@: (%{public}@)%{public}@"
+ "Microstackshot PMI cycle interval overridden to %llu"
+ "Must be root to get microstackshot cycle override"
+ "Must be root to set microstackshot cycle override"
+ "PMICycleInterval"
+ "com.apple.microstackshots"
+ "com.apple.microstackshots.preferences_changed"
+ "endtime"
+ "root"

```
