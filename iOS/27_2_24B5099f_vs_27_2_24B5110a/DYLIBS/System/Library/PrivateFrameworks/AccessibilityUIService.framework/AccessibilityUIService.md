## AccessibilityUIService

> `/System/Library/PrivateFrameworks/AccessibilityUIService.framework/AccessibilityUIService`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`

```diff

-3245.8.4.2.0
-  __TEXT.__text: 0x1f380
-  __TEXT.__objc_methlist: 0x1c64
+3245.8.9.0.0
+  __TEXT.__text: 0x1f9d8
+  __TEXT.__objc_methlist: 0x1cac
   __TEXT.__const: 0x880
   __TEXT.__constg_swiftt: 0x184
   __TEXT.__swift5_typeref: 0x1d7

   __TEXT.__cstring: 0x1561
   __TEXT.__swift5_types: 0x24
   __TEXT.__swift5_capture: 0x44
-  __TEXT.__oslogstring: 0x1a70
+  __TEXT.__oslogstring: 0x1ca5
   __TEXT.__swift5_reflstr: 0xb5
   __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_proto: 0x48
   __TEXT.__swift_as_entry: 0x10
   __TEXT.__swift_as_ret: 0x10
   __TEXT.__swift_as_cont: 0x20
-  __TEXT.__gcc_except_tab: 0x4bc
-  __TEXT.__unwind_info: 0xa10
+  __TEXT.__gcc_except_tab: 0x4d0
+  __TEXT.__unwind_info: 0xa20
   __TEXT.__eh_frame: 0x408
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_classlist: 0xd0
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x18d8
+  __DATA_CONST.__objc_selrefs: 0x1908
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x78
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__got: 0x518
   __AUTH_CONST.__const: 0x4b0
   __AUTH_CONST.__cfstring: 0xaa0
-  __AUTH_CONST.__objc_const: 0x2880
+  __AUTH_CONST.__objc_const: 0x28e0
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__auth_got: 0x890
   __AUTH.__objc_data: 0x260
   __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0x19c
+  __DATA.__objc_ivar: 0x1a4
   __DATA.__data: 0x690
   __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0x640

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 749
-  Symbols:   1489
-  CStrings:  228
+  Functions: 756
+  Symbols:   1499
+  CStrings:  233
 
Symbols:
+ -[AXUIDisplayManager _beginPendingSceneRequestForSceneClientIdentifier:]
+ -[AXUIDisplayManager _clearPendingSceneRequestForSceneClientIdentifier:]
+ -[AXUIDisplayManager pendingSceneRequestIdentifiers]
+ -[AXUIDisplayManager pendingSceneRequestTimers]
+ -[AXUIDisplayManager setPendingSceneRequestIdentifiers:]
+ -[AXUIDisplayManager setPendingSceneRequestTimers:]
+ GCC_except_table332
+ GCC_except_table333
+ GCC_except_table342
+ GCC_except_table343
+ GCC_except_table361
+ GCC_except_table362
+ GCC_except_table369
+ GCC_except_table377
+ GCC_except_table382
+ GCC_except_table398
+ GCC_except_table412
+ GCC_except_table433
+ GCC_except_table435
+ GCC_except_table452
+ _OBJC_IVAR_$_AXUIDisplayManager._pendingSceneRequestIdentifiers
+ _OBJC_IVAR_$_AXUIDisplayManager._pendingSceneRequestTimers
+ ___72-[AXUIDisplayManager _beginPendingSceneRequestForSceneClientIdentifier:]_block_invoke
- GCC_except_table328
- GCC_except_table329
- GCC_except_table338
- GCC_except_table339
- GCC_except_table357
- GCC_except_table358
- GCC_except_table365
- GCC_except_table373
- GCC_except_table378
- GCC_except_table394
- GCC_except_table426
- GCC_except_table428
- GCC_except_table445
CStrings:
+ "AXOverlayMonitor[Window]: attached %{public}@ scene=%{public}@ level=%f siblings=%lu"
+ "Active window scene for '%{public}@' changed from %{public}@ to %{public}@; migrating tracked content VCs"
+ "Adding contentVC=%p %@ service=%@ sceneClientIdentifier:%{public}@ windowScene=%{public}@, savedWindowScene=%{public}@"
+ "DisplayManager: Adding scene pending sceneClientIdentifier: %@"
+ "DisplayManager: No existing scene for identifier %@, requesting scene creation for service %@ at level %f"
+ "DisplayManager: Notifying newly registered service %@ about existing scene %@"
+ "DisplayManager: Removing scene pending sceneClientIdentifier: %@"
+ "DisplayManager: Scene creation already requested for identifier %@, skip requesting for service %@"
+ "DisplayManager: Scene creation request for identifier %@ never produced a scene, clearing request"
+ "Scene connected for Service: %@. windowScene: %{public}@ sceneClientIdentifier: %{public}@"
+ "Scene disconnected for Service: %@. windowScene: %{public}@ sceneClientIdentifier: %{public}@"
- "Active window scene for '%{public}@' changed from %p to %p; migrating tracked content VCs"
- "Adding contentVC=%p %@ service=%@ sceneClientIdentifier:%@ windowScene=%p, savedWindowScene=%p"
- "No existing scenes for identifier %@, requesting scene creation for service %@ at level %f"
- "Notifying newly registered service %@ about existing scene %@"
- "Scene connected for Service: %@. windowScene: %@"
- "Scene disconnected for Service: %@. windowScene: %@"
```
