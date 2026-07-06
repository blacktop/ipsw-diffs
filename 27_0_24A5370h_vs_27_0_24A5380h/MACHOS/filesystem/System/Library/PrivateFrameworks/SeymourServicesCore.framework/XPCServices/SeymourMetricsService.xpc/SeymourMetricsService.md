## SeymourMetricsService

> `/System/Library/PrivateFrameworks/SeymourServicesCore.framework/XPCServices/SeymourMetricsService.xpc/SeymourMetricsService`

```diff

-  __TEXT.__text: 0x1934
+  __TEXT.__text: 0x1930
   __TEXT.__auth_stubs: 0x430
   __TEXT.__const: 0x2a
   __TEXT.__cstring: 0x1a
-  __TEXT.__oslogstring: 0xc3
+  __TEXT.__oslogstring: 0xd3
   __TEXT.__swift5_typeref: 0x39
   __TEXT.__swift5_entry: 0x8
   __TEXT.__swift5_capture: 0x20

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 20
-  Symbols:   51
+  Symbols:   50
   CStrings:  5
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
Symbols:
- _os_proc_available_memory
Functions:
~ sub_100001020 : 1468 -> 1464
CStrings:
+ "[%{public}s] %{public}s begin footprint=%{public}fKB"
- "[%{public}s] %{public}s begin mem=%{public}fKB"

```
