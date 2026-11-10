## libspindump.dylib

> `/usr/lib/libspindump.dylib`

```diff

-448.0.0.0.0
-  __TEXT.__text: 0x44d4
+453.1.0.0.0
+  __TEXT.__text: 0x46cc
   __TEXT.__const: 0xc0
-  __TEXT.__cstring: 0x500
-  __TEXT.__oslogstring: 0xd72
+  __TEXT.__cstring: 0x54a
+  __TEXT.__oslogstring: 0xe16
   __TEXT.__unwind_info: 0x160
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_methname: 0x0
   __DATA_CONST.__const: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x38
+  __DATA_CONST.__objc_selrefs: 0x40
   __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x190
   __AUTH_CONST.__cfstring: 0x40
-  __AUTH_CONST.__auth_got: 0x1f8
+  __AUTH_CONST.__auth_got: 0x210
   __AUTH_CONST.__auth_ptr: 0x0
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x240
-  __DATA_DIRTY.__bss: 0x128
+  __DATA.__bss: 0x48
+  __DATA_DIRTY.__bss: 0x328
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/Versions/A/CoreAnalytics
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 98
-  Symbols:   207
-  CStrings:  124
+  Functions: 99
+  Symbols:   215
+  CStrings:  126
 
Symbols:
+ _OBJC_CLASS_$_NSNumber
+ _SPStringFromInfoDictionaryValue
+ _gActionCountSinceLastSignpost
+ _gHIDEventCountSinceLastSignpost
+ _objc_autoreleaseReturnValue
+ _objc_msgSend$stringValue
+ _objc_opt_class
+ _objc_opt_isKindOfClass
Functions:
~ _SPCheckHIDResponseTime2 : 3832 -> 4116
~ ___SPSubmitHIDTelemetry_block_invoke : 804 -> 868
+ _SPStringFromInfoDictionaryValue
CStrings:
+ "%{public, signpost.description:begin_time}llu %{public, signpost.description:end_time}llu hidEventCountSinceLastSignpost=%{public,name=hidEventCountSinceLastSignpost}llu userActionCountSinceLastSignpost=%{public,name=userActionCountSinceLastSignpost}llu"
+ "hid_event_count_since_last_signpost"
+ "user_action_count_since_last_signpost"
- "%{public, signpost.description:begin_time}llu %{public, signpost.description:end_time}llu"
```
