## CallKit

> `/System/Library/Frameworks/CallKit.framework/CallKit`

```diff

-1397.100.1.0.0
-  __TEXT.__text: 0x67700
-  __TEXT.__objc_methlist: 0x927c
+1403.100.1.0.0
+  __TEXT.__text: 0x678a8
+  __TEXT.__objc_methlist: 0x92a4
   __TEXT.__const: 0x130
   __TEXT.__cstring: 0x63ab
-  __TEXT.__oslogstring: 0x3bb1
-  __TEXT.__gcc_except_tab: 0x6e4
+  __TEXT.__oslogstring: 0x3c25
+  __TEXT.__gcc_except_tab: 0x6f8
   __TEXT.__unwind_info: 0x1de8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 3240
-  Symbols:   6840
-  CStrings:  1005
+  Functions: 3244
+  Symbols:   6844
+  CStrings:  1006
 
Symbols:
+ -[CXProvider _registerCurrentConfigurationIfAudioSessionIDStaleOnQueue]
+ -[CXProvider _registerCurrentConfigurationOnQueue]
+ -[CXProvider currentOpaqueAudioSessionID]
+ ___28-[CXProvider performAction:]_block_invoke
CStrings:
+ "Cached audioSessionID %u no longer matches current opaqueSessionID %u; re-registering configuration for CXProvider."
```
