## locationaccessstored

> `/usr/libexec/locationaccessstored`

```diff

-3056.0.6.0.2
-  __TEXT.__text: 0x36e8
-  __TEXT.__auth_stubs: 0x320
-  __TEXT.__objc_stubs: 0xc80
+3056.0.14.0.0
+  __TEXT.__text: 0x3ac0
+  __TEXT.__auth_stubs: 0x360
+  __TEXT.__objc_stubs: 0xca0
   __TEXT.__objc_methlist: 0x26c
-  __TEXT.__const: 0x90
-  __TEXT.__oslogstring: 0x867
-  __TEXT.__cstring: 0x1d6
-  __TEXT.__gcc_except_tab: 0x7d8
+  __TEXT.__const: 0x98
+  __TEXT.__oslogstring: 0x994
+  __TEXT.__cstring: 0x215
+  __TEXT.__gcc_except_tab: 0x83c
   __TEXT.__objc_methname: 0xb63
   __TEXT.__objc_classname: 0x65
   __TEXT.__objc_methtype: 0x179
-  __TEXT.__unwind_info: 0x1b0
-  __DATA_CONST.__auth_got: 0x1a0
-  __DATA_CONST.__got: 0xc0
-  __DATA_CONST.__const: 0x130
+  __TEXT.__unwind_info: 0x1b8
+  __DATA_CONST.__auth_got: 0x1c0
+  __DATA_CONST.__got: 0xd0
+  __DATA_CONST.__const: 0x158
   __DATA_CONST.__cfstring: 0x220
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x18

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: FD002B07-0912-3C31-8A06-3678E3A49D60
-  Functions: 38
-  Symbols:   83
-  CStrings:  238
+  UUID: B9CA48A8-6851-35D1-B649-9C3F36E54589
+  Functions: 40
+  Symbols:   89
+  CStrings:  244
 
Symbols:
+ _OBJC_CLASS_$_NSArray
+ _OBJC_EHTYPE_$_NSException
+ ___objc_personality_v0
+ _objc_begin_catch
+ _objc_end_catch
+ _objc_retainAutoreleasedReturnValue
+ _xpc_set_event_stream_handler
- ___gxx_personality_v0
CStrings:
+ "#CLLA Can't store client data"
+ "#CLLA JSON data is not an array"
+ "com.apple.locationd.appreset"
+ "v16@?0@\"NSObject<OS_xpc_object>\"8"
+ "{\"msg%{public}.0s\":\"#CLLA Can't store client data\", \"jsonArray\":%{public, location:escape_only}@, \"exception\":%{public, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#CLLA JSON data is not an array\", \"path\":%{public, location:escape_only}@}"

```
