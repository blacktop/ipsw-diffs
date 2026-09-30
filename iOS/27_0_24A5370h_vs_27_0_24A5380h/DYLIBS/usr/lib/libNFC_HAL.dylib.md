## libNFC_HAL.dylib

> `/usr/lib/libNFC_HAL.dylib`

```diff

-  __TEXT.__text: 0x180cc
-  __TEXT.__const: 0x120
-  __TEXT.__cstring: 0x2e33
-  __TEXT.__oslogstring: 0x2578
-  __TEXT.__unwind_info: 0x238
+  __TEXT.__text: 0x17ed8
+  __TEXT.__const: 0xf0
+  __TEXT.__cstring: 0x2dc6
+  __TEXT.__oslogstring: 0x24fc
+  __TEXT.__unwind_info: 0x248
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x268
   __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x100
   __AUTH_CONST.__cfstring: 0x360
   __AUTH_CONST.__auth_got: 0x0
-  __DATA_DIRTY.__data: 0x2
-  __DATA_DIRTY.__bss: 0x248
+  __DATA.__bss: 0x18
+  __DATA_DIRTY.__data: 0x10
+  __DATA_DIRTY.__bss: 0x230
   __DATA_DIRTY.__common: 0x28
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libnfshared.dylib
   Functions: 178
   Symbols:   273
-  CStrings:  676
+  CStrings:  671
 
Sections:
~ __DATA_CONST.__const : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
CStrings:
+ "Error : read received after shutdown : %p / %p. Driver context 0x%016llX"
- "%s:%i Read aborted while in progress since %llu."
- "%s:%i Socket is non-blocking"
- "%{public}s:%i Read aborted while in progress since %llu."
- "%{public}s:%i Socket is non-blocking"
- "Error : read received after shutdown : %p / %p. Driver controller type 0x%x, Controller config type %d"
- "NFHardwareSerialReadBlockAbort"

```
