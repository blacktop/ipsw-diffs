## DeviceRecovery

> `/System/Library/PrivateFrameworks/DeviceRecovery.framework/DeviceRecovery`

```diff

-150.40.7.0.0
-  __TEXT.__text: 0x101ec
-  __TEXT.__objc_methlist: 0x768
+150.40.9.0.0
+  __TEXT.__text: 0x10908
+  __TEXT.__objc_methlist: 0x7c0
   __TEXT.__const: 0xe2
   __TEXT.__gcc_except_tab: 0x1c0
-  __TEXT.__cstring: 0x2779
-  __TEXT.__oslogstring: 0x1145
+  __TEXT.__cstring: 0x2889
+  __TEXT.__oslogstring: 0x11e7
   __TEXT.__constg_swiftt: 0x78
   __TEXT.__swift5_typeref: 0x38
   __TEXT.__swift5_reflstr: 0x20
   __TEXT.__swift5_fieldmd: 0x34
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x6b8
+  __TEXT.__unwind_info: 0x6e0
   __TEXT.__eh_frame: 0xd8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x520
+  __DATA_CONST.__const: 0x528
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x538
+  __DATA_CONST.__objc_selrefs: 0x560
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__got: 0xd8
   __AUTH_CONST.__const: 0x1c0
-  __AUTH_CONST.__cfstring: 0xf40
-  __AUTH_CONST.__objc_const: 0x8e8
+  __AUTH_CONST.__cfstring: 0xf80
+  __AUTH_CONST.__objc_const: 0x928
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__auth_got: 0x3d0
-  __DATA.__objc_ivar: 0x60
+  __DATA.__objc_ivar: 0x64
   __DATA.__data: 0x28
   __DATA_DIRTY.__objc_data: 0x1f0
   __DATA_DIRTY.__data: 0x1b8

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  Functions: 525
-  Symbols:   544
-  CStrings:  313
+  Functions: 539
+  Symbols:   553
+  CStrings:  322
 
Symbols:
+ -[DeviceRecoveryController addEraseAndUpdateRestrictionForClient:completion:]
+ -[DeviceRecoveryController eraseAndUpdateRestricted]
+ -[DeviceRecoveryController removeEraseAndUpdateRestrictionForClient:completion:]
+ -[DeviceRecoveryController setEraseAndUpdateRestricted:]
+ -[DeviceRecoveryController setEraseAndUpdateRestriction:forClient:completion:]
+ _DRServiceAttributeEraseAndUpdateRestricted
+ _OBJC_IVAR_$_DeviceRecoveryController._eraseAndUpdateRestricted
+ _OUTLINED_FUNCTION_33
+ ___78-[DeviceRecoveryController setEraseAndUpdateRestriction:forClient:completion:]_block_invoke
CStrings:
+ "%{public}s: Could not update EACS / Software Update restriction: %{public}@"
+ "%{public}s: Framework: %{public}s EACS / Software Update restriction for '%{public}@'"
+ "-[DeviceRecoveryController setEraseAndUpdateRestriction:forClient:completion:]"
+ "-[DeviceRecoveryController setEraseAndUpdateRestriction:forClient:completion:]_block_invoke"
+ "EraseAndUpdateRestricted"
+ "adding"
+ "clientIdentifier.length > 0"
+ "no client identifier provided"
+ "removing"
```
