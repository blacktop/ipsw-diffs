## PS

> `/System/Library/Spotlight/PS.mdimporter/Contents/MacOS/PS`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__cfstring`

```diff

-236.0.0.0.0
-  __TEXT.__text: 0x9bc
+236.1.0.0.0
+  __TEXT.__text: 0x944
   __TEXT.__auth_stubs: 0x160
   __TEXT.__cstring: 0x63
   __TEXT.__unwind_info: 0x78

   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices
   - /usr/lib/libSystem.B.dylib
-  Functions: 14
-  Symbols:   47
+  Functions: 15
+  Symbols:   48
   CStrings:  7
 
Symbols:
+ _OUTLINED_FUNCTION_6
Functions:
~ _OUTLINED_FUNCTION_0 : 32 -> 28
~ _OUTLINED_FUNCTION_1 : 24 -> 12
~ _OUTLINED_FUNCTION_2 : 24 -> 12
~ _OUTLINED_FUNCTION_3 : 28 -> 12
+ _OUTLINED_FUNCTION_6
~ _GetMetadataForFile : 1528 -> 1420
```
