## AppleGameControllerPersonality_development

> `/System/Library/Extensions/AppleGameControllerPersonality.kext/AppleGameControllerPersonality_development`

### Sections with Same Size but Changed Content

- `__DATA.__data`
- `__DATA_CONST.__const`

```diff

-14.0.19.0.0
-  __TEXT.__cstring: 0x235
-  __TEXT.__os_log: 0x27e
-  __TEXT_EXEC.__text: 0x1edc
+14.0.21.0.0
+  __TEXT.__cstring: 0x24b
+  __TEXT.__os_log: 0x2e3
+  __TEXT_EXEC.__text: 0x1f44
   __TEXT_EXEC.__auth_stubs: 0x140
   __DATA.__data: 0xc8
   __DATA.__common: 0x88

   __DATA_CONST.__auth_got: 0xa0
   __DATA_CONST.__got: 0x70
   Functions: 60
-  Symbols:   369
-  CStrings:  33
+  Symbols:   370
+  CStrings:  35
 
Symbols:
+ __ZZN37AppleGCIOHIDEventDriverPropertyMerger5probeEP9IOServicePiE11_os_log_fmt_4
Functions:
~ _OUTLINED_FUNCTION_3 : 16 -> 12
~ __ZN37AppleGCIOHIDEventDriverPropertyMerger5probeEP9IOServicePi : 2064 -> 2172
CStrings:
+ "AppleGCHIDUserEventDriver not matching on <IOHIDDevice %#010llx> with missing GameControllerPointer."
+ "GameControllerPointer"
```
