## libspindump.dylib

> `/usr/lib/libspindump.dylib`

```diff

-453.0.0.0.0
-  __TEXT.__text: 0x3950
+453.1.0.0.0
+  __TEXT.__text: 0x39bc
   __TEXT.__const: 0xb8
-  __TEXT.__oslogstring: 0xd3e
-  __TEXT.__cstring: 0x4da
+  __TEXT.__oslogstring: 0xde2
+  __TEXT.__cstring: 0x524
   __TEXT.__unwind_info: 0x1a0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0xe0
   __AUTH_CONST.__cfstring: 0x40
-  __AUTH_CONST.__auth_got: 0x268
+  __AUTH_CONST.__auth_got: 0x270
   __DATA.__crash_info: 0x148
   __DATA_DIRTY.__bss: 0x238
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 88
-  Symbols:   180
-  CStrings:  121
+  Symbols:   183
+  CStrings:  123
 
Symbols:
+ _gActionCountSinceLastSignpost
+ _gHIDEventCountSinceLastSignpost
+ _objc_release_x27
Functions:
~ _SPCheckHIDResponseTime2 : 2564 -> 2672
CStrings:
+ "%{public, signpost.description:begin_time}llu %{public, signpost.description:end_time}llu hidEventCountSinceLastSignpost=%{public,name=hidEventCountSinceLastSignpost}llu userActionCountSinceLastSignpost=%{public,name=userActionCountSinceLastSignpost}llu"
+ "hid_event_count_since_last_signpost"
+ "user_action_count_since_last_signpost"
- "%{public, signpost.description:begin_time}llu %{public, signpost.description:end_time}llu"
```
