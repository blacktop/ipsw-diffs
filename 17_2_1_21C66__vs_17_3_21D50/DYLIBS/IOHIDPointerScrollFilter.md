## IOHIDPointerScrollFilter

> `/System/Library/HIDPlugins/IOHIDPointerScrollFilter.plugin/IOHIDPointerScrollFilter`

```diff

-2008.60.7.0.0
-  __TEXT.__text: 0x85c0
-  __TEXT.__auth_stubs: 0x690
-  __TEXT.__gcc_except_tab: 0x700
+2008.80.3.0.1
+  __TEXT.__text: 0x85b4
+  __TEXT.__auth_stubs: 0x6c0
+  __TEXT.__gcc_except_tab: 0x710
   __TEXT.__const: 0x3b6
-  __TEXT.__cstring: 0x6d9
-  __TEXT.__oslogstring: 0x3e4
-  __TEXT.__unwind_info: 0x43c
+  __TEXT.__cstring: 0x6d2
+  __TEXT.__oslogstring: 0x41f
+  __TEXT.__unwind_info: 0x438
   __TEXT.__eh_frame: 0x74
   __DATA_CONST.__got: 0x90
-  __DATA_CONST.__const: 0xd8
+  __DATA_CONST.__const: 0x98
   __AUTH_CONST.__cfstring: 0x9a0
   __AUTH_CONST.__const: 0x5b0
-  __AUTH_CONST.__auth_got: 0x350
+  __AUTH_CONST.__auth_got: 0x368
   __AUTH.__data: 0x78
   __DATA.__got_weak: 0xa0
   __DATA.__data: 0x98

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   Functions: 201
-  Symbols:   227
+  Symbols:   231
   CStrings:  124
 
Symbols:
+ __ZN24IOHIDPointerScrollFilter18statsTimerCallbackEPv
+ _analytics_is_event_used
+ _analytics_send_event
+ _dispatch_set_context
+ _dispatch_source_set_event_handler_f
+ _xpc_release
- _analytics_send_event_lazy
- _dispatch_source_set_event_handler
CStrings:
+ "_service is null, no acceleration stats will be collected\n"
- "^v8@?0"

```
