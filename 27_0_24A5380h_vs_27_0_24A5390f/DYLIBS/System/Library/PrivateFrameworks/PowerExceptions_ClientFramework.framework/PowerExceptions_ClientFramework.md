## PowerExceptions_ClientFramework

> `/System/Library/PrivateFrameworks/PowerExceptions_ClientFramework.framework/PowerExceptions_ClientFramework`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-174.0.0.0.0
-  __TEXT.__text: 0x10850
-  __TEXT.__objc_methlist: 0xd58
+177.0.8.502.1
+  __TEXT.__text: 0x11424
+  __TEXT.__objc_methlist: 0xdb8
   __TEXT.__const: 0xe0
-  __TEXT.__gcc_except_tab: 0x5d0
+  __TEXT.__gcc_except_tab: 0x618
   __TEXT.__cstring: 0x4a1
-  __TEXT.__oslogstring: 0x16d5
-  __TEXT.__unwind_info: 0x6b0
+  __TEXT.__oslogstring: 0x176c
+  __TEXT.__unwind_info: 0x700
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8b0
+  __DATA_CONST.__objc_selrefs: 0x8f0
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x28
   __DATA_CONST.__got: 0xb8
   __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__cfstring: 0x280
-  __AUTH_CONST.__objc_const: 0xf88
+  __AUTH_CONST.__objc_const: 0xfa8
   __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x90
   __DATA.__data: 0x2a0

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 425
-  Symbols:   773
-  CStrings:  186
+  Functions: 441
+  Symbols:   789
+  CStrings:  190
 
Symbols:
+ -[ComputeSafeguardsManagingClient addBoostWatchForPid:name:reason:error:]
+ -[ComputeSafeguardsManagingClient getBoostObservationsForPid:error:]
+ -[ComputeSafeguardsManagingClient removeBoostWatchForPid:reason:error:]
+ -[ComputeSafeguardsManagingClient resetBoostCountersForPid:error:]
+ GCC_except_table204
+ GCC_except_table207
+ GCC_except_table210
+ GCC_except_table213
+ ___66-[ComputeSafeguardsManagingClient resetBoostCountersForPid:error:]_block_invoke
+ ___68-[ComputeSafeguardsManagingClient getBoostObservationsForPid:error:]_block_invoke
+ ___71-[ComputeSafeguardsManagingClient removeBoostWatchForPid:reason:error:]_block_invoke
+ ___73-[ComputeSafeguardsManagingClient addBoostWatchForPid:name:reason:error:]_block_invoke
+ _objc_msgSend$addBoostWatchForPid:name:reason:reply:
+ _objc_msgSend$getBoostObservationsForPid:reply:
+ _objc_msgSend$removeBoostWatchForPid:reason:reply:
+ _objc_msgSend$resetBoostCountersForPid:reply:
CStrings:
+ "addBoostWatchForPid: XPC error %@"
+ "getBoostObservationsForPid: XPC error %@"
+ "removeBoostWatchForPid: XPC error %@"
+ "resetBoostCountersForPid: XPC error %@"
```
