## com.apple.driver.AppleFirmwareKit

> `com.apple.driver.AppleFirmwareKit`

### Sections with Same Size but Changed Content

- `__DATA.__data`
- `__DATA_CONST.__mod_init_func`
- `__DATA_CONST.__mod_term_func`
- `__DATA_CONST.__const`
- `__DATA_CONST.__kalloc_type`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`

```diff

-743.0.2.0.0
+743.0.4.0.0
   __TEXT.__const: 0x288
   __TEXT.__cstring: 0x48d8
   __TEXT.__os_log: 0x148a
-  __TEXT_EXEC.__text: 0x42500
+  __TEXT_EXEC.__text: 0x4253c
   __TEXT_EXEC.__auth_stubs: 0x980
   __DATA.__data: 0x508
   __DATA.__common: 0x728

   __DATA_CONST.__auth_got: 0x4c0
   __DATA_CONST.__got: 0x148
   __DATA_CONST.__auth_ptr: 0x8
-  Functions: 2186
-  Symbols:   3052
+  Functions: 2185
+  Symbols:   3051
   CStrings:  760
 
Symbols:
- _ZN27AFKEPInterfaceEventSourceV217stateCompleteImplEv
Functions:
~ __ZN27AFKEPInterfaceEventSourceV26doTaskEv : 704 -> 720
~ __ZN27AFKEPInterfaceEventSourceV213stateCompleteEv : 56 -> 100
~ __ZN27AFKEPInterfaceEventSourceV217stateCompleteImplEv : 64 -> 40
~ __ZN27AFKEPInterfaceEventSourceV28clearAllEv : 372 -> 420
- _ZN27AFKEPInterfaceEventSourceV24freeEv.cold.1
```
