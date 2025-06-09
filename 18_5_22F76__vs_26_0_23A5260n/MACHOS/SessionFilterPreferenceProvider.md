## SessionFilterPreferenceProvider

> `/System/Library/PrivateFrameworks/MultitouchSessionFilterSupport.framework/XPCServices/SessionFilterPreferenceProvider.xpc/SessionFilterPreferenceProvider`

```diff

-8140.4.0.0.0
-  __TEXT.__text: 0x8a0
+9100.23.0.0.0
+  __TEXT.__text: 0x8b0
   __TEXT.__auth_stubs: 0x180
   __TEXT.__objc_stubs: 0x200
-  __TEXT.__objc_methlist: 0x1f0
-  __TEXT.__const: 0x70
+  __TEXT.__objc_methlist: 0x20c
+  __TEXT.__const: 0x78
   __TEXT.__objc_classname: 0x79
-  __TEXT.__objc_methname: 0x3ce
-  __TEXT.__objc_methtype: 0x143
+  __TEXT.__objc_methname: 0x40b
+  __TEXT.__objc_methtype: 0x166
   __TEXT.__cstring: 0xb7
-  __TEXT.__oslogstring: 0x8d
+  __TEXT.__oslogstring: 0x6c
   __TEXT.__unwind_info: 0x88
   __DATA_CONST.__auth_got: 0xc8
   __DATA_CONST.__got: 0x28

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA.__objc_const: 0x3f8
-  __DATA.__objc_selrefs: 0x158
+  __DATA.__objc_const: 0x420
+  __DATA.__objc_selrefs: 0x160
   __DATA.__objc_ivar: 0xc
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0x120

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: CC9B3254-1C86-3BF4-BB04-1FE8AB3A8CB3
-  Functions: 18
-  Symbols:   112
-  CStrings:  98
+  UUID: 09D01745-2BA4-3032-8843-D87F15527FD9
+  Functions: 19
+  Symbols:   113
+  CStrings:  100
 
Symbols:
+ -[SessionFilterPreferenceProvider continuousRecordingUpdateInternalToggleStateWithReply:reply:]
Functions:
~ -[SessionFilterPreferenceProvider continuousRecordingEnabledWithReply:] : 360 -> 220
+ -[SessionFilterPreferenceProvider continuousRecordingUpdateInternalToggleStateWithReply:reply:]
CStrings:
+ "continuousRecordingUpdateInternalToggleStateWithReply:reply:"
+ "v28@0:8B16@?20"
+ "v28@0:8B16@?<v@?>20"
- "Continuous recording enabled: %d"

```
