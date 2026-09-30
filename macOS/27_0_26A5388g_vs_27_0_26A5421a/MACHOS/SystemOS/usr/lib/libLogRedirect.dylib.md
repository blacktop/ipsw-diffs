## libLogRedirect.dylib

> `/usr/lib/libLogRedirect.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__AUTH_CONST.__interpose`

```diff

-64578.53.2.0.0
-  __TEXT.__text: 0x24b0
+64578.57.1.0.0
+  __TEXT.__text: 0x24cc
   __TEXT.__auth_stubs: 0x290
   __TEXT.__init_offsets: 0x4
   __TEXT.__const: 0x60
-  __TEXT.__cstring: 0x4b9
+  __TEXT.__cstring: 0x4ed
   __TEXT.__oslogstring: 0x19
   __TEXT.__unwind_info: 0xc8
   __DATA_CONST.__const: 0x60

   - /usr/lib/libSystem.B.dylib
   Functions: 25
   Symbols:   99
-  CStrings:  65
+  CStrings:  66
 
Functions:
~ _LogPredicate_Evaluate : 640 -> 668
CStrings:
+ "/System/Library/Frameworks/CoreFoundation.framework"
```
