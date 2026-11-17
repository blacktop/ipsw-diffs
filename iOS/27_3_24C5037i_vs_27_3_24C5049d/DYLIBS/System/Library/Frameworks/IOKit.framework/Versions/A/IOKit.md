## IOKit

> `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`

```diff

 100288.60.4.0.0
-  __TEXT.__text: 0xa1d00
+  __TEXT.__text: 0xa18b4
   __TEXT.__objc_methlist: 0x150
   __TEXT.__const: 0x104bc
   __TEXT.__oslogstring: 0x590b

   - /usr/lib/libenergytrace.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 3590
+  Functions: 3585
   Symbols:   3970
   CStrings:  2597
 
Symbols:
+ _os_unfair_recursive_lock_lock
- _os_unfair_recursive_lock_lock_with_options
CStrings:
+ "OSKEXT_BUILD_DATE 01:01:31 Nov 10 2026"
- "OSKEXT_BUILD_DATE 23:19:39 Oct 22 2026"
```
