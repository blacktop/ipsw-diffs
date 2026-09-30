## VDC

> `/System/Library/Frameworks/CoreMediaIO.framework/Versions/A/Resources/VDC.plugin/Contents/MacOS/VDC`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`

```diff

-520.0.0.0.0
-  __TEXT.__text: 0x354d8
+520.21.1.0.0
+  __TEXT.__text: 0x35460
   __TEXT.__auth_stubs: 0xe30
-  __TEXT.__gcc_except_tab: 0x2d3c
+  __TEXT.__gcc_except_tab: 0x2d20
   __TEXT.__const: 0x818
   __TEXT.__oslogstring: 0x5f6c
   __TEXT.__cstring: 0x305d
-  __TEXT.__unwind_info: 0x1370
+  __TEXT.__unwind_info: 0x1378
   __DATA_CONST.__const: 0x2210
   __DATA_CONST.__cfstring: 0x920
   __DATA_CONST.__auth_got: 0x720

   - /System/Library/Frameworks/IOSurface.framework/Versions/A/IOSurface
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 1399
+  Functions: 1400
   Symbols:   1120
   CStrings:  596
 
Functions:
~ __ZN4CMIO2DP3VDC6PlugIn18UpdateDevicesStateEv : 1380 -> 988
+ sub_27448
```
