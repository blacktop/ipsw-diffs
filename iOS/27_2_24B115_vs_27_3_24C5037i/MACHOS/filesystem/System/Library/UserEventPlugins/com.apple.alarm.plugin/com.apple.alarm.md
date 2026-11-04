## com.apple.alarm

> `/System/Library/UserEventPlugins/com.apple.alarm.plugin/com.apple.alarm`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`
- `__DATA.__const`
- `__DATA.__cfstring`

```diff

-359.0.0.0.0
-  __TEXT.__text: 0x2294
+362.60.2.0.0
+  __TEXT.__text: 0x23d4
   __TEXT.__auth_stubs: 0x480
-  __TEXT.__const: 0xc0
+  __TEXT.__const: 0xd0
   __TEXT.__cstring: 0x1af
-  __TEXT.__oslogstring: 0x6a8
-  __TEXT.__unwind_info: 0x110
+  __TEXT.__oslogstring: 0x6ed
+  __TEXT.__unwind_info: 0x118
   __DATA.__const: 0x130
   __DATA.__cfstring: 0x200
   __DATA.__data: 0x8

   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
-  Functions: 39
+  Functions: 41
   Symbols:   92
-  CStrings:  64
+  CStrings:  65
 
CStrings:
+ "Alarm \"%{public}s\" is sooner than the scheduled wake, re-scheduling."
```
