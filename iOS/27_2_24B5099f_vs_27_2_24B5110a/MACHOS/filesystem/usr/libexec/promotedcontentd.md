## promotedcontentd

> `/usr/libexec/promotedcontentd`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-557.2.13.0.0
-  __TEXT.__text: 0x3cb7d8
+557.2.14.0.0
+  __TEXT.__text: 0x3cbdbc
   __TEXT.__auth_stubs: 0x5db0
-  __TEXT.__objc_stubs: 0x1a220
-  __TEXT.__objc_methlist: 0x151f8
+  __TEXT.__objc_stubs: 0x1a320
+  __TEXT.__objc_methlist: 0x15258
   __TEXT.__const: 0x2b4ba
-  __TEXT.__gcc_except_tab: 0x1348
-  __TEXT.__cstring: 0x15d35
-  __TEXT.__objc_methname: 0x2711d
-  __TEXT.__oslogstring: 0x113ac
+  __TEXT.__gcc_except_tab: 0x1370
+  __TEXT.__cstring: 0x15d55
+  __TEXT.__objc_methname: 0x2721d
+  __TEXT.__oslogstring: 0x1153c
   __TEXT.__objc_classname: 0x4db7
   __TEXT.__objc_methtype: 0x518d
   __TEXT.__constg_swiftt: 0x65d0

   __TEXT.__swift_as_ret: 0x104
   __TEXT.__swift_as_cont: 0x254
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x86f0
+  __TEXT.__unwind_info: 0x8700
   __TEXT.__eh_frame: 0x4874
   __DATA_CONST.__const: 0x1c3b8
-  __DATA_CONST.__cfstring: 0xf800
+  __DATA_CONST.__cfstring: 0xf840
   __DATA_CONST.__objc_classlist: 0x1018
   __DATA_CONST.__objc_catlist: 0xb8
   __DATA_CONST.__objc_protolist: 0x300

   __DATA_CONST.__auth_got: 0x2ee8
   __DATA_CONST.__got: 0x18e8
   __DATA_CONST.__auth_ptr: 0x1610
-  __DATA.__objc_const: 0x2b7e0
-  __DATA.__objc_selrefs: 0x9490
-  __DATA.__objc_ivar: 0x1458
+  __DATA.__objc_const: 0x2b840
+  __DATA.__objc_selrefs: 0x94d0
+  __DATA.__objc_ivar: 0x1460
   __DATA.__objc_data: 0x9908
   __DATA.__data: 0xe998
   __DATA.__common: 0xd70

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 11756
+  Functions: 11764
   Symbols:   2300
-  CStrings:  11682
+  CStrings:  11697
 
CStrings:
+ "Content for context %{public}@ with ID %{public}@ appeared on screen with no status to report."
+ "OnScreen metric with content identifier %{public}@ is collapsed while ready, but it did not finish loading while its slot was on screen. Not reporting AdLoadedTooLate. displayed: %{public}@"
+ "TB,V_becameReadyWhileOnScreen"
+ "TB,V_isOnScreen"
+ "_becameReadyWhileOnScreen"
+ "_isOnScreen"
+ "appearedOnScreen"
+ "becameReadyWhileOnScreen"
+ "b\xc1"
+ "hasBeenDisplayed"
+ "interfaceOffScreen"
+ "interfaceOnScreen"
+ "isOnScreen"
+ "setBecameReadyWhileOnScreen:"
+ "setIsOnScreen:"
+ "shouldSendAdSpaceStatusEvent: NOT sending ASE %{public}@ for content %{public}@ because the ad has already been displayed."
- "R\xc1"
```
