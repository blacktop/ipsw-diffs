## com.apple.DriverKit-AppleBCMWLAN

> `/System/Library/DriverExtensions/com.apple.DriverKit-AppleBCMWLAN.dext/com.apple.DriverKit-AppleBCMWLAN`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__cstring`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA.__data`

```diff

-1582.4.0.0.0
-  __TEXT.__text: 0x28b79c
+1582.5.0.0.0
+  __TEXT.__text: 0x28b7e8
   __TEXT.__auth_stubs: 0x25c0
   __TEXT.__init_offsets: 0x1bc
   __TEXT.__cstring: 0x83602
   __TEXT.__const: 0x7f168
   __TEXT.__oslogstring: 0x1f27
-  __TEXT.__unwind_info: 0xa480
+  __TEXT.__unwind_info: 0xa488
   __TEXT.__eh_frame: 0x38
   __DATA_CONST.__const: 0x211a8
   __DATA_CONST.__osclassinfo: 0x388

   - /System/DriverKit/System/Library/PrivateFrameworks/IOFileValidation.framework/IOFileValidation
   - /System/DriverKit/System/Library/PrivateFrameworks/OLYHALDriverKit.framework/OLYHALDriverKit
   - /System/DriverKit/usr/lib/libc++.dylib
-  Functions: 14196
-  Symbols:   12068
+  Functions: 14198
+  Symbols:   12070
   CStrings:  13147
 
Symbols:
+ __ZN24AppleBCMWLANNANInterface15flushFlowQueuesEP10ether_addr
+ __ZThn96_N24AppleBCMWLANNANInterface15flushFlowQueuesEP10ether_addr
CStrings:
+ "\"AppleBCMWLANV3_driverkit-1582.5\""
+ "AppleBCMWLANV3_driverkit-1582.5"
- "\"AppleBCMWLANV3_driverkit-1582.4\""
- "AppleBCMWLANV3_driverkit-1582.4"
```
